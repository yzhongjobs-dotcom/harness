# ARIS Method Design 科研流程与标准 — Handoff

## 0. 本 Handoff 的唯一用途

本 Handoff 只负责梳理已经确认的 **Method Design（方法设计）科研流程和科研标准**。

当前任务的最终目标不是总结“顶刊论文有什么特点”，也不是建立一套形式完整的流程审计，而是让 Auto Research（自动科研）真正具备：

> **从真实 Failure（失败）和 Mechanism-Level Root Cause（机制级根因）出发，主动发现、验证、迁移/重构并最小化实现一个顶会顶刊级 Strong Method Seed（强方法种子）的能力。**

后续所有 Harness（科研流程执行框架）设计，都应以这里的科研逻辑为上游依据；不能因为现有 Harness 容易实现，就反过来削弱科研标准。

---

# 1. 总任务与阶段关系

总任务：

> **“先逆向分析，然后确定科研标准和流程，然后转化为方法设计模块的 Harness。”**

因此严格分为两阶段：

### Phase I（第一阶段）：科研方法论与顶级案例逆向分析

目标：

> **搞清楚真实科研过程到底怎么走、每一步什么情况下算对、什么情况下算错。**

最终标准不能提前拍脑袋确定，而必须通过：

> **多篇顶级成功案例 + 同路径近失败/普通 application（应用）案例 + 必要反事实证据 → Cross-Case Causal Induction（跨案例因果归纳）。**

### Phase II（第二阶段）：Harness（科研流程执行框架）化

只有科研流程和标准确定后，才转成：

> **Agent（智能体）可执行 → Reviewer（审查器）可判断 → Validator（验证器）可检查 → Gate（门控）可阻断 → 失败可回退。**

---

# 2. 当前重点研究的 Method-Formation Path（方法形成路径）

不同顶级研究可能有不同的 formation mode（形成模式），例如：

- Failure / RCA + Mechanism Intervention / Transfer（失败 / 根因分析 + 机制干预 / 迁移）；
- Representation / Certificate Construction（表示 / 证书构造）；
- Formal Obstruction / Generalization（形式障碍 / 泛化）；
- Measurement / Identifiability（测量 / 可辨识性）；
- Capability Complementarity / System Co-design（能力互补 / 系统协同设计）；
- Infrastructure / Evaluation（基础设施 / 评估）；
- Mechanism / Evidence Clarification（机制 / 证据澄清）。

当前重点只研究第一条：

> **从失败中找问题并分析根因 + 通过方法/机制迁移解决问题。**

不能把所有顶级论文混在一起总结，否则容易只得到：

> “问题重要、方法新颖、实验充分”

这种无法指导 Agent（智能体）发明方法的泛化经验。

其他 formation mode（形成模式）主要作为对照，用于区分：

> **哪些是所有顶级研究共有的要求，哪些才是 RCA-Transfer（根因分析—迁移）路径特有的形成规律。**

不得为了统一模板给其他类型论文虚构 Failure（失败）、Root Cause（根因）或 Source Transfer（源迁移）。

---

# 3. 整个任务真正的中心：Method Genesis（方法生成逻辑）

最重要的不是：

> “论文最后用了什么 Method（方法）？”

而是恢复：

> **失败**
> **→ 根因**
> **→ 需要改变什么机制**
> **→ 为什么想到这个源机制**
> **→ 为什么它能迁**
> **→ 为什么必须这样改造**
> **→ 最终 Method（方法）。**

也就是恢复 Method Genesis（方法生成逻辑）。

整个流程真正要回答的只有三个核心“为什么”：

### 1. 为什么会想到这个 Source Mechanism（源机制）？

即：

> **Target Root Cause（目标根因）**
> **→ Required Mechanism Change（所需机制改变）**
> **→ 为什么会想到这个 Source Mechanism（源机制）？**

### 2. 为什么这个机制逻辑上真的能迁？

核心不是“有 analogy（类比）”，而是：

> **Source Intervention（源干预） = Target Root Cause（目标根因）真正需要的干预。**

### 3. 为什么迁过来以后会自然形成一个新的强 Method（方法）？

必须恢复：

> **Source Mechanism（源机制） + Target Domain Constraints（目标域约束）**
> **→ New Method Structure（新方法结构）。**

方法谱系、文献追踪、目标域 novelty 检查、反事实实验、负案例等都只服务于这三个核心问题，不能与它们平级。

所以最终 Method Design（方法设计）绝不能退化为：

> “十几个检查项全部打勾”。

真正要恢复的是一篇：

> **“方法发明解剖报告”。**

核心问题仍然是：

> **这个方法为什么会被想到？为什么逻辑上应该迁？为什么迁完以后会自然变成这个新方法？**

这三个“为什么”才是 ARIS 真正能够自己产生 Strong Method Seed（强方法种子）的核心知识。

---

# 4. Method Genealogy（方法谱系）是恢复 Method Genesis 的必要证据

很多顶刊论文不会写：

> “我们从领域 X 搬来了方法 Y。”

甚至会把它写成目标问题自然推导。

因此必须追踪：

> **Target Paper（目标论文）**
> **→ 方法前驱**
> **→ 核心机制来源论文**
> **→ 必要时更早的原始机制来源。**

真正需要恢复：

> **Source Problem（源问题）**
> **→ Source Intervention（源干预）**
> **→ Changed Variable / Structure（被改变变量 / 结构）**
> **→ Causal Effect（因果作用）**
> **→ Outcome（结果）**
> **→ Target Paper（目标论文）最终保留什么、改变什么。**

不能死板相信论文包装后的 motivation（动机）。

但也不能把可重建的 causal formation logic（因果形成逻辑）冒充作者真实历史构思过程。

逆向分析证据应区分：

- **E1：原文显式证据**——论文直接说了什么；
- **E2：结构性重建**——根据公式、citation genealogy（引用谱系）、作者前作、ablation（消融）、naive variant（朴素变体）等可靠恢复；
- **E3：历史猜测**——关于作者当时究竟怎么想到的推测。

没有真实 genesis evidence（生成过程证据）时，只能说：

> **“该论文最终方法具有这样的 causal formation logic（因果形成逻辑）。”**

不能声称：

> “作者当时就是这么想出来的。”

E1 / E2 / E3 是逆向分析的证据纪律，不要求机械变成 Runtime（运行时）的三个字段。

---

# 5. RCA-Transfer 路径的核心科研判断

对于当前重点研究的 RCA-Transfer（根因分析—迁移）路径，强 Method Seed（方法种子）的核心形成逻辑是：

> **真实且重要的 Target Failure / Root Cause（目标失败 / 根因）**
> **→ 明确 Required Mechanism Change（所需机制改变）**
> **→ 主动发现能够实施该改变的 Strong Source / Solution Principle（强源机制 / 解决原理）**
> **→ 通过 Intervention-Level Alignment（干预级对齐）证明逻辑上能迁**
> **→ 证明 Target Domain 尚未覆盖等价 causal intervention（等价因果干预）**
> **→ 仅按真实 Target Constraints（目标约束）完成必要改造**
> **→ 形成可从 Target Root Cause 自然推出、具有清晰 Mechanism / Scientific Delta（机制 / 科学增量）的 Strong Method Seed。**

