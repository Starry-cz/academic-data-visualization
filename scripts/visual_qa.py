"""Matplotlib 成图前的布局审查：拦截图例遮挡、文字越界与文字重叠。"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

from matplotlib.figure import Figure
from matplotlib.transforms import Bbox


@dataclass(frozen=True)
class VisualQAReport:
    """单张图的可读性审查结果。"""

    figure_name: str
    checked_texts: int
    checked_legends: int


def _intersection_area(first: Bbox, second: Bbox) -> float:
    """返回两个屏幕坐标边界框的交叠面积。"""
    width = max(0.0, min(first.x1, second.x1) - max(first.x0, second.x0))
    height = max(0.0, min(first.y1, second.y1) - max(first.y0, second.y0))
    return width * height


def _figure_texts(figure: Figure):
    """收集标题、注释和图例文字；刻度标签不参与成对重叠判定。"""
    texts = list(figure.texts)
    for axis in figure.axes:
        texts.extend(axis.texts)
        texts.extend((axis.title, axis._left_title, axis._right_title))
        legend = axis.get_legend()
        if legend is not None:
            texts.extend(legend.get_texts())
    return [text for text in texts if text.get_visible() and text.get_text().strip()]


def audit_figure(figure: Figure, figure_name: str) -> VisualQAReport:
    """绘制后检查关键文字与图例；发现问题即中止导出，避免发布缺陷图。"""
    figure.canvas.draw()
    renderer = figure.canvas.get_renderer()
    figure_box = figure.bbox
    tolerance = 1.0
    issues: list[str] = []
    legends_checked = 0

    # 图例位于坐标轴绘图区内时会直接遮挡数据，因此统一要求移到图外或改用直接标注。
    for axis in figure.axes:
        legend = axis.get_legend()
        if legend is None or not legend.get_visible():
            continue
        legends_checked += 1
        legend_box = legend.get_window_extent(renderer)
        axis_box = axis.get_window_extent(renderer)
        overlap = _intersection_area(legend_box, axis_box)
        if overlap / max(legend_box.width * legend_box.height, 1.0) >= 0.98:
            issues.append(f"图例位于数据绘图区：{axis.get_title() or '未命名子图'}")

    texts = _figure_texts(figure)
    text_boxes: list[tuple[str, Bbox]] = []
    for text in texts:
        box = text.get_window_extent(renderer)
        if (
            box.x0 < figure_box.x0 - tolerance
            or box.y0 < figure_box.y0 - tolerance
            or box.x1 > figure_box.x1 + tolerance
            or box.y1 > figure_box.y1 + tolerance
        ):
            issues.append(f"文字越出画布：{text.get_text()}")
        text_boxes.append((text.get_text(), box))

    # 仅把明显的文字块交叠视为失败，避免抗锯齿边缘或相邻短标签产生误报。
    for (first_text, first_box), (second_text, second_box) in combinations(text_boxes, 2):
        overlap = _intersection_area(first_box, second_box)
        smaller_area = min(first_box.width * first_box.height, second_box.width * second_box.height)
        if smaller_area > 0 and overlap / smaller_area >= 0.30:
            issues.append(f"文字重叠：{first_text} / {second_text}")

    if issues:
        summary = "；".join(dict.fromkeys(issues))
        raise RuntimeError(f"视觉审查未通过（{figure_name}）：{summary}")
    return VisualQAReport(figure_name, len(texts), legends_checked)
