<div align="center">

<!-- omit in toc -->

<picture>
  <source width="550" media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/PrefectHQ/fastmcp/main/docs/assets/brand/f-watercolor-waves-4-dark.png">
  <source width="550" media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/PrefectHQ/fastmcp/main/docs/assets/brand/f-watercolor-waves-4.png">
  <img width="550" alt="FastMCP Logo" src="https://raw.githubusercontent.com/PrefectHQ/fastmcp/main/docs/assets/brand/f-watercolor-waves-2.png">
</picture>

# FastMCP 🚀

<strong>**快速行动，高效构建。**</strong>

*由 [Prefect](https://www.prefect.io/) 用 💙 打造*

[![Docs](https://img.shields.io/badge/docs-gofastmcp.com-blue)](https://gofastmcp.com)
[![Discord](https://img.shields.io/badge/community-discord-5865F2?logo=discord&logoColor=white)](https://discord.gg/uu8dJCgttd)
[![PyPI - Version](https://img.shields.io/pypi/v/fastmcp.svg)](https://pypi.org/project/fastmcp)
[![Tests](https://github.com/PrefectHQ/fastmcp/actions/workflows/run-tests.yml/badge.svg)](https://github.com/PrefectHQ/fastmcp/actions/workflows/run-tests.yml)
[![License](https://img.shields.io/github/license/PrefectHQ/fastmcp.svg)](https://github.com/PrefectHQ/fastmcp/blob/main/LICENSE)

<a href="https://trendshift.io/repositories/13266" target="_blank"><img src="https://trendshift.io/api/badge/repositories/13266" alt="prefecthq%2Ffastmcp | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</div>

---

[模型上下文协议](https://modelcontextprotocol.io/)（Model Context Protocol, MCP）将大语言模型与工具和数据进行连接。FastMCP 为你提供从原型开发到生产环境部署所需的一切：

```python
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run()
```

## 为什么选择 FastMCP

构建一个高效的 MCP 应用并非易事。FastMCP 帮你处理所有底层细节。只需使用 Python 函数声明工具，即可自动生成 Schema、验证逻辑和文档。通过 URL 连接服务器后，传输协商、身份认证以及协议生命周期管理都会自动为你完成。你只需专注于业务逻辑，其余的 MCP 相关部分都能完美运行：**借助 FastMCP，最佳实践已内置其中。**

**这就是为什么 FastMCP 成为使用 MCP 的标准框架。** FastMCP 1.0 于 2024 年并入官方 MCP Python SDK。如今，这个持续维护的独立项目日下载量达百万次，且各语言版本的 MCP 服务器中约有 70% 都由 FastMCP 的不同版本提供支持。

FastMCP 拥有三大核心支柱：

<table>
<tr>
<td align="center" valign="top" width="33%">
<a href="https://gofastmcp.com/servers/server">
<img src="https://raw.githubusercontent.com/PrefectHQ/fastmcp/main/docs/assets/images/servers-card.png" alt="Servers" />
<br /><strong>Servers（服务器）</strong>
</a>
<br />向大语言模型暴露工具、资源和提示词。
</td>
<td align="center" valign="top" width="33%">
<a href="https://gofastmcp.com/apps/overview">
<img src="https://raw.githubusercontent.com/PrefectHQ/fastmcp/main/docs/assets/images/apps-card.png" alt="Apps" />
<br /><strong>Apps（应用）</strong>
</a>
<br />为你的工具提供可直接在对话中渲染的交互式界面。
</td>
<td align="center" valign="top" width="33%">
<a href="https://gofastmcp.com/clients/client">
<img src="https://raw.githubusercontent.com/PrefectHQ/fastmcp/main/docs/assets/images/clients-card.png" alt="Clients" />
<br /><strong>Clients（客户端）</strong>
</a>
<br />连接任意 MCP 服务器——无论是本地还是远程，编程调用还是命令行均可。
</td>
</tr>
</table>

**[Servers](https://gofastmcp.com/servers/server)** 将你的 Python 函数封装为符合 MCP 标准的工具、资源和提示词。**[Clients](https://gofastmcp.com/clients/client)** 提供完整的协议支持以连接任意服务器。而 **[Apps](https://gofastmcp.com/apps/overview)** 则让你的工具具备可直接在对话中渲染的交互式界面。

准备好开始构建了吗？请阅读[安装指南](https://gofastmcp.com/getting-started/installation)，或直接前往[快速入门](https://gofastmcp.com/getting-started/quickstart)。

## 使用 Horizon 在生产环境中运行 FastMCP

FastMCP 是构建 MCP 服务器的标准方式。**[Prefect Horizon](https://www.prefect.io/horizon?utm_source=github&utm_medium=readme&utm_campaign=readme_horizon&utm_content=readme_body)** 则是用于安全运行这些服务器企业级 MCP 网关。

Horizon 由 FastMCP 团队打造，封装了我们在发布全球最受欢迎的 MCP 框架过程中积累的最佳实践。

从 GitHub 部署 FastMCP 服务器，支持分支预览与即时回滚。创建公司所用所有 MCP 的私有注册表。通过单点登录（SSO）和工具级基于角色的访问控制（RBAC）保障访问安全。获取审计日志、可观测性及全栈治理功能。将已审批的工具重新组合，为团队和智能体打造专用端点。

从 FastMCP 开始起步。[借助 Horizon 实现规模扩展 →](https://www.prefect.io/horizon?utm_source=github&utm_medium=readme&utm_campaign=readme_horizon&utm_content=readme_cta)

## 安装

我们推荐使用 [uv](https://docs.astral.sh/uv/) 安装 FastMCP：

```bash
uv pip install fastmcp
```

完整的安装说明（包括验证和升级步骤）请参阅[**安装指南**](https://gofastmcp.com/getting-started/installation)。

**正在升级？** 我们提供以下指南：
- [从 FastMCP v2 升级](https://gofastmcp.com/getting-started/upgrading/from-fastmcp-2)
- [从 MCP Python SDK 升级](https://gofastmcp.com/getting-started/upgrading/from-mcp-sdk)
- [从底层 SDK 升级](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk)

## 📚 文档

FastMCP 的完整文档位于 **[gofastmcp.com](https://gofastmcp.com)**，包含详细指南、API 参考以及高级使用模式。

文档还提供 [llms.txt 格式](https://llmstxt.org/)，这是一种简单的 Markdown 标准，便于大语言模型直接解析：

- [`llms.txt`](https://gofastmcp.com/llms.txt) 本质上是一个站点地图（sitemap），列出了文档中的所有页面。
- [`llms-full.txt`](https://gofastmcp.com/llms-full.txt) 包含全部文档内容。请注意，其体积可能超出你使用的 LLM 上下文窗口限制。

**社区：** 加入我们的 [Discord 服务器](https://discord.gg/uu8dJCgttd)，与其他 FastMCP 开发者交流，分享你的项目成果。

## 贡献指南

我们欢迎任何形式的贡献！请参阅[贡献指南](https://gofastmcp.com/development/contributing)获取环境配置说明、测试要求及 Pull Request（PR）规范。