这一路径中的创新性不要求 Source primitive（源基础技术）本身原创，也不要求为了“显得创新”制造大量 Target Transformation（目标域改造）。真正决定创新强度的是：**目标问题是否真实重要、目标域是否首次实现关键 causal intervention、机制关系是否实质改变、以及由此产生的 Scientific Delta 是否足够强。**

## 5.1 Strong Source Mechanism（强源机制）

“强”不是：

- venue（期刊会议等级）高；
- 方法热门；
- primitive（基础技术单元）新。

真正的 Strong Source Mechanism（强源机制）要求恢复：

> **Source Problem（源问题）**
> **→ Source Intervention（源干预）**
> **→ Changed Variable / Structure（被改变变量 / 结构）**
> **→ Causal Effect（因果作用）**
> **→ Outcome（结果）**
> **→ Assumptions / Boundary（假设 / 边界）。**

并且有可信原域 Evidence（证据）表明：

> **Source Intervention（源干预）**
> **→ Mechanism Change（机制改变）**
> **→ Outcome（结果）。**

必须知道它**为什么在源领域有效**，而不是只知道“用了某个算法”。

---

## 5.2 True Isomorphism（真实同构）= Intervention-Level Alignment（干预级对齐）

真正必须同构的是：

> **Source Intervention（源干预）**
> **↔ Target Required Structural Change（目标所需结构改变）。**

形式上：

Target（目标）：

> **Vₜ : v₀ → v₁**

Source（源）：

> **Vₛ : u₀ → u₁**

需要存在映射，使：

> **Source 实际改变的 causal/computational variable（因果 / 计算变量），就是 Target RCA（目标根因分析）证明必须改变的变量。**

核心原话：

> **“Source Intervention = Target Root Cause 真正需要的干预。”**

真正需要同构的是 intervention structure（干预结构），不是整个 problem story（问题故事）。问题名称相似、任务相似、网络结构相似、两边都有 uncertainty / sequence / contact（不确定性 / 序列 / 接触），都不能证明同构。

---

## 5.3 Collision-Driven Necessary Adaptation（冲突驱动必要改造）

Target Adaptation（目标域改造）的标准是：

> **Source Assumption（源假设）**
> **× Target Constraint（目标约束）**
> **→ Observable Incompatibility（可观察不兼容）**
> **→ Required Repair / Claim Restriction（必要修复 / 声明限制）。**

所有真实 Assumption–Constraint Collision（假设—约束冲突）必须闭合。

> **没有真实 Collision（冲突）时，不得为了显得创新而强行增加结构。**

因此，**直接迁移并不天然弱**：如果 Source Intervention 与 Target Required Change 精确对齐、目标域尚未覆盖等价干预、没有新的 Target Collision，并且 Mechanism / Scientific Delta 足够强，较少甚至没有结构改造仍然可以形成强创新。

---

## 5.4 Target Intervention Novelty（目标域干预新颖性）

不能只查：

> “目标领域有没有使用同名算法？”

真正要证明的是：

> **Target-Domain SOTA（目标领域最先进工作）没有已经实现相同或等价的 causal intervention（因果干预）。**

所以：

> **算法名不同但 causal intervention（因果干预）相同，也属于已覆盖。**

反之：

> **Source primitive 已知、甚至在别的领域成熟，也不妨碍目标域首次实现关键 causal intervention 成为强创新。**

---

## 5.5 Natural Growth / Natural Derivation（自然生长 / 自然推导）

这是判断方法迁移是否真正完成的关键检验。

删掉所有 Source-Domain Story（源领域故事），只留下：

> **Target Failure（目标失败）**
> **→ Target Root Cause（目标根因）**
> **→ Required Mechanism Change（所需机制改变）**
> **→ Target Constraints（目标约束）**
> **→ Final Method（最终方法）。**

然后问：

> **“从目标问题自身的根因出发，这个方法是否仍然显得必要、自然、无冗余？”**

如果必须说：

> “因为领域 X 有一个很牛的方法，所以我们拿来试试”

才能解释 Method（方法），说明迁移没有真正完成。

核心原话：

> **“方法像是从目标 Root Cause 自然推导出来的。”**

> **“源领域只负责告诉研究者去哪里发现这个解决机制。”**

---

## 5.6 创新性的判断与科研表达

创新性必须分清“技术从哪里来”和“目标领域新增了什么”。一个已知 Source Mechanism（源机制）被迁移到新的 Target causal position（目标因果位置），如果第一次解决了真实未解 Root Cause（根因）并形成新的 Target causal/mechanism relation（目标因果 / 机制关系），可以构成顶会顶刊级强创新。

因此：

- **Source primitive originality（源基础技术原创性）不是 Strong Method Seed 的必要条件；**
- **Target Intervention Novelty（目标干预新颖性）和 Scientific / Mechanism Delta（科学 / 机制增量）才是关键；**
- cross-domain / cross-paradigm mechanism transfer（跨领域 / 跨范式机制迁移）本身可以是核心创新来源；
- contribution framing / positioning（贡献定位 / 表述）可以把真实创新表达得更准确、更有力，但不能制造不存在的 Root Cause、Novelty 或 Scientific Delta。

# 6. 已冻结的主科研流程

当前 RCA-Transfer（根因分析—迁移）主路径为：

> **Failure Activation（失败激活）**
> **→ Operating Envelope（工作范围）**
> **→ Simple-Repair Falsifier（简单修复反证）**
> **→ Mechanism-Level RCA（机制级根因分析）**
> **→ Required Intervention / Required Mechanism Change（所需干预 / 所需机制改变）**
> **→ Required Capability（所需能力）**
> **→ Canonical Design Obligations（规范设计义务）**
> **→ Four-Space Principle Search（四空间原理搜索）**
> **→ Candidate Principle / Underdetermination Check（候选原理 / 欠确定性检查）**
> **→ Early Target-Intervention Novelty（早期目标域干预新颖性）**
> **→ Provisional Scientific Delta（初步科学增量）**
> **→ Discriminating Prediction / Killer Test（判别预测 / 关键测试）**
> **→ Human Gate（人工门控）**
> **→ Evidence Update & Principle Convergence（证据更新与原理收敛）**
> **→ Selected Principle（选定原理）**
> **→ Assumption–Constraint Collision（假设—约束冲突）**
> **→ Minimal Faithful Target Realization（最小忠实目标域实现）**
> **→ Principle-Only Closure（纯原理闭合）**
> **→ Residual MUST（残余必要条件）**
> **→ Minimal Necessary Composition（最小必要组合）**
> **→ Causal Repair DAG（因果修复有向无环图）**
> **→ Mechanism Delta Freeze（机制增量冻结）**
> **→ Final Target-Intervention Novelty Closure（最终目标域干预新颖性闭合）**
> **→ Natural-Derivation Test（自然推导测试）**
> **→ Claim-Proportional Feasibility Closure（与声明匹配的可行性闭合）**
> **→ Counterfactual Necessity Package（反事实必要性包）**
> **→ Final Scientific Delta Claim（最终科学增量声明）**
> **→ Top-Venue Method Strength Gate（顶会顶刊方法强度门）**
> **→ Top-Venue Strong Method Seed Acceptance（顶会顶刊级强方法种子接受）**
> **→ Full Causal Validation（完整因果验证）**
> **→ Established Scientific Delta（已建立科学增量）。**

