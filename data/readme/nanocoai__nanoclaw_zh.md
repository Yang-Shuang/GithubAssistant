<p align="center">
  <img src="assets/nanoclaw-logo.png" alt="NanoClaw" width="400">
</p>

<p align="center">
  一个在独立容器中安全运行 Agent（智能体）的 AI 助手。轻量级，旨在易于理解并完全根据你的需求进行定制。
</p>

<p align="center">
  <a href="https://nanoclaw.dev">nanoclaw.dev</a>&nbsp; • &nbsp;
  <a href="https://docs.nanoclaw.dev">文档</a>&nbsp; • &nbsp;
  <a href="README_zh.md">中文</a>&nbsp; • &nbsp;
  <a href="README_ja.md">日本語</a>&nbsp; • &nbsp;
  <a href="https://discord.gg/VDdww8qS42"><img src="https://img.shields.io/discord/1470188214710046894?label=Discord&logo=discord&v=2" alt="Discord" valign="middle"></a>&nbsp; • &nbsp;
  <a href="repo-tokens"><img src="repo-tokens/badge.svg" alt="repo tokens" valign="middle"></a>
</p>

---

## 为什么构建 NanoClaw

[OpenClaw](https://github.com/openclaw/openclaw) 是一个令人印象深刻的项目，但如果我把完全访问权限交给一个我不理解且包含复杂逻辑的软件，我根本睡不着觉。OpenClaw 拥有近五十万行代码、53 个配置文件和 70+ 依赖项。它的安全防护停留在应用层面（白名单、配对码），而非真正的操作系统级隔离。所有进程都在同一个 Node.js 进程中运行并共享内存。

NanoClaw 提供了相同的核心功能，但代码库足够小以至于你可以轻松理解：仅一个进程和寥寥数个文件。Claude Agent（智能体）运行在独立的 Linux 容器中，具备文件系统级隔离，而不仅仅是依赖权限检查。

## 快速开始

```bash
git clone https://github.com/nanocoai/nanoclaw.git nanoclaw-v2
cd nanoclaw-v2
bash nanoclaw.sh
```

`nanoclaw.sh` 会引导你从一台全新的机器配置到一个可对话的命名 Agent。它会安装 Node、pnpm 和 Docker（如果缺失），通过 OneCLI 注册你的 Anthropic 凭据，构建 Agent 容器，并配对你的第一个频道（Telegram、Discord、WhatsApp 或本地 CLI）。如果某一步骤失败，将自动调用 Claude Code 进行诊断并从断点处恢复。

<details>
<summary><strong>从 NanoClaw v1 迁移？</strong></summary>

在与你的 v1 安装目录相邻的位置克隆一个新的 v2 版本并运行：

```bash
git clone https://github.com/nanocoai/nanoclaw.git nanoclaw-v2
cd nanoclaw-v2
bash migrate-v2.sh
```

`migrate-v2.sh` 会查找你的 v1 安装位置（同级目录，或通过环境变量 `NANOCLAW_V1_PATH=/path/to/nanoclaw` 指定），将状态迁移到 v2 版本中，然后 `exec` 进入 Claude Code 以完成需要人工判断的部分（所有者初始化、CLAUDE.local.md 清理、分支定制回放）。

**请直接运行该脚本，不要从 Claude 会话内部执行**——确定性流程需要交互式提示和真实的 Shell I/O 来完成 Node/pnpm 引导、Docker、OneCLI 及容器构建。

**它的作用：** 合并 `.env`，将 `registered_groups` 数据导入 v2 数据库，复制群组文件夹 + 会话数据 + 定时任务，安装你选择的频道适配器，复制频道认证状态（包括 WhatsApp 的 Baileys keystore + LID 映射），并构建 Agent 容器。

**它不会做的：** 切换系统服务。在提示时选择 *"switch to v2"*，或在测试完成后手动执行——你的 v1 安装将保持完全 untouched（不受影响）。

查看 [docs/v1-to-v2-changes.md](docs/v1-to-v2-changes.md) 了解差异，以及 [docs/migration-dev.md](docs/migration-dev.md) 获取开发说明。

</details>

## 设计理念

**足够小，易于理解。** 一个进程、少量源文件且无微服务架构。如果你想彻底理解整个 NanoClaw 代码库，只需让 Claude Code 带你逐步浏览即可。

**通过隔离保障安全。** Agent 运行在 Linux 容器中，只能访问显式挂载的资源。Bash 操作是安全的，因为命令在容器内执行，而非你的宿主机上。

**为个人用户打造。** NanoClaw 不是臃肿的单体框架；它是贴合每个用户确切需求的软件。与其让项目逐渐变成功能堆砌（bloatware），NanoClaw 被设计为可高度定制。你可以 Fork 该项目，并让 Claude Code 修改它以匹配你的需求。

**定制即代码修改。** 拒绝配置文件泛滥。想要不同行为？直接修改代码。由于代码库足够小，进行安全修改是可行的。

**原生 AI 驱动，混合架构设计。** 安装和引导流程是一条经过优化的脚本路径，快速且确定性高。当某一步骤需要判断时（无论是安装失败、引导决策还是定制需求），控制权会无缝移交至 Claude Code。除了设置阶段外，没有监控面板或调试 UI：在聊天中描述问题，Claude Code 即可处理。

**技能优先于功能。** 主干代码提供注册表和基础设施，而非具体的频道适配器或替代 Agent 提供商。频道（Discord、Slack、Telegram、WhatsApp、…）位于长期维护的 `channels` 分支；替代提供商（OpenCode、Ollama）位于 `providers` 分支。你只需运行 `/add-telegram`、`/add-opencode` 等，技能模块会将恰好需要的代码复制到你的 Fork 中。不附带任何你不需要的功能。

**最佳框架，最佳模型。** NanoClaw 原生通过 Anthropic 官方 Claude Agent SDK 使用 Claude Code，因此你能获得最新的 Claude 模型及完整工具集（包括修改和扩展你自己的 NanoClaw Fork 的能力）。其他提供商即插即用：`/add-codex` 用于 OpenAI 的 Codex（ChatGPT 订阅或 API Key），`/add-opencode` 用于通过 OpenCode 接入 OpenRouter、Google、DeepSeek 等，以及 `/add-ollama-provider` 用于本地开源权重模型。提供商可按 Agent 组单独配置。

## 支持的功能

- **多频道消息通信** — WhatsApp、Telegram、Discord、Slack、Microsoft Teams、iMessage、Matrix、Google Chat、Webex、Linear、GitHub、微信，以及通过 Resend 发送邮件。按需安装 `/add-<channel>` 技能即可启用。可同时运行一个或多个。
- **灵活的隔离机制** — 为每个频道连接独立的 Agent 以实现完全隐私；让多个频道共享同一个 Agent 以统一记忆但保持独立对话；或将多个频道折叠到单个共享会话中，使一次对话跨越多个平台。通过 `/manage-channels` 按频道选择。详见 [docs/isolation-model.md](docs/isolation-model.md)。
- **独立的 Agent 工作区** — 每个 Agent 组拥有自己的 `CLAUDE.md`、独立记忆、专属容器以及仅你允许的挂载点。除非你主动配置，否则数据不会跨越边界。
- **定时任务** — 定期运行 Claude 并可将结果消息推送给你。
- **网页访问能力** — 搜索和抓取网络内容。
- **容器级隔离** — Agent 在 Docker（macOS/Linux/WSL2）中沙盒化，可选配 [Docker Sandboxes](docs/docker-sandboxes.md) 微虚拟机隔离或 Apple Container（macOS 原生轻量运行时）。
- **凭据安全** — Agent 永不持有原始 API Key。出站请求通过 [OneCLI 的 Agent Vault](https://github.com/onecli/onecli) 路由，在请求时动态注入凭据，并强制执行每 Agent 策略和速率限制。

## 使用方法

使用触发词（默认：`@Andy`）与你的助手对话：

```
@Andy send an overview of the sales pipeline every weekday morning at 9am (has access to my Obsidian vault folder)
@Andy review the git history for the past week each Friday and update the README if there's drift
@Andy every Monday at 8am, compile news on AI developments from Hacker News and TechCrunch and message me a briefing
```

在你拥有或管理的频道中，你可以管理群组和任务：
```
@Andy list all scheduled tasks across groups
@Andy pause the Monday briefing task
@Andy join the Family Chat group
```

## 自定义配置

NanoClaw 不使用配置文件。要修改设置，只需告诉 Claude Code 你的需求：

- "将触发词改为 @Bob"
- "记住以后回复要更简短直接"
- "当我问候早安时添加自定义欢迎语"
- "每周存储对话摘要"

或运行 `/customize` 获取引导式配置。

代码库足够小，Claude 可以安全地修改它。

## 贡献指南

**不要添加功能，请添加技能（Skills）。**

如果你想新增频道或 Agent 提供商，请勿直接提交到主干。新频道适配器应合并至 `channels` 分支；新 Agent 提供商应合并至 `providers` 分支。用户通过 `/add-<name>` 技能在自己的 Fork 中安装它们，这些技能会将相关模块复制到标准路径、配置注册表并锁定依赖项。

这能保持主干代码纯粹作为注册表和基础设施，同时确保每个用户的 Fork 保持精简——用户仅获得他们请求的频道和提供商，无多余功能。

### RFS（技能需求列表）

我们希望看到的技能：

**通信频道**
- `/add-signal` — 添加 Signal 作为可用频道

## 环境要求

- macOS 或 Linux（Windows 需通过 WSL2）
- Node.js 20+ 和 pnpm 10+（安装程序会自动检测并安装缺失项）
- [Docker Desktop](https://docker.com/products/docker-desktop)（macOS/Windows）或 Docker Engine（Linux）
- [Claude Code](https://claude.ai/download) 用于 `/customize`、`/debug`、安装过程中的错误恢复，以及所有 `/add-<channel>` 技能

## 架构设计

```
messaging apps → host process (router) → inbound.db → container (Bun, Claude Agent SDK) → outbound.db → host process (delivery) → messaging apps
```

单个 Node.js 主机编排每个会话的 Agent 容器。当消息到达时，主机通过实体模型（用户 → 消息组 → Agent 组 → 会话）进行路由，将其写入会话的 `inbound.db`，并唤醒容器。容器内的 agent-runner 轮询 `inbound.db`，运行 Claude，并将响应写入 `outbound.db`。主机轮询 `outbound.db` 并通过频道适配器将消息发送回去。

每个会话仅两个 SQLite 文件，且各自只有一个写入者——无跨挂载点竞争、无需 IPC（进程间通信）、无需 stdin 管道传输。频道和替代提供商在启动时自动注册；主干代码提供注册表和 Chat SDK 桥接，而适配器本身通过技能按需安装到各个 Fork 中。

完整架构说明见 [docs/architecture.md](docs/architecture.md)；三级隔离模型详见 [docs/isolation-model.md](docs/isolation-model.md)。

关键文件：
- `src/index.ts` — 入口点：DB 初始化、频道适配器、投递轮询、清理任务
- `src/router.ts` — 入站路由：消息组 → Agent 组 → 会话 → `inbound.db`
- `src/delivery.ts` — 轮询 `outbound.db`，通过适配器投递，处理系统级操作
- `src/host-sweep.ts` — 60秒清理任务：过期检测、到期唤醒、循环调度
- `src/session-manager.ts` — 解析会话，打开 `inbound.db` / `outbound.db`
- `src/container-runner.ts` — 按 Agent 组启动容器，OneCLI 凭据注入
- `src/db/` — 中央数据库（用户、角色、Agent 组、消息组、路由配置、迁移脚本）
- `src/channels/` — 频道适配器基础设施（通过 `/add-<channel>` 技能安装）
- `src/providers/` — 主机端提供商配置（内置 `claude`；其他通过技能提供）
- `container/agent-runner/` — Bun agent-runner：轮询循环、MCP 工具、提供商抽象层
- `groups/<folder>/` — 按 Agent 组的文件系统结构（CLAUDE.md、技能、容器配置）

## 常见问题

**为什么使用 Docker？**

Docker 提供跨平台支持（macOS、Linux 和 Windows via WSL2）且生态成熟。在 macOS 上，你可以通过 `/convert-to-apple-container` 切换至 Apple Container 以获得更轻量的原生运行时。如需额外隔离层，[Docker Sandboxes](docs/docker-sandboxes.md) 可在微虚拟机内运行每个容器。

**能在 Linux 或 Windows 上运行吗？**

可以。Docker 是默认运行时，兼容 macOS、Linux 和 Windows（通过 WSL2）。只需运行 `bash nanoclaw.sh` 即可。

**这安全吗？**

Agent 运行在容器中，而非依赖应用层权限检查。它们只能访问显式挂载的目录。凭据绝不会进入容器——出站 API 请求通过 [OneCLI 的 Agent Vault](https://github.com/onecli/onecli) 路由，该服务在代理层注入认证信息并支持速率限制和访问策略。你仍应审查运行的内容，但得益于代码库足够小，这完全可行。详见 [安全文档](https://docs.nanoclaw.dev/concepts/security)。

**为什么不使用配置文件？**

我们拒绝配置泛滥（configuration sprawl）。每个用户都应定制 NanoClaw 使代码精确符合需求，而非配置一个通用系统。如果你偏好配置文件，可以告诉 Claude 添加它们。

**可以使用第三方或开源模型吗？**

可以。官方支持的路径是 `/add-opencode`（通过 OpenCode 接入 OpenRouter、OpenAI、Google、DeepSeek 等）或 `/add-ollama-provider`（通过 Ollama 使用本地开源权重模型）。两者均可按 Agent 组配置，因此同一安装中不同 Agent 可运行在不同后端上。

对于一次性实验，任何兼容 Claude API 的端点也可通过 `.env` 环境变量临时指定：

```bash
ANTHROPIC_BASE_URL=https://your-api-endpoint.com
ANTHROPIC_AUTH_TOKEN=your-token-here
```

**如何调试问题？**

直接询问 Claude Code。“为什么调度器没运行？”“最近的日志里有什么？”“这条消息为什么没有回复？”这正是支撑 NanoClaw 的原生 AI 交互方式。

**为什么我的安装流程不工作？**

如果某一步骤失败，`nanoclaw.sh` 会自动移交至 Claude Code 进行诊断和恢复。若仍未解决，请手动运行 `claude`，然后输入 `/debug`。如果 Claude 识别出可能影响其他用户的问题，请针对相关安装步骤或技能提交 PR。

**哪些修改会被合并到主干代码中？**

仅安全修复、Bug 修复和明确的改进会被接受至基础配置。仅此而已。

其余所有功能（新能力、OS 兼容性、硬件支持、增强特性）应作为技能贡献至 `channels` 或 `providers` 分支。这能保持基础系统精简，并允许每个用户自定义安装而不继承不需要的功能。

## 社区

有疑问？有想法？[加入 Discord](https://discord.gg/VDdww8qS42)。

## 更新日志

查看 [CHANGELOG.md](CHANGELOG.md) 了解破坏性变更，或访问文档站点的 [完整发布历史](https://docs.nanoclaw.dev/changelog)。

## 许可证

MIT

<img referrerpolicy="no-referrer-when-downgrade" src="https://static.scarf.sh/a.png?x-pxid=47894bd5-353b-42fe-bb97-74144e6df0bf" />