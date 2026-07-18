# Academic Data Visualization Instructions for Codex
# Auto-generated from academic-data-visualization/SKILL.md — 2026-07-17 03:28 UTC

# Academic Data Visualization Portable Core Rules
# Auto-generated from academic-data-visualization/SKILL.md — 2026-07-17 03:28 UTC
# These rules work across Claude Code, Codex, Cursor, and Copilot.

## Design Principles
1. One figure, one core message. Remove gridlines, borders, and redundant legends.
2. Restrained color > abundant color. Use 2-4 semantic colors + 1 accent. Never default palettes.
3. Design for print, not screen. Single column 89mm, double column 183mm.
4. Vector first, raster fallback. PDF/SVG/EPS for line art; TIFF/PNG (≥300dpi) for raster.

## Color Palette — COPY VERBATIM

```python
# Academic Data Visualization — muted research information-design palette
# 雾蓝、鼠尾草绿、浅杏黄与柔和陶土；适合白底、多面板、印刷与灰度阅读。
CATEGORICAL = ["#6F93A9", "#AFC7B2", "#F1C37E", "#B9A6C8", "#D98764", "#8FAFB2"]
CATEGORICAL_EXTENDED = [
    "#6F93A9", "#AFC7B2", "#F1C37E", "#B9A6C8", "#D98764", "#8FAFB2",
    "#BCD3DE", "#DCEADF", "#F7E6B8", "#DDD3E5", "#EBC2B2", "#C8D8D5",
]
DIVERGING = ["#5F8195", "#F7F8F6", "#C97B6D"]
SEQUENTIAL = ["#F4F7F6", "#BCD3DE", "#6F93A9"]
ACCENT = "#C97B6D"
INK = "#31404A"
GREY = "#8A989C"
GRID = "#E3E9E9"
BACKGROUND = "#FFFFFF"
```

```r
# Academic Data Visualization — muted research information-design palette
categorical <- c("#6F93A9", "#AFC7B2", "#F1C37E", "#B9A6C8", "#D98764", "#8FAFB2")
categorical_extended <- c(
  "#6F93A9", "#AFC7B2", "#F1C37E", "#B9A6C8", "#D98764", "#8FAFB2",
  "#BCD3DE", "#DCEADF", "#F7E6B8", "#DDD3E5", "#EBC2B2", "#C8D8D5"
)
diverging <- c("#5F8195", "#F7F8F6", "#C97B6D")
sequential <- c("#F4F7F6", "#BCD3DE", "#6F93A9")
accent <- "#C97B6D"
ink <- "#31404A"
grey <- "#8A989C"
grid <- "#E3E9E9"
background <- "#FFFFFF"
```

Color roles: mist blue (#6F93A9) = baseline/main evidence; sage (#AFC7B2) = secondary group; apricot (#F1C37E) = supporting contrast; terracotta (#C97B6D) = one emphasis; grey-green (#8A989C) = background/non-significant. Never use jet/rainbow or default matplotlib/seaborn palettes.

## Typography — COPY VERBATIM

```python
# Academic Figure Skill Typography Baseline — COPY VERBATIM, place at TOP of script
import matplotlib as mpl
mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "Liberation Sans"],
    "font.size": 8,
    "axes.titlesize": 8,
    "axes.labelsize": 8,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "legend.fontsize": 8,
    "figure.titlesize": 9,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.linewidth": 0.6,
    "xtick.direction": "out",
    "ytick.direction": "out",
    "xtick.major.width": 0.6,
    "ytick.major.width": 0.6,
    "legend.frameon": False,
})
```

```r
# Academic Figure Skill Typography Baseline — COPY VERBATIM, place at TOP of script
library(ggplot2)
theme_cns <- theme_bw(base_size = 8, base_family = "Arial") +
  theme(
    axis.title = element_text(size = 8),
    axis.text = element_text(size = 7, color = "#333333"),
    legend.title = element_text(size = 8, face = "bold"),
    legend.text = element_text(size = 7),
    strip.text = element_text(size = 8, face = "bold"),
    panel.grid = element_blank(),
    legend.background = element_blank(),
    legend.key = element_blank()
  )
```

Font: Arial/Helvetica. No text below 5pt at final print dimensions. Panel labels: lowercase bold a,b,c... at consistent positions.

## Export — COPY VERBATIM

```python
# Academic Figure Skill Export Baseline — COPY VERBATIM
mpl.rcParams.update({
    "pdf.fonttype": 42,         # TrueType font embedding
    "svg.fonttype": "none",     # editable text in SVG
    "savefig.bbox": "tight",    # trim whitespace
    "savefig.dpi": 300,
})

def save_cns_figure(fig, filename):
    """Standard Academic Figure Skill export: vector PDF + 300dpi PNG preview."""
    fig.savefig(f"{filename}.pdf", bbox_inches="tight", dpi=300)
    fig.savefig(f"{filename}.png", bbox_inches="tight", dpi=300)
```

## Layout Rules
- Single column: 89mm wide. Double column: 183mm wide. Max height: 247mm.
- Remove top and right spines. Ticks outward. Gridlines off by default.
- Legend: outside plot area or direct labeling. Never inside occluding data.
- Panel width never below 35mm. Below 45mm = warn.
- Multi-panel: rows have aspect-ratio-correct heights (heatmap=1.0, ridge=0.65).

## Production Scripts
- Check `assets/figures/<type>/` for matching production scripts first.
- If found, copy-modify-run — change only data paths and labels.
- If not found, cross-type inherit from similar figure type.
- R scripts: png(type="cairo"), showtext_auto(FALSE) before export.

## QA Checklist
- [ ] Custom hex colors used (no defaults)
- [ ] Top/right spines removed
- [ ] Arial/Helvetica font set
- [ ] PDF vector + 300dpi PNG preview saved
- [ ] Dimensions match journal column width
- [ ] Panel labels consistent (a,b,c...)
- [ ] Legend outside plot or direct labeling
- [ ] Colorblind-friendly (no red-green only pairs)