任何不可修复硬失败进入 **NO-GO（终止）** 并停止该 Seed；NO-GO 不继续进入 Full Causal Validation。

Four-Space Principle Search（四空间原理搜索）包括：

1. First-Principles Derivation（第一性原理推导）；
2. Problem Representation Transformation（问题表示变换）；
3. Same-Field Mechanisms（同领域机制）；
4. Cross-Domain Structurally-Isomorphic Problem–Intervention Pairs（跨领域结构同构问题—干预对）。

其中 Cross-Domain Search（跨领域搜索）必须真实执行，但**最终采用的 Principle 不要求一定来自跨领域 Source**。若采用 Source-derived Principle（源机制派生原理），必须完成 Source Discovery、Genealogy、Causal Efficacy 和 Intervention-Level Alignment；若采用 First-Principles / Representation 路径，则必须有对应 derivation evidence（推导证据），不得强行制造 Source Story（源故事）。

核心原则：

> **任何硬门失败必须回到真正对应的上游步骤，不能靠更漂亮的论文叙事继续推进。**

# 7. Step 1 — Failure Activation（失败激活）

Failure（失败）必须写成：

> **condition（条件）**
> **→ observable failure（可观察失败）**
> **→ consequence（后果）。**

不能只写：

> “泛化差”“鲁棒性不足”“精度低”“效率低”“可能不稳定”。

必须证明：

- 在目标条件下 Failure（失败）真实发生；
- 有实验、文献、多源证据或形式分析；
- Failure 实际限制性能、能力、保证、可辨识性或可实现性。

核心原则：

> **correct mechanism + wrong bottleneck = weak research**
> **正确机制 + 错误瓶颈 = 弱研究。**

---

# 8. Step 2 — Operating Envelope（工作范围）

在设计方法前明确 Failure（失败）和 Method Claim（方法声明）真正覆盖的：

- dynamics（动力学）；
- contact / interaction（接触 / 交互）；
- noise / uncertainty（噪声 / 不确定性）；
- sensing / observability（感知 / 可观测性）；
- hardware（硬件）；
- data（数据）；
- real-time（实时性）；
- safety（安全性）；
- task boundary（任务边界）；
- 明确不声称覆盖的范围。

目的：

> **防止通过极端条件制造一个“问题”，再把普通改进包装成必要的新 Method（方法）。**

---

# 9. Step 3 — Simple-Repair Falsifier / Necessity（简单修复反证 / 必要性）

在声称“必须设计新机制”前，先测试或严谨排除：

- tuning / gain scheduling（调参 / 增益调度）；
- standard filter / estimator / observer（标准滤波器 / 估计器 / 观测器）；
- 已知 constraint / certificate（约束 / 证书）；
- 增加数据 / 容量但不改变核心计算关系；
- local reparameterization（局部重新参数化）；
- 更强已有 baseline（基线）；
- 最近已有机制的公平组合。

核心问题：

> **“旧机制真的补不上吗？”**

Simple Repair（简单修复）既可由文献，也可由 empirical / analytical validation（实验 / 分析验证）判断。

最终必须区分：

- **FULLY\_COVERED（完全覆盖）**：Simple Repair 已覆盖目标 Failure Envelope（失败范围），没有新 Method（方法）的必要性；
- **RESIDUAL\_SAME\_PROBLEM（残余仍是同一问题）**：Simple Repair 只覆盖部分范围，仍存在重要 residual failure（残余失败）；
- **RESIDUAL\_REDEFINES\_PROBLEM（残余重新定义问题）**：剩余问题已经实质改变，需要重新定义 Problem（问题）；
- **UNRESOLVED（未解决）**：证据不足，不能继续假装 Necessity（必要性）成立。

FULLY\_COVERED（完全覆盖）不是：

> “Method Seed 被拒绝”。

而是：

> **no new method needed（不需要新方法）。**

---

# 10. Step 4 — Mechanism-Level RCA（机制级根因分析）

RCA（根因分析）必须继续追到具体：

- state（状态）；
- relation（关系）；
- information path（信息路径）；
- representation（表示）；
- constraint（约束）；
- observability condition（可观测条件）；
- optimization variable（优化变量）；
- decision relation（决策关系）；
- guarantee quantifier（保证量词）；
- causal/computational variable（因果 / 计算变量）。

必须：

1. 给出 causal chain（因果链）；
2. 至少保留一个可证伪 Rival RCA（竞争根因）；
3. 能预测 Failure（失败）何时出现 / 不出现；
4. 禁止因为已经知道某个 Method X（方法 X），再事后把 Root Cause（根因）写成“需要 X”。

PASS（通过）的 RCA 必须：

> \*\*解释 Failure Boundary（失败边界）
>
> - 区分 Rival RCA（竞争根因）
> - 推出 Required Mechanism Change（所需机制改变）。\*\*

---

# 11. Step 5 — Required Mechanism Change / Required Intervention（所需机制改变 / 所需干预）

必须在看到具体算法前，从 RCA（根因分析）独立推出：

> **variable / relation X（变量 / 关系 X）：**
> **existing state A（现有状态 A）**
> **→ required state B（所需状态 B）。**

核心问题：

> **“理论上什么东西必须发生改变，才能解除这个 Root Cause（根因）？”**

不能写成：

> “需要 Transformer / Diffusion / MPC / GP / RL。”

而应说明：

- causal/failing structure（因果 / 失败结构）；
- required change（所需改变）；
- change direction（改变方向）；
- causal position（因果位置）；
- activation condition（生效条件）；
- root-cause resolution rationale（解除根因的理由）。

RMC（所需机制改变）本身负责描述**必须发生什么变化**。

PASS / FAIL（通过 / 失败）以及如何验证这个变化，应放在后续 Validation Obligation（验证义务），不是塞进 RMC 本身。

---

# 12. Step 6 — Required Capability / Canonical Design Obligations（所需能力 / 规范设计义务）

Required Mechanism Change（所需机制改变）之后，先明确实现该改变所需的 Required Capability（所需能力），再形成 Canonical Design Obligation Set（规范设计义务集合）。

Design Obligation（设计义务）不是：

> “希望方法更鲁棒 / 更泛化 / 更智能”。

