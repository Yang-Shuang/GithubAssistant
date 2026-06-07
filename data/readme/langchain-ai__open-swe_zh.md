<div align="center">
  <a href="https://github.com/langchain-ai/open-swe">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="static/dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="static/light.svg">
      <img alt="Open SWE Logo" src="static/dark.svg" width="35%">
    </picture>
  </a>
</div>

<div align="center">
  <h3>用于构建组织内部编码 Agent 的开源框架。</h3>
</div>

<div align="center">
  <a href="https://opensource.org/licenses/MIT" target="_blank"><img src="https://img.shields.io/github/license/langchain-ai/open-swe" alt="License"></a>
  <a href="https://github.com/langchain-ai/open-swe/stargazers" target="_blank"><img src="https://img.shields.io/github/stars/langchain-ai/open-swe" alt="GitHub Stars"></a>
  <a href="https://github.com/langchain-ai/langgraph" target="_blank"><img src="https://img.shields.io/badge/Built%20on-LangGraph-blue" alt="Built on LangGraph"></a>
  <a href="https://github.com/langchain-ai/deepagents" target="_blank"><img src="https://img.shields.io/badge/Built%20on-Deep%20Agents-blue" alt="Built on Deep Agents"></a>
  <a href="https://x.com/langchain" target="_blank"><img src="https://img.shields.io/twitter/url/https/twitter.com/langchain.svg?style=social&label=Follow%20%40LangChain" alt="Twitter / X"></a>
</div>

<br>

顶尖工程团队（如 Stripe、Ramp 和 Coinbase）正在构建自己的内部编码 Agent —— 包括 Slackbot、CLI 和 Web 应用，无缝融入工程师现有的工作场景。这些 Agent 与内部系统相连，具备合适的上下文、权限和安全边界，从而在极少人工干预下自主运行。

