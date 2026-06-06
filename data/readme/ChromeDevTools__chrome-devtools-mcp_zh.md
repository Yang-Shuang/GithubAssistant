# 面向 Agent 的 Chrome DevTools

[![npm chrome-devtools-mcp package](https://img.shields.io/npm/v/chrome-devtools-mcp.svg)](https://npmjs.org/package/chrome-devtools-mcp)

面向 Agent 的 Chrome DevTools（`chrome-devtools-mcp`）让你的编程 Agent（如 Antigravity、Claude、Cursor 或 Copilot）能够控制和检查正在运行的 Chrome 浏览器。它作为模型上下文协议（Model-Context-Protocol, MCP）服务器运行，为你的 AI 编程助手提供完整的 Chrome DevTools 功能，以实现可靠的自动化操作、深度调试和性能分析。此外还提供了 [CLI](docs/cli.md) 供不使用 MCP 的场景使用。

## [工具参考](./docs/tool-reference.md) | [更新日志](./CHANGELOG.md) | [贡献指南](./CONTRIBUTING.md) | [故障排除](./docs/troubleshooting.md) | [设计原则](./docs/design-principles.md)

## 核心功能

- **获取性能洞察**：利用 [Chrome DevTools](https://github.com/ChromeDevTools/devtools-frontend) 记录追踪数据并提取可操作的绩效分析结果。
- **高级浏览器调试**：分析网络请求、截取屏幕截图，并检查浏览器控制台消息（包含源映射堆栈追踪）。
- **可靠的自动化**。使用 [puppeteer](https://github.com/puppeteer/puppeteer) 在 Chrome 中执行自动化操作，并自动等待操作结果。

## 免责声明

`chrome-devtools-mcp` 会将浏览器实例的内容暴露给 MCP 客户端，允许它们检查、调试和修改浏览器或 DevTools 中的任何数据。请避免共享你不想与 MCP 客户端共享的敏感或个人信息。

`chrome-devtools-mcp` 官方仅支持 Google Chrome 和 [Chrome for Testing](https://developer.chrome.com/blog/chrome-for-testing/)。其他基于 Chromium 的浏览器可能可用，但不保证兼容性，你可能会遇到意外行为。请自行斟酌使用。我们致力于为 [Extended Stable Chrome](https://chromiumdash.appspot.com/schedule) 的最新版本提供修复和支持。

性能工具可能会将追踪 URL 发送至 Google CrUX API 以获取真实用户体验数据。这有助于通过并列展示现场数据和实验室数据来提供全面的性能视图。该数据由 [Chrome User Experience Report (CrUX)](https://developer.chrome.com/docs/crux) 收集。要禁用此功能，请运行 `--no-performance-crux` 标志。

## **使用统计**

Google 会收集使用统计数据（如工具调用成功率、延迟和环境信息），以改进 Chrome DevTools MCP 的可靠性和性能。

数据收集默认启用。你可以通过启动服务器时传递 `--no-usage-statistics` 标志来退出：

```json
"args": ["-y", "chrome-devtools-mcp@latest", "--no-usage-statistics"]
```

Google 将依据 [Google 隐私政策](https://policies.google.com/privacy) 处理此数据。

Google 对 Chrome DevTools MCP 的使用统计收集独立于 Chrome 浏览器的使用统计。退出 Chrome 指标不会自动退出本工具，反之亦然。

如果设置了 `CHROME_DEVTOOLS_MCP_NO_USAGE_STATISTICS` 或 `CI` 环境变量，则禁用收集。

## 更新检查

默认情况下，服务器会定期检查 npm 注册表以获取更新，并在有新版本可用时记录通知。你可以通过设置 `CHROME_DEVTOOLS_MCP_NO_UPDATE_CHECKS` 环境变量来禁用这些更新检查。

## 环境要求

- [Node.js](https://nodejs.org/) [LTS](https://github.com/nodejs/Release#release-schedule) 版本。
- [Chrome](https://www.google.com/chrome/) 当前稳定版或更高版本。
- [npm](https://www.npmjs.com/)

## 快速开始

将以下配置添加到你的 MCP 客户端：

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

> [!NOTE]
> 使用 `chrome-devtools-mcp@latest` 可确保你的 MCP 客户端始终使用最新版本的 Chrome DevTools MCP 服务器。

如果你只希望执行基本的浏览器任务，请使用 `--slim` 模式：

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest", "--slim", "--headless"]
    }
  }
}
```

参见 [精简工具参考](./docs/slim-tool-reference.md)。

### MCP 客户端配置

<details>
  <summary>Amp</summary>
  遵循 https://ampcode.com/manual#mcp 并使用上述配置。你也可以通过 CLI 安装 Chrome DevTools MCP 服务器：

```bash
amp mcp add chrome-devtools -- npx chrome-devtools-mcp@latest
```

</details>

<details>
  <summary>Antigravity</summary>

要使用 Chrome DevTools MCP 服务器，请遵循 <a href="https://antigravity.google/docs/mcp">Antigravity 文档</a> 中的说明安装自定义 MCP 服务器。将以下配置添加到 MCP 服务器配置中：

```bash
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": [
        "chrome-devtools-mcp@latest",
        "--browser-url=http://127.0.0.1:9222",
        "-y"
      ]
    }
  }
}
```

这将使 Chrome DevTools MCP 服务器自动连接到 Antigravity 正在使用的浏览器。如果你未使用 9222 端口，请确保相应调整。

使用此方法时，Chrome DevTools MCP 不会自动启动浏览器实例，因为该服务器会连接到 Antigravity 内置的浏览器。如果浏览器尚未运行，你需要先点击右上角的 Chrome 图标来启动它。

</details>

<details>
  <summary>Claude Code</summary>

**通过 CLI 安装（仅限 MCP）**

使用 Claude Code CLI 添加 Chrome DevTools MCP 服务器 (<a href="https://code.claude.com/docs/en/mcp">指南</a>)：

```bash
claude mcp add chrome-devtools --scope user npx chrome-devtools-mcp@latest
```

**作为插件安装（MCP + Skills）**

> [!NOTE]
> 如果你之前已为 Claude Code 安装了 Chrome DevTools MCP，请确保先从你的安装和配置文件中将其移除。

要使用技能安装 Chrome DevTools MCP，请在 Claude Code 中添加市场注册表：

```sh
/plugin marketplace add ChromeDevTools/chrome-devtools-mcp
```

然后，安装插件：

```sh
/plugin install chrome-devtools-mcp@chrome-devtools-plugins
```

重启 Claude Code 以加载 MCP 服务器和技能（可通过 `/skills` 检查）。

> [!TIP]
> 如果插件安装失败并提示 `Failed to clone repository` 错误（例如，企业防火墙后的 HTTPS 连接问题），请参阅 [故障排除指南](./docs/troubleshooting.md#claude-code-plugin-installation-fails-with-failed-to-clone-repository) 获取变通方法，或改用上面的 CLI 安装方式。

</details>

<details>
  <summary>Cline</summary>
  遵循 https://docs.cline.bot/mcp/configuring-mcp-servers 并使用上述配置。
</details>

<details>
  <summary>Codex</summary>
  使用上面的标准配置遵循 <a href="https://developers.openai.com/codex/mcp/#configure-with-the-cli">MCP 配置指南</a>。你也可以通过 Codex CLI 安装 Chrome DevTools MCP 服务器：

```bash
codex mcp add chrome-devtools -- npx chrome-devtools-mcp@latest
```

**在 Windows 11 上**

通过更新 `.codex/config.toml` 并添加以下 `env` 和 `startup_timeout_ms` 参数来配置 Chrome 安装位置并增加启动超时时间：

```
[mcp_servers.chrome-devtools]
command = "cmd"
args = [
    "/c",
    "npx",
    "-y",
    "chrome-devtools-mcp@latest",
]
env = { SystemRoot="C:\\Windows", PROGRAMFILES="C:\\Program Files" }
startup_timeout_ms = 20_000
```

</details>

<details>
  <summary>Command Code</summary>

使用 Command Code CLI 添加 Chrome DevTools MCP 服务器 (<a href="https://commandcode.ai/docs/mcp">MCP 指南</a>)：

```bash
cmd mcp add chrome-devtools --scope user npx chrome-devtools-mcp@latest
```

</details>

<details>
  <summary>Copilot CLI</summary>

启动 Copilot CLI：

```
copilot
```

运行以下命令打开添加新 MCP 服务器的对话框：

```
/mcp add
```

配置以下字段并按 `CTRL+S` 保存配置：

- **Server name:** `chrome-devtools`
- **Server Type:** `[1] Local`
- **Command:** `npx -y chrome-devtools-mcp@latest`

</details>

<details>
  <summary>Copilot / VS Code</summary>

**作为插件安装（推荐）**

最简单的方法是作为代理插件安装 `chrome-devtools-mcp`。这将把 **MCP 服务器**和所有 **技能**捆绑在一起，使你的代理获得有效使用它们所需的工具和专家指导。

1. 打开 **命令面板** (`Cmd+Shift+P` on macOS or `Ctrl+Shift+P` on Windows/Linux)。
2. 搜索并运行 **Chat: Install Plugin From Source** 命令。
3. 粘贴我们的仓库名称：`ChromeDevTools/chrome-devtools-mcp`。

就是这样！你的代理现已具备强大的 Chrome DevTools 功能。

---

**作为 MCP 服务器安装（仅限 MCP）**

**点击按钮安装：**

[<img src="https://img.shields.io/badge/VS_Code-VS_Code?style=flat-square&label=Install%20Server&color=0098FF" alt="Install in VS Code">](https://vscode.dev/redirect/mcp/install?name=io.github.ChromeDevTools%2Fchrome-devtools-mcp&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22chrome-devtools-mcp%22%5D%2C%22env%22%3A%7B%7D%7D)

[<img src="https://img.shields.io/badge/VS_Code_Insiders-VS_Code_Insiders?style=flat-square&label=Install%20Server&color=24bfa5" alt="Install in VS Code Insiders">](https://insiders.vscode.dev/redirect?url=vscode-insiders%3Amcp%2Finstall%3F%257B%2522name%2522%253A%2522io.github.ChromeDevTools%252Fchrome-devtools-mcp%2522%252C%2522config%2522%253A%257B%2522command%2522%253A%2522npx%2522%252C%2522args%2522%253A%255B%2522-y%2522%252C%2522chrome-devtools-mcp%2522%255D%252C%2522env%2522%253A%257B%257D%257D%257D)

**或手动安装：**

使用上面的标准配置遵循 VS Code [MCP 配置指南](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_add-an-mcp-server)，或使用 CLI：

对于 macOS 和 Linux：

```bash
code --add-mcp '{"name":"io.github.ChromeDevTools/chrome-devtools-mcp","command":"npx","args":["-y","chrome-devtools-mcp"],"env":{}}'
```

对于 Windows (PowerShell)：

```powershell
code --add-mcp '{"""name""":"""io.github.ChromeDevTools/chrome-devtools-mcp""","""command""":"""npx""","""args""":["""-y""","""chrome-devtools-mcp"""]}'
```

</details>

<details>
  <summary>Cursor</summary>

**点击按钮安装：**

[<img src="https://cursor.com/deeplink/mcp-install-dark.svg" alt="Install in Cursor">](https://cursor.com/en/install-mcp?name=chrome-devtools&config=eyJjb21tYW5kIjoibnB4IC15IGNocm9tZS1kZXZ0b29scy1tY3BAbGF0ZXN0In0%3D)

**或手动安装：**

前往 `Cursor Settings` -> `MCP` -> `New MCP Server`。使用上述配置。

</details>

<details>
  <summary>Factory CLI</summary>
使用 Factory CLI 添加 Chrome DevTools MCP 服务器 (<a href="https://docs.factory.ai/cli/configuration/mcp">指南</a>)：

```bash
droid mcp add chrome-devtools "npx -y chrome-devtools-mcp@latest"
```

</details>

<details>
  <summary>Gemini CLI</summary>
使用 Gemini CLI 安装 Chrome DevTools MCP 服务器。

**项目范围：**

```bash
# 仅 MCP：
gemini mcp add chrome-devtools npx chrome-devtools-mcp@latest
# 或作为 Gemini 扩展（MCP+Skills）：
gemini extensions install --auto-update https://github.com/ChromeDevTools/chrome-devtools-mcp
```

**全局范围：**

```bash
gemini mcp add -s user chrome-devtools npx chrome-devtools-mcp@latest
```

或者，遵循 <a href="https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md#how-to-set-up-your-mcp-server">MCP 指南</a> 并使用上面的标准配置。

</details>

<details>
  <summary>Gemini Code Assist</summary>
使用上面的标准配置遵循 <a href="https://cloud.google.com/gemini/docs/codeassist/use-agentic-chat-pair-programmer#configure-mcp-servers">MCP 配置指南</a>。
</details>

<details>
  <summary>JetBrains AI Assistant & Junie</summary>

前往 `Settings | Tools | AI Assistant | Model Context Protocol (MCP)` -> `Add`。使用上述配置。同样地，可在 `Settings | Tools | Junie | MCP Settings` -> `Add` 中为 JetBrains Junie 配置 chrome-devtools-mcp。使用上述配置。

</details>

<details>
  <summary>Kiro</summary>

在 **Kiro Settings** 中，前往 `Configure MCP` > `Open Workspace or User MCP Config` > 使用上述配置代码片段。

或者，从 IDE **Activity Bar** > `Kiro` > `MCP Servers` > `Click Open MCP Config`。使用上述配置代码片段。

</details>

<details>
  <summary>Katalon Studio</summary>

Chrome DevTools MCP 服务器可通过 MCP 代理与 <a href="https://docs.katalon.com/katalon-studio/studioassist/mcp-servers/setting-up-chrome-devtools-mcp-server-for-studioassist">Katalon StudioAssist</a> 配合使用。

**步骤 1：** 遵循 <a href="https://docs.katalon.com/katalon-studio/studioassist/mcp-servers/setting-up-mcp-proxy-for-stdio-mcp-servers">MCP 代理设置指南</a> 安装 MCP 代理。

**步骤 2：** 启动带有代理的 Chrome DevTools MCP 服务器：

```bash
mcp-proxy --transport streamablehttp --port 8080 -- npx -y chrome-devtools-mcp@latest
```

**注意：** 如果 8080 端口已被占用，你可能需要选择其他端口。

**步骤 3：** 在 Katalon Studio 中，使用以下设置将服务器添加到 StudioAssist：

- **Connection URL:** `http://127.0.0.1:8080/mcp`
- **Transport type:** `HTTP`

连接成功后，Chrome DevTools MCP 工具将在 StudioAssist 中可用。

</details>

<details>
  <summary>Mistral Vibe</summary>

在 `~/.vibe/config.toml` 中添加以下内容：

```toml
[[mcp_servers]]
name = "chrome-devtools"
transport = "stdio"
command = "npx"
args = ["chrome-devtools-mcp@latest"]
```

</details>

<details>
  <summary>OpenCode</summary>

将以下配置添加到你的 `opencode.json` 文件中。如果没有该文件，请在 `~/.config/opencode/opencode.json` 处创建它（<a href="https://opencode.ai/docs/mcp-servers">指南</a>）：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "chrome-devtools": {
      "type": "local",
      "command": ["npx", "-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

</details>

<details>
  <summary>Qoder</summary>

在 **Qoder Settings** 中，前往 `MCP Server` > `+ Add` > 使用上述配置代码片段。

或者，遵循 <a href="https://docs.qoder.com/user-guide/chat/model-context-protocol">MCP 指南</a> 并使用上面的标准配置。

</details>

<details>
  <summary>Qoder CLI</summary>

使用 Qoder CLI 安装 Chrome DevTools MCP 服务器（<a href="https://docs.qoder.com/cli/using-cli#mcp-servers">指南</a>）：

**项目范围：**

```bash
qodercli mcp add chrome-devtools -- npx chrome-devtools-mcp@latest
```

**全局范围：**

```bash
qodercli mcp add -s user chrome-devtools -- npx chrome-devtools-mcp@latest
```

</details>

<details>
  <summary>Visual Studio</summary>

**点击按钮安装：**

[<img src="https://img.shields.io/badge/Visual_Studio-Install-C16FDE?logo=visualstudio&logoColor=white" alt="Install in Visual Studio">](https://vs-open.link/mcp-install?%7B%22name%22%3A%22chrome-devtools%22%2C%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22chrome-devtools-mcp%40latest%22%5D%7D)

</details>

<details>
  <summary>Warp</summary>

前往 `Settings | AI | Manage MCP Servers` -> `+ Add` 以[添加 MCP 服务器](https://docs.warp.dev/knowledge-and-collaboration/mcp#adding-an-mcp-server)。使用上述配置。

</details>

<details>
  <summary>Windsurf</summary>
使用上面的标准配置遵循 <a href="https://docs.windsurf.com/windsurf/cascade/mcp#mcp-config-json">MCP 配置指南</a>。
</details>

### 你的第一条提示词

在你的 MCP 客户端中输入以下提示词以检查一切是否正常：

```
Check the performance of https://developers.chrome.com
```

你的 MCP 客户端应打开浏览器并记录性能追踪数据。

> [!NOTE]
> 一旦 MCP 客户端使用需要运行中浏览器实例的工具，MCP 服务器将自动启动浏览器。仅连接到 Chrome DevTools MCP 服务器不会自动启动浏览器。

## 工具

如果遇到任何问题，请查看我们的 [故障排除指南](./docs/troubleshooting.md)。

<!-- BEGIN AUTO GENERATED TOOLS -->

- **Input automation** (10 tools)
  - [`click`](docs/tool-reference.md#click)
  - [`drag`](docs/tool-reference.md#drag)
  - [`fill`](docs/tool-reference.md#fill)
  - [`fill_form`](docs/tool-reference.md#fill_form)
  - [`handle_dialog`](docs/tool-reference.md#handle_dialog)
  - [`hover`](docs/tool-reference.md#hover)
  - [`press_key`](docs/tool-reference.md#press_key)
  - [`type_text`](docs/tool-reference.md#type_text)
  - [`upload_file`](docs/tool-reference.md#upload_file)
  - [`click_at`](docs/tool-reference.md#click_at)
- **Navigation automation** (6 tools)
  - [`close_page`](docs/tool-reference.md#close_page)
  - [`list_pages`](docs/tool-reference.md#list_pages)
  - [`navigate_page`](docs/tool-reference.md#navigate_page)
  - [`new_page`](docs/tool-reference.md#new_page)
  - [`select_page`](docs/tool-reference.md#select_page)
  - [`wait_for`](docs/tool-reference.md#wait_for)
- **Emulation** (2 tools)
  - [`emulate`](docs/tool-reference.md#emulate)
  - [`resize_page`](docs/tool-reference.md#resize_page)
- **Performance** (3 tools)
  - [`performance_analyze_insight`](docs/tool-reference.md#performance_analyze_insight)
  - [`performance_start_trace`](docs/tool-reference.md#performance_start_trace)
  - [`performance_stop_trace`](docs/tool-reference.md#performance_stop_trace)
- **Network** (2 tools)
  - [`get_network_request`](docs/tool-reference.md#get_network_request)
  - [`list_network_requests`](docs/tool-reference.md#list_network_requests)
- **Debugging** (8 tools)
  - [`evaluate_script`](docs/tool-reference.md#evaluate_script)
  - [`get_console_message`](docs/tool-reference.md#get_console_message)
  - [`lighthouse_audit`](docs/tool-reference.md#lighthouse_audit)
  - [`list_console_messages`](docs/tool-reference.md#list_console_messages)
  - [`take_screenshot`](docs/tool-reference.md#take_screenshot)
  - [`take_snapshot`](docs/tool-reference.md#take_snapshot)
  - [`screencast_start`](docs/tool-reference.md#screencast_start)
  - [`screencast_stop`](docs/tool-reference.md#screencast_stop)
- **Memory** (5 tools)
  - [`take_heapsnapshot`](docs/tool-reference.md#take_heapsnapshot)
  - [`get_heapsnapshot_class_nodes`](docs/tool-reference.md#get_heapsnapshot_class_nodes)
  - [`get_heapsnapshot_details`](docs/tool-reference.md#get_heapsnapshot_details)
  - [`get_heapsnapshot_retainers`](docs/tool-reference.md#get_heapsnapshot_retainers)
  - [`get_heapsnapshot_summary`](docs/tool-reference.md#get_heapsnapshot_summary)
- **Extensions** (5 tools)
  - [`install_extension`](docs/tool-reference.md#install_extension)
  - [`list_extensions`](docs/tool-reference.md#list_extensions)
  - [`reload_extension`](docs/tool-reference.md#reload_extension)
  - [`trigger_extension_action`](docs/tool-reference.md#trigger_extension_action)
  - [`uninstall_extension`](docs/tool-reference.md#uninstall_extension)
- **Third-party** (2 tools)
  - [`execute_3p_developer_tool`](docs/tool-reference.md#execute_3p_developer_tool)
  - [`list_3p_developer_tools`](docs/tool-reference.md#list_3p_developer_tools)
- **WebMCP** (2 tools)
  - [`execute_webmcp_tool`](docs/tool-reference.md#execute_webmcp_tool)
  - [`list_webmcp_tools`](docs/tool-reference.md#list_webmcp_tools)

<!-- END AUTO GENERATED TOOLS -->

## 配置

Chrome DevTools MCP 服务器支持以下配置选项：

<!-- BEGIN AUTO GENERATED OPTIONS -->

- **`--autoConnect`/ `--auto-connect`**
  If specified, automatically connects to a browser (Chrome 144+) running locally from the user data directory identified by the channel param (default channel is stable). Requires the remote debugging server to be started in the Chrome instance via chrome://inspect/#remote-debugging.
  - **Type:** boolean
  - **Default:** `false`

- **`--browserUrl`/ `--browser-url`, `-u`**
  Connect to a running, debuggable Chrome instance (e.g. `http://127.0.0.1:9222`). For more details see: https://github.com/ChromeDevTools/chrome-devtools-mcp#connecting-to-a-running-chrome-instance.
  - **Type:** string

- **`--wsEndpoint`/ `--ws-endpoint`, `-w`**
  WebSocket endpoint to connect to a running Chrome instance (e.g., ws://127.0.0.1:9222/devtools/browser/<id>). Alternative to --browserUrl.
  - **Type:** string

- **`--wsHeaders`/ `--ws-headers`**
  Custom headers for WebSocket connection in JSON format (e.g., '{"Authorization":"Bearer token"}'). Only works with --wsEndpoint.
  - **Type:** string

- **`--headless`**
  Whether to run in headless (no UI) mode.
  - **Type:** boolean
  - **Default:** `false`

- **`--executablePath`/ `--executable-path`, `-e`**
  Path to custom Chrome executable.
  - **Type:** string

- **`--isolated`**
  If specified, creates a temporary user-data-dir that is automatically cleaned up after the browser is closed. Defaults to false.
  - **Type:** boolean

- **`--userDataDir`/ `--user-data-dir`**
  Path to the user data directory for Chrome. Default is $HOME/.cache/chrome-devtools-mcp/chrome-profile$CHANNEL_SUFFIX_IF_NON_STABLE
  - **Type:** string

- **`--channel`**
  Specify a different Chrome channel that should be used. The default is the stable channel version.
  - **Type:** string
  - **Choices:** `canary`, `dev`, `beta`, `stable`

- **`--logFile`/ `--log-file`**
  Path to a file to write debug logs to. Set the env variable `DEBUG` to `*` to enable verbose logs. Useful for submitting bug reports.
  - **Type:** string

- **`--viewport`**
  Initial viewport size for the Chrome instances started by the server. For example, `1280x720`. In headless mode, max size is 3840x2160px.
  - **Type:** string

- **`--proxyServer`/ `--proxy-server`**
  Proxy server configuration for Chrome passed as --proxy-server when launching the browser. See https://www.chromium.org/developers/design-documents/network-settings/ for details.
  - **Type:** string

- **`--acceptInsecureCerts`/ `--accept-insecure-certs`**
  If enabled, ignores errors relative to self-signed and expired certificates. Use with caution.
  - **Type:** boolean

- **`--experimentalPageIdRouting`/ `--experimental-page-id-routing`**
  Whether to expose pageId on page-scoped tools and route requests by page ID (useful for concurrent agent sessions).
  - **Type:** boolean

- **`--experimentalDevtools`/ `--experimental-devtools`**
  Whether to enable automation over DevTools targets
  - **Type:** boolean

- **`--experimentalVision`/ `--experimental-vision`**
  Whether to enable coordinate-based tools such as click_at(x,y). Usually requires a computer-use model able to produce accurate coordinates by looking at screenshots.
  - **Type:** boolean

- **`--experimentalMemory`/ `--experimental-memory`**
  Whether to enable experimental memory tools.
  - **Type:** boolean

- **`--experimentalStructuredContent`/ `--experimental-structured-content`**
  Whether to output structured formatted content.
  - **Type:** boolean

- **`--experimentalIncludeAllPages`/ `--experimental-include-all-pages`**
  Whether to include all kinds of pages such as webviews or background pages as pages.
  - **Type:** boolean

- **`--experimentalScreencast`/ `--experimental-screencast`**
  Exposes experimental screencast tools (requires ffmpeg). Install ffmpeg https://www.ffmpeg.org/download.html and ensure it is available in the MCP server PATH.
  - **Type:** boolean

- **`--experimentalFfmpegPath`/ `--experimental-ffmpeg-path`**
  Path to ffmpeg executable for screencast recording.
  - **Type:** string

- **`--categoryExperimentalWebmcp`/ `--category-experimental-webmcp`**
  Set to true to enable debugging WebMCP tools. Requires Chrome 149+ with the following flags: `--enable-features=WebMCPTesting,DevToolsWebMCPSupport`
  - **Type:** boolean

- **`--chromeArg`/ `--chrome-arg`**
  Additional arguments for Chrome. Only applies when Chrome is launched by chrome-devtools-mcp.
  - **Type:** array

- **`--ignoreDefaultChromeArg`/ `--ignore-default-chrome-arg`**
  Explicitly disable default arguments for Chrome. Only applies when Chrome is launched by chrome-devtools-mcp.
  - **Type:** array

- **`--categoryEmulation`/ `--category-emulation`**
  Set to false to exclude tools related to emulation.
  - **Type:** boolean
  - **Default:** `true`

- **`--categoryPerformance`/ `--category-performance`**
  Set to false to exclude tools related to performance.
  - **Type:** boolean
  - **Default:** `true`

- **`--categoryNetwork`/ `--category-network`**
  Set to false to exclude tools related to network.
  - **Type:** boolean
  - **Default:** `true`

- **`--categoryExtensions`/ `--category-extensions`**
  Set to true to include tools related to extensions. Note: This feature is currently only supported with a pipe connection. autoConnect, browserUrl, and wsEndpoint are not supported with this feature until 149 will be released.
  - **Type:** boolean
  - **Default:** `false`

- **`--categoryExperimentalThirdParty`/ `--category-experimental-third-party`**
  Set to true to enable third-party developer tools exposed by the inspected page itself
  - **Type:** boolean
  - **Default:** `false`

- **`--performanceCrux`/ `--performance-crux`**
  Set to false to disable sending URLs from performance traces to CrUX API to get field performance data.
  - **Type:** boolean
  - **Default:** `true`

- **`--usageStatistics`/ `--usage-statistics`**
  Set to false to opt-out of usage statistics collection. Google collects usage data to improve the tool, handled under the Google Privacy Policy (https://policies.google.com/privacy). This is independent from Chrome browser metrics. Disabled if `CHROME_DEVTOOLS_MCP_NO_USAGE_STATISTICS` or `CI` env variables are set.
  - **Type:** boolean
  - **Default:** `true`

- **`--slim`**
  Exposes a "slim" set of 3 tools covering navigation, script execution and screenshots only. Useful for basic browser tasks.
  - **Type:** boolean

- **`--redactNetworkHeaders`/ `--redact-network-headers`**
  If true, redacts some of the network headers considered sensitive before returning to the client.
  - **Type:** boolean
  - **Default:** `false`

<!-- END AUTO GENERATED OPTIONS -->

通过 JSON 配置中的 `args` 属性传递这些参数。例如：

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": [
        "chrome-devtools-mcp@latest",
        "--channel=canary",
        "--headless=true",
        "--isolated=true"
      ]
    }
  }
}
```

### 通过 WebSocket 连接并自定义头部

你可以直接连接到 Chrome WebSocket 端点，并在请求中包含自定义头部（例如用于身份验证）：

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": [
        "chrome-devtools-mcp@latest",
        "--wsEndpoint=ws://127.0.0.1:9222/devtools/browser/<id>",
        "--wsHeaders={\"Authorization\":\"Bearer YOUR_TOKEN\"}"
      ]
    }
  }
}
```

要从正在运行的 Chrome 实例获取 WebSocket 端点，请访问 `http://127.0.0.1:9222/json/version` 并查找 `webSocketDebuggerUrl` 字段。

你也可以运行 `npx chrome-devtools-mcp@latest --help` 查看所有可用的配置选项。

## 概念

### 并发会话

大多数 MCP 客户端为每次对话启动一个 Chrome DevTools MCP 服务器。如果你的客户端在并发 Agent 或子代理之间共享单个服务器实例，请使用 `--experimentalPageIdRouting` 启动服务器。这会在页面级工具中暴露 `pageId`，以便每个 Agent 将工具调用路由到其正在处理的标签页。

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": [
        "-y",
        "chrome-devtools-mcp@latest",
        "--experimentalPageIdRouting"
      ]
    }
  }
}
```

如果你运行多个独立的 MCP 客户端会话，并希望每个会话启动自己的临时 Chrome 配置文件，请同时传递 `--isolated`。这可以避免在这些服务器实例之间共享默认的 Chrome DevTools MCP 用户数据目录。

### 用户数据目录

`chrome-devtools-mcp` 使用以下用户数据目录启动 Chrome 的稳定版实例：

- Linux / macOS: `$HOME/.cache/chrome-devtools-mcp/chrome-profile-$CHANNEL`
- Windows: `%HOMEPATH%/.cache/chrome-devtools-mcp/chrome-profile-$CHANNEL`

该用户数据目录在运行之间不会清除，且所有 `chrome-devtools-mcp` 实例共享它。将 `isolated` 选项设置为 `true` 以改用临时用户数据目录，该目录将在浏览器关闭后自动清除。

### 连接到正在运行的 Chrome 实例

默认情况下，Chrome DevTools MCP 服务器将启动一个带有专用配置文件的新 Chrome 实例。这在某些场景下可能并非最佳选择：

- 如果你希望在手动站点测试和 Agent 驱动测试之间保持相同的应用程序状态。
- 当 MCP 需要登录网站时。某些账户在浏览器通过 WebDriver（Chrome DevTools MCP 服务器的默认启动机制）控制时会阻止登录。
- 如果你在沙盒环境中运行你的 LLM，但希望连接到在沙盒外部运行的 Chrome 实例。

在这些情况下，请先启动 Chrome，然后让 Chrome DevTools MCP 服务器连接至它。有两种实现方式：

- **自动连接（适用于 Chrome 144+）**：最适合在手动测试和 Agent 驱动测试之间共享状态。
- **通过远程调试端口手动连接**：最适合在沙盒环境中运行。

#### 自动连接到正在运行的 Chrome 实例

**步骤 1：** 在 Chrome 中设置远程调试

在 Chrome (\>= M144) 中，执行以下操作以设置远程调试：

1.  导航至 `chrome://inspect/#remote-debugging` 以启用远程调试。
2.  按照对话框 UI 允许或拒绝传入的调试连接。

**步骤 2：** 配置 Chrome DevTools MCP 服务器以自动连接到正在运行的 Chrome 实例

要将 `chrome-devtools-mcp` 服务器连接到正在运行的 Chrome 实例，请对 MCP 服务器使用 `--autoConnect` 命令行参数。

以下代码片段是 gemini-cli 的配置示例：

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["chrome-devtools-mcp@latest", "--autoConnect"]
    }
  }
}
```

**步骤 3：** 测试你的设置

确保浏览器正在运行。打开 gemini-cli 并运行以下提示词：

```none
Check the performance of https://developers.chrome.com
```

> [!NOTE]
> `<code>autoConnect</code>` 选项要求用户启动 Chrome。如果用户有多个活动配置文件，MCP 服务器将连接到默认配置文件（由 Chrome 确定）。MCP 服务器可访问所选配置文件的所有打开窗口。

Chrome DevTools MCP 服务器将尝试连接到你的正在运行的 Chrome 实例。它会显示一个请求用户权限的对话框。

点击**允许（Allow）**后，Chrome DevTools MCP 服务器将打开 [developers.chrome.com](http://developers.chrome.com) 并记录性能追踪数据。

#### 使用端口转发进行手动连接

你可以通过使用 `--browser-url` 选项连接到正在运行的 Chrome 实例。如果你在沙盒环境中运行 MCP 服务器且不允许启动新的 Chrome 实例，这将非常有用。

以下是如何连接到正在运行的 Chrome 实例的分步指南：

**步骤 1：配置 MCP 客户端**

将 `--browser-url` 选项添加到你的 MCP 客户端配置中。该选项的值应为正在运行的 Chrome 实例的 URL。`http://127.0.0.1:9222` 是常见的默认值。

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": [
        "chrome-devtools-mcp@latest",
        "--browser-url=http://127.0.0.1:9222"
      ]
    }
  }
}
```

**步骤 2：启动 Chrome 浏览器**

> [!WARNING]
> 启用远程调试端口会在正在运行的浏览器实例上打开一个调试端口。你机器上的任何应用程序都可以连接到此端口并控制浏览器。请确保在调试端口开启时不要浏览任何敏感网站。

以启用远程调试端口的方式启动 Chrome 浏览器。确保在启动带有调试端口的新的 Chrome 实例之前关闭所有正在运行的 Chrome 实例。你选择的端口号必须与你 MCP 客户端配置中 `--browser-url` 选项指定的端口相同。

出于安全原因，[Chrome 要求你在启用远程调试端口时使用非默认用户数据目录](https://developer.chrome.com/blog/remote-debugging-port)。你可以使用 `--user-data-dir` 标志指定自定义目录。这可以确保你的常规浏览配置文件和数据不会暴露给调试会话。

**macOS**

```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-profile-stable
```

**Linux**

```bash
/usr/bin/google-chrome --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-profile-stable
```

**Windows**

```bash
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="%TEMP%\chrome-profile-stable"
```

**步骤 3：测试你的设置**

配置好 MCP 客户端并启动 Chrome 浏览器后，你可以在 MCP 客户端中运行一个简单的提示词来测试设置：

```
Check the performance of https://developers.chrome.com
```

你的 MCP 客户端应连接到正在运行的 Chrome 实例并接收性能报告。

如果遇到 VM 到主机端口转发问题，请参见 [`docs/troubleshooting.md`](./docs/troubleshooting.md#remote-debugging-between-virtual-machine-vm-and-host-fails) 中的“虚拟机 (VM) 与主机之间的远程调试失败”部分。

有关远程调试的更多详细信息，请参阅 [Chrome DevTools 文档](https://developer.chrome.com/docs/devtools/remote-debugging/)。

### 在 Android 上调试 Chrome

请参阅[这些说明](./docs/debugging-android.md)。

## 已知限制

参见 [故障排除](./docs/troubleshooting.md)。