#!/usr/bin/env python3
"""Run one verified asset in an isolated output directory and validate its bundle."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

from manifest_lib import ROOT, load_manifest, manifest_by_chart_id, validate_manifest
from palette_lib import THEME_IDS, resolve_theme


RUNNER_VERSION = "2.0.0"
ALLOWED_RENDERER_STDERR_LINES = {
    "Matplotlib is building the font cache; this may take a moment.",
}


def unexpected_renderer_stderr(stderr: str) -> str:
    """Remove only known one-time runtime notices; preserve every real warning."""
    # 全新 CI 主机首次建立字体缓存属于状态通知，不是渲染或数据质量警告。
    lines = [line.strip() for line in stderr.splitlines() if line.strip()]
    return "\n".join(line for line in lines if line not in ALLOWED_RENDERER_STDERR_LINES)


def repository_snapshot(excluded: Path) -> dict[Path, tuple[int, int]]:
    snapshot: dict[Path, tuple[int, int]] = {}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        try:
            path.resolve().relative_to(excluded)
            continue
        except ValueError:
            pass
        stat = path.stat()
        snapshot[path.resolve()] = (stat.st_size, stat.st_mtime_ns)
    return snapshot


def changed_paths(before: dict[Path, tuple[int, int]], excluded: Path) -> list[str]:
    after = repository_snapshot(excluded)
    changed = set(before) ^ set(after)
    changed.update(path for path in set(before) & set(after) if before[path] != after[path])
    return sorted(str(path.relative_to(ROOT.resolve())) for path in changed)


def run_asset(
    manifest_path: Path,
    output_dir: Path,
    input_path: Path | None,
    demo: bool,
    profile: str,
    theme: str,
    seed: int,
    config: Path | None,
    timeout: int,
    overwrite: bool,
    validate_evidence: bool = True,
) -> dict[str, Any]:
    manifest_path = manifest_path.resolve()
    asset_dir = manifest_path.parent
    manifest = load_manifest(manifest_path)
    errors = validate_manifest(manifest, asset_dir, check_artifact_hashes=validate_evidence)
    if errors:
        raise ValueError("Invalid manifest: " + "; ".join(errors))
    if manifest["asset_status"] not in {"demo_runnable", "production_verified"}:
        raise ValueError(f"run_asset accepts runnable v2 assets only, got {manifest['asset_status']}")
    if demo == (input_path is not None):
        raise ValueError("Choose exactly one of demo mode or an input file")
    theme = resolve_theme(manifest["asset_id"], theme)
    output_dir = output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    if any(output_dir.iterdir()) and not overwrite:
        raise FileExistsError(f"Output directory is not empty: {output_dir}")
    entrypoint = (asset_dir / manifest["entrypoint"]["path"]).resolve()
    command = [
        sys.executable,
        str(entrypoint),
        "--chart-id",
        manifest["asset_id"],
        "--output-dir",
        str(output_dir),
        "--profile",
        profile,
        "--theme",
        theme,
        "--seed",
        str(seed),
    ]
    command.extend(["--demo"] if demo else ["--input", str(input_path.resolve())])
    if config:
        command.extend(["--config", str(config.resolve())])
    if overwrite:
        command.append("--overwrite")

    # 审计记录使用可移植占位符，避免把维护者机器的绝对路径写入仓库证据。
    recorded_command = [
        "python",
        "scripts/verified_template.py",
        "--chart-id",
        manifest["asset_id"],
        "--output-dir",
        "<OUTPUT_DIR>",
        "--profile",
        profile,
        "--theme",
        theme,
        "--seed",
        str(seed),
    ]
    recorded_command.extend(["--demo"] if demo else ["--input", "<INPUT_CSV>"])
    if config:
        recorded_command.extend(["--config", "<CONFIG_JSON>"])
    if overwrite:
        recorded_command.append("--overwrite")

    # 将 Matplotlib 缓存放入输出目录，避免模板修改用户目录或仓库。
    environment = os.environ.copy()
    environment.update(
        {
            "MPLBACKEND": "Agg",
            "MPLCONFIGDIR": str(output_dir / ".mplconfig"),
            "PIP_NO_INDEX": "1",
            "PYTHONDONTWRITEBYTECODE": "1",
        }
    )
    before = repository_snapshot(output_dir)
    started = time.time()
    completed = subprocess.run(command, capture_output=True, text=True, timeout=timeout, env=environment, cwd=output_dir, check=False)
    duration = time.time() - started
    changed = changed_paths(before, output_dir)
    if completed.returncode != 0:
        raise RuntimeError(f"Renderer failed ({completed.returncode}):\n{completed.stdout}\n{completed.stderr}")
    unexpected_stderr = unexpected_renderer_stderr(completed.stderr)
    if unexpected_stderr:
        raise RuntimeError(f"Renderer emitted stderr in strict production mode:\n{unexpected_stderr}")
    renderer_payload = json.loads(completed.stdout)
    if renderer_payload.get("chart_id") != manifest["asset_id"]:
        raise RuntimeError("Renderer JSON does not identify the requested asset")
    if changed:
        raise RuntimeError(f"Renderer modified files outside output_dir: {changed}")

    qa_path = ROOT / "scripts" / "qa_validator.py"
    qa_report = output_dir / "qa-report.json"
    qa_command = [sys.executable, str(qa_path), "--output-dir", str(output_dir), "--manifest", str(manifest_path), "--report", str(qa_report)]
    qa_completed = subprocess.run(qa_command, capture_output=True, text=True, timeout=timeout, env=environment, cwd=output_dir, check=False)
    if qa_completed.returncode != 0:
        raise RuntimeError(f"Rendered QA failed:\n{qa_completed.stdout}\n{qa_completed.stderr}")
    qa = json.loads(qa_report.read_text(encoding="utf-8"))
    record: dict[str, Any] = {
        "runner_version": RUNNER_VERSION,
        "asset_id": manifest["asset_id"],
        "mode": "demo" if demo else "input",
        "profile": profile,
        "theme": theme,
        "seed": seed,
        "command": recorded_command,
        "duration_seconds": round(duration, 3),
        "renderer_returncode": completed.returncode,
        "qa_passed": qa["passed"],
        "renderer_summary": {
            "chart_id": renderer_payload["chart_id"],
            "outputs": renderer_payload["outputs"],
        },
        "stderr": "",
    }
    (output_dir / "run-record.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return record


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    identity = parser.add_mutually_exclusive_group(required=True)
    identity.add_argument("--chart-id")
    identity.add_argument("--manifest", type=Path)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--input", type=Path)
    source.add_argument("--demo", action="store_true")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--config", type=Path)
    parser.add_argument("--profile", default="journal_print", choices=["journal_print", "report_web", "keynote_screen", "poster_large"])
    parser.add_argument("--theme", default="auto", choices=("auto", *THEME_IDS))
    parser.add_argument("--seed", type=int, default=20260801)
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    manifest_path = args.manifest
    if args.chart_id:
        manifest_path, _ = manifest_by_chart_id(args.chart_id)
    record = run_asset(
        manifest_path=manifest_path,
        output_dir=args.output_dir,
        input_path=args.input,
        demo=args.demo,
        profile=args.profile,
        theme=args.theme,
        seed=args.seed,
        config=args.config,
        timeout=args.timeout,
        overwrite=args.overwrite,
    )
    print(json.dumps(record, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
