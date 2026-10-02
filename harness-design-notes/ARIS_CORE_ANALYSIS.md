# ARIS 科研核心流程：现状、缺口与最小改造方案

## 1. 本项目真正要解决什么

目标不是“自动生成看起来新颖的方法”，而是建立一条可审计的主链：

> 可靠地理解研究现状 → 发现并证明一个值得研究的问题 → 从问题的约束和机制中推导方法 → 设计能证伪核心主张的验证。

当前只改这条核心链。ARIS 的代码生成、实验执行和论文写作模块保留，不做重写。

## 2. 分析基线

- 主框架：ARIS，官方仓库完整克隆，基线提交 `53562a7c64cc1d55946cba1fb8a8416137143d14`
- ARIS 当前主链：
  `research-lit → idea-creator → novelty-check → research-review → research-refine-pipeline`
- 借鉴但不另建平行流程：
  - Academic Research Suite 的 FINER 问题评估、明确阶段边界、`Question drives method`
  - Nature Academic Search 的“概念拆分—同义词—数据库路由—查询迭代—去重”
  - ARIS 自己的交叉模型裁决、引用核验、Problem Anchor、最小充分机制、单一规范输出

## 3. 对 ARIS 真实代码的判断

### 3.1 `research-lit`

已有优点：

- 多来源检索、去重、论文身份核验和降级策略完整。
- 会区分共识与分歧，能识别 gaps。
- composed mode 已解决重复文档问题。

核心缺口：

- 每篇论文只抽取 `Problem / Method / Results / Relevance`，不足以判断研究现状。
- 没有系统记录证据强度、适用边界、关键假设、失败条件和相互矛盾的结果。
- “找到 papers”之后缺少覆盖度检查；“没有搜到”容易被误当成“没人做过”。
- “find gaps that our work could fill”过早把证据综合跳成了选题判断。

### 3.2 `idea-creator`

已有优点：

- 已有 contradiction、untested assumption、diagnostic 等好视角。
- fan-out 只负责扩大候选集，交叉模型 jury 才裁决质量，设计正确。
- 已有反对 “apply X to Y”、预算硬门槛、novelty-check 和小规模 pilot。

核心断点：

- lens 直接生成的是“idea / hypothesis / minimum viable experiment”，没有先生成和认证“问题候选”。
- 外部模型被要求直接生成 8–12 个 research ideas，仍是从 gap 跳向方案。
- 当前报告明确要求每个推荐项先写 `Method`、后写 `Hypothesis`；方向与本项目目标相反。
- 问题重要性、两种可能答案的价值、证伪条件、决策后果没有形成硬门槛。

### 3.3 `novelty-check`

已有优点：

- 多查询、多来源、最近文献、交叉模型复核、反幻觉处理都值得保留。

核心缺口：

- 输入和评分对象是“proposed method/idea”。
- 没有区分：
  1. 研究问题是否已经被回答；
  2. 问题是否重要；
  3. 拟用机制是否新；
  4. 即便机制不新，新的证据或发现是否仍有贡献。

### 3.4 `research-review`

已有优点：

- 外部 reviewer、连续多轮、原始 trace、可执行批评，保留。

核心缺口：

- 默认把对象当成已有方法/项目，主要审逻辑、方法、实验和论文叙事。
- 在方法出现以前，没有专门审查“这个问题是否真的值得投入”。

### 3.5 `research-refine`

已有优点：

- `Problem Anchor`、`smallest adequate mechanism wins`、一个主贡献、反对强行追热点，正是需要的骨架。
- 方法—主张—最小验证已经连通。

核心缺口：

- Problem Anchor 来自已经选中的“idea + vague approach”，不是经过证据认证的问题。
- 当前会并列比较 “minimal route” 与 “frontier-native route”，容易先从流行方法库挑工具。
- rubric 给 `Frontier Leverage` 15% 权重；这会奖励“新潮”，但新潮不等于问题—方法匹配。
- 没有把问题拆成可追踪的 `design obligations`，所以方法不是严格从约束推导出来的。

### 3.6 `idea-discovery-robot`

已有优点：

