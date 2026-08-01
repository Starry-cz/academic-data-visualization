#!/usr/bin/env python3
"""Manifest v2 helpers shared by asset validation and execution tools."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_VERSION = "2.0.0"
ASSET_STATES = {"legacy_example", "demo_runnable", "production_verified", "deprecated"}
PROFILES = {"journal_print", "report_web", "keynote_screen", "poster_large"}
TEXT_HASH_SUFFIXES = {".csv", ".json", ".md", ".svg", ".txt", ".yaml", ".yml"}


def load_manifest(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256_file(path: Path) -> str:
    """Return a platform-stable digest while preserving strict binary checks."""
    if path.suffix.lower() in TEXT_HASH_SUFFIXES:
        # Git 在不同平台可能签出 CRLF 或 LF；文本证据先统一换行再计算哈希。
        content = path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
        return hashlib.sha256(content.encode("utf-8")).hexdigest()
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_manifest(
    manifest: dict[str, Any],
    asset_dir: Path,
    *,
    check_artifact_hashes: bool = True,
) -> list[str]:
    """Validate fields that define truthful state, runnable entrypoints, and safe outputs."""
    errors: list[str] = []
    required = {
        "manifest_version",
        "asset_id",
        "chart_ids",
        "asset_status",
        "entrypoint",
        "environment",
        "data_contract",
        "outputs",
        "safety",
        "provenance",
        "verification",
    }
    missing = sorted(required - manifest.keys())
    if missing:
        return [f"missing manifest fields: {missing}"]
    if manifest["manifest_version"] != MANIFEST_VERSION:
        errors.append(f"manifest_version must be {MANIFEST_VERSION}")
    if manifest["asset_status"] not in ASSET_STATES:
        errors.append(f"unknown asset_status: {manifest['asset_status']}")
    if manifest["asset_id"] not in manifest.get("chart_ids", []):
        errors.append("asset_id must be listed in chart_ids")
    entrypoint = manifest.get("entrypoint", {})
    if set(entrypoint) != {"role", "backend", "path", "interface_version"}:
        errors.append("entrypoint must declare role, backend, path, and interface_version")
    else:
        entrypoint_path = (asset_dir / entrypoint["path"]).resolve()
        if not entrypoint_path.is_file():
            errors.append(f"entrypoint does not exist: {entrypoint['path']}")
        if entrypoint["role"] not in {"legacy", "production"}:
            errors.append("entrypoint.role must be legacy or production")
        if entrypoint["backend"] not in {"python", "r"}:
            errors.append("entrypoint.backend must be python or r")
    environment = manifest.get("environment", {})
    if environment.get("network_allowed") is not False:
        errors.append("network_allowed must be false for repository assets")
    safety = manifest.get("safety", {})
    for key in ("overwrite_default", "writes_only_to_output_dir"):
        if key not in safety:
            errors.append(f"safety.{key} is required")
    if manifest["asset_status"] == "production_verified":
        if entrypoint.get("role") != "production" or entrypoint.get("interface_version") != "1.0.0":
            errors.append("production_verified requires the unified production interface")
        contract = manifest.get("data_contract", {})
        if not contract.get("formats") or contract.get("missing_value_policy") != "error":
            errors.append("production_verified requires formats and an explicit missing-value policy")
        outputs = manifest.get("outputs", {}).get("required", [])
        required_outputs = {
            "figure.pdf",
            "figure.svg",
            "figure.png",
            "figure-grayscale.png",
            "figure-metadata.json",
            "alt-text.txt",
            "source-data.csv",
            "qa-report.json",
            "run-record.json",
        }
        if not required_outputs.issubset(outputs):
            errors.append(f"production output contract is incomplete: {sorted(required_outputs - set(outputs))}")
        verification = manifest.get("verification", {})
        if verification.get("status") != "release_passed":
            errors.append("production_verified requires verification.status=release_passed")
        evidence_path = asset_dir / verification.get("evidence", "")
        if not evidence_path.is_file():
            errors.append("production verification evidence is missing")
        example_dir = asset_dir / manifest.get("outputs", {}).get("example_directory", "")
        if not example_dir.is_dir():
            errors.append("production example output directory is missing")
        else:
            hashes = verification.get("artifact_sha256", {})
            for name in outputs:
                output_path = example_dir / name
                if not output_path.is_file():
                    errors.append(f"required example output is missing: {name}")
                elif check_artifact_hashes and name in hashes and sha256_file(output_path) != hashes[name]:
                    errors.append(f"recorded hash differs for {name}")
    elif manifest.get("verification", {}).get("status") == "release_passed":
        errors.append("non-production assets cannot claim release_passed")
    return errors


def find_asset_manifests() -> list[Path]:
    roots = [ROOT / "assets" / "figures", ROOT / "templates" / "production-verified"]
    manifests = [path for root in roots if root.exists() for path in root.glob("*/asset.yaml")]
    # 使用仓库相对 POSIX 路径，避免 Windows 与 Linux 的大小写排序差异。
    return sorted(manifests, key=lambda path: path.relative_to(ROOT).as_posix().casefold())


def manifest_by_chart_id(chart_id: str) -> tuple[Path, dict[str, Any]]:
    matches: list[tuple[Path, dict[str, Any]]] = []
    for path in find_asset_manifests():
        manifest = load_manifest(path)
        if chart_id in manifest.get("chart_ids", []):
            matches.append((path, manifest))
    if len(matches) != 1:
        raise ValueError(f"Expected exactly one manifest for {chart_id!r}, found {len(matches)}")
    return matches[0]
