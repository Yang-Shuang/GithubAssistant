![Microsoft Agent Framework](docs/assets/readme-banner.png)

# 欢迎使用 Microsoft Agent Framework！

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/b5zjErwbQM?style=flat)](https://discord.gg/b5zjErwbQM)
[![MS Learn Documentation](https://img.shields.io/badge/MS%20Learn-Documentation-blue)](https://learn.microsoft.com/en-us/agent-framework/)
[![PyPI](https://img.shields.io/pypi/v/agent-framework)](https://pypi.org/project/agent-framework/)
[![NuGet](https://img.shields.io/nuget/v/Microsoft.Agents.AI)](https://www.nuget.org/profiles/MicrosoftAgentFramework/)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/agent-framework?style=social)](https://github.com/microsoft/agent-framework/stargazers)


Microsoft Agent Framework（简称 MAF）是一个开源的多语言框架，用于在 **.NET 和 Python** 中构建**生产级 AI Agent（智能体）和多 Agent 工作流**。

MAF 专为将 Agent 从原型推向生产环境的团队而设计。它提供了在 Python 和 .NET 中构建、编排和运行 Agent 系统的一致基础，同时随着需求演进保持架构选择的开放性。框架支持广泛的生态系统，包括 Microsoft Foundry、Azure OpenAI、OpenAI 以及 GitHub Copilot SDK，并提供适用于本地开发和云部署的示例及托管模式。

<p align="center">
  <a href="https://www.youtube.com/watch?v=AAgdMhftj8w" title="观看完整的 Agent Framework 介绍视频（30分钟）">
    <img src="https://img.youtube.com/vi/AAgdMhftj8w/hqdefault.jpg"
         alt="观看完整的 Agent Framework 介绍视频（30分钟）" width="480">
  </a>
</p>
<p align="center">
  <a href="https://www.youtube.com/watch?v=AAgdMhftj8w">
    观看完整的 Agent Framework 介绍视频（30分钟）
  </a>
</p>

## 这是否适合你？

如果你符合以下情况，MAF 将非常适合：
- 正在构建预期在生产环境中运行的 Agent 和工作流；
- 需要超越单一提示词或无状态对话循环的编排能力；
- 希望采用基于图的模式，如顺序、并发、交接和小组协作；
- 关注持久性、可重启性、可观测性、治理或人工介入（human-in-the-loop）控制；
- 需要供应商灵活性，以便架构能在无需大规模重构的情况下演进。

## 核心功能
请访问[官方博客](https://devblogs.microsoft.com/agent-framework/)探索最新的 MAF 功能和实际实现模式。

- **Python 和 C#/.NET 支持**：为 Python 和 C#/.NET 提供完整的框架支持与一致的 API
  - [Python 包](./python/packages/) | [.NET 源码](./dotnet/src/)
- **多 Agent 供应商支持**：支持多种大语言模型（LLM）供应商，并持续增加更多
  - [Python 示例](./python/samples/02-agents/providers/) | [.NET 示例](./dotnet/samples/02-agents/AgentProviders/)
- **中间件（Middleware）**：灵活的中间件系统，用于请求/响应处理、异常处理和自定义管道
  - [Python 中间件](./python/samples/02-agents/middleware/) | [.NET 中间件](./dotnet/samples/02-agents/Agents/Agent_Step11_Middleware/)
- **编排模式与工作流**：使用基于图的工作流构建多 Agent 系统，支持顺序、并发、交接和小组协作模式；包含检查点、流式传输、人工介入和时间回溯功能
  - [Python 工作流](./python/samples/03-workflows/) | [.NET 工作流](./dotnet/samples/03-workflows/)
- **Foundry 托管 Agent（新增）**：仅需额外添加 2 行代码，即可将 Agent 部署并托管至 Foundry 基础设施
  - [Python 示例](./python/samples/04-hosting/foundry-hosted-agents/) | [.NET 示例](./dotnet/samples/04-hosting/FoundryHostedAgents/)
- **可观测性（Observability）**：内置 OpenTelemetry 集成，支持分布式追踪、监控和调试
  - [Python 可观测性示例](./python/samples/02-agents/observability/) | [.NET 遥测示例](./dotnet/samples/02-agents/AgentOpenTelemetry/)
- **声明式 Agent（Declarative Agents）**：使用 YAML 定义 Agent，以实现更快的配置和版本管理
  - [声明式 Agent 示例](./declarative-agents/)
- **Agent 技能（Agent Skills）**：从多个来源（文件、内联代码、类库）构建领域特定知识库，供 Agent 发现和使用
  - [技能设计文档](./docs/decisions/0021-agent-skills-design.md)
- **AF Labs**：用于前沿功能的实验性包，包括基准测试、强化学习和研究项目
  - [实验室目录](./python/packages/lab/)
- **开发者界面（DevUI）**：用于 Agent 开发、测试和调试工作流的交互式开发者界面
  - [查看 DevUI 实际运行效果](https://www.youtube.com/watch?v=mOAaGY4WPvc)

## 目录

- [快速开始](#getting-started)
  - [安装](#installation)
  - [学习资源](#learning-resources)
  - [快速入门](#quickstart)
    - [基础 Agent - Python](#basic-agent---python)
    - [基础 Agent - .NET](#basic-agent---net)
- [更多示例与代码库](#more-examples--samples)
- [社区与反馈](#community--feedback)
- [故障排除](#troubleshooting)
- [贡献者资源](#contributor-resources)

## 快速开始
### 安装
Python

```bash
pip install agent-framework
# This will install all sub-packages, see `python/packages` for individual packages.
# It may take a minute on first install on Windows.
```

.NET

```bash
dotnet add package Microsoft.Agents.AI
# For Foundry integration (used in the .NET quickstart below):
dotnet add package Microsoft.Agents.AI.Foundry
dotnet add package Azure.AI.Projects
dotnet add package Azure.Identity
```

### 学习资源

- **[概述](https://learn.microsoft.com/agent-framework/overview/agent-framework-overview)** - 框架的高级概览
- **[快速入门](https://learn.microsoft.com/agent-framework/tutorials/quick-start)** - 使用一个简单的 Agent 开始上手
- **[教程](https://learn.microsoft.com/agent-framework/tutorials/overview)** - 逐步操作指南
- **[用户指南](https://learn.microsoft.com/en-us/agent-framework/user-guide/overview)** - 构建 Agent 和工作流的深入指南
- **[从 Semantic Kernel 迁移](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-semantic-kernel)** - 迁移指南
- **[从 AutoGen 迁移](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen)** - 迁移指南

### 快速入门

#### 基础 Agent - Python

创建一个简单的 Azure Responses Agent，为其撰写一首关于 Microsoft Agent Framework 的俳句。

```python
# pip install agent-framework
# Use `az login` to authenticate with Azure CLI
import os
import asyncio
from agent_framework import Agent
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


async def main():
    # Initialize a chat agent with Microsoft Foundry
    # the endpoint, deployment name, and api version can be set via environment variables
    # or they can be passed in directly to the FoundryChatClient constructor
    agent = Agent(
      client=FoundryChatClient(
          credential=AzureCliCredential(),
          # project_endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
          # model=os.environ["FOUNDRY_MODEL_DEPLOYMENT_NAME"],
      ),
      name="HaikuAgent",
      instructions="You are an upbeat assistant that writes beautifully.",
    )

    print(await agent.run("Write a haiku about Microsoft Agent Framework."))

if __name__ == "__main__":
    asyncio.run(main())
```

#### 基础 Agent - .NET
创建一个使用 Microsoft Foundry 的简单 Agent，为其撰写一首关于 Microsoft Agent Framework 的俳句。

```c#
// This sample shows how to create and run a basic agent with AIProjectClient.AsAIAgent(...).

using Azure.AI.Projects;
using Azure.Identity;
using Microsoft.Agents.AI;

string endpoint = Environment.GetEnvironmentVariable("AZURE_AI_PROJECT_ENDPOINT") ?? throw new InvalidOperationException("AZURE_AI_PROJECT_ENDPOINT is not set.");
string deploymentName = Environment.GetEnvironmentVariable("AZURE_AI_MODEL_DEPLOYMENT_NAME") ?? "gpt-5.4-mini";

AIAgent agent =
    new AIProjectClient(new Uri(endpoint), new DefaultAzureCredential())
    .AsAIAgent(model: deploymentName, instructions: "You are an upbeat assistant that writes beautifully.", name: "HaikuAgent");

// Once you have the agent, you can invoke it like any other AIAgent.
Console.WriteLine(await agent.RunAsync("Write a haiku about Microsoft Agent Framework."));
```

## 更多示例与代码库

### Python

- [快速开始](./python/samples/01-get-started)：从 Hello World 到托管的渐进式教程
- [Agent（智能体）概念](./python/samples/02-agents)：按主题深入探索的示例（工具、中间件、供应商等）
- [工作流](./python/samples/03-workflows)：工作流的创建及其与 Agent 的集成
- [托管](./python/samples/04-hosting)：A2A、Azure Functions、Durable Task 托管
- [端到端应用](./python/samples/05-end-to-end)：完整应用程序、评估与演示

### .NET

- [快速开始](./dotnet/samples/01-get-started)：从 Hello Agent 到托管的渐进式教程
- [Agent（智能体）概念](./dotnet/samples/02-agents/Agents)：基础 Agent 创建与工具使用
- [Agent 供应商](./dotnet/samples/02-agents/AgentProviders)：展示不同 Agent 供应商的示例
- [工作流](./dotnet/samples/03-workflows)：高级多 Agent 模式与工作流编排
- [托管](./dotnet/samples/04-hosting)：A2A、Durable Agent（持久化智能体）、Durable Workflow（持久化工作流）
- [端到端应用](./dotnet/samples/05-end-to-end)：完整应用程序与演示

## 社区与反馈

- **发现 Bug？** 请提交 [GitHub Issue](https://github.com/microsoft/agent-framework/issues) 帮助我们改进。
- **喜欢 MAF？** [![GitHub stars](https://img.shields.io/badge/Star-us%20on%20GitHub-yellow)](https://github.com/microsoft/agent-framework) 点亮星标以表示支持，并帮助更多人发现该项目。
- **有疑问？** 加入我们的 [Discord](https://discord.gg/b5zjErwbQM) 或访问[每周办公时间](./COMMUNITY.md#public-community-office-hours)。

## 故障排除

### 身份验证（Authentication）

| 问题 | 原因 | 解决方法 |
|---------|-------|----------|
| 使用 Azure 凭据时出现身份验证错误 | 未登录 Azure CLI | 在启动应用前运行 `az login` |
| API 密钥报错 | 密钥错误或缺失 | 验证密钥并确保其适用于正确的资源/供应商 |

> **提示：** `DefaultAzureCredential` 在开发阶段很方便，但在生产环境中，建议使用特定凭据（例如 `ManagedIdentityCredential`）以避免延迟问题、意外的凭据探测以及回退机制带来的潜在安全风险。

### 环境变量
有关各示例特定的环境变量配置，请参阅对应示例目录中的 README（[Python 示例](./python/samples/) | [.NET 示例](./dotnet/samples/)）。

## 贡献者资源

- [贡献指南](./CONTRIBUTING.md)
- [Python 开发指南](./python/DEV_SETUP.md)
- [设计文档](./docs/design)
- [架构决策记录（ADR）](./docs/decisions)

## 重要说明

> [!IMPORTANT]
> 如果您使用 Microsoft Agent Framework 构建应用程序，并与任何第三方服务器、Agent、代码或非 Azure Direct 模型（“第三方系统”）进行交互，则需自行承担风险。根据《Microsoft 产品条款》，第三方系统属于非微软产品，并受其各自的第三方许可条款约束。您对任何使用情况及相关费用负责。
> 
> 我们建议您审查与第三方系统共享及接收的所有数据，并充分了解第三方在数据处理、共享、保留和存储位置方面的做法。您有责任管理您的数据是否会流出组织的 Azure 合规范围及地理边界及相关影响，并确保已配置适当的权限、边界和审批流程。
>  
> 您有责任在特定使用场景的上下文中，仔细审查和测试使用 Microsoft Agent Framework 构建的应用程序，并做出所有适当的决策和定制。这包括实施您自己的负责任 AI（AI）缓解措施，如元提示词（metaprompt）、内容过滤器或其他安全系统，并确保您的应用程序符合适当的质量、可靠性、安全性和可信度标准。另请参阅：[透明度常见问题解答](./TRANSPARENCY_FAQ.md)