- embodiment、传感器、控制接口、仿真/实机、安全、失败指标等领域约束很实用。

核心缺口：

- 它复制并分叉了通用流程，已经发生漂移。
- 它缺少通用入口现有的 `research-refine-pipeline`、research contract 和完整 composed-mode 规则。
- 它在 `idea-creator` 之后再次“rewrite and filter”，可能绕过统一 jury，形成重复裁决。

## 4. 什么才算“真正的好问题”

不直接照搬 FINER 分数。采用更适合科研发现的六维标准，并设置不可互相补偿的硬门槛。

| 维度 | 权重 | 判断问题 |
|---|---:|---|
| 重要性与决策价值 | 25% | 答案会改变哪种理论、设计、评测或实践决策？ |
| 真实知识缺口 | 20% | 未知来自矛盾、边界失效或缺证据，而不只是“论文少”吗？ |
| 精确与可证伪 | 15% | 能否写成一个明确、可被结果否定的问题？ |
| 可回答与可行性 | 15% | 在现有数据、设备、时间和伦理约束下能获得判别性证据吗？ |
| 新颖与非平凡性 | 15% | 最近和基础文献是否尚未充分回答？答案是否不是显然的？ |
| 方法生成力 | 10% | 问题能否导出明确设计义务，并允许比较多个合理机制？ |

硬门槛：

1. 没有可核验的缺口证据，不能标为 `CERTIFIED`。
2. 说不清“答案为正/负分别改变什么”，不能进入方法阶段。
3. 没有可行的判别性测试，只能标为 `HOLD`，不能假装可执行。
4. 安全、伦理或合规不通过时直接 `BLOCKED`，不能用平均分补偿。
5. 交叉模型 reviewer 必须对问题质量作最终裁决；执行模型不能自我放行。

## 5. 最小的新主线

不增加一堆新 skill。仍使用 ARIS 的五个核心 skill，只改变它们之间传递的对象。

```text
研究范围
  ↓
证据地图（不是论文清单）
  ↓
问题候选集
  ↓
好问题门槛：CERTIFIED / HOLD / REJECT
  ↓
设计义务：方法必须满足什么，而不是先选什么方法
  ↓
2–3 条最小机制路线
  ↓
问题新颖性 + 方法新颖性分别核验
  ↓
方法精炼 + 主张驱动验证
```

唯一新增的“概念”是 **Research Problem Contract**，但不新增独立输出文件：

- 在 `IDEA_REPORT.md` 中作为规范章节；
- 选中问题后，写入现有 `idea-stage/docs/research_contract.md`；
- `research-refine` 直接读取同一份契约；
- 不创建 `PROBLEM_REPORT.md`、`GAP_REPORT.md`、`METHOD_REPORT.md` 等重复文档。

## 6. 准备把什么改成什么

### A. `research-lit/SKILL.md`

把每篇论文的：

`Problem / Method / Results / Relevance`

替换为更完整但仍紧凑的 Evidence Card：

`claim / setting / mechanism / evidence / boundary / assumptions / failure / conflicts / verification`

把简单的“按主题总结 + 找 gaps”升级为：

- 证据收敛与冲突矩阵；
- 方法在哪些条件下有效/失效；
- 明示假设与被忽略变量；
- gap 类型和证据强度；
- 搜索覆盖与不确定性；
- “未发现证据”不得写成“证明没人做过”。

这些内容仍折叠进 `IDEA_REPORT.md`，不新增 landscape 文件。

### B. `idea-creator/SKILL.md`

保留 fan-out、机械去重、交叉模型 jury、novelty-check 和预算门槛。

把 lens shard 的输出从“方法 idea”改为“问题候选”：

`observed anomaly / affected scope / evidence / unresolved question / why either answer matters / falsifier / feasible probe / dedup_key`

把外部 brainstorm 从：

“Generate 8–12 concrete research ideas”

改为两步：

1. 生成并裁决 6–10 个问题候选；
2. 只对通过问题门槛的 2–3 个问题，从 `design obligations` 推导最小机制路线。

把报告顺序从：

`Method → Hypothesis → Experiment`

