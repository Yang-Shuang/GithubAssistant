<p align="center">
  <img src="assets/icons/icon.png" width="80" alt="Cline" />
</p>

<h1 align="center">Cline</h1>

<p align="center">
你的 IDE 和终端中的开源编码智能体。
</p>

<div align="center">

<div align="center">
<table>
<tbody>
<td align="center">
<a href="https://docs.cline.bot" target="_blank"><strong>文档</strong></a>
</td>
<td align="center">
<a href="https://discord.gg/cline" target="_blank"><strong>Discord</strong></a>
</td>
<td align="center">
<a href="https://www.reddit.com/r/cline/" target="_blank"><strong>r/cline</strong></a>
</td>
<td align="center">
<a href="https://github.com/cline/cline/discussions/categories/feature-requests?discussions_q=is%3Aopen+category%3A%22Feature+Requests%22+sort%3Atop" target="_blank"><strong>功能建议</strong></a>
</td>
<td align="center">
<a href="https://cline.bot/join-us" target="_blank"><strong>加入我们！</strong></a>
</td>
</tbody>
</table>
</div>

</div>

<br>

<div align="center">
<table>
<tr>
<td align="center" width="50%">

### CLI

在终端中运行 Cline。
支持交互式对话，或完全无头模式用于 CI/CD 和脚本编写。

```
npm i -g cline
```

<a href="./apps/cli/README.md">了解更多</a>
<br><br>

</td>
<td align="center" width="50%">

### Kanban

从基于 Web 的任务看板并行运行多个智能体。每张卡片拥有独立的工作树（worktree）、自动提交和依赖链。

```
npm i -g kanban
```

<a href="https://github.com/cline/kanban">了解更多</a>
<br><br>

</td>
</tr>
<tr>
<td align="center" width="50%">

### VS Code Extension

编辑器中的 AI 编码助手。
创建文件、运行命令、浏览网页，并使用工具（需人工审批）。

<a href="https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev">从 VS Marketplace 安装</a>
<br><br>

</td>
<td align="center" width="50%">

### JetBrains Plugin

在 IntelliJ IDEA、PyCharm、WebStorm、GoLand 等 JetBrains 全家桶中获得相同的 Cline 体验。

<a href="https://plugins.jetbrains.com/plugin/28247-cline">从 JetBrains Marketplace 安装</a>
<br><br>

</td>
</tr>
</table>
</div>

<div align="center">
<table>
<tr>
<td align="center">

### SDK

使用驱动 CLI、Kanban、VS Code 扩展和 JetBrains 插件的同一引擎，构建你自己的 AI 智能体和集成应用。支持自定义工具、多智能体团队、连接器、定时自动化等更多功能。

```
npm install @cline/sdk
```

<a href="https://docs.cline.bot/cline-sdk/overview">文档</a>
<br><br>

</td>
</tr>
</table>
</div>

---

## Index

