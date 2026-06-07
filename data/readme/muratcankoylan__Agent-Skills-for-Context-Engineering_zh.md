# 用于上下文工程（Context Engineering）的智能体技能

一个全面、开源的集合，专注于上下文工程和 Harness（运行框架）工程原则，旨在构建生产级 AI 智能体系统。这些技能教授如何精心策展上下文信息、设计智能体运行循环，并在任何智能体平台上评估智能体行为。

[DeepWiki：在此了解更多](https://deepwiki.com/muratcankoylan/Agent-Skills-for-Context-Engineering)

## 什么是上下文工程？

上下文工程是管理大语言模型（LLM）上下文窗口的学科。与专注于编写有效指令的提示词工程不同，上下文工程关注的是如何全面策展进入模型有限注意力预算的所有信息：系统提示、工具定义、检索文档、消息历史以及工具输出。

核心挑战在于，上下文窗口受限于注意力机制而非原始 token 容量。随着上下文长度增加，模型会表现出可预测的退化模式：“中间丢失”现象（lost-in-the-middle）、U型注意力曲线以及注意力稀缺性。有效的上下文工程意味着找到尽可能小的、高信号密度的 token 集合，以最大化期望结果的概率。

## 引用与认可

该仓库被学术研究引用为静态技能架构的基础工作：

> “尽管静态技能已得到广泛认可 [Anthropic, 2025b; Muratcan Koylan, 2025]，但 MCE（元上下文工程）是首批动态演进这些技能的方案之一 bridging manual skill engineering and autonomous self-improvement.”
1. [Meta Context Engineering via Agentic Skill Evolution](https://arxiv.org/pdf/2601.21557)，北京大学通用人工智能全国重点实验室 (2025)
2. [Agent Harness Engineering: A Survey](https://openreview.net/pdf/f358711a95aaaf61fdeffd4ef3fc60fba9b8da57.pdf)，CMU、Yale、JHU、NEU、Tulane、UAB、OSU、Virginia Tech 及 Amazon (2026)

## 技能概览

### 基础技能（Foundational Skills）

这些技能为后续所有上下文工程工作奠定理解基础。

| 技能 | 描述 |
|-------|-------------|
| [context-fundamentals](skills/context-fundamentals/) | 理解上下文的定义、重要性，以及智能体系统中上下文的构成要素 |
| [context-degradation](skills/context-degradation/) | 识别上下文失效模式：中间丢失、污染（poisoning）、干扰（distraction）与冲突（clash） |
| [context-compression](skills/context-compression/) | 设计与评估长会话场景下的压缩策略 |

### 架构技能（Architectural Skills）

这些技能涵盖构建高效智能体系统的模式与结构。

| 技能 | 描述 |
|-------|-------------|
| [multi-agent-patterns](skills/multi-agent-patterns/) | 掌握编排器、对等网络及分层多智能体架构 |
| [memory-systems](skills/memory-systems/) | 设计短期、长期及基于图结构的记忆架构 |
| [tool-design](skills/tool-design/) | 构建智能体可高效使用的工具 |
| [filesystem-context](skills/filesystem-context/) | 利用文件系统实现动态上下文发现、工具输出卸载与计划持久化 |
| [hosted-agents](skills/hosted-agents/) | **新增** 使用沙盒虚拟机、预构建镜像、多人协作支持及多客户端接口构建后台编码智能体 |

### 操作技能（Operational Skills）

这些技能解决智能体系统的持续运行与优化问题。

| 技能 | 描述 |
|-------|-------------|
| [context-optimization](skills/context-optimization/) | 应用压缩、掩码和缓存策略 |
| [latent-briefing](skills/latent-briefing/) | 当工作节点运行时环境可控时，通过任务引导的 KV Cache 压缩向工作节点共享编排器状态 |
| [evaluation](skills/evaluation/) | 构建智能体系统的评估框架 |
| [advanced-evaluation](skills/advanced-evaluation/) | 掌握 LLM 作为裁判（LLM-as-a-Judge）技术：直接打分、成对比较、评分标准生成及偏差缓解 |
| [harness-engineering](skills/harness-engineering/) | 设计具备锁定指标、持久化日志、新颖性门控（novelty gates）、回滚机制与人工审批边界的自主智能体运行框架 |

### 开发方法论（Development Methodology）

这些技能涵盖构建 LLM 驱动项目的元级实践。

| 技能 | 描述 |
|-------|-------------|
| [project-development](skills/project-development/) | 从构思到部署设计与构建 LLM 项目，包括任务-模型适配分析、流水线架构与结构化输出设计 |

### 认知架构技能（Cognitive Architecture Skills）

这些技能涵盖理性智能体系统的形式化认知建模。

| 技能 | 描述 |
|-------|-------------|
| [bdi-mental-states](skills/bdi-mental-states/) | **新增** 使用形式化 BDI（信念-愿望-意图）本体模式将外部 RDF 上下文转换为智能体心理状态（信念、欲望、意图），以实现审慎推理和可解释性 |

## 设计哲学

### 渐进式披露（Progressive Disclosure）

每个技能的结构均针对高效上下文使用进行了优化。启动时，智能体仅加载技能名称与描述。完整内容仅在激活相关任务所需的技能时才加载。

### 平台无关性（Platform Agnosticism）

这些技能聚焦于可迁移的原则，而非特定厂商的实现方案。这些模式适用于 Claude Code、Cursor 以及任何支持技能或允许自定义指令的智能体平台。

### 概念基础与实践示例结合（Conceptual Foundation with Practical Examples）

脚本与示例使用跨环境兼容的 Python 伪代码演示概念，无需安装特定依赖即可运行。

## 使用方法

### 与 Claude Code 配合使用

该仓库是一个 **Claude Code 插件市场**，包含 Claude 会根据你的任务上下文自动发现并激活的上下文工程技能。

### 安装

**步骤 1：添加市场源**

在 Claude Code 中运行以下命令以注册此仓库为插件源：

```
/plugin marketplace add muratcankoylan/Agent-Skills-for-Context-Engineering
```

**步骤 2：安装插件**

选项 A - 浏览并安装：
1. 选择 `Browse and install plugins`（浏览并安装插件）
2. 选择 `context-engineering-marketplace`
3. 选择 `context-engineering`
4. 选择 `Install now`（立即安装）

选项 B - 通过命令直接安装：

```
/plugin install context-engineering@context-engineering-marketplace
```

这将一次性安装全部 15 个技能。技能会根据你的任务上下文自动激活。

### 技能激活场景

| 技能 | 激活条件 |
|-------|---------------|
| `context-fundamentals` | 建立上下文窗口心智模型、规划智能体架构，或解释上下文组件如何影响模型行为时 |
| `context-degradation` | 诊断注意力失效、上下文污染、中间丢失行为，或在长会话中评估性能下降时 |
| `context-compression` | 在上下文压力下保留有效状态，同时缩减对话、工具输出或轨迹大小时 |
| `context-optimization` | 提升 token 效率、检索精度、前缀复用、掩码处理、分区策略或预算分配时 |
| `latent-briefing` | 当工作节点运行时环境可控且模型兼容时，通过任务引导的 KV Cache 压缩向工作节点共享编排器轨迹 |
| `multi-agent-patterns` | 选择协调模式、隔离智能体间上下文、设计交接流程，或评估并行智能体是否合理时 |
| `memory-systems` | 持久化跨会话知识、追踪实体随时间的变化、选择记忆框架，或设计检索与更新语义时 |
| `tool-design` | 定义智能体-工具契约、整合工具入口、优化描述，或将工具错误转化为可操作信息时 |
| `filesystem-context` | 将大型或持久化上下文移至文件、创建临时工作区（scratchpads）、支持即时发现，或通过共享工件协调智能体时 |
| `hosted-agents` | 在远程沙盒、后台环境、预热池或多玩家智能体基础设施中运行编码智能体时 |
| `evaluation` | 为智能体行为创建确定性检查项、评分标准、回归测试套件、生产监控或质量门禁时 |
| `advanced-evaluation` | 使用 LLM 裁判、成对比较、校准、偏差缓解或与人类对齐的质量评估时 |
| `harness-engineering` | 设计具备锁定评估器、可编辑入口、持久化日志、新颖性门控、回滚与审批边界的自主循环时 |
| `project-development` | 判断 LLM 是否适用、构建批处理流水线、创建分阶段工件，或估算运营成本时 |
| `bdi-mental-states` | 建模信念、欲望、意图、理性行为轨迹，或智能体的神经符号状态转换时 |

<img width="1014" height="894" alt="Screenshot 2025-12-26 at 12 34 47 PM" src="https://github.com/user-attachments/assets/f79aaf03-fd2d-4c71-a630-7027adeb9bfe" />

### 适用于 Cursor（开放插件）

该仓库已收录于 [Cursor 插件目录](https://cursor.directory/plugins/context-engineering)。

`.plugin/plugin.json` 清单遵循 [Open Plugins](https://open-plugins.com) 标准，因此该仓库也可与任何兼容的智能体工具（如 Codex、GitHub Copilot 等）配合使用。

### 单独使用某个技能

若无需安装完整插件即可使用单个技能，可将其 `SKILL.md` 直接复制到项目的 `.claude/skills/` 目录中：

```bash
# 示例：仅添加 context-fundamentals 技能
mkdir -p .claude/skills
curl -o .claude/skills/context-fundamentals.md \
  https://raw.githubusercontent.com/muratcankoylan/Agent-Skills-for-Context-Engineering/main/skills/context-fundamentals/SKILL.md
```

可用技能：`context-fundamentals`, `context-degradation`, `context-compression`, `context-optimization`, `latent-briefing`, `multi-agent-patterns`, `memory-systems`, `tool-design`, `filesystem-context`, `hosted-agents`, `evaluation`, `advanced-evaluation`, `harness-engineering`, `project-development`, `bdi-mental-states`

### 用于自定义实现

提取任意技能中的原则与模式，并在你的智能体框架中自行实现。这些技能刻意保持平台无关性。

## 示例

[examples](examples/) 文件夹包含完整的系统设计，演示多个技能如何在实际场景中协同工作。

| 示例 | 描述 | 应用技能 |
|---------|-------------|----------------|
| [digital-brain-skill](examples/digital-brain-skill/) | **新增** 创始人和创作者的个人操作系统。完整的 Claude Code 技能，含 6 个模块与 4 个自动化脚本 | context-fundamentals, context-optimization, memory-systems, tool-design, multi-agent-patterns, evaluation, project-development |
| [x-to-book-system](examples/x-to-book-system/) | 监控 X（原 Twitter）账号并生成每日合成书籍的多智能体系统 | multi-agent-patterns, memory-systems, context-optimization, tool-design, evaluation |
| [llm-as-judge-skills](examples/llm-as-judge-skills/) | 生产就绪的 LLM 评估工具，含 TypeScript 实现与 19 项通过测试 | advanced-evaluation, tool-design, context-fundamentals, evaluation |
| [book-sft-pipeline](examples/book-sft-pipeline/) | 训练模型以任意作者风格写作。包含 Gertrude Stein 案例研究（Pangram 数据集人类评分达 70%，总成本仅 $2） | project-development, context-compression, multi-agent-patterns, evaluation |
| [interleaved-thinking](examples/interleaved-thinking/) | 推理轨迹优化器，捕获、分析并将智能体失败模式转化为生成的技能 | evaluation, advanced-evaluation, context-degradation, harness-engineering |

每个示例均包含：
- 完整的 PRD（产品需求文档）与架构决策说明
- 技能映射表，展示哪些概念支撑了各项决策
- 实施指导

### 数字大脑技能示例

[digital-brain-skill](examples/digital-brain-skill/) 示例是一个完整的个人操作系统，展示了综合技能的全面应用：

- **渐进式披露**：3级加载机制（SKILL.md → MODULE.md → data files）
- **模块隔离**：6个独立模块（身份、内容、知识、网络、操作、智能体）
- **仅追加记忆（Append-Only Memory）**：JSONL 文件配合首行 Schema，便于智能体解析
- **自动化脚本**：4个整合工具（weekly_review, content_ideas, stale_contacts, idea_to_draft）

在 [HOW-SKILLS-BUILT-THIS.md](examples/digital-brain-skill/HOW-SKILLS-BUILT-THIS.md) 中提供了详细的可追溯性记录，将每项架构决策映射到具体的技能原则。

### LLM 作为裁判的技能示例

[llm-as-judge-skills](examples/llm-as-judge-skills/) 示例是一个完整的 TypeScript 实现，展示了：

- **直接打分**：基于加权标准评估响应（支持评分标准）
- **成对比较**：对比响应并缓解位置偏差
- **评分标准生成**：创建领域特定的评估标准
- **EvaluatorAgent**：高级智能体整合所有评估能力

### 书籍 SFT 流水线示例

[book-sft-pipeline](examples/book-sft-pipeline/) 示例演示了如何训练小型模型（8B）以任意作者风格写作：

- **智能分块**：双层分块配合重叠区域，最大化训练样本量
- **提示词多样性**：15+ 模板防止死记硬背并强制风格学习
- **Tinker 集成**：完整的 LoRA 训练工作流，总成本仅 $2
- **验证方法论**：现代场景测试证明风格迁移优于内容记忆

该示例集成了上下文工程技能：project-development, context-compression, multi-agent-patterns, evaluation。

## Researcher（研究者）操作系统

[researcher](researcher/) 目录是一个基于文件的操作系统，用于将外部研究成果转化为技能更新。它的存在使本仓库能够作为持续累积的单一事实来源（source of truth），而非单纯的资料汇编。

### 经测量的技能路由器基准测试结果

负责决定是否为给定任务加载正确技能的“技能路由器”已通过 [Cursor SDK](https://cursor.com/docs/sdk/typescript) 针对四款前沿模型进行了端到端基准测试。三次完整扫描（50 个提示词 × 4 个模型 × 3 次重复 = 各 600 次调用）：

- 基线结果：[`researcher/benchmarks/router/results-published/2026-05-15.md`](researcher/benchmarks/router/results-published/2026-05-15.md)
- 定向描述重写后：[`researcher/benchmarks/router/results-published/2026-05-15-v2.md`](researcher/benchmarks/router/results-published/2026-05-15-v2.md)（含与基线的增量对比）
- 语料库全面加固后：[`researcher/benchmarks/router/results-published/2026-05-19.md`](researcher/benchmarks/router/results-published/2026-05-19.md)（600/600 可用记录，格式失败率为 0）

数据标记的三项技能的单技能效应量：

| 技能 | 基线 Top-1 | 重写后 | 增量 |
| --- | --- | --- | --- |
| `context-fundamentals` | 0.255 | 0.489 | +23.4pp（百分比点） |
| `project-development` | 0.750 | 1.000 | +25pp（已达完美） |
| `tool-design` | 0.729 | 0.807 | +7.8pp |

语料库全面加固后各模型的 Top-1 准确率：

| 模型 | Top-1 | Top-3 |
| --- | --- | --- |
| gemini-3.1-pro | 0.920 | 0.933 |
| composer-2 | 0.913 | 0.947 |
| gpt-5.5 | 0.913 | 0.973 |
| claude-opus-4-7 | 0.840 | 0.933 |

你可通过 `researcher/benchmarks/sdk-runner/` 下的运行器精确复现上述任何数据。

### 包含内容

- **来源注册表**（`researcher/source-registry.md`）：优先级来源、排除规则与监控查询。
- **评分标准**（`researcher/rubrics/`）：内容策展、技能变更、Harness 变更、成对技能修订。
- **机制注册表**（`researcher/mechanisms/registry.jsonl` + `ledgers/`）：16 项已采纳的行为变更作为主要新颖性信号，附带仅追加的已采纳/拒绝账本用于机构记忆。
- **声明溯源**（`researcher/claims/index.jsonl`）：12 条带溯源追踪的声明，含来源 URL、证据强度、波动性与最后审查日期。
- **语料库索引**（`researcher/corpus/index.json`）：技能、激活场景、机制 ID 与声明 ID 的标准机器可读映射。
- **运行状态机**（`researcher/runs/<run-id>/run-state.json`）：`initialized -> retrieved -> evaluated -> proposed -> novelty_checked -> validated -> pr_ready -> closed`。
- **激活回归测试**（`researcher/fixtures/activation-cases.jsonl`）：19 个确定性提示词，用于捕获技能边界混淆问题。
- **对抗性基准 Harness**（`researcher/benchmarks/`）：试图操纵循环的场景（重复机制、未检索证据、错误评分标准计算、自批准评分标准变更、弱证据新颖性等）。
- **持续循环**（`researcher/scripts/loop_*.py` + `researcher/orchestration/launchd/`）：收件箱、来源发现、单步推进、日常运维、暂停审查队列与 launchd 服务定义。
- **技能健康门禁**（`researcher/scripts/skill_health.py`）：确定性内容质量评分；当前严格语料库得分为 0.9117，标记问题技能数为 0。

### 运维命令

```bash
# 确定性门禁（每次 PR 时也在 CI 中运行）
python3 researcher/scripts/validate_repo.py --strict
python3 researcher/scripts/skill_health.py --strict --no-history
python3 researcher/scripts/run_benchmarks.py
python3 researcher/scripts/check_activation_cases.py

# 单次运行就绪检查（仅限活跃运行）
python3 researcher/scripts/validate_run.py --run-dir researcher/runs/<run-id>

# 持续循环，手动执行
python3 researcher/scripts/loop_discover.py
python3 researcher/scripts/loop_step.py --allow-fetch
python3 researcher/scripts/loop_daily.py
python3 researcher/scripts/loop_status.py

# 持续循环，守护进程（macOS）
researcher/orchestration/launchd/install.sh    # 安装 launchd 任务（10分钟步进、12小时发现、日常运维）
researcher/orchestration/launchd/uninstall.sh  # 移除 launchd 任务
```

详见 [researcher/runbooks/continuous-operation.md](researcher/runbooks/continuous-operation.md) 获取守护进程详情、预算配置与人工审查界面说明。

### 保障机制

- 循环绝不会调用付费 LLM 或执行外部写入；HTTP 检索仅使用 stdlib（标准库），限制 1.5 MB 且超时为 30 秒。
- 机制升级需记录人类审核员签名并通过运行就绪检查。
- 所有队列变更均为原子操作（临时文件 + `os.replace`）并通过 `fcntl` 锁序列化。
- 智能体可在门禁通过后准备 PR；合并与推送仍由人工控制。

## Star 历史
<img width="3664" height="2808" alt="star-history-2026526" src="https://github.com/user-attachments/assets/c9f88769-21b8-4762-9472-d4cf1fe1c802" />

## 目录结构

每个技能均遵循 Agent Skills 规范：

```
skill-name/
├── SKILL.md              # 必填：指令与元数据
├── scripts/              # 可选：演示概念的可执行代码
└── references/           # 可选：补充文档与资源
```

详见 [template](template/) 文件夹中的标准技能结构。

## 贡献指南

本仓库遵循 Agent Skills 开放开发模式，欢迎生态系统的广泛参与。贡献时请遵守以下规范：

1. 遵循技能模板结构
2. 提供清晰、可操作的指令
3. 在适当处包含可运行的示例
4. 记录权衡取舍与潜在问题
5. 保持 `SKILL.md` 在 500 行以内以确保最佳性能

欢迎随时联系 [Muratcan Koylan](https://x.com/koylanai) 探讨合作机会或提出疑问。

## 许可证

MIT License - 详见 LICENSE 文件获取详细信息。

## 参考资料

本技能集中的原则源自顶级 AI 实验室与框架开发者的研究与生产实践经验。每项技能均包含指导其建议的底层研究与案例研究参考文献。