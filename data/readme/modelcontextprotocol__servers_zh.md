# Model Context Protocol 服务器

本仓库收录了 [Model Context Protocol](https://modelcontextprotocol.io/)（简称 MCP）的*参考实现*，以及社区构建的服务器和更多相关资源。

> [!IMPORTANT]
> 如果你正在寻找 MCP 服务器列表，可以浏览 [MCP Registry](https://registry.modelcontextprotocol.io/) 上已发布的服务器。本 README 所在的仓库仅用于托管由 MCP 指导小组维护的少量参考服务器。

> [!WARNING]
> 本仓库中的服务器旨在作为**参考实现**，用于演示 MCP 功能与 SDK 用法。它们主要面向希望自行开发 MCP 服务器的开发者提供教学示例，而非直接投入生产环境使用的解决方案。开发者应根据自身的安全需求及特定的威胁模型和使用场景，评估并实施相应的安全措施。

本仓库中的服务器展示了 MCP 的灵活性与可扩展性，演示了如何利用它为大语言模型（LLM）提供安全、受控的工具与数据源访问权限。通常，每个 MCP 服务器都基于对应的 MCP SDK 实现：

- [C# MCP SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Go MCP SDK](https://github.com/modelcontextprotocol/go-sdk)
- [Java MCP SDK](https://github.com/modelcontextprotocol/java-sdk)
- [Kotlin MCP SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [PHP MCP SDK](https://github.com/modelcontextprotocol/php-sdk)
- [Python MCP SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Ruby MCP SDK](https://github.com/modelcontextprotocol/ruby-sdk)
- [Rust MCP SDK](https://github.com/modelcontextprotocol/rust-sdk)
- [Swift MCP SDK](https://github.com/modelcontextprotocol/swift-sdk)
- [TypeScript MCP SDK](https://github.com/modelcontextprotocol/typescript-sdk)

## 🌟 参考服务器

这些服务器旨在演示 MCP 功能及官方 SDK 的使用方式。

- **[Everything](src/everything)** - 包含提示词、资源与工具的参考/测试服务器。
- **[Fetch](src/fetch)** - 用于高效 LLM 使用的网页内容抓取与转换工具。
- **[Filesystem](src/filesystem)** - 支持可配置访问控制的安全文件操作。
- **[Git](src/git)** - 用于读取、搜索和操作 Git 仓库的工具集。
- **[Memory](src/memory)** - 基于知识图谱的持久化记忆系统。
- **[Sequential Thinking](src/sequentialthinking)** - 通过思维序列进行动态与反思性问题解决。
- **[Time](src/time)** - 时间与时区转换功能。

### 已归档

以下参考服务器现已归档，可在 [servers-archived](https://github.com/modelcontextprotocol/servers-archived) 查看。

- **[AWS KB Retrieval](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/aws-kb-retrieval-server)** - 使用 Bedrock Agent Runtime 从 AWS 知识库中检索信息。
- **[Brave Search](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/brave-search)** - 基于 Brave Search API 的网页与本地搜索功能。该服务器已被 [官方服务器](https://github.com/brave/brave-search-mcp-server) 取代。
- **[EverArt](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/everart)** - 使用多种模型进行 AI 图像生成。
- **[GitHub](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/github)** - 仓库管理、文件操作及 GitHub API 集成。
- **[GitLab](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/gitlab)** - GitLab API，支持项目管理功能。
- **[Google Drive](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/gdrive)** - Google Drive 的文件访问与搜索能力。
- **[Google Maps](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/google-maps)** - 位置服务、路线规划与地点详情查询。
- **[PostgreSQL](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/postgres)** - 只读数据库访问及模式（schema）检查功能。
- **[Puppeteer](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/puppeteer)** - 浏览器自动化与网页爬取工具。
- **[Redis](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/redis)** - 与 Redis 键值存储进行交互。
- **[Sentry](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/sentry)** - 检索与分析 Sentry.io 上的问题报告。
- **[Slack](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/slack)** - 频道管理与消息传递功能。现由 [Zencoder](https://github.com/zencoderai/slack-mcp-server) 维护。
- **[SQLite](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/sqlite)** - 数据库交互与商业智能（BI）分析能力。

## 🚀 快速开始

### 使用本仓库的 MCP 服务器
本仓库中的 TypeScript 服务器可直接通过 `npx` 运行。

例如，以下命令将启动 [Memory](src/memory) 服务器：
```sh
npx -y @modelcontextprotocol/server-memory
```

本仓库中的 Python 服务器可直接通过 [`uvx`](https://docs.astral.sh/uv/concepts/tools/) 或 [`pip`](https://pypi.org/project/pip/) 运行。推荐使用 `uvx`，因其配置更简便。

例如，以下命令将启动 [Git](src/git) 服务器：
```sh
# With uvx
uvx mcp-server-git

# With pip
pip install mcp-server-git
python -m mcp_server_git
```

请按照[这些指引](https://docs.astral.sh/uv/getting-started/installation/)安装 `uv` / `uvx`，并按照[此处说明](https://pip.pypa.io/en/stable/installation/)安装 `pip`。

### 使用 MCP 客户端
然而，单独运行服务器实用性有限，建议将其配置到 MCP 客户端中使用。例如，以下是 Claude Desktop 使用该服务器的配置：

```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

在 Windows 系统上，需将 `npx` 用 `cmd /c` 包裹：

```json
{
  "mcpServers": {
    "memory": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

使用 Claude Desktop 作为 MCP 客户端的其他示例如下：

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/files"]
    },
    "git": {
      "command": "uvx",
      "args": ["mcp-server-git", "--repository", "path/to/git/repo"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "<YOUR_TOKEN>"
      }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://localhost/mydb"]
    }
  }
}
```

在 Windows 系统上，需对上述所有基于 `npx` 的配置项应用相同的包裹方式：将 `"command"` 的值改为 `"cmd"`，并在原有 `args` 数组前追加 `"/c", "npx"`。使用 `uvx` 的配置项保持不变。

## 🛠️ 创建你自己的服务器

想要开发自己的 MCP 服务器？请访问官方文档 [modelcontextprotocol.io](https://modelcontextprotocol.io/introduction)，获取全面的指南、最佳实践以及关于实现 MCP 服务器的技术细节。

## 📚 了解更多

查看 [ADDITIONAL.md](ADDITIONAL.md) 以获取精选的框架与资源列表，这些工具可简化 MCP 服务器和客户端的开发。

## 🤝 参与贡献

有关向本仓库提交贡献的信息，请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 🔒 安全性

如需报告安全漏洞，请参阅 [SECURITY.md](SECURITY.md)。

## 📜 许可证

本项目采用 Apache License, Version 2.0（适用于新贡献），现有代码沿用 MIT 协议 - 详见 [LICENSE](LICENSE) 文件。

## 💬 社区

- [GitHub 讨论](https://github.com/orgs/modelcontextprotocol/discussions)

## ⭐ 支持

如果你觉得 MCP 服务器很有用，欢迎收藏本仓库（Star），并贡献新的服务器或改进！

---

由 Anthropic 维护，并与社区共同构建。Model Context Protocol 为开源项目，我们鼓励所有人贡献自己的服务器与改进方案！