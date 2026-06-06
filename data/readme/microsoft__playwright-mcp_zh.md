## Playwright MCP

一个基于 [Playwright](https://playwright.dev) 提供浏览器自动化能力的模型上下文协议（Model Context Protocol, MCP）服务器。该服务器使大语言模型能够通过结构化的可访问性快照与网页进行交互，从而无需截图或视觉调优模型。

### Playwright MCP vs Playwright CLI

本软件包提供了对 Playwright 的 MCP 接口。如果你使用的是**编码智能体（coding agent）**，使用 [CLI+SKILLS](https://github.com/microsoft/playwright-cli) 可能会更有优势。

- **CLI**: 现代**编码智能体**越来越倾向于基于 CLI–的工作流，并将其作为 SKILLs 暴露出来，而不是 MCP，因为 CLI 调用的 token 效率更高：它们避免了将大型工具模式和冗长的可访问性树加载到模型上下文中，允许智能体通过简洁的专用命令进行操作。这使得 CLI + SKILLS 更适合于必须在有限的上下文窗口中平衡浏览器自动化、大型代码库、测试和推理的高吞吐量编码智能体。<br>**了解更多关于 [Playwright CLI with SKILLS](https://github.com/microsoft/playwright-cli)** 的信息。

- **MCP**: MCP 对于受益于持久状态、丰富的自省功能以及对页面结构进行迭代推理的专用智能体循环仍然具有相关性，例如探索性自动化、自愈测试或长期运行的自主工作流，在这些场景中维持持续的浏览器上下文比 token 成本问题更重要。

### 主要特性

- **快速且轻量**。使用 Playwright 的可访问性树，而非基于像素的输入。
- **对大语言模型友好**。无需视觉模型，完全基于结构化数据运行。
- **确定性的工具应用**。避免了基于截图的方法中常见的歧义问题。

### 要求
- Node.js 18 或更高版本
- VS Code、Cursor、Windsurf、Claude Desktop、Goose、Junie 或其他任何 MCP 客户端

<!--
// Generate using:
node utils/generate-links.js
-->

### 入门指南

首先，在你的客户端中安装 Playwright MCP 服务器。

**标准配置**适用于大多数工具：

```js
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ]
    }
  }
}
```

[<img src="https://img.shields.io/badge/VS_Code-VS_Code?style=flat-square&label=Install%20Server&color=0098FF" alt="在 VS Code 中安装">](https://insiders.vscode.dev/redirect?url=vscode%3Amcp%2Finstall%3F%257B%2522name%2522%253A%2522playwright%2522%252C%2522command%2522%253A%2522npx%2522%252C%2522args%2522%253A%255B%2522%2540playwright%252Fmcp%2540latest%2522%255D%257D) [<img alt="在 VS Code Insiders 中安装" src="https://img.shields.io/badge/VS_Code_Insiders-VS_Code_Insiders?style=flat-square&label=Install%20Server&color=24bfa5">](https://insiders.vscode.dev/redirect?url=vscode-insiders%3Amcp%2Finstall%3F%257B%2522name%2522%253A%2522playwright%2522%252C%2522command%2522%253A%2522npx%2522%252C%2522args%2522%253A%255B%2522%2540playwright%252Fmcp%2540latest%2522%255D%257D)

<details>
<summary>Amp</summary>

通过 Amp VS Code 扩展设置屏幕添加，或通过更新你的 `settings.json` 文件：

```json
"amp.mcpServers": {
  "playwright": {
    "command": "npx",
    "args": [
      "@playwright/mcp@latest"
    ]
  }
}
```

**Amp CLI 设置：**

通过以下 `amp mcp add` 命令添加：

```bash
amp mcp add playwright -- npx @playwright/mcp@latest
```

</details>

<details>
<summary>Antigravity</summary>

通过 Antigravity 设置或更新你的配置文件添加：

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ]
    }
  }
}
```

</details>

<details>
<summary>Claude Code</summary>

使用 Claude Code CLI 添加 Playwright MCP 服务器：

```bash
claude mcp add playwright npx @playwright/mcp@latest
```
</details>

<details>
<summary>Claude Desktop</summary>

遵循 MCP 安装 [指南](https://modelcontextprotocol.io/quickstart/user)，使用上面的标准配置。

</details>

<details>
<summary>Cline</summary>

请按照 [配置 MCP 服务器](https://docs.cline.bot/mcp/configuring-mcp-servers) 部分中的说明进行操作。

**示例：本地设置**

将以下内容添加到你的 [`cline_mcp_settings.json`](https://docs.cline.bot/mcp/configuring-mcp-servers#editing-mcp-settings-files) 文件中：

```json
{
  "mcpServers": {
    "playwright": {
      "type": "stdio",
      "command": "npx",
      "timeout": 30,
      "args": [
        "-y",
        "@playwright/mcp@latest"
      ],
      "disabled": false
    }
  }
}
```

</details>

<details>
<summary>Codex</summary>

使用 Codex CLI 添加 Playwright MCP 服务器：

```bash
codex mcp add playwright npx "@playwright/mcp@latest"
```

或者，创建或编辑配置文件 `~/.codex/config.toml` 并添加：

```toml
[mcp_servers.playwright]
command = "npx"
args = ["@playwright/mcp@latest"]
```

更多信息，请参阅 [Codex MCP 文档](https://github.com/openai/codex/blob/main/codex-rs/config.md#mcp_servers)。

</details>

<details>
<summary>Copilot</summary>

使用 Copilot CLI 交互式添加 Playwright MCP 服务器：

```bash
/mcp add
```

或者，创建或编辑配置文件 `~/.copilot/mcp-config.json` 并添加：

```json
{
  "mcpServers": {
    "playwright": {
      "type": "local",
      "command": "npx",
      "tools": [
        "*"
      ],
      "args": [
        "@playwright/mcp@latest"
      ]
    }
  }
}
```

更多信息，请参阅 [Copilot CLI 文档](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli)。

</details>

<details>
<summary>Cursor</summary>

#### 点击按钮安装：

[<img src="https://cursor.com/deeplink/mcp-install-dark.svg" alt="在 Cursor 中安装">](https://cursor.com/en/install-mcp?name=Playwright&config=eyJjb21tYW5kIjoibnB4IEBwbGF5d3JpZ2h0L21jcEBsYXRlc3QifQ%3D%3D)

#### 或者手动安装：

前往 `Cursor Settings` -> `MCP` -> `Add new MCP Server`。名称随你喜欢，使用 `command` 类型并输入命令 `npx @playwright/mcp@latest`。你也可以通过点击 `Edit` 来验证配置或添加命令行参数。

</details>

<details>
<summary>Factory</summary>

使用 Factory CLI 添加 Playwright MCP 服务器：

```bash
droid mcp add playwright "npx @playwright/mcp@latest"
```

或者，在 Factory droid 中输入 `/mcp` 以打开用于管理 MCP 服务器的交互式 UI。

更多信息，请参阅 [Factory MCP 文档](https://docs.factory.ai/cli/configuration/mcp)。

</details>

<details>
<summary>Gemini CLI</summary>

遵循 MCP 安装 [指南](https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md#configure-the-mcp-server-in-settingsjson)，使用上面的标准配置。

</details>

<details>
<summary>Goose</summary>

#### 点击按钮安装：

[![在 Goose 中安装](https://block.github.io/goose/img/extension-install-dark.svg)](https://block.github.io/goose/extension?cmd=npx&arg=%40playwright%2Fmcp%40latest&id=playwright&name=Playwright&description=Interact%20with%20web%20pages%20through%20structured%20accessibility%20snapshots%20using%20Playwright)

#### 或者手动安装：

前往 `Advanced settings` -> `Extensions` -> `Add custom extension`。名称随你喜欢，使用类型 `STDIO`，并将 `command` 设置为 `npx @playwright/mcp`。点击 "Add Extension"。
</details>

<details>
<summary>Junie</summary>

要在 Junie CLI 中添加 Playwright MCP 服务器：

1. 输入 `/mcp`
2. 按 `Ctrl+A` 添加新的 MCP 服务器
3. 从列表中选择 **Playwright**

或者，添加到 `.junie/mcp/mcp.json`：

```json
{
  "mcpServers": {
    "Playwright": {
      "command": "npx",
      "args": [
        "-y",
        "@playwright/mcp@latest"
      ]
    }
  }
}
```

更多信息，请参阅 [Junie MCP 配置文档](https://junie.jetbrains.com/docs/junie-cli-mcp-configuration.html)。

</details>

<details>
<summary>Kiro</summary>

[![添加到 Kiro](https://kiro.dev/images/add-to-kiro.svg)](https://kiro.dev/launch/mcp/add?name=playwright&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22%40playwright%2Fmcp%40latest%22%5D%7D)

遵循 MCP 服务器 [文档](https://kiro.dev/docs/mcp/)。例如在 `.kiro/settings/mcp.json` 中：

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ]
    }
  }
}
```
</details>

