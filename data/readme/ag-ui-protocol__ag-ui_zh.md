# <img src="https://github.com/user-attachments/assets/ebc0dd08-8732-4519-9b6c-452ce54d8058" alt="ag-ui Logo" width="22"/> AG-UI：智能体与用户交互协议

AG-UI 是一项开源、轻量级的基于事件（event）的协议，旨在标准化 AI 智能体如何连接到面向用户的应用程序。该协议以简洁和灵活为设计核心，实现了 AI 智能体、实时用户上下文与用户界面之间的无缝集成。

---


<br>


[![Version](https://img.shields.io/npm/v/@ag-ui/core?label=Version&color=6963ff&logo=npm&logoColor=white)](https://www.npmjs.com/package/@ag-ui/core)
![MIT](https://img.shields.io/github/license/copilotkit/copilotkit?color=%236963ff&label=License)
![Discord](https://img.shields.io/discord/1379082175625953370?logo=discord&logoColor=%23FFFFFF&label=Discord&color=%236963ff)

<a href="https://discord.gg/Jd3FzfdJa8" target="_blank"> 加入我们的 Discord → </a> &nbsp;&nbsp;&nbsp; <a href="https://ag-ui.com/" target="_blank"> 阅读文档 → </a> &nbsp;&nbsp;&nbsp; <a href="https://dojo.ag-ui.com/" target="_blank"> 前往 AG-UI Dojo → </a> &nbsp;&nbsp;&nbsp; <a href="https://x.com/CopilotKit" target="_blank"> 关注我们 → </a>

<img width="1600" height="680" alt="1600x680" src="https://github.com/user-attachments/assets/00ec7366-713e-443f-a8f0-8db52ad28ef4" />



## 🚀 快速开始
在几秒内创建一个新的 AG-UI 应用：
```bash
npx create-ag-ui-app my-agent-app
```

<h3> 常用链接：</h3>

- [AG-UI Dojo（演练场）](https://dojo.ag-ui.com/)
- [构建基于 AG-UI 的应用程序（快速入门）](https://docs.ag-ui.com/quickstart/applications)
- [开发新的 AG-UI 框架集成（快速入门）](https://go.copilotkit.ai/agui-contribute)
- [预约通话，探讨新框架的 AG-UI 集成方案](https://calendly.com/markus-copilotkit/ag-ui)
- [加入 Discord 社区](https://discord.gg/Jd3FzfdJa8)

## 什么是 AG-UI？

AG-UI 是一项面向智能体与人交互的开源、轻量级基于事件（event）协议，专为简洁与灵活而设计：

- 在智能体执行过程中，后端服务会**发出与 AG-UI 的约 16 种标准事件类型之一兼容的事件（event）**
- 智能体后端可作为参数**接收几种简单的、符合 AG-UI 标准的输入（input）**

**AG-UI 包含一个灵活的中间件层（middleware layer）**，以确保跨不同环境的兼容性：

- 支持**任意事件传输方式**（如 SSE、WebSockets、webhook 等）
- 允许**宽松的事件格式匹配**，从而实现广泛的智能体与应用互操作性

此外，它还附带了**参考版 HTTP 实现（implementation）**和**默认连接器（connector）**，帮助团队快速上手。


[了解更多规范详情 →](https://go.copilotkit.ai/ag-ui-introduction)


## 为什么选择 AG-UI？

AG-UI 基于实际业务需求以及在应用内构建智能体交互的实践经验而开发。


## AG-UI 在智能体协议栈中的定位？
AG-UI 与其他两大主流智能体协议互为补充：
- MCP（Model Context Protocol）为智能体提供工具调用能力
- A2A（Agent-to-Agent）允许智能体之间相互通信
- AG-UI 将智能体引入面向用户的应用程序中

<div align="center">
  <img width="2048" height="1182" alt="The Agent Protocol Stack" src="https://github.com/user-attachments/assets/41138f71-50be-4812-98aa-20e0ad595716" />
</div>

## 🚀 核心特性

- 💬 支持流式传输（streaming）的实时智能体对话
- 🔄 双向状态同步
- 🧩 生成式用户界面（Generative UI）与结构化消息
- 🧠 实时上下文增强
- 🛠️ 前端工具集成
- 🧑‍💻 人机协同（Human-in-the-loop）协作


## 🛠 支持的集成方案

AG-UI 源于 CopilotKit 最初与 LangGraph 和 CrewAI 的**合作**——它将备受瞩目的智能体用户交互基础设施带入了更广泛的智能体生态系统。

**官方（1st Party）** = 内置 AG‑UI 并提供指导文档的平台。

## 框架集成

| Framework                                                          | Status                   | AG-UI Resources                                                                 |
| ------------------------------------------------------------------ | ------------------------ | -------------------------------------------------------------------------------- |
| Built-in Agent                                                | ✅ Supported             | ➡️ [Docs](https://docs.copilotkit.ai/direct-to-llm)  |

### 🤝 合作伙伴集成
| Framework | Status | AG-UI Resources |
| ---------- | ------- | ---------------- |
| [LangGraph](https://www.langchain.com/langgraph) | ✅ Supported | ➡️ [Docs](https://docs.copilotkit.ai/langgraph/) 🎮 [Demos](https://dojo.ag-ui.com/langgraph-fastapi/feature/shared_state) |
| [CrewAI](https://crewai.com/) | ✅ Supported | ➡️ [Docs](https://docs.copilotkit.ai/crewai-flows) 🎮 [Demos](https://dojo.ag-ui.com/crewai/feature/shared_state) |

### 🧩 官方（1st Party）
| Framework | Status | AG-UI Resources |
| ---------- | ------- | ---------------- |
| [Microsoft Agent Framework](https://azure.microsoft.com/en-us/blog/introducing-microsoft-agent-framework/) | ✅ Supported | ➡️ [Docs](https://docs.copilotkit.ai/microsoft-agent-framework) 🎮 [Demos](https://dojo.ag-ui.com/microsoft-agent-framework-dotnet/feature/shared_state) |
| [Google ADK](https://google.github.io/adk-docs/get-started/) | ✅ Supported | ➡️ [Docs](https://docs.copilotkit.ai/adk) 🎮 [Demos](https://dojo.ag-ui.com/adk-middleware/feature/shared_state?openCopilot=true) |
| [AWS Strands Agents](https://github.com/strands-agents/sdk-python) | ✅ Supported | ➡️ [Docs](https://docs.copilotkit.ai/aws-strands) 🎮 [Demos](https://dojo.ag-ui.com/aws-strands/feature/shared_state) |
| [Mastra](https://mastra.ai/) | ✅ Supported | ➡️ [Docs](https://docs.copilotkit.ai/mastra/) 🎮 [Demos](https://dojo.ag-ui.com/mastra/feature/tool_based_generative_ui) |
| [Pydantic AI](https://github.com/pydantic/pydantic-ai) | ✅ Supported | ➡️ [Docs](https://docs.copilotkit.ai/pydantic-ai/) 🎮 [Demos](https://dojo.ag-ui.com/pydantic-ai/feature/shared_state) |
| [Agno](https://github.com/agno-agi/agno) | ✅ Supported | ➡️ [Docs](https://docs.copilotkit.ai/agno/) 🎮 [Demos](https://dojo.ag-ui.com/agno/feature/tool_based_generative_ui) |
| [LlamaIndex](https://github.com/run-llama/llama_index) | ✅ Supported | ➡️ [Docs](https://docs.copilotkit.ai/llamaindex/) 🎮 [Demos](https://dojo.ag-ui.com/llamaindex/feature/shared_state) |
| [AG2](https://ag2.ai/) | ✅ Supported | ➡️ [Docs](https://docs.copilotkit.ai/ag2/)  🎮 [Demos](https://dojo.ag-ui.com/ag2/feature/shared_state) |
| [AWS Bedrock Agents](https://aws.amazon.com/bedrock/agents/) | 🛠️ In Progress | – |



### 🌐 社区集成
| Framework | Status | AG-UI Resources |
| ---------- | ------- | ---------------- |
| [Claude Agent SDK](https://github.com/ag-ui-protocol/ag-ui/tree/main/integrations/claude-agent-sdk) | ✅ Supported | 🎮 [Demos](https://dojo.ag-ui.com/claude-agent-sdk-python/feature/shared_state) |
| [Langroid](https://github.com/ag-ui-protocol/ag-ui/tree/main/integrations/langroid) | ✅ Supported | 🎮 [Demos](https://dojo.ag-ui.com/langroid/feature/shared_state) |
| [OpenAI Agent SDK](https://openai.github.io/openai-agents-python/) | 🛠️ In Progress | – |
| [Cloudflare Agents](https://developers.cloudflare.com/agents/) | 🛠️ In Progress | – |


## 智能体交互协议

| Protocols | Status | AG-UI Resources | Integrations |
| ---------- | ------- | ---------------- | ------------- |
| [A2A]() | ✅ Supported | ➡️ [Docs](https://docs.copilotkit.ai/a2a-protocol) | Partnership |


## 基础设施 / 部署平台
| Platform | Status | AG-UI Resources | Integrations |
| ---------- | ------- | ---------------- | ------------- |
| [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) | ✅ Supported | ➡️ [Docs](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-agui.html) | 1st Party |


## 规范（标准）
| Framework | Status | AG-UI Resources |
| ---------- | ------- | ---------------- |
| [Oracle Agent Spec](http://oracle.github.io/agent-spec/) | ✅ Supported | ➡️ [Docs](https://go.copilotkit.ai/copilotkit-oracle-docs) 🎮 [Demos](https://dojo.ag-ui.com/agent-spec-langgraph/feature/tool_based_generative_ui) |

## 生成式用户界面（Generative UI）
| Framework | Status | AG-UI Resources |
| ---------- | ------- | ---------------- |
| [MCP Apps](https://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/) | ✅ Supported | ➡️ [Docs](https://docs.copilotkit.ai/generative-ui-specs/mcp-apps) 🎮 [Demos]() |


## SDK

| SDK | Status | AG-UI Resources | Integrations |
| --- | ------- | ---------------- | ------------- |
| [Kotlin]() | ✅ Supported | ➡️ [快速入门](https://github.com/ag-ui-protocol/ag-ui/blob/main/docs/sdk/kotlin/overview.mdx) | 社区 |
| [Golang]() | ✅ Supported | ➡️ [快速入门](https://github.com/ag-ui-protocol/ag-ui/blob/main/docs/sdk/go/overview.mdx) | 社区 |
| [Dart]() | ✅ Supported | ➡️ [快速入门](https://github.com/ag-ui-protocol/ag-ui/tree/main/sdks/community/dart) | 社区 |
| [Java]() | ✅ Supported | ➡️ [快速入门](https://github.com/ag-ui-protocol/ag-ui/blob/main/docs/sdk/java/overview.mdx) | 社区 |
| [Rust]() | ✅ Supported | ➡️ [快速入门](https://github.com/ag-ui-protocol/ag-ui/tree/main/sdks/community/rust/crates/ag-ui-client) | 社区 |
| [Ruby]() | ✅ Supported | ➡️ [快速入门](https://github.com/ag-ui-protocol/ag-ui/tree/main/sdks/community/ruby) | 社区 |
| [C++]() | ✅ Supported | ➡️ [源码地址](https://github.com/ag-ui-protocol/ag-ui/tree/main/sdks/community/c%2B%2B) | 社区 |
| [.NET]() | 🛠️ In Progress | ➡️ [PR](https://github.com/ag-ui-protocol/ag-ui/pull/38) | 社区 |
| [Nim]() | 🛠️ In Progress | ➡️ [PR](https://github.com/ag-ui-protocol/ag-ui/pull/29) | 社区 |
| [Flowise]() | 🛠️ In Progress | ➡️ [GitHub Source](https://github.com/ag-ui-protocol/ag-ui/issues/367) | 社区 |
| [Langflow]() | 🛠️ In Progress | ➡️ [GitHub Source](https://github.com/ag-ui-protocol/ag-ui/issues/366) | 社区 |

## 客户端（Clients）

| Client | Status | AG-UI Resources | Integrations |
| --- | ------- | ---------------- | ------------- |
| [CopilotKit](https://github.com/CopilotKit/CopilotKit) | ✅ Supported | ➡️ [快速入门](https://docs.copilotkit.ai/direct-to-llm/guides/quickstart) | 1st Party |
| [Terminal + Agent]() | ✅ Supported | ➡️ [快速入门](https://docs.ag-ui.com/quickstart/clients) | 社区 |
| [React Native]() | 🛠️ Help Wanted | ➡️ [GitHub Source](https://github.com/ag-ui-protocol/ag-ui/issues/510) | 社区 |

[查看所有支持的集成方案 →](https://docs.ag-ui.com/introduction#supported-integrations)

## 示例
### Hello World 应用

演示视频：

https://github.com/user-attachments/assets/18c03330-1ebc-4863-b2b8-cc6c3a4c7bae

https://agui-demo.vercel.app/



## AG-UI Dojo（构建块查看器）
AG-UI Dojo 通过简洁聚焦的示例演示了 AG-UI 的核心构建模块——每个示例仅包含 50 到 200 行代码。

可在[此处](https://github.com/ag-ui-protocol/ag-ui/tree/main/apps/dojo)查看 Dojo 及所有框架集成的源代码。

https://github.com/user-attachments/assets/c298eea8-3f39-4a94-b968-7712429b0c49



## 🙋🏽‍♂️ 参与贡献

请查阅[贡献指南](https://github.com/ag-ui-protocol/ag-ui/blob/main/CONTRIBUTING.md)

- **[AG-UI 双周工作组（Bi-weekly）](https://lu.ma/CopilotKit?k=c)**
  📅 关注 CopilotKit Luma 活动日历

## 路线图

查看[AG-UI 路线图](https://github.com/orgs/ag-ui-protocol/projects/1)，了解当前开发进度并找到你的参与切入点。


## 📄 许可证

AG-UI 是开源软件，[采用 MIT 协议授权](https://opensource.org/licenses/MIT)。