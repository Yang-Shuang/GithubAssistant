# OpenMythos

<p align="left">
  <a href="https://pypi.org/project/open-mythos/" target="_blank">
    <picture>
      <source srcset="https://img.shields.io/pypi/v/open-mythos?style=for-the-badge&color=3670A0" media="(prefers-color-scheme: dark)">
      <img alt="Version" src="https://img.shields.io/pypi/v/open-mythos?style=for-the-badge&color=3670A0">
    </picture>
  </a>
  <a href="https://twitter.com/kyegomezb/">
    <picture>
      <source srcset="https://img.shields.io/badge/Twitter-Follow-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" media="(prefers-color-scheme: dark)">
      <img src="https://img.shields.io/badge/Twitter-Follow-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter">
    </picture>
  </a>
  <a href="https://discord.gg/3keGBK9Pvr" target="_blank">
    <picture>
      <source srcset="https://img.shields.io/badge/Discord-Join-5865F2?style=for-the-badge&logo=discord&logoColor=white" media="(prefers-color-scheme: dark)">
      <img alt="Discord" src="https://img.shields.io/badge/Discord-Join-5865F2?style=for-the-badge&logo=discord&logoColor=white">
    </picture>
  </a>
  <a href="https://pytorch.org" target="_blank">
    <picture>
      <source srcset="https://img.shields.io/badge/PyTorch-Implemented-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" media="(prefers-color-scheme: dark)">
      <img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-Implemented-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white">
    </picture>
  </a>
</p>

> **免责声明：** OpenMythos 是一个独立的、社区驱动的理论重构项目，仅基于公开的研究成果与合理推测。它与 Anthropic（Anthropic）或其任何专有系统均无关联、未获背书或授权。

OpenMythos 是 Claude Mythos 模型的一个开源理论实现。它采用循环深度 Transformer（Recurrent-Depth Transformer, RDT）架构，包含三个阶段：**序曲（Prelude）**（标准 Transformer 块）、循环执行的**递归模块（Recurrent Block）**（最多 `max_loop_iters` 次），以及最终的**尾声（Coda）**。注意力机制可在 MLA 与 GQA 之间切换，前馈网络采用稀疏的混合专家模型（Mixture of Experts, MoE），包含路由专家和共享专家，非常适合探索计算自适应、深度可变的推理能力。

## 安装

```bash
pip install open-mythos

#uv pip install open-mythos
```

要在 `GQAttention` 中启用 Flash Attention 2（需 CUDA 及编译工具）：

```bash
pip install open-mythos[flash]
```

## 使用方式

```python

import torch
from open_mythos.main import OpenMythos, MythosConfig


attn_type = "mla"  # or "gqa"

base = {
    "vocab_size": 1000,
    "dim": 256,
    "n_heads": 8,
    "max_seq_len": 128,
    "max_loop_iters": 4,
    "prelude_layers": 1,
    "coda_layers": 1,
    "n_experts": 8,
    "n_shared_experts": 1,
    "n_experts_per_tok": 2,
    "expert_dim": 64,
    "lora_rank": 8,
    "attn_type": attn_type,
}

if attn_type == "gqa":
    cfg = MythosConfig(**base, n_kv_heads=2)
else:
    cfg = MythosConfig(
        **base,
        n_kv_heads=8,
        kv_lora_rank=32,
        q_lora_rank=64,
        qk_rope_head_dim=16,
        qk_nope_head_dim=16,
        v_head_dim=16,
    )

model = OpenMythos(cfg)
total = sum(p.numel() for p in model.parameters())
print(f"\n[{attn_type.upper()}] Parameters: {total:,}")

ids = torch.randint(0, cfg.vocab_size, (2, 16))
logits = model(ids, n_loops=4)
print(f"[{attn_type.upper()}] Logits shape: {logits.shape}")

out = model.generate(ids, max_new_tokens=8, n_loops=8)
print(f"[{attn_type.upper()}] Generated shape: {out.shape}")

A = model.recurrent.injection.get_A()
rho = torch.linalg.eigvals(A).abs().max().item()
print(
    f"[{attn_type.upper()}] Spectral radius ρ(A) = {rho:.4f} (must be < 1)"
)
```



