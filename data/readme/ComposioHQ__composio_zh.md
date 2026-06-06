<div align="center">

<img src="https://raw.githubusercontent.com/ComposioHQ/composio/next/public/cover.png" alt="Composio Logo" width="auto" height="auto" style="margin-bottom: 20px;"/>


# Composio SDK

为智能体（Agents）持续进化的技能

[🌐 Website](https://composio.dev) • [📚 Documentation](https://docs.composio.dev)

[![GitHub Stars](https://img.shields.io/github/stars/ComposioHQ/composio?style=social)](https://github.com/ComposioHQ/composio/stargazers)
[![PyPI Downloads](https://img.shields.io/pypi/dm/composio?label=PyPI%20Downloads)](https://pypi.org/project/composio/)
[![NPM Downloads](https://img.shields.io/npm/dt/@composio/core?label=NPM%20Downloads)](https://www.npmjs.com/package/@composio/core)
[![Discord](https://img.shields.io/badge/Discord-join-5865F2?logo=discord&logoColor=white)](https://discord.gg/composio)
</div>

本仓库包含 Composio 的官方软件开发工具包（SDK），提供与 Python 和 TypeScript 智能体框架及库无缝集成的能力。

## 入门指南

### TypeScript SDK 安装

```bash
# Using npm
npm install @composio/core

# Using yarn
yarn add @composio/core

# Using pnpm
pnpm add @composio/core
```

#### 快速开始：

```typescript
import { Composio } from '@composio/core';
// Initialize the SDK
const composio = new Composio({
  // apiKey: 'your-api-key',
});
```

#### 使用 OpenAI Agents 创建简单智能体

```bash
npm install @composio/openai-agents @openai/agents
```

```typescript
import { Composio } from '@composio/core';
import { OpenAIAgentsProvider } from '@composio/openai-agents';
import { Agent, run } from '@openai/agents';

const composio = new Composio({
  provider: new OpenAIAgentsProvider(),
});

const userId = 'user@acme.org';

const tools = await composio.tools.get(userId, {
  toolkits: ['HACKERNEWS'],
});

const agent = new Agent({
  name: 'Hackernews assistant',
  tools: tools,
});

const result = await run(agent, 'What is the latest hackernews post about?');

console.log(JSON.stringify(result.finalOutput, null, 2));
// will return the response from the agent with data from HACKERNEWS API.
```

### Python SDK 安装

```bash
# Using pip
pip install composio

# Using poetry
poetry add composio
```

#### 快速开始：

```python
from composio import Composio

composio = Composio(
  # api_key="your-api-key",
)
```

#### 使用 OpenAI Agents 创建简单智能体

```bash
pip install composio_openai_agents openai-agents
```

```python
import asyncio
from agents import Agent, Runner
from composio import Composio
from composio_openai_agents import OpenAIAgentsProvider

# Initialize Composio client with OpenAI Agents Provider
composio = Composio(provider=OpenAIAgentsProvider())

user_id = "user@acme.org"
tools = composio.tools.get(user_id=user_id, toolkits=["HACKERNEWS"])

# Create an agent with the tools
agent = Agent(
    name="Hackernews Agent",
    instructions="You are a helpful assistant.",
    tools=tools,
)

# Run the agent
async def main():
    result = await Runner.run(
        starting_agent=agent,
        input="What's the latest Hackernews post about?",
    )
    print(result.final_output)

asyncio.run(main())
# will return the response from the agent with data from HACKERNEWS API.
```

如需更详细的使用说明和示例，请参阅各 SDK 的专属文档。

### OpenAPI 规范

要更新用于生成 SDK 文档的 OpenAPI 规范：

```bash
# Pull the latest API specifications from the backend
pnpm api:pull
```

该命令会从 `https://backend.composio.dev/api/v3/openapi.json` 拉取 OpenAPI 规范，并更新本地 API 文档文件。

构建步骤会自动执行此操作。

## 可用 SDK

### TypeScript SDK (/ts)

TypeScript SDK 提供了一种现代化且类型安全的交互方式，用于调用 Composio 服务。它专为 Node.js 和浏览器环境设计，提供完整的 TypeScript 支持及全面的类型定义。

有关 TypeScript SDK 的详细信息，请参阅 [TypeScript SDK 文档](/ts/README.md)。

### Python SDK (/python)

Python SDK 提供了符合 Python 编程习惯的接口，便于将 Composio 集成到你的 Python 应用中。它支持 Python 3.10+，并遵循现代 Python 开发实践。

有关 Python SDK 的详细信息，请参阅 [Python SDK 文档](/python/README.md)。

## 提供商支持

下表展示了各 SDK 支持的 AI 框架与平台：

| Provider | TypeScript | Python |
|----------|:----------:|:------:|
| OpenAI | ✅ | ✅ |
| OpenAI Agents | ✅ | ✅ |
| Anthropic | ✅ | ✅ |
| LangChain | ✅ | ✅ |
| LangGraph | ✅* | ✅ |
| LlamaIndex | ✅ | ✅ |
| Vercel AI SDK | ✅ | ❌ |
| Google Gemini | ✅ | ✅ |
| Google ADK | ❌ | ✅ |
| Mastra | ✅ | ❌ |
| Cloudflare Workers AI | ✅ | ❌ |
| CrewAI | ❌ | ✅ |
| AutoGen | ❌ | ✅ |

\* *TypeScript 中的 LangGraph 通过 `@composio/langchain` 包提供支持。*

> **没找到你的提供商？** 了解如何[构建自定义提供商](https://docs.composio.dev/sdk/typescript/custom-providers)以集成任意 AI 框架。

## 软件包

### 核心软件包

| Package | Version |
|---------|---------|
| **TypeScript** | |
| [@composio/core](https://www.npmjs.com/package/@composio/core) | ![npm version](https://img.shields.io/npm/v/@composio/core) |
| **Python** | |
| [composio](https://pypi.org/project/composio/) | ![PyPI version](https://img.shields.io/pypi/v/composio) |

### 提供商软件包

| Package | Version |
|---------|---------|
| **TypeScript** | |
| [@composio/openai](https://www.npmjs.com/package/@composio/openai) | ![npm version](https://img.shields.io/npm/v/@composio/openai) |
| [@composio/openai-agents](https://www.npmjs.com/package/@composio/openai-agents) | ![npm version](https://img.shields.io/npm/v/@composio/openai-agents) |
| [@composio/anthropic](https://www.npmjs.com/package/@composio/anthropic) | ![npm version](https://img.shields.io/npm/v/@composio/anthropic) |
| [@composio/langchain](https://www.npmjs.com/package/@composio/langchain) | ![npm version](https://img.shields.io/npm/v/@composio/langchain) |
| [@composio/llamaindex](https://www.npmjs.com/package/@composio/llamaindex) | ![npm version](https://img.shields.io/npm/v/@composio/llamaindex) |
| [@composio/vercel](https://www.npmjs.com/package/@composio/vercel) | ![npm version](https://img.shields.io/npm/v/@composio/vercel) |
| [@composio/google](https://www.npmjs.com/package/@composio/google) | ![npm version](https://img.shields.io/npm/v/@composio/google) |
| [@composio/mastra](https://www.npmjs.com/package/@composio/mastra) | ![npm version](https://img.shields.io/npm/v/@composio/mastra) |
| [@composio/cloudflare](https://www.npmjs.com/package/@composio/cloudflare) | ![npm version](https://img.shields.io/npm/v/@composio/cloudflare) |
| **Python** | |
| [composio-openai](https://pypi.org/project/composio-openai/) | ![PyPI version](https://img.shields.io/pypi/v/composio-openai) |
| [composio-openai-agents](https://pypi.org/project/composio-openai-agents/) | ![PyPI version](https://img.shields.io/pypi/v/composio-openai-agents) |
| [composio-anthropic](https://pypi.org/project/composio-anthropic/) | ![PyPI version](https://img.shields.io/pypi/v/composio-anthropic) |
| [composio-langchain](https://pypi.org/project/composio-langchain) | ![PyPI version](https://img.shields.io/pypi/v/composio-langchain) |
| [composio-langgraph](https://pypi.org/project/composio-langgraph/) | ![PyPI version](https://img.shields.io/pypi/v/composio-langgraph) |
| [composio-llamaindex](https://pypi.org/project/composio-llamaindex/) | ![PyPI version](https://img.shields.io/pypi/v/composio-llamaindex) |
| [composio-crewai](https://pypi.org/project/composio-crewai/) | ![PyPI version](https://img.shields.io/pypi/v/composio-crewai) |
| [composio-autogen](https://pypi.org/project/composio-autogen/) | ![PyPI version](https://img.shields.io/pypi/v/composio-autogen) |
| [composio-gemini](https://pypi.org/project/composio-gemini/) | ![PyPI version](https://img.shields.io/pypi/v/composio-gemini) |
| [composio-google](https://pypi.org/project/composio-google/) | ![PyPI version](https://img.shields.io/pypi/v/composio-google) |
| [composio-google-adk](https://pypi.org/project/composio-google-adk/) | ![PyPI version](https://img.shields.io/pypi/v/composio-google-adk) |

### 工具软件包

| Package | Version |
|---------|---------|
| [@composio/json-schema-to-zod](https://www.npmjs.com/package/@composio/json-schema-to-zod) | ![npm version](https://img.shields.io/npm/v/@composio/json-schema-to-zod) |
| [@composio/ts-builders](https://www.npmjs.com/package/@composio/ts-builders) | ![npm version](https://img.shields.io/npm/v/@composio/ts-builders) |

_if you are looking for the older sdk, you can find them [here](https://github.com/ComposioHQ/composio/tree/master)_ -> _如果你正在寻找旧版 SDK，可以在[这里](https://github.com/ComposioHQ/composio/tree/master)找到它们。_

## Rube

[Rube](https://rube.app) 是一款基于 Composio 构建的模型上下文协议（MCP）服务器。它将你的 AI 工具连接到 Gmail、Slack、GitHub 和 Notion 等 500 多个应用。只需在 AI 客户端中安装，一次性完成应用认证，即可让 AI 执行“发送电子邮件”或“创建任务”等实际操作。 

它支持 Cursor、Claude Desktop、VS Code、Claude Code 以及任何自定义 MCP 兼容客户端。你可以在这些客户端之间切换，你的集成配置将随之跟随。

## 贡献指南

我们欢迎对两个 SDK 的贡献！提交拉取请求（Pull Request）前，请阅读我们的[贡献指南](https://github.com/ComposioHQ/composio/blob/next/CONTRIBUTING.md)。

## 许可证

本项目采用 MIT 许可证开源——详见 LICENSE 文件。

## 技术支持

如果你在遇到任何问题或对 SDK 有任何疑问：

- 在此仓库中提交 Issue
- 联系我们的 [支持团队](mailto:support@composio.dev)
- 查阅我们的 [文档](https://docs.composio.dev/)