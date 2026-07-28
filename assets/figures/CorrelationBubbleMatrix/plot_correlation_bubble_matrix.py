#!/usr/bin/env python3
"""Correlation bubble matrix with redundant colour and area encoding.

Input CSV: observations in rows and numeric variables in columns. Colour shows
the sign of Pearson's r; bubble area and printed values show its magnitude.
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
from matplotlib.colors import LinearSegmentedColormap


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
from visual_qa import audit_figure


DIVERGING = ["#565AA7", "#F7F7F7", "#A90B2F"]


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
    rng = np.random.default_rng(728)
    latent = rng.normal(size=(70, 3))
    noise = rng.normal(scale=0.42, size=(70, 7))
    values = np.column_stack(
        [
            latent[:, 0],
            0.78 * latent[:, 0] + noise[:, 1],
            0.48 * latent[:, 0] + noise[:, 2],
            latent[:, 1],
            -0.66 * latent[:, 1] + noise[:, 4],
            latent[:, 2],
            0.72 * latent[:, 2] + noise[:, 6],
        ]
    )
    return pd.DataFrame(values, columns=list("ABCDEFG"))


def validate_data(data: pd.DataFrame) -> pd.DataFrame:
    numeric = data.select_dtypes(include=np.number).copy()
    if numeric.shape[1] < 3:
        raise ValueError("at least three numeric variables are required")
    if numeric.shape[0] < 3:
        raise ValueError("at least three observations are required")
    if not np.isfinite(numeric.to_numpy()).all():
        raise ValueError("numeric variables must be finite")
    if (numeric.nunique() < 2).any():
        raise ValueError("each numeric variable must contain variation")
    return numeric


def plot_correlation_bubble_matrix(data: pd.DataFrame) -> plt.Figure:
    numeric = validate_data(data)
    corr = numeric.corr(method="pearson")
    names = list(corr.columns)
    n = len(names)
    row, col = np.indices((n, n))
    values = corr.to_numpy()
    mask = row >= col

    cmap = LinearSegmentedColormap.from_list("blue_red_signal", DIVERGING)
    fig, ax = plt.subplots(figsize=(5.2, 4.5), constrained_layout=True)
    scatter = ax.scatter(
        col[mask],
        row[mask],
        s=35 + 470 * np.abs(values[mask]),
        c=values[mask],
        cmap=cmap,
        vmin=-1,
        vmax=1,
        edgecolor="#FFFFFF",
        linewidth=0.8,
    )
    for x, y, value in zip(col[mask], row[mask], values[mask]):
        ax.text(x, y, f"{value:.2f}", ha="center", va="center", fontsize=6.5,
                color="white" if abs(value) >= 0.63 else "#252A31")

    ax.set_xticks(range(n), names, rotation=45, ha="right")
    ax.set_yticks(range(n), names)
    ax.set_xlim(-0.6, n - 0.4)
    ax.set_ylim(n - 0.4, -0.6)
    ax.set_aspect("equal")
    ax.tick_params(length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_title("Correlation structure (Pearson r)")
    colorbar = fig.colorbar(scatter, ax=ax, fraction=0.045, pad=0.04)
    colorbar.set_label("Pearson r")
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
    source.add_argument("--input", type=Path, help="CSV with observations × numeric variables")
    source.add_argument("--demo", action="store_true")
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("correlation_bubble_matrix"))
    args = parser.parse_args()
    apply_style()
    data = demo_data() if args.demo else pd.read_csv(args.input)
    save_figure(plot_correlation_bubble_matrix(data), args.output)


if __name__ == "__main__":
    main()
