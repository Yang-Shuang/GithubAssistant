<div align="center">
  <img src="assets/octo-white-background-rounded.png" width="150">
  <h1>Tambo AI</h1>
  <h3>构建能与你的 UI 无缝交互的 Agent</h3>
  <p>面向 React 的开源生成式 UI（generative UI）工具包。连接你的组件——Tambo 负责处理流式传输、状态管理和 MCP。</p>
</div>

<p align="center">
  <a href="https://www.npmjs.com/package/@tambo-ai/react"><img src="https://img.shields.io/npm/v/%40tambo-ai%2Freact?logo=npm" alt="npm version" /></a>
  <a href="https://github.com/tambo-ai/tambo/blob/main/LICENSE"><img src="https://img.shields.io/github/license/tambo-ai/tambo" alt="License" /></a>
  <a href="https://github.com/tambo-ai/tambo/commits/main"><img src="https://img.shields.io/github/last-commit/tambo-ai/tambo" alt="Last Commit" /></a>
  <a href="https://discord.gg/dJNvPEHth6"><img src="https://img.shields.io/discord/1251581895414911016?color=7289da&label=discord" alt="Discord"></a>
  <a href="https://github.com/tambo-ai/tambo"><img src="https://img.shields.io/github/stars/tambo-ai/tambo" alt="GitHub stars" /></a>
</p>

<p align="center">
  <a href="https://trendshift.io/repositories/15734" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/repositories/15734" alt="tambo-ai/tambo | Trendshift" width="250" height="55" /></a>
</p>

<p align="center">
  <a href="https://tambo.link/yXkF0hQ">免费开始使用</a> •
  <a href="https://docs.tambo.co">文档</a> •
  <a href="https://discord.gg/dJNvPEHth6">Discord</a>
</p>

---

