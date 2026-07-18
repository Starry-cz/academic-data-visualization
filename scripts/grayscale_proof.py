"""为科研图生成灰度可读性校样。"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps


def create_grayscale_proof(input_path: Path, output_path: Path) -> Path:
    """按标准亮度转换 PNG，并在有透明通道时保留原透明度。"""
    if not input_path.is_file():
        raise FileNotFoundError(f"未找到输入图像：{input_path}")

    with Image.open(input_path) as source:
        rgba = source.convert("RGBA")
        # 灰度校样只改变颜色信息，保留透明元素的覆盖关系以便真实审查。
        luminance = ImageOps.grayscale(rgba.convert("RGB"))
        proof = Image.merge("LA", (luminance, rgba.getchannel("A"))).convert("RGBA")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        proof.save(output_path)

    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="为科研图生成灰度可读性校样")
    parser.add_argument("input", type=Path, help="待审查的 PNG 预览图")
    parser.add_argument("--output", type=Path, help="灰度校样输出路径")
    args = parser.parse_args()

    output_path = args.output or args.input.with_name(f"{args.input.stem}-grayscale.png")
    proof_path = create_grayscale_proof(args.input, output_path)
    print(f"[GRAY PROOF] {proof_path}")


if __name__ == "__main__":
    main()
