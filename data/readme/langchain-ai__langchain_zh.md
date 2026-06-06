<div align="center">
  <a href="https://docs.langchain.com/oss/python/langchain/overview">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset=".github/images/logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset=".github/images/logo-light.svg">
      <img alt="LangChain Logo" src=".github/images/logo-dark.svg" width="50%">
    </picture>
  </a>
</div>

<div align="center">
  <h3>智能体工程平台。</h3>
</div>

<div align="center">
  <a href="https://opensource.org/licenses/MIT" target="_blank"><img src="https://img.shields.io/pypi/l/langchain" alt="PyPI - License"></a>
  <a href="https://pypistats.org/packages/langchain" target="_blank"><img src="https://img.shields.io/pepy/dt/langchain" alt="PyPI - Downloads"></a>
  <a href="https://pypi.org/project/langchain/#history" target="_blank"><img src="https://img.shields.io/pypi/v/langchain?label=%20" alt="Version"></a>
  <a href="https://x.com/langchain_oss" target="_blank"><img src="https://img.shields.io/twitter/url/https/twitter.com/langchain_oss.svg?style=social&label=Follow%20%40LangChain" alt="Twitter / X"></a>
</div>

<br>

LangChain 是一个用于构建智能体与基于大语言模型（LLM）应用的框架。它将可互操作的组件和第三方集成串联起来，简化 AI 应用开发流程——并在底层技术不断迭代的过程中，让你的架构决策保持前瞻性。

> [!TIP]
> 刚入门？请查看 **[Deep Agents](http://docs.langchain.com/oss/python/deepagents/)** ——这是一个基于 LangChain 构建的高级包，专为智能体设计，内置了规划、子智能体（subagents）、文件系统使用等常见模式的集成能力。

## 快速上手

```bash
pip install langchain
# or
uv add langchain
```

```python
from langchain.chat_models import init_chat_model

model = init_chat_model("openai:gpt-5.4")
result = model.invoke("Hello, world!")
```

如果你需要更高级的自定义功能或智能体编排能力，请查看 [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview)，这是我们用于构建可控智能体工作流的框架。

如需等效的 JS/TS 库，请查看 [LangChain.js](https://github.com/langchain-ai/langchainjs)。

> [!TIP]
> 如需开发、调试和部署 AI 智能体及大语言模型应用，请参阅 [LangSmith](https://docs.langchain.com/langsmith/home)。

## LangChain 生态系统

虽然 LangChain 框架可以独立使用，但它也能与任何 LangChain 产品无缝集成，为开发者在构建大语言模型应用时提供全套工具。

- **[Deep Agents](http://docs.langchain.com/oss/python/deepagents/)** — 构建能够进行规划、调用子智能体并利用文件系统处理复杂任务的智能体
- **[LangGraph](https://docs.langchain.com/oss/python/langgraph/overview)** — 通过我们低级别的智能体编排框架，构建能够可靠处理复杂任务的智能体
- **[Integrations](https://docs.langchain.com/oss/python/integrations/providers/overview)** — 聊天与嵌入模型（embedding models）、工具包等更多集成组件
- **[LangSmith](https://www.langchain.com/langsmith)** — 面向大语言模型应用的智能体评估、可观测性与调试工具
- **[LangSmith Deployment](https://docs.langchain.com/langsmith/deployments)** — 使用专为长运行、有状态工作流设计的平台，部署并扩展智能体

## 为什么选择 LangChain？

LangChain 通过为模型、嵌入（embedding）、向量数据库（vector store）等提供标准接口，帮助开发者构建由大语言模型驱动的应用。

- **实时数据增强** —— 轻松将大语言模型连接到各类数据源及内外部系统，充分利用 LangChain 丰富的集成库（涵盖模型提供商、工具、向量数据库、检索器等）
- **模型互操作性** —— 工程团队在实验寻找最适合应用需求的模型时，可自由切换。随着行业前沿技术的演进快速适应变化——LangChain 的抽象设计让你保持开发节奏，无需推倒重来
- **快速原型开发** —— 借助 LangChain 模块化、基于组件的架构，快速构建和迭代大语言模型应用。无需从零开始重建即可测试不同的方法与工作流，大幅缩短开发周期
- **生产就绪特性** —— 通过 LangSmith 等集成内置对监控、评估和调试的支持，部署可靠的应用。借助经过实战检验的模式与最佳实践，自信地进行规模扩展
- **活跃的社区与生态系统** —— 利用丰富的集成、模板和社区贡献组件生态。通过活跃的开源社区获得持续改进，并紧跟最新的 AI 技术动态
- **灵活的抽象层级** —— 根据你的需求选择抽象级别——从用于快速上手的“链（chain）”到提供细粒度控制的底层组件。LangChain 的复杂度随你的应用共同成长

---

## 文档

- [docs.langchain.com](https://docs.langchain.com/oss/python/langchain/overview) – 全面的技术文档，涵盖概念概览与使用指南
- [reference.langchain.com/python](https://reference.langchain.com/python) – LangChain 软件包的 API 参考文档
- [Chat LangChain](https://chat.langchain.com/) – 与 LangChain 文档对话，获取你的问题答案

**讨论区（Discussions）**：访问 [LangChain 论坛](https://forum.langchain.com)，与社区建立联系，分享你的技术问题、想法和反馈。

## 其他资源

- [Contributing Guide](https://docs.langchain.com/oss/python/contributing/overview) – 了解如何为 LangChain 项目做出贡献，并寻找适合入门的 Issue。
- [Code of Conduct](https://github.com/langchain-ai/langchain/?tab=coc-ov-file) – 我们的社区参与规范与标准。
- [LangChain Academy](https://academy.langchain.com/) – 由 LangChain 团队打造的全面免费课程，涵盖 LangChain 库与产品。