#!/usr/bin/env python3
"""Publication-ready bubble scatter.

Input CSV columns: x, y, size, group, label. Bubble area encodes ``size``;
colour encodes ``group``. Use ``--demo`` only to rebuild the bundled preview.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
from visual_qa import audit_figure


PALETTE = ["#EEA599", "#FAC795", "#E3EDE0", "#ABD3E1", "#92B4C8", "#6B7280"]
MARKERS = ["o", "s", "^", "D", "P", "X"]
REQUIRED = {"x", "y", "size", "group", "label"}


def apply_style() -> None:
    mpl.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "Helvetica", "Liberation Sans"],
            "font.size": 8,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.linewidth": 0.7,
            "xtick.direction": "out",
            "ytick.direction": "out",
            "legend.frameon": False,
            "pdf.fonttype": 42,
            "svg.fonttype": "none",
            "savefig.dpi": 450,
        }
    )


def demo_data() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "x": [12, 20, 27, 34, 41, 49, 55, 63, 70, 78, 86, 92],
            "y": [22, 47, 35, 68, 51, 28, 59, 43, 76, 33, 62, 85],
            "size": [18, 35, 14, 42, 25, 48, 29, 21, 52, 17, 38, 31],
            "group": ["A", "B", "A", "C", "B", "C", "A", "B", "C", "A", "B", "C"],
            "label": [f"S{i:02d}" for i in range(1, 13)],
        }
    )


def validate_data(data: pd.DataFrame) -> pd.DataFrame:
    missing = REQUIRED - set(data.columns)
    if missing:
        raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")
    frame = data.copy()
    numeric = frame[["x", "y", "size"]].apply(pd.to_numeric, errors="raise")
    if not np.isfinite(numeric.to_numpy()).all():
        raise ValueError("x, y, and size must be finite")
    if (numeric["size"] <= 0).any() or numeric["size"].nunique() < 2:
        raise ValueError("size must contain at least two distinct positive values")
    frame[["x", "y", "size"]] = numeric
    return frame


def scale_area(values: pd.Series, minimum: float = 35, maximum: float = 360) -> np.ndarray:
    """将数值映射到圆面积；平方根只用于视觉面积缩放，不改变数据值。"""
    roots = np.sqrt(values.to_numpy(dtype=float))
    return minimum + (roots - roots.min()) / (roots.max() - roots.min()) * (maximum - minimum)


def plot_bubble_scatter(data: pd.DataFrame) -> plt.Figure:
    frame = validate_data(data)
    groups = list(dict.fromkeys(frame["group"].astype(str)))
    if len(groups) > len(PALETTE):
        raise ValueError(f"At most {len(PALETTE)} groups are supported by this template")

    color_map = dict(zip(groups, PALETTE))
    marker_map = dict(zip(groups, MARKERS))
    fig, ax = plt.subplots(figsize=(5.3, 3.7))
    # 为两组图例预留固定右栏，确保终稿尺寸下不越出画布。
    fig.subplots_adjust(left=0.12, right=0.72, bottom=0.14, top=0.88)
    sizes = scale_area(frame["size"])
    for group in groups:
        selected = frame["group"].astype(str).eq(group)
        ax.scatter(
            frame.loc[selected, "x"],
            frame.loc[selected, "y"],
            s=sizes[selected.to_numpy()],
            color=color_map[group],
            marker=marker_map[group],
            edgecolor="#FFFFFF",
            linewidth=0.9,
            alpha=0.92,
            label=group,
        )

    # 只标注最大气泡，控制标签密度并保留最重要观测的可追溯性。
    for index in frame["size"].nlargest(min(4, len(frame))).index:
        row = frame.loc[index]
        ax.annotate(
            str(row["label"]),
            (row["x"], row["y"]),
            xytext=(4, 4),
            textcoords="offset points",
            fontsize=7,
            color="#30343B",
        )

    ax.set(xlabel="Variable X", ylabel="Variable Y", title="Bubble scatter: magnitude and group")
    group_legend = ax.legend(title="Group", loc="upper left", bbox_to_anchor=(1.03, 1.0))
    ax.add_artist(group_legend)

    legend_values = np.quantile(frame["size"], [0.25, 0.5, 0.75])
    legend_sizes = scale_area(pd.Series([frame["size"].min(), *legend_values, frame["size"].max()]))[1:-1]
    handles = [
        ax.scatter([], [], s=size, color="#B8C1CC", edgecolor="white", linewidth=0.8)
        for size in legend_sizes
    ]
    size_legend = ax.legend(
        handles,
        [f"{value:.0f}" for value in legend_values],
        title="Magnitude",
        loc="lower left",
        bbox_to_anchor=(1.02, 0.0),
        labelspacing=1.3,
    )
    ax.add_artist(size_legend)
    return fig


def save_figure(fig: plt.Figure, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    audit_figure(fig, output.stem)
    fig.savefig(output.with_suffix(".svg"), bbox_inches="tight")
    fig.savefig(output.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(output.with_suffix(".png"), dpi=450, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--input", type=Path, help="CSV with x,y,size,group,label")
    source.add_argument("--demo", action="store_true", help="Render deterministic preview data")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("bubble_scatter"),
        help="Output prefix without extension",
    )
    args = parser.parse_args()
    apply_style()
    data = demo_data() if args.demo else pd.read_csv(args.input)
    save_figure(plot_bubble_scatter(data), args.output)


if __name__ == "__main__":
    main()
