[![Go Report Card](https://goreportcard.com/badge/github.com/github/github-mcp-server)](https://goreportcard.com/report/github.com/github/github-mcp-server)

# GitHub MCP Server

GitHub MCP Server 将 AI 工具直接连接到 GitHub 平台。这使得 AI 代理、助手和聊天机器人能够读取仓库和代码文件、管理 Issue 和 PR、分析代码以及自动化工作流。所有操作均通过自然语言交互完成。

### 使用场景

- **仓库管理**：浏览和查询代码，搜索文件，分析提交记录，并了解你有权访问的任何项目的结构。
- **Issue 与 PR 自动化**：创建、更新和管理 Issue 及 Pull Request。让 AI 协助分类 Bug、审查代码变更以及维护项目看板。
- **CI/CD 与工作流智能**：监控 GitHub Actions 工作流运行，分析构建失败，管理发布，并获取开发流水线的洞察。
- **代码分析**：检查安全发现结果，审查 Dependabot 警报，理解代码模式，并获得对代码库的全面洞察。
- **团队协作**：访问讨论区，管理通知，分析团队活动，并为你的团队优化流程。

专为希望将 AI 工具与 GitHub 上下文和功能连接起来的开发者打造，从简单的自然语言查询到复杂的多步代理工作流均可胜任。

---

## 远程 GitHub MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders)

远程 GitHub MCP Server 由 GitHub 托管，是最便捷的快速上手方式。如果你的 MCP 主机不支持远程 MCP 服务器，别担心！你可以改用 [GitHub MCP Server 的本地版本](https://github.com/github/github-mcp-server?tab=readme-ov-file#local-github-mcp-server)。

### 前置条件

1. 支持远程服务器的兼容 MCP 主机（VS Code 1.101+、Claude Desktop、Cursor、Windsurf 等）
2. 已启用任何适用的[策略](https://github.com/github/github-mcp-server/blob/main/docs/policies-and-governance.md)

### 在 VS Code 中安装

如需快速安装，请使用上方的任意一键安装按钮。完成流程后，切换至 Agent 模式（位于 Copilot Chat 文本输入框旁），服务器即可启动。请确保你使用的是 [VS Code 1.101](https://code.visualstudio.com/updates/v1_101) 或[更高版本](https://code.visualstudio.com/updates)，以支持远程 MCP 和 OAuth。

或者，若要手动配置 VS Code，请从下方的示例中选择相应的 JSON 代码块并添加到你的主机配置中：

<table>
<tr><th>使用 OAuth</th><th>使用 GitHub PAT</th></tr>
<tr><th align=left colspan=2>VS Code（版本 1.101 或更高）</th></tr>
<tr valign=top>
<td>

```json
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    }
  }
}
```

</td>
<td>

```json
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${input:github_mcp_pat}"
      }
    }
  },
  "inputs": [
    {
      "type": "promptString",
      "id": "github_mcp_pat",
      "description": "GitHub Personal Access Token",
      "password": true
    }
  ]
}
```

</td>
</tr>
</table>

### 在其他 MCP 主机中安装

- **[Copilot CLI](/docs/installation-guides/install-copilot-cli.md)** - GitHub Copilot CLI 安装指南
- **[其他 IDE 中的 GitHub Copilot](/docs/installation-guides/install-other-copilot-ides.md)** - JetBrains、Visual Studio、Eclipse 和 Xcode 搭配 GitHub Copilot 的安装说明
- **[Claude Applications](/docs/installation-guides/install-claude.md)** - Claude Desktop 和 Claude Code CLI 安装指南
- **[Codex](/docs/installation-guides/install-codex.md)** - OpenAI Codex 安装指南
- **[Cursor](/docs/installation-guides/install-cursor.md)** - Cursor IDE 安装指南
- **[Windsurf](/docs/installation-guides/install-windsurf.md)** - Windsurf IDE 安装指南
- **[Rovo Dev CLI](/docs/installation-guides/install-rovo-dev-cli.md)** - Rovo Dev CLI 安装指南

> **注意：**每个 MCP 主机应用程序都需要配置一个 GitHub App 或 OAuth App，以支持通过 OAuth 进行远程访问。任何支持远程 MCP 服务器的主机应用都应支持使用 PAT 认证的远程 GitHub 服务器。具体配置细节和支持程度因主机而异。请务必查阅对应主机应用的文档以获取更多信息。

### 配置

#### 工具集配置

有关远程服务器配置的完整详情、工具集、标头及高级用法，请参阅[远程服务器文档](docs/remote-server.md)。该文件提供了在 VS Code 和其他 MCP 主机中连接、自定义和安装远程 GitHub MCP Server 的全面指南。

当未指定任何工具集时，将使用[默认工具集](#default-toolset)。

#### Insiders（预览）模式

> **抢先体验新功能！**远程服务器提供 insiders 版本，可提前访问新功能和实验性工具。

<table>
<tr><th>使用 URL Path</th><th>使用 Header</th></tr>
<tr valign=top>
<td>

```json
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/insiders"
    }
  }
}
```

</td>
<td>

```json
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "X-MCP-Insiders": "true"
      }
    }
  }
}
```

</td>
</tr>
</table>

有关更多详情和示例，请参阅[远程服务器文档](docs/remote-server.md#insiders-mode)，并查看 [Insiders 功能列表](docs/insiders-features.md)以了解全部可用内容。

#### GitHub Enterprise

##### 具有数据驻留功能的 GitHub Enterprise Cloud（ghe.com）

GitHub Enterprise Cloud 也可以使用远程服务器。

以 `https://octocorp.ghe.com` 为例，使用 GitHub PAT 令牌：

```
{
    ...
    "github-octocorp": {
      "type": "http",
      "url": "https://copilot-api.octocorp.ghe.com/mcp",
      "headers": {
        "Authorization": "Bearer ${input:github_mcp_pat}"
      }
    },
    ...
}
```

> **注意：**在 VS Code 和 GitHub Copilot 中使用 OAuth 搭配 GitHub Enterprise 时，你还需要配置 VS Code 设置以指向你的 GitHub Enterprise 实例——请参阅[从 VS Code 进行身份验证](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/configure-personal-settings/authenticate-to-ghecom)

##### GitHub Enterprise Server

GitHub Enterprise Server 不支持远程服务器托管。请参阅本地服务器配置中的 [GitHub Enterprise Server 和具有数据驻留功能的 Enterprise Cloud（ghe.com）](#github-enterprise-server-and-enterprise-cloud-with-data-residency-ghecom)。

---

## 本地 GitHub MCP Server

[![Install with Docker in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&inputs=%5B%7B%22id%22%3A%22github_token%22%2C%22type%22%3A%22promptString%22%2C%22description%22%3A%22GitHub%20Personal%20Access%20Token%22%2C%22password%22%3Atrue%7D%5D&config=%7B%22command%22%3A%22docker%22%2C%22args%22%3A%5B%22run%22%2C%22-i%22%2C%22--rm%22%2C%22-e%22%2C%22GITHUB_PERSONAL_ACCESS_TOKEN%22%2C%22ghcr.io%2Fgithub%2Fgithub-mcp-server%22%5D%2C%22env%22%3A%7B%22GITHUB_PERSONAL_ACCESS_TOKEN%22%3A%22%24%7Binput%3Agithub_token%7D%22%7D%7D) [![Install with Docker in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&inputs=%5B%7B%22id%22%3A%22github_token%22%2C%22type%22%3A%22promptString%22%2C%22description%22%3A%22GitHub%20Personal%20Access%20Token%22%2C%22password%22%3Atrue%7D%5D&config=%7B%22command%22%3A%22docker%22%2C%22args%22%3A%5B%22run%22%2C%22-i%22%2C%22--rm%22%2C%22-e%22%2C%22GITHUB_PERSONAL_ACCESS_TOKEN%22%2C%22ghcr.io%2Fgithub%2Fgithub-mcp-server%22%5D%2C%22env%22%3A%7B%22GITHUB_PERSONAL_ACCESS_TOKEN%22%3A%22%24%7Binput%3Agithub_token%7D%22%7D%7D&quality=insiders)

### 前置条件

1. 若要在容器中运行服务器，你需要安装 [Docker](https://www.docker.com/)。
2. 安装 Docker 后，还需确保 Docker 正在运行。该镜像位于 `ghcr.io/github/github-mcp-server`。该镜像为公开仓库；如果在拉取时遇到错误，可能是你的令牌已过期，需要执行 `docker logout ghcr.io`。
3. 最后，你需要[创建一个 GitHub 个人访问令牌（PAT）](https://github.com/settings/personal-access-tokens/new)。MCP 服务器可以使用许多 GitHub API，因此请启用你愿意授予 AI 工具的权限（如需了解更多关于访问令牌的详情，请参阅[文档](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)）。

<details><summary><b>安全处理 PAT 令牌</b></summary>

### 环境变量（推荐）

为保持你的 GitHub PAT 安全并在不同 MCP 主机间复用：

1. **将 PAT 存储在环境变量中**

   ```bash
   export GITHUB_PAT=your_token_here
   ```

   或创建 `.env` 文件：

   ```env
   GITHUB_PAT=your_token_here
   ```

2. **保护你的 `.env` 文件**

   ```bash
   # 添加到 .gitignore 以防止意外提交
   echo ".env" >> .gitignore
   ```

3. **在配置中引用令牌**

   ```bash
   # CLI 使用方式
   claude mcp update github -e GITHUB_PERSONAL_ACCESS_TOKEN=$GITHUB_PAT

   # 在配置文件中使用（若支持）
   "env": {
     "GITHUB_PERSONAL_ACCESS_TOKEN": "$GITHUB_PAT"
   }
   ```

> **注意：**环境变量支持因主机应用和 IDE 而异。某些应用程序（如 Windsurf）要求在配置文件中硬编码令牌。

### 令牌安全最佳实践

- **最小作用域**：仅授予必要的权限
  - `repo` - 仓库操作
  - `read:packages` - Docker 镜像访问
  - `read:org` - 组织团队访问
- **令牌分离**：为不同项目/环境使用不同的 PAT
- **定期轮换**：定期更新令牌
- **切勿提交**：确保令牌不出现在版本控制中
- **文件权限**：限制对包含令牌的配置文件的访问

  ```bash
  chmod 600 ~/.your-app/config.json
  ```

</details>

### 具有数据驻留功能的 GitHub Enterprise Server 和 Enterprise Cloud（ghe.com）

可使用标志 `--gh-host` 和环境变量 `GITHUB_HOST` 来设置 GitHub Enterprise Server 或具有数据驻留功能的 GitHub Enterprise Cloud 的主机名。

- 对于 GitHub Enterprise Server，需为域名添加 `https://` URI 方案前缀，否则默认使用 `http://`（GitHub Enterprise Server 不支持）。
- 对于具有数据驻留功能的 GitHub Enterprise Cloud，请使用 `https://YOURSUBDOMAIN.ghe.com` 作为主机名。

``` json
"github": {
    "command": "docker",
    "args": [
    "run",
    "-i",
    "--rm",
    "-e",
    "GITHUB_PERSONAL_ACCESS_TOKEN",
    "-e",
    "GITHUB_HOST",
    "ghcr.io/github/github-mcp-server"
    ],
    "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${input:github_token}",
        "GITHUB_HOST": "https://<your GHES or ghe.com domain name>"
    }
}
```

## 安装

### 在 VS Code 的 GitHub Copilot 中安装

如需快速安装，请使用上方的任意一键安装按钮。完成流程后，切换至 Agent 模式（位于 Copilot Chat 文本输入框旁），服务器即可启动。

在 VS Code 的 [Agent 模式文档](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)中了解更多关于使用 MCP 服务器工具的信息。

### 在其他 IDE（如 JetBrains、Visual Studio、Eclipse 等）的 GitHub Copilot 中安装

将以下 JSON 代码块添加到你的 IDE 的 MCP 设置中。

```json
{
  "mcp": {
    "inputs": [
      {
        "type": "promptString",
        "id": "github_token",
        "description": "GitHub Personal Access Token",
        "password": true
      }
    ],
    "servers": {
      "github": {
        "command": "docker",
        "args": [
          "run",
          "-i",
          "--rm",
          "-e",
          "GITHUB_PERSONAL_ACCESS_TOKEN",
          "ghcr.io/github/github-mcp-server"
        ],
        "env": {
          "GITHUB_PERSONAL_ACCESS_TOKEN": "${input:github_token}"
        }
      }
    }
  }
}
```

可选地，你可以添加一个类似的示例（即不包含 `mcp` 键）到工作区中的 `.vscode/mcp.json` 文件中。这将允许你将配置与其他接受相同格式的主机应用共享。

<details>
<summary><b>不包含 MCP 键的 JSON 代码块示例</b></summary>
<br>

```json
{
  "inputs": [
    {
      "type": "promptString",
      "id": "github_token",
      "description": "GitHub Personal Access Token",
      "password": true
    }
  ],
  "servers": {
    "github": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "GITHUB_PERSONAL_ACCESS_TOKEN",
        "ghcr.io/github/github-mcp-server"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${input:github_token}"
      }
    }
  }
}
```

</details>

### 在其他 MCP 主机中安装

对于其他 MCP 主机应用程序，请参阅我们的安装指南：

- **[Copilot CLI](docs/installation-guides/install-copilot-cli.md)** - GitHub Copilot CLI 安装指南
- **[其他 IDE 中的 GitHub Copilot](/docs/installation-guides/install-other-copilot-ides.md)** - JetBrains、Visual Studio、Eclipse 和 Xcode 搭配 GitHub Copilot 的安装说明
- **[Claude Code & Claude Desktop](docs/installation-guides/install-claude.md)** - Claude Code 和 Claude Desktop 安装指南
- **[Cursor](docs/installation-guides/install-cursor.md)** - Cursor IDE 安装指南
- **[Google Gemini CLI](docs/installation-guides/install-gemini-cli.md)** - Google Gemini CLI 安装指南
- **[Windsurf](docs/installation-guides/install-windsurf.md)** - Windsurf IDE 安装指南

如需查看所有安装选项的完整概览，请参阅我们的 **[安装指南索引](docs/installation-guides)**。

> **注意：**任何支持本地 MCP 服务器的主机应用都应能访问本地 GitHub MCP Server。然而，具体的配置流程、语法和集成稳定性会因主机应用而异。虽然许多可能遵循与上述示例类似的格式，但这并非绝对保证。请参阅你的主机应用程序文档以获取正确的 MCP 配置语法和设置流程。

### 从源码构建

如果你没有安装 Docker，可以使用 `go build` 在 `cmd/github-mcp-server` 目录下编译二进制文件，并使用设置了 `GITHUB_PERSONAL_ACCESS_TOKEN` 环境变量的 `github-mcp-server stdio` 命令。要指定构建输出位置，请使用 `-o` 标志。你应该配置服务器以使用编译后的可执行文件作为其 `command`。例如：

```JSON
{
  "mcp": {
    "servers": {
      "github": {
        "command": "/path/to/github-mcp-server",
        "args": ["stdio"],
        "env": {
          "GITHUB_PERSONAL_ACCESS_TOKEN": "<YOUR_TOKEN>"
        }
      }
    }
  }
}
```

### CLI 工具

`github-mcp-server` 二进制文件包含几个用于调试和探索服务器的 CLI 子命令。

- `github-mcp-server tool-search "<查询词>"`：按名称、描述和输入参数名搜索工具。使用 `--max-results` 可返回更多匹配结果。示例（彩色输出需要 TTY；在 Docker 中运行请使用 `docker run -t` (或 `-it`)）：
```bash
docker run -it --rm ghcr.io/github/github-mcp-server tool-search "issue" --max-results 5
github-mcp-server tool-search "issue" --max-results 5
```

## 工具配置

GitHub MCP Server 支持通过 `--toolsets` 标志启用或禁用特定功能组。这允许你控制 AI 工具可用的 GitHub API 能力。仅启用所需的工具集有助于 LLM 进行工具选择并减少上下文大小。

_工具集不仅限于工具。在适用情况下，相关的 MCP 资源和提示词（Prompts）也包含在内。_

当未指定任何工具集时，将使用[默认工具集](#default-toolset)。

> **需要示例？**请参阅[服务器配置指南](./docs/server-configuration.md)，查看常见配方（如最小化设置、只读模式以及结合工具与工具集的方法）。

#### 指定工具集

要为 LLM 指定可用的工具集，你可以通过以下两种方式传递白名单：

1. **使用命令行参数**：

   ```bash
   github-mcp-server --toolsets repos,issues,pull_requests,actions,code_security
   ```

2. **使用环境变量**：

   ```bash
   GITHUB_TOOLSETS="repos,issues,pull_requests,actions,code_security" ./github-mcp-server
   ```

如果同时提供了两者，环境变量 `GITHUB_TOOLSETS` 的优先级高于命令行参数。

#### 指定单个工具

你也可以使用 `--tools` 标志配置特定工具。这些工具可独立使用，或与工具集及动态工具集发现功能结合以实现精细控制。

1. **使用命令行参数**：

   ```bash
   github-mcp-server --tools get_file_contents,issue_read,create_pull_request
   ```

2. **使用环境变量**：

   ```bash
   GITHUB_TOOLS="get_file_contents,issue_read,create_pull_request" ./github-mcp-server
   ```

3. **与工具集结合**（累加）：

   ```bash
   github-mcp-server --toolsets repos,issues --tools get_gist
   ```

   这将注册来自 `repos` 和 `issues` 工具集的所有工具，以及 `get_gist`。

4. **与动态工具集结合**（累加）：

   ```bash
   github-mcp-server --tools get_file_contents --dynamic-toolsets
   ```

   这将注册 `get_file_contents` 以及动态工具集工具（`enable_toolset`、`list_available_toolsets`、`get_toolset_tools`）。

**注意事项：**

- 工具、工具集和动态工具集均可结合使用
- **只读模式优先级更高**：如果设置了 `--read-only`，即使通过 `--tools` 显式请求了写入工具，也会被跳过
- 工具名称必须完全匹配（例如 `get_file_contents`，而非 `getFileContents`）。无效的工具名称会导致服务器启动失败并报错
- 当工具重命名时，旧名称会保留为别名以向后兼容。详情请参阅[工具重命名](docs/tool-renaming.md)

### 在 Docker 中使用工具集

使用 Docker 时，你可以通过环境变量传递工具集：

```bash
docker run -i --rm \
  -e GITHUB_PERSONAL_ACCESS_TOKEN=<your-token> \
  -e GITHUB_TOOLSETS="repos,issues,pull_requests,actions,code_security" \
  ghcr.io/github/github-mcp-server
```

### 在 Docker 中使用工具

使用 Docker 时，你可以通过环境变量传递特定工具。你也可以将工具与工具集结合使用：

```bash
# 仅使用工具
docker run -i --rm \
  -e GITHUB_PERSONAL_ACCESS_TOKEN=<your-token> \
  -e GITHUB_TOOLS="get_file_contents,issue_read,create_pull_request" \
  ghcr.io/github/github-mcp-server

# 工具与工具集结合（累加）
docker run -i --rm \
  -e GITHUB_PERSONAL_ACCESS_TOKEN=<your-token> \
  -e GITHUB_TOOLSETS="repos,issues" \
  -e GITHUB_TOOLS="get_gist" \
  ghcr.io/github/github-mcp-server
```

### 特殊工具集

#### `all` 工具集

提供特殊工具集 `all` 可启用所有可用工具集，不受其他配置影响：

```bash
./github-mcp-server --toolsets all
```

或使用环境变量：

```bash
GITHUB_TOOLSETS="all" ./github-mcp-server
```

#### `default` 工具集

如果未指定任何工具集，将向服务器传递默认配置 `default`。

默认配置包含：
- context
- repos
- issues
- pull_requests
- users

若要保留默认配置并添加额外工具集：

```bash
GITHUB_TOOLSETS="default,stargazers" ./github-mcp-server
```

### Insiders（预览）模式

本地 GitHub MCP Server 提供 insiders 版本，可提前访问新功能和实验性工具。

1. **使用命令行参数**：

   ```bash
   ./github-mcp-server --insiders
   ```

2. **使用环境变量**：

   ```bash
   GITHUB_INSIDERS=true ./github-mcp-server
   ```

使用 Docker 时：

```bash
docker run -i --rm \
  -e GITHUB_PERSONAL_ACCESS_TOKEN=<your-token> \
  -e GITHUB_INSIDERS=true \
  ghcr.io/github/github-mcp-server
```

### 可用工具集

以下提供可用的工具集：

<!-- START AUTOMATED TOOLSETS -->
|     | Toolset                 | Description                                                   |
| --- | ----------------------- | ------------------------------------------------------------- |
| <picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/person-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/person-light.png"><img src="pkg/octicons/icons/person-light.png" width="20" height="20" alt="person"></picture> | `context`               | **强烈推荐**：提供当前用户上下文及你正在操作的 GitHub 上下文的工具 |
| <picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/workflow-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/workflow-light.png"><img src="pkg/octicons/icons/workflow-light.png" width="20" height="20" alt="workflow"></picture> | `actions` | GitHub Actions 工作流与 CI/CD 操作 |
| <picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/codescan-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/codescan-light.png"><img src="pkg/octicons/icons/codescan-light.png" width="20" height="20" alt="codescan"></picture> | `code_security` | 代码安全相关工具，例如 GitHub Code Scanning |
| <picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/copilot-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/copilot-light.png"><img src="pkg/octicons/icons/copilot-light.png" width="20" height="20" alt="copilot"></picture> | `copilot` | Copilot 相关工具 |
| <picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/dependabot-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/dependabot-light.png"><img src="pkg/octicons/icons/dependabot-light.png" width="20" height="20" alt="dependabot"></picture> | `dependabot` | Dependabot 工具 |
| <picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/comment-discussion-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/comment-discussion-light.png"><img src="pkg/octicons/icons/comment-discussion-light.png" width="20" height="20" alt="comment-discussion"></picture> | `discussions` | GitHub Discussions 相关工具 |
| <picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/logo-gist-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/logo-gist-light.png"><img src="pkg/octicons/icons/logo-gist-light.png" width="20" height="20" alt="logo-gist"></picture> | `gists` | GitHub Gist 相关工具 |
| <picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/git-branch-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/git-branch-light.png"><img src="pkg/octicons/icons/git-branch-light.png" width="20" height="20" alt="git-branch"></picture> | `git` | 用于底层 Git 操作的 GitHub Git API 相关工具 |
| <picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/issue-opened-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/issue-opened-light.png"><img src="pkg/octicons/icons/issue-opened-light.png" width="20" height="20" alt="issue-opened"></picture> | `issues` | GitHub Issues 相关工具 |
| <picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/tag-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/tag-light.png"><img src="pkg/octicons/icons/tag-light.png" width="20" height="20" alt="tag"></picture> | `labels` | GitHub Labels 相关工具 |
| <picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/bell-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/bell-light.png"><img src="pkg/octicons/icons/bell-light.png" width="20" height="20" alt="bell"></picture> | `notifications` | GitHub Notifications 相关工具 |
| <picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/organization-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/organization-light.png"><img src="pkg/octicons/icons/organization-light.png" width="20" height="20" alt="organization"></picture> | `orgs` | GitHub Organization 相关工具 |
| <picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/project-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/project-light.png"><img src="pkg/octicons/icons/project-light.png" width="20" height="20" alt="project"></picture> | `projects` | GitHub Projects 相关工具 |
| <picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/git-pull-request-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/git-pull-request-light.png"><img src="pkg/octicons/icons/git-pull-request-light.png" width="20" height="20" alt="git-pull-request"></picture> | `pull_requests` | GitHub Pull Request 相关工具 |
| <picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/repo-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/repo-light.png"><img src="pkg/octicons/icons/repo-light.png" width="20" height="20" alt="repo"></picture> | `repos` | GitHub Repository 相关工具 |
| <picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/shield-lock-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/shield-lock-light.png"><img src="pkg/octicons/icons/shield-lock-light.png" width="20" height="20" alt="shield-lock"></picture> | `secret_protection` | 密钥保护相关工具，例如 GitHub Secret Scanning |
| <picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/shield-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/shield-light.png"><img src="pkg/octicons/icons/shield-light.png" width="20" height="20" alt="shield"></picture> | `security_advisories` | 安全公告相关工具 |
| <picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/star-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/star-light.png"><img src="pkg/octicons/icons/star-light.png" width="20" height="20" alt="star"></picture> | `stargazers` | GitHub Stargazers 相关工具 |
| <picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/people-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/people-light.png"><img src="pkg/octicons/icons/people-light.png" width="20" height="20" alt="people"></picture> | `users` | GitHub User 相关工具 |
<!-- END AUTOMATED TOOLSETS -->

### 远程 GitHub MCP Server 的额外工具集

| Toolset                 | Description                                                   |
| ----------------------- | ------------------------------------------------------------- |
| `copilot` | Copilot 相关工具（例如 Copilot Coding Agent） |
| `copilot_spaces` | Copilot Spaces 相关工具 |
| `github_support_docs_search` | 搜索文档以回答 GitHub 产品和售后支持问题 |

## 工具

<!-- START AUTOMATED TOOLS -->
<details>

<summary><picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/workflow-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/workflow-light.png"><img src="pkg/octicons/icons/workflow-light.png" width="20" height="20" alt="workflow"></picture> Actions</summary>

- **actions_get** - 获取 GitHub Actions 资源详情（工作流、运行记录、任务和工件）
  - **Required OAuth Scopes**: `repo`
  - `method`: 要执行的方法 (string, required)
  - `owner`: 仓库所有者 (string, required)
  - `repo`: 仓库名称 (string, required)
  - `resource_id`: 资源的唯一标识符。这将根据提供的 "method" 而变化，请确保提供正确的 ID：
    - 对于 'get_workflow' 方法，提供工作流 ID 或工作流文件名（例如 ci.yaml）。
    - 对于 'get_workflow_run', 'get_workflow_run_usage', 和 'get_workflow_run_logs_url' 方法，提供运行记录 ID。
    - 对于 'download_workflow_run_artifact' 方法，提供工件 ID。
    - 对于 'get_workflow_job' 方法，提供任务 ID。
     (string, required)

- **actions_list** - 列出仓库中的 GitHub Actions 工作流
  - **Required OAuth Scopes**: `repo`
  - `method`: 要执行的操作 (string, required)
  - `owner`: 仓库所有者 (string, required)
  - `page`: 分页页码（默认：1）(number, optional)
  - `per_page`: 每页结果数用于分页（默认：30，最大：100）(number, optional)
  - `repo`: 仓库名称 (string, required)
  - `resource_id`: 资源的唯一标识符。这将根据提供的 "method" 而变化，请确保提供正确的 ID：
    - 'list_workflows' 方法不提供任何资源 ID。
    - 'list_workflow_runs' 方法提供工作流 ID 或文件名（例如 ci.yaml），或不提供以列出仓库中的所有运行记录。
    - 'list_workflow_jobs' 和 'list_workflow_run_artifacts' 方法提供运行记录 ID。
     (string, optional)
  - `workflow_jobs_filter`: 用于过滤工作流的过滤器。**仅**在 method 为 'list_workflow_jobs' 时使用 (object, optional)
  - `workflow_runs_filter`: 用于过滤运行记录的过滤器。**仅**在 method 为 'list_workflow_runs' 时使用 (object, optional)

- **actions_run_trigger** - 触发 GitHub Actions 工作流操作
  - **Required OAuth Scopes**: `repo`
  - `inputs`: 工作流接受的输入。仅用于 'run_workflow' 方法。(object, optional)
  - `method`: 要执行的方法 (string, required)
  - `owner`: 仓库所有者 (string, required)
  - `ref`: 工作流的 git 引用。可以是分支或标签名称。对于 'run_workflow' 方法是必需的。(string, optional)
  - `repo`: 仓库名称 (string, required)
  - `run_id`: 运行记录的 ID。除 'run_workflow' 外的所有方法均必需。(number, optional)
  - `workflow_id`: 工作流 ID（数字）或工作流文件名（例如，main.yml, ci.yaml）。对于 'run_workflow' 方法是必需的。(string, optional)

- **get_job_logs** - 获取 GitHub Actions 工作流任务日志
  - **Required OAuth Scopes**: `repo`
  - `failed_only`: 为 true 时，获取指定运行记录中所有失败任务的日志。需要提供 run_id。(boolean, optional)
  - `job_id`: 任务的唯一标识符。获取单个任务日志时需要提供。(number, optional)
  - `owner`: 仓库所有者 (string, required)
  - `repo`: 仓库名称 (string, required)
  - `return_content`: 返回实际日志内容而非 URL (boolean, optional)
  - `run_id`: 运行记录的唯一标识符。当 failed_only 为 true 以获取所有失败任务日志时需要提供。(number, optional)
  - `tail_lines`: 从日志末尾返回的行数 (number, optional)

</details>

<details>

<summary><picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/codescan-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/codescan-light.png"><img src="pkg/octicons/icons/codescan-light.png" width="20" height="20" alt="codescan"></picture> Code Security</summary>

- **get_code_scanning_alert** - 获取代码扫描警报
  - **Required OAuth Scopes**: `security_events`
  - **Accepted OAuth Scopes**: `repo`, `security_events`
  - `alertNumber`: 警报编号。(number, required)
  - `owner`: 仓库所有者。(string, required)
  - `repo`: 仓库名称。(string, required)

- **list_code_scanning_alerts** - 列出代码扫描警报
  - **Required OAuth Scopes**: `security_events`
  - **Accepted OAuth Scopes**: `repo`, `security_events`
  - `owner`: 仓库所有者。(string, required)
  - `ref`: 你要列出的结果的 Git 引用。(string, optional)
  - `repo`: 仓库名称。(string, required)
  - `severity`: 按严重程度过滤代码扫描警报 (string, optional)
  - `state`: 按状态过滤代码扫描警报。默认为 open (string, optional)
  - `tool_name`: 用于代码扫描的工具名称。(string, optional)

</details>

<details>

<summary><picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/person-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/person-light.png"><img src="pkg/octicons/icons/person-light.png" width="20" height="20" alt="person"></picture> Context</summary>

- **get_me** - 获取我的用户资料
  - 无需参数

- **get_team_members** - 获取团队成员
  - **Required OAuth Scopes**: `read:org`
  - **Accepted OAuth Scopes**: `admin:org`, `read:org`, `write:org`
  - `org`: 包含该团队的组织登录名（所有者）。(string, required)
  - `team_slug`: 团队标识符 (string, required)

- **get_teams** - 获取团队
  - **Required OAuth Scopes**: `read:org`
  - **Accepted OAuth Scopes**: `admin:org`, `read:org`, `write:org`
  - `user`: 获取其团队的用户名。如果未提供，则使用已认证用户。(string, optional)

</details>

<details>

<summary><picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/copilot-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/copilot-light.png"><img src="pkg/octicons/icons/copilot-light.png" width="20" height="20" alt="copilot"></picture> Copilot</summary>

- **assign_copilot_to_issue** - 分配 Copilot 到 Issue
  - **Required OAuth Scopes**: `repo`
  - `base_ref`: Agent 开始工作的 Git 引用（例如分支）。如果未指定，默认为仓库的默认分支 (string, optional)
  - `custom_instructions`: 可选的自定义指令以引导 Agent。用于提供问题描述中未包含的额外上下文、约束或指导。(string, optional)
  - `issue_number`: Issue 编号 (number, required)
  - `owner`: 仓库所有者 (string, required)
  - `repo`: 仓库名称 (string, required)

- **request_copilot_review** - 请求 Copilot 审查
  - **Required OAuth Scopes**: `repo`
  - `owner`: 仓库所有者 (string, required)
  - `pullNumber`: Pull Request 编号 (number, required)
  - `repo`: 仓库名称 (string, required)

</details>

<details>

<summary><picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/dependabot-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/dependabot-light.png"><img src="pkg/octicons/icons/dependabot-light.png" width="20" height="20" alt="dependabot"></picture> Dependabot</summary>

- **get_dependabot_alert** - 获取 Dependabot 警报
  - **Required OAuth Scopes**: `security_events`
  - **Accepted OAuth Scopes**: `repo`, `security_events`
  - `alertNumber`: 警报编号。(number, required)
  - `owner`: 仓库所有者。(string, required)
  - `repo`: 仓库名称。(string, required)

- **list_dependabot_alerts** - 列出 Dependabot 警报
  - **Required OAuth Scopes**: `security_events`
  - **Accepted OAuth Scopes**: `repo`, `security_events`
  - `owner`: 仓库所有者。(string, required)
  - `repo`: 仓库名称。(string, required)
  - `severity`: 按严重程度过滤 Dependabot 警报 (string, optional)
  - `state`: 按状态过滤 Dependabot 警报。默认为 open (string, optional)

</details>

<details>

<summary><picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/comment-discussion-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/comment-discussion-light.png"><img src="pkg/octicons/icons/comment-discussion-light.png" width="20" height="20" alt="comment-discussion"></picture> Discussions</summary>

- **get_discussion** - 获取讨论
  - **Required OAuth Scopes**: `repo`
  - `discussionNumber`: 讨论编号 (number, required)
  - `owner`: 仓库所有者 (string, required)
  - `repo`: 仓库名称 (string, required)

- **get_discussion_comments** - 获取讨论评论
  - **Required OAuth Scopes**: `repo`
  - `after`: 分页游标。对于 GraphQL API，使用上一页 PageInfo 的 endCursor。(string, optional)
  - `discussionNumber`: 讨论编号 (number, required)
  - `owner`: 仓库所有者 (string, required)
  - `perPage`: 每页结果数用于分页（最小 1，最大 100）(number, optional)
  - `repo`: 仓库名称 (string, required)

- **list_discussion_categories** - 列出讨论分类
  - **Required OAuth Scopes**: `repo`
  - `owner`: 仓库所有者 (string, required)
  - `repo`: 仓库名称。如果未提供，将在组织级别查询讨论分类。(string, optional)

- **list_discussions** - 列出讨论
  - **Required OAuth Scopes**: `repo`
  - `after`: 分页游标。对于 GraphQL API，使用上一页 PageInfo 的 endCursor。(string, optional)
  - `category`: 按讨论分类 ID 过滤（可选）。如果提供，仅列出该分类下的讨论。(string, optional)
  - `direction`: 排序方向。(string, optional)
  - `orderBy`: 按字段对讨论进行排序。如果提供，还需要提供 'direction'。(string, optional)
  - `owner`: 仓库所有者 (string, required)
  - `perPage`: 每页结果数用于分页（最小 1，最大 100）(number, optional)
  - `repo`: 仓库名称。如果未提供，将在组织级别查询讨论。(string, optional)

</details>

<details>

<summary><picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/logo-gist-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/logo-gist-light.png"><img src="pkg/octicons/icons/logo-gist-light.png" width="20" height="20" alt="logo-gist"></picture> Gists</summary>

- **create_gist** - 创建 Gist
  - **Required OAuth Scopes**: `gist`
  - `content`: 用于简单单文件 Gist 创建的内容 (string, required)
  - `description`: Gist 的描述 (string, optional)
  - `filename`: 用于简单单文件 Gist 创建的文件名 (string, required)
  - `public`: Gist 是否为公开 (boolean, optional)

- **get_gist** - 获取 Gist 内容
  - `gist_id`: Gist 的 ID (string, required)

- **list_gists** - 列出 Gists
  - `page`: 分页页码（最小 1）(number, optional)
  - `perPage`: 每页结果数用于分页（最小 1，最大 100）(number, optional)
  - `since`: 仅返回在此时间之后更新的 Gist（ISO 8601 时间戳）(string, optional)
  - `username`: GitHub 用户名（省略以获取已认证用户的 Gists）(string, optional)

- **update_gist** - 更新 Gist
  - **Required OAuth Scopes**: `gist`
  - `content`: 文件内容 (string, required)
  - `description`: 更新的 Gist 描述 (string, optional)
  - `filename`: 要更新或创建的文件名 (string, required)
  - `gist_id`: 要更新的 Gist ID (string, required)

</details>

<details>

<summary><picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/git-branch-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/git-branch-light.png"><img src="pkg/octicons/icons/git-branch-light.png" width="20" height="20" alt="git-branch"></picture> Git</summary>

- **get_repository_tree** - 获取仓库树
  - **Required OAuth Scopes**: `repo`
  - `owner`: 仓库所有者（用户名或组织）(string, required)
  - `path_filter`: 可选的路径前缀以过滤树结果（例如，'src/' 仅显示 src 目录中的文件）(string, optional)
  - `recursive`: 设置为 true 将返回树引用的对象或子树。默认为 false (boolean, optional)
  - `repo`: 仓库名称 (string, required)
  - `tree_sha`: 树的 SHA1 值或引用（分支或标签）名称。默认为仓库的默认分支 (string, optional)

</details>

<details>

<summary><picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/issue-opened-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/issue-opened-light.png"><img src="pkg/octicons/icons/issue-opened-light.png" width="20" height="20" alt="issue-opened"></picture> Issues</summary>

- **add_issue_comment** - 为 Issue 添加评论
  - **Required OAuth Scopes**: `repo`
  - `body`: 评论内容 (string, required)
  - `issue_number`: 要评论的 Issue 编号 (number, required)
  - `owner`: 仓库所有者 (string, required)
  - `repo`: 仓库名称 (string, required)

- **get_label** - 获取仓库中的特定标签。
  - **Required OAuth Scopes**: `repo`
  - `name`: 标签名称。(string, required)
  - `owner`: 仓库所有者（用户名或组织名称）(string, required)
  - `repo`: 仓库名称 (string, required)

- **issue_read** - 获取 Issue 详情
  - **Required OAuth Scopes**: `repo`
  - `issue_number`: Issue 编号 (number, required)
  - `method`: 对单个 Issue 执行的读取操作。
    选项包括：
    1. get - 获取特定 Issue 的详情。
    2. get_comments - 获取 Issue 评论。
    3. get_sub_issues - 获取该 Issue 的子 Issue。
    4. get_labels - 获取分配给该 Issue 的标签。
     (string, required)
  - `owner`: 仓库所有者 (string, required)
  - `page`: 分页页码（最小 1）(number, optional)
  - `perPage`: 每页结果数用于分页（最小 1，最大 100）(number, optional)
  - `repo`: 仓库名称 (string, required)

- **issue_write** - 创建或更新 Issue。
  - **Required OAuth Scopes**: `repo`
  - `assignees`: 分配给该 Issue 的用户名 (string[], optional)
  - `body`: Issue 正文内容 (string, optional)
  - `duplicate_of`: 此 Issue 所属的重复 Issue 编号。仅在 state_reason 为 'duplicate' 时使用。(number, optional)
  - `issue_number`: 要更新的 Issue 编号 (number, optional)
  - `labels`: 应用于该 Issue 的标签 (string[], optional)
  - `method`: 对单个 Issue 执行的写入操作。
    选项包括：
    - 'create' - 创建新 Issue。
    - 'update' - 更新现有 Issue。
     (string, required)
  - `milestone`: 里程碑编号 (number, optional)
  - `owner`: 仓库所有者 (string, required)
  - `repo`: 仓库名称 (string, required)
  - `state`: 新状态 (string, optional)
  - `state_reason`: 状态变更原因。除非 state 已更改，否则忽略。(string, optional)
  - `title`: Issue 标题 (string, optional)
  - `type`: Issue 类型。仅当仓库配置了 Issue 类型时使用。使用 list_issue_types 工具获取组织的有效类型值。如果仓库不支持 Issue 类型，请省略此参数。(string, optional)

- **list_issue_types** - 列出可用的 Issue 类型
  - **Required OAuth Scopes**: `read:org`
  - **Accepted OAuth Scopes**: `admin:org`, `read:org`, `write:org`
  - `owner`: 仓库的所有者组织 (string, required)

- **list_issues** - 列出 Issues
  - **Required OAuth Scopes**: `repo`
  - `after`: 分页游标。对于 GraphQL API，使用上一页 PageInfo 的 endCursor。(string, optional)
  - `direction`: 排序方向。如果提供，还需要提供 'orderBy'。(string, optional)
  - `labels`: 按标签过滤 (string[], optional)
  - `orderBy`: 按字段对 Issues 进行排序。如果提供，还需要提供 'direction'。(string, optional)
  - `owner`: 仓库所有者 (string, required)
  - `perPage`: 每页结果数用于分页（最小 1，最大 100）(number, optional)
  - `repo`: 仓库名称 (string, required)
  - `since`: 按日期过滤（ISO 8601 时间戳）(string, optional)
  - `state`: 按状态过滤。未提供时默认返回 open 和 closed Issues (string, optional)

- **search_issues** - 搜索 Issues
  - **Required OAuth Scopes**: `repo`
  - `order`: 排序顺序 (string, optional)
  - `owner`: 可选的仓库所有者。如果与 repo 一起提供，仅列出该仓库的 Issue。(string, optional)
  - `page`: 分页页码（最小 1）(number, optional)
  - `perPage`: 每页结果数用于分页（最小 1，最大 100）(number, optional)
  - `query`: 使用 GitHub Issue 搜索语法的查询条件 (string, required)
  - `repo`: 可选的仓库名称。如果与 owner 一起提供，仅列出该仓库的 Issue。(string, optional)
  - `sort`: 按类别匹配数排序的字段，默认为最佳匹配 (string, optional)

- **sub_issue_write** - 更改子 Issue
  - **Required OAuth Scopes**: `repo`
  - `after_id`: 排在后面的子 Issue ID（应指定 after_id 或 before_id）(number, optional)
  - `before_id`: 排在前面的子 Issue ID（应指定 after_id 或 before_id）(number, optional)
  - `issue_number`: 父 Issue 的编号 (number, required)
  - `method`: 对单个子 Issue 执行的操作
    选项包括：
    - 'add' - 向 GitHub 仓库中的父 Issue 添加子 Issue。
    - 'remove' - 从 GitHub 仓库中的父 Issue 移除子 Issue。
    - 'reprioritize' - 更改 GitHub 仓库中父 Issue 内子 Issue 的顺序。使用 'after_id' 或 'before_id' 指定新位置。
    				 (string, required)
  - `owner`: 仓库所有者 (string, required)
  - `replace_parent`: 为 true 时，替换子 Issue 当前的父 Issue。仅与 'add' 方法一起使用。(boolean, optional)
  - `repo`: 仓库名称 (string, required)
  - `sub_issue_id`: 要添加的子 Issue ID。ID 不同于 Issue 编号 (number, required)

</details>

<details>

<summary><picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/tag-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/tag-light.png"><img src="pkg/octicons/icons/tag-light.png" width="20" height="20" alt="tag"></picture> Labels</summary>

- **get_label** - 获取仓库中的特定标签。
  - **Required OAuth Scopes**: `repo`
  - `name`: 标签名称。(string, required)
  - `owner`: 仓库所有者（用户名或组织名称）(string, required)
  - `repo`: 仓库名称 (string, required)

- **label_write** - 对仓库标签执行写入操作。
  - **Required OAuth Scopes**: `repo`
  - `color`: 标签颜色，为不带 '#' 前缀的 6 位十六进制代码（例如 'f29513'）。对于 'create' 必需，对于 'update' 可选。(string, optional)
  - `description`: 标签描述文本。对于 'create' 和 'update' 可选。(string, optional)
  - `method`: 要执行的操作：'create', 'update', 或 'delete' (string, required)
  - `name`: 标签名称 - 所有操作均必需 (string, required)
  - `new_name`: 标签的新名称（仅与 'update' 方法一起使用以重命名）(string, optional)
  - `owner`: 仓库所有者（用户名或组织名称）(string, required)
  - `repo`: 仓库名称 (string, required)

- **list_label** - 列出仓库中的标签
  - **Required OAuth Scopes**: `repo`
  - `owner`: 仓库所有者（用户名或组织名称）- 所有操作均必需 (string, required)
  - `repo`: 仓库名称 - 所有操作均必需 (string, required)

</details>

<details>

<summary><picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/bell-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/bell-light.png"><img src="pkg/octicons/icons/bell-light.png" width="20" height="20" alt="bell"></picture> Notifications</summary>

- **dismiss_notification** - 关闭通知
  - **Required OAuth Scopes**: `notifications`
  - `state`: 通知的新状态（read/done）(string, required)
  - `threadID`: 通知线程的 ID (string, required)

- **get_notification_details** - 获取通知详情
  - **Required OAuth Scopes**: `notifications`
  - `notificationID`: 通知的 ID (string, required)

- **list_notifications** - 列出通知
  - **Required OAuth Scopes**: `notifications`
  - `before`: 仅显示在此时间之前更新的通知（ISO 8601 格式）(string, optional)
  - `filter`: 过滤通知类型，使用默认值除非另有指定。已读通知是用户已确认的通知。参与式通知是用户直接参与的通知，例如他们评论或创建的 Issue 或 PR。(string, optional)
  - `owner`: 可选的仓库所有者。如果与 repo 一起提供，仅列出该仓库的通知。(string, optional)
  - `page`: 分页页码（最小 1）(number, optional)
  - `perPage`: 每页结果数用于分页（最小 1，最大 100）(number, optional)
  - `repo`: 可选的仓库名称。如果与 owner 一起提供，仅列出该仓库的通知。(string, optional)
  - `since`: 仅显示在此时间之后更新的通知（ISO 8601 格式）(string, optional)

- **manage_notification_subscription** - 管理通知订阅
  - **Required OAuth Scopes**: `notifications`
  - `action`: 要执行的操作：ignore, watch, 或删除通知订阅。(string, required)
  - `notificationID`: 通知线程的 ID。(string, required)

- **manage_repository_notification_subscription** - 管理仓库通知订阅
  - **Required OAuth Scopes**: `notifications`
  - `action`: 要执行的操作：ignore, watch, 或删除仓库通知订阅。(string, required)
  - `owner`: 仓库的所有者账户。(string, required)
  - `repo`: 仓库名称。(string, required)

- **mark_all_notifications_read** - 将所有通知标记为已读
  - **Required OAuth Scopes**: `notifications`
  - `lastReadAt`: 描述上次检查通知的时间点（可选）。默认：当前时间 (string, optional)
  - `owner`: 可选的仓库所有者。如果与 repo 一起提供，仅将该仓库的通知标记为已读。(string, optional)
  - `repo`: 可选的仓库名称。如果与 owner 一起提供，仅将该仓库的通知标记为已读。(string, optional)

</details>

<details>

<summary><picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/organization-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/organization-light.png"><img src="pkg/octicons/icons/organization-light.png" width="20" height="20" alt="organization"></picture> Organizations</summary>

- **search_orgs** - 搜索组织
  - **Required OAuth Scopes**: `read:org`
  - **Accepted OAuth Scopes**: `admin:org`, `read:org`, `write:org`
  - `order`: 排序顺序 (string, optional)
  - `page`: 分页页码（最小 1）(number, optional)
  - `perPage`: 每页结果数用于分页（最小 1，最大 100）(number, optional)
  - `query`: 组织搜索查询。示例：'microsoft', 'location:california', 'created:>=2025-01-01'。搜索自动限定为 type:org。(string, required)
  - `sort`: 按类别排序的字段 (string, optional)

</details>

<details>

<summary><picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/project-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/project-light.png"><img src="pkg/octicons/icons/project-light.png" width="20" height="20" alt="project"></picture> Projects</summary>

- **projects_get** - 获取 GitHub Projects 资源详情
  - **Required OAuth Scopes**: `read:project`
  - **Accepted OAuth Scopes**: `project`, `read:project`
  - `field_id`: 字段的 ID。对于 'get_project_field' 方法必需。(number, optional)
  - `fields`: 获取项目项时包含的特定字段 ID 列表（例如 ["102589", "985201", "169875"]）。如果未提供，仅包含标题字段。仅用于 'get_project_item' 方法。(string[], optional)
  - `item_id`: 项的 ID。对于 'get_project_item' 方法必需。(number, optional)
  - `method`: 要执行的方法 (string, required)
  - `owner`: 所有者（用户或组织登录名）。名称不区分大小写。(string, optional)
  - `owner_type`: 所有者类型（user 或 org）。如果未提供，将自动检测。(string, optional)
  - `project_number`: 项目编号。(number, optional)
  - `status_update_id`: 项目状态更新的节点 ID。对于 'get_project_status_update' 方法必需。(string, optional)

- **projects_list** - 列出 GitHub Projects 资源
  - **Required OAuth Scopes**: `read:project`
  - **Accepted OAuth Scopes**: `project`, `read:project`
  - `after`: 来自上一页 pageInfo.nextCursor 的前向分页游标。(string, optional)
  - `before`: 来自上一页 pageInfo.prevCursor 的后向分页游标（罕见）。(string, optional)
  - `fields`: 列出项目项时要包含的字段 ID（例如 ["102589", "985201"]）。关键：务必提供以获取字段值。不提供则仅返回标题。仅用于 'list_project_items' 方法。(string[], optional)
  - `method`: 要执行的操作 (string, required)
  - `owner`: 所有者（用户或组织登录名）。名称不区分大小写。(string, required)
  - `owner_type`: 所有者类型（user 或 org）。如果未提供，将自动尝试两者。(string, optional)
  - `per_page`: 每页结果数（最大 50）(number, optional)
  - `project_number`: 项目编号。对于 'list_project_fields', 'list_project_items', 和 'list_project_status_updates' 方法必需。(number, optional)
  - `query`: 过滤/查询字符串。对于 list_projects：按标题文本和状态过滤（例如 "roadmap is:open"）。对于 list_project_items：使用 GitHub 项目过滤语法进行高级过滤。(string, optional)

- **projects_write** - 修改 GitHub Project 项
  - **Required OAuth Scopes**: `project`
  - `body`: 状态更新的正文（markdown）。用于 'create_project_status_update' 方法。(string, optional)
  - `issue_number`: Issue 编号（当 item_type 为 'issue' 且使用 'add_project_item' 方法时使用）。提供 issue_number 或 pull_request_number 之一。(number, optional)
  - `item_id`: 项目项 ID。对于 'update_project_item' 和 'delete_project_item' 方法必需。(number, optional)
  - `item_owner`: 包含 Issue 或 PR 的仓库的所有者（用户或组织）。对于 'add_project_item' 方法必需。(string, optional)
  - `item_repo`: 包含 Issue 或 PR 的仓库名称。对于 'add_project_item' 方法必需。(string, optional)
  - `item_type`: 项的类型，即 issue 或 pull_request。对于 'add_project_item' 方法必需。(string, optional)
  - `method`: 要执行的方法 (string, required)
  - `owner`: 项目所有者（用户或组织登录名）。名称不区分大小写。(string, required)
  - `owner_type`: 所有者类型（user 或 org）。如果未提供，将自动检测。(string, optional)
  - `project_number`: 项目编号。(number, required)
  - `pull_request_number`: PR 编号（当 item_type 为 'pull_request' 且使用 'add_project_item' 方法时使用）。提供 issue_number 或 pull_request_number 之一。(number, optional)
  - `start_date`: 状态更新的开始日期，格式 YYYY-MM-DD。用于 'create_project_status_update' 方法。(string, optional)
  - `status`: 项目状态。用于 'create_project_status_update' 方法。(string, optional)
  - `target_date`: 状态更新的目标日期，格式 YYYY-MM-DD。用于 'create_project_status_update' 方法。(string, optional)
  - `updated_field`: 包含要更新的字段 ID 和新值的对象。要清空该字段，将值设置为 null。示例：{"id": 123456, "value": "New Value"}。对于 'update_project_item' 方法必需。(object, optional)

</details>

<details>

<summary><picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/git-pull-request-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/git-pull-request-light.png"><img src="pkg/octicons/icons/git-pull-request-light.png" width="20" height="20" alt="git-pull-request"></picture> Pull Requests</summary>

- **add_comment_to_pending_review** - 向请求者的最新待处理 PR 审查添加评论
  - **Required OAuth Scopes**: `repo`
  - `body`: 审查评论的文本 (string, required)
  - `line`: PR diff 中应用评论的文件行号。对于多行注释，为范围的最后一行 (number, optional)
  - `owner`: 仓库所有者 (string, required)
  - `path`: 需要添加评论的文件相对路径 (string, required)
  - `pullNumber`: Pull Request 编号 (number, required)
  - `repo`: 仓库名称 (string, required)
  - `side`: 要注释的 diff 侧。LEFT 表示旧状态，RIGHT 表示新状态 (string, optional)
  - `startLine`: 对于多行注释，应用评论的范围的第一行 (number, optional)
  - `startSide`: 对于多行注释，应用评论的 diff 起始侧。LEFT 表示旧状态，RIGHT 表示新状态 (string, optional)
  - `subjectType`: 注释目标级别 (string, required)

- **add_reply_to_pull_request_comment** - 回复 PR 评论
  - **Required OAuth Scopes**: `repo`
  - `body`: 回复的文本 (string, required)
  - `commentId`: 要回复的评论 ID (number, required)
  - `owner`: 仓库所有者 (string, required)
  - `pullNumber`: Pull Request 编号 (number, required)
  - `repo`: 仓库名称 (string, required)

- **create_pull_request** - 打开新的 Pull Request
  - **Required OAuth Scopes**: `repo`
  - `base`: 要合并到的分支 (string, required)
  - `body`: PR 描述 (string, optional)
  - `draft`: 创建为草稿 PR (boolean, optional)
  - `head`: 包含更改的分支 (string, required)
  - `maintainer_can_modify`: 允许维护者编辑 (boolean, optional)
  - `owner`: 仓库所有者 (string, required)
  - `repo`: 仓库名称 (string, required)
  - `title`: PR 标题 (string, required)

- **list_pull_requests** - 列出 Pull Requests
  - **Required OAuth Scopes**: `repo`
  - `base`: 按基础分支过滤 (string, optional)
  - `direction`: 排序方向 (string, optional)
  - `head`: 按 head 用户/组织和分支过滤 (string, optional)
  - `owner`: 仓库所有者 (string, required)
  - `page`: 分页页码（最小 1）(number, optional)
  - `perPage`: 每页结果数用于分页（最小 1，最大 100）(number, optional)
  - `repo`: 仓库名称 (string, required)
  - `sort`: 排序依据 (string, optional)
  - `state`: 按状态过滤 (string, optional)

- **merge_pull_request** - 合并 Pull Request
  - **Required OAuth Scopes**: `repo`
  - `commit_message`: 合并提交的额外说明 (string, optional)
  - `commit_title`: 合并提交的标题 (string, optional)
  - `merge_method`: 合并方法 (string, optional)
  - `owner`: 仓库所有者 (string, required)
  - `pullNumber`: Pull Request 编号 (number, required)
  - `repo`: 仓库名称 (string, required)

- **pull_request_read** - 获取单个 PR 的详情
  - **Required OAuth Scopes**: `repo`
  - `method`: 指定需要从 GitHub 检索哪些 PR 数据的操作。 
    可能选项： 
     1. get - 获取特定 PR 的详情。
     2. get_diff - 获取 PR 的差异。
     3. get_status - 获取 PR 中 head commit 的组合提交状态。
     4. get_files - 获取 PR 中更改的文件列表。配合分页参数控制返回结果数。
     5. get_review_comments - 获取 PR 上的审查线程。每个线程包含在 PR 审查期间在同一代码位置逻辑分组的评论。返回带有元数据（isResolved, isOutdated, isCollapsed）的线程及其关联评论。使用基于游标的分页（perPage, after）控制结果。
     6. get_reviews - 获取 PR 上的审查意见。当需要审查评论时，请使用 get_review_comments 方法。配合分页参数控制返回结果数。
     7. get_comments - 获取 PR 上的评论。如果用户不特别要求审查评论，请使用此选项。配合分页参数控制返回结果数。
     8. get_check_runs - 获取 PR head commit 的检查运行记录。检查运行是 PR 上运行的各个 CI/CD 任务和检查。
     (string, required)
  - `owner`: 仓库所有者 (string, required)
  - `page`: 分页页码（最小 1）(number, optional)
  - `perPage`: 每页结果数用于分页（最小 1，最大 100）(number, optional)
  - `pullNumber`: Pull Request 编号 (number, required)
  - `repo`: 仓库名称 (string, required)

- **pull_request_review_write** - 对 PR 审查执行写入操作（创建、提交、删除）。
  - **Required OAuth Scopes**: `repo`
  - `body`: 审查评论文本 (string, optional)
  - `commitID`: 要审查的 commit SHA (string, optional)
  - `event`: 要执行的审查操作。(string, optional)
  - `method`: 对 PR 审查执行的写入操作。(string, required)
  - `owner`: 仓库所有者 (string, required)
  - `pullNumber`: Pull Request 编号 (number, required)
  - `repo`: 仓库名称 (string, required)
  - `threadId`: 审查线程的节点 ID（例如 PRRT_kwDOxxx）。对于 resolve_thread 和 unresolve_thread 方法必需。通过 pull_request_read 配合 method get_review_comments 获取线程 ID。(string, optional)

- **search_pull_requests** - 搜索 Pull Requests
  - **Required OAuth Scopes**: `repo`
  - `order`: 排序顺序 (string, optional)
  - `owner`: 可选的仓库所有者。如果与 repo 一起提供，仅列出该仓库的 PR。(string, optional)
  - `page`: 分页页码（最小 1）(number, optional)
  - `perPage`: 每页结果数用于分页（最小 1，最大 100）(number, optional)
  - `query`: 使用 GitHub PR 搜索语法的查询条件 (string, required)
  - `repo`: 可选的仓库名称。如果与 owner 一起提供，仅列出该仓库的 PR。(string, optional)
  - `sort`: 按类别匹配数排序的字段，默认为最佳匹配 (string, optional)

- **update_pull_request** - 编辑 Pull Request
  - **Required OAuth Scopes**: `repo`
  - `base`: 新的基础分支名称 (string, optional)
  - `body`: 新描述 (string, optional)
  - `draft`: 标记 PR 为草稿（true）或准备审查（false）(boolean, optional)
  - `maintainer_can_modify`: 允许维护者编辑 (boolean, optional)
  - `owner`: 仓库所有者 (string, required)
  - `pullNumber`: 要更新的 Pull Request 编号 (number, required)
  - `repo`: 仓库名称 (string, required)
  - `reviewers`: 请求审查的 GitHub 用户名 (string[], optional)
  - `state`: 新状态 (string, optional)
  - `title`: 新标题 (string, optional)

- **update_pull_request_branch** - 更新 Pull Request 分支
  - **Required OAuth Scopes**: `repo`
  - `expectedHeadSha`: PR 的 HEAD 引用预期的 SHA (string, optional)
  - `owner`: 仓库所有者 (string, required)
  - `pullNumber`: Pull Request 编号 (number, required)
  - `repo`: 仓库名称 (string, required)

</details>

<details>

<summary><picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/repo-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/repo-light.png"><img src="pkg/octicons/icons/repo-light.png" width="20" height="20" alt="repo"></picture> Repositories</summary>

- **create_branch** - 创建分支
  - **Required OAuth Scopes**: `repo`
  - `branch`: 新分支名称 (string, required)
  - `from_branch`: 源分支（默认为仓库默认分支）(string, optional)
  - `owner`: 仓库所有者 (string, required)
  - `repo`: 仓库名称 (string, required)

- **create_or_update_file** - 创建或更新文件
  - **Required OAuth Scopes**: `repo`
  - `branch`: 在其中创建/更新文件的分支 (string, required)
  - `content`: 文件内容 (string, required)
  - `message`: 提交信息 (string, required)
  - `owner`: 仓库所有者（用户名或组织）(string, required)
  - `path`: 创建/更新文件的路径 (string, required)
  - `repo`: 仓库名称 (string, required)
  - `sha`: 要替换的文件的 blob SHA。如果文件已存在则必需。(string, optional)

- **create_repository** - 创建仓库
  - **Required OAuth Scopes**: `repo`
  - `autoInit`: 使用 README 初始化 (boolean, optional)
  - `description`: 仓库描述 (string, optional)
  - `name`: 仓库名称 (string, required)
  - `organization`: 在其中创建仓库的组织（省略以在个人账户中创建）(string, optional)
  - `private`: 仓库是否应为私有 (boolean, optional)

- **delete_file** - 删除文件
  - **Required OAuth Scopes**: `repo`
  - `branch`: 从中删除文件的分支 (string, required)
  - `message`: 提交信息 (string, required)
  - `owner`: 仓库所有者（用户名或组织）(string, required)
  - `path`: 要删除的文件路径 (string, required)
  - `repo`: 仓库名称 (string, required)

- **fork_repository** - Fork 仓库
  - **Required OAuth Scopes**: `repo`
  - `organization`: Fork 到的组织 (string, optional)
  - `owner`: 仓库所有者 (string, required)
  - `repo`: 仓库名称 (string, required)

- **get_commit** - 获取提交详情
  - **Required OAuth Scopes**: `repo`
  - `include_diff`: 是否在响应中包含文件差异和统计信息。默认为 true。(boolean, optional)
  - `owner`: 仓库所有者 (string, required)
  - `page`: 分页页码（最小 1）(number, optional)
  - `perPage`: 每页结果数用于分页（最小 1，最大 100）(number, optional)
  - `repo`: 仓库名称 (string, required)
  - `sha`: Commit SHA、分支名或标签名 (string, required)

- **get_file_contents** - 获取文件或目录内容
  - **Required OAuth Scopes**: `repo`
  - `owner`: 仓库所有者（用户名或组织）(string, required)
  - `path`: 文件/目录路径 (string, optional)
  - `ref`: 接受可选的 git 引用，例如 `refs/tags/{tag}`, `refs/heads/{branch}` 或 `refs/pull/{pr_number}/head` (string, optional)
  - `repo`: 仓库名称 (string, required)
  - `sha`: 接受可选的 commit SHA。如果指定，将替代 ref 使用。(string, optional)

- **get_latest_release** - 获取最新发行版
  - **Required OAuth Scopes**: `repo`
  - `owner`: 仓库所有者 (string, required)
  - `repo`: 仓库名称 (string, required)

- **get_release_by_tag** - 按标签名获取发行版
  - **Required OAuth Scopes**: `repo`
  - `owner`: 仓库所有者 (string, required)
  - `repo`: 仓库名称 (string, required)
  - `tag`: 标签名称（例如 'v1.0.0'）(string, required)

- **get_tag** - 获取标签详情
  - **Required OAuth Scopes**: `repo`
  - `owner`: 仓库所有者 (string, required)
  - `repo`: 仓库名称 (string, required)
  - `tag`: 标签名称 (string, required)

- **list_branches** - 列出分支
  - **Required OAuth Scopes**: `repo`
  - `owner`: 仓库所有者 (string, required)
  - `page`: 分页页码（最小 1）(number, optional)
  - `perPage`: 每页结果数用于分页（最小 1，最大 100）(number, optional)
  - `repo`: 仓库名称 (string, required)

- **list_commits** - 列出提交记录
  - **Required OAuth Scopes**: `repo`
  - `author`: 按作者用户名或邮箱过滤提交的过滤器 (string, optional)
  - `owner`: 仓库所有者 (string, required)
  - `page`: 分页页码（最小 1）(number, optional)
  - `path`: 仅返回包含此文件路径的提交记录 (string, optional)
  - `perPage`: 每页结果数用于分页（最小 1，最大 100）(number, optional)
  - `repo`: 仓库名称 (string, required)
  - `sha`: 要列出提交的 Commit SHA、分支或标签名。如果未提供，使用仓库默认分支。如果提供了 commit SHA，将列出该 SHA 之前的提交记录。(string, optional)
  - `since`: 仅返回此日期之后的提交记录（ISO 8601 格式：YYYY-MM-DDTHH:MM:SSZ 或 YYYY-MM-DD）(string, optional)
  - `until`: 仅返回此日期之前的提交记录（ISO 8601 格式：YYYY-MM-DDTHH:MM:SSZ 或 YYYY-MM-DD）(string, optional)

- **list_releases** - 列出发行版
  - **Required OAuth Scopes**: `repo`
  - `owner`: 仓库所有者 (string, required)
  - `page`: 分页页码（最小 1）(number, optional)
  - `perPage`: 每页结果数用于分页（最小 1，最大 100）(number, optional)
  - `repo`: 仓库名称 (string, required)

- **list_tags** - 列出标签
  - **Required OAuth Scopes**: `repo`
  - `owner`: 仓库所有者 (string, required)
  - `page`: 分页页码（最小 1）(number, optional)
  - `perPage`: 每页结果数用于分页（最小 1，最大 100）(number, optional)
  - `repo`: 仓库名称 (string, required)

- **push_files** - 推送文件到仓库
  - **Required OAuth Scopes**: `repo`
  - `branch`: 要推送到哪个分支 (string, required)
  - `files`: 要推送的文件对象数组，每个对象包含 path（字符串）和 content（字符串）(object[], required)
  - `message`: 提交信息 (string, required)
  - `owner`: 仓库所有者 (string, required)
  - `repo`: 仓库名称 (string, required)

- **search_code** - 搜索代码
  - **Required OAuth Scopes**: `repo`
  - `order`: 结果排序顺序 (string, optional)
  - `page`: 分页页码（最小 1）(number, optional)
  - `perPage`: 每页结果数用于分页（最小 1，最大 100）(number, optional)
  - `query`: 使用 GitHub 强大代码搜索语法的查询条件。示例：'content:Skill language:Java org:github', 'NOT is:archived language:Python OR language:go', 'repo:github/github-mcp-server'。支持精确匹配、语言过滤器、路径过滤器等。(string, required)
  - `sort`: 排序字段（仅 'indexed'）(string, optional)

- **search_repositories** - 搜索仓库
  - **Required OAuth Scopes**: `repo`
  - `minimal_output`: 返回最小化仓库信息（默认：true）。为 false 时，返回完整的 GitHub API 仓库对象。(boolean, optional)
  - `order`: 排序顺序 (string, optional)
  - `page`: 分页页码（最小 1）(number, optional)
  - `perPage`: 每页结果数用于分页（最小 1，最大 100）(number, optional)
  - `query`: 仓库搜索查询。示例：'machine learning in:name stars:>1000 language:python', 'topic:react', 'user:facebook'。支持高级搜索语法以实现精确过滤。(string, required)
  - `sort`: 按字段对仓库排序，默认为最佳匹配 (string, optional)

</details>

<details>

<summary><picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/shield-lock-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/shield-lock-light.png"><img src="pkg/octicons/icons/shield-lock-light.png" width="20" height="20" alt="shield-lock"></picture> Secret Protection</summary>

- **get_secret_scanning_alert** - 获取密钥扫描警报
  - **Required OAuth Scopes**: `security_events`
  - **Accepted OAuth Scopes**: `repo`, `security_events`
  - `alertNumber`: 警报编号。(number, required)
  - `owner`: 仓库所有者。(string, required)
  - `repo`: 仓库名称。(string, required)

- **list_secret_scanning_alerts** - 列出密钥扫描警报
  - **Required OAuth Scopes**: `security_events`
  - **Accepted OAuth Scopes**: `repo`, `security_events`
  - `owner`: 仓库所有者。(string, required)
  - `repo`: 仓库名称。(string, required)
  - `resolution`: 按解决状态过滤 (string, optional)
  - `secret_type`: 要返回的密钥类型逗号分隔列表。默认返回所有默认密钥模式。要返回通用模式，请在参数中传递令牌名称。(string, optional)
  - `state`: 按状态过滤 (string, optional)

</details>

<details>

<summary><picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/shield-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/shield-light.png"><img src="pkg/octicons/icons/shield-light.png" width="20" height="20" alt="shield"></picture> Security Advisories</summary>

- **get_global_security_advisory** - 获取全局安全公告
  - **Required OAuth Scopes**: `security_events`
  - **Accepted OAuth Scopes**: `repo`, `security_events`
  - `ghsaId`: GitHub 安全公告 ID（格式：GHSA-xxxx-xxxx-xxxx）。(string, required)

- **list_global_security_advisories** - 列出全局安全公告
  - **Required OAuth Scopes**: `security_events`
  - **Accepted OAuth Scopes**: `repo`, `security_events`
  - `affects`: 按受影响包或版本过滤（例如 "package1,package2@1.0.0"）。(string, optional)
  - `cveId`: 按 CVE ID 过滤。(string, optional)
  - `cwes`: 按通用弱点枚举 ID 过滤（例如 ["79", "284", "22"]）。(string[], optional)
  - `ecosystem`: 按包生态系统过滤。(string, optional)
  - `ghsaId`: 按 GitHub 安全公告 ID 过滤（格式：GHSA-xxxx-xxxx-xxxx）。(string, optional)
  - `isWithdrawn`: 是否仅返回已撤回的公告。(boolean, optional)
  - `modified`: 按发布或更新日期/日期范围过滤（ISO 8601 日期或范围）。(string, optional)
  - `published`: 按发布日期或日期范围过滤（ISO 8601 日期或范围）。(string, optional)
  - `severity`: 按严重程度过滤。(string, optional)
  - `type`: 公告类型。(string, optional)
  - `updated`: 按更新日期或日期范围过滤（ISO 8601 日期或范围）。(string, optional)

- **list_org_repository_security_advisories** - 列出组织仓库安全公告
  - **Required OAuth Scopes**: `security_events`
  - **Accepted OAuth Scopes**: `repo`, `security_events`
  - `direction`: 排序方向。(string, optional)
  - `org`: 组织登录名。(string, required)
  - `sort`: 排序字段。(string, optional)
  - `state`: 按公告状态过滤。(string, optional)

- **list_repository_security_advisories** - 列出仓库安全公告
  - **Required OAuth Scopes**: `security_events`
  - **Accepted OAuth Scopes**: `repo`, `security_events`
  - `direction`: 排序方向。(string, optional)
  - `owner`: 仓库所有者。(string, required)
  - `repo`: 仓库名称。(string, required)
  - `sort`: 排序字段。(string, optional)
  - `state`: 按公告状态过滤。(string, optional)

</details>

<details>

<summary><picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/star-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/star-light.png"><img src="pkg/octicons/icons/star-light.png" width="20" height="20" alt="star"></picture> Stargazers</summary>

- **list_starred_repositories** - 列出已加星的仓库
  - **Required OAuth Scopes**: `repo`
  - `direction`: 结果排序方向。(string, optional)
  - `page`: 分页页码（最小 1）(number, optional)
  - `perPage`: 每页结果数用于分页（最小 1，最大 100）(number, optional)
  - `sort`: 如何排序结果。可以是 'created'（加星时）或 'updated'（最后推送时）。(string, optional)
  - `username`: 列出其已加星仓库的用户名。默认为已认证用户。(string, optional)

- **star_repository** - 给仓库加星
  - **Required OAuth Scopes**: `repo`
  - `owner`: 仓库所有者 (string, required)
  - `repo`: 仓库名称 (string, required)

- **unstar_repository** - 取消仓库加星
  - **Required OAuth Scopes**: `repo`
  - `owner`: 仓库所有者 (string, required)
  - `repo`: 仓库名称 (string, required)

</details>

<details>

<summary><picture><source media="(prefers-color-scheme: dark)" srcset="pkg/octicons/icons/people-dark.png"><source media="(prefers-color-scheme: light)" srcset="pkg/octicons/icons/people-light.png"><img src="pkg/octicons/icons/people-light.png" width="20" height="20" alt="people"></picture> Users</summary>

- **search_users** - 搜索用户
  - **Required OAuth Scopes**: `repo`
  - `order`: 排序顺序 (string, optional)
  - `page`: 分页页码（最小 1）(number, optional)
  - `perPage`: 每页结果数用于分页（最小 1，最大 100）(number, optional)
  - `query`: 用户搜索查询。示例：'john smith', 'location:seattle', 'followers:>100'。搜索自动限定为 type:user。(string, required)
  - `sort`: 按关注者数量、仓库数量或加入 GitHub 的时间对用户进行排序。(string, optional)

</details>
<!-- END AUTOMATED TOOLS -->

### 远程 GitHub MCP Server 的额外工具

<details>

<summary>Copilot</summary>

- **create_pull_request_with_copilot** - 使用 GitHub Copilot 编码代理执行任务
  - `owner`: 仓库所有者。你可以猜测所有者，但在继续之前请与用户确认。(string, required)
  - `repo`: 仓库名称。你可以猜测仓库名称，但在继续之前请与用户确认。(string, required)
  - `problem_statement`: 要执行的详细任务描述（例如 '实现一个做 X 的功能', '修复 Y Bug' 等）(string, required)
  - `title`: 将要创建的 PR 的标题 (string, required)
  - `base_ref`: Agent 开始工作的 Git 引用（例如分支）。如果未指定，默认为仓库的默认分支。(string, optional)

</details>

<details>

<summary>Copilot Spaces</summary>

- **get_copilot_space** - 获取 Copilot Space
  - `owner`: Space 的所有者。(string, required)
  - `name`: Space 的名称。(string, required)

- **list_copilot_spaces** - 列出 Copilot Spaces

</details>

<details>

<summary>GitHub Support Docs Search</summary>

- **github_support_docs_search** - 检索相关文档以回答 GitHub 产品和售后支持问题。支持主题包括：GitHub Actions Workflows、Authentication、GitHub Support Inquiries、Pull Request Practices、Repository Maintenance、GitHub Pages、GitHub Packages、GitHub Discussions、Copilot Spaces
  - `query`: 用户关于需要解答的问题的输入。这是最新的原始未编辑用户消息。你应始终保留用户消息原样，切勿修改它。(string, required)

</details>

## 动态工具发现

**注意**：此功能目前处于 beta 阶段，在远程 GitHub MCP Server 中不可用。请测试并告知我们是否遇到任何问题。

与默认启用所有工具不同，你可以开启动态工具集发现功能。动态工具集允许 MCP 主机根据用户提示列出和启用工具集。这有助于避免模型因可用工具数量过多而感到困惑的情况。

### 使用动态工具发现

使用二进制文件时，可以传递 `--dynamic-toolsets` 标志。

```bash
./github-mcp-server --dynamic-toolsets
```

使用 Docker 时，可以通过环境变量传递：

```bash
docker run -i --rm \
  -e GITHUB_PERSONAL_ACCESS_TOKEN=<your-token> \
  -e GITHUB_DYNAMIC_TOOLSETS=1 \
  ghcr.io/github/github-mcp-server
```

## 只读模式

要以只读模式运行服务器，可以使用 `--read-only` 标志。这将仅提供只读工具，防止对仓库、Issue、PR 等进行任何修改。

```bash
./github-mcp-server --read-only
```

使用 Docker 时，可以通过环境变量传递只读模式：

```bash
docker run -i --rm \
  -e GITHUB_PERSONAL_ACCESS_TOKEN=<your-token> \
  -e GITHUB_READ_ONLY=1 \
  ghcr.io/github/github-mcp-server
```

## Lockdown（锁定）模式

Lockdown 模式限制服务器从公共仓库中展示的内容。启用后，服务器会检查每个项目的作者是否对该仓库具有 push 权限。私有仓库不受影响，协作者仍保留对其自身内容的完全访问权限。

```bash
./github-mcp-server --lockdown-mode
```

使用 Docker 运行时，设置相应的环境变量：

```bash
docker run -i --rm \
  -e GITHUB_PERSONAL_ACCESS_TOKEN=<your-token> \
  -e GITHUB_LOCKDOWN_MODE=1 \
  ghcr.io/github/github-mcp-server
```

Lockdown 模式的行为取决于调用的工具。

以下工具在作者缺乏 push 权限时将返回错误：

- `issue_read:get`
- `pull_request_read:get`

以下工具将过滤掉缺乏 push 权限用户的内容：

- `issue_read:get_comments`
- `issue_read:get_sub_issues`
- `pull_request_read:get_comments`
- `pull_request_read:get_review_comments`
- `pull_request_read:get_reviews`

## i18n / 覆盖描述

可以通过在与二进制文件相同的目录中创建 `github-mcp-server-config.json` 文件来覆盖工具的说明。

该文件应包含一个 JSON 对象，以工具名称为键，新说明为值。例如：

```json
{
  "TOOL_ADD_ISSUE_COMMENT_DESCRIPTION": "an alternative description",
  "TOOL_CREATE_BRANCH_DESCRIPTION": "Create a new branch in a GitHub repository"
}
```

你可以通过使用 `--export-translations` 标志运行二进制文件来导出当前的翻译。

此标志将保留你已进行的任何翻译/覆盖，同时添加自上次导出以来二进制文件中新增的任何新翻译。

```sh
./github-mcp-server --export-translations
cat github-mcp-server-config.json
```

你也可以使用环境变量（ENV vars）来覆盖说明。环境变量名称与 JSON 文件中的键相同，前缀为 `GITHUB_MCP_` 且全部大写。

例如，要覆盖 `TOOL_ADD_ISSUE_COMMENT_DESCRIPTION` 工具，你可以设置以下环境变量：

```sh
export GITHUB_MCP_TOOL_ADD_ISSUE_COMMENT_DESCRIPTION="an alternative description"
```

### 覆盖服务器名称和标题

相同的覆盖机制也可用于自定义初始化响应中 MCP 服务器的 `name` 和 `title` 字段。这在运行多个 GitHub MCP Server 实例（例如，一个用于 github.com，另一个用于 GitHub Enterprise Server）时非常有用，以便代理能够区分它们。

| Key | Environment Variable | Default |
|-----|---------------------|---------|
| `SERVER_NAME` | `GITHUB_MCP_SERVER_NAME` | `github-mcp-server` |
| `SERVER_TITLE` | `GITHUB_MCP_SERVER_TITLE` | `GitHub MCP Server` |

例如，为 GitHub Enterprise Server 配置服务器实例：

```json
{
  "SERVER_NAME": "ghes-mcp-server",
  "SERVER_TITLE": "GHES MCP Server"
}
```

或使用环境变量：

```sh
export GITHUB_MCP_SERVER_NAME="ghes-mcp-server"
export GITHUB_MCP_SERVER_TITLE="GHES MCP Server"
```

## Library Usage

此模块导出的 Go API 目前应视为不稳定，且可能随时发生破坏性变更。未来我们可能会提供稳定性保证；如果存在适用此功能的用例，请提交 Issue。

## License

本项目根据 MIT 开源许可证的条款进行许可。请参阅 [MIT](./LICENSE) 获取完整条款。