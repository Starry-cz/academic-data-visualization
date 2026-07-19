<p align="center">
  <img src="assets/readme/academic-data-visualization-workflow-v5.png" width="100%" alt="Academic Data Visualization：从研究问题、数据剖析和图型论证，到投稿级图表与视觉审查">
</p>

<h1 align="center">Academic Data Visualization</h1>

<p align="center">
  <strong>先判断，再绘制：把科研问题与真实数据转化为可复现、可审查、可投稿的 Python / R 图表。</strong>
</p>

<p align="center">
  <a href="#一分钟开始"><img src="https://img.shields.io/badge/Agent_Skill-Codex_%7C_Claude_%7C_Cursor-4573B4?style=flat-square" alt="Agent Skill"></a>
  <a href="references/figure-type-catalog.md"><img src="https://img.shields.io/badge/图型模式-96-73C79E?style=flat-square" alt="96 个图型模式"></a>
  <a href="#配色主题库"><img src="https://img.shields.io/badge/配色主题-20-F599A1?style=flat-square" alt="20 个配色主题"></a>
  <a href="#可复现的质量证据"><img src="https://img.shields.io/badge/QA-四轮闭环-95AEDA?style=flat-square" alt="四轮 QA 闭环"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache--2.0-7A939F?style=flat-square" alt="Apache-2.0 License"></a>
</p>

<p align="center">
  <a href="#一分钟开始">一分钟开始</a> ·
  <a href="#它解决什么问题">能力边界</a> ·
  <a href="references/figure-type-catalog.md">图型目录</a> ·
  <a href="#生产图表索引">生产图表</a> ·
  <a href="#配色主题库">配色主题</a> ·
  <a href="#可复现的质量证据">质量证据</a> ·
  <a href="#安装与更新">安装</a> ·
  <a href="README_EN.md">English</a>
</p>

> 这不是“把数据塞进模板”的画图库。Skill 会先确认研究问题、观测单位、数据结构和目标期刊，再选择图型、组织面板、调用生产资产，并对最终尺寸的 RGB 与灰度校样执行审查。

## 它解决什么问题

<table width="100%">
  <colgroup>
    <col width="250">
    <col width="573">
  </colgroup>
  <thead>
    <tr><th width="30%" valign="middle">普通画图请求</th><th width="70%" valign="middle">Academic Data Visualization</th></tr>
  </thead>
  <tbody>
    <tr><td>先选柱状图、热图或散点图</td><td>先问“这张图要让读者比较、关联还是判断什么？”</td></tr>
    <tr><td>默认忽略样本量、分布和重复测量</td><td>先剖析变量类型、缺失、组大小、异常值与依赖结构</td></tr>
    <tr><td>用默认配色和固定模板美化</td><td>按数据语义、期刊尺寸和证据层级建立视觉系统</td></tr>
    <tr><td>脚本能运行就结束</td><td>程序审查 + 最终尺寸读图 + 灰度校样，发现问题后回改重绘</td></tr>
    <tr><td>只交付一张 PNG</td><td>交付代码、矢量主文件、高分辨率校样与 QA 报告</td></tr>
  </tbody>
</table>

<table width="100%">
  <thead>
    <tr>
      <th width="30%" align="left" valign="middle">规模</th>
      <th width="70%" align="left" valign="middle"><span aria-hidden="true">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>当前仓库提供<span aria-hidden="true">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></th>
    </tr>
  </thead>
  <tbody>
    <tr><td width="30%"><strong>96 个图型模式</strong></td><td width="70%">6 组图鉴 × 16 个已核验模式；另有 9 类专业选图路径，按数据与依赖实现</td></tr>
    <tr><td><strong>29 类生产资产</strong></td><td>Python / R 脚本、示例数据约束与可核验预览</td></tr>
    <tr><td><strong>20 个主题配色</strong></td><td>分类色、发散色、连续色及参考图个性化重绘流程</td></tr>
    <tr><td><strong>4 轮 QA 审查</strong></td><td>反模式、代码与导出、科学逻辑、最终渲染审查</td></tr>
  </tbody>
