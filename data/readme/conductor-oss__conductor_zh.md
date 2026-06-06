<picture>
  <!-- Dark mode logo -->
  <source srcset="https://github.com/user-attachments/assets/104b3a67-6013-4622-8075-a45da3a9e726" media="(prefers-color-scheme: dark)">
  <!-- Light mode logo -->
  <img src="https://assets.conductor-oss.org/logo.png" alt="Logo">
</picture>


<h1 align="center" style="border-bottom: none">
    Conductor - 面向互联网规模的智能体工作流引擎
</h1>


[![GitHub stars](https://img.shields.io/github/stars/conductor-oss/conductor?style=social)](https://github.com/conductor-oss/conductor/stargazers)
[![Github release](https://img.shields.io/github/v/release/conductor-oss/conductor.svg)](https://github.com/conductor-oss/conductor/releases)
[![License](https://img.shields.io/github/license/conductor-oss/conductor.svg)](http://www.apache.org/licenses/LICENSE-2.0)
[![Conductor Slack](https://img.shields.io/badge/Slack-Join%20the%20Community-blueviolet?logo=slack)](https://join.slack.com/t/orkes-conductor/shared_invite/zt-2vdbx239s-Eacdyqya9giNLHfrCavfaA)
[![Conductor OSS](https://img.shields.io/badge/Conductor%20OSS-Visit%20Site-blue)](https://conductor-oss.org)

#### 编排分布式系统意味着要与故障、重试和状态恢复不断搏斗。Conductor 替你处理所有这些，让你无需操心。

Conductor 是一款开源的持久化工作流引擎（Durable Workflow Engine），由 [Netflix](https://netflixtechblog.com/netflix-conductor-a-microservices-orchestrator-2e8d4771bf40) 开发，用于在互联网规模下编排微服务、AI 智能体（Agent）和持久化工作流。它已在 Netflix、特斯拉、LinkedIn 和摩根大通的生产环境中得到广泛验证与信赖。该项目由 [Orkes](https://orkes.io) 积极维护，并拥有一个不断壮大的 [社区](https://join.slack.com/t/orkes-conductor/shared_invite/zt-2vdbx239s-Eacdyqya9giNLHfrCavfaA)。

[![conductor_oss_getting_started](https://github.com/user-attachments/assets/6153aa58-8ad1-4ec5-93d1-38ba1b83e3f4)](https://youtu.be/4azDdDlx27M)

---

# 60秒快速上手

**前置条件：**必须已安装 [Node.js](https://nodejs.org/) v16+ 和 Java 21+。

```shell
npm install -g @conductor-oss/conductor-cli
conductor server start
```

打开 [http://localhost:8080](http://localhost:8080) —— 你的服务器已启动并内置了 Web UI。

**运行你的第一个工作流：**

```shell
# Create a workflow that calls an API and parses the response — no workers needed
curl -s https://raw.githubusercontent.com/conductor-oss/conductor/main/docs/quickstart/workflow.json -o workflow.json
conductor workflow create workflow.json
```

> **注意：** 重复执行此命令会在第二次调用时返回错误——工作流已存在。这是预期行为。请使用 `conductor workflow update` 修改现有工作流。

```shell
conductor workflow start -w hello_workflow --sync
```

请参阅 [快速入门指南](https://docs.conductor-oss.org/quickstart/) 获取完整教程，包括如何编写 Worker（任务执行器）和重放工作流。

**Conductor Docker 镜像：**

```shell
docker run -p 8080:8080 conductoross/conductor:latest # replace latest with the published version to pin to a specific version
```

所有 CLI 命令均对应等效的 cURL/API 调用。详见 [快速入门](https://docs.conductor-oss.org/quickstart/)。


---

# 为什么开发者首选 Conductor 作为工作流引擎

| | |
|---|---|
| **持久化执行（Durable Execution）** | 每个步骤都会持久保存。可承受崩溃、重启和网络故障，支持配置重试和超时。 |
| **确定性设计（Deterministic by Design）** | 编排（Orchestration）与业务逻辑分离——确定性是架构层面的保障，而非依赖开发者的纪律约束。Worker 可运行任意代码；工作流图通过构建保证确定性。 |
| **AI 智能体编排（AI Agent Orchestration）** | 原生支持 14+ LLM 提供商、MCP 工具调用、函数调用、人工审批（Human-in-the-loop）以及用于 RAG 的向量数据库。 |
| **运行时动态解析（Dynamic at Runtime）** | 在运行时动态解析分支、任务和子工作流。LLM 可生成 JSON 格式的工作流定义，Conductor 立即执行。 |
| **完整重放能力（Full Replayability）** | 可从头重启、从任意任务重新运行，或仅重试失败步骤——适用于任何工作流，随时可用。 |
| **互联网级规模（Internet Scale）** | 经 Netflix、特斯拉、LinkedIn 和摩根大通实战检验。支持水平扩展至数十亿次工作流执行。 |
| **多语言 Worker（Polyglot Workers）** | 支持 Java、Python、Go、JavaScript、C#、Ruby 或 Rust 编写的 Worker。Worker 负责轮询、执行和上报——可在任何地方运行。 |
| **自托管，无厂商锁定（Self-hosted, No Lock-in）** | Apache 2.0 开源协议。支持 5 种持久化后端和 6 种消息队列。可在 Docker 或 JVM 运行的任何环境中部署。 |

# 交付智能体，而非框架代码

Conductor 的 Worker 就是纯代码——支持任意语言、任意库、任意 I/O。无确定性约束，无需遵循 SDK 规范。编排层采用声明式且机器可读的设计，因此 LLM 可以原生地生成和组合工作流。如果智能体在第 12 次迭代时崩溃，它将从第 12 次迭代处恢复运行。

**Conductor 中的自主思考-执行智能体：**通过 MCP 发现工具，利用 LLM 进行推理，调用选定的工具，循环直至完成任务。

```json
{
  "name": "autonomous_agent",
  "description": "Agent that loops until the task is complete",
  "version": 1,
  "tasks": [
    {
      "name": "discover_tools",
      "taskReferenceName": "discover",
      "type": "LIST_MCP_TOOLS",
      "inputParameters": {
        "mcpServer": "${workflow.input.mcpServerUrl}"
      }
    },
    {
      "name": "agent_loop",
      "taskReferenceName": "loop",
      "type": "DO_WHILE",
      "loopCondition": "if ($.loop['think'].output.result.done == true) { false; } else { true; }",
      "loopOver": [
        {
          "name": "think",
          "taskReferenceName": "think",
          "type": "LLM_CHAT_COMPLETE",
          "inputParameters": {
            "llmProvider": "openai",
            "model": "gpt-4o-mini",
            "messages": [
              {
                "role": "system",
                "message": "You are an autonomous agent. Available tools: ${discover.output.tools}. Previous results: ${loop.output.results}. Respond with JSON: {\"action\": \"tool_name\", \"arguments\": {}, \"done\": false} or {\"answer\": \"final answer\", \"done\": true}."
              },
              { "role": "user", "message": "${workflow.input.task}" }
            ]
          }
        },
        {
          "name": "act",
          "taskReferenceName": "act",
          "type": "SWITCH",
          "expression": "$.think.output.result.done ? 'done' : 'call_tool'",
          "decisionCases": {
            "call_tool": [
              {
                "name": "execute_tool",
                "taskReferenceName": "tool_call",
                "type": "CALL_MCP_TOOL",
                "inputParameters": {
                  "mcpServer": "${workflow.input.mcpServerUrl}",
                  "method": "${think.output.result.action}",
                  "arguments": "${think.output.result.arguments}"
                }
              }
            ]
          }
        }
      ]
    }
  ]
}
```

每个步骤都会持久化保存——无需框架，无 SDK 锁定。基于代码的引擎强制你的代码具备确定性以便框架进行重放；而 Conductor 让引擎本身具备确定性——因此你的代码无需受此限制。

请参阅 [构建你的第一个 AI 智能体](https://docs.conductor-oss.org/devguide/ai/first-ai-agent.html) 指南获取完整教程。

---

## 面向 AI 编程助手的 Conductor Skills

**[Conductor Skills](https://github.com/conductor-oss/conductor-skills)** 允许 AI 编程助手（如 Claude Code、Gemini CLI 及其他工具）直接从终端创建、管理和部署 Conductor 工作流。

### Claude
```shell
# Install Skills for Claude Code
/plugin marketplace add conductor-oss/conductor-skills
/plugin install conductor@conductor-skills
```

### 一键安装所有已检测的智能体

一条命令即可自动检测系统中所有支持的智能体，并在可能的情况下全局安装。可随时重新运行——它仅会为新增检测到的智能体执行安装。

**macOS / Linux**
```bash
curl -sSL https://conductor-oss.github.io/conductor-skills/install.sh | bash -s -- --all
```

**Windows (PowerShell) / (cmd)**
```powershell
# powershell
irm https://conductor-oss.github.io/conductor-skills/install.ps1 -OutFile install.ps1; .\install.ps1 -All

# cmd
powershell -c "irm https://conductor-oss.github.io/conductor-skills/install.ps1 -OutFile install.ps1; .\install.ps1 -All"
```

---

# SDKs

| 语言 | 仓库 | 安装方式 |
|----------|------------|---------|
| ☕ Java | [conductor-oss/java-sdk](https://github.com/conductor-oss/java-sdk) | [Maven Central](https://mvnrepository.com/artifact/org.conductoross/conductor-client) |
| 🐍 Python | [conductor-oss/python-sdk](https://github.com/conductor-oss/python-sdk) | `pip install conductor-python` |
| 🟨 JavaScript | [conductor-oss/javascript-sdk](https://github.com/conductor-oss/javascript-sdk) | `npm install @io-orkes/conductor-javascript` |
| 🐹 Go | [conductor-oss/go-sdk](https://github.com/conductor-oss/go-sdk) | `go get github.com/conductor-sdk/conductor-go` |
| 🟣 C# | [conductor-oss/csharp-sdk](https://github.com/conductor-oss/csharp-sdk) | `dotnet add package conductor-csharp` |
| 💎 Ruby | [conductor-oss/ruby-sdk](https://github.com/conductor-oss/ruby-sdk) | *(孵化中)* |
| 🦀 Rust | [conductor-oss/rust-sdk](https://github.com/conductor-oss/rust-sdk) | *(孵化中)* |

---

# 文档与社区

- **[文档](https://conductor-oss.org)** — 架构说明、指南、API 参考和实战示例。
- **[Slack](https://join.slack.com/t/orkes-conductor/shared_invite/zt-2vdbx239s-Eacdyqya9giNLHfrCavfaA)** — 社区讨论与技术支持。
- **[社区论坛](https://community.orkes.io/)** — 提问交流并分享最佳实践。

---

<details>
<summary><strong>后端配置</strong></summary>

| 后端 | 配置文件 |
|---------|---------------|
| Redis + ES7（默认） | [config-redis.properties](docker/server/config/config-redis.properties) |
| Redis + ES8 | [config-redis-es8.properties](docker/server/config/config-redis-es8.properties) |
| Redis + OpenSearch | [config-redis-os.properties](docker/server/config/config-redis-os.properties) |
| Postgres | [config-postgres.properties](docker/server/config/config-postgres.properties) |
| Postgres + ES7 | [config-postgres-es7.properties](docker/server/config/config-postgres-es7.properties) |
| MySQL + ES7 | [config-mysql.properties](docker/server/config/config-mysql.properties) |

</details>

---

# 从源码构建

<details>
<summary><strong>环境要求与说明</strong></summary>

**环境要求：**Docker Desktop、Java (JDK) 21+、Node 18（用于构建 UI）

```shell
git clone https://github.com/conductor-oss/conductor
cd conductor
./gradlew build

# (optional) Build UI
# ./build_ui.sh

# Start local server
cd server
../gradlew bootRun
```

详见 [完整构建指南](docs/devguide/running/source.md)。
</details>

---

# 常见问题（FAQ）

<details>
<summary><strong>这和 Netflix 的 Conductor 是同一个项目吗？</strong></summary>

是的。Conductor OSS 是原始 [Netflix Conductor](https://github.com/Netflix/conductor) 仓库的延续，在 Netflix 将该项目贡献给开源基金会后继续发展。
</details>

<details>
<summary><strong>Conductor 是开源的吗？</strong></summary>

是的。Conductor 是一款完全开源的工作流引擎，采用 Apache 2.0 许可证授权。你可以在自有基础设施上自托管，支持 5 种持久化后端和 6 种消息队列。
</details>

<details>
<summary><strong>该项目是否积极维护中？</strong></summary>

是的。[Orkes](https://orkes.io) 是主要维护方，并提供面向所有主流云厂商的 Conductor 企业级 SaaS 平台。
</details>

<details>
<summary><strong>Conductor 能否扩展以处理我的业务负载？</strong></summary>

可以。该项目由 Netflix 构建，在互联网规模下经过实战检验。Conductor 支持跨多个服务器实例水平扩展，可轻松应对数十亿次工作流执行。
</details>

<details>
<summary><strong>Conductor 是否支持持久化执行？</strong></summary>

是的。Conductor 开创了持久化执行模式，确保工作流和智能体即使在基础设施故障或崩溃时也能可靠完成。每个步骤都会持久保存并可恢复。
</details>

<details>
<summary><strong>工作流完成后或失败后能否重放？</strong></summary>

可以。Conductor 会永久保留完整的执行历史。你可以通过 API 或 UI 从头重启、从特定任务重新运行，或仅重试失败步骤。
</details>

<details>
<summary><strong>Conductor 能否编排 AI 智能体和 LLM？</strong></summary>

可以。Conductor 原生集成 14+ 个 LLM 提供商（Anthropic、OpenAI、Gemini、Bedrock 等）、MCP 工具调用、函数调用、人工审批以及用于 RAG 的向量数据库集成。
</details>

<details>
<summary><strong>为什么 Conductor 将编排与代码分离？</strong></summary>

将编排逻辑与业务逻辑耦合会迫使开发者手动维护确定性约束——工作流定义中不能包含直接 I/O、系统时间或随机数。Conductor 通过架构设计使编排层具备确定性，从而彻底消除此类 bug。Worker 就是纯代码，无任何框架限制——可用任意语言编写，调用任意库和 API。
</details>

<details>
<summary><strong>用代码而非 JSON 编写工作流不是更强大吗？</strong></summary>

这取决于你对“强大”的定义。在基于代码的引擎中，工作流定义与业务逻辑共享同一运行时——这意味着框架必须重放你的代码以恢复状态。这会迫使你的业务逻辑遵循确定性约束：不能直接 I/O、不能使用系统时间、线程或随机数。Conductor 将这些关注点分离。编排图是声明式的（JSON），因此天生具备确定性。你的 Worker 是无限制的纯代码——可用任意语言、库和 API。你在关键处（业务逻辑）获得代码的全部能力，而在非关键处（编排）免除框架负担。
</details>

<details>
<summary><strong>JSON 工作流能否处理分支、循环和错误处理等复杂逻辑？</strong></summary>

可以。Conductor 支持 `SWITCH`（条件分支）、`DO_WHILE`（带配置清理的循环）、`FORK_JOIN`（动态扇出的并行执行）、`SUB_WORKFLOW`（组合）以及运行时解析的 `DYNAMIC` 任务。这些组件可自由嵌套——例如在分支内嵌套循环，在 Fork 中嵌套分支。对于错误处理，每个任务均支持配置重试、超时及可选/补偿任务。声明式模型不会限制复杂度——它让复杂逻辑变得可见且易于调试。
</details>

<details>
<summary><strong>Conductor 如何处理工作流版本管理？</strong></summary>

工作流定义按版本号递增。正在运行的执行将继续使用其启动时的版本——部署新版本绝不会中断进行中的工作流。由于 Conductor 不会重放你的代码，因此不存在重放兼容性问题。编排图是权威数据源（Source of Truth），每次执行都绑定到其定义版本。你可以更新编排逻辑而无需重新部署 Worker，也无需担心破坏正在运行的工作流。
</details>

<details>
<summary><strong>开发者体验如何——IDE 支持、类型检查和调试？</strong></summary>

Conductor 内置可视化 UI，用于设计、运行和调试工作流。每次执行完全可观测：你可以检查每个任务的输入、输出、耗时和重试历史。为保障类型安全，Conductor 会根据 JSON Schema 验证工作流输入和任务 I/O。Worker 是你所选语言的纯代码——你可获得完整的 IDE 支持、类型检查和调试能力来开发业务逻辑。编排层在 UI 中清晰可见，而非隐藏在框架内部。
</details>

<details>
<summary><strong>Conductor 能否处理长周期工作流（数天、数周甚至数月）？</strong></summary>

可以。Conductor 专为长周期工作流设计。执行状态完全持久化——工作流可暂停数月以等待人工审批、外部信号或定时任务，并在恢复时精确回到断点处。不存在内存状态丢失的风险。这也是 AI 智能体循环具备持久性的机制：如果第 12 次迭代因等待人类审核而暂停三周，第 13 次迭代将无缝接续。
</details>

<details>
<summary><strong>不在代码中编写编排逻辑是否会损失灵活性？</strong></summary>

恰恰相反，你获得了更多灵活性。由于工作流是 JSON 格式，LLM 可以在运行时生成和修改它们——无需经历编译/部署周期。动态分支允许你在运行时扇出到可变数量的并行任务。动态子工作流允许一个工作流按名称组合其他工作流。此外，由于 Worker 与编排解耦，你可以独立更新工作流图或替换 Worker 实现。基于代码的引擎将这些耦合在一起，因此更改编排意味着需要重新部署和版本化你的代码。
</details>

<details>
<summary><strong>Conductor 与其他工作流引擎相比如何？</strong></summary>

Conductor 是一款开源工作流引擎，原生支持 14+ 个 LLM 任务类型、内置 MCP 集成、持久化执行、完整重放能力以及 7 种语言的 SDK。与基于代码的引擎不同，Conductor 将编排与业务逻辑分离——确定性是架构层面的保障，而非开发者的约束。你的 Worker 是无框架规则的纯代码。编排层采用声明式设计，因此具备可观测性、版本化能力，并可被 LLM 组合使用。经 Netflix、特斯拉、LinkedIn 和摩根大通实战检验。
</details>

<details>
<summary><strong>Orkes Conductor 是否与 Conductor OSS 兼容？</strong></summary>

100% 完全兼容。Orkes Conductor 基于 Conductor OSS 构建，提供完整的 API 和工作流兼容性。
</details>

---

# 贡献代码

我们欢迎所有人的贡献！

- **报告问题：**在 [GitHub](https://github.com/conductor-oss/conductor/issues) 提交 Issue。
- **贡献代码：**查阅我们的 [贡献指南](CONTRIBUTING.md) 和 [适合新手的 Issues](https://github.com/conductor-oss/conductor/labels/good%20first%20issue)。
- **完善文档：**帮助我们维护出色的 [文档](https://github.com/conductor-oss/conductor/tree/main/docs)。

## Contributors

<a href="https://github.com/conductor-oss/conductor/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=conductor-oss/conductor" />
</a>

---

# 路线图

[查看 Conductor OSS 路线图](ROADMAP.md)。想要参与？[联系我们](https://forms.gle/P2i1xHrxPQLrjzTB7)。

# 许可证

Conductor 遵循 [Apache 2.0 License](LICENSE) 开源协议。