它必须是：

> **Method（方法）若不满足，就无法解除 Root Cause（根因）的 MUST（硬性必要条件）。**

每个 obligation（义务）必须对应：

- Root Cause 中必须改变的机制；
- Target Operating Envelope（目标工作范围）中不可违反的约束；
- 或后续设计引入的真实 Residual MUST（残余必要条件）。

它负责：

> **驱动 Source Search（源机制搜索）并约束 Candidate Principle（候选原理），防止先选热门算法再写理由。**

---

# 13. Step 7 — Four-Space Principle Search（四空间原理搜索）

这是 Auto Research（自动科研）能否真正“发明方法”的关键。目标不是先找一个热门算法，而是从 RMC / Design Obligations（所需机制改变 / 设计义务）出发，主动寻找或推导能够实施 Required Intervention（所需干预）的 Solution Principle（解决原理）。

Search Coverage（搜索覆盖）按四类组织：

1. **First-Principles Derivation（第一性原理推导）**；
2. **Problem Representation Transformation（问题表示变换）**；
3. **Same-Field Mechanisms（同领域机制）**；
4. **Cross-Domain Structurally-Isomorphic Problem–Intervention Pairs（跨领域结构同构的问题—干预对）**。

其中：

- 前两项主要是 Cognitive Operation（认知操作），不应为了形式统一伪装成文献 Query（查询）；
- Same-Field（同领域）和 Cross-Domain（跨领域）需要真实 Evidence / provenance（证据 / 来源）；
- Cross-Domain Search（跨领域搜索）必须真实执行，但最终方法**不要求一定采用跨领域 Source（源机制）**；
- 如果没有可靠跨域同构，或者 First-Principles（第一性原理）/ Representation Transformation（表示变换）更自然、更强，应采用更合理的 Principle；
- 不设置固定 query（查询）数量、固定候选数或固定领域列表；
- author prior / genealogy / nearest prior（作者前作 / 谱系 / 最近邻工作）属于 discovery / genealogy / novelty evidence（发现 / 谱系 / 新颖性证据），不单独制造第五个 Search Space（搜索空间）。

对于 Cross-Domain / Source-derived branch（跨领域 / 源机制派生分支），真正搜索的问题是：

> **“哪个已有机制已经成功改变了我这里必须改变的 causal/computational variable（因果 / 计算变量）？”**

搜索对象是：

> **Solution Principle / Intervention Operator（解决原理 / 干预算子）**

而不是算法标签。

---

# 14. Cross-Domain Source Discovery（跨领域源机制发现）执行逻辑

本节只适用于 Cross-Domain / Source-derived branch（跨领域 / 源机制派生分支），直接回答最高层问题：**为什么会想到这个 Source Mechanism（源机制）？** Cross-Domain Search 本身仍是四空间搜索的必执行分支，但最终 Candidate 不要求采用这里找到的 Source。

## 14.1 RMC（所需机制改变）先派生 Target Mechanism Signature（目标机制签名）

正确关系：

> **Accepted RMC（已接受的所需机制改变）**
> **→ derive Target Mechanism Signature（派生目标机制签名）。**

Target Mechanism Signature（目标机制签名）只是 Source Discovery（源机制发现）和 Alignment（对齐）的 reasoning anchor（推理锚点），不替代 RMC（所需机制改变）。

---

## 14.2 去领域化表示用于 Reasoning（推理），不能直接当成唯一 Retrieval Language（检索语言）

不同学科研究同一种 causal problem–intervention structure（因果问题—干预结构）时，往往使用完全不同的专业术语。

因此不是：

> “把目标问题翻译成几个无领域关键词 → 搜遍所有学科”。

而应是：

> **Target Mechanism Signature（目标机制签名）**
> **→ 找可能存在同构 Problem–Intervention Pair（问题—干预对）的 Candidate Domain（候选领域）**
> **→ 学习该领域自己的 Terminology（术语）**
> **→ 用该领域自己的术语搜索**
> **→ 再回到统一 Mechanism Space（机制空间）判断 Intervention-Level Alignment（干预级对齐）。**

最终原则：

> **Retrieval Space（检索空间）要领域化；**
> **Reasoning Space（推理空间）要机制化。**

---

## 14.3 Candidate Domain Discovery（候选领域发现）

必须执行两个互补的核心通道：

### MODEL\_PRIOR（模型科研先验）

利用模型已有科研知识提出：

> “哪些成熟领域可能处理过这个结构问题、可能存在什么 intervention family（干预家族）？”

但：

> **MODEL\_PRIOR = Search Hypothesis（搜索假设），不是 Scientific Evidence（科研证据）。**

### ACADEMIC\_BRIDGE（学术桥接）

通过正式文献搜索 / 阅读中的：

- review / tutorial（综述 / 教程）；
- 已读论文术语；
- Related Work（相关工作）；
- references / citation chain（参考文献 / 引用链）；
- query refinement（查询细化）

发现模型先验遗漏的领域和专业术语。

GitHub / Reddit / StackExchange / X 等专业讨论如果有现成线索，可以作为 weak discovery signal（弱发现信号）帮助提出 Candidate Domain / Terminology Hypothesis（候选领域 / 术语假设），但不能作为 Source Causal Efficacy（源机制因果有效性）的科研证据，也不是当前 mandatory coverage（强制覆盖）通道。

---

## 14.4 Domain Terminology Grounding（领域术语落地）

Candidate Domain（候选领域）正式进入 Source Search（源机制搜索）前，应通过：

- review（综述）；
- tutorial（教程）；
- foundational paper（奠基论文）；
- representative work（代表性工作）

确认该领域自己的：

- canonical problem terms（规范问题术语）；
- variable / state terms（变量 / 状态术语）；
- intervention terms（干预术语）；
- method-family terms（方法家族术语）。

之后使用该领域自己的语言搜索。

---

## 14.5 Domain-Specific Problem–Intervention Search（领域内问题—干预搜索）

真正恢复：

> **Source Problem（源问题）**
> **→ Source Intervention（源干预）**
> **→ Changed Variable / Structure（被改变变量 / 结构）**
> **→ Causal Effect（因果作用）**
> **→ Outcome（结果）。**

---

## 14.6 Iterative Domain Expansion（迭代扩域）

搜索过程中，如果发现新的：

- terminology（术语）；
- mechanism（机制）；
- reference / citation（参考文献 / 引用）；
- research community（研究社区）

并指向新的合理 Candidate Domain（候选领域），可以继续扩域。

但必须：

> **先形成 Domain Hypothesis（领域假设），再进行对应搜索。**

禁止：

> **先找到一个 Source（源机制），再事后编造“为什么想到它”的 Discovery Story（发现故事）。**

这条要求的根本目的不是增加字段，而是防止 post-hoc rationalization（事后合理化），真正保存：

> **“为什么找到这个 Source（源机制）？”**

---

