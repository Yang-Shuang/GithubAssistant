# Claude Squad [![CI](https://github.com/smtg-ai/claude-squad/actions/workflows/build.yml/badge.svg)](https://github.com/smtg-ai/claude-squad/actions/workflows/build.yml) [![GitHub Release](https://img.shields.io/github/v/release/smtg-ai/claude-squad)](https://github.com/smtg-ai/claude-squad/releases/latest)

[Claude Squad](https://smtg-ai.github.io/claude-squad/) 是一款终端应用，可在独立工作区中管理多个 [Claude Code](https://github.com/anthropics/claude-code)、[Codex](https://github.com/openai/codex)、[Gemini](https://github.com/google-gemini/gemini-cli)（以及其他本地代理，包括 [Aider](https://github.com/Aider-AI/aider)），让你能够同时处理多个任务。

![Claude Squad Screenshot](assets/screenshot.png)

### 亮点
- 后台完成任务（包括 yolo / 自动接受模式！）
- 在一个终端窗口中管理实例和任务
- 应用更改前进行审查，推送分支前检出更改
- 每个任务拥有独立的 git 工作区，避免冲突

<br />

https://github.com/user-attachments/assets/aef18253-e58f-4525-9032-f5a3d66c975a

<br />

### 安装

无论是通过 Homebrew 还是手动安装，Claude Squad 都会在你的系统上以 `cs` 命令的形式安装。

#### Homebrew

```bash
brew install claude-squad
ln -s "$(brew --prefix)/bin/claude-squad" "$(brew --prefix)/bin/cs"
```

#### 手动安装

你还可以通过运行以下命令来安装 Claude Squad：

```bash
curl -fsSL https://raw.githubusercontent.com/smtg-ai/claude-squad/main/install.sh | bash
```

这会将 `cs` 可执行文件放置到 `~/.local/bin` 目录中。

如需为可执行文件指定自定义名称：

```bash
curl -fsSL https://raw.githubusercontent.com/smtg-ai/claude-squad/main/install.sh | bash -s -- --name <your-binary-name>
```

### 前置条件

- [tmux](https://github.com/tmux/tmux/wiki/Installing)
- [gh](https://cli.github.com/)

### 使用方法

```
Usage:
  cs [flags]
  cs [command]

Available Commands:
  completion  Generate the autocompletion script for the specified shell
  debug       Print debug information like config paths
  help        Help about any command
  reset       Reset all stored instances
  version     Print the version number of claude-squad

Flags:
  -y, --autoyes          [experimental] If enabled, all instances will automatically accept prompts for claude code & aider
  -h, --help             help for claude-squad
  -p, --program string   Program to run in new instances (e.g. 'aider --model ollama_chat/gemma3:1b')
```

运行应用：

```bash
cs
```
注意：默认程序为 `claude`，建议使用最新版本。

<br />

<b>与其他 AI 助手配合使用：</b>
- 对于 [Codex](https://github.com/openai/codex)：通过 `export OPENAI_API_KEY=<your_key>` 设置你的 API 密钥
- 使用特定助手启动：
   - Codex：`cs -p "codex"`
   - Aider：`cs -p "aider ..."`
   - Gemini：`cs -p "gemini"`
- 将其设为默认值，可通过修改配置文件实现（使用 `cs debug` 查找路径）

<br />

#### 菜单
屏幕底部的菜单显示了可用的命令： 

##### 实例/会话管理
- `n` - 创建新会话
- `N` - 使用提示词创建新会话
- `D` - 终止（删除）选中的会话
- `↑/j`、`↓/k` - 在会话间导航

##### 操作
- `↵/o` - 附加到选中会话继续对话
- `ctrl-q` - 从会话中分离
- `s` - 提交并推送分支到 GitHub
- `c` - 检出。提交更改并暂停会话
- `r` - 恢复已暂停的会话
- `?` - 显示帮助菜单

##### 导航
- `tab` - 在预览标签页和差异标签页之间切换
- `q` - 退出应用
- `shift-↓/↑` - 在差异视图中滚动

### 配置

Claude Squad 将配置存储在 `~/.claude-squad/config.json` 中。运行 `cs debug` 可获取确切路径。

#### Profiles

Profiles 允许你定义多个命名的程序配置，并在创建新会话时进行切换。当定义了多个 profile 时，会话创建覆盖层会显示一个 profile 选择器，你可以通过 `←`/`→` 键进行导航。

要配置 profiles，请在配置文件中添加 `profiles` 数组，并将 `default_program` 设置为默认选中的 profile 名称：

```json
{
  "default_program": "claude",
  "profiles": [
    { "name": "claude", "program": "claude" },
    { "name": "codex", "program": "codex" },
    { "name": "aider", "program": "aider --model ollama_chat/gemma3:1b" }
  ]
}
```

每个 profile 包含两个字段：

| 字段        | 描述                                                     |
|-----------|----------------------------------------------------------|
| `name`    | 在 profile 选择器中显示的名称                            |
| `program` | 用于启动该 profile 代理的 Shell 命令                     |

如果未定义任何 profiles，Claude Squad 将直接使用 `default_program` 作为启动命令（默认为 `claude`）。

### 常见问题

#### 无法启动新会话

如果出现类似 `failed to start new session: timed out waiting for tmux session` 的错误，请将底层程序（例如 `claude`）更新到最新版本。

### 工作原理

1. 使用 **tmux** 为每个代理创建独立的终端会话
2. 使用 **git worktrees** 隔离代码库，使每个会话在独立分支上工作
3. 提供简单的 TUI 界面，便于导航和管理

### 许可证

[AGPL-3.0](LICENSE.md)

### Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=smtg-ai/claude-squad&type=Date)](https://www.star-history.com/#smtg-ai/claude-squad&Date)