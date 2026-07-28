# 科研数据可视化图表源分类

> 本文件保存当前可验证的 24 类源分类与命名。规范化 ID、别名和实现状态以
> `chart-registry.yaml` 为准。不要手工从本文件推断生产资产状态。
>
> 重要：输入方案声明原始清单应有 714 条，但所提供文件未包含该清单。
> 本版本保留 24 类结构，并登记现有仓库、现有目录及方案 P0–P3 中可验证的条目；
> 待原始清单补充后，可用 `scripts/build_chart_registry.py` 导入并审计差额。

## 01. 数值比较与排序 / Comparison and Ranking

- `dot-plot` — 点图（Dot Plot）
- `lollipop-chart` — 棒棒糖图（Lollipop Chart）
- `horizontal-bar-chart` — 水平条形图（Horizontal Bar Chart）
- `grouped-bar-chart` — 分组柱状图（Grouped Bar Chart）
- `categorical-bar-chart` — 分类柱状图（Categorical Bar Chart）
- `method-comparison-bar-chart` — 方法比较柱状图（Method Comparison Bar Chart）
- `ablation-bar-chart` — 消融柱状图（Ablation Bar Chart）
- `dumbbell-chart` — 哑铃图（Dumbbell Chart）
- `slope-chart` — 坡度图（Slope Chart）
- `pareto-chart` — 帕累托图（Pareto Chart）
- `contribution-waterfall-chart` — 贡献瀑布图（Contribution Waterfall Chart）
- `before-after-bar-chart` — 前后比较柱状图（Before–After Bar Chart）

## 02. 时间、趋势与动态 / Time, Trend, and Dynamics

- `slope-chart` — 坡度图（Slope Chart）
- `line-chart` — 折线图（Line Chart）
- `step-chart` — 阶梯图（Step Chart）
- `confidence-band-plot` — 置信带图（Confidence Band Plot）
- `moving-average-plot` — 移动平均图（Moving Average Plot）
- `area-chart` — 面积图（Area Chart）
- `stacked-area-chart` — 堆叠面积图（Stacked Area Chart）
- `streamgraph` — 流图（Streamgraph）
- `horizon-chart` — 地平线图（Horizon Chart）
- `run-chart` — 运行图（Run Chart）
- `control-chart` — 控制图（Control Chart）
- `gantt-chart` — 甘特图（Gantt Chart）
- `timeline` — 时间线（Timeline）
- `spaghetti-plot` — 个体纵向轨迹图（Spaghetti Plot）
- `interrupted-time-series` — 中断时间序列图（Interrupted Time-series Plot）

## 03. 分布与统计诊断 / Distribution and Statistical Diagnostics

- `dot-plot` — 点图（Dot Plot）
- `histogram` — 直方图（Histogram）
- `kernel-density-plot` — 核密度图（Kernel Density Plot）
- `ecdf-plot` — 经验累积分布图（ECDF Plot）
- `qq-plot` — Q-Q图（Q-Q Plot）
- `box-plot` — 箱线图（Box Plot）
- `violin-plot` — 小提琴图（Violin Plot）
- `grouped-violin-plot` — 分组小提琴图（Grouped Violin Plot）
- `raincloud-plot` — 雨云图（Raincloud Plot）
- `beeswarm-plot` — 蜂群图（Beeswarm Plot）
- `ridgeline-plot` — 山脊图（Ridgeline Plot）
- `paired-box-scatter` — 配对箱线散点图（Paired Box Scatter）
- `rug-plot` — 地毯图（Rug Plot）

## 04. 关系与回归 / Relationship and Regression

- `kernel-density-plot` — 核密度图（Kernel Density Plot）
- `scatter-plot` — 散点图（Scatter Plot）
- `scatter-regression-plot` — 回归散点图（Scatter Regression Plot）
- `bubble-scatter` — 气泡散点图（Bubble Scatter）
- `marginal-density-scatter` — 边际密度散点图（Marginal Density Scatter）
- `hexbin-plot` — 六边形分箱图（Hexbin Plot）
- `two-dimensional-histogram` — 二维直方图（Two-dimensional Histogram）
- `connected-scatter` — 连接散点图（Connected Scatter Plot）
- `bland-altman-plot` — Bland–Altman图（Bland–Altman Plot）