## 模型变体

预配置了从 10亿（1B）到 1万亿（1T）参数的规模：

```python
from open_mythos import (
    mythos_1b,
    mythos_3b,
    mythos_10b,
    mythos_50b,
    mythos_100b,
    mythos_500b,
    mythos_1t,
    OpenMythos,
)

cfg = mythos_7b()  # returns a MythosConfig
model = OpenMythos(cfg)

total = sum(p.numel() for p in model.parameters())
print(f"Parameters: {total:,}")
```

| 变体 | `dim` | 专家数 | `expert_dim` | 循环次数 | 上下文长度 | 最大输出长度 |
|---|---|---|---|---|---|---|
| `mythos_1b` | 2048 | 64 | 2048 | 16 | 4k | 4k |
| `mythos_3b` | 3072 | 64 | 4096 | 16 | 4k | 4k |
| `mythos_10b` | 4096 | 128 | 5632 | 24 | 8k | 4k |
| `mythos_50b` | 6144 | 256 | 9728 | 32 | 8k | 4k |
| `mythos_100b` | 8192 | 256 | 13568 | 32 | 1M | 128k |
| `mythos_500b` | 12288 | 512 | 23040 | 48 | 1M | 128k |
| `mythos_1t` | 16384 | 512 | 34560 | 64 | 1M | 128k |

---

## 训练

FineWeb-Edu 数据集上 30亿（3B）模型的训练脚本位于 [`training/3b_fine_web_edu.py`](training/3b_fine_web_edu.py)。

**单卡：**
```bash
python training/3b_fine_web_edu.py
```

**多卡（自动检测 GPU 数量）：**
```bash
torchrun --nproc_per_node=$(python -c "import torch; print(torch.cuda.device_count())") training/3b_fine_web_edu.py
```

关键设计选择：

| 特性 | 详情 |
|---|---|
| 优化器 | AdamW |
| 数据集 | `HuggingFaceFW/fineweb-edu`（默认使用 `sample-10BT`，完整训练可替换为 `sample-100BT` 或 `default`） |
| 分词器 | 通过 `MythosTokenizer` 调用 `openai/gpt-oss-20b` |
| 并行策略 | 基于 PyTorch DDP（使用 `torchrun`），支持分片流式数据集 |
| 精度 | H100/A100 上使用 bfloat16，旧款 GPU 使用 float16 + GradScaler |
| 学习率调度 | 线性预热（2000步）→ 余弦衰减 |
| 目标数据量 | 300亿 tokens（针对循环架构按 Chinchilla 定律调整） |

---

## 文档

| 文档页 | 说明 |
|---|---|
| [`docs/open_mythos.md`](docs/open_mythos.md) | `OpenMythos` 类的完整 API 参考 —— 构造函数、`forward`、`generate`、所有子模块、配置参考及使用示例 |
| [`docs/datasets.md`](docs/datasets.md) | 推荐训练数据集及各模型规模对应的 Token 预算指南 |

---

## 核心假设

Claude Mythos 被认为是一种**循环深度 Transformer（Recurrent-Depth Transformer, RDT）**——也称为循环 Transformer（Looped Transformer, LT）。它并非堆叠数百个独立层，而是复用部分网络结构，在前向传播中多次执行。权重共享，循环次数增加，推理更深。

这并非思维链（Chain-of-Thought）。过程中不输出任何中间 Token。所有推理均在**单次前向传播内部、连续潜空间中以静默方式完成**。

---

## 架构设计

循环 Transformer 将网络层划分为三个功能模块：

