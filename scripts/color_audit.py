#!/usr/bin/env python3
"""Inspect actual SVG paint usage for background contrast and grayscale risks."""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


HEX_RE = re.compile(r"^#([0-9a-f]{3}|[0-9a-f]{6}|[0-9a-f]{8})$", re.IGNORECASE)
RGB_RE = re.compile(r"^rgba?\(([^)]+)\)$", re.IGNORECASE)
NAMED_COLOURS = {
    "black": "#000000",
    "white": "#FFFFFF",
    "gray": "#808080",
    "grey": "#808080",
    "red": "#FF0000",
    "green": "#008000",
    "blue": "#0000FF",
}


@dataclass(frozen=True)
class ColourFinding:
    check_id: str
    pass_: bool
    severity: str
    detail: str


@dataclass(frozen=True)
class PaintSample:
    element_id: str
    tag: str
    role: str
    channel: str
    raw_hex: str
    composited_hex: str
    opacity: float
    contrast: float


@dataclass(frozen=True)
class SvgColourAnalysis:
    background_hex: str | None
    paints: tuple[PaintSample, ...]
    unsupported_paints: tuple[str, ...]
    embedded_images: int


def _style_map(value: str | None) -> dict[str, str]:
    if not value:
        return {}
    result: dict[str, str] = {}
    for declaration in value.split(";"):
        if ":" not in declaration:
            continue
        key, raw_value = declaration.split(":", 1)
        result[key.strip().lower()] = raw_value.strip()
    return result


def _number(value: str | None, default: float = 1.0) -> float:
    if value is None:
        return default
    parsed = float(value.strip())
    return max(0.0, min(1.0, parsed))


def _normalise_colour(value: str | None) -> tuple[str, float] | None:
    if not value:
        return None
    token = value.strip()
    lowered = token.lower()
    if lowered in {"none", "transparent", "currentcolor"} or lowered.startswith("url("):
        return None
    token = NAMED_COLOURS.get(lowered, token)
    match = HEX_RE.fullmatch(token)
    if match:
        body = match.group(1)
        if len(body) == 3:
            body = "".join(character * 2 for character in body)
        alpha = 1.0
        if len(body) == 8:
            alpha = int(body[6:8], 16) / 255.0
            body = body[:6]
        return f"#{body.upper()}", alpha
    rgb_match = RGB_RE.fullmatch(token)
    if not rgb_match:
        return None
    parts = [part.strip() for part in rgb_match.group(1).split(",")]
    if len(parts) not in {3, 4}:
        return None
    channels: list[int] = []
    for part in parts[:3]:
        if part.endswith("%"):
            channels.append(round(float(part[:-1]) * 2.55))
        else:
            channels.append(round(float(part)))
    if any(channel < 0 or channel > 255 for channel in channels):
        return None
    alpha = _number(parts[3]) if len(parts) == 4 else 1.0
    return "#{:02X}{:02X}{:02X}".format(*channels), alpha


def _rgb(hex_colour: str) -> tuple[float, float, float]:
    return tuple(int(hex_colour[index:index + 2], 16) / 255.0 for index in (1, 3, 5))  # type: ignore[return-value]


def _hex(rgb: Iterable[float]) -> str:
    values = [round(max(0.0, min(1.0, channel)) * 255) for channel in rgb]
    return "#{:02X}{:02X}{:02X}".format(*values)


def composite_colour(foreground: str, background: str, alpha: float) -> str:
    foreground_rgb = _rgb(foreground)
    background_rgb = _rgb(background)
    return _hex(
        foreground_channel * alpha + background_channel * (1.0 - alpha)
        for foreground_channel, background_channel in zip(foreground_rgb, background_rgb, strict=True)
    )


def relative_luminance(hex_colour: str) -> float:
    linear: list[float] = []
    for channel in _rgb(hex_colour):
        linear.append(channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4)
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast_ratio(first: str, second: str) -> float:
    first_luminance = relative_luminance(first)
    second_luminance = relative_luminance(second)
    lighter, darker = max(first_luminance, second_luminance), min(first_luminance, second_luminance)
    return (lighter + 0.05) / (darker + 0.05)


def _role_for(ancestry_ids: tuple[str, ...], tag: str) -> str:
    if tag == "text":
        return "text"
    if any(identifier in {"patch_1", "patch_2"} for identifier in ancestry_ids):
        return "background"
    if any(identifier.startswith("FillBetweenPolyCollection") for identifier in ancestry_ids):
        return "uncertainty"
    if any(identifier.startswith("matplotlib.axis") for identifier in ancestry_ids):
        return "structural"
    if any(identifier.startswith("legend") for identifier in ancestry_ids):
        return "legend"
    return "graphical"


def _paint_value(node: ET.Element, style: dict[str, str], channel: str) -> str | None:
    return style.get(channel, node.get(channel))


