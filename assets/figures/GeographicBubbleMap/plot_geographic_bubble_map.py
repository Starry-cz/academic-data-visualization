#!/usr/bin/env python3
"""Coordinate-aware geographic bubble map.

Input CSV columns: longitude, latitude, size, group, label. Country boundaries
come from an explicit GeoJSON file; the bundled preview uses Natural Earth
1:110m public-domain boundaries. Bubble area encodes ``size``.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.collections import PolyCollection


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
from visual_qa import audit_figure


PALETTE = ["#497AB7", "#7EB6D5", "#BDE2ED", "#FEEAA1", "#FCB567", "#F27144"]
MARKERS = ["o", "s", "^", "D", "P", "X"]
REQUIRED = {"longitude", "latitude", "size", "group", "label"}
BUNDLED_BOUNDARY = Path(__file__).with_name("ne_110m_admin_0_countries.geojson")


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
            "longitude": [-122.4, -99.1, -74.0, -0.1, 13.4, 31.2, 103.8, 116.4, 139.7, 151.2],
            "latitude": [37.8, 19.4, 40.7, 51.5, 52.5, 30.0, 1.35, 39.9, 35.7, -33.9],
            "size": [26, 18, 35, 22, 20, 17, 31, 42, 38, 28],
            "group": ["Americas", "Americas", "Americas", "Europe", "Europe",
                      "Africa", "Asia-Pacific", "Asia-Pacific", "Asia-Pacific", "Asia-Pacific"],
            "label": ["San Francisco", "Mexico City", "New York", "London", "Berlin",
                      "Cairo", "Singapore", "Beijing", "Tokyo", "Sydney"],
        }
    )


def validate_data(data: pd.DataFrame) -> pd.DataFrame:
    missing = REQUIRED - set(data.columns)
    if missing:
        raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")
    frame = data.copy()
    frame[["longitude", "latitude", "size"]] = frame[
        ["longitude", "latitude", "size"]
    ].apply(pd.to_numeric, errors="raise")
    if not np.isfinite(frame[["longitude", "latitude", "size"]].to_numpy()).all():
        raise ValueError("longitude, latitude, and size must be finite")
    if not frame["longitude"].between(-180, 180).all():
        raise ValueError("longitude must be within [-180, 180]")
    if not frame["latitude"].between(-90, 90).all():
        raise ValueError("latitude must be within [-90, 90]")
    if (frame["size"] <= 0).any() or frame["size"].nunique() < 2:
        raise ValueError("size must contain at least two distinct positive values")
    return frame


def load_polygons(boundary_path: Path) -> list[list[list[float]]]:
    document = json.loads(boundary_path.read_text(encoding="utf-8"))
    if document.get("type") != "FeatureCollection":
        raise ValueError("boundary GeoJSON must be a FeatureCollection")
    polygons: list[list[list[float]]] = []
    for feature in document["features"]:
        geometry = feature.get("geometry") or {}
        coordinates = geometry.get("coordinates", [])
        if geometry.get("type") == "Polygon":
            polygons.extend(coordinates[:1])
        elif geometry.get("type") == "MultiPolygon":
            polygons.extend(polygon[0] for polygon in coordinates if polygon)
    if not polygons:
        raise ValueError("boundary GeoJSON contains no Polygon or MultiPolygon geometry")
    return polygons


def scale_area(values: pd.Series, minimum: float = 28, maximum: float = 240) -> np.ndarray:
    roots = np.sqrt(values.to_numpy(dtype=float))
    return minimum + (roots - roots.min()) / (roots.max() - roots.min()) * (maximum - minimum)


def plot_geographic_bubble_map(data: pd.DataFrame, boundary_path: Path) -> plt.Figure:
    frame = validate_data(data)
    groups = list(dict.fromkeys(frame["group"].astype(str)))
    if len(groups) > len(PALETTE):
        raise ValueError(f"At most {len(PALETTE)} groups are supported")
    color_map = dict(zip(groups, PALETTE))
    marker_map = dict(zip(groups, MARKERS))

    fig = plt.figure(figsize=(7.2, 4.35))
    grid = fig.add_gridspec(
        2, 1, height_ratios=[5.0, 0.72], left=0.08, right=0.99, bottom=0.04, top=0.9, hspace=0.22
    )
    ax = fig.add_subplot(grid[0, 0])
    legend_ax = fig.add_subplot(grid[1, 0])
    legend_ax.set_axis_off()
    # 使用真实经纬度边界；不以装饰性轮廓替代空间证据。
    collection = PolyCollection(
        load_polygons(boundary_path),
        facecolor="#EEF1F3",
        edgecolor="#C6CDD3",
        linewidth=0.35,
        zorder=1,
    )
    ax.add_collection(collection)
    sizes = scale_area(frame["size"])
    for group in groups:
        selected = frame["group"].astype(str).eq(group)
        ax.scatter(
            frame.loc[selected, "longitude"],
            frame.loc[selected, "latitude"],
            s=sizes[selected.to_numpy()],
            color=color_map[group],
            marker=marker_map[group],
            edgecolor="#FFFFFF",
            linewidth=0.8,
            alpha=0.95,
            label=group,
            zorder=3,
        )
    for index in frame["size"].nlargest(min(6, len(frame))).index:
        row = frame.loc[index]
        ax.annotate(str(row["label"]), (row["longitude"], row["latitude"]),
                    xytext=(4, 4), textcoords="offset points", fontsize=6.5, zorder=4)

    ax.set_xlim(-180, 180)
    ax.set_ylim(-60, 90)
    ax.set_xticks([-120, -60, 0, 60, 120], ["120°W", "60°W", "0°", "60°E", "120°E"])
    ax.set_yticks([-30, 0, 30, 60], ["30°S", "0°", "30°N", "60°N"])
    ax.set(xlabel="Longitude", ylabel="Latitude", title="Geographic distribution and magnitude")
    handles, labels = ax.get_legend_handles_labels()
    legend_ax.legend(handles, labels, title="Region", loc="center", ncol=len(groups))
    legend_ax.text(1.0, 0.02, "Boundary: Natural Earth 1:110m (public domain)",
                   transform=legend_ax.transAxes, ha="right", fontsize=6, color="#6B7280")
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
    source.add_argument("--input", type=Path, help="CSV with longitude,latitude,size,group,label")
    source.add_argument("--demo", action="store_true")
    parser.add_argument("--boundary", type=Path, default=BUNDLED_BOUNDARY)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("geographic_bubble_map"))
    args = parser.parse_args()
    apply_style()
    data = demo_data() if args.demo else pd.read_csv(args.input)
    save_figure(plot_geographic_bubble_map(data, args.boundary), args.output)


if __name__ == "__main__":
    main()
