#!/usr/bin/env python3
"""Load approved colour themes from the repository's single source of truth."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PALETTE_LIBRARY_PATH = ROOT / "references" / "palette-library.json"

# 画廊中的图彼此独立，因此按证据类型分配已批准主题；同一张图内部仍保持语义映射一致。
DEFAULT_THEME_BY_CHART = {
    "grouped-bar-chart": "pastel-harmony",
    "line-chart": "coastal-sunset",
    "violin-plot": "pastel-harmony",
    "correlation-matrix": "pastel-harmony",
    "pca-biplot": "pastel-omics",
    "forest-plot": "literature-clinical",
    "roc-curve": "literature-clinical",
    "precision-recall-curve": "literature-clinical",
    "calibration-curve": "literature-clinical",
    "volcano-plot": "blue-red-signal",
    "kaplan-meier-curve": "literature-clinical",
    "sankey-diagram": "coastal-sunset",
}


def load_palette_library() -> dict[str, dict[str, Any]]:
    """Read and strictly validate the tracked palette registry without fallback colours."""
    payload = json.loads(PALETTE_LIBRARY_PATH.read_text(encoding="utf-8"))
    themes = payload.get("themes")
    if payload.get("schema_version") != 1 or not isinstance(themes, list):
        raise ValueError(f"Invalid palette library schema: {PALETTE_LIBRARY_PATH}")
    result: dict[str, dict[str, Any]] = {}
    required = {"id", "categorical", "sequential", "diverging", "accent"}
    for theme in themes:
        if not isinstance(theme, dict) or not required.issubset(theme):
            raise ValueError("Every palette theme must define id, categorical, sequential, diverging, and accent")
        theme_id = str(theme["id"])
        if theme_id in result:
            raise ValueError(f"Duplicate palette theme id: {theme_id}")
        for role in ("categorical", "sequential", "diverging"):
            colours = theme[role]
            if not isinstance(colours, list) or len(colours) < 3 or not all(isinstance(value, str) and value.startswith("#") for value in colours):
                raise ValueError(f"Theme {theme_id!r} has an invalid {role} palette")
        if not isinstance(theme["accent"], str) or not theme["accent"].startswith("#"):
            raise ValueError(f"Theme {theme_id!r} has an invalid accent colour")
        result[theme_id] = theme
    if set(DEFAULT_THEME_BY_CHART.values()) - set(result):
        raise ValueError("Default chart routing references an unknown palette theme")
    return result


THEMES = load_palette_library()
THEME_IDS = tuple(sorted(THEMES))


def resolve_theme(chart_id: str, requested: str) -> str:
    """Resolve `auto` to the approved chart-specific route; reject unknown themes."""
    theme_id = DEFAULT_THEME_BY_CHART[chart_id] if requested == "auto" else requested
    if theme_id not in THEMES:
        raise ValueError(f"Unknown palette theme: {theme_id}")
    return theme_id
