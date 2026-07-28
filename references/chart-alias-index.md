# 图型别名索引 / Chart Alias Index

> 本文件由 `scripts/generate_chart_catalog.py` 生成；不要手工编辑。
> 用户语言先路由到 canonical ID，再根据实现状态决定资产复用或新实现。

## 同名异义

| 术语 | 候选 canonical IDs | 路由规则 |
|---|---|---|
| 漏斗图 | `meta-analysis-funnel-plot`, `conversion-funnel-chart` | 出现发表偏倚、元分析时选择前者；出现转化、阶段流失时选择后者。 |
| 棒棒糖图 | `lollipop-chart`, `mutation-lollipop-plot` | 普通类别排序选择前者；蛋白结构或突变位点选择后者。 |

## 全部名称与别名

| Canonical ID | 中文名 | English name | 其他别名 | 分类 | 状态 |
|---|---|---|---|---|---|
| `dot-plot` | 点图 | Dot Plot | Cleveland dot plot | 数值比较与排序、分布与统计诊断 | 可复用模式 |
| `lollipop-chart` | 棒棒糖图 | Lollipop Chart | 无 | 数值比较与排序 | 可复用模式 |
| `horizontal-bar-chart` | 水平条形图 | Horizontal Bar Chart | 无 | 数值比较与排序 | 可复用模式 |
| `grouped-bar-chart` | 分组柱状图 | Grouped Bar Chart | 无 | 数值比较与排序 | 生产模板 |
| `categorical-bar-chart` | 分类柱状图 | Categorical Bar Chart | 无 | 数值比较与排序 | 生产模板 |
| `method-comparison-bar-chart` | 方法比较柱状图 | Method Comparison Bar Chart | 无 | 数值比较与排序 | 生产模板 |
| `ablation-bar-chart` | 消融柱状图 | Ablation Bar Chart | 无 | 数值比较与排序、机器学习解释 | 生产模板 |
| `dumbbell-chart` | 哑铃图 | Dumbbell Chart | 无 | 数值比较与排序 | 可复用模式 |
| `slope-chart` | 坡度图 | Slope Chart | 无 | 数值比较与排序、时间、趋势与动态 | 可复用模式 |
| `pareto-chart` | 帕累托图 | Pareto Chart | 无 | 数值比较与排序、项目、质量与运营 | 可复用模式 |
| `contribution-waterfall-chart` | 贡献瀑布图 | Contribution Waterfall Chart | waterfall chart | 数值比较与排序、项目、质量与运营 | 可复用模式 |
| `line-chart` | 折线图 | Line Chart | trend plot | 时间、趋势与动态 | 生产模板 |
| `step-chart` | 阶梯图 | Step Chart | 无 | 时间、趋势与动态 | 可复用模式 |
| `confidence-band-plot` | 置信带图 | Confidence Band Plot | 无 | 时间、趋势与动态、不确定性与效应量 | 可复用模式 |
| `moving-average-plot` | 移动平均图 | Moving Average Plot | 无 | 时间、趋势与动态 | 可复用模式 |
| `area-chart` | 面积图 | Area Chart | 无 | 时间、趋势与动态、组成与比例 | 可复用模式 |
| `stacked-area-chart` | 堆叠面积图 | Stacked Area Chart | 无 | 时间、趋势与动态、组成与比例 | 生产模板 |
| `streamgraph` | 流图 | Streamgraph | 无 | 时间、趋势与动态、组成与比例 | 可复用模式 |
| `horizon-chart` | 地平线图 | Horizon Chart | 无 | 时间、趋势与动态 | 按需实现 |
| `run-chart` | 运行图 | Run Chart | 无 | 时间、趋势与动态、项目、质量与运营 | 可复用模式 |
| `control-chart` | 控制图 | Control Chart | Shewhart chart | 时间、趋势与动态、项目、质量与运营 | 可复用模式 |
| `gantt-chart` | 甘特图 | Gantt Chart | 无 | 时间、趋势与动态、项目、质量与运营 | 可复用模式 |
| `timeline` | 时间线 | Timeline | 无 | 时间、趋势与动态、流向、流程与层级 | 可复用模式 |
| `spaghetti-plot` | 个体纵向轨迹图 | Spaghetti Plot | longitudinal trajectory plot | 时间、趋势与动态 | 按需实现 |
| `histogram` | 直方图 | Histogram | 无 | 分布与统计诊断 | 可复用模式 |
| `kernel-density-plot` | 核密度图 | Kernel Density Plot | KDE | 分布与统计诊断、关系与回归 | 生产模板 |
| `ecdf-plot` | 经验累积分布图 | ECDF Plot | 无 | 分布与统计诊断 | 可复用模式 |
| `qq-plot` | Q-Q图 | Q-Q Plot | quantile-quantile plot | 分布与统计诊断、模型评估与诊断 | 可复用模式 |
| `box-plot` | 箱线图 | Box Plot | box-and-whisker plot | 分布与统计诊断 | 可复用模式 |
| `violin-plot` | 小提琴图 | Violin Plot | 无 | 分布与统计诊断 | 生产模板 |
| `grouped-violin-plot` | 分组小提琴图 | Grouped Violin Plot | 无 | 分布与统计诊断 | 生产模板 |
| `raincloud-plot` | 雨云图 | Raincloud Plot | 无 | 分布与统计诊断 | 可复用模式 |
| `beeswarm-plot` | 蜂群图 | Beeswarm Plot | swarm plot；Sina plot | 分布与统计诊断 | 可复用模式 |
| `ridgeline-plot` | 山脊图 | Ridgeline Plot | ridge plot | 分布与统计诊断 | 生产模板 |
| `paired-box-scatter` | 配对箱线散点图 | Paired Box Scatter | before-after plot | 分布与统计诊断 | 生产模板 |
| `rug-plot` | 地毯图 | Rug Plot | 无 | 分布与统计诊断 | 可复用模式 |
| `scatter-plot` | 散点图 | Scatter Plot | 无 | 关系与回归 | 可复用模式 |
| `scatter-regression-plot` | 回归散点图 | Scatter Regression Plot | scatter with fit | 关系与回归 | 可复用模式 |
| `bubble-scatter` | 气泡散点图 | Bubble Scatter | bubble chart | 关系与回归 | 生产模板 |
| `marginal-density-scatter` | 边际密度散点图 | Marginal Density Scatter | 无 | 关系与回归 | 生产模板 |
| `hexbin-plot` | 六边形分箱图 | Hexbin Plot | 无 | 关系与回归 | 可复用模式 |
| `two-dimensional-histogram` | 二维直方图 | Two-dimensional Histogram | 2D histogram | 关系与回归、矩阵、热图与模式 | 可复用模式 |
| `connected-scatter` | 连接散点图 | Connected Scatter Plot | 无 | 关系与回归 | 可复用模式 |
| `bland-altman-plot` | Bland–Altman图 | Bland–Altman Plot | agreement plot | 关系与回归、模型评估与诊断 | 可复用模式 |
| `correlation-matrix` | 相关矩阵 | Correlation Matrix | correlation heatmap | 多变量与降维、矩阵、热图与模式 | 生产模板 |
| `grouped-correlation-matrix` | 分组相关矩阵 | Grouped Correlation Matrix | 无 | 多变量与降维、矩阵、热图与模式 | 生产模板 |
| `correlation-bubble-matrix` | 相关性气泡矩阵 | Correlation Bubble Matrix | corrplot | 多变量与降维、矩阵、热图与模式 | 生产模板 |
| `scatterplot-matrix` | 散点矩阵 | Scatterplot Matrix | pair plot；SPLOM | 多变量与降维 | 可复用模式 |
| `pca-biplot` | PCA双标图 | PCA Biplot | principal component analysis plot | 多变量与降维 | 生产模板 |
| `rda-triplot` | RDA三标图 | RDA Triplot | redundancy analysis plot | 多变量与降维 | 可复用模式 |
| `umap-plot` | UMAP图 | UMAP Plot | UMAP | 多变量与降维、单细胞与空间组学 | 按需实现 |
| `tsne-plot` | t-SNE图 | t-SNE Plot | tSNE | 多变量与降维、单细胞与空间组学 | 按需实现 |
| `manifold-embedding-plot` | 流形嵌入图 | Manifold Embedding Plot | Swiss roll | 多变量与降维 | 生产模板 |
| `parallel-coordinates` | 平行坐标图 | Parallel Coordinates | 无 | 多变量与降维、复合图与高级可视化 | 可复用模式 |
| `ternary-plot` | 三元图 | Ternary Plot | 无 | 多变量与降维、组成与比例 | 可复用模式 |
| `heatmap` | 热图 | Heatmap | 无 | 矩阵、热图与模式 | 生产模板 |
| `clustered-heatmap` | 聚类热图 | Clustered Heatmap | 无 | 矩阵、热图与模式 | 可复用模式 |
| `annotated-heatmap` | 注释热图 | Annotated Heatmap | 无 | 矩阵、热图与模式 | 可复用模式 |
| `density-heatmap` | 密度热图 | Density Heatmap | 无 | 矩阵、热图与模式 | 生产模板 |
| `three-dimensional-heatmap` | 三维热图 | Three-dimensional Heatmap | 3D heatmap | 矩阵、热图与模式、复合图与高级可视化 | 生产模板 |
| `frequency-3d-heatmap` | 三维频率热图 | Three-dimensional Frequency Heatmap | 无 | 矩阵、热图与模式、复合图与高级可视化 | 生产模板 |
| `sparse-matrix-plot` | 稀疏矩阵图 | Sparse Matrix Plot | 无 | 矩阵、热图与模式 | 可复用模式 |
| `calendar-heatmap` | 日历热图 | Calendar Heatmap | 无 | 矩阵、热图与模式、项目、质量与运营 | 可复用模式 |
| `mosaic-plot` | 马赛克图 | Mosaic Plot | 无 | 矩阵、热图与模式、组成与比例 | 可复用模式 |
| `forest-plot` | 森林图 | Forest Plot | 无 | 不确定性与效应量、临床试验与流行病学 | 可复用模式 |
| `coefficient-plot` | 系数图 | Coefficient Plot | dot-whisker plot | 不确定性与效应量、模型评估与诊断 | 可复用模式 |
| `interval-plot` | 区间图 | Interval Plot | 无 | 不确定性与效应量 | 可复用模式 |
| `error-bar-plot` | 误差线图 | Error Bar Plot | 无 | 不确定性与效应量 | 可复用模式 |
| `meta-analysis-funnel-plot` | 元分析漏斗图 | Meta-analysis Funnel Plot | publication-bias funnel plot | 不确定性与效应量、临床试验与流行病学 | 可复用模式 |
| `roc-curve` | ROC曲线 | ROC Curve | AUROC；receiver operating characteristic | 模型评估与诊断、临床试验与流行病学 | 生产模板 |
| `precision-recall-curve` | 精确率-召回率曲线 | Precision–Recall Curve | PR curve | 模型评估与诊断 | 可复用模式 |
| `calibration-curve` | 校准曲线 | Calibration Curve | reliability diagram | 模型评估与诊断、临床试验与流行病学 | 可复用模式 |
| `confusion-matrix` | 混淆矩阵 | Confusion Matrix | 无 | 模型评估与诊断 | 生产模板 |
| `decision-curve` | 决策曲线 | Decision Curve | decision curve analysis；DCA | 模型评估与诊断、临床试验与流行病学 | 按需实现 |
| `residual-diagnostic-plot` | 残差诊断图 | Residual Diagnostic Plot | 无 | 模型评估与诊断 | 可复用模式 |
| `learning-curve` | 学习曲线 | Learning Curve | 无 | 模型评估与诊断、机器学习解释 | 可复用模式 |
| `feature-importance-plot` | 特征重要性图 | Feature Importance Plot | 无 | 机器学习解释 | 可复用模式 |
| `shap-beeswarm` | SHAP蜂群图 | SHAP Beeswarm | SHAP summary plot | 机器学习解释 | 按需实现 |
| `partial-dependence-plot` | 部分依赖图 | Partial Dependence Plot | PDP | 机器学习解释 | 按需实现 |
| `ice-plot` | 个体条件期望图 | Individual Conditional Expectation Plot | ICE plot | 机器学习解释 | 按需实现 |
| `permutation-importance-plot` | 置换重要性图 | Permutation Importance Plot | 无 | 机器学习解释 | 可复用模式 |
| `stacked-bar-chart` | 堆叠柱状图 | Stacked Bar Chart | 无 | 组成与比例 | 可复用模式 |
| `percent-stacked-bar-chart` | 百分比堆叠柱状图 | 100% Stacked Bar Chart | 无 | 组成与比例 | 可复用模式 |
| `diverging-stacked-bar-chart` | 发散堆叠柱状图 | Diverging Stacked Bar Chart | Likert chart | 组成与比例 | 可复用模式 |
| `composition-bar-chart` | 组成柱状图 | Composition Bar Chart | 无 | 组成与比例 | 生产模板 |
| `stacked-bar-scatter` | 堆叠柱状散点图 | Stacked Bar Scatter | 无 | 组成与比例 | 生产模板 |
| `population-pyramid` | 人口金字塔 | Population Pyramid | 无 | 组成与比例、地理空间与制图 | 可复用模式 |
| `radar-chart` | 雷达图 | Radar Chart | spider chart | 组成与比例 | 生产模板 |
| `treemap` | 矩形式树图 | Treemap | 无 | 组成与比例、流向、流程与层级 | 可复用模式 |
| `pie-chart` | 饼图 | Pie Chart | 无 | 组成与比例 | 可复用模式 |
| `upset-plot` | UpSet图 | UpSet Plot | 无 | 集合与交集 | 可复用模式 |
| `venn-diagram` | 韦恩图 | Venn Diagram | 无 | 集合与交集 | 可复用模式 |
| `euler-diagram` | 欧拉图 | Euler Diagram | 无 | 集合与交集 | 可复用模式 |
| `set-matrix` | 集合成员矩阵 | Set Membership Matrix | 无 | 集合与交集 | 可复用模式 |
| `sankey-diagram` | 桑基图 | Sankey Diagram | 无 | 流向、流程与层级 | 生产模板 |
| `alluvial-diagram` | 冲积图 | Alluvial Diagram | 无 | 流向、流程与层级 | 可复用模式 |
| `conversion-funnel-chart` | 转化漏斗图 | Conversion Funnel Chart | marketing funnel | 流向、流程与层级、项目、质量与运营 | 可复用模式 |
| `hierarchy-tree` | 层级树 | Hierarchy Tree | 无 | 流向、流程与层级 | 可复用模式 |
| `sunburst-chart` | 旭日图 | Sunburst Chart | 无 | 流向、流程与层级 | 可复用模式 |
| `circular-packing` | 圆形打包图 | Circle Packing | 无 | 流向、流程与层级 | 可复用模式 |
| `process-flow-diagram` | 流程图 | Process Flow Diagram | 无 | 流向、流程与层级、项目、质量与运营 | 按需实现 |
| `consort-flow-diagram` | CONSORT流程图 | CONSORT Flow Diagram | 无 | 流向、流程与层级、临床试验与流行病学 | 按需实现 |
| `prisma-flow-diagram` | PRISMA流程图 | PRISMA Flow Diagram | 无 | 流向、流程与层级、临床试验与流行病学、文献计量与科学知识图谱 | 按需实现 |
| `correlation-network` | 相关网络图 | Correlation Network | 无 | 网络与图结构、多变量与降维 | 生产模板 |
| `co-occurrence-network` | 共现网络 | Co-occurrence Network | 无 | 网络与图结构、文献计量与科学知识图谱 | 可复用模式 |
| `arc-diagram` | 弧线图 | Arc Diagram | 无 | 网络与图结构 | 可复用模式 |
| `chord-diagram` | 弦图 | Chord Diagram | 无 | 网络与图结构、基因组与转录组 | 按需实现 |
| `dendrogram` | 树状图 | Dendrogram | 无 | 网络与图结构、矩阵、热图与模式 | 可复用模式 |
| `phylogenetic-tree` | 系统发育树 | Phylogenetic Tree | 无 | 网络与图结构、基因组与转录组 | 按需实现 |
| `proportional-symbol-map` | 比例符号地图 | Proportional Symbol Map | geographic bubble map | 地理空间与制图 | 生产模板 |
| `choropleth-map` | 分级设色地图 | Choropleth Map | 无 | 地理空间与制图 | 按需实现 |
| `spatial-heatmap` | 空间热图 | Spatial Heatmap | 无 | 地理空间与制图 | 按需实现 |
| `contour-map` | 等值线地图 | Contour Map | 无 | 地理空间与制图 | 按需实现 |
| `raster-map` | 栅格地图 | Raster Map | 无 | 地理空间与制图 | 按需实现 |
| `flow-map` | 流向地图 | Flow Map | 无 | 地理空间与制图 | 按需实现 |
| `hexbin-map` | 蜂窝地图 | Hexbin Map | 无 | 地理空间与制图 | 按需实现 |
| `kaplan-meier-curve` | Kaplan–Meier曲线 | Kaplan–Meier Curve | KM curve | 生存与事件史、临床试验与流行病学 | 可复用模式 |
| `cumulative-hazard-curve` | 累计风险曲线 | Cumulative Hazard Curve | 无 | 生存与事件史 | 可复用模式 |
| `cumulative-incidence-curve` | 累计发生率曲线 | Cumulative Incidence Curve | 无 | 生存与事件史、临床试验与流行病学 | 按需实现 |
| `competing-risk-plot` | 竞争风险图 | Competing Risk Plot | 无 | 生存与事件史、临床试验与流行病学 | 按需实现 |
| `swimmer-plot` | 游泳图 | Swimmer Plot | 无 | 生存与事件史、临床试验与流行病学 | 按需实现 |
| `love-plot` | 协变量平衡图 | Love Plot | standardized mean difference plot | 临床试验与流行病学、因果推断与政策评估 | 可复用模式 |
| `difference-in-differences-plot` | 双重差分图 | Difference-in-Differences Plot | DID plot | 临床试验与流行病学、因果推断与政策评估 | 可复用模式 |
| `event-study-plot` | 事件研究图 | Event Study Plot | 无 | 临床试验与流行病学、因果推断与政策评估 | 可复用模式 |
| `diagnostic-test-plot` | 诊断试验性能图 | Diagnostic Test Performance Plot | 无 | 临床试验与流行病学、模型评估与诊断 | 可复用模式 |
| `volcano-plot` | 火山图 | Volcano Plot | 无 | 基因组与转录组 | 生产模板 |
| `ma-plot` | MA图 | MA Plot | 无 | 基因组与转录组 | 可复用模式 |
| `manhattan-plot` | 曼哈顿图 | Manhattan Plot | 无 | 基因组与转录组 | 按需实现 |
| `locuszoom-plot` | 区域关联图 | LocusZoom Plot | 无 | 基因组与转录组 | 按需实现 |
| `genome-browser-track` | 基因组浏览器轨道 | Genome Browser Track | 无 | 基因组与转录组、复合图与高级可视化 | 按需实现 |
| `mutation-lollipop-plot` | 突变棒棒糖图 | Mutation Lollipop Plot | 无 | 基因组与转录组 | 按需实现 |
| `oncoprint` | 肿瘤突变谱图 | OncoPrint | 无 | 基因组与转录组 | 按需实现 |
| `gsea-curve` | GSEA富集曲线 | GSEA Enrichment Curve | 无 | 基因组与转录组 | 按需实现 |
| `mantel-correlation-plot` | Mantel相关图 | Mantel Correlation Plot | Mantel test | 基因组与转录组、多变量与降维 | 生产模板 |
| `marker-gene-dot-plot` | 标记基因点图 | Marker-gene Dot Plot | 无 | 单细胞与空间组学、基因组与转录组 | 生产模板 |
| `single-cell-umap` | 单细胞UMAP图 | Single-cell UMAP | 无 | 单细胞与空间组学 | 按需实现 |
| `single-cell-trajectory` | 单细胞轨迹图 | Single-cell Trajectory | pseudotime plot | 单细胞与空间组学 | 按需实现 |
| `spatial-transcriptomics-overlay` | 空间转录组叠加图 | Spatial Transcriptomics Overlay | 无 | 单细胞与空间组学、显微图像与定量 | 按需实现 |
| `cell-composition-plot` | 细胞组成图 | Cell Composition Plot | 无 | 单细胞与空间组学、组成与比例 | 可复用模式 |
| `pseudotime-heatmap` | 拟时间热图 | Pseudotime Heatmap | 无 | 单细胞与空间组学、矩阵、热图与模式 | 按需实现 |
| `microscopy-image-plate` | 显微图像板 | Microscopy Image Plate | 无 | 显微图像与定量、复合图与高级可视化 | 按需实现 |
| `pathology-image-plate` | 病理图像板 | Pathology Image Plate | 无 | 显微图像与定量、复合图与高级可视化 | 按需实现 |
| `colocalization-plot` | 共定位图 | Colocalization Plot | 无 | 显微图像与定量 | 按需实现 |
| `line-scan-intensity` | 线扫描强度图 | Line-scan Intensity Plot | 无 | 显微图像与定量 | 按需实现 |
| `volume-rendering` | 体渲染 | Volume Rendering | 无 | 显微图像与定量、复合图与高级可视化 | 按需实现 |
| `isosurface` | 等值面 | Isosurface | 无 | 显微图像与定量、复合图与高级可视化 | 按需实现 |
| `item-characteristic-curve` | 题目特征曲线 | Item Characteristic Curve | ICC | 教育测量与心理计量 | 按需实现 |
| `test-information-curve` | 测验信息曲线 | Test Information Curve | 无 | 教育测量与心理计量 | 按需实现 |
| `wright-map` | Wright图 | Wright Map | person-item map | 教育测量与心理计量 | 按需实现 |
| `scree-plot` | 碎石图 | Scree Plot | 无 | 教育测量与心理计量、多变量与降维 | 可复用模式 |
| `parallel-analysis-plot` | 平行分析图 | Parallel Analysis Plot | 无 | 教育测量与心理计量、多变量与降维 | 可复用模式 |
| `sem-path-diagram` | 结构方程路径图 | SEM Path Diagram | 无 | 教育测量与心理计量、因果推断与政策评估 | 按需实现 |
| `latent-profile-plot` | 潜在剖面图 | Latent Profile Plot | 无 | 教育测量与心理计量 | 按需实现 |
| `causal-dag` | 因果有向无环图 | Causal DAG | causal diagram | 因果推断与政策评估 | 按需实现 |
| `regression-discontinuity-plot` | 回归不连续图 | Regression Discontinuity Plot | RDD plot | 因果推断与政策评估 | 可复用模式 |
| `synthetic-control-plot` | 合成控制图 | Synthetic Control Plot | 无 | 因果推断与政策评估 | 按需实现 |
| `interrupted-time-series` | 中断时间序列图 | Interrupted Time-series Plot | ITS plot | 因果推断与政策评估、时间、趋势与动态 | 可复用模式 |
| `co-citation-network` | 共被引网络 | Co-citation Network | 无 | 文献计量与科学知识图谱、网络与图结构 | 按需实现 |
| `keyword-burst-plot` | 关键词突现图 | Keyword Burst Plot | 无 | 文献计量与科学知识图谱 | 按需实现 |
| `thematic-map` | 主题图 | Thematic Map | 无 | 文献计量与科学知识图谱 | 按需实现 |
| `bibliographic-coupling-network` | 文献耦合网络 | Bibliographic Coupling Network | 无 | 文献计量与科学知识图谱、网络与图结构 | 按需实现 |
| `co-word-network` | 共词网络 | Co-word Network | 无 | 文献计量与科学知识图谱、网络与图结构 | 按需实现 |
| `strategic-diagram` | 战略坐标图 | Strategic Diagram | 无 | 文献计量与科学知识图谱 | 按需实现 |
| `before-after-bar-chart` | 前后比较柱状图 | Before–After Bar Chart | 无 | 项目、质量与运营、数值比较与排序 | 生产模板 |
| `cohort-retention-heatmap` | 队列留存热图 | Cohort Retention Heatmap | 无 | 项目、质量与运营、矩阵、热图与模式 | 可复用模式 |
| `bullet-chart` | 子弹图 | Bullet Chart | 无 | 项目、质量与运营 | 可复用模式 |
| `kpi-card` | KPI卡片 | KPI Card | 无 | 项目、质量与运营 | 按需实现 |
| `quality-control-overview` | 质量控制总览 | Quality-control Overview | 无 | 项目、质量与运营、复合图与高级可视化 | 按需实现 |
| `three-dimensional-surface` | 三维表面图 | Three-dimensional Surface | 3D surface | 复合图与高级可视化 | 按需实现 |
| `three-dimensional-vector-field` | 三维矢量场 | Three-dimensional Vector Field | 3D vector field | 复合图与高级可视化 | 按需实现 |
| `grand-tour` | Grand Tour动态图 | Grand Tour | 无 | 复合图与高级可视化、多变量与降维 | 按需实现 |
| `hyperbolic-tree` | 双曲树 | Hyperbolic Tree | 无 | 复合图与高级可视化、流向、流程与层级 | 按需实现 |
| `circos-plot` | Circos图 | Circos Plot | 无 | 复合图与高级可视化、基因组与转录组 | 按需实现 |
| `complex-process-mining` | 复杂流程挖掘图 | Complex Process-mining Plot | 无 | 复合图与高级可视化、流向、流程与层级 | 按需实现 |
| `image-plus-quant-composite` | 图像与定量复合图 | Image-plus-quantification Composite | 无 | 复合图与高级可视化、显微图像与定量 | 按需实现 |
| `asymmetric-multipanel` | 非对称多面板图 | Asymmetric Multipanel Figure | 无 | 复合图与高级可视化 | 可复用模式 |
| `small-multiples` | 小多图 | Small Multiples | faceted plot | 复合图与高级可视化 | 可复用模式 |