```
Input
  ↓
[Prelude P]        — standard transformer layers, run once
  ↓
[Recurrent Block R] — looped T times
  ↑_______↓         (hidden state h updated each loop with input injection e)
  ↓
[Coda C]           — standard transformer layers, run once
  ↓
Output
```

递归模块在每次循环步骤 `t` 的更新规则如下：

```
h_{t+1} = A·h_t + B·e + Transformer(h_t, e)
```

**参数说明：**
- `h_t`：第 `t` 次循环后的隐藏状态
- `e`：编码输入（来自序曲模块），在每次循环中注入
- `A` 和 `B`：学习到的注入参数
- Transformer 块按常规方式执行注意力计算与多层感知机（MLP）操作

在每一步注入 `e` 可防止模型状态漂移——它确保原始输入信号在整个递归深度中始终保持活跃。

完整实现位于 [`open_mythos/main.py`](open_mythos/main.py)。详见 [`OpenMythos` 类参考文档](docs/open_mythos.md)，其中包含详细的 API 说明、配置选项及使用示例。

### 注意力机制实现

注意力层可通过 `cfg.attn_type` 进行切换：

| 选项 | 类名 | 说明 |
|---|---|---|
| `"gqa"` | `GQAttention` | 分组查询注意力（Grouped Query Attention）(Ainslie et al., 2023) —— KV 头数量少于 Q 头 (`n_kv_heads < n_heads`)，将 KV-cache 内存占用降低至原来的 `n_heads / n_kv_heads`。当安装 `flash-attn>=2.8.3` 时会使用 **Flash Attention 2** (Dao et al., 2023)：原生支持 GQA（无需扩展 KV 头），实现 I/O 最优，若未安装该包则自动透明回退至手动缩放点积注意力。 |
| `"mla"` | `MLAttention` | 多潜注意力（Multi-Latent Attention）(DeepSeek-V2) —— 缓存压缩后的 KV 潜变量 (`kv_lora_rank`) 而非完整 K/V，采用分离的 RoPE / 无 RoPE 头维度以实现位置感知压缩。 |

缓存前会对 Q 和 K 应用 RoPE，因此检索时缓存值无需重新旋转。

---

## 为何该架构能解释 Mythos 的行为

### 1. 系统性泛化能力

传统 Transformer 难以组合训练中从未见过的知识模式。循环 Transformer 则能顺利通过此项测试。该能力的涌现经历了一个**三阶段顿悟（grokking）过程**：

1. 记忆阶段 —— 模型拟合训练数据分布
2. 分布内泛化 —— 模型处理已知组合
3. 系统性泛化 —— 模型以突变且突然的方式处理分布外（OOD）的新颖组合

这就是为什么 Mythos 在面对新颖问题时表现出与其他模型截然不同的定性差异——其能力是发生相变式跃迁，而非渐进式涌现。

### 2. 深度外推能力

在 5跳推理链上训练，测试时输入 10跳。传统 Transformer 会失败，而循环 Transformer 能通过增加推理时的循环次数来成功解决。这直接印证了 Mythos 无需显式思维链即可处理深度组合问题（如多步数学、长程规划、分层论证）的观察结果。

更多循环次数 = 更深的推理链 = 解决更复杂的问题。

### 3. 潜变量思考作为隐式思维链

每次循环迭代在功能上等价于思维链（CoT）的一步，但它在连续潜空间而非 Token 空间中运行。执行 `T` 次循环的模型隐式地模拟了 `T` 步 CoT 推理。这在理论上已得到证明 (Saunshi et al., 2025)。

此外，连续的潜变量思考——与离散的 Token 输出不同——能够**同时编码多个备选下一步**。这使得模型能够在推理空间中进行类似广度优先搜索（BFS）的探索，而非局限于单一的推理路径。模型实际上是在每次前向传播收敛之前，内部并行探索多种可能方向。

### 4. 无参数量爆炸

一个包含 `k` 层网络并循环执行 `L` 次的模型，其效果可达到拥有 `k×L` 层的非循环模型水平，但参数量仅相当于 `k` 层。对于 Mythos 规模的部署而言，这具有重大意义：

