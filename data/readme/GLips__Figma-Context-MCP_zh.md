<a href="https://www.framelink.ai/?utm_source=github&utm_medium=referral&utm_campaign=readme" target="_blank" rel="noopener">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://www.framelink.ai/github/HeaderDark.png" />
    <img alt="Framelink" src="https://www.framelink.ai/github/HeaderLight.png" />
  </picture>
</a>

<div align="center">
  <h1>Framelink MCP for Figma</h1>
  <h3>让你的编程代理访问你的 Figma 数据。<br/>一键在任何框架中实现设计稿。</h3>
  <a href="https://npmcharts.com/compare/figma-developer-mcp?interval=30">
    <img alt="weekly downloads" src="https://img.shields.io/npm/dm/figma-developer-mcp.svg">
  </a>
  <a href="https://github.com/GLips/Figma-Context-MCP/blob/main/LICENSE">
    <img alt="MIT License" src="https://img.shields.io/github/license/GLips/Figma-Context-MCP" />
  </a>
  <a href="https://framelink.ai/discord">
    <img alt="Discord" src="https://img.shields.io/discord/1352337336913887343?color=7389D8&label&logo=discord&logoColor=ffffff" />
  </a>
  <br />
  <a href="https://twitter.com/glipsman">
    <img alt="Twitter" src="https://img.shields.io/twitter/url?url=https%3A%2F%2Fx.com%2Fglipsman&label=%40glipsman" />
  </a>
</div>

<br/>

通过此 [模型上下文协议（Model Context Protocol）](https://modelcontextprotocol.io/introduction) 服务器，让 [Cursor](https://cursor.sh/) 及其他 AI 编程工具访问你的 Figma 文件。

当 Cursor 能够获取 Figma 设计数据时，它在一次性准确实现设计稿的能力上远超粘贴截图等传统方法。

<h3><a href="https://www.framelink.ai/docs/quickstart?utm_source=github&utm_medium=referral&utm_campaign=readme">查看快速入门指南 →</a></h3>

## 演示

[观看在 Cursor 中使用 Figma 设计数据构建 UI 的演示视频](https://youtu.be/6G9yb-LrEqg)

[![Watch the video](https://img.youtube.com/vi/6G9yb-LrEqg/maxresdefault.jpg)](https://youtu.be/6G9yb-LrEqg)

## 工作原理

1. 打开你的 IDE 聊天窗口（例如 Cursor 中的 Agent 模式）。
2. 粘贴 Figma 文件、画框或组合的链接。
3. 让 Cursor 对 Figma 文件执行操作——例如实现该设计。
4. Cursor 将从 Figma 获取相关元数据，并据此编写代码。

该 MCP 服务器专为与 Cursor 配合使用而设计。在向模型提供来自 [Figma API](https://www.figma.com/developers/api) 的上下文之前，它会先简化并转换响应内容，确保仅向模型提供最相关的布局和样式信息。

减少提供给模型的上下文量有助于提高 AI 的准确度，并使生成的回复更具相关性。

## 快速开始

许多代码编辑器及其他 AI 客户端使用配置文件来管理 MCP 服务器。

你可以通过在配置文件中添加以下内容来配置 `figma-developer-mcp` 服务器。

> **注意**：你需要创建一个 Figma 访问令牌才能使用此服务器。创建 Figma API 访问令牌的说明请参见[此处](https://help.figma.com/hc/en-us/articles/8085703771159-Manage-personal-access-tokens)。

### macOS / Linux

```json
{
  "mcpServers": {
    "Framelink MCP for Figma": {
      "command": "npx",
      "args": ["-y", "figma-developer-mcp", "--figma-api-key=YOUR-KEY", "--stdio"]
    }
  }
}
```

### Windows

```json
{
  "mcpServers": {
    "Framelink MCP for Figma": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "figma-developer-mcp", "--figma-api-key=YOUR-KEY", "--stdio"]
    }
  }
}
```

或者，你也可以在 `env` 字段中设置 `FIGMA_API_KEY` 和 `PORT`。

如需了解如何配置 Framelink MCP for Figma 的更多信息，请参阅 [Framelink 文档](https://www.framelink.ai/docs/quickstart?utm_source=github&utm_medium=referral&utm_campaign=readme)。

## Star 历史记录

<a href="https://star-history.com/#GLips/Figma-Context-MCP"><img src="https://api.star-history.com/svg?repos=GLips/Figma-Context-MCP&type=Date" alt="Star History Chart" width="600" /></a>

## 了解更多

Framelink MCP for Figma 简洁而强大。前往 [Framelink](https://framelink.ai?utm_source=github&utm_medium=referral&utm_campaign=readme) 网站了解更多，以充分发挥其作用。