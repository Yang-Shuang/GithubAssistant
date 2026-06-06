<a name="readme-top"></a>

<div align="center">
<img src="https://microsoft.github.io/autogen/0.2/img/ag.svg" alt="AutoGen Logo" width="100">

[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/cloudposse.svg?style=social&label=Follow%20%40pyautogen)](https://twitter.com/pyautogen)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Company?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/105812540)
[![Discord](https://img.shields.io/badge/discord-chat-green?logo=discord)](https://aka.ms/autogen-discord)
[![Documentation](https://img.shields.io/badge/Documentation-AutoGen-blue?logo=read-the-docs)](https://microsoft.github.io/autogen/)
[![Blog](https://img.shields.io/badge/Blog-AutoGen-blue?logo=blogger)](https://devblogs.microsoft.com/autogen/)

</div>

# AutoGen [![Maintenance Mode](https://img.shields.io/badge/status-maintenance%20mode-orange)](https://github.com/microsoft/agent-framework)

**AutoGen** 是一个用于创建多智能体 AI 应用的框架，这些应用可以自主运行或与人协同工作。

> [!CAUTION]
> **⚠️ 维护模式**
>
> AutoGen 现已进入维护模式。它将不再接收新功能或增强，并由社区进行管理。
>
> 新用户可以开始使用 [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)。现有用户建议使用《[AutoGen → Microsoft Agent Framework 迁移指南](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/)》进行迁移。
>
> Microsoft Agent Framework (MAF) 是 AutoGen 的企业级继任者。Microsoft Agent Framework 现已作为生产就绪版本发布：提供稳定的 API，并承诺长期支持。无论你是构建单个助手还是编排一组专业智能体，Microsoft Agent Framework 1.0 都能为你提供企业级的多智能体编排能力、多提供商模型支持以及通过 A2A 和 MCP 实现的跨运行时互操作性。

## 安装

AutoGen 需要 **Python 3.10 或更高版本**。

```bash
# Install AgentChat and OpenAI client from Extensions
pip install -U "autogen-agentchat" "autogen-ext[openai]"
```

当前稳定版可在 [发布页面](https://github.com/microsoft/autogen/releases) 找到。如果你是从 AutoGen v0.2 升级，请参阅《[迁移指南](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/migration-guide.html)》获取更新代码和配置的详细说明。

```bash
# Install AutoGen Studio for no-code GUI
pip install -U "autogenstudio"
```

## 快速入门

以下示例调用了 OpenAI API，因此你需要先创建账户并导出密钥：`export OPENAI_API_KEY="sk-..."`。

### Hello World

使用 OpenAI 的 GPT-4o 模型创建一个助手智能体。请参阅 [其他支持的模型](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/models.html)。

```python
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

async def main() -> None:
    model_client = OpenAIChatCompletionClient(model="gpt-4.1")
    agent = AssistantAgent("assistant", model_client=model_client)
    print(await agent.run(task="Say 'Hello World!'"))
    await model_client.close()

asyncio.run(main())
```

### MCP 服务器

创建一个使用 Playwright MCP 服务器的网页浏览助手智能体。

```python
# First run `npm install -g @playwright/mcp@latest` to install the MCP server.
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.mcp import McpWorkbench, StdioServerParams


async def main() -> None:
    model_client = OpenAIChatCompletionClient(model="gpt-4.1")
    server_params = StdioServerParams(
        command="npx",
        args=[
            "@playwright/mcp@latest",
            "--headless",
        ],
    )
    async with McpWorkbench(server_params) as mcp:
        agent = AssistantAgent(
            "web_browsing_assistant",
            model_client=model_client,
            workbench=mcp, # For multiple MCP servers, put them in a list.
            model_client_stream=True,
            max_tool_iterations=10,
        )
        await Console(agent.run_stream(task="Find out how many contributors for the microsoft/autogen repository"))


asyncio.run(main())
```

> **警告**：仅连接受信任的 MCP 服务器，因为它们可能会在本地环境中执行命令或暴露敏感信息。

### 多智能体编排

你可以使用 `AgentTool` 创建一个基础的多智能体编排设置。

```python
import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.tools import AgentTool
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient


async def main() -> None:
    model_client = OpenAIChatCompletionClient(model="gpt-4.1")

    math_agent = AssistantAgent(
        "math_expert",
        model_client=model_client,
        system_message="You are a math expert.",
        description="A math expert assistant.",
        model_client_stream=True,
    )
    math_agent_tool = AgentTool(math_agent, return_value_as_last_message=True)

    chemistry_agent = AssistantAgent(
        "chemistry_expert",
        model_client=model_client,
        system_message="You are a chemistry expert.",
        description="A chemistry expert assistant.",
        model_client_stream=True,
    )
    chemistry_agent_tool = AgentTool(chemistry_agent, return_value_as_last_message=True)

    agent = AssistantAgent(
        "assistant",
        system_message="You are a general assistant. Use expert tools when needed.",
        model_client=model_client,
        model_client_stream=True,
        tools=[math_agent_tool, chemistry_agent_tool],
        max_tool_iterations=10,
    )
    await Console(agent.run_stream(task="What is the integral of x^2?"))
    await Console(agent.run_stream(task="What is the molecular weight of water?"))


asyncio.run(main())
```

如需更高级的多智能体编排和工作流，请阅读 [AgentChat 文档](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/index.html)。

### AutoGen Studio

使用 AutoGen Studio 在不编写代码的情况下快速原型设计和运行多智能体工作流。

> **注意**：AutoGen Studio 旨在帮助你快速原型化多智能体工作流，并展示基于 AutoGen 构建的终端用户界面示例。**它并非面向生产环境的应用**。建议开发者使用 AutoGen 框架构建自己的应用，以实现部署所需的安全、认证等功能。更多详情请参阅 [安全说明](https://microsoft.github.io/autogen/dev/user-guide/autogenstudio-user-guide/index.html#a-note-on-security)。

```bash
# Run AutoGen Studio on http://localhost:8080
autogenstudio ui --port 8080 --appdir ./my-app
```

## 为什么选择 AutoGen？

<div align="center">
  <img src="autogen-landing.jpg" alt="AutoGen Landing" width="500">
</div>

该框架由微软研究院首创，为实验性多智能体编排模式开辟了道路，并启发了整个社区。尽管 AutoGen 现已进入维护模式，现有用户仍可继续使用本文档所述架构的框架。**对于新项目，我们推荐使用 [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)**，它在吸取了 AutoGen 经验教训的基础上提供了企业级支持。

`autogen` _framework_ 采用分层且可扩展的设计。各层职责明确，并建立在底层之上。这种设计使你能够在不同抽象级别使用框架，从高级 API 到低级组件均可适用。

- [Core API](./python/packages/autogen-core/)：实现消息传递、事件驱动智能体以及本地和分布式运行时环境，以提供灵活性和强大功能。它还支持 .NET 和 Python 的跨语言互操作性。
- [AgentChat API](./python/packages/autogen-agentchat/)：提供更简洁但具有明确设计导向的 API，便于快速原型开发。该 API 基于 Core API 构建，最接近 v0.2 用户的熟悉体验，并支持常见的多智能体模式（如双智能体对话或群聊）。
- [Extensions API](./python/packages/autogen-ext/)：使第一方和第三方扩展能够持续丰富框架能力。它支持特定 LLM 客户端实现（例如 OpenAI、AzureOpenAI）以及代码执行等功能。

该生态系统还包含两个关键的 _开发者工具_：

<div align="center">
  <img src="https://media.githubusercontent.com/media/microsoft/autogen/refs/heads/main/python/packages/autogen-studio/docs/ags_screen.png" alt="AutoGen Studio Screenshot" width="500">
</div>

- [AutoGen Studio](./python/packages/autogen-studio/)：提供用于构建多智能体应用的无代码 GUI。
- [AutoGen Bench](./python/packages/agbench/)：提供评估智能体性能的基准测试套件。

你可以使用 AutoGen 框架和开发者工具为你的领域创建应用。例如，[Magentic-One](./python/packages/magentic-one-cli/) 是一个基于 AgentChat API 和 Extensions API 构建的尖端多智能体团队，能够处理需要网页浏览、代码执行和文件处理的各类任务。

如需社区支持，请访问我们的 [Discord 服务器](https://aka.ms/autogen-discord) 或 [GitHub Discussions](https://github.com/microsoft/autogen/discussions)。请注意，AutoGen 现已由社区管理，回复可能受限。

## 下一步该怎么做？

> **开始新项目？** 请前往 [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) 获取具备长期支持的最新多智能体功能。
>
> **现有 AutoGen 用户？** 请使用《[迁移指南](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/)》进行过渡，或参考以下资源查看当前 AutoGen 文档。

<div align="center">

|               | [![Python](https://img.shields.io/badge/AutoGen-Python-blue?logo=python&logoColor=white)](./python)                                                                                                                                                                                                                                                                                                                | [![.NET](https://img.shields.io/badge/AutoGen-.NET-green?logo=.net&logoColor=white)](./dotnet)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | [![Studio](https://img.shields.io/badge/AutoGen-Studio-purple?logo=visual-studio&logoColor=white)](./python/packages/autogen-studio)                        |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 安装          | [![Installation](https://img.shields.io/badge/Install-blue)](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/installation.html)                                                                                                                                                                                                                                                         | [![Install](https://img.shields.io/badge/Install-green)](https://microsoft.github.io/autogen/dotnet/dev/core/installation.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | [![Install](https://img.shields.io/badge/Install-purple)](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/installation.html) |
| 快速入门      | [![Quickstart](https://img.shields.io/badge/Quickstart-blue)](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/quickstart.html#)                                                                                                                                                                                                                                                         | [![Quickstart](https://img.shields.io/badge/Quickstart-green)](https://microsoft.github.io/autogen/dotnet/dev/core/index.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | [![Usage](https://img.shields.io/badge/Quickstart-purple)](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/usage.html#)      |
| 教程          | [![Tutorial](https://img.shields.io/badge/Tutorial-blue)](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/index.html)                                                                                                                                                                                                                                                          | [![Tutorial](https://img.shields.io/badge/Tutorial-green)](https://microsoft.github.io/autogen/dotnet/dev/core/tutorial.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | [![Usage](https://img.shields.io/badge/Tutorial-purple)](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/usage.html#)        |
| API 参考      | [![API](https://img.shields.io/badge/Docs-blue)](https://microsoft.github.io/autogen/stable/reference/index.html#)                                                                                                                                                                                                                                                                                                 | [![API](https://img.shields.io/badge/Docs-green)](https://microsoft.github.io/autogen/dotnet/dev/api/Microsoft.AutoGen.Contracts.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [![API](https://img.shields.io/badge/Docs-purple)](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/usage.html)               |
| 软件包        | [![PyPi autogen-core](https://img.shields.io/badge/PyPi-autogen--core-blue?logo=pypi)](https://pypi.org/project/autogen-core/) <br> [![PyPi autogen-agentchat](https://img.shields.io/badge/PyPi-autogen--agentchat-blue?logo=pypi)](https://pypi.org/project/autogen-agentchat/) <br> [![PyPi autogen-ext](https://img.shields.io/badge/PyPi-autogen--ext-blue?logo=pypi)](https://pypi.org/project/autogen-ext/) | [![NuGet Contracts](https://img.shields.io/badge/NuGet-Contracts-green?logo=nuget)](https://www.nuget.org/packages/Microsoft.AutoGen.Contracts/) <br> [![NuGet Core](https://img.shields.io/badge/NuGet-Core-green?logo=nuget)](https://www.nuget.org/packages/Microsoft.AutoGen.Core/) <br> [![NuGet Core.Grpc](https://img.shields.io/badge/NuGet-Core.Grpc-green?logo=nuget)](https://www.nuget.org/packages/Microsoft.AutoGen.Core.Grpc/) <br> [![NuGet RuntimeGateway.Grpc](https://img.shields.io/badge/NuGet-RuntimeGateway.Grpc-green?logo=nuget)](https://www.nuget.org/packages/Microsoft.AutoGen.RuntimeGateway.Grpc/) | [![PyPi autogenstudio](https://img.shields.io/badge/PyPi-autogenstudio-purple?logo=pypi)](https://pypi.org/project/autogenstudio/)                          |

</div>

有兴趣贡献代码？请参阅 [CONTRIBUTING.md](./CONTRIBUTING.md) 获取指南。由于 AutoGen 处于维护模式，贡献仅限于错误修复、安全补丁和文档改进。如需开发新功能，请考虑向 [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) 提交贡献。

有疑问？查阅我们的《[常见问题解答 (FAQ)](./FAQ.md)》。社区支持可通过 [GitHub Discussions](https://github.com/microsoft/autogen/discussions) 和 [Discord 服务器](https://aka.ms/autogen-discord) 获取，但由于 AutoGen 现已由社区管理，回复时间可能有所延长。如需获得积极支持的工具体系，请参阅 [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)。

## 法律声明

Microsoft 及任何贡献者根据 [知识共享署名 4.0 国际公共许可证](https://creativecommons.org/licenses/by/4.0/legalcode)（详见 [LICENSE](LICENSE) 文件）授予你使用本仓库中微软文档及其他内容的许可，并根据 [MIT 许可证](https://opensource.org/licenses/MIT)（详见 [LICENSE-CODE](LICENSE-CODE) 文件）授予你使用仓库中任何代码的许可。

Microsoft、Windows、Microsoft Azure 以及本文档中提及的其他微软产品或服务可能是微软在美国和其他国家的商标或注册商标。本项目的许可证未赋予你使用任何微软名称、徽标或商标的权利。微软的一般商标指南可参见 <http://go.microsoft.com/fwlink/?LinkID=254653>。

隐私信息可参见 <https://go.microsoft.com/fwlink/?LinkId=521839>

Microsoft 及任何贡献者保留所有其他权利，无论是依据其各自的版权、专利还是商标，无论是通过暗示、禁止反言还是其他方式。

<p align="right" style="font-size: 14px; color: #555; margin-top: 20px;">
  <a href="#readme-top" style="text-decoration: none; color: blue; font-weight: bold;">
    ↑ Back to Top ↑
  </a>
</p>