- 显存占用不会随推理深度增加而膨胀
- 推理计算量仅随循环次数扩展，与模型规模无关
- 这使得在参数量不变的情况下实现更深层次的推理成为可能（“免费”加深）

---

## 稳定性问题（及可能的解决方案）

训练循环模型以极不稳定著称。主要存在两种失败模式：

- **残差爆炸（Residual Explosion）** —— 隐藏状态 `h_t` 在多次循环中无界增长
- **损失值尖峰（Loss Spikes）** —— 注入参数的谱范数过大导致训练突然发散

### 动力系统视角

将循环过程重构为残差流上的离散线性时不变（LTI）动力系统。忽略非线性 Transformer 的贡献后，递推关系变为：

```
h_{t+1} = A·h_t + B·e
```

对于该 LTI 系统，稳定性完全由矩阵 `A` 的**谱半径（Spectral Radius）**决定：
- `ρ(A) < 1` —— 稳定且收敛
- `ρ(A) ≥ 1` —— 不稳定且发散

经验表明，所有发散的训练过程最终都会学到 `ρ(A) ≥ 1`。而所有收敛的训练过程均能维持 `ρ(A) < 1`。

### 解决方案

对注入参数施加约束，以确保稳定性在结构上得到保证：

1. 将 `A` 参数化为连续负对角矩阵
2. 使用零阶保持（ZOH）/欧拉法进行离散化：`A_discrete = exp(Δt · A_continuous)`
3. 通过 `A := Diag(-exp(log_A))` 强制负值，并引入可学习标量 `Δt`
4. 无论学习率或批次噪声如何变化，此设计均能确保 `ρ(A) < 1` 恒成立

效果：循环模型对超参数选择的鲁棒性显著提升，即使在高学习率下也能稳定训练。这就是 Parcae 架构 (Prairie et al., 2026)，也是 Anthropic 最可能采用的使 Mythos 可训练的解决方案类别。

---

## 循环模型的缩放定律

Parcae 确立了首个可预测的循环训练缩放定律：

- **训练阶段**：在固定参数量与算力预算下，增加平均循环次数并减少 Token 数量，比使用少量循环处理更多数据能获得更低的损失。最优循环次数与最优 Token 数量均遵循**幂律（Power Laws）**，且指数在不同规模下保持一致。
- **推理阶段**：增加测试时的循环次数可按**可预测的饱和指数衰减规律**提升质量——收益真实但边际递减。这与思维链（CoT）的推理时缩放特性类似。

在 7.7亿参数量下，循环模型可达到与同数据训练的 13亿参数固定深度 Transformer 相当的下游性能——仅用**一半的参数量实现同等质量**。

应用于 Mythos：若遵循这些缩放定律训练，Mythos 的实际参数量效率可能远超表面所见。其表观“能力”的很大一部分来源于循环深度，而非原始参数量。

---

## 循环索引嵌入假设

一个关键未解问题是：循环模块在每次迭代中是否以**完全相同的方式运行**，还是能够学习在不同循环深度下执行不同的操作。

若缺乏跨循环的位置信号，同一组权重必须同时处理早期模式匹配与后期精调——这是一个严格的约束。若在每一步将输入与**类似 RoPE 的循环索引嵌入（Loop Index Embedding）**一同注入，即可让相同参数在不同迭代中实现功能各异的运算，类似于 RoPE 使注意力头在不同序列位置表现出不同行为的方式。

若 Mythos 采用此技术，则每次循环并非简单重复——而是独立的计算阶段。所有阶段共享权重，但运行在不同的表征空间中。这将显著提升递归模块的表达能力，而无需增加参数量。

---

## 过度思考问题

更多循环次数并不总是更好。超过某一深度后，过度的递归会**降低预测质量**——隐藏状态会越过最优解并陷入噪声。这就是“过度思考（Overthinking）”失败模式。