<details>
<summary>LM Studio</summary>

#### 点击按钮安装：

[![添加 MCP Server playwright 到 LM Studio](https://files.lmstudio.ai/deeplink/mcp-install-light.svg)](https://lmstudio.ai/install-mcp?name=playwright&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyJAcGxheXdyaWdodC9tY3BAbGF0ZXN0Il19)

#### 或者手动安装：

前往右侧边栏的 `Program` -> `Install` -> `Edit mcp.json`。使用上面的标准配置。
</details>

<details>
<summary>opencode</summary>

遵循 MCP 服务器 [文档](https://opencode.ai/docs/mcp-servers/)。例如在 `~/.config/opencode/opencode.json` 中：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "playwright": {
      "type": "local",
      "command": [
        "npx",
        "@playwright/mcp@latest"
      ],
      "enabled": true
    }
  }
}

```
</details>

<details>
<summary>Qodo Gen</summary>

在 VSCode 或 IntelliJ 中打开 [Qodo Gen](https://docs.qodo.ai/qodo-documentation/qodo-gen) 聊天面板 → Connect more tools → + Add new MCP → 粘贴上面的标准配置。

点击 <code>Save</code>。
</details>

<details>
<summary>VS Code</summary>

#### 点击按钮安装：

[<img src="https://img.shields.io/badge/VS_Code-VS_Code?style=flat-square&label=Install%20Server&color=0098FF" alt="在 VS Code 中安装">](https://insiders.vscode.dev/redirect?url=vscode%3Amcp%2Finstall%3F%257B%2522name%2522%253A%2522playwright%2522%252C%2522command%2522%253A%2522npx%2522%252C%2522args%2522%253A%255B%2522%2540playwright%252Fmcp%2540latest%2522%255D%257D) [<img alt="在 VS Code Insiders 中安装" src="https://img.shields.io/badge/VS_Code_Insiders-VS_Code_Insiders?style=flat-square&label=Install%20Server&color=24bfa5">](https://insiders.vscode.dev/redirect?url=vscode-insiders%3Amcp%2Finstall%3F%257B%2522name%2522%253A%2522playwright%2522%252C%2522command%2522%253A%2522npx%2522%252C%2522args%2522%253A%255B%2522%2540playwright%252Fmcp%2540latest%2522%255D%257D)

#### 或者手动安装：

遵循 MCP 安装 [指南](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_add-an-mcp-server)，使用上面的标准配置。你也可以使用 VS Code CLI 安装 Playwright MCP 服务器：

```bash
# For VS Code
code --add-mcp '{"name":"playwright","command":"npx","args":["@playwright/mcp@latest"]}'
```

安装完成后，Playwright MCP 服务器将在 VS Code 中与你的 GitHub Copilot 智能体一起使用。
</details>

<details>
<summary>Warp</summary>

前往 `Settings` -> `AI` -> `Manage MCP Servers` -> `+ Add` 以 [添加 MCP 服务器](https://docs.warp.dev/knowledge-and-collaboration/mcp#adding-an-mcp-server)。使用上面的标准配置。

或者，在 Warp 提示符中使用斜杠命令 `/add-mcp` 并粘贴上面的标准配置：
```js
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ]
    }
  }
}
```

</details>

<details>
<summary>Windsurf</summary>

遵循 Windsurf MCP [文档](https://docs.windsurf.com/windsurf/cascade/mcp)。使用上面的标准配置。

</details>

### 配置

Playwright MCP 服务器支持以下参数。它们可以在上面的 JSON 配置中作为 `"args"` 列表的一部分提供：

<!--- Options generated by update-readme.js -->

| 选项 | 描述 |
|--------|-------------|
| --allowed-hosts <hosts...> | 允许该服务器提供服务的域名逗号分隔列表。默认为服务器绑定的主机。传递 '*' 以禁用主机检查。<br>*环境变量* `PLAYWRIGHT_MCP_ALLOWED_HOSTS` |
| --allowed-origins <origins> | 分号分隔的信任来源列表，允许浏览器请求。默认是允许所有。重要提示：*不*作为安全边界，也*不影响*重定向。<br>*环境变量* `PLAYWRIGHT_MCP_ALLOWED_ORIGINS` |
| --allow-unrestricted-file-access | 允许访问工作区根目录之外的文件。还允许对 file:// URL 的无限制访问。默认情况下，文件系统访问仅限于工作区根目录（如果未配置根目录则为 cwd），并且阻止导航到 file:// URL。<br>*环境变量* `PLAYWRIGHT_MCP_ALLOW_UNRESTRICTED_FILE_ACCESS` |
| --blocked-origins <origins> | 分号分隔的域名列表，用于阻止浏览器请求。黑名单在允许列表之前进行评估。如果未与允许列表一起使用，则不匹配黑名单的请求仍然被允许。重要提示：*不*作为安全边界，也*不影响*重定向。<br>*环境变量* `PLAYWRIGHT_MCP_BLOCKED_ORIGINS` |
| --block-service-workers | 阻止服务工作者<br>*环境变量* `PLAYWRIGHT_MCP_BLOCK_SERVICE_WORKERS` |
| --browser <browser> | 要使用的浏览器或 chrome 通道，可能的值：chrome, firefox, webkit, msedge。<br>*环境变量* `PLAYWRIGHT_MCP_BROWSER` |
| --caps <caps> | 逗号分隔的附加功能列表以启用，可能的值：vision, pdf, devtools。<br>*环境变量* `PLAYWRIGHT_MCP_CAPS` |
| --cdp-endpoint <endpoint> | 要连接的 CDP 端点。<br>*环境变量* `PLAYWRIGHT_MCP_CDP_ENDPOINT` |
| --cdp-header <headers...> | 随连接请求发送的 CDP 头，可以指定多个。<br>*环境变量* `PLAYWRIGHT_MCP_CDP_HEADER` |
| --cdp-timeout <timeout> | 连接到 CDP 端点的超时时间（毫秒），默认为 30000ms<br>*环境变量* `PLAYWRIGHT_MCP_CDP_TIMEOUT` |
| --codegen <lang> | 指定用于代码生成的语言，可能的值："typescript", "none"。默认为 "typescript"。<br>*环境变量* `PLAYWRIGHT_MCP_CODEGEN` |
| --config <path> | 配置文件的路径。<br>*环境变量* `PLAYWRIGHT_MCP_CONFIG` |
| --console-level <level> | 要返回的控制台消息级别："error", "warning", "info", "debug"。每个级别包含更严重级别的 message。<br>*环境变量* `PLAYWRIGHT_MCP_CONSOLE_LEVEL` |
| --device <device> | 模拟的设备，例如："iPhone 15"<br>*环境变量* `PLAYWRIGHT_MCP_DEVICE` |
| --executable-path <path> | 浏览器可执行文件的路径。<br>*环境变量* `PLAYWRIGHT_MCP_EXECUTABLE_PATH` |
| --extension | 连接到正在运行的浏览器实例（仅限 Edge/Chrome）。需要安装 "Playwright Extension"。<br>*环境变量* `PLAYWRIGHT_MCP_EXTENSION` |
| --endpoint <endpoint> | 要连接的绑定浏览器端点。<br>*环境变量* `PLAYWRIGHT_MCP_ENDPOINT` |
| --grant-permissions <permissions...> | 授予浏览器上下文的权限列表，例如 "geolocation", "clipboard-read", "clipboard-write"。<br>*环境变量* `PLAYWRIGHT_MCP_GRANT_PERMISSIONS` |
| --headless | 在无头模式下运行浏览器，默认为有头模式<br>*环境变量* `PLAYWRIGHT_MCP_HEADLESS` |
| --host <host> | 服务器绑定的主机。默认为 localhost。使用 0.0.0.0 绑定到所有接口。<br>*环境变量* `PLAYWRIGHT_MCP_HOST` |
| --ignore-https-errors | 忽略 https 错误<br>*环境变量* `PLAYWRIGHT_MCP_IGNORE_HTTPS_ERRORS` |
| --init-page <path...> | 要在 Playwright page object 上评估的 TypeScript 文件路径。<br>*环境变量* `PLAYWRIGHT_MCP_INIT_PAGE` |
| --init-script <path...> | 要添加为初始化脚本的 JavaScript 文件路径。该脚本将在任何页面脚本之前在每个页面上进行评估。可以指定多次。<br>*环境变量* `PLAYWRIGHT_MCP_INIT_SCRIPT` |
| --isolated | 将浏览器配置文件保留在内存中，不保存到磁盘。<br>*环境变量* `PLAYWRIGHT_MCP_ISOLATED` |
| --image-responses <mode> | 是否向客户端发送图像响应。可以是 "allow" 或 "omit"，默认为 "allow"。<br>*环境变量* `PLAYWRIGHT_MCP_IMAGE_RESPONSES` |
| --no-sandbox | 禁用所有通常沙盒化的进程类型的沙箱。<br>*环境变量* `PLAYWRIGHT_MCP_NO_SANDBOX` |
| --output-dir <path> | 输出文件目录的路径。<br>*环境变量* `PLAYWRIGHT_MCP_OUTPUT_DIR` |
| --output-mode <mode> | 是否将快照、控制台消息、网络日志保存到文件或标准输出。可以是 "file" 或 "stdout"。默认为 "stdout"。<br>*环境变量* `PLAYWRIGHT_MCP_OUTPUT_MODE` |
| --port <port> | 用于 SSE 传输的监听端口。<br>*环境变量* `PLAYWRIGHT_MCP_PORT` |
| --proxy-bypass <bypass> | 逗号分隔的要绕过代理的域名，例如 ".com,chromium.org,.domain.com"<br>*环境变量* `PLAYWRIGHT_MCP_PROXY_BYPASS` |
| --proxy-server <proxy> | 指定代理服务器，例如 "http://myproxy:3128" 或 "socks5://myproxy:8080"<br>*环境变量* `PLAYWRIGHT_MCP_PROXY_SERVER` |
| --sandbox | 启用所有通常不沙盒化的进程类型的沙箱。<br>*环境变量* `PLAYWRIGHT_MCP_SANDBOX` |
| --save-session | 是否将 Playwright MCP 会话保存到输出目录中。<br>*环境变量* `PLAYWRIGHT_MCP_SAVE_SESSION` |
| --secrets <path> | 包含 dotenv 格式密钥的文件路径<br>*环境变量* `PLAYWRIGHT_MCP_SECRETS_FILE` |
| --shared-browser-context | 在所有连接的 HTTP 客户端之间重用相同的浏览器上下文。<br>*环境变量* `PLAYWRIGHT_MCP_SHARED_BROWSER_CONTEXT` |
| --snapshot-mode <mode> | 在生成响应快照时，指定要使用的模式。可以是 "full" 或 "none"。默认为 "full"。<br>*环境变量* `PLAYWRIGHT_MCP_SNAPSHOT_MODE` |
| --storage-state <path> | 用于隔离会话的存储状态文件路径。<br>*环境变量* `PLAYWRIGHT_MCP_STORAGE_STATE` |
| --test-id-attribute <attribute> | 指定要使用的测试 ID 属性，默认为 "data-testid"<br>*环境变量* `PLAYWRIGHT_MCP_TEST_ID_ATTRIBUTE` |
| --timeout-action <timeout> | 指定操作超时时间（毫秒），默认为 5000ms<br>*环境变量* `PLAYWRIGHT_MCP_TIMEOUT_ACTION` |
| --timeout-navigation <timeout> | 指定导航超时时间（毫秒），默认为 60000ms<br>*环境变量* `PLAYWRIGHT_MCP_TIMEOUT_NAVIGATION` |
| --user-agent <ua string> | 指定用户代理字符串<br>*环境变量* `PLAYWRIGHT_MCP_USER_AGENT` |
| --user-data-dir <path> | 用户数据目录的路径。如果未指定，将创建一个临时目录。<br>*环境变量* `PLAYWRIGHT_MCP_USER_DATA_DIR` |
| --viewport-size <size> | 指定浏览器视口大小（像素），例如 "1280x720"<br>*环境变量* `PLAYWRIGHT_MCP_VIEWPORT_SIZE` |

<!--- End of options generated section -->

### 用户配置文件

你可以像普通浏览器一样使用持久化配置运行 Playwright MCP，在隔离上下文中进行测试会话，或使用浏览器扩展连接到现有浏览器。

**持久化配置 (Persistent profile)**

所有登录信息都将存储在持久化配置中，如果你想清除离线状态，可以在会话之间删除它。
持久化配置位于以下位置，你可以使用 `--user-data-dir` 参数覆盖它。

```bash
# Windows
%USERPROFILE%\AppData\Local\ms-playwright\mcp-{channel}-{workspace-hash}

