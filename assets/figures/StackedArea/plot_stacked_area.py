#!/usr/bin/env python3
"""Publication-ready stacked area chart.

Input CSV columns: time, category, value. Values must be non-negative and each
time/category pair must be unique. Use ``--demo`` to rebuild the preview.
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


PALETTE = ["#497AB7", "#7EB6D5", "#BDE2ED", "#F0F0D9", "#FEEAA1", "#FCB567", "#F27144"]
REQUIRED = {"time", "category", "value"}


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
    years = np.arange(2017, 2025)
    values = {
        "A": [22, 24, 25, 27, 29, 31, 33, 35],
        "B": [17, 18, 19, 20, 21, 22, 24, 25],
        "C": [14, 15, 16, 17, 18, 19, 20, 22],
        "D": [12, 13, 14, 15, 16, 17, 18, 19],
        "E": [9, 10, 11, 12, 13, 15, 16, 18],
        "F": [7, 8, 9, 10, 11, 12, 13, 15],
        "G": [5, 6, 7, 8, 9, 10, 11, 12],
    }
    return pd.DataFrame(
        [(year, category, series[i]) for category, series in values.items() for i, year in enumerate(years)],
        columns=["time", "category", "value"],
    )


def validate_data(data: pd.DataFrame) -> pd.DataFrame:
    missing = REQUIRED - set(data.columns)
    if missing:
        raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")
    frame = data.copy()
    frame["time"] = pd.to_numeric(frame["time"], errors="raise")
    frame["value"] = pd.to_numeric(frame["value"], errors="raise")
    if not np.isfinite(frame[["time", "value"]].to_numpy()).all():
        raise ValueError("time and value must be finite")
    if (frame["value"] < 0).any():
        raise ValueError("stacked area values must be non-negative")
    if frame.duplicated(["time", "category"]).any():
        raise ValueError("each time/category pair must be unique")
    if frame["time"].nunique() < 3:
        raise ValueError("at least three ordered time points are required")
    return frame


def plot_stacked_area(data: pd.DataFrame) -> plt.Figure:
    frame = validate_data(data)
    categories = list(dict.fromkeys(frame["category"].astype(str)))
    if len(categories) > len(PALETTE):
        raise ValueError(f"At most {len(PALETTE)} categories are supported")
    table = (
        frame.assign(category=frame["category"].astype(str))
        .pivot(index="time", columns="category", values="value")
        .reindex(columns=categories)
        .sort_index()
    )
    if table.isna().any().any():
        raise ValueError("all time/category combinations must be present")

    fig, ax = plt.subplots(figsize=(6.2, 3.5), constrained_layout=True)
    ax.stackplot(
        table.index.to_numpy(),
        *[table[column].to_numpy() for column in categories],
        colors=PALETTE[: len(categories)],
        edgecolor="#FFFFFF",
        linewidth=0.7,
        alpha=0.98,
    )
    cumulative = table.cumsum(axis=1)
    lower = cumulative.shift(axis=1, fill_value=0)
    final_x = table.index[-1]
    # 直接标注末端层中心，避免图例与面积层之间来回查找。
    for category, color in zip(categories, PALETTE):
        center = (lower.loc[final_x, category] + cumulative.loc[final_x, category]) / 2
        ax.text(final_x + (table.index.max() - table.index.min()) * 0.025, center, category,
                va="center", color=color, fontweight="bold", fontsize=7)

    ax.set(
        xlabel="Time",
        ylabel="Cumulative value",
        title="Composition over ordered time",
        xlim=(table.index.min(), table.index.max() + (table.index.max() - table.index.min()) * 0.13),
        ylim=(0, cumulative.iloc[-1, -1] * 1.05),
    )
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
    source.add_argument("--input", type=Path, help="CSV with time,category,value")
    source.add_argument("--demo", action="store_true")
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("stacked_area"))
    args = parser.parse_args()
    apply_style()
    data = demo_data() if args.demo else pd.read_csv(args.input)
    save_figure(plot_stacked_area(data), args.output)


if __name__ == "__main__":
    main()
