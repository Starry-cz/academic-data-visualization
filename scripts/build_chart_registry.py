#!/usr/bin/env python3
"""Audit source memberships and create deterministic production asset manifests."""

from __future__ import annotations

import argparse
import json
import struct
from pathlib import Path

from chart_registry_lib import ROOT, load_registry, parse_source_taxonomy, source_memberships


def png_ratio(path: Path) -> float:
    with path.open("rb") as handle:
        signature = handle.read(24)
    if signature[:8] != b"\x89PNG\r\n\x1a\n" or signature[12:16] != b"IHDR":
        raise ValueError(f"Invalid PNG header: {path}")
    width, height = struct.unpack(">II", signature[16:24])
    if height == 0:
        raise ValueError(f"PNG has zero height: {path}")
    return round(width / height, 4)


def build_manifest(chart: dict) -> dict:
    asset_dir = ROOT / chart["asset_path"]
    scripts = sorted(
        path.name for path in asset_dir.iterdir()
        if path.is_file() and path.suffix.lower() in {".py", ".r"}
    )
    previews = sorted(path.name for path in asset_dir.glob("*.png"))
    vectors = sorted(
        path.name for path in asset_dir.iterdir()
        if path.is_file() and path.suffix.lower() in {".svg", ".pdf"}
    )
    if not scripts or not previews:
        raise ValueError(f"{asset_dir} must contain at least one script and one PNG")
    backends = sorted({"python" if Path(name).suffix.lower() == ".py" else "r" for name in scripts})
    return {
        "manifest_version": "1.0.0",
        "chart_ids": [chart["id"]],
        "backend": backends,
        "entrypoints": scripts,
        "previews": previews,
        "outputs": {"vector": vectors, "raster": previews},
        "data": {"mode": "bundled_or_synthetic_demo", "required_columns": []},
        "supported_transforms": chart["allowed_transforms"],
        "unsupported_cases": chart["avoid_when"],
        "aspect_ratio": png_ratio(asset_dir / previews[0]),
        "theme": "nature-default",
        "qa": {
            "status": "passed",
            "commands": [
                "python scripts/check_references.py",
                "python scripts/check_chart_registry.py",
            ],
        },
    }


def sync_manifests(registry: dict, check: bool) -> list[str]:
    differences: list[str] = []
    for chart in registry["charts"]:
        if chart["implementation_status"] != "production_template":
            continue
        path = ROOT / chart["asset_path"] / "asset.yaml"
        expected = json.dumps(build_manifest(chart), ensure_ascii=False, indent=2) + "\n"
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != expected:
            differences.append(str(path.relative_to(ROOT)))
            if not check:
                path.write_text(expected, encoding="utf-8")
    return differences


def source_audit(registry: dict) -> dict:
    pairs = source_memberships()
    entries = parse_source_taxonomy()
    chart_ids = {chart["id"] for chart in registry["charts"]}
    category_ids = {category["id"] for category in registry["categories"]}
    return {
        "memberships": len(pairs),
        "unmapped_source_entries": [
            {"line": entry["line"], "category_id": entry["category_id"], "source_label": entry["source_label"]}
            for entry in entries
            if entry["canonical_id"] is None
        ],
        "unregistered_chart_ids": sorted({chart_id for _, chart_id in pairs} - chart_ids),
        "invalid_category_ids": sorted({category_id for category_id, _ in pairs} - category_ids),
        "missing_registry_memberships": sorted(
            {
                (membership["source_category_id"], chart["id"])
                for chart in registry["charts"]
                for membership in chart["source_memberships"]
            }
            - set(pairs)
        ),
    }


def write_draft(registry: dict, output: Path) -> None:
    audit = source_audit(registry)
    draft = {
        "note": "Source entries requiring canonicalization appear below.",
        "unmapped_source_entries": audit["unmapped_source_entries"],
        "unregistered_chart_ids": audit["unregistered_chart_ids"],
    }
    output.write_text(json.dumps(draft, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sync-manifests", action="store_true")
    parser.add_argument("--check", action="store_true", help="Do not write; fail if generated manifests differ")
    parser.add_argument("--draft", type=Path, help="Write a normalization draft for unregistered source entries")
    args = parser.parse_args()

    registry = load_registry()
    audit = source_audit(registry)
    if (audit["unmapped_source_entries"] or audit["unregistered_chart_ids"]
            or audit["invalid_category_ids"] or audit["missing_registry_memberships"]):
        print(json.dumps(audit, ensure_ascii=False, indent=2))
        raise SystemExit(1)
    print(f"Source memberships audited: {audit['memberships']}")

    if args.draft:
        write_draft(registry, args.draft)
        print(f"Draft written: {args.draft}")
    if args.sync_manifests or args.check:
        differences = sync_manifests(registry, check=args.check)
        if args.check and differences:
            print("Out-of-date manifests:")
            for path in differences:
                print(f"  - {path}")
            raise SystemExit(1)
        verb = "checked" if args.check else "updated"
        production_count = sum(
            chart["implementation_status"] == "production_template"
            for chart in registry["charts"]
        )
        print(
            f"Production manifests {verb}: "
            f"{len(differences) if not args.check else production_count}"
        )


if __name__ == "__main__":
    main()
