<div align="center">
<div align="center">
  <a href="https://mcp-use.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="./static/logo_white.svg">
      <source media="(prefers-color-scheme: light)" srcset="./static/logo_black.svg">
      <img alt="mcp use logo" src="./static/logo_black.svg" width="60%" >
    </picture>
  </a>
</div>
&nbsp;

<p align="center">
    <a href="https://mcp-use.com/docs" alt="文档">
        <img src="https://img.shields.io/badge/mcp--use-docs-blue?labelColor=white" /></a>
    <a href="https://manufact.com" alt="官网">
        <img src="https://img.shields.io/badge/made by-manufact.com-blue" /></a>
    <a href="https://github.com/mcp-use/mcp-use/blob/main/LICENSE" alt="许可证">
        <img src="https://img.shields.io/github/license/mcp-use/mcp-use" /></a>
    <a href="https://discord.gg/XkNkSkMz3V" alt="Discord 社区">
        <img src="https://dcbadge.limes.pink/api/server/XkNkSkMz3V?style=flat" /></a>
    <br/>
    <a href="https://mcp-use.com/docs/python" alt="Python 文档">
        <img src="https://img.shields.io/badge/python-docs-blue?labelColor=white&logo=python" alt="Badge"></a>
    <a href="https://pypi.org/project/mcp_use/" alt="PyPI 版本">
        <img src="https://img.shields.io/pypi/v/mcp_use.svg"/></a>
    <a href="https://pypi.org/project/mcp_use/" alt="PyPI 下载量">
        <img src="https://static.pepy.tech/badge/mcp-use" /></a>
    <br/>
    <a href="https://mcp-use.com/docs/typescript" alt="TypeScript 文档">
        <img src="https://img.shields.io/badge/typescript-docs-blue?labelColor=white&logo=typescript" alt="Badge"></a>
    <a href="https://www.npmjs.com/package/mcp-use" alt="NPM 版本">
        <img src="https://img.shields.io/npm/v/mcp-use.svg"/></a>
    <a href="https://www.npmjs.com/package/mcp-use" alt="NPM 下载量">
        <img src="https://img.shields.io/npm/dw/mcp-use.svg"/></a>
    <br/>
</p>
</div>

## 简介

<b>mcp-use</b> 是一个全栈 MCP（Model Context Protocol）框架，用于为 ChatGPT/Claude 构建 MCP App，并为 AI Agent 构建 MCP Server。