</table>

### 适合

- 论文主图、补充图、学位论文与学术报告中的数据图；
- 不确定选什么图，需要先从研究问题和数据结构判断；
- 重绘旧图、统一多面板视觉语言或适配目标期刊；
- 投稿前检查文字遮挡、裁切、误导性图型、配色和导出风险。

### 不适合

- 交互式仪表盘、网页数据产品或演示文稿排版；
- 以插画、流程示意或机制图为主体且没有数据图的任务；
- 只做统计检验、数据清洗或文献综述而不需要出图。

## 一分钟开始

### 1. 安装完整 Skill

Windows PowerShell：

```powershell
git clone https://github.com/Starry-cz/academic-data-visualization.git "$env:USERPROFILE\.codex\skills\academic-data-visualization"
```

macOS / Linux：

```bash
git clone https://github.com/Starry-cz/academic-data-visualization.git ~/.codex/skills/academic-data-visualization
```

请安装**完整目录**，不要只复制 `SKILL.md`；`references/`、`scripts/` 与 `assets/` 共同提供图型约束、质量检查和生产资产。

### 2. 直接这样说

```text
使用 academic-data-visualization 分析 experiment.csv。
我要比较三种处理在四个时间点的变化，请先检查样本量、分布和重复测量结构，
再论证图型与多面板方案；目标是双栏论文主图，最终交付可编辑矢量文件、
450 dpi 校样、灰度校样和 QA 报告。
```

### 更多可直接使用的提示词

<table width="100%">
  <thead>
    <tr><th width="16%" valign="middle">场景</th><th width="84%" valign="middle">提示词</th></tr>
  </thead>
  <tbody>
    <tr><td>不知道选什么图</td><td><code>检查 experiment.csv 的变量类型、样本量、分布和分组结构。根据我要论证的结论推荐图型，不要先套模板。</code></td></tr>
    <tr><td>组织论文主图</td><td><code>把这些结果组织成一张投稿级多面板主图，说明每个面板回答什么，以及它们如何形成一条证据链。</code></td></tr>
    <tr><td>重绘旧图</td><td><code>结合 old_figure.png 和 source_data.csv 重建可编辑图表；保留数据含义，不要只美化截图。</code></td></tr>
    <tr><td>适配期刊</td><td><code>按 Nature 双栏终稿尺寸审查并重绘 figure.py，包括字体、栏宽、配色、统计表达与导出。</code></td></tr>
    <tr><td>投稿前审查</td><td><code>审查这张图的图型合理性、文字裁切、图例遮挡、灰度可读性、矢量文本和数据表达风险。</code></td></tr>
  </tbody>
</table>

## 工作方式

<table width="100%">
  <thead>
    <tr><th width="18%" valign="middle">阶段</th><th width="52%" valign="middle"><span aria-hidden="true">&nbsp;&nbsp;</span>Skill 完成什么<span aria-hidden="true">&nbsp;&nbsp;</span></th><th width="30%" valign="middle">主要产物</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>1. 图形合同</strong></td><td>明确研究问题、核心结论、观测单位和目标期刊</td><td>一句话结论 + 面板数据合同</td></tr>
    <tr><td><strong>2. 数据剖析</strong></td><td>检查变量类型、缺失、组大小、分布、异常值和依赖结构</td><td>与论证相关的数据摘要</td></tr>
    <tr><td><strong>3. 选图论证</strong></td><td>根据数据形态选择图型，并主动拦截误导性方案</td><td>主方案 + 备选方案 + 理由</td></tr>
    <tr><td><strong>4. 视觉系统</strong></td><td>固定终稿尺寸、面板层级、字体、色彩语义和后端</td><td>多面板设计简报</td></tr>
    <tr><td><strong>5. 生成复用</strong></td><td>将每个面板分类为原生复用、视觉适配或全新实现</td><td>可复现 Python / R 脚本</td></tr>
    <tr><td><strong>6. 审查交付</strong></td><td>四轮 QA、RGB / 灰度读图、修复重绘与多格式导出</td><td>PDF / SVG、450 dpi 校样、QA 报告</td></tr>
  </tbody>
