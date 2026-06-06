![Cover](https://github.com/upstash/context7/blob/master/public/cover.png?raw=true)

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en/install-mcp?name=context7&config=eyJ1cmwiOiJodHRwczovL21jcC5jb250ZXh0Ny5jb20vbWNwIn0%3D)

# Context7 平台 —— 为任意提示词提供最新代码文档

[![Website](https://img.shields.io/badge/Website-context7.com-blue)](https://context7.com) [![smithery badge](https://smithery.ai/badge/@upstash/context7-mcp)](https://smithery.ai/server/@upstash/context7-mcp) [![NPM Version](https://img.shields.io/npm/v/%40upstash%2Fcontext7-mcp?color=red)](https://www.npmjs.com/package/@upstash/context7-mcp) [![MIT licensed](https://img.shields.io/npm/l/%40upstash%2Fcontext7-mcp)](./LICENSE)

[![繁體中文](https://img.shields.io/badge/docs-繁體中文-yellow)](./i18n/README.zh-TW.md) [![简体中文](https://img.shields.io/badge/docs-简体中文-yellow)](./i18n/README.zh-CN.md) [![日本語](https://img.shields.io/badge/docs-日本語-b7003a)](./i18n/README.ja.md) [![한국어 문서](https://img.shields.io/badge/docs-한국어-green)](./i18n/README.ko.md) [![Documentación en Español](https://img.shields.io/badge/docs-Español-orange)](./i18n/README.es.md) [![Documentation en Français](https://img.shields.io/badge/docs-Français-blue)](./i18n/README.fr.md) [![Documentação em Português (Brasil)](<https://img.shields.io/badge/docs-Português%20(Brasil)-purple>)](./i18n/README.pt-BR.md) [![Documentazione in italiano](https://img.shields.io/badge/docs-Italian-red)](./i18n/README.it.md) [![Dokumentasi Bahasa Indonesia](https://img.shields.io/badge/docs-Bahasa%20Indonesia-pink)](./i18n/README.id-ID.md) [![Dokumentation auf Deutsch](https://img.shields.io/badge/docs-Deutsch-darkgreen)](./i18n/README.de.md) [![Документация на русском языке](https://img.shields.io/badge/docs-Русский-darkblue)](./i18n/README.ru.md) [![Українська документація](https://img.shields.io/badge/docs-Українська-lightblue)](./i18n/README.uk.md) [![Türkçe Doküman](https://img.shields.io/badge/docs-Türkçe-blue)](./i18n/README.tr.md) [![Arabic Documentation](https://img.shields.io/badge/docs-Arabic-white)](./i18n/README.ar.md) [![Tiếng Việt](https://img.shields.io/badge/docs-Tiếng%20Việt-red)](./i18n/README.vi.md)

## ❌ 没有 Context7

LLM（大语言模型）依赖的库信息通常已过时或过于通用。你将得到：

- ❌ 代码示例过时，基于一年前的训练数据
- ❌ 幻觉 API（根本不存在）
- ❌ 针对旧包版本的通用回答

## ✅ 使用 Context7

Context7 直接从源头获取最新、特定版本的技术文档和代码示例，并将其直接放入你的提示词中。

```txt
Create a Next.js middleware that checks for a valid JWT in cookies
and redirects unauthenticated users to `/login`. use context7
```

```txt
Configure a Cloudflare Worker script to cache
JSON API responses for five minutes. use context7
```

```txt
Show me the Supabase auth API for email/password sign-up.
```

Context7 将最新代码示例和文档直接拉取到 LLM 的上下文窗口中。无需切换标签页，不会生成不存在的幻觉 API，也不会产出过时代码。

支持两种工作模式：

- **CLI + Skills（技能）** —— 安装一个技能，引导你的 AI Agent 使用 `ctx7` CLI 命令获取文档（无需 MCP）
- **MCP** —— 注册 Context7 MCP Server，使你的 Agent 能够原生调用文档工具

## Installation（安装）

> [!NOTE]
> **推荐使用 API Key**：前往 [context7.com/dashboard](https://context7.com/dashboard) 获取免费 API Key，以获得更高的调用频率限制。

只需一条命令即可为你的编程 AI Agent 配置 Context7。`ctx7` CLI 需要 Node.js 18 或更高版本。

```bash
npx ctx7 setup
```

该命令将通过 OAuth 进行身份验证，生成 API Key，并安装相应的技能。你可以选择 CLI + Skills 模式或 MCP 模式。使用 `--cursor`、`--claude` 或 `--opencode` 可指定目标 AI Agent。

若需移除后续生成的配置，请运行 `npx ctx7 remove`。如果你通过 `npm install -g ctx7` 全局安装了 CLI，请单独使用 `npm uninstall -g ctx7` 卸载该包。

如需手动配置，请在你的 MCP Client 中使用 Context7 服务端地址 `https://mcp.context7.com/mcp`，并通过 `CONTEXT7_API_KEY` 请求头传递你的 API Key。客户端具体设置说明请参见下方链接。

**[Manual Installation / Other Clients →](https://context7.com/docs/resources/all-clients)**（手动安装 / 其他客户端）

## Important Tips（重要提示）

### Use Library Id（使用库 ID）

如果你已经明确知道要使用的具体库，请在提示词中附加其 Context7 ID。这样 Context7 可跳过库匹配步骤，直接检索文档。

```txt
Implement basic authentication with Supabase. use library /supabase/supabase for API and docs.
```

斜杠语法（`/library/name`）会明确告知 Context7 需要加载哪个库的文档。

### Specify a Version（指定版本）

若要获取特定版本的库文档，只需在提示词中提及版本号：

```txt
How do I set up Next.js 14 middleware? use context7
```

Context7 将自动匹配相应的版本。

### Add a Rule（添加规则）

如果你通过 `ctx7 setup` 安装，系统会自动配置一个技能，用于在遇到库相关问题时触发 Context7。若需手动设置规则，请为你的编程 AI Agent 添加以下内容：

- **Cursor**：`Cursor Settings > Rules`
- **Claude Code**：`CLAUDE.md`
- 或其他编程 AI Agent 的对应配置项

**Example rule（示例规则）：**

```txt
Always use Context7 when I need library/API documentation, code generation, setup or configuration steps without me having to explicitly ask.
```

## Available Tools（可用工具）

### CLI Commands（CLI 命令）

- `ctx7 library <name> <query>`：按库名称搜索 Context7 索引，并返回匹配的库及其 ID。
- `ctx7 docs <libraryId> <query>`：使用兼容 Context7 的库 ID（例如 `/mongodb/docs`、`/vercel/next.js`）检索指定库的文档。

### MCP Tools（MCP 工具）

- `resolve-library-id`：将通用库名称解析为兼容 Context7 的库 ID。
  - `query`（必填）：用户的问题或任务（用于按相关性对结果排序）
  - `libraryName`（必填）：要搜索的库名称
- `query-docs`：使用兼容 Context7 的库 ID 检索指定库的文档。
  - `libraryId`（必填）：精确的兼容 Context7 的库 ID（例如 `/mongodb/docs`、`/vercel/next.js`）
  - `query`（必填）：需要获取相关文档的问题或任务

## More Documentation（更多文档）

- [CLI Reference](https://context7.com/docs/clients/cli) - Full CLI documentation → **[CLI 参考手册]**(https://context7.com/docs/clients/cli) - 完整的 CLI 文档
- [MCP Clients](https://context7.com/docs/resources/all-clients) - Manual MCP installation for 30+ clients → **[MCP Client 支持]**(https://context7.com/docs/resources/all-clients) - 30+ 客户端的手动 MCP 安装指南
- [Adding Libraries](https://context7.com/docs/adding-libraries) - Submit your library to Context7 → **[添加新库]**(https://context7.com/docs/adding-libraries) - 向 Context7 提交你的项目/库
- [Troubleshooting](https://context7.com/docs/resources/troubleshooting) - Common issues and solutions → **[故障排除]**(https://context7.com/docs/resources/troubleshooting) - 常见问题与解决方案
- [API Reference](https://context7.com/docs/api-guide) - REST API documentation → **[API 参考手册]**(https://context7.com/docs/api-guide) - REST API 文档
- [Developer Guide](https://context7.com/docs/resources/developer) - Run Context7 MCP locally → **[开发者指南]**(https://context7.com/docs/resources/developer) - 本地运行 Context7 MCP

## Packages（相关包）

- [`@upstash/context7-mcp`](https://www.npmjs.com/package/@upstash/context7-mcp) - MCP server → `MCP Server`
- [`ctx7`](https://www.npmjs.com/package/ctx7) - CLI → `CLI 工具`
- [`@upstash/context7-sdk`](https://www.npmjs.com/package/@upstash/context7-sdk) - TypeScript SDK → `TypeScript SDK`
- [`@upstash/context7-tools-ai-sdk`](https://www.npmjs.com/package/@upstash/context7-tools-ai-sdk) - Vercel AI SDK tools → `Vercel AI SDK 工具集成`
- [`@upstash/context7-pi`](https://www.npmjs.com/package/@upstash/context7-pi) - pi.dev extension → `pi.dev 浏览器扩展`

## Disclaimer（免责声明）

1. Context7 收录的项目由社区贡献。尽管我们致力于维护高质量内容，但无法保证所有库文档的准确性、完整性或安全性。Context7 中列出的项目均由其各自的所有者开发和维护，而非 Context7 官方。如果你发现任何可疑、不当或潜在有害的内容，请立即使用项目页面上的“举报”按钮通知我们。我们会认真对待每一份报告，并迅速审核标记内容，以维护平台的安全与完整。使用 Context7 即表示你知悉并承担相关风险。

2. 本仓库仅托管 MCP Server 的源代码。其他支持组件（包括 API 后端、解析引擎和爬虫引擎）均为私有项目，不包含在此仓库中。

## 🤝 Connect with Us（与我们连接）

获取最新动态并加入我们的社区：

- 📢 Follow us on [X](https://x.com/context7ai) for the latest news and updates → - 📢 在 [X (原 Twitter)](https://x.com/context7ai) 关注我们，获取最新资讯与更新
- 🌐 Visit our [Website](https://context7.com) → - 🌐 访问我们的 [官网](https://context7.com)
- 💬 Join our [Discord Community](https://upstash.com/discord) → - 💬 加入我们的 [Discord 社区](https://upstash.com/discord)

## 📺 Context7 In Media（媒体报道）

- [Better Stack: "Free Tool Makes Cursor 10x Smarter"](https://youtu.be/52FC3qObp9E)
- [Cole Medin: "This is Hands Down the BEST MCP Server for AI Coding Assistants"](https://www.youtube.com/watch?v=G7gK8H6u7Rs)
- [Income Stream Surfers: "Context7 + SequentialThinking MCPs: Is This AGI?"](https://www.youtube.com/watch?v=-ggvzyLpK6o)
- [Julian Goldie SEO: "Context7: New MCP AI Agent Update"](https://www.youtube.com/watch?v=CTZm6fBYisc)
- [JeredBlu: "Context 7 MCP: Get Documentation Instantly + VS Code Setup"](https://www.youtube.com/watch?v=-ls0D-rtET4)
- [Income Stream Surfers: "Context7: The New MCP Server That Will CHANGE AI Coding"](https://www.youtube.com/watch?v=PS-2Azb-C3M)
- [AICodeKing: "Context7 + Cline & RooCode: This MCP Server Makes CLINE 100X MORE EFFECTIVE!"](https://www.youtube.com/watch?v=qZfENAPMnyo)
- [Sean Kochel: "5 MCP Servers For Vibe Coding Glory (Just Plug-In & Go)"](https://www.youtube.com/watch?v=LqTQi8qexJM)

## ⭐ Star History（星标历史）

[![Star History Chart](https://api.star-history.com/svg?repos=upstash/context7&type=Date)](https://www.star-history.com/#upstash/context7&Date)

## 📄 License（许可证）

MIT