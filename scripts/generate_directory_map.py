#!/usr/bin/env python3
"""Generate the truthful verified-template and retained-legacy asset directory map."""

from __future__ import annotations

import argparse
from pathlib import Path

from chart_registry_lib import ROOT, load_registry
from manifest_lib import find_asset_manifests, load_manifest


OUTPUT = ROOT / "references" / "directory-map.md"


def render() -> str:
    registry = load_registry()
    by_id = {chart["id"]: chart for chart in registry["charts"]}
    verified: list[tuple[Path, dict]] = []
    legacy: list[tuple[Path, dict]] = []
    for path in find_asset_manifests():
        manifest = load_manifest(path)
        if manifest["asset_status"] == "production_verified":
            verified.append((path, manifest))
        elif manifest["asset_status"] == "legacy_example":
            legacy.append((path, manifest))

    lines = [
        "# Asset Directory Map / 资产目录",
        "",
        "> 本文件由 `scripts/generate_directory_map.py` 生成。生产模板与历史示例严格分开；历史示例不能作为已验证模板直接路由。",
        "",
        "## Release-verified templates / 发布级已验证模板",
        "",
        "这些模板均已完成 demo 与固定 fixture 两条执行路径、程序 QA、最终尺寸 RGB/灰度审阅和证据哈希。",
        "",
        "| Chart | Canonical ID | Backend | Asset path | Run |",
        "|---|---|---|---|---|",
    ]
    for path, manifest in verified:
        chart = by_id[manifest["asset_id"]]
        asset_path = path.parent.relative_to(ROOT).as_posix()
        lines.append(
            f"| {chart['name_zh']} / {chart['name_en']} | `{chart['id']}` | "
            f"{manifest['entrypoint']['backend']} | `{asset_path}` | "
            f"`python scripts/run_asset.py --chart-id {chart['id']} --demo --output-dir <dir>` |"
        )
    lines.extend(
        [
            "",
            "## Retained legacy examples / 保留的历史示例",
            "",
            "这些目录保留原脚本与图片供人工参考，但未满足统一输入接口、隔离输出、真实渲染 QA 或发布证据门禁。",
            "",
            "| Legacy asset | Related canonical chart | Backend | Directory | Verification |",
            "|---|---|---|---|---|",
        ]
    )
    for path, manifest in legacy:
        successor = manifest.get("provenance", {}).get("canonical_successor")
        canonical_id = successor or manifest["asset_id"]
        chart = by_id.get(canonical_id)
        name = f"{chart['name_zh']} / {chart['name_en']}" if chart else manifest["asset_id"]
        lines.append(
            f"| `{manifest['asset_id']}` | {name} (`{canonical_id}`) | "
            f"{manifest['entrypoint']['backend']} | `{path.parent.relative_to(ROOT).as_posix()}` | "
            f"`{manifest['verification']['status']}` |"
        )
    lines.extend(
        [
            "",
            "## Routing rules / 路由规则",
            "",
            "1. 先用 `python scripts/query_chart.py --name <名称>` 或 `--question <研究问题>` 获取 canonical record。",
            "2. 只有 `production_verified + release_passed` 才能交给统一运行器；其他状态只能作为知识或人工改造参考。",
            "3. 不得为缺少真实实现的图型伪造目录、预览或发布状态。",
            "4. 精选成图与配色资产由 `references/showcase-lock.json` 单独锁定，不随生产模板迁移而替换。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = render()
    if args.check:
        raise SystemExit(0 if OUTPUT.is_file() and OUTPUT.read_text(encoding="utf-8") == expected else 1)
    OUTPUT.write_text(expected, encoding="utf-8")
    print(f"Generated {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
