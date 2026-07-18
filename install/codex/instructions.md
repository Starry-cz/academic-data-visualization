# Academic Data Visualization Instructions for Codex
# Auto-generated from academic-data-visualization/SKILL.md — 2026-07-18 16:15 UTC

# Academic Data Visualization Portable Core Rules
# Auto-generated from academic-data-visualization/SKILL.md — 2026-07-18 16:15 UTC
# These rules work across Claude Code, Codex, Cursor, and Copilot.

## Advisor Workflow
1. Define the scientific claim and unit of observation before selecting a chart.
2. Profile only the relevant sample sizes, distributions, missingness, outliers, grouping, and dependence.
3. Recommend the chart from data structure + argument; actively warn about misleading choices.
4. Fix the target journal, final physical size, panel hierarchy, and backend before plotting.
5. Render an RGB proof, run programmatic QA, inspect RGB + grayscale proofs, revise, then export.

## Design Principles
1. One figure, one core message. Remove gridlines, borders, and redundant legends.
2. Restrained color > abundant color. Use 2-4 semantic colors + 1 accent. Never default palettes.
3. Design for print, not screen. Single column 89mm, double column 183mm.
4. Vector first, raster fallback. Editable PDF/SVG/EPS for line art; TIFF/PNG (≥450dpi) for raster.
5. Never call a composite fully editable when it embeds rasterized panel images.

## Color Palette — COPY VERBATIM

```python
# Academic Data Visualization — Nature-ready accessible palette
# 使用色盲安全主色；低对比度信息通过透明度和中性灰处理，而不是新增相近色。
CATEGORICAL = ["#0072B2", "#009E73", "#E69F00", "#CC79A7", "#D55E00", "#56B4E9"]
CATEGORICAL_EXTENDED = [
    "#0072B2", "#009E73", "#E69F00", "#CC79A7", "#D55E00", "#56B4E9", "#999999"
]
DIVERGING = ["#2166AC", "#F7F7F7", "#B2182B"]
SEQUENTIAL = ["#F7FBFF", "#C6DBEF", "#6BAED6", "#2171B5", "#084594"]
ACCENT = "#D55E00"
INK = "#1A1A1A"
GREY = "#6B7280"
GRID = "#D7DEE6"  # 仅在确有读数需要时使用极淡主网格。
BACKGROUND = "#FFFFFF"
```

```r
# Academic Data Visualization — Nature-ready accessible palette
categorical <- c("#0072B2", "#009E73", "#E69F00", "#CC79A7", "#D55E00", "#56B4E9")
categorical_extended <- c(
  "#0072B2", "#009E73", "#E69F00", "#CC79A7", "#D55E00", "#56B4E9", "#999999"
)
diverging <- c("#2166AC", "#F7F7F7", "#B2182B")
sequential <- c("#F7FBFF", "#C6DBEF", "#6BAED6", "#2171B5", "#084594")
accent <- "#D55E00"
ink <- "#1A1A1A"
grey <- "#6B7280"
grid <- "#D7DEE6"
background <- "#FFFFFF"
```

Color roles: blue (#0072B2) = baseline/main evidence; bluish green (#009E73) = secondary group; orange (#E69F00) = supporting contrast; vermilion (#D55E00) = one emphasis; grey (#6B7280) = background/non-significant. Never use jet/rainbow or default matplotlib/seaborn palettes.

## Typography — COPY VERBATIM

```python
# Academic Data Visualization typography baseline — place at TOP of script
import matplotlib as mpl
mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "Liberation Sans"],
    "font.size": 7,
    "axes.titlesize": 7,
    "axes.labelsize": 7,
    "xtick.labelsize": 6,
    "ytick.labelsize": 6,
    "legend.fontsize": 6,
    "figure.titlesize": 7,
    "text.color": "#1A1A1A",
    "axes.labelcolor": "#1A1A1A",
    "xtick.color": "#1A1A1A",
    "ytick.color": "#1A1A1A",
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
# Academic Data Visualization typography baseline — place at TOP of script
library(ggplot2)
theme_cns <- theme_classic(base_size = 7, base_family = "Arial") +
  theme(
    axis.title = element_text(size = 7, color = "#1A1A1A"),
    axis.text = element_text(size = 6, color = "#1A1A1A"),
    legend.title = element_text(size = 7, face = "bold"),
    legend.text = element_text(size = 6),
    strip.text = element_text(size = 7, face = "bold"),
    panel.grid = element_blank(),
    axis.line = element_line(linewidth = 0.6, color = "#1A1A1A"),
    axis.ticks = element_line(linewidth = 0.6, color = "#1A1A1A"),
    legend.background = element_blank(),
    legend.key = element_blank()
  )
```

Font: Arial/Helvetica. No text below 5pt at final print dimensions. Panel labels: lowercase bold a,b,c... at consistent positions.

## Export — COPY VERBATIM

```python
# Academic Data Visualization export baseline
mpl.rcParams.update({
    "pdf.fonttype": 42,         # TrueType font embedding
    "svg.fonttype": "none",     # editable text in SVG
    "savefig.bbox": "tight",    # trim whitespace
    "savefig.dpi": 450,
})

def save_nature_ready_figure(fig, filename):
    """导出可编辑 PDF 主文件与 450 dpi RGB 预览图。"""
    fig.savefig(f"{filename}.pdf", bbox_inches="tight")
    fig.savefig(f"{filename}.png", bbox_inches="tight", dpi=450)
```

## Layout Rules
- Single column: 89mm wide. Double column: 183mm wide. Max height: 247mm.
- Remove top and right spines. Ticks outward. Gridlines off by default.
- Legend: outside plot area or direct labeling. Never inside occluding data.
- Panel width never below 35mm. Below 45mm = warn.
- Multi-panel: rows have aspect-ratio-correct heights (heatmap=1.0, ridge=0.65).

## Production Scripts
- Check `assets/figures/<type>/` and its companion preview before writing new code.
- Classify each panel as native reuse, visual adapt, or new implementation.
- Reuse only when chart semantics and data structure are compatible.
- Preserve per-panel vector masters when a mixed composite must embed raster images.
- R scripts: png(type="cairo"), showtext_auto(FALSE) before export.

## QA Checklist
- [ ] Custom hex colors used (no defaults)
- [ ] Top/right spines removed
- [ ] Arial/Helvetica font set
- [ ] Editable PDF/SVG master + 450dpi RGB PNG/TIFF proof saved
- [ ] Dimensions match journal column width
- [ ] Panel labels consistent (a,b,c...)
- [ ] Legend outside plot or direct labeling
- [ ] Colorblind-friendly (no red-green only pairs)
- [ ] RGB and grayscale proofs inspected at intended size
- [ ] Rasterized composite panels disclosed