# macOS
- ~/Library/Caches/ms-playwright/mcp-{channel}-{workspace-hash}

# Linux
- ~/.cache/ms-playwright/mcp-{channel}-{workspace-hash}
```

`{workspace-hash}` 源自 MCP 客户端的工作区根目录，因此不同项目会自动获得单独的配置文件。

> [!IMPORTANT]
> 持久化配置一次只能被一个浏览器实例使用，因此共享相同工作区的并发 MCP 客户端会发生冲突。要并行运行多个客户端，请启动每个额外的客户端并使用 `--isolated` 或指向不同的 `--user-data-dir`。

**隔离模式 (Isolated)**

在隔离模式下，每次会话都在隔离配置中启动。每次你要求 MCP 关闭浏览器时，
会话就会关闭，并且该会话的所有存储状态都会丢失。你可以提供初始存储状态
通过配置的 `contextOptions` 或通过 `--storage-state` 参数传递给浏览器。了解更多关于存储
状态的信息 [在此处](https://playwright.dev/docs/auth)。

```js
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest",
        "--isolated",
        "--storage-state={path/to/storage.json}"
      ]
    }
  }
}
```

**浏览器扩展 (Browser Extension)**

Playwright MCP Chrome 扩展允许你连接到现有的浏览器标签页并利用你的登录会话和浏览器状态。请参阅 [microsoft/playwright › packages/extension](https://github.com/microsoft/playwright/tree/main/packages/extension#readme) 以获取安装和设置说明。

### 初始状态

有多种方法可以向浏览器上下文或页面提供初始状态。

对于存储状态，你可以：
- 使用 `--user-data-dir` 参数从用户数据目录开始。这将使所有浏览器数据在会话之间持久化。
- 使用 `--storage-state` 参数从存储状态文件开始。这会将 cookies 和本地存储从文件加载到隔离的浏览器上下文中。

对于页面状态，你可以使用：

- `--init-page` 指向一个 TypeScript 文件，该文件将在 Playwright page object 上评估。这允许你运行任意代码来设置页面。

```ts
// init-page.ts
export default async ({ page }) => {
  await page.context().grantPermissions(['geolocation']);
  await page.context().setGeolocation({ latitude: 37.7749, longitude: -122.4194 });
  await page.setViewportSize({ width: 1280, height: 720 });
};
```

- `--init-script` 指向一个 JavaScript 文件，该文件将作为初始化脚本添加。该脚本将在任何页面脚本之前在每个页面上进行评估。
这对于覆盖浏览器 API 或设置环境非常有用。

```js
// init-script.js
window.isPlaywrightMCP = true;
```

### 配置文件

Playwright MCP 服务器可以使用 JSON 配置文件进行配置。你可以使用 `--config` 命令行选项指定配置文件：

```bash
npx @playwright/mcp@latest --config path/to/config.json
```

<details>
<summary>配置文件模式</summary>

<!--- Config generated by update-readme.js -->

```typescript
{
  /**
   * The browser to use.
   */
  browser?: {
    /**
     * The type of browser to use.
     */
    browserName?: 'chromium' | 'firefox' | 'webkit';

    /**
     * Keep the browser profile in memory, do not save it to disk.
     */
    isolated?: boolean;

    /**
     * Path to a user data directory for browser profile persistence.
     * Temporary directory is created by default.
     */
    userDataDir?: string;

    /**
     * Launch options passed to
     * @see https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context
     *
     * This is useful for settings options like `channel`, `headless`, `executablePath`, etc.
     */
    launchOptions?: playwright.LaunchOptions;

    /**
     * Context options for the browser context.
     *
     * This is useful for settings options like `viewport`.
     */
    contextOptions?: playwright.BrowserContextOptions;

    /**
     * Chrome DevTools Protocol endpoint to connect to an existing browser instance in case of Chromium family browsers.
     */
    cdpEndpoint?: string;

    /**
     * CDP headers to send with the connect request.
     */
    cdpHeaders?: Record<string, string>;

    /**
     * Timeout in milliseconds for connecting to CDP endpoint. Defaults to 30000 (30 seconds). Pass 0 to disable timeout.
     */
    cdpTimeout?: number;

    /**
     * Remote endpoint to connect to an existing Playwright server.
     */
    remoteEndpoint?: string;

    /**
     * Paths to TypeScript files to add as initialization scripts for Playwright page.
     */
    initPage?: string[];

    /**
     * Paths to JavaScript files to add as initialization scripts.
     * The scripts will be evaluated in every page before any of the page's scripts.
     */
    initScript?: string[];
  },

  /**
   * Connect to a running browser instance (Edge/Chrome only). If specified, `browser`
   * config is ignored.
   * Requires the "Playwright Extension" to be installed.
   */
  extension?: boolean;

  server?: {
    /**
     * The port to listen on for SSE or MCP transport.
     */
    port?: number;

    /**
     * The host to bind the server to. Default is localhost. Use 0.0.0.0 to bind to all interfaces.
     */
    host?: string;

    /**
     * The hosts this server is allowed to serve from. Defaults to the host server is bound to.
     * This is not for CORS, but rather for the DNS rebinding protection.
     */
    allowedHosts?: string[];
  },

  /**
   * List of enabled tool capabilities. Possible values:
   *   - 'core': Core browser automation features.
   *   - 'pdf': PDF generation and manipulation.
   *   - 'vision': Coordinate-based interactions.
   *   - 'devtools': Developer tools features.
   */
  capabilities?: ToolCapability[];

  /**
   * Whether to save the Playwright session into the output directory.
   */
  saveSession?: boolean;

  /**
   * Reuse the same browser context between all connected HTTP clients.
   */
  sharedBrowserContext?: boolean;

  /**
   * Secrets are used to replace matching plain text in the tool responses to prevent the LLM
   * from accidentally getting sensitive data. It is a convenience and not a security feature,
   * make sure to always examine information coming in and from the tool on the client.
   */
  secrets?: Record<string, string>;

  /**
   * The directory to save output files.
   */
  outputDir?: string;

  console?: {
    /**
     * The level of console messages to return. Each level includes the messages of more severe levels. Defaults to "info".
     */
    level?: 'error' | 'warning' | 'info' | 'debug';
  },

  network?: {
    /**
     * List of origins to allow the browser to request. Default is to allow all. Origins matching both `allowedOrigins` and `blockedOrigins` will be blocked.
     *
     * Supported formats:
     * - Full origin: `https://example.com:8080` - matches only that origin
     * - Wildcard port: `http://localhost:*` - matches any port on localhost with http protocol
     */
    allowedOrigins?: string[];

    /**
     * List of origins to block the browser to request. Origins matching both `allowedOrigins` and `blockedOrigins` will be blocked.
     *
     * Supported formats:
     * - Full origin: `https://example.com:8080` - matches only that origin
     * - Wildcard port: `http://localhost:*` - matches any port on localhost with http protocol
     */
    blockedOrigins?: string[];
  };

  /**
   * Specify the attribute to use for test ids, defaults to "data-testid".
   */
  testIdAttribute?: string;

  timeouts?: {
    /*
     * Configures default action timeout: https://playwright.dev/docs/api/class-page#page-set-default-timeout. Defaults to 5000ms.
     */
    action?: number;

    /*
     * Configures default navigation timeout: https://playwright.dev/docs/api/class-page#page-set-default-navigation-timeout. Defaults to 60000ms.
     */
    navigation?: number;

    /**
     * Configures default expect timeout: https://playwright.dev/docs/test-timeouts#expect-timeout. Defaults to 5000ms.
     */
    expect?: number;
  };

  /**
   * Whether to send image responses to the client. Can be "allow", "omit", or "auto". Defaults to "auto", which sends images if the client can display them.
   */
  imageResponses?: 'allow' | 'omit';

  snapshot?: {
    /**
     * When taking snapshots for responses, specifies the mode to use.
     */
    mode?: 'full' | 'none';
  };

  /**
   * allowUnrestrictedFileAccess acts as a guardrail to prevent the LLM from accidentally
   * wandering outside its intended workspace. It is a convenience defense to catch unintended
   * file access, not a secure boundary; a deliberate attempt to reach other directories can be
   * easily worked around, so always rely on client-level permissions for true security.
   */
  allowUnrestrictedFileAccess?: boolean;

  /**
   * Specify the language to use for code generation.
   */
  codegen?: 'typescript' | 'none';
}
```

<!--- End of config generated section -->

</details>

### 独立 MCP 服务器

当在无显示器的系统上或有 IDE 的 worker 进程中运行有头浏览器时，
从具有 DISPLAY 的环境中运行 MCP 服务器并传递 `--port` 标志以启用 HTTP 传输。

```bash
npx @playwright/mcp@latest --port 8931
```

然后在 MCP 客户端配置中，将 `url` 设置为 HTTP 端点：

```js
{
  "mcpServers": {
    "playwright": {
      "url": "http://localhost:8931/mcp"
    }
  }
}
```

## 安全性

Playwright MCP **不是**安全边界。请参阅 [MCP 安全最佳实践](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices) 以获取保护部署的指导。

<details>
<summary><b>Docker</b></summary>

**注意：** Docker 实现目前仅支持无头 chromium。

```js
{
  "mcpServers": {
    "playwright": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "--init", "--pull=always", "mcr.microsoft.com/playwright/mcp"]
    }
  }
}
```

或者，如果你更喜欢将容器作为长期运行的服务运行，而不是让 MCP 客户端生成它，请使用：

```
docker run -d -i --rm --init --pull=always \
  --entrypoint node \
  --name playwright \
  -p 8931:8931 \
  mcr.microsoft.com/playwright/mcp \
  /app/cli.js --headless --browser chromium --no-sandbox --port 8931 --host 0.0.0.0
