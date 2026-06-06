# Mastra

[![npm version](https://badge.fury.io/js/@mastra%2Fcore.svg)](https://www.npmjs.com/package/@mastra/core)
[![CodeQl](https://github.com/mastra-ai/mastra/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/mastra-ai/mastra/actions/workflows/github-code-scanning/codeql)
[![GitHub Repo stars](https://img.shields.io/github/stars/mastra-ai/mastra)](https://github.com/mastra-ai/mastra/stargazers)
[![Discord](https://img.shields.io/discord/1309558646228779139?logo=discord&label=Discord&labelColor=white&color=7289DA)](https://discord.gg/BTYqqHKUrf)
[![Twitter Follow](https://img.shields.io/twitter/follow/mastra?style=social)](https://x.com/mastra)
[![NPM Downloads](https://img.shields.io/npm/dm/%40mastra%252Fcore)](https://www.npmjs.com/package/@mastra/core)
[![Static Badge](https://img.shields.io/badge/Y%20Combinator-W25-orange)](https://www.ycombinator.com/companies?batch=W25)

Mastra 是一个基于现代 TypeScript 技术栈的框架，用于构建 AI 驱动的应用程序和智能体（Agent）。

它涵盖了从早期原型到生产就绪应用所需的一切。Mastra 可与 React、Next.js 和 Node 等前后端框架集成，或者你也可以将其作为独立服务器部署在任何地方。这是构建、调优和扩展可靠 AI 产品最简单的方式。

## 为什么选择 Mastra？

Mastra 专为 TypeScript 打造，并围绕成熟的 AI 设计模式构建，开箱即用，为你提供构建优秀 AI 应用所需的一切。

部分亮点功能包括：

- [**模型路由（Model Routing）**](https://mastra.ai/models) - 通过统一的标准接口连接 40 多个提供商。使用来自 OpenAI、Anthropic、Gemini 等平台的模型。

- [**智能体（Agents）**](https://mastra.ai/docs/agents/overview) - 构建自主运行的智能体，利用大语言模型（LLM）和工具解决开放式任务。智能体会对目标进行推理，决定使用哪些工具，并在内部不断迭代，直到模型输出最终答案或满足可选的停止条件。

- [**工作流（Workflows）**](https://mastra.ai/docs/workflows/overview) - 当你需要明确控制执行流程时，可使用基于图的工作流引擎来编排复杂的多步骤任务。Mastra 工作流采用直观的语法来控制流程（`.then()`、`.branch()`、`.parallel()`）。

- [**人机协同（Human-in-the-loop）**](https://mastra.ai/docs/workflows/suspend-and-resume) - 挂起智能体或工作流，并在恢复前等待用户输入或审批。Mastra 使用[存储模块](https://mastra.ai/docs/server-db/storage)来记录执行状态，因此你可以无限期暂停，并在需要时从中断处继续运行。

- **上下文管理** - 在恰当的时间为你的智能体提供恰当的上下文。提供[对话历史](https://mastra.ai/docs/memory/conversation-history)，从你的数据源（API、数据库、文件）中[检索](https://mastra.ai/docs/rag/overview)数据，并添加类似人类的[工作记忆](https://mastra.ai/docs/memory/working-memory)和[语义记忆](https://mastra.ai/docs/memory/semantic-recall)，使智能体的行为更加连贯一致。

- **集成（Integrations）** - 将智能体和工作流打包到现有的 React、Next.js 或 Node.js 应用中，或以独立端点的形式发布。在构建用户界面时，可集成 Vercel 的 AI SDK UI 和 CopilotKit 等智能体库，让你的 AI 助手在 Web 端生动呈现。

- [**MCP 服务器（MCP Servers）**](https://mastra.ai/docs/tools-mcp/mcp-overview) - 开发模型上下文协议（Model Context Protocol）服务器，通过 MCP 接口暴露智能体、工具和其他结构化资源。随后，任何支持该协议的系统或智能体均可访问这些资源。

- **生产环境必备** - 发布可靠的智能体需要持续的洞察、评估与迭代。借助内置的[评测（Evals）](https://mastra.ai/docs/evals/overview)和[可观测性（Observability）](https://mastra.ai/docs/observability/overview)功能，Mastra 为你提供持续监控、衡量和优化所需的工具。

## 快速开始

使用 Mastra 的**推荐**方式是运行以下命令：

```shell
npm create mastra@latest
```

请查阅[安装指南](https://mastra.ai/docs/getting-started/installation)，了解如何通过 CLI 或手动方式进行逐步设置。

如果你是 AI 智能体开发的新手，可以查看我们的[模板](https://mastra.ai/docs/getting-started/templates)、[课程](https://mastra.ai/course)和 [YouTube 视频教程](https://youtube.com/@mastra-ai)，今天就开始使用 Mastra 进行构建。

## 文档

请访问我们的[官方文档](https://mastra.ai/docs)。

## 使用 AI 进行开发

跟随[AI 辅助构建指南](https://mastra.ai/docs/getting-started/build-with-ai)，学习如何让你的智能体成为 Mastra 专家。

## 贡献指南

想要参与贡献？我们欢迎任何形式的帮助，包括代码编写、测试以及功能规范制定。阅读 [CONTRIBUTING.md](./CONTRIBUTING.md) 了解更多参与方式。

如果你是开发者并希望贡献代码，请在提交 Pull Request（PR）之前先创建 Issue 进行讨论。

有关项目环境搭建的信息，请参阅[开发文档](./DEVELOPMENT.md)。

## 支持

我们拥有一个[开放的社区 Discord](https://discord.gg/BTYqqHKUrf)。欢迎前来打招呼，并告诉我们你是否有任何问题或需要运行方面的帮助。

如果你能在[页面顶部](https://github.com/mastra-ai/mastra)给项目点个 Star，也将是对我们莫大的支持。

## 许可证

本仓库采用双许可证模式：

- **Apache License 2.0** —— 核心框架及该代码库的绝大部分内容均在 Apache-2.0 许可下开源。
- **Mastra 企业许可证** —— 任何名为 `ee/` 的目录下的代码（例如 `packages/core/src/auth/ee/`）均在 Mastra 企业许可下提供源代码。这些功能在生产环境中使用需要有效的企业许可证，但可自由用于开发和测试。

完整许可证映射请参阅 [LICENSE.md](./LICENSE.md)，企业许可条款请参阅 [ee/LICENSE](./ee/LICENSE)。

## 安全

我们致力于维护本仓库及 Mastra 整体的安全性。如果你发现任何安全问题，请通过 [security@mastra.ai](mailto:security@mastra.ai) 向我们负责任地披露，我们将尽快回复你。