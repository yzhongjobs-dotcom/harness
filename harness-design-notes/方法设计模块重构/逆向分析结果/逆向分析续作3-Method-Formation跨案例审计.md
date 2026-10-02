# Method Formation 逆向分析续作（第三轮）：从真实失败到 Strong Method Seed

日期：2026-08-29  
研究范围：`user-batch` 与 `user-batch-v2` 中的阻抗控制顶会、顶刊及高水平论文  
用途：为 ARIS/Harness 的 Method Design 提供科研逻辑与判定标准；本轮不修改 Harness

## 0. 本轮结论先行

本轮新增案例总体支持“真实失败 → 机制级 RCA → Required Intervention → Source Mechanism → Target Transformation → Strong Method Seed”这条形成路径，但同时给出三个重要修正。

第一，这不是顶级方法形成的唯一模式。稳定状态依赖 VIC 更接近 **representation/formal-construction first**；接触转换稳定性属于 **failure diagnosis + certificate**；刚度推断属于 **measurement/identifiability first**；混合逆动力学属于 **system-identification co-design**。因此，Root-Cause Transfer 应成为一个 formation-mode 分支，而不是所有论文的统一模板。

第二，真正应当成为硬门槛的不是“必须进行足够非平凡的跨域改造”，而是：

> 若 Source Mechanism 的成立假设与 Target Constraints 相冲突，则这些冲突必须被逐一闭合；若没有冲突，直接迁移本身不应被人为判弱，但仍必须通过目标干预新颖性、自然推导和可行性审查。

第三，顶刊论文的科学贡献强，不等于它一定提供了新的 Method Seed。非对称阻抗矩阵论文的主要价值是机制辨析、受控比较与适用边界；其作者此前已经学习过完整非对称矩阵。因此，“论文被顶级 venue 接收”不能作为“目标干预新颖”的替代证据。

由本轮案例得到的最关键判据是：

> Strong Method Seed 不是一个新名词或 A+B+C 组合，而是一条最小、可检验的 causal repair program：每个模块都有 causal parent；核心前后关系能写成 `Existing Mechanism → New Mechanism`；目标失败要求改变的变量、Source 实际能改变的变量、最终方法真实改变的变量三者一致；所有新增冲突与可行性债务在进入大规模实验前已有闭合路径。

## 1. 研究方法、证据边界与案例选择

### 1.1 继承而非重启

本轮首先继承了已有 handoff、前两轮逆向分析、Method Design 合同、Root Cause Analysis 文档和 gap audit。已有结论被视为待检验假设，而不是既定真理。重点新增：

- 从原文 Related Work、公式、引用和作者前作恢复 genealogy；
- 主动选择成功、边界、失败和非适用案例；
- 区分 paper story、可重建的 formation logic 与真实历史 genesis；
- 用 naive variant、ablation、简单修补和既有等价干预作为 counterfactual。

### 1.2 认识论标签

全文使用三种证据强度：

- **E1：原文显式证据**——论文明确陈述来源、失败、假设、限制或扩展关系；
- **E2：结构性重建**——从公式、引用谱系、模块依赖和对照实验可以可靠恢复；
- **E3：历史猜测**——关于作者当时怎样想到方法的推断。本报告不把 E3 写成事实。

“formation logic”在本文中只表示论文可以被重建出的因果设计逻辑，不声称等同于作者真实构思历史。

### 1.3 高信息量案例与饱和

本轮没有平均分析全部 70 篇材料，而是选择能改变规则的案例。主要样本如下。

| 案例 | 主要角色 | Formation mode | 对规则的净信息 |
|---|---|---|---|
| Accuracy/Robustness Dilemma | 强成功 | RCA + 双 Source Mechanism | Source intervention 与目标变量精确对齐；repair DAG 清晰 |
| Complementary Stability & Loop Shaping | 强成功 | RCA + robust-control transfer | Source/Target 表面问题不同，但结构变量一致 |
| Risk-Sensitive Impedance | 强种子、可行性未闭合 | RCA + stochastic-control transfer | naive uncertainty models 反而失败，证明 target transformation 必要 |
| Adaptive Energy-Bounding | 最干净的显式迁移 | haptics → industrial interaction | “改造量”应改写为 assumption-collision closure |
| Stable State-Dependent VIC / SNEUM | 强成功、非迁移主路径 | representation + certificate | 稳定性可以嵌入表示，而非事后过滤 |
| Composite Learning VIC | 强整合 | adaptive-control transfer/co-design | 多模块均有 causal parent，但证明依赖 IE、线性参数化 |
| Constrained VIC via QP | 中等强度 | reparameterization + constrained optimization | 明确 delta，但 passivity/stability closure 不足 |
| Passivity Filter | 合理但增量 | target-domain extension | 对齐正确且模块不孤立，仍可能因既有等价干预而创新有限 |
| Asymmetric Impedance Matrices | 重要纠偏 | mechanism/evidence first | 强科学证据不等于新 Method Seed |
| Diffusion-Based Impedance Learning | 强性能、闭合不完整 | representation bridge + control | 明确承认 stiffness restoration 不一般被动 |
| Segmentation + MOBO | 普通 application/composition | search-space design | 模块有用但更接近工程组合与应用 |
| Contact Transition Stability | 简单修补反例 | failure diagnosis + certificate | 有些真实失败可由阻尼区间等简单修补解决 |
| Perturbation-Based Stiffness Inference | 非适用对照 | measurement/identifiability first | 不能强行制造 Source Transfer 故事 |
| Hybrid Inverse Dynamics | 非适用对照 | system identification/co-design | 物理模型 + friction + residual，不是 RCA transfer 共性样本 |

新增样本对核心判断已出现重复支持，同时负例覆盖了直接照搬、目标干预已存在、简单修补、可行性未闭合和 formation-mode 不适用等关键边界，因此主要规则已经趋于饱和。饱和不代表穷尽文献，而表示继续加入同类成功论文不太可能改变下面的门槛结构。

