# Export Specifications

> **Profile-first rule:** keep text and line work editable, then follow the named journal or venue specification. Nature recommends RGB and editable standard fonts; 300 dpi is a common minimum for photographic raster content, while a 450 dpi proof can maximise detail in Nature's online proof workflow. DPI does not improve vector line art. Source: <https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/>.

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
| Heatmap colour blocks, micrographs, photos | TIFF or PNG at the target specification; absent one, ≥300 dpi at final size | True raster content only |
| Mixed (scatter with >100K rasterized points on vector axes) | PDF with `rasterized=True` on the data layer | Keeps axes/labels as vector text |

**For journal figures deliver:**
1. One vector master file for line/text content (PDF preferred, or SVG/EPS if specified)
2. One RGB raster proof at the target specification; 450 dpi remains the repository's high-detail review default when the target is silent
3. One grayscale proof and a list of any intentionally rasterized layers

**For keynote/product-launch charts deliver:**
1. One editable SVG/PDF master
2. Exact-pixel RGB PNG files for the target screen, normally 1920×1080 and/or 3840×2160
3. Light/dark-background proofs when both contexts are expected

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
| Nature | PDF/SVG/EPS preferred | ≥300 dpi for photographs; a 450 dpi proof maximises online-proof detail |
| IEEE | Vector preferred; >600 dpi if black-and-white line art must be raster | >300 dpi for colour/grayscale raster |
| Other journals | Verify current author instructions | Do not infer one family-wide value |

**Guideline:** Do not rasterize line art merely to chase DPI. Export editable vector artwork, keep genuine raster content at its native resolution, and never upscale a low-resolution source to manufacture compliance.

## File Naming Convention

- Use descriptive names: `fig1_microbiome_heatmap.pdf` not `figure1.pdf`
- Match the numbering in your manuscript: `fig2a_volcano.pdf`, `fig2b_pathway.pdf`
- Supplementary figures: `figS1_quality_control.pdf`
