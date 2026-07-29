# 图型别名索引 / Chart Alias Index

> 本文件由 `scripts/generate_chart_catalog.py` 生成；不要手工编辑。
> 用户语言先路由到 canonical ID，再根据实现状态决定资产复用或新实现。

## 同名异义

| 术语 | 候选 canonical IDs | 路由规则 |
|---|---|---|
| 漏斗图 | `meta-analysis-funnel-plot`, `conversion-funnel-chart` | 统计估计或医学证据综合使用 meta-analysis-funnel-plot；流程转化使用 conversion-funnel-chart。 |
| 棒棒糖图 | `lollipop-chart`, `mutation-lollipop-plot` | 通用类别排序使用 lollipop-chart；基因突变位点使用 mutation-lollipop-plot。 |
| 瀑布图 | `contribution-waterfall-chart`, `tumor-response-waterfall-plot` | 一般增减贡献使用 contribution-waterfall-chart；肿瘤疗效使用 tumor-response-waterfall-plot。 |
| 蜘蛛图 | `radar-chart`, `tumor-burden-spider-plot` | 多指标画像使用 radar-chart；肿瘤负荷随时间变化使用 tumor-burden-spider-plot。 |

## 全部名称与别名

| Canonical ID | 中文名 | English name | 其他别名 | 分类 | 状态 |
|---|---|---|---|---|---|
| `2d-density-plot` | 二维密度图 | 2D Density Plot | 无 | 数据分布图 | 可复用模式 |
| `ablation-bar-chart` | 消融柱状图 | Ablation Bar Chart | 无 | 数值比较与排序图、分类、预测与机器学习评估图 | 生产模板 |
| `accessibility-map` | 可达性地图 | Accessibility Map | 无 | 空间与地理数据图 | 按需实现 |
| `accumulated-local-effects-plot` | ALE图 | Accumulated Local Effects Plot | 无 | 分类、预测与机器学习评估图 | 按需实现 |
| `adjacency-matrix` | 邻接矩阵图 | Adjacency Matrix | 无 | 网络与关系结构图 | 按需实现 |
| `age-period-cohort-plot` | 年龄—时期—队列图 | Age–Period–Cohort Plot | 无 | 时间趋势与动态变化图 | 可复用模式 |
| `aic-plot` | 信息准则比较图 | AIC Plot | BIC Plot | 回归与统计模型诊断图 | 可复用模式 |
| `ale-plot` | 累积局部效应图 | ALE Plot | 无 | 变量关系与相关性图 | 可复用模式 |
| `algorithm-flow-diagram` | 算法流程图 | Algorithm Flow Diagram | 无 | 研究流程与论文规范图 | 按需实现 |
| `alluvial-diagram` | 冲积图 | Alluvial Diagram | 无 | 流程、迁移与流量图 | 可复用模式 |
| `alluvial-network-evolution-diagram` | Alluvial网络演化图 | Alluvial Network Evolution Diagram | 无 | 网络与关系结构图 | 按需实现 |
| `andrews-curve` | Andrews曲线 | Andrews Curve | 无 | 高维与多变量数据图 | 按需实现 |
| `annotated-heatmap` | 注释热图 | Annotated Heatmap | 无 | 高维与多变量数据图 | 可复用模式 |
| `annual-publication-trend-plot` | 年度发文趋势图 | Annual Publication Trend Plot | 无 | 文献计量与科学知识图谱 | 按需实现 |
| `arc-diagram` | 弧线图 | Arc Diagram | 无 | 网络与关系结构图 | 可复用模式 |
| `area-chart` | 面积图 | Area Chart | 无 | 时间趋势与动态变化图、构成、比例与整体—部分关系图 | 可复用模式 |
| `association-plot` | 关联图 | Association Plot | 无 | 变量关系与相关性图、集合、重叠与分类组合图 | 可复用模式 |
| `association-rule-network` | 关联规则网络图 | Association Rule Network | 无 | 网络与关系结构图 | 按需实现 |
| `asymmetric-multipanel` | 非对称多面板图 | Asymmetric Multipanel Figure | 无 | 复合图与高级科研图形 | 可复用模式 |
| `author-collaboration-network` | 作者合作网络图 | Author Collaboration Network | 无 | 网络与关系结构图、文献计量与科学知识图谱 | 按需实现 |
| `autocorrelation-plot` | 自相关图 | Autocorrelation Plot | ACF | 时间趋势与动态变化图 | 可复用模式 |
| `bar-and-line-composite-chart` | 柱线组合图 | Bar and Line Composite Chart | 无 | 复合图与高级科研图形 | 按需实现 |
| `bar-matrix` | 条形图矩阵 | Bar Matrix | 无 | 数值比较与排序图 | 可复用模式 |
| `bathtub-curve` | 浴盆曲线 | Bathtub Curve | 无 | 工程、质量管理与过程控制图 | 按需实现 |
| `bayesian-half-eye-plot` | 贝叶斯半眼图 | Bayesian Half-eye Plot | 无 | 统计估计、效应量与不确定性图 | 可复用模式 |
| `bayesian-ridgeline-plot` | 贝叶斯山脊图 | Bayesian Ridgeline Plot | 无 | 统计估计、效应量与不确定性图 | 可复用模式 |
| `bean-plot` | 豆荚图 | Bean Plot | 无 | 数据分布图 | 可复用模式 |
| `beeswarm-plot` | 蜂群图 | Beeswarm Plot | Sina图；Sina plot；Sina Plot；swarm plot | 数据分布图 | 可复用模式 |
| `before-after-bar-chart` | 前后比较柱状图 | Before–After Bar Chart | 无 | 数值比较与排序图、工程、质量管理与过程控制图 | 生产模板 |
| `between-group-box-plot` | 组间箱线图 | Between-group Box Plot | 无 | 实验设计与组间差异图 | 可复用模式 |
| `between-group-mean-plot` | 组间均值图 | Between-group Mean Plot | 无 | 实验设计与组间差异图 | 可复用模式 |
| `bias-variance-plot` | 偏差—方差图 | Bias Variance Plot | 无 | 回归与统计模型诊断图 | 可复用模式 |
| `bibliographic-coupling` | 文献耦合网络图 | Bibliographic Coupling | 无 | 网络与关系结构图 | 按需实现 |
| `bibliographic-coupling-network` | 文献耦合网络 | Bibliographic Coupling Network | 文献耦合图 | 网络与关系结构图、文献计量与科学知识图谱 | 按需实现 |
| `bifurcation-diagram` | 分岔图 | Bifurcation Diagram | 无 | 三维、曲面与科学计算图 | 按需实现 |
| `binary-contingency-table-plot` | 二元交叉表图 | Binary Contingency Table Plot | 无 | 集合、重叠与分类组合图 | 可复用模式 |
| `biomarker-box-plot` | 生物标志物箱线图 | Biomarker Box Plot | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `bipartite-network` | 二模网络图 | Bipartite Network | 无 | 网络与关系结构图 | 按需实现 |
| `biplot` | 双标图 | Biplot | 无 | 变量关系与相关性图、高维与多变量数据图 | 可复用模式 |
| `bivariate-choropleth-map` | 双变量分级设色地图 | Bivariate Choropleth Map | 无 | 空间与地理数据图 | 按需实现 |
| `bland-altman-plot` | Bland–Altman图 | Bland–Altman Plot | agreement plot | 变量关系与相关性图、实验设计与组间差异图、回归与统计模型诊断图、医学、公共卫生与生命科学常用图 | 可复用模式 |
| `bode-plot` | Bode图 | Bode Plot | 无 | 三维、曲面与科学计算图 | 按需实现 |
| `bootstrap-distribution-plot` | Bootstrap分布图 | Bootstrap Distribution Plot | 无 | 统计估计、效应量与不确定性图 | 可复用模式 |
| `box-and-scatter-overlay-plot` | 箱线—散点叠加图 | Box and Scatter Overlay Plot | 无 | 复合图与高级科研图形 | 按需实现 |
| `box-plot` | 箱线图 | Box Plot | box-and-whisker plot | 数据分布图 | 可复用模式 |
| `boxen-plot` | 箱百分位图 | Boxen Plot | Letter-value Plot | 数据分布图 | 可复用模式 |
| `bradford-zones-plot` | Bradford分区图 | Bradford Zones Plot | 无 | 文献计量与科学知识图谱 | 按需实现 |
| `bubble-scatter` | 气泡散点图 | Bubble Scatter | 气泡图；bubble chart；Bubble Chart | 变量关系与相关性图 | 生产模板 |
| `bullet-chart` | 子弹图 | Bullet Chart | 无 | 数值比较与排序图、工程、质量管理与过程控制图 | 可复用模式 |
| `bump-chart` | 排名变化图 | Bump Chart | 无 | 数值比较与排序图 | 可复用模式 |
| `c-control-chart` | C控制图 | C Control Chart | 无 | 工程、质量管理与过程控制图 | 按需实现 |
| `calendar-heatmap` | 日历热图 | Calendar Heatmap | 日历热力图 | 时间趋势与动态变化图、高维与多变量数据图、工程、质量管理与过程控制图 | 可复用模式 |
| `calibration-curve` | 校准曲线 | Calibration Curve | 校准图；Calibration Plot；reliability diagram | 回归与统计模型诊断图、分类、预测与机器学习评估图、医学、公共卫生与生命科学常用图 | 可复用模式 |
| `canonical-correlation-plot` | 典型相关图 | Canonical Correlation Plot | 无 | 变量关系与相关性图 | 可复用模式 |
| `cartogram` | Cartogram变形地图 | Cartogram | 无 | 空间与地理数据图 | 按需实现 |
| `case-comparison-matrix` | 案例比较矩阵 | Case Comparison Matrix | 无 | 质性研究与文本分析图 | 按需实现 |
| `case-timeline` | 病例时间轴 | Case Timeline | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `categorical-bar-chart` | 分类柱状图 | Categorical Bar Chart | 柱状图；Bar Chart | 数值比较与排序图 | 生产模板 |
| `caterpillar-plot` | 毛毛虫图 | Caterpillar Plot | 无 | 统计估计、效应量与不确定性图 | 可复用模式 |
| `causal-dag` | 因果有向无环图 | Causal DAG | 因果图；causal diagram；DAG | 实验设计与组间差异图、因果机制与理论模型图 | 按需实现 |
| `causal-flow-diagram` | 因果流程图 | Causal Flow Diagram | 无 | 流程、迁移与流量图 | 按需实现 |
| `causal-forest-plot` | 因果森林图 | Causal Forest Plot | 无 | 因果机制与理论模型图 | 按需实现 |
| `causal-loop-diagram` | 因果回路图 | Causal Loop Diagram | 无 | 因果机制与理论模型图 | 按需实现 |
| `causal-relationship-plot` | 因果关系图 | Causal Relationship Plot | 无 | 质性研究与文本分析图 | 按需实现 |
| `cdf-plot` | 累积分布图 | CDF Plot | 无 | 数据分布图 | 可复用模式 |
| `cell-communication-network` | 细胞通信网络图 | Cell Communication Network | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `cell-composition-plot` | 细胞组成图 | Cell Composition Plot | 无 | 构成、比例与整体—部分关系图、医学、公共卫生与生命科学常用图 | 可复用模式 |
| `chaotic-attractor-plot` | 混沌吸引子图 | Chaotic Attractor Plot | 无 | 三维、曲面与科学计算图 | 按需实现 |
| `chart-and-table-composite-figure` | 图表—表格组合 | Chart and Table Composite Figure | 无 | 复合图与高级科研图形 | 按需实现 |
| `chernoff-faces-plot` | Chernoff脸谱图 | Chernoff Faces Plot | 无 | 高维与多变量数据图 | 按需实现 |
| `chord-diagram` | 弦图 | Chord Diagram | 无 | 网络与关系结构图、流程、迁移与流量图、医学、公共卫生与生命科学常用图 | 生产模板 |
| `choropleth-map` | 分级设色地图 | Choropleth Map | 无 | 空间与地理数据图 | 按需实现 |
| `circos-plot` | Circos图 | Circos Plot | 无 | 医学、公共卫生与生命科学常用图、复合图与高级科研图形 | 按需实现 |
| `circular-hierarchy-plot` | 圆环层级图 | Circular Hierarchy Plot | 无 | 构成、比例与整体—部分关系图 | 可复用模式 |
| `circular-packing` | 圆形打包图 | Circle Packing | 无 | 构成、比例与整体—部分关系图、层级与分类结构图、流程、迁移与流量图 | 可复用模式 |
| `citation-lifecycle-plot` | 引用生命周期图 | Citation Lifecycle Plot | 无 | 文献计量与科学知识图谱 | 按需实现 |
| `citation-network` | 引文网络图 | Citation Network | 无 | 网络与关系结构图、文献计量与科学知识图谱 | 按需实现 |
| `citation-relationship-plot` | 引文关系图 | Citation Relationship Plot | 无 | 质性研究与文本分析图 | 按需实现 |
| `citation-tree-ring-plot` | 引文年轮图 | Citation Tree-ring Plot | 无 | 文献计量与科学知识图谱 | 按需实现 |
| `class-and-school-value-added-plot` | 班级／学校增值图 | Class and School Value-added Plot | 无 | 教育学与心理测量常用图 | 按需实现 |
| `classification-tree-plot` | 分类树图 | Classification Tree Plot | 无 | 层级与分类结构图 | 按需实现 |
| `classroom-interaction-network` | 课堂互动网络图 | Classroom Interaction Network | 无 | 教育学与心理测量常用图 | 按需实现 |
| `cluster-timeline-view` | 聚类时间线视图 | Cluster Timeline View | 无 | 文献计量与科学知识图谱 | 按需实现 |
| `clustered-heatmap` | 聚类热图 | Clustered Heatmap | 聚类热力图 | 分类、预测与机器学习评估图、高维与多变量数据图 | 可复用模式 |
| `clustering-hierarchy-heatmap` | 聚类层级热力图 | Clustering Hierarchy Heatmap | 无 | 层级与分类结构图 | 按需实现 |
| `co-citation-network` | 共被引网络 | Co-citation Network | 共被引网络图 | 网络与关系结构图、文献计量与科学知识图谱 | 按需实现 |
| `co-occurrence-matrix` | 共现矩阵图 | Co-occurrence Matrix | 无 | 变量关系与相关性图 | 可复用模式 |
| `co-occurrence-network` | 共现网络 | Co-occurrence Network | 共现网络图 | 网络与关系结构图、文献计量与科学知识图谱 | 可复用模式 |
| `co-plot` | 协调图 | Co-plot | 无 | 高维与多变量数据图 | 按需实现 |
| `co-word-matrix-heatmap` | 共词矩阵热力图 | Co-word Matrix Heatmap | 无 | 质性研究与文本分析图 | 按需实现 |
| `co-word-network` | 共词网络 | Co-word Network | 共词网络图 | 网络与关系结构图、文献计量与科学知识图谱 | 按需实现 |
| `coding-co-occurrence-plot` | 编码共现图 | Coding Co-occurrence Plot | 无 | 质性研究与文本分析图 | 按需实现 |
| `coding-framework-diagram` | 编码框架图 | Coding Framework Diagram | 无 | 研究流程与论文规范图 | 按需实现 |
| `coding-frequency-plot` | 编码频次图 | Coding Frequency Plot | 无 | 质性研究与文本分析图 | 按需实现 |
| `coefficient-plot` | 系数图 | Coefficient Plot | dot-whisker plot | 统计估计、效应量与不确定性图、回归与统计模型诊断图 | 可复用模式 |
| `cognitive-diagnosis-attribute-mastery-plot` | 认知诊断属性掌握图 | Cognitive Diagnosis Attribute Mastery Plot | 无 | 教育学与心理测量常用图 | 按需实现 |
| `cohort-retention-heatmap` | 队列留存热图 | Cohort Retention Heatmap | 无 | 高维与多变量数据图、工程、质量管理与过程控制图 | 可复用模式 |
| `collaboration-chord-diagram` | 合作弦图 | Collaboration Chord Diagram | 无 | 文献计量与科学知识图谱 | 按需实现 |
| `colocalization-plot` | 共定位图 | Colocalization Plot | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `combination-matrix` | 组合矩阵 | Combination Matrix | 无 | 集合、重叠与分类组合图 | 可复用模式 |
| `community-network` | 社群网络图 | Community Network | 无 | 网络与关系结构图 | 按需实现 |
| `competing-risk-plot` | 竞争风险图 | Competing Risk Plot | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `complex-plane-plot` | 复平面图 | Complex Plane Plot | 无 | 三维、曲面与科学计算图 | 按需实现 |
| `complex-process-mining` | 复杂流程挖掘图 | Complex Process-mining Plot | 流程挖掘图；Process Mining Diagram | 流程、迁移与流量图、复合图与高级科研图形 | 按需实现 |
| `component-plus-residual-plot` | 成分残差图 | Component-plus-residual Plot | 无 | 回归与统计模型诊断图 | 可复用模式 |
| `composition-bar-chart` | 组成柱状图 | Composition Bar Chart | 无 | 构成、比例与整体—部分关系图 | 生产模板 |
| `concentration-time-curve` | 浓度—时间曲线 | Concentration–time Curve | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `concept-classification-tree` | 概念分类树 | Concept Classification Tree | 无 | 层级与分类结构图 | 按需实现 |
| `concept-framework-diagram` | 概念框架图 | Concept Framework Diagram | 无 | 因果机制与理论模型图 | 按需实现 |
| `concept-map` | 概念地图 | Concept Map | 无 | 质性研究与文本分析图 | 按需实现 |
| `concept-network` | 概念网络图 | Concept Network | 无 | 网络与关系结构图 | 按需实现 |
| `conceptual-mechanism-matrix` | 概念机制矩阵 | Conceptual Mechanism Matrix | 无 | 因果机制与理论模型图 | 按需实现 |
| `conditional-effects-plot` | 条件效应图 | Conditional Effects Plot | 无 | 变量关系与相关性图 | 可复用模式 |
| `conditional-frequency-plot` | 条件频率图 | Conditional Frequency Plot | 无 | 集合、重叠与分类组合图 | 可复用模式 |
| `conditional-scatter-plot` | 条件散点图 | Conditional Scatter Plot | 无 | 变量关系与相关性图 | 可复用模式 |
| `confidence-band-plot` | 置信带图 | Confidence Band Plot | Confidence Band | 时间趋势与动态变化图、统计估计、效应量与不确定性图 | 可复用模式 |
| `confirmatory-factor-analysis-path-diagram` | 验证性因素分析路径图 | Confirmatory Factor Analysis Path Diagram | 无 | 教育学与心理测量常用图 | 按需实现 |
| `confusion-matrix` | 混淆矩阵 | Confusion Matrix | 无 | 回归与统计模型诊断图、分类、预测与机器学习评估图 | 生产模板 |
| `confusion-matrix-heatmap` | 混淆矩阵热力图 | Confusion Matrix Heatmap | 无 | 回归与统计模型诊断图 | 可复用模式 |
| `connected-scatter` | 连接散点图 | Connected Scatter Plot | Connected Dot Plot | 变量关系与相关性图、实验设计与组间差异图 | 可复用模式 |
| `consort-flow-diagram` | CONSORT流程图 | CONSORT Flow Diagram | 无 | 流程、迁移与流量图、医学、公共卫生与生命科学常用图、研究流程与论文规范图 | 按需实现 |
| `context-mechanism-outcome-plot` | Context–Mechanism–Outcome图 | Context Mechanism Outcome Plot | 无 | 因果机制与理论模型图 | 按需实现 |
| `contour-map` | 等值线地图 | Contour Map | 等高线地图；Isoline Map | 空间与地理数据图 | 按需实现 |
| `contour-optimization-plot` | 等高线优化图 | Contour Optimization Plot | 无 | 工程、质量管理与过程控制图 | 按需实现 |
| `contour-plot` | 等高线图 | Contour Plot | 等值线图 | 变量关系与相关性图、三维、曲面与科学计算图 | 可复用模式 |
| `contribution-waterfall-chart` | 贡献瀑布图 | Contribution Waterfall Chart | 瀑布图；waterfall chart；Waterfall Chart | 数值比较与排序图、工程、质量管理与过程控制图 | 可复用模式 |
| `control-chart` | 控制图 | Control Chart | Shewhart chart | 时间趋势与动态变化图、工程、质量管理与过程控制图 | 可复用模式 |
| `convergence-diagnostic-plot` | 收敛诊断图 | Convergence Diagnostic Plot | 无 | 统计估计、效应量与不确定性图 | 可复用模式 |
| `conversion-funnel-chart` | 转化漏斗图 | Conversion Funnel Chart | 漏斗图；漏斗转化图；Funnel Chart；marketing funnel | 流程、迁移与流量图、工程、质量管理与过程控制图 | 可复用模式 |
| `cooks-distance-plot` | Cook距离图 | Cook’s Distance Plot | 无 | 回归与统计模型诊断图 | 可复用模式 |
| `correlation-bubble-matrix` | 相关性气泡矩阵 | Correlation Bubble Matrix | corrplot | 高维与多变量数据图 | 生产模板 |
| `correlation-matrix` | 相关矩阵 | Correlation Matrix | 相关圆图；相关热力图；相关矩阵图；Correlation Heatmap；correlation heatmap；Correlogram | 变量关系与相关性图、高维与多变量数据图 | 生产模板 |
| `correlation-network` | 相关网络图 | Correlation Network | 无 | 网络与关系结构图、高维与多变量数据图 | 生产模板 |
| `country-collaboration-network` | 国家合作网络图 | Country Collaboration Network | 无 | 网络与关系结构图、文献计量与科学知识图谱 | 按需实现 |
| `covariance-matrix-plot` | 协方差矩阵图 | Covariance Matrix Plot | 无 | 变量关系与相关性图 | 可复用模式 |
| `cp-and-cpk-plot` | Cp/Cpk图 | Cp and Cpk Plot | 无 | 工程、质量管理与过程控制图 | 按需实现 |
| `credible-interval-plot` | 后验区间图 | Credible Interval Plot | 无 | 统计估计、效应量与不确定性图 | 可复用模式 |
| `cross-level-effect-model-diagram` | 跨层作用模型图 | Cross-level Effect Model Diagram | 无 | 因果机制与理论模型图 | 按需实现 |
| `cross-validation-results-plot` | 交叉验证结果图 | Cross-validation Results Plot | 无 | 回归与统计模型诊断图 | 可复用模式 |
| `cumming-estimation-plot` | Cumming估计图 | Cumming Estimation Plot | 无 | 统计估计、效应量与不确定性图 | 可复用模式 |
| `cumulative-curve` | 累积曲线 | Cumulative Curve | 无 | 时间趋势与动态变化图 | 可复用模式 |
| `cumulative-gains-chart` | 累积增益图 | Cumulative Gains Chart | 无 | 分类、预测与机器学习评估图 | 按需实现 |
| `cumulative-hazard-curve` | 累计风险曲线 | Cumulative Hazard Curve | 累积风险曲线 | 医学、公共卫生与生命科学常用图 | 可复用模式 |
| `cumulative-incidence-curve` | 累计发生率曲线 | Cumulative Incidence Curve | 累积发生函数图 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `cumulative-incidence-plot` | 累积发生图 | Cumulative Incidence Plot | 无 | 时间趋势与动态变化图 | 可复用模式 |
| `cusum-control-chart` | CUSUM控制图 | CUSUM Control Chart | 无 | 工程、质量管理与过程控制图 | 按需实现 |
| `data-cleaning-flow-diagram` | 数据清洗流程图 | Data Cleaning Flow Diagram | 无 | 研究流程与论文规范图 | 按需实现 |
| `data-flow-diagram` | 数据流图 | Data Flow Diagram | 无 | 流程、迁移与流量图 | 按需实现 |
| `data-processing-flow-diagram` | 数据处理流程图 | Data Processing Flow Diagram | 无 | 研究流程与论文规范图 | 按需实现 |
| `database-structure-diagram` | 数据库结构图 | Database Structure Diagram | 无 | 研究流程与论文规范图 | 按需实现 |
| `decision-curve` | 决策曲线 | Decision Curve | DCA；decision curve analysis；Decision Curve Analysis | 回归与统计模型诊断图、分类、预测与机器学习评估图、医学、公共卫生与生命科学常用图 | 按需实现 |
| `decision-tree-diagram` | 决策树图 | Decision Tree Diagram | 无 | 分类、预测与机器学习评估图、层级与分类结构图 | 按需实现 |
| `dem` | 数字高程模型图 | DEM | 无 | 空间与地理数据图 | 按需实现 |
| `dendrogram` | 树状图 | Dendrogram | 系统树图；聚类树状图 | 分类、预测与机器学习评估图、层级与分类结构图、网络与关系结构图、高维与多变量数据图、医学、公共卫生与生命科学常用图 | 可复用模式 |
| `density-contour-plot` | 等高密度图 | Density Contour Plot | 无 | 数据分布图 | 可复用模式 |
| `density-heatmap` | 密度热图 | Density Heatmap | 无 | 高维与多变量数据图 | 生产模板 |
| `diagnostic-test-plot` | 诊断试验性能图 | Diagnostic Test Performance Plot | 无 | 回归与统计模型诊断图、医学、公共卫生与生命科学常用图 | 可复用模式 |
| `difference-in-differences-plot` | 双重差分图 | Difference-in-Differences Plot | 差异中的差异图；DID plot | 实验设计与组间差异图、医学、公共卫生与生命科学常用图 | 可复用模式 |
| `differential-item-functioning-plot` | DIF项目图 | Differential Item Functioning Plot | 无 | 教育学与心理测量常用图 | 按需实现 |
| `dimension-correlation-network` | 维度相关网络图 | Dimension Correlation Network | 无 | 高维与多变量数据图 | 按需实现 |
| `dimensionality-reduction-scatter-plot` | 降维散点图 | Dimensionality Reduction Scatter Plot | 无 | 分类、预测与机器学习评估图 | 按需实现 |
| `discipline-flow-sankey-diagram` | 学科流动桑基图 | Discipline Flow Sankey Diagram | 无 | 文献计量与科学知识图谱 | 按需实现 |
| `discourse-structure-diagram` | 话语结构图 | Discourse Structure Diagram | 无 | 质性研究与文本分析图 | 按需实现 |
| `displacement-contour-plot` | 位移云图 | Displacement Contour Plot | 无 | 三维、曲面与科学计算图 | 按需实现 |
| `diverging-bar-chart` | 双向条形图 | Diverging Bar Chart | 无 | 数值比较与排序图 | 可复用模式 |
| `diverging-stacked-bar-chart` | 发散堆叠柱状图 | Diverging Stacked Bar Chart | Likert chart | 构成、比例与整体—部分关系图 | 可复用模式 |
| `document-co-citation-cluster-plot` | 文献共被引聚类图 | Document Co-citation Cluster Plot | 无 | 文献计量与科学知识图谱 | 按需实现 |
| `document-term-matrix-plot` | 文档—术语矩阵图 | Document–term Matrix Plot | 无 | 质性研究与文本分析图 | 按需实现 |
| `donut-chart` | 环形图 | Donut Chart | 无 | 构成、比例与整体—部分关系图 | 可复用模式 |
| `dose-response-curve` | 剂量—反应曲线 | Dose Response Curve | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `dose-response-plot` | 剂量—反应图 | Dose–Response Plot | 无 | 实验设计与组间差异图 | 可复用模式 |
| `dot-density-map` | 点密度地图 | Dot Density Map | 无 | 空间与地理数据图 | 按需实现 |
| `dot-distribution-plot` | 点阵分布图 | Dot Distribution Plot | 无 | 数据分布图 | 可复用模式 |
| `dot-plot` | 点图 | Dot Plot | 克利夫兰点图；Cleveland Dot Plot；Cleveland dot plot | 数值比较与排序图、数据分布图 | 可复用模式 |
| `dual-axis-chart` | 双轴图 | Dual-axis Chart | 无 | 复合图与高级科研图形 | 按需实现 |
| `dual-map-overlay` | 双图叠加图 | Dual-map Overlay | 无 | 文献计量与科学知识图谱 | 按需实现 |
| `dumbbell-chart` | 哑铃图 | Dumbbell Chart | 无 | 数值比较与排序图 | 可复用模式 |
| `ecdf-plot` | 经验累积分布图 | ECDF Plot | ECDF图；Empirical Cumulative Distribution Function | 数据分布图 | 可复用模式 |
| `effect-size-plot` | 效应量图 | Effect Size Plot | 无 | 统计估计、效应量与不确定性图 | 可复用模式 |
| `ego-network` | Ego Network | Ego Network | 无 | 网络与关系结构图 | 按需实现 |
| `elbow-plot` | 肘部法图 | Elbow Plot | 无 | 分类、预测与机器学习评估图 | 按需实现 |
| `electric-field-distribution-plot` | 电场分布图 | Electric Field Distribution Plot | 无 | 三维、曲面与科学计算图 | 按需实现 |
| `energy-flow-diagram` | 能量流图 | Energy Flow Diagram | 无 | 流程、迁移与流量图 | 按需实现 |
| `enrichment-bar-chart` | 富集条形图 | Enrichment Bar Chart | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `enrichment-bubble-plot` | 富集气泡图 | Enrichment Bubble Plot | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `epidemic-curve` | 流行病曲线 | Epidemic Curve | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `equivalence-plot` | 等效性检验图 | Equivalence Plot | 无 | 实验设计与组间差异图 | 可复用模式 |
| `error-analysis-matrix` | 误差分析矩阵 | Error Analysis Matrix | 无 | 分类、预测与机器学习评估图 | 按需实现 |
| `error-bar-plot` | 误差线图 | Error Bar Plot | 误差棒图 | 统计估计、效应量与不确定性图 | 可复用模式 |
| `estimated-marginal-means-plot` | 边际均值图 | Estimated Marginal Means Plot | 无 | 统计估计、效应量与不确定性图 | 可复用模式 |
| `euler-diagram` | 欧拉图 | Euler Diagram | Euler图 | 集合、重叠与分类组合图 | 可复用模式 |
| `event-sequence-plot` | 事件序列图 | Event Sequence Plot | 无 | 流程、迁移与流量图 | 按需实现 |
| `event-study-plot` | 事件研究图 | Event Study Plot | 无 | 时间趋势与动态变化图、实验设计与组间差异图、医学、公共卫生与生命科学常用图 | 可复用模式 |
| `event-tree` | 事件树 | Event Tree | 无 | 工程、质量管理与过程控制图 | 按需实现 |
| `evidence-chain-diagram` | 证据链图 | Evidence Chain Diagram | 无 | 质性研究与文本分析图、因果机制与理论模型图 | 按需实现 |
| `evidence-synthesis-flow-diagram` | 证据综合流程图 | Evidence Synthesis Flow Diagram | 无 | 研究流程与论文规范图 | 按需实现 |
| `evolutionary-tree` | 进化树 | Evolutionary Tree | 无 | 层级与分类结构图 | 按需实现 |
| `ewma-control-chart` | EWMA控制图 | EWMA Control Chart | 无 | 工程、质量管理与过程控制图 | 按需实现 |
| `experiment-apparatus-schematic` | 实验装置示意图 | Experiment Apparatus Schematic | 无 | 研究流程与论文规范图 | 按需实现 |
| `experiment-step-plot` | 实验步骤图 | Experiment Step Plot | 无 | 研究流程与论文规范图 | 按需实现 |
| `facet-plot` | 分面图 | Facet Plot | 无 | 复合图与高级科研图形 | 按需实现 |
| `faceted-scatter-plot` | 分面散点图 | Faceted Scatter Plot | 无 | 变量关系与相关性图 | 可复用模式 |
| `factor-loading-plot` | 因子载荷图 | Factor Loading Plot | 无 | 高维与多变量数据图、教育学与心理测量常用图 | 按需实现 |
| `fan-chart` | 扇形预测图 | Fan Chart | 扇形图 | 时间趋势与动态变化图、统计估计、效应量与不确定性图 | 可复用模式 |
| `fault-tree` | 故障树 | Fault Tree | 无 | 工程、质量管理与过程控制图 | 按需实现 |
| `feature-importance-plot` | 特征重要性图 | Feature Importance Plot | 无 | 分类、预测与机器学习评估图 | 可复用模式 |
| `feature-interaction-plot` | 特征交互图 | Feature Interaction Plot | 无 | 分类、预测与机器学习评估图 | 按需实现 |
| `finite-element-mesh-plot` | 有限元网格图 | Finite Element Mesh Plot | 无 | 三维、曲面与科学计算图 | 按需实现 |
| `flow-ability-plot` | 流程能力图 | Flow Ability Plot | 无 | 工程、质量管理与过程控制图 | 按需实现 |
| `flow-map` | 流向地图 | Flow Map | 迁徙流向地图 | 空间与地理数据图 | 按需实现 |
| `fluid-particle-trajectory-plot` | 流体粒子轨迹图 | Fluid Particle Trajectory Plot | 无 | 三维、曲面与科学计算图 | 按需实现 |
| `fmea-risk-matrix` | FMEA风险矩阵 | FMEA Risk Matrix | 无 | 工程、质量管理与过程控制图 | 按需实现 |
| `force-plot` | SHAP力图 | Force Plot | 无 | 分类、预测与机器学习评估图 | 按需实现 |
| `forecast-plot` | 时间序列预测图 | Forecast Plot | 无 | 时间趋势与动态变化图 | 可复用模式 |
| `forest-and-funnel-composite-figure` | 森林图—漏斗图组合 | Forest and Funnel Composite Figure | 无 | 复合图与高级科研图形 | 按需实现 |
| `forest-plot` | 森林图 | Forest Plot | 无 | 统计估计、效应量与不确定性图、医学、公共卫生与生命科学常用图 | 可复用模式 |
| `framework-matrix` | 框架矩阵 | Framework Matrix | 无 | 质性研究与文本分析图 | 按需实现 |
| `frequency-3d-heatmap` | 三维频率热图 | Three-dimensional Frequency Heatmap | 无 | 高维与多变量数据图、复合图与高级科研图形 | 生产模板 |
| `frequency-polygon` | 频率多边形 | Frequency Polygon | 无 | 数据分布图 | 可复用模式 |
| `gage-r-and-r-plot` | Gage R&R图 | Gage R&R Plot | 无 | 工程、质量管理与过程控制图 | 按需实现 |
| `gain-curve` | Gain曲线 | Gain Curve | 无 | 回归与统计模型诊断图 | 可复用模式 |
| `gantt-chart` | 甘特图 | Gantt Chart | 无 | 时间趋势与动态变化图、工程、质量管理与过程控制图 | 可复用模式 |
| `gardner-altman-estimation-plot` | Gardner–Altman估计图 | Gardner Altman Estimation Plot | 无 | 统计估计、效应量与不确定性图 | 可复用模式 |
| `gene-expression-heatmap` | 基因表达热力图 | Gene Expression Heatmap | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `genealogy-plot` | 家谱图 | Genealogy Plot | 无 | 层级与分类结构图 | 按需实现 |
| `genome-browser-track` | 基因组浏览器轨道 | Genome Browser Track | 基因组浏览器轨迹图 | 医学、公共卫生与生命科学常用图、复合图与高级科研图形 | 按需实现 |
| `geographic-network` | 地理网络图 | Geographic Network | 无 | 空间与地理数据图 | 按需实现 |
| `geographic-scatter-plot` | 地理散点图 | Geographic Scatter Plot | 无 | 空间与地理数据图 | 按需实现 |
| `geographically-weighted-regression-map` | 地理加权回归地图 | Geographically Weighted Regression Map | 无 | 空间与地理数据图 | 按需实现 |
| `glyph-plot` | Glyph图 | Glyph Plot | 无 | 高维与多变量数据图 | 按需实现 |
| `grand-tour` | Grand Tour动态图 | Grand Tour | 无 | 高维与多变量数据图、复合图与高级科研图形 | 按需实现 |
| `grid-map` | 网格地图 | Grid Map | 无 | 空间与地理数据图 | 按需实现 |
| `grounded-theory-category-relationship-diagram` | 扎根理论范畴关系图 | Grounded Theory Category Relationship Diagram | 无 | 质性研究与文本分析图 | 按需实现 |
| `grouped-bar-chart` | 分组柱状图 | Grouped Bar Chart | 无 | 数值比较与排序图 | 生产模板 |
| `grouped-correlation-matrix` | 分组相关矩阵 | Grouped Correlation Matrix | 无 | 高维与多变量数据图 | 生产模板 |
| `grouped-violin-plot` | 分组小提琴图 | Grouped Violin Plot | 组间小提琴图 | 数据分布图、实验设计与组间差异图 | 生产模板 |
| `growth-curve` | 成长曲线图 | Growth Curve | 生长曲线 | 教育学与心理测量常用图、医学、公共卫生与生命科学常用图 | 按需实现 |
| `gsea-curve` | GSEA富集曲线 | GSEA Enrichment Curve | GSEA曲线 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `half-eye-plot` | 半眼图 | Half-eye Plot | 无 | 数据分布图 | 可复用模式 |
| `heat-conduction-field-plot` | 热传导场图 | Heat Conduction Field Plot | 无 | 三维、曲面与科学计算图 | 按需实现 |
| `heatmap` | 热图 | Heatmap | 无 | 高维与多变量数据图 | 生产模板 |
| `heatmap-and-dendrogram-composite-plot` | 热力图—聚类树组合图 | Heatmap and Dendrogram Composite Plot | 无 | 复合图与高级科研图形 | 按需实现 |
| `heteroscedasticity-diagnostic-plot` | 异方差诊断图 | Heteroscedasticity Diagnostic Plot | 无 | 回归与统计模型诊断图 | 可复用模式 |
| `hexbin-map` | 蜂窝地图 | Hexbin Map | 六边形网格地图 | 空间与地理数据图 | 按需实现 |
| `hexbin-plot` | 六边形分箱图 | Hexbin Plot | 六边形散点密度图；Hexbin | 数据分布图、变量关系与相关性图 | 可复用模式 |
| `hierarchy-tree` | 层级树 | Hierarchy Tree | Tree Diagram | 层级与分类结构图、流程、迁移与流量图 | 可复用模式 |
| `high-dimensional-clustering-tree` | 高维聚类树 | High-dimensional Clustering Tree | 无 | 高维与多变量数据图 | 按需实现 |
| `highly-cited-publication-ranking-plot` | 高被引文献排名图 | Highly Cited Publication Ranking Plot | 无 | 文献计量与科学知识图谱 | 按需实现 |
| `hillshade` | 阴影地形图 | Hillshade | 无 | 空间与地理数据图 | 按需实现 |
| `histogram` | 直方图 | Histogram | 无 | 数据分布图 | 可复用模式 |
| `hive-plot` | Hive Plot | Hive Plot | 无 | 网络与关系结构图 | 按需实现 |
| `horizon-chart` | 地平线图 | Horizon Chart | 无 | 时间趋势与动态变化图 | 按需实现 |
| `horizontal-bar-chart` | 水平条形图 | Horizontal Bar Chart | 横向条形图 | 数值比较与排序图 | 可复用模式 |
| `hotspot-map` | 热点地图 | Hotspot Map | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `hyperbolic-tree` | 双曲树 | Hyperbolic Tree | 双曲树图 | 层级与分类结构图、流程、迁移与流量图、复合图与高级科研图形 | 按需实现 |
| `hypergraph` | 超图 | Hypergraph | 无 | 网络与关系结构图 | 按需实现 |
| `ice-plot` | 个体条件期望图 | Individual Conditional Expectation Plot | ICE图；ICE plot；ICE Plot | 变量关系与相关性图、分类、预测与机器学习评估图 | 按需实现 |
| `icicle-chart` | 冰柱图 | Icicle Chart | 无 | 层级与分类结构图 | 按需实现 |
| `image-plus-quant-composite` | 图像与定量复合图 | Image-plus-quantification Composite | 无 | 医学、公共卫生与生命科学常用图、复合图与高级科研图形 | 按需实现 |
| `incidence-map` | 发病率地图 | Incidence Map | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `index-chart` | 指数变化图 | Index Chart | 无 | 时间趋势与动态变化图 | 可复用模式 |
| `individual-change-plot` | 个体变化图 | Individual Change Plot | 无 | 实验设计与组间差异图 | 可复用模式 |
| `individual-growth-curve` | 个体成长曲线图 | Individual Growth Curve | 无 | 时间趋势与动态变化图 | 可复用模式 |
| `influence-plot` | 影响度图 | Influence Plot | 无 | 回归与统计模型诊断图 | 可复用模式 |
| `input-process-output-diagram` | 投入—过程—产出图 | Input Process Output Diagram | 无 | 因果机制与理论模型图 | 按需实现 |
| `input-process-output-model-diagram` | IPO模型图 | Input–Process–Output Model Diagram | 无 | 因果机制与理论模型图 | 按需实现 |
| `inset-plot` | 嵌套图 | Inset Plot | 无 | 复合图与高级科研图形 | 按需实现 |
| `institution-collaboration-network` | 机构合作网络图 | Institution Collaboration Network | 无 | 网络与关系结构图、文献计量与科学知识图谱 | 按需实现 |
| `interaction-effect-plot` | 交互效应图 | Interaction Effect Plot | 无 | 回归与统计模型诊断图、工程、质量管理与过程控制图 | 可复用模式 |
| `interaction-plot` | 交互作用图 | Interaction Plot | 无 | 实验设计与组间差异图、教育学与心理测量常用图 | 可复用模式 |
| `interrupted-time-series` | 中断时间序列图 | Interrupted Time-series Plot | 间断时间序列图；ITS plot | 时间趋势与动态变化图、实验设计与组间差异图 | 可复用模式 |
| `intersection-bar-chart` | 交集条形图 | Intersection Bar Chart | 无 | 集合、重叠与分类组合图 | 可复用模式 |
| `interval-heatmap` | 区间热力图 | Interval Heatmap | 无 | 统计估计、效应量与不确定性图 | 可复用模式 |
| `interval-plot` | 区间图 | Interval Plot | 点—区间图；Point-range Plot | 统计估计、效应量与不确定性图 | 可复用模式 |
| `ishikawa-diagram` | 鱼骨图 | Ishikawa Diagram | 无 | 工程、质量管理与过程控制图 | 按需实现 |
| `isochrone-map` | 等时圈地图 | Isochrone Map | 无 | 空间与地理数据图 | 按需实现 |
| `isopleth-map` | 等值区域图 | Isopleth Map | 无 | 空间与地理数据图 | 按需实现 |
| `isosurface` | 等值面 | Isosurface | 等值面图；Isosurface Plot | 医学、公共卫生与生命科学常用图、三维、曲面与科学计算图、复合图与高级科研图形 | 按需实现 |
| `item-characteristic-curve` | 题目特征曲线 | Item Characteristic Curve | 题目反应曲线；ICC | 教育学与心理测量常用图 | 按需实现 |
| `item-difficulty-distribution-plot` | 项目难度分布图 | Item Difficulty Distribution Plot | 无 | 教育学与心理测量常用图 | 按需实现 |
| `item-fit-plot` | 项目拟合图 | Item Fit Plot | 无 | 教育学与心理测量常用图 | 按需实现 |
| `item-information-curve` | 项目信息曲线 | Item Information Curve | 无 | 教育学与心理测量常用图 | 按需实现 |
| `jitter-plot` | 抖动散点图 | Jitter Plot | 无 | 数据分布图 | 可复用模式 |
| `joint-plot` | 联合分布图 | Joint Plot | 无 | 变量关系与相关性图 | 可复用模式 |
| `journal-publication-count-plot` | 期刊发文量图 | Journal Publication Count Plot | 无 | 文献计量与科学知识图谱 | 按需实现 |
| `kaplan-meier-curve` | Kaplan–Meier曲线 | Kaplan–Meier Curve | Kaplan–Meier生存曲线；KM curve | 医学、公共卫生与生命科学常用图 | 可复用模式 |
| `kernel-density-map` | 核密度地图 | Kernel Density Map | 无 | 空间与地理数据图 | 按需实现 |
| `kernel-density-plot` | 核密度图 | Kernel Density Plot | 密度图；核密度估计图；Density Plot；KDE | 数据分布图、变量关系与相关性图 | 生产模板 |
| `keyword-burst-plot` | 关键词突现图 | Keyword Burst Plot | Burst Detection | 质性研究与文本分析图、文献计量与科学知识图谱 | 按需实现 |
| `keyword-clustering-plot` | 关键词聚类图 | Keyword Clustering Plot | 无 | 文献计量与科学知识图谱 | 按需实现 |
| `keyword-co-occurrence-network` | 关键词共现网络图 | Keyword Co-occurrence Network | 无 | 质性研究与文本分析图、文献计量与科学知识图谱 | 按需实现 |
| `keyword-time-zone-plot` | 关键词时区图 | Keyword Time-zone Plot | 无 | 文献计量与科学知识图谱 | 按需实现 |
| `keyword-timeline-plot` | 关键词时间线图 | Keyword Timeline Plot | 无 | 文献计量与科学知识图谱 | 按需实现 |
| `knowledge-base-cluster-plot` | 知识基础聚类图 | Knowledge Base Cluster Plot | 无 | 文献计量与科学知识图谱 | 按需实现 |
| `knowledge-graph` | 知识图谱 | Knowledge Graph | 无 | 网络与关系结构图 | 按需实现 |
| `knowledge-mastery-heatmap` | 知识掌握热力图 | Knowledge Mastery Heatmap | 无 | 教育学与心理测量常用图 | 按需实现 |
| `kolmogorov-smirnov-curve` | KS曲线 | Kolmogorov–Smirnov Curve | 无 | 回归与统计模型诊断图 | 可复用模式 |
| `kolmogorov-smirnov-plot` | KS图 | Kolmogorov–Smirnov Plot | 无 | 分类、预测与机器学习评估图 | 按需实现 |
| `kpi-card` | KPI卡片 | KPI Card | 无 | 工程、质量管理与过程控制图 | 按需实现 |
| `lag-plot` | 滞后图 | Lag Plot | 无 | 时间趋势与动态变化图 | 可复用模式 |
| `land-use-classification-plot` | 土地利用分类图 | Land Use Classification Plot | 无 | 空间与地理数据图 | 按需实现 |
| `lasso-coefficient-path-plot` | LASSO系数路径图 | LASSO Coefficient Path Plot | 无 | 回归与统计模型诊断图 | 可复用模式 |
| `latent-class-probability-plot` | 潜在类别概率图 | Latent Class Probability Plot | 无 | 教育学与心理测量常用图 | 按需实现 |
| `latent-growth-curve-plot` | 潜在增长曲线图 | Latent Growth Curve Plot | 无 | 教育学与心理测量常用图 | 按需实现 |
| `latent-profile-plot` | 潜在剖面图 | Latent Profile Plot | 无 | 教育学与心理测量常用图 | 按需实现 |
| `learner-profile-cluster-plot` | 学习者画像聚类图 | Learner Profile Cluster Plot | 无 | 教育学与心理测量常用图 | 按需实现 |
| `learning-achievement-distribution-plot` | 学习成绩分布图 | Learning Achievement Distribution Plot | 无 | 教育学与心理测量常用图 | 按需实现 |
| `learning-behavior-time-series-plot` | 学习行为时间序列图 | Learning Behavior Time-series Plot | 无 | 教育学与心理测量常用图 | 按需实现 |
| `learning-curve` | 学习曲线 | Learning Curve | 无 | 回归与统计模型诊断图、分类、预测与机器学习评估图 | 可复用模式 |
| `learning-engagement-radar-chart` | 学习投入雷达图 | Learning Engagement Radar Chart | 无 | 教育学与心理测量常用图 | 按需实现 |
| `learning-path-diagram` | 学习路径图 | Learning Path Diagram | 无 | 流程、迁移与流量图 | 按需实现 |
| `learning-path-sankey-diagram` | 学习路径桑基图 | Learning Path Sankey Diagram | 无 | 教育学与心理测量常用图 | 按需实现 |
| `learning-trajectory-plot` | 学习轨迹图 | Learning Trajectory Plot | 无 | 教育学与心理测量常用图 | 按需实现 |
| `leverage-plot` | 杠杆值图 | Leverage Plot | 无 | 回归与统计模型诊断图 | 可复用模式 |
| `lifetime-distribution-plot` | 寿命分布图 | Lifetime Distribution Plot | 无 | 工程、质量管理与过程控制图 | 按需实现 |
| `lift-chart` | 提升图 | Lift Chart | 无 | 分类、预测与机器学习评估图 | 按需实现 |
| `lift-curve` | Lift曲线 | Lift Curve | 无 | 回归与统计模型诊断图 | 可复用模式 |
| `lime-explanation-plot` | LIME解释图 | LIME Explanation Plot | 无 | 分类、预测与机器学习评估图 | 按需实现 |
| `line-chart` | 折线图 | Line Chart | 多序列折线图；Multiple Line Chart；trend plot | 时间趋势与动态变化图 | 生产模板 |
| `line-scan-intensity` | 线扫描强度图 | Line-scan Intensity Plot | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `literature-screening-plot` | 文献筛选图 | Literature Screening Plot | 无 | 研究流程与论文规范图 | 按需实现 |
| `local-indicators-of-spatial-association-cluster-map` | LISA聚类地图 | Local Indicators of Spatial Association Cluster Map | 无 | 空间与地理数据图 | 按需实现 |
| `locuszoom-plot` | 区域关联图 | LocusZoom Plot | Regional Association Plot | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `loess-plot` | 散点平滑图 | LOESS Plot | LOWESS Plot | 变量关系与相关性图 | 可复用模式 |
| `logic-model-plot` | 逻辑模型图 | Logic Model Plot | Logic Model | 质性研究与文本分析图、因果机制与理论模型图 | 按需实现 |
| `logic-tree` | 逻辑树 | Logic Tree | 无 | 因果机制与理论模型图 | 按需实现 |
| `lollipop-chart` | 棒棒糖图 | Lollipop Chart | 无 | 数值比较与排序图 | 可复用模式 |
| `lotka-distribution-plot` | Lotka分布图 | Lotka Distribution Plot | 无 | 文献计量与科学知识图谱 | 按需实现 |
| `love-plot` | 协变量平衡图 | Love Plot | standardized mean difference plot | 实验设计与组间差异图、医学、公共卫生与生命科学常用图 | 可复用模式 |
| `ma-plot` | MA图 | MA Plot | 无 | 医学、公共卫生与生命科学常用图 | 可复用模式 |
| `magnetic-field-distribution-plot` | 磁场分布图 | Magnetic Field Distribution Plot | 无 | 三维、曲面与科学计算图 | 按需实现 |
| `main-effects-plot` | 主效应图 | Main Effects Plot | 无 | 实验设计与组间差异图、工程、质量管理与过程控制图 | 可复用模式 |
| `main-figure-with-magnified-inset` | 主图—局部放大图 | Main Figure with Magnified Inset | 无 | 复合图与高级科研图形 | 按需实现 |
| `manhattan-plot` | 曼哈顿图 | Manhattan Plot | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `manifold-embedding-plot` | 流形嵌入图 | Manifold Embedding Plot | Swiss roll | 高维与多变量数据图 | 生产模板 |
| `mantel-correlation-plot` | Mantel相关图 | Mantel Correlation Plot | Mantel test | 高维与多变量数据图、医学、公共卫生与生命科学常用图 | 生产模板 |
| `map-and-sankey-composite-figure` | 地图—桑基图组合 | Map and Sankey Composite Figure | 无 | 复合图与高级科研图形 | 按需实现 |
| `map-and-time-series-composite-figure` | 地图—时间序列组合 | Map and Time-series Composite Figure | 无 | 复合图与高级科研图形 | 按需实现 |
| `marginal-density-scatter` | 边际密度散点图 | Marginal Density Scatter | 边际分布散点图；Marginal Plot | 变量关系与相关性图 | 生产模板 |
| `marginal-effects-plot` | 边际效应图 | Marginal Effects Plot | 无 | 变量关系与相关性图、回归与统计模型诊断图 | 可复用模式 |
| `marker-gene-dot-plot` | 标记基因点图 | Marker-gene Dot Plot | 无 | 医学、公共卫生与生命科学常用图 | 生产模板 |
| `markov-transition-diagram` | 马尔可夫转移图 | Markov Transition Diagram | 无 | 流程、迁移与流量图 | 按需实现 |
| `material-flow-diagram` | 物质流图 | Material Flow Diagram | 无 | 流程、迁移与流量图 | 按需实现 |
| `matrix-composite-figure` | 矩阵式综合图 | Matrix Composite Figure | 无 | 复合图与高级科研图形 | 按需实现 |
| `mean-and-ci-plot` | 均值—置信区间图 | Mean and CI Plot | 无 | 统计估计、效应量与不确定性图 | 可复用模式 |
| `measurement-agreement-plot` | 测量一致性图 | Measurement Agreement Plot | 无 | 实验设计与组间差异图 | 可复用模式 |
| `measurement-invariance-comparison-plot` | 测量不变性比较图 | Measurement Invariance Comparison Plot | 无 | 教育学与心理测量常用图 | 按需实现 |
| `measurement-system-analysis-plot` | 测量系统分析图 | Measurement System Analysis Plot | 无 | 工程、质量管理与过程控制图 | 按需实现 |
| `mechanism-chain-diagram` | 机制链条图 | Mechanism Chain Diagram | 无 | 因果机制与理论模型图 | 按需实现 |
| `mediation-effect-plot` | 中介效应图 | Mediation Effect Plot | 无 | 教育学与心理测量常用图 | 按需实现 |
| `mediation-model-plot` | 中介模型图 | Mediation Model Plot | 无 | 因果机制与理论模型图 | 按需实现 |
| `mekko-chart` | Marimekko图 | Mekko Chart | 无 | 构成、比例与整体—部分关系图 | 可复用模式 |
| `meta-analysis-funnel-plot` | 元分析漏斗图 | Meta-analysis Funnel Plot | 漏斗图；Funnel Plot；publication-bias funnel plot | 统计估计、效应量与不确定性图、医学、公共卫生与生命科学常用图 | 可复用模式 |
| `method-comparison-bar-chart` | 方法比较柱状图 | Method Comparison Bar Chart | 无 | 数值比较与排序图 | 生产模板 |
| `method-integration-plot` | 方法整合图 | Method Integration Plot | 无 | 研究流程与论文规范图 | 按需实现 |
| `microscopy-image-plate` | 显微图像板 | Microscopy Image Plate | 无 | 医学、公共卫生与生命科学常用图、复合图与高级科研图形 | 按需实现 |
| `mind-map` | 思维导图 | Mind Map | 无 | 质性研究与文本分析图 | 按需实现 |
| `mirror-bar-chart` | 镜像条形图 | Mirror Bar Chart | 无 | 数值比较与排序图 | 可复用模式 |
| `mixed-research-design-plot` | 混合研究设计图 | Mixed Research Design Plot | 无 | 研究流程与论文规范图 | 按需实现 |
| `model-architecture-plot` | 模型架构图 | Model Architecture Plot | 无 | 研究流程与论文规范图 | 按需实现 |
| `model-comparison-plot` | 模型比较图 | Model Comparison Plot | 无 | 回归与统计模型诊断图 | 可复用模式 |
| `model-fairness-comparison-plot` | 模型公平性比较图 | Model Fairness Comparison Plot | 无 | 分类、预测与机器学习评估图 | 按需实现 |
| `model-residual-distribution-plot` | 模型残差分布图 | Model Residual Distribution Plot | 无 | 分类、预测与机器学习评估图 | 按需实现 |
| `moderated-mediation-model-diagram` | 有调节的中介模型图 | Moderated Mediation Model Diagram | 无 | 教育学与心理测量常用图 | 按需实现 |
| `moderation-effect-plot` | 调节效应图 | Moderation Effect Plot | 无 | 教育学与心理测量常用图 | 按需实现 |
| `moderation-mediation-model-plot` | 调节中介模型图 | Moderation Mediation Model Plot | 无 | 因果机制与理论模型图 | 按需实现 |
| `moderation-model-plot` | 调节模型图 | Moderation Model Plot | 无 | 因果机制与理论模型图 | 按需实现 |
| `moran-scatter-plot` | Moran散点图 | Moran Scatter Plot | 无 | 空间与地理数据图 | 按需实现 |
| `mosaic-plot` | 马赛克图 | Mosaic Plot | 无 | 变量关系与相关性图、构成、比例与整体—部分关系图、高维与多变量数据图、集合、重叠与分类组合图 | 可复用模式 |
| `moving-average-plot` | 移动平均图 | Moving Average Plot | 无 | 时间趋势与动态变化图 | 可复用模式 |
| `multi-panel-figure` | 多面板图 | Multi-panel Figure | 无 | 复合图与高级科研图形 | 按需实现 |
| `multiclass-precision-recall-plot` | 多分类PR图 | Multiclass Precision–Recall Plot | 无 | 分类、预测与机器学习评估图 | 按需实现 |
| `multiclass-roc-plot` | 多分类ROC图 | Multiclass ROC Plot | 无 | 分类、预测与机器学习评估图 | 按需实现 |
| `multicollinearity-plot` | 多重共线性图 | Multicollinearity Plot | 无 | 回归与统计模型诊断图 | 可复用模式 |
| `multidimensional-scaling` | MDS图 | Multidimensional Scaling | 无 | 高维与多变量数据图 | 按需实现 |
| `multidimensional-scaling-bubble-plot` | 多维尺度气泡图 | Multidimensional Scaling Bubble Plot | 无 | 高维与多变量数据图 | 按需实现 |
| `multifactor-response-surface-plot` | 多因素响应曲面图 | Multifactor Response Surface Plot | 无 | 实验设计与组间差异图 | 可复用模式 |
| `multilayer-network` | 多层网络图 | Multilayer Network | 无 | 网络与关系结构图 | 按需实现 |
| `multilevel-classification-network` | 多层分类网络图 | Multilevel Classification Network | 无 | 层级与分类结构图 | 按需实现 |
| `multilevel-model-caterpillar-plot` | 多层模型毛毛虫图 | Multilevel Model Caterpillar Plot | 无 | 教育学与心理测量常用图 | 按需实现 |
| `multilevel-theoretical-model-plot` | 多层理论模型图 | Multilevel Theoretical Model Plot | 无 | 因果机制与理论模型图 | 按需实现 |
| `multimodal-visualization` | 多模态可视化图 | Multimodal Visualization | 无 | 复合图与高级科研图形 | 按需实现 |
| `multivariate-box-plot` | 多变量箱线图 | Multivariate Box Plot | 无 | 高维与多变量数据图 | 按需实现 |
| `multivariate-density-plot` | 多变量密度图 | Multivariate Density Plot | 无 | 高维与多变量数据图 | 按需实现 |
| `mutation-landscape` | Mutation Landscape | Mutation Landscape | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `mutation-lollipop-plot` | 突变棒棒糖图 | Mutation Lollipop Plot | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `narrative-timeline` | 叙事时间轴 | Narrative Timeline | 无 | 质性研究与文本分析图 | 按需实现 |
| `nelson-aalen-curve` | Nelson–Aalen曲线 | Nelson–Aalen Curve | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `network-and-timeline-composite-figure` | 网络图—时间线组合 | Network and Timeline Composite Figure | 无 | 复合图与高级科研图形 | 按需实现 |
| `network-centrality-distribution-plot` | 网络中心性分布图 | Network Centrality Distribution Plot | 无 | 网络与关系结构图 | 按需实现 |
| `network-community-sankey-diagram` | 网络社区桑基图 | Network Community Sankey Diagram | 无 | 网络与关系结构图 | 按需实现 |
| `network-degree-distribution-plot` | 网络度分布图 | Network Degree Distribution Plot | 无 | 网络与关系结构图 | 按需实现 |
| `network-matrix-heatmap` | 网络矩阵热力图 | Network Matrix Heatmap | 无 | 网络与关系结构图 | 按需实现 |
| `neural-network-architecture-diagram` | 神经网络结构图 | Neural Network Architecture Diagram | 无 | 研究流程与论文规范图 | 按需实现 |
| `nightingale-rose-chart` | 南丁格尔玫瑰图 | Nightingale Rose Chart | 无 | 数值比较与排序图、构成、比例与整体—部分关系图 | 可复用模式 |
| `node-link-diagram` | 节点—连线图 | Node-link Diagram | 无 | 网络与关系结构图 | 按需实现 |
| `nomogram` | 列线图 | Nomogram | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `non-inferiority-plot` | 非劣效性图 | Non-inferiority Plot | 无 | 实验设计与组间差异图 | 可复用模式 |
| `notched-box-plot` | 缺口箱线图 | Notched Box Plot | 无 | 数据分布图 | 可复用模式 |
| `np-control-chart` | NP控制图 | NP Control Chart | 无 | 工程、质量管理与过程控制图 | 按需实现 |
| `nyquist-plot` | Nyquist图 | Nyquist Plot | 无 | 三维、曲面与科学计算图 | 按需实现 |
| `objective-tree` | 目标树 | Objective Tree | 无 | 因果机制与理论模型图 | 按需实现 |
| `od-map` | OD地图 | OD Map | 无 | 空间与地理数据图 | 按需实现 |
| `odds-ratio-forest-plot` | OR值森林图 | Odds Ratio Forest Plot | 无 | 统计估计、效应量与不确定性图 | 可复用模式 |
| `oncoplot` | Oncoplot | Oncoplot | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `oncoprint` | 肿瘤突变谱图 | OncoPrint | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `organization-structure-diagram` | 组织结构图 | Organization Structure Diagram | 无 | 层级与分类结构图 | 按需实现 |
| `origin-destination-flow` | OD流向图 | Origin–Destination Flow | 无 | 流程、迁移与流量图 | 按需实现 |
| `orthogonal-design-effect-plot` | 正交设计效应图 | Orthogonal Design Effect Plot | 无 | 实验设计与组间差异图 | 可复用模式 |
| `overlap-heatmap` | 重叠热力图 | Overlap Heatmap | 无 | 集合、重叠与分类组合图 | 可复用模式 |
| `p-control-chart` | P控制图 | P Control Chart | 无 | 工程、质量管理与过程控制图 | 按需实现 |
| `packed-bubble-chart` | 嵌套气泡图 | Packed Bubble Chart | 无 | 构成、比例与整体—部分关系图 | 可复用模式 |
| `paired-box-scatter` | 配对箱线散点图 | Paired Box Scatter | before-after plot | 数据分布图 | 生产模板 |
| `paired-dot-plot` | 配对点图 | Paired Dot Plot | 无 | 实验设计与组间差异图 | 可复用模式 |
| `paired-line-plot` | 前后测配对线图 | Paired Line Plot | 无 | 实验设计与组间差异图 | 可复用模式 |
| `parallel-analysis-plot` | 平行分析图 | Parallel Analysis Plot | 无 | 高维与多变量数据图、教育学与心理测量常用图 | 可复用模式 |
| `parallel-coordinates` | 平行坐标图 | Parallel Coordinates | 无 | 数值比较与排序图、高维与多变量数据图、复合图与高级科研图形 | 可复用模式 |
| `parallel-sets` | 平行集合图 | Parallel Sets | 无 | 流程、迁移与流量图、高维与多变量数据图 | 按需实现 |
| `pareto-chart` | 帕累托图 | Pareto Chart | 无 | 数值比较与排序图、工程、质量管理与过程控制图 | 可复用模式 |
| `partial-autocorrelation-plot` | 偏自相关图 | Partial Autocorrelation Plot | PACF | 时间趋势与动态变化图 | 可复用模式 |
| `partial-correlation-plot` | 偏相关图 | Partial Correlation Plot | 无 | 变量关系与相关性图 | 可复用模式 |
| `partial-dependence-plot` | 部分依赖图 | Partial Dependence Plot | PDP图；PDP | 变量关系与相关性图、分类、预测与机器学习评估图 | 按需实现 |
| `partial-regression-plot` | 偏回归图 | Partial Regression Plot | 无 | 回归与统计模型诊断图 | 可复用模式 |
| `path-diagram` | 路径图 | Path Diagram | 无 | 因果机制与理论模型图 | 按需实现 |
| `pathology-image-plate` | 病理图像板 | Pathology Image Plate | 无 | 医学、公共卫生与生命科学常用图、复合图与高级科研图形 | 按需实现 |
| `patient-flow-diagram` | 患者流程图 | Patient Flow Diagram | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `patient-path-diagram` | 患者路径图 | Patient Path Diagram | 无 | 流程、迁移与流量图 | 按需实现 |
| `pca-biplot` | PCA双标图 | PCA Biplot | PCA图；主成分双标图；principal component analysis plot | 高维与多变量数据图、医学、公共卫生与生命科学常用图 | 生产模板 |
| `pca-loading-plot` | PCA载荷图 | PCA Loading Plot | 无 | 分类、预测与机器学习评估图、高维与多变量数据图 | 按需实现 |
| `pca-score-plot` | PCA得分图 | PCA Score Plot | 无 | 分类、预测与机器学习评估图、高维与多变量数据图 | 按需实现 |
| `percent-stacked-area-chart` | 百分比堆积面积图 | 100% Stacked Area Chart | 无 | 时间趋势与动态变化图、构成、比例与整体—部分关系图 | 可复用模式 |
| `percent-stacked-bar-chart` | 百分比堆叠柱状图 | 100% Stacked Bar Chart | 百分比堆积柱状图 | 数值比较与排序图、构成、比例与整体—部分关系图 | 可复用模式 |
| `permutation-importance-plot` | 置换重要性图 | Permutation Importance Plot | 排列重要性图；Permutation Importance | 分类、预测与机器学习评估图 | 可复用模式 |
| `petal-plot` | 花瓣图 | Petal Plot | 无 | 集合、重叠与分类组合图 | 可复用模式 |
| `pharmacokinetic-curve` | 药代动力学曲线 | Pharmacokinetic Curve | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `phase-diagram` | 相图 | Phase Diagram | 无 | 三维、曲面与科学计算图 | 按需实现 |
| `phase-space-plot` | 相空间图 | Phase-space Plot | 无 | 三维、曲面与科学计算图 | 按需实现 |
| `phylogenetic-tree` | 系统发育树 | Phylogenetic Tree | 系谱图 | 层级与分类结构图、网络与关系结构图、医学、公共卫生与生命科学常用图 | 按需实现 |
| `pictogram-chart` | 图标阵列图 | Pictogram Chart | 无 | 数值比较与排序图 | 可复用模式 |
| `pictogram-proportion-plot` | 图标比例图 | Pictogram Proportion Plot | 无 | 构成、比例与整体—部分关系图 | 可复用模式 |
| `pie-chart` | 饼图 | Pie Chart | 无 | 构成、比例与整体—部分关系图 | 可复用模式 |
| `pixel-oriented-visualization` | Pixel-oriented Visualization | Pixel-oriented Visualization | 无 | 高维与多变量数据图 | 按需实现 |
| `placebo-test-plot` | 安慰剂检验图 | Placebo Test Plot | 无 | 实验设计与组间差异图 | 可复用模式 |
| `poincar-section-plot` | 庞加莱截面图 | Poincaré Section Plot | 无 | 三维、曲面与科学计算图 | 按需实现 |
| `polar-area-chart` | 极坐标面积图 | Polar Area Chart | 无 | 构成、比例与整体—部分关系图 | 可复用模式 |
| `polar-bar-chart` | 极坐标柱状图 | Polar Bar Chart | 无 | 数值比较与排序图 | 可复用模式 |
| `polar-coordinate-plot` | 极坐标图 | Polar Coordinate Plot | 无 | 三维、曲面与科学计算图 | 按需实现 |
| `population-pyramid` | 人口金字塔 | Population Pyramid | 人口分布金字塔图；人口金字塔图 | 数值比较与排序图、数据分布图、构成、比例与整体—部分关系图、空间与地理数据图 | 可复用模式 |
| `posterior-distribution-plot` | 后验分布图 | Posterior Distribution Plot | 无 | 统计估计、效应量与不确定性图 | 可复用模式 |
| `precision-recall-curve` | 精确率-召回率曲线 | Precision–Recall Curve | PR曲线；PR curve | 回归与统计模型诊断图、分类、预测与机器学习评估图 | 可复用模式 |
| `predicted-versus-observed-plot` | 预测值—实际值图 | Predicted versus Observed Plot | 无 | 回归与统计模型诊断图 | 可复用模式 |
| `prediction-interval-plot` | 预测区间图 | Prediction Interval Plot | 无 | 统计估计、效应量与不确定性图 | 可复用模式 |
| `prediction-probability-plot` | 预测概率图 | Prediction Probability Plot | 无 | 统计估计、效应量与不确定性图 | 可复用模式 |
| `pretest-posttest-paired-plot` | 前后测配对图 | Pretest–posttest Paired Plot | 无 | 教育学与心理测量常用图 | 按需实现 |
| `principal-component-score-plot` | 主成分得分图 | Principal Component Score Plot | 无 | 实验设计与组间差异图 | 可复用模式 |
| `prior-and-posterior-comparison-plot` | 先验—后验比较图 | Prior and Posterior Comparison Plot | 无 | 统计估计、效应量与不确定性图 | 可复用模式 |
| `prisma-flow-diagram` | PRISMA流程图 | PRISMA Flow Diagram | 无 | 流程、迁移与流量图、医学、公共卫生与生命科学常用图、文献计量与科学知识图谱、研究流程与论文规范图 | 按需实现 |
| `probability-calibration-band-plot` | 概率校准带图 | Probability Calibration Band Plot | 无 | 统计估计、效应量与不确定性图 | 可复用模式 |
| `probability-probability-plot` | P-P图 | Probability–Probability Plot | 无 | 数据分布图 | 可复用模式 |
| `problem-tree` | 问题树 | Problem Tree | 无 | 因果机制与理论模型图 | 按需实现 |
| `process-capability-histogram` | 过程能力直方图 | Process Capability Histogram | 无 | 工程、质量管理与过程控制图 | 按需实现 |
| `process-flow-diagram` | 流程图 | Process Flow Diagram | Flowchart | 流程、迁移与流量图、工程、质量管理与过程控制图 | 按需实现 |
| `process-map` | 过程图 | Process Map | 无 | 流程、迁移与流量图 | 按需实现 |
| `profile-likelihood-plot` | 轮廓似然图 | Profile Likelihood Plot | 无 | 统计估计、效应量与不确定性图 | 可复用模式 |
| `propensity-score-distribution-plot` | 倾向得分分布图 | Propensity Score Distribution Plot | 无 | 实验设计与组间差异图 | 可复用模式 |
| `propensity-score-overlap-plot` | 倾向得分重叠图 | Propensity Score Overlap Plot | 无 | 实验设计与组间差异图 | 可复用模式 |
| `proportional-symbol-map` | 比例符号地图 | Proportional Symbol Map | 气泡地图；Bubble Map；geographic bubble map | 空间与地理数据图 | 生产模板 |
| `pseudotime-heatmap` | 拟时间热图 | Pseudotime Heatmap | 无 | 高维与多变量数据图、医学、公共卫生与生命科学常用图 | 按需实现 |
| `q-matrix-heatmap` | Q矩阵热力图 | Q-matrix Heatmap | 无 | 教育学与心理测量常用图 | 按需实现 |
| `qq-plot` | Q-Q图 | Q-Q Plot | 正态概率图；Normal Probability Plot；Quantile–Quantile Plot；quantile-quantile plot | 数据分布图、回归与统计模型诊断图 | 可复用模式 |
| `quadrant-chart` | 四象限图 | Quadrant Chart | 无 | 变量关系与相关性图 | 可复用模式 |
| `qualitative-coding-tree` | 质性编码树 | Qualitative Coding Tree | 无 | 质性研究与文本分析图 | 按需实现 |
| `quality-control-overview` | 质量控制总览 | Quality-control Overview | 无 | 工程、质量管理与过程控制图、复合图与高级科研图形 | 按需实现 |
| `quantile-plot` | 分位数图 | Quantile Plot | 无 | 数据分布图 | 可复用模式 |
| `quaternary-plot` | 四元图 | Quaternary Plot | 无 | 高维与多变量数据图 | 按需实现 |
| `quiver-plot` | 箭矢图 | Quiver Plot | 无 | 三维、曲面与科学计算图 | 按需实现 |
| `r-control-chart` | R控制图 | R Control Chart | 无 | 工程、质量管理与过程控制图 | 按需实现 |
| `radar-ability-profile` | 雷达能力画像图 | Radar Ability Profile | 无 | 教育学与心理测量常用图 | 按需实现 |
| `radar-chart` | 雷达图 | Radar Chart | 雷达图／蜘蛛图；Spider Chart；spider chart | 数值比较与排序图、构成、比例与整体—部分关系图、高维与多变量数据图 | 生产模板 |
| `radial-tree` | 径向树图 | Radial Tree | 无 | 层级与分类结构图 | 按需实现 |
| `radviz-plot` | RadViz图 | RadViz Plot | 无 | 高维与多变量数据图 | 按需实现 |
| `raincloud-plot` | 雨云图 | Raincloud Plot | 无 | 数据分布图、复合图与高级科研图形 | 可复用模式 |
| `random-forest-tree-structure-diagram` | 随机森林树结构图 | Random Forest Tree Structure Diagram | 无 | 分类、预测与机器学习评估图 | 按需实现 |
| `randomization-test-distribution-plot` | 随机化检验分布图 | Randomization Test Distribution Plot | 无 | 实验设计与组间差异图 | 可复用模式 |
| `rasch-item-map` | Rasch项目地图 | Rasch Item Map | 无 | 教育学与心理测量常用图 | 按需实现 |
| `raster-map` | 栅格地图 | Raster Map | 无 | 空间与地理数据图 | 按需实现 |
| `rda-triplot` | RDA三标图 | RDA Triplot | redundancy analysis plot | 高维与多变量数据图 | 可复用模式 |
| `regression-coefficient-forest-plot` | 回归系数森林图 | Regression Coefficient Forest Plot | 无 | 统计估计、效应量与不确定性图 | 可复用模式 |
| `regression-coefficient-plot` | 回归系数图 | Regression Coefficient Plot | 无 | 回归与统计模型诊断图 | 可复用模式 |
| `regression-discontinuity-plot` | 回归不连续图 | Regression Discontinuity Plot | RDD plot | 实验设计与组间差异图 | 可复用模式 |
| `regularization-path` | 正则化路径图 | Regularization Path | 无 | 回归与统计模型诊断图 | 可复用模式 |
| `reliability-coefficient-plot` | 信度系数图 | Reliability Coefficient Plot | 无 | 教育学与心理测量常用图 | 按需实现 |
| `reliability-curve` | 可靠性曲线 | Reliability Curve | 无 | 工程、质量管理与过程控制图 | 按需实现 |
| `remote-sensing-false-color-image` | 遥感假彩色图 | Remote-sensing False-color Image | 无 | 空间与地理数据图 | 按需实现 |
| `repeated-measures-trajectory-plot` | 重复测量轨迹图 | Repeated-measures Trajectory Plot | 无 | 实验设计与组间差异图 | 可复用模式 |
| `research-dashboard-figure` | 仪表板式科研图 | Research Dashboard Figure | 无 | 复合图与高级科研图形 | 按需实现 |
| `research-design-flow-diagram` | 研究设计流程图 | Research Design Flow Diagram | 无 | 研究流程与论文规范图 | 按需实现 |
| `research-framework-diagram` | 研究框架图 | Research Framework Diagram | 无 | 研究流程与论文规范图 | 按需实现 |
| `research-front-evolution-plot` | 研究前沿演化图 | Research Front Evolution Plot | 无 | 文献计量与科学知识图谱 | 按需实现 |
| `research-hypothesis-relationship-plot` | 研究假设关系图 | Research Hypothesis Relationship Plot | 无 | 因果机制与理论模型图 | 按需实现 |
| `research-question-mapping-diagram` | 研究问题映射图 | Research Question Mapping Diagram | 无 | 研究流程与论文规范图 | 按需实现 |
| `research-stage-gantt-chart` | 研究阶段甘特图 | Research-stage Gantt Chart | 无 | 研究流程与论文规范图 | 按需实现 |
| `research-technical-roadmap` | 研究技术路线图 | Research Technical Roadmap | 无 | 研究流程与论文规范图 | 按需实现 |
| `residual-diagnostic-plot` | 残差诊断图 | Residual Diagnostic Plot | 无 | 回归与统计模型诊断图 | 可复用模式 |
| `residual-q-q-plot` | 残差Q-Q图 | Residual Q-Q Plot | 无 | 回归与统计模型诊断图 | 可复用模式 |
| `residuals-vs-fitted` | 拟合值—残差图 | Residuals vs Fitted | 无 | 回归与统计模型诊断图 | 可复用模式 |
| `response-surface-plot` | 响应曲面图 | Response Surface Plot | 无 | 工程、质量管理与过程控制图 | 按需实现 |
| `ridgeline-plot` | 山脊图 | Ridgeline Plot | Joy Plot；ridge plot | 数据分布图 | 生产模板 |
| `risk-heatmap` | 风险热力图 | Risk Heatmap | 无 | 工程、质量管理与过程控制图 | 按需实现 |
| `risk-ratio-forest-plot` | RR值森林图 | Risk Ratio Forest Plot | 无 | 统计估计、效应量与不确定性图 | 可复用模式 |
| `risk-score-plot` | 风险评分图 | Risk Score Plot | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `roc-confidence-interval-plot` | ROC置信区间图 | ROC Confidence Interval Plot | 无 | 分类、预测与机器学习评估图 | 按需实现 |
| `roc-curve` | ROC曲线 | ROC Curve | AUROC；receiver operating characteristic | 回归与统计模型诊断图、分类、预测与机器学习评估图、医学、公共卫生与生命科学常用图 | 生产模板 |
| `roc-space-plot` | ROC空间图 | ROC Space Plot | 无 | 回归与统计模型诊断图 | 可复用模式 |
| `rug-plot` | 地毯图 | Rug Plot | 分布地毯图 | 数据分布图 | 可复用模式 |
| `rule-extraction-plot` | 规则提取图 | Rule Extraction Plot | 无 | 分类、预测与机器学习评估图 | 按需实现 |
| `run-chart` | 运行图 | Run Chart | 无 | 时间趋势与动态变化图、工程、质量管理与过程控制图 | 可复用模式 |
| `s-control-chart` | S控制图 | S Control Chart | 无 | 工程、质量管理与过程控制图 | 按需实现 |
| `sample-screening-flow-diagram` | 样本筛选流程图 | Sample Screening Flow Diagram | 无 | 研究流程与论文规范图 | 按需实现 |
| `sankey-diagram` | 桑基图 | Sankey Diagram | 无 | 流程、迁移与流量图 | 生产模板 |
| `satellite-image-overlay` | 卫星影像叠加图 | Satellite Image Overlay | 无 | 空间与地理数据图 | 按需实现 |
| `scale-location-plot` | 尺度—位置图 | Scale–Location Plot | 无 | 回归与统计模型诊断图 | 可复用模式 |
| `scatter-and-marginal-density-composite-plot` | 散点—边际密度组合图 | Scatter and Marginal Density Composite Plot | 无 | 复合图与高级科研图形 | 按需实现 |
| `scatter-plot` | 散点图 | Scatter Plot | 无 | 变量关系与相关性图、工程、质量管理与过程控制图 | 可复用模式 |
| `scatter-regression-plot` | 回归散点图 | Scatter Regression Plot | 带回归线散点图；scatter with fit | 变量关系与相关性图 | 可复用模式 |
| `scatterplot-matrix` | 散点矩阵 | Scatterplot Matrix | 成对关系图；pair plot；Pair Plot；SPLOM | 变量关系与相关性图、高维与多变量数据图 | 可复用模式 |
| `school-effect-forest-plot` | 学校效应森林图 | School Effect Forest Plot | 无 | 教育学与心理测量常用图 | 按需实现 |
| `scree-plot` | 碎石图 | Scree Plot | 无 | 高维与多变量数据图、教育学与心理测量常用图 | 可复用模式 |
| `seasonal-decomposition-plot` | 季节分解图 | Seasonal Decomposition Plot | 无 | 时间趋势与动态变化图 | 可复用模式 |
| `self-organizing-map` | SOM自组织映射图 | Self-organizing Map | 无 | 高维与多变量数据图 | 按需实现 |
| `sem-diagram` | 结构方程模型图 | SEM Diagram | 无 | 因果机制与理论模型图 | 按需实现 |
| `sem-path-diagram` | 结构方程路径图 | SEM Path Diagram | 结构方程模型路径图 | 实验设计与组间差异图、教育学与心理测量常用图 | 按需实现 |
| `semantic-difference-plot` | 语义差异图 | Semantic Difference Plot | 无 | 质性研究与文本分析图 | 按需实现 |
| `semantic-hierarchy-plot` | 语义层级图 | Semantic Hierarchy Plot | 无 | 层级与分类结构图 | 按需实现 |
| `semantic-network` | 语义网络图 | Semantic Network | 无 | 网络与关系结构图、质性研究与文本分析图 | 按需实现 |
| `semi-donut-chart` | 半环图 | Semi-donut Chart | 无 | 构成、比例与整体—部分关系图 | 可复用模式 |
| `sentiment-polarity-distribution-plot` | 情感极性分布图 | Sentiment Polarity Distribution Plot | 无 | 质性研究与文本分析图 | 按需实现 |
| `sentiment-radar-chart` | 情感雷达图 | Sentiment Radar Chart | 无 | 质性研究与文本分析图 | 按需实现 |
| `sentiment-trend-plot` | 情感趋势图 | Sentiment Trend Plot | 无 | 质性研究与文本分析图 | 按需实现 |
| `set-matrix` | 集合成员矩阵 | Set Membership Matrix | 集合矩阵图 | 集合、重叠与分类组合图 | 可复用模式 |
| `set-sankey-diagram` | 集合桑基图 | Set Sankey Diagram | 无 | 集合、重叠与分类组合图 | 可复用模式 |
| `shap-beeswarm` | SHAP蜂群图 | SHAP Beeswarm | 无 | 分类、预测与机器学习评估图 | 按需实现 |
| `shap-dependence-plot` | SHAP依赖图 | SHAP Dependence Plot | 无 | 分类、预测与机器学习评估图 | 按需实现 |
| `shap-summary-plot` | SHAP摘要图 | SHAP Summary Plot | 无 | 分类、预测与机器学习评估图 | 按需实现 |
| `shap-waterfall-plot` | SHAP瀑布图 | SHAP Waterfall Plot | 无 | 分类、预测与机器学习评估图 | 按需实现 |
| `silhouette-plot` | 聚类轮廓图 | Silhouette Plot | 无 | 分类、预测与机器学习评估图 | 按需实现 |
| `simple-effects-plot` | 简单效应图 | Simple Effects Plot | 无 | 实验设计与组间差异图 | 可复用模式 |
| `single-cell-trajectory` | 单细胞轨迹图 | Single-cell Trajectory | pseudotime plot | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `single-cell-umap` | 单细胞UMAP图 | Single-cell UMAP | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `slice-plot` | 切片图 | Slice Plot | 无 | 三维、曲面与科学计算图 | 按需实现 |
| `slope-chart` | 坡度图 | Slope Chart | 无 | 数值比较与排序图、时间趋势与动态变化图 | 可复用模式 |
| `small-multiple-maps` | 小倍数地图 | Small-multiple Maps | 无 | 空间与地理数据图 | 按需实现 |
| `small-multiples` | 小多图 | Small Multiples | 小倍数图；faceted plot | 复合图与高级科研图形 | 可复用模式 |
| `smith-chart` | Smith圆图 | Smith Chart | 无 | 三维、曲面与科学计算图 | 按需实现 |
| `social-network-graph` | 社会网络图 | Social Network Graph | 无 | 网络与关系结构图 | 按需实现 |
| `spaghetti-plot` | 个体纵向轨迹图 | Spaghetti Plot | 意大利面图；longitudinal trajectory plot | 时间趋势与动态变化图 | 按需实现 |
| `sparkline` | 火花线 | Sparkline | 无 | 时间趋势与动态变化图 | 可复用模式 |
| `sparse-matrix-plot` | 稀疏矩阵图 | Sparse Matrix Plot | 无 | 高维与多变量数据图 | 可复用模式 |
| `spatial-autocorrelation-plot` | 空间自相关图 | Spatial Autocorrelation Plot | 无 | 空间与地理数据图 | 按需实现 |
| `spatial-clustering-map` | 空间聚类地图 | Spatial Clustering Map | 无 | 空间与地理数据图 | 按需实现 |
| `spatial-heatmap` | 空间热图 | Spatial Heatmap | 热力地图 | 空间与地理数据图 | 按需实现 |
| `spatial-regression-coefficient-map` | 空间回归系数地图 | Spatial Regression Coefficient Map | 无 | 空间与地理数据图 | 按需实现 |
| `spatial-residual-plot` | 空间残差图 | Spatial Residual Plot | 无 | 空间与地理数据图 | 按需实现 |
| `spatial-transcriptomics-overlay` | 空间转录组叠加图 | Spatial Transcriptomics Overlay | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `spatiotemporal-trajectory-plot` | 时空轨迹图 | Spatiotemporal Trajectory Plot | 无 | 空间与地理数据图 | 按需实现 |
| `spherical-coordinate-plot` | 球坐标图 | Spherical Coordinate Plot | 无 | 三维、曲面与科学计算图 | 按需实现 |
| `stacked-area-chart` | 堆叠面积图 | Stacked Area Chart | 堆积面积图 | 时间趋势与动态变化图、构成、比例与整体—部分关系图 | 生产模板 |
| `stacked-bar-chart` | 堆叠柱状图 | Stacked Bar Chart | 堆积柱状图 | 数值比较与排序图、构成、比例与整体—部分关系图 | 可复用模式 |
| `stacked-bar-scatter` | 堆叠柱状散点图 | Stacked Bar Scatter | 无 | 构成、比例与整体—部分关系图 | 生产模板 |
| `standardized-residual-plot` | 标准化残差图 | Standardized Residual Plot | 无 | 回归与统计模型诊断图 | 可复用模式 |
| `star-plot` | 星形图 | Star Plot | 无 | 高维与多变量数据图 | 按需实现 |
| `state-transition-diagram` | 状态转移图 | State Transition Diagram | 无 | 流程、迁移与流量图 | 按需实现 |
| `state-transition-matrix-heatmap` | 状态迁移矩阵热力图 | State Transition Matrix Heatmap | 无 | 流程、迁移与流量图 | 按需实现 |
| `statistical-significance-interval-plot` | 统计显著性区间图 | Statistical Significance Interval Plot | 无 | 统计估计、效应量与不确定性图 | 可复用模式 |
| `stem-and-leaf-plot` | 茎叶图 | Stem-and-Leaf Plot | 无 | 数据分布图 | 可复用模式 |
| `step-chart` | 阶梯图 | Step Chart | 无 | 时间趋势与动态变化图 | 可复用模式 |
| `strategic-diagram` | 战略坐标图 | Strategic Diagram | 主题图；Thematic Map | 文献计量与科学知识图谱 | 按需实现 |
| `streamgraph` | 流图 | Streamgraph | 无 | 时间趋势与动态变化图、构成、比例与整体—部分关系图 | 可复用模式 |
| `streamline-plot` | 流线图 | Streamline Plot | 无 | 三维、曲面与科学计算图 | 按需实现 |
| `stress-contour-plot` | 应力云图 | Stress Contour Plot | 无 | 三维、曲面与科学计算图 | 按需实现 |
| `strip-plot` | 条带图 | Strip Plot | 无 | 数据分布图 | 可复用模式 |
| `strobe-study-flow-diagram` | STROBE研究流程图 | STROBE Study Flow Diagram | 无 | 研究流程与论文规范图 | 按需实现 |
| `sunburst-chart` | 旭日图 | Sunburst Chart | 无 | 构成、比例与整体—部分关系图、层级与分类结构图、流程、迁移与流量图 | 可复用模式 |
| `swimlane-diagram` | 泳道图 | Swimlane Diagram | 无 | 流程、迁移与流量图 | 按需实现 |
| `swimmer-plot` | 游泳图 | Swimmer Plot | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `synthetic-control-plot` | 合成控制图 | Synthetic Control Plot | 无 | 实验设计与组间差异图 | 按需实现 |
| `system-architecture-plot` | 系统架构图 | System Architecture Plot | 无 | 研究流程与论文规范图 | 按需实现 |
| `system-dynamics-stock-and-flow-diagram` | 系统动力学库存—流量图 | System Dynamics Stock and Flow Diagram | 无 | 因果机制与理论模型图 | 按需实现 |
| `table-heatmap` | 表格热力图 | Table Heatmap | 无 | 数值比较与排序图 | 可复用模式 |
| `teacher-student-relationship-network` | 教师—学生关系网络图 | Teacher–student Relationship Network | 无 | 教育学与心理测量常用图 | 按需实现 |
| `temporal-network-evolution-plot` | 网络时间演化图 | Temporal Network Evolution Plot | 无 | 网络与关系结构图 | 按需实现 |
| `ternary-plot` | 三元图 | Ternary Plot | 无 | 构成、比例与整体—部分关系图、高维与多变量数据图 | 可复用模式 |
| `terrain-plot` | 地形图 | Terrain Plot | 无 | 空间与地理数据图 | 按需实现 |
| `test-feature-curve` | 测验特征曲线 | Test Feature Curve | 无 | 教育学与心理测量常用图 | 按需实现 |
| `test-information-curve` | 测验信息曲线 | Test Information Curve | 无 | 教育学与心理测量常用图 | 按需实现 |
| `text-clustering-plot` | 文本聚类图 | Text Clustering Plot | 无 | 质性研究与文本分析图 | 按需实现 |
| `text-flow` | 文本流图 | Text Flow | 无 | 质性研究与文本分析图 | 按需实现 |
| `text-similarity-heatmap` | 文本相似度热力图 | Text Similarity Heatmap | 无 | 质性研究与文本分析图 | 按需实现 |
| `theme-bubble-plot` | 主题气泡图 | Theme Bubble Plot | 无 | 质性研究与文本分析图、文献计量与科学知识图谱 | 按需实现 |
| `theme-density-and-centrality-plot` | 主题密度—中心度图 | Theme Density and Centrality Plot | 无 | 文献计量与科学知识图谱 | 按需实现 |
| `theme-evolution-network` | 主题演化网络图 | Theme Evolution Network | 无 | 网络与关系结构图 | 按需实现 |
| `theme-evolution-plot` | 主题演化图 | Theme Evolution Plot | 无 | 质性研究与文本分析图、文献计量与科学知识图谱 | 按需实现 |
| `theme-hierarchy-plot` | 主题层级图 | Theme Hierarchy Plot | 无 | 层级与分类结构图 | 按需实现 |
| `theme-matrix` | 主题矩阵 | Theme Matrix | 无 | 质性研究与文本分析图 | 按需实现 |
| `theme-model-plot` | 主题模型图 | Theme Model Plot | 无 | 质性研究与文本分析图 | 按需实现 |
| `theme-river` | 主题河流图 | Theme River | 无 | 质性研究与文本分析图、文献计量与科学知识图谱 | 按需实现 |
| `theme-sankey-diagram` | 主题桑基图 | Theme Sankey Diagram | 无 | 质性研究与文本分析图 | 按需实现 |
| `theoretical-analysis-framework` | 理论分析框架图 | Theoretical Analysis Framework | 无 | 研究流程与论文规范图 | 按需实现 |
| `theoretical-model-plot` | 理论模型图 | Theoretical Model Plot | 无 | 因果机制与理论模型图 | 按需实现 |
| `theory-of-change-diagram` | Theory of Change图 | Theory of Change Diagram | 无 | 因果机制与理论模型图 | 按需实现 |
| `thiessen-polygon-map` | 泰森多边形图 | Thiessen Polygon Map | 无 | 空间与地理数据图 | 按需实现 |
| `three-dimensional-bar-chart` | 三维柱状图 | Three-dimensional Bar Chart | 无 | 三维、曲面与科学计算图 | 按需实现 |
| `three-dimensional-contour-plot` | 三维等高线图 | Three-dimensional Contour Plot | 无 | 三维、曲面与科学计算图 | 按需实现 |
| `three-dimensional-heatmap` | 三维热图 | Three-dimensional Heatmap | 3D heatmap | 高维与多变量数据图、复合图与高级科研图形 | 生产模板 |
| `three-dimensional-scatter-plot` | 三维散点图 | 3D Scatter Plot | 无 | 变量关系与相关性图、三维、曲面与科学计算图 | 可复用模式 |
| `three-dimensional-surface` | 三维表面图 | Three-dimensional Surface | 三维曲面图；曲面图；3D surface；Surface Plot | 变量关系与相关性图、三维、曲面与科学计算图、复合图与高级科研图形 | 按需实现 |
| `three-dimensional-terrain-plot` | 三维地形图 | Three-dimensional Terrain Plot | 无 | 空间与地理数据图 | 按需实现 |
| `three-dimensional-vector-field` | 三维矢量场 | Three-dimensional Vector Field | 三维矢量场图；3D vector field | 三维、曲面与科学计算图、复合图与高级科研图形 | 按需实现 |
| `three-fields-plot` | 三字段图 | Three-fields Plot | 无 | 文献计量与科学知识图谱 | 按需实现 |
| `time-band-chart` | 时间带状图 | Time Band Chart | 无 | 时间趋势与动态变化图 | 可复用模式 |
| `time-series-heatmap` | 时间序列热力图 | Time-series Heatmap | 无 | 时间趋势与动态变化图 | 可复用模式 |
| `time-slice-network` | 时间切片网络图 | Time-slice Network | 无 | 文献计量与科学知识图谱 | 按需实现 |
| `time-slider-map` | 时间滑块地图 | Time-slider Map | 无 | 空间与地理数据图 | 按需实现 |
| `timeline` | 时间线 | Timeline | 时间轴图 | 时间趋势与动态变化图、流程、迁移与流量图 | 可复用模式 |
| `topic-transition-plot` | 话题迁移图 | Topic Transition Plot | 无 | 质性研究与文本分析图 | 按需实现 |
| `trace-plot` | 参数轨迹图 | Trace Plot | 无 | 统计估计、效应量与不确定性图 | 可复用模式 |
| `trajectory-map` | 路径轨迹地图 | Trajectory Map | 无 | 空间与地理数据图 | 按需实现 |
| `trajectory-plot` | 轨迹图 | Trajectory Plot | 无 | 时间趋势与动态变化图 | 可复用模式 |
| `transition-flow-plot` | 迁移流向图 | Transition Flow Plot | 无 | 流程、迁移与流量图 | 按需实现 |
| `transition-probability-plot` | 转移概率图 | Transition Probability Plot | 无 | 流程、迁移与流量图 | 按需实现 |
| `transmission-network` | 传播网络图 | Transmission Network | 无 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `treemap` | 矩形式树图 | Treemap | 矩形树图 | 构成、比例与整体—部分关系图、层级与分类结构图、流程、迁移与流量图 | 可复用模式 |
| `trivariate-map` | 三变量地图 | Trivariate Map | 无 | 空间与地理数据图 | 按需实现 |
| `tsne-plot` | t-SNE图 | t-SNE Plot | tSNE | 分类、预测与机器学习评估图、高维与多变量数据图、医学、公共卫生与生命科学常用图 | 按需实现 |
| `tumor-burden-spider-plot` | 肿瘤负荷蜘蛛图 | Tumor Burden Spider Plot | 蜘蛛图 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `tumor-response-waterfall-plot` | 肿瘤疗效瀑布图 | Tumor Response Waterfall Plot | 瀑布图 | 医学、公共卫生与生命科学常用图 | 按需实现 |
| `two-by-two-table-plot` | 四格表图 | Two-by-two Table Plot | 无 | 集合、重叠与分类组合图 | 可复用模式 |
| `two-dimensional-histogram` | 二维直方图 | Two-dimensional Histogram | 双变量直方图；2D histogram；Bivariate Histogram | 数据分布图、变量关系与相关性图、高维与多变量数据图 | 可复用模式 |
| `two-dimensional-kernel-density-plot` | 二维核密度图 | Two-dimensional Kernel Density Plot | 无 | 变量关系与相关性图 | 可复用模式 |
| `u-control-chart` | U控制图 | U Control Chart | 无 | 工程、质量管理与过程控制图 | 按需实现 |
| `umap-plot` | UMAP图 | UMAP Plot | UMAP | 分类、预测与机器学习评估图、高维与多变量数据图、医学、公共卫生与生命科学常用图 | 按需实现 |
| `unit-chart` | 单位图 | Unit Chart | 无 | 构成、比例与整体—部分关系图 | 可复用模式 |
| `upset-plot` | UpSet图 | UpSet Plot | 无 | 医学、公共卫生与生命科学常用图、集合、重叠与分类组合图 | 可复用模式 |
| `user-journey-flow` | 用户路径图 | User Journey Flow | 无 | 流程、迁移与流量图 | 按需实现 |
| `validation-curve` | 验证曲线 | Validation Curve | 无 | 回归与统计模型诊断图、分类、预测与机器学习评估图 | 可复用模式 |
| `value-stream-map` | 价值流图 | Value Stream Map | 无 | 流程、迁移与流量图 | 按需实现 |
| `variable-relationship-plot` | 变量关系图 | Variable Relationship Plot | 无 | 研究流程与论文规范图 | 按需实现 |
| `variance-inflation-factor-plot` | VIF图 | Variance Inflation Factor Plot | 无 | 回归与统计模型诊断图 | 可复用模式 |
| `venn-diagram` | 韦恩图 | Venn Diagram | Venn图 | 医学、公共卫生与生命科学常用图、集合、重叠与分类组合图 | 可复用模式 |
| `venn-network` | 韦恩网络图 | Venn Network | 无 | 集合、重叠与分类组合图 | 可复用模式 |
| `violin-box-and-scatter-composite-plot` | 小提琴—箱线—散点组合图 | Violin Box and Scatter Composite Plot | 无 | 复合图与高级科研图形 | 按需实现 |
| `violin-plot` | 小提琴图 | Violin Plot | 无 | 数据分布图 | 生产模板 |
| `volcano-plot` | 火山图 | Volcano Plot | 无 | 医学、公共卫生与生命科学常用图 | 生产模板 |
| `volume-rendering` | 体渲染 | Volume Rendering | 体渲染图 | 医学、公共卫生与生命科学常用图、三维、曲面与科学计算图、复合图与高级科研图形 | 按需实现 |
| `voronoi-hierarchy-diagram` | Voronoi层级图 | Voronoi Hierarchy Diagram | 无 | 层级与分类结构图 | 按需实现 |
| `voronoi-map` | Voronoi地图 | Voronoi Map | 无 | 空间与地理数据图 | 按需实现 |
| `voronoi-treemap` | Voronoi树图 | Voronoi Treemap | 无 | 构成、比例与整体—部分关系图 | 可复用模式 |
| `waffle-chart` | 华夫饼图 | Waffle Chart | 无 | 数值比较与排序图、构成、比例与整体—部分关系图 | 可复用模式 |
| `weibull-probability-plot` | Weibull概率图 | Weibull Probability Plot | 无 | 工程、质量管理与过程控制图 | 按需实现 |
| `wireframe-plot` | 网格曲面图 | Wireframe Plot | 无 | 三维、曲面与科学计算图 | 按需实现 |
| `word-cloud` | 词云 | Word Cloud | 无 | 质性研究与文本分析图 | 按需实现 |
| `word-frequency-bar-chart` | 词频条形图 | Word-frequency Bar Chart | 无 | 质性研究与文本分析图 | 按需实现 |
| `wright-map` | Wright图 | Wright Map | 项目—人对应图；person-item map | 教育学与心理测量常用图 | 按需实现 |
| `x-bar-control-chart` | X-bar控制图 | X-bar Control Chart | 无 | 工程、质量管理与过程控制图 | 按需实现 |
| `year-on-year-and-period-on-period-change-plot` | 同比／环比变化图 | Year-on-year and Period-on-period Change Plot | 无 | 时间趋势与动态变化图 | 可复用模式 |
| `xps-peak-deconvolution-plot` | XPS 峰拟合分峰图 | XPS Peak Deconvolution Plot | XPS 分峰图；XPS 峰拟合图；XPS 高分辨谱；XPS peak fitting；XPS component fit；high-resolution XPS spectrum | 工程、质量管理与过程控制图 | 生产模板 |
| `xanes-spectrum` | XANES 吸收近边谱 | XANES Spectrum | X 射线吸收近边结构谱；吸收边谱；X-ray absorption near-edge spectrum；XANES edge plot | 工程、质量管理与过程控制图 | 可复用模式 |
| `exafs-fourier-transform-spectrum` | EXAFS 傅里叶变换谱 | EXAFS Fourier-transform Spectrum | EXAFS R 空间谱；傅里叶变换 EXAFS；FT-EXAFS；EXAFS R-space magnitude | 工程、质量管理与过程控制图 | 可复用模式 |
| `exafs-r-space-fitting-plot` | EXAFS R 空间拟合图 | EXAFS R-space Fitting Plot | EXAFS 拟合图；R 空间拟合；EXAFS fit；R-space EXAFS fit | 工程、质量管理与过程控制图 | 可复用模式 |
| `exafs-wavelet-transform-map` | EXAFS 小波变换图 | EXAFS Wavelet-transform Map | WT-EXAFS 图；EXAFS 小波等高图；EXAFS 小波三维图；WT-EXAFS；EXAFS wavelet map；EXAFS wavelet surface | 三维、曲面与科学计算图、工程、质量管理与过程控制图 | 生产模板 |
| `cyclic-voltammetry-curve` | 循环伏安曲线 | Cyclic Voltammetry Curve | CV 曲线；循环伏安图；CV curve；cyclic voltammogram | 时间趋势与动态变化图、工程、质量管理与过程控制图 | 可复用模式 |
| `galvanostatic-charge-discharge-curve` | 恒流充放电曲线 | Galvanostatic Charge-discharge Curve | GCD 曲线；充放电曲线；GCD profile；galvanostatic profile | 时间趋势与动态变化图、工程、质量管理与过程控制图 | 可复用模式 |
| `battery-rate-capability-plot` | 电池倍率性能图 | Battery Rate Capability Plot | 倍率性能图；倍率测试图；rate performance plot；rate capability test | 时间趋势与动态变化图、工程、质量管理与过程控制图 | 可复用模式 |
| `battery-cycling-stability-plot` | 电池循环稳定性图 | Battery Cycling Stability Plot | 长循环性能图；循环寿命图；long-term cycling plot；cycling performance plot | 时间趋势与动态变化图、工程、质量管理与过程控制图 | 可复用模式 |
| `electrochemical-kinetics-contour-map` | 电化学动力学等高图 | Electrochemical Kinetics Contour Map | 峰电位扫描速率等高图；电化学动力学热图；electrochemical kinetics heatmap；potential scan-rate contour | 高维与多变量数据图、工程、质量管理与过程控制图 | 可复用模式 |
| `peak-current-scan-rate-log-log-plot` | 峰电流-扫描速率双对数图 | Peak-current Scan-rate Log-log Plot | b 值拟合图；log i-log v 图；b-value plot；log peak current vs log scan rate | 变量关系与相关性图、工程、质量管理与过程控制图 | 可复用模式 |
| `capacitive-diffusion-contribution-plot` | 电容-扩散贡献图 | Capacitive-diffusion Contribution Plot | 电容贡献堆积图；扩散控制贡献图；capacitive contribution plot；diffusion-controlled contribution plot | 构成、比例与整体—部分关系图、工程、质量管理与过程控制图 | 可复用模式 |
| `ion-diffusion-coefficient-profile` | 离子扩散系数状态曲线 | Ion Diffusion-coefficient Profile | 扩散系数-反应状态图；GITT 扩散系数曲线；diffusion coefficient vs state；GITT diffusion profile | 时间趋势与动态变化图、工程、质量管理与过程控制图 | 可复用模式 |
