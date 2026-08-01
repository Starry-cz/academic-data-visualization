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
    "production_verified": "生产已验证",
    "demo_runnable": "演示可运行",
    "legacy_example": "历史示例",
    "pattern": "可复用模式",
    "none": "知识登记",
    "deprecated": "已弃用",
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
        "2. 只有 `生产已验证` 才能直接进入资产运行流程；历史示例不能冒充可复现模板。",
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
    origin_counts = {
        origin: sum(chart["registry_origin"] == origin for chart in registry["charts"])
        for origin in ("source_taxonomy", "repository_extension")
    }
    return {
        "registry_version": registry["registry_version"],
        "categories": len(registry["categories"]),
        "canonical_charts": len(registry["charts"]),
        "source_memberships": registry["source_expectation"]["available_source_memberships"],
        "declared_source_memberships": registry["source_expectation"]["declared_memberships"],
        "source_complete": registry["source_expectation"]["source_complete"],
        **origin_counts,
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
        rows = [
            (
                "Unsure which chart to use",
                "Compare defensible candidates from the research question and real data structure",
                "Chart rationale and risk notes",
            ),
            (
                "Have data and need a figure",
                f"Reuse one of {values['production_verified']} release-verified templates when suitable; "
                "otherwise build for the actual data",
                "Python / R script and editable vector master",
            ),
            (
                "Need a coherent multipanel figure",
                "Unify physical size, typography, colour, legends, and panel hierarchy",
                "Journal-sized main or supplementary figure",
            ),
            (
                "Preparing a submission",
                "Run anti-pattern, code/export, scientific-logic, and final-render checks",
                "RGB and grayscale proofs plus a QA report",
            ),
            (
                "Need a keynote or product-launch chart",
                "Derive a 16:9 distant-reading view from the same analysis while preserving "
                "baselines, uncertainty, and source",
                "SVG/PDF, 1080p/4K proofs, and alt text",
            ),
            (
                "Need a specialist chart",
                "Use a genuine domain implementation instead of a generic visual look-alike",
                "Dependencies, limitations, and alternatives",
            ),
        ]
        intro = (
            "The Skill turns a research question, data structure, and delivery constraints into "
            "a defensible figure workflow; you do not need to choose from a long list of chart names."
        )
        footer = (
            f"Coverage spans {values['categories']} research-task families, including comparison, "
            "trend, distribution, association, ordination, model evaluation, medicine, bioinformatics, "
            "and geospatial analysis. Browse the "
            "[chart catalogue](references/figure-type-catalog.md) or "
            "[verified production assets](references/directory-map.md) when you need the full index."
        )
    else:
        rows = [
            (
                "不知道该选什么图",
                "根据研究问题与真实数据结构比较可辩护的候选图型",
                "选图理由与风险提示",
            ),
            (
                "已有数据，需要尽快成图",
                f"适合时复用 {values['production_verified']} 个发布级验证模板；不匹配时按真实数据实现",
                "Python / R 脚本与可编辑矢量主文件",
            ),
            (
                "需要统一多面板或旧图",
                "统一物理尺寸、字体、配色、图例与面板层级",
                "符合期刊尺寸的主图或补充图",
            ),
            (
                "正在准备投稿",
                "依次检查反模式、代码与导出、科学逻辑和最终渲染",
                "RGB、灰度校样与 QA 报告",
            ),
            (
                "需要演讲或产品发布数据图",
                "从同一分析结果派生 16:9 远距阅读版本，保留基线、不确定性与来源",
                "SVG/PDF、1080p/4K 校样与替代文本",
            ),
            (
                "需要专业领域图型",
                "使用真实专业实现，不用外形相似的普通图冒充",
                "依赖、限制与替代方案说明",
            ),
        ]
        intro = (
            "Skill 把研究问题、数据结构和交付约束转换成一条可执行、可审查的成图路径；"
            "你不需要先从长长的图名清单里自行选择。"
        )
        footer = (
            f"能力覆盖比较、趋势、分布、关联、降维、模型评估、医学、生物信息和空间分析等 "
            f"{values['categories']} 类研究任务。需要完整索引时，可查看"
            "[图型目录](references/figure-type-catalog.md)或"
            "[真实生产资产](references/directory-map.md)。"
        )
    lines = [intro, "", '<table width="100%" align="center">']
    if english:
        lines.append(
            '  <tr><th width="28%">Your situation</th><th width="44%">What the Skill does</th>'
            '<th width="28%">What you receive</th></tr>'
        )
    else:
        lines.append(
            '  <tr><th width="28%">你的情况</th><th width="44%">Skill 会怎么做</th>'
            '<th width="28%">你会得到什么</th></tr>'
        )
    for index, (situation, action, outcome) in enumerate(rows):
        spacer = (
            '<img src="assets/readme/table-full-width-spacer.svg" '
            'width="800" height="1" align="right" alt="">'
            if index == 0
            else ""
        )
        lines.append(
            f"  <tr><td width=\"28%\"><strong>{situation}</strong></td>"
            f"<td width=\"44%\">{spacer}{action}</td>"
            f"<td width=\"28%\">{outcome}</td></tr>"
        )
    lines.extend(["</table>", "", footer])
    return "\n".join(lines)


def render_catalog_data(registry: dict) -> str:
    """Build a machine-readable catalogue without inventing previews for non-production charts."""
    categories = {category["id"]: category for category in registry["categories"]}
    charts = []
    for chart in registry["charts"]:
        preview = None
        if chart["implementation_status"] == "production_verified":
            asset_dir = ROOT / chart["asset_path"]
            manifest = json.loads((asset_dir / "asset.yaml").read_text(encoding="utf-8"))
            preview = f"{chart['asset_path']}/{manifest['outputs']['previews'][0]}"
        charts.append(
            {
                "id": chart["id"],
                "name_zh": chart["name_zh"],
                "name_en": chart["name_en"],
                "categories": [categories[item]["slug"] for item in chart["category_ids"]],
                "implementation_status": chart["implementation_status"],
                "registry_origin": chart["registry_origin"],
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
    expected_category_paths = {
        path for path in outputs if path.parent == CHART_TYPES_DIR
    }
    stale_category_paths = set(CHART_TYPES_DIR.glob("*.md")) - expected_category_paths
    differences: list[str] = []
    for path in sorted(stale_category_paths):
        differences.append(str(path.relative_to(ROOT)))
        if not args.check:
            # 分类文档完全由注册表生成；类别重命名后删除失效文件。
            path.unlink()
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
