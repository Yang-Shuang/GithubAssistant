# MCP Inspector

MCP Inspector 是一款用于测试和调试 MCP 服务器的开发者工具。

![MCP Inspector Screenshot](https://raw.githubusercontent.com/modelcontextprotocol/inspector/main/mcp-inspector.png)

## 架构概述

MCP Inspector 由两个协同工作的主要组件组成：

- **MCP Inspector Client (MCPI)**: 基于 React 的 Web UI，提供用于测试和调试 MCP 服务器的交互式界面
- **MCP Proxy (MCPP)**: 一个 Node.js 服务器，充当协议桥接器，通过多种传输方式（stdio、SSE、streamable-http）将 Web UI 与 MCP 服务器连接起来

请注意，该代理并非用于拦截流量的网络代理。相反，它同时作为 MCP 客户端（连接你的 MCP 服务器）和 HTTP 服务器（提供 Web UI），从而实现通过浏览器与使用不同传输协议的 MCP 服务器进行交互。

## 运行 Inspector

### 环境要求

- Node.js: ^22.7.5

### 快速开始（UI 模式）

要立即使用 UI 启动运行，只需执行以下命令：

```bash
npx @modelcontextprotocol/inspector
```

服务器将启动，UI 可通过 `http://localhost:6274` 访问。

### Docker 容器

你也可以通过以下命令在 Docker 容器中启动它：

```bash
docker run --rm \
  -p 127.0.0.1:6274:6274 \
  -p 127.0.0.1:6277:6277 \
  -e HOST=0.0.0.0 \
  -e MCP_AUTO_OPEN_ENABLED=false \
  ghcr.io/modelcontextprotocol/inspector:latest
```

### 从 MCP 服务器仓库运行

若要检查某个 MCP 服务器的实现，无需克隆本仓库。直接使用 `npx` 即可。例如，如果你的服务器构建在 `build/index.js`：

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

你可以向你的 MCP 服务器同时传递参数和环境变量。参数会直接传递给服务器，而环境变量可以使用 `-e` 标志设置：

```bash
# Pass arguments only
npx @modelcontextprotocol/inspector node build/index.js arg1 arg2

# Pass environment variables only
npx @modelcontextprotocol/inspector -e key=value -e key2=$VALUE2 node build/index.js

# Pass both environment variables and arguments
npx @modelcontextprotocol/inspector -e key=value -e key2=$VALUE2 node build/index.js arg1 arg2

# Use -- to separate inspector flags from server arguments
npx @modelcontextprotocol/inspector -e key=$VALUE -- node build/index.js -e server-flag
```

Inspector 同时运行 MCP Inspector（MCPI）客户端 UI（默认端口 6274）和 MCP Proxy（MCPP）服务器（默认端口 6277）。在浏览器中打开 MCPI 客户端 UI 即可使用 Inspector。（这些端口分别源自 MCPI 和 MCPP 的 T9 拨号盘映射，便于记忆）。如有需要，你可以自定义端口：

```bash
CLIENT_PORT=8080 SERVER_PORT=9000 npx @modelcontextprotocol/inspector node build/index.js
```

有关使用 Inspector 的更多详细信息，请参阅 [MCP 文档站点的 Inspector 部分](https://modelcontextprotocol.io/docs/tools/inspector)。如需调试帮助，请参阅[调试指南](https://modelcontextprotocol.io/docs/tools/debugging)。

### 服务器文件导出

MCP Inspector 提供了便捷的按钮，用于导出服务器启动配置，以便在 Cursor、Claude Code 或 Inspector 的 CLI 等客户端中使用。该文件通常命名为 `mcp.json`。

- **Server Entry（服务器条目）** - 将单个服务器配置条目复制到剪贴板。你可以将其添加到你的 `mcp.json` 文件的 `mcpServers` 对象中，并指定你喜欢的服务器名称。

  **STDIO transport example：**

  ```json
  {
    "command": "node",
    "args": ["build/index.js", "--debug"],
    "env": {
      "API_KEY": "your-api-key",
      "DEBUG": "true"
    }
  }
  ```

  **SSE transport example：**

  ```json
  {
    "type": "sse",
    "url": "http://localhost:3000/events",
    "note": "For SSE connections, add this URL directly in Client"
  }
  ```

  **Streamable HTTP transport example：**

  ```json
  {
    "type": "streamable-http",
    "url": "http://localhost:3000/mcp",
    "note": "For Streamable HTTP connections, add this URL directly in your MCP Client"
  }
  ```

- **Servers File（服务器文件）** - 将完整的 MCP 配置文件结构复制到剪贴板，并将当前服务器配置添加为 `default-server`。你可以直接将其保存为 `mcp.json`。

  **STDIO transport example：**

  ```json
  {
    "mcpServers": {
      "default-server": {
        "command": "node",
        "args": ["build/index.js", "--debug"],
        "env": {
          "API_KEY": "your-api-key",
          "DEBUG": "true"
        }
      }
    }
  }
  ```

  **SSE transport example：**

  ```json
  {
    "mcpServers": {
      "default-server": {
        "type": "sse",
        "url": "http://localhost:3000/events",
        "note": "For SSE connections, add this URL directly in Client"
      }
    }
  }
  ```

  **Streamable HTTP transport example：**

  ```json
  {
    "mcpServers": {
      "default-server": {
        "type": "streamable-http",
        "url": "http://localhost:3000/mcp",
        "note": "For Streamable HTTP connections, add this URL directly in your MCP Client"
      }
    }
  }
  ```

在配置好你的服务器设置后，这些按钮会出现在 Inspector UI 中，方便你保存和复用配置。

对于 SSE 和 Streamable HTTP 传输连接，Inspector 为这两个按钮提供了类似的功能。“Server Entry”按钮复制可添加到现有配置文件的配置，而“Servers File”按钮创建包含 URL 的完整配置文件，以便在客户端中直接使用。

你可以将 Server Entry 粘贴到你现有 `mcp.json` 文件的选定服务器名称下，或者使用完整的 Servers File payload 来创建新的配置文件。

### 认证

Inspector 支持用于 SSE 连接的 Bearer Token 认证。在连接 MCP 服务器时，请在 UI 中输入你的令牌，它将被包含在 Authorization 请求头中发送。你可以使用侧边栏中的输入框覆盖该请求头的名称。

### 安全注意事项

MCP Inspector 包含一个代理服务器，它可以运行并与本地 MCP 进程通信。不应将该代理服务器暴露在不信任的网络中，因为它具有生成本地进程的权限，并且可以连接到任何指定的 MCP 服务器。

#### 认证机制

MCP Inspector 代理服务器默认需要身份验证。启动服务器时，会生成一个随机会话令牌并打印到控制台：

```
🔑 Session token: 3a1c267fad21f7150b7d624c160b7f09b0b8c4f623c7107bbf13378f051538d4

🔗 Open inspector with token pre-filled:
   http://localhost:6274/?MCP_PROXY_AUTH_TOKEN=3a1c267fad21f7150b7d624c160b7f09b0b8c4f623c7107bbf13378f051538d4
```

该令牌必须作为 Bearer Token 包含在所有请求的 Authorization 请求头中。Inspector 会自动在浏览器中打开已预填令牌的 URL。

**Automatic browser opening** - 启用认证后，Inspector 现在会自动在浏览器中打开已预填令牌的 URL。

**Alternative: Manual configuration** - 如果你已经打开了 Inspector：

1. Click the "Configuration" button in the sidebar
2. Find "Proxy Session Token" and enter the token displayed in the proxy console
3. Click "Save" to apply the configuration

该令牌将保存在浏览器的本地存储中，供以后使用。

If you need to disable authentication (NOT RECOMMENDED), you can set the `DANGEROUSLY_OMIT_AUTH` environment variable:

```bash
DANGEROUSLY_OMIT_AUTH=true npm start
```

---

**🚨 WARNING 🚨**

Disabling authentication with `DANGEROUSLY_OMIT_AUTH` is incredibly dangerous! Disabling auth leaves your machine open to attack not just when exposed to the public internet, but also **via your web browser**. Meaning, visiting a malicious website OR viewing a malicious advertizement could allow an attacker to remotely compromise your computer. Do not disable this feature unless you truly understand the risks.

Read more about the risks of this vulnerability on Oligo's blog: [Critical RCE Vulnerability in Anthropic MCP Inspector - CVE-2025-49596](https://www.oligo.security/blog/critical-rce-vulnerability-in-anthropic-mcp-inspector-cve-2025-49596)

---

You can also set the token via the `MCP_PROXY_AUTH_TOKEN` environment variable when starting the server:

```bash
MCP_PROXY_AUTH_TOKEN=$(openssl rand -hex 32) npm start
```

#### Local-only Binding

By default, both the MCP Inspector proxy server and client bind only to `localhost` to prevent network access. This ensures they are not accessible from other devices on the network. If you need to bind to all interfaces for development purposes, you can override this with the `HOST` environment variable:

```bash
HOST=0.0.0.0 npm start
```

**Warning:** Only bind to all interfaces in trusted network environments, as this exposes the proxy server's ability to execute local processes and both services to network access.

#### DNS Rebinding Protection

To prevent DNS rebinding attacks, the MCP Inspector validates the `Origin` header on incoming requests. By default, only requests from the client origin are allowed (respects `CLIENT_PORT` if set, defaulting to port 6274). You can configure additional allowed origins by setting the `ALLOWED_ORIGINS` environment variable (comma-separated list):

```bash
ALLOWED_ORIGINS=http://localhost:6274,http://localhost:8000 npm start
```

### Configuration

The MCP Inspector supports the following configuration settings. To change them, click on the `Configuration` button in the MCP Inspector UI:

| Setting                                 | Description                                                                                                                                         | Default |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `MCP_SERVER_REQUEST_TIMEOUT`            | Client-side timeout (ms) - Inspector will cancel the request if no response is received within this time. Note: servers may have their own timeouts | 300000  |
| `MCP_REQUEST_TIMEOUT_RESET_ON_PROGRESS` | Reset timeout on progress notifications                                                                                                             | true    |
| `MCP_REQUEST_MAX_TOTAL_TIMEOUT`         | Maximum total timeout for requests sent to the MCP server (ms) (Use with progress notifications)                                                    | 60000   |
| `MCP_PROXY_FULL_ADDRESS`                | Set this if you are running the MCP Inspector Proxy on a non-default address. Example: http://10.1.1.22:5577                                        | ""      |
| `MCP_AUTO_OPEN_ENABLED`                 | Enable automatic browser opening when inspector starts (works with authentication enabled). Only as environment var, not configurable in browser.   | true    |

**Note on Timeouts:** The timeout settings above control when the Inspector (as an MCP client) will cancel requests. These are independent of any server-side timeouts. For example, if a server tool has a 10-minute timeout but the Inspector's timeout is set to 30 seconds, the Inspector will cancel the request after 30 seconds. Conversely, if the Inspector's timeout is 10 minutes but the server times out after 30 seconds, you'll receive the server's timeout error. For tools that require user interaction (like elicitation) or long-running operations, ensure the Inspector's timeout is set appropriately.

These settings can be adjusted in real-time through the UI and will persist across sessions.

The inspector also supports configuration files to store settings for different MCP servers. This is useful when working with multiple servers or complex configurations:

```bash
npx @modelcontextprotocol/inspector --config path/to/config.json --server everything
```

Example server configuration file:

```json
{
  "mcpServers": {
    "everything": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-everything"],
      "env": {
        "hello": "Hello MCP!"
      }
    },
    "my-server": {
      "command": "node",
      "args": ["build/index.js", "arg1", "arg2"],
      "env": {
        "key": "value",
        "key2": "value2"
      }
    }
  }
}
```

#### Transport Types in Config Files

The inspector automatically detects the transport type from your config file. You can specify different transport types:

**STDIO (default):**

```json
{
  "mcpServers": {
    "my-stdio-server": {
      "type": "stdio",
      "command": "npx",
      "args": ["@modelcontextprotocol/server-everything"]
    }
  }
}
```

**SSE (Server-Sent Events):**

```json
{
  "mcpServers": {
    "my-sse-server": {
      "type": "sse",
      "url": "http://localhost:3000/sse"
    }
  }
}
```

**Streamable HTTP:**

```json
{
  "mcpServers": {
    "my-http-server": {
      "type": "streamable-http",
      "url": "http://localhost:3000/mcp"
    }
  }
}
```

#### Default Server Selection

You can launch the inspector without specifying a server name if your config has:

1. **A single server** - automatically selected:

```bash
# Automatically uses "my-server" if it's the only one
npx @modelcontextprotocol/inspector --config mcp.json
```

2. **A server named "default-server"** - automatically selected:

```json
{
  "mcpServers": {
    "default-server": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-everything"]
    },
    "other-server": {
      "command": "node",
      "args": ["other.js"]
    }
  }
}
```

> **Tip:** You can easily generate this configuration format using the **Server Entry** and **Servers File** buttons in the Inspector UI, as described in the Servers File Export section above.

You can also set the initial `transport` type, `serverUrl`, `serverCommand`, and `serverArgs` via query params, for example:

```
http://localhost:6274/?transport=sse&serverUrl=http://localhost:8787/sse
http://localhost:6274/?transport=streamable-http&serverUrl=http://localhost:8787/mcp
http://localhost:6274/?transport=stdio&serverCommand=npx&serverArgs=arg1%20arg2
```

You can also set initial config settings via query params, for example:

```
http://localhost:6274/?MCP_SERVER_REQUEST_TIMEOUT=60000&MCP_REQUEST_TIMEOUT_RESET_ON_PROGRESS=false&MCP_PROXY_FULL_ADDRESS=http://10.1.1.22:5577
```

Note that if both the query param and the corresponding localStorage item are set, the query param will take precedence.

### From this repository

If you're working on the inspector itself:

Development mode:

```bash
npm run dev

# To co-develop with the typescript-sdk package (assuming it's cloned in ../typescript-sdk; set MCP_SDK otherwise):
npm run dev:sdk "cd sdk && npm run examples:simple-server:w"
# then open http://localhost:3000/mcp as SHTTP in the inspector.
# To go back to the deployed SDK version:
#   npm run unlink:sdk && npm i
```

> **Note for Windows users:**
> On Windows, use the following command instead:
>
> ```bash
> npm run dev:windows
> ```

Production mode:

```bash
npm run build
npm start
```

### CLI Mode

CLI mode enables programmatic interaction with MCP servers from the command line, ideal for scripting, automation, and integration with coding assistants. This creates an efficient feedback loop for MCP server development.

```bash
npx @modelcontextprotocol/inspector --cli node build/index.js
```

The CLI mode supports most operations across tools, resources, and prompts. A few examples:

```bash
# Basic usage
npx @modelcontextprotocol/inspector --cli node build/index.js

# With config file
npx @modelcontextprotocol/inspector --cli --config path/to/config.json --server myserver

# List available tools
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list

# Call a specific tool
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/call --tool-name mytool --tool-arg key=value --tool-arg another=value2

# Call a tool with JSON arguments
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/call --tool-name mytool --tool-arg 'options={"format": "json", "max_tokens": 100}'

# List available resources
npx @modelcontextprotocol/inspector --cli node build/index.js --method resources/list

# List available prompts
npx @modelcontextprotocol/inspector --cli node build/index.js --method prompts/list

# Connect to a remote MCP server (default is SSE transport)
npx @modelcontextprotocol/inspector --cli https://my-mcp-server.example.com

# Connect to a remote MCP server (with Streamable HTTP transport)
npx @modelcontextprotocol/inspector --cli https://my-mcp-server.example.com --transport http --method tools/list

# Connect to a remote MCP server (with custom headers)
npx @modelcontextprotocol/inspector --cli https://my-mcp-server.example.com --transport http --method tools/list --header "X-API-Key: your-api-key"

# Call a tool on a remote server
npx @modelcontextprotocol/inspector --cli https://my-mcp-server.example.com --method tools/call --tool-name remotetool --tool-arg param=value

# List resources from a remote server
npx @modelcontextprotocol/inspector --cli https://my-mcp-server.example.com --method resources/list
```

### UI Mode vs CLI Mode: When to Use Each

| Use Case                 | UI Mode                                                                   | CLI Mode                                                                                                                                             |
| ------------------------ | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Server Development**   | Visual interface for interactive testing and debugging during development | Scriptable commands for quick testing and continuous integration; creates feedback loops with AI coding assistants like Cursor for rapid development |
| **Resource Exploration** | Interactive browser with hierarchical navigation and JSON visualization   | Programmatic listing and reading for automation and scripting                                                                                        |
| **Tool Testing**         | Form-based parameter input with real-time response visualization          | Command-line tool execution with JSON output for scripting                                                                                           |
| **Prompt Engineering**   | Interactive sampling with streaming responses and visual comparison       | Batch processing of prompts with machine-readable output                                                                                             |
| **Debugging**            | Request history, visualized errors, and real-time notifications           | Direct JSON output for log analysis and integration with other tools                                                                                 |
| **Automation**           | N/A                                                                       | Ideal for CI/CD pipelines, batch processing, and integration with coding assistants                                                                  |
| **Learning MCP**         | Rich visual interface helps new users understand server capabilities      | Simplified commands for focused learning of specific endpoints                                                                                       |

## Tool Input Validation Guidelines

When implementing or modifying tool input parameter handling in the Inspector:

- **Omit optional fields with empty values** - When processing form inputs, omit empty strings or null values for optional parameters, UNLESS the field has an explicit default value in the schema that matches the current value
- **Preserve explicit default values** - If a field schema contains an explicit default (e.g., `default: null`), and the current value matches that default, include it in the request. This is a meaningful value the tool expects
- **Always include required fields** - Preserve required field values even when empty, allowing the MCP server to validate and return appropriate error messages
- **Defer deep validation to the server** - Implement basic field presence checking in the Inspector client, but rely on the MCP server for parameter validation according to its schema

These guidelines maintain clean parameter passing and proper separation of concerns between the Inspector client and MCP servers.

## License

This project is licensed under the MIT License—see the [LICENSE](LICENSE) file for details.