# Method Seed 科研准则外部测试：冻结训练规则后的 Holdout Evaluation

日期：2026-08-30  
状态：测试协议、测试集与 Phase A 预测均已冻结；Phase B 已完成  
目的：检验前三轮文献归纳出的科研准则能否在未参与规则形成的论文上，生成或拒绝合理的创新方法，而不是继续用案例修正规则。

## 1. 训练集与测试集隔离

### 1.1 训练信息

训练信息仅包括：

- `逆向分析结果1.txt` 与 `逆向分析结果2.txt` 中用于形成早期准则的案例；
- `逆向分析续作3-Method-Formation跨案例审计.md` 中列出的 16 个阻抗控制核心、边界和反例；
- 在前三轮中已经显式使用的 Source genealogy。

### 1.2 测试集排除规则

以下论文及其直接分析结果不得作为测试样本：Accuracy/Robustness、Complementary Stability、Risk-Sensitive Impedance、Adaptive EBA、SNEUM、Composite Learning VIC、Passivity Filter、Asymmetric Matrices、Diffusion-Based Impedance、Constrained VIC-QP、Segmentation+MOBO、Contact Transition、Perturbation Stiffness Inference、Hybrid Inverse Dynamics、Stable Execution、Stability Considerations。

### 1.3 冻结测试集

测试集从剩余 `user-batch-v2` 文献中分层选择。选择覆盖 passivity/stability、optimization/predictive control、learning/adaptation、flexible-joint、human-guided interaction 和疑似普通组合，避免只测与训练强案例最相似的论文。

| Test ID | Paper ID | Year | Paper |
|---|---:|---:|---|
| T01 | X3fLqXpiIBoJ | 2016 | Passive Interaction Control With Dynamical Systems |
| T02 | yWRyC18EraoJ | 2018 | Development of a Safety- and Energy-Aware Impedance Controller for Collaborative Robots |
| T03 | ioYGUCT49JIJ | 2018 | Robust Passivity and Passivity Relaxation for Flexible-Joint Robots with Inner-Loop Torque Control |
| T04 | mWLHYOo4c4wJ | 2018 | A DMPs-Based Framework for Learning and Generalization of Humanlike Variable Impedance Skills |
| T05 | pO9mjm67fekJ | 2022 | Deflection-Domain Passivity Control of Variable Stiffnesses Based on Potential Energy Reference |
| T06 | w4w_nVaBi-4J | 2022 | Model-Based Actor-Critic Learning of Robotic Impedance Control in Complex Interactive Environment |
| T07 | sXzu51TTSB0J | 2022 | Variable Impedance Skill Learning for Contact-Rich Manipulation |
| T08 | eenWQDjapxgJ | 2023 | Impedance Learning for Human-Guided Robots in Contact With Unknown Environments |
| T09 | xlNjdqnC2fMJ | 2023 | Model Predictive Variable Impedance Control for Adaptive Precision-Compliance Tradeoff |
| T10 | Qm5BKnMez5cJ | 2024 | Variable Impedance Based on Power-Shaping Signals and Partial Link-Side Dynamics for Flexible-Joint Robots |
| T11 | lLfdIFGp-oYJ | 2024 | Passive Model-Predictive Impedance Control for Safe Physical Human–Robot Interaction |
| T12 | ur6FQs3aZv0J | 2024 | Event-Triggered Adaptive Neural Impedance Control of Robotic Systems |
| T13 | q3JkVkVjN94J | 2025 | Impedance Learning-Based Adaptive Force Tracking for Robot on Unknown Terrains |

## 2. 防泄漏测试程序

每篇论文分两个阶段读取。

### Phase A：Design Simulation（禁止查看最终方法）

只允许使用：

- 论文发表前已存在的目标问题与 prior work；
- Introduction 中首次出现 `we propose / we develop / our method / contributions` 之前的 failure 与 gap；
- 目标域 observability、dynamics、geometry、feedback、real-time、data 与 safety constraints；
- 冻结的科研准则。

禁止使用 abstract 中的方法描述、contribution list、method section、公式实现和实验结果。

Phase A 必须预注册：

1. formation mode；
2. activated failure 与 operating envelope；
3. strongest baseline 与 simple-repair verdict；
4. mechanism-level RCA；
5. required intervention；
6. 一个最小 Candidate Method Seed；
7. Mechanism Delta；
8. 预期 collision、repair 和 feasibility kill tests；
9. `GO / CONDITIONAL / NO-GO / ROUTE-ELSEWHERE`。

### Phase B：Reveal and Score

Phase A 冻结后才允许读取完整论文。随后比较：

- 实际论文的核心机制是否与预注册 required intervention 一致；
- Candidate Seed 是否命中等价 causal/computational relation；
- 准则是否正确判断论文为强方法、增量方法、普通 application 或其他 formation mode；
- 准则是否提前发现论文真实的 feasibility/novelty 边界；
- 论文是否暴露准则的新盲点。

## 3. 评分规则

### 3.1 预测分数

