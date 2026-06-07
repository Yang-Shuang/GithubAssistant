<p align="center"><a href="https://github.com/tadata-org/fastapi_mcp"><img src="https://github.com/user-attachments/assets/7e44e98b-a0ba-4aff-a68a-4ffee3a6189c" alt="fastapi-to-mcp" height=100/></a></p>

<div align="center">
  <span style="font-size: 0.85em; font-weight: normal;">由 <a href="https://tadata.com">Tadata</a> 构建</span>
</div>

<h1 align="center">
  FastAPI-MCP
</h1>

<div align="center">
<a href="https://trendshift.io/repositories/14064" target="_blank"><img src="https://trendshift.io/api/badge/repositories/14064" alt="tadata-org%2Ffastapi_mcp | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</div>

<p align="center">将你的 FastAPI 端点（endpoints）作为模型上下文协议（Model Context Protocol, MCP）工具暴露出来，并原生支持身份验证！</p>
<div align="center">

[![PyPI version](https://img.shields.io/pypi/v/fastapi-mcp?color=%2334D058&label=pypi%20package)](https://pypi.org/project/fastapi-mcp/)
[![Python Versions](https://img.shields.io/pypi/pyversions/fastapi-mcp.svg)](https://pypi.org/project/fastapi-mcp/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009485.svg?logo=fastapi&logoColor=white)](#)
[![CI](https://github.com/tadata-org/fastapi_mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/tadata-org/fastapi_mcp/actions/workflows/ci.yml)
[![Coverage](https://codecov.io/gh/tadata-org/fastapi_mcp/branch/main/graph/badge.svg)](https://codecov.io/gh/tadata-org/fastapi_mcp)

</div>


<p align="center"><a href="https://github.com/tadata-org/fastapi_mcp"><img src="https://github.com/user-attachments/assets/b205adc6-28c0-4e3c-a68b-9c1a80eb7d0c" alt="fastapi-mcp-usage" height="400"/></a></p>


## 功能特性

- **内置认证**：直接使用你现有的 FastAPI 依赖即可实现身份验证与授权！
- **原生支持 FastAPI**：不仅仅是另一个 OpenAPI 到 MCP 的转换器，而是深度集成方案
- **零配置或极低配置**：只需指向你的 FastAPI 应用即可直接运行
- **保留 Schema 定义**：完整保留请求模型和响应模型的 `Schema`（数据结构）
- **保留文档注释**：所有端点的说明文档将原样保留，与 Swagger 中显示的一致
- **灵活的部署方式**：可将 MCP 服务挂载到同一应用中，或选择独立部署
- **基于 ASGI 的传输层**：直接利用 FastAPI 的 ASGI 接口进行高效通信


## 托管服务

如果你更倾向于使用托管解决方案，请访问 [tadata.com](https://tadata.com)。

## 安装

推荐使用 [uv](https://docs.astral.sh/uv/)（一款快速的 Python 包管理器）进行安装：

```bash
uv add fastapi-mcp
```

或者，你也可以使用 pip 安装：

```bash
pip install fastapi-mcp
```

## 基本用法

使用 FastAPI-MCP 最简单的方法是直接将 MCP 服务添加到你的 FastAPI 应用中：

```python
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

app = FastAPI()

mcp = FastApiMCP(app)

# Mount the MCP server directly to your FastAPI app
mcp.mount()
```

完成！你自动生成的 MCP 服务现在可通过 `https://app.base.url/mcp` 访问。

## 文档、示例与高级用法

FastAPI-MCP 提供了[详尽的官方文档](https://fastapi-mcp.tadata.com/)。此外，请查看 [examples 目录](examples)，其中包含展示各项功能实际运行的代码示例。

## 以 FastAPI 为核心

FastAPI-MCP 被设计为 FastAPI 的原生扩展，而不仅仅是一个从你的 API 生成 MCP 工具的转换器。这种设计带来了以下核心优势：

- **原生依赖注入**：使用你熟悉的 FastAPI `Depends()` 为 MCP 端点提供身份验证和授权保护
- **ASGI 传输层**：通过 ASGI 接口直接与你的 FastAPI 应用通信，无需 MCP 向你的 API 发起额外的 HTTP 请求
- **统一的基础设施**：你的 FastAPI 应用无需与 MCP 服务分开运行（当然也支持[独立部署](https://fastapi-mcp.tadata.com/advanced/deploy#deploying-separately-from-original-fastapi-app)）

这一设计理念确保了在现有 FastAPI 服务中集成 MCP 功能时，能够最大程度地减少适配成本。


## 开发与贡献

感谢你对为 FastAPI-MCP 做出贡献的关注！我们鼓励社区成员提交 Issue（问题反馈）和创建 Pull Request（合并请求）。

在开始之前，请参阅我们的[贡献指南](CONTRIBUTING.md)。

## 社区交流

加入 [MCParty Slack 社区](https://join.slack.com/t/themcparty/shared_invite/zt-30yxr1zdi-2FG~XjBA0xIgYSYuKe7~Xg)，与其他 MCP 爱好者交流，提问并分享你使用 FastAPI-MCP 的经验。

## 环境要求

- Python 3.10+（推荐 3.12）
- uv

## 许可证

MIT 开源许可证。版权所有 © 2025 Tadata Inc。保留所有权利。