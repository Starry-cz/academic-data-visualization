# Asset Directory Map / 资产目录

> 本文件由 `scripts/generate_directory_map.py` 生成。生产模板与历史示例严格分开；历史示例不能作为已验证模板直接路由。

## Release-verified templates / 发布级已验证模板

这些模板均已完成 demo 与固定 fixture 两条执行路径、程序 QA、最终尺寸 RGB/灰度审阅和证据哈希。

| Chart | Canonical ID | Backend | Asset path | Run |
|---|---|---|---|---|
| 校准曲线 / Calibration Curve | `calibration-curve` | python | `templates/production-verified/calibration-curve` | `python scripts/run_asset.py --chart-id calibration-curve --demo --output-dir <dir>` |
| 相关矩阵 / Correlation Matrix | `correlation-matrix` | python | `templates/production-verified/correlation-matrix` | `python scripts/run_asset.py --chart-id correlation-matrix --demo --output-dir <dir>` |
| 森林图 / Forest Plot | `forest-plot` | python | `templates/production-verified/forest-plot` | `python scripts/run_asset.py --chart-id forest-plot --demo --output-dir <dir>` |
| 分组柱状图 / Grouped Bar Chart | `grouped-bar-chart` | python | `templates/production-verified/grouped-bar-chart` | `python scripts/run_asset.py --chart-id grouped-bar-chart --demo --output-dir <dir>` |
| Kaplan–Meier曲线 / Kaplan–Meier Curve | `kaplan-meier-curve` | python | `templates/production-verified/kaplan-meier-curve` | `python scripts/run_asset.py --chart-id kaplan-meier-curve --demo --output-dir <dir>` |
| 折线图 / Line Chart | `line-chart` | python | `templates/production-verified/line-chart` | `python scripts/run_asset.py --chart-id line-chart --demo --output-dir <dir>` |
| PCA双标图 / PCA Biplot | `pca-biplot` | python | `templates/production-verified/pca-biplot` | `python scripts/run_asset.py --chart-id pca-biplot --demo --output-dir <dir>` |
| 精确率-召回率曲线 / Precision–Recall Curve | `precision-recall-curve` | python | `templates/production-verified/precision-recall-curve` | `python scripts/run_asset.py --chart-id precision-recall-curve --demo --output-dir <dir>` |
| ROC曲线 / ROC Curve | `roc-curve` | python | `templates/production-verified/roc-curve` | `python scripts/run_asset.py --chart-id roc-curve --demo --output-dir <dir>` |
| 桑基图 / Sankey Diagram | `sankey-diagram` | python | `templates/production-verified/sankey-diagram` | `python scripts/run_asset.py --chart-id sankey-diagram --demo --output-dir <dir>` |
| 小提琴图 / Violin Plot | `violin-plot` | python | `templates/production-verified/violin-plot` | `python scripts/run_asset.py --chart-id violin-plot --demo --output-dir <dir>` |
| 火山图 / Volcano Plot | `volcano-plot` | python | `templates/production-verified/volcano-plot` | `python scripts/run_asset.py --chart-id volcano-plot --demo --output-dir <dir>` |

## Retained legacy examples / 保留的历史示例

这些目录保留原脚本与图片供人工参考，但未满足统一输入接口、隔离输出、真实渲染 QA 或发布证据门禁。

