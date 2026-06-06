<p align="center">
  <img
    src="https://img.alicdn.com/imgextra/i1/O1CN01nTg6w21NqT5qFKH1u_!!6000000001621-55-tps-550-550.svg"
    alt="AgentScope Logo"
    width="200"
  />
</p>

<span align="center">

[**中文主页**](https://github.com/agentscope-ai/agentscope/blob/main/README_zh.md) | [**教程**](https://docs.agentscope.io/) | [**路线图**](https://github.com/orgs/agentscope-ai/projects/2/views/1)

</span>

<p align="center">
    <a href="https://arxiv.org/abs/2402.14034">
        <img
            src="https://img.shields.io/badge/cs.MA-2402.14034-B31C1C?logo=arxiv&logoColor=B31C1C"
            alt="arxiv"
        />
    </a>
    <a href="https://pypi.org/project/agentscope/">
        <img
            src="https://img.shields.io/badge/python-3.11+-blue?logo=python"
            alt="pypi"
        />
    </a>
    <a href="https://pypi.org/project/agentscope/">
        <img
            src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpypi.org%2Fpypi%2Fagentscope%2Fjson&query=%24.info.version&prefix=v&logo=pypi&label=version"
            alt="pypi"
        />
    </a>
    <a href="https://discord.gg/eYMpfnkG8h">
        <img
            src="https://img.shields.io/discord/1194846673529213039?label=Discord&logo=discord"
            alt="discord"
        />
    </a>
    <a href="https://docs.agentscope.io/">
        <img
            src="https://img.shields.io/badge/Docs-English%7C%E4%B8%AD%E6%96%87-blue?logo=markdown"
            alt="docs"
        />
    </a>
    <a href="./LICENSE">
        <img
            src="https://img.shields.io/badge/license-Apache--2.0-black"
            alt="license"
        />
    </a>
</p>

<p align="center">
<img src="https://trendshift.io/api/badge/repositories/20310" alt="agentscope-ai%2Fagentscope | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/>
</p>

## 什么是 AgentScope 2.0？

AgentScope 2.0 是一个面向生产环境、易于使用的智能体（Agent）框架，提供了核心抽象设计以适配不断增强的模型能力，并内置微调支持。

我们专为日益具备自主性的 LLM 设计。我们的方法侧重于利用模型的推理和工具调用能力，而非通过严格的提示词或预设的编排逻辑对其进行限制。

## 为什么选择 AgentScope？

- **简单**：内置 ReAct 智能体、工具、技能、人机协同控制（human-in-the-loop）、记忆、规划、实时语音、评估及模型微调功能，5 分钟即可开始构建你的智能体
- **可扩展**：提供大量用于工具、记忆和可观测性的生态集成；内置对 MCP 和 A2A 的支持；消息中心（message hub）支持灵活的多智能体编排与工作流
- **生产就绪**：内置 OpenTelemetry（OTel）支持，可本地部署、云端无服务器运行或部署至 Kubernetes 集群

<img src="assets/images/agentscope.png" alt="agentscope" width="100%"/>

## 最新动态
<!-- BEGIN NEWS -->
- **[2026-05] `RELS`：** AgentScope 2.0 正式发布！[文档](https://docs.agentscope.io/)
<!-- END NEWS -->

[更多动态 →](./docs/NEWS.md)

## 社区

欢迎加入我们的社区：

| [Discord](https://discord.gg/eYMpfnkG8h)                                                                                         | 钉钉                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <img src="https://gw.alicdn.com/imgextra/i1/O1CN01hhD1mu1Dd3BWVUvxN_!!6000000000238-2-tps-400-400.png" width="100" height="100"> | <img src="./assets/images/dingtalk_qr_code.png" width="100" height="100"> |

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## 📑 目录

- [快速开始](#quickstart)
  - [安装](#installation)
    - [从 PyPI 安装](#from-pypi)
    - [从源码安装](#from-source)
- [Hello AgentScope!](#hello-agentscope)
- [智能体服务](#agent-service)
- [贡献指南](#contributing)
- [开源协议](#license)
- [引用论文](#publications)
- [贡献者](#contributors)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## 快速开始

### 安装

> AgentScope 需要 **Python 3.11** 或更高版本。

#### 从 PyPI 安装

```bash
uv pip install agentscope
# or
# pip install agentscope
```

#### 从源码安装

```bash
# Pull the source code from GitHub
git clone -b main https://github.com/agentscope-ai/agentscope.git

# Install the package in editable mode
cd agentscope

uv pip install -e .
# or
# pip install -e .
```

## Hello AgentScope!

使用 AgentScope 2.0，5 分钟启动你的第一个智能体：

```python
from agentscope.agent import Agent
from agentscope.tool import Toolkit, Bash, Grep, Glob, Read, Write, Edit
from agentscope.credential import DashScopeCredential
from agentscope.model import DashScopeChatModel
from agentscope.message import UserMsg
from agentscope.event import EventType

import os, asyncio


async def main() -> None:
    agent = Agent(
        name="Friday",
        system_prompt="You're a helpful assistant named Friday.",
        model=DashScopeChatModel(
            credential=DashScopeCredential(
              api_key=os.environ["DASHSCOPE_API_KEY"]
            ),
            model="qwen3.6-plus",
        ),
        toolkit=Toolkit(
            tools=[
                Bash(),
                Grep(),
                Glob(),
                Read(),
                Write(),
                Edit(),
            ]
        ),
    )

    async for evt in agent.reply_stream(UserMsg("Tony", "Hi, Friday!")):
        # Handle the event stream, e.g., print the message, update UI, etc.
        match evt.type:
            case EventType.REPLY_START:
                ...
            case EventType.MODEL_CALL_START:
                ...
            case EventType.TEXT_BLOCK_START:
                ...
            case EventType.TEXT_BLOCK_DELTA:
                ...
            case EventType.TEXT_BLOCK_END:
                ...

            # Handle other event types

asyncio.run(main())
```

## 智能体服务

一个基于 FastAPI 的、支持扩展的**多租户**与**多会话**智能体服务，内置于 `examples/web_ui` 中的 Web UI。

```bash
git clone https://github.com/agentscope-ai/agentscope

cd agentscope/examples/agent_service

# start the agent service backend
python main.py
```

然后在另一个终端中启动 Web UI：

```bash
cd agentscope/examples/web_ui

# start the webui
pnpm install
pnpm dev
```

体验聊天式界面，与你的智能体进行交互。

<img src="https://gw.alicdn.com/imgextra/i1/O1CN01vGGiBw20agWwpzmjy_!!6000000006866-2-tps-2934-1732.png" alt="Permission System" width="100%">


## 贡献指南

我们欢迎社区贡献！有关如何参与贡献的规范，请参阅我们的 [CONTRIBUTING.md](./CONTRIBUTING.md)。

## 开源协议

AgentScope 采用 Apache License 2.0 协议发布。

## 引用论文

如果您的研究或应用受益于我们的工作，请引用以下论文：

- [AgentScope 1.0: A Developer-Centric Framework for Building Agentic Applications](https://arxiv.org/abs/2508.16279)

- [AgentScope: A Flexible yet Robust Multi-Agent Platform](https://arxiv.org/abs/2402.14034)

```
@article{agentscope_v1,
    author  = {Dawei Gao, Zitao Li, Yuexiang Xie, Weirui Kuang, Liuyi Yao, Bingchen Qian, Zhijian Ma, Yue Cui, Haohao Luo, Shen Li, Lu Yi, Yi Yu, Shiqi He, Zhiling Luo, Wenmeng Zhou, Zhicheng Zhang, Xuguang He, Ziqian Chen, Weikai Liao, Farruh Isakulovich Kushnazarov, Yaliang Li, Bolin Ding, Jingren Zhou}
    title   = {AgentScope 1.0: A Developer-Centric Framework for Building Agentic Applications},
    journal = {CoRR},
    volume  = {abs/2508.16279},
    year    = {2025},
}

@article{agentscope,
    author  = {Dawei Gao, Zitao Li, Xuchen Pan, Weirui Kuang, Zhijian Ma, Bingchen Qian, Fei Wei, Wenhao Zhang, Yuexiang Xie, Daoyuan Chen, Liuyi Yao, Hongyi Peng, Zeyu Zhang, Lin Zhu, Chen Cheng, Hongzhu Shi, Yaliang Li, Bolin Ding, Jingren Zhou}
    title   = {AgentScope: A Flexible yet Robust Multi-Agent Platform},
    journal = {CoRR},
    volume  = {abs/2402.14034},
    year    = {2024},
}
```

## 贡献者

感谢所有贡献者：

<a href="https://github.com/agentscope-ai/agentscope/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=agentscope-ai/agentscope&max=999&columns=12&anon=1" />
</a>