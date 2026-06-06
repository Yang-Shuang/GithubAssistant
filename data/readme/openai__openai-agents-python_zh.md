# OpenAI Agents SDK [![PyPI](https://img.shields.io/pypi/v/openai-agents?label=pypi%20package)](https://pypi.org/project/openai-agents/)

OpenAI Agents SDK 是一个轻量且强大的框架，用于构建多智能体（multi-agent）工作流。它不绑定特定模型提供商，兼容 OpenAI Responses 和 Chat Completions API，并支持 100+ 其他大语言模型（LLM）。

<img src="https://cdn.openai.com/API/docs/images/orchestration.png" alt="Image of the Agents Tracing UI" style="max-height: 803px;">

> [!NOTE]
> 需要 JavaScript/TypeScript 版本？请查看 [Agents SDK JS/TS](https://github.com/openai/openai-agents-js)。

### 核心概念：

1. [**智能体（Agents）**](https://openai.github.io/openai-agents-python/agents)：配置了指令、工具、护栏和交接功能的 LLM
1. [**沙箱智能体（Sandbox Agents）**](https://openai.github.io/openai-agents-python/sandbox_agents)：预配置为与容器配合使用，以在长周期内执行任务的智能体。
1. **[将智能体作为工具使用（Agents as tools）/ [交接功能（Handoffs）]**](https://openai.github.io/openai-agents-python/tools/#agents-as-tools)/[**交接功能（Handoffs）**](https://openai.github.io/openai-agents-python/handoffs/)：将特定任务委派给其他智能体
1. [**工具（Tools）**](https://openai.github.io/openai-agents-python/tools/)：各类工具让智能体能够执行操作（如函数、MCP、托管工具）
1. [**护栏（Guardrails）**](https://openai.github.io/openai-agents-python/guardrails/)：可配置的安全检查，用于输入和输出验证
1. [**人机协同（Human in the loop）**](https://openai.github.io/openai-agents-python/human_in_the_loop/)：内置机制，支持在智能体运行过程中引入人工参与
1. [**会话（Sessions）**](https://openai.github.io/openai-agents-python/sessions/)：跨智能体运行的自动对话历史管理
1. [**追踪（Tracing）**](https://openai.github.io/openai-agents-python/tracing/)：内置的智能体运行跟踪功能，让你能够查看、调试和优化你的工作流
1. [**实时智能体（Realtime Agents）**](https://openai.github.io/openai-agents-python/realtime/quickstart/)：使用 `gpt-realtime-2` 和完整的智能体功能构建强大的语音智能体

浏览 [示例](https://github.com/openai/openai-agents-python/tree/main/examples) 目录以查看 SDK 的实际运行效果，并阅读我们的[文档](https://openai.github.io/openai-agents-python/)获取更多详细信息。

## 快速上手

要开始使用，请设置你的 Python 环境（需要 Python 3.10 或更高版本），然后安装 OpenAI Agents SDK 包。

### venv

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install openai-agents
```

如需语音支持，请安装可选的 `voice` 依赖组：`pip install 'openai-agents[voice]'`。如需 Redis 会话支持，请安装可选的 `redis` 依赖组：`pip install 'openai-agents[redis]'`。

### uv

如果你熟悉 [uv](https://docs.astral.sh/uv/)，安装该包将更加简单：

```bash
uv init
uv add openai-agents
```

如需语音支持，请安装可选的 `voice` 依赖组：`uv add 'openai-agents[voice]'`。如需 Redis 会话支持，请安装可选的 `redis` 依赖组：`uv add 'openai-agents[redis]'`。

## 运行你的第一个沙箱智能体（Sandbox Agent）

[沙箱智能体](https://openai.github.io/openai-agents-python/sandbox_agents) 是 v0.14.0 版本的新特性。沙箱智能体是一种利用计算机环境（包含文件系统）执行实际任务的智能体，该环境由你配置并控制。当智能体需要检查文件、运行命令、应用补丁或在较长任务中保持工作区状态时，沙箱智能体会非常有用。

```python
from agents import Runner
from agents.run import RunConfig
from agents.sandbox import Manifest, SandboxAgent, SandboxRunConfig
from agents.sandbox.entries import GitRepo
from agents.sandbox.sandboxes import UnixLocalSandboxClient

agent = SandboxAgent(
    name="Workspace Assistant",
    instructions="Inspect the sandbox workspace before answering.",
    default_manifest=Manifest(
        entries={
            "repo": GitRepo(repo="openai/openai-agents-python", ref="main"),
        }
    ),
)

result = Runner.run_sync(
    agent,
    "Inspect the repo README and summarize what this project does.",
    # Run this agent on the local filesystem
    run_config=RunConfig(sandbox=SandboxRunConfig(client=UnixLocalSandboxClient())),
)
print(result.final_output)

# This project provides a Python SDK for building multi-agent workflows.
```

（_运行此代码前，请确保已设置 `OPENAI_API_KEY` 环境变量_）

（_Jupyter Notebook 用户请参阅 [hello_world_jupyter.ipynb](https://github.com/openai/openai-agents-python/blob/main/examples/basic/hello_world_jupyter.ipynb)_）

浏览 [示例](https://github.com/openai/openai-agents-python/tree/main/examples) 目录以查看 SDK 的实际运行效果，并阅读我们的[文档](https://openai.github.io/openai-agents-python/)获取更多详细信息。

## 鸣谢

我们非常感谢开源社区的杰出贡献，特别是：

- [Pydantic](https://docs.pydantic.dev/latest/)
- [Requests](https://github.com/psf/requests)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Griffe](https://github.com/mkdocstrings/griffe)

本库包含以下可选依赖项：

- [websockets](https://github.com/python-websockets/websockets)
- [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy)
- [any-llm](https://github.com/mozilla-ai/any-llm) 和 [LiteLLM](https://github.com/BerriAI/litellm)

我们还使用以下工具来管理项目：

- [uv](https://github.com/astral-sh/uv) 和 [ruff](https://github.com/astral-sh/ruff)
- [mypy](https://github.com/python/mypy) 和 [Pyright](https://github.com/microsoft/pyright)
- [pytest](https://github.com/pytest-dev/pytest) 和 [Coverage.py](https://github.com/coveragepy/coveragepy)
- [MkDocs](https://github.com/squidfunk/mkdocs-material)

我们致力于继续将 Agents SDK 构建为一个开源框架，以便社区中的其他人能够在此基础上扩展我们的方法。