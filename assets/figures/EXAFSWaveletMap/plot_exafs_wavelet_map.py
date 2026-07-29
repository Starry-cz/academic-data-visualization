#!/usr/bin/env python3
"""EXAFS wavelet-transform magnitude as a 3D surface with 2D floor projection.

Input CSV columns: ``k``, ``r``, ``magnitude`` on a complete rectangular grid.
Use ``--demo`` only to rebuild the bundled preview.
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


REQUIRED = {"k", "r", "magnitude"}
WAVELET_CMAP = LinearSegmentedColormap.from_list(
    "wavelet_blue_rose",
    ["#E7F3F8", "#74B8DD", "#F7F7F5", "#EEAFB1", "#B85C77"],
)
SEMANTIC_COLOR_ROLES = {"low": "#E7F3F8", "mid": "#F7F7F5", "high": "#B85C77"}


def apply_style() -> None:
    mpl.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "Helvetica", "Liberation Sans"],
            "font.size": 8,
            "axes.linewidth": 0.65,
            "xtick.direction": "out",
            "ytick.direction": "out",
            "legend.frameon": False,
            "pdf.fonttype": 42,
            "svg.fonttype": "none",
            "savefig.dpi": 600,
        }
    )


def demo_data() -> pd.DataFrame:
    k = np.linspace(2.0, 14.0, 90)
    r = np.linspace(0.5, 5.2, 75)
    kk, rr = np.meshgrid(k, r)
    main = np.exp(-((kk - 8.2) ** 2 / 4.2 + (rr - 2.25) ** 2 / 0.22))
    shoulder = 0.46 * np.exp(-((kk - 5.0) ** 2 / 2.0 + (rr - 3.45) ** 2 / 0.34))
    ridge = 0.22 * np.exp(-((kk - 11.2) ** 2 / 3.6 + (rr - 1.35) ** 2 / 0.18))
    magnitude = main + shoulder + ridge
    return pd.DataFrame({"k": kk.ravel(), "r": rr.ravel(), "magnitude": magnitude.ravel()})


def validate_grid(data: pd.DataFrame) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    missing = REQUIRED - set(data.columns)
    if missing:
        raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")
    frame = data.copy()
    for column in REQUIRED:
        frame[column] = pd.to_numeric(frame[column], errors="raise")
    if not np.isfinite(frame[list(REQUIRED)].to_numpy()).all():
        raise ValueError("k, r, and magnitude must be finite")
    if (frame["magnitude"] < 0).any():
        raise ValueError("wavelet magnitude must be non-negative")
    pivot = frame.pivot(index="r", columns="k", values="magnitude").sort_index().sort_index(axis=1)
    if pivot.isna().any().any():
        raise ValueError("input must define a complete rectangular k × r grid")
    k_values = pivot.columns.to_numpy(dtype=float)
    r_values = pivot.index.to_numpy(dtype=float)
    kk, rr = np.meshgrid(k_values, r_values)
    return kk, rr, pivot.to_numpy(dtype=float)


def plot_wavelet_map(data: pd.DataFrame) -> plt.Figure:
    kk, rr, magnitude = validate_grid(data)
    if magnitude.max() <= 0:
        raise ValueError("magnitude must contain a positive signal")
    scaled = magnitude / magnitude.max()
    floor = 1.18

    fig = plt.figure(figsize=(7.2, 6.55))
    ax = fig.add_subplot(111, projection="3d")
    fig.subplots_adjust(left=0.02, right=0.96, bottom=0.06, top=0.92)
    ax.plot_surface(
        kk,
        rr,
        scaled,
        cmap=WAVELET_CMAP,
        vmin=0,
        vmax=1,
        rcount=70,
        ccount=85,
        linewidth=0,
        antialiased=True,
        alpha=0.94,
    )
    ax.contourf(
        kk,
        rr,
        scaled,
        zdir="z",
        offset=floor,
        levels=np.linspace(0, 1, 18),
        cmap=WAVELET_CMAP,
        vmin=0,
        vmax=1,
        alpha=0.96,
    )
    ax.set(xlabel=r"$k$ ($\AA^{-1}$)", ylabel=r"$R$ ($\AA$)", zlabel="WT magnitude")
    ax.set_title("EXAFS wavelet-transform map")
    ax.set_zlim(floor, 0)
    ax.view_init(elev=27, azim=-55)
    ax.set_box_aspect((1.15, 1.0, 0.9))
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.pane.set_facecolor((1, 1, 1, 0))
        axis.pane.set_edgecolor("#CBD5E1")
    ax.grid(False)
    fig.text(
        0.5,
        0.015,
        "The floor projection is the quantitative lookup view; the 3D surface provides structural context.",
        ha="center",
        fontsize=6.5,
        color="#5F6772",
    )
    return fig


def save_figure(fig: plt.Figure, output: Path, export_tiff: bool) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    audit_figure(fig, output.stem)
    fig.savefig(output.with_suffix(".svg"), bbox_inches="tight")
    fig.savefig(output.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(output.with_suffix(".png"), dpi=600, bbox_inches="tight")
    if export_tiff:
        fig.savefig(output.with_suffix(".tiff"), dpi=600, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--input", type=Path, help="CSV with k,r,magnitude on a complete grid")
    source.add_argument("--demo", action="store_true", help="Render deterministic preview data")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("exafs_wavelet_map"),
        help="Output prefix without extension",
    )
    parser.add_argument("--tiff", action="store_true", help="Also export a 600 dpi TIFF submission raster")
    args = parser.parse_args()
    apply_style()
    data = demo_data() if args.demo else pd.read_csv(args.input)
    save_figure(plot_wavelet_map(data), args.output, args.tiff)


if __name__ == "__main__":
    main()
