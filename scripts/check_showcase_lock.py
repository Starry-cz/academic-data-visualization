#!/usr/bin/env python3
"""Protect the maintainer-approved README gallery and palette assets from drift."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOCK_PATH = ROOT / "references" / "showcase-lock.json"
FEATURED_ORDER = [
    "3Dheatmap.png",
    "PCA.png",
    "auroc.png",
    "CorrelationDensity.png",
    "Correlationmatrix.png",
    "radar.png",
    "RidgePlot.png",
    "bubble_scatter.png",
    "correlation_bubble_matrix.png",
    "correlation_network.png",
    "chord_diagram.png",
    "phate_trajectory.png",
    "bar.png",
    "GroupedBarChart.png",
    "MantelCorrelation.png",
    "violin_chart.png",
    "trend.png",
    "StackedBarScatter.png",
    "Frequency_3DHeatmap.png",
    "sankey.png",
    "stacked_area.png",
    "geographic_bubble_map.png",
    "xps_peak_deconvolution.png",
    "exafs_wavelet_map.png",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def snapshot() -> dict:
    protected = [
        ROOT / "references" / "palette-library.json",
        ROOT / "references" / "color-palettes.md",
        *sorted((ROOT / "assets" / "palette-gallery").glob("*")),
        *[ROOT / "assets" / "figure-atlas" / "readme-cards" / name for name in FEATURED_ORDER],
    ]
    files = {
        path.relative_to(ROOT).as_posix(): sha256(path)
        for path in protected
        if path.is_file()
    }
    readme_orders = {}
    for name in ("README.md", "README_EN.md"):
        text = (ROOT / name).read_text(encoding="utf-8")
        readme_orders[name] = re.findall(r"assets/figure-atlas/readme-cards/([^\"?]+\.png)", text)
    return {
        "lock_version": "1.0.0",
        "featured_order": FEATURED_ORDER,
        "readme_orders": readme_orders,
        "sha256": files,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Explicitly accept the current approved gallery and palettes")
    args = parser.parse_args()
    current = snapshot()
    if any(order != FEATURED_ORDER for order in current["readme_orders"].values()):
        raise SystemExit("README featured chart order differs from the maintainer-approved 24-card set")
    if args.write:
        LOCK_PATH.write_text(json.dumps(current, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {LOCK_PATH.relative_to(ROOT)}")
        return
    expected = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    if current != expected:
        raise SystemExit("Featured figures or palette assets changed; obtain maintainer approval before refreshing showcase-lock.json")
    print("Showcase and palette lock: PASS")


if __name__ == "__main__":
    main()
