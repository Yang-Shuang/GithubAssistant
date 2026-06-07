<a href="https://www.assistant-ui.com">
  <img src="https://raw.githubusercontent.com/assistant-ui/assistant-ui/main/.github/assets/header.svg" alt="assistant-ui Header" width="100%" />
</a>

<p align="center">
  <a href="https://www.assistant-ui.com">产品</a> ·
  <a href="https://www.assistant-ui.com/docs">文档</a> ·
  <a href="https://www.assistant-ui.com/examples">示例</a> ·
  <a href="https://discord.gg/S9dwgCNEFs">Discord</a> ·
  <a href="https://cal.com/simon-farshid/assistant-ui">联系销售</a>
</p>

[![npm version](https://img.shields.io/npm/v/@assistant-ui/react)](https://www.npmjs.com/package/@assistant-ui/react)
[![npm downloads](https://img.shields.io/npm/dm/@assistant-ui/react)](https://www.npmjs.com/package/@assistant-ui/react)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/assistant-ui/assistant-ui)
[![Weave Badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fapp.workweave.ai%2Fapi%2Frepository%2Fbadge%2Forg_GhSIrtWo37b5B3Mv0At3wQ1Q%2F722184017&cacheSeconds=3600)](https://app.workweave.ai/reports/repository/org_GhSIrtWo37b5B3Mv0At3wQ1Q/722184017)
![GitHub License](https://img.shields.io/github/license/assistant-ui/assistant-ui)
[![GitHub stars](https://img.shields.io/github/stars/assistant-ui/assistant-ui)](https://github.com/assistant-ui/assistant-ui)
![Backed by Y Combinator](https://img.shields.io/badge/Backed_by-Y_Combinator-orange)

## 在你的 React 应用中实现 ChatGPT 般的交互体验 💬🚀

**assistant-ui** 是一个开源的 TypeScript/React 库，可快速构建生产级 AI 聊天体验。

## Installation（安装）

最快的上手方式是使用 CLI（命令行工具），它可为你生成一个 Next.js 应用，或将样式组件添加到现有项目中：

```bash
npx assistant-ui@latest create   # new project
npx assistant-ui@latest init     # add to existing project
```

或直接安装相关包：

```bash
npm install @assistant-ui/react @assistant-ui/react-ai-sdk
```

## Usage（使用）

```tsx
"use client";

import { AssistantRuntimeProvider } from "@assistant-ui/react";
import { useChatRuntime } from "@assistant-ui/react-ai-sdk";
import { Thread } from "@/components/assistant-ui/thread";

export function Chat() {
  const runtime = useChatRuntime();
  return (
    <AssistantRuntimeProvider runtime={runtime}>
      <Thread />
    </AssistantRuntimeProvider>
  );
}
```

`useChatRuntime` 默认即可连接 Vercel AI SDK。你可以将其替换为 `useLangGraphRuntime`、`useDataStreamRuntime` 或任何自定义运行时，以接入你自己的后端服务。

[![assistant-ui starter template](https://raw.githubusercontent.com/assistant-ui/assistant-ui/main/.github/assets/assistant-ui-starter.gif)](https://youtu.be/k6Dc8URmLjk)

## What you get（核心特性）

- **可组合的基础组件**：基于 `Thread`、`Message`、`Composer`、`ThreadList`、`ActionBar` 等基础组件构建任意聊天交互体验。你可以自行精细调整每个像素的样式，或从 CLI 自动复制到项目中的精美 shadcn/ui 主题开始。
- **开箱即用的生产级交互**：支持流式输出、自动滚动、重试机制、附件上传、Markdown 渲染、代码高亮、语音输入、键盘快捷键以及无障碍访问（Accessibility）。
- **生成式 UI**：将工具调用和 JSON 数据渲染为 React 组件，收集内联人工审批结果，并向模型暴露安全的前端操作。
- **完善的 TypeScript 支持**：从运行时 API、工具模式（schema）、消息结构到适配器，全程提供完整的类型定义。

## Backends（后端集成）

| Integration                            | Package                                                          |
| -------------------------------------- | ---------------------------------------------------------------- |
| Vercel AI SDK                          | `@assistant-ui/react-ai-sdk`                                     |
| LangGraph / LangChain                  | `@assistant-ui/react-langgraph`, `@assistant-ui/react-langchain` |
| AG-UI / A2A protocols                  | `@assistant-ui/react-ag-ui`, `@assistant-ui/react-a2a`           |
| Google ADK / OpenCode                  | `@assistant-ui/react-google-adk`, `@assistant-ui/react-opencode` |
| Custom data-stream backend             | `@assistant-ui/react-data-stream`                                |
| Managed thread history, telemetry, and file storage | `assistant-cloud`                                       |

默认广泛支持各类大模型（OpenAI、Anthropic、Google Gemini、Mistral、Perplexity、AWS Bedrock、Azure、Fireworks、Ollama），并通过 AI SDK 兼容社区提供的其他服务。同时可轻松扩展至任意自定义 HTTP 后端。

## Customization（定制）

采用 Radix 风格：摒弃单一臃肿的聊天组件，你可以通过组合基础组件并引入自定义样式来打造界面。CLI 提供了一个出色的起步模板；其余部分由你完全掌控。

![Overview of components](https://raw.githubusercontent.com/assistant-ui/assistant-ui/main/.github/assets/components.png)

示例：定制一个类 Perplexity 风格的界面：

![Perplexity clone created with assistant-ui](https://raw.githubusercontent.com/assistant-ui/assistant-ui/main/.github/assets/perplexity.gif)

## Used in production by（生产环境应用）

<a href="https://mastra.ai/?ref=assistant-ui" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/assistant-ui/assistant-ui/main/.github/assets/logos/Mastra.svg" height="20" alt="Mastra"></a>, <a href="https://langchain.com/?ref=assistant-ui" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/assistant-ui/assistant-ui/main/.github/assets/logos/LangChain.svg" height="20" alt="LangChain"></a>, <a href="https://athenaintelligence.ai/?ref=assistant-ui" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/assistant-ui/assistant-ui/main/.github/assets/logos/Athena-Intelligence.svg" height="20" alt="Athena Intelligence"></a>, <a href="https://browser-use.com/?ref=assistant-ui" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/assistant-ui/assistant-ui/main/.github/assets/logos/Browser-Use.svg" height="20" alt="Browser Use"></a>, <a href="https://stack-ai.com/?ref=assistant-ui" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/assistant-ui/assistant-ui/main/.github/assets/logos/Stack.svg" height="20" alt="Stack"></a>, <a href="https://inconvo.com/?ref=assistant-ui" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/assistant-ui/assistant-ui/main/.github/assets/logos/Inconvo.svg" height="20" alt="Inconvo"></a>, <a href="https://iterable.com/?ref=assistant-ui" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/assistant-ui/assistant-ui/main/.github/assets/logos/Iterable.svg" height="20" alt="Iterable"></a>, <a href="https://helicone.ai/?ref=assistant-ui" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/assistant-ui/assistant-ui/main/.github/assets/logos/helicone.svg" height="20" alt="Helicone"></a>, <a href="https://getgram.ai/?ref=assistant-ui" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/assistant-ui/assistant-ui/main/.github/assets/logos/gram.svg" height="20" alt="Gram"></a>, <a href="https://coreviz.io/?ref=assistant-ui" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/assistant-ui/assistant-ui/main/.github/assets/logos/Coreviz.svg" height="20" alt="Coreviz"></a>, and many more.

![Chart of assistant-ui's traction](https://raw.githubusercontent.com/assistant-ui/assistant-ui/main/.github/assets/traction.png)

## Demos（演示）

<table>
  <tr>
    <td align="center">
      <a href="https://youtu.be/ZW56UHlqTCQ">
        <img src="https://img.youtube.com/vi/ZW56UHlqTCQ/hqdefault.jpg" alt="Short Demo" />
      </a>
    </td>
    <td align="center">
      <a href="https://youtu.be/9eLKs9AM4tU">
        <img src="https://img.youtube.com/vi/9eLKs9AM4tU/hqdefault.jpg" alt="Long Demo" />
      </a>
    </td>
  </tr>
</table>

## Community & Support（社区与支持）

- [Examples](https://www.assistant-ui.com/examples)
- [Documentation](https://www.assistant-ui.com/docs/)
- [Discord](https://discord.com/invite/S9dwgCNEFs)
- [Book a sales call](https://cal.com/simon-farshid/assistant-ui)

## For other platforms（其他平台支持）

- React Native：[`@assistant-ui/react-native`](https://www.npmjs.com/package/@assistant-ui/react-native)
- 终端（Ink）：[`@assistant-ui/react-ink`](https://www.npmjs.com/package/@assistant-ui/react-ink)

## License（开源协议）

MIT，可选搭配 Assistant Cloud 用于托管对话历史持久化与数据分析服务。

由 Y Combinator 投资孵化。