| Metric | 2 | 1 | 0 |
|---|---|---|---|
| Formation Route | 正确识别主 mode | mode 相邻但可用 | 强行套错路径 |
| RCA | 命中实际 performance-limiting mechanism | 命中上位原因 | 仅复述任务 gap |
| Required Intervention | 命中变量、方向与作用层级 | 方向正确但变量过粗 | 跳到算法名/错误变量 |
| Mechanism Delta | 与论文核心等价或更小更清楚 | 只命中一个主要模块 | 组合词或不相关机制 |
| Novelty Calibration | 正确区分新干预、增量、应用 | 基本正确但强度偏差 | venue/算法名替代 novelty |
| Feasibility Calibration | 提前命中主要边界/kill test | 发现一般风险 | 漏掉致命障碍 |
| Decision | GO/拒绝/改道与揭示后证据一致 | 强度轻微偏差 | false positive/false negative |

单篇满分 14。`≥11` 为强命中，`8–10` 为部分命中，`≤7` 为失败。

### 3.2 更严格的“能设计出创新方法”判定

只有同时满足以下条件才记为 `GENERATIVE SUCCESS`：

1. Phase A 在未知论文最终方法时提出明确 before→after Mechanism Delta；
2. 该 delta 与论文核心干预在 causal function 上等价，或提出一个经最近邻检索仍未覆盖的合理替代；
3. 不是只预测到“用 RL/MPC/NN/passivity”；
4. simple repair、novelty 与 feasibility 三个 gate 没有被跳过；
5. 揭示后没有依靠重写 Phase A 来追认成功。

若准则正确拒绝普通组合、错误必要性或不可行 seed，记为 `DISCRIMINATIVE SUCCESS`。两者必须分开统计。

## 4. 预注册总假设

- H1：准则应在多数真正机制型论文上命中 required intervention，但不一定预测到同一数学工具。
- H2：准则对 stability/passivity 类论文的 RCA 命中率应高于端到端 learning 类论文，因为前者的 causal variable 更可识别。
- H3：Formation-Mode Router 会把一部分学习论文改道为 representation/search/system-co-design，而不是错误执行 Source Transfer。
- H4：Simple-Repair、Target Intervention Novelty 与 Feasibility Closure 会降低“所有测试论文都被判成强创新”的 false-positive rate。
- H5：最大的预期失败不是无法生成方法，而是 required intervention 的粒度不足，导致可生成多个同样合理但无法区分的 seed。

## 5. Phase A 预注册结果

### 5.1 泄漏审计

PDF 是双栏排版，自动截断在少数论文中越过了 contribution marker。T01、T02、T09、T11、T12 因而暴露了核心方法；T10 的标题和引言暴露了高层机制族。这六篇仍保留在冻结测试集中，但只承担区分性、边界和评分校准，不进入主生成命中率。主生成集为 T03、T04、T05、T06、T07、T08、T13；T10 只在敏感性分析中加入。该处理在揭示 Method/Results 前冻结。

### 5.2 未污染主生成集

#### T03 — Robust Passivity / Passivity Relaxation

- **Mode**：formal control / mechanism repair，而非 source-transfer。
- **Failure envelope**：柔性关节机器人采用内力矩环、高阻抗和不确定负载时，名义解析被动并不保证真实交互稳定；二值被动性也无法给出控制器增益上界。
- **Simple repair**：继续降增益或加阻尼能提高稳定余量，但会直接损失阻抗性能，不能回答“允许多大非被动性”。
- **RCA → intervention**：问题变量不是单一增益，而是闭环从环境端口看到的最坏情形 passivity margin。必须把名义二值判据改为含参数不确定性的定量裕度，并把允许的 passivity shortage 与环境动态界联系起来。
- **Candidate Seed / Delta**：`nominal binary passivity → uncertainty-aware passivity radius + bounded-environment relaxation`；在频域计算最坏裕度，并由小增益/耗散关系给出可安全放宽的阻抗区间。
- **Kill tests**：参数集合覆盖性；频域条件是否可计算；允许环境集合是否可观测/可界定。
- **Decision**：GO。

#### T04 — DMP Variable Impedance Generalization

- **Mode**：representation/generalization；不能强行套 mechanism-transfer。
- **Failure envelope**：只模仿轨迹不能迁移人类示教中的时变刚度；独立回放轨迹与刚度在新目标、时间缩放或空间变换下可能失配。
- **Simple repair**：给轨迹和刚度各拟合一个 DMP 是最强简单基线；除非证明独立缩放破坏两者的相位/任务关系，否则不足以支持强创新。
- **RCA → intervention**：需要改变的是 motion–impedance 的共同相位与任务变换关系，而不是单纯增加回归器。
- **Candidate Seed / Delta**：`independent trajectory/stiffness replay → phase-coupled motion–stiffness primitive with joint spatial/temporal transformation`；刚度保持正定，并随任务几何变化作结构化变换。
- **Kill tests**：EMG 刚度标签可靠性；新目标下刚度变换是否有物理依据；执行稳定性/被动性。
- **Decision**：CONDITIONAL；若只是双 DMP 并列则是 application/组合。

