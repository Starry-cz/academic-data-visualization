#!/usr/bin/env python3
"""Build a contact sheet for human review of verified template previews."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--grayscale", action="store_true", help="Use the stored grayscale evidence instead of colour previews")
    args = parser.parse_args()
    pattern = "*/example-output/figure-grayscale.png" if args.grayscale else "*/preview.png"
    previews = sorted((ROOT / "templates" / "production-verified").glob(pattern))
    if not previews:
        raise SystemExit("No verified template previews were found")

    columns = 3
    cell_width, cell_height = 720, 540
    label_height = 44
    rows = (len(previews) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * cell_width, rows * (cell_height + label_height)), "white")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 24)
    for index, preview in enumerate(previews):
        row, column = divmod(index, columns)
        with Image.open(preview) as source:
            image = source.convert("RGB")
            image.thumbnail((cell_width - 24, cell_height - 24), Image.Resampling.LANCZOS)
        # 单元格内居中，保留原始长宽比，避免审阅图二次拉伸误导判断。
        x = column * cell_width + (cell_width - image.width) // 2
        y = row * (cell_height + label_height) + 12
        sheet.paste(image, (x, y))
        label = preview.parents[1].name if args.grayscale else preview.parent.name
        label_box = draw.textbbox((0, 0), label, font=font)
        label_x = column * cell_width + (cell_width - (label_box[2] - label_box[0])) // 2
        label_y = row * (cell_height + label_height) + cell_height + 6
        draw.text((label_x, label_y), label, fill="#111827", font=font)
        draw.rectangle(
            (
                column * cell_width,
                row * (cell_height + label_height),
                (column + 1) * cell_width - 1,
                (row + 1) * (cell_height + label_height) - 1,
            ),
            outline="#cbd5e1",
            width=1,
        )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(args.output, optimize=True)
    print(args.output.resolve())


if __name__ == "__main__":
    main()
