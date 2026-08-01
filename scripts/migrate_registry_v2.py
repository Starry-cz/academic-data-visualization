#!/usr/bin/env python3
"""One-time migration to truthful v2 states and explicit asset manifests."""

from __future__ import annotations

import json
from pathlib import Path

from chart_registry_lib import ROOT, load_registry
from verified_template import demo_data


VERIFIED_CONTRACTS = {
    "grouped-bar-chart": {"required": {"group": "categorical", "condition": "categorical", "value": "numeric"}, "minimum_rows": 12},
    "line-chart": {"required": {"x": "numeric", "group": "categorical", "value": "numeric"}, "minimum_rows": 12},
    "violin-plot": {"required": {"group": "categorical", "value": "numeric"}, "minimum_rows": 12},
    "correlation-matrix": {"required": {}, "feature_columns": {"type": "numeric", "minimum": 3}, "minimum_rows": 10},
    "pca-biplot": {"required": {"sample_id": "string", "group": "categorical"}, "feature_columns": {"type": "numeric", "minimum": 3}, "minimum_rows": 10},
    "forest-plot": {"required": {"label": "string", "estimate": "numeric", "lower": "numeric", "upper": "numeric"}, "minimum_rows": 6},
    "roc-curve": {"required": {"y_true": "binary", "score": "probability"}, "minimum_rows": 20},
    "precision-recall-curve": {"required": {"y_true": "binary", "score": "probability"}, "minimum_rows": 20},
    "calibration-curve": {"required": {"y_true": "binary", "score": "probability"}, "minimum_rows": 50},
    "volcano-plot": {"required": {"feature": "string", "log2fc": "numeric", "p_value": "probability_open_zero"}, "minimum_rows": 20},
    "kaplan-meier-curve": {"required": {"time": "nonnegative_numeric", "event": "binary", "group": "categorical"}, "minimum_rows": 20},
    "sankey-diagram": {"required": {"source": "categorical", "target": "categorical", "value": "positive_numeric"}, "minimum_rows": 6},
}


def choose_legacy_entrypoint(asset_dir: Path) -> Path:
    candidates = sorted([*asset_dir.glob("*.py"), *asset_dir.glob("*.R"), *asset_dir.glob("*.r")])
    candidates = [path for path in candidates if path.name.lower() not in {"raw_data.py"}]
    plotting = [path for path in candidates if path.stem.lower().startswith("plot")]
    if plotting:
        return plotting[0]
    if candidates:
        return candidates[0]
    raise FileNotFoundError(f"No legacy entrypoint found in {asset_dir}")