</table>

## 生产图表索引

这里仅保留重点生产资产的预览，不再重复展示全部图型。完整的选图范围、限制与实现等级见 [`references/figure-type-catalog.md`](references/figure-type-catalog.md)；生成时 Skill 会先检查数据结构与语义是否兼容，再决定原生复用、视觉适配或全新实现。缩略图按画幅分组，原始图仍可点击查看。

### 近方形图型 · 3 × 3

<table width="100%">
  <tr>
    <td width="33%" align="center" valign="top"><strong>3D 热图</strong><br><a href="assets/figure-atlas/3Dheatmap.png"><img src="assets/figure-atlas/readme-cards/3Dheatmap.png?v=card-layout-v1" width="280" alt="3D 热图"></a><br><sub>三维强度矩阵</sub></td>
    <td width="33%" align="center" valign="top"><strong>密度热图</strong><br><a href="assets/figure-atlas/density_heatmap.png"><img src="assets/figure-atlas/readme-cards/density_heatmap.png?v=card-layout-v1" width="280" alt="密度热图"></a><br><sub>大样本二维密度</sub></td>
    <td width="33%" align="center" valign="top"><strong>PCA 双标图</strong><br><a href="assets/figure-atlas/PCA.png"><img src="assets/figure-atlas/readme-cards/PCA.png?v=card-layout-v1" width="280" alt="PCA 双标图"></a><br><sub>样本分离与载荷</sub></td>
  </tr>
  <tr>
    <td align="center" valign="top"><strong>AUROC 曲线</strong><br><a href="assets/figure-atlas/auroc.png"><img src="assets/figure-atlas/readme-cards/auroc.png?v=card-layout-v1" width="280" alt="AUROC 曲线"></a><br><sub>分类与阈值敏感性</sub></td>
    <td align="center" valign="top"><strong>相关性密度图</strong><br><a href="assets/figure-atlas/CorrelationDensity.png"><img src="assets/figure-atlas/readme-cards/CorrelationDensity.png?v=card-layout-v1" width="280" alt="相关性密度图"></a><br><sub>关系、密集区与异常点</sub></td>
    <td align="center" valign="top"><strong>相关性矩阵</strong><br><a href="assets/figure-atlas/Correlationmatrix.png"><img src="assets/figure-atlas/readme-cards/Correlationmatrix.png?v=card-layout-v1" width="280" alt="相关性矩阵"></a><br><sub>多变量关系与共线性</sub></td>
  </tr>
  <tr>
    <td align="center" valign="top"><strong>分组相关矩阵</strong><br><a href="assets/figure-atlas/GroupCorrelationmatrix.png"><img src="assets/figure-atlas/readme-cards/GroupCorrelationmatrix.png?v=card-layout-v1" width="280" alt="分组相关矩阵"></a><br><sub>条件间相关结构</sub></td>
    <td align="center" valign="top"><strong>雷达图</strong><br><a href="assets/figure-atlas/radar.png"><img src="assets/figure-atlas/readme-cards/radar.png?v=card-layout-v1" width="280" alt="雷达图"></a><br><sub>少量对象多指标</sub></td>
    <td align="center" valign="top"><strong>山脊图</strong><br><a href="assets/figure-atlas/RidgePlot.png"><img src="assets/figure-atlas/readme-cards/RidgePlot.png?v=card-layout-v1" width="280" alt="山脊图"></a><br><sub>多组分布变化</sub></td>
  </tr>
</table>

### 横向图型 · 2 × 4

