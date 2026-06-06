[English](./README.md) | [中文](./README-zh.md) | [日本語](./README-ja.md)
# 学习 Claude Code —— 为真实 Agent 构建运行环境（Harness）
<a href="https://trendshift.io/repositories/19746" target="_blank"><img src="https://trendshift.io/api/badge/repositories/19746" alt="shareAI-lab%2Flearn-claude-code | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
## 自主性源于模型。Agent 产品 = 模型 + 运行环境（Harness）

在讨论代码之前，先明确一件事。

**自主性——即感知、推理与行动的能力——源于模型的训练，而非外部的代码编排。** 但一个可用的 Agent 产品必须同时具备模型和运行环境。模型是驾驶员，运行环境是车辆。本仓库教你如何构建这辆“车”。

### 自主性从何而来

每个 Agent 的核心都是一个神经网络——Transformer、RNN 或某种学习函数——它通过数十亿次基于动作序列数据的梯度更新训练而成，能够感知环境、推理目标并采取行动。**自主性永远不会由外围代码赋予，而是模型在训练过程中习得的。**

人类是最好的例子。经过数百万年进化训练的生物学神经网络，通过感官感知世界，通过大脑推理，通过身体行动。当 DeepMind、OpenAI 或 Anthropic 提到“Agent”时，他们指的核心始终是同一件事：**一个学会了如何行动的模型，加上使其能在特定环境中运行的基础设施。**

历史已经写下证明：