> **Tambo 1.0 已正式发布！** 阅读公告：[介绍 Tambo：面向 React 的生成式 UI](https://tambo.co/blog/posts/introducing-tambo-generative-ui)

---

## 目录

- [什么是 Tambo？](#what-is-tambo)
- [快速开始](#get-started)
- [工作原理](#how-it-works)
- [功能特性](#features)
- [Tambo 与其他方案对比](#how-tambo-compares)
- [社区](#community)
- [许可证](#license)

## 什么是 Tambo？

Tambo 是一个用于构建渲染 UI 的 Agent（也称为生成式 UI）的 React 工具包。

使用 Zod schema（数据校验模式）注册你的组件。Agent 会自动选择最合适的组件，并流式传输 `props`（属性），以便用户与之交互。“按地区显示销售额”会渲染你的 `<Chart>`，“添加任务”会更新你的 `<TaskBoard>`。

**[5 分钟快速入门 →](#get-started)**

https://github.com/user-attachments/assets/8381d607-b878-4823-8b24-ecb8053bef23

### 核心组成

Tambo 是面向应用添加生成式 UI 的全栈解决方案。你将获得一个 React SDK，以及一个负责处理对话状态和 Agent 执行的后端服务。

**1. 内置 Agent** —— Tambo 为你运行大语言模型（LLM）对话循环。只需提供你自己的 API Key（支持 OpenAI、Anthropic、Gemini、Mistral 或任何兼容 OpenAI 的提供商）。它可与 LangChain 和 Mastra 等 Agent 框架配合使用，但并非必需。

**2. 流式传输基础设施** —— 随着 LLM 生成内容，`props` 会实时流式传输到你的组件中。取消操作、错误恢复和重连均由 Tambo 自动处理。

**3. Tambo Cloud 或自建部署** —— Cloud 是托管的后端服务，负责管理对话状态和 Agent 编排。Self-hosted（自建）则通过 Docker 在你的基础设施上运行相同的后端。

大多数软件都围绕“一刀切”的交互模型构建。我们开发 Tambo，是为了帮助开发者打造能够适应用户的软件。

## 快速开始

```bash
npm create tambo-app my-tambo-app  # 自动初始化 git + tambo 配置
cd my-tambo-app
npm run dev
```

[**Tambo Cloud**](https://tambo.link/yXkF0hQ) 是托管后端服务，免费开始使用并拥有充足的额度供你构建。**自建部署（Self-hosted）** 则运行在你自己的基础设施上。

查看[预构建的组件库](https://ui.tambo.co)，获取 Agent 和生成式 UI 的基础组件：

https://github.com/user-attachments/assets/6cbc103b-9cc7-40f5-9746-12e04c976dff

或者 Fork（复刻）一个模板：

| 模板                                                                 | 描述                                       |
| ------------------------------------------------------------------------ | ------------------------------------------------- |
| [AI Chat with Generative UI](https://github.com/tambo-ai/tambo-template) | 带有动态组件生成的 AI 对话界面  |
| [AI Analytics Dashboard](https://github.com/tambo-ai/analytics-template) | 具备 AI 驱动可视化的数据分析面板 |

## 工作原理

告诉 AI 它可以调用哪些组件。Zod schema 定义了 `props`。这些 schema 会转化为 LLM 的工具定义——Agent 像调用函数一样使用它们，Tambo 负责渲染结果。

### 生成式组件（Generative Components）

响应消息一次性渲染。适用于图表、摘要和数据可视化等场景。

https://github.com/user-attachments/assets/3bd340e7-e226-4151-ae40-aab9b3660d8b

```tsx
const components: TamboComponent[] = [
  {
    name: "Graph",
    description: "Displays data as charts using Recharts library",
    component: Graph,
    propsSchema: z.object({
      data: z.array(z.object({ name: z.string(), value: z.number() })),
      type: z.enum(["line", "bar", "pie"]),
    }),
  },
];
```

### 可交互组件（Interactable Components）

随着用户细化请求而持久化并更新。适用于购物车、电子表格和任务看板等场景。

https://github.com/user-attachments/assets/12d957cd-97f1-488e-911f-0ff900ef4062

```tsx
const InteractableNote = withInteractable(Note, {
  componentName: "Note",
  description: "A note supporting title, content, and color modifications",
  propsSchema: z.object({
    title: z.string(),
    content: z.string(),
    color: z.enum(["white", "yellow", "blue", "green"]).optional(),
  }),
});
```

文档：[生成式组件](https://docs.tambo.co/concepts/generative-interfaces/generative-components)、[可交互组件](https://docs.tambo.co/concepts/generative-interfaces/interactable-components)

### Provider（上下文提供者）

使用 `TamboProvider` 包裹你的应用。你必须提供 `userKey` 或 `userToken` 来标识会话（Thread）的所有者。

```tsx
<TamboProvider
  apiKey={process.env.NEXT_PUBLIC_TAMBO_API_KEY!}
  userKey={currentUserId}
  components={components}
>
  <Chat />
  <InteractableNote id="note-1" title="My Note" content="Start writing..." />
</TamboProvider>
```

在服务器端或可信环境中使用 `userKey`。在客户端应用中使用 `userToken`（OAuth access token），其中包含用户身份信息。详情请参阅[用户认证](https://docs.tambo.co/concepts/user-authentication)。

文档：[Provider 选项](https://docs.tambo.co/reference/react-sdk/providers)

### Hooks

`useTambo()` 是核心 Hook——它提供消息列表、流式传输状态和会话管理。`useTamboThreadInput()` 负责处理用户输入和消息提交。

```tsx
const { messages, isStreaming } = useTambo();
const { value, setValue, submit, isPending } = useTamboThreadInput();
```

文档：[会话与消息](https://docs.tambo.co/concepts/conversation-storage)、[流式传输状态](https://docs.tambo.co/concepts/generative-interfaces/component-state)、[完整教程](https://docs.tambo.co/getting-started/quickstart)

## 功能特性

### MCP（模型上下文协议）集成

连接 Linear、Slack、数据库或你自己的 MCP 服务器。Tambo 支持完整的 MCP 协议：工具调用（tools）、提示词（prompts）、信息获取（elicitations）和采样（sampling）。

```tsx
import { MCPTransport } from "@tambo-ai/react/mcp";

const mcpServers = [
  {
    name: "filesystem",
    url: "http://localhost:8261/mcp",
    transport: MCPTransport.HTTP,
  },
];

<TamboProvider
  apiKey={process.env.NEXT_PUBLIC_TAMBO_API_KEY!}
  userKey={currentUserId}
  components={components}
  mcpServers={mcpServers}
>
  <App />
</TamboProvider>;
```

https://github.com/user-attachments/assets/c7a13915-8fed-4758-be1b-30a60fad0cda

文档：[MCP 集成](https://docs.tambo.co/concepts/model-context-protocol)

### 本地工具（Local Tools）

有时你需要在浏览器中运行的函数。例如 DOM 操作、带认证的请求（authenticated fetches）、访问 React 状态等。将它们定义为工具，AI 即可调用它们。

```tsx
const tools: TamboTool[] = [
  {
    name: "getWeather",
    description: "Fetches weather for a location",
    tool: async (params: { location: string }) =>
      fetch(`/api/weather?q=${encodeURIComponent(params.location)}`).then((r) =>
        r.json(),
      ),
    inputSchema: z.object({
      location: z.string(),
    }),
    outputSchema: z.object({
      temperature: z.number(),
      condition: z.string(),
      location: z.string(),
    }),
  },
];

<TamboProvider
  apiKey={process.env.NEXT_PUBLIC_TAMBO_API_KEY!}
  userKey={currentUserId}
  tools={tools}
  components={components}
>
  <App />
</TamboProvider>;
```

文档：[本地工具](https://docs.tambo.co/guides/take-actions/register-tools)

### 上下文、认证与建议（Context, Auth, and Suggestions）

**附加上下文（Additional context）** 允许你传递元数据，为 AI 提供更优的响应。例如用户状态、应用设置或当前页面。**用户认证（User authentication）** 会从你的认证提供商处获取令牌并传递给 AI。**建议（Suggestions）** 会根据用户的操作生成可点击的提示词。

```tsx
<TamboProvider
  apiKey={process.env.NEXT_PUBLIC_TAMBO_API_KEY!}
  userToken={userToken}
  contextHelpers={{
    selectedItems: () => ({
      key: "selectedItems",
      value: selectedItems.map((i) => i.name).join(", "),
    }),
    currentPage: () => ({ key: "page", value: window.location.pathname }),
  }}
/>
```

```tsx
const { suggestions, accept } = useTamboSuggestions({ maxSuggestions: 3 });

suggestions.map((s) => (
  <button key={s.id} onClick={() => accept(s)}>
    {s.title}
  </button>
));
```

文档：[附加上下文](https://docs.tambo.co/concepts/additional-context)、[用户认证](https://docs.tambo.co/concepts/user-authentication)、[建议](https://docs.tambo.co/concepts/suggestions)

### 支持的 LLM 提供商（Supported LLM Providers）

支持 OpenAI、Anthropic、Cerebras、Google Gemini、Mistral，以及任何兼容 OpenAI 的提供商。[完整列表](https://docs.tambo.co/reference/llm-providers)。缺少某个？[请告诉我们](https://github.com/tambo-ai/tambo/issues)。

## Tambo 与其他方案对比

| 功能特性                             | Tambo                                 | Vercel AI SDK                    | CopilotKit                       | Assistant UI         |
| ---------------------------------- | ------------------------------------- | -------------------------------- | -------------------------------- | -------------------- |
| **组件选择**            | Agent 自动决定渲染哪些组件 | 手动将工具映射到组件 | 通过 Agent 框架（LangGraph） | 聚焦聊天的工具型 UI |
| **MCP 集成**                | 内置支持                              | 实验性（v4.2+）             | 近期新增                   | 需依赖 AI SDK v5   |
| **持久化状态组件**         | 支持                                   | 不支持                               | 共享状态模式            | 不支持                   |
| **客户端工具执行**     | 声明式，自动                | 通过 `onToolCall` 手动调用            | 仅限 Agent 端                  | 不支持   |
| **可自建部署**                  | MIT（SDK + 后端）                   | Apache 2.0（仅 SDK）            | MIT                              | MIT                  |
| **托管选项**                  | Tambo Cloud                           | 无                               | CopilotKit Cloud                 | Assistant Cloud      |
| **最佳适用场景**                       | 完整应用 UI 控制                   | 流式传输与工具抽象  | 多 Agent 工作流            | 聊天界面交互      |

## 社区

加入 [Discord](https://discord.gg/dJNvPEHth6)，与其他开发者和核心团队交流。

有兴趣参与贡献？请阅读[贡献指南](./CONTRIBUTING.md)。

在 Twitter（现 X）上加入讨论，并关注 [@tambo_ai](https://twitter.com/tambo_ai)。

## 许可证

除非另有说明，否则采用 [MIT](LICENSE) 许可证。部分工作区（如 `apps/api`）采用 [Apache-2.0](apps/api/LICENSE) 许可证。

---

<p align="center">
  <img src="assets/tambo-animation.gif" alt="Tambo AI Animation" width="800">
</p>

**面向 AI/LLM Agent：** [docs.tambo.co/llms.txt](https://docs.tambo.co/llms.txt)