#### T05 — Deflection-Domain Passivity

- **Mode**：mechanism repair。
- **Failure envelope**：在线变刚度会注入能量；energy tank/TDPA 为保被动性可能长时间把指令衰减到零刚度，摧毁接触任务所需的非零机械行为。
- **Simple repair**：增大初始 tank 能量、限制刚度变化率或调大阻尼只是转移预算/牺牲响应，不能消除“安全动作等于关闭期望刚度”的结构问题。
- **RCA → intervention**：能量监管作用在全局控制输出，而任务能量实际由弹性偏转和期望势能决定。监管变量应从全局 tank 余额改为 deflection-domain 的实际/参考势能差，并以最小方式修正变刚度动作。
- **Candidate Seed / Delta**：`global energy budget and force attenuation → deflection-domain potential-energy reference regulation`；只在势能增量违反被动条件时投影/修正 stiffness 或 deflection command，保留可行的非零刚度。
- **Kill tests**：偏转可测/可估；非线性刚度势能可积；离散实现不引入漏算能量。
- **Decision**：GO。

#### T06 — Model-Based Actor–Critic Impedance Learning

- **Mode**：system-co-design / safe learning，不是“从别域搬 RL”。
- **Failure envelope**：快速变化的接触环境中，常规自适应慢；model-free RL 真实探索危险、样本低效，连续动作的贪婪更新慢，且既有 IC-RL 常缺少闭环力反馈。
- **Simple repair**：奖励惩罚、动作裁剪和更多数据能减轻风险，却不能修复探索所需真实危险交互与已知机器人结构被浪费的问题。
- **RCA → intervention**：必须改变 value/policy 更新的信息来源：从仅真实转移样本，变为利用已知/学习到的阻抗闭环交互模型和力反馈来产生梯度/想象更新，同时显式约束物理动作。
- **Candidate Seed / Delta**：`model-free actor–critic over raw interaction → impedance-structured model-based actor–critic with force-state feedback and bounded safe action layer`。
- **Kill tests**：模型偏差是否把策略推向危险区域；是否有真实安全保证而非 reward shaping；实时求解成本。
- **Decision**：CONDITIONAL；若无 model-error/safety closure，只能算样本效率型增量。

#### T07 — Variable Impedance Skill Learning

- **Mode**：action/representation design + real-system learning。
- **Failure envelope**：接触丰富操作中，位置动作受阻会产生大力矩，直接力矩策略又必须从数据中学习接触瞬态和柔顺性；固定阻抗无法兼顾自由空间精度与接触顺应。
- **Simple repair**：降低固定刚度或加动作平滑只是在两个工况间折中，不改变策略面对的接触动力学。
- **RCA → intervention**：必须把策略动作变量从直接运动/力矩改成受物理结构约束的 equilibrium 与 impedance，使低层闭环吸收接触瞬态，并让阻抗随状态变化。
- **Candidate Seed / Delta**：`direct pose/torque or fixed impedance action → bounded state-dependent variable-impedance action (reference offset + SPD stiffness/damping)`。
- **Kill tests**：此前是否已有同等 VIC action interface；真实机器人样本量和稳定边界；刚度参数化是否始终正定。
- **Decision**：CONDITIONAL；mechanism 合理，但 target-intervention novelty 很可能仅为增量。

#### T08 — Human-Guided Robot in Unknown Environment

- **Mode**：interaction-channel decomposition / learning-control co-design。
- **Failure envelope**：同一末端同时受人和环境作用；低阻抗利于人引导却难以拒绝环境重复扰动，高阻抗稳定接触却会抵抗人的意图。
- **Simple repair**：统一调低/调高阻抗、带宽 tuning 或单一力滤波仍把两种外力当作同一信号，必然保留冲突。
- **RCA → intervention**：关键变量是 external interaction 的来源/可预测结构。必须在计算上把 desired human-guidance channel 与 repeatable/learnable environment channel 分开，只补偿后者。
- **Candidate Seed / Delta**：`single impedance response to summed external force → compliant human port + trial/trajectory-conditioned learned environmental feedforward compensation`；加 forgetting/robustness 与闭环稳定约束。
- **Kill tests**：人/环境力是否可辨识；环境重复性破坏时是否安全退化；学习补偿是否影响被动端口。
- **Decision**：GO。

#### T13 — Unknown-Terrain Force Tracking