<table width="100%">
  <tr>
    <td width="50%" align="center" valign="top"><strong>柱状图</strong><br><a href="assets/figure-atlas/bar.png"><img src="assets/figure-atlas/readme-cards/bar.png?v=card-layout-v1" width="390" alt="柱状图"></a><br><sub>组间摘要、误差与原始点</sub></td>
    <td width="50%" align="center" valign="top"><strong>分组柱状图</strong><br><a href="assets/figure-atlas/GroupedBarChart.png"><img src="assets/figure-atlas/readme-cards/GroupedBarChart.png?v=card-layout-v1" width="390" alt="分组柱状图"></a><br><sub>多处理 × 多指标</sub></td>
  </tr>
  <tr>
    <td align="center" valign="top"><strong>Mantel 检验图</strong><br><a href="assets/figure-atlas/MantelCorrelation.png"><img src="assets/figure-atlas/readme-cards/MantelCorrelation.png?v=card-layout-v1" width="390" alt="Mantel 检验图"></a><br><sub>距离矩阵与环境关联</sub></td>
    <td align="center" valign="top"><strong>小提琴图</strong><br><a href="assets/figure-atlas/violin_chart.png"><img src="assets/figure-atlas/readme-cards/violin_chart.png?v=card-layout-v1" width="390" alt="小提琴图"></a><br><sub>分布形态与异常值</sub></td>
  </tr>
  <tr>
    <td align="center" valign="top"><strong>趋势图</strong><br><a href="assets/figure-atlas/trend.png"><img src="assets/figure-atlas/readme-cards/trend.png?v=card-layout-v1" width="390" alt="趋势图"></a><br><sub>时间、剂量与环境梯度</sub></td>
    <td align="center" valign="top"><strong>堆叠柱状散点图</strong><br><a href="assets/figure-atlas/StackedBarScatter.png"><img src="assets/figure-atlas/readme-cards/StackedBarScatter.png?v=card-layout-v1" width="390" alt="堆叠柱状散点图"></a><br><sub>组成与样本级观测</sub></td>
  </tr>
  <tr>
    <td align="center" valign="top"><strong>频率 3D 热图</strong><br><a href="assets/figure-atlas/Frequency_3DHeatmap.png"><img src="assets/figure-atlas/readme-cards/Frequency_3DHeatmap.png?v=card-layout-v1" width="390" alt="频率 3D 热图"></a><br><sub>分箱频次与双因子计数</sub></td>
    <td align="center" valign="top"><strong>桑基图</strong><br><a href="assets/figure-atlas/sankey.png"><img src="assets/figure-atlas/readme-cards/sankey.png?v=card-layout-v1" width="390" alt="桑基图"></a><br><sub>类别流向与状态转换</sub></td>
  </tr>
</table>

<p align="center"><a href="references/figure-type-catalog.md"><strong>查看完整图型目录与选择约束 →</strong></a></p>

## 配色主题库

默认主题是 `nature-default`；README 的重点预览按图型分配不同主题，`warm-cool-kinetics` 仅用于动力学类图。每个主题同时定义分类色、发散色和连续色角色，不只是若干十六进制色块。

