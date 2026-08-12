#!/usr/bin/env python3
"""Generate README previews with the Nature-ready accessible visual system.

The data are deterministic synthetic examples.  They exist only to show the
visual grammar of the skill: semantic colourblind-safe colours, light structure,
and a clear evidence hierarchy across panels.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib as mpl
# README 预览在 CI 与无桌面环境中运行，必须在导入 pyplot 前固定为无界面后端。
mpl.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, rgb_to_hsv
from matplotlib.patches import Ellipse
from PIL import Image

from visual_qa import audit_figure


ROOT = Path(__file__).resolve().parents[1]
ATLAS_DIR = ROOT / "assets" / "figure-atlas"

# 统一视觉令牌：与 references/color-palettes.md 保持一致，防止预览和实际脚本脱节。
INK = "#1A1A1A"
AXIS = "#1A1A1A"
GRID = "#D7DEE6"
MIST_BLUE = "#0072B2"
SAGE = "#009E73"
APRICOT = "#E69F00"
MAUVE = "#CC79A7"
TERRACOTTA = "#D55E00"
TEAL = "#56B4E9"
PALETTE = [MIST_BLUE, SAGE, APRICOT, MAUVE, TERRACOTTA, TEAL]

# 重点图索引展示独立主题，不把单一配色误当作所有图型的默认外观。
# 键值对应原图中常见的色相角色：蓝色是主证据，红色是强调，其他色为并列比较。
GALLERY_THEMES = {
    "teal-genome": {"red": "#3D3539", "orange": "#8B84A3", "green": "#8CD1B2", "blue": "#0F9EA8", "mauve": "#45728F"},
    "bright-bio": {"red": "#E36889", "orange": "#F7A63A", "green": "#80C662", "blue": "#557CFF", "mauve": "#866AD2"},
    "pastel-omics": {"red": "#F6B593", "orange": "#EFC372", "green": "#84C492", "blue": "#81CAEA", "mauve": "#C0A3ED"},
    "method-blueprint": {"red": "#B64342", "orange": "#8BCF8B", "green": "#42949E", "blue": "#0F4D92", "mauve": "#3775BA"},
    "literature-clinical": {"red": "#D87B67", "orange": "#D4B261", "green": "#72AE9E", "blue": "#477E95", "mauve": "#9C86B3"},
    "electrochemistry": {"red": "#E26E67", "orange": "#F8D1B5", "green": "#A4D86A", "blue": "#509CBA", "mauve": "#91BFDB"},
    "soft-academic": {"red": "#F8B9B8", "orange": "#FFC6BC", "green": "#A5CDE2", "blue": "#5FA3CB", "mauve": "#668FCA"},
    "warm-cool-kinetics": {"red": "#D7312D", "orange": "#F2724D", "green": "#FEE395", "blue": "#115FA4", "mauve": "#6090C1"},
    "aquifer-recovery": {"red": "#F599A1", "orange": "#FCD590", "green": "#73C79E", "blue": "#5299CC", "mauve": "#A577AD"},
}

GALLERY_THEME_BY_FILE = {
    "3Dheatmap.png": "teal-genome",
    "auroc.png": "method-blueprint",
    "bar.png": "bright-bio",
    "CorrelationDensity.png": "soft-academic",
    "Correlationmatrix.png": "teal-genome",
    "density_heatmap.png": "pastel-omics",
    "Frequency_3DHeatmap.png": "electrochemistry",
    "GroupCorrelationmatrix.png": "literature-clinical",
    "GroupedBarChart.png": "bright-bio",
    "MantelCorrelation.png": "literature-clinical",
    "PCA.png": "pastel-omics",
    "radar.png": "soft-academic",
    "RidgePlot.png": "literature-clinical",
    "sankey.png": "method-blueprint",
    "StackedBarScatter.png": "warm-cool-kinetics",
    "trend.png": "aquifer-recovery",
    "violin_chart.png": "soft-academic",
}


def configure_style() -> None:
    """Set a compact white-background publication style for all preview panels."""
    mpl.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "DejaVu Sans"],
        "font.size": 8,
        "axes.titlesize": 10,
        "axes.labelsize": 8.5,
        "xtick.labelsize": 7.5,
        "ytick.labelsize": 7.5,
        "legend.fontsize": 7.5,
        "axes.linewidth": 0.65,
        "axes.labelcolor": INK,
        "xtick.color": AXIS,
        "ytick.color": AXIS,
        "xtick.major.width": 0.6,
        "ytick.major.width": 0.6,
        "xtick.major.size": 3,
        "ytick.major.size": 3,
        "grid.color": GRID,
        "grid.linewidth": 0.65,
        "grid.alpha": 0.9,
        "axes.axisbelow": True,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "legend.frameon": False,
        "savefig.dpi": 260,
        "savefig.facecolor": "#FFFFFF",
        "pdf.fonttype": 42,
        "svg.fonttype": "none",
    })


def style_axis(ax: plt.Axes, *, grid: bool = True) -> None:
    """Keep the data layer prominent and render only necessary structure."""
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(AXIS)
        ax.spines[side].set_linewidth(0.65)
    if grid:
        ax.grid(axis="y")


def panel_label(ax: plt.Axes, label: str) -> None:
    ax.text(-0.12, 1.08, f"({label})", transform=ax.transAxes, color=INK,
            fontsize=11, fontweight="bold", va="top", ha="left")


def add_ridges(ax: plt.Axes) -> None:
    """Draw compact distributions with low-saturation fills and direct labels."""
    x = np.linspace(-3.7, 3.7, 320)
    labels = ["Baseline", "Treatment A", "Treatment B", "Follow-up", "Reference"]
    means = [-0.55, -0.15, 0.32, 0.58, 0.05]
    spreads = [0.82, 0.68, 0.74, 0.62, 0.9]
    colors = [MIST_BLUE, SAGE, APRICOT, MAUVE, TEAL]

    for index, (label, mean, spread, color) in enumerate(zip(labels, means, spreads, colors)):
        base = len(labels) - 1 - index
        density = np.exp(-0.5 * ((x - mean) / spread) ** 2)
        density /= density.max()
        # 轻微扰动让示例更接近真实经验分布，不改变可读性。
        density *= 0.96 + 0.04 * np.sin(x * (index + 2) + index * 0.61)
        ax.fill_between(x, base, base + density * 0.64, color=color, alpha=0.84, linewidth=0)
        ax.plot(x, base + density * 0.64, color=INK, linewidth=0.95)
        ax.hlines(base, -3.8, 3.8, color=GRID, linewidth=0.75)
        ax.text(-4.12, base + 0.1, label, color=INK, ha="right", va="center", fontsize=7.5)

    ax.set_xlim(-4.0, 4.15)
    ax.set_ylim(-0.3, len(labels) - 0.1)
    ax.set_yticks([])
    ax.set_xlabel("Standardized value")
    ax.set_title("Distribution profiles", loc="left", pad=8, color=INK, fontweight="bold")
    style_axis(ax, grid=False)
    ax.spines["left"].set_visible(False)


def add_correlation(ax: plt.Axes, fig: plt.Figure) -> None:
    """Show signed associations with a neutral midpoint and sparse labels."""
    labels = ["Signal", "Response", "Score", "Load", "Risk", "Recovery"]
    matrix = np.array([
        [1.00, 0.54, 0.34, -0.21, -0.48, 0.42],
        [0.54, 1.00, 0.28, -0.08, -0.33, 0.51],
        [0.34, 0.28, 1.00, 0.46, -0.22, 0.18],
        [-0.21, -0.08, 0.46, 1.00, 0.38, -0.18],
        [-0.48, -0.33, -0.22, 0.38, 1.00, -0.45],
        [0.42, 0.51, 0.18, -0.18, -0.45, 1.00],
    ])
    cmap = LinearSegmentedColormap.from_list("muted_diverging", ["#5F8195", "#F7F8F6", TERRACOTTA])
    image = ax.imshow(matrix, cmap=cmap, vmin=-1, vmax=1, aspect="equal")
    ax.set_xticks(range(len(labels)), labels, rotation=38, ha="right")
    ax.set_yticks(range(len(labels)), labels)
    ax.tick_params(length=0)
    for row in range(matrix.shape[0]):
        for column in range(matrix.shape[1]):
            value = matrix[row, column]
            if row == column or abs(value) >= 0.33:
                text_color = "white" if abs(value) > 0.5 else INK
                ax.text(column, row, f"{value:+.2f}", ha="center", va="center",
                        fontsize=6.7, color=text_color, fontweight="bold" if abs(value) > 0.45 else "normal")
    ax.set_xticks(np.arange(-0.5, len(labels), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(labels), 1), minor=True)
    ax.grid(which="minor", color="white", linewidth=1.3)
    ax.tick_params(which="minor", bottom=False, left=False)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_title("Correlation structure", loc="left", pad=8, color=INK, fontweight="bold")
    colorbar = fig.colorbar(image, ax=ax, fraction=0.046, pad=0.04, ticks=[-1, 0, 1])
    colorbar.outline.set_visible(False)
    colorbar.ax.tick_params(length=0, labelsize=6.8, color=AXIS)
    colorbar.set_label("r", color=INK, fontsize=7.5, labelpad=2)


def add_pca(ax: plt.Axes) -> None:
    """Render dense observations with restrained groups and an evidence-first legend."""
    centers = [(-1.05, -0.42), (0.62, -0.16), (-0.04, 0.95)]
    scales = [(0.58, 0.37), (0.47, 0.43), (0.55, 0.34)]
    colors = [MIST_BLUE, SAGE, MAUVE]
    names = ["Cluster 1", "Cluster 2", "Cluster 3"]
    for group_index, (center, scale, color, name) in enumerate(zip(centers, scales, colors, names)):
        # Fibonacci 圆盘采样提供均匀、可复现的点云，不依赖随机数生成器。
        point_index = np.arange(210)
        radius = np.sqrt((point_index + 0.5) / len(point_index))
        angle = point_index * 2.399963229728653 + group_index * 0.83
        points = np.column_stack((
            center[0] + np.cos(angle) * radius * scale[0] * 1.8,
            center[1] + np.sin(angle) * radius * scale[1] * 1.8,
        ))
        ax.scatter(points[:, 0], points[:, 1], s=8, color=color, alpha=0.52, edgecolors="none", rasterized=True)
        ellipse = Ellipse(center, width=scale[0] * 3.8, height=scale[1] * 3.8,
                          facecolor="none", edgecolor=color, linewidth=1.1, linestyle=(0, (4, 2)))
        ax.add_patch(ellipse)
        ax.text(center[0], center[1], name[-1], ha="center", va="center", fontsize=7.5,
                color=INK, fontweight="bold",
                bbox={"boxstyle": "round,pad=0.18", "facecolor": "white", "edgecolor": color, "linewidth": 0.7})
    ax.axhline(0, color=GRID, linewidth=0.75, zorder=0)
    ax.axvline(0, color=GRID, linewidth=0.75, zorder=0)
    ax.set_xlabel("PC1 (34.2%)")
    ax.set_ylabel("PC2 (21.6%)")
    ax.set_title("Sample separation", loc="left", pad=8, color=INK, fontweight="bold")
    style_axis(ax, grid=False)


def add_contributions(subgrid: mpl.gridspec.GridSpecFromSubplotSpec) -> tuple[plt.Axes, plt.Axes]:
    """Use aligned horizontal bars to make the model contribution comparison scannable."""
    ax_left = plt.subplot(subgrid[0, 0])
    ax_right = plt.subplot(subgrid[0, 1])
    labels_left = ["Feature A", "Feature B", "Feature C", "Feature D", "Feature E"]
    labels_right = ["Feature F", "Feature G", "Feature H", "Feature I", "Feature J"]
    values_left = np.array([0.31, 0.26, 0.22, 0.16, 0.11])
    values_right = np.array([0.29, 0.24, 0.18, 0.13, 0.08])
    colors_left = [MIST_BLUE, MIST_BLUE, SAGE, APRICOT, APRICOT]
    colors_right = [MAUVE, MAUVE, SAGE, TERRACOTTA, APRICOT]

    for ax, labels, values, colors, title in [
        (ax_left, labels_left, values_left, colors_left, "Axis 1"),
        (ax_right, labels_right, values_right, colors_right, "Axis 2"),
    ]:
        positions = np.arange(len(labels))[::-1]
        ax.barh(positions, values, color=colors, height=0.56, edgecolor="none")
        ax.set_yticks(positions, labels)
        ax.set_xlim(0, 0.36)
        ax.set_xticks([0, 0.15, 0.30], ["0", "0.15", "0.30"])
        ax.axvline(0.15, color=GRID, linewidth=0.8, linestyle=(0, (2, 2)))
        for y, value in zip(positions, values):
            ax.text(value + 0.008, y, f"{value:.2f}", va="center", ha="left", fontsize=6.3, color=INK)
        ax.set_title(title, fontsize=8, color=INK, fontweight="bold", pad=5)
        style_axis(ax, grid=False)
        ax.spines["left"].set_visible(False)
        ax.tick_params(axis="y", length=0)
    return ax_left, ax_right


def save_preview() -> Path:
    """Create the four-panel README hero preview from deterministic synthetic data."""
    # README 预览同时作为双栏（183 mm）可复用示例，因此先按最终物理宽度出图。
    fig = plt.figure(figsize=(7.2, 4.75), facecolor="white")
    grid = fig.add_gridspec(2, 2, width_ratios=[1.0, 1.12], height_ratios=[0.96, 1.0], wspace=0.30, hspace=0.30)
    ax_corr = fig.add_subplot(grid[0, 0])
    ax_ridge = fig.add_subplot(grid[0, 1])
    ax_pca = fig.add_subplot(grid[1, 0])
    contribution_grid = grid[1, 1].subgridspec(1, 2, wspace=0.55)
    fig.subplots_adjust(left=0.06, right=0.985, top=0.93, bottom=0.08, wspace=0.30, hspace=0.34)

    add_correlation(ax_corr, fig)
    add_ridges(ax_ridge)
    add_pca(ax_pca)
    ax_left, _ = add_contributions(contribution_grid)
    panel_label(ax_corr, "a")
    panel_label(ax_ridge, "b")
    panel_label(ax_pca, "c")
    panel_label(ax_left, "d")
    output = ATLAS_DIR / "preview.png"
    report = audit_figure(fig, output.stem)
    print(f"[QA PASS] {report.figure_name}: {report.checked_texts} texts, {report.checked_legends} legends")
    fig.savefig(output, dpi=600, bbox_inches="tight", pad_inches=0.08)
    fig.savefig(output.with_suffix(".svg"), format="svg", bbox_inches="tight", pad_inches=0.08)
    fig.savefig(output.with_suffix(".pdf"), format="pdf", bbox_inches="tight", pad_inches=0.08)
    fig.savefig(output.with_suffix(".tiff"), format="tiff", dpi=600, bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)
    return output


def save_secondary_preview() -> Path:
    """Create a second README figure showing distribution, effect and feature evidence layers."""
    fig = plt.figure(figsize=(7.2, 3.35), constrained_layout=True, facecolor="white")
    grid = fig.add_gridspec(1, 3, width_ratios=[1.05, 1.1, 0.95], wspace=0.32)
    ax_dist = fig.add_subplot(grid[0, 0])
    ax_effect = fig.add_subplot(grid[0, 1])
    ax_heat = fig.add_subplot(grid[0, 2])

    groups = ["Control", "Low dose", "High dose", "Recovery"]
    means = [0.0, 0.34, 0.67, 0.22]
    colors = [MIST_BLUE, SAGE, APRICOT, MAUVE]
    observation = np.arange(42)
    base_shape = (
        0.72 * np.sin(observation * 1.71)
        + 0.33 * np.cos(observation * 0.63)
        + 0.16 * np.sin(observation * 2.93)
    )
    samples = [mean + (0.35 + i * 0.025) * base_shape for i, mean in enumerate(means)]
    violin = ax_dist.violinplot(samples, positions=np.arange(4), widths=0.75, showmeans=False, showmedians=False, showextrema=False)
    for body, color in zip(violin["bodies"], colors):
        body.set_facecolor(color)
        body.set_edgecolor(INK)
        body.set_linewidth(0.65)
        body.set_alpha(0.72)
    for index, (sample, color) in enumerate(zip(samples, colors)):
        jitter = 0.12 * np.sin(observation * 2.17 + index * 0.73)
        ax_dist.scatter(np.full(len(sample), index) + jitter, sample, s=8, color=color, alpha=0.36, edgecolors="none")
        median = np.median(sample)
        ax_dist.hlines(median, index - 0.2, index + 0.2, color=INK, linewidth=1.15)
    ax_dist.set_xticks(range(4), groups, rotation=20, ha="right")
    ax_dist.set_ylabel("Response score")
    ax_dist.set_title("Individual distributions", loc="left", color=INK, fontweight="bold", pad=8)
    style_axis(ax_dist)
    panel_label(ax_dist, "a")

    effects = np.array([-0.42, -0.24, -0.05, 0.12, 0.26, 0.48])
    errors = np.array([0.11, 0.10, 0.09, 0.08, 0.12, 0.10])
    effect_labels = ["Marker 1", "Marker 2", "Marker 3", "Marker 4", "Marker 5", "Marker 6"]
    y = np.arange(len(effects))[::-1]
    point_colors = [MIST_BLUE if value < 0 else TERRACOTTA for value in effects]
    ax_effect.axvline(0, color=AXIS, linewidth=0.8)
    ax_effect.errorbar(effects, y, xerr=errors, fmt="none", ecolor=AXIS, elinewidth=0.9, capsize=2, zorder=1)
    ax_effect.scatter(effects, y, s=35, color=point_colors, edgecolors="white", linewidths=0.7, zorder=2)
    ax_effect.set_yticks(y, effect_labels)
    ax_effect.set_xlabel("Standardized effect (95% CI)")
    ax_effect.set_title("Effect estimates", loc="left", color=INK, fontweight="bold", pad=8)
    style_axis(ax_effect, grid=False)
    ax_effect.spines["left"].set_visible(False)
    ax_effect.tick_params(axis="y", length=0)
    panel_label(ax_effect, "b")

    heat = np.array([
        [0.20, 0.45, 0.65, 0.78, 0.38],
        [0.12, 0.31, 0.58, 0.72, 0.41],
        [0.08, 0.23, 0.46, 0.61, 0.35],
        [0.05, 0.19, 0.32, 0.50, 0.27],
        [0.02, 0.14, 0.28, 0.39, 0.18],
    ])
    cmap = LinearSegmentedColormap.from_list("mist", ["#F4F7F6", "#BCD3DE", MIST_BLUE])
    ax_heat.imshow(heat, cmap=cmap, vmin=0, vmax=0.8, aspect="auto")
    ax_heat.set_xticks(range(5), ["T1", "T2", "T3", "T4", "T5"])
    ax_heat.set_yticks(range(5), ["Pathway A", "Pathway B", "Pathway C", "Pathway D", "Pathway E"])
    # 总标题与面板标签已说明证据层次；不在狭窄热图上再放会越界的长标题。
    for row in range(heat.shape[0]):
        for column in range(heat.shape[1]):
            ax_heat.text(column, row, f"{heat[row, column]:.2f}", ha="center", va="center",
                         fontsize=6.3, color="white" if heat[row, column] > 0.52 else INK)
    ax_heat.set_xticks(np.arange(-0.5, 5, 1), minor=True)
    ax_heat.set_yticks(np.arange(-0.5, 5, 1), minor=True)
    ax_heat.grid(which="minor", color="white", linewidth=1.2)
    ax_heat.tick_params(which="both", length=0)
    for spine in ax_heat.spines.values():
        spine.set_visible(False)
    panel_label(ax_heat, "c")

    # 交给 constrained layout 预留标题空间，避免总标题压住子图标题和面板标签。
    fig.suptitle("Evidence layers: distribution, effect and feature structure", x=0.02, ha="left",
                 fontsize=13, color=INK, fontweight="bold")
    output = ATLAS_DIR / "data-figure.png"
    report = audit_figure(fig, output.stem)
    print(f"[QA PASS] {report.figure_name}: {report.checked_texts} texts, {report.checked_legends} legends")
    fig.savefig(output, dpi=600, bbox_inches="tight", pad_inches=0.08)
    fig.savefig(output.with_suffix(".svg"), format="svg", bbox_inches="tight", pad_inches=0.08)
    fig.savefig(output.with_suffix(".pdf"), format="pdf", bbox_inches="tight", pad_inches=0.08)
    fig.savefig(output.with_suffix(".tiff"), format="tiff", dpi=600, bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)
    return output


def recolor_gallery_assets() -> int:
    """按图型语义分配主题，保留几何和标注，不再全库套用同一组色。"""
    count = 0
    for image_path in sorted(ATLAS_DIR.glob("*.png")):
        if image_path.name not in GALLERY_THEME_BY_FILE:
            continue
        theme_id = GALLERY_THEME_BY_FILE[image_path.name]
        targets = {
            role: np.array(mpl.colors.to_rgb(value))
            for role, value in GALLERY_THEMES[theme_id].items()
        }
        image = Image.open(image_path).convert("RGB")
        pixels = np.asarray(image, dtype=np.float32) / 255.0
        hsv = rgb_to_hsv(pixels)
        hue, saturation, value = hsv[..., 0], hsv[..., 1], hsv[..., 2]
        result = pixels.copy()

        # 无彩色区域保持亮度；只把深色文字/轴线统一为蓝灰墨色。
        neutral = saturation < 0.12
        dark_neutral = neutral & (value < 0.62)
        if np.any(dark_neutral):
            ink = np.array(mpl.colors.to_rgb(INK))
            weight = (0.72 - value[dark_neutral])[:, None] / 0.72
            result[dark_neutral] = pixels[dark_neutral] * (1 - weight * 0.4) + ink * (weight * 0.4)

        colored = ~neutral
        hue_targets = np.empty_like(pixels)
        hue_targets[:] = targets["blue"]
        hue_targets[(hue < 0.055) | (hue >= 0.94)] = targets["red"]
        hue_targets[(hue >= 0.055) & (hue < 0.17)] = targets["orange"]
        hue_targets[(hue >= 0.17) & (hue < 0.47)] = targets["green"]
        hue_targets[(hue >= 0.70) & (hue < 0.94)] = targets["mauve"]
        # 色彩越饱和，保留的目标色越多；低饱和背景保持轻盈。
        blend = np.clip(0.32 + 0.58 * saturation, 0.32, 0.90)[..., None]
        result[colored] = (1 - blend[colored]) + hue_targets[colored] * blend[colored]
        output = Image.fromarray(np.uint8(np.clip(result, 0, 1) * 255), mode="RGB")
        output.save(image_path, optimize=True)
        count += 1
    return count


def main() -> None:
    ATLAS_DIR.mkdir(parents=True, exist_ok=True)
    configure_style()
    hero = save_preview()
    secondary = save_secondary_preview()
    recolored = recolor_gallery_assets()
    print(f"Saved {hero}")
    print(f"Saved {secondary}")
    print(f"Recolored {recolored} gallery thumbnails")


if __name__ == "__main__":
    main()