# 15. Step 8 — Source Genealogy & Causal Efficacy（源机制谱系与因果有效性）

本 Step 只适用于 Source-derived Principle（源机制派生原理）。First-Principles / Representation-derived Candidate（第一性原理 / 表示推导候选）以对应 derivation evidence（推导证据）替代 Source Genealogy。

每个 Source Mechanism（源机制）必须回答：

> **Source Problem（源问题）是什么？**
> **Source Intervention（源干预）到底做了什么？**
> **改变哪个 Variable / Relation（变量 / 关系）？**
> **这个改变产生什么 Causal Effect（因果作用）？**
> **为什么 Outcome（结果）改善？**
> **Assumption / Activation / Boundary（假设 / 生效条件 / 边界）是什么？**

Source Mechanism（源机制）必须有正式 Scientific Evidence（科研证据）。

MODEL\_PRIOR（模型先验）等只能解释：

> “为什么去那里找？”

不能证明：

> “这个 Source（源机制）真的有效。”

---

# 16. Step 9 — Intervention-Level Alignment（干预级对齐）

本 Step 只适用于 Source-derived Principle（源机制派生原理）；其他 Candidate 必须证明自身 derivation 与 Target Required Mechanism Change（目标所需机制改变）一致。

Source-derived Principle 的最终硬门：

> **Source Intervention（源干预）必须改变 Target RCA（目标根因分析）证明必须改变的 causal/computational variable（因果 / 计算变量）。**

至少判断：

- causal role（因果角色）；
- variable / relation（变量 / 关系）；
- change direction（变化方向）；
- intervention position（干预位置）；
- causal direction（因果方向）；
- activation condition（生效条件）；
- causal effect（因果作用）；
- mismatch / target constraints（不匹配 / 目标约束）。

Alignment PASS（对齐通过）后，先从 Source 中抽象：

> **Solution Principle / Intervention Operator（解决原理 / 干预算子）**

即只保留“在什么条件下，对什么变量实施什么干预，为什么能解除对应 causal failure（因果失败）”，不直接复制 Source implementation（源实现）。

Alignment FAIL（对齐失败）时：

- Source 本身不匹配 → 利用新术语 / mechanism clue（机制线索）回到 Domain Discovery / Source Search（领域发现 / 源搜索）；
- Target mapping / activation（目标映射 / 生效条件）不成立 → 重做 mapping 或换 Source；
- 多个合理 Source 都暴露同一 RMC 问题 → 返回 RCA，重新检查 Required Mechanism Change（所需机制改变）。

> **核心映射失败的 Source 不能生成 Active Candidate Principle（有效候选原理）。**

# 17. Step 10 — Early Target Intervention Novelty（早期目标域干预新颖性）

在继续投入 Candidate Principle（候选原理）前，先检查 Target Domain（目标领域）是否已经实现 equivalent causal intervention（等价因果干预）。

必须检查：

- 同名方法；
- 异名等价干预；
- nearest target priors（目标域最近邻已有工作）；
- 作者前作；
- citation genealogy（引用谱系）。

已经被目标领域覆盖的 Candidate（候选）不得因为 Source Primitive（源基础技术）很新，就包装成新的强 Method Seed（方法种子）。

---

# 18. Step 11 — Candidate Principle / Underdetermination（候选原理 / 欠确定性）

Human Gate（人工门控）前的核心对象首先是：

> **Solution Principle（解决原理）**

而不是完整 Method（方法）。

如果 solution space（解空间）确实 underdetermined（欠确定），保留真正不同的 Candidate Principles（候选原理）。

如果 geometry / invariance / formal constraints（几何 / 不变性 / 形式约束）已经把解空间高度限制：

> **允许只有一个自然 Principle（原理），不得机械制造多个候选。**

C-K Theory（概念—知识理论）在本流程中的有效要求是：

> **Concept（概念）和 Knowledge（知识）允许联动演化；新的 Knowledge（知识）可以修改 Principle（原理），必要时甚至让上游 RCA（根因分析）重新打开。**

不需要把 C-K 单独做成一个并行模块。

---

# 19. Step 12 — Discriminating Prediction / Killer Test（判别预测 / 关键测试）

Strong Inference（强推断）在本流程中的有效要求是：

> **保留竞争解释，并设计能够区分它们的实验。**

测试不是：

> “看看性能涨不涨”。

而是：

> **如果 Principle P（原理 P）成立，Observable Y（可观察量 Y）应出现 Pattern A（模式 A）；**
> **如果 Rival Principle / Rival RCA（竞争原理 / 竞争根因）成立，应出现不同 Pattern B（模式 B）。**

Cheapest / Killer Test（最低成本 / 关键测试）优先，但必须具有真正 discriminative power（判别力）。

普通 ablation（消融）不自动等于判别实验。

---

# 20. Step 13 — Human Gate（人工门控）与 Evidence Convergence（证据收敛）

在真实需要成本 / 外部执行的测试之前，由 Human Gate（人工门控）批准。

测试 Evidence（证据）必须能够让科学判断：

- retain（保留）；
- revise（修正）；
- reject（拒绝）。

并能够修改：

- Principle（原理）；
- assumption（假设）；
- applicability boundary（适用边界）；
- Source–Target mapping（源—目标映射）；
- target operationalization（目标操作化）；
- Rival RCA（竞争根因）；
- Root Cause（根因）；
- 必要时 Necessity / residual envelope（必要性 / 残余范围）。

阴性结果只有在：

1. operationalization（操作化）忠实；
2. test（测试）有足够判别力；
3. activation condition（生效条件）成立；

时，才能真正削弱 Principle（原理）。

Method Design（方法设计）不是单向流水线。

---

# 21. Step 14 — Assumption–Constraint Collision（假设—约束冲突）

Selected Principle（选定原理）迁入 Target（目标域）以后，必须检查：

> **Source Assumption（源假设）**
> **× Target Constraint（目标约束）**
> **→ Observable Consequence（可观察后果）**
> **→ Required Repair / Claim Restriction（必要修复 / 声明限制）。**

至少考虑：

- observability（可观测性）；
- dynamics（动力学）；
- geometry（几何）；
- interaction（交互）；
- feedback（反馈）；
- partial information（部分信息）；
- embodiment（具身约束）；
- real-time（实时性）；
- data / measurement（数据 / 测量）；
- optimization solvability（优化可解性）；
- safety / physics（安全 / 物理）；
- closed-loop requirement（闭环要求）。

所有真实 Collision（冲突）必须闭合。

没有真实 Collision（冲突）：

> **不要制造改造。**

---

# 22. Step 15 — Minimal Faithful Target Realization（最小忠实目标域实现）

先问：

> **“怎样用最小 Target-Specific Structure（目标域特定结构），让 Selected Principle（选定原理）真实执行 Required Intervention（所需干预）？”**

要求：

- 保留 Source（源机制）真正起作用的 intervention（干预）；
- 去掉只服务 Source Task（源任务）的具体实现；
- 只加入 Target（目标域）真正必要的结构；
- 不为了总性能提前堆模块。