<table width="100%">
  <tr>
    <td width="50%" align="center" valign="top"><strong>Nature 默认 · nature-default</strong><br><img src="assets/palette-gallery/nature-default.png?qa=direct-labels-v1" width="390" alt="Nature 默认配色预览"></td>
    <td width="50%" align="center" valign="top"><strong>高辨识信号 · vivid-signal</strong><br><img src="assets/palette-gallery/vivid-signal.png?qa=direct-labels-v1" width="390" alt="高辨识信号配色预览"></td>
  </tr>
  <tr>
    <td align="center" valign="top"><strong>明亮生物 · bright-bio</strong><br><img src="assets/palette-gallery/bright-bio.png?qa=direct-labels-v1" width="390" alt="明亮生物配色预览"></td>
    <td align="center" valign="top"><strong>青绿组学 · teal-genome</strong><br><img src="assets/palette-gallery/teal-genome.png?qa=direct-labels-v1" width="390" alt="青绿组学配色预览"></td>
  </tr>
  <tr>
    <td align="center" valign="top"><strong>柔和微生物 · muted-microbe</strong><br><img src="assets/palette-gallery/muted-microbe.png?qa=direct-labels-v1" width="390" alt="柔和微生物配色预览"></td>
    <td align="center" valign="top"><strong>免疫信号 · immuno-signal</strong><br><img src="assets/palette-gallery/immuno-signal.png?qa=direct-labels-v1" width="390" alt="免疫信号配色预览"></td>
  </tr>
  <tr>
    <td align="center" valign="top"><strong>粉彩催化 · pastel-catalysis</strong><br><img src="assets/palette-gallery/pastel-catalysis.png?qa=direct-labels-v1" width="390" alt="粉彩催化配色预览"></td>
    <td align="center" valign="top"><strong>电化学柔彩 · electrochemistry</strong><br><img src="assets/palette-gallery/electrochemistry.png?qa=direct-labels-v1" width="390" alt="电化学柔彩配色预览"></td>
  </tr>
  <tr>
    <td align="center" valign="top"><strong>柔和成本 · soft-cost</strong><br><img src="assets/palette-gallery/soft-cost.png?qa=direct-labels-v1" width="390" alt="柔和成本配色预览"></td>
    <td align="center" valign="top"><strong>柔和学术 · soft-academic</strong><br><img src="assets/palette-gallery/soft-academic.png?qa=direct-labels-v1" width="390" alt="柔和学术配色预览"></td>
  </tr>
  <tr>
    <td align="center" valign="top"><strong>柔彩组学 · pastel-omics</strong><br><img src="assets/palette-gallery/pastel-omics.png?qa=direct-labels-v1" width="390" alt="柔彩组学配色预览"></td>
    <td align="center" valign="top"><strong>暖冷动力学 · warm-cool-kinetics</strong><br><img src="assets/palette-gallery/warm-cool-kinetics.png?qa=direct-labels-v1" width="390" alt="暖冷动力学配色预览"></td>
  </tr>
  <tr>
    <td align="center" valign="top"><strong>含水层复苏 · aquifer-recovery</strong><br><img src="assets/palette-gallery/aquifer-recovery.png?qa=direct-labels-v1" width="390" alt="含水层复苏配色预览"></td>
    <td align="center" valign="top"><strong>神经深蓝 · neuro-navy</strong><br><img src="assets/palette-gallery/neuro-navy.png?qa=direct-labels-v1" width="390" alt="神经深蓝配色预览"></td>
  </tr>
  <tr>
    <td align="center" valign="top"><strong>低温电解质 · cryo-electrolyte</strong><br><img src="assets/palette-gallery/cryo-electrolyte.png?qa=direct-labels-v1" width="390" alt="低温电解质配色预览"></td>
    <td align="center" valign="top"><strong>临床文献 · literature-clinical</strong><br><img src="assets/palette-gallery/literature-clinical.png?qa=direct-labels-v1" width="390" alt="临床文献配色预览"></td>
  </tr>
  <tr>
    <td align="center" valign="top"><strong>鼠尾草方法 · sage-methods</strong><br><img src="assets/palette-gallery/sage-methods.png?qa=direct-labels-v1" width="390" alt="鼠尾草方法配色预览"></td>
    <td align="center" valign="top"><strong>静谧图谱 · quiet-atlas</strong><br><img src="assets/palette-gallery/quiet-atlas.png?qa=direct-labels-v1" width="390" alt="静谧图谱配色预览"></td>
  </tr>
  <tr>
    <td align="center" valign="top"><strong>方法蓝图 · method-blueprint</strong><br><img src="assets/palette-gallery/method-blueprint.png?qa=direct-labels-v1" width="390" alt="方法蓝图配色预览"></td>
    <td align="center" valign="top"><strong>消融对照 · ablation-contrast</strong><br><img src="assets/palette-gallery/ablation-contrast.png?qa=direct-labels-v1" width="390" alt="消融对照配色预览"></td>
  </tr>