def _discover_background(root: ET.Element) -> str | None:
    """读取 Matplotlib 明确导出的画布底色；没有明确底色时不猜测。"""
    discovered: str | None = None

    def visit(node: ET.Element, ancestry_ids: tuple[str, ...], in_defs: bool) -> None:
        nonlocal discovered
        if discovered is not None:
            return
        tag = node.tag.rsplit("}", 1)[-1]
        next_ids = ancestry_ids + ((node.get("id") or ""),)
        next_in_defs = in_defs or tag == "defs"
        if not next_in_defs and tag in {"path", "rect"} and "patch_1" in next_ids:
            style = _style_map(node.get("style"))
            parsed = _normalise_colour(_paint_value(node, style, "fill"))
            if parsed and parsed[1] == 1.0:
                discovered = parsed[0]
                return
        for child in node:
            visit(child, next_ids, next_in_defs)

    visit(root, (), False)
    return discovered


def analyse_svg_colours(path: Path) -> SvgColourAnalysis:
    root = ET.parse(path).getroot()
    background = _discover_background(root)
    if background is None:
        return SvgColourAnalysis(None, (), (), 0)

    samples: list[PaintSample] = []
    unsupported: set[str] = set()
    embedded_images = 0

    def visit(
        node: ET.Element,
        ancestry_ids: tuple[str, ...],
        inherited: dict[str, str],
        inherited_opacity: float,
        in_defs: bool,
    ) -> None:
        nonlocal embedded_images
        tag = node.tag.rsplit("}", 1)[-1]
        node_id = node.get("id") or ""
        next_ids = ancestry_ids + (node_id,)
        next_in_defs = in_defs or tag == "defs"
        style = dict(inherited)
        style.update(_style_map(node.get("style")))
        for property_name in ("fill", "stroke", "fill-opacity", "stroke-opacity", "visibility", "display"):
            if node.get(property_name) is not None:
                style[property_name] = str(node.get(property_name))
        opacity = inherited_opacity * _number(style.get("opacity"), 1.0)
        hidden = style.get("visibility") == "hidden" or style.get("display") == "none" or opacity == 0.0

        if not next_in_defs and not hidden:
            if tag == "image":
                embedded_images += 1
            role = _role_for(next_ids, tag)
            channels = ("fill",) if tag == "text" else ("fill", "stroke")
            for channel in channels:
                raw_value = _paint_value(node, style, channel)
                if tag == "text" and channel == "fill" and raw_value is None:
                    raw_value = "#000000"
                if raw_value and (raw_value.strip().lower().startswith("url(") or raw_value.strip().lower() == "currentcolor"):
                    unsupported.add(raw_value.strip())
                    continue
                parsed = _normalise_colour(raw_value)
                if parsed is None:
                    continue
                raw_hex, embedded_alpha = parsed
                channel_opacity = _number(style.get(f"{channel}-opacity"), 1.0)
                effective_opacity = opacity * channel_opacity * embedded_alpha
                if effective_opacity <= 0.01:
                    continue
                composited = composite_colour(raw_hex, background, effective_opacity)
                samples.append(
                    PaintSample(
                        element_id=node_id,
                        tag=tag,
                        role=role,
                        channel=channel,
                        raw_hex=raw_hex,
                        composited_hex=composited,
                        opacity=effective_opacity,
                        contrast=contrast_ratio(composited, background),
                    )
                )

        child_inherited = {
            key: value
            for key, value in style.items()
            if key in {"fill", "stroke", "fill-opacity", "stroke-opacity", "visibility", "display"}
        }
        for child in node:
            visit(child, next_ids, child_inherited, opacity, next_in_defs)

    visit(root, (), {}, 1.0, False)
    return SvgColourAnalysis(background, tuple(samples), tuple(sorted(unsupported)), embedded_images)


def _aggregate(samples: Iterable[PaintSample], limit: int = 6) -> str:
    counter = Counter(
        (sample.raw_hex, sample.composited_hex, round(sample.opacity, 2), round(sample.contrast, 2))
        for sample in samples
    )
    fragments = []
    for (raw_hex, composited_hex, opacity, ratio), count in counter.most_common(limit):
        fragments.append(f"{raw_hex}->{composited_hex} alpha={opacity:.2f} CR={ratio:.2f}:1 x{count}")
    return "; ".join(fragments)


def _severity(has_issue: bool, strict: bool) -> tuple[bool, str]:
    if not has_issue:
        return True, "PASS"
    return False, "FAIL" if strict else "WARN"