---

# 23. Step 16 — Principle-Only Closure → Residual MUST（纯原理闭合 → 残余必要条件）

Selected Principle（选定原理）先独立闭合。

只有仍存在真实 Residual MUST（残余必要条件），才允许加入额外 support mechanism（辅助机制）。

Residual MUST 必须：

- 真实；
- 有独立 Evidence（证据）；
- 不解决会破坏核心 claim / causal effect / feasibility（声明 / 因果作用 / 可行性）；
- 不能由 dominant principle（主导原理）自身合理解决。

每个新增模块必须对应唯一 causal parent（因果父节点）：

1. Primary Root Cause（主要根因）；
2. Target Constraint（目标约束）；
3. Earlier Design 引入的新 Incompatibility（早期设计引入的新不兼容）。

禁止 Method Soup（方法拼盘）。

---

# 24. Step 17 — Causal Repair DAG（因果修复有向无环图）

Final Method（最终方法）不能表示为：

> **A + B + C + D**

而必须能够写成：

> **Primary Root Cause（主要根因）**
> **→ Core Intervention（核心干预）**
> **→ Target Incompatibility（目标不兼容）**
> **→ Repair（修复）**
> **→ New Bottleneck（新瓶颈）**
> **→ Repair（修复）**
> **→ …**

每个模块都要有 causal parent（因果父节点）。

每条关键 causal edge（因果边）都应该能够验证。

Final Method（最终方法）应是一条：

> **Minimal Causal Repair Program（最小因果修复程序）。**

---

# 25. Step 18 — Mechanism Delta（机制增量）

Method Seed（方法种子）必须明确写成：

> **Existing Mechanism / Relation（现有机制 / 关系）**
> **→ New Mechanism / Relation（新机制 / 关系）。**

不能只写：

> “结合 A、B、C，提高 robustness / adaptability（鲁棒性 / 适应性）。”

最终必须满足：

> **Target Required Change（目标所需改变）**
> **= Source Intervention 真正改变的变量**
> **= Final Method 实际改变的变量。**

---

# 26. Scientific Delta（科学增量）与 Contribution-Type Separation（贡献类型分离）

Scientific Delta（科学增量）与 Performance Gain（性能提升）、Feasibility（可行性）、Empirical Evidence Strength（实验证据强度）必须分轨判断。

核心问题：

> **“相对于 nearest prior（最近邻已有工作），这个 Method（方法）对目标问题新增了什么可验证、可归因的科学内容？”**

以下不能单独作为 Scientific Delta（科学增量）：

- performance（性能）更高；
- 新数据集有效；
- 多模块组合；
- 热门 primitive（基础技术）；
- 代码更多；
- 只换领域或换名称；
- engineering convenience（工程便利）。

> **Performance Gain ≠ Scientific Delta**
> **性能提升 ≠ 科学增量。**

但必须同时明确：

> **Source primitive 已知 ≠ Target innovation 弱。**

如果已知 Source Mechanism（源机制）第一次在目标领域正确 causal position（因果位置）上实现此前不存在的 intervention（干预），解决真实未解 Root Cause（根因），并产生清晰 Mechanism / Scientific Delta，那么方法迁移本身可以构成强创新。

Scientific Delta 分三层：

- **Provisional Scientific Delta（初步科学增量）**：Candidate Principle（候选原理）阶段提出；
- **Final Scientific Delta Claim（最终科学增量声明）**：Final Method（最终方法）形成并完成 Novelty / Mechanism / Feasibility / Counterfactual closure 后冻结，表示“如果当前 causal story 成立，这个方法新增了什么”；
- **Established Scientific Delta（已建立科学增量）**：只能由 Full Causal Validation（完整因果验证）实际支持的 Final Scientific Delta Claim elements（最终科学增量声明要素）产生。

必须把以下五类贡献分开判断，不能互相替代：

1. **Scientific Insight Novelty（科学洞见新颖性）**：是否发现了新的机制、因果关系、边界或解释；
2. **Target Intervention Novelty（目标域干预新颖性）**：目标领域是否首次实现该 causal intervention；
3. **Method Seed Strength（方法种子强度）**：Method 是否形成足够强、必要、可验证的机制改变；
4. **Empirical Evidence Strength（实验证据强度）**：已有 Evidence 对 claim 的支持程度；
5. **Feasibility / Deployment Readiness（可行性 / 部署成熟度）**：方法是否已达到相应实现与部署成熟度。

顶刊论文可以因 Scientific Insight / Evidence 很强而成立，但不自动意味着存在新的 Strong Method Seed；反过来，一个 Strong Method Seed 也可以在尚未 deployment-ready 时具有顶刊潜力，只要未闭合问题被明确限制在 claim 之外或有可信验证路径。

科研 framing / positioning（贡献定位 / 表述）应准确突出真实 Problem、Mechanism Delta 和 Scientific Delta；它可以决定贡献是否被清楚理解，但不能制造不存在的创新。

# 27. Final Target-Intervention Novelty Closure（最终目标域干预新颖性闭合）

Candidate（候选）阶段的新颖性检查不是最终结论。

Final Method Kernel（最终方法内核）形成后，要重新比较：

> **nearest target prior（目标域最近邻已有工作）**
> **vs.**
> **proposed final mechanism（提出的最终机制）。**

最终确认新的：

- causal relation（因果关系）；
- intervention（干预）；
- guarantee（保证）；
- interface（接口）；
- regime（适用区间）

是否真正未被已有工作覆盖。

---

# 28. Natural-Derivation Test（自然推导测试）

删除全部 Source Story（源领域故事）。

只保留：

> **Target Failure（目标失败）**
> **→ Target Root Cause（目标根因）**
> **→ Required Intervention（所需干预）**
> **→ Target Constraints（目标约束）**
> **→ Final Method（最终方法）。**

如果仍然能够自然、必要、简洁地推出 Final Method（最终方法），迁移才真正完成。

这是最终迁移合法性的核心检查之一。

---

# 29. Claim-Proportional Feasibility（与声明匹配的可行性）

Feasibility（可行性）不是笼统 yes / no（是 / 否）。

必须根据具体 Claim（声明）检查：

- observability / estimability（可观测性 / 可估计性）；
- estimation error（估计误差）；
- optimization solvability（优化可解性）；
- compute（计算）；
- real-time（实时性）；
- closed-loop（闭环）；
- stability（稳定性）；
- safety / physics（安全 / 物理）；
- data（数据）；
- hardware（硬件）；
- verification path（验证路径）。

允许：

> **Strong Research Seed（强研究种子） + Explicit Unresolved Debt（明确未闭合问题）。**

不允许把未解决问题包装成已经 deployment-ready / theoretically guaranteed（可部署 / 有理论保证）。

---

# 30. Counterfactual Necessity Package（反事实必要性包）

在大规模 benchmark（基准实验）之前，必须能验证主要 causal edges（因果边）。

