#!/usr/bin/env python3
"""Audit v2 asset manifests; this command never manufactures a passing status."""

from __future__ import annotations

import argparse
import json

from chart_registry_lib import ROOT, asset_records, load_registry
from manifest_lib import find_asset_manifests, load_manifest, validate_manifest


def audit_manifests() -> list[str]:
    registry = load_registry()
    errors: list[str] = []
    expected = {(ROOT / chart["asset_path"] / "asset.yaml").resolve(): chart for chart in asset_records(registry)}
    actual = {path.resolve() for path in find_asset_manifests()}
    for path in sorted(set(expected) - actual):
        errors.append(f"registry asset has no manifest: {path.relative_to(ROOT)}")
    chart_ids = {chart["id"] for chart in registry["charts"]}
    for path in sorted(actual - set(expected)):
        manifest = load_manifest(path)
        successor = manifest.get("provenance", {}).get("canonical_successor")
        is_retained_legacy = (
            manifest.get("asset_status") == "legacy_example"
            and str(manifest.get("asset_id", "")).startswith("legacy-")
            and successor in chart_ids
        )
        if not is_retained_legacy:
            errors.append(f"manifest is not registered: {path.relative_to(ROOT)}")
        errors.extend(f"{path.parent.relative_to(ROOT)}: {error}" for error in validate_manifest(manifest, path.parent))
    for path in sorted(actual & set(expected)):
        manifest = load_manifest(path)
        chart = expected[path]
        if chart["id"] not in manifest.get("chart_ids", []):
            errors.append(f"{chart['id']}: manifest does not list the canonical chart ID")
        expected_status = chart["implementation_status"]
        if expected_status in {"legacy_example", "demo_runnable", "production_verified", "deprecated"} and manifest.get("asset_status") != expected_status:
            errors.append(f"{chart['id']}: registry status {expected_status} differs from manifest {manifest.get('asset_status')}")
        errors.extend(f"{path.parent.relative_to(ROOT)}: {error}" for error in validate_manifest(manifest, path.parent))
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Accepted for compatibility; audits are always read-only")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    errors = audit_manifests()
    payload = {"manifest_version": "2.0.0", "errors": errors, "valid": not errors}
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"Manifest v2 audit: {'PASS' if not errors else 'FAIL'}")
        for error in errors:
            print(f"  - {error}")
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
