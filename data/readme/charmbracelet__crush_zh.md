# Crush

<p align="center">
    <a href="https://stuff.charm.sh/crush/charm-crush.png"><img width="450" alt="Charm Crush Logo" src="https://github.com/user-attachments/assets/cf8ca3ce-8b02-43f0-9d0f-5a331488da4b" /></a><br />
    <a href="https://github.com/charmbracelet/crush/releases"><img src="https://img.shields.io/github/release/charmbracelet/crush" alt="Latest Release"></a>
    <a href="https://github.com/charmbracelet/crush/actions"><img src="https://github.com/charmbracelet/crush/actions/workflows/build.yml/badge.svg" alt="Build Status"></a>
</p>

<p align="center">Your new coding bestie, now available in your favourite terminal.<br />Your tools, code, and workflows, wired into your LLM of choice.</p>
<p align="center">终端里的编程新搭档，<br />无缝接入你的工具、代码与工作流，全面兼容主流 LLM 模型。</p>

<p align="center"><img width="800" alt="Crush Demo" src="https://github.com/user-attachments/assets/58280caf-851b-470a-b6f7-d5c4ea8a1968" /></p>

## Features

- **多模型支持：** 从广泛的 LLM 中选择，或通过兼容 OpenAI/Anthropic 的 API 添加你自己的模型
- **灵活切换：** 在会话中途切换 LLM 并保留上下文
- **基于会话：** 为每个项目维护多个工作会话和上下文
- **LSP 增强：** Crush 像您一样使用语言服务器协议（LSP）获取额外上下文以辅助决策
- **可扩展性：** 通过模型上下文协议（MCP）添加功能（支持 `http`、`stdio` 和 `sse`）
- **全平台兼容：** 在 macOS、Linux、Windows（含 PowerShell 与 WSL）、Android、FreeBSD、OpenBSD 和 NetBSD 的所有终端中提供一流支持
- **企业级品质：** 基于 Charm 生态系统构建，驱动超过 2.5 万个应用，从顶级开源项目到关键业务基础设施

## Installation

使用包管理器安装：

```bash
# Homebrew
brew install charmbracelet/tap/crush

# NPM
npm install -g @charmland/crush

# Arch Linux (btw)
yay -S crush-bin

# Nix
nix run github:numtide/nix-ai-tools#crush

# FreeBSD
pkg install crush
```

Windows 用户：

```bash
# Winget
winget install charmbracelet.crush

# Scoop
scoop bucket add charm https://github.com/charmbracelet/scoop-bucket.git
scoop install crush
```

<details>
<summary><strong>Nix (NUR)</strong></summary>

可通过官方 Charm [NUR](https://github.com/nix-community/NUR) 获取 Crush，路径为 `nur.repos.charmbracelet.crush`，这是在 Nix 中获取最新版本 Crush 的最佳方式。

你也可以通过 NUR 配合 `nix-shell` 试用 Crush：

```bash
# Add the NUR channel.
nix-channel --add https://github.com/nix-community/NUR/archive/main.tar.gz nur
nix-channel --update

# Get Crush in a Nix shell.
nix-shell -p '(import <nur> { pkgs = import <nixpkgs> {}; }).repos.charmbracelet.crush'
```

### NixOS & Home Manager Module Usage via NUR

Crush 通过 NUR 提供 NixOS 和 Home Manager 模块。你可以直接在 Flake 中从 NUR 导入这些模块使用。由于它会自动检测是 Home Manager 还是 NixOS 环境，因此导入方式完全相同 :)

```nix
{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    nur.url = "github:nix-community/NUR";
  };

  outputs = { self, nixpkgs, nur, ... }: {
    nixosConfigurations.your-hostname = nixpkgs.lib.nixosSystem {
      system = "x86_64-linux";
      modules = [
        nur.modules.nixos.default
        nur.repos.charmbracelet.modules.crush
        {
          programs.crush = {
            enable = true;
            settings = {
              providers = {
                openai = {
                  id = "openai";
                  name = "OpenAI";
                  base_url = "https://api.openai.com/v1";
                  type = "openai";
                  api_key = "sk-fake123456789abcdef...";
                  models = [
                    {
                      id = "gpt-4";
                      name = "GPT-4";
                    }
                  ];
                };
              };
              lsp = {
                go = { command = "gopls"; enabled = true; };
                nix = { command = "nil"; enabled = true; };
              };
              options = {
                context_paths = [ "/etc/nixos/configuration.nix" ];
                tui = { compact_mode = true; };
                debug = false;
              };
            };
          };
        }
      ];
    };
  };
}
```