可包括：

- strongest baseline（最强基线）；
- Simple Repair（简单修复）；
- old mechanism without required change（没有所需改变的旧机制）；
- naive Source transfer（朴素源迁移）；
- wrong target representation（错误目标表示）；
- no-repair variant（无修复变体）；
- nearest equivalent prior（最近等价已有工作）；
- Rival RCA / Rival Principle（竞争根因 / 竞争原理）。

目标不是：

> “去掉模块以后分数下降。”

而是证明：

> **“为什么旧机制补不上？”**

和：

> **“为什么这个 Intervention（干预）在正确 Causal Position（因果位置）上补上了？”**

---

# 31. Top-Venue Method Strength Gate（顶会顶刊方法强度门）

必须区分：

> **Valid Method Seed（有效方法种子） ≠ Top-Venue Strong Method Seed（顶会顶刊级强方法种子）。**

顶会顶刊级 Strong Method Seed 至少同时满足：

### A. Problem Value（问题价值）

真实 Active Bottleneck（激活瓶颈）重要，不是人为制造的小问题。

### B. Necessity（必要性）

Simple Repair（简单修复）无法覆盖目标 Failure Envelope（失败范围），新机制确实有必要。

### C. Target Intervention Novelty（目标域干预新颖性）

目标域不存在等价 causal intervention（因果干预）。

### D. Mechanism Strength（机制强度）

能够明确写成 `Existing Mechanism → New Mechanism（现有机制 → 新机制）`，改变的是关键 causal/computational relation（因果 / 计算关系）。

### E. Final Scientific Delta Claim（最终科学增量声明）

相对 nearest prior（最近邻已有工作）存在具体、可验证、可归因的新科学内容，并明确哪些 claim elements 必须由后续 Full Causal Validation 建立。

### F. Causal Coherence（因果一致性）

Required Structural Change（所需结构改变）、Source Intervention（源干预）和 Final Computational Change（最终计算改变）一致；Final Method 是最小 Causal Repair DAG（因果修复有向无环图）。

### G. Natural Derivation（自然推导）

删除 Source Story（源故事）后仍然能从 Target Root Cause（目标根因）自然推出。

### H. Feasibility（可行性）

Claim（声明）范围内不存在破坏核心 Seed（种子）的致命可行性问题。

### I. Discriminative Validation（判别性验证）

存在能验证关键 causal edge（因果边）、区分旧机制、naive transfer（朴素迁移）、错误 mapping（映射）和 proposed mechanism（提出机制）的低成本实验 / 理论测试。

任何一项都不能由：

> 算法名、能力形容词、venue（期刊会议等级）、模块数量、总性能

代替。

---

# 31.1 Full Causal Validation（完整因果验证）与 Established Scientific Delta（已建立科学增量）

Top-Venue Method Strength Gate（顶会顶刊方法强度门）通过意味着：当前设计已经形成一个具有顶会顶刊潜力的 Strong Method Seed（强方法种子），以及一组明确的 Final Scientific Delta Claim（最终科学增量声明）。它仍不等于这些科学声明已经被最终建立。

Full Causal Validation（完整因果验证）必须验证的不只是总性能，而是完整 causal story（因果故事）：

> **predicted mechanism change（预测机制改变）**
> **→ observed mechanism change（观察到的机制改变）**
> **→ discriminating evidence（判别性证据）**
> **→ performance / capability consequence（性能 / 能力后果）。**

至少覆盖仍属于 Final Claim（最终声明）的：

- Required Mechanism Changes（所需机制改变）；
- Required Capabilities / Design Obligations（所需能力 / 设计义务）；
- Causal Repair DAG（因果修复 DAG）的关键 edge（边）；
- fatal assumptions / activation conditions（致命假设 / 生效条件）；
- discriminating predictions（判别预测）；
- unresolved feasibility obligations（未闭合可行性义务）；
- Counterfactual Necessity obligations（反事实必要性义务）；
- Final Scientific Delta Claim elements（最终科学增量声明要素）。

只有被 Full Causal Validation 实际支持的 claim elements，才能进入：

> **Established Scientific Delta（已建立科学增量）。**

如果验证推翻 Necessity（必要性）、RCA（根因）、Principle（原理）或 Method causal edge（方法因果边），必须返回对应上游阶段，不得用总体 benchmark 分数掩盖 causal failure（因果失败）。

---

# 32. 普通 Application（应用）、Method Soup（方法拼盘）和 Strong Method Seed（强方法种子）的分界

### 普通迁移 / Application（应用）

普通 Application 的关键不是“Source Primitive 是否直接使用”，而是目标域没有形成新的强 causal/mechanism contribution（因果 / 机制贡献）。典型表现：

- Failure（失败）主要停留任务级，缺少重要机制瓶颈；
- Source Primitive（源基础技术）虽然被迁入，但目标域已有相同 / 等价 causal intervention，或没有形成新的关键 intervention；
- Novelty（新颖性）主要依赖算法名、应用场景或包装差异；
- 核心 causal relation（因果关系）没有实质新变化；
- Scientific / Mechanism Delta（科学 / 机制增量）弱。

> **直接迁移本身不构成 Application 的判据。**
> 如果没有真实 Target Collision（目标冲突），无需为了“非平凡改造”增加结构；只要 Target Intervention Novelty、Mechanism Delta、Scientific Delta 和 Natural Derivation 成立，直接或少改造迁移仍可形成 Strong Method Seed。

### Method Soup（方法拼盘）

- Failure / RCA（失败 / 根因分析）模糊或事后编造；
- 多个能力模块平铺；
- 用组合数量代替创新；
- Source / Target incompatibility（源 / 目标不兼容）不显式；
- 有 orphan / redundancy（孤立 / 重复模块）；
- feasibility debt（可行性债务）隐藏；
- 论文故事强于 causal chain（因果链）。

### Strong Method Seed（强方法种子）

- Failure（失败）真实且通过 Necessity（必要性）检查；
- Required Intervention（所需干预）清楚；
- Source / Principle（源机制 / 原理）精确改变 required variable（所需变量）；
- Target Equivalent Intervention（目标域等价干预）未覆盖；
- Target Adaptation（目标域改造）只由真实 Collision / Residual MUST（冲突 / 残余必要条件）驱动；
- Method（方法）是 Minimal Causal Repair DAG（最小因果修复有向无环图）；
- Mechanism Delta（机制增量）明确；
- Natural Derivation（自然推导）成立；
- Final Scientific Delta Claim（最终科学增量声明）独立于 Performance（性能）成立；
- Claim-Proportional Feasibility（与声明匹配的可行性）闭合；
- 有能验证 causal edges（因果边）的 Counterfactual / Killer Tests（反事实 / 关键测试）。

# 33. 回退原则

Method Design（方法设计）不是单向流水线。

必须允许：

