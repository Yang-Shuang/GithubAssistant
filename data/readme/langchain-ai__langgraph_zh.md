<div align="center">
  <a href="https://www.langchain.com/langgraph">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset=".github/images/logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset=".github/images/logo-light.svg">
      <img alt="LangGraph Logo" src=".github/images/logo-dark.svg" width="50%">
    </picture>
  </a>
</div>

<div align="center">
  <h3>用于构建有状态智能体的底层编排框架。</h3>
</div>

<div align="center">
  <a href="https://opensource.org/licenses/MIT" target="_blank"><img src="https://img.shields.io/pypi/l/langgraph" alt="PyPI - License"></a>
  <a href="https://pypistats.org/packages/langgraph" target="_blank"><img src="https://img.shields.io/pepy/dt/langgraph" alt="PyPI - Downloads"></a>
  <a href="https://pypi.org/project/langgraph/" target="_blank"><img src="https://img.shields.io/pypi/v/langgraph.svg?label=%20" alt="Version"></a>
  <a href="https://x.com/langchain_oss" target="_blank"><img src="https://img.shields.io/twitter/url/https/twitter.com/langchain_oss.svg?style=social&label=Follow%20%40LangChain" alt="Twitter / X"></a>
</div>

<br>

受到众多致力于塑造智能体未来的公司的信赖——包括 Klarna、Replit、Elastic 等，LangGraph 是一个用于构建、管理和部署长期运行且有状态智能体的底层编排框架。

```bash
pip install -U langgraph
```

> [!TIP]
> 如果你想快速构建智能体，请查看 **[Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview)** ——这是一个基于 LangGraph 的更高层级包，专为能够进行规划、使用子代理并利用文件系统处理复杂任务的智能体设计。

如需使用等效的 JS/TS 库，请查阅 [LangGraph.js](https://github.com/langchain-ai/langgraphjs) 及对应的 [JS 文档](https://docs.langchain.com/oss/javascript/langgraph/overview)。

## 为什么选择 LangGraph？

LangGraph 为*任何*长期运行的有状态工作流或智能体提供底层支持基础设施：

- **[持久化执行 (Durable execution)](https://docs.langchain.com/oss/python/langgraph/durable-execution)** —— 构建能够抵御故障并在长时间内持续运行的智能体，它会自动从断点处精确恢复运行。
- **[人机协同监督 (Human-in-the-loop)](https://docs.langchain.com/oss/python/langgraph/interrupts)** —— 通过在执行过程中的任意节点检查并修改智能体状态，无缝融入人类监督机制。
- **[全面记忆管理 (Comprehensive memory)](https://docs.langchain.com/oss/python/langgraph/memory)** —— 创建真正具备有状态能力的智能体，同时拥有用于持续推理的短期工作记忆和跨会话的长期持久记忆。
- **[使用 LangSmith 进行调试](https://www.langchain.com/langsmith)** —— 借助可视化追踪执行路径、捕获状态转换并提供详细运行时指标的工具，深入洞察复杂智能体行为。
- **[生产级部署 (Production-ready deployment)](https://docs.langchain.com/langsmith/deployments)** —— 使用专为应对有状态、长期运行工作流独特挑战而设计的可扩展基础设施，自信地部署复杂的智能体系统。

> [!TIP]
> 如需开发、调试和部署 AI 智能体及大语言模型（LLM）应用，请参阅 [LangSmith](https://docs.langchain.com/langsmith/home)。

## LangGraph 生态系统

虽然 LangGraph 可以独立使用，但它也能与任何 LangChain 产品无缝集成，为开发者提供一套完整的智能体构建工具。

为了提升你的大语言模型（LLM）应用开发效率，建议将 LangGraph 与以下组件配合使用：

- [Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview) —— 构建能够进行规划、调用子代理并利用文件系统处理复杂任务的智能体。
- [LangChain](https://docs.langchain.com/oss/python/langchain/overview) —— 提供集成与可组合组件，简化大语言模型应用开发流程。
- [LangSmith](https://www.langchain.com/langsmith) —— 助力智能体评估与可观测性。调试表现不佳的 LLM 应用运行，评估智能体轨迹，提升生产环境可见度，并持续优化性能。
- [LangSmith 部署平台](https://docs.langchain.com/langsmith/deployments) —— 借助专为长期运行、有状态工作流打造的部署平台，轻松部署和扩展智能体。跨团队发现、复用、配置和共享智能体——并通过 [LangSmith Studio](https://docs.langchain.com/langsmith/studio) 中的可视化原型设计快速迭代。

---

## 文档资源

- [docs.langchain.com](https://docs.langchain.com/oss/python/langgraph/overview) —— 全面的技术文档，包含概念概述与使用指南
- [reference.langchain.com/python/langgraph](https://reference.langchain.com/python/langgraph) —— LangGraph 包的 API 参考文档
- [LangGraph 快速入门](https://docs.langchain.com/oss/python/langgraph/quickstart) —— 开始使用 LangGraph 进行开发
- [Chat LangChain](https://chat.langchain.com/) —— 与 LangChain 文档对话，获取你的问题答案

**讨论区**：访问 [LangChain 论坛](https://forum.langchain.com) 与社区连接，分享你的技术问题、想法和反馈。

## 其他资源

- **[指南](https://docs.langchain.com/oss/python/learn)** —— 提供针对流式传输、添加记忆与持久化以及设计模式（如分支、子图等）的快速可操作代码示例。
- **[LangChain 学院](https://academy.langchain.com/courses/intro-to-langgraph)** —— 通过我们免费的结构化课程学习 LangGraph 基础知识。
- **[案例研究](https://www.langchain.com/built-with-langgraph)** —— 了解行业领导者如何利用 LangGraph 规模化交付 AI 应用。
- [贡献指南](https://docs.langchain.com/oss/python/contributing/overview) —— 了解如何为 LangChain 项目做出贡献，并寻找适合初学者的 Issue。
- [行为准则](https://github.com/langchain-ai/langchain/?tab=coc-ov-file) —— 我们的社区规范与参与标准。

---

## 致谢

LangGraph 的设计灵感来源于 [Pregel](https://research.google/pubs/pub37252/) 和 [Apache Beam](https://beam.apache.org/)。其公共接口的设计借鉴了 [NetworkX](https://networkx.org/documentation/latest/)。LangGraph 由 LangChain 的创造者 LangChain Inc. 开发，但无需依赖 LangChain 即可独立使用。