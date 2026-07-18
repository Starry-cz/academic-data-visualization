# Export Specifications

> **Nature-ready baseline:** Nature requests editable vector artwork for text and line work, RGB colour, embedded standard fonts, and 450 dpi or higher for raster images. Use PDF as the master for quantitative figures and keep a 450 dpi PNG/TIFF proof for review. Source: <https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/>.

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

```r
# Academic Data Visualization export baseline
save_nature_ready_figure <- function(plot, filename, width_mm = 183, height_mm = NULL) {
  ggsave(paste0(filename, ".pdf"), plot, device = cairo_pdf,
         width = width_mm, height = height_mm, units = "mm")
  png(paste0(filename, ".png"), width = width_mm, height = height_mm,
      units = "mm", res = 450, type = "cairo")
  print(plot)
  dev.off()
}
```

---

## Format Selection

| Content Type | Format | Notes |
|-------------|--------|-------|
| Line plots, scatter plots, bar charts, boxplots | PDF or SVG or EPS | Vector elements (lines, text, shapes) must remain vector |
| Heatmap colour blocks, micrographs, photos | TIFF or PNG at ≥450 dpi | True raster content only |
| Mixed (scatter with >100K rasterized points on vector axes) | PDF with `rasterized=True` on the data layer | Keeps axes/labels as vector text |

**Always deliver:**
1. One vector master file (PDF preferred, or SVG/EPS if specified by journal)
2. One 450 dpi RGB PNG proof (for quick viewing, visual QA, manuscript drafts)

## Python Matplotlib Export

```python
# Vector master (submission-ready)
fig.savefig("figure.pdf", bbox_inches="tight")

# Raster proof
fig.savefig("figure.png", bbox_inches="tight", dpi=450)

# For scatter plots with very large point counts:
ax.scatter(x, y, s=2, rasterized=True)  # rasterize data layer only
```

Key matplotlib rcParams:
```python
mpl.rcParams.update({
    "svg.fonttype": "none",     # Editable text in SVG
    "pdf.fonttype": 42,         # TrueType font embedding in PDF
    "savefig.bbox": "tight",    # Trim whitespace
    "savefig.dpi": 450,
})
```

## R ggplot2 Export

```r
# Vector master
ggsave("figure.pdf", width = 89, height = 70, units = "mm",
       device = cairo_pdf)

# Raster preview
ggsave("figure.png", width = 89, height = 70, units = "mm", dpi = 450)
```

## R ComplexHeatmap Export

```r
# Vector master
cairo_pdf("heatmap.pdf", width = 183/25.4, height = 120/25.4)
draw(ht)
dev.off()

# Raster preview
png("heatmap_preview.png", width = 183, height = 120, units = "mm", res = 450)
draw(ht)
dev.off()
```

## Resolution Requirements by Journal

| Journal Family | Line Art | Raster/Photo |
|---------------|----------|-------------|
| Nature | PDF/SVG/EPS preferred | ≥450 dpi at final physical size |
| Cell | ≥600 dpi when raster line art is requested | ≥300 dpi |
| Science | ≥600 dpi when raster line art is requested | ≥300 dpi |

**Guideline:** Do not rasterize line art merely to chase DPI. Export editable vector artwork; use 450 dpi or higher only for genuine raster content.

## File Naming Convention

- Use descriptive names: `fig1_microbiome_heatmap.pdf` not `figure1.pdf`
- Match the numbering in your manuscript: `fig2a_volcano.pdf`, `fig2b_pathway.pdf`
- Supplementary figures: `figS1_quality_control.pdf`
