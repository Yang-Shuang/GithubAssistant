[![Memori Labs](https://images.memorilabs.ai/banner-dark-large.jpg)](https://memorilabs.ai/)

<p align="center">
  <strong>记忆源于智能体的行为，而不仅仅是其言语。</strong>
</p>

<p align="center">
  <i>Memori 无缝接入你已使用的软件与基础设施。它不依赖特定的大语言模型（LLM）、数据存储或框架，可与你既有的架构完美融合。</i>
</p>

<p align="center">
  <strong>→ <a href="https://memorilabs.ai/docs/memori-cloud/">Memori Cloud</a></strong> —— 零配置。获取 API Key，几分钟内即可开始构建。
</p>
<p align="center">
  <a href="https://trendshift.io/repositories/15435" target="_blank"><img src="https://trendshift.io/api/badge/repositories/15435" alt="MemoriLabs%2FMemori | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

<p align="center">
  <a href="https://badge.fury.io/py/memori">
    <img src="https://badge.fury.io/py/memori.svg" alt="PyPI version">
  </a>
  <a href="https://www.npmjs.com/package/@memorilabs/memori">
    <img src="https://img.shields.io/npm/v/@memorilabs/memori.svg" alt="NPM version">
  </a>
  <a href="https://pepy.tech/projects/memori">
    <img src="https://static.pepy.tech/badge/memori" alt="Downloads">
  </a>
  <a href="https://opensource.org/license/apache-2-0">
    <img src="https://img.shields.io/badge/license-Apache%202.0-blue" alt="License">
  </a>
  <a href="https://discord.gg/abD4eGym6v">
    <img src="https://img.shields.io/discord/1042405378304004156?logo=discord" alt="Discord">
  </a>
</p>

<p align="center">
  <a href="https://github.com/MemoriLabs/Memori/stargazers">
    <img src="https://img.shields.io/badge/⭐%20Give%20a%20Star-Support%20the%20project-orange?style=for-the-badge" alt="Give a Star">
  </a>
</p>

<p align="center">
  <strong>选择真正高效运行的记忆方案</strong>
</p>



[![Memori Labs](https://images.memorilabs.ai/stats.jpg)](https://memorilabs.ai/benchmark)

---

## Getting Started（快速开始）

### Installation（安装）

<details open>
<summary><b>TypeScript SDK</b></summary>

```bash
npm install @memorilabs/memori
```
</details>

<details open>
<summary><b>Python SDK</b></summary>

```bash
pip install memori
```
</details>

### Quickstart（快速上手）

前往 [app.memorilabs.ai](https://app.memorilabs.ai) 注册，获取 Memori API Key，即可开始构建。完整文档：[memorilabs.ai/docs/memori-cloud/](https://memorilabs.ai/docs/memori-cloud/)。

设置 `MEMORI_API_KEY` 和你的大语言模型（LLM）API Key（例如 `OPENAI_API_KEY`），然后：

<details open>
<summary><b>TypeScript SDK</b></summary>

```typescript
import { OpenAI } from 'openai';
import { Memori } from '@memorilabs/memori';

// Requires MEMORI_API_KEY and OPENAI_API_KEY in your environment
const client = new OpenAI();
const mem = new Memori().llm
  .register(client)
  .attribution('user_123', 'support_agent');

async function main() {
  await client.chat.completions.create({
    model: 'gpt-4o-mini',
    messages: [{ role: 'user', content: 'My favorite color is blue.' }],
  });
  // Conversations are persisted and recalled automatically in the background.

  const response = await client.chat.completions.create({
    model: 'gpt-4o-mini',
    messages: [{ role: 'user', content: "What's my favorite color?" }],
  });
  // Memori recalls that your favorite color is blue.
}
```
</details>

<details open>
<summary><b>Python SDK</b></summary>

```python
from memori import Memori
from openai import OpenAI

# Requires MEMORI_API_KEY and OPENAI_API_KEY in your environment
client = OpenAI()
mem = Memori().llm.register(client)

mem.attribution(entity_id="user_123", process_id="support_agent")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "My favorite color is blue."}]
)
# Conversations are persisted and recalled automatically.

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "What's my favorite color?"}]
)
# Memori recalls that your favorite color is blue.
```
</details>

## Explore the Memories（探索记忆）

使用 [控制台](https://app.memorilabs.ai) —— 查看记忆、分析数据、运行沙盒（Playground）以及管理 API Key。

> [!TIP]
> 想使用自己的数据库？请查阅 Memori BYODB（自带数据库）文档：
> [https://memorilabs.ai/docs/memori-byodb/](https://memorilabs.ai/docs/memori-byodb/)。
> 对于临时性 BYODB 开发数据库，请参阅 TiDB Zero 配置指南：
> [docs/memori-byodb/databases/tidb.mdx](docs/memori-byodb/databases/tidb.mdx)。

## LoCoMo Benchmark（基准测试）

在 LoCoMo 长对话记忆基准测试中，Memori 取得了 **81.95%** 的整体准确率，同时每次查询平均仅消耗 **1,294 个 token**。这仅相当于完整上下文占用量的 **4.97%**，证明了结构化内存可以在不向每次请求强行注入大提示词（Prompt）的情况下，保持推理质量。

与其他基于检索的记忆系统相比，Memori 的表现优于 Zep、LangMem 和 Mem0，同时提示词体积较 Zep 减少了约 **67%**，上下文成本较完整上下文提示方式降低了 **20 倍以上**。

阅读[基准测试概览](docs/memori-cloud/benchmark/overview.mdx)，查看[测试结果](docs/memori-cloud/benchmark/results.mdx)，或下载[研究论文](https://arxiv.org/abs/2603.19935)。

!["Memori's average accuracy along with the standard deviation"](https://images.memorilabs.ai/docs/memori-locomo-benchmark.webp)

## OpenClaw (Persistent Memory for Your Gateway)（OpenClaw 网关的持久化记忆）

默认情况下，OpenClaw 智能体在会话之间会遗忘所有内容。Memori 插件解决了这一问题。它会在每次交互后自动捕获对话与智能体执行过程中的结构化记忆——包括工具调用、决策及结果——供智能体按需检索。

无需修改你的智能体代码或提示词。该插件直接接入 OpenClaw 的生命周期，让你只需安装一个即插即用型（drop-in）插件，即可获得结构化记忆、智能体可控检索以及高级增强功能。

```bash
openclaw plugins install @memorilabs/openclaw-memori
openclaw plugins enable openclaw-memori

openclaw memori init \
  --api-key "YOUR_MEMORI_API_KEY" \
  --entity-id "your-app-user-id" \
  --project-id "my-project"

openclaw gateway restart
```

有关设置与配置，请参阅[OpenClaw 快速上手指南](docs/memori-cloud/openclaw/quickstart.mdx)。有关架构与生命周期详情，请参阅[OpenClaw 概述](docs/memori-cloud/openclaw/overview.mdx)。

## Hermes Agent (Persistent Memory Provider)（Hermes Agent 持久化记忆提供者）

Memori 同时也作为 Hermes Agent 的记忆提供者发布。它会在后台捕获已完成的对话，并为 Hermes 提供明确的 `memori_recall` 和 `memori_recall_summary` 工具，供智能体控制检索过程。

```bash
pip install hermes-memori
hermes-memori install

hermes config set memory.provider memori
HERMES_HOME="${HERMES_HOME:-$HOME/.hermes}"
mkdir -p "$HERMES_HOME"
echo "MEMORI_API_KEY=YOUR_MEMORI_API_KEY" >> "$HERMES_HOME/.env"
echo "MEMORI_ENTITY_ID=your-app-user-id" >> "$HERMES_HOME/.env"
```

可选参数 `MEMORI_PROJECT_ID`：若未提供，该提供者将使用 Hermes 的当前活动项目上下文进行作用域划分。

有关设置与配置，请参阅[Hermes 快速上手指南](docs/memori-cloud/hermes/quickstart.mdx)。有关架构与生命周期详情，请参阅[Hermes 概述](docs/memori-cloud/hermes/overview.mdx)。

## MCP (Connect Your Agent in One Command)（MCP：一条命令连接智能体）

你的智能体在会话之间会遗忘所有内容。Memori 解决了这一问题。它会记住你的技术栈、编码规范以及你偏好的操作方式，让你无需重复说明。

适用于独立开发者与团队。你的智能体会随时间推移学习代码模式、审查者偏好及项目规范。对团队而言，这意味着共享上下文：新工程师可在入职第一天就快速上手，无需耗费数月去摸索团队隐性经验。

如果你使用 Claude Code、Cursor、Codex、Warp 或 Antigravity，无需进行 SDK 集成即可连接 Memori：

```bash
claude mcp add --transport http memori https://api.memorilabs.ai/mcp/ \
  --header "X-Memori-API-Key: ${MEMORI_API_KEY}" \
  --header "X-Memori-Entity-Id: your_username" \
  --header "X-Memori-Process-Id: claude-code"
```

对于 Cursor、Codex、Warp 及其他客户端，请参阅[MCP 客户端设置指南](docs/memori-cloud/mcp/client-setup.mdx)。

## Attribution（归属标识）

为了充分发挥 Memori 的效能，你需要将大语言模型（LLM）交互关联到一个实体（Entity，如人、地点或事物；例如用户）和一个流程/进程（Process，如你的智能体、LLM 交互或程序）。

如果你不提供任何归属标识，Memori 将无法为你生成记忆。

<details open>
<summary><b>TypeScript SDK</b></summary>

```typescript
mem.attribution("12345", "my-ai-bot");
```
</details>

<details open>
<summary><b>Python SDK</b></summary>

```python
mem.attribution(entity_id="12345", process_id="my-ai-bot")
```
</details>

## Session Management（会话管理）

Memori 使用会话（Session）来分组你的大语言模型交互。例如，如果你的智能体需要执行多个步骤，你希望将这些操作记录在同一个会话中。

默认情况下，Memori 会自动为你管理会话设置。但你可以通过运行以下命令来开启新会话或覆盖当前会话：

<details open>
<summary><b>TypeScript SDK</b></summary>

```typescript
mem.resetSession();
// or
mem.setSession(sessionId);
```
</details>

<details open>
<summary><b>Python SDK</b></summary>

```python
mem.new_session()
# or
mem.set_session(session_id)
```
</details>

## Supported LLMs（支持的大语言模型）

- Anthropic
- Bedrock
- DeepSeek
- Gemini
- Grok (xAI)
- OpenAI (Chat Completions & Responses API)

_(unstreamed, streamed, synchronous and asynchronous)_

## Supported Frameworks（支持的框架）

- Agno
- LangChain
- Pydantic AI

## Supported Platforms（支持的平台）

- DeepSeek
- Nebius AI Studio

## Examples（示例）

如需更多示例与演示，请查看 [Memori Cookbook](https://github.com/MemoriLabs/memori-cookbook)。

## Memori Advanced Augmentation（Memori 高级增强功能）

记忆在以下几个不同层级进行追踪：

- **entity**：实体（如人、地点或事物；例如用户）
- **process**：流程/进程（你的智能体、LLM 交互或程序）
- **session**：会话（当前实体、流程与 LLM 之间的交互）

[Memori 高级增强功能](docs/memori-cloud/concepts/advanced-augmentation.mdx) 在这些层级上为记忆增加了以下属性：

- attributes（属性）
- events（事件）
- facts（事实）
- people（人物）
- preferences（偏好）
- relationships（关系）
- rules（规则）
- skills（技能）

Memori 清楚你的用户是谁、智能体处理哪些任务，并在两者之间构建无与伦比的上下文关联。增强功能在后台运行，不会产生额外延迟。

默认情况下，Memori 高级增强功能无需账号即可使用，但存在速率限制。当你需要更高的限额时，可[注册 Memori 高级增强服务](https://app.memorilabs.ai/signup)，或使用 Memori CLI：

```bash
# Install the CLI via pip to manage your account
python -m memori sign-up <email_address>
```

Memori 高级增强功能对开发者始终免费！

获取 API Key 后，请设置以下环境变量（Python 和 TypeScript SDK 均使用）：

```bash
export MEMORI_API_KEY=[api_key]
```

Memori CLI 会优先读取你导出的环境变量，若缺失则自动从运行命令所在目录的 `.env` 文件中填充。

## Managing Your Quota（配额管理）

随时可通过 Memori CLI 检查你的配额（适用于所有 SDK）：

```bash
python -m memori quota
```

或登录 [https://app.memorilabs.ai/](https://app.memorilabs.ai/) 查看账户信息。如果你的 IP 地址配额已用尽，请注册并获取 API Key 以提升限额。

若你的 API Key 超出配额限制，我们将通过邮件通知你。

## Command Line Interface (CLI)（命令行界面）

Memori CLI 是统一管理所有 SDK 账号、密钥和配额的集成工具。在命令行中执行以下命令即可使用：

```bash
# Requires Python installed
python -m memori
```

这将显示可用选项菜单。如需了解 Memori CLI 的更多功能，请参阅[命令行界面](docs/memori-byodb/concepts/cli-quickstart.mdx)。

## Contributing（贡献指南）

我们欢迎社区的贡献！有关以下内容的详细信息，请参阅我们的 [Contributing Guidelines](https://github.com/MemoriLabs/Memori/blob/main/CONTRIBUTING.md)：

- 搭建开发环境
- 代码风格与规范
- 提交 Pull Request
- 报告问题

---

## Support（支持）

- [**Memori Cloud Documentation**](https://memorilabs.ai/docs/memori-cloud)
- [**Memori BYODB Documentation**](https://memorilabs.ai/docs/memori-byodb)
- [**Discord**](https://discord.gg/FpytKAxnFb)
- [**Issues**](https://github.com/MemoriLabs/Memori/issues)
---

## License（许可证）

Apache 2.0 - see [LICENSE](https://github.com/MemoriLabs/Memori/blob/main/LICENSE)