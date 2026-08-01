#!/usr/bin/env python3
"""Validate references, retained examples, generated maps, and registry integrity."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from check_chart_registry import validate_registry
from generate_directory_map import OUTPUT as DIRECTORY_MAP, render as render_directory_map
from manifest_lib import load_manifest


ROOT = Path(__file__).resolve().parents[1]
SKILL_MD = ROOT / "SKILL.md"
REFERENCES = ROOT / "references"
FIGURES_DIR = ROOT / "assets" / "figures"


def finding(check: str, severity: str, detail: str) -> dict[str, str]:
    return {"check": check, "severity": severity, "detail": detail}


def skill_targets() -> set[str]:
    text = SKILL_MD.read_text(encoding="utf-8")
    targets = set(re.findall(r"`((?:references|scripts)/[^`]+\.(?:md|json|py|R))`", text))
    return {target for target in targets if "<" not in target and ">" not in target}


def check_skill_links() -> list[dict[str, str]]:
    return [
        finding("missing_skill_target", "FAIL", target)
        for target in sorted(skill_targets())
        if not (ROOT / target).is_file()
    ]


def check_reference_health() -> list[dict[str, str]]:
    expected = {
        "asset-reuse-protocol.md",
        "checklist.md",
        "color-palettes.md",
        "chart-alias-index.md",
        "chart-coverage-audit.md",
        "chart-taxonomy-source.md",
        "common-pitfalls.md",
        "directory-map.md",
        "export-specs.md",
        "figure-contract.md",
        "figure-design-brief.md",
        "figure-type-catalog.md",
        "github-practice-notes.md",
        "journal-intel.md",
        "journal-specs.md",
        "multipanel-layout.md",
        "production-verification.md",
        "typography.md",
        "visual-review-protocol.md",
        "visual-style.md",
    }
    results: list[dict[str, str]] = []
    for name in sorted(expected):
        path = REFERENCES / name
        if not path.is_file():
            results.append(finding("missing_reference", "FAIL", name))
        elif path.stat().st_size < 100:
            results.append(finding("small_reference", "WARN", f"{name}: {path.stat().st_size} bytes"))
    return results


def retained_asset_dirs() -> list[Path]:
    return sorted(
        path
        for path in FIGURES_DIR.iterdir()
        if path.is_dir() and any([*path.glob("*.py"), *path.glob("*.R"), *path.glob("*.r")])
    )


def check_retained_assets() -> list[dict[str, str]]:
    results: list[dict[str, str]] = []
    for asset_dir in retained_asset_dirs():
        manifest_path = asset_dir / "asset.yaml"
        if not manifest_path.is_file():
            results.append(finding("missing_legacy_manifest", "FAIL", str(asset_dir.relative_to(ROOT))))
            continue
        manifest = load_manifest(manifest_path)
        if manifest.get("asset_status") != "legacy_example":
            results.append(finding("legacy_status_mismatch", "FAIL", str(manifest_path.relative_to(ROOT))))
        if not list(asset_dir.glob("*.png")):
            results.append(finding("missing_legacy_preview", "WARN", str(asset_dir.relative_to(ROOT))))
    return results


def check_generated_directory_map() -> list[dict[str, str]]:
    if not DIRECTORY_MAP.is_file() or DIRECTORY_MAP.read_text(encoding="utf-8") != render_directory_map():
        return [finding("stale_directory_map", "FAIL", "Run python scripts/generate_directory_map.py")]
    return []


def run_all() -> dict:
    results = [
        *check_skill_links(),
        *check_reference_health(),
        *check_retained_assets(),
        *check_generated_directory_map(),
        *[finding("chart_registry_integrity", "FAIL", error) for error in validate_registry()],
    ]
    failures = sum(item["severity"] == "FAIL" for item in results)
    warnings = sum(item["severity"] == "WARN" for item in results)
    return {
        "summary": {
            "retained_asset_dirs": len(retained_asset_dirs()),
            "skill_targets": len(skill_targets()),
            "failures": failures,
            "warnings": warnings,
            "healthy": failures == 0,
        },
        "findings": results,
    }


def main() -> None:
    report = run_all()
    if "--json" in sys.argv:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        summary = report["summary"]
        print(f"Reference integrity: {'PASS' if summary['healthy'] else 'FAIL'}")
        print(f"Retained assets: {summary['retained_asset_dirs']}; warnings: {summary['warnings']}")
        for item in report["findings"]:
            print(f"[{item['severity']}] {item['check']}: {item['detail']}")
    raise SystemExit(0 if report["summary"]["healthy"] else 1)


if __name__ == "__main__":
    main()
