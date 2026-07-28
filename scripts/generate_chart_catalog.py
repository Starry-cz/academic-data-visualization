#!/usr/bin/env python3
"""Generate the 24 category documents, alias index, statistics, and README blocks."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

from chart_registry_lib import (
    ALIAS_INDEX_PATH,
    CHART_TYPES_DIR,
    ROOT,
    category_filename,
    load_registry,
    replace_generated_block,
    status_counts,
)


STATUS_ZH = {
    "production_template": "生产模板",
    "reusable_pattern": "可复用模式",
    "on_demand": "按需实现",
}


def joined(values: list[str]) -> str:
    return "；".join(values) if values else "无"


def render_category(category: dict, charts: list[dict]) -> str:
    lines = [
        f"# {category['name_zh']} / {category['name_en']}",
        "",
        "> 本文件由 `scripts/generate_chart_catalog.py` 从 `chart-registry.yaml` 生成；不要手工编辑。",
        "",
        "## 类别用途",
        "",
        f"用于路由“{category['name_zh']}”相关研究问题。先核对数据契约，再按实现状态决定复用或新实现。",
        "",
        "## 选择总则",
        "",
        "1. 先确认研究问题、观测单位和必需变量；不得从图名反推数据。",
        "2. `生产模板` 才能直接进入资产复用流程；其余状态仍需按数据实现并完成四轮 QA。",
        "3. 优先保留原始证据、效应量和不确定性，不用装饰性编码替代统计信息。",
        "",
        "## 数据契约总览",
        "",
        "| Canonical ID | 观测单位 | 必需变量 | 实现状态 |",
        "|---|---|---|---|",
    ]
    for chart in charts:
        lines.append(
            f"| `{chart['id']}` | {chart['observation_unit']} | "
            f"{', '.join(chart['required_variables'])} | {STATUS_ZH[chart['implementation_status']]} |"
        )
    lines.extend(["", "## 图型索引", "", "| 图型 | Canonical ID | 信息任务 | 状态 |", "|---|---|---|---|"])
    for chart in charts:
        lines.append(
            f"| {chart['name_zh']} / {chart['name_en']} | `{chart['id']}` | "
            f"{joined(chart['information_tasks'])} | {STATUS_ZH[chart['implementation_status']]} |"
        )
    lines.extend(["", "## 图型详细条目", ""])
    for chart in charts:
        asset = f"`{chart['asset_path']}`" if chart["asset_path"] else "无现成资产"
        aliases = [*chart["aliases_zh"], *chart["aliases_en"]]
        lines.extend(
            [
                f"### {chart['name_zh']}（{chart['name_en']}）",
                "",
                f"- **Canonical ID**：`{chart['id']}`",
                f"- **别名**：{joined(aliases)}",
                f"- **适合回答**：{joined(chart['research_questions'])}",
                f"- **定义**：{chart['definition']}",
                f"- **必需数据**：{joined(chart['required_variables'])}",
                f"- **可选数据**：{joined(chart['optional_variables'])}",
                f"- **观测单位**：{chart['observation_unit']}",
                f"- **推荐编码**：{joined(chart['visual_encoding'])}",
                f"- **适用条件**：{joined(chart['suitable_when'])}",
                f"- **不适用条件**：{joined(chart['avoid_when'])}",
                f"- **统计与不确定性**：{joined(chart['statistics'] + chart['uncertainty'])}",
                f"- **样本量与分布要求**：{chart['minimum_sample']}",
                f"- **轴、尺度与变换**：{joined(chart['axes_scales'] + chart['allowed_transforms'])}",
                f"- **禁止变换**：{joined(chart['forbidden_transforms'])}",
                f"- **颜色、灰度与无障碍**：{joined(chart['color_grayscale'] + chart['accessibility'])}",
                f"- **标注规则**：{joined(chart['annotations'])}",
                f"- **常见投稿风险**：{joined(chart['publication_risks'])}",
                f"- **实现状态**：`{chart['implementation_status']}`",
                f"- **可复用资产**：{asset}",
                f"- **后端与依赖**：{joined(chart['backends'] + chart['dependencies'])}",
                f"- **复用限制**：{joined(chart['reuse_constraints'])}",
                f"- **替代 / 补充图型**：{joined(chart['alternatives'] + chart['complements'])}",
                f"- **QA 规则**：{joined(chart['qa_rules'])}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def render_alias_index(registry: dict) -> str:
    categories = {category["id"]: category for category in registry["categories"]}
    lines = [
        "# 图型别名索引 / Chart Alias Index",
        "",
        "> 本文件由 `scripts/generate_chart_catalog.py` 生成；不要手工编辑。",
        "> 用户语言先路由到 canonical ID，再根据实现状态决定资产复用或新实现。",
        "",
        "## 同名异义",
        "",
        "| 术语 | 候选 canonical IDs | 路由规则 |",
        "|---|---|---|",
    ]
    for term in registry["ambiguous_terms"]:
        candidates = ", ".join(f"`{chart_id}`" for chart_id in term["candidate_ids"])
        lines.append(f"| {term['term']} | {candidates} | {term['resolution']} |")
    lines.extend(
        [
            "",
            "## 全部名称与别名",
            "",
            "| Canonical ID | 中文名 | English name | 其他别名 | 分类 | 状态 |",
            "|---|---|---|---|---|---|",
        ]
    )
    for chart in registry["charts"]:
        aliases = [*chart["aliases_zh"], *chart["aliases_en"]]
        category_names = "、".join(categories[item]["name_zh"] for item in chart["category_ids"])
        lines.append(
            f"| `{chart['id']}` | {chart['name_zh']} | {chart['name_en']} | "
            f"{joined(aliases)} | {category_names} | {STATUS_ZH[chart['implementation_status']]} |"
        )
    return "\n".join(lines).rstrip() + "\n"


def stats(registry: dict) -> dict:
    counts = status_counts(registry)
    return {
        "registry_version": registry["registry_version"],
        "categories": len(registry["categories"]),
        "canonical_charts": len(registry["charts"]),
        "source_memberships": registry["source_expectation"]["available_source_memberships"],
        "declared_source_memberships": registry["source_expectation"]["declared_memberships"],
        "source_complete": registry["source_expectation"]["source_complete"],
        **counts,
    }


def render_category_index(registry: dict) -> str:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for chart in registry["charts"]:
        for category_id in chart["category_ids"]:
            grouped[category_id].append(chart)
    lines = [
        "| 编号 | 分类 | 适用研究问题 | 图型数量 | 文档 |",
        "|---|---|---|---:|---|",
    ]
    for category in registry["categories"]:
        charts = grouped[category["id"]]
        # 分类摘要优先使用主分类记录，避免跨类复用图型稀释该分类的核心语义。
        tasks = sorted(
            {
                task
                for chart in charts
                if chart["primary_category_id"] == category["id"]
                for task in chart["information_tasks"]
            }
        )
        if not tasks:
            tasks = sorted({task for chart in charts for task in chart["information_tasks"]})
        lines.append(
            f"| {category['id']} | {category['name_zh']} / {category['name_en']} | "
            f"{'；'.join(tasks[:2])} | {len(charts)} | "
            f"[打开](chart-types/{category_filename(category)}) |"
        )
    return "\n".join(lines)


def render_readme_summary(registry: dict, english: bool) -> str:
    values = stats(registry)
    if english:
        source_note = (
            f"{values['source_memberships']} verifiable memberships; the declared 714-entry source list "
            "was not included in the supplied plan"
        )
        rows = [
            ("Taxonomy categories", f"{values['categories']}"),
            ("Canonical chart records", f"{values['canonical_charts']}"),
            ("Source memberships", source_note),
            ("Production templates", f"{values['production_template']}"),
            ("Reusable patterns", f"{values['reusable_pattern']}"),
            ("On-demand routes", f"{values['on_demand']}"),
        ]
        intro = (
            "The registry separates catalogue coverage from implementation status. "
            "Only production templates have reusable scripts, previews, and manifests."
        )
    else:
        source_note = (
            f"{values['source_memberships']} 条可验证归属；方案声明的 714 条原始清单未随文件提供"
        )
        rows = [
            ("分类体系", f"{values['categories']} 类"),
            ("规范化图型", f"{values['canonical_charts']} 个"),
            ("源分类归属", source_note),
            ("生产模板", f"{values['production_template']} 类"),
            ("可复用模式", f"{values['reusable_pattern']} 类"),
            ("按需实现", f"{values['on_demand']} 类"),
        ]
        intro = "注册表严格区分目录覆盖与实现状态；只有生产模板拥有可复用脚本、预览和 manifest。"
    lines = [intro, "", '<table width="100%" align="center">']
    for label, value in rows:
        lines.append(f"  <tr><td width=\"35%\"><strong>{label}</strong></td><td>{value}</td></tr>")
    lines.append("</table>")
    return "\n".join(lines)


def render_catalog_data(registry: dict) -> str:
    """Build a machine-readable catalogue without inventing previews for non-production charts."""
    categories = {category["id"]: category for category in registry["categories"]}
    charts = []
    for chart in registry["charts"]:
        preview = None
        if chart["implementation_status"] == "production_template":
            asset_dir = ROOT / chart["asset_path"]
            manifest = json.loads((asset_dir / "asset.yaml").read_text(encoding="utf-8"))
            preview = f"{chart['asset_path']}/{manifest['previews'][0]}"
        charts.append(
            {
                "id": chart["id"],
                "name_zh": chart["name_zh"],
                "name_en": chart["name_en"],
                "categories": [categories[item]["slug"] for item in chart["category_ids"]],
                "implementation_status": chart["implementation_status"],
                "preview": preview,
            }
        )
    document = {
        "registry_version": registry["registry_version"],
        "note": "Preview is non-null only for verified production templates.",
        "charts": charts,
    }
    return json.dumps(document, ensure_ascii=False, indent=2) + "\n"


def expected_outputs(registry: dict) -> dict[Path, str]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for chart in registry["charts"]:
        for category_id in chart["category_ids"]:
            grouped[category_id].append(chart)
    outputs: dict[Path, str] = {}
    for category in registry["categories"]:
        charts = sorted(grouped[category["id"]], key=lambda chart: chart["id"])
        outputs[CHART_TYPES_DIR / category_filename(category)] = render_category(category, charts)
    outputs[ALIAS_INDEX_PATH] = render_alias_index(registry)
    outputs[ROOT / "references" / "chart-registry-stats.json"] = (
        json.dumps(stats(registry), ensure_ascii=False, indent=2) + "\n"
    )
    outputs[ROOT / "assets" / "chart-catalog" / "catalog.json"] = render_catalog_data(registry)

    catalog = ROOT / "references" / "figure-type-catalog.md"
    outputs[catalog] = replace_generated_block(
        catalog.read_text(encoding="utf-8"), "chart-registry:category-index", render_category_index(registry)
    )
    for path, english in [(ROOT / "README.md", False), (ROOT / "README_EN.md", True)]:
        outputs[path] = replace_generated_block(
            path.read_text(encoding="utf-8"),
            "chart-registry:summary",
            render_readme_summary(registry, english),
        )
    return outputs


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    registry = load_registry()
    outputs = expected_outputs(registry)
    differences: list[str] = []
    for path, expected in outputs.items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != expected:
            differences.append(str(path.relative_to(ROOT)))
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(expected, encoding="utf-8")
    if args.check and differences:
        print("Generated catalog files are stale:")
        for path in differences:
            print(f"  - {path}")
        raise SystemExit(1)
    action = "checked" if args.check else "updated"
    print(f"Chart catalog {action}: {len(outputs)} files")


if __name__ == "__main__":
    main()
