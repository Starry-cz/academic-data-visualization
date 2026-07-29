#!/usr/bin/env python3
"""Weighted chord diagram for cross-domain relationships.

Input CSV columns: ``source``, ``target``, ``weight``.
Use ``--demo`` only to rebuild the bundled preview.
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Circle, PathPatch, Wedge
from matplotlib.path import Path as MplPath


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
from visual_qa import audit_figure


REQUIRED = {"source", "target", "weight"}
NODE_COLOURS = [
    "#4B7FA5",
    "#E38B4D",
    "#58A6A6",
    "#8B78B8",
    "#D86557",
    "#D6B34C",
    "#6F9D72",
    "#687487",
]
SEMANTIC_COLOR_ROLES = {
    "nodes": NODE_COLOURS,
    "links": "source-node colour with transparency",
    "labels": "#263746",
}


def apply_style() -> None:
    mpl.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "Helvetica", "Liberation Sans"],
            "font.size": 8,
            "axes.linewidth": 0.7,
            "pdf.fonttype": 42,
            "svg.fonttype": "none",
            "savefig.dpi": 600,
        }
    )


def demo_data() -> pd.DataFrame:
    edges = [
        ("Genomics", "Proteomics", 24),
        ("Genomics", "Clinical", 17),
        ("Genomics", "Microbiome", 11),
        ("Proteomics", "Metabolomics", 21),
        ("Proteomics", "Imaging", 8),
        ("Metabolomics", "Environment", 16),
        ("Metabolomics", "Clinical", 13),
        ("Imaging", "Clinical", 19),
        ("Imaging", "Outcomes", 12),
        ("Clinical", "Outcomes", 25),
        ("Environment", "Microbiome", 23),
        ("Environment", "Outcomes", 7),
        ("Microbiome", "Clinical", 15),
        ("Microbiome", "Outcomes", 10),
    ]
    return pd.DataFrame(edges, columns=["source", "target", "weight"])


def validate_data(data: pd.DataFrame) -> pd.DataFrame:
    missing = REQUIRED - set(data.columns)
    if missing:
        raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")
    frame = data.loc[:, ["source", "target", "weight"]].copy()
    frame["source"] = frame["source"].astype(str).str.strip()
    frame["target"] = frame["target"].astype(str).str.strip()
    frame["weight"] = pd.to_numeric(frame["weight"], errors="raise")
    if frame[["source", "target"]].eq("").any().any():
        raise ValueError("source and target labels must not be empty")
    if not np.isfinite(frame["weight"]).all() or (frame["weight"] <= 0).any():
        raise ValueError("weight must contain finite positive values")
    if frame["source"].eq(frame["target"]).any():
        raise ValueError("self-links are not supported by this template")
    nodes = list(dict.fromkeys([*frame["source"], *frame["target"]]))
    if not 3 <= len(nodes) <= 12:
        raise ValueError("This template supports three to twelve nodes")
    # 无向关系在绘图前聚合，避免重复边被误读为两个独立方向。
    frame["pair"] = frame.apply(lambda row: tuple(sorted((row["source"], row["target"]))), axis=1)
    grouped = frame.groupby("pair", sort=False, as_index=False)["weight"].sum()
    grouped[["source", "target"]] = pd.DataFrame(grouped["pair"].tolist(), index=grouped.index)
    return grouped[["source", "target", "weight"]]


def polar_point(angle: float, radius: float) -> np.ndarray:
    return np.array([radius * np.cos(angle), radius * np.sin(angle)])


def ribbon_patch(
    source_span: tuple[float, float],
    target_span: tuple[float, float],
    colour: str,
) -> PathPatch:
    s0, s1 = source_span
    t0, t1 = target_span
    p0, p1 = polar_point(s0, 0.82), polar_point(s1, 0.82)
    q0, q1 = polar_point(t0, 0.82), polar_point(t1, 0.82)
    control = 0.18
    vertices = [
        p0,
        p0 * control,
        q1 * control,
        q1,
        q0,
        q0 * control,
        p1 * control,
        p1,
        p0,
    ]
    codes = [
        MplPath.MOVETO,
        MplPath.CURVE4,
        MplPath.CURVE4,
        MplPath.CURVE4,
        MplPath.LINETO,
        MplPath.CURVE4,
        MplPath.CURVE4,
        MplPath.CURVE4,
        MplPath.CLOSEPOLY,
    ]
    return PathPatch(
        MplPath(vertices, codes),
        facecolor=colour,
        edgecolor=mpl.colors.to_rgba(colour, 0.72),
        linewidth=0.35,
        alpha=0.52,
    )


def plot_chord(data: pd.DataFrame) -> plt.Figure:
    frame = validate_data(data)
    nodes = list(dict.fromkeys([*frame["source"], *frame["target"]]))
    totals = defaultdict(float)
    for row in frame.itertuples(index=False):
        totals[row.source] += row.weight
        totals[row.target] += row.weight

    gap = np.deg2rad(3.2)
    available = 2 * np.pi - gap * len(nodes)
    total_weight = sum(totals.values())
    sectors: dict[str, tuple[float, float]] = {}
    cursor = np.deg2rad(92)
    for node in nodes:
        span = available * totals[node] / total_weight
        sectors[node] = (cursor, cursor + span)
        cursor += span + gap

    allocation_cursor = {node: sectors[node][0] for node in nodes}
    spans: list[tuple[tuple[float, float], tuple[float, float], str, float]] = []
    colour_map = {node: NODE_COLOURS[index % len(NODE_COLOURS)] for index, node in enumerate(nodes)}
    for row in frame.sort_values("weight").itertuples(index=False):
        source_width = (sectors[row.source][1] - sectors[row.source][0]) * row.weight / totals[row.source]
        target_width = (sectors[row.target][1] - sectors[row.target][0]) * row.weight / totals[row.target]
        source_span = (allocation_cursor[row.source], allocation_cursor[row.source] + source_width)
        target_span = (allocation_cursor[row.target], allocation_cursor[row.target] + target_width)
        allocation_cursor[row.source] += source_width
        allocation_cursor[row.target] += target_width
        spans.append((source_span, target_span, colour_map[row.source], row.weight))

    fig, ax = plt.subplots(figsize=(7.2, 6.2))
    fig.subplots_adjust(left=0.03, right=0.97, bottom=0.08, top=0.90)
    ax.set_aspect("equal")
    ax.axis("off")

    for source_span, target_span, colour, _ in spans:
        ax.add_patch(ribbon_patch(source_span, target_span, colour))

    for node in nodes:
        start, end = sectors[node]
        ax.add_patch(
            Wedge(
                (0, 0),
                1.0,
                np.rad2deg(start),
                np.rad2deg(end),
                width=0.14,
                facecolor=colour_map[node],
                edgecolor="white",
                linewidth=1.0,
            )
        )
        middle = (start + end) / 2
        x, y = polar_point(middle, 1.10)
        horizontal = "left" if np.cos(middle) >= 0 else "right"
        ax.text(
            x,
            y,
            node,
            ha=horizontal,
            va="center",
            fontsize=8,
            fontweight="bold",
            color="#263746",
        )

    ax.add_patch(Circle((0, 0), 0.22, facecolor="white", edgecolor="#D7DEE7", linewidth=0.7, zorder=5))
    ax.text(
        0,
        0.045,
        "Cross-domain",
        ha="center",
        va="center",
        fontsize=12,
        fontweight="bold",
        color="#263746",
        zorder=6,
    )
    ax.text(0, -0.035, "evidence links", ha="center", va="center", fontsize=9, color="#687487", zorder=6)
    ax.set_xlim(-1.34, 1.34)
    ax.set_ylim(-1.22, 1.22)
    ax.set_title("Weighted chord diagram", fontsize=12, pad=8)
    fig.text(
        0.5,
        0.022,
        "Ribbon width encodes association weight; use the source matrix for exact values.",
        ha="center",
        fontsize=6.5,
        color="#5F6772",
    )
    return fig


def save_figure(fig: plt.Figure, output: Path, export_tiff: bool) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    audit_figure(fig, output.stem)
    svg_path = output.with_suffix(".svg")
    fig.savefig(svg_path, bbox_inches="tight")
    # Matplotlib 会在多行 SVG 路径末尾保留空格；规范化后避免版本库出现空白错误。
    svg_text = svg_path.read_text(encoding="utf-8")
    svg_path.write_text(
        "\n".join(line.rstrip() for line in svg_text.splitlines()) + "\n",
        encoding="utf-8",
    )
    fig.savefig(output.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(output.with_suffix(".png"), dpi=600, bbox_inches="tight")
    if export_tiff:
        fig.savefig(output.with_suffix(".tiff"), dpi=600, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--input", type=Path, help="CSV with source,target,weight")
    source.add_argument("--demo", action="store_true", help="Render deterministic preview data")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("chord_diagram"),
        help="Output prefix without extension",
    )
    parser.add_argument("--tiff", action="store_true", help="Also export a 600 dpi TIFF submission raster")
    args = parser.parse_args()
    apply_style()
    data = demo_data() if args.demo else pd.read_csv(args.input)
    save_figure(plot_chord(data), args.output, args.tiff)


if __name__ == "__main__":
    main()
