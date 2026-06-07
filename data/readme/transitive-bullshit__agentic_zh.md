> [!IMPORTANT]
> 截至 2026 年 2 月，由于该项目已不再积极开发，我将归档此项目。Agentic 曾有过一段不错的历程，并探索了一些当时真正有趣的想法，例如 HTTP <> MCP 兼容层、AI 函数的 TypeScript 标准库，以及与所有主流 LLM 库和 AI SDK 的交叉兼容性。但归根结底，该项目未能取得预期进展（gain traction），因此我已将精力转向其他项目。

<p align="center">
  <a href="https://agentic.so">
    <img alt="Agentic" src="https://raw.githubusercontent.com/transitive-bullshit/agentic/main/apps/web/public/agentic-social-image-light.jpg" width="640">
  </a>
</p>

<p>
  <a href="https://github.com/transitive-bullshit/agentic/actions/workflows/main.yml"><img alt="Build Status" src="https://github.com/transitive-bullshit/agentic/actions/workflows/main.yml/badge.svg" /></a>
  <a href="https://prettier.io"><img alt="Prettier Code Formatting" src="https://img.shields.io/badge/code_style-prettier-brightgreen.svg" /></a>
</p>

# Agentic <!-- omit from toc -->

你可以将 Agentic 视为 **LLM 工具的 RapidAPI**。

Agentic 市场上的所有工具均经过精心筛选，并定期通过全面的集成测试与评估（evals）进行验证。**Agentic 追求的是质量而非数量**。

另一方面，Agentic 让你可以轻松地将**自己的 MCP 服务器与 OpenAPI 服务**发布到 Agentic 的 MCP Gateway，并立即开始为智能体工具调用收费。

- [官网](https://agentic.so)
- [文档](https://docs.agentic.so)

## 核心特性

- **高度精选的工具**：所有公开列出的 Agentic 工具均经过人工审核，以维持极高的质量标准。
- **Agentic UX（智能体用户体验）**：所有 Agentic 工具均为 LLM 工具调用场景专门手工打造。我们称之为 Agentic UX，这也是为什么 Agentic 工具在 LLM 与 MCP 用例中比传统 API 表现更好的核心原因。
- **一等公民的 MCP 支持**：在发布端和消费端，Agentic 都将 MCP 视为真正的一等公民（first-class primitive）原生支持——而非事后补充的功能。
- **世界级的 TypeScript DX（开发者体验）**：Agentic 使用 TS 编写，并致力于提供类似 Vercel 的 DX，包括与所有主流 TS LLM SDK 的一行代码集成。
- **Stripe 计费**：Agentic 采用 Stripe 进行计费，且大多数工具为 _按量付费_ 模式，因此你只需为你（及你的智能体）实际使用的部分付费。
- **极速 MCP Gateway**：Agentic 的 MCP Gateway 由 _Cloudflare 全球边缘网络_ 驱动。工具自带可自定义的缓存与限流功能，让你可以放心地确保你的智能体始终获得快速可靠的体验。
- **语义化版本控制（Semver）**：所有 Agentic 工具均采用 semver 进行版本管理，因此你可以自行决定如何处理破坏性更新（breaking changes）。

## 快速开始

- [MCP 市场](https://docs.agentic.so/marketplace) - 使用工具
- [发布 MCP](https://docs.agentic.so/publishing/quickstart) - 发布你自己的工具

### TypeScript LLM SDK 支持

Agentic 全面支持所有主流 TS LLM SDK，包括：

- [Vercel AI SDK](https://docs.agentic.so/marketplace/ts-sdks/ai-sdk)
- [OpenAI](https://docs.agentic.so/marketplace/ts-sdks/openai-chat)
- [LangChain](https://docs.agentic.so/marketplace/ts-sdks/langchain)
- [LlamaIndex](https://docs.agentic.so/marketplace/ts-sdks/llamaindex)
- [Firebase Genkit](https://docs.agentic.so/marketplace/ts-sdks/genkit)
- [Mastra](https://docs.agentic.so/marketplace/ts-sdks/mastra)

## 发布你自己的 MCP 产品

<p align="center">
  <a href="https://agentic.so/publishing">
    <img alt="Agentic" src="https://raw.githubusercontent.com/transitive-bullshit/agentic/main/apps/web/public/agentic-publishing-social-image-dark-github.jpg" width="640">
  </a>
</p>

- [了解更多关于使用 Agentic 发布信息](https://agentic.so/publishing)
- [使用 Agentic 发布现有 MCP 服务器](https://docs.agentic.so/publishing/guides/existing-mcp-server)
- [使用 Agentic 发布现有 OpenAPI 服务](https://docs.agentic.so/publishing/guides/existing-openapi-service)

任何人都可以通过 Agentic 发布自己的实时 MCP 产品，但在将其上架到主 Agentic 市场之前，你需要向我们提交你的 MCP。

## 加入社区

- 在 [Twitter](https://x.com/transitive_bs) 上关注我们
- 在我们的[文档](https://docs.agentic.so)中阅读更多内容

## 贡献指南

**Agentic 自豪地保持 100% 开源。**

有兴趣参与贡献或从零构建 Agentic？请参阅 [contributing.md](./contributing.md)。