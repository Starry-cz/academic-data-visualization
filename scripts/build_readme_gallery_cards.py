#!/usr/bin/env python3
"""Build consistently sized README gallery cards without cropping scientific evidence."""

from __future__ import annotations

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
ATLAS_DIR = ROOT / "assets" / "figure-atlas"
CARD_DIR = ATLAS_DIR / "readme-cards"

# 近方形图以 3 列展示；横向图以 2 列展示。顺序与 README 两个图组保持一致。
SQUARE_FILES = (
    "3Dheatmap.png",
    "density_heatmap.png",
    "PCA.png",
    "auroc.png",
    "CorrelationDensity.png",
    "Correlationmatrix.png",
    "GroupCorrelationmatrix.png",
    "radar.png",
    "RidgePlot.png",
)
WIDE_FILES = (
    "bar.png",
    "GroupedBarChart.png",
    "MantelCorrelation.png",
    "violin_chart.png",
    "trend.png",
    "StackedBarScatter.png",
    "Frequency_3DHeatmap.png",
    "sankey.png",
)

SQUARE_CANVAS = (1800, 1800)
WIDE_CANVAS = (1800, 1000)
INSET = 44


def build_card(source_path: Path, canvas_size: tuple[int, int]) -> Path:
    """Place a source preview on a fixed white canvas while preserving its full aspect ratio."""
    source = Image.open(source_path).convert("RGB")
    max_width = canvas_size[0] - INSET * 2
    max_height = canvas_size[1] - INSET * 2
    scale = min(max_width / source.width, max_height / source.height)
    target_size = (round(source.width * scale), round(source.height * scale))
    preview = source.resize(target_size, Image.Resampling.LANCZOS)

    card = Image.new("RGB", canvas_size, "#FFFFFF")
    offset = ((canvas_size[0] - preview.width) // 2, (canvas_size[1] - preview.height) // 2)
    card.paste(preview, offset)

    output_path = CARD_DIR / source_path.name
    card.save(output_path, optimize=True)
    return output_path


def main() -> None:
    CARD_DIR.mkdir(parents=True, exist_ok=True)
    rendered = []
    for filename in SQUARE_FILES:
        rendered.append(build_card(ATLAS_DIR / filename, SQUARE_CANVAS))
    for filename in WIDE_FILES:
        rendered.append(build_card(ATLAS_DIR / filename, WIDE_CANVAS))
    print(f"Built {len(rendered)} README gallery cards in {CARD_DIR}")


if __name__ == "__main__":
    main()