</table>

首版图通过审查后，Skill 会询问是否保留当前主题，或改用其他主题、你提供的十六进制颜色、配色参考图或论文图进行个性化重绘。重绘只改变视觉角色，不改变数据、统计、图型、分组顺序或颜色语义。

## 可复现的质量证据

当前仓库基线：

- **40 / 40** 条触发测试正确，包含应触发与不应触发场景；
- **29 / 29** 类生产图型均有可解析脚本；
- **26 / 26** 个 QA 用例命中预期，覆盖 **15 / 15** 类程序检查；
- 组合引擎通过栏宽、450 dpi、TrueType 字体嵌入、矢量导出和配色检查。

```bash
# Skill 结构与触发准确率
python scripts/trigger_benchmark.py

# 引用、生产资产与 QA 规则覆盖
python scripts/check_references.py
python scripts/qa_coverage.py
python scripts/eval_runner.py --report-only

# 审查一个实际绘图脚本
python scripts/qa_validator.py path/to/figure.py

# 为最终 PNG 生成灰度可读性校样
python scripts/grayscale_proof.py figure-proof.png --output figure-proof-grayscale.png
```

质量结论遵循 [`references/checklist.md`](references/checklist.md)：只有反模式、代码与导出、科学逻辑、最终渲染四轮检查全部完成，才可标记为 `READY`。

## 安装与更新

<table width="100%">
  <thead>
    <tr><th width="30%" valign="middle">平台</th><th width="70%" valign="middle"><span aria-hidden="true">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>使用方式<span aria-hidden="true">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Codex</strong></td><td>将完整仓库放入 <code>~/.codex/skills/academic-data-visualization/</code></td></tr>
    <tr><td><strong>Claude Code</strong></td><td>将完整仓库放入 <code>~/.claude/skills/academic-data-visualization/</code></td></tr>
    <tr><td><strong>Cursor</strong></td><td>使用完整 Skill，并按需复制 <a href="install/cursor/.cursorrules">install/cursor/.cursorrules</a></td></tr>
    <tr><td><strong>GitHub Copilot</strong></td><td>使用 <a href="install/copilot/copilot-instructions.md">install/copilot/copilot-instructions.md</a></td></tr>
  </tbody>
</table>

如果保留了本地 clone，更新只需：

```bash
git -C ~/.codex/skills/academic-data-visualization pull
```

Windows PowerShell：

```powershell
git -C "$env:USERPROFILE\.codex\skills\academic-data-visualization" pull
```

## 项目结构

```text
academic-data-visualization/
├── SKILL.md                 # 精简的决策入口与按需路由
├── agents/openai.yaml       # Codex 展示名称与默认提示元数据
├── references/              # 选图、期刊、配色、布局、复用、导出与 QA
├── scripts/                 # 组合、验证、缩略图、配色和灰度校样工具
├── assets/                  # 生产脚本、重点缩略图、配色预览与内部测试资产
└── install/                 # Codex / Cursor / Copilot / Claude 适配文件
```

## 设计参考与致谢

README 与工作流独立吸收了这些公开项目的优秀方法：渐进式展示来自 [GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill)，真实生产脚本的视觉证明来自 [figures4papers](https://github.com/ChenLiu-1996/figures4papers)，问题驱动与多轮 QA 来自 [academic-figure-skill](https://github.com/TingxiYu/academic-figure-skill)，数据顾问与渲染回看闭环来自 [scipilot-figure-skill](https://github.com/Haojae/scipilot-figure-skill)，期刊样式的快速上手与示例组织参考了 [SciencePlots](https://github.com/garrettj403/SciencePlots)。本仓库没有复制这些项目的脚本或生成图。

## 贡献与许可

欢迎提交期刊规范、可访问性改进、真实研究场景和新图型。新增生产模板应同时提供可复现脚本、数据假设、渲染预览和 QA 结果。

本项目采用 [Apache-2.0](LICENSE) 许可证。