早期的通用 Transformer（Universal Transformer, Dehghani et al., 2018）通过**自适应计算时间（Adaptive Computation Time, ACT）**的停止机制解决了此问题：为每个位置学习一个标量，动态决定何时终止循环。处理难度较高的位置获得更多计算资源；简单 Token 则提前停止。

Mythos 几乎必然包含类似机制。模型无法对每个输入盲目执行最大循环次数——它需要一个学习到的信号来判断答案是否已收敛。ACT 机制还在特定假设下使模型具备**图灵完备性（Turing-complete）**，这对其可解决问题的类别具有理论意义。

---

## 混合专家模型（MoE）——大参数量下的合理推测

循环 Transformer 解释了 Mythos 推理的深度，但无法解释其广度。仅凭一组权重处理代码、数学、文学、科学、法律等截然不同的领域，必须依赖**混合专家模型（Mixture of Experts, MoE）**。推测的设计是将递归模块中的每个前馈网络（FFN）替换为细粒度 MoE 层：每个 FFN 被拆分为多个小型专家（规模为常规的 `1/m`），路由器通过学习的亲和度分数为每个 Token 选择 Top-mK 个专家，同时始终激活少量**共享专家**以吸收跨领域的通用知识——如语法、基础推理、通用上下文等——否则这些知识会被所有路由专家冗余学习。通过在训练期间动态调整路由器 logits 的偏置项来防止路由坍塌（Routing Collapse），从而在不扭曲损失信号的前提下保持各专家负载平衡。 

随着隐藏状态 `h_t` 在循环迭代中演变，路由器可能在每个深度选择不同的专家子集，使得尽管权重共享，每次循环的计算过程依然不同。MoE 提供广度，循环提供深度。若激活比例约为 5%，Mythos 可能拥有数千亿总参数量，但每个 Token 仅激活其中极小一部分——即使未来公开其真实参数量，那也将是存储数字而非实际计算量。

---

## 记忆与推理的权衡

循环模型呈现出一种有趣的二元性：循环机制能提升推理能力，但可能损害记忆表现。该递归结构专为迭代式组合优化——即向前运行推理链——但并不天然改善死记硬背类事实的存储。

这对应了 Mythos 的一个可观测特征：它对从未见过的新颖问题推理能力极强，但事实回忆表现却不稳定。该架构在结构上更偏向组合推理而非记忆存储。

基于循环的正则化方法（Saunshi et al., 2025）可用于在训练期间平衡此权衡——对推理任务施加更强的循环约束，而对检索任务放宽限制。

---

## 通过 LoRA 适配实现参数复用

来自松弛递归 Transformer（Relaxed Recursive Transformers, Bae et al., 2024）的补充方案：无需在每次循环中强制权重完全一致，而是在每次迭代时添加一个小型**深度方向 LoRA 模块**。这既保留了参数共享的紧凑性，又允许每个循环微调其行为。

效果：
- 每次循环共享大型公共权重矩阵（递归基础）
- 小型秩为 `r` 的适配矩阵使行为随迭代深度发生偏移
- 总参数量开销极小

此方案弥合了纯权重绑定（极致节省参数但表达能力有限）与完全独立层（极致表达但无参数量优势）之间的差距。Mythos 很可能处于该谱系的某个位置。

---

## 连续深度批处理

递归架构的衍生优势：**连续深度批处理（Continuous Depth-wise Batching）**。由于所有 Token 共享同一递归模块，模型允许不同 Token 或序列在不同深度退出循环——简单输入快速处理，复杂输入增加迭代次数，全部在同一批次内完成。

理论分析表明推理吞吐量可提升 2~3 倍。对于像 Mythos 这样同时服务大量用户的部署模型而言，这将带来显著的效率增益。

---

## 总结：Mythos 的可能形态