</details>

<details>
<summary><strong>Debian/Ubuntu</strong></summary>

```bash
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://repo.charm.sh/apt/gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/charm.gpg
echo "deb [signed-by=/etc/apt/keyrings/charm.gpg] https://repo.charm.sh/apt/ * *" | sudo tee /etc/apt/sources.list.d/charm.list
sudo apt update && sudo apt install crush
```

</details>

<details>
<summary><strong>Fedora/RHEL</strong></summary>

```bash
echo '[charm]
name=Charm
baseurl=https://repo.charm.sh/yum/
enabled=1
gpgcheck=1
gpgkey=https://repo.charm.sh/yum/gpg.key' | sudo tee /etc/yum.repos.d/charm.repo
sudo yum install crush
```

</details>

或者，直接下载：

- [软件包][releases] 提供 Debian 和 RPM 格式
- [预编译二进制文件][releases] 支持 Linux、macOS、Windows、FreeBSD、OpenBSD 和 NetBSD

[releases]: https://github.com/charmbracelet/crush/releases

或者直接使用 Go 安装：

```
go install github.com/charmbracelet/crush@latest
```

> [!WARNING]
> 使用 Crush 可能会提升你的工作效率，初次使用时甚至可能让你忍不住停下来钻研技术细节。如果症状持续，欢迎加入 [Slack][slack] 或 [Discord][discord] 和其他人一起交流切磋。

## Getting Started

快速上手的最佳方式是获取你偏好的提供商（如 Anthropic、OpenAI、Groq、OpenRouter 或 Vercel AI Gateway）的 API Key，然后直接启动 Crush。系统会提示你输入该密钥。

当然，你也可以通过设置环境变量来指定提供商。

| Environment Variable        | Provider                                           |
| --------------------------- | -------------------------------------------------- |
| `HYPER_API_KEY`             | Charm Hyper                                        |
| `ANTHROPIC_API_KEY`         | Anthropic                                          |
| `OPENAI_API_KEY`            | OpenAI                                             |
| `VERCEL_API_KEY`            | Vercel AI Gateway                                  |
| `GEMINI_API_KEY`            | Google Gemini                                      |
| `SYNTHETIC_API_KEY`         | Synthetic                                          |
| `ZAI_API_KEY`               | Z.ai                                               |
| `MINIMAX_API_KEY`           | MiniMax                                            |
| `HF_TOKEN`                  | Hugging Face Inference                             |
| `CEREBRAS_API_KEY`          | Cerebras                                           |
| `OPENROUTER_API_KEY`        | OpenRouter                                         |
| `IONET_API_KEY`             | io.net                                             |
| `ALIBABA_SINGAPORE_API_KEY` | Alibaba (Singapore)                                |
| `GROQ_API_KEY`              | Groq                                               |
| `AVIAN_API_KEY`             | Avian                                              |
| `OPENCODE_API_KEY`          | OpenCode Zen & Go                                  |
| `VERTEXAI_PROJECT`          | Google Cloud VertexAI (Gemini)                     |
| `VERTEXAI_LOCATION`         | Google Cloud VertexAI (Gemini)                     |
| `AWS_ACCESS_KEY_ID`         | Amazon Bedrock (Claude)                            |
| `AWS_SECRET_ACCESS_KEY`     | Amazon Bedrock (Claude)                            |
| `AWS_REGION`                | Amazon Bedrock (Claude)                            |
| `AWS_PROFILE`               | Amazon Bedrock (Custom Profile)                    |
| `AWS_BEARER_TOKEN_BEDROCK`  | Amazon Bedrock                                     |
| `AZURE_OPENAI_API_ENDPOINT` | Azure OpenAI models                                |
| `AZURE_OPENAI_API_KEY`      | Azure OpenAI models (optional when using Entra ID) |
| `AZURE_OPENAI_API_VERSION`  | Azure OpenAI models                                |

### Subscriptions

如果你更倾向于订阅制使用方式，以下套餐在 Crush 中表现良好：

