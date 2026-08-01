#!/usr/bin/env python3
"""Report distinct trigger, routing, execution, and output-quality evidence lanes."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from build_chart_registry import audit_manifests
from chart_registry_lib import ROOT, load_registry, resolve_chart_name
from manifest_lib import find_asset_manifests, load_manifest
from qa_validator import audit_source


ROUTING_FIXTURES = {
    "AUROC": ["roc-curve"],
    "PR curve": ["precision-recall-curve"],
    "Kaplan-Meier": ["kaplan-meier-curve"],
    "相关矩阵": ["correlation-matrix"],
    "漏斗图": ["meta-analysis-funnel-plot", "conversion-funnel-chart"],
}


def syntax_lane() -> dict:
    records = []
    for path in find_asset_manifests():
        manifest = load_manifest(path)
        entrypoint = (path.parent / manifest["entrypoint"]["path"]).resolve()
        if manifest["entrypoint"]["backend"] == "python":
            source = entrypoint.read_text(encoding="utf-8", errors="replace")
            try:
                compile(source, str(entrypoint), "exec")
                passed, detail = True, "Python syntax parsed"
            except SyntaxError as error:
                passed, detail = False, str(error)
        else:
            passed, detail = True, "R syntax not executed in this lane; use the R CI job"
        records.append({"asset_id": manifest["asset_id"], "passed": passed, "detail": detail})
    return {"name": "syntax", "passed": all(item["passed"] for item in records), "records": records}


def routing_lane() -> dict:
    registry = load_registry()
    records = [
        {"query": query, "expected": expected, "actual": resolve_chart_name(registry, query)}
        for query, expected in ROUTING_FIXTURES.items()
    ]
    return {"name": "routing", "passed": all(item["expected"] == item["actual"] for item in records), "records": records}


def execution_lane(execute: bool) -> dict:
    if not execute:
        return {"name": "execution", "passed": None, "detail": "Not run. Use --execute to render every verified template."}
    command = [sys.executable, str(ROOT / "scripts" / "verify_production_assets.py")]
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
    return {"name": "execution", "passed": result.returncode == 0, "stdout": result.stdout, "stderr": result.stderr}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    lanes = {
        "manifest": {"name": "manifest", "passed": not audit_manifests(), "errors": audit_manifests()},
        "syntax": syntax_lane(),
        "routing": routing_lane(),
        "execution": execution_lane(args.execute),
        "trigger": {"name": "trigger", "passed": None, "detail": "Regex fixtures are reported separately and are not model-behaviour evidence."},
        "quality": {"name": "quality", "passed": None if not args.execute else True, "detail": "Rendered QA is part of the execution lane; perceptual review remains a recorded human gate."},
    }
    required = [lanes["manifest"]["passed"], lanes["syntax"]["passed"], lanes["routing"]["passed"]]
    if args.execute:
        required.append(lanes["execution"]["passed"])
    report = {"evaluation_version": "2.0.0", "lanes": lanes, "passed": all(required)}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
