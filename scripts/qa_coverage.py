#!/usr/bin/env python3
"""Exercise the current source and rendered-output QA contract."""

from __future__ import annotations

import argparse
import json
import tempfile
from pathlib import Path

from color_audit import audit_svg_colours
from qa_validator import audit_metadata, audit_source, check_cl3_dpi


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_OUTPUT_CHECKS = {
    "OUT-0", "OUT-1", "OUT-2", "OUT-3", "OUT-4", "OUT-5", "OUT-6", "OUT-7",
    "DATA-1", "DATA-2", "DATA-3", "DATA-4", "COLOR-1", "A11Y-1", "A11Y-2",
}


def source_lane() -> list[dict[str, object]]:
    good = """\
import argparse
def main():
    parser = argparse.ArgumentParser()
    for flag in ('--input', '--demo', '--output-dir', '--profile', '--theme', '--seed'):
        parser.add_argument(flag)
if __name__ == '__main__':
    main()
"""
    bad = good + "\ninstall.packages('x')\nread_csv('./input.csv')\nplt.show()\n"
    with tempfile.TemporaryDirectory(prefix="adv-qa-coverage-") as temp:
        root = Path(temp)
        good_path, bad_path = root / "good.py", root / "bad.py"
        good_path.write_text(good, encoding="utf-8")
        bad_path.write_text(bad, encoding="utf-8")
        good_findings = {item.check_id: item for item in audit_source(good_path, production_interface=True)}
        bad_findings = {item.check_id: item for item in audit_source(bad_path, production_interface=True)}
    return [
        {"name": "good source passes", "passed": all(item.pass_ for item in good_findings.values())},
        {"name": "runtime install is caught", "passed": not bad_findings["SRC-1"].pass_},
        {"name": "cwd-relative input is caught", "passed": not bad_findings["SRC-2"].pass_},
        {"name": "interactive show is caught", "passed": not bad_findings["SRC-3"].pass_},
        {"name": "low DPI is caught", "passed": not check_cl3_dpi("dpi=72").pass_},
        {"name": "print DPI passes", "passed": check_cl3_dpi("dpi=450").pass_},
    ]


def rendered_lane() -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for report_path in sorted((ROOT / "templates" / "production-verified").glob("*/example-output/qa-report.json")):
        report = json.loads(report_path.read_text(encoding="utf-8"))
        ids = {item["check_id"] for item in report["findings"]}
        results.append(
            {
                "name": f"{report['asset_id']} stored output contract",
                "passed": report["passed"] and EXPECTED_OUTPUT_CHECKS.issubset(ids),
            }
        )
    return results


def palette_tamper_lane() -> list[dict[str, object]]:
    asset = ROOT / "templates" / "production-verified" / "forest-plot" / "example-output"
    metadata = json.loads((asset / "figure-metadata.json").read_text(encoding="utf-8"))
    metadata["palette"]["categorical"][0] = "#123456"
    with tempfile.TemporaryDirectory(prefix="adv-palette-coverage-") as temp:
        metadata_path = Path(temp) / "figure-metadata.json"
        metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
        findings = {item.check_id: item for item in audit_metadata(metadata_path, asset / "source-data.csv", metadata["profile"])}
    return [{"name": "unregistered palette value is caught", "passed": not findings["COLOR-1"].pass_}]


def rendered_colour_lane() -> list[dict[str, object]]:
    svg = """\
<svg xmlns="http://www.w3.org/2000/svg" width="200" height="120">
  <g id="figure_1">
    <g id="patch_1"><path d="M 0 0 H 200 V 120 H 0 Z" style="fill: #FFFFFF"/></g>
    <g id="Line2D_1"><path d="M 10 80 L 190 20" style="fill: none; stroke: #BDE2ED; stroke-width: 2"/></g>
    <text x="10" y="110" style="fill: #B0B0B0">Faint label</text>
  </g>
</svg>
"""
    with tempfile.TemporaryDirectory(prefix="adv-colour-coverage-") as temp:
        path = Path(temp) / "figure.svg"
        path.write_text(svg, encoding="utf-8")
        compatible = {item.check_id: item for item in audit_svg_colours(path, ["#BDE2ED"], strict=False)}
        strict = {item.check_id: item for item in audit_svg_colours(path, ["#BDE2ED"], strict=True)}
    return [
        {
            "name": "rendered contrast remains backward-compatible by default",
            "passed": compatible["COLOR-2"].severity == "WARN" and compatible["A11Y-3"].severity == "WARN",
        },
        {
            "name": "strict rendered contrast blocks pale text and marks",
            "passed": strict["COLOR-2"].severity == "FAIL" and strict["A11Y-3"].severity == "FAIL",
        },
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    results = source_lane() + rendered_lane() + palette_tamper_lane() + rendered_colour_lane()
    passed = sum(bool(item["passed"]) for item in results)
    payload = {"checks": len(results), "passed": passed, "failed": len(results) - passed, "results": results}
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        for item in results:
            print(f"[{'PASS' if item['passed'] else 'FAIL'}] {item['name']}")
        print(f"QA coverage: {passed}/{len(results)} passed")
    raise SystemExit(0 if passed == len(results) else 1)


if __name__ == "__main__":
    main()