- **Mode**：adaptive/learning control；可能含 composite-learning 路线，但不预设具体算法。
- **Failure envelope**：未知地形的非线性位置/刚度使估计式调参考方法持续有误差；人类示教工作量大；model-free RL 需要危险物理探索、收敛和可解释性差。
- **Simple repair**：更高阶环境估计器或更大网络仍依赖错误模型/危险探索；只调学习率不能建立安全和收敛证据。
- **RCA → intervention**：应直接学习/估计“阻抗参数变化到力误差”的可解释闭环关系，而不是重建完整地形；在线更新必须由可验证的误差/历史信息驱动，并置于稳定自适应环内。
- **Candidate Seed / Delta**：`explicit terrain identification or opaque policy search → stability-constrained, data-assisted impedance adaptation using force-error/history excitation`；用离线/安全数据初始化，在线只作有界修正。
- **Kill tests**：未知非线性的逼近误差界；持续激励/历史数据充分性；接触切换时的稳定与执行器饱和。
- **Decision**：CONDITIONAL；required intervention 不唯一，若实际只以神经网络替代估计器则 novelty 较弱。

### 5.3 污染/诊断集（不计主生成率）

| ID | 冻结的诊断判断 |
|---|---|
| T01 | 稳定动力系统在交互力作用下可注入能量；应从“名义稳定 DS”改为端口能量受监管的 DS。若只是把已知 energy tank 直接接到 DS，alignment 正确但 target transformation/novelty 未必强。 |
| T02 | 单自由度能量/功率监管不能直接处理多自由度刚体 twist–wrench 耦合与方向性安全；需要坐标一致的多通道能量归因。若只是把一维 tank 复制到各轴，应拒绝强创新。 |
| T09 | MPC 应直接把 impedance parameters 作为决策变量，并在精度–柔顺目标、动力学/输入约束和 passivity budget 下优化；这是明确 delta，但 MPC/tank primitives 已成熟，强度取决于统一建模而非算法名称。 |
| T10 | `full-model/high-derivative flexible-joint impedance → partial link-side power-shaping signals`；高层变量已由题名暴露。预判为形式控制增量，须检查与作者前序 power-shaping 工作的距离。 |
| T11 | 变刚度底层产生候选动作，顶层优化只施加满足能量/被动约束的最小补偿；应检查是否真的避免传统逐通道 passivity filter 的保守性和 tank 初始化敏感性。 |
| T12 | 连续神经自适应更新的计算/通信负担可由 Lyapunov 触发的稀疏更新修复，但 event-triggered adaptive NN 是成熟 intervention；预判为合理 application/增量，而非强 target novelty。 |

## 6. Phase B 揭示、评分与错误分析

### 6.1 逐篇揭示结果

评分顺序为：`Route / RCA / Intervention / Delta / Novelty / Feasibility / Decision`。`G` 是严格生成命中，`P` 是部分生成命中，`D` 是正确降级或拒绝，`C` 是协议污染，仅作诊断。

