<div align="center">
  <a href="https://docs.langchain.com/oss/python/deepagents/overview#deep-agents-overview">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset=".github/images/logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset=".github/images/logo-light.svg">
      <img alt="Deep Agents Logo" src=".github/images/logo-dark.svg" width="50%">
    </picture>
  </a>
</div>

<div align="center">
  <h3>开箱即用的 Agent（智能体）框架。</h3>
</div>

<div align="center">
  <a href="https://opensource.org/licenses/MIT" target="_blank"><img src="https://img.shields.io/pypi/l/deepagents" alt="PyPI - License"></a>
  <a href="https://pypistats.org/packages/deepagents" target="_blank"><img src="https://img.shields.io/pepy/dt/deepagents" alt="PyPI - Downloads"></a>
  <a href="https://pypi.org/project/deepagents/#history" target="_blank"><img src="https://img.shields.io/pypi/v/deepagents?label=%20" alt="Version"></a>
  <a href="https://x.com/langchain_oss" target="_blank"><img src="https://img.shields.io/twitter/url/https/twitter.com/langchain_oss.svg?style=social&label=Follow%20%40LangChain" alt="Twitter / X"></a>
</div>

<br>

Deep Agents 是一个开源的 Agent（智能体）框架——一个设计倾向明确、开箱即用的 Agent。你可以扩展、覆盖或替换其中的任意模块。

**核心原则：**

- **有明确设计倾向（Opinionated）** —— 默认配置针对长周期、多步骤任务进行了优化
- **可扩展（Extensible）** —— 无需 Fork，即可覆盖或替换任意模块
- **模型无关（Model-agnostic）** —— 兼容任何支持工具调用的 LLM：无论是前沿闭源 API、开源权重模型，还是本地部署模型
- **生产就绪（Production-ready）** —— 基于 LangGraph 构建（支持流式传输、持久化与检查点），并通过 LangSmith 提供一流的追踪、评估与部署功能

**主要特性包括：**

- **子 Agent（Sub-agents）** —— 将任务委派给拥有独立上下文窗口的 Agent
- **文件系统（Filesystem）** —— 支持读写、编辑或搜索可插拔的本地、沙箱化或远程后端存储
- **上下文管理（Context management）** —— 自动总结长对话线程，并将工具输出卸载至磁盘以节省内存
- **终端访问（Shell access）** —— 在你选择的沙箱环境中执行命令
- **持久化记忆（Persistent memory）** —— 支持可插拔的状态与存储后端，实现跨会话的记忆恢复
- **人在回路（Human-in-the-loop）** —— 在工具调用执行前进行审批、编辑或拒绝
- **技能（Skills）** —— Agent 可按需加载的可复用行为模块
- **工具（Tools）** —— 支持接入自定义函数或任意 MCP 服务器

> [!NOTE]
> Deep Agents 也提供 JavaScript/TypeScript 版本库 —— 请参阅 [deepagents.js](https://github.com/langchain-ai/deepagentsjs)。

## 快速开始

```bash
uv add deepagents
```

```python
from deepagents import create_deep_agent

agent = create_deep_agent(
    model="openai:gpt-5.5",
    tools=[my_custom_tool],
    system_prompt="You are a research assistant.",
)
result = agent.invoke({"messages": "Research LangGraph and write a summary"})
```

该 Agent 具备任务规划、文件读写以及自主上下文管理能力。你可以添加自定义工具、更换模型、定制 prompt、配置子 Agent，并进行更多操作。完整详情请参阅[官方文档](https://docs.langchain.com/oss/python/deepagents/overview)。

> [!TIP]
> 如需开发、调试和部署 AI Agent 及 LLM 应用，请参阅 [LangSmith](https://docs.langchain.com/langsmith/home)。

> [!NOTE]
> **Deep Agents Code** —— 终端内置的预配置编程 Agent，功能类似 Claude Code 或 Cursor，支持接入任意 LLM。安装命令：`curl -LsSf https://langch.in/dcode | bash`。完整功能集请参阅[官方文档](https://docs.langchain.com/deepagents-code)。

## 常见问题（FAQ）

### 这与 LangGraph 或 LangChain 有什么区别？

LangGraph 是图运行时（graph runtime）。LangChain 的 `create_agent` 是基于它构建的最小化 Agent 框架。Deep Agents 则是基于 `create_agent` 打造的、设计倾向更强的框架——底层构建模块相同，但内置了文件系统、子 Agent、上下文管理和技能等功能。关于三者的关系，请参阅 [LangChain 生态概览](https://docs.langchain.com/oss/python/concepts/products)。

### 是否支持开源权重模型或本地部署模型？

支持。任何支持工具调用的模型均可使用——包括前沿 API（OpenAI、Anthropic、Google）、托管在 Baseten 或 Fireworks 等平台的开源权重模型，以及通过 Ollama、vLLM 或 llama.cpp 自托管的本地模型。你可以直接使用任意 [LangChain 聊天模型](https://docs.langchain.com/oss/python/langchain/models)。

### 能否用于生产环境？

可以！Deep Agents 基于 LangGraph 构建，专为生产环境的 Agent 部署而设计。建议搭配 [LangSmith](https://docs.langchain.com/langsmith/home) 使用，以实现追踪、评估和监控功能。完整指南请参阅[迈向生产环境](https://docs.langchain.com/oss/python/deepagents/going-to-production)。

### 何时应该选择 Deep Agents，而非直接使用 LangChain 或 LangGraph？

这三者属于同一技术栈的不同层级——具体关系请参阅 [LangChain 生态概览](https://docs.langchain.com/oss/python/concepts/products)。如果你希望开箱即用，获得包含任务规划、上下文管理、任务委派等完整功能的框架，请选择 **Deep Agents**。如果你想要更轻量级的框架且不需要内置中间件，请使用 [**LangChain 的 `create_agent`**](https://docs.langchain.com/oss/python/langchain/agents)。如果你的 Agent 循环逻辑不适合标准结构，需要自定义图拓扑，则应直接使用 [**LangGraph**](https://docs.langchain.com/oss/python/langgraph/overview)。

各层级之间可组合使用：任何 LangGraph 的 `CompiledStateGraph` 均可作为子 Agent 传入 Deep Agents，因此自定义编排逻辑可与框架默认配置无缝集成。

---

## 资源链接

- [示例代码](examples/) —— 可运行的 Agent 案例与设计模式
- [官方文档](https://docs.langchain.com/oss/python/deepagents/overview) —— 概念概览与使用指南
- [LangChain 生态概览](https://docs.langchain.com/oss/python/concepts/products) —— Deep Agents、LangChain、LangGraph 与 LangSmith 的协同关系
- [API 参考手册](https://reference.langchain.com/python/deepagents/) —— 所有公开类、函数与类型的完整文档
- [社区讨论区](https://forum.langchain.com/c/oss-product-help-lc-and-lg/deep-agents/18) —— 用于技术问答、交流想法与提供反馈的社区论坛
- [贡献指南](https://docs.langchain.com/oss/python/contributing/overview) —— 如何参与贡献及寻找适合新手的 Issue
- [行为准则](https://github.com/langchain-ai/langchain/?tab=coc-ov-file) —— 社区规范与标准

---

## 致谢

灵感来源于 Claude Code：旨在提炼其通用能力的核心要素，并在此基础上进一步拓展。

## 安全说明

Deep Agents 采用“信任 LLM”的安全模型。Agent 可执行其工具所允许的任何操作。安全边界应在工具/沙箱层面进行强制约束，而非依赖模型自我监管。更多信息请参阅[安全策略](https://github.com/langchain-ai/deepagents?tab=security-ov-file)。