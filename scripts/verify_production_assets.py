#!/usr/bin/env python3
"""Execute every candidate template twice, preserve evidence, and promote only passing assets."""

from __future__ import annotations

import argparse
import importlib.metadata
import json
import platform
import shutil
import sys
import tempfile
from datetime import date
from pathlib import Path

from manifest_lib import ROOT, load_manifest, sha256_file, validate_manifest
from run_asset import run_asset


PACKAGES = ("matplotlib", "numpy", "pandas", "Pillow")


def package_versions() -> dict[str, str]:
    versions: dict[str, str] = {}
    for package in PACKAGES:
        versions[package] = importlib.metadata.version(package)
    return versions


def verify_one(manifest_path: Path, refresh_evidence: bool) -> dict:
    asset_dir = manifest_path.parent
    manifest = load_manifest(manifest_path)
    fixture = asset_dir / manifest["data_contract"]["fixtures"]["validation"]
    if not fixture.is_file():
        raise FileNotFoundError(f"Validation fixture is missing: {fixture}")
    with tempfile.TemporaryDirectory(prefix=f"adv-{manifest['asset_id']}-") as temp_root:
        temp = Path(temp_root)
        demo_record = run_asset(manifest_path, temp / "demo", None, True, "journal_print", "auto", 20260801, None, 120, False)
        input_record = run_asset(manifest_path, temp / "input", fixture, False, "journal_print", "auto", 20260801, None, 120, False)
        if not refresh_evidence:
            return {"asset_id": manifest["asset_id"], "demo": demo_record, "input": input_record}
        example_dir = asset_dir / manifest["outputs"]["example_directory"]
        if example_dir.exists():
            shutil.rmtree(example_dir)
        shutil.copytree(temp / "input", example_dir)
        cache_dir = example_dir / ".mplconfig"
        if cache_dir.exists():
            # 字体缓存可能包含维护者机器路径，不属于可复现交付证据。
            shutil.rmtree(cache_dir)
        shutil.copy2(example_dir / "figure.png", asset_dir / "preview.png")
        output_hashes = {name: sha256_file(example_dir / name) for name in manifest["outputs"]["required"]}
        evidence = {
            "verification_version": "2.0.0",
            "asset_id": manifest["asset_id"],
            "verified_at": date.today().isoformat(),
            "python": sys.version.split()[0],
            "platform": platform.platform(),
            "packages": package_versions(),
            "fixture": {
                "path": fixture.name,
                "sha256": sha256_file(fixture),
            },
            "modes": {
                "demo": demo_record,
                "input": input_record,
            },
            "artifact_sha256": output_hashes,
            "visual_review": {
                "status": "pending",
                "rubric": "references/visual-review-protocol.md",
                "reviewer": None,
            },
        }
        evidence_path = asset_dir / "verification-record.json"
        evidence_path.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        manifest["asset_status"] = "demo_runnable"
        manifest["verification"] = {
            "status": "rendered_passed",
            "verified_at": evidence["verified_at"],
            "verifier_version": evidence["verification_version"],
            "evidence": evidence_path.name,
            "fixture_sha256": evidence["fixture"]["sha256"],
            "artifact_sha256": output_hashes,
        }
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return evidence


def approve_visual_review(manifest_path: Path, reviewer: str) -> dict:
    """人工看图完成后，校验留存证据并晋升为正式生产模板。"""
    asset_dir = manifest_path.parent
    manifest = load_manifest(manifest_path)
    evidence_path = asset_dir / "verification-record.json"
    if not evidence_path.is_file():
        raise FileNotFoundError(f"Verification evidence is missing: {evidence_path}")
    evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
    failed_modes = [name for name, record in evidence.get("modes", {}).items() if not record.get("qa_passed")]
    if failed_modes or set(evidence.get("modes", {})) != {"demo", "input"}:
        raise ValueError(f"Both demo and input modes must have passing QA: {failed_modes}")
    example_dir = asset_dir / manifest["outputs"]["example_directory"]
    for name, expected_hash in evidence["artifact_sha256"].items():
        artifact = example_dir / name
        if not artifact.is_file() or sha256_file(artifact) != expected_hash:
            raise ValueError(f"Artifact changed after rendering: {artifact}")
    qa_report = json.loads((example_dir / "qa-report.json").read_text(encoding="utf-8"))
    if not qa_report.get("passed"):
        raise ValueError(f"Stored QA evidence does not pass: {example_dir / 'qa-report.json'}")
    evidence["visual_review"] = {
        "status": "passed",
        "rubric": "references/visual-review-protocol.md",
        "reviewer": reviewer,
    }
    evidence_path.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    manifest["asset_status"] = "production_verified"
    manifest["verification"]["status"] = "release_passed"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    errors = validate_manifest(manifest, asset_dir)
    if errors:
        raise ValueError("Manifest failed after visual approval: " + "; ".join(errors))
    return evidence


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chart-id", action="append", default=[])
    parser.add_argument("--refresh-evidence", action="store_true")
    parser.add_argument("--approve-visual", action="store_true")
    parser.add_argument("--reviewer")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.approve_visual and (args.refresh_evidence or not args.reviewer):
        raise SystemExit("--approve-visual requires --reviewer and cannot be combined with --refresh-evidence")
    root = ROOT / "templates" / "production-verified"
    manifests = sorted(root.glob("*/asset.yaml"))
    if args.chart_id:
        selected = set(args.chart_id)
        manifests = [path for path in manifests if load_manifest(path)["asset_id"] in selected]
        missing = selected - {load_manifest(path)["asset_id"] for path in manifests}
        if missing:
            raise SystemExit(f"Unknown verified template IDs: {sorted(missing)}")
    results = []
    for manifest_path in manifests:
        if args.approve_visual:
            print(f"Approving visual review for {manifest_path.parent.name} ...", flush=True)
            results.append(approve_visual_review(manifest_path, args.reviewer))
        else:
            print(f"Verifying {manifest_path.parent.name} ...", flush=True)
            results.append(verify_one(manifest_path, args.refresh_evidence))
    print(json.dumps({"verified": len(results), "assets": [item["asset_id"] for item in results]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