| ID | Phase B 实际核心机制 | 分项分数 | 总分 | 判定与误差 |
|---|---|---:|---:|---|
| T01 | 将任意运动 DS 分解为 conservative/residual 分量；阻尼特征向量与期望速度对齐，以选择性耗散给 tank 充能，再由 tank 门控非保守分量。[DOI](https://doi.org/10.1109/LRA.2015.2509025) | 2/1/1/1/1/2/2 | 10 | **C/D**。只猜中“端口能量监管”不足以恢复 DS 分解、方向阻尼和 residual gating；证明 intervention family 不是完整 seed。 |
| T02 | screw-theoretic Cartesian spring；统一缩放 co-stiffness 满足能量阈值、缩放关节阻尼满足功率阈值，并以逐关节 tanks 保证在线增益变化的被动性。[DOI](https://doi.org/10.1109/LRA.2018.2795639) | 2/2/1/1/1/2/2 | 11 | **C/D**。诊断正确，但“多轴复制 tank”仍是主要实现；属于对已知 primitive 的多自由度安全扩展，不应因模块多而自动判强。 |
| T03 | 以乘性 motor uncertainty 建立 robust passivity bound；Cayley transform 把严格被动转成 small-gain 条件；低频被动、高频 robot–environment gain product 小于一时允许有限频段非被动。[DOI](https://doi.org/10.1109/TMECH.2018.2870846) | 2/2/2/2/2/2/2 | 14 | **G**。Phase A 同时命中最坏 passivity margin 与 mixed passivity/small-gain relaxation；1-DoF、LTI、环境模型和频域不确定集也被提前识别。 |
| T04 | EMG 估计人的 endpoint stiffness；extended DMP 同时编码轨迹和刚度，并以 goal parameters 泛化终点/终端刚度；示教混合权重是定性选择。[DOI](https://doi.org/10.1109/TMECH.2018.2817589) | 2/1/2/1/2/2/2 | 12 | **P/D**。命中联合表示，但预注册的“共同任务变换/独立 DMP 反例”强于论文证据。论文没有排除双回归器等简单基线，也没有稳定性证明，故可复现 method family，不能据此宣称 strong novelty。 |
| T05 | OBG-K 观察弹簧势能，在 spring-deflection domain 上用梯度约束 stiffness；无需初始 tank reserve，并可保留任选的非零最小刚度。[DOI](https://doi.org/10.1109/LRA.2022.3147566) | 2/2/2/2/2/2/2 | 14 | **G**。几乎逐项命中；揭示后的关键限制也与 kill tests 一致：仅 1-DoF、deadband 能量忽略、快速加刚度偏保守、通信通道仍可能触发 TDPA 衰减。 |
| T06 | 线性/线性化离散模型把 force 纳入 state，以 quadratic value 和 impedance indices 学习线性 feedback gain；model-constrained deterministic actor–critic 收敛到 Riccati 解，Qd/Qf stability map 约束可交互外部刚度；先虚拟力训练再迁移。[DOI](https://doi.org/10.1109/TIE.2021.3134082) | 2/2/2/1/2/2/2 | 13 | **G**。命中“模型和力状态进入 actor–critic 更新”这一 causal relation；未唯一推出 Riccati 等价、index stability map 与 virtual-force transfer，因此 delta 只给 1。线性化边界与真实探索安全被正确预警。 |
| T07 | VIA-SPiRL 先以每种 peg 200 条 FSM demonstrations 学 latent skill prior，再由 SAC 高层同时选 latent motion skill 与四个 Cartesian stiffness 分量，低层 impedance controller 执行。[DOI](https://doi.org/10.1109/LRA.2022.3187276) | 2/1/1/1/2/2/2 | 11 | **P/D**。只命中 variable-impedance action interface，漏掉“skill prior 降低真实样本需求”这一并列 bottleneck/核心模块。target intervention 已有前驱，且无 passivity、force-bound 或 safe-exploration guarantee；正确降级为增量型 system design。 |
| T08 | 非重复任务用 position/velocity/constant lumped disturbance 的 Lyapunov adaptation；空间重复任务用跨 execution 的 position-dependent iterative learning，并在近零速度处修复 inverse-speed singularity；不需力传感器。[DOI](https://doi.org/10.1109/TRO.2023.3281483) | 2/2/2/2/1/2/2 | 13 | **G**。命中“保留 compliant human port，只学习/抵消环境通道”与重复环境的空间前馈补偿；没有唯一推出非重复分支的三组 adaptation laws，且 novelty genealogy 预注册不够细，故 novelty 给 1。重复性、可辨识性和零速度奇异性 kill tests 均兑现。 |
| T09 | 直接把 variable impedance parameters 作为 MPC input；one-step QP / multistep state-constrained MPC；tank correction 保被动，并以 state-dependent minimum stiffness 修复插管碰撞。[DOI](https://doi.org/10.1109/TMECH.2022.3204350) | 2/2/2/2/2/2/2 | 14 | **C**。与污染后诊断完全一致，不能作为生成证据；可用于确认 Mechanism Delta 与 constraint collision 的评分方式。 |
| T10 | UMVIC 用 Lyapunov/power shaping，仅需 gravity torque 与 motor-side dynamics，省去 link inertia/Coriolis 和 link acceleration/jerk；允许任意速率 gain modulation 与 nonlinear passive stiffness。[DOI](https://doi.org/10.1109/TMECH.2023.3287789) | 2/2/2/2/1/1/2 | 12 | **C/D**。标题泄漏高层变量；实际主要是形式控制扩展，仍需准确 motor model，且不负责 gain selection。说明 target transformation 可有价值，但不是 source primitive 一出现就构成新的 Method Seed。 |
| T11 | 底层 VIC 之外，上层 receding-horizon QP 选择最小 complementary force，使 augmented dissipated-energy state 满足下界；定理给出 recursive feasibility 和特定变换端口下的 passivity。[DOI](https://doi.org/10.1109/TCDS.2023.3275217) | 2/2/2/2/2/2/2 | 14 | **C**。机制已泄漏，不计生成；其边界验证 Feasibility Closure 必须与 claim 对齐：准确 inverse dynamics、局部预测、无 saturation/delay/model uncertainty，且负 energy bound 是放宽被动而非严格被动。 |
| T12 | nominal model + RBFNN 补偿聚合不确定性；事件时更新网络权重、状态和 torque，间隔内 ZOH；连续/离散 Lyapunov 分析给 local UUB 与正 inter-event lower bound。[DOI](https://doi.org/10.1109/TNNLS.2023.3278301) | 2/2/2/2/2/2/2 | 14 | **C/D**。正确识别为成熟 event-triggered adaptive-NN intervention 的应用/增量，而不是 target-level 强创新；仿真资源节省也不能升级为真实实时可行性证明。 |
| T13 | 在随机虚拟地形预训练 DRL neural feedforward，动作是阻抗增量；回归量含前次 trial 的 input/state，当前 force error 提供 feedback；以简化接触模型、Lipschitz 条件和 observable regression state 给出条件性分析。[DOI](https://doi.org/10.1109/TRO.2025.3530345) | 2/1/1/1/1/2/2 | 10 | **FAIL（严格生成）/D**。Phase A 命中“历史数据 + 稳定约束的 impedance learning”家族和 observability kill test，却没有推出 sim-pretrained DRL feedforward、trial regression 与 feedback 的明确结构；多个算子同样满足 required intervention。准则正确保持 CONDITIONAL，但不能把宽泛家族预测追认为 seed 命中。 |

### 6.2 主生成集统计

污染样本不进入任何主指标。七篇主生成集的结果为：

- 严格 `GENERATIVE SUCCESS`：T03、T05、T06、T08，**4/7 = 57.1%**；
- 部分生成命中：T04、T07，**2/7 = 28.6%**；
- 严格生成失败：T13，**1/7 = 14.3%**；
- 能给出有用 route/RCA/拒绝结论：**7/7**；
- 平均预测分：**87/98 = 12.43/14**。该高分包含正确拒绝和边界预测，不能冒充严格 seed 复现率；
- passivity/mechanism-repair（T03、T05）严格命中 **2/2**；learning/system-design（T04、T06、T07、T08、T13）严格命中 **2/5**，部分命中 2/5，失败 1/5。

若把部分泄漏的 T10 加入敏感性分析，因题名已经给出 `power-shaping + partial link-side dynamics`，不会报告扩大后的生成率；这正是对评价协议的必要约束，而不是删掉不利样本。

### 6.3 五个预注册假设的判决

| 假设 | 判决 | 跨案例证据 |
|---|---|---|
| H1：机制型论文多数可命中 required intervention | **支持，但修正** | 6/7 至少达到可用 intervention，4/7 达到严格 seed；“变量与方向”可预测，不等于实现算子可唯一识别。 |
| H2：passivity/stability 高于端到端 learning | **支持** | T03/T05 全命中；learning 中 T07 漏掉并列 skill-prior bottleneck，T13 出现 operator non-identifiability。 |
| H3：Router 会把学习论文改道 | **支持** | T04 被路由为 representation，T06 为 system-co-design，T07 为 action/skill representation，T13 为 adaptive/learning control；没有伪造 source-transfer 故事。 |
| H4：三类 gate 可降低 false positives | **支持** | T04 被 simple-repair 降级，T07/T12 被 target novelty 降级，T06/T07/T11/T13 被 claim-proportional feasibility 限定。 |
| H5：主要失败是 intervention 粒度不足、多个 seed 不可区分 | **强支持** | T13 是直接反例；T01 表明同一 energy intervention family 下还需 DS decomposition/directional damping；T07 表明多 bottleneck 论文只命中一个 intervention 会造成假阳性。 |

### 6.4 这次测试真正暴露的错误类型

1. **Intervention-family hit 误报为 Method-Seed hit**：预测“energy tank / learning compensation / variable impedance action”只到家族层级。完整 seed 至少还要给出作用对象、信息流、约束位置和更新关系。T01、T07、T13 是控制例。
2. **单 bottleneck 假设**：一篇论文可有正交的 active bottlenecks。T07 同时修复接触动作安全与真实样本效率；只命中前者不是完整机制覆盖。
3. **论文不是唯一 ground truth**：failure/RCA 通常只能确定 intervention equivalence class。评价应接受经 prior-art 与 feasibility gate 后仍成立的更简单替代，但不能因“看起来合理”自动算命中。
4. **安全词汇膨胀**：经验上没有 emergency stop、使用虚拟训练、UUB 或 passivity 都不是通用安全证明。Feasibility evidence 必须逐 claim 对齐。
5. **Novelty 不能由模块稀有度替代**：DMP+EMG、SPiRL+VIC、event-trigger+RBFNN 都可以合理有效，却可能仍是 application/增量。要检索的是目标域已有的等价 causal intervention。

## 7. 测试集对准则的最终判决

### 7.1 对冻结准则逐项裁决

| 原准则 | 裁决 | 测试后版本 |
|---|---|---|
| Active Root Cause / performance-limiting bottleneck | **支持并扩展** | 保留；新增 **Bottleneck Coverage Vector**，允许多个相互独立的 active bottlenecks，逐个决定 cover/defer/reject。 |
| Required-Intervention Extraction | **支持但不充分** | 必须输出 `variable + direction + operating layer + information required + invariants`，不能停在算法家族。 |
| Strong Source Mechanism | **降级为条件步骤** | 仅在 transfer/composition 路线启用。formal synthesis、representation redesign、system-co-design 可由目标 RCA 直接形成，不应硬造 Source Method。 |
| Intervention-Level Alignment | **支持** | 保留 `Source intervention ↔ target required structural change`，但增加 operator-level specificity；同功能并不等于同 method。 |
| Target Intervention Novelty | **强支持** | 必须按发表时点建立 nearest-neighbor/genealogy，检索等价 causal intervention，而非同名算法；T07/T12 表明这是强拒绝门。 |
| Nontrivial Target Transformation | **证伪其硬必要性** | 替换为 **Assumption–Constraint Collision Closure**：只有 source assumptions 与 target constraints 冲突时才要求 repair；无冲突的直接机制也可能新颖，复杂改造也可能只是工程化。 |
| Assumption–Constraint Collision | **强支持** | 每个 collision 必须有 evidence、repair 与新增 feasibility obligation。T05 的 deflection observability、T08 的 zero-speed singularity是正例。 |
| No-Orphan-Module | **支持但仅必要条件** | 无 orphan 只能证明结构可解释，不能证明 novelty/necessity；成熟模块有 causal parent 仍可能是 method soup。 |
| Mechanism Delta | **强支持并收紧** | 强制写成 `旧的信息流/状态更新/约束位置 → 新关系`；算法名和 “A+B+C” 不得通过。 |
| Natural Derivation | **支持但降级为必要非充分** | 能从 target failure 自然推出不等于新颖；T04/T12 可自然推出却仍可能只是增量。 |
| Feasibility Closure | **强支持并收紧** | 采用 **claim-proportional certificate**：稳定、被动、力限、安全探索、实时、泛化分别需要对应证据，禁止互相代替。 |
| Simple-repair falsifier | **强支持** | 在 source search 之前执行；若 tuning、独立回归、已知 filter 或现成 action interface 已解决核心 failure，则回退重选 bottleneck 或降低 claim。 |

### 7.2 新增三条硬标准

#### A. Seed Identifiability Gate

Required intervention 后必须生成至少三个竞争算子（包括最简单修补、论文式机制族和不同机制族），在同一 failure envelope 下比较：

`causal sufficiency × prior-art distance × assumption burden × observability × computational cost × falsifiability`。

只有一个候选在关键维度形成可证优势，或多个候选中有一个经过证据淘汰后胜出，才允许输出单一 Strong Seed。若多个候选不可区分，输出 `UNDERDETERMINED`，回到 discriminating evidence search；T13 不再被迫猜算法。

#### B. Mechanism Coverage Gate

先建立 bottleneck vector，再为最终每个核心模块标注父节点。若论文/seed 声称同时解决安全、样本效率、精度和泛化，则必须分别存在 intervention 和证据。只覆盖一个 bottleneck 时应缩小 claim，不得以总分掩盖；这是 T07 的直接修正。

#### C. Evaluation Leakage Gate

评估 Agent 是否“能生成”时，题名、摘要和 contribution list 中出现的机制词均视为 label。盲包只允许 target failure、pre-publication prior work 与约束；若任务标题本身泄漏机制，只能测试 RCA/拒绝能力。任何污染样本不得进入生成率。

### 7.3 可直接执行的科研流程

| Research Step | Input | Cognitive Operation | Required Evidence | PASS | FAIL | Recovery |
|---|---|---|---|---|---|---|
| 0. Claim freeze | 目标能力、场景、评价预算 | 把 claim 写成可证伪句，固定 operating envelope | 变量、边界、metric、失败阈值 | reviewer 可判真伪 | “更鲁棒/更智能” | 缩小 claim，补可测量定义 |
| 1. Formation router | failure packet、prior work | 在 transfer / formal synthesis / representation / optimization / system-co-design / application 间路由 | 至少两条排他性理由 | 路线决定后续证据类型 | 所有论文都套 source transfer | 改道；不纳入该路径统计 |
| 2. Failure activation | 最强 baseline、真实工况 | 找到何时、何输入、何状态下发生可复现失败 | 实验、反例、理论不兼容或多源一致证据 | failure 影响目标能力 | 仅“可能不稳/可能不足” | 补诊断实验或停止 |
| 3. Simple-repair falsifier | failure + strongest baseline | 依次测试 tuning、容量、数据、滤波、约束、现成模块 | repair 的反例或不可接受 tradeoff | 简单修补不能同时保留目标能力 | 未测试或已足够解决 | 采用简单修补；降低 novelty claim |
| 4. Mechanism RCA | failure traces、方程、信息图 | 反事实删除候选原因，定位 performance-limiting state/relation | `若改 X 则 failure 消失` 的机制证据 | 原因在适用 envelope 内可干预 | 复述 task gap/症状 | 设计判别实验，回到 Step 2 |
| 5. Bottleneck vector | RCA 结果 | 分离正交 bottlenecks 与依赖关系 | 每个 bottleneck 的独立 failure trace | claim 覆盖范围明确 | 把安全、效率、精度揉成一个词 | 拆 claim 或选择主 bottleneck |
| 6. Required intervention | active RCA | 在不知道算法名时写出 variable、方向、层级、信息与 invariant | before→after causal relation | 可排除不相关算法 | “使用 MPC/RL/NN” | 抽象回 computational relation |
| 7. Candidate competition | required intervention | 生成 ≥3 个算子并比较 sufficiency/assumption/cost | 能淘汰候选的差异证据 | 有胜者或明确 Pareto 选择 | 多个候选不可区分 | 标记 UNDERDETERMINED；搜索判别证据 |
| 8. Source/genealogy search | 胜出算子的功能描述 | 仅在适用路线追踪原始机制、前驱和作者早期工作 | 原公式/结构、原问题、原有效性证据 | 知道借的是哪个 intervention | 只引综述/Introduction story | 沿引用回溯；换 source |
| 9. Alignment + novelty | target RCA、source mechanism、发表时点 prior art | 比较 intervention variable，而非问题外观/算法名 | target-domain 等价干预最近邻表 | target relation 未被覆盖且 source 能改目标变量 | 同名新、等价旧，或只换场景 | 缩 claim、换 intervention、转 application |
| 10. Collision/repair DAG | source assumptions、target constraints | 逐项碰撞 observability/dynamics/geometry/feedback/realtime/safety | 每个 repair 有 causal parent | 无 orphan，且 repair 关闭冲突 | repair 产生未处理新瓶颈 | 继续 repair 链或拒绝迁移 |
| 11. Mechanism Delta + coverage | 全部核心模块 | 压缩为一条主 delta，并对 bottleneck/module 建 coverage matrix | 旧/新方程、信息流或约束位置 | 一个主干预，模块均可追溯 | A+B+C slogan；漏掉并列 bottleneck | 删除 orphan/缩 claim/补干预 |
| 12. Feasibility closure | 最终 seed、目标平台 | 对可观测、可解、实时、数据、闭环、饱和、安全逐项 kill-test | 与每个 claim 同类型的 certificate/测量计划 | 无未关闭致命障碍 | 用 passivity 代替安全、用仿真代替实时 | 加 estimator/filter/shield；缩 envelope；NO-GO |
| 13. Natural derivation audit | 删除 source 故事后的 seed | 仅用 Failure→RCA→Intervention→Constraint 重推方法 | 独立审阅可复现同一 delta family | 简洁、必要、无装饰模块 | 依赖“来自热门领域”才成立 | 回到 RCA 或删模块 |
| 14. Pre-experiment gate | seed + alternatives | 设计最便宜的 counterfactual：simple repair、naive transfer、去模块、oracle | 明确 kill criterion 与预期差异 | 大实验能区分 mechanism | 只比较弱 baseline/总 reward | 先做小规模判别实验 |

### 7.4 Strong Method Seed 的最终判定式

测试后，不能把“顶刊 seed”压成一个分数；最低合取条件是：

`Activated Failure`
`∧ Simple Repair Falsified`
`∧ Active RCA Identified`
`∧ Required Intervention Explicit`
`∧ Seed Identifiable among Competitors`
`∧ Target Intervention Novel`
`∧ Collision/Repair Closed`
`∧ Mechanism Coverage Complete for Claimed Bottlenecks`
`∧ Claim-Proportional Feasibility Closed`
`∧ One Clear Before→After Mechanism Delta`。

缺一项时不是一律丢弃：可以回退、缩小 claim、改走 application/system-engineering 路线，或输出 `UNDERDETERMINED`。但不得进入“顶会顶刊级 Strong Method Seed”队列。

### 7.5 普通迁移、method soup 与 Strong Seed 的可操作分界

| 类型 | 判别特征 |
|---|---|
| 普通 application | source primitive 有效、实现可行，但 target 等价 intervention 已存在，或只更换数据/平台/场景。 |
| 普通方法迁移 | alignment 正确，但没有新的 assumption–constraint collision，且机制关系不变；价值可以很高，novelty claim 必须降级。 |
| Method soup | 模块各自有好处，却无法映射到 bottleneck vector；删除任一模块也说不清哪个 failure 会重新出现。 |
| 强但不可行 seed | delta 新且必要，却依赖不可观测量、不可解优化、无安全探索或不可能的实时预算；停在研究假设，不进大实验。 |
| Strong Method Seed | 在真实 activated failure 上，简单修补失败；新 delta 精确改变 active causal variable；目标域 prior art 未覆盖；collision/repair 与 feasibility 全闭合；counterfactual 可验证。 |

### 7.6 最终回答

冻结准则**能够稳定完成问题路由、RCA、弱方案拒绝和 feasibility 边界识别，但只能在 57.1% 的未污染样本上独立恢复到严格等价的 Method Seed**。它还不是“输入 failure 就唯一生成顶刊方法”的算法；最大的缺口是从 required-intervention equivalence class 到具体 operator 的可识别性，以及多 bottleneck 论文的机制覆盖。

因此，对 Method Design 最重要的新增要求不是再堆更多 source mechanisms，而是加入 `Candidate Competition → Seed Identifiability → Mechanism Coverage` 三个认知步骤。这样 Agent 在大规模实验前必须明确：为何是这个算子、为何不是简单修补、为何已有等价干预不能解决、每个模块修复哪个 bottleneck、以及哪项证据会直接杀死该 seed。测试表明，这会保留 T03/T05/T06/T08 一类强机制候选，同时拒绝把 T04/T07/T12 一类合理但增量的组合和 T13 一类尚未唯一化的学习方案过度包装为 Strong Seed。

## 8. 约束

- 在 Phase B 完成前不修改冻结准则；
- 测试失败不能通过删除样本或更换评分定义修复；
- 如论文自身证据不足，区分“准则预测失败”与“ground truth 不确定”；
- 本测试不修改 Harness 或正式运行状态。
