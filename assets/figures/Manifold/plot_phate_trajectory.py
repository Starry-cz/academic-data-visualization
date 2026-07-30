#!/usr/bin/env python3
"""Render a high-fidelity PHATE trajectory template from explicit demo coordinates."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, Normalize
from matplotlib.patches import Patch
import numpy as np
from scipy.interpolate import PchipInterpolator


SEED = 20260730
GROUP_COLORS = ("#D83E8D", "#F0AD38", "#4297A8", "#4051A3")
GROUP_FILLS = ("#F2B7D2", "#F8DDA5", "#A8D5DC", "#A9B2DF")
LANDMARKS = ("1", "8", "15", "22", "28")
LANDMARK_POSITIONS = np.array([0.03, 0.25, 0.50, 0.75, 0.97])

# 控制点复现参考图中的四条连续轨迹；真实研究应替换为已计算的 PHATE 坐标。
PATH_CONTROLS = (
    (
        (-2.68, 0.05),
        (-2.30, 0.63),
        (-1.62, 1.12),
        (-0.72, 1.34),
        (0.18, 1.24),
        (1.15, 0.98),
        (2.10, 0.73),
    ),
    (
        (-2.72, -0.03),
        (-2.17, 0.15),
        (-1.35, 0.06),
        (-0.35, -0.05),
        (0.65, 0.01),
        (1.65, 0.12),
        (2.62, 0.11),
    ),
    (
        (-2.74, -0.12),
        (-2.15, -0.34),
        (-1.34, -0.58),
        (-0.40, -0.82),
        (0.55, -0.73),
        (1.58, -0.43),
        (2.58, -0.12),
    ),
    (
        (-2.72, -0.19),
        (-2.20, -0.56),
        (-1.48, -1.10),
        (-0.64, -1.50),
        (0.20, -1.66),
        (1.05, -1.45),
        (1.82, -0.96),
        (2.52, -0.31),
    ),
)
WIDTH_CONTROLS = (
    (0.20, 0.34, 0.40, 0.33, 0.23),
    (0.14, 0.22, 0.28, 0.23, 0.15),
    (0.16, 0.28, 0.38, 0.30, 0.18),
    (0.18, 0.30, 0.46, 0.39, 0.22),
)

mpl.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
        "font.size": 7,
        "axes.linewidth": 0.8,
        "svg.fonttype": "none",
        "pdf.fonttype": 42,
        "savefig.dpi": 600,
    }
)


def smooth_path(control_points: tuple[tuple[float, float], ...]) -> tuple[np.ndarray, np.ndarray]:
    """使用保形插值生成不会明显过冲的轨迹中心线。"""
    controls = np.asarray(control_points, dtype=float)
    control_t = np.linspace(0, 1, len(controls))
    dense_t = np.linspace(0, 1, 320)
    x = PchipInterpolator(control_t, controls[:, 0])(dense_t)
    y = PchipInterpolator(control_t, controls[:, 1])(dense_t)
    return x, y


def smooth_width(width_controls: tuple[float, ...]) -> np.ndarray:
    control_t = np.linspace(0, 1, len(width_controls))
    return PchipInterpolator(control_t, np.asarray(width_controls))(np.linspace(0, 1, 320))


def sample_cloud(
    rng: np.random.Generator,
    x: np.ndarray,
    y: np.ndarray,
    width: np.ndarray,
    group: int,
    count: int = 210,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """围绕轨迹采样点云，并生成与纵向位置一致的 DSO 连续色标。"""
    positions = rng.uniform(0, 1, count)
    indices = np.clip((positions * (len(x) - 1)).astype(int), 0, len(x) - 1)
    cloud_x = x[indices] + rng.normal(0, 0.085, count)
    cloud_y = y[indices] + rng.normal(0, width[indices] * 0.72, count)
    dso = np.clip(0.90 * cloud_y + rng.normal(0, 0.32, count), -1.7, 1.8)

    # 顶部群组补充少量离群观测，匹配参考图上方的稀疏点云。
    if group == 0:
        extra = 36
        cloud_x = np.concatenate([cloud_x, rng.normal(-0.85, 0.75, extra)])
        cloud_y = np.concatenate([cloud_y, rng.normal(1.48, 0.26, extra)])
        dso = np.concatenate([dso, np.clip(rng.normal(1.35, 0.28, extra), -1.7, 1.8)])
    return cloud_x, cloud_y, dso


def add_landmarks(
    ax: plt.Axes,
    x: np.ndarray,
    y: np.ndarray,
    color: str,
) -> None:
    """沿轨迹标注 1、8、15、22、28 五个伪时间节点。"""
    for label, position in zip(LANDMARKS, LANDMARK_POSITIONS, strict=True):
        index = round(position * (len(x) - 1))
        ax.text(
            x[index],
            y[index],
            label,
            ha="center",
            va="center",
            color="white",
            fontsize=5.4,
            fontweight="bold",
            bbox={
                "boxstyle": "round,pad=0.18",
                "facecolor": color,
                "edgecolor": "white",
                "linewidth": 0.35,
            },
            zorder=6,
        )


def render(output_dir: Path) -> None:
    rng = np.random.default_rng(SEED)
    paths = [smooth_path(control_points) for control_points in PATH_CONTROLS]
    widths = [smooth_width(controls) for controls in WIDTH_CONTROLS]

    dso_cmap = LinearSegmentedColormap.from_list(
        "dso",
        ("#3E8FA3", "#B7B9B7", "#B65C3D"),
    )
    dso_norm = Normalize(vmin=-1.7, vmax=1.8)

    fig = plt.figure(figsize=(7.2, 4.15), facecolor="white")
    ax = fig.add_axes([0.065, 0.11, 0.70, 0.80])

    clouds: list[tuple[np.ndarray, np.ndarray, np.ndarray]] = []
    for group, ((x, y), width) in enumerate(zip(paths, widths, strict=True)):
        ax.fill_between(
            x,
            y - width,
            y + width,
            color=GROUP_FILLS[group],
            alpha=0.26,
            linewidth=0,
            zorder=1,
        )
        ax.fill_between(
            x,
            y - width * 0.56,
            y + width * 0.56,
            color=GROUP_FILLS[group],
            alpha=0.32,
            linewidth=0,
            zorder=1,
        )
        clouds.append(sample_cloud(rng, x, y, width, group))

    scatter = None
    for cloud_x, cloud_y, dso in clouds:
        scatter = ax.scatter(
            cloud_x,
            cloud_y,
            c=dso,
            cmap=dso_cmap,
            norm=dso_norm,
            s=8,
            alpha=0.72,
            edgecolors="white",
            linewidths=0.20,
            rasterized=True,
            zorder=3,
        )

    for group, (x, y) in enumerate(paths):
        ax.plot(
            x,
            y,
            color=GROUP_COLORS[group],
            linewidth=1.7,
            solid_capstyle="round",
            zorder=5,
        )
        add_landmarks(ax, x, y, GROUP_COLORS[group])

    ax.set_xlim(-3.05, 3.00)
    ax.set_ylim(-1.92, 1.86)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    arrow = {"arrowstyle": "->", "color": "#111111", "linewidth": 0.85, "shrinkA": 0, "shrinkB": 0}
    ax.annotate("", xy=(1.025, 0), xytext=(0, 0), xycoords="axes fraction", arrowprops=arrow)
    ax.annotate("", xy=(0, 1.025), xytext=(0, 0), xycoords="axes fraction", arrowprops=arrow)
    ax.text(0.01, -0.045, "PHATE 1", transform=ax.transAxes, ha="left", va="top", fontsize=7)
    ax.text(-0.045, 0.03, "PHATE 2", transform=ax.transAxes, ha="right", va="bottom", rotation=90, fontsize=7)
    ax.text(0.50, 1.055, "DSO", transform=ax.transAxes, ha="center", va="bottom", fontsize=7)

    legend_handles = [
        Patch(
            facecolor=GROUP_FILLS[index],
            edgecolor=GROUP_COLORS[index],
            linewidth=0.8,
            label=str(index + 1),
        )
        for index in range(4)
    ]
    ax.legend(
        handles=legend_handles,
        title="Cluster",
        loc="center left",
        bbox_to_anchor=(1.01, 0.40),
        frameon=False,
        borderaxespad=0,
        handlelength=2.2,
        handleheight=0.9,
        labelspacing=0.35,
        fontsize=6.5,
        title_fontsize=6.5,
    )

    if scatter is None:
        raise RuntimeError("No PHATE points were generated.")
    colorbar_axis = fig.add_axes([0.885, 0.20, 0.020, 0.69])
    colorbar = fig.colorbar(scatter, cax=colorbar_axis)
    colorbar.set_ticks([-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5])
    colorbar.ax.tick_params(labelsize=5.8, width=0.6, length=2)
    colorbar.outline.set_linewidth(0.65)

    output_dir.mkdir(parents=True, exist_ok=True)
    base = output_dir / "phate_trajectory"
    fig.savefig(base.with_suffix(".png"), dpi=600, bbox_inches="tight", facecolor="white")
    fig.savefig(base.with_suffix(".svg"), bbox_inches="tight", facecolor="white")
    fig.savefig(base.with_suffix(".pdf"), bbox_inches="tight", facecolor="white")
    fig.savefig(
        base.with_suffix(".tiff"),
        dpi=600,
        bbox_inches="tight",
        facecolor="white",
        pil_kwargs={"compression": "tiff_lzw"},
    )
    plt.close(fig)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--demo",
        action="store_true",
        help="确认使用脚本内置的合成演示坐标，防止误当作真实 PHATE 结果。",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="PNG、SVG、PDF 与 TIFF 的输出目录。",
    )
    args = parser.parse_args()
    if not args.demo:
        parser.error("本模板仅在显式传入 --demo 时生成合成示例。")
    return args


if __name__ == "__main__":
    arguments = parse_args()
    render(arguments.output_dir)
