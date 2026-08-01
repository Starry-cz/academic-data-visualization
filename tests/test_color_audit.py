from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from color_audit import analyse_svg_colours, audit_svg_colours


def write_svg(path: Path, body: str, background: str = "#FFFFFF") -> None:
    path.write_text(
        f"""\
<svg xmlns="http://www.w3.org/2000/svg" width="200" height="120">
  <g id="figure_1">
    <g id="patch_1"><path d="M 0 0 H 200 V 120 H 0 Z" style="fill: {background}"/></g>
    {body}
  </g>
</svg>
""",
        encoding="utf-8",
    )


class RenderedColourAuditTests(unittest.TestCase):
    def test_actual_text_and_graphics_pass_on_white(self) -> None:
        with tempfile.TemporaryDirectory(prefix="adv-colour-") as temp:
            path = Path(temp) / "figure.svg"
            write_svg(
                path,
                """
<g id="Line2D_1"><path d="M 10 80 L 190 20" style="fill: none; stroke: #0F4D92; stroke-width: 2"/></g>
<text x="10" y="110" style="fill: #272727">Readable label</text>
""",
            )
            findings = {item.check_id: item for item in audit_svg_colours(path, ["#0F4D92"], strict=True)}
        self.assertTrue(findings["COLOR-2"].pass_)
        self.assertTrue(findings["A11Y-3"].pass_)

    def test_compatible_mode_warns_and_strict_mode_fails(self) -> None:
        with tempfile.TemporaryDirectory(prefix="adv-colour-") as temp:
            path = Path(temp) / "figure.svg"
            write_svg(
                path,
                """
<g id="Line2D_1"><path d="M 10 80 L 190 20" style="fill: none; stroke: #BDE2ED; stroke-width: 2"/></g>
<text x="10" y="110" style="fill: #B0B0B0">Faint label</text>
""",
            )
            compatible = {item.check_id: item for item in audit_svg_colours(path, ["#BDE2ED"], strict=False)}
            strict = {item.check_id: item for item in audit_svg_colours(path, ["#BDE2ED"], strict=True)}
        self.assertEqual(compatible["COLOR-2"].severity, "WARN")
        self.assertEqual(compatible["A11Y-3"].severity, "WARN")
        self.assertEqual(strict["COLOR-2"].severity, "FAIL")
        self.assertEqual(strict["A11Y-3"].severity, "FAIL")

    def test_alpha_is_composited_before_contrast(self) -> None:
        with tempfile.TemporaryDirectory(prefix="adv-colour-") as temp:
            path = Path(temp) / "figure.svg"
            write_svg(
                path,
                """
<g id="PathCollection_1"><use href="#marker" style="fill: #0F4D92; fill-opacity: 0.2"/></g>
<text x="10" y="110">Label</text>
""",
            )
            analysis = analyse_svg_colours(path)
            mark = next(sample for sample in analysis.paints if sample.role == "graphical" and sample.channel == "fill")
        self.assertEqual(mark.raw_hex, "#0F4D92")
        self.assertNotEqual(mark.raw_hex, mark.composited_hex)
        self.assertLess(mark.contrast, 3.0)

    def test_uncertainty_band_remains_non_blocking_in_strict_mode(self) -> None:
        with tempfile.TemporaryDirectory(prefix="adv-colour-") as temp:
            path = Path(temp) / "figure.svg"
            write_svg(
                path,
                """
<g id="FillBetweenPolyCollection_1"><path d="M 10 80 L 190 20 V 40 Z" style="fill: #497AB7; fill-opacity: 0.16"/></g>
<text x="10" y="110">Label</text>
""",
            )
            findings = {item.check_id: item for item in audit_svg_colours(path, ["#497AB7"], strict=True)}
        self.assertEqual(findings["COLOR-3"].severity, "WARN")
        self.assertTrue(findings["COLOR-2"].pass_)

    def test_canvas_coloured_text_is_a_local_background_warning(self) -> None:
        with tempfile.TemporaryDirectory(prefix="adv-colour-") as temp:
            path = Path(temp) / "figure.svg"
            write_svg(
                path,
                """
<rect x="10" y="10" width="80" height="50" style="fill: #0F4D92"/>
<text x="20" y="40" style="fill: #FFFFFF">Cell label</text>
""",
            )
            findings = {item.check_id: item for item in audit_svg_colours(path, ["#0F4D92"], strict=True)}
        self.assertTrue(findings["A11Y-3"].pass_)
        self.assertEqual(findings["A11Y-5"].severity, "WARN")

    def test_grayscale_check_uses_only_rendered_categorical_colours(self) -> None:
        with tempfile.TemporaryDirectory(prefix="adv-colour-") as temp:
            path = Path(temp) / "figure.svg"
            write_svg(
                path,
                """
<g id="Line2D_1"><path d="M 10 30 L 190 30" style="fill: none; stroke: #767676; stroke-width: 2"/></g>
<g id="Line2D_2"><path d="M 10 60 L 190 60" style="fill: none; stroke: #808080; stroke-width: 2"/></g>
<text x="10" y="110">Label</text>
""",
            )
            findings = {
                item.check_id: item
                for item in audit_svg_colours(path, ["#767676", "#808080", "#F6CFCB"], strict=True)
            }
        self.assertEqual(findings["A11Y-4"].severity, "WARN")
        self.assertIn("#767676/#808080", findings["A11Y-4"].detail)
        self.assertNotIn("#F6CFCB", findings["A11Y-4"].detail)

    def test_embedded_image_requires_visual_colour_review(self) -> None:
        with tempfile.TemporaryDirectory(prefix="adv-colour-") as temp:
            path = Path(temp) / "figure.svg"
            write_svg(path, '<image x="10" y="10" width="80" height="50" href="data:image/png;base64,AA=="/>')
            findings = {item.check_id: item for item in audit_svg_colours(path, [], strict=True)}
        self.assertEqual(findings["COLOR-4"].severity, "WARN")
        self.assertIn("embedded raster/image layers: 1", findings["COLOR-4"].detail)


if __name__ == "__main__":
    unittest.main()