| 属性 | 说明 |
|---|---|
| 架构 | 循环深度 Transformer（序曲 + 循环递归模块 + 尾声） |
| FFN 层 | 推测为 MoE —— 细粒度专家 + 始终激活的共享专家 |
| 参数量 | 总量极大；每个 Token 仅激活极小部分（约 5%） |
| 推理机制 | 通过迭代潜变量更新实现隐式多跳推理 —— 步骤间无 Token 输出 |
| 推理时缩放 | 更多循环 = 更深推理，遵循可预测的指数衰减规律 |
| 训练稳定性 | LTI 约束注入参数，谱半径 < 1 |
| 循环区分 | 可能采用类似 RoPE 的每迭代循环索引位置嵌入 |
| 停止机制 | 自适应计算时间（ACT）或学习到的收敛判据 |
| 注意力机制 | GQA（可选 Flash Attention 2）或带压缩 KV 潜缓存的 MLA |
| 缩放定律 | 最优训练需同步扩展循环次数与数据量，而非仅增加参数量 |
| 推理 vs 记忆 | 结构上偏向组合推理；记忆功能需额外处理 |
| 部署特性 | 连续深度批处理支持按请求动态分配计算资源 |

---

## References

### Twitter / X

- Why Claude Mythos is so good — looped transformer theory (Sigrid Jin): https://x.com/realsigridjin/status/2044620031410266276
- LT implicit reasoning over parametric knowledge unlocks generalization (Yuekun Yao): https://x.com/yuekun_yao/status/2044229171627639004
- Looped transformer cyclic trajectories and input injection (rosinality): https://x.com/rosinality/status/2043953033428541853
- Parcae scaling laws for stable looped language models — thread (Hayden Prairie): https://x.com/hayden_prairie/status/2044453231913537927
- RoPE-like loop index embedding idea to differentiate functions across iterations (davidad): https://x.com/davidad/status/2044453231913537927
- On the Looped Transformers Controversy by ChrisHayduk: https://x.com/ChrisHayduk/status/2045947623572688943
- On the Looped Transformers Controversy Summary by @realsigridjin https://x.com/realsigridjin/status/2046012743778766875


### 论文

- Fine-grained expert segmentation and shared expert isolation in MoE: https://arxiv.org/abs/2401.06066
- Loop, Think, & Generalize — Implicit Reasoning in Recurrent Depth Transformers: https://arxiv.org/pdf/2604.07822
- Parcae — Scaling Laws for Stable Looped Language Models: https://arxiv.org/abs/2604.12946
- Parcae blog: https://sandyresearch.github.io/parcae/
- Universal Transformers: https://arxiv.org/pdf/1807.03819
- Reasoning with Latent Thoughts — On the Power of Looped Transformers: https://arxiv.org/abs/2502.17416
- Training Large Language Models to Reason in a Continuous Latent Space: https://arxiv.org/abs/2412.06769
- Relaxed Recursive Transformers — Effective Parameter Sharing with Layer-wise LoRA: https://arxiv.org/pdf/2410.20672
- Mixture-of-Depths Attention: https://arxiv.org/abs/2603.15619
- Hyperloop Transformers: https://arxiv.org/abs/2604.21254
- The Recurrent Transformer: Greater Effective Depth and Efficient Decoding: https://arxiv.org/abs/2604.21215
- LT2: Linear-Time Looped Transformers: https://arxiv.org/pdf/2605.20670

---

## 引用

若在你的研究中使用 OpenMythos 或基于此工作展开，请引用：

```bibtex
@software{gomez2026openmythos,
  author    = {Kye Gomez},
  title     = {OpenMythos: A Theoretical Reconstruction of the Claude Mythos Architecture},
  year      = {2026},
  url       = {https://github.com/kyegomez/OpenMythos},
  note      = {Recurrent-Depth Transformer with MoE, MLA, LTI-stable injection, and ACT halting}
}
```

---

## 许可证

MIT License — Copyright (c) 2026 Kye Gomez. See [`LICENSE`](LICENSE) for the full text.