## 05. 多变量与降维 / Multivariate and Dimension Reduction

- `correlation-matrix` — 相关矩阵（Correlation Matrix）
- `grouped-correlation-matrix` — 分组相关矩阵（Grouped Correlation Matrix）
- `correlation-bubble-matrix` — 相关性气泡矩阵（Correlation Bubble Matrix）
- `scatterplot-matrix` — 散点矩阵（Scatterplot Matrix）
- `pca-biplot` — PCA双标图（PCA Biplot）
- `rda-triplot` — RDA三标图（RDA Triplot）
- `umap-plot` — UMAP图（UMAP Plot）
- `tsne-plot` — t-SNE图（t-SNE Plot）
- `manifold-embedding-plot` — 流形嵌入图（Manifold Embedding Plot）
- `parallel-coordinates` — 平行坐标图（Parallel Coordinates）
- `ternary-plot` — 三元图（Ternary Plot）
- `correlation-network` — 相关网络图（Correlation Network）
- `mantel-correlation-plot` — Mantel相关图（Mantel Correlation Plot）
- `scree-plot` — 碎石图（Scree Plot）
- `parallel-analysis-plot` — 平行分析图（Parallel Analysis Plot）
- `grand-tour` — Grand Tour动态图（Grand Tour）

## 06. 矩阵、热图与模式 / Matrix, Heatmap, and Pattern

- `two-dimensional-histogram` — 二维直方图（Two-dimensional Histogram）
- `correlation-matrix` — 相关矩阵（Correlation Matrix）
- `grouped-correlation-matrix` — 分组相关矩阵（Grouped Correlation Matrix）
- `correlation-bubble-matrix` — 相关性气泡矩阵（Correlation Bubble Matrix）
- `heatmap` — 热图（Heatmap）
- `clustered-heatmap` — 聚类热图（Clustered Heatmap）
- `annotated-heatmap` — 注释热图（Annotated Heatmap）
- `density-heatmap` — 密度热图（Density Heatmap）
- `three-dimensional-heatmap` — 三维热图（Three-dimensional Heatmap）
- `frequency-3d-heatmap` — 三维频率热图（Three-dimensional Frequency Heatmap）
- `sparse-matrix-plot` — 稀疏矩阵图（Sparse Matrix Plot）
- `calendar-heatmap` — 日历热图（Calendar Heatmap）
- `mosaic-plot` — 马赛克图（Mosaic Plot）
- `dendrogram` — 树状图（Dendrogram）
- `pseudotime-heatmap` — 拟时间热图（Pseudotime Heatmap）
- `cohort-retention-heatmap` — 队列留存热图（Cohort Retention Heatmap）

## 07. 不确定性与效应量 / Uncertainty and Effect Size

- `confidence-band-plot` — 置信带图（Confidence Band Plot）
- `forest-plot` — 森林图（Forest Plot）
- `coefficient-plot` — 系数图（Coefficient Plot）
- `interval-plot` — 区间图（Interval Plot）
- `error-bar-plot` — 误差线图（Error Bar Plot）
- `meta-analysis-funnel-plot` — 元分析漏斗图（Meta-analysis Funnel Plot）

## 08. 模型评估与诊断 / Model Evaluation and Diagnostics

- `qq-plot` — Q-Q图（Q-Q Plot）
- `bland-altman-plot` — Bland–Altman图（Bland–Altman Plot）
- `coefficient-plot` — 系数图（Coefficient Plot）
- `roc-curve` — ROC曲线（ROC Curve）
- `precision-recall-curve` — 精确率-召回率曲线（Precision–Recall Curve）
- `calibration-curve` — 校准曲线（Calibration Curve）
- `confusion-matrix` — 混淆矩阵（Confusion Matrix）
- `decision-curve` — 决策曲线（Decision Curve）
- `residual-diagnostic-plot` — 残差诊断图（Residual Diagnostic Plot）
- `learning-curve` — 学习曲线（Learning Curve）
- `diagnostic-test-plot` — 诊断试验性能图（Diagnostic Test Performance Plot）

## 09. 机器学习解释 / Machine Learning Explainability