改为：

`Problem evidence → Research question → Why it matters → Falsifier → Design obligations → Derived method → Validation`

### C. `novelty-check/SKILL.md`

保留现有检索与交叉模型复核，增加两个明确模式：

- `problem novelty`：问题是否已被回答、在哪些边界尚未回答、是否只是措辞新。
- `method novelty`：机制、组合、训练信号和实验设定是否已有最近工作。

输出分别给结论，禁止用“方法新”替代“问题好”，也禁止因方法不新而自动否定新的关键发现。

### D. `research-review/SKILL.md`

不再添加另一套 reviewer skill。给现有 reviewer 增加 stage-aware brief：

- `stage=problem`：审问题重要性、真实未知、可证伪性、两面价值、可回答性和隐藏假设。
- `stage=method`：继续使用现有方法/实验审查。

问题阶段的 verdict 为 `CERTIFIED / HOLD / REJECT`，并遵守交叉模型 gate。

### E. `research-refine/SKILL.md`

保留 Problem Anchor、最小充分机制、单一主贡献和多轮 refine。

把输入从“problem + vague approach”改为：

`Certified Problem Contract + constraints + design obligations`

把“minimal route vs frontier-native route”替换为：

1. 从每条 design obligation 推导所需机制；
2. 生成 2–3 条满足义务的最小路线；
3. 用解释力、充分性、可证伪性、复杂度和可行性比较；
4. 只有在现代工具确实更匹配义务时才采用。

review rubric 中把 `Frontier Leverage` 替换为 `Problem–Method Fit`。新潮性只作为时效检查，不再获得独立奖励。

### F. `idea-discovery/SKILL.md`

仍是唯一主编排器，不另建 Scientific Research 大编排器。

主要变化：

- Phase 1 产出 evidence map；
- Phase 2 先完成问题发现和认证，再生成方法；
- Phase 3 分开核验 problem novelty 与 method novelty；
- Phase 4 分开进行 problem review 与 method review；
- Phase 4.5 把完整 Problem Contract 传给 `research-refine-pipeline`；
- `IDEA_REPORT.md` 仍是唯一规范报告。

### G. `idea-discovery-robot/SKILL.md`

不再维护一条复制的机器人科研流程。改成薄领域配置层：

- 调用通用 `idea-discovery` 主链；
- 只补充 robotics evidence profile：embodiment、交互对象、控制接口、稳定性/安全约束、接触与不确定性、仿真—实机、失败指标和硬件可用性；
- 不重复检索、筛选、novelty、review、refine 和输出协议。

这能让“柔顺交互 / 最优阻抗控制”同时覆盖人机与机器人—环境交互，又不会把通用框架写死成机器人专用框架。

### H. 现有模板与镜像

- 修改现有 `RESEARCH_CONTRACT_TEMPLATE.md`，加入：
  `problem evidence / RQ / scope / importance / falsifier / design obligations / unresolved risks`。
- 不新增重复模板。
- 同步 `skills/skills-codex/` 镜像及必要 Claude/Gemini overlay。
- 增加静态测试，检查主线顺序、contract 字段、镜像一致性和机器人入口不再分叉。

## 7. 明确不做什么

- 不重写 ARIS。
- 不把 FINER、Nature、ARS 各复制成一条平行 pipeline。
- 不新增多个同义报告。
- 不把“热门”“引用多”“使用 foundation model”当成好问题标准。
- 不在问题认证前开始堆方法。
- 暂不修改实验执行、代码生成和论文写作模块。

## 8. 推荐实施顺序

1. 先修改 `research-lit` 的证据地图契约。
2. 再修改 `idea-creator`，把“问题认证”放在方法生成前。
3. 修改 `novelty-check` 与 `research-review`，形成问题级 gate。
4. 修改 `research-refine`，让 design obligations 驱动方法。
5. 更新 `idea-discovery` 编排和现有 research contract。
6. 最后把 `idea-discovery-robot` 收敛为薄领域配置层。
7. 同步 Codex 镜像并运行相关测试；与 ARIS 原始 Windows 基线失败分开报告。
