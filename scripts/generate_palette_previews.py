"""生成 README 的主题预览图；示例数据仅用于展示配色，不表达科学结论。"""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

# 在无桌面环境中使用独立缓存和 Agg 后端，避免依赖 Tk 图形界面。
os.environ.setdefault(
    "MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "academic-data-visualization-matplotlib")
)

import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap


ROOT = Path(__file__).resolve().parents[1]
LIBRARY_PATH = ROOT / "references" / "palette-library.json"
OUTPUT_DIR = ROOT / "assets" / "palette-gallery"


def apply_preview_style() -> None:
    """统一预览图字体和可编辑 SVG 文本设置。"""
    mpl.rcParams.update(
        {
            "font.family": "sans-serif",
            # 英文优先 Arial；中文主题名称回退到 Windows 常见中文字体。
            "font.sans-serif": ["Arial", "Microsoft YaHei", "SimHei", "DejaVu Sans", "Liberation Sans"],
            "svg.fonttype": "none",
            "pdf.fonttype": 42,
            "font.size": 8,
            "axes.spines.right": False,
            "axes.spines.top": False,
            "axes.linewidth": 0.75,
            "legend.frameon": False,
        }
    )


def add_panel_label(ax: plt.Axes, label: str) -> None:
    """添加简洁的多面板标签。"""
    ax.text(-0.16, 1.06, label, transform=ax.transAxes, fontweight="bold", va="top")


def render_theme(theme: dict[str, object]) -> None:
    """用四个常见图表展示一个主题的分类、连续和发散配色。"""
    colors = theme["categorical"]
    sequential = theme["sequential"]
    diverging = theme["diverging"]
    ink = "#1A1A1A"
    grid = "#D7DEE6"

    seq_cmap = LinearSegmentedColormap.from_list(f"{theme['id']}-sequential", sequential)
    div_cmap = LinearSegmentedColormap.from_list(f"{theme['id']}-diverging", diverging)
    fig, axes = plt.subplots(2, 2, figsize=(7.2, 4.3), constrained_layout=True)
    # 预览图使用英文主题 ID，避免跨平台导出时缺少中文字体字形。
    fig.suptitle(f"{theme['id']}  |  palette preview", fontsize=13, fontweight="bold", color=ink)

    # a：分组柱状图展示分类色；柱顶数值仅是确定性示例数据。
    values = np.array([3.1, 4.2, 3.6, 5.0])
    x = np.arange(values.size)
    axes[0, 0].bar(x, values, color=colors[:4], width=0.64)
    axes[0, 0].set_xticks(x, ["A", "B", "C", "D"])
    axes[0, 0].set_ylabel("Response")
    axes[0, 0].set_title("Categorical comparison", fontsize=9)
    axes[0, 0].grid(axis="y", color=grid, linewidth=0.45)
    add_panel_label(axes[0, 0], "a")

    # b：折线和置信带展示主次色及透明度的组合。
    t = np.linspace(0, 8, 100)
    for index, color in enumerate(colors[:3]):
        y = 0.15 * index + np.sin(t * (0.72 + index * 0.05)) * 0.22 + 0.48
        axes[0, 1].plot(t, y, color=color, linewidth=2.0, label=f"Group {index + 1}")
        axes[0, 1].fill_between(t, y - 0.07, y + 0.07, color=color, alpha=0.18)
    axes[0, 1].set_xlabel("Time")
    axes[0, 1].set_ylabel("Normalized value")
    axes[0, 1].set_title("Trend with interval", fontsize=9)
    axes[0, 1].legend(loc="upper left", fontsize=7)
    add_panel_label(axes[0, 1], "b")

    # c：矩阵使用主题的发散色，白色固定表示科学零点。
    matrix = np.array(
        [[-1.0, -0.6, -0.2, 0.1, 0.5], [-0.7, -0.3, 0.0, 0.4, 0.9],
         [-0.4, -0.1, 0.2, 0.6, 1.0], [-0.8, -0.5, 0.1, 0.5, 0.8]]
    )
    image = axes[1, 0].imshow(matrix, cmap=div_cmap, vmin=-1, vmax=1, aspect="auto")
    axes[1, 0].set_xticks(range(5), ["S1", "S2", "S3", "S4", "S5"])
    axes[1, 0].set_yticks(range(4), ["G1", "G2", "G3", "G4"])
    axes[1, 0].set_title("Diverging matrix", fontsize=9)
    fig.colorbar(image, ax=axes[1, 0], fraction=0.05, pad=0.03, label="Effect")
    add_panel_label(axes[1, 0], "c")

    # d：连续色带展示丰度、密度等单方向量的编码方式。
    gradient = np.linspace(0, 1, 240).reshape(1, -1)
    axes[1, 1].imshow(gradient, cmap=seq_cmap, aspect="auto")
    axes[1, 1].set_yticks([])
    axes[1, 1].set_xticks([0, 120, 239], ["Low", "Mid", "High"])
    axes[1, 1].set_title("Sequential abundance", fontsize=9)
    for spine in axes[1, 1].spines.values():
        spine.set_visible(False)
    add_panel_label(axes[1, 1], "d")

    output_prefix = OUTPUT_DIR / str(theme["id"])
    # README 使用 PNG；同时保留矢量文件，便于后续编辑或复用主题卡片。
    fig.savefig(output_prefix.with_suffix(".png"), dpi=320, bbox_inches="tight")
    fig.savefig(output_prefix.with_suffix(".svg"), bbox_inches="tight")
    fig.savefig(output_prefix.with_suffix(".pdf"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    """读取唯一的主题库并生成全部 README 预览图。"""
    apply_preview_style()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with LIBRARY_PATH.open(encoding="utf-8") as handle:
        library = json.load(handle)
    for theme in library["themes"]:
        render_theme(theme)


if __name__ == "__main__":
    main()