- `ablation-bar-chart` — 消融柱状图（Ablation Bar Chart）
- `learning-curve` — 学习曲线（Learning Curve）
- `feature-importance-plot` — 特征重要性图（Feature Importance Plot）
- `shap-beeswarm` — SHAP蜂群图（SHAP Beeswarm）
- `partial-dependence-plot` — 部分依赖图（Partial Dependence Plot）
- `ice-plot` — 个体条件期望图（Individual Conditional Expectation Plot）
- `permutation-importance-plot` — 置换重要性图（Permutation Importance Plot）

## 10. 组成与比例 / Composition and Proportion

- `area-chart` — 面积图（Area Chart）
- `stacked-area-chart` — 堆叠面积图（Stacked Area Chart）
- `streamgraph` — 流图（Streamgraph）
- `ternary-plot` — 三元图（Ternary Plot）
- `mosaic-plot` — 马赛克图（Mosaic Plot）
- `stacked-bar-chart` — 堆叠柱状图（Stacked Bar Chart）
- `percent-stacked-bar-chart` — 百分比堆叠柱状图（100% Stacked Bar Chart）
- `diverging-stacked-bar-chart` — 发散堆叠柱状图（Diverging Stacked Bar Chart）
- `composition-bar-chart` — 组成柱状图（Composition Bar Chart）
- `stacked-bar-scatter` — 堆叠柱状散点图（Stacked Bar Scatter）
- `population-pyramid` — 人口金字塔（Population Pyramid）
- `radar-chart` — 雷达图（Radar Chart）
- `treemap` — 矩形式树图（Treemap）
- `pie-chart` — 饼图（Pie Chart）
- `cell-composition-plot` — 细胞组成图（Cell Composition Plot）

## 11. 集合与交集 / Sets and Overlap

- `upset-plot` — UpSet图（UpSet Plot）
- `venn-diagram` — 韦恩图（Venn Diagram）
- `euler-diagram` — 欧拉图（Euler Diagram）
- `set-matrix` — 集合成员矩阵（Set Membership Matrix）

## 12. 流向、流程与层级 / Flow, Process, and Hierarchy

- `timeline` — 时间线（Timeline）
- `treemap` — 矩形式树图（Treemap）
- `sankey-diagram` — 桑基图（Sankey Diagram）
- `alluvial-diagram` — 冲积图（Alluvial Diagram）
- `conversion-funnel-chart` — 转化漏斗图（Conversion Funnel Chart）
- `hierarchy-tree` — 层级树（Hierarchy Tree）
- `sunburst-chart` — 旭日图（Sunburst Chart）
- `circular-packing` — 圆形打包图（Circle Packing）
- `process-flow-diagram` — 流程图（Process Flow Diagram）
- `consort-flow-diagram` — CONSORT流程图（CONSORT Flow Diagram）
- `prisma-flow-diagram` — PRISMA流程图（PRISMA Flow Diagram）
- `hyperbolic-tree` — 双曲树（Hyperbolic Tree）
- `complex-process-mining` — 复杂流程挖掘图（Complex Process-mining Plot）

## 13. 网络与图结构 / Network and Graph Structure

- `correlation-network` — 相关网络图（Correlation Network）
- `co-occurrence-network` — 共现网络（Co-occurrence Network）
- `arc-diagram` — 弧线图（Arc Diagram）
- `chord-diagram` — 弦图（Chord Diagram）
- `dendrogram` — 树状图（Dendrogram）
- `phylogenetic-tree` — 系统发育树（Phylogenetic Tree）
- `co-citation-network` — 共被引网络（Co-citation Network）
- `bibliographic-coupling-network` — 文献耦合网络（Bibliographic Coupling Network）
- `co-word-network` — 共词网络（Co-word Network）

## 14. 地理空间与制图 / Geospatial and Cartography

- `population-pyramid` — 人口金字塔（Population Pyramid）
- `proportional-symbol-map` — 比例符号地图（Proportional Symbol Map）
- `choropleth-map` — 分级设色地图（Choropleth Map）
- `spatial-heatmap` — 空间热图（Spatial Heatmap）
- `contour-map` — 等值线地图（Contour Map）
- `raster-map` — 栅格地图（Raster Map）
- `flow-map` — 流向地图（Flow Map）
- `hexbin-map` — 蜂窝地图（Hexbin Map）

## 15. 生存与事件史 / Survival and Event History

