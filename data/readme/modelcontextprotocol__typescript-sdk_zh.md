# MCP TypeScript SDK

<!-- prettier-ignore -->
> [!IMPORTANT]
> **这是 `main` 分支，包含 SDK 的 v2 版本（目前处于开发阶段，为预 Alpha 版）。**
>
> 我们预计将在 2026 年第三季度发布稳定的 v2 版本，并同步推出[更新后的 MCP 规范](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)。在此之前，**v1.x 仍是生产环境的推荐版本**。在 v2 正式发布后至少 6 个月内，v1.x 将继续接收错误修复和安全更新，以便你有充足时间进行升级。
>
> v1 文档请参阅 [V1 API 文档](https://ts.sdk.modelcontextprotocol.io/)。v2 API 文档请参阅 [`/v2/`](https://ts.sdk.modelcontextprotocol.io/v2/)。

<!-- prettier-ignore -->
> [!WARNING]
> **由于正在实施[新规范](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)的相关工作，为管理审查者容量，我们暂时仅接受贡献者的 PR。**
>
> 请继续提交 Issue 作为主要反馈渠道。我们预计在新规范稳定发布后将重新开放（新规范目前计划于 2026 年 7 月 28 日发布）。

[![NPM Version - Server](https://img.shields.io/npm/v/%40modelcontextprotocol%2Fserver?label=%40modelcontextprotocol%2Fserver)](https://www.npmjs.com/package/@modelcontextprotocol/server)
[![NPM Version - Client](https://img.shields.io/npm/v/%40modelcontextprotocol%2Fclient?label=%40modelcontextprotocol%2Fclient)](https://www.npmjs.com/package/@modelcontextprotocol/client) ![MIT licensed](https://img.shields.io/npm/l/%40modelcontextprotocol%2Fserver)

<details>
<summary>目录</summary>

- [概述](#overview)
- [软件包](#packages)
- [安装](#installation)
- [快速开始](#getting-started)
- [文档](#documentation)
- [贡献指南](#contributing)
- [许可证](#license)

</details>

## 概述

Model Context Protocol（MCP）允许应用程序以标准化的方式为大语言模型（LLM）提供上下文，将提供上下文的职责与实际的大语言模型交互分离开来。

本仓库包含了 MCP 规范的 TypeScript SDK 实现。它可在 **Node.js**、**Bun** 和 **Deno** 上运行，并提供：
- MCP **服务端**库（工具/资源/提示词、Streamable HTTP、stdio、认证辅助）
- MCP **客户端**库（传输层、高级辅助函数、OAuth 辅助）
- 针对特定运行时/框架的可选 **中间件包**（Express、Hono、Node.js HTTP）
- 可运行的 **示例代码**（位于 [`examples/`](https://github.com/modelcontextprotocol/typescript-sdk/tree/main/examples) 目录下）

## 软件包

此单体仓库发布分拆的软件包：
- **`@modelcontextprotocol/server`**：构建 MCP 服务端
- **`@modelcontextprotocol/client`**：构建 MCP 客户端

工具与提示词（prompt）Schema 使用 [Standard Schema](https://standardschema.dev/) —— 支持 Zod v4、Valibot、ArkType 或任何兼容库。

### 中间件软件包（可选）

该 SDK 还在 [`packages/middleware/`](https://github.com/modelcontextprotocol/typescript-sdk/tree/main/packages/middleware) 下发布了轻量级的“中间件”软件包，帮助你**将 MCP 接入特定的运行时或 Web 框架**。

这些适配器设计得尽可能精简：不应引入新的 MCP 功能或业务逻辑。详情请参阅 [`packages/middleware/README.md`](packages/middleware/README.md)。
- **`@modelcontextprotocol/node`**：用于 `IncomingMessage` / `ServerResponse` 的 Node.js Streamable HTTP 传输层封装
- **`@modelcontextprotocol/express`**：Express 辅助工具（应用默认配置 + Host 头验证）
- **`@modelcontextprotocol/hono`**：Hono 辅助工具（应用默认配置 + JSON 请求体解析钩子 + Host 头验证）

## 安装

### 服务端

```bash
npm install @modelcontextprotocol/server
# or
bun add @modelcontextprotocol/server
# or
deno add npm:@modelcontextprotocol/server
```

### 客户端

```bash
npm install @modelcontextprotocol/client
# or
bun add @modelcontextprotocol/client
# or
deno add npm:@modelcontextprotocol/client
```

### 可选中间件软件包

该 SDK 还发布了可选的“中间件”软件包，帮助你**将 MCP 接入特定的运行时或 Web 框架**（例如 Express、Hono 或 Node.js `http`）。

这些软件包是轻量级适配器，不应引入额外的 MCP 功能或业务逻辑。详情请参阅 [`packages/middleware/README.md`](packages/middleware/README.md)。

```bash
# Node.js HTTP (IncomingMessage/ServerResponse) Streamable HTTP 传输层：
npm install @modelcontextprotocol/node

# Express 集成：
npm install @modelcontextprotocol/express express

# Hono 集成：
npm install @modelcontextprotocol/hono hono
```

## 快速开始

以下是一个 MCP 服务端的示例。这个最小化示例通过 stdio 暴露了一个名为 `greet` 的工具：

```typescript
import { McpServer } from '@modelcontextprotocol/server';
import { StdioServerTransport } from '@modelcontextprotocol/server/stdio';
import * as z from 'zod/v4';

const server = new McpServer({ name: 'greeting-server', version: '1.0.0' });

server.registerTool(
    'greet',
    {
        description: 'Greet someone by name',
        inputSchema: z.object({ name: z.string() })
    },
    async ({ name }) => ({
        content: [{ type: 'text', text: `Hello, ${name}!` }]
    })
);

async function main() {
    const transport = new StdioServerTransport();
    await server.connect(transport);
}

main();
```

准备好构建实际项目了吗？请按照分步快速入门教程操作：

- [构建天气服务端](docs/server-quickstart.md) — 服务端快速开始
- [构建大语言模型驱动的聊天机器人](docs/client-quickstart.md) — 客户端快速开始

每个教程的完整代码位于 [`examples/server-quickstart/`](https://github.com/modelcontextprotocol/typescript-sdk/tree/main/examples/server-quickstart/) 和 [`examples/client-quickstart/`](https://github.com/modelcontextprotocol/typescript-sdk/tree/main/examples/client-quickstart/)。如需更多高级可运行示例，请参见：

- [`examples/server/README.md`](examples/server/README.md) — 服务端示例索引
- [`examples/client/README.md`](examples/client/README.md) — 客户端示例索引

## 文档

- [服务端指南](docs/server.md) — 构建 MCP 服务端：传输层、工具、资源、提示词、服务端发起的请求及部署
- [客户端指南](docs/client.md) — 构建 MCP 客户端：连接、工具、资源、提示词、服务端发起的请求及错误处理
- [常见问题](docs/faq.md) — 常见问题解答与故障排除
- [API 文档](https://modelcontextprotocol.github.io/typescript-sdk/)
- [MCP 官方文档](https://modelcontextprotocol.io/docs)
- [MCP 规范](https://modelcontextprotocol.io/specification/latest)

### 在本地构建文档

要在本地生成 API 参考文档：

```bash
pnpm docs          # 仅生成 V2 文档（输出目录：tmp/docs/）
pnpm docs:multi    # 生成合并的 V1 + V2 文档（输出目录：tmp/docs-combined/）
```

`docs:multi` 脚本会通过 git worktree 检出 `v1.x` 和 `main` 分支，分别构建后生成一个合并站点，其中 V1 文档位于根目录，V2 文档位于 `/v2/` 下。

## v1（历史版本）文档与修复

如果你正在使用 SDK 的 **v1** 版本，可访问 [`https://ts.sdk.modelcontextprotocol.io/`](https://ts.sdk.modelcontextprotocol.io/) 查看 **v1 API 文档**。v1 源代码及所有针对 v1 的修复均维护在长期分支 [`v1.x` branch](https://github.com/modelcontextprotocol/typescript-sdk/tree/v1.x) 上。V2 API 文档位于 [`/v2/`](https://ts.sdk.modelcontextprotocol.io/v2/)。

## 贡献指南

欢迎在 GitHub 上提交 Issue 和 Pull Request：<https://github.com/modelcontextprotocol/typescript-sdk>。

## 许可证

本项目采用双重许可：新贡献的代码遵循 Apache License 2.0，现有代码保留 MIT 许可证。详情请参阅 [LICENSE](LICENSE) 文件。