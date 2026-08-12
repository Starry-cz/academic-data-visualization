#!/usr/bin/env python3
"""Audit the registered palette library for near-duplicate categorical colours."""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

from palette_lib import THEMES


# CIE76 ΔE < 10 专门拦截紧凑科研面板中会坍缩为同一视觉角色的分类色，
# 不把仅色相相近、但明度或饱和度仍可区分的主题误删。
MIN_CATEGORICAL_DELTA_E = 10.0
MERGE_CANDIDATE_DELTA_E = 10.0


@dataclass(frozen=True)
class PaletteFinding:
    """One actionable categorical-colour or whole-theme similarity finding."""

    check_id: str
    first: str
    second: str
    delta_e: float


def _srgb_to_linear(value: float) -> float:
    return value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4


def _hex_to_lab(hex_colour: str) -> tuple[float, float, float]:
    """Convert an opaque #RRGGBB colour to CIE Lab (D65) without extra packages."""
    red, green, blue = (
        _srgb_to_linear(int(hex_colour[index : index + 2], 16) / 255.0)
        for index in (1, 3, 5)
    )
    # sRGB D65 -> XYZ, then normalise against the D65 reference white.
    x = (red * 0.4124 + green * 0.3576 + blue * 0.1805) / 0.95047
    y = red * 0.2126 + green * 0.7152 + blue * 0.0722
    z = (red * 0.0193 + green * 0.1192 + blue * 0.9505) / 1.08883

    def transform(value: float) -> float:
        return value ** (1 / 3) if value > 0.008856 else 7.787 * value + 16 / 116

    fx, fy, fz = (transform(value) for value in (x, y, z))
    return 116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)


def delta_e(first: str, second: str) -> float:
    """Return perceptual CIE76 distance for two registered hex colours."""
    return math.dist(_hex_to_lab(first), _hex_to_lab(second))


def _symmetric_nearest_distance(first: list[str], second: list[str]) -> float:
    """Score whether two categorical palettes describe the same visual role set."""
    first_to_second = sum(min(delta_e(a, b) for b in second) for a in first) / len(first)
    second_to_first = sum(min(delta_e(b, a) for a in first) for b in second) / len(second)
    return (first_to_second + second_to_first) / 2


def audit_palette_library() -> tuple[list[PaletteFinding], list[PaletteFinding]]:
    """Return in-theme clashes and whole-theme merge candidates from the registry."""
    colour_findings: list[PaletteFinding] = []
    theme_findings: list[PaletteFinding] = []
    items = list(THEMES.items())

    for theme_id, theme in items:
        colours = list(theme["categorical"])
        for index, first in enumerate(colours):
            for second in colours[index + 1 :]:
                distance = delta_e(first, second)
                if distance < MIN_CATEGORICAL_DELTA_E:
                    colour_findings.append(PaletteFinding("PAL-1", f"{theme_id}:{first}", f"{theme_id}:{second}", distance))

    for index, (first_id, first_theme) in enumerate(items):
        first_colours = list(first_theme["categorical"])
        for second_id, second_theme in items[index + 1 :]:
            distance = _symmetric_nearest_distance(first_colours, list(second_theme["categorical"]))
            if distance < MERGE_CANDIDATE_DELTA_E:
                theme_findings.append(PaletteFinding("PAL-2", first_id, second_id, distance))
    return colour_findings, theme_findings


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Exit non-zero when a merge or cleanup is required")
    args = parser.parse_args()
    colour_findings, theme_findings = audit_palette_library()
    for finding in [*colour_findings, *theme_findings]:
        print(f"{finding.check_id} {finding.first} <> {finding.second}: ΔE={finding.delta_e:.2f}")
    if not colour_findings and not theme_findings:
        print(f"Palette library: PASS ({len(THEMES)} distinct themes)")
    if args.check and (colour_findings or theme_findings):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
