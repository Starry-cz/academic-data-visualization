# Typography & Font Specifications

> **Nature journal baseline:** Nature's current figure guide requires editable, standard sans-serif text, with routine figure text between 5 and 7 pt and multi-panel labels at 8 pt bold. These values apply at final manuscript size, not to keynote, web, or poster outputs. Read `delivery-profiles.md` before copying a block. Source: <https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/>.

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

---

## Font Family

Always use editable sans-serif text. **Preferred:** Arial or Helvetica. **Fallback:** Liberation Sans. Do not convert text to outlines.

## Font Size Floor

At final print dimensions: axis ticks and legend labels 5–6 pt; axis titles, panel titles, and annotations 6–7 pt; panel labels 8 pt bold, upright, and lowercase (`a`, `b`, `c`). Do not use routine figure text above 7 pt or below 5 pt.

For `keynote_screen`, use the pixel-based starting ranges in `delivery-profiles.md` and verify them at the actual screen size and viewing distance. Never reuse the 5–7 pt manuscript block on a 16:9 stage graphic.

## R ggplot2 Setup

```r
library(ggplot2)

theme_cns <- theme_classic(base_size = 7, base_family = "Arial") +
  theme(
    axis.title = element_text(size = 8),
    axis.text = element_text(size = 6, color = "#1A1A1A"),
    legend.title = element_text(size = 7, face = "bold"),
    legend.text = element_text(size = 6),
    strip.text = element_text(size = 8, face = "bold")
  )
```

## R ComplexHeatmap Setup

```r
library(ComplexHeatmap)
library(grid)

ht_opt(
  heatmap_column_names_gp = gpar(fontfamily = "Arial", fontsize = 6, col = "#1A1A1A"),
  heatmap_row_names_gp = gpar(fontfamily = "Arial", fontsize = 6, col = "#1A1A1A"),
  legend_title_gp = gpar(fontfamily = "Arial", fontsize = 7, fontface = "bold"),
  legend_labels_gp = gpar(fontfamily = "Arial", fontsize = 6)
)
```

## Cross-platform Font Notes

- Windows: Arial is installed by default
- macOS: Helvetica is installed by default; Arial is also available
- Linux: Neither Arial nor Helvetica is guaranteed. Use `Liberation Sans` or install `fonts-liberation` / `msttcorefonts`
- For R on Linux: use `showtext` package to register and embed fonts; export with `cairo_pdf()` device
- Always embed fonts in PDF output: `pdf.fonttype: 42` (matplotlib), `cairo_pdf()` (R)

## Panel Labels

Use one helper and keep every multi-panel label consistent. Panel labels are the sole permitted 8-pt text category.

```python
# 子图标签使用 8 pt 加粗小写字母，位置在所有面板中保持一致。
def add_panel_label(ax, label):
    ax.text(-0.12, 1.03, label, transform=ax.transAxes,
            fontsize=8, fontweight="bold", va="bottom", ha="left")
```
