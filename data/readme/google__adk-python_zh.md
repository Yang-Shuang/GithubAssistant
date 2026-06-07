# Agent Development Kit (ADK) 2.0

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

<h2 align="center">
  <img src="https://raw.githubusercontent.com/google/adk-python/main/assets/agent-development-kit.png" width="256"/>
</h2>
<h3 align="center">
  一个开源的、代码优先（code-first）Python 框架，用于构建、评估和部署复杂 AI 智能体，兼具灵活性与可控性。
</h3>
<h3 align="center">
  重要链接：
  <a href="https://google.github.io/adk-docs/">文档</a>、
  <a href="https://github.com/google/adk-samples">示例</a> 及 
  <a href="https://github.com/google/adk-web">ADK Web</a>。
</h3>

______________________________________________________________________

> **⚠️ 来自 1.x 版本的重大变更（Breaking Changes）**
>
> 本次发布包含对智能体 API、事件模型和会话模式（session schema）的重大变更。**ADK 2.0 生成的会话可由 ADK 1.28+ 读取（额外字段将被忽略），但与较旧的 1.x 版本不兼容。**

______________________________________________________________________

## 🔥 2.0 新增功能

- **工作流运行时（Workflow Runtime）**：一种基于图的执行引擎，用于编排具有确定性执行流程的 AI 智能体应用。支持路由、扇出/扇入（fan-out/fan-in）、循环、重试、状态管理、动态节点、人机协同（human-in-the-loop）以及嵌套工作流。

- **任务 API（Task API）**：提供结构化的智能体间委托功能，支持多轮对话模式、单轮受控输出、混合委托模式、人机协同，并允许将任务智能体作为工作流节点使用。

## 🚀 安装

```bash
pip install google-adk
```

**环境要求：** Python 3.11+。

如需安装可选的集成扩展，可使用以下命令：

```bash
pip install "google-adk[extensions]"
```

发布周期约为每两周一次。

## 快速开始

### Agent

```python
from google.adk import Agent

root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.5-flash",
    instruction="You are a helpful assistant. Greet the user warmly.",
)
```

### Workflow

```python
from google.adk import Agent, Workflow

generate_fruit_agent = Agent(
    name="generate_fruit_agent",
    instruction="Return the name of a random fruit. Return only the name.",
)

generate_benefit_agent = Agent(
    name="generate_benefit_agent",
    instruction="Tell me a health benefit about the specified fruit.",
)

root_agent = Workflow(
    name="root_agent",
    edges=[("START", generate_fruit_agent, generate_benefit_agent)],
)
```

### Run Locally

```bash
# Interactive CLI
adk run path/to/my_agent

# Web UI (supports multi-agent directories or pointing directly to a single agent folder)
adk web path/to/agents_dir
```

## 📚 文档

- **入门指南**：https://google.github.io/adk-docs/
- **示例代码**：参见 `contributing/workflow_samples/` 和 `contributing/task_samples/` 目录，其中包含工作流与任务 API 的使用示例。

## 🤝 贡献指南

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 📄 许可证

本项目采用 Apache 2.0 许可证开源——详见 [LICENSE](LICENSE) 文件。