def audit_svg_colours(path: Path, categorical: list[str], strict: bool = False) -> list[ColourFinding]:
    analysis = analyse_svg_colours(path)
    if analysis.background_hex is None:
        return [
            ColourFinding("COLOR-2", False, "FAIL" if strict else "WARN", "SVG has no explicit canvas background; rendered contrast was not inferred"),
            ColourFinding("A11Y-3", False, "FAIL" if strict else "WARN", "SVG text contrast could not be evaluated without an explicit background"),
            ColourFinding("A11Y-4", False, "WARN", "Grayscale separation requires an explicit background and rendered colours"),
        ]

    background = analysis.background_hex
    # 与画布同色的文字通常位于热图等局部深色区域；没有几何相交分析时只提示人工复核。
    text_local_background = [
        sample
        for sample in analysis.paints
        if sample.role == "text" and sample.raw_hex == background and sample.contrast < 4.5
    ]
    text_low = [
        sample
        for sample in analysis.paints
        if sample.role == "text" and sample.raw_hex != background and sample.contrast < 4.5
    ]
    text_pass, text_severity = _severity(bool(text_low), strict)
    text_detail = (
        f"Rendered text reaches 4.5:1 against {background}"
        if not text_low
        else f"Rendered text below 4.5:1 against {background}: {_aggregate(text_low)}"
    )

    graphical_roles = {"graphical", "legend"}
    graphical_low = [
        sample
        for sample in analysis.paints
        if sample.role in graphical_roles
        and sample.raw_hex != background
        and sample.contrast < 3.0
    ]
    # 主线和较实的填充属于关键证据；更低透明度的点或带先作为上下文警告，避免误杀降噪层。
    graphical_essential = [
        sample
        for sample in graphical_low
        if (sample.channel == "stroke" and sample.opacity >= 0.75)
        or (sample.channel == "fill" and sample.opacity >= 0.60)
    ]
    graphical_context = [sample for sample in graphical_low if sample not in graphical_essential]
    graphical_pass, graphical_severity = _severity(bool(graphical_essential), strict)
    graphical_detail = (
        f"Rendered essential graphical objects reach 3:1 against {background}"
        if not graphical_essential
        else f"Rendered essential graphical objects below 3:1 after opacity compositing: {_aggregate(graphical_essential)}"
    )

    contextual_low = [
        sample
        for sample in analysis.paints
        if sample.role == "uncertainty" and sample.raw_hex != background and sample.contrast < 3.0
    ]
    contextual_detail = (
        "No low-contrast uncertainty band was detected"
        if not contextual_low
        else "Low-contrast uncertainty bands are allowed only as non-essential context: " + _aggregate(contextual_low)
    )

    used_categorical = sorted(
        {
            sample.raw_hex
            for sample in analysis.paints
            if sample.role in {"graphical", "legend", "uncertainty"}
            and sample.raw_hex in {colour.upper() for colour in categorical if HEX_RE.fullmatch(colour)}
        }
    )
    close_pairs: list[tuple[str, str, float]] = []
    for index, first in enumerate(used_categorical):
        for second in used_categorical[index + 1:]:
            ratio = contrast_ratio(first, second)
            if ratio < 1.2:
                close_pairs.append((first, second, ratio))
    grayscale_detail = (
        "Rendered categorical colours retain basic luminance separation"
        if not close_pairs
        else "Categorical colours with similar grayscale luminance require line/shape/label redundancy: "
        + "; ".join(f"{first}/{second} CR={ratio:.2f}:1" for first, second, ratio in close_pairs[:8])
    )

    findings = [
        ColourFinding("COLOR-2", graphical_pass, graphical_severity, graphical_detail),
        ColourFinding("A11Y-3", text_pass, text_severity, text_detail),
        ColourFinding("COLOR-3", not contextual_low, "PASS" if not contextual_low else "WARN", contextual_detail),
        ColourFinding(
            "COLOR-5",
            not graphical_context,
            "PASS" if not graphical_context else "WARN",
            "No low-contrast subdued graphical context was detected"
            if not graphical_context
            else "Subdued graphical marks need visual confirmation that they are non-essential: " + _aggregate(graphical_context),
        ),
        ColourFinding("A11Y-4", not close_pairs, "PASS" if not close_pairs else "WARN", grayscale_detail),
        ColourFinding(
            "A11Y-5",
            not text_local_background,
            "PASS" if not text_local_background else "WARN",
            "No text relies on an unresolved local background"
            if not text_local_background
            else "Text matching the canvas colour may rely on a local dark fill; inspect cell-level contrast: "
            + _aggregate(text_local_background),
        ),
    ]
    if analysis.unsupported_paints or analysis.embedded_images:
        unresolved_parts: list[str] = []
        if analysis.unsupported_paints:
            unresolved_parts.append("paint expressions: " + ", ".join(analysis.unsupported_paints[:6]))
        if analysis.embedded_images:
            unresolved_parts.append(f"embedded raster/image layers: {analysis.embedded_images}")
        findings.append(
            ColourFinding(
                "COLOR-4",
                False,
                "WARN",
                "SVG contains colour-bearing content that needs visual inspection: " + "; ".join(unresolved_parts),
            )
        )
    else:
        findings.append(ColourFinding("COLOR-4", True, "PASS", "All rendered solid paints were parsed for colour QA"))
    return findings
