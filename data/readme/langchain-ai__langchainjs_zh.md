<div align="center">
  <a href="https://www.langchain.com/">
    <picture>
      <source media="(prefers-color-scheme: light)" srcset=".github/images/logo-light.svg">
      <source media="(prefers-color-scheme: dark)" srcset=".github/images/logo-dark.svg">
      <img alt="LangChain Logo" src=".github/images/logo-dark.svg" width="50%">
    </picture>
  </a>
</div>

<div align="center">
  <h3>智能体工程平台。</h3>
</div>

![npm](https://img.shields.io/npm/dm/langchain) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Twitter](https://img.shields.io/twitter/url/https/twitter.com/langchain_js.svg?style=social&label=Follow%20%40LangChain)](https://x.com/langchain_js)

LangChain 是一个用于构建基于大语言模型（LLM）应用的框架。它帮助你串联起可互操作的组件和第三方集成，从而简化 AI 应用开发——随着底层技术的演进，这些设计也能确保你的架构保持面向未来的兼容性。

> [!TIP]
> 初次使用？请查看 **[Deep Agents](http://docs.langchain.com/oss/javascript/deepagents/)** ——这是一个基于 LangChain 构建的高级包，为智能体内置了规划、子智能体、文件系统访问等常见模式的调用能力。

**文档**：想了解更多关于 LangChain 的信息，请查阅[官方文档](https://docs.langchain.com/oss/javascript/langchain/overview)。如果你需要更高级的自定义功能或智能体编排能力，可以查看 [LangGraph.js](https://docs.langchain.com/oss/javascript/langgraph/overview)，这是我们用于构建智能体和可控工作流的框架。如需对应的 Python 库，请查阅 [LangChain](https://github.com/langchain-ai/langchain)。为了帮助你更快地将 LangChain 应用推向生产环境，推荐使用 [LangSmith](https://smith.langchain.com)，这是一个用于构建、测试和监控 LLM 应用的统一开发者平台。

## ⚡️ Quick Install
你可以使用 npm、pnpm 或 yarn 来安装 LangChain.js

`npm install -S langchain` 或 `pnpm install langchain` 或 `yarn add langchain`

## 🚀 Why use LangChain?
LangChain 通过为智能体、模型、嵌入向量（embeddings）、向量数据库等提供标准接口，帮助开发者构建由大语言模型驱动的应用。

使用 LangChain 可实现：

- **实时数据增强**。轻松将 LLM 连接到各类数据源及内外部系统，充分利用 LangChain 庞大的集成库，涵盖模型提供商、工具、向量数据库、检索器等。
- **模型互操作性**。你的工程团队在实验过程中可以灵活替换模型，以找到最适合应用需求的方案。随着行业前沿技术的演进，LangChain 的抽象设计能让你快速适应变化，保持开发节奏不受影响。
- **快速原型开发**。借助 LangChain 模块化、基于组件的架构，快速构建并迭代 LLM 应用。无需从头重写即可测试不同的方法和流程，从而加速开发周期。
- **生产就绪特性**。通过 LangSmith 等集成内置对监控、评估和调试的支持，部署可靠的应用。借助经过实战检验的模式与最佳实践，自信地进行规模化扩展。
- **活跃的社区与生态系统**。利用丰富的集成、模板和社区贡献组件。通过活跃的开源社区获得持续改进，并随时掌握最新的 AI 动态。
- **灵活的抽象层级**。根据你的需求选择合适的工作层级——从用于快速上手的顶层链（chains）到提供细粒度控制的底层组件。LangChain 会随着应用复杂度的增加而共同成长。

## 📦 LangChain's ecosystem
- [Deep Agents (JS)](https://docs.langchain.com/oss/javascript/deepagents/overview) ——构建能够进行规划、使用子智能体并利用文件系统处理复杂任务的智能体。这是基于 LangChain 构建的高级包。
- [LangSmith](https://www.langchain.com/langsmith) ——用于构建、测试和监控 LLM 应用的统一开发者平台。借助 LangSmith，你可以调试表现不佳的 LLM 应用运行结果、评估智能体轨迹、获得生产环境的可观测性，并自信地部署智能体。
- [LangSmith Deployment](https://docs.langchain.com/langsmith/deployments) ——使用专为长运行、有状态工作流设计的平台来部署和扩展智能体。
- [LangGraph](https://docs.langchain.com/oss/javascript/langgraph/overview) ——使用我们底层的智能体编排框架 LangGraph，构建能够可靠处理复杂任务的智能体。LangGraph 提供可自定义的架构、长期记忆和人工介入（human-in-the-loop）工作流——已被 LinkedIn、Uber、Klarna 和 GitLab 等公司用于生产环境并备受信赖。
- [Integrations](https://docs.langchain.com/oss/javascript/integrations/providers/overview) ——聊天与嵌入模型、工具包等更多组件。

## 🌐 Supported Environments
LangChain.js 使用 TypeScript 编写，可在以下环境中运行：

- Node.js（ESM 和 CommonJS） - 20.x, 22.x, 24.x
- Cloudflare Workers
- Vercel / Next.js（浏览器、无服务器函数和边缘函数）
- Supabase Edge Functions
- 浏览器环境
- Deno
- Bun

## 📖 Additional Resources
- [Getting started](https://docs.langchain.com/oss/javascript/langchain/overview)：安装、环境配置及简单示例。
- [Learn](https://docs.langchain.com/oss/javascript/learn)：深入了解 LangChain 的核心概念。
- [LangChain Forum](https://forum.langchain.com)：与社区连接，分享你的技术问题、想法和反馈。
- [Chat LangChain](https://chat.langchain.com)：提问并与我们的文档进行对话交互。

## 💁 Contributing
作为一个处于快速发展领域的开源项目，我们非常欢迎任何形式的贡献，无论是新功能、基础设施改进还是文档优化。

有关如何参与贡献的详细信息，请参阅 [`CONTRIBUTING.md`](https://github.com/langchain-ai/langchainjs/blob/main/CONTRIBUTING.md)。

请按照我们的[安全规范](https://github.com/langchain-ai/.github/blob/main/SECURITY.md)报告任何安全问题或疑虑。