```

服务器将在主机端口 **8931** 上监听，任何 MCP 客户端都可以访问。  

你可以自己构建 Docker 镜像。

```
docker build -t mcr.microsoft.com/playwright/mcp .
```
</details>

<details>
<summary><b>编程式用法</b></summary>

```js
import http from 'http';

import { createConnection } from '@playwright/mcp';
import { SSEServerTransport } from '@modelcontextprotocol/sdk/server/sse.js';

http.createServer(async (req, res) => {
  // ...

  // Creates a headless Playwright MCP server with SSE transport
  const connection = await createConnection({ browser: { launchOptions: { headless: true } } });
  const transport = new SSEServerTransport('/messages', res);
  await connection.connect(transport);

  // ...
});
```
</details>

### 工具

<!--- Tools generated by update-readme.js -->

<details>
<summary><b>核心自动化 (Core automation)</b></summary>

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_click**
  - Title: 点击
  - Description: 在网页上执行点击操作
  - Parameters:
    - `element` (string, optional): 用于获取与元素交互权限的人类可读元素描述
    - `target` (string): 来自页面快照的确切目标元素引用，或唯一元素选择器
    - `doubleClick` (boolean, optional): 是否执行双击而不是单击
    - `button` (string, optional): 要点击的按钮，默认为左键
    - `modifiers` (array, optional): 要按下的修饰键
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_close**
  - Title: 关闭浏览器
  - Description: 关闭页面
  - Parameters: None
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_console_messages**
  - Title: 获取控制台消息
  - Description: 返回所有控制台消息
  - Parameters:
    - `level` (string): 要返回的控制台消息级别。每个级别包含更严重级别的 message。默认为 "info"。
    - `all` (boolean, optional): 返回自会话开始以来的所有控制台消息，而不仅仅是上次导航后的消息。默认为 false。
    - `filename` (string, optional): 保存控制台消息的文件名。如果未提供，则作为文本返回 message。
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_drag**
  - Title: 拖动鼠标
  - Description: 在两个元素之间执行拖放操作
  - Parameters:
    - `startElement` (string, optional): 用于获取与源元素交互权限的人类可读描述
    - `startTarget` (string): 来自页面快照的确切目标元素引用，或唯一元素选择器
    - `endElement` (string, optional): 用于获取与目标元素交互权限的人类可读描述
    - `endTarget` (string): 来自页面快照的确切目标元素引用，或唯一元素选择器
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_drop**
  - Title: 将文件或数据拖放到元素上
  - Description: 将文件或将 MIME 类型的数据拖放到元素上，就像从页面外部拖动一样。必须提供 "paths" 或 "data" 中的至少一个。
  - Parameters:
    - `element` (string, optional): 用于获取与元素交互权限的人类可读元素描述
    - `target` (string): 来自页面快照的确切目标元素引用，或唯一元素选择器
    - `paths` (array, optional): 要拖放到元素上的文件的绝对路径。
    - `data` (object, optional): 要拖放的数据，作为 MIME 类型到字符串值的映射（例如 {"text/plain": "hello", "text/uri-list": "https://example.com"}）。
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_evaluate**
  - Title: 评估 JavaScript
  - Description: 在页面或元素上评估 JavaScript 表达式
  - Parameters:
    - `element` (string, optional): 用于获取与元素交互权限的人类可读元素描述
    - `target` (string, optional): 来自页面快照的确切目标元素引用，或唯一元素选择器
    - `function` (string): () => { /* code */ } 或 (element) => { /* code */ }（当提供 element 时）
    - `filename` (string, optional): 保存结果的文件名。如果未提供，则作为文本返回 result。
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_file_upload**
  - Title: 上传文件
  - Description: 上传一个或多个文件
  - Parameters:
    - `paths` (array, optional): 要上传的文件的绝对路径。可以是单个文件或多个文件。如果省略，则取消文件选择器。
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_fill_form**
  - Title: 填写表单
  - Description: 填写多个表单字段
  - Parameters:
    - `fields` (array): 要填写的字段
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_handle_dialog**
  - Title: 处理对话框
  - Description: 处理对话框
  - Parameters:
    - `accept` (boolean): 是否接受对话框。
    - `promptText` (string, optional): 提示对话框中的提示文本。
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_hover**
  - Title: 悬停鼠标
  - Description: 在页面上的元素上悬停
  - Parameters:
    - `element` (string, optional): 用于获取与元素交互权限的人类可读元素描述
    - `target` (string): 来自页面快照的确切目标元素引用，或唯一元素选择器
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_navigate**
  - Title: 导航至 URL
  - Description: 导航到 URL
  - Parameters:
    - `url` (string): 要导航到的 URL
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_navigate_back**
  - Title: 后退
  - Description: 返回到历史记录中的上一页
  - Parameters: None
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_network_request**
  - Title: 显示网络请求详情
  - Description: 返回单个网络请求的完整详情（headers 和 body），或者如果设置了 `part`，则返回一部分。使用 browser_network_requests 中的数字。
  - Parameters:
    - `index` (integer): 1-based 索引，由 browser_network_requests 打印。
    - `part` (string, optional): 仅返回请求的这部分。省略以返回完整详情。
    - `filename` (string, optional): 保存结果的文件名。如果未提供，则作为文本输出 result。
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_network_requests**
  - Title: 列出网络请求
  - Description: 返回自加载页面以来的编号网络请求列表。使用 browser_network_request 和数字获取完整详情。
  - Parameters:
    - `static` (boolean): 是否包含成功的静态资源，如图像、字体、脚本等。默认为 false。
    - `filter` (string, optional): 仅返回 URL 与此正则表达式匹配的请求（例如 "/api/.*user"）。
    - `filename` (string, optional): 保存网络请求的文件名。如果未提供，则作为文本返回 requests。
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_press_key**
  - Title: 按下键
  - Description: 在键盘上按下键
  - Parameters:
    - `key` (string): 要按下的键的名称或生成的字符，例如 `ArrowLeft` 或 `a`
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_resize**
  - Title: 调整浏览器窗口大小
  - Description: 调整浏览器窗口大小
  - Parameters:
    - `width` (number): 浏览器窗口的宽度
    - `height` (number): 浏览器窗口的高度
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_run_code_unsafe**
  - Title: 运行 Playwright 代码（不安全）
  - Description: 运行 Playwright 代码片段。不安全：在 Playwright 服务器进程中执行任意 JavaScript，相当于 RCE。
  - Parameters:
    - `code` (string, optional): 包含要执行的 Playwright 代码的 JavaScript 函数。它将被调用并带有一个参数 page，你可以用它进行任何页面交互。例如：`async (page) => { await page.getByRole('button', { name: 'Submit' }).click(); return await page.title(); }`
    - `filename` (string, optional): 从指定文件加载代码。如果同时提供了 code 和 filename，则忽略 code。
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_select_option**
  - Title: 选择选项
  - Description: 在下拉菜单中选择一个选项
  - Parameters:
    - `element` (string, optional): 用于获取与元素交互权限的人类可读元素描述
    - `target` (string): 来自页面快照的确切目标元素引用，或唯一元素选择器
    - `values` (array): 要在下拉菜单中选择的值数组。这可以是单个值或多个值。
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_snapshot**
  - Title: 页面快照
  - Description: 捕获当前页面的可访问性快照，这比截图更好
  - Parameters:
    - `target` (string, optional): 来自页面快照的确切目标元素引用，或唯一元素选择器
    - `filename` (string, optional): 将快照保存到 markdown 文件而不是在响应中返回。
    - `depth` (number, optional): 限制快照树的深度
    - `boxes` (boolean, optional): 在快照中包含每个元素的边界框 [box=x,y,width,height]。坐标是视口相关的，以 CSS 像素为单位（Element.getBoundingClientRect）
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_take_screenshot**
  - Title: 截图
  - Description: 截取当前页面的屏幕截图。你不能基于截图执行操作，请使用 browser_snapshot 进行操作。
  - Parameters:
    - `element` (string, optional): 用于获取与元素交互权限的人类可读元素描述
    - `target` (string, optional): 来自页面快照的确切目标元素引用，或唯一元素选择器
    - `type` (string): 截图的图像格式。默认为 png。
    - `filename` (string, optional): 保存截图的文件名。如果未指定，默认为 `page-{timestamp}.{png|jpeg}`。建议使用相对文件名以保持在输出目录内。
    - `fullPage` (boolean, optional): 当为 true 时，截取整个可滚动页面的屏幕截图，而不是当前可见的视口。不能与元素截图一起使用。
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_type**
  - Title: 输入文本
  - Description: 将文本输入到可编辑元素中
  - Parameters:
    - `element` (string, optional): 用于获取与元素交互权限的人类可读元素描述
    - `target` (string): 来自页面快照的确切目标元素引用，或唯一元素选择器
    - `text` (string): 要输入到元素中的文本
    - `submit` (boolean, optional): 是否提交输入的文本（之后按 Enter）
    - `slowly` (boolean, optional): 是否一次输入一个字符。这对于触发页面中的键处理程序很有用。默认情况下，整个文本是一次性填充的。
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_wait_for**
  - Title: 等待
  - Description: 等待文本出现或消失或经过指定的时间
  - Parameters:
    - `time` (number, optional): 要等待的时间（秒）
    - `text` (string, optional): 要等待的文本
    - `textGone` (string, optional): 要等待消失的文本
  - Read-only: **false**

</details>

<details>
<summary><b>标签页管理 (Tab management)</b></summary>

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_tabs**
  - Title: 管理标签页
  - Description: 列出、创建、关闭或选择浏览器标签页。
  - Parameters:
    - `action` (string): 要执行的操作
    - `index` (number, optional): 标签页索引，用于关闭/选择。如果省略关闭操作，则关闭当前标签页。
    - `url` (string, optional): 在新标签页中导航到的 URL，用于新建。
  - Read-only: **false**

</details>

<details>
<summary><b>浏览器安装 (Browser installation)</b></summary>

</details>

<details>
<summary><b>配置（通过 --caps=config 选择加入）(Configuration)</b></summary>

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_get_config**
  - Title: 获取配置
  - Description: 在合并 CLI 选项、环境变量和配置文件后获取最终解析的配置。
  - Parameters: None
  - Read-only: **true**

</details>

<details>
<summary><b>网络（通过 --caps=network 选择加入）(Network)</b></summary>

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_network_state_set**
  - Title: 设置网络状态
  - Description: 将浏览器网络状态设置为在线或离线。当离线时，所有网络请求都将失败。
  - Parameters:
    - `state` (string): 设置为 "offline" 以模拟离线模式，"online" 以恢复网络连接
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_route**
  - Title: 模拟网络请求
  - Description: 设置路由以模拟匹配 URL 模式的网络请求
  - Parameters:
    - `pattern` (string): 要匹配的 URL 模式（例如，"**/api/users", "**/*.{png,jpg}"）
    - `status` (number, optional): 要返回的 HTTP 状态码（默认：200）
    - `body` (string, optional): 响应正文（文本或 JSON 字符串）
    - `contentType` (string, optional): Content-Type header（例如，"application/json", "text/html"）
    - `headers` (array, optional): 以 "Name: Value" 格式添加的 Headers
    - `removeHeaders` (string, optional): 要从请求中移除的 header 名称的逗号分隔列表
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_route_list**
  - Title: 列出网络路由
  - Description: 列出所有活动的网络路由
  - Parameters: None
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_unroute**
  - Title: 移除网络路由
  - Description: 移除匹配模式（或未指定模式时移除所有路由）的网络路由
  - Parameters:
    - `pattern` (string, optional): 要取消路由的 URL 模式（省略以移除所有路由）
  - Read-only: **false**

</details>

<details>
<summary><b>存储（通过 --caps=storage 选择加入）(Storage)</b></summary>

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_cookie_clear**
  - Title: 清除 cookies
  - Description: 清除所有 cookies
  - Parameters: None
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_cookie_delete**
  - Title: 删除 cookie
  - Description: 删除特定的 cookie
  - Parameters:
    - `name` (string): 要删除的 cookie 名称
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_cookie_get**
  - Title: 获取 cookie
  - Description: 通过名称获取特定的 cookie
  - Parameters:
    - `name` (string): 要获取的 cookie 名称
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_cookie_list**
  - Title: 列出 cookies
  - Description: 列出所有 cookies（可选择按域名/路径过滤）
  - Parameters:
    - `domain` (string, optional): 按域名过滤 cookies
    - `path` (string, optional): 按路径过滤 cookies
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_cookie_set**
  - Title: 设置 cookie
  - Description: 设置带有可选标志（域名、路径、过期时间、httpOnly、secure、sameSite）的 cookie
  - Parameters:
    - `name` (string): Cookie 名称
    - `value` (string): Cookie 值
    - `domain` (string, optional): Cookie 域名
    - `path` (string, optional): Cookie 路径
    - `expires` (number, optional): Cookie 过期时间，Unix 时间戳
    - `httpOnly` (boolean, optional): 该 cookie 是否仅限 HTTP
    - `secure` (boolean, optional): 该 cookie 是否安全
    - `sameSite` (string, optional): Cookie SameSite 属性
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_localstorage_clear**
  - Title: 清除 localStorage
  - Description: 清除所有 localStorage
  - Parameters: None
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_localstorage_delete**
  - Title: 删除 localStorage 项
  - Description: 删除一个 localStorage 项
  - Parameters:
    - `key` (string): 要删除的键
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_localstorage_get**
  - Title: 获取 localStorage 项
  - Description: 通过键获取一个 localStorage 项
  - Parameters:
    - `key` (string): 要获取的键
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_localstorage_list**
  - Title: 列出 localStorage
  - Description: 列出所有 localStorage 键值对
  - Parameters: None
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_localstorage_set**
  - Title: 设置 localStorage 项
  - Description: 设置一个 localStorage 项
  - Parameters:
    - `key` (string): 要设置的键
    - `value` (string): 要设置的值
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_sessionstorage_clear**
  - Title: 清除 sessionStorage
  - Description: 清除所有 sessionStorage
  - Parameters: None
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_sessionstorage_delete**
  - Title: 删除 sessionStorage 项
  - Description: 删除一个 sessionStorage 项
  - Parameters:
    - `key` (string): 要删除的键
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_sessionstorage_get**
  - Title: 获取 sessionStorage 项
  - Description: 通过键获取一个 sessionStorage 项
  - Parameters:
    - `key` (string): 要获取的键
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_sessionstorage_list**
  - Title: 列出 sessionStorage
  - Description: 列出所有 sessionStorage 键值对
  - Parameters: None
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_sessionstorage_set**
  - Title: 设置 sessionStorage 项
  - Description: 设置一个 sessionStorage 项
  - Parameters:
    - `key` (string): 要设置的键
    - `value` (string): 要设置的值
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_set_storage_state**
  - Title: 恢复存储状态
  - Description: 从文件恢复存储状态（cookies、本地存储）。这将在恢复之前清除现有的 cookies 和本地存储。
  - Parameters:
    - `filename` (string): 要从中恢复的存储状态文件路径
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_storage_state**
  - Title: 保存存储状态
  - Description: 将存储状态（cookies、本地存储）保存到文件中以便以后重用
  - Parameters:
    - `filename` (string, optional): 保存存储状态的文件名。如果未指定，默认为 `storage-state-{timestamp}.json`。
  - Read-only: **true**

</details>

<details>
<summary><b>开发者工具（通过 --caps=devtools 选择加入）(DevTools)</b></summary>

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_annotate**
  - Title: 注释当前页面
  - Description: 在当前页面上打开 Playwright Dashboard 的注释模式，并等待用户绘制注释。返回带注释的屏幕截图、ARIA 快照和注释列表。
  - Parameters: None
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_hide_highlight**
  - Title: 隐藏元素高亮
  - Description: 移除先前为元素添加的高亮覆盖层。
  - Parameters:
    - `element` (string, optional): 用于添加高亮时的人类可读描述；必须与传递给 browser_highlight 的值匹配。
    - `target` (string, optional): 来自页面快照的确切目标元素引用，或唯一元素选择器
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_highlight**
  - Title: 高亮显示元素
  - Description: 在页面上的元素周围显示持久的高亮覆盖层。
  - Parameters:
    - `element` (string, optional): 用于获取与元素交互权限的人类可读元素描述
    - `target` (string): 来自页面快照的确切目标元素引用，或唯一元素选择器
    - `style` (string, optional): 应用于高亮覆盖层的额外内联 CSS，例如 "outline: 2px dashed red"。
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_resume**
  - Title: 恢复暂停的脚本执行
  - Description: 在脚本被暂停后恢复执行。当使用 step=true 调用时，将在下一个动作之前再次暂停执行。
  - Parameters:
    - `step` (boolean, optional): 当为 true 时，将在下一个动作之前再次暂停执行，允许逐步调试。
    - `location` (string, optional): 在特定 <file>:<line> 处暂停执行，例如 "example.spec.ts:42"。
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_start_tracing**
  - Title: 开始追踪
  - Description: 开始录制追踪
  - Parameters: None
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_start_video**
  - Title: 开始视频
  - Description: 开始录制视频
  - Parameters:
    - `filename` (string, optional): 保存视频的文件名。
    - `size` (object, optional): 视频尺寸
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_stop_tracing**
  - Title: 停止追踪
  - Description: 停止录制追踪
  - Parameters: None
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_stop_video**
  - Title: 停止视频
  - Description: 停止录制视频
  - Parameters: None
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_video_chapter**
  - Title: 视频章节
  - Description: 向视频录制中添加章节标记。显示带有模糊背景的全屏章节卡。
  - Parameters:
    - `title` (string): 章节标题
    - `description` (string, optional): 章节描述
    - `duration` (number, optional): 显示章节卡的持续时间（毫秒）
  - Read-only: **true**

</details>

<details>
<summary><b>基于坐标的交互（通过 --caps=vision 选择加入）(Coordinate-based)</b></summary>

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_mouse_click_xy**
  - Title: 点击
  - Description: 在给定位置点击鼠标按钮
  - Parameters:
    - `x` (number): X 坐标
    - `y` (number): Y 坐标
    - `button` (string, optional): 要点击的按钮，默认为左键
    - `clickCount` (number, optional): 点击次数，默认为 1
    - `delay` (number, optional): 鼠标按下和鼠标抬起之间等待的时间（毫秒），默认为 0
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_mouse_down**
  - Title: 按下鼠标键
  - Description: 按下鼠标键
  - Parameters:
    - `button` (string, optional): 要按下的按钮，默认为左键
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_mouse_drag_xy**
  - Title: 拖动鼠标
  - Description: 将左鼠标按钮拖到给定位置
  - Parameters:
    - `startX` (number): 起始 X 坐标
    - `startY` (number): 起始 Y 坐标
    - `endX` (number): 结束 X 坐标
    - `endY` (number): 结束 Y 坐标
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_mouse_move_xy**
  - Title: 移动鼠标
  - Description: 将鼠标移动到给定位置
  - Parameters:
    - `x` (number): X 坐标
    - `y` (number): Y 坐标
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_mouse_up**
  - Title: 释放鼠标键
  - Description: 释放鼠标键
  - Parameters:
    - `button` (string, optional): 要按下的按钮，默认为左键
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_mouse_wheel**
  - Title: 滚动鼠标滚轮
  - Description: 滚动鼠标滚轮
  - Parameters:
    - `deltaX` (number): X 增量
    - `deltaY` (number): Y 增量
  - Read-only: **false**

</details>

<details>
<summary><b>PDF 生成（通过 --caps=pdf 选择加入）(PDF generation)</b></summary>

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_pdf_save**
  - Title: 保存为 PDF
  - Description: 将页面保存为 PDF
  - Parameters:
    - `filename` (string, optional): 保存 pdf 的文件名。如果未指定，默认为 `page-{timestamp}.pdf`。建议使用相对文件名以保持在输出目录内。
  - Read-only: **true**

</details>

<details>
<summary><b>测试断言（通过 --caps=testing 选择加入）(Test assertions)</b></summary>

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_generate_locator**
  - Title: 为元素创建定位器
  - Description: 为给定元素生成用于测试的定位器
  - Parameters:
    - `element` (string, optional): 用于获取与元素交互权限的人类可读元素描述
    - `target` (string): 来自页面快照的确切目标元素引用，或唯一元素选择器
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_verify_element_visible**
  - Title: 验证元素可见性
  - Description: 验证元素在页面上是否可见
  - Parameters:
    - `role` (string): 元素的 ROLE。可以在快照中找到，如下所示： `- {ROLE} "Accessible Name":`
    - `accessibleName` (string): 元素的 ACCESSIBLE_NAME。可以在快照中找到，如下所示： `- role "{ACCESSIBLE_NAME}"`
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_verify_list_visible**
  - Title: 验证列表可见性
  - Description: 验证列表在页面上是否可见
  - Parameters:
    - `element` (string): 人类可读的列表描述
    - `target` (string): 指向该列表的确切目标元素引用
    - `items` (array): 要验证的项目
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_verify_text_visible**
  - Title: 验证文本可见性
  - Description: 验证文本在页面上是否可见。如果可能，请优先使用 browser_verify_element_visible。
  - Parameters:
    - `text` (string): 要验证的 TEXT。可以在快照中找到，如下所示： `- role "Accessible Name": {TEXT}` 或这样： `- text: {TEXT}`
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_verify_value**
  - Title: 验证值
  - Description: 验证元素值
  - Parameters:
    - `type` (string): 元素的类型
    - `element` (string): 人类可读的元素描述
    - `target` (string): 来自页面快照的确切目标元素引用
    - `value` (string): 要验证的值。对于复选框，使用 "true" 或 "false"。
  - Read-only: **false**

</details>


<!--- End of tools generated section -->