- Test（测试）问题 → 重做 Test；
- Operationalization（操作化）问题 → 重做 Mapping（映射）；
- Source（源机制）不匹配 → 换 Source；
- Principle（原理）不成立 → 换 Principle；
- Required Intervention（所需干预）错误 → 返回 RCA；
- Necessity / Residual Envelope（必要性 / 残余范围）错误 → 返回 Necessity；
- Root Cause（根因）前提不足 → Reopen RCA（重新打开根因分析）；
- Problem Identity / Premise（问题身份 / 前提）改变 → 重新定义 Problem（问题）。

核心原则：

> **不能因为已经写出了漂亮 Method（方法），就拒绝科学回退。**

C-K（概念—知识）与 Strong Inference（强推断）在本流程中的有效要求分别是：

- Knowledge（知识）变化可以推动 Concept / Principle（概念 / 原理）变化，并允许回退上游；
- 保留 Rival Hypothesis（竞争假设），用 Discriminating Experiment（判别实验）主动排除错误解释。

不需要再做独立平行模块。

---

# 34. NO-GO（终止）的科学标准

> **“没有找到 Solution（解决方案）” ≠ “已经证明不存在 Solution（解决方案）”。**

因此：

- cross-domain（跨领域）没有找到可信 Source；
- 当前四类 Search Space（搜索空间）暂时没有找到可信 Principle；

都不能自动得到 NO-GO（终止）。

Terminal NO-GO（终止）只应在：

> **有 Evidence（证据）证明核心科学前提 / 可行性无法成立，并且合理的回退、claim restriction（声明限制）、重新选 Source / Principle（源机制 / 原理）等 Recovery（恢复路径）均已被排除**

时成立。

---

# 35. 最终核心公式

当前 RCA-Transfer（根因分析—迁移）路径可以压缩为：

> **真实且重要的 Active Failure（真实激活失败）**
> **→ Mechanism-Level Root Cause（机制级根因）**
> **→ Required Structural Intervention（所需结构干预）**
> **→ Four-Space Principle Search（四空间原理搜索）**
> **→ Strong Solution Principle（强解决原理；可来自 First-Principles / Representation / Same-Field / Cross-Domain）**
> **→ Target Intervention Novelty（目标域干预新颖性）**
> **→ Collision-Driven Necessary Adaptation（冲突驱动必要改造，如有真实冲突）**
> **→ Minimal Causal Repair DAG（最小因果修复有向无环图）**
> **→ Clear Mechanism Delta（明确机制增量）**
> **→ Natural Derivation（自然推导）**
> **→ Claim-Proportional Feasibility（与声明匹配的可行性）**
> **→ Discriminative Counterfactual Evidence（判别性反事实证据）**
> **→ Final Scientific Delta Claim（最终科学增量声明）**
> **→ Top-Venue Strong Method Seed（顶会顶刊级强方法种子）**
> **→ Full Causal Validation（完整因果验证）**
> **→ Established Scientific Delta（已建立科学增量）。**

对于 Cross-Domain / Source-derived branch，还必须插入：

> **Target Mechanism Signature → Domain Discovery → Terminology Grounding → Source Mechanism / Genealogy / Causal Efficacy → Intervention-Level Alignment → Solution Principle。**

---

# 36. Phase II：转化成 Harness（科研流程执行框架）的硬要求

每一个科研规则必须最终明确：

1. **Input（输入）**
   需要什么上游 Artifact / Evidence（产物 / 证据）。
2. **Cognitive Operation（认知操作）**
   Agent（智能体）真正执行什么科研操作，而不是“思考一下”。
3. **Required Evidence（所需证据）**
   哪些判断不能只靠 Agent 自己声称成立。
4. **PASS（通过）**
   明确什么条件代表科研上通过。
5. **FAIL（失败）**
   能够真正拒绝弱 Problem / RCA / Principle / Method（问题 / 根因 / 原理 / 方法）。
6. **Recovery（恢复 / 回退）**
   失败后究竟返回哪里、补什么证据、换什么机制或是否终止。

并且科研 reasoning（推理）必须进入真实 execution lifecycle（执行生命周期）：

> **Input（输入）**
> **→ Execution（执行）**
> **→ Result（结果）**
> **→ Consumption（消费）**
> **→ Evidence Feedback（证据反馈）**
> **→ Reviewer / Human Decision（审查器 / 人工决策）**
> **→ Loop / Recovery / Convergence（循环 / 回退 / 收敛）**
> **→ Downstream Handoff（下游交接）。**

不能只存在于 Prompt（提示词）、Skill（技能）、Schema（结构）或 Artifact Name（产物名称）里。

最终必须做到：

> **Agent 可执行**
> **→ Reviewer 可判断**
> **→ Validator 可检查**
> **→ Gate 可阻断**
> **→ 失败可回退。**

---

# 37. 后续任何 Harness 修改最不能弱化的核心

后续接手者不要重新发散科研方法论，优先把上述已经确认的科研真值忠实转成 Harness。最不能弱化的是以下七点：

1. **Problem-first：**先证明真实 Failure、Necessity 和 Mechanism-Level RCA，再允许设计机制；不能从热门算法倒推 Root Cause。
2. **RMC-first Search：**Source / Principle Search 寻找“谁已经成功改变过这个必须改变的变量”，不是“谁的任务看起来像我”。
3. **Cross-domain search 必须执行，但 adoption 不强制：**跨领域机制发现是当前 RCA-Transfer 路径的核心创新策略；最终应选择最合理的 Principle，不为模板制造虚假 Source。
4. **Innovation 不等于新 primitive 或大量改造：**已知 Source Mechanism 通过新的 Target causal intervention 解决真实未解 Root Cause，可以形成顶会顶刊级强创新；Target Constraints 只驱动真实必要改造。
5. **Method 必须自然且最小：**Target Required Change、Source / Principle Intervention、Final Method Actual Change 必须一致；Final Method 是 Minimal Causal Repair Program，不是 Method Soup。
6. **Novelty / Scientific Delta 看因果贡献：**Novelty 检查 Target-Domain Equivalent Causal Intervention，不看算法名；Performance Gain 不能代替 Scientific Delta；贡献 framing 只能准确表达真实创新，不能制造创新。
7. **证据必须能推翻设计：**Killer Test、Counterfactual、Full Causal Validation 必须能够让 Principle、RCA、Necessity 或 Method 真正回退；只有验证支持的 Final Scientific Delta Claim 才能成为 Established Scientific Delta。

最高层仍然只回答三个问题：

> **为什么想到这个机制？为什么逻辑上应该采用 / 迁移它？为什么经过目标域约束后会自然形成这个新的强方法？**

最终不是：

> **“检查一个 idea（想法）是否像顶刊。”**

而是：

> **让 Auto Research（自动科研）真正学会：顶刊级创新 Method（方法）如何从真实 Root Cause（根因）出发，通过发现、选择、验证、迁移 / 重构并最小化实现一个强机制自然生长出来，以及每一步如何判断做对了。**
