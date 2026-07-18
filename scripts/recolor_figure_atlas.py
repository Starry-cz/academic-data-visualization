"""按主题重绘 README 图表索引缩略图的颜色层，不改变图形结构或文字。"""

from __future__ import annotations

import argparse
import colorsys
import io
import json
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
LIBRARY_PATH = ROOT / "references" / "palette-library.json"
# 仓库基线中有一张约 1.23 亿像素的已知索引图；保留炸弹保护，但提高到其实际尺寸。
Image.MAX_IMAGE_PIXELS = 150_000_000
# 索引中实际引用的缩略图；显式列出可避免意外改动非索引资产。
INDEX_THUMBNAILS = (
    "3Dheatmap.png", "auroc.png", "bar.png", "CorrelationDensity.png",
    "Correlationmatrix.png", "density_heatmap.png", "Frequency_3DHeatmap.png",
    "GroupCorrelationmatrix.png", "GroupedBarChart.png", "MantelCorrelation.png",
    "PCA.png", "radar.png", "RidgePlot.png", "sankey.png",
    "StackedBarScatter.png", "trend.png", "violin_chart.png",
)


def read_theme(theme_id: str) -> dict[str, object]:
    """读取唯一主题库中的指定配色。"""
    with LIBRARY_PATH.open(encoding="utf-8") as handle:
        library = json.load(handle)
    for theme in library["themes"]:
        if theme["id"] == theme_id:
            return theme
    available = ", ".join(theme["id"] for theme in library["themes"])
    raise ValueError(f"未知主题 {theme_id!r}；可用主题：{available}")


def hex_to_rgb(color: str) -> np.ndarray:
    """将 #RRGGBB 转为 0-1 RGB 数组。"""
    return np.array([int(color[index:index + 2], 16) for index in (1, 3, 5)], dtype=float) / 255.0


def hue_targets(theme: dict[str, object]) -> tuple[np.ndarray, np.ndarray]:
    """按主题色建立错位映射，让缩略图明显呈现所选主题。"""
    colors = [hex_to_rgb(color) for color in theme["categorical"]]
    # 色相锚点依次对应红、橙黄、绿、青、蓝、紫、粉。
    # 有意错开原有色相与目标色，避免原图蓝/黄体系在换主题后看起来没有变化。
    hue_anchors = np.array([0.0, 0.14, 0.34, 0.50, 0.63, 0.77, 0.92])
    target_positions = [0.90, 0.00, 0.65, 0.45, 0.75, 0.25, 0.55]
    target_indices = [round(position * (len(colors) - 1)) for position in target_positions]
    return hue_anchors, np.array([colors[index] for index in target_indices])


def nearest_hue_color(hue: np.ndarray, anchors: np.ndarray, targets: np.ndarray) -> np.ndarray:
    """选择环形色相距离最近的目标颜色，避免红色边界处跳色。"""
    distance = np.abs(hue[..., None] - anchors)
    distance = np.minimum(distance, 1.0 - distance)
    return targets[distance.argmin(axis=-1)]


def recolor_image(image: Image.Image, theme: dict[str, object]) -> Image.Image:
    """仅替换有色数据层，保留白底、灰阶网格、文字与轴线。"""
    rgba = np.asarray(image.convert("RGBA"), dtype=np.float32) / 255.0
    rgb = rgba[..., :3]
    alpha = rgba[..., 3:4]
    flat = rgb.reshape(-1, 3)
    hsv = np.array([colorsys.rgb_to_hsv(*pixel) for pixel in flat], dtype=np.float32).reshape(rgb.shape)
    hue, saturation, value = hsv[..., 0], hsv[..., 1], hsv[..., 2]
    anchors, targets = hue_targets(theme)
    target_rgb = nearest_hue_color(hue, anchors, targets)

    # 低饱和度像素通常承担文字、轴线、网格或背景信息，必须保持中性。
    chromatic = (saturation >= 0.16) & (value >= 0.12)
    # 保留抗锯齿与透明度造成的明暗层次，避免把密度与热图压成纯色块。
    color_weight = np.clip((saturation - 0.12) / 0.72, 0.0, 1.0)[..., None]
    shade = (0.52 + 0.48 * value)[..., None]
    toned_target = np.clip(target_rgb * shade, 0.0, 1.0)
    recolored = (1.0 - color_weight) * rgb + color_weight * toned_target
    rgb[chromatic] = recolored[chromatic]

    output = np.concatenate([rgb, alpha], axis=-1)
    return Image.fromarray(np.round(output * 255).astype(np.uint8), mode="RGBA")


def resize_for_readme(image: Image.Image, max_dimension: int) -> Image.Image:
    """按 README 缩略图用途限制超大图尺寸，避免无效的百兆像素处理。"""
    if max(image.size) <= max_dimension:
        return image
    scale = max_dimension / max(image.size)
    size = tuple(max(1, round(dimension * scale)) for dimension in image.size)
    return image.resize(size, Image.Resampling.LANCZOS)


def read_baseline_image(revision: str, filename: str) -> Image.Image:
    """从主题改造前的 Git 版本读取基线，保证脚本可重复执行。"""
    object_name = f"{revision}:assets/figure-atlas/{filename}"
    result = subprocess.run(
        ["git", "-c", f"safe.directory={ROOT.as_posix()}", "show", object_name],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return Image.open(io.BytesIO(result.stdout)).copy()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--theme", default="pastel-omics", help="palette-library.json 中的主题 ID")
    parser.add_argument("--source-revision", default="b60c432", help="包含原始缩略图的 Git 提交")
    parser.add_argument("--max-dimension", type=int, default=1800, help="README 缩略图的最长边像素")
    parser.add_argument(
        "--filenames",
        nargs="*",
        choices=INDEX_THUMBNAILS,
        help="仅重绘指定索引缩略图；未提供时重绘全部。",
    )
    args = parser.parse_args()

    theme = read_theme(args.theme)
    output_dir = ROOT / "assets" / "figure-atlas"
    filenames = args.filenames or INDEX_THUMBNAILS
    for filename in filenames:
        baseline = resize_for_readme(read_baseline_image(args.source_revision, filename), args.max_dimension)
        recolor_image(baseline, theme).convert("RGB").save(output_dir / filename)


if __name__ == "__main__":
    main()
