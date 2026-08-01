#!/usr/bin/env python3
"""Query the lightweight registry without loading hundreds of records into model context."""

from __future__ import annotations

import argparse
import json
import re

from chart_registry_lib import load_registry, normalize_alias, resolve_chart_name


def chart_summary(chart: dict) -> dict:
    return {
        "id": chart["id"],
        "name_zh": chart["name_zh"],
        "name_en": chart["name_en"],
        "information_tasks": chart["information_tasks"],
        "implementation_status": chart["implementation_status"],
        "verification_status": chart["verification_status"],
        "asset_path": chart["asset_path"],
        "required_variables": chart["required_variables"],
        "suitable_when": chart["suitable_when"],
        "avoid_when": chart["avoid_when"],
        "publication_risks": chart["publication_risks"],
    }


def query_tokens(question: str) -> set[str]:
    """Tokenise English words and overlapping Chinese phrases for lightweight routing."""
    tokens = set(re.findall(r"[a-z0-9]+", question.casefold()))
    for sequence in re.findall(r"[\u4e00-\u9fff]+", question):
        # 中文没有空格分词；2–4 字滑窗可以识别“效应量”“置信区间”等图型语义。
        for width in range(2, min(4, len(sequence)) + 1):
            tokens.update(sequence[index:index + width] for index in range(len(sequence) - width + 1))
    return tokens


def question_score(chart: dict, question: str) -> int:
    tokens = query_tokens(question)
    text = " ".join(
        [
            chart["id"], chart["name_zh"], chart["name_en"],
            *chart["aliases_zh"], *chart["aliases_en"], *chart["information_tasks"],
            *chart["research_questions"], *chart["suitable_when"],
        ]
    ).casefold()
    return sum(3 if token in normalize_alias(chart["name_zh"] + chart["name_en"]) else 1 for token in tokens if token in text)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--id")
    mode.add_argument("--name")
    mode.add_argument("--question")
    mode.add_argument("--status", choices=["production_verified", "demo_runnable", "legacy_example", "pattern", "none", "deprecated"])
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--full", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    registry = load_registry()
    by_id = {chart["id"]: chart for chart in registry["charts"]}
    charts: list[dict]
    if args.id:
        charts = [by_id[args.id]] if args.id in by_id else []
    elif args.name:
        charts = [by_id[chart_id] for chart_id in resolve_chart_name(registry, args.name)]
    elif args.status:
        charts = [chart for chart in registry["charts"] if chart["implementation_status"] == args.status]
    else:
        scored = [(question_score(chart, args.question), chart) for chart in registry["charts"]]
        charts = [chart for score, chart in sorted(scored, key=lambda item: (-item[0], item[1]["id"])) if score > 0]
    charts = charts[: args.limit]
    payload = charts if args.full else [chart_summary(chart) for chart in charts]
    print(json.dumps({"count": len(payload), "charts": payload}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
