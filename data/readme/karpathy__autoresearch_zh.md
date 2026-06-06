# autoresearch

![teaser](progress.png)

*“曾经，前沿 AI 研究是由‘肉鸡’（meat computers，指人类）在吃饭、睡觉、娱乐以及偶尔通过声波互联进行同步的‘团队会议’仪式中完成的。那个时代早已远去。如今的研究完全由自主运行的 AI Agent 集群主导，它们在云端计算集群巨型架构上协同工作。据这些 Agent 声称，代码库目前已迭代到第 10,205 代；无论如何，没人能判断这是否正确，因为‘代码’现在是一个自我修改的二进制文件，其复杂度已超出人类的理解范畴。这个仓库记录了这一切是如何开始的。——@karpathy, 2026年3月”*

核心思路：给一个 AI Agent 提供一个小型但真实的 LLM（大语言模型）训练环境，让它通宵自主实验。它会修改代码、运行 5 分钟训练、检查结果是否提升、保留或丢弃结果，然后重复该过程。第二天早上醒来，你会看到一份实验日志以及（希望是）性能更好的模型。这里的训练代码是 [nanochat](https://github.com/karpathy/nanochat) 的简化单 GPU 实现。核心理念在于：你不需要像传统研究员那样直接修改任何 Python 文件。相反，你是在编写 `program.md` Markdown 文件，这些文件为 AI Agent 提供上下文并搭建你的自主研究组织（research org）。本仓库中默认的 `program.md` 故意保持为最简基线版本；显然，随着时间的推移，你可以迭代它来找到能实现最快科研进度的“研究组织代码”，以及如何引入更多 Agent 等。关于该项目的更多背景可参考这条 [推文](https://x.com/karpathy/status/2029701092347630069) 和 [这条推文](https://x.com/karpathy/status/2031135152349524125)。

## How it works

本仓库刻意保持精简，实际上只有三个核心文件：

- **`prepare.py`** —— 固定常量、一次性数据预处理（下载训练数据、训练 BPE 分词器）以及运行时工具函数（dataloader 数据加载器、评估）。此文件不会被修改。
- **`train.py`** —— Agent 唯一会编辑的文件。包含完整的 GPT 模型、优化器（Muon + AdamW）以及训练循环。所有内容均可调整：架构、超参数、优化器、batch size 等。**此文件由 Agent 编辑和迭代**。
- **`program.md`** —— 单个 Agent 的基础指令。将你的 Agent 指向此处即可放手让它运行。**此文件由人类编辑和迭代**。

设计上，训练任务始终运行一个**固定的 5 分钟时间预算**（wall clock 墙钟时间，不含启动/编译耗时），与你的计算设备细节无关。评估指标为 **val_bpb**（验证集每字节比特数 validation bits per byte）——数值越低越好，且该指标独立于词表大小 vocab-size，因此可以公平地比较架构变化带来的影响。

如果你是神经网络新手，这篇 [“小白指南”](https://x.com/hooeem/status/2030720614752039185) 提供了丰富的背景知识，非常值得一读。

## Quick start

**环境要求：** 单张 NVIDIA GPU（已在 H100 上测试）、Python 3.10+、[uv](https://docs.astral.sh/uv/)。

```bash
# 1. Install uv project manager (if you don't already have it)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Install dependencies
uv sync

# 3. Download data and train tokenizer (one-time, ~2 min)
uv run prepare.py

# 4. Manually run a single training experiment (~5 min)
uv run train.py
```

如果上述命令均运行正常，说明你的环境配置已完成，可以进入自主研究模式。

## Running the agent

只需在此仓库中启动你使用的 Claude/Codex（或任意其他工具，并确保禁用所有权限），然后输入类似以下的提示词：

```
Hi have a look at program.md and let's kick off a new experiment! let's do the setup first.
```

`program.md` 文件本质上是一个超轻量级的“技能（skill）”定义。

## Project structure

```
prepare.py      — constants, data prep + runtime utilities (do not modify)
train.py        — model, optimizer, training loop (agent modifies this)
program.md      — agent instructions
pyproject.toml  — dependencies
```

## Design choices

- **仅修改单个文件。** Agent 只会操作 `train.py`。这能有效控制变更范围，并使代码差异（diffs）易于审查。
- **固定时间预算。** 无论你的具体平台如何，训练任务始终精确运行 5 分钟。这意味着你大约可以期望每小时完成 12 次实验，睡眠期间约可完成 100 次实验。该设计有两个优势：首先，这使得实验结果具有直接可比性，不受 Agent 修改内容（如模型大小、batch size、架构等）的影响；其次，这意味着 autoresearch 会在该时间预算内为你的平台找到最优模型。缺点是，你的运行过程及结果将难以与其他人在不同计算平台上运行的结果进行对比。
- **高度自包含。** 除 PyTorch 和少量基础包外，无其他外部依赖。无需分布式训练，无需复杂配置。单张 GPU、单个文件、单一指标。

## Platform support

当前代码仅要求配备单张 NVIDIA GPU。原则上完全支持 CPU、MPS 及其他平台，但这会导致代码体积膨胀。目前我个人并不打算亲自接手这部分工作。你可以参考（或让 Agent 参考）完整的/父级 nanochat 仓库，该仓库提供了更广泛的平台支持及多种解决方案（例如 Flash Attention 3 内核回退实现、通用设备支持、自动检测等）。欢迎为其他平台创建 Fork 或发起讨论，我很乐意在 README 的“知名 Fork”章节中链接它们。

鉴于似乎有很多人在远小于 H100 的计算平台上尝试折腾 autoresearch，这里补充几句。如果你打算在较小的计算机（如 MacBook 等）上运行 autoresearch，建议参考下方的某个 Fork。此外，以下是针对更小模型调整默认参数的建议：

1. 为了获得尚可的结果，建议使用熵（entropy）低得多的数据集，例如这个 [TinyStories 数据集](https://huggingface.co/datasets/karpathy/tinystories-gpt4-clean)。这些是由 GPT-4 生成的短篇故事。由于数据范围较窄，使用小得多的模型也能得到合理结果（训练后采样即可验证）。
2. 可以尝试减小 `vocab_size`，例如从 8192 降至 4096、2048、1024，甚至直接使用 UTF-8 编码后的字节级分词器（byte-level tokenizer），仅包含 256 个可能字节。
3. 在 `prepare.py` 中，你需要大幅降低 `MAX_SEQ_LEN`，根据电脑性能甚至可降至 256。随着 `MAX_SEQ_LEN` 的减小，你可能需要尝试略微增加 `train.py` 中的 `DEVICE_BATCH_SIZE` 以作补偿。每次前向/反向传播（fwd/bwd pass）处理的 token 数量是这两者的乘积。
4. 同样在 `prepare.py` 中，你需要减小 `EVAL_TOKENS`，以便用更少的数据评估验证损失（validation loss）。
5. 在 `train.py` 中，控制模型复杂度的核心单一参数是 `DEPTH`（此处默认为 8）。许多变量都是基于它计算的，因此可将其降至例如 4。
6. 你大概率需要仅使用 `"L"` 作为 `WINDOW_PATTERN`，因为 `"SSSL"` 使用的交替带状注意力模式（alternating banded attention pattern）在你平台上可能效率极低。可以试试其他组合。
7. 你需要大幅降低 `TOTAL_BATCH_SIZE`，但保持其为 2 的幂次方，例如降至 `2**14`（约 16K）甚至更低，具体视情况而定。

我认为这些是合理的可调超参数。不妨让你的编程 Agent 帮忙调整，并将本指南及完整源代码粘贴给它即可。

## Notable forks

- [miolini/autoresearch-macos](https://github.com/miolini/autoresearch-macos)（MacOS）
- [trevin-creator/autoresearch-mlx](https://github.com/trevin-creator/autoresearch-mlx)（MacOS）
- [jsegov/autoresearch-win-rtx](https://github.com/jsegov/autoresearch-win-rtx)（Windows）
- [andyluo7/autoresearch](https://github.com/andyluo7/autoresearch)（AMD）

## License

MIT