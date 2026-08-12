#!/usr/bin/env python3
"""Build the tracked lightweight plugin package and check it for drift."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from chart_registry_lib import ROOT


PACKAGE_ROOT = ROOT / "skills" / "academic-data-visualization"
FILES = [
    "LICENSE",
    "SKILL.md",
    "agents/openai.yaml",
    "pyproject.toml",
    "requirements/verified-core.txt",
    "fonts/LICENSES.md",
    "references/chart-registry.yaml",
    "references/chart-alias-index.md",
    "references/figure-type-catalog.md",
    "references/directory-map.md",
    "references/figure-contract.md",
    "references/figure-design-brief.md",
    "references/delivery-profiles.md",
    "references/visual-style.md",
    "references/typography.md",
    "references/color-palettes.md",
    "references/color-accessibility-qa.md",
    "references/palette-library.json",
    "references/multipanel-layout.md",
    "references/export-specs.md",
    "references/checklist.md",
    "references/common-pitfalls.md",
    "references/asset-reuse-protocol.md",
    "references/production-verification.md",
    "references/visual-review-protocol.md",
    "references/github-practice-notes.md",
    "scripts/chart_registry_lib.py",
    "scripts/manifest_lib.py",
    "scripts/palette_lib.py",
    "scripts/audit_palette_library.py",
    "scripts/color_audit.py",
    "scripts/query_chart.py",
    "scripts/run_asset.py",
    "scripts/qa_validator.py",
    "scripts/verified_template.py",
]


def expected_files() -> dict[Path, bytes]:
    result: dict[Path, bytes] = {}
    for relative in FILES:
        result[PACKAGE_ROOT / relative] = (ROOT / relative).read_bytes()
    for path in sorted((ROOT / "templates" / "production-verified").rglob("*")):
        if path.is_file():
            relative = path.relative_to(ROOT)
            result[PACKAGE_ROOT / relative] = path.read_bytes()
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = expected_files()
    current = {path for path in PACKAGE_ROOT.rglob("*") if path.is_file()} if PACKAGE_ROOT.exists() else set()
    stale = sorted(str(path.relative_to(ROOT)) for path in current - set(expected))
    changed = [str(path.relative_to(ROOT)) for path, payload in expected.items() if not path.exists() or path.read_bytes() != payload]
    differences = stale + changed
    if args.check:
        for path in differences:
            print(path)
        raise SystemExit(1 if differences else 0)
    if PACKAGE_ROOT.exists():
        shutil.rmtree(PACKAGE_ROOT)
    for path, payload in expected.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)
    print(f"Built skill package with {len(expected)} files")


if __name__ == "__main__":
    main()