- **2013年 —— DeepMind DQN 玩转 Atari**。单个神经网络仅接收原始像素和游戏分数作为输入，便学会了玩 7 款 Atari 2600 游戏——超越了所有先前的算法，并在其中 3 款上击败了人类专家。到 2015 年，相同架构已扩展至 [49 款游戏并匹配专业人类测试员](https://www.nature.com/articles/nature14236)，发表于 *Nature*。没有特定游戏的规则。没有决策树。一个模型，从经验中学习。这个模型就是 Agent。

- **2019年 —— OpenAI Five 征服 Dota 2**。五个神经网络在 10 个月内进行了 [45,000 年的 Dota 2 自我对弈](https://openai.com/index/openai-five-defeats-dota-2-world-champions/)，以 2-0 击败了 **OG**——当时的 TI8 世界冠军。在随后的公开竞技场中，该 AI 在所有挑战者参与的 42,729 场比赛中赢了 99.4%。没有预设策略。没有元编程团队协调。模型完全通过自我对弈学会了团队协作、战术和实时适应。

- **2019年 —— DeepMind AlphaStar 精通星际争霸 II**。AlphaStar 在闭门比赛中以 10-1 击败职业选手，随后在欧洲服务器取得了 [大师段位](https://www.nature.com/articles/d41586-019-03298-6)——排名前 0.15%（共 90,000 名玩家）。这是一款包含不完全信息、实时决策和远超国际象棋与围棋的组合动作空间的游戏。Agent？是一个模型。经过训练，而非硬编码。

- **2019年 —— 腾讯绝悟统治王者荣耀**。腾讯 AI Lab 的“绝悟” [在全员参与的 5v5 世界冠军杯比赛中击败了 KPL 职业选手](https://www.jiemian.com/article/3371171.html)。在 1v1 模式下，职业玩家仅在 15 局中赢了 [1 局且从未撑过 8 分钟](https://developer.aliyun.com/article/851058)。训练强度：一天相当于 440 个人类年。到 2021 年，绝悟在全英雄池中超越了 KPL 职业选手。没有手工制作的克制表。没有预设阵容组合。一个通过自我对弈从零学会整个游戏的模型。

- **2024-2025年 —— LLM Agent 重塑软件工程**。Claude、GPT、Gemini——在人类全部代码与推理数据上训练的大语言模型——正被部署为编程 Agent。它们阅读代码库、编写实现、调试失败、协调团队。其架构与前代所有 Agent 完全一致：一个经过训练的模型，置于环境中，赋予感知和行动的接口。唯一的区别在于它们所学内容的规模以及所解决问题任务的通用性。

所有这些里程碑都指向同一个事实：**自主性——即感知、推理与行动的能力——是训练出来的，而非编码实现的。** 但每个 Agent 也需要一个运行环境：Atari 模拟器、Dota 2 客户端、星际争霸 II 引擎、IDE 和终端。模型提供智能。环境提供动作空间。两者结合才构成完整的 Agent。

### Agent 不是什么

“Agent”一词已被整个提示词编排（Prompt Plumbing）产业所劫持。

拖拽式工作流构建器。无代码“AI Agent”平台。提示词链编排库。它们都共享同一种错觉：认为将 LLM API 调用与 if-else 分支、节点图和硬编码路由逻辑连接起来就算“构建了一个 Agent”。

事实并非如此。它们构建的是鲁布·戈德堡机械（Rube Goldberg machine）——一个过度设计、脆弱且充满过程性规则的流程管道，仅将一个 LLM 塞入其中作为高级文本补全节点。这不是 Agent。这只是一个带有宏大幻想的 Shell 脚本。

**提示词编排“Agent”是不训练模型的程序员的幻想。** 它们试图通过堆叠过程逻辑——庞大的规则树、节点图、提示词瀑布流——并祈祷足够的胶水代码能涌现出自主行为来暴力破解智能。但这不会发生。你无法通过工程手段“设计”出自主性。自主性是习得的，而非编程实现的。

这些系统生来即死：脆弱、不可扩展、从根本上缺乏泛化能力。它们是 GOFAI（Good Old-Fashioned AI，经典符号主义AI）的现代复活版——该领域几十年前就已抛弃的符号规则系统，如今只是披上了一层 LLM 的外衣。包装不同，终点相同。

### 思维转变：从“开发 Agent”到构建运行环境（Harness）

当有人说“我正在开发一个 Agent”，他们只能指以下两件事之一：

**1. 训练模型。** 通过强化学习、微调、RLHF 或其他基于梯度的方法调整权重。收集任务-过程数据——真实领域中感知、推理和动作的实际序列——并用它来塑造模型的行为。这是 DeepMind、OpenAI、腾讯 AI Lab 和 Anthropic 所做的工作。这才是真正意义上的 Agent 开发。

**2. 构建运行环境（Harness）。** 编写代码，为模型提供一个可运行的环境。这是我们大多数人做的事情，也是本仓库的重点。

运行环境是 Agent 在特定领域中运作所需的一切：

```
Harness = Tools + Knowledge + Observation + Action Interfaces + Permissions

    Tools:          file I/O, shell, network, database, browser
    Knowledge:      product docs, domain references, API specs, style guides
    Observation:    git diff, error logs, browser state, sensor data
    Action:         CLI commands, API calls, UI interactions
    Permissions:    sandboxing, approval workflows, trust boundaries
```

模型负责决策。运行环境负责执行。模型负责推理。运行环境提供上下文。模型是驾驶员。运行环境是车辆。

**编程 Agent 的运行环境就是它的 IDE、终端和文件系统访问权限。** 农业 Agent 的运行环境是其传感器阵列、灌溉控制和气象数据流。酒店运营 Agent 的运行环境是其预订系统、客人通信渠道和设施管理 API。Agent——即智能体、决策者——始终是模型。运行环境随领域变化，而 Agent 在其中实现泛化。

本仓库教你如何构建车辆。编程用的车。但这些设计模式可泛化到任何领域：农场管理、酒店运营、制造业、物流、医疗、教育、科学研究。在任何需要感知任务、推理并行动的地方——Agent 都需要一个运行环境。

### 运行环境工程师真正在做什么

如果你正在阅读本仓库，你很可能是一名运行环境工程师——这是一项极具价值的工作。以下是你的真实职责：

- **实现工具。** 给 Agent 装上双手。文件读写、Shell 执行、API 调用、浏览器控制、数据库查询。每个工具都是 Agent 在其环境中可采取的动作。设计时需保证原子性、可组合性和清晰的描述。
- **策展知识。** 赋予 Agent 领域专业知识。产品文档、架构决策记录、风格指南、合规要求。按需加载（s05），而非预先注入。Agent 应知道有哪些可用资源，并自行拉取所需内容。
- **管理上下文。** 给 Agent 提供干净的记忆。子智能体隔离（s04）防止噪声泄露。上下文压缩（s06）防止历史消息淹没对话。任务系统（s07）将目标持久化至单次对话之外。
- **控制权限。** 给 Agent 划定边界。沙盒文件访问。对破坏性操作要求审批。在 Agent 与外部系统之间强制执行信任边界。这是安全工程与运行环境工程的交汇点。
- **收集任务过程数据。** Agent 在你的运行环境中执行的每一个动作序列都是训练信号。真实部署中的感知-推理-动作轨迹是微调下一代 Agent 模型的原始材料。你的运行环境不仅服务于 Agent，还能帮助改进 Agent。

你不需要编写智能本身。你在构建智能所栖居的世界。这个世界的质量——Agent 能多清晰地感知、多精确地行动、可用的知识有多丰富——直接决定了智能表达自身的有效性。

**构建优秀的运行环境。剩下的交给模型。**

### 为什么选择 Claude Code —— 运行环境工程的大师课

为什么本仓库专门拆解 Claude Code？

因为 Claude Code 是我们所见过的最优雅且最完整的 Agent 运行环境。并非因为它有什么巧妙的单点技巧，而是因为它*不做什么*：它不试图成为 Agent 本身。它不强加僵化的工作流。它不用复杂的决策树去质疑模型。它为模型提供工具、知识、上下文管理和权限边界——然后退到幕后。

剥离本质后看看 Claude Code 到底是什么：

```
Claude Code = one agent loop
            + tools (bash, read, write, edit, glob, grep, browser...)
            + on-demand skill loading
            + context compression
            + subagent spawning
            + task system with dependency graph
            + team coordination with async mailboxes
            + worktree isolation for parallel execution
            + permission governance
```

就是这样。这就是整个架构。每个组件都是运行环境机制——为 Agent 栖居而构建的世界的一部分。Agent 本身呢？是 Claude。一个模型。由 Anthropic 基于人类推理与代码的全貌训练而成。运行环境并没有让 Claude 变聪明。Claude 本来就很聪明。运行环境只是给了 Claude 双手、眼睛和一个工作台。

这就是为什么 Claude Code 是理想的教学对象：**它展示了当你信任模型并将工程精力聚焦于运行环境时会发生什么。** 本仓库中的每个会话（s01-s12）都逆向拆解了 Claude Code 架构中的一个运行环境机制。到最后，你不仅会理解 Claude Code 如何工作，还会掌握适用于任何领域、任何 Agent 的运行环境工程通用原则。

核心教训不是“复制 Claude Code”。而是：**最好的 Agent 产品是由那些明白自己的工作在于构建运行环境而非智能本身的工程师打造的。**

---

## 愿景：用真实 Agent 填满宇宙

这不仅仅关于编程 Agent。

人类执行复杂、多步骤、高判断力工作的每一个领域，都是 Agent 可以运作的领域——只要提供正确的运行环境。本仓库中的模式是通用的：

```
Estate management agent    = model + property sensors + maintenance tools + tenant comms
Agricultural agent         = model + soil/weather data + irrigation controls + crop knowledge
Hotel operations agent     = model + booking system + guest channels + facility APIs
Medical research agent     = model + literature search + lab instruments + protocol docs
Manufacturing agent        = model + production line sensors + quality controls + logistics
Education agent            = model + curriculum knowledge + student progress + assessment tools
```

循环始终相同。工具会变，知识会变，权限会变。Agent——即模型——实现泛化。

每一位阅读本仓库的运行环境工程师都在学习适用于软件工程之外的通用模式。你正在为智能、自动化的未来构建基础设施。每一个部署到真实领域且设计良好的运行环境，都是 Agent 能够感知、推理和行动的一个新场所。

我们先填满工作室。然后是农场、医院、工厂。接着是城市。最后是星球。

**只需 Bash。真实 Agent 足以填满宇宙。**

---

```
                    THE AGENT PATTERN
                    =================

    User --> messages[] --> LLM --> response
                                      |
                            stop_reason == "tool_use"?
                           /                          \
                         yes                           no
                          |                             |
                    execute tools                    return text
                    append results
                    loop back -----------------> messages[]


    That's the minimal loop. Every AI agent needs this loop.
    The MODEL decides when to call tools and when to stop.
    The CODE just executes what the model asks for.
    This repo teaches you to build what surrounds this loop --
    the harness that makes the agent effective in a specific domain.
```

**12 个渐进式会话，从基础循环到隔离的自主执行。**
**每个会话增加一个运行环境机制。每个机制对应一句座右铭。**

> **s01** &nbsp; *“One loop & Bash is all you need”* &mdash; 一个工具 + 一个循环 = 一个 Agent
>
> **s02** &nbsp; *"Adding a tool means adding one handler"* &mdash; 循环保持不变；新工具注册到分发映射中
>
> **s03** &nbsp; *"An agent without a plan drifts"* &mdash; 先列出步骤，再执行；完成度翻倍
>
> **s04** &nbsp; *"Break big tasks down; each subtask gets a clean context"* &mdash; 拆解大任务；每个子任务获得独立上下文
>
> **s05** &nbsp; *"Load knowledge when you need it, not upfront"* &mdash; 通过 tool_result 注入知识，而非系统提示词
>
> **s06** &nbsp; *"Context will fill up; you need a way to make room"* &mdash; 三层压缩策略应对无限会话
>
> **s07** &nbsp; *"Break big goals into small tasks, order them, persist to disk"* &mdash; 基于文件的依赖任务图，为多 Agent 协作奠定基础
>
> **s08** &nbsp; *"Run slow operations in the background; the agent keeps thinking"* &mdash; 守护线程执行命令，完成后注入通知
>
> **s09** &nbsp; *"When the task is too big for one, delegate to teammates"* &mdash; 持久化队友 + 异步邮箱
>
> **s10** &nbsp; *"Teammates need shared communication rules"* &mdash; 单一请求-响应模式驱动所有协商
>
> **s11** &nbsp; *"Teammates scan the board and claim tasks themselves"* &mdash; 无需主节点逐个分配任务
>
> **s12** &nbsp; *"Each works in its own directory, no interference"* &mdash; 任务管理目标，工作树管理目录，受 ID 约束

---

## 核心模式

```python
def agent_loop(messages):
    while True:
        response = client.messages.create(
            model=MODEL, system=SYSTEM,
            messages=messages, tools=TOOLS,
        )
        messages.append({"role": "assistant",
                         "content": response.content})

        if response.stop_reason != "tool_use":
            return

        results = []
        for block in response.content:
            if block.type == "tool_use":
                output = TOOL_HANDLERS[block.name](**block.input)
                results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": output,
                })
        messages.append({"role": "user", "content": results})
```

每个会话都在此循环之上叠加一个运行环境机制——且不改变循环本身。循环属于 Agent。机制属于运行环境。

## 范围说明（重要）

本仓库是一个面向运行环境工程的 0->1 学习项目——构建围绕 Agent 模型的外围环境。
它有意简化或省略了若干生产级机制：

- 完整的事件/钩子总线（例如 PreToolUse、SessionStart/End、ConfigChange）。
  s12 仅包含一个用于教学的最小化追加型生命周期事件流。
- 基于规则的权限治理与信任工作流
- 会话生命周期控制（恢复/分支）和高级工作树生命周期控制
- 完整的 MCP 运行时细节（传输层/OAuth/资源订阅轮询）

请将本仓库中的团队 JSONL 邮箱协议视为教学实现，而非对任何特定生产内部架构的主张。

## 快速开始

```sh
git clone https://github.com/shareAI-lab/learn-claude-code
cd learn-claude-code
pip install -r requirements.txt
cp .env.example .env   # 编辑 .env 填入你的 ANTHROPIC_API_KEY

python agents/s01_agent_loop.py       # 从这里开始
python agents/s12_worktree_task_isolation.py  # 完整进阶终点
python agents/s_full.py               # 毕业设计：所有机制组合
```

### Web 平台

交互式可视化、逐步图解、源码查看器和文档。

```sh
cd web && npm install && npm run dev   # http://localhost:3000
```

## 学习路径

```
Phase 1: THE LOOP                    Phase 2: PLANNING & KNOWLEDGE
==================                   ==============================
s01  The Agent Loop          [1]     s03  TodoWrite               [5]
     while + stop_reason                  TodoManager + nag reminder
     |                                    |
     +-> s02  Tool Use            [4]     s04  Subagents            [5]
              dispatch map: name->handler     fresh messages[] per child
                                              |
                                         s05  Skills               [5]
                                              SKILL.md via tool_result
                                              |
                                         s06  Context Compact      [5]
                                              3-layer compression

Phase 3: PERSISTENCE                 Phase 4: TEAMS
==================                   =====================
s07  Tasks                   [8]     s09  Agent Teams             [9]
     file-based CRUD + deps graph         teammates + JSONL mailboxes
     |                                    |
s08  Background Tasks        [6]     s10  Team Protocols          [12]
     daemon threads + notify queue        shutdown + plan approval FSM
                                          |
                                     s11  Autonomous Agents       [14]
                                          idle cycle + auto-claim
                                     |
                                     s12  Worktree Isolation      [16]
                                          task coordination + optional isolated execution lanes

                                     [N] = number of tools
```

## 架构

```
learn-claude-code/
|
|-- agents/                        # Python reference implementations (s01-s12 + s_full capstone)
|-- docs/{en,zh,ja}/               # Mental-model-first documentation (3 languages)
|-- web/                           # Interactive learning platform (Next.js)
|-- skills/                        # Skill files for s05
+-- .github/workflows/ci.yml      # CI: typecheck + build
```

## 文档

心智模型优先：问题、解决方案、ASCII 图解、最小化代码。
提供 [English](./docs/en/) | [中文](./docs/zh/) | [日本語](./docs/ja/) 版本。

| Session | Topic | Motto |
|---------|-------|-------|
| [s01](./docs/en/s01-the-agent-loop.md) | The Agent Loop | *One loop & Bash is all you need* |
| [s02](./docs/en/s02-tool-use.md) | Tool Use | *Adding a tool means adding one handler* |
| [s03](./docs/en/s03-todo-write.md) | TodoWrite | *An agent without a plan drifts* |
| [s04](./docs/en/s04-subagent.md) | Subagents | *Break big tasks down; each subtask gets a clean context* |
| [s05](./docs/en/s05-skill-loading.md) | Skills | *Load knowledge when you need it, not upfront* |
| [s06](./docs/en/s06-context-compact.md) | Context Compact | *Context will fill up; you need a way to make room* |
| [s07](./docs/en/s07-task-system.md) | Tasks | *Break big goals into small tasks, order them, persist to disk* |
| [s08](./docs/en/s08-background-tasks.md) | Background Tasks | *Run slow operations in the background; the agent keeps thinking* |
| [s09](./docs/en/s09-agent-teams.md) | Agent Teams | *When the task is too big for one, delegate to teammates* |
| [s10](./docs/en/s10-team-protocols.md) | Team Protocols | *Teammates need shared communication rules* |
| [s11](./docs/en/s11-autonomous-agents.md) | Autonomous Agents | *Teammates scan the board and claim tasks themselves* |
| [s12](./docs/en/s12-worktree-task-isolation.md) | Worktree + Task Isolation | *Each works in its own directory, no interference* |

## 下一步 —— 从理解到交付

完成 12 个会话后，你将彻底掌握运行环境工程的运作原理。以下是将知识投入实战的两种方式：

### Kode Agent CLI —— 开源编程 Agent CLI

> `npm i -g @shareai-lab/kode`

支持 Skill & LSP、兼容 Windows、可插拔 GLM / MiniMax / DeepSeek 等开放模型。安装即用。

GitHub: **[shareAI-lab/Kode-cli](https://github.com/shareAI-lab/Kode-cli)**

### Kode Agent SDK —— 将 Agent 能力嵌入你的应用

官方 Claude Code Agent SDK 在底层与完整的 CLI 进程通信——每个并发用户意味着一个独立的终端进程。Kode SDK 是一个独立库，无单用户进程开销，可嵌入后端、浏览器扩展、嵌入式设备或任何运行时环境。

GitHub: **[shareAI-lab/Kode-agent-sdk](https://github.com/shareAI-lab/Kode-agent-sdk)**

---

## 姊妹仓库：从 *按需会话* 到 *常驻助手*

本仓库教授的运行环境是**用完即弃型（use-and-discard）**——打开终端，给 Agent 分配任务，完成后关闭，下次会话从零开始。这是 Claude Code 的模式。

[OpenClaw](https://github.com/openclaw/openclaw) 证明了另一种可能：在相同的 Agent 核心之上，两个运行环境机制将 Agent 从“戳一下才动”转变为“每 30 秒醒来寻找任务”：

- **心跳（Heartbeat）**——每 30 秒运行环境向 Agent 发送一条消息检查是否有事可做。无事？继续休眠。有事？立即行动。
- **定时任务（Cron）**——Agent 可安排自己的未来任务，到时间自动执行。

添加多通道 IM 路由（WhatsApp / Telegram / Slack / Discord、13+ 平台）、持久化上下文记忆和 Soul 人格系统后，Agent 就从一次性工具转变为常驻个人 AI 助手。

**[claw0](https://github.com/shareAI-lab/claw0)** 是我们的配套教学仓库，从零拆解这些运行环境机制：

```
claw agent = agent core + heartbeat + cron + IM chat + memory + soul
```

```
learn-claude-code                   claw0
(agent harness core:                (proactive always-on harness:
 loop, tools, planning,              heartbeat, cron, IM channels,
 teams, worktree isolation)          memory, soul personality)
```

## 关于
<img width="260" src="https://github.com/user-attachments/assets/fe8b852b-97da-4061-a467-9694906b5edf" /><br>

微信扫码关注我们，
或在 X 上关注：[shareAI-Lab](https://x.com/baicai003)

## License

MIT

---

**自主性源于模型。运行环境让自主性成为现实。构建优秀的运行环境。剩下的交给模型。**

**只需 Bash。真实 Agent 足以填满宇宙。**