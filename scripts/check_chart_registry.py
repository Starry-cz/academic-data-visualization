#!/usr/bin/env python3
"""Validate chart taxonomy, aliases, source memberships, and production assets."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

from chart_registry_lib import (
    FIGURES_DIR,
    ROOT,
    load_registry,
    load_schema,
    normalize_alias,
    parse_source_taxonomy,
    production_records,
    source_memberships,
    status_counts,
    validate_schema,
)


def validate_registry() -> list[str]:
    registry = load_registry()
    schema = load_schema()
    errors = validate_schema(registry, schema, schema)
    categories = registry["categories"]
    charts = registry["charts"]
    category_ids = [category["id"] for category in categories]
    chart_ids = [chart["id"] for chart in charts]

    if category_ids != [f"{index:02d}" for index in range(1, 25)]:
        errors.append("$.categories: IDs must be exactly 01 through 24 in order")
    for label, values in [("category id", category_ids), ("category slug", [c["slug"] for c in categories]),
                          ("chart id", chart_ids)]:
        duplicates = sorted(value for value, count in Counter(values).items() if count > 1)
        if duplicates:
            errors.append(f"duplicate {label}: {duplicates}")

    category_set = set(category_ids)
    chart_set = set(chart_ids)
    alias_owners: dict[str, set[str]] = defaultdict(set)
    for chart in charts:
        if chart["primary_category_id"] not in chart["category_ids"]:
            errors.append(f"{chart['id']}: primary category is not in category_ids")
        invalid_categories = set(chart["category_ids"]) - category_set
        if invalid_categories:
            errors.append(f"{chart['id']}: invalid categories {sorted(invalid_categories)}")
        for membership in chart["source_memberships"]:
            if membership["source_category_id"] not in chart["category_ids"]:
                errors.append(f"{chart['id']}: source membership is outside category_ids")
        for related_field in ("alternatives", "complements", "components"):
            unknown = set(chart[related_field]) - chart_set
            if unknown:
                errors.append(f"{chart['id']}: unknown {related_field} {sorted(unknown)}")
        for alias in [chart["name_zh"], chart["name_en"], *chart["aliases_zh"], *chart["aliases_en"]]:
            alias_owners[normalize_alias(alias)].add(chart["id"])

        if chart["implementation_status"] == "production_template":
            if not chart["asset_path"]:
                errors.append(f"{chart['id']}: production template has no asset_path")
                continue
            if not chart["backends"]:
                errors.append(f"{chart['id']}: production template must declare its real backend")
            asset_dir = ROOT / chart["asset_path"]
            if not asset_dir.is_dir():
                errors.append(f"{chart['id']}: asset directory does not exist: {chart['asset_path']}")
                continue
            scripts = [*asset_dir.glob("*.py"), *asset_dir.glob("*.R"), *asset_dir.glob("*.r")]
            previews = list(asset_dir.glob("*.png"))
            manifest_path = asset_dir / "asset.yaml"
            if not scripts or not previews or not manifest_path.is_file():
                errors.append(f"{chart['id']}: production asset requires script, PNG, and asset.yaml")
                continue
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            required_manifest_fields = {
                "manifest_version", "chart_ids", "backend", "entrypoints", "previews",
                "outputs", "data", "supported_transforms", "unsupported_cases",
                "aspect_ratio", "theme", "qa",
            }
            missing_manifest_fields = required_manifest_fields - manifest.keys()
            if missing_manifest_fields:
                errors.append(
                    f"{chart['id']}: manifest missing fields {sorted(missing_manifest_fields)}"
                )
            if chart["id"] not in manifest.get("chart_ids", []):
                errors.append(f"{chart['id']}: manifest does not list the canonical ID")
            for field in ("entrypoints", "previews"):
                for name in manifest.get(field, []):
                    if not (asset_dir / name).is_file():
                        errors.append(f"{chart['id']}: manifest {field} path missing: {name}")
        elif chart["asset_path"] is not None:
            errors.append(f"{chart['id']}: non-production record must not declare asset_path")

    resolved_terms = {normalize_alias(term["term"]) for term in registry["ambiguous_terms"]}
    for alias, owners in alias_owners.items():
        if len(owners) > 1 and alias not in resolved_terms:
            errors.append(f"unresolved alias collision {alias!r}: {sorted(owners)}")
    for term in registry["ambiguous_terms"]:
        unknown = set(term["candidate_ids"]) - chart_set
        if unknown:
            errors.append(f"ambiguous term {term['term']!r} has unknown candidates {sorted(unknown)}")

    entries = parse_source_taxonomy()
    unmapped = [entry for entry in entries if entry["canonical_id"] is None]
    if unmapped:
        errors.append(
            "source taxonomy contains unmapped entries: "
            + ", ".join(f"line {entry['line']} ({entry['source_label']})" for entry in unmapped[:10])
        )
    pairs = source_memberships()
    registry_pairs = {
        (membership["source_category_id"], chart["id"])
        for chart in charts
        for membership in chart["source_memberships"]
    }
    if set(pairs) != registry_pairs:
        errors.append("source taxonomy memberships differ from registry source_memberships")
    if len(pairs) != registry["source_expectation"]["available_source_memberships"]:
        errors.append("source_expectation.available_source_memberships is stale")

    production_paths = {ROOT / chart["asset_path"] for chart in production_records(registry)}
    asset_dirs = {
        path for path in FIGURES_DIR.iterdir()
        if path.is_dir() and any([*path.glob("*.py"), *path.glob("*.R"), *path.glob("*.r")])
    }
    missing_registry = sorted(str(path.relative_to(ROOT)) for path in asset_dirs - production_paths)
    orphan_registry = sorted(str(path.relative_to(ROOT)) for path in production_paths - asset_dirs)
    if missing_registry:
        errors.append(f"production asset directories missing from registry: {missing_registry}")
    if orphan_registry:
        errors.append(f"registry production paths without assets: {orphan_registry}")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    errors = validate_registry()
    registry = load_registry()
    result = {
        "categories": len(registry["categories"]),
        "canonical_charts": len(registry["charts"]),
        "source_memberships": registry["source_expectation"]["available_source_memberships"],
        "source_complete": registry["source_expectation"]["source_complete"],
        "status_counts": status_counts(registry),
        "errors": errors,
        "valid": not errors,
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("=" * 64)
        print("Chart Registry Validation")
        print(f"  Categories          : {result['categories']}/24")
        print(f"  Canonical charts    : {result['canonical_charts']}")
        print(f"  Source memberships  : {result['source_memberships']}")
        print(f"  Production templates: {result['status_counts']['production_template']}")
        print(f"  Reusable patterns   : {result['status_counts']['reusable_pattern']}")
        print(f"  On-demand routes    : {result['status_counts']['on_demand']}")
        if errors:
            print("  Errors:")
            for error in errors:
                print(f"    - {error}")
        print("=" * 64)
        print(f"Verdict: {'PASS' if not errors else 'FAIL'}")
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