Open SWE 是该模式的开源版本。基于 [LangGraph](https://langchain-ai.github.io/langgraph/) 和 [Deep Agents](https://github.com/langchain-ai/deepagents) 构建，它提供了这些公司内部架构的核心要素：云沙箱、Slack 与 Linear 调用、子 Agent 编排以及自动 PR 创建 —— 你只需稍作定制即可适配自身的代码库与工作流。

> [!NOTE]
> 💬 在此阅读**公告博客文章 [here](https://blog.langchain.com/open-swe-an-open-source-framework-for-internal-coding-agents/)**

---

## Architecture（架构）

Open SWE 做出了与顶尖内部编码 Agent 相同的底层架构决策。以下是它如何映射到 [这篇概述](https://x.com/kishan_dahya/status/2028971339974099317) 中描述的 Stripe Minions、Ramp Inspect 和 Coinbase Cloudbot 的模式：

### 1. Agent Harness —— 基于 Deep Agents 组合

与直接 fork 现有 Agent 或从零开始不同，Open SWE **组合（compose）**了 [Deep Agents](https://github.com/langchain-ai/deepagents) 框架 —— 类似于 Ramp 基于 OpenCode 的构建方式。这既为你保留了升级路径（可拉取上游改进），又允许你针对组织需求自定义编排逻辑、工具和中间件。

```python
create_deep_agent(
    model="openai:gpt-5.5",
    system_prompt=construct_system_prompt(...),
    tools=[http_request, fetch_url, linear_comment, slack_thread_reply],
    backend=sandbox_backend,
    middleware=[ToolErrorMiddleware(), check_message_queue_before_model, ...],
)
```

### 2. Sandbox —— 隔离的云环境

每个任务都在其独立的**隔离云沙箱**中运行 —— 这是一个具备完整 Shell 访问权限的远程 Linux 环境。代码库会被克隆至其中，Agent 获得完整权限，且任何失误的影响范围都被严格限制在沙箱内。无需生产环境访问权限，也无需确认提示。

Open SWE 开箱即支持多个沙箱提供商 —— [Modal](https://modal.com/)、[Daytona](https://www.daytona.io/)、[Runloop](https://www.runloop.ai/) 和 [LangSmith](https://smith.langchain.com/)，你也可以接入自己的服务商。详情见 [自定义指南](CUSTOMIZATION.md#1-sandbox)。

这遵循了这三家公司共同采用的原则：**先隔离边界，再在内部授予完整权限。**
- 每个对话线程（thread）对应一个持久化沙箱（跨后续消息复用）
- 若沙箱失联，将自动重建
- 多任务并行运行 —— 每个任务独占一个沙箱，无需排队

### 3. Tools —— 精选而非堆砌

Stripe 的核心洞察：*工具的筛选比数量更重要。* Open SWE 遵循这一原则，采用精简且聚焦的工具集：

| Tool | Purpose |
|---|---|
| `execute` | 在沙箱中执行 Shell 命令 |
| `fetch_url` | 以 Markdown 格式抓取网页内容 |
| `http_request` | API 调用（GET、POST 等） |
| `linear_comment` | 向 Linear 工单发布更新 |
| `slack_thread_reply` | 在 Slack 线程中回复 |

在沙箱内部，GitHub 操作通过 `GH_TOKEN=dummy gh` 执行，并由 LangSmith 代理提供支持。此外还内置了 Deep Agents 工具：`read_file`、`write_file`、`edit_file`、`ls`、`glob`、`grep`、`write_todos` 和 `task`（用于生成子 Agent）。

### 4. Context Engineering —— AGENTS.md + 源上下文

Open SWE 从两个来源收集上下文：
- **`AGENTS.md`** —— 如果代码库根目录包含 `AGENTS.md` 文件，它将从沙箱中读取并注入到系统提示词（system prompt）中。这相当于 Stripe 的规则文件：编码规范、测试要求以及每个 Agent 运行都应遵循的架构决策。
- **源上下文（Source context）** —— 完整的 Linear Issue（标题、描述、评论）或 Slack 线程历史会被组装并传递给 Agent，使其在开始时就拥有丰富上下文，而非依赖工具调用逐步发现。

### 5. Orchestration —— 子 Agent + 中间件

Open SWE 的编排包含两个层级：

**子 Agent（Subagents）：** Deep Agents 框架原生支持通过 `task` 工具生成子 Agent。主 Agent 可将独立的子任务分发至隔离的子 Agent —— 每个子 Agent 拥有自己的中间件栈、待办列表和文件操作权限。这类似于 Ramp 的并行工作子会话。

**中间件（Middleware）：** 确定性中间件钩子围绕 Agent 循环运行：
- **`check_message_queue_before_model`** —— 在下次模型调用前注入后续消息（运行中途到达的 Linear 评论或 Slack 消息）。你可以在 Agent 运行时发送消息，它会在下一步拾取你的输入。
- **`notify_step_limit_reached`** —— Agent 后置钩子，当 Agent 达到模型调用上限时发布 Slack 回复，让用户获得明确提示而非静默失败。
- **`ToolErrorMiddleware`** —— 优雅捕获并处理工具错误。

### 6. Invocation —— Slack、Linear 和 GitHub

文章中提到的三家公司都将 **Slack** 作为主要调用入口。Open SWE 同样如此：
- **Slack** —— 在任何线程中提及该 Bot。支持使用 `repo:owner/name` 语法指定要操作的代码库。Agent 会在当前线程内回复状态更新和 PR 链接。
- **Linear** —— 在任何 Issue 下评论 `@openswe`。Agent 会读取完整的 Issue 上下文，以 👀 表情回应表示已接收，并将结果作为评论发布回来。
- **GitHub** —— 在 Agent 创建的 PR 评论中 @`@openswe`，让它处理代码审查反馈并将修复推送到同一分支。

每次调用都会生成一个确定性线程 ID，因此针对同一 Issue 或线程的后续消息会路由到同一个正在运行的 Agent。

### 7. Validation —— 提示词驱动

Agent 被指示在提交前运行 Linter、Formatter 和测试，并端到端负责代码提交、推送、创建/更新草稿 PR，以及在源频道回复。
这是你可以针对组织扩展 Open SWE 的领域：作为额外的中间件加入确定性 CI 检查、视觉验证或审查门禁。具体方法见 [自定义指南](CUSTOMIZATION.md#6-middleware)。

---

## Comparison（对比）

| Decision | Open SWE | Stripe (Minions) | Ramp (Inspect) | Coinbase (Cloudbot) |
|---|---|---|---|---|
| **Harness** | 组合式（Deep Agents/LangGraph） | Forked（Goose） | 组合式（OpenCode） | 从零构建 |
| **Sandbox** | 可插拔（Modal, Daytona, Runloop 等） | AWS EC2 devboxes（预初始化） | Modal 容器（预初始化） | 自研 |
| **Tools** | ~15，精选 | ~500，按 Agent 筛选 | OpenCode SDK + 扩展 | MCPs + 自定义 Skills |
| **Context** | AGENTS.md + Issue/线程 | 规则文件 + 预加载 | OpenCode 内置 | Linear优先 + MCPs |
| **Orchestration** | 子Agent + 中间件 | Blueprints（确定性+智能体） | Sessions + 子会话 | 三种模式 |
| **Invocation** | Slack, Linear, GitHub | Slack + 嵌入式按钮 | Slack + Web + Chrome 扩展 | Slack原生 |
| **Validation** | 提示词驱动 | 3层（本地+CI+1次重试） | 视觉DOM验证 | 多Agent评审团+自动合并 |

---

## Features（特性）

- **支持从 Linear、Slack 或 GitHub 触发** —— 在评论中提及 `@openswe` 即可启动任务
- **即时响应确认** —— 接收到消息的瞬间以 👀 表情回应
- **运行中可继续对话** —— 在任务中途发送后续消息，它会在下一步拾取处理
- **多任务并行执行** —— 每个任务在独立的云沙箱中运行
- **内置 GitHub OAuth** —— 自动完成 GitHub 账号认证
- **自动创建 PR** —— 完成后提交更改并打开草稿 PR，链接回你的工单/Issue
- **支持子 Agent** —— Agent 可生成子 Agent 处理并行子任务
- **Web 仪表盘** —— 配套应用（位于 `ui/` 目录），支持 GitHub 登录、按用户配置模型/资料、团队默认设置、启用的代码库与审查风格管理、用户映射，以及 Agent 聊天界面

---

## Getting Started（快速开始）

- **[Installation Guide](INSTALLATION.md)** —— 本地开发（后端+仪表盘）、GitHub App 创建、LangSmith 配置、Linear/Slack/GitHub 触发器设置及生产环境部署
- **[Customization Guide](CUSTOMIZATION.md)** —— 为你的组织替换沙箱、模型、工具、触发器、系统提示词和中间件

## License（许可证）

MIT