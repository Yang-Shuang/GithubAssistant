# MCP Python SDK

<div align="center">

<strong>模型上下文协议（Model Context Protocol，简称 MCP）的 Python 实现</strong>

[![PyPI][pypi-badge]][pypi-url]
[![MIT licensed][mit-badge]][mit-url]
[![Python Version][python-badge]][python-url]
[![Documentation][docs-badge]][docs-url]
[![Protocol][protocol-badge]][protocol-url]
[![Specification][spec-badge]][spec-url]

</div>

<!-- TODO(v2): Replace this README with README.v2.md when v2 is released -->

> [!NOTE]
> **本 README 文档记录的是 MCP Python SDK v1.x（当前稳定版）。**
>
> 如需查看 v1.x 的代码和文档，请参阅 [`v1.x` 分支](https://github.com/modelcontextprotocol/python-sdk/tree/v1.x)。
> 即将发布的 v2 文档（处于 pre-alpha 阶段，在 `main` 分支上开发中），请参阅 [`README.v2.md`](README.v2.md)。

<!-- omit in toc -->
## 目录

- [MCP Python SDK](#mcp-python-sdk)
  - [概述](#概述)
  - [安装](#安装)
    - [将 MCP 添加到你的 Python 项目](#将-mcp-添加到你的-python-项目)
    - [运行独立的 MCP 开发工具](#运行独立的-mcp-开发工具)
  - [快速入门](#快速入门)
  - [什么是 MCP？](#什么是-mcp)
  - [核心概念](#核心概念)
    - [服务器（Server）](#服务器server)
    - [资源（Resources）](#资源resources)
    - [工具（Tools）](#工具tools)
      - [结构化输出](#结构化输出)
    - [提示词（Prompts）](#提示词prompts)
    - [图标](#图标)
    - [图片](#图片)
    - [上下文（Context）](#上下文context)
      - [在函数中获取上下文](#在函数中获取上下文)
      - [上下文的属性与方法](#上下文的属性与方法)
    - [补全建议（Completions）](#补全建议completions)
    - [信息获取（Elicitation）](#信息获取elicitation)
    - [采样（Sampling）](#采样sampling)
    - [日志与通知](#日志与通知)
    - [身份验证（Authentication）](#身份验证authentication)
    - [FastMCP 属性](#fastmcp-属性)
    - [Session 属性与方法](#session-属性与方法)
    - [请求上下文属性](#请求上下文属性)
  - [运行你的服务器](#运行你的服务器)
    - [开发模式](#开发模式)
    - [Claude Desktop 集成](#claude-desktop-集成)
    - [直接执行](#直接执行)
    - [可流式传输的 HTTP 传输（Streamable HTTP）](#可流式传输的-http-传输streamable-http)
      - [面向浏览器客户端的 CORS 配置](#面向浏览器客户端的-cors-配置)
    - [挂载到现有 ASGI 服务器](#挂载到现有-asgi-服务器)
      - [StreamableHTTP 服务器](#streamablehttp-服务器)
        - [基础挂载](#基础挂载)
        - [基于主机的路由](#基于主机的路由)
        - [使用路径配置挂载多个服务器](#使用路径配置挂载多个服务器)
        - [初始化时配置路径](#初始化时配置路径)
      - [SSE 服务器](#sse-服务器)
  - [高级用法](#高级用法)
    - [底层服务器（Low-Level Server）](#底层服务器low-level-server)
      - [结构化输出支持](#结构化输出支持)
    - [分页（高级）](#分页高级)
    - [编写 MCP 客户端](#编写-mcp-客户端)
    - [客户端显示工具](#客户端显示工具)
    - [客户端的 OAuth 身份验证](#客户端的-oauth-身份验证)
    - [解析工具结果](#解析工具结果)
    - [MCP 基础原语](#mcp-基础原语)
    - [服务器能力（Server Capabilities）](#服务器能力server-capabilities)
  - [文档](#文档)
  - [贡献指南](#贡献指南)
  - [许可证](#许可证)

[pypi-badge]: https://img.shields.io/pypi/v/mcp.svg
[pypi-url]: https://pypi.org/project/mcp/
[mit-badge]: https://img.shields.io/pypi/l/mcp.svg
[mit-url]: https://github.com/modelcontextprotocol/python-sdk/blob/main/LICENSE
[python-badge]: https://img.shields.io/pypi/pyversions/mcp.svg
[python-url]: https://www.python.org/downloads/
[docs-badge]: https://img.shields.io/badge/docs-python--sdk-blue.svg
[docs-url]: https://modelcontextprotocol.github.io/python-sdk/
[protocol-badge]: https://img.shields.io/badge/protocol-modelcontextprotocol.io-blue.svg
[protocol-url]: https://modelcontextprotocol.io
[spec-badge]: https://img.shields.io/badge/spec-spec.modelcontextprotocol.io-blue.svg
[spec-url]: https://modelcontextprotocol.io/specification/latest

## 概述

模型上下文协议（Model Context Protocol）允许应用程序以标准化的方式为大语言模型提供上下文，将上下文的提供与实际的大语言模型交互分离开来。本 Python SDK 实现了完整的 MCP 规范，使以下操作变得简单：

- 构建可连接到任意 MCP 服务器的客户端
- 创建暴露资源、提示词和工具的 MCP 服务器
- 使用标准传输协议（如 stdio、SSE 和 Streamable HTTP）
- 处理所有 MCP 协议消息及生命周期事件

## 安装

### 将 MCP 添加到你的 Python 项目

我们建议使用 [uv](https://docs.astral.sh/uv/) 来管理你的 Python 项目。

如果你尚未创建由 uv 管理的项目，请先创建一个：

   ```bash
   uv init mcp-server-demo
   cd mcp-server-demo
   ```

   然后将 MCP 添加到你的项目依赖中：

   ```bash
   uv add "mcp[cli]"
   ```

或者，对于使用 pip 管理依赖的项目：

```bash
pip install "mcp[cli]"
```

### 运行独立的 MCP 开发工具

要使用 uv 运行 mcp 命令：

```bash
uv run mcp
```

## 快速入门

让我们创建一个简单的 MCP 服务器，它暴露一个计算器工具和部分数据：

<!-- snippet-source examples/snippets/servers/fastmcp_quickstart.py -->
```python
"""
FastMCP quickstart example.

Run from the repository root:
    uv run examples/snippets/servers/fastmcp_quickstart.py
"""

from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo", json_response=True)


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


# Add a prompt
@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    """Generate a greeting prompt"""
    styles = {
        "friendly": "Please write a warm, friendly greeting",
        "formal": "Please write a formal, professional greeting",
        "casual": "Please write a casual, relaxed greeting",
    }

    return f"{styles.get(style, styles['friendly'])} for someone named {name}."


# Run with streamable HTTP transport
if __name__ == "__main__":
    mcp.run(transport="streamable-http")
```

_Full example: [examples/snippets/servers/fastmcp_quickstart.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/fastmcp_quickstart.py)_
<!-- /snippet-source -->

你可以将此服务器安装到 [Claude Code](https://docs.claude.com/en/docs/claude-code/mcp) 中并立即进行交互。首先，运行服务器：

```bash
uv run --with mcp examples/snippets/servers/fastmcp_quickstart.py
```

然后将其添加到 Claude Code：

```bash
claude mcp add --transport http my-server http://localhost:8000/mcp
```

或者，你也可以使用 MCP Inspector 进行测试。按上述方式启动服务器后，在另一个终端中运行：

```bash
npx -y @modelcontextprotocol/inspector
```

在 inspector UI 中，连接到 `http://localhost:8000/mcp`。

## 什么是 MCP？

[模型上下文协议（MCP）](https://modelcontextprotocol.io) 允许你构建服务器，以安全、标准化的方式向大语言模型应用暴露数据和功能。可以把它想象成一种 Web API，但它是专门为与大语言模型交互而设计的。MCP 服务器可以：

- 通过 **资源（Resources）** 暴露数据（类似于 GET 端点；用于将信息加载到大语言模型的上下文中）
- 通过 **工具（Tools）** 提供功能（类似于 POST 端点；用于执行代码或产生其他副作用）
- 通过 **提示词（Prompts）** 定义交互模式（可复用的大语言模型交互模板）
- 以及更多！

## 核心概念

### 服务器（Server）

FastMCP 服务器是你与 MCP 协议交互的核心接口。它负责连接管理、协议合规性检查以及消息路由：

<!-- snippet-source examples/snippets/servers/lifespan_example.py -->
```python
"""Example showing lifespan support for startup/shutdown with strong typing."""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass

from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession


# Mock database class for example
class Database:
    """Mock database class for example."""

    @classmethod
    async def connect(cls) -> "Database":
        """Connect to database."""
        return cls()

    async def disconnect(self) -> None:
        """Disconnect from database."""
        pass

    def query(self) -> str:
        """Execute a query."""
        return "Query result"


@dataclass
class AppContext:
    """Application context with typed dependencies."""

    db: Database


@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    """Manage application lifecycle with type-safe context."""
    # Initialize on startup
    db = await Database.connect()
    try:
        yield AppContext(db=db)
    finally:
        # Cleanup on shutdown
        await db.disconnect()


# Pass lifespan to server
mcp = FastMCP("My App", lifespan=app_lifespan)


# Access type-safe lifespan context in tools
@mcp.tool()
def query_db(ctx: Context[ServerSession, AppContext]) -> str:
    """Tool that uses initialized resources."""
    db = ctx.request_context.lifespan_context.db
    return db.query()
```

_Full example: [examples/snippets/servers/lifespan_example.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/lifespan_example.py)_
<!-- /snippet-source -->

### 资源（Resources）

资源是你向大语言模型暴露数据的方式。它们类似于 REST API 中的 GET 端点——提供数据，但不应执行大量计算或产生副作用：

<!-- snippet-source examples/snippets/servers/basic_resource.py -->
```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="Resource Example")


@mcp.resource("file://documents/{name}")
def read_document(name: str) -> str:
    """Read a document by name."""
    # This would normally read from disk
    return f"Content of {name}"


@mcp.resource("config://settings")
def get_settings() -> str:
    """Get application settings."""
    return """{
  "theme": "dark",
  "language": "en",
  "debug": false
}"""
```

_Full example: [examples/snippets/servers/basic_resource.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/basic_resource.py)_
<!-- /snippet-source -->

### 工具（Tools）

工具允许大语言模型通过你的服务器采取行动。与资源不同，工具预期会执行计算并产生副作用：

<!-- snippet-source examples/snippets/servers/basic_tool.py -->
```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="Tool Example")


@mcp.tool()
def sum(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


@mcp.tool()
def get_weather(city: str, unit: str = "celsius") -> str:
    """Get weather for a city."""
    # This would normally call a weather API
    return f"Weather in {city}: 22degrees{unit[0].upper()}"
```

_Full example: [examples/snippets/servers/basic_tool.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/basic_tool.py)_
<!-- /snippet-source -->

工具可以通过包含带有 `Context` 类型注解的参数来接收上下文对象。该上下文由 FastMCP 框架自动注入，并提供对 MCP 能力的访问：

<!-- snippet-source examples/snippets/servers/tool_progress.py -->
```python
from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession

mcp = FastMCP(name="Progress Example")


@mcp.tool()
async def long_running_task(task_name: str, ctx: Context[ServerSession, None], steps: int = 5) -> str:
    """Execute a task with progress updates."""
    await ctx.info(f"Starting: {task_name}")

    for i in range(steps):
        progress = (i + 1) / steps
        await ctx.report_progress(
            progress=progress,
            total=1.0,
            message=f"Step {i + 1}/{steps}",
        )
        await ctx.debug(f"Completed step {i + 1}")

    return f"Task '{task_name}' completed"
```

_Full example: [examples/snippets/servers/tool_progress.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/tool_progress.py)_
<!-- /snippet-source -->

#### 结构化输出

默认情况下，如果工具的返回类型注解兼容，它将返回结构化结果。否则，将返回非结构化结果。

结构化输出支持以下返回类型：

- Pydantic 模型（BaseModel 子类）
- TypedDicts
- Dataclasses 及其他带有类型提示的类
- `dict[str, T]`（其中 T 是任何可 JSON 序列化的类型）
- 基础类型（str、int、float、bool、bytes、None）——包装在 `{"result": value}` 中
- 泛型类型（list、tuple、Union、Optional 等）——包装在 `{"result": value}` 中

没有类型提示的类无法为结构化输出进行序列化。只有正确注解了属性的类才会被转换为 Pydantic 模型，用于 schema 生成和验证。

结构化结果会根据从注解生成的输出模式自动进行验证。这确保工具返回类型良好且经过验证的数据，客户端可以轻松处理这些数据。

**注意：** 为了向后兼容，也会返回非结构化结果。提供非结构化结果是为了与 MCP 规范的早期版本保持向后兼容，并且在本 SDK 版本中与 FastMCP 的早期版本保持 quirks-compatible（行为一致）。

**注意：** 在某些情况下，如果工具的函数返回类型注解导致该工具被分类为结构化 _且这并不理想_，可以通过向 `@tool` 装饰器传递 `structured_output=False` 来抑制这种分类。

##### 高级：直接调用 CallToolResult

为了完全控制工具响应（包括 `_meta` 字段，用于向客户端应用程序传递数据而不暴露给模型），你可以直接返回 `CallToolResult`：

<!-- snippet-source examples/snippets/servers/direct_call_tool_result.py -->
```python
"""Example showing direct CallToolResult return for advanced control."""

from typing import Annotated

from pydantic import BaseModel

from mcp.server.fastmcp import FastMCP
from mcp.types import CallToolResult, TextContent

mcp = FastMCP("CallToolResult Example")


class ValidationModel(BaseModel):
    """Model for validating structured output."""

    status: str
    data: dict[str, int]


@mcp.tool()
def advanced_tool() -> CallToolResult:
    """Return CallToolResult directly for full control including _meta field."""
    return CallToolResult(
        content=[TextContent(type="text", text="Response visible to the model")],
        _meta={"hidden": "data for client applications only"},
    )


@mcp.tool()
def validated_tool() -> Annotated[CallToolResult, ValidationModel]:
    """Return CallToolResult with structured output validation."""
    return CallToolResult(
        content=[TextContent(type="text", text="Validated response")],
        structuredContent={"status": "success", "data": {"result": 42}},
        _meta={"internal": "metadata"},
    )


@mcp.tool()
def empty_result_tool() -> CallToolResult:
    """For empty results, return CallToolResult with empty content."""
    return CallToolResult(content=[])
```

_Full example: [examples/snippets/servers/direct_call_tool_result.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/direct_call_tool_result.py)_
<!-- /snippet-source -->

**重要：** `CallToolResult` 必须始终被返回（不能是 `Optional` 或 `Union`）。对于空结果，请使用 `CallToolResult(content=[])`。对于可选的基础类型，请不使用 `CallToolResult`，直接使用 `str | None`。

<!-- snippet-source examples/snippets/servers/structured_output.py -->
```python
"""Example showing structured output with tools."""

from typing import TypedDict

from pydantic import BaseModel, Field

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Structured Output Example")


# Using Pydantic models for rich structured data
class WeatherData(BaseModel):
    """Weather information structure."""

    temperature: float = Field(description="Temperature in Celsius")
    humidity: float = Field(description="Humidity percentage")
    condition: str
    wind_speed: float


@mcp.tool()
def get_weather(city: str) -> WeatherData:
    """Get weather for a city - returns structured data."""
    # Simulated weather data
    return WeatherData(
        temperature=22.5,
        humidity=45.0,
        condition="sunny",
        wind_speed=5.2,
    )


# Using TypedDict for simpler structures
class LocationInfo(TypedDict):
    latitude: float
    longitude: float
    name: str


@mcp.tool()
def get_location(address: str) -> LocationInfo:
    """Get location coordinates"""
    return LocationInfo(latitude=51.5074, longitude=-0.1278, name="London, UK")


# Using dict[str, Any] for flexible schemas
@mcp.tool()
def get_statistics(data_type: str) -> dict[str, float]:
    """Get various statistics"""
    return {"mean": 42.5, "median": 40.0, "std_dev": 5.2}


# Ordinary classes with type hints work for structured output
class UserProfile:
    name: str
    age: int
    email: str | None = None

    def __init__(self, name: str, age: int, email: str | None = None):
        self.name = name
        self.age = age
        self.email = email


@mcp.tool()
def get_user(user_id: str) -> UserProfile:
    """Get user profile - returns structured data"""
    return UserProfile(name="Alice", age=30, email="alice@example.com")


# Classes WITHOUT type hints cannot be used for structured output
class UntypedConfig:
    def __init__(self, setting1, setting2):  # type: ignore[reportMissingParameterType]
        self.setting1 = setting1
        self.setting2 = setting2


@mcp.tool()
def get_config() -> UntypedConfig:
    """This returns unstructured output - no schema generated"""
    return UntypedConfig("value1", "value2")


# Lists and other types are wrapped automatically
@mcp.tool()
def list_cities() -> list[str]:
    """Get a list of cities"""
    return ["London", "Paris", "Tokyo"]
    # Returns: {"result": ["London", "Paris", "Tokyo"]}


@mcp.tool()
def get_temperature(city: str) -> float:
    """Get temperature as a simple float"""
    return 22.5
    # Returns: {"result": 22.5}
```

_Full example: [examples/snippets/servers/structured_output.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/structured_output.py)_
<!-- /snippet-source -->

### 提示词（Prompts）

提示词是可复用的模板，帮助大语言模型有效地与你的服务器交互：

<!-- snippet-source examples/snippets/servers/basic_prompt.py -->
```python
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

mcp = FastMCP(name="Prompt Example")


@mcp.prompt(title="Code Review")
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"


@mcp.prompt(title="Debug Assistant")
def debug_error(error: str) -> list[base.Message]:
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]
```

_Full example: [examples/snippets/servers/basic_prompt.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/basic_prompt.py)_
<!-- /snippet-source -->

### 图标

MCP 服务器可以为 UI 显示提供图标。图标可以添加到服务器实现、工具、资源和提示词中：

```python
from mcp.server.fastmcp import FastMCP, Icon

# Create an icon from a file path or URL
icon = Icon(
    src="icon.png",
    mimeType="image/png",
    sizes="64x64"
)

# Add icons to server
mcp = FastMCP(
    "My Server",
    website_url="https://example.com",
    icons=[icon]
)

# Add icons to tools, resources, and prompts
@mcp.tool(icons=[icon])
def my_tool():
    """Tool with an icon."""
    return "result"

@mcp.resource("demo://resource", icons=[icon])
def my_resource():
    """Resource with an icon."""
    return "content"
```

_Full example: [examples/fastmcp/icons_demo.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/fastmcp/icons_demo.py)_

### 图片

FastMCP 提供了一个 `Image` 类，可自动处理图像数据：

<!-- snippet-source examples/snippets/servers/images.py -->
```python
"""Example showing image handling with FastMCP."""

from PIL import Image as PILImage

from mcp.server.fastmcp import FastMCP, Image

mcp = FastMCP("Image Example")


@mcp.tool()
def create_thumbnail(image_path: str) -> Image:
    """Create a thumbnail from an image"""
    img = PILImage.open(image_path)
    img.thumbnail((100, 100))
    return Image(data=img.tobytes(), format="png")
```

_Full example: [examples/snippets/servers/images.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/images.py)_
<!-- /snippet-source -->

### 上下文（Context）

`Context` 对象会自动注入到通过类型提示请求它的工具和资源函数中。它提供对日志记录、进度报告、资源读取、用户交互和请求元数据等 MCP 能力的访问。

#### 在函数中获取上下文

要在工具或资源函数中使用上下文，请添加一个带有 `Context` 类型注解的参数：

```python
from mcp.server.fastmcp import Context, FastMCP

mcp = FastMCP(name="Context Example")


@mcp.tool()
async def my_tool(x: int, ctx: Context) -> str:
    """Tool that uses context capabilities."""
    # The context parameter can have any name as long as it's type-annotated
    return await process_with_context(x, ctx)
```

#### 上下文的属性与方法

`Context` 对象提供以下能力：

- `ctx.request_id` - 当前请求的唯一 ID
- `ctx.client_id` - 客户端 ID（如果可用）
- `ctx.fastmcp` - 访问 FastMCP 服务器实例（见 [FastMCP 属性](#fastmcp-属性)）
- `ctx.session` - 访问底层 session 以进行高级通信（见 [Session 属性与方法](#session-属性与方法)）
- `ctx.request_context` - 访问请求特定数据和生命周期资源（见 [请求上下文属性](#请求上下文属性)）
- `await ctx.debug(message)` - 发送调试日志消息
- `await ctx.info(message)` - 发送信息日志消息  
- `await ctx.warning(message)` - 发送警告日志消息
- `await ctx.error(message)` - 发送错误日志消息
- `await ctx.log(level, message, logger_name=None)` - 发送带有自定义级别的日志
- `await ctx.report_progress(progress, total=None, message=None)` - 报告操作进度
- `await ctx.read_resource(uri)` - 通过 URI 读取资源
- `await ctx.elicit(message, schema)` - 请求用户提供额外信息并进行验证

<!-- snippet-source examples/snippets/servers/tool_progress.py -->
```python
from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession

mcp = FastMCP(name="Progress Example")


@mcp.tool()
async def long_running_task(task_name: str, ctx: Context[ServerSession, None], steps: int = 5) -> str:
    """Execute a task with progress updates."""
    await ctx.info(f"Starting: {task_name}")

    for i in range(steps):
        progress = (i + 1) / steps
        await ctx.report_progress(
            progress=progress,
            total=1.0,
            message=f"Step {i + 1}/{steps}",
        )
        await ctx.debug(f"Completed step {i + 1}")

    return f"Task '{task_name}' completed"
```

_Full example: [examples/snippets/servers/tool_progress.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/tool_progress.py)_
<!-- /snippet-source -->

### 补全建议（Completions）

MCP 支持为提示词参数和资源模板参数提供补全建议。借助上下文参数，服务器可以基于之前解析的值提供补全：

客户端用法：

<!-- snippet-source examples/snippets/clients/completion_client.py -->
```python
"""
cd to the `examples/snippets` directory and run:
    uv run completion-client
"""

import asyncio
import os

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.types import PromptReference, ResourceTemplateReference

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="uv",  # Using uv to run the server
    args=["run", "server", "completion", "stdio"],  # Server with completion support
    env={"UV_INDEX": os.environ.get("UV_INDEX", "")},
)


async def run():
    """Run the completion client example."""
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # List available resource templates
            templates = await session.list_resource_templates()
            print("Available resource templates:")
            for template in templates.resourceTemplates:
                print(f"  - {template.uriTemplate}")

            # List available prompts
            prompts = await session.list_prompts()
            print("\nAvailable prompts:")
            for prompt in prompts.prompts:
                print(f"  - {prompt.name}")

            # Complete resource template arguments
            if templates.resourceTemplates:
                template = templates.resourceTemplates[0]
                print(f"\nCompleting arguments for resource template: {template.uriTemplate}")

                # Complete without context
                result = await session.complete(
                    ref=ResourceTemplateReference(type="ref/resource", uri=template.uriTemplate),
                    argument={"name": "owner", "value": "model"},
                )
                print(f"Completions for 'owner' starting with 'model': {result.completion.values}")

                # Complete with context - repo suggestions based on owner
                result = await session.complete(
                    ref=ResourceTemplateReference(type="ref/resource", uri=template.uriTemplate),
                    argument={"name": "repo", "value": ""},
                    context_arguments={"owner": "modelcontextprotocol"},
                )
                print(f"Completions for 'repo' with owner='modelcontextprotocol': {result.completion.values}")

            # Complete prompt arguments
            if prompts.prompts:
                prompt_name = prompts.prompts[0].name
                print(f"\nCompleting arguments for prompt: {prompt_name}")

                result = await session.complete(
                    ref=PromptReference(type="ref/prompt", name=prompt_name),
                    argument={"name": "style", "value": ""},
                )
                print(f"Completions for 'style' argument: {result.completion.values}")


def main():
    """Entry point for the completion client."""
    asyncio.run(run())


if __name__ == "__main__":
    main()
```

_Full example: [examples/snippets/clients/completion_client.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/clients/completion_client.py)_
<!-- /snippet-source -->
### 信息获取（Elicitation）

请求用户提供额外信息。此示例展示了工具调用期间的 Elicitation：

<!-- snippet-source examples/snippets/servers/elicitation.py -->
```python
"""Elicitation examples demonstrating form and URL mode elicitation.

Form mode elicitation collects structured, non-sensitive data through a schema.
URL mode elicitation directs users to external URLs for sensitive operations
like OAuth flows, credential collection, or payment processing.
"""

import uuid

from pydantic import BaseModel, Field

from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession
from mcp.shared.exceptions import UrlElicitationRequiredError
from mcp.types import ElicitRequestURLParams

mcp = FastMCP(name="Elicitation Example")


class BookingPreferences(BaseModel):
    """Schema for collecting user preferences."""

    checkAlternative: bool = Field(description="Would you like to check another date?")
    alternativeDate: str = Field(
        default="2024-12-26",
        description="Alternative date (YYYY-MM-DD)",
    )


@mcp.tool()
async def book_table(date: str, time: str, party_size: int, ctx: Context[ServerSession, None]) -> str:
    """Book a table with date availability check.

    This demonstrates form mode elicitation for collecting non-sensitive user input.
    """
    # Check if date is available
    if date == "2024-12-25":
        # Date unavailable - ask user for alternative
        result = await ctx.elicit(
            message=(f"No tables available for {party_size} on {date}. Would you like to try another date?"),
            schema=BookingPreferences,
        )

        if result.action == "accept" and result.data:
            if result.data.checkAlternative:
                return f"[SUCCESS] Booked for {result.data.alternativeDate}"
            return "[CANCELLED] No booking made"
        return "[CANCELLED] Booking cancelled"

    # Date available
    return f"[SUCCESS] Booked for {date} at {time}"


@mcp.tool()
async def secure_payment(amount: float, ctx: Context[ServerSession, None]) -> str:
    """Process a secure payment requiring URL confirmation.

    This demonstrates URL mode elicitation using ctx.elicit_url() for
    operations that require out-of-band user interaction.
    """
    elicitation_id = str(uuid.uuid4())

    result = await ctx.elicit_url(
        message=f"Please confirm payment of ${amount:.2f}",
        url=f"https://payments.example.com/confirm?amount={amount}&id={elicitation_id}",
        elicitation_id=elicitation_id,
    )

    if result.action == "accept":
        # In a real app, the payment confirmation would happen out-of-band
        # and you'd verify the payment status from your backend
        return f"Payment of ${amount:.2f} initiated - check your browser to complete"
    elif result.action == "decline":
        return "Payment declined by user"
    return "Payment cancelled"


@mcp.tool()
async def connect_service(service_name: str, ctx: Context[ServerSession, None]) -> str:
    """Connect to a third-party service requiring OAuth authorization.

    This demonstrates the "throw error" pattern using UrlElicitationRequiredError.
    Use this pattern when the tool cannot proceed without user authorization.
    """
    elicitation_id = str(uuid.uuid4())

    # Raise UrlElicitationRequiredError to signal that the client must complete
    # a URL elicitation before this request can be processed.
    # The MCP framework will convert this to a -32042 error response.
    raise UrlElicitationRequiredError(
        [
            ElicitRequestURLParams(
                mode="url",
                message=f"Authorization required to connect to {service_name}",
                url=f"https://{service_name}.example.com/oauth/authorize?elicit={elicitation_id}",
                elicitationId=elicitation_id,
            )
        ]
    )
```

_Full example: [examples/snippets/servers/elicitation.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/elicitation.py)_
<!-- /snippet-source -->

Elicitation 模式支持所有字段类型的默认值。默认值会自动包含在发送给客户端的 JSON schema 中，允许它们预填充表单。

`elicit()` 方法返回一个 `ElicitationResult`，其中包含：

- `action`: "accept"、"decline" 或 "cancel"
- `data`: 验证后的响应（仅在接受时）
- `validation_error`: 任何验证错误消息

### 采样（Sampling）

工具可以通过采样（生成文本）与大语言模型交互：

<!-- snippet-source examples/snippets/servers/sampling.py -->
```python
from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession
from mcp.types import SamplingMessage, TextContent

mcp = FastMCP(name="Sampling Example")


@mcp.tool()
async def generate_poem(topic: str, ctx: Context[ServerSession, None]) -> str:
    """Generate a poem using LLM sampling."""
    prompt = f"Write a short poem about {topic}"

    result = await ctx.session.create_message(
        messages=[
            SamplingMessage(
                role="user",
                content=TextContent(type="text", text=prompt),
            )
        ],
        max_tokens=100,
    )

    # Since we're not passing tools param, result.content is single content
    if result.content.type == "text":
        return result.content.text
    return str(result.content)
```

_Full example: [examples/snippets/servers/sampling.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/sampling.py)_
<!-- /snippet-source -->

### 日志与通知

工具可以通过上下文发送日志和通知：

<!-- snippet-source examples/snippets/servers/notifications.py -->
```python
from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession

mcp = FastMCP(name="Notifications Example")


@mcp.tool()
async def process_data(data: str, ctx: Context[ServerSession, None]) -> str:
    """Process data with logging."""
    # Different log levels
    await ctx.debug(f"Debug: Processing '{data}'")
    await ctx.info("Info: Starting processing")
    await ctx.warning("Warning: This is experimental")
    await ctx.error("Error: (This is just a demo)")

    # Notify about resource changes
    await ctx.session.send_resource_list_changed()

    return f"Processed: {data}"
```

_Full example: [examples/snippets/servers/notifications.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/notifications.py)_
<!-- /snippet-source -->

### 身份验证（Authentication）

希望暴露访问受保护资源的工具时，服务器可以使用身份验证。

`mcp.server.auth` 实现了 OAuth 2.1 资源服务器功能，其中 MCP 服务器作为资源服务器（RS），用于验证由独立授权服务器（AS）签发的令牌。这遵循了 [MCP 授权规范](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization)，并实现了 RFC 9728（受保护资源元数据）以进行 AS 发现。

MCP 服务器可以通过提供 `TokenVerifier` 协议的实现来使用身份验证：

<!-- snippet-source examples/snippets/servers/oauth_server.py -->
```python
"""
Run from the repository root:
    uv run examples/snippets/servers/oauth_server.py
"""

from pydantic import AnyHttpUrl

from mcp.server.auth.provider import AccessToken, TokenVerifier
from mcp.server.auth.settings import AuthSettings
from mcp.server.fastmcp import FastMCP


class SimpleTokenVerifier(TokenVerifier):
    """Simple token verifier for demonstration."""

    async def verify_token(self, token: str) -> AccessToken | None:
        pass  # This is where you would implement actual token validation


# Create FastMCP instance as a Resource Server
mcp = FastMCP(
    "Weather Service",
    json_response=True,
    # Token verifier for authentication
    token_verifier=SimpleTokenVerifier(),
    # Auth settings for RFC 9728 Protected Resource Metadata
    auth=AuthSettings(
        issuer_url=AnyHttpUrl("https://auth.example.com"),  # Authorization Server URL
        resource_server_url=AnyHttpUrl("http://localhost:3001"),  # This server's URL
        required_scopes=["user"],
    ),
)


@mcp.tool()
async def get_weather(city: str = "London") -> dict[str, str]:
    """Get weather data for a city"""
    return {
        "city": city,
        "temperature": "22",
        "condition": "Partly cloudy",
        "humidity": "65%",
    }


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
```

_Full example: [examples/snippets/servers/oauth_server.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/oauth_server.py)_
<!-- /snippet-source -->

有关包含独立授权服务器和资源服务器实现的完整示例，请参阅 [`examples/servers/simple-auth/`](examples/servers/simple-auth/)。

**架构：**

- **授权服务器（AS）**：处理 OAuth 流程、用户身份验证和令牌签发
- **资源服务器（RS）**：你的 MCP 服务器，用于验证令牌并serve受保护的资源
- **客户端**：通过 RFC 9728 发现 AS，获取令牌，并在 MCP 服务器中使用它们

有关实现令牌验证的更多详细信息，请参阅 [TokenVerifier](src/mcp/server/auth/provider.py)。

### FastMCP 属性

可通过 `ctx.fastmcp` 访问的 FastMCP 服务器实例提供对服务器配置和元数据的访问：

- `ctx.fastmcp.name` - 初始化时定义的服务器名称
- `ctx.fastmcp.instructions` - 提供给客户端的服务器指令/描述
- `ctx.fastmcp.website_url` - 服务器的可选网站 URL
- `ctx.fastmcp.icons` - 用于 UI 显示的可选图标列表
- `ctx.fastmcp.settings` - 包含完整服务器配置的配置对象，其中：
  - `debug` - 调试模式标志
  - `log_level` - 当前日志级别
  - `host` 和 `port` - 服务器网络配置
  - `mount_path`, `sse_path`, `streamable_http_path` - 传输路径
  - `stateless_http` - 服务器是否以无状态模式运行
  - 以及其他配置选项

```python
@mcp.tool()
def server_info(ctx: Context) -> dict:
    """Get information about the current server."""
    return {
        "name": ctx.fastmcp.name,
        "instructions": ctx.fastmcp.instructions,
        "debug_mode": ctx.fastmcp.settings.debug,
        "log_level": ctx.fastmcp.settings.log_level,
        "host": ctx.fastmcp.settings.host,
        "port": ctx.fastmcp.settings.port,
    }
```

### Session 属性与方法

可通过 `ctx.session` 访问的 session 对象提供对客户端通信的高级控制：

- `ctx.session.client_params` - 客户端初始化参数和声明的能力
- `await ctx.session.send_log_message(level, data, logger)` - 发送具有完全控制的日志消息
- `await ctx.session.create_message(messages, max_tokens)` - 请求大语言模型采样/补全
- `await ctx.session.send_progress_notification(token, progress, total, message)` - 直接进度更新
- `await ctx.session.send_resource_updated(uri)` - 通知客户端特定资源已更改
- `await ctx.session.send_resource_list_changed()` - 通知客户端资源列表已更改
- `await ctx.session.send_tool_list_changed()` - 通知客户端工具列表已更改
- `await ctx.session.send_prompt_list_changed()` - 通知客户端提示词列表已更改

```python
@mcp.tool()
async def notify_data_update(resource_uri: str, ctx: Context) -> str:
    """Update data and notify clients of the change."""
    # Perform data update logic here
    
    # Notify clients that this specific resource changed
    await ctx.session.send_resource_updated(AnyUrl(resource_uri))
    
    # If this affects the overall resource list, notify about that too
    await ctx.session.send_resource_list_changed()
    
    return f"Updated {resource_uri} and notified clients"
```

### 请求上下文属性

可通过 `ctx.request_context` 访问的请求上下文包含请求特定信息和资源：

- `ctx.request_context.lifespan_context` - 访问服务器启动期间初始化的资源
  - 数据库连接、配置对象、共享服务
  - 对服务器生命周期函数中定义的资源进行类型安全的访问
- `ctx.request_context.meta` - 来自客户端的请求元数据，包括：
  - `progressToken` - 进度通知令牌
  - 其他客户端提供的元数据
- `ctx.request_context.request` - 原始 MCP 请求对象，用于高级处理
- `ctx.request_context.request_id` - 此请求的唯一标识符

```python
# Example with typed lifespan context
@dataclass
class AppContext:
    db: Database
    config: AppConfig

@mcp.tool()
def query_with_config(query: str, ctx: Context) -> str:
    """Execute a query using shared database and configuration."""
    # Access typed lifespan context
    app_ctx: AppContext = ctx.request_context.lifespan_context
    
    # Use shared resources
    connection = app_ctx.db
    settings = app_ctx.config
    
    # Execute query with configuration
    result = connection.execute(query, timeout=settings.query_timeout)
    return str(result)
```

_Full lifespan example: [examples/snippets/servers/lifespan_example.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/lifespan_example.py)_

## 运行你的服务器

### 开发模式

测试和调试服务器的最快方法是使用 MCP Inspector：

```bash
uv run mcp dev server.py

# Add dependencies
uv run mcp dev server.py --with pandas --with numpy

# Mount local code
uv run mcp dev server.py --with-editable .
```

### Claude Desktop 集成

当你的服务器准备就绪后，将其安装到 Claude Desktop：

```bash
uv run mcp install server.py

# Custom name
uv run mcp install server.py --name "My Analytics Server"

# Environment variables
uv run mcp install server.py -v API_KEY=abc123 -v DB_URL=postgres://...
uv run mcp install server.py -f .env
```

### 直接执行

对于高级场景（如自定义部署）：

<!-- snippet-source examples/snippets/servers/direct_execution.py -->
```python
"""Example showing direct execution of an MCP server.

This is the simplest way to run an MCP server directly.
cd to the `examples/snippets` directory and run:
    uv run direct-execution-server
    or
    python servers/direct_execution.py
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My App")


@mcp.tool()
def hello(name: str = "World") -> str:
    """Say hello to someone."""
    return f"Hello, {name}!"


def main():
    """Entry point for the direct execution server."""
    mcp.run()


if __name__ == "__main__":
    main()
```

_Full example: [examples/snippets/servers/direct_execution.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/direct_execution.py)_
<!-- /snippet-source -->

使用以下方式运行：

```bash
python servers/direct_execution.py
# or
uv run mcp run servers/direct_execution.py
```

请注意，`uv run mcp run` 或 `uv run mcp dev` 仅支持使用 FastMCP 的服务器，不支持底层服务器变体。

### 可流式传输的 HTTP 传输（Streamable HTTP）

> **注意**：Streamable HTTP 传输是生产部署推荐使用的传输方式。使用 `stateless_http=True` 和 `json_response=True` 以获得最佳的可扩展性。

<!-- snippet-source examples/snippets/servers/streamable_config.py -->
```python
"""
Run from the repository root:
    uv run examples/snippets/servers/streamable_config.py
"""

from mcp.server.fastmcp import FastMCP

# Stateless server with JSON responses (recommended)
mcp = FastMCP("StatelessServer", stateless_http=True, json_response=True)

# Other configuration options:
# Stateless server with SSE streaming responses
# mcp = FastMCP("StatelessServer", stateless_http=True)

# Stateful server with session persistence
# mcp = FastMCP("StatefulServer")


# Add a simple tool to demonstrate the server
@mcp.tool()
def greet(name: str = "World") -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"


# Run server with streamable_http transport
if __name__ == "__main__":
    mcp.run(transport="streamable-http")
```

_Full example: [examples/snippets/servers/streamable_config.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/streamable_config.py)_
<!-- /snippet-source -->

你可以在 Starlette 应用中挂载多个 FastMCP 服务器：

<!-- snippet-source examples/snippets/servers/streamable_starlette_mount.py -->
```python
"""
Run from the repository root:
    uvicorn examples.snippets.servers.streamable_starlette_mount:app --reload
"""

import contextlib

from starlette.applications import Starlette
from starlette.routing import Mount

from mcp.server.fastmcp import FastMCP

# Create the Echo server
echo_mcp = FastMCP(name="EchoServer", stateless_http=True, json_response=True)


@echo_mcp.tool()
def echo(message: str) -> str:
    """A simple echo tool"""
    return f"Echo: {message}"


# Create the Math server
math_mcp = FastMCP(name="MathServer", stateless_http=True, json_response=True)


@math_mcp.tool()
def add_two(n: int) -> int:
    """Tool to add two to the input"""
    return n + 2


# Create a combined lifespan to manage both session managers
@contextlib.asynccontextmanager
async def lifespan(app: Starlette):
    async with contextlib.AsyncExitStack() as stack:
        await stack.enter_async_context(echo_mcp.session_manager.run())
        await stack.enter_async_context(math_mcp.session_manager.run())
        yield


# Create the Starlette app and mount the MCP servers
app = Starlette(
    routes=[
        Mount("/echo", echo_mcp.streamable_http_app()),
        Mount("/math", math_mcp.streamable_http_app()),
    ],
    lifespan=lifespan,
)

# Note: Clients connect to http://localhost:8000/echo/mcp and http://localhost:8000/math/mcp
# To mount at the root of each path (e.g., /echo instead of /echo/mcp):
# echo_mcp.settings.streamable_http_path = "/"
# math_mcp.settings.streamable_http_path = "/"
```

_Full example: [examples/snippets/servers/streamable_starlette_mount.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/streamable_starlette_mount.py)_
<!-- /snippet-source -->

对于使用 Streamable HTTP 实现的底层服务器，请参阅：

- 有状态服务器：[`examples/servers/simple-streamablehttp/`](examples/servers/simple-streamablehttp/)
- 无状态服务器：[`examples/servers/simple-streamablehttp-stateless/`](examples/servers/simple-streamablehttp-stateless/)

Streamable HTTP 传输支持：

- 有状态和无状态操作模式
- 使用事件存储的恢复能力（Resumability）
- JSON 或 SSE 响应格式
- 多节点部署更好的可扩展性

#### 面向浏览器客户端的 CORS 配置

如果你的服务器希望被基于浏览器的 MCP 客户端访问，你需要配置 CORS 头。`Mcp-Session-Id` 标头必须暴露给浏览器客户端以便访问：

```python
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware

# Create your Starlette app first
starlette_app = Starlette(routes=[...])

# Then wrap it with CORS middleware
starlette_app = CORSMiddleware(
    starlette_app,
    allow_origins=["*"],  # Configure appropriately for production
    allow_methods=["GET", "POST", "DELETE"],  # MCP streamable HTTP methods
    expose_headers=["Mcp-Session-Id"],
)
```

此配置是必要的，因为：

- MCP Streamable HTTP 传输使用 `Mcp-Session-Id` 标头进行会话管理
- 浏览器限制对响应标头的访问，除非通过 CORS 明确暴露
- 如果没有此配置，基于浏览器的客户端将无法从初始化响应中读取会话 ID

### 挂载到现有 ASGI 服务器

默认情况下，SSE 服务器挂载在 `/sse`，Streamable HTTP 服务器挂载在 `/mcp`。你可以使用下文描述的方法自定义这些路径。

有关在 Starlette 中挂载应用的更多信息，请参阅 [Starlette 文档](https://www.starlette.io/routing/#submounting-routes)。

#### StreamableHTTP 服务器

你可以使用 `streamable_http_app` 方法将 StreamableHTTP 服务器挂载到现有 ASGI 服务器上。这允许你将 StreamableHTTP 服务器与其他 ASGI 应用集成。

##### 基础挂载

<!-- snippet-source examples/snippets/servers/streamable_http_basic_mounting.py -->
```python
"""
Basic example showing how to mount StreamableHTTP server in Starlette.

Run from the repository root:
    uvicorn examples.snippets.servers.streamable_http_basic_mounting:app --reload
"""

import contextlib

from starlette.applications import Starlette
from starlette.routing import Mount

from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("My App", json_response=True)


@mcp.tool()
def hello() -> str:
    """A simple hello tool"""
    return "Hello from MCP!"


# Create a lifespan context manager to run the session manager
@contextlib.asynccontextmanager
async def lifespan(app: Starlette):
    async with mcp.session_manager.run():
        yield


# Mount the StreamableHTTP server to the existing ASGI server
app = Starlette(
    routes=[
        Mount("/", app=mcp.streamable_http_app()),
    ],
    lifespan=lifespan,
)
```

_Full example: [examples/snippets/servers/streamable_http_basic_mounting.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/streamable_http_basic_mounting.py)_
<!-- /snippet-source -->

##### 基于主机的路由

<!-- snippet-source examples/snippets/servers/streamable_http_host_mounting.py -->
```python
"""
Example showing how to mount StreamableHTTP server using Host-based routing.

Run from the repository root:
    uvicorn examples.snippets.servers.streamable_http_host_mounting:app --reload
"""

import contextlib

from starlette.applications import Starlette
from starlette.routing import Host

from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("MCP Host App", json_response=True)


@mcp.tool()
def domain_info() -> str:
    """Get domain-specific information"""
    return "This is served from mcp.acme.corp"


# Create a lifespan context manager to run the session manager
@contextlib.asynccontextmanager
async def lifespan(app: Starlette):
    async with mcp.session_manager.run():
        yield


# Mount using Host-based routing
app = Starlette(
    routes=[
        Host("mcp.acme.corp", app=mcp.streamable_http_app()),
    ],
    lifespan=lifespan,
)
```

_Full example: [examples/snippets/servers/streamable_http_host_mounting.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/streamable_http_host_mounting.py)_
<!-- /snippet-source -->

##### 使用路径配置挂载多个服务器

<!-- snippet-source examples/snippets/servers/streamable_http_multiple_servers.py -->
```python
"""
Example showing how to mount multiple StreamableHTTP servers with path configuration.

Run from the repository root:
    uvicorn examples.snippets.servers.streamable_http_multiple_servers:app --reload
"""

import contextlib

from starlette.applications import Starlette
from starlette.routing import Mount

from mcp.server.fastmcp import FastMCP

# Create multiple MCP servers
api_mcp = FastMCP("API Server", json_response=True)
chat_mcp = FastMCP("Chat Server", json_response=True)


@api_mcp.tool()
def api_status() -> str:
    """Get API status"""
    return "API is running"


@chat_mcp.tool()
def send_message(message: str) -> str:
    """Send a chat message"""
    return f"Message sent: {message}"


# Configure servers to mount at the root of each path
# This means endpoints will be at /api and /chat instead of /api/mcp and /chat/mcp
api_mcp.settings.streamable_http_path = "/"
chat_mcp.settings.streamable_http_path = "/"


# Create a combined lifespan to manage both session managers
@contextlib.asynccontextmanager
async def lifespan(app: Starlette):
    async with contextlib.AsyncExitStack() as stack:
        await stack.enter_async_context(api_mcp.session_manager.run())
        await stack.enter_async_context(chat_mcp.session_manager.run())
        yield


# Mount the servers
app = Starlette(
    routes=[
        Mount("/api", app=api_mcp.streamable_http_app()),
        Mount("/chat", app=chat_mcp.streamable_http_app()),
    ],
    lifespan=lifespan,
)
```

_Full example: [examples/snippets/servers/streamable_http_multiple_servers.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/streamable_http_multiple_servers.py)_
<!-- /snippet-source -->

##### 初始化时配置路径

<!-- snippet-source examples/snippets/servers/streamable_http_path_config.py -->
```python
"""
Example showing path configuration during FastMCP initialization.

Run from the repository root:
    uvicorn examples.snippets.servers.streamable_http_path_config:app --reload
"""

from starlette.applications import Starlette
from starlette.routing import Mount

from mcp.server.fastmcp import FastMCP

# Configure streamable_http_path during initialization
# This server will mount at the root of wherever it's mounted
mcp_at_root = FastMCP(
    "My Server",
    json_response=True,
    streamable_http_path="/",
)


@mcp_at_root.tool()
def process_data(data: str) -> str:
    """Process some data"""
    return f"Processed: {data}"


# Mount at /process - endpoints will be at /process instead of /process/mcp
app = Starlette(
    routes=[
        Mount("/process", app=mcp_at_root.streamable_http_app()),
    ]
)
```

_Full example: [examples/snippets/servers/streamable_http_path_config.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/streamable_http_path_config.py)_
<!-- /snippet-source -->

#### SSE 服务器

> **注意**：SSE 传输正被 [Streamable HTTP 传输](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http) 取代。

你可以使用 `sse_app` 方法将 SSE 服务器挂载到现有 ASGI 服务器上。这允许你将 SSE 服务器与其他 ASGI 应用集成。

```python
from starlette.applications import Starlette
from starlette.routing import Mount, Host
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("My App")

# Mount the SSE server to the existing ASGI server
app = Starlette(
    routes=[
        Mount('/', app=mcp.sse_app()),
    ]
)

# or dynamically mount as host
app.router.routes.append(Host('mcp.acme.corp', app=mcp.sse_app()))
```

在不同路径下挂载多个 MCP 服务器时，你可以通过多种方式配置挂载路径：

```python
from starlette.applications import Starlette
from starlette.routing import Mount
from mcp.server.fastmcp import FastMCP

# Create multiple MCP servers
github_mcp = FastMCP("GitHub API")
browser_mcp = FastMCP("Browser")
curl_mcp = FastMCP("Curl")
search_mcp = FastMCP("Search")

# Method 1: Configure mount paths via settings (recommended for persistent configuration)
github_mcp.settings.mount_path = "/github"
browser_mcp.settings.mount_path = "/browser"

# Method 2: Pass mount path directly to sse_app (preferred for ad-hoc mounting)
# This approach doesn't modify the server's settings permanently

# Create Starlette app with multiple mounted servers
app = Starlette(
    routes=[
        # Using settings-based configuration
        Mount("/github", app=github_mcp.sse_app()),
        Mount("/browser", app=browser_mcp.sse_app()),
        # Using direct mount path parameter
        Mount("/curl", app=curl_mcp.sse_app("/curl")),
        Mount("/search", app=search_mcp.sse_app("/search")),
    ]
)

# Method 3: For direct execution, you can also pass the mount path to run()
if __name__ == "__main__":
    search_mcp.run(transport="sse", mount_path="/search")
```

有关在 Starlette 中挂载应用的更多信息，请参阅 [Starlette 文档](https://www.starlette.io/routing/#submounting-routes)。

## 高级用法

### 底层服务器（Low-Level Server）

为了获得更细粒度的控制，你可以直接使用底层服务器实现。这使你能够完全访问协议，并允许你自定义服务器的每个方面，包括通过生命周期 API 进行生命周期管理：

<!-- snippet-source examples/snippets/servers/lowlevel/lifespan.py -->
```python
"""
Run from the repository root:
    uv run examples/snippets/servers/lowlevel/lifespan.py
"""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Any

import mcp.server.stdio
import mcp.types as types
from mcp.server.lowlevel import NotificationOptions, Server
from mcp.server.models import InitializationOptions


# Mock database class for example
class Database:
    """Mock database class for example."""

    @classmethod
    async def connect(cls) -> "Database":
        """Connect to database."""
        print("Database connected")
        return cls()

    async def disconnect(self) -> None:
        """Disconnect from database."""
        print("Database disconnected")

    async def query(self, query_str: str) -> list[dict[str, str]]:
        """Execute a query."""
        # Simulate database query
        return [{"id": "1", "name": "Example", "query": query_str}]


@asynccontextmanager
async def server_lifespan(_server: Server) -> AsyncIterator[dict[str, Any]]:
    """Manage server startup and shutdown lifecycle."""
    # Initialize resources on startup
    db = await Database.connect()
    try:
        yield {"db": db}
    finally:
        # Clean up on shutdown
        await db.disconnect()


# Pass lifespan to server
server = Server("example-server", lifespan=server_lifespan)


@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """List available tools."""
    return [
        types.Tool(
            name="query_db",
            description="Query the database",
            inputSchema={
                "type": "object",
                "properties": {"query": {"type": "string", "description": "SQL query to execute"}},
                "required": ["query"],
            },
        )
    ]


@server.call_tool()
async def query_db(name: str, arguments: dict[str, Any]) -> list[types.TextContent]:
    """Handle database query tool call."""
    if name != "query_db":
        raise ValueError(f"Unknown tool: {name}")

    # Access lifespan context
    ctx = server.request_context
    db = ctx.lifespan_context["db"]

    # Execute query
    results = await db.query(arguments["query"])

    return [types.TextContent(type="text", text=f"Query results: {results}")]


async def run():
    """Run the server with lifespan management."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="example-server",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

_Full example: [examples/snippets/servers/lowlevel/lifespan.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/lowlevel/lifespan.py)_
<!-- /snippet-source -->

生命周期 API 提供：

- 一种在服务启动时初始化资源并在停止时清理它们的方法
- 通过处理程序中的请求上下文访问已初始化的资源
- 在生命周期和处理程序之间进行类型安全的上下文传递

<!-- snippet-source examples/snippets/servers/lowlevel/basic.py -->
```python
"""
Run from the repository root:
uv run examples/snippets/servers/lowlevel/basic.py
"""

import asyncio

import mcp.server.stdio
import mcp.types as types
from mcp.server.lowlevel import NotificationOptions, Server
from mcp.server.models import InitializationOptions

# Create a server instance
server = Server("example-server")


@server.list_prompts()
async def handle_list_prompts() -> list[types.Prompt]:
    """List available prompts."""
    return [
        types.Prompt(
            name="example-prompt",
            description="An example prompt template",
            arguments=[types.PromptArgument(name="arg1", description="Example argument", required=True)],
        )
    ]


@server.get_prompt()
async def handle_get_prompt(name: str, arguments: dict[str, str] | None) -> types.GetPromptResult:
    """Get a specific prompt by name."""
    if name != "example-prompt":
        raise ValueError(f"Unknown prompt: {name}")

    arg1_value = (arguments or {}).get("arg1", "default")

    return types.GetPromptResult(
        description="Example prompt",
        messages=[
            types.PromptMessage(
                role="user",
                content=types.TextContent(type="text", text=f"Example prompt text with argument: {arg1_value}"),
            )
        ],
    )


async def run():
    """Run the basic low-level server."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="example",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )


if __name__ == "__main__":
    asyncio.run(run())
```

_Full example: [examples/snippets/servers/lowlevel/basic.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/lowlevel/basic.py)_
<!-- /snippet-source -->

注意：`uv run mcp run` 和 `uv run mcp dev` 工具不支持底层服务器。

#### 结构化输出支持

底层服务器支持工具的结构化输出，允许你返回人类可读的内容和机器可读的结构化数据。工具可以定义 `outputSchema` 来验证其结构化输出：

<!-- snippet-source examples/snippets/servers/lowlevel/structured_output.py -->
```python
"""
Run from the repository root:
    uv run examples/snippets/servers/lowlevel/structured_output.py
"""

import asyncio
from typing import Any

import mcp.server.stdio
import mcp.types as types
from mcp.server.lowlevel import NotificationOptions, Server
from mcp.server.models import InitializationOptions

server = Server("example-server")


@server.list_tools()
async def list_tools() -> list[types.Tool]:
    """List available tools with structured output schemas."""
    return [
        types.Tool(
            name="get_weather",
            description="Get current weather for a city",
            inputSchema={
                "type": "object",
                "properties": {"city": {"type": "string", "description": "City name"}},
                "required": ["city"],
            },
            outputSchema={
                "type": "object",
                "properties": {
                    "temperature": {"type": "number", "description": "Temperature in Celsius"},
                    "condition": {"type": "string", "description": "Weather condition"},
                    "humidity": {"type": "number", "description": "Humidity percentage"},
                    "city": {"type": "string", "description": "City name"},
                },
                "required": ["temperature", "condition", "humidity", "city"],
            },
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> dict[str, Any]:
    """Handle tool calls with structured output."""
    if name == "get_weather":
        city = arguments["city"]

        # Simulated weather data - in production, call a weather API
        weather_data = {
            "temperature": 22.5,
            "condition": "partly cloudy",
            "humidity": 65,
            "city": city,  # Include the requested city
        }

        # low-level server will validate structured output against the tool's
        # output schema, and additionally serialize it into a TextContent block
        # for backwards compatibility with pre-2025-06-18 clients.
        return weather_data
    else:
        raise ValueError(f"Unknown tool: {name}")


async def run():
    """Run the structured output server."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="structured-output-example",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )


if __name__ == "__main__":
    asyncio.run(run())
```

_Full example: [examples/snippets/servers/lowlevel/structured_output.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/lowlevel/structured_output.py)_
<!-- /snippet-source -->

工具可以通过四种方式返回数据：

1. **仅内容**：返回内容块列表（规范修订版 2025-06-18 之前的默认行为）
2. **仅结构化数据**：返回将序列化为 JSON 的字典（在规范修订版 2025-06-18 中引入）
3. **两者兼有**：返回 `(内容, 结构化数据)` 元组，这是用于向后兼容的首选选项
4. **直接调用 CallToolResult**：直接返回 `CallToolResult` 以获得完全控制（包括 `_meta` 字段）

当定义了 `outputSchema` 时，服务器会自动根据该 schema 验证结构化输出。这确保了类型安全并有助于尽早捕获错误。

##### 直接返回 CallToolResult

为了完全控制响应（包括 `_meta` 字段，用于向客户端应用程序传递数据而不暴露给模型），请直接返回 `CallToolResult`：

<!-- snippet-source examples/snippets/servers/lowlevel/direct_call_tool_result.py -->
```python
"""
Run from the repository root:
    uv run examples/snippets/servers/lowlevel/direct_call_tool_result.py
"""

import asyncio
from typing import Any

import mcp.server.stdio
import mcp.types as types
from mcp.server.lowlevel import NotificationOptions, Server
from mcp.server.models import InitializationOptions

server = Server("example-server")


@server.list_tools()
async def list_tools() -> list[types.Tool]:
    """List available tools."""
    return [
        types.Tool(
            name="advanced_tool",
            description="Tool with full control including _meta field",
            inputSchema={
                "type": "object",
                "properties": {"message": {"type": "string"}},
                "required": ["message"],
            },
        )
    ]


@server.call_tool()
async def handle_call_tool(name: str, arguments: dict[str, Any]) -> types.CallToolResult:
    """Handle tool calls by returning CallToolResult directly."""
    if name == "advanced_tool":
        message = str(arguments.get("message", ""))
        return types.CallToolResult(
            content=[types.TextContent(type="text", text=f"Processed: {message}")],
            structuredContent={"result": "success", "message": message},
            _meta={"hidden": "data for client applications only"},
        )

    raise ValueError(f"Unknown tool: {name}")


async def run():
    """Run the server."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="example",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )


if __name__ == "__main__":
    asyncio.run(run())
```

_Full example: [examples/snippets/servers/lowlevel/direct_call_tool_result.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/lowlevel/direct_call_tool_result.py)_
<!-- /snippet-source -->

**注意：** 当返回 `CallToolResult` 时，你将绕过自动的内容/结构化转换。你必须自己构造完整的响应。

### 分页（高级）

对于需要处理大型数据集的服务器，底层服务器提供了列表操作的分页版本。这是一种可选优化——除非你的服务器处理数百或数千个项目，否则大多数服务器不需要分页。

#### 服务端实现

<!-- snippet-source examples/snippets/servers/pagination_example.py -->
```python
"""
Example of implementing pagination with MCP server decorators.
"""

from pydantic import AnyUrl

import mcp.types as types
from mcp.server.lowlevel import Server

# Initialize the server
server = Server("paginated-server")

# Sample data to paginate
ITEMS = [f"Item {i}" for i in range(1, 101)]  # 100 items


@server.list_resources()
async def list_resources_paginated(request: types.ListResourcesRequest) -> types.ListResourcesResult:
    """List resources with pagination support."""
    page_size = 10

    # Extract cursor from request params
    cursor = request.params.cursor if request.params is not None else None

    # Parse cursor to get offset
    start = 0 if cursor is None else int(cursor)
    end = start + page_size

    # Get page of resources
    page_items = [
        types.Resource(uri=AnyUrl(f"resource://items/{item}"), name=item, description=f"Description for {item}")
        for item in ITEMS[start:end]
    ]

    # Determine next cursor
    next_cursor = str(end) if end < len(ITEMS) else None

    return types.ListResourcesResult(resources=page_items, nextCursor=next_cursor)
```

_Full example: [examples/snippets/servers/pagination_example.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/pagination_example.py)_
<!-- /snippet-source -->

#### 客户端消费

<!-- snippet-source examples/snippets/clients/pagination_client.py -->
```python
"""
Example of consuming paginated MCP endpoints from a client.
"""

import asyncio

from mcp.client.session import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client
from mcp.types import PaginatedRequestParams, Resource


async def list_all_resources() -> None:
    """Fetch all resources using pagination."""
    async with stdio_client(StdioServerParameters(command="uv", args=["run", "mcp-simple-pagination"])) as (
        read,
        write,
    ):
        async with ClientSession(read, write) as session:
            await session.initialize()

            all_resources: list[Resource] = []
            cursor = None

            while True:
                # Fetch a page of resources
                result = await session.list_resources(params=PaginatedRequestParams(cursor=cursor))
                all_resources.extend(result.resources)

                print(f"Fetched {len(result.resources)} resources")

                # Check if there are more pages
                if result.nextCursor:
                    cursor = result.nextCursor
                else:
                    break

            print(f"Total resources: {len(all_resources)}")


if __name__ == "__main__":
    asyncio.run(list_all_resources())
```

_Full example: [examples/snippets/clients/pagination_client.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/clients/pagination_client.py)_
<!-- /snippet-source -->

#### 关键点

- **游标（Cursors）是不透明的字符串**——服务器定义其格式（数字偏移量、时间戳等）
- **当没有更多页面时返回 `nextCursor=None`**
- **向后兼容**——不支持分页的客户端仍然可以正常工作（它们只会获取第一页）
- **灵活的页面大小**——每个端点可以根据数据特征定义自己的页面大小

有关完整实现，请参阅 [simple-pagination 示例](examples/servers/simple-pagination)。

### 编写 MCP 客户端

SDK 提供了高级客户端接口，用于使用各种 [传输协议](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports) 连接到 MCP 服务器：

<!-- snippet-source examples/snippets/clients/stdio_client.py -->
```python
"""
cd to the `examples/snippets/clients` directory and run:
    uv run client
"""

import asyncio
import os

from pydantic import AnyUrl

from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
from mcp.shared.context import RequestContext

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="uv",  # Using uv to run the server
    args=["run", "server", "fastmcp_quickstart", "stdio"],  # We're already in snippets dir
    env={"UV_INDEX": os.environ.get("UV_INDEX", "")},
)


# Optional: create a sampling callback
async def handle_sampling_message(
    context: RequestContext[ClientSession, None], params: types.CreateMessageRequestParams
) -> types.CreateMessageResult:
    print(f"Sampling request: {params.messages}")
    return types.CreateMessageResult(
        role="assistant",
        content=types.TextContent(
            type="text",
            text="Hello, world! from model",
        ),
        model="gpt-3.5-turbo",
        stopReason="endTurn",
    )


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write, sampling_callback=handle_sampling_message) as session:
            # Initialize the connection
            await session.initialize()

            # List available prompts
            prompts = await session.list_prompts()
            print(f"Available prompts: {[p.name for p in prompts.prompts]}")

            # Get a prompt (greet_user prompt from fastmcp_quickstart)
            if prompts.prompts:
                prompt = await session.get_prompt("greet_user", arguments={"name": "Alice", "style": "friendly"})
                print(f"Prompt result: {prompt.messages[0].content}")

            # List available resources
            resources = await session.list_resources()
            print(f"Available resources: {[r.uri for r in resources.resources]}")

            # List available tools
            tools = await session.list_tools()
            print(f"Available tools: {[t.name for t in tools.tools]}")

            # Read a resource (greeting resource from fastmcp_quickstart)
            resource_content = await session.read_resource(AnyUrl("greeting://World"))
            content_block = resource_content.contents[0]
            if isinstance(content_block, types.TextContent):
                print(f"Resource content: {content_block.text}")

            # Call a tool (add tool from fastmcp_quickstart)
            result = await session.call_tool("add", arguments={"a": 5, "b": 3})
            result_unstructured = result.content[0]
            if isinstance(result_unstructured, types.TextContent):
                print(f"Tool result: {result_unstructured.text}")
            result_structured = result.structuredContent
            print(f"Structured tool result: {result_structured}")


def main():
    """Entry point for the client script."""
    asyncio.run(run())


if __name__ == "__main__":
    main()
```

_Full example: [examples/snippets/clients/stdio_client.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/clients/stdio_client.py)_
<!-- /snippet-source -->

客户端也可以使用 [Streamable HTTP 传输](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http) 进行连接：

<!-- snippet-source examples/snippets/clients/streamable_basic.py -->
```python
"""
Run from the repository root:
    uv run examples/snippets/clients/streamable_basic.py
"""

import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client


async def main():
    # Connect to a streamable HTTP server
    async with streamable_http_client("http://localhost:8000/mcp") as (
        read_stream,
        write_stream,
        _,
    ):
        # Create a session using the client streams
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()
            # List available tools
            tools = await session.list_tools()
            print(f"Available tools: {[tool.name for tool in tools.tools]}")


if __name__ == "__main__":
    asyncio.run(main())
```

_Full example: [examples/snippets/clients/streamable_basic.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/clients/streamable_basic.py)_
<!-- /snippet-source -->

### 客户端显示工具

在构建 MCP 客户端时，SDK 提供了实用程序来帮助显示工具、资源和提示词的人类可读名称：

<!-- snippet-source examples/snippets/clients/display_utilities.py -->
```python
"""
cd to the `examples/snippets` directory and run:
    uv run display-utilities-client
"""

import asyncio
import os

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.shared.metadata_utils import get_display_name

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="uv",  # Using uv to run the server
    args=["run", "server", "fastmcp_quickstart", "stdio"],
    env={"UV_INDEX": os.environ.get("UV_INDEX", "")},
)


async def display_tools(session: ClientSession):
    """Display available tools with human-readable names"""
    tools_response = await session.list_tools()

    for tool in tools_response.tools:
        # get_display_name() returns the title if available, otherwise the name
        display_name = get_display_name(tool)
        print(f"Tool: {display_name}")
        if tool.description:
            print(f"   {tool.description}")


async def display_resources(session: ClientSession):
    """Display available resources with human-readable names"""
    resources_response = await session.list_resources()

    for resource in resources_response.resources:
        display_name = get_display_name(resource)
        print(f"Resource: {display_name} ({resource.uri})")

    templates_response = await session.list_resource_templates()
    for template in templates_response.resourceTemplates:
        display_name = get_display_name(template)
        print(f"Resource Template: {display_name}")


async def run():
    """Run the display utilities example."""
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            print("=== Available Tools ===")
            await display_tools(session)

            print("\n=== Available Resources ===")
            await display_resources(session)


def main():
    """Entry point for the display utilities client."""
    asyncio.run(run())


if __name__ == "__main__":
    main()
```

_Full example: [examples/snippets/clients/display_utilities.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/clients/display_utilities.py)_
<!-- /snippet-source -->

`get_display_name()` 函数实现了显示名称的正确优先级规则：

- 对于工具：`title` > `annotations.title` > `name`
- 对于其他对象：`title` > `name`

这确保你的客户端 UI 显示服务器提供的最用户友好的名称。

### 客户端的 OAuth 身份验证

SDK 包含 [授权支持](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization) 以连接到受保护的 MCP 服务器：

<!-- snippet-source examples/snippets/clients/oauth_client.py -->
```python
"""
Before running, specify running MCP RS server URL.
To spin up RS server locally, see
    examples/servers/simple-auth/README.md

cd to the `examples/snippets` directory and run:
    uv run oauth-client
"""

import asyncio
from urllib.parse import parse_qs, urlparse

import httpx
from pydantic import AnyUrl

from mcp import ClientSession
from mcp.client.auth import OAuthClientProvider, TokenStorage
from mcp.client.streamable_http import streamable_http_client
from mcp.shared.auth import OAuthClientInformationFull, OAuthClientMetadata, OAuthToken


class InMemoryTokenStorage(TokenStorage):
    """Demo In-memory token storage implementation."""

    def __init__(self):
        self.tokens: OAuthToken | None = None
        self.client_info: OAuthClientInformationFull | None = None

    async def get_tokens(self) -> OAuthToken | None:
        """Get stored tokens."""
        return self.tokens

    async def set_tokens(self, tokens: OAuthToken) -> None:
        """Store tokens."""
        self.tokens = tokens

    async def get_client_info(self) -> OAuthClientInformationFull | None:
        """Get stored client information."""
        return self.client_info

    async def set_client_info(self, client_info: OAuthClientInformationFull) -> None:
        """Store client information."""
        self.client_info = client_info


async def handle_redirect(auth_url: str) -> None:
    print(f"Visit: {auth_url}")


async def handle_callback() -> tuple[str, str | None]:
    callback_url = input("Paste callback URL: ")
    params = parse_qs(urlparse(callback_url).query)
    return params["code"][0], params.get("state", [None])[0]


async def main():
    """Run the OAuth client example."""
    oauth_auth = OAuthClientProvider(
        server_url="http://localhost:8001",
        client_metadata=OAuthClientMetadata(
            client_name="Example MCP Client",
            redirect_uris=[AnyUrl("http://localhost:3000/callback")],
            grant_types=["authorization_code", "refresh_token"],
            response_types=["code"],
            scope="user",
        ),
        storage=InMemoryTokenStorage(),
        redirect_handler=handle_redirect,
        callback_handler=handle_callback,
    )

    async with httpx.AsyncClient(auth=oauth_auth, follow_redirects=True) as custom_client:
        async with streamable_http_client("http://localhost:8001/mcp", http_client=custom_client) as (read, write, _):
            async with ClientSession(read, write) as session:
                await session.initialize()

                tools = await session.list_tools()
                print(f"Available tools: {[tool.name for tool in tools.tools]}")

                resources = await session.list_resources()
                print(f"Available resources: {[r.uri for r in resources.resources]}")


def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()
```

_Full example: [examples/snippets/clients/oauth_client.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/clients/oauth_client.py)_
<!-- /snippet-source -->

有关完整的工作示例，请参阅 [`examples/clients/simple-auth-client/`](examples/clients/simple-auth-client/)。

### 解析工具结果

通过 MCP 调用工具时，`CallToolResult` 对象以结构化格式包含工具的响应。了解如何解析此结果对于正确处理工具输出至关重要。

```python
"""examples/snippets/clients/parsing_tool_results.py"""

import asyncio

from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client


async def parse_tool_results():
    """Demonstrates how to parse different types of content in CallToolResult."""
    server_params = StdioServerParameters(
        command="python", args=["path/to/mcp_server.py"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Example 1: Parsing text content
            result = await session.call_tool("get_data", {"format": "text"})
            for content in result.content:
                if isinstance(content, types.TextContent):
                    print(f"Text: {content.text}")

            # Example 2: Parsing structured content from JSON tools
            result = await session.call_tool("get_user", {"id": "123"})
            if hasattr(result, "structuredContent") and result.structuredContent:
                # Access structured data directly
                user_data = result.structuredContent
                print(f"User: {user_data.get('name')}, Age: {user_data.get('age')}")

            # Example 3: Parsing embedded resources
            result = await session.call_tool("read_config", {})
            for content in result.content:
                if isinstance(content, types.EmbeddedResource):
                    resource = content.resource
                    if isinstance(resource, types.TextResourceContents):
                        print(f"Config from {resource.uri}: {resource.text}")
                    elif isinstance(resource, types.BlobResourceContents):
                        print(f"Binary data from {resource.uri}")

            # Example 4: Parsing image content
            result = await session.call_tool("generate_chart", {"data": [1, 2, 3]})
            for content in result.content:
                if isinstance(content, types.ImageContent):
                    print(f"Image ({content.mimeType}): {len(content.data)} bytes")

            # Example 5: Handling errors
            result = await session.call_tool("failing_tool", {})
            if result.isError:
                print("Tool execution failed!")
                for content in result.content:
                    if isinstance(content, types.TextContent):
                        print(f"Error: {content.text}")


async def main():
    await parse_tool_results()


if __name__ == "__main__":
    asyncio.run(main())
```

### MCP 基础原语

MCP 协议定义了服务器可以实现三个核心原语：

| 原语 | 控制权               | 描述                                         | 示例用途                  |
|-----------|-----------------------|-----------------------------------------------------|------------------------------|
| Prompts（提示词）   | 用户控制       | 由用户选择触发的交互式模板        | 斜杠命令、菜单选项 |
| Resources（资源） | 应用控制| 由客户端应用程序管理的上下文数据   | 文件内容、API 响应 |
| Tools（工具）     | 模型控制      | 暴露给大语言模型以采取行动的函数        | API 调用、数据更新      |

### 服务器能力（Server Capabilities）

MCP 服务器在初始化时声明其能力：

| 能力   | 功能标志                 | 描述                        |
|--------------|------------------------------|------------------------------------|
| `prompts`    | `listChanged`                | 提示词模板管理         |
| `resources`  | `subscribe`<br/>`listChanged`| 资源暴露和更新      |
| `tools`      | `listChanged`                | 工具发现和执行       |
| `logging`    | -                            | 服务器日志配置       |
| `completions`| -                            | 参数补全建议    |

## 文档

- [API 参考](https://modelcontextprotocol.github.io/python-sdk/api/)
- [实验性功能（Tasks）](https://modelcontextprotocol.github.io/python-sdk/experimental/tasks/)
- [模型上下文协议文档](https://modelcontextprotocol.io)
- [模型上下文协议规范](https://modelcontextprotocol.io/specification/latest)
- [官方支持的服务器](https://github.com/modelcontextprotocol/servers)

## 贡献指南

我们热衷于支持不同经验水平的贡献者，并非常希望看到你参与到项目中来。请参阅 [贡献指南](CONTRIBUTING.md) 以开始你的贡献之旅。

## 许可证

本项目采用 MIT License 许可——详情请参阅 LICENSE 文件。