| Legacy asset | Related canonical chart | Backend | Directory | Verification |
|---|---|---|---|---|
| `three-dimensional-heatmap` | 三维热图 / Three-dimensional Heatmap (`three-dimensional-heatmap`) | r | `assets/figures/3DHeatmap` | `syntax_parsed` |
| `legacy-roc-curve` | ROC曲线 / ROC Curve (`roc-curve`) | python | `assets/figures/AUROC` | `syntax_parsed` |
| `ablation-bar-chart` | 消融柱状图 / Ablation Bar Chart (`ablation-bar-chart`) | python | `assets/figures/BarAblation` | `syntax_parsed` |
| `categorical-bar-chart` | 分类柱状图 / Categorical Bar Chart (`categorical-bar-chart`) | python | `assets/figures/BarCategorical` | `syntax_parsed` |
| `method-comparison-bar-chart` | 方法比较柱状图 / Method Comparison Bar Chart (`method-comparison-bar-chart`) | python | `assets/figures/BarComparison` | `syntax_parsed` |
| `composition-bar-chart` | 组成柱状图 / Composition Bar Chart (`composition-bar-chart`) | python | `assets/figures/BarComposition` | `syntax_parsed` |
| `before-after-bar-chart` | 前后比较柱状图 / Before–After Bar Chart (`before-after-bar-chart`) | python | `assets/figures/BarDistribution` | `syntax_parsed` |
| `bubble-scatter` | 气泡散点图 / Bubble Scatter (`bubble-scatter`) | python | `assets/figures/BubbleScatter` | `syntax_parsed` |
| `chord-diagram` | 弦图 / Chord Diagram (`chord-diagram`) | python | `assets/figures/ChordDiagram` | `syntax_parsed` |
| `confusion-matrix` | 混淆矩阵 / Confusion Matrix (`confusion-matrix`) | python | `assets/figures/ConfusionMatrix` | `syntax_parsed` |
| `correlation-bubble-matrix` | 相关性气泡矩阵 / Correlation Bubble Matrix (`correlation-bubble-matrix`) | python | `assets/figures/CorrelationBubbleMatrix` | `syntax_parsed` |
| `legacy-correlation-matrix` | 相关矩阵 / Correlation Matrix (`correlation-matrix`) | r | `assets/figures/CorrelationMatrix` | `syntax_parsed` |
| `correlation-network` | 相关网络图 / Correlation Network (`correlation-network`) | python | `assets/figures/CorrelationNetwork` | `syntax_parsed` |
| `density-heatmap` | 密度热图 / Density Heatmap (`density-heatmap`) | r | `assets/figures/DensityHeatmap` | `syntax_parsed` |
| `exafs-wavelet-transform-map` | EXAFS 小波变换图 / EXAFS Wavelet-transform Map (`exafs-wavelet-transform-map`) | python | `assets/figures/EXAFSWaveletMap` | `syntax_parsed` |
| `frequency-3d-heatmap` | 三维频率热图 / Three-dimensional Frequency Heatmap (`frequency-3d-heatmap`) | r | `assets/figures/Frequency_3DHeatmap` | `syntax_parsed` |
| `proportional-symbol-map` | 比例符号地图 / Proportional Symbol Map (`proportional-symbol-map`) | python | `assets/figures/GeographicBubbleMap` | `syntax_parsed` |
| `legacy-grouped-bar-chart` | 分组柱状图 / Grouped Bar Chart (`grouped-bar-chart`) | python | `assets/figures/GroupedBarChart` | `syntax_parsed` |
| `grouped-correlation-matrix` | 分组相关矩阵 / Grouped Correlation Matrix (`grouped-correlation-matrix`) | r | `assets/figures/GroupedCorrelationMatrix` | `syntax_parsed` |
| `grouped-violin-plot` | 分组小提琴图 / Grouped Violin Plot (`grouped-violin-plot`) | python | `assets/figures/GroupedViolin` | `syntax_parsed` |
| `heatmap` | 热图 / Heatmap (`heatmap`) | python | `assets/figures/heatmap` | `syntax_parsed` |
| `kernel-density-plot` | 核密度图 / Kernel Density Plot (`kernel-density-plot`) | r | `assets/figures/KernelDensity` | `syntax_parsed` |
| `legacy-line-chart` | 折线图 / Line Chart (`line-chart`) | python | `assets/figures/LineTrend` | `syntax_parsed` |
| `manifold-embedding-plot` | 流形嵌入图 / Manifold Embedding Plot (`manifold-embedding-plot`) | python | `assets/figures/Manifold` | `syntax_parsed` |
| `mantel-correlation-plot` | Mantel相关图 / Mantel Correlation Plot (`mantel-correlation-plot`) | r | `assets/figures/MantelCorrelation` | `syntax_parsed` |
| `marginal-density-scatter` | 边际密度散点图 / Marginal Density Scatter (`marginal-density-scatter`) | python | `assets/figures/MarginalDensity` | `syntax_parsed` |
| `marker-gene-dot-plot` | 标记基因点图 / Marker-gene Dot Plot (`marker-gene-dot-plot`) | python | `assets/figures/MarkerGeneDotPlot` | `syntax_parsed` |
| `paired-box-scatter` | 配对箱线散点图 / Paired Box Scatter (`paired-box-scatter`) | r | `assets/figures/PairedBoxScatter` | `syntax_parsed` |
| `legacy-pca-biplot` | PCA双标图 / PCA Biplot (`pca-biplot`) | r | `assets/figures/PCA` | `syntax_parsed` |
| `radar-chart` | 雷达图 / Radar Chart (`radar-chart`) | python | `assets/figures/Radar` | `syntax_parsed` |
| `ridgeline-plot` | 山脊图 / Ridgeline Plot (`ridgeline-plot`) | r | `assets/figures/RidgePlot` | `syntax_parsed` |
| `legacy-sankey-diagram` | 桑基图 / Sankey Diagram (`sankey-diagram`) | python | `assets/figures/SankeyDiagram` | `syntax_parsed` |
| `stacked-area-chart` | 堆叠面积图 / Stacked Area Chart (`stacked-area-chart`) | python | `assets/figures/StackedArea` | `syntax_parsed` |
| `stacked-bar-scatter` | 堆叠柱状散点图 / Stacked Bar Scatter (`stacked-bar-scatter`) | python | `assets/figures/StackedBarScatter` | `syntax_parsed` |
| `legacy-violin-plot` | 小提琴图 / Violin Plot (`violin-plot`) | python | `assets/figures/Violin` | `syntax_parsed` |
| `legacy-volcano-plot` | 火山图 / Volcano Plot (`volcano-plot`) | python | `assets/figures/volcano` | `syntax_parsed` |
| `xps-peak-deconvolution-plot` | XPS 峰拟合分峰图 / XPS Peak Deconvolution Plot (`xps-peak-deconvolution-plot`) | python | `assets/figures/XPSPeakDeconvolution` | `syntax_parsed` |

## Routing rules / 路由规则

1. 先用 `python scripts/query_chart.py --name <名称>` 或 `--question <研究问题>` 获取 canonical record。
2. 只有 `production_verified + release_passed` 才能交给统一运行器；其他状态只能作为知识或人工改造参考。
3. 不得为缺少真实实现的图型伪造目录、预览或发布状态。
4. 精选成图与配色资产由 `references/showcase-lock.json` 单独锁定，不随生产模板迁移而替换。