## 2. 核心案例的机制级逆向

### 2.1 Accuracy/Robustness Dilemma：最完整的 causal repair DAG

论文：[Kang, Jin & Chang, 2009](https://doi.org/10.1109/TMECH.2008.2005524)

#### Failure 与 RCA

Dynamics-based impedance control 能在模型准确时精确实现目标阻抗，但模型误差直接进入闭环；position-based 结构借助内位置环提高鲁棒性，却把本应隐藏的内环动力学带入目标阻抗，导致阻抗失真，甚至影响接触保持。这不是“鲁棒性可能不够”，而是两类主流实现之间可观察的结构性两难。

RCA 不是“模型不准”这么宽泛，而是：**同一个补偿通道同时承担机器人动力学消除与目标阻抗塑形，模型残差因而直接污染目标端口关系；加入内环后，隐藏动力学又成为新的端口动态。** 增益 tuning 只能在精度与鲁棒性之间移动，不能移除这条污染路径。

#### Required Intervention

必须把目标阻抗本身置于一个能显式比较“期望端口动态与真实端口动态”的误差校正结构中，同时用不依赖完整动力学模型的机制补偿机器人未知动力学。也就是同时改变：

1. 目标阻抗如何进入闭环；
2. 未知机器人动力学如何被估计。

#### Source genealogy 与 Intervention Alignment

论文明确以两个 Source Mechanism 为基础：

- [Garcia 与 Morari 的 Internal Model Control](https://doi.org/10.1021/i200017a016) 最初用于过程控制，其干预是用内部模型和模型逆实现目标映射，并由模型—对象输出差校正失配；
- [Youcef-Toumi 与 Wu 的 Time-Delay Control/TDE](https://doi.org/10.1115/1.2896491) 用前一采样时刻的输入与加速度近似当前未知非线性动力学，避免完整模型计算。

来源核对还发现一个应由 citation-integrity gate 捕获的小问题：Kang 论文正文和参考文献把经典 IMC 论文作者写成 Economou 与 Morari，但原始题名和 DOI 记录对应 Garcia 与 Morari。本报告按原始记录使用 Garcia。这个细节不改变方法谱系，却说明 Agent 不能把目标论文参考文献当作无需核验的真值。

这里不是 Source Problem 与 Target Problem 相似，而是：

`IMC 的模型误差校正 + 目标模型注入` ↔ `目标阻抗不能再被机器人模型残差污染`；

`TDE 的短时未知动力学重构` ↔ `完整机器人动力学不可得但必须被补偿`。

#### Target Transformation 与 repair DAG

IMC 不能直接把机器人当普通 process 照搬。论文先识别 dynamics-based impedance control 本身具有 IMC-compatible 结构，再把“内部模型”设为期望阻抗动态，并把交互力从一般扰动中分离。随后：

`Primary dilemma`  
→ `IMC 注入期望阻抗并校正误差`  
→ `新不相容：IMC 仍需机器人模型`  
→ `TDE 替代完整模型`  
→ `新瓶颈：采样延迟、加速度估计、量化噪声`  
→ `递推形式、遗忘因子/低通处理与增益约束`。

这是 No-Orphan-Module 的正例：每个主要模块都能追溯到 primary RCA 或前一设计决定产生的新问题。

#### Mechanism Delta 与限制

`直接模型消除或位置内环隔离`  
→ `围绕目标阻抗的双自由度 IMC 误差校正 + 基于短时延信息的动力学补偿`。

其局限也很明确：零延迟完美抵消只是理想性质；实际效果受采样率、加速度估计、摩擦快速变化和滤波相位影响。该案例支持强 formation logic，但不证明所有复杂非平稳接触都能由 TDE 解决。

### 2.2 Complementary Stability：从 universal passivity 到 bounded-environment robust stability

论文：[Buerger & Hogan, 2007](https://doi.org/10.1109/TRO.2007.892229)

#### Failure、RCA 与 Required Intervention

被动机器人可与广泛的被动环境稳定耦合，但这种 universal guarantee 会严格限制可实现的低惯量、低阻尼和高带宽性能。传统 servo loop shaping 也不能直接回答交互稳定性，因为性能由机器人端口性质决定，而耦合稳定性取决于机器人与环境端口的乘积，控制器又非线性嵌入该关系。

RCA 是：**稳定保证的量词过强。** 系统为“所有被动环境”支付性能代价，而实际任务只需要面对一个有界的 intended environment class。

因此 Required Intervention 不是调低被动性裕量，而是把稳定条件从：

`robot is passive for every passive environment`

改为：

`robot is robustly stable for a bounded, task-relevant environment set`。

#### Source Mechanism 与 Target Transformation

Source Mechanism 是 robust control 中的小增益/结构奇异值思想和 loop-shaping 搜索。迁移成立不是因为“人与不确定系统很像”，而是 robust stability 正好能改变保证的量词与不确定集合。

目标域改造包括：建立人臂质量—阻尼—刚度集合；把机器人阻抗转为便于耦合分析的 admittance；将端口性能代价与耦合稳定约束分离；在控制器族上搜索可行解。最终变化为：

`universal passive cone` → `task/environment-class robust-stability feasible set`。

该案例强力支持 Intervention-Level Alignment，同时说明“更强的理论保证”并不总是更好；与任务量词不匹配的保证本身可能是 active bottleneck。

局限是线性、SISO/低维、人臂集合正确性和控制器族覆盖。它保证设定集合内的 robust stability，不自动等于真实人机安全。

### 2.3 Risk-Sensitive Impedance：对齐正确仍会因 uncertainty representation 错误而失败

论文：[Hammoud, Khadiv & Righetti, 2021](https://doi.org/10.1109/LRA.2021.3068951)

#### Failure 与 Required Intervention

标准 DDP 的局部反馈偏向精确跟踪，遇到未预期早接触时高增益会产生大冲击甚至失稳；统一降低增益又损失任务精度。RCA 是反馈增益只由确定性名义轨迹和代价曲率决定，没有把“接触位置在哪里不确定”作为决定阻抗的计算变量。

因此必须把：

`deterministic local feedback gain`

改成：

`feedback gain conditioned on the distribution and geometry of contact uncertainty`。

#### Source genealogy 与目标域改造

论文明确继承 Jacobson 的指数型 risk-sensitive cost、Farshidian 的非线性迭代扩展，以及 [Pontón 等把 measurement uncertainty 通过 observer/EKF dynamics 增广进局部最优控制](https://arxiv.org/abs/1605.04344) 的工作。Pontón 的方法此前只在简单二维机械臂/接触任务上验证。

Source intervention 是让 uncertainty covariance 进入 value recursion 与 feedback gain，而非简单增加“风险惩罚项”。目标域不能直接照搬，必须处理：

- hard contact phase switching；
- 浮动基座与 SE(3) 局部误差；
- swing-foot 接触位置协方差到 whole-body state 的映射；
- 对 active-contact null space 的投影；
- 将局部反馈矩阵解释为接触前后的 stiffness/damping schedule。

#### 最干净的 counterfactual

论文中的 Risk-Uniform 和 Risk-SwingJoint 并没有因使用 risk-sensitive control 就成功；它们在意外撞击后甚至比 DDP 更差。只有把不确定性放在 swing-foot 接触位置，并按接触几何映射与投影的模型才能降低冲击并保持运动。

这证明：

> Source primitive 对齐只是必要条件；Target Representation 必须把 uncertainty 放到 RCA 指向的因果位置。错误的 uncertainty model 会使正确算法执行错误干预。

#### Method Strength 与 Feasibility

`gain from nominal tracking curvature` → `gain from nominal curvature + contact-structured measurement covariance`。

这是强 Method Seed，但 feasibility closure 尚未完成：论文是仿真验证，使用预定义接触序列与时序、Gaussian covariance、刚性接触优化和弹簧阻尼仿真，优化为局部解，且没有 hardware 或闭环稳定/安全定理。因此应判为“强、可研究的 seed”，而不是“可直接部署的方法”。

### 2.4 Adaptive Energy-Bounding：Nontrivial Transformation 应改写为 Collision Closure

论文：[Kim, Kim & Ryu, 2014](https://doi.org/10.1109/TMECH.2013.2276935)

#### 显式 Source genealogy

论文明确把作者此前用于 haptic virtual environments 的 [energy-bounding algorithm](https://doi.org/10.1177/0278364909338770) 迁移到 position-controlled industrial robot 与 real environment。Source mechanism 限制 sample-and-hold 产生的能量，使其不超过 haptic system 有效阻尼能够耗散的能量，并保证 virtual environment/controller 被动。

#### 为什么不能直接照搬

Source 与 Target 的关键冲突是：

| Source assumption | Target constraint | Required repair |
|---|---|---|
| torque-controlled、轻量、可回驱 haptic device | 高惯量、高减速比、封闭位置环工业机器人 | 先用 PBIC 把外部行为转成 impedance-like port |
| virtual environment | 储能未知的 real environment | 在被动性条件中加入真实环境能量项并修改 lemma |
| 固定 EBA 参数 | 环境刚度跨很大范围变化 | 在线估计/调节 `c2`，同时受离线识别的 plant dissipation bound `c1` 约束 |

最终机制是：

`fixed PBIC under assumed environment range`  
→ `force-update slope bounded by plant dissipation and measured real-contact energy, with online environment adaptation`。

#### 对规则的修正

该案例支持目标改造的重要性，但更精确的规律不是“迁移必须看起来非平凡”，而是：所有真实 collision 必须有 repair。若 Source assumptions 与 Target 已一致，强迫加入改造只会制造 method soup。

其 feasibility 边界也很清晰：`c1` 需在高刚度环境下离线保守识别；高估可能失稳，低估会牺牲性能；理论与实验主要是 1-DOF、被动环境。因此，它是强迁移逻辑，不是无条件通用方案。

### 2.5 SNEUM：强方法可以来自“把证书变成表示”，而非 Source Transfer

论文：[Jin et al., 2025](https://doi.org/10.1109/TMECH.2024.3466950)

#### Failure 与机制级 RCA

当 stiffness `K(e)` 随状态变化时，传统固定增益能量函数的导数出现与 `K̇` 有关的非受控能量注入项。energy tank 会在能量耗尽时扭曲期望阻抗；Kronander–Billard 的条件主要适合离线、时变 profile，并限制灵活性。

RCA 是：**稳定性与 stiffness representation 分离。** 任意网络先输出 `K(e)e`，再由外部 filter/tank 修补，稳定性自然变成事后约束。

#### Required Intervention 与 genealogy

必须把 variable elastic force 从任意矩阵乘积改写成一个有效势能的梯度，使表示本身携带稳定证书。论文基于作者 2023 年的 NEUM——“具有全局唯一最小值的神经能量函数”——而不是跨域迁移。Target transformation 是加入 sign symmetry、零点光滑性、正二次项和针对 VIC 的参数约束，形成 SNEUM，并推导 coupled/decoupled controller。

Mechanism Delta：

`arbitrary learned K(e)e + external stability repair`

→

`elastic force = ∂V(e)/∂e, where V is positive-definite, radially unbounded and has a unique minimum by construction`。

#### 对 formation 模型的意义

这是顶级 Method Design 的强例，但真实 formation mode 更接近 representation-first + formal generalization。它仍可用 Failure/RCA 解释“为什么必要”，却不应被强行包装成跨域 Source Mechanism 搜索。

其边界包括名义模型补偿、保守梯度场、主要依赖 position-error 的状态依赖，以及接触中的 passivity 不等于任意环境下任务收敛或安全。

### 2.6 Composite Learning VIC：parented modules 不等于无条件成立

论文：[Pan et al., 2024](https://doi.org/10.1109/LRA.2023.3327675)

该方法面向三个相互关联的 failure：未知机器人参数使目标阻抗不能精确实现；经典 adaptive control 的 persistent excitation 在交互任务中难满足；多工作模式切换可能不平滑或破坏 passivity。

其 repair DAG 是：

`parametric uncertainty`  
→ `composite parameter learning using instantaneous + stored filtered regressions`  
→ `PE burden`  
→ `interval excitation and stored informative interval`；

`robot/human/collaboration modes`  
→ `smooth weighting functions`；

`acceleration unavailable`  
→ `filtered regressors`；

`safe passive interaction`  
→ `Lyapunov/passivity-compatible control law`。

Source genealogy 包含作者早期 composite learning robot control。目标域创新不在“用了 adaptive control”，而在 exact parameter convergence、variable impedance、multi-mode transition 与 passivity 的共同闭合。

这是 No-Orphan 的正例，但也暴露必要边界：已知线性参数化、IE 发生、存储数据足够、权重函数满足条件。一个 Agent 不能把“在 IE 下收敛”压缩成“无需模型和激励即可自适应”。

## 3. 判别案例与反事实控制

### 3.1 Passivity Filter：对齐正确，但目标干预已存在

[Bednarczyk et al., 2020](https://doi.org/10.1109/IROS45743.2020.9340758) 直接建立在 Kronander–Billard 2016 的 VIC 稳定/被动条件上。已有条件能离线检查 profile，但不能在线把不合法 profile 改成合法 profile；论文将其变成 rate filter，并用新的时变 storage function 降低保守性。

其模块有清晰 causal parent，机制 delta 也明确：

`requested impedance profile` → `rate-filtered passive profile`。

但 target domain 已存在相同稳定条件、energy tank 和等价被动性干预，因此它是合理且有用的 target extension，不应仅因“filter + new storage function”就判为全新 causal intervention。这个案例证明：**No-Orphan、Alignment、Mechanism Delta 全部通过，仍不足以保证强 novelty。**

### 3.2 Asymmetric Matrices：顶刊贡献与 Method Seed 必须分轨

[Kozlovsky et al., 2022](https://doi.org/10.1109/LRA.2022.3191070) 的受控比较证明 asymmetric stiffness/damping 的 antisymmetric part 形成 curl field，能实现力/矩到横向位姿修正；相比 diagonal 和 symmetric matrix，插孔成功率更高，并显示近似 space-invariance。

但是原文 Related Work 明确指出：

- 目标领域已有预设 non-diagonal stiffness；
- 已有 risk-sensitive joint-space matrices 包含 asymmetric elements；
- 作者团队 2021 年的 residual admittance policy 已经显式学习 full asymmetric stiffness matrices。

因此本论文的真实强项是“非对称项究竟起什么作用”的机制证据、action-space restriction 和系统比较，而不是首次把 asymmetric causal intervention 引入目标域。对 Method Design，正确输出应是：

- **Scientific contribution：强**；
- **New Method Seed：弱到中等**；
- **Formation mode：mechanism/evidence first**。

### 3.3 Diffusion-Based Impedance：性能强，但 passivity debt 不能由叙事消失

[Geiger et al., 2026](https://doi.org/10.1109/TRO.2026.3717255) 用 wrench-conditioned Transformer diffusion 重建 simulated zero-force trajectory，再据此进行方向性 stiffness/damping adaptation。消融显示：无方向调节的 diffusion、仅基于 nominal ZFT 的方向调节、固定高/中/低阻抗均明显失败；完整方法在多种 peg geometry 上达到高成功率。这说明两个模块并非任意堆叠。

但论文也明确承认：降低 stiffness 会释放/耗散势能，恢复到 baseline stiffness 时若位移非零会注入能量，**一般不能保证 passivity**，需要再结合既有 passive impedance shaping。此外，训练和部署保持同一 baseline impedance；不同 baseline 的泛化尚未验证。

因此应判断为：

- causal parents：基本成立；
- mechanism delta：成立；
- empirical capability：强；
- feasibility closure：对“完整周期被动自适应”这一强主张不通过；
- recovery：加入 energy budget/tank/passivity filter，或把 claim 限定为实验范围内的性能方法。

该案例直接说明：顶刊实验性能不能替代 feasibility closure；反过来，存在一个明确可补的 feasibility debt 也不等于整篇论文“弱”。Gate 必须对 **seed strength、evidence strength、deployment readiness** 分开打分。

### 3.4 Constrained VIC via QP：把关键变量变成 decision variable 是实质 delta

[Jin et al., 2022](https://doi.org/10.1109/ICRA46639.2022.9812210) 观察到基于 tracking error 的优化会在碰撞时迅速提高 stiffness，从而产生大接触力；已有 VIC 很少把 impedance range 当作硬约束。其核心改造不是“用了 QP”，而是建立以 impedance-related parameters 为控制输入的预测模型，使 stiffness/damping bounds 可直接进入优化；为位置/速度约束另加 complementary force QP。

`impedance as tuned parameter outside optimizer` → `impedance parameter as constrained control decision`。

这是实质机制变化，但 feasibility 尚有限：解耦/低维建模、模型误差、complementary force 与期望阻抗关系、passivity/stability 都没有充分闭合。它应是中等强 Seed，而非因“QP 是成熟算法”被自动降为应用，也不能因“首次加 impedance constraint”被自动升为强方法。

### 3.5 Segmentation + MOBO：parented composition 仍可能只是普通 application

[Okada et al., 2023](https://doi.org/10.1109/IROS55552.2023.10342096) 用 impedance-aware switching linear dynamics 做任务分段和 stiffness prior，再用 multi-objective Bayesian optimization 搜索 task/compliance Pareto 解。每个模块都有用途：分段降低维度，prior 减少真实试验，MOBO 避免手工 scalarization。

但是形成逻辑主要是“把已有搜索工具高效应用到阶段化 stiffness tuning”，而不是改变接触系统的核心 causal relation。其限制包括阶段数/模型假设、每段常量 stiffness、真实交互成本和无稳定性保证。它是有效 application/composition，不应被 No-Orphan 误判为强 Method Seed。

### 3.6 Contact Transition Stability：强制 simple-patch falsifier

[Surdilovic, 1997](https://doi.org/10.1109/ROBOT.1997.620140) 区分接触后的 coupled stability 与进入接触瞬间的 transition stability：一个 in-contact equilibrium 稳定的控制器仍可能因单边接触、环境/目标刚度比、阻尼不足和延迟发生 rebound。

重要反例是，这类 failure 在给定模型范围内可由高目标阻尼和保守 small-gain bound 解决。它没有要求新架构。因而 Method Design 必须在 Source Mechanism 搜索之前执行：

> 若旧方法在合理参数、常规 estimator、已知约束或局部重写下即可闭合 failure，则不得把该 failure 升格为新方法必要性；应输出 tuning/certificate/baseline improvement，或寻找剩余未解决范围。

### 3.7 非适用路径：不要制造假的 transfer story

- [Perturbation-Based Stiffness Inference, 2022](https://doi.org/10.1109/LRA.2022.3187866)：核心是 identifiability 与主动测量；不确定性指导 informative perturbation，EMG/人类监督帮助消歧。真实 mode 是 measurement-first。
- [Hybrid Inverse Dynamics, RSS 2022](https://doi.org/10.15607/RSS.2022.XVIII.066)：物理一致 rigid-body term、显式摩擦与 residual LSTM 联合训练，服务低增益自由空间阻抗。真实 mode 是 system-identification co-design；其物理一致性不覆盖接触 passivity/stability。
- [Stability Considerations for VIC, 2016](https://doi.org/10.1109/TRO.2016.2593492)：由能量导数中的 `K̇` 项直接推出 sufficient matrix condition，属于 formal obstruction → certificate，而非 transfer。

这些案例要求 Method Design 在进入 RCA-transfer 模板前先路由 formation mode。

## 4. 原有 Method Design 假设逐项审计

| 原假设 | 本轮结论 | 修订后的规则 | 关键证据 |
|---|---|---|---|
| Active Root Cause | **支持，但限于本路径** | 对 Failure/RCA 路径是硬门；对 representation/formal/measurement-first 需使用对应入口 | Accuracy、Risk、Contact Transition；非适用对照 |
| Performance-limiting Bottleneck | **修正** | bottleneck 可是性能损失、能力缺失、保证量词过强、不可识别或不可实现；必须有现行证据 | Complementary Stability 的 universal guarantee；Perturbation 的 identifiability |
| Required-Intervention Extraction | **支持，硬门** | 必须在看到 final method 前写出变量及方向；写不出则 RCA 仍太粗 | Accuracy、Risk、SNEUM |
| Strong Source Mechanism | **修正** | Source 可来自外域、同域、作者前作、定理或表示；“强”指 intervention 可描述且有原域证据，不指来源 venue | IMC/TDE、risk-sensitive、NEUM、composite learning |
| Intervention-Level Alignment | **强支持，硬门** | 比较 `Source Intervention ↔ Target Required Change`，不比较 problem labels | Complementary Stability、Risk、Adaptive EBA |
| Target Intervention Novelty | **强支持，独立硬门** | 检索等价 causal intervention，而非同名算法；primitive 新颖与 target-method 新颖分开 | Asymmetric、Passivity Filter |
| Nontrivial Target Transformation | **降级并替换** | 不要求最低“改造量”；若有 assumption–constraint collision，必须闭合；无冲突时可直接迁移 | Adaptive EBA；Passivity Filter |
| Assumption–Constraint Collision | **强支持，迁移路径硬门** | 必须列 Source assumption、Target constraint、observable consequence、repair | Adaptive EBA、Risk |
| No-Orphan-Module | **支持为必要非充分条件** | orphan 直接拒绝；无 orphan 仍需 novelty、delta、minimality | Accuracy 正例；Segmentation+MOBO 反例 |
| Mechanism Delta | **强支持，硬门** | 必须写成可计算 before→after relation，禁止只有能力形容词 | 所有强案例；普通 application 反例 |
| Natural Derivation | **支持，硬门** | 删除 Source 故事后，final method 仍应从 Target failure/RCA/constraints 推出；只证明设计合理，不证明历史 genesis | Accuracy、Adaptive EBA、SNEUM |
| Feasibility Closure | **强支持，硬门但按 claim 分级** | observability、optimization、real-time、closed-loop、safety、data 与验证路径逐项闭合；可输出 strong seed + unresolved debt，但不得伪装为 ready method | Risk、Diffusion、QP |
| 简单修补可能性 | **新增为前置硬门** | 必须运行 tuning/estimator/constraint/local-rewrite falsifier | Contact Transition、Stable Execution |

## 5. 新增规则

### 5.1 Formation-Mode Router

在任何统一模板前，先判断主要创新压力来自哪里：

1. Failure/RCA + mechanism intervention；
2. Representation/certificate construction；
3. Formal obstruction/generalization；
4. Measurement/identifiability；
5. Capability complementarity/system co-design；
6. Infrastructure/evaluation；
7. Mechanism/evidence clarification。

只有第 1 类强制执行完整 Source Mechanism transfer 链；其他类型仍要说明必要性、delta、novelty 与 feasibility，但不制造假的 Source Problem。

### 5.2 Simple-Repair Falsifier

在宣称“必须新方法”前，至少测试或严谨排除：

- 合理 tuning/增益调度；
- 标准滤波、估计器或观测器；
- 已知 constraint/certificate；
- 增加模型容量/数据但不改变计算关系；
- 局部 reparameterization；
- 更强的现有 baseline 或其公平组合。

若简单修补覆盖目标 operating envelope，则新方法必要性 FAIL。若只覆盖子域，应把剩余 failure envelope 写清楚，而不是忽略修补。

### 5.3 Causal Repair DAG

最终方法不再用平面模块列表表示，而用有向图：

`Primary Root Cause → Core Intervention → Incompatibility_i → Repair_i → New Bottleneck_j → Repair_j`

每个模块只允许有三类 parent：primary RCA、target constraint、上一步决策产生的不相容。无 parent 是 Orphan；多个模块共同修同一变量但没有可区分作用，是 redundancy/soup risk。

### 5.4 Counterfactual Necessity Package

普通性能 ablation 不足以证明形成逻辑。每个核心结构至少需要一种更干净的 counterfactual：

- 不改变 required variable 的旧机制；
- 使用 Source primitive 但不做 target transformation；
- transformation 错位的 naive variant；
- 去掉某一 repair 后暴露其对应 incompatibility；
- 简单修补 baseline；
- 最近邻等价干预。

Risk-Uniform/Risk-SwingJoint 和 Diffusion 的 nominal-ZFT/uniform variants 就比“去掉模块后性能下降”提供了更强的因果证据。

### 5.5 Contribution-Type Separation

Method Design 输出必须分开：

- **Scientific insight novelty**；
- **Target intervention novelty**；
- **Method seed strength**；
- **empirical evidence strength**；
- **feasibility/deployment readiness**。

Asymmetric matrices 可在第一、第四项很强，却不必在第二、第三项同样强；Risk-sensitive seed 在第二、第三项强，却在第五项尚未闭合。

### 5.6 Claim-Proportional Feasibility

Feasibility 不是单个 yes/no。先写 claim，再审查支撑它所需的 closure：

- 若只声称“仿真中产生合理 gain schedule”，Risk 论文可以通过；
- 若声称“真实机器人稳定安全执行”，同一证据不通过；
- 若 Diffusion 只声称实验范围内成功，可通过；若声称 stiffness 全周期变化仍严格 passive，则不通过。

## 6. 从真实失败到 Strong Method Seed 的实际科研流程

下面是可直接实现为 Agent、Reviewer、Validator 和 Gate 的流程。`PASS` 表示允许进入下一步；`FAIL` 必须回退，不得用文字润色掩盖。

| Research Step | Input | Cognitive Operation | Required Evidence | PASS | FAIL | Recovery |
|---|---|---|---|---|---|---|
| 0. Formation-mode routing | problem observations、已有工作、目标贡献 | 判断创新压力来自 failure、representation、formal、measurement 还是 system co-design | 至少两个候选 mode 及排除理由 | 主 mode 与证据匹配 | 为套模板而虚构 Source/RCA | 切换对应 pipeline；保留通用 novelty/feasibility gates |
| 1. Failure activation | 失败日志、论文、实验、用户需求 | 写成 `condition → observable failure → consequence` | 真实场景、频率/幅度、性能或能力限制 | 可复现或有多源一致证据 | 只有“可能不鲁棒/不智能” | 补采 failure evidence；停止方法生成 |
| 2. Operating-envelope definition | failure + task constraints | 定义方法必须覆盖与不必覆盖的范围 | dynamics、contact、noise、hardware、safety 边界 | failure 在目标 envelope 内重要 | 通过任意极端条件制造问题 | 缩小/重写 claim |
| 3. Simple-repair falsifier | strongest baseline + envelope | 尝试 tuning、标准估计、已知约束、局部修补和公平组合 | 修补后的 counterfactual 结果或理论排除 | failure 仍存在且原因未变 | 简单修补已覆盖 envelope | 输出 baseline improvement；寻找剩余 failure |
| 4. Mechanism-level RCA | activated failure + system model | 定位引起 failure 的状态、信息路径、表示、约束、量词或决策关系 | causal chain；至少一个可证伪 rival RCA | 能解释何时发生/不发生并区分 rival | 原因只是“复杂、数据少、模型差” | 做诊断实验、敏感性/消融、形式分析 |
| 5. Required-intervention extraction | RCA，不看 final method | 写 `variable/relation X must change from A to B` | 与 failure consequence 的推导 | 变量、方向、作用位置明确 | 直接跳到算法名或模块列表 | 返回 RCA，直到能提出结构变化 |
| 6. Source-mechanism search | required intervention | 跨名称/领域检索能执行该 structural change 的 operator/mechanism | 原始 Source paper、公式、有效性证据、成立假设 | Source 实际改变同一变量 | 只因问题/术语相似 | 换机制；扩大 genealogy search |
| 7. Intervention alignment | Target required change + Source intervention | 比较变量、方向、作用层级、时间尺度与量词 | alignment table + mismatch list | 关键变量一致，mismatch 可修 | Source 只提供泛化能力形容词 | 拒绝迁移或重做 RCA |
| 8. Target-intervention novelty | candidate intervention + nearest priors | 检索目标域中同名与异名等价 causal intervention | 最近邻 before→after delta；作者前作；引用/专利谱系 | 等价干预未覆盖，或新适用域改变了实质关系 | primitive 新但 target intervention 已存在 | 降级为 application/evidence；寻找新 delta |
| 9. Assumption–constraint collision | Source assumptions + target reality | 逐项检查 observability、dynamics、geometry、feedback、real-time、data、safety | collision ledger | 每个真实冲突都有 repair 或被限定出 claim | 用“domain adaptation”一词代替具体冲突 | 构造必要 transformation；否则拒绝 |
| 10. Causal repair DAG | core intervention + repairs | 追踪每个设计决策产生的新 incompatibility | parent mapping；无环依赖；模块最小性 | 每个核心模块有 parent 且作用不可替代 | orphan、重复模块、目的只写“增强鲁棒性” | 删除、合并，或补出可验证 parent |
| 11. Mechanism-delta freeze | repair DAG + nearest prior | 固化最小技术 kernel | `Existing relation → New relation`；方程/伪代码；输入输出 | reviewer 可指出具体改变的计算关系 | “结合 A+B+C 提升性能” | 回到 5/8/10，缩小到单一核心 delta |
| 12. Natural-derivation test | target-only story | 删除 Source-domain 叙事，重新从 failure 推导 final method | target-only derivation + alternative comparison | 方法仍显得必要、简洁 | 只有讲 Source 故事才合理 | 拒绝 opportunistic transfer；重新设计 |
| 13. Feasibility closure | frozen kernel + target constraints | 审查可观测性、估计误差、可解性、计算、实时、闭环、安全、数据、验证 | feasibility ledger；debt owner；kill test | 无致命障碍，未闭合项有低成本验证路径 | 依赖不可测变量、不可解优化或无法验证的保证 | 加 estimator/relaxation/certificate；缩小 claim；终止 seed |
| 14. Counterfactual package | final seed | 设计能验证每条 causal edge 的最小实验 | naive transfer、wrong representation、no-repair、simple patch、nearest prior | 结果能区分“为什么有效” | 只有总分提升实验 | 重新设计实验；不得进大规模 benchmark |
| 15. Seed acceptance | 全部 artifacts | 综合 novelty、necessity、coherence、feasibility 与 evidence | 完整 Seed Contract | 全部硬门通过；soft debt 已标注 | 任一硬门被叙事替代 | 回退到对应步骤或明确 NO-GO |

## 7. Reviewer/Validator 可执行的拒绝规则

以下任一项应直接拒绝 Strong Method Seed 标签：

1. 失败没有 `condition → observable consequence`，只有抽象风险；
2. strongest baseline 或简单修补未测试；
3. RCA 不能推出明确 required variable；
4. Source Mechanism 只在问题故事或名字上相似；
5. 目标域已有等价 causal intervention，却只比较同名方法；
6. Source assumptions 与 target constraints 的冲突未列出；
7. final method 有无法追溯的核心模块；
8. delta 只能写成“A+B+C improves robustness”；
9. 删除 Source 故事后方法不能从 target failure 推出；
10. 所需状态不可测且无可靠估计路径；
11. 优化/推理在目标周期内不可解，或闭环/安全 claim 无对应证据；
12. 大规模实验只能证明总性能，不能验证 causal repair edges。

以下特征通常区分三类产出：

| 类型 | Failure/RCA | Intervention | Novelty | Transformation | Modules | Feasibility |
|---|---|---|---|---|---|---|
| 普通迁移/application | 任务级描述 | Source primitive 直接套用 | 常只查同名 | 参数适配 | 可有 parent | 多为经验可跑 |
| method soup | 模糊或事后编造 | 多个能力模块并列 | 用组合数量代替 | 不相容未显式化 | 存在 orphan/重复 | 债务隐藏 |
| Strong Method Seed | 机制级且通过简单修补反证 | 精确改变 required variable | 查等价 causal intervention | 只做 collision 驱动的必要改造 | causal repair DAG、最小化 | claim-proportional closure + kill tests |

## 8. 建议的 Method Seed Contract（科研语义，不是 Harness 实现方案）

进入大规模实验前，候选方法至少应包含以下字段：

```yaml
formation_mode:
target_failure:
operating_envelope:
failure_evidence:
strongest_baseline:
simple_repairs_tested:
primary_root_cause:
rival_root_causes:
required_intervention:
  variable_or_relation:
  existing_state:
  required_state:
source_genealogy:
  original_mechanism:
  original_problem:
  demonstrated_intervention:
  assumptions:
intervention_alignment:
nearest_target_priors:
target_intervention_novelty:
collision_ledger:
causal_repair_dag:
mechanism_delta:
minimal_technical_kernel:
natural_derivation:
feasibility_ledger:
  observability:
  optimization:
  realtime:
  closed_loop:
  safety_physics:
  data:
  verification:
counterfactual_tests:
claim_scope:
unresolved_debts:
go_no_go:
```

其中 `mechanism_delta`、`required_intervention.variable_or_relation`、`nearest_target_priors`、`collision_ledger`、`causal_repair_dag` 和 `feasibility_ledger` 为空时，不允许以“Candidate Principle”替代后继续推进。

## 9. 对当前 Method Design 思路的最终修改

### 保留为硬规则

- 真实 failure activation；
- simple-repair falsifier；
- mechanism-level RCA；
- Required-Intervention Extraction；
- Intervention-Level Alignment；
- Target Intervention Novelty；
- Assumption–Constraint Collision closure；
- Mechanism Delta；
- Natural Derivation；
- Feasibility Closure；
- counterfactual necessity tests。

### 保留但明确“必要非充分”

- No-Orphan-Module；
- modules 与 target constraints 的对应；
- Source mechanism 在原域有效。

### 删除或替换

- 删除“所有强方法都必须有 Source Transfer”；改为 formation-mode router；
- 删除“必须有最低程度的 nontrivial transformation”；改为 collision-driven transformation；
- 删除“顶级 paper 可作为强 Method Seed 标签”；改为贡献类型分轨；
- 删除“更多模块/更多领域融合表示更强”；改为最小 causal repair DAG。

### 降级为软规则

- Source Problem 与 Target Problem 的表面相似；
- Source Root Cause 与 Target Root Cause 一致；
- Source 必须来自其他领域；
- 方法必须包含学习、优化或复杂模型；
- target transformation 的结构数量。

## 10. 最终回答验收问题

### 10.1 实际过程应怎样执行

先路由 formation mode；对 RCA-transfer 路径，依次执行 failure activation、operating envelope、simple repair falsifier、mechanism RCA、required intervention、source genealogy、intervention alignment、target intervention novelty、collision ledger、causal repair DAG、mechanism delta freeze、natural derivation、feasibility closure 和 counterfactual package。任何硬门失败都回退，而不是继续生成更漂亮的故事。

### 10.2 什么情况算做对，什么情况必须失败

做对的最低证据是：失败可观察；RCA 能预测 failure boundary；required variable 可写；Source 真能改变该变量；目标域等价干预未覆盖；每个改造由真实 collision 触发；最终 delta 可计算；目标-only 推导成立；致命 feasibility debt 不存在；counterfactual 能验证 causal edge。

只要其中一项被算法名、能力形容词、venue、模块数量或总性能替代，就必须失败或降级。

### 10.3 顶级 Seed 与普通迁移/method soup/application 的区别

区别不在用了什么热门 primitive，而在：

`required structural change`、`source intervention`、`final computational change` 三者是否同一；

以及最终方法是否是由 collision 驱动的最小 repair DAG，而不是可任意替换的组件集合。

### 10.4 哪些假设被修改

Active RCA、Required Intervention、Alignment、Target Novelty、Mechanism Delta、Natural Derivation 和 Feasibility 得到支持；No-Orphan 被确认只是必要条件；Nontrivial Transformation 被替换为 Collision Closure；“所有顶刊方法都属于 transfer”被证伪；simple-repair falsifier、formation router、contribution-type separation 和 counterfactual package 被新增。

### 10.5 如何在大实验前保证创新、必要、可行

冻结一个带明确 before→after relation 的 Method Seed Contract；要求最近邻 causal delta、simple-repair 结果、collision ledger、repair DAG、feasibility ledger 和最小 counterfactual tests 同时存在。先运行最便宜的 kill tests：可观测性、实时性、小规模闭环稳定、naive transfer、simple patch 和 nearest prior。只有这些没有杀死 seed，才允许进入大规模实验。

## 附录 A：本轮核心原始 PDF

- [Accuracy/Robustness Dilemma](D:/桌面/科研Agent%20Harness设计/impedance-control-e2e/source-materials/user-batch/A_Solution_to_the_Accuracy_Robustness_Dilemma_in_Impedance_Control.pdf)
- [Composite Learning VIC](D:/桌面/科研Agent%20Harness设计/impedance-control-e2e/source-materials/user-batch/Composite_Learning_Variable_Impedance_Robot_Control_With_Stability_and_Passivity_Guarantees.pdf)
- [Contact Transition Stability](D:/桌面/科研Agent%20Harness设计/impedance-control-e2e/source-materials/user-batch/Contact_transition_stability_in_the_impedance_control.pdf)
- [Stable State-Dependent VIC / SNEUM](D:/桌面/科研Agent%20Harness设计/impedance-control-e2e/source-materials/user-batch/Learning_Stable_State-Dependent_Variable_Impedance_Control_for_Compliant_Manipulation.pdf)
- [Stability Considerations for VIC](D:/桌面/科研Agent%20Harness设计/impedance-control-e2e/source-materials/user-batch/Stability_Considerations_for_Variable_Impedance_Control.pdf)
- [Stable Execution of Contact Tasks](D:/桌面/科研Agent%20Harness设计/impedance-control-e2e/source-materials/user-batch/Stable_execution_of_contact_tasks_using_impedance_control.pdf)
- [Adaptive Energy-Bounding](D:/桌面/科研Agent%20Harness设计/impedance-control-e2e/source-materials/user-batch-v2/Adaptive_Energy-Bounding_Approach_for_Robustly_Stable_Interaction_Control_of_Impedance-Controlled_Industrial_Robot_With_Uncertain_Environments.pdf)
- [Complementary Stability & Loop Shaping](D:/桌面/科研Agent%20Harness设计/impedance-control-e2e/source-materials/user-batch-v2/Complementary_Stability_and_Loop_Shaping_for_Improved_HumanRobot_Interaction.pdf)
- [Constrained VIC using QP](D:/桌面/科研Agent%20Harness设计/impedance-control-e2e/source-materials/user-batch-v2/Constrained_Variable_Impedance_Control_using_Quadratic_Programming.pdf)
- [Diffusion-Based Impedance Learning](D:/桌面/科研Agent%20Harness设计/impedance-control-e2e/source-materials/user-batch-v2/Diffusion-Based%20Impedance%20Learning%20for%20Contact-Rich%20Manipulation%20Tasks.pdf)
- [Hybrid Inverse Dynamics](D:/桌面/科研Agent%20Harness设计/impedance-control-e2e/source-materials/user-batch-v2/End-to-End%20Learning%20of%20Hybrid%20Inverse%20Dynamics%20Models%20for%20Precise%20and%20Compliant%20Impedance%20Control.pdf)
- [Risk-Sensitive Impedance](D:/桌面/科研Agent%20Harness设计/impedance-control-e2e/source-materials/user-batch-v2/Impedance_Optimization_for_Uncertain_Contact_Interactions_Through_Risk_Sensitive_Optimal_Control.pdf)
- [Segmentation + MOBO](D:/桌面/科研Agent%20Harness设计/impedance-control-e2e/source-materials/user-batch-v2/Learning_Compliant_Stiffness_by_Impedance_Control-Aware_Task_Segmentation_and_Multi-Objective_Bayesian_Optimization_with_Priors.pdf)
- [Passivity Filter](D:/桌面/科研Agent%20Harness设计/impedance-control-e2e/source-materials/user-batch-v2/Passivity_Filter_for_Variable_Impedance_Control.pdf)
- [Perturbation-Based Stiffness Inference](D:/桌面/科研Agent%20Harness设计/impedance-control-e2e/source-materials/user-batch-v2/Perturbation-Based_Stiffness_Inference_in_Variable_Impedance_Control.pdf)
- [Asymmetric Impedance Matrices](D:/桌面/科研Agent%20Harness设计/impedance-control-e2e/source-materials/user-batch-v2/Reinforcement_Learning_of_Impedance_Policies_for_Peg-in-Hole_Tasks_Role_of_Asymmetric_Matrices.pdf)

## 附录 B：本轮未声称的内容

- 未声称已恢复作者真实历史构思过程；
- 未声称所有顶会顶刊方法都遵循 RCA-transfer；
- 未声称论文中出现某个 Source citation 就证明直接借鉴；只有明确扩展关系或公式/结构谱系足够时才纳入 genealogy；
- 未因个别论文的局限否定其整体科学价值；本报告只审查其对 Method Seed 生成规则的意义；
- 未提前修改 Harness、正式状态或已接受 artifacts。
