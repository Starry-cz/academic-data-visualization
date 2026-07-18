<p align="center">
  <img src="assets/readme/academic-data-visualization-workflow-v5.png" width="100%" alt="Academic Data Visualization：从研究问题、数据质检、图形设计到投稿级图表交付的完整工作流与图鉴">
</p>

<div align="center">

# Academic Data Visualization

**面向科研数据的投稿级可视化 Skill：从研究问题到可复现、可审阅的学术图表。**

让 AI 编程助手先理解你要证明什么，再选择图型、组织多面板证据、统一视觉语言，并交付可编辑的投稿文件。

[![Stars](https://img.shields.io/github/stars/Starry-cz/academic-data-visualization?style=flat-square&color=E69F00&label=stars)](https://github.com/Starry-cz/academic-data-visualization/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/Starry-cz/academic-data-visualization?style=flat-square&color=0072B2)](https://github.com/Starry-cz/academic-data-visualization/commits/main)
[![License](https://img.shields.io/github/license/Starry-cz/academic-data-visualization?style=flat-square&color=009E73)](LICENSE)
[![Python](https://img.shields.io/badge/Python-matplotlib%20%7C%20seaborn-0072B2?style=flat-square)](https://matplotlib.org/)
[![R](https://img.shields.io/badge/R-ggplot2%20%7C%20ComplexHeatmap-CC79A7?style=flat-square)](https://ggplot2.tidyverse.org/)

[快速开始](#快速开始) · [直接这样说](#直接这样说) · [全部图表](#全部图表导航) · [安装与更新](#安装与更新) · [质量保证](#质量保证) · [English](README_EN.md)

</div>

<p align="center">
  <strong>研究问题 · 数据结构 · 图型选择 · 多面板叙事 · 质量检验 · 投稿级交付</strong>
</p>

> 图中示例只展示视觉语言和信息层级；实际成图始终依据你的研究问题、真实数据和目标期刊规范重建。

## 快速开始

```bash
git clone https://github.com/Starry-cz/academic-data-visualization.git
```

将**完整目录**放入所用 Agent 的 skills 目录；不要只复制 `SKILL.md`。`references/`、`scripts/` 和 `assets/` 共同提供图型规则、QA 与可复用生产资产。

然后自然描述任务即可。这个 Skill 不把数据直接套进模板：它会先确认研究问题、数据结构和目标期刊，再提出图表方案。

## 直接这样说

安装后，将数据、已有图或研究目标交给 Agent。下面的提示词可以直接复制并按需替换。

| 你的场景 | 可以直接这样说 |
|---|---|
| 不确定应该画什么图 | `请使用 academic-data-visualization 分析 experiment.csv。我想比较三组干预在四个时间点的差异与不确定性，目标是双栏期刊图。先给出图表方案和理由，再生成。` |
| 把结果组织成一张多面板主图 | `请使用 academic-data-visualization，把这些结果组织为一张投稿主图。请明确每个面板回答的问题、英雄面板与支持面板的证据关系。` |
| 重绘或提升旧图 | `请使用 academic-data-visualization 参考 old_figure.png 和 source_data.csv，重建为低饱和、可编辑的投稿级图表；保留数据含义，不要把截图直接美化。` |
| 为目标期刊适配规格 | `请使用 academic-data-visualization，按 Nature 双栏图的尺寸、字体、导出规范审查并重做 figure.py。` |
| 出图前做检查 | `请使用 academic-data-visualization 审查这个图表脚本的统计表达、色盲可读性、文字裁切、面板对齐和矢量导出风险。` |

如果你只给了数据、尚未说明要回答的科学问题，Skill 会先追问，而不是生成一组无针对性的默认图。

## 能力与图型

| 任务 | Skill 如何处理 | 交付结果 |
|---|---|---|
| 不知道该选什么图 | 从研究问题、变量类型、样本量、分布和分组结构论证图型 | 有理由的单图或多面板方案 |
| 图表看起来像软件默认值 | 统一字体、语义配色、留白、线宽与标注层级 | 投稿级视觉一致性 |
| 多项证据需要放在同一图中 | 识别英雄面板，安排支持面板，保持跨面板颜色语义 | 清晰的多面板叙事 |
| 重现或迭代旧图 | 优先复用同类生产脚本，并继承尺寸与比例参数 | 可追溯、可修改的代码 |
| 投稿前审查 | 检查图型选择、统计表达、输出格式、可读性与无障碍风险 | 可操作的修改清单 |

覆盖相关性矩阵、热图、散点 / PCA / RDA、柱状与误差线、箱线 / 小提琴 / 山脊图、趋势图、火山图、AUROC、森林图、Mantel、桑基、UpSet、混淆矩阵及其他长尾科研图型。完整的科研与日常工作图型选择规则见 [`references/figure-type-catalog.md`](references/figure-type-catalog.md)：它按信息任务整理比较、分布、时间、关系、组学、模型、空间、网络与业务监控图型，并明确现有模板与按需实现的边界。

## Nature-ready 图形标准

本 Skill 不复刻某一篇 Nature 论文的装饰风格，而是把 Nature 官方图件要求转化为可执行默认值。

| 维度 | 默认执行 |
|---|---|
| 字体与字号 | Arial / Helvetica；最终尺寸下常规文字 5–7 pt，子图标签 8 pt 加粗小写 |
| 配色 | 色盲安全的语义色；同一概念跨面板保持一致；颜色不作为唯一识别线索 |
| 坐标与留白 | 保留必要的坐标轴、刻度与单位；默认不使用背景网格、阴影和装饰图标 |
| 交付 | RGB；文本与线稿优先可编辑 PDF / SVG；真实栅格内容提供 450 dpi PNG / TIFF |

完整执行合同见 [`references/nature-publication-style.md`](references/nature-publication-style.md)，并与 [`references/typography.md`](references/typography.md)、[`references/color-palettes.md`](references/color-palettes.md) 和 [`references/export-specs.md`](references/export-specs.md) 联动。

## 全部图表导航

目前共有 **96 种可复用图表视觉模式**。可以直接在提示词中写出下列名称；若不确定该选哪一种，描述研究问题即可，Skill 会依据数据结构与图型目录推荐方案。

<table>
  <thead>
    <tr>
      <th width="16%">图表分类</th>
      <th width="74%">可直接使用的图表类型</th>
      <th width="10%">图鉴</th>
    </tr>
  </thead>
  <tbody>
    <tr><td valign="top"><strong>比较、排序与组成</strong></td><td valign="top">分组柱状图、堆叠柱状图、水平柱状图、带原始点柱状图、显著性柱状图、配对柱状图、点图、条带散点叠加柱状图、100% 堆叠柱状图、发散柱状图、瀑布图、棒棒糖图、水平百分比堆叠柱状图、嵌套分组柱状图、误差线图、范围图</td><td valign="top"><a href="assets/chart-atlas/atlas-01-bar-charts.png">柱状与比较图鉴</a></td></tr>
    <tr><td valign="top"><strong>趋势、散点与关系</strong></td><td valign="top">散点图、回归散点图、多序列折线图、剂量反应散点图、相关性散点图、气泡图、均值 ± SEM 置信带、带边际直方图散点图、阶梯图、连接散点图、多组散点图、LOESS 曲线图、stem 图、极坐标散点图、面积图、高亮趋势图</td><td valign="top"><a href="assets/chart-atlas/atlas-02-line-scatter.png">趋势与关系图鉴</a></td></tr>
    <tr><td valign="top"><strong>热图、矩阵与模式</strong></td><td valign="top">发散热图、掩码相关性矩阵、带注释热图、分块热图、聚类热图、密度热图、分类热图、半树状图热图、上三角相关矩阵、行标准化热图、离散热图、稀疏矩阵热图、多注释热图、间隙热图、二值热图、连续梯度热图</td><td valign="top"><a href="assets/chart-atlas/atlas-03-heatmaps.png">热图与矩阵图鉴</a></td></tr>
    <tr><td valign="top"><strong>分布与统计诊断</strong></td><td valign="top">箱线图、小提琴图、箱线 + 原始点、直方图、重叠 KDE、山脊图、半小提琴图、蜂群图、Sina 图、分裂小提琴图、ECDF、QQ 图、重叠直方图、雨云图、二维直方图、rug 图</td><td valign="top"><a href="assets/chart-atlas/atlas-04-distributions.png">分布图鉴</a></td></tr>
    <tr><td valign="top"><strong>科研、模型与组学</strong></td><td valign="top">标准火山图、标注火山图、分面火山图、MA 图、四象限散点图、森林图、雷达图、UpSet 图、基因组瀑布图、Manhattan 图、Bland–Altman 图、ROC 图、PR 曲线、校准曲线、元分析漏斗图、Venn 图</td><td valign="top"><a href="assets/chart-atlas/atlas-05-volcano-special.png">科研与模型图鉴</a></td></tr>
    <tr><td valign="top"><strong>领域科研与日常工作</strong></td><td valign="top">Kaplan–Meier 生存曲线、哑铃图、坡度图、帕累托图、控制图、甘特图、阶段漏斗图、树图、日历热图、网络图、空间气泡图、dendrogram、基因组 lollipop 图、SHAP beeswarm、系数 / 点须图、三元图</td><td valign="top"><a href="assets/chart-atlas/atlas-06-domain-work.png">领域与工作图鉴</a></td></tr>
  </tbody>
</table>

> “图鉴”展示的是可复用视觉模式；带有完整脚本的生产模板、按需实现图型及其数据约束见 [`references/figure-type-catalog.md`](references/figure-type-catalog.md) 和 [`references/directory-map.md`](references/directory-map.md)。

## 图表索引

<table width="100%">
  <thead><tr><th width="14%">图表名称</th><th width="38%">预览</th><th width="23%">图形特征</th><th width="25%">典型应用场景</th></tr></thead>
  <tbody>
    <tr><td valign="top">3D 热图</td><td align="center" valign="top"><img src="assets/figure-atlas/3Dheatmap.png?theme=warm-cool-kinetics-v1" width="310"></td><td valign="top">三维柱面同时编码矩阵数值，高度与颜色双重呈现</td><td valign="top">多因子交互效应、基因型 × 环境矩阵、三维强度分布</td></tr>
    <tr><td valign="top">AUROC 曲线图</td><td align="center" valign="top"><img src="assets/figure-atlas/auroc.png?theme=warm-cool-kinetics-v1" width="310"></td><td valign="top">TPR–FPR 曲线，包含对角参考线与 AUC 标注</td><td valign="top">分类模型评估、多模型 ROC 对比、阈值敏感性分析</td></tr>
    <tr><td valign="top">柱状图</td><td align="center" valign="top"><img src="assets/figure-atlas/bar.png?theme=warm-cool-kinetics-v1" width="310"></td><td valign="top">单变量柱形高度编码，可配合误差线和原始样本点</td><td valign="top">组间均值比较、单指标排序、计数统计</td></tr>
    <tr><td valign="top">相关性密度图</td><td align="center" valign="top"><img src="assets/figure-atlas/CorrelationDensity.png?theme=warm-cool-kinetics-v1" width="310"></td><td valign="top">散点叠加二维核密度等高线与拟合关系</td><td valign="top">两变量关系强弱、密集区识别、异常点检测</td></tr>
    <tr><td valign="top">相关性矩阵图</td><td align="center" valign="top"><img src="assets/figure-atlas/Correlationmatrix.png?theme=warm-cool-kinetics-v1" width="310"></td><td valign="top">方形网格以色阶和数值呈现成对相关系数</td><td valign="top">多变量相关性总览、特征筛选前共线性检查</td></tr>
    <tr><td valign="top">密度热图</td><td align="center" valign="top"><img src="assets/figure-atlas/density_heatmap.png?theme=warm-cool-kinetics-v1" width="310"></td><td valign="top">连续二维核密度以颜色梯度铺满网格</td><td valign="top">大样本点云密度分布、替代过度重叠散点图</td></tr>
    <tr><td valign="top">频率 3D 热图</td><td align="center" valign="top"><img src="assets/figure-atlas/Frequency_3DHeatmap.png?theme=warm-cool-kinetics-v1" width="310"></td><td valign="top">立体柱面展示分箱频次，兼顾分组与数量</td><td valign="top">等位基因频率分布、双因子计数交叉展示</td></tr>
    <tr><td valign="top">分组相关性矩阵图</td><td align="center" valign="top"><img src="assets/figure-atlas/GroupCorrelationmatrix.png?theme=warm-cool-kinetics-v1" width="310"></td><td valign="top">按处理或环境拆分多个相关矩阵并列呈现</td><td valign="top">不同处理 / 环境下相关结构差异比较</td></tr>
    <tr><td valign="top">分组柱状图</td><td align="center" valign="top"><img src="assets/figure-atlas/GroupedBarChart.png?theme=warm-cool-kinetics-v1" width="310"></td><td valign="top">同一类别下并列多个子组柱形，可配误差线</td><td valign="top">多处理 × 多指标对比、重复实验组间差异</td></tr>
    <tr><td valign="top">Mantel 相关性检验图</td><td align="center" valign="top"><img src="assets/figure-atlas/MantelCorrelation.png?theme=warm-cool-kinetics-v1" width="310"></td><td valign="top">相关矩阵热图叠加连线，标注 Mantel r 与显著性</td><td valign="top">环境因子与群落 / 基因型矩阵关联、距离矩阵分析</td></tr>
    <tr><td valign="top">PCA 双标图</td><td align="center" valign="top"><img src="assets/figure-atlas/PCA.png?theme=warm-cool-kinetics-v1" width="310"></td><td valign="top">主成分散点、分组置信椭圆与变量载荷组合</td><td valign="top">样本分离、群体结构、降维与变量贡献展示</td></tr>
    <tr><td valign="top">雷达图</td><td align="center" valign="top"><img src="assets/figure-atlas/radar.png?theme=warm-cool-kinetics-v1" width="310"></td><td valign="top">多轴闭合轮廓比较多个指标的相对表现</td><td valign="top">少量对象的多指标画像、处理综合性状比较</td></tr>
    <tr><td valign="top">山脊图</td><td align="center" valign="top"><img src="assets/figure-atlas/RidgePlot.png?theme=warm-cool-kinetics-v1" width="310"></td><td valign="top">多组核密度曲线沿纵向错位堆叠</td><td valign="top">多组或多时间点的分布变化与重叠模式</td></tr>
    <tr><td valign="top">桑基图</td><td align="center" valign="top"><img src="assets/figure-atlas/sankey.png?theme=warm-cool-kinetics-v1" width="310"></td><td valign="top">带宽编码流量，连接来源、过程与去向</td><td valign="top">分类流向、物质 / 能量转移、状态转换展示</td></tr>
    <tr><td valign="top">堆叠柱状散点图</td><td align="center" valign="top"><img src="assets/figure-atlas/StackedBarScatter.png?theme=warm-cool-kinetics-v1" width="310"></td><td valign="top">堆叠组成与原始散点结合，兼顾比例和个体差异</td><td valign="top">组成结构比较、样本级观测与汇总结果联读</td></tr>
    <tr><td valign="top">趋势图</td><td align="center" valign="top"><img src="assets/figure-atlas/trend.png?theme=warm-cool-kinetics-v1" width="310"></td><td valign="top">连续折线展示时间、剂量或梯度方向的变化</td><td valign="top">时间序列、剂量反应、环境梯度趋势</td></tr>
    <tr><td valign="top">小提琴图</td><td align="center" valign="top"><img src="assets/figure-atlas/violin_chart.png?theme=warm-cool-kinetics-v1" width="310"></td><td valign="top">分布密度轮廓与中位数 / 四分位等统计摘要结合</td><td valign="top">分组分布、离散程度与异常值比较</td></tr>
  </tbody>
</table>

### 科研与工作扩展图鉴

除上表的生产图型外，Skill 新增了 16 种可复用的科研与日常工作图型视觉模式：Kaplan–Meier、生存 / 效应估计、哑铃图、坡度图、帕累托、控制图、甘特、阶段漏斗、树图、日历热图、网络、空间气泡、dendrogram、基因组 lollipop、SHAP beeswarm、三元图。实际选择与约束见 [`references/figure-type-catalog.md`](references/figure-type-catalog.md)。

<p align="center">
  <img src="assets/chart-atlas/atlas-06-domain-work.png?theme=warm-cool-kinetics-v1" width="100%" alt="科研与工作扩展图型图鉴：Kaplan-Meier、甘特图、网络图、SHAP beeswarm 等">
</p>

## 工作流与视觉系统

```text
研究问题 → 数据结构 → 图型论证 → 面板设计 → 风格注入
                     → 脚本 / 资产匹配 → 原生渲染 → QA → 投稿级交付
```

1. 明确研究问题、目标期刊与要传达的核心结论。
2. 检查变量类型、分组、样本量、分布与异常值，并提出图表方案。
3. 围绕一个结论组织英雄面板和支持面板；不以固定模板拼图。
4. 注入字体、物理尺寸、语义配色、统计标注和导出规则，优先复用生产脚本。
5. 输出 PNG 预览、SVG/PDF 矢量版与投稿级 TIFF，并完成代码和视觉 QA。

默认视觉语言采用 Nature-ready、色盲安全的 `nature-default` 主题：蓝 `#0072B2`、蓝绿色 `#009E73`、橙 `#E69F00`、紫 `#CC79A7`、朱红 `#D55E00`，并以深灰 `#1A1A1A` 承载文字与轴线。完整规范见 [`references/color-palettes.md`](references/color-palettes.md) 与 [`references/visual-style.md`](references/visual-style.md)。

## 配色主题库与个性化重绘

Skill 默认使用 `nature-default`，同时提供 14 组由科研图配色参考整理而成的可选主题。每张预览都包含柱状图、趋势图、发散矩阵和连续色带，便于比较分类色、发散色与连续色的实际效果。

<table>
  <tr>
    <td width="50%" align="center" valign="top"><strong>Nature 默认</strong><br><img src="assets/palette-gallery/nature-default.png?qa=direct-labels-v1" width="390" alt="Nature 默认配色预览"></td>
    <td width="50%" align="center" valign="top"><strong>高辨识信号</strong><br><img src="assets/palette-gallery/vivid-signal.png?qa=direct-labels-v1" width="390" alt="高辨识信号配色预览"></td>
  </tr>
  <tr>
    <td align="center" valign="top"><strong>明亮生物</strong><br><img src="assets/palette-gallery/bright-bio.png?qa=direct-labels-v1" width="390" alt="明亮生物配色预览"></td>
    <td align="center" valign="top"><strong>青绿组学</strong><br><img src="assets/palette-gallery/teal-genome.png?qa=direct-labels-v1" width="390" alt="青绿组学配色预览"></td>
  </tr>
  <tr>
    <td align="center" valign="top"><strong>柔和微生物</strong><br><img src="assets/palette-gallery/muted-microbe.png?qa=direct-labels-v1" width="390" alt="柔和微生物配色预览"></td>
    <td align="center" valign="top"><strong>免疫信号</strong><br><img src="assets/palette-gallery/immuno-signal.png?qa=direct-labels-v1" width="390" alt="免疫信号配色预览"></td>
  </tr>
  <tr>
    <td align="center" valign="top"><strong>粉彩催化</strong><br><img src="assets/palette-gallery/pastel-catalysis.png?qa=direct-labels-v1" width="390" alt="粉彩催化配色预览"></td>
    <td align="center" valign="top"><strong>电化学柔彩</strong><br><img src="assets/palette-gallery/electrochemistry.png?qa=direct-labels-v1" width="390" alt="电化学柔彩配色预览"></td>
  </tr>
  <tr>
    <td align="center" valign="top"><strong>柔和成本</strong><br><img src="assets/palette-gallery/soft-cost.png?qa=direct-labels-v1" width="390" alt="柔和成本配色预览"></td>
    <td align="center" valign="top"><strong>柔和学术</strong><br><img src="assets/palette-gallery/soft-academic.png?qa=direct-labels-v1" width="390" alt="柔和学术配色预览"></td>
  </tr>
  <tr>
    <td align="center" valign="top"><strong>柔彩组学</strong><br><img src="assets/palette-gallery/pastel-omics.png?qa=direct-labels-v1" width="390" alt="柔彩组学配色预览"></td>
    <td align="center" valign="top"><strong>暖冷动力学</strong><br><img src="assets/palette-gallery/warm-cool-kinetics.png?qa=direct-labels-v1" width="390" alt="暖冷动力学配色预览"></td>
  </tr>
  <tr>
    <td align="center" valign="top"><strong>含水层复苏</strong><br><img src="assets/palette-gallery/aquifer-recovery.png?qa=direct-labels-v1" width="390" alt="含水层复苏配色预览"></td>
    <td align="center" valign="top"><strong>神经深蓝</strong><br><img src="assets/palette-gallery/neuro-navy.png?qa=direct-labels-v1" width="390" alt="神经深蓝配色预览"></td>
  </tr>
  <tr>
    <td colspan="2" align="center" valign="top"><strong>低温电解质</strong><br><img src="assets/palette-gallery/cryo-electrolyte.png?qa=direct-labels-v1" width="390" alt="低温电解质配色预览"></td>
  </tr>
</table>

使用时可以直接说“使用 `teal-genome` 主题绘制”，也可以先看默认预览。首版预览通过质量检查后，Skill 会询问是否保留当前主题，或改用上述主题、你提供的十六进制颜色、配色图或论文图作为参考进行个性化重绘。自定义仅改变视觉配色，不改变数据、统计、图型、分组顺序或颜色语义。

图表索引当前使用 `warm-cool-kinetics`（暖冷动力学）主题；索引缩略图的中性文字、轴线与灰色信息保持不变。

## 安装与更新

### Codex

```bash
git clone https://github.com/Starry-cz/academic-data-visualization.git
mkdir -p ~/.codex/skills/academic-data-visualization
cp -r academic-data-visualization/* ~/.codex/skills/academic-data-visualization/
```

如果保留了本地 clone，后续更新只需进入仓库目录并执行：

```bash
git pull
```

### Claude Code、Cursor 与 GitHub Copilot

- **Claude Code：** 复制完整目录到 `~/.claude/skills/academic-data-visualization/`。
- **Cursor：** 将 [`install/cursor/.cursorrules`](install/cursor/.cursorrules) 复制到目标项目根目录。
- **GitHub Copilot：** 将 [`install/copilot/copilot-instructions.md`](install/copilot/copilot-instructions.md) 复制到目标项目的 `.github/` 目录。

各平台适配文件位于 [`install/`](install/)，Codex 的入口说明见 [`install/codex/instructions.md`](install/codex/instructions.md)。

## 质量保证

质量检查覆盖“能否运行”之外的科研表达风险：

- **反模式：** 默认或彩虹配色、厚重边框、遮挡数据的图例、低分辨率截图；
- **代码与导出：** 字体、栏宽、线宽、语义色、可编辑矢量文字与分辨率；
- **数据与论证：** 不当均值柱、样本丢失、相关 / 分离度表述与统计注释；
- **视觉复核：** 文字裁切、刻度重叠、子图对齐、灰度与色盲可读性。

```bash
# 核查一个生成脚本
python scripts/qa_validator.py path/to/figure.py

# 运行 QA 规则覆盖测试，并重建 README 图表预览
python scripts/qa_coverage.py
python scripts/generate_readme_previews.py
python scripts/generate_atlas.py
```

## 项目结构

```text
academic-data-visualization/
├── SKILL.md                 # Agent 入口与完整工作流
├── references/              # 图型、视觉、导出与 QA 规范
├── scripts/                 # 组合、验证、预览与图鉴生成器
├── assets/                  # 可复用生产脚本与 README 图表预览
└── install/                 # Codex / Cursor / Copilot / Claude 适配文件
```

## 贡献与许可

欢迎通过 issue 或 PR 提出期刊规范、可访问性、图型或真实研究场景的改进建议。新增模板请同时提供可复现脚本、数据假设说明和渲染预览。

本项目采用 [Apache-2.0](LICENSE) 许可。
