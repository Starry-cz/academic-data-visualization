# 图型覆盖审计

## 审计结论

本次升级以仓库提交 `1d4c909` 为基线。升级前的确定性检查全部通过：

- Skill metadata：PASS；
- directory map 与生产资产：34 / 34，0 FAIL，0 WARN；
- trigger benchmark：40 / 40；
- QA fixtures：26 / 26，覆盖 15 / 15 类检查；
- Python 源码：compileall PASS。

当前注册表建立了 24 个类别、177 个 canonical chart records 和 257 条可验证的分类归属。其中：

- `production_template`：34；
- `reusable_pattern`：83；
- `on_demand`：60。

## 原始清单缺口

输入方案声明存在 714 条源分类条目，但所提供的 Markdown 只有执行方案和字段示例，没有附带 714 条原始清单，也没有另一份可读取的源文件。仓库和工作区全文检索均未发现该清单。

因此本版本采取保守策略：

1. 不伪造 714 / 714 覆盖；
2. 以当前 96 个图型模式、34 类真实生产资产、方案列出的 P1–P3 图型及领域路由建立 24 类注册表；
3. 在 `source_expectation` 中保留声明数量、可验证数量和 `source_complete: false`；
4. 让生成器和检查器支持后续导入，并将缺失源条目暴露为待规范化草稿；
5. README 明确区分“可验证源归属”和“方案声明但未提供的原始条目”。

收到原始清单后，应把重复出现保留为 `source_memberships`，但不得复制 canonical 定义。

## 现有生产资产迁移

`assets/figures/` 下所有 34 个含脚本的生产目录均已映射到唯一 canonical ID，并补充 `asset.yaml`。每个 manifest 记录：

- canonical chart ID；
- Python / R 后端；
- 实际入口脚本；
- 真实 PNG 预览；
- 可用 SVG / PDF；
- 数据模式、复用限制、宽高比、主题和 QA 命令。

`directory-map.md` 仍只承担真实生产目录路由，没有写入未实现图型。

## 别名、重复与同名异义

- 跨类别重复通过一个 canonical record 加多个 `category_ids` 处理；
- 中文名、英文名、缩写和常见别名由 `chart-alias-index.md` 统一生成；
- “漏斗图”拆分为元分析发表偏倚与转化流程两种语义；
- “棒棒糖图”拆分为通用排序与突变位点两种数据契约；
- `check_chart_registry.py` 会阻止未解决的别名冲突。

## 状态判定依据

### production_template

仅当真实目录同时存在脚本、PNG 与 `asset.yaml`，且 manifest 与 registry 双向一致时使用。

### reusable_pattern

用于统计与视觉规则成熟、可用通用后端可靠实现，但尚未形成独立生产资产包的图型。不得填写 `asset_path`。

### on_demand

用于依赖坐标、拓扑、专业注释、模型对象、图像标定或复杂后端的图型。不得用外形相似的普通图冒充，也不得生成虚假预览。

## 现有图鉴与路由

- 旧 6 组 × 16 个图鉴模式及原路径保留；
- `figure-type-catalog.md` 继续提供按信息任务的快速选择；
- 新增的 24 类索引只在匹配请求时读取 1–3 个分类文件；
- 用户名称先进入 alias index，再进入 canonical record、实现状态和真实资产路径；
- 未改变现有 README 图鉴、配色预览和生产脚本路径。

## 仍待外部输入

唯一未能完成的声明性指标是“714 / 714 原始源条目映射”，原因是源条目未包含在输入文件中。该缺口不是实现错误，也不会降低现有 177 个图型记录、257 条归属和 34 个生产资产的真实性。