| Product | Description | Location | CHANGELOG |
|---------|------------|--------------|--------------|
| **SDK** | Node.js 编程式智能体 API 及扩展导出。 | [`sdk/`](https://github.com/cline/cline/tree/main/sdk) | [CHANGELOG.md](https://github.com/cline/cline/blob/main/sdk/CHANGELOG.md) |
| **CLI** | 终端界面、无头模式、Shell 命令及 CLI 专属工作流。 | [`apps/cli/`](https://github.com/cline/cline/tree/main/apps/cli) | [CHANGELOG.md](https://github.com/cline/cline/blob/main/apps/cli/CHANGELOG.md) |
| **VS Code Extension** | 市场扩展及扩展主机集成。 | [`/`](https://github.com/cline/cline/tree/main)（迁移中 / WIP） | [CHANGELOG.md](https://github.com/cline/cline/blob/main/CHANGELOG.md) |
| **JetBrains Plugin** | 托管于 JetBrains 的客户端，与共享智能体核心通信。 | 目前我们未开源 JetBrains 插件 | - |
| **Kanban** | 基于 Web 的多智能体任务看板。 | [`cline/kanban`](https://github.com/cline/kanban) | [CHANGELOG.md](https://github.com/cline/kanban/blob/main/CHANGELOG.md) |
| **Docs site** | 公开文档页面。 | [`docs/`](https://docs.cline.bot/) | - |

## Edits Code Across Your Project

Cline 会读取你的项目结构，理解文件间的关联关系，并在整个代码库中进行协调性修改。在运行过程中监控 Linter 和编译器报错，在你察觉之前自动修复缺失导入、类型不匹配和语法错误等问题。在 VS Code 和 JetBrains 中，每次修改都会以 Diff（差异）形式展示，供你审查、修改或还原。所有更改均通过检查点记录，方便你轻松撤销智能体的操作。

## Runs Bash Commands

Cline 直接在终端中执行命令并实时监视输出。安装依赖包、运行构建脚本、执行测试、部署应用及管理数据库。对于开发服务器等长时间运行的进程，Cline 会在后台继续工作并实时响应新输出，即时捕获编译错误、测试失败和服务器崩溃。

## Plan and Act

在 Plan 模式和 Act 模式之间切换。在 Plan 模式下，Cline 会探索你的代码库、提出澄清性问题并制定策略。确认一致后，切换到 Act 模式由 Cline 执行该计划。每次文件修改和终端命令都需要你的批准，确保你始终掌控实际发生的变更。或者开启 auto-approve（自动审批），让 Cline 自主运行。

## Rules and Skills

在 `.clinerules` 文件中定义项目专属规则，指导 Cline 在你的代码库中的工作方式：包括编码规范、架构约定、部署流程及测试要求。CLI、VS Code 扩展和 JetBrains 插件会自动读取这些规则。使用 skills（技能）让模型在需要时加载特定规则。 

## Works With Every Model

Cline 不绑定单一 AI 服务商。你可以根据工作流自由选用任意模型：

| Provider | Models |
|----------|--------|
| Anthropic | Claude Opus, Sonnet, Haiku |
| OpenAI | GPT series model |
| Google | Gemini series model |
| OpenRouter | 200+ models from any provider |
| Vercel AI Gateway | Models through Vercel AI Gateway |
| AWS Bedrock | Claude, Llama, and more |
| Azure / GCP Vertex | All hosted models |
| Cerebras / Groq | Fast inference models |
| Ollama / LM Studio | Run local models on your machine |
| Any OpenAI-compatible API | Self-hosted or third-party endpoints |

## Extend With Plugins or MCP Servers

通过插件扩展 Cline 的能力。借助 SDK，你可以通过插件系统以编程方式注册工具和 lifecycle hooks（生命周期钩子），用于日志记录、审计、策略执行或添加领域特定功能。下方为简单插件示例。

```typescript
import { Agent, createTool } from "@cline/sdk"

const deployTool = createTool({
  name: "deploy",
  description: "Deploy the current branch to staging.",
  inputSchema: { type: "object", properties: { env: { type: "string" } }, required: ["env"] },
  execute: async (input) => {
    // your deployment logic
  },
})

const agent = new Agent({ tools: [deployTool], /* ... */ })
```
...或使用 [MCP servers](https://github.com/modelcontextprotocol)连接数据库、查询 API、管理云基础设施并与外部系统交互。可使用[社区构建的服务器](https://github.com/modelcontextprotocol/servers)，或让 Cline 按需动态创建自定义工具。在 CLI 中，使用 `cline mcp` 管理服务器。

## Multi-Agent Teams

协调多个智能体协同处理复杂任务。一个 coordinator agent（协调员智能体会将工作拆分为子任务，并委派给 specialist agents（专家智能体），每个智能体拥有独立的工具和上下文。团队状态会在会话间持久化保存，方便你随时接续之前的进度。

```bash
cline --team-name auth-sprint "Plan and implement user authentication with tests"
```

## Scheduled Agents

基于 Cron 计划任务运行智能体，实现周期性自动化。每日 PR（Pull Request）摘要、每周依赖检查、代码库健康报告等。定时任务会在重启后保留，且独立于任何终端会话运行。

```bash
cline schedule create "PR summary" \
  --cron "0 9 * * MON-FRI" \
  --prompt "List all open PRs and their review status" \
  --workspace /path/to/repo
```

## Connect to Slack, Telegram, Discord, and More

通过任意消息平台与你的智能体对话：Telegram、Slack、Discord、Google Chat、WhatsApp 和 Linear。每个对话线程对应一个具有完整上下文的智能体会话。可设置访问控制，限制与你的智能体交互的用户权限。

```bash
cline connect telegram -k $BOT_TOKEN
cline connect slack --token $SLACK_TOKEN --signing-secret $SECRET --base-url $URL
```

## Headless CLI for CI/CD

以零交互方式运行 Cline，用于脚本编写和自动化。支持管道输入、获取 JSON 输出、命令链式调用及集成到 CI/CD 流水线中。

```bash
cline "Run tests and fix any failures"
git diff origin/main | cline  "Review these changes for issues"
cline --json "List all TODO comments" | jq -r 'select(.type == "agent_event" and .event.text) | .event.text'
```

## Contributing

请先阅读 [Contributing Guide](CONTRIBUTING.md)。加入我们的 [Discord](https://discord.gg/cline) 并前往 `#contributors` 频道，与其他贡献者交流。查看我们的 [招聘页面](https://cline.bot/join-us) 了解全职岗位信息。

## License

[Apache 2.0 © 2026 Cline Bot Inc.](./LICENSE)