- `kaplan-meier-curve` — Kaplan–Meier曲线（Kaplan–Meier Curve）
- `cumulative-hazard-curve` — 累计风险曲线（Cumulative Hazard Curve）
- `cumulative-incidence-curve` — 累计发生率曲线（Cumulative Incidence Curve）
- `competing-risk-plot` — 竞争风险图（Competing Risk Plot）
- `swimmer-plot` — 游泳图（Swimmer Plot）

## 16. 临床试验与流行病学 / Clinical Trials and Epidemiology

- `forest-plot` — 森林图（Forest Plot）
- `meta-analysis-funnel-plot` — 元分析漏斗图（Meta-analysis Funnel Plot）
- `roc-curve` — ROC曲线（ROC Curve）
- `calibration-curve` — 校准曲线（Calibration Curve）
- `decision-curve` — 决策曲线（Decision Curve）
- `consort-flow-diagram` — CONSORT流程图（CONSORT Flow Diagram）
- `prisma-flow-diagram` — PRISMA流程图（PRISMA Flow Diagram）
- `kaplan-meier-curve` — Kaplan–Meier曲线（Kaplan–Meier Curve）
- `cumulative-incidence-curve` — 累计发生率曲线（Cumulative Incidence Curve）
- `competing-risk-plot` — 竞争风险图（Competing Risk Plot）
- `swimmer-plot` — 游泳图（Swimmer Plot）
- `love-plot` — 协变量平衡图（Love Plot）
- `difference-in-differences-plot` — 双重差分图（Difference-in-Differences Plot）
- `event-study-plot` — 事件研究图（Event Study Plot）
- `diagnostic-test-plot` — 诊断试验性能图（Diagnostic Test Performance Plot）

## 17. 基因组与转录组 / Genomics and Transcriptomics

- `chord-diagram` — 弦图（Chord Diagram）
- `phylogenetic-tree` — 系统发育树（Phylogenetic Tree）
- `volcano-plot` — 火山图（Volcano Plot）
- `ma-plot` — MA图（MA Plot）
- `manhattan-plot` — 曼哈顿图（Manhattan Plot）
- `locuszoom-plot` — 区域关联图（LocusZoom Plot）
- `genome-browser-track` — 基因组浏览器轨道（Genome Browser Track）
- `mutation-lollipop-plot` — 突变棒棒糖图（Mutation Lollipop Plot）
- `oncoprint` — 肿瘤突变谱图（OncoPrint）
- `gsea-curve` — GSEA富集曲线（GSEA Enrichment Curve）
- `mantel-correlation-plot` — Mantel相关图（Mantel Correlation Plot）
- `marker-gene-dot-plot` — 标记基因点图（Marker-gene Dot Plot）
- `circos-plot` — Circos图（Circos Plot）

## 18. 单细胞与空间组学 / Single-cell and Spatial Omics

- `umap-plot` — UMAP图（UMAP Plot）
- `tsne-plot` — t-SNE图（t-SNE Plot）
- `marker-gene-dot-plot` — 标记基因点图（Marker-gene Dot Plot）
- `single-cell-umap` — 单细胞UMAP图（Single-cell UMAP）
- `single-cell-trajectory` — 单细胞轨迹图（Single-cell Trajectory）
- `spatial-transcriptomics-overlay` — 空间转录组叠加图（Spatial Transcriptomics Overlay）
- `cell-composition-plot` — 细胞组成图（Cell Composition Plot）
- `pseudotime-heatmap` — 拟时间热图（Pseudotime Heatmap）

## 19. 显微图像与定量 / Microscopy and Image Quantification

- `spatial-transcriptomics-overlay` — 空间转录组叠加图（Spatial Transcriptomics Overlay）
- `microscopy-image-plate` — 显微图像板（Microscopy Image Plate）
- `pathology-image-plate` — 病理图像板（Pathology Image Plate）
- `colocalization-plot` — 共定位图（Colocalization Plot）
- `line-scan-intensity` — 线扫描强度图（Line-scan Intensity Plot）
- `volume-rendering` — 体渲染（Volume Rendering）
- `isosurface` — 等值面（Isosurface）
- `image-plus-quant-composite` — 图像与定量复合图（Image-plus-quantification Composite）

## 20. 教育测量与心理计量 / Education and Psychometrics

