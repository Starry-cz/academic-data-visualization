#!/usr/bin/env python3
"""XPS peak-deconvolution plot with stacked spectra and component fills.

Input CSV columns: ``spectrum``, ``energy``, ``component``, ``intensity``.
Each spectrum must contain ``observed``, ``fit``, and ``background`` rows plus
one or more chemical peak components. Use ``--demo`` only for the bundled preview.
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


REQUIRED = {"spectrum", "energy", "component", "intensity"}
PEAK_COLOURS = ["#74B8DD", "#EEAFB1", "#F5D89A", "#A8CDB7"]
SEMANTIC_COLOR_ROLES = {
    "observed": "#25313C",
    "fit": "#4B7FA5",
    "background": "#80BFC1",
    "components": PEAK_COLOURS,
}


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
            "savefig.dpi": 600,
        }
    )


def gaussian(x: np.ndarray, centre: float, width: float, amplitude: float) -> np.ndarray:
    return amplitude * np.exp(-0.5 * ((x - centre) / width) ** 2)


def demo_data() -> pd.DataFrame:
    energy = np.linspace(526, 538, 360)
    records: list[pd.DataFrame] = []
    specifications = {
        "Material A": [(531.7, 0.48, 1.00, "M–O"), (533.1, 0.65, 0.35, "O–H"), (529.8, 0.42, 0.30, "Defect O")],
        "Material B": [(531.6, 0.52, 0.82, "M–O"), (533.0, 0.72, 0.27, "O–H"), (529.7, 0.46, 0.24, "Defect O")],
    }
    for spectrum_index, (spectrum, peaks) in enumerate(specifications.items()):
        background = 0.045 + 0.004 * (energy - energy.min())
        components = {label: gaussian(energy, centre, width, amplitude) for centre, width, amplitude, label in peaks}
        fit = background + sum(components.values())
        # 示例扰动使用固定谐波，既表现观测与拟合差异，也避免随机预览随环境变化。
        phase = np.linspace(0, 12 * np.pi, energy.size) + spectrum_index * 0.7
        observed = fit + 0.010 * np.sin(phase) + 0.004 * np.cos(2.3 * phase)
        series = {"observed": observed, "fit": fit, "background": background, **components}
        for component, intensity in series.items():
            records.append(
                pd.DataFrame(
                    {
                        "spectrum": spectrum,
                        "energy": energy,
                        "component": component,
                        "intensity": intensity,
                    }
                )
            )
    return pd.concat(records, ignore_index=True)


def validate_data(data: pd.DataFrame) -> pd.DataFrame:
    missing = REQUIRED - set(data.columns)
    if missing:
        raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")
    frame = data.copy()
    frame["energy"] = pd.to_numeric(frame["energy"], errors="raise")
    frame["intensity"] = pd.to_numeric(frame["intensity"], errors="raise")
    if not np.isfinite(frame[["energy", "intensity"]].to_numpy()).all():
        raise ValueError("energy and intensity must be finite")
    for spectrum, subset in frame.groupby("spectrum", sort=False):
        components = set(subset["component"].astype(str))
        required_components = {"observed", "fit", "background"}
        if not required_components.issubset(components):
            missing_components = required_components - components
            raise ValueError(f"{spectrum} is missing: {', '.join(sorted(missing_components))}")
        counts = subset.groupby("component").size()
        if counts.nunique() != 1:
            raise ValueError(f"{spectrum} components must share the same energy grid")
    return frame


def plot_xps(data: pd.DataFrame) -> plt.Figure:
    frame = validate_data(data)
    spectra = list(dict.fromkeys(frame["spectrum"].astype(str)))
    if not 1 <= len(spectra) <= 4:
        raise ValueError("This template supports one to four stacked spectra")

    fig, ax = plt.subplots(figsize=(7.2, 6.1))
    fig.subplots_adjust(left=0.15, right=0.96, bottom=0.14, top=0.90)
    offset_step = 1.25
    for index, spectrum in enumerate(spectra):
        subset = frame[frame["spectrum"].astype(str).eq(spectrum)]
        pivot = subset.pivot(index="energy", columns="component", values="intensity").sort_index()
        offset = (len(spectra) - index - 1) * offset_step
        components = [name for name in pivot.columns if name not in {"observed", "fit", "background"}]
        for peak_index, component in enumerate(components):
            values = pivot[component].to_numpy()
            base = pivot["background"].to_numpy() + offset
            ax.fill_between(
                pivot.index,
                base,
                base + values,
                color=PEAK_COLOURS[peak_index % len(PEAK_COLOURS)],
                alpha=0.72,
                linewidth=0,
            )
            maximum = int(np.argmax(values))
            if index == 0:
                ax.annotate(
                    component,
                    (pivot.index[maximum], base[maximum] + values[maximum]),
                    xytext=(0, 6),
                    textcoords="offset points",
                    ha="center",
                    fontsize=7,
                    color="#334155",
                )

        ax.plot(pivot.index, pivot["observed"] + offset, color="#25313C", lw=0.65, alpha=0.72)
        ax.plot(pivot.index, pivot["fit"] + offset, color="#4B7FA5", lw=1.25)
        ax.plot(pivot.index, pivot["background"] + offset, color="#80BFC1", lw=0.8)
        ax.text(
            pivot.index.max() - 0.15,
            offset + 0.09,
            spectrum,
            ha="left",
            va="bottom",
            fontsize=8,
            fontweight="bold",
            color="#263746",
        )

    ax.invert_xaxis()
    ax.set_xlabel("Binding energy (eV)")
    ax.set_ylabel("Intensity (a.u.)")
    ax.set_title("XPS peak deconvolution")
    ax.set_yticks([])
    ax.margins(x=0.01, y=0.08)
    fig.text(
        0.5,
        0.025,
        "Component areas require a declared background, line shape, constraints, and fit diagnostics.",
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
    source.add_argument("--input", type=Path, help="Long CSV with spectrum,energy,component,intensity")
    source.add_argument("--demo", action="store_true", help="Render deterministic preview data")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("xps_peak_deconvolution"),
        help="Output prefix without extension",
    )
    parser.add_argument("--tiff", action="store_true", help="Also export a 600 dpi TIFF submission raster")
    args = parser.parse_args()
    apply_style()
    data = demo_data() if args.demo else pd.read_csv(args.input)
    save_figure(plot_xps(data), args.output, args.tiff)


if __name__ == "__main__":
    main()