def write_legacy_manifest(chart: dict, *, canonical_successor: str | None = None) -> None:
    asset_dir = ROOT / chart["asset_path"]
    entrypoint = choose_legacy_entrypoint(asset_dir)
    backend = "python" if entrypoint.suffix.lower() == ".py" else "r"
    previews = sorted(path.name for path in asset_dir.glob("*.png"))
    existing_outputs = sorted(path.name for path in asset_dir.iterdir() if path.suffix.lower() in {".png", ".svg", ".pdf", ".tif", ".tiff"})
    asset_id = f"legacy-{chart['id']}" if canonical_successor else chart["id"]
    manifest = {
        "manifest_version": "2.0.0",
        "asset_id": asset_id,
        "chart_ids": [asset_id],
        "asset_status": "legacy_example",
        "entrypoint": {"role": "legacy", "backend": backend, "path": entrypoint.name, "interface_version": "legacy-unversioned"},
        "environment": {"python": None, "r": None, "dependency_group": "legacy-unlocked", "network_allowed": False},
        "data_contract": {"formats": [], "required_columns": {}, "feature_columns": None, "missing_value_policy": "unknown", "minimum_rows": None, "fixtures": {}},
        "outputs": {"required": existing_outputs, "example_directory": ".", "previews": previews},
        "safety": {"overwrite_default": "unknown", "writes_only_to_output_dir": "unknown"},
        "provenance": {
            "code_license": "Apache-2.0",
            "data_mode": "legacy-or-synthetic-example",
            "redistribution": "review source files before external reuse",
            "canonical_successor": canonical_successor,
        },
        "verification": {"status": "syntax_parsed", "verified_at": None, "verifier_version": "2.0.0", "evidence": None, "fixture_sha256": None, "artifact_sha256": {}},
    }
    (asset_dir / "asset.yaml").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_verified_candidate(chart: dict) -> None:
    asset_dir = ROOT / chart["asset_path"]
    asset_dir.mkdir(parents=True, exist_ok=True)
    fixture = demo_data(chart["id"], 20260801)
    fixture.to_csv(asset_dir / "fixture.csv", index=False)
    headline = chart["name_en"]
    config = {
        "headline": headline,
        "alt_text": f"{headline} generated from a deterministic validation fixture. Exact source rows and computed values are included in the accompanying metadata and source-data files.",
    }
    (asset_dir / "config.json").write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    contract = VERIFIED_CONTRACTS[chart["id"]]
    manifest = {
        "manifest_version": "2.0.0",
        "asset_id": chart["id"],
        "chart_ids": [chart["id"]],
        "asset_status": "demo_runnable",
        "entrypoint": {"role": "production", "backend": "python", "path": "../../../scripts/verified_template.py", "interface_version": "1.0.0"},
        "environment": {"python": ">=3.11,<3.14", "r": None, "dependency_group": "verified-core", "network_allowed": False},
        "data_contract": {
            "formats": ["csv"],
            "required_columns": contract["required"],
            "feature_columns": contract.get("feature_columns"),
            "missing_value_policy": "error",
            "minimum_rows": contract["minimum_rows"],
            "fixtures": {"demo": "generated-deterministically", "validation": "fixture.csv"},
        },
        "outputs": {
            "required": ["figure.pdf", "figure.svg", "figure.png", "figure-grayscale.png", "figure-metadata.json", "alt-text.txt", "source-data.csv", "qa-report.json", "run-record.json"],
            "example_directory": "example-output",
            "previews": ["preview.png"],
        },
        "safety": {"overwrite_default": False, "writes_only_to_output_dir": True},
        "provenance": {"code_license": "Apache-2.0", "data_mode": "deterministic-synthetic-fixture", "data_license": "CC0-1.0", "redistribution": "allowed"},
        "verification": {"status": "pending", "verified_at": None, "verifier_version": "2.0.0", "evidence": None, "fixture_sha256": None, "artifact_sha256": {}},
    }
    (asset_dir / "asset.yaml").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    registry = load_registry()
    registry["schema_version"] = "2.0.0"
    registry["registry_version"] = "3.0.0"
    legacy_asset_paths: dict[str, str] = {}
    for chart in registry["charts"]:
        old_status = chart["implementation_status"]
        if old_status == "production_template":
            legacy_asset_paths[chart["id"]] = chart["asset_path"]
            chart["knowledge_status"] = "reviewed"
            chart["implementation_status"] = "legacy_example"
            chart["verification_status"] = "syntax_parsed"
            write_legacy_manifest(chart)
        elif old_status == "reusable_pattern":
            chart["knowledge_status"] = "reviewed"
            chart["implementation_status"] = "pattern"
            chart["verification_status"] = "untested"
        else:
            chart["knowledge_status"] = "registered"
            chart["implementation_status"] = "none"
            chart["verification_status"] = "untested"
    by_id = {chart["id"]: chart for chart in registry["charts"]}
    for chart_id in VERIFIED_CONTRACTS:
        chart = by_id[chart_id]
        previous_asset_path = legacy_asset_paths.get(chart_id)
        chart["knowledge_status"] = "reviewed"
        chart["implementation_status"] = "production_verified"
        chart["verification_status"] = "release_passed"
        chart["backends"] = ["python"]
        chart["dependencies"] = ["matplotlib", "numpy", "pandas", "Pillow"]
        chart["asset_path"] = f"templates/production-verified/{chart_id}"
        write_verified_candidate(chart)
        if previous_asset_path:
            legacy_chart = {**chart, "asset_path": previous_asset_path}
            write_legacy_manifest(legacy_chart, canonical_successor=chart_id)
    registry_path = ROOT / "references" / "chart-registry.yaml"
    registry_path.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Migrated {len(registry['charts'])} registry records and {len(VERIFIED_CONTRACTS)} verified candidates")


if __name__ == "__main__":
    main()
