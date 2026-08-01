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
    asset_records,
    load_registry,
    load_schema,
    normalize_alias,
    parse_source_taxonomy,
    production_records,
    source_memberships,
    status_counts,
    validate_schema,
)
from manifest_lib import load_manifest, validate_manifest


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

        if chart["implementation_status"] in {"legacy_example", "demo_runnable", "production_verified", "deprecated"}:
            if not chart["asset_path"]:
                errors.append(f"{chart['id']}: implemented record has no asset_path")
                continue
            asset_dir = ROOT / chart["asset_path"]
            if not asset_dir.is_dir():
                errors.append(f"{chart['id']}: asset directory does not exist: {chart['asset_path']}")
                continue
            manifest_path = asset_dir / "asset.yaml"
            if not manifest_path.is_file():
                errors.append(f"{chart['id']}: implemented asset requires asset.yaml")
                continue
            manifest = load_manifest(manifest_path)
            errors.extend(f"{chart['id']}: {error}" for error in validate_manifest(manifest, asset_dir))
            if chart["id"] not in manifest.get("chart_ids", []):
                errors.append(f"{chart['id']}: manifest does not list the canonical ID")
            if manifest.get("asset_status") != chart["implementation_status"]:
                errors.append(f"{chart['id']}: manifest and registry implementation status differ")
            if chart["implementation_status"] == "production_verified":
                if not chart["backends"]:
                    errors.append(f"{chart['id']}: production_verified must declare its backend")
                if chart["verification_status"] != "release_passed":
                    errors.append(f"{chart['id']}: production_verified must be release_passed")
                if not chart["asset_path"].startswith("templates/production-verified/"):
                    errors.append(f"{chart['id']}: verified template must live under templates/production-verified")
        elif chart["asset_path"] is not None:
            errors.append(f"{chart['id']}: knowledge-only record must not declare asset_path")

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
    registry_memberships = [
        (membership["source_category_id"], chart["id"], membership["source_label"])
        for chart in charts
        for membership in chart["source_memberships"]
    ]
    source_membership_records = [
        (entry["category_id"], entry["canonical_id"], entry["source_label"])
        for entry in entries
        if entry["canonical_id"] is not None
    ]
    if Counter(source_membership_records) != Counter(registry_memberships):
        errors.append("source taxonomy memberships differ from registry source_memberships")
    if len(pairs) != registry["source_expectation"]["available_source_memberships"]:
        errors.append("source_expectation.available_source_memberships is stale")
    if registry["source_expectation"]["source_complete"] and (
        len(pairs) != registry["source_expectation"]["declared_memberships"]
    ):
        errors.append("source_complete is true but declared and available memberships differ")
    for chart in charts:
        if chart["registry_origin"] == "source_taxonomy" and not chart["source_memberships"]:
            errors.append(f"{chart['id']}: source_taxonomy record has no source membership")
        if chart["registry_origin"] == "repository_extension" and chart["source_memberships"]:
            errors.append(f"{chart['id']}: repository_extension unexpectedly has source memberships")

    # 旧资产可作为历史示例保留；它们通过 manifest 的 canonical_successor
    # 指向唯一的生产模板，而不再占用 canonical chart 的执行入口。
    legacy_paths = {
        path
        for path in FIGURES_DIR.iterdir()
        if path.is_dir() and (path / "asset.yaml").is_file()
    }
    asset_dirs = {
        path for path in FIGURES_DIR.iterdir()
        if path.is_dir() and any([*path.glob("*.py"), *path.glob("*.R"), *path.glob("*.r")])
    }
    missing_registry = sorted(str(path.relative_to(ROOT)) for path in asset_dirs - legacy_paths)
    orphan_registry = sorted(str(path.relative_to(ROOT)) for path in legacy_paths - asset_dirs)
    if missing_registry:
        errors.append(f"legacy asset directories missing from registry: {missing_registry}")
    if orphan_registry:
        errors.append(f"registry legacy paths without assets: {orphan_registry}")
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
        "origin_counts": {
            origin: sum(chart["registry_origin"] == origin for chart in registry["charts"])
            for origin in ("source_taxonomy", "repository_extension")
        },
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
        print(f"  Source chart records: {result['origin_counts']['source_taxonomy']}")
        print(f"  Repository extensions: {result['origin_counts']['repository_extension']}")
        print(f"  Production verified: {result['status_counts']['production_verified']}")
        print(f"  Legacy examples     : {result['status_counts']['legacy_example']}")
        print(f"  Reusable patterns   : {result['status_counts']['pattern']}")
        print(f"  Knowledge-only      : {result['status_counts']['none']}")
        if errors:
            print("  Errors:")
            for error in errors:
                print(f"    - {error}")
        print("=" * 64)
        print(f"Verdict: {'PASS' if not errors else 'FAIL'}")
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
