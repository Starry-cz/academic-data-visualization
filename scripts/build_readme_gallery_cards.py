#!/usr/bin/env python3
"""Build consistently sized README gallery cards without cropping scientific evidence."""

from __future__ import annotations

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
ATLAS_DIR = ROOT / "assets" / "figure-atlas"
CARD_DIR = ATLAS_DIR / "readme-cards"

# 近方形图以 3 列展示；横向图以 2 列展示。统一画布避免 README 两侧高度不齐。
SQUARE_SPECS = (
    (ATLAS_DIR / "3Dheatmap.png", "3Dheatmap.png"),
    (ATLAS_DIR / "PCA.png", "PCA.png"),
    (ATLAS_DIR / "auroc.png", "auroc.png"),
    (ATLAS_DIR / "CorrelationDensity.png", "CorrelationDensity.png"),
    (ATLAS_DIR / "Correlationmatrix.png", "Correlationmatrix.png"),
    (ATLAS_DIR / "radar.png", "radar.png"),
    (ATLAS_DIR / "RidgePlot.png", "RidgePlot.png"),
    (ROOT / "assets" / "figures" / "BubbleScatter" / "bubble_scatter.png", "bubble_scatter.png"),
    (
        ROOT / "assets" / "figures" / "CorrelationBubbleMatrix" / "correlation_bubble_matrix.png",
        "correlation_bubble_matrix.png",
    ),
    (
        ROOT / "assets" / "figures" / "CorrelationNetwork" / "correlation_network.png",
        "correlation_network.png",
    ),
)
WIDE_SPECS = (
    (ATLAS_DIR / "bar.png", "bar.png"),
    (ATLAS_DIR / "GroupedBarChart.png", "GroupedBarChart.png"),
    (ATLAS_DIR / "MantelCorrelation.png", "MantelCorrelation.png"),
    (ATLAS_DIR / "violin_chart.png", "violin_chart.png"),
    (ATLAS_DIR / "trend.png", "trend.png"),
    (ATLAS_DIR / "StackedBarScatter.png", "StackedBarScatter.png"),
    (ATLAS_DIR / "Frequency_3DHeatmap.png", "Frequency_3DHeatmap.png"),
    (ATLAS_DIR / "sankey.png", "sankey.png"),
    (ROOT / "assets" / "figures" / "StackedArea" / "stacked_area.png", "stacked_area.png"),
    (
        ROOT / "assets" / "figures" / "GeographicBubbleMap" / "geographic_bubble_map.png",
        "geographic_bubble_map.png",
    ),
)
MATERIAL_SPECS = (
    (
        ROOT / "assets" / "figures" / "XPSPeakDeconvolution" / "xps_peak_deconvolution.png",
        "xps_peak_deconvolution.png",
    ),
    (
        ROOT / "assets" / "figures" / "EXAFSWaveletMap" / "exafs_wavelet_map.png",
        "exafs_wavelet_map.png",
    ),
)
NETWORK_SPECS = (
    (
        ROOT / "assets" / "figures" / "ChordDiagram" / "chord_diagram.png",
        "chord_diagram.png",
    ),
    (
        ROOT / "assets" / "figures" / "Manifold" / "diffusion_swiss_roll.png",
        "manifold_embedding.png",
    ),
)

SQUARE_CANVAS = (1800, 1800)
WIDE_CANVAS = (1800, 1000)
INSET = 44


def build_card(source_path: Path, output_name: str, canvas_size: tuple[int, int]) -> Path:
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

    output_path = CARD_DIR / output_name
    card.save(output_path, optimize=True)
    return output_path


def main() -> None:
    CARD_DIR.mkdir(parents=True, exist_ok=True)
    rendered = []
    for source_path, output_name in SQUARE_SPECS:
        rendered.append(build_card(source_path, output_name, SQUARE_CANVAS))
    for source_path, output_name in WIDE_SPECS:
        rendered.append(build_card(source_path, output_name, WIDE_CANVAS))
    for source_path, output_name in MATERIAL_SPECS:
        rendered.append(build_card(source_path, output_name, SQUARE_CANVAS))
    for source_path, output_name in NETWORK_SPECS:
        rendered.append(build_card(source_path, output_name, SQUARE_CANVAS))
    print(f"Built {len(rendered)} README gallery cards in {CARD_DIR}")


if __name__ == "__main__":
    main()