- **开发**：使用 mcp-use SDK ([ts](https://www.npmjs.com/package/mcp-use) | [py](https://pypi.org/project/mcp_use/)) 构建 MCP Servers 和 MCP Apps
- **预览**：通过 mcp-use MCP Inspector（[在线版](https://inspector.mcp-use.com/inspector) | [开源版](https://github.com/mcp-use/mcp-use/tree/main/libraries/typescript/packages/inspector)）测试和调试你的 MCP Servers 与 Apps
- **部署**：在 [Manufact MCP Cloud](https://manufact.com) 上发布：连接 GitHub 仓库，一键将 MCP Server 和 App 投入生产环境，内置可观测性、指标监控、日志记录、分支部署等功能

## 文档

访问我们的 [文档](https://mcp-use.com/docs)，或直接跳转至快速入门指南（[TypeScript](https://mcp-use.com/docs/typescript/getting-started/quickstart) | [Python](https://mcp-use.com/docs/python/getgetting-started/quickstart)）

### 编程 Agent 技能

> **正在使用 Claude Code、Codex、Cursor 或其他 AI 编程 Agent？**
>
> **[安装 mcp-use MCP App 构建技能](https://skills.sh/mcp-use/mcp-use/mcp-apps-builder)**

## 快速入门：MCP Servers 与 MCP Apps

### <img src="./static/typescript.svg" height="14" style="margin-right:4px; top:-1px; position:relative;" align="center" /> TypeScript

构建你的第一个 MCP Server 或 MCP App：

```bash
npx create-mcp-use-app@latest
```

或手动创建 Server：

```typescript
import { MCPServer, text } from "mcp-use/server";
import { z } from "zod";

const server = new MCPServer({
  name: "my-server",
  version: "1.0.0",
});

server.tool({
  name: "get_weather",
  description: "Get weather for a city",
  schema: z.object({ city: z.string() }),
}, async ({ city }) => {
  return text(`Temperature: 72°F, Condition: sunny, City: ${city}`);
});

await server.listen(3000);
// Inspector at http://localhost:3000/inspector
```

[**→ 完整 TypeScript Server 文档**](https://mcp-use.com/docs/typescript/server)

## MCP Apps

MCP App 让你能够构建跨 Claude、ChatGPT 及其他 MCP 客户端运行的交互式组件 —— 一次编写，处处运行。

**Server**：定义一个 tool 并指向对应的 widget：

```typescript
import { MCPServer, widget } from "mcp-use/server";
import { z } from "zod";

const server = new MCPServer({
  name: "weather-app",
  version: "1.0.0",
});

server.tool({
  name: "get-weather",
  description: "Get weather for a city",
  schema: z.object({ city: z.string() }),
  widget: "weather-display", // references resources/weather-display/widget.tsx
}, async ({ city }) => {
  return widget({
    props: { city, temperature: 22, conditions: "Sunny" },
    message: `Weather in ${city}: Sunny, 22°C`,
  });
});

await server.listen(3000);
```

**Widget**：在 `resources/weather-display/widget.tsx` 中创建 React 组件：

```tsx
import { useWidget, type WidgetMetadata } from "mcp-use/react";
import { z } from "zod";

const propSchema = z.object({
  city: z.string(),
  temperature: z.number(),
  conditions: z.string(),
});

export const widgetMetadata: WidgetMetadata = {
  description: "Display weather information",
  props: propSchema,
};

const WeatherDisplay: React.FC = () => {
  const { props, isPending, theme } = useWidget<z.infer<typeof propSchema>>();
  const isDark = theme === "dark";

  if (isPending) return <div>Loading...</div>;

  return (
    <div style={{
      background: isDark ? "#1a1a2e" : "#f0f4ff",
      borderRadius: 16, padding: 24,
    }}>
      <h2>{props.city}</h2>
      <p>{props.temperature}° — {props.conditions}</p>
    </div>
  );
};

export default WeatherDisplay;
```

`resources/` 目录下的 Widgets **支持自动发现** —— 无需手动注册。

访问 [**MCP Apps 文档**](https://mcp-use.com/docs/typescript/server/mcp-apps)

## 模板

开箱即用的 MCP App，支持一键部署或 Fork 为你自己的项目。

| 预览 | 名称 | 工具 | 演示链接 | 仓库 | 部署 |
| --- | --- | --- | --- | --- | --- |
| ![Chart Builder](https://raw.githubusercontent.com/mcp-use/mcp-chart-builder/main/repo-assets/demo.gif) | Chart Builder（图表构建器） | `create-chart` | [打开 URL](https://yellow-shadow-21833.run.mcp-use.com/mcp) | [mcp-use/mcp-chart-builder](https://github.com/mcp-use/mcp-chart-builder) | [![Deploy to mcp-use](https://cdn.mcp-use.com/deploy.svg)](https://mcp-use.com/deploy/start?repository-url=https%3A%2F%2Fgithub.com%2Fmcp-use%2Fmcp-chart-builder&branch=main&project-name=mcp-chart-builder&port=3000&runtime=node&base-image=node%3A20) |
| ![Diagram Builder](https://raw.githubusercontent.com/mcp-use/mcp-diagram-builder/main/repo-assets/demo.gif) | Diagram Builder（图表绘制器） | `create-diagram`, `edit-diagram` | [打开 URL](https://lucky-darkness-402ph.run.mcp-use.com/mcp) | [mcp-use/mcp-diagram-builder](https://github.com/mcp-use/mcp-diagram-builder) | [![Deploy to mcp-use](https://cdn.mcp-use.com/deploy.svg)](https://mcp-use.com/deploy/start?repository-url=https%3A%2F%2Fgithub.com%2Fmcp-use%2Fmcp-diagram-builder&branch=main&project-name=mcp-diagram-builder&port=3000&runtime=node&base-image=node%3A20) |
| ![Slide Deck](https://raw.githubusercontent.com/mcp-use/mcp-slide-deck/main/repo-assets/demo.gif) | Slide Deck（幻灯片） | `create-slides`, `edit-slide` | [打开 URL](https://solitary-block-r6m6x.run.mcp-use.com/mcp) | [mcp-use/mcp-slide-deck](https://github.com/mcp-use/mcp-slide-deck) | [![Deploy to mcp-use](https://cdn.mcp-use.com/deploy.svg)](https://mcp-use.com/deploy/start?repository-url=https%3A%2F%2Fgithub.com%2Fmcp-use%2Fmcp-slide-deck&branch=main&project-name=mcp-slide-deck&port=3000&runtime=node&base-image=node%3A20) |
| ![Maps Explorer](https://raw.githubusercontent.com/mcp-use/mcp-maps-explorer/main/repo-assets/demo.gif) | Maps Explorer（地图探索器） | `show-map`, `get-place-details`, `add-markers` | [打开 URL](https://super-night-ttde2.run.mcp-use.com/mcp) | [mcp-use/mcp-maps-explorer](https://github.com/mcp-use/mcp-maps-explorer) | [![Deploy to mcp-use](https://cdn.mcp-use.com/deploy.svg)](https://mcp-use.com/deploy/start?repository-url=https%3A%2F%2Fgithub.com%2Fmcp-use%2Fmcp-maps-explorer&branch=main&project-name=mcp-maps-explorer&port=3000&runtime=node&base-image=node%3A20) |
| ![Hugging Face Spaces](https://raw.githubusercontent.com/mcp-use/mcp-huggingface-spaces/main/repo-assets/demo.gif) | Hugging Face Spaces（空间管理） | `search-spaces`, `show-space`, `trending-spaces` | [打开 URL](https://gentle-frost-pvxpk.run.mcp-use.com/mcp) | [mcp-use/mcp-huggingface-spaces](https://github.com/mcp-use/mcp-huggingface-spaces) | [![Deploy to mcp-use](https://cdn.mcp-use.com/deploy.svg)](https://mcp-use.com/deploy/start?repository-url=https%3A%2F%2Fgithub.com%2Fmcp-use%2Fmcp-huggingface-spaces&branch=main&project-name=mcp-huggingface-spaces&port=3000&runtime=node&base-image=node%3A20) |
| ![Recipe Finder](https://raw.githubusercontent.com/mcp-use/mcp-recipe-finder/main/repo-assets/demo.gif) | Recipe Finder（食谱查找） | `search-recipes`, `get-recipe`, `meal-plan`, `recipe-suggestion` | [打开 URL](https://bold-tree-1fe79.run.mcp-use.com/mcp) | [mcp-use/mcp-recipe-finder](https://github.com/mcp-use/mcp-recipe-finder) | [![Deploy to mcp-use](https://cdn.mcp-use.com/deploy.svg)](https://mcp-use.com/deploy/start?repository-url=https%3A%2F%2Fgithub.com%2Fmcp-use%2Fmcp-recipe-finder&branch=main&project-name=mcp-recipe-finder&port=3000&runtime=node&base-image=node%3A20) |
| ![Widget Gallery](https://raw.githubusercontent.com/mcp-use/mcp-widget-gallery/main/repo-assets/demo.gif) | Widget Gallery（组件画廊） | `show-react-widget`, `html-greeting`, `mcp-ui-poll`, `programmatic-counter`, `detect-client` | [打开 URL](https://wandering-lake-mmxhs.run.mcp-use.com/mcp) | [mcp-use/mcp-widget-gallery](https://github.com/mcp-use/mcp-widget-gallery) | [![Deploy to mcp-use](https://cdn.mcp-use.com/deploy.svg)](https://mcp-use.com/deploy/start?repository-url=https%3A%2F%2Fgithub.com%2Fmcp-use%2Fmcp-widget-gallery&branch=main&project-name=mcp-widget-gallery&port=3000&runtime=node&base-image=node%3A20) |
| ![Multi Server Hub](https://raw.githubusercontent.com/mcp-use/mcp-multi-server-hub/main/repo-assets/demo.gif) | Multi Server Hub（多服务枢纽） | `hub-status`, `hub-config-example`, `audit-log` | [打开 URL](https://soft-voice-4nxfi.run.mcp-use.com/mcp) | [mcp-use/mcp-multi-server-hub](https://github.com/mcp-use/mcp-multi-server-hub) | [![Deploy to mcp-use](https://cdn.mcp-use.com/deploy.svg)](https://mcp-use.com/deploy/start?repository-url=https%3A%2F%2Fgithub.com%2Fmcp-use%2Fmcp-multi-server-hub&branch=main&project-name=mcp-multi-server-hub&port=3000&runtime=node&base-image=node%3A20) |
| ![File Manager](https://raw.githubusercontent.com/mcp-use/mcp-file-manager/main/repo-assets/demo.gif) | File Manager（文件管理器） | `open-vault`, `get-file`, `list-files` | [打开 URL](https://muddy-pond-eyays.run.mcp-use.com/mcp) | [mcp-use/mcp-file-manager](https://github.com/mcp-use/mcp-file-manager) | [![Deploy to mcp-use](https://cdn.mcp-use.com/deploy.svg)](https://mcp-use.com/deploy/start?repository-url=https%3A%2F%2Fgithub.com%2Fmcp-use%2Fmcp-file-manager&branch=main&project-name=mcp-file-manager&port=3000&runtime=node&base-image=node%3A20) |
| ![Progress Demo](https://raw.githubusercontent.com/mcp-use/mcp-progress-demo/main/repo-assets/demo.gif) | Progress Demo（进度演示） | `process-data`, `fetch-report`, `delete-dataset`, `search-external`, `failing-tool` | [打开 URL](https://crimson-river-pzsz1.run.mcp-use.com/mcp) | [mcp-use/mcp-progress-demo](https://github.com/mcp-use/mcp-progress-demo) | [![Deploy to mcp-use](https://cdn.mcp-use.com/deploy.svg)](https://mcp-use.com/deploy/start?repository-url=https%3A%2F%2Fgithub.com%2Fmcp-use%2Fmcp-progress-demo&branch=main&project-name=mcp-progress-demo&port=3000&runtime=node&base-image=node%3A20) |
| ![i18n Adaptive](https://raw.githubusercontent.com/mcp-use/mcp-i18n-adaptive/main/repo-assets/demo.gif) | i18n Adaptive（国际化自适应） | `show-context`, `detect-caller` | [打开 URL](https://falling-grass-58yov.run.mcp-use.com/mcp) | [mcp-use/mcp-i18n-adaptive](https://github.com/mcp-use/mcp-i18n-adaptive) | [![Deploy to mcp-use](https://cdn.mcp-use.com/deploy.svg)](https://mcp-use.com/deploy/start?repository-url=https%3A%2F%2Fgithub.com%2Fmcp-use%2Fmcp-i18n-adaptive&branch=main&project-name=mcp-i18n-adaptive&port=3000&runtime=node&base-image=node%3A20) |
| ![Media Mixer](https://raw.githubusercontent.com/mcp-use/mcp-media-mixer/main/repo-assets/demo.gif) | Media Mixer（媒体混排器） | `generate-image`, `generate-audio`, `generate-pdf`, `get-report`, `get-html-snippet`, `get-xml-config`, `get-stylesheet`, `get-script`, `get-data-array` | [打开 URL](https://wandering-breeze-nuipu.run.mcp-use.com/mcp) | [mcp-use/mcp-media-mixer](https://github.com/mcp-use/mcp-media-mixer) | [![Deploy to mcp-use](https://cdn.mcp-use.com/deploy.svg)](https://mcp-use.com/deploy/start?repository-url=https%3A%2F%2Fgithub.com%2Fmcp-use%2Fmcp-media-mixer&branch=main&project-name=mcp-media-mixer&port=3000&runtime=node&base-image=node%3A20) |
| ![Resource Watcher](https://raw.githubusercontent.com/mcp-use/mcp-resource-watcher/main/repo-assets/demo.gif) | Resource Watcher（资源监听器） | `show-config`, `update-config`, `toggle-feature`, `list-roots` | [打开 URL](https://fragrant-term-zmdks.run.mcp-use.com/mcp) | [mcp-use/mcp-resource-watcher](https://github.com/mcp-use/mcp-resource-watcher) | [![Deploy to mcp-use](https://cdn.mcp-use.com/deploy.svg)](https://mcp-use.com/deploy/start?repository-url=https%3A%2F%2Fgithub.com%2Fmcp-use%2Fmcp-resource-watcher&branch=main&project-name=mcp-resource-watcher&port=3000&runtime=node&base-image=node%3A20) |

---
### <img src="./static/python.svg" height="14" style="margin-right:4px; top:-1px; position:relative;" align="center" /> Python

```bash
pip install mcp-use
```

```python
from typing import Annotated

from mcp.types import ToolAnnotations
from pydantic import Field

from mcp_use import MCPServer

server = MCPServer(name="Weather Server", version="1.0.0")

@server.tool(
    name="get_weather",
    description="Get current weather information for a location",
    annotations=ToolAnnotations(readOnlyHint=True, openWorldHint=True),
)
async def get_weather(
    city: Annotated[str, Field(description="City name")],
) -> str:
    return f"Temperature: 72°F, Condition: sunny, City: {city}"

# Start server with auto-inspector
server.run(transport="streamable-http", port=8000)
# 🎉 Inspector at http://localhost:8000/inspector
```

[**→ 完整 Python Server 文档**](https://mcp-use.com/docs/python/server/index)

---

## Inspector（调试器）

mcp-use Inspector 让你可以交互式地测试和调试 MCP Servers。

**自动集成**：使用 `server.listen()` 时默认包含：

```typescript
server.listen(3000);
// Inspector at http://localhost:3000/inspector
```

**在线版**：连接托管的 MCP Server 时使用：
<br>
>访问 https://inspector.mcp-use.com

**独立运行**：调试任意 MCP Server：

```bash
npx @mcp-use/inspector --url http://localhost:3000/mcp
```

访问 [**Inspector 文档**](https://mcp-use.com/docs/inspector/index)

---

## 部署

将你的 MCP Server 部署至生产环境：

```bash
npx @mcp-use/cli login
npx @mcp-use/cli deploy
```

或在 [manufact.com](https://manufact.com) 连接 GitHub 仓库 —— 开箱即用的生产级环境，内置可观测性、指标监控、日志记录及分支部署功能。

---

## 包概览

本 Monorepo 包含 Python 和 TypeScript 两个生态的多个包：

### Python Packages

| Package     | Description                           | Version                                                                                 |
| ----------- | ------------------------------------- | --------------------------------------------------------------------------------------- |
| **mcp-use** | Complete MCP server and MCP agent SDK | [![PyPI](https://img.shields.io/pypi/v/mcp_use.svg)](https://pypi.org/project/mcp_use/) |

### TypeScript Packages

| Package                | Description                                     | Version                                                                                                         |
| ---------------------- | ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **mcp-use**            | Core framework for MCP servers, MCP apps, and MCP agents | [![npm](https://img.shields.io/npm/v/mcp-use.svg)](https://www.npmjs.com/package/mcp-use)                       |
| **@mcp-use/cli**       | Build tool with hot reload and auto-inspector   | [![npm](https://img.shields.io/npm/v/@mcp-use/cli.svg)](https://www.npmjs.com/package/@mcp-use/cli)             |
| **@mcp-use/inspector** | Web-based previewer and debugger for MCP servers              | [![npm](https://img.shields.io/npm/v/@mcp-use/inspector.svg)](https://www.npmjs.com/package/@mcp-use/inspector) |
| **create-mcp-use-app** | Project scaffolding tool                        | [![npm](https://img.shields.io/npm/v/create-mcp-use-app.svg)](https://www.npmjs.com/package/create-mcp-use-app) |

---

## 扩展：MCP Agent & Client

mcp-use 同时提供了完整的 MCP Agent（智能体）与 Client（客户端）实现。

<details>
<summary>构建 AI Agent</summary>

### <img src="./static/python.svg" height="14" style="margin-right:4px; top:-1px; position:relative;" align="center" /> Python

```bash
pip install mcp-use langchain-openai
```

```python
import asyncio
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient

async def main():
    config = {
        "mcpServers": {
            "filesystem": {
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"]
            }
        }
    }

    client = MCPClient.from_dict(config)
    llm = ChatOpenAI(model="gpt-4o")
    agent = MCPAgent(llm=llm, client=client)

    result = await agent.run("List all files in the directory")
    print(result)

asyncio.run(main())
```

[**→ 完整 Python Agent 文档**](./libraries/python/README.md#quick-start)

### <img src="./static/typescript.svg" height="14" style="margin-right:4px; top:-1px; position:relative;" align="center" /> TypeScript

```bash
npm install mcp-use @langchain/openai
```

```typescript
import { ChatOpenAI } from "@langchain/openai";
import { MCPAgent, MCPClient } from "mcp-use";

async function main() {
  const config = {
    mcpServers: {
      filesystem: {
        command: "npx",
        args: ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"],
      },
    },
  };

  const client = MCPClient.fromDict(config);
  const llm = new ChatOpenAI({ modelName: "gpt-4o" });
  const agent = new MCPAgent({ llm, client });

  const result = await agent.run("List all files in the directory");
  console.log(result);
}

main();
```

[**→ 完整 TypeScript Agent 文档**](./libraries/typescript/README.md#-quick-start)

</details>

<details>
<summary>使用 MCP Client</summary>

### <img src="./static/python.svg" height="14" style="margin-right:4px; top:-1px; position:relative;" align="center" /> Python

```python
import asyncio
from mcp_use import MCPClient

async def main():
    config = {
        "mcpServers": {
            "calculator": {
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-everything"]
            }
        }
    }

    client = MCPClient.from_dict(config)
    await client.create_all_sessions()

    session = client.get_session("calculator")
    result = await session.call_tool(name="add", arguments={"a": 5, "b": 3})

    print(f"Result: {result.content[0].text}")
    await client.close_all_sessions()

asyncio.run(main())
```

[**→ Python Client 文档**](./libraries/python/README.md#direct-tool-calls-without-llm)

### <img src="./static/typescript.svg" height="14" style="margin-right:4px; top:-1px; position:relative;" align="center" /> TypeScript

```typescript
import { MCPClient } from "mcp-use";

async function main() {
  const config = {
    mcpServers: {
      calculator: {
        command: "npx",
        args: ["-y", "@modelcontextprotocol/server-everything"],
      },
    },
  };

  const client = new MCPClient(config);
  await client.createAllSessions();

  const session = client.getSession("calculator");
  const result = await session.callTool("add", { a: 5, b: 3 });

  console.log(`Result: ${result.content[0].text}`);
  await client.closeAllSessions();
}

main();
```

[**→ TypeScript Client 文档**](./libraries/typescript/README.md#basic-usage)

</details>

---

## Model Context Protocol 兼容性验证

<div align="center">
    <a href="https://github.com/mcp-use/mcp-use/actions/workflows/conformance.yml" alt="Python MCP Conformance">
        <img src="https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/tonxxd/6edf670f0446dc9f7a1f32d6bfda2b70/raw/python-conformance.json" /></a>
    <a href="https://github.com/mcp-use/mcp-use/actions/workflows/conformance.yml" alt="Python MCP Client Conformance">
        <img src="https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/tonxxd/6edf670f0446dc9f7a1f32d6bfda2b70/raw/python-client-conformance.json" /></a>
    <a href="https://github.com/mcp-use/mcp-use/actions/workflows/conformance.yml" alt="TypeScript MCP Conformance">
        <img src="https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/tonxxd/6edf670f0446dc9f7a1f32d6bfda2b70/raw/typescript-conformance.json" /></a>
    <a href="https://github.com/mcp-use/mcp-use/actions/workflows/conformance.yml" alt="TypeScript MCP Client Conformance">
      <img src="https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/tonxxd/6edf670f0446dc9f7a1f32d6bfda2b70/raw/typescript-node-client-conformance.json" /></a>
</div>

---

## 安全策略
详见 [SECURITY.md](https://github.com/mcp-use/mcp-use/blob/main/SECURITY.md)

## 社区与支持

- **Discord**：[加入我们的社区](https://discord.gg/XkNkSkMz3V)
- **GitHub Issues**：[报告 Bug 或提交功能建议](https://github.com/mcp-use/mcp-use/issues)
- **文档中心**：[mcp-use.com/docs](https://mcp-use.com/docs)
- **官方网站**：[manufact.com](https://manufact.com)
- **X (Twitter)**：关注 [Manufact](https://x.com/manufact)
- **贡献指南**：详见 [CONTRIBUTING.md](https://github.com/mcp-use/mcp-use/blob/main/CONTRIBUTING.md)
- **开源协议**：MIT © [MCP-Use Contributors](https://github.com/mcp-use/mcp-use/graphs/contributors)

---

## Star 增长历史

[![Star History Chart](https://api.star-history.com/svg?repos=mcp-use/mcp-use&type=Date)](https://www.star-history.com/#mcp-use/mcp-use&Date)

---

## 贡献者

感谢所有精彩的贡献者们！

### 核心成员

1. **Pietro** ([@pietrozullo](https://github.com/pietrozullo))
2. **Luigi** ([@pederzh](https://github.com/pederzh))
3. **Enrico** ([@tonxxd](https://github.com/tonxxd))

<br>

<a href="https://github.com/mcp-use/mcp-use/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=mcp-use/mcp-use" />
</a>

---

<div align="center">
  <strong>Built with ❤️ by Manufact team and the mcp-use community</strong>
  <br/>
  <sub>San Francisco | Zürich</sub>
</div>