- `item-characteristic-curve` — 题目特征曲线（Item Characteristic Curve）
- `test-information-curve` — 测验信息曲线（Test Information Curve）
- `wright-map` — Wright图（Wright Map）
- `scree-plot` — 碎石图（Scree Plot）
- `parallel-analysis-plot` — 平行分析图（Parallel Analysis Plot）
- `sem-path-diagram` — 结构方程路径图（SEM Path Diagram）
- `latent-profile-plot` — 潜在剖面图（Latent Profile Plot）

## 21. 因果推断与政策评估 / Causal Inference and Policy Evaluation

- `love-plot` — 协变量平衡图（Love Plot）
- `difference-in-differences-plot` — 双重差分图（Difference-in-Differences Plot）
- `event-study-plot` — 事件研究图（Event Study Plot）
- `sem-path-diagram` — 结构方程路径图（SEM Path Diagram）
- `causal-dag` — 因果有向无环图（Causal DAG）
- `regression-discontinuity-plot` — 回归不连续图（Regression Discontinuity Plot）
- `synthetic-control-plot` — 合成控制图（Synthetic Control Plot）
- `interrupted-time-series` — 中断时间序列图（Interrupted Time-series Plot）

## 22. 文献计量与科学知识图谱 / Bibliometrics and Science Mapping

- `prisma-flow-diagram` — PRISMA流程图（PRISMA Flow Diagram）
- `co-occurrence-network` — 共现网络（Co-occurrence Network）
- `co-citation-network` — 共被引网络（Co-citation Network）
- `keyword-burst-plot` — 关键词突现图（Keyword Burst Plot）
- `thematic-map` — 主题图（Thematic Map）
- `bibliographic-coupling-network` — 文献耦合网络（Bibliographic Coupling Network）
- `co-word-network` — 共词网络（Co-word Network）
- `strategic-diagram` — 战略坐标图（Strategic Diagram）

## 23. 项目、质量与运营 / Project, Quality, and Operations

- `pareto-chart` — 帕累托图（Pareto Chart）
- `contribution-waterfall-chart` — 贡献瀑布图（Contribution Waterfall Chart）
- `run-chart` — 运行图（Run Chart）
- `control-chart` — 控制图（Control Chart）
- `gantt-chart` — 甘特图（Gantt Chart）
- `calendar-heatmap` — 日历热图（Calendar Heatmap）
- `conversion-funnel-chart` — 转化漏斗图（Conversion Funnel Chart）
- `process-flow-diagram` — 流程图（Process Flow Diagram）
- `before-after-bar-chart` — 前后比较柱状图（Before–After Bar Chart）
- `cohort-retention-heatmap` — 队列留存热图（Cohort Retention Heatmap）
- `bullet-chart` — 子弹图（Bullet Chart）
- `kpi-card` — KPI卡片（KPI Card）
- `quality-control-overview` — 质量控制总览（Quality-control Overview）

## 24. 复合图与高级可视化 / Composite and Advanced Visualization

- `parallel-coordinates` — 平行坐标图（Parallel Coordinates）
- `three-dimensional-heatmap` — 三维热图（Three-dimensional Heatmap）
- `frequency-3d-heatmap` — 三维频率热图（Three-dimensional Frequency Heatmap）
- `genome-browser-track` — 基因组浏览器轨道（Genome Browser Track）
- `microscopy-image-plate` — 显微图像板（Microscopy Image Plate）
- `pathology-image-plate` — 病理图像板（Pathology Image Plate）
- `volume-rendering` — 体渲染（Volume Rendering）
- `isosurface` — 等值面（Isosurface）
- `quality-control-overview` — 质量控制总览（Quality-control Overview）
- `three-dimensional-surface` — 三维表面图（Three-dimensional Surface）
- `three-dimensional-vector-field` — 三维矢量场（Three-dimensional Vector Field）
- `grand-tour` — Grand Tour动态图（Grand Tour）
- `hyperbolic-tree` — 双曲树（Hyperbolic Tree）
- `circos-plot` — Circos图（Circos Plot）
- `complex-process-mining` — 复杂流程挖掘图（Complex Process-mining Plot）
- `image-plus-quant-composite` — 图像与定量复合图（Image-plus-quantification Composite）
- `asymmetric-multipanel` — 非对称多面板图（Asymmetric Multipanel Figure）
- `small-multiples` — 小多图（Small Multiples）