- [Synthetic](https://synthetic.new/pricing)
- [GLM Coding Plan](https://z.ai/subscribe)
- [Kimi Code](https://www.kimi.com/membership/pricing)
- [MiniMax Coding Plan](https://platform.minimax.io/subscribe/coding-plan)

### By the Way

希望 Crush 支持哪些提供商？或者现有模型需要更新吗？

Crush 的默认模型列表由社区支持的开源仓库 [Catwalk](https://github.com/charmbracelet/catwalk) 管理，欢迎贡献你的修改。

<a href="https://github.com/charmbracelet/catwalk"><img width="174" height="174" alt="Catwalk Badge" src="https://github.com/user-attachments/assets/95b49515-fe82-4409-b10d-5beb0873787d" /></a>

## Configuration

> [!TIP]
> Crush 内置了 `crush-config` 技能用于自我配置。在许多情况下，你只需直接让 Crush 自行完成配置即可。

Crush 无需任何配置即可良好运行。当然，如果你需要或希望自定义 Crush，可以将其添加到项目本地或全局环境中，优先级如下：

1. `.crush.json`
2. `crush.json`
3. `$HOME/.config/crush/crush.json`

配置文件本身以 JSON 对象格式存储：

```json
{
  "this-setting": { "this": "that" },
  "that-setting": ["ceci", "cela"]
}
```

另外需要注意的是，Crush 还会将临时数据（如应用状态）存储在另一个位置：

```bash
# Unix
$HOME/.local/share/crush/crush.json

# Windows
%LOCALAPPDATA%\crush\crush.json
```

> [!TIP]
> 你可以通过设置以下环境变量来覆盖用户配置和数据配置的路径：
>
> - `CRUSH_GLOBAL_CONFIG`
> - `CRUSH_GLOBAL_DATA`

### LSPs

Crush 可以像您一样使用语言服务器协议（LSP）获取额外上下文，以辅助决策。你可以按如下方式手动添加 LSP：

```json
{
  "$schema": "https://charm.land/crush.json",
  "lsp": {
    "go": {
      "command": "gopls",
      "env": {
        "GOTOOLCHAIN": "go1.24.5"
      }
    },
    "typescript": {
      "command": "typescript-language-server",
      "args": ["--stdio"]
    },
    "nix": {
      "command": "nil"
    }
  }
}
```

### MCPs

Crush 还支持通过三种传输类型使用模型上下文协议（MCP）服务器：用于命令行服务器的 `stdio`、用于 HTTP 端点的 `http`，以及用于服务端推送事件（SSE）的 `sse`。

在 `command`、`args`、`env`、`headers` 和 `url` 中支持 Shell 风格的值展开（如 `$VAR`、`${VAR:-default}`、`$(command)`、引号包裹及嵌套），因此基于文件的密钥开箱即用。你可以使用类似 `"$TOKEN"` 或 `"$(cat /path/to/secret/token)"` 的值。展开操作通过 Crush 内置的 Shell 执行，因此相同语法在所有支持的系统（包括 Windows）上均有效。

未设置的变量默认展开为空字符串，与 Bash 行为一致。对于必需的凭证，请使用 `${VAR:?message}` 格式，这样在加载时如果变量未设置会抛出带有 `message` 的错误，而不是静默解析为空：

```json
{ "api_key": "${CODEBERG_TOKEN:?set CODEBERG_TOKEN}" }
```

如果请求头（包括 MCP `headers` 和提供商 `extra_headers`）的值解析为空字符串，则会在发出请求时将其丢弃，而不是作为 `Header:` 发送。这样可以确保在变量未设置时，可选的环境依赖型请求头（如 `"OpenAI-Organization": "$OPENAI_ORG_ID"`）保持干净。

提供商配置中的 `extra_body` 为非展开的 JSON 透传字段；请将受环境变量影响的值放在 `extra_headers` 或提供商的 `api_key` / `base_url` 中，这些字段均支持展开。

> **安全提示：** `crush.json` 被视为可信代码。其中包含的任何 `$(...)` 都会在加载时以你当前 Shell 的权限执行，且发生在 UI 出现之前。请勿在未审查目录下的 `crush.json` 中启动 Crush。

```json
{
  "$schema": "https://charm.land/crush.json",
  "mcp": {
    "filesystem": {
      "type": "stdio",
      "command": "node",
      "args": ["/path/to/mcp-server.js"],
      "timeout": 120,
      "disabled": false,
      "disabled_tools": ["some-tool-name"],
      "env": {
        "NODE_ENV": "production"
      }
    },
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "timeout": 120,
      "disabled": false,
      "disabled_tools": ["create_issue", "create_pull_request"],
      "headers": {
        "Authorization": "Bearer $GH_PAT"
      }
    },
    "streaming-service": {
      "type": "sse",
      "url": "https://example.com/mcp/sse",
      "timeout": 120,
      "disabled": false,
      "headers": {
        "API-Key": "$(echo $API_KEY)"
      }
    }
  }
}
```

### Hooks

Crush 目前提供对 Hook（钩子）的初步支持。详情请参阅[钩子指南](./docs/hooks/)。

### Sharing a workspace across clients

当 Crush 连接到共享后端时（例如两个 TUI 客户端连接同一个 `crush serve`），客户端会按解析后的 `--cwd` 分组到**工作区**。具有相同 `--cwd` 的两个客户端将加入同一底层工作区，从而共享会话列表、消息历史、权限队列、LSP 和 MCP 状态。

加入过程是隐式的：将第二个客户端指向相同的工作目录即可将其附加到现有工作区。但每次新启动默认都会创建一个全新的会话。若要接续其他客户端已打开的对话，请使用会话管理器（会话选择器）并选中它。在该界面中会显示两个状态信号：

- `IsBusy`：当该会话的代理正在处理任务时设置此标志。
- `AttachedClients`：报告当前查看该会话的客户端数量。

当 `AttachedClients` 不为零（通常与 `IsBusy` 结合）时，表明该会话正在其他客户端上“进行中”，加入它将实时镜像该视图。

首个创建工作区的客户端将固定其进程级标志。特别是 `--yolo` 和 `--debug` 遵循**先到先得（first-wins）**规则：后续到达相同 `--cwd` 但使用不同标志值的客户端不会更改正在运行的工作区。系统会输出一条调试日志记录该不匹配情况，且工作区保留创建时使用的标志。

只要至少有一个客户端保持与该工作区的 SSE 事件流连接，该工作区就会持续存在。当最后一个流断开时，工作区将被销毁。在调用 `POST /v1/workspaces` 后存在一个短暂的宽限期，以确保已创建工作区但尚未打开事件流的客户端能在被回收前成功附加。

### Ignoring Files

默认情况下，Crush 会遵循 `.gitignore` 文件。你还可以创建 `.crushignore` 文件来指定 Crush 应忽略的其他文件和目录。这对于排除版本控制中需要保留、但不希望 Crush 在提供上下文时考虑的文件非常有用。

`.crushignore` 文件使用与 `.gitignore` 相同的语法，可放置在项目根目录或子目录中。

### Allowing Tools

默认情况下，Crush 在执行工具调用前会向你请求权限。如果你愿意，可以允许工具无需提示即可执行。请谨慎使用此功能。

```json
{
  "$schema": "https://charm.land/crush.json",
  "permissions": {
    "allowed_tools": [
      "view",
      "ls",
      "grep",
      "edit",
      "mcp_context7_get-library-doc"
    ]
  }
}
```

你也可以通过添加 `--yolo` 标志运行 Crush 来完全跳过所有权限提示。请务必极度谨慎地使用此功能。

### Disabling Built-In Tools

如果你希望完全禁止 Crush 使用某些内置工具，可以通过 `options.disabled_tools` 列表将其禁用。被禁用的工具将对代理完全隐藏。

```json
{
  "$schema": "https://charm.land/crush.json",
  "options": {
    "disabled_tools": ["bash", "sourcegraph"]
  }
}
```

要禁用来自 MCP 服务器的工具，请参阅[MCP 配置部分](#mcps)。

### Disabling Skills

如果你希望完全禁止 Crush 使用某些技能，可以通过 `options.disabled_skills` 列表将其禁用。被禁用的技能将对代理隐藏（包括内置技能和从磁盘发现的技能）。

```json
{
  "$schema": "https://charm.land/crush.json",
  "options": {
    "disabled_skills": ["crush-config"]
  }
}
```

### Agent Skills

Crush 支持 [Agent Skills](https://agentskills.io) 开放标准，允许通过可复用的技能包扩展代理能力。技能是包含 `SKILL.md` 文件的文件夹，其中附有指令，Crush 可根据需要发现并激活它们。

我们搜索技能的**全局路径**如下：

* `$CRUSH_SKILLS_DIR`
* `$XDG_CONFIG_HOME/agents/skills` 或 `~/.config/agents/skills/`
* `$XDG_CONFIG_HOME/crush/skills` 或 `~/.config/crush/skills/`
* `~/.agents/skills/`
* `~/.claude/skills/`
* 在 Windows 上，我们还会检查：
  * `%LOCALAPPDATA%\agents\skills\` 或 `%USERPROFILE%\AppData\Local\agents\skills\`
  * `%LOCALAPPDATA%\crush\skills\` 或 `%USERPROFILE%\AppData\Local\crush\skills\`
* 通过 `options.skills_paths` 配置的其他路径

此外，我们还支持从以下**相对路径**加载项目内的技能：

* `.agents/skills`
* `.crush/skills`
* `.claude/skills`
* `.cursor/skills`

```jsonc
{
  "$schema": "https://charm.land/crush.json",
  "options": {
    "skills_paths": [
      "~/.config/crush/skills", // Windows: "%LOCALAPPDATA%\\crush\\skills",
      "./project-skills",
    ],
  },
}
```

你可以从 [anthropics/skills](https://github.com/anthropics/skills) 获取示例技能来快速上手：

```bash
# Unix
mkdir -p ~/.config/crush/skills
cd ~/.config/crush/skills
git clone https://github.com/anthropics/skills.git _temp
mv _temp/skills/* . && rm -rf _temp
```

```powershell
# Windows (PowerShell)
mkdir -Force "$env:LOCALAPPDATA\crush\skills"
cd "$env:LOCALAPPDATA\crush\skills"
git clone https://github.com/anthropics/skills.git _temp
mv _temp/skills/* . ; rm -r -force _temp
```

#### User-Invocable Skills

技能可以通过命令调色板（Ctrl+P）作为命令调用。在技能的 YAML frontmatter 中添加 `user-invocable: true`：

```yaml
---
name: my-skill
description: A skill that can be invoked as a command.
user-invocable: true
---
```

用户可调用的技能会出现在命令调色板中，并带有 `user:` 或 `project:` 前缀：
- 来自全局目录的技能显示为 `user:skill-name`
- 来自项目目录的技能显示为 `project:skill-name`

调用时，技能的指令会被加载到对话上下文中。

若要防止模型自动触发技能（但仍允许用户手动调用），请添加 `disable-model-invocation: true`：

```yaml
---
name: my-skill
description: Only invocable by users, not the model.
user-invocable: true
disable-model-invocation: true
---
```

带有 `disable-model-invocation` 的技能不会出现在模型可用的技能列表中，但仍可由用户手动调用。

### Desktop notifications

当工具调用需要权限或代理完成一轮任务时，Crush 会发送桌面通知。仅当终端窗口未获得焦点且你的终端支持报告焦点状态时才会发送。

```jsonc
{
  "$schema": "https://charm.land/crush.json",
  "options": {
    "disable_notifications": false, // default
  },
}
```

若要在配置中禁用桌面通知，请将 `disable_notifications` 设置为 `true`。由于平台限制，macOS 上的通知目前暂无图标。

### Initialization

初始化项目时，Crush 会分析你的代码库并创建一个上下文文件，以便在未来的会话中更高效地工作。默认情况下，该文件名为 `AGENTS.md`，但你可以通过 `initialize_as` 选项自定义其名称和位置：

```json
{
  "$schema": "https://charm.land/crush.json",
  "options": {
    "initialize_as": "AGENTS.md"
  }
}
```

如果你偏好不同的命名约定或希望将文件放置在特定目录（例如 `CRUSH.md` 或 `docs/LLMs.md`），这将非常有用。Crush 会在该文件中填充项目特定的上下文信息，如构建命令、代码模式和惯例等。

### Attribution Settings

默认情况下，Crush 会为其创建的 Git 提交和拉取请求添加署名信息。你可以通过 `attribution` 选项自定义此行为：

```json
{
  "$schema": "https://charm.land/crush.json",
  "options": {
    "attribution": {
      "trailer_style": "co-authored-by",
      "generated_with": true
    }
  }
}
```

- `trailer_style`：控制添加到提交消息中的署名后缀（默认：`assisted-by`）
  - `assisted-by`：添加 `Assisted-by: Crush:[ModelID]`，符合[该规范](https://docs.kernel.org/process/coding-assistants.html#attribution)
  - `co-authored-by`：添加 `Co-Authored-By: Crush <crush@charm.land>`
  - `none`：不添加署名后缀
- `generated_with`：当为 `true`（默认）时，在提交消息和 PR 描述中添加 `💘 Generated with Crush` 行

### Custom Providers

Crush 支持自定义提供商配置，兼容 OpenAI 和 Anthropic API。

> [!NOTE]
> 请注意我们支持两种“类型”用于 OpenAI。请选择正确的类型以确保获得最佳体验！
>
> - `openai`：当通过 OpenAI 代理或路由请求时使用。
> - `openai-compat`：使用具有 OpenAI 兼容 API 的非 OpenAI 提供商时。

#### OpenAI-Compatible APIs

以下是 Deepseek（使用 OpenAI 兼容 API）的配置示例。别忘了在环境变量中设置 `DEEPSEEK_API_KEY`。

```json
{
  "$schema": "https://charm.land/crush.json",
  "providers": {
    "deepseek": {
      "type": "openai-compat",
      "base_url": "https://api.deepseek.com/v1",
      "api_key": "$DEEPSEEK_API_KEY",
      "models": [
        {
          "id": "deepseek-chat",
          "name": "Deepseek V3",
          "cost_per_1m_in": 0.27,
          "cost_per_1m_out": 1.1,
          "cost_per_1m_in_cached": 0.07,
          "cost_per_1m_out_cached": 1.1,
          "context_window": 64000,
          "default_max_tokens": 5000
        }
      ]
    }
  }
}
```

#### Anthropic-Compatible APIs

自定义 Anthropic 兼容提供商遵循以下格式：

```json
{
  "$schema": "https://charm.land/crush.json",
  "providers": {
    "custom-anthropic": {
      "type": "anthropic",
      "base_url": "https://api.anthropic.com/v1",
      "api_key": "$ANTHROPIC_API_KEY",
      "extra_headers": {
        "anthropic-version": "2023-06-01"
      },
      "models": [
        {
          "id": "claude-sonnet-4-20250514",
          "name": "Claude Sonnet 4",
          "cost_per_1m_in": 3,
          "cost_per_1m_out": 15,
          "cost_per_1m_in_cached": 3.75,
          "cost_per_1m_out_cached": 0.3,
          "context_window": 200000,
          "default_max_tokens": 50000,
          "can_reason": true,
          "supports_attachments": true
        }
      ]
    }
  }
}
```

### Amazon Bedrock

Crush 目前支持通过 Bedrock 运行 Anthropic 模型（缓存已禁用）。

- 配置好 AWS 后（即执行 `aws configure`），Bedrock 提供商将自动出现
- Crush 还期望设置 `AWS_REGION` 或 `AWS_DEFAULT_REGION`
- 要使用特定的 AWS 配置文件，请在环境中设置 `AWS_PROFILE`，例如 `AWS_PROFILE=myprofile crush`
- 除了 `aws configure`，你也可以直接设置 `AWS_BEARER_TOKEN_BEDROCK`

### Vertex AI Platform

当设置 `VERTEXAI_PROJECT` 和 `VERTEXAI_LOCATION` 时，Vertex AI 将出现在可用提供商列表中。你还需要进行身份验证：

```bash
gcloud auth application-default login
```

要向配置中添加特定模型，请按如下方式配置：

```json
{
  "$schema": "https://charm.land/crush.json",
  "providers": {
    "vertexai": {
      "models": [
        {
          "id": "claude-sonnet-4@20250514",
          "name": "VertexAI Sonnet 4",
          "cost_per_1m_in": 3,
          "cost_per_1m_out": 15,
          "cost_per_1m_in_cached": 3.75,
          "cost_per_1m_out_cached": 0.3,
          "context_window": 200000,
          "default_max_tokens": 50000,
          "can_reason": true,
          "supports_attachments": true
        }
      ]
    }
  }
}
```

### Local Models

本地模型也可以通过 OpenAI 兼容 API 进行配置。以下是两个常见示例：

#### Ollama

```json
{
  "providers": {
    "ollama": {
      "name": "Ollama",
      "base_url": "http://localhost:11434/v1/",
      "type": "openai-compat",
      "models": [
        {
          "name": "Qwen 3 30B",
          "id": "qwen3:30b",
          "context_window": 256000,
          "default_max_tokens": 20000
        }
      ]
    }
  }
}
```

#### LM Studio

```json
{
  "providers": {
    "lmstudio": {
      "name": "LM Studio",
      "base_url": "http://localhost:1234/v1/",
      "type": "openai-compat",
      "models": [
        {
          "name": "Qwen 3 30B",
          "id": "qwen/qwen3-30b-a3b-2507",
          "context_window": 256000,
          "default_max_tokens": 20000
        }
      ]
    }
  }
}
```

## Logging

有时你需要查看日志。幸运的是，Crush 会记录各种信息。日志文件相对于项目目录存储在 `./.crush/logs/crush.log`。

CLI 还提供了一些辅助命令来方便查阅最近的日志：

```bash
# Print the last 1000 lines
crush logs

# Print the last 500 lines
crush logs --tail 500

# Follow logs in real time
crush logs --follow
```

需要更详细的日志？运行 `crush` 时添加 `--debug` 标志，或在配置中启用它：

```json
{
  "$schema": "https://charm.land/crush.json",
  "options": {
    "debug": true,
    "debug_lsp": true
  }
}
```

## Provider Auto-Updates

默认情况下，Crush 会自动从 [Catwalk](https://github.com/charmbracelet/catwalk)（开源的 Crush 提供商数据库）检查最新的提供商和模型列表。这意味着当有新的提供商或模型可用，或者模型元数据发生变更时，Crush 会自动更新你的本地配置。

### Disabling automatic provider updates

对于网络受限的用户，或偏好工作在物理隔离环境中的用户，这可能不是他们想要的功能，该功能可以禁用。

要禁用自动提供商更新，请在 `crush.json` 配置中设置 `disable_provider_auto_update`：

```json
{
  "$schema": "https://charm.land/crush.json",
  "options": {
    "disable_provider_auto_update": true
  }
}
```

或者设置环境变量 `CRUSH_DISABLE_PROVIDER_AUTO_UPDATE`：

```bash
export CRUSH_DISABLE_PROVIDER_AUTO_UPDATE=1
```

### Manually updating providers

你可以使用 `crush update-providers` 命令手动更新提供商：

```bash
# Update providers remotely from Catwalk.
crush update-providers

# Update providers from a custom Catwalk base URL.
crush update-providers https://example.com/

# Update providers from a local file.
crush update-providers /path/to/local-providers.json

# Reset providers to the embedded version, embedded at crush at build time.
crush update-providers embedded

# For more info:
crush update-providers --help
```

## Metrics

Crush 会记录伪匿名使用指标（绑定至设备专属哈希值），维护者据此确定开发与支持优先级。这些指标仅包含使用元数据；**绝不会收集提示词和回复内容**。

关于具体收集内容的详细信息见源代码（[此处](https://github.com/charmbracelet/crush/tree/main/internal/event) 和 [此处](https://github.com/charmbracelet/crush/blob/main/internal/llm/agent/event.go)）。

你可以随时通过设置环境变量来退出指标收集：

```bash
export CRUSH_DISABLE_METRICS=1
```

或在配置中设置以下内容：

```json
{
  "options": {
    "disable_metrics": true
  }
}
```

Crush 也遵循 [`DO_NOT_TRACK`](https://donottrack.sh/) 约定，你可以通过 `export DO_NOT_TRACK=1` 启用。

## Q&A

### Why is clipboard copy and paste not working?

在类 Unix 环境中可能需要安装额外的工具。

| Environment         | Tool                     |
| ------------------- | ------------------------ |
| Windows             | Native support           |
| macOS               | Native support           |
| Linux/BSD + Wayland | `wl-copy` and `wl-paste` |
| Linux/BSD + X11     | `xclip` or `xsel`        |

## Contributing

请参阅[贡献指南](https://github.com/charmbracelet/crush?tab=contributing-ov-file#contributing)。

## Whatcha think?

我们非常乐意听取你对本项目的想法。需要帮助？随时找我们。你可以通过以下渠道找到我们：

- [Twitter](https://twitter.com/charmcli)
- [Slack][slack]
- [Discord][discord]
- [The Fediverse](https://mastodon.social/@charmcli)
- [Bluesky](https://bsky.app/profile/charm.land)

[slack]: https://charm.land/slack
[discord]: https://charm.land/discord

## License

[FSL-1.1-MIT](https://github.com/charmbracelet/crush/raw/main/LICENSE.md)

---

Part of [Charm](https://charm.land).

<a href="https://charm.land/"><img alt="The Charm logo" width="400" src="https://stuff.charm.sh/charm-banner-softy.jpg" /></a>

<!--prettier-ignore-->
Charm热爱开源 • Charm loves open source