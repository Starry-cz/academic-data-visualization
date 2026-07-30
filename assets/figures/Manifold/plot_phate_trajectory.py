#!/usr/bin/env python3
"""Render a publication-style PHATE trajectory map from an explicit demo dataset."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import phate
from scipy.ndimage import gaussian_filter1d
from scipy.stats import gaussian_kde


SEED = 20260730
GROUP_COLORS = ("#98145A", "#FDAC2C", "#4B98B7", "#4052A5")

mpl.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
        "font.size": 7,
        "axes.linewidth": 0.8,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "xtick.direction": "out",
        "ytick.direction": "out",
        "svg.fonttype": "none",
        "pdf.fonttype": 42,
        "savefig.dpi": 600,
    }
)


def build_demo_data(samples_per_group: int = 220) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """构造四条高维连续轨迹，仅用于模板预览，不代表真实实验结果。"""
    rng = np.random.default_rng(SEED)
    features: list[np.ndarray] = []
    groups: list[np.ndarray] = []
    pseudotimes: list[np.ndarray] = []

    for group in range(4):
        t = np.sort(rng.uniform(0, 1, samples_per_group))
        x = -2.7 + 5.4 * t + rng.normal(0, 0.16, samples_per_group)
        offsets = (1.25, 0.25, -0.35, -0.95)
        amplitudes = (1.10, 0.20, 0.48, -0.78)
        phases = (0.00, 0.35, 0.70, 0.15)
        y = (
            offsets[group]
            + amplitudes[group] * np.sin(np.pi * (t + phases[group]))
            + 0.18 * np.sin(3 * np.pi * t + group)
            + rng.normal(0, 0.13, samples_per_group)
        )

        # 将潜在轨迹非线性提升到高维空间，再由 PHATE 恢复连续结构。
        lifted = np.column_stack(
            [
                x,
                y,
                t,
                x * y,
                x**2,
                y**2,
                np.sin(x),
                np.cos(x),
                np.sin(2 * np.pi * t),
                np.cos(2 * np.pi * t),
                np.tanh(x + y),
                np.exp(-0.18 * (x**2 + y**2)),
            ]
        )
        lifted += rng.normal(0, 0.055, lifted.shape)
        features.append(lifted)
        groups.append(np.full(samples_per_group, group, dtype=int))
        pseudotimes.append(t)

    matrix = np.vstack(features)
    matrix = (matrix - matrix.mean(axis=0)) / matrix.std(axis=0)
    return matrix, np.concatenate(groups), np.concatenate(pseudotimes)


def orient_embedding(embedding: np.ndarray, pseudotime: np.ndarray) -> np.ndarray:
    """旋转并定向嵌入，使伪时间主要沿横轴递增，提升跨次渲染可读性。"""
    centered = embedding - embedding.mean(axis=0)
    _, _, vectors = np.linalg.svd(centered, full_matrices=False)
    rotated = centered @ vectors.T
    if np.corrcoef(rotated[:, 0], pseudotime)[0, 1] < 0:
        rotated[:, 0] *= -1
    return rotated


def density_layer(
    ax: plt.Axes,
    points: np.ndarray,
    color: str,
    x_grid: np.ndarray,
    y_grid: np.ndarray,
) -> None:
    """绘制克制的组内密度带，避免遮盖原始观测点。"""
    xx, yy = np.meshgrid(x_grid, y_grid)
    values = gaussian_kde(points.T, bw_method=0.28)(np.vstack([xx.ravel(), yy.ravel()]))
    zz = values.reshape(xx.shape)
    levels = zz.max() * np.array([0.08, 0.18, 0.35, 0.60, 1.001])
    ax.contourf(xx, yy, zz, levels=levels, colors=[color], alpha=0.075, antialiased=True)


def trajectory_layer(
    ax: plt.Axes,
    points: np.ndarray,
    pseudotime: np.ndarray,
    color: str,
    group_label: str,
) -> None:
    """用等伪时间分箱中心展示群组轨迹，并以离散标签提供冗余编码。"""
    edges = np.linspace(0, 1, 29)
    centers = np.empty((28, 2))
    for index in range(28):
        mask = (pseudotime >= edges[index]) & (pseudotime <= edges[index + 1])
        centers[index] = np.median(points[mask], axis=0)
    centers[:, 0] = gaussian_filter1d(centers[:, 0], sigma=1.1)
    centers[:, 1] = gaussian_filter1d(centers[:, 1], sigma=1.1)

    ax.plot(
        centers[:, 0],
        centers[:, 1],
        color=color,
        linewidth=2.0,
        label=group_label,
        zorder=4,
    )
    for index in (0, 7, 14, 21, 27):
        ax.text(
            centers[index, 0],
            centers[index, 1],
            str(index + 1),
            ha="center",
            va="center",
            color="white",
            fontsize=5.2,
            fontweight="bold",
            bbox={"boxstyle": "round,pad=0.18", "facecolor": color, "edgecolor": "none"},
            zorder=5,
        )


def render(output_dir: Path) -> None:
    matrix, groups, pseudotime = build_demo_data()
    operator = phate.PHATE(
        n_components=2,
        knn=14,
        decay=40,
        t="auto",
        random_state=SEED,
        n_jobs=1,
        verbose=0,
    )
    embedding = orient_embedding(operator.fit_transform(matrix), pseudotime)

    x_pad = np.ptp(embedding[:, 0]) * 0.08
    y_pad = np.ptp(embedding[:, 1]) * 0.10
    x_limits = (embedding[:, 0].min() - x_pad, embedding[:, 0].max() + x_pad)
    y_limits = (embedding[:, 1].min() - y_pad, embedding[:, 1].max() + y_pad)
    x_grid = np.linspace(*x_limits, 180)
    y_grid = np.linspace(*y_limits, 150)

    fig, ax = plt.subplots(figsize=(7.2, 5.6), constrained_layout=True)
    for group, color in enumerate(GROUP_COLORS):
        mask = groups == group
        group_points = embedding[mask]
        density_layer(ax, group_points, color, x_grid, y_grid)
        ax.scatter(
            group_points[:, 0],
            group_points[:, 1],
            s=11,
            color=color,
            alpha=0.30,
            edgecolors="white",
            linewidths=0.25,
            rasterized=True,
            zorder=2,
        )
        trajectory_layer(
            ax,
            group_points,
            pseudotime[mask],
            color,
            f"State {group + 1}",
        )

    ax.set_xlim(x_limits)
    ax.set_ylim(y_limits)
    ax.set_xlabel("PHATE 1", fontweight="bold")
    ax.set_ylabel("PHATE 2", fontweight="bold")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(
        "PHATE trajectory map",
        loc="left",
        fontsize=12,
        fontweight="bold",
        color="#14213D",
        pad=13,
    )
    ax.text(
        0,
        1.012,
        "Continuous high-dimensional states with pseudotime landmarks",
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=7,
        color="#667085",
    )
    ax.legend(
        title="Response state",
        loc="upper right",
        ncol=2,
        handlelength=1.8,
        columnspacing=1.1,
        frameon=False,
    )
    ax.text(
        0.995,
        0.012,
        "Synthetic demonstration · labels mark pseudotime bins",
        transform=ax.transAxes,
        ha="right",
        va="bottom",
        fontsize=5.5,
        color="#7A8494",
    )

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
        help="确认使用脚本内置的合成演示数据，防止误当作真实实验结果。",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="PNG、SVG 与 PDF 的输出目录。",
    )
    args = parser.parse_args()
    if not args.demo:
        parser.error("本模板仅在显式传入 --demo 时生成合成示例。")
    return args


if __name__ == "__main__":
    arguments = parse_args()
    render(arguments.output_dir)
