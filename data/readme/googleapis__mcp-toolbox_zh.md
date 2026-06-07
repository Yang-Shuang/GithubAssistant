<div align="center">

![logo](./logo.png)

# 数据库 MCP Toolbox

<a href="https://trendshift.io/repositories/13019" target="_blank"><img src="https://trendshift.io/api/badge/repositories/13019" alt="googleapis%2Fmcp-toolbox | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

[![Go Report Card](https://goreportcard.com/badge/github.com/googleapis/mcp-toolbox)](https://goreportcard.com/report/github.com/googleapis/mcp-toolbox)
[![License: Apache
2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Docs](https://img.shields.io/badge/Docs-MCP_Toolbox-blue)](https://mcp-toolbox.dev/)
[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=flat&logo=discord&logoColor=white)](https://discord.gg/Dmm69peqjh)
[![Medium](https://img.shields.io/badge/Medium-12100E?style=flat&logo=medium&logoColor=white)](https://medium.com/@mcp_toolbox)

[![Python SDK](https://img.shields.io/pypi/v/toolbox-core?logo=python&logoColor=white&label=Python%20SDK)](https://pypi.org/project/toolbox-core/)
[![JS/TS SDK](https://img.shields.io/npm/v/@toolbox-sdk/core?logo=javascript&logoColor=white&label=JS%20SDK)](https://www.npmjs.com/package/@toolbox-sdk/core)
[![Go SDK](https://img.shields.io/github/v/release/googleapis/mcp-toolbox-sdk-go?logo=go&logoColor=white&label=Go%20SDK)](https://pkg.go.dev/github.com/googleapis/mcp-toolbox-sdk-go)
[![Java SDK](https://img.shields.io/maven-central/v/com.google.cloud.mcp/mcp-toolbox-sdk-java?logo=apache-maven&logoColor=white&label=Java%20SDK)](https://mvnrepository.com/artifact/com.google.cloud.mcp/mcp-toolbox-sdk-java)
</div>

数据库 MCP Toolbox 是一个开源的模型上下文协议（Model Context Protocol，简称 MCP）服务器，可将你的 AI 智能体、IDE 和应用程序直接连接到企业级数据库。 

<p align="center">
<img src="docs/en/documentation/introduction/architecture.png" alt="architecture" width="50%"/>
</p>

它提供**双重用途**：
1. **开箱即用的 MCP 服务器（构建时）：** 使用我们*预构建的通用工具*，将 Gemini CLI、Google Antigravity、Claude Code、Codex 或其他 MCP 客户端即时连接到你的数据库。直接与数据对话、探索模式并生成代码，无需编写样板代码。
2. **自定义工具框架（运行时）：** 一个强大的框架，用于为你的生产环境智能体构建专业化且高度安全的 AI 工具。安全便捷地定义结构化查询、语义搜索和 NL2SQL 功能。

本 README 提供简要概述。如需详细信息，请参阅[完整文档](https://mcp-toolbox.dev/)。

> [!IMPORTANT]  
> **仓库名称更新：** `genai-toolbox` 仓库已正式更名为 `mcp-toolbox`。为确保本地环境反映新名称，你可以更新远程地址：
> `git remote set-url origin https://github.com/googleapis/mcp-toolbox.git`

> [!NOTE]
> 该解决方案最初名为“Gen AI Toolbox for Databases”（github.com/googleapis/genai-toolbox），因其早期开发早于 MCP，后更名为当前名称以符合 MCP 兼容性。

<!-- TOC ignore:true -->
## 目录

- [为什么选择 MCP Toolbox？](#why-mcp-toolbox)
- [快速入门：预构建工具](#quick-start-prebuilt-tools)
- [快速入门：自定义工具](#quick-start-custom-tools)
- [安装与运行 Toolbox 服务器](#install--run-the-toolbox-server)
- [连接至 Toolbox](#connect-to-toolbox)
  - [MCP 客户端](#mcp-client)
  - [Toolbox SDK：集成到你的应用中](#toolbox-sdks-integrate-with-your-application)
- [其他功能](#additional-features)
- [版本控制](#versioning)
- [贡献指南](#contributing)
- [社区交流](#community)

---

## 为什么选择 MCP Toolbox？

- **开箱即用的数据库访问：** 预构建的通用工具可让你直接从 IDE 或 CLI 即时探索数据（例如 `list_tables`、`execute_sql`）。
- **自定义工具框架：** 使用你自己的预定义逻辑构建生产级工具，通过受限访问、结构化查询和语义搜索确保安全。
- **简化开发流程：** 在不到 10 行代码内将工具集成到你的 Agent Development Kit (ADK)、LangChain、LlamaIndex 或自定义智能体中。
- **更优性能：** 开箱即用地处理连接池、集成身份验证（IAM）和端到端可观测性（OpenTelemetry）。
- **增强的安全性：** 内置集成的身份验证，为你的数据提供更安全的访问。
- **端到端可观测性：** 开箱即用的指标和追踪功能，内置对 OpenTelemetry 的支持。

---

## 快速入门：预构建工具

告别上下文切换，让你的 AI 助手成为真正的协同开发者。通过将你的 IDE 与数据库连接至 MCP Toolbox，你可以用自然语言查询数据、自动化模式发现与管理，并生成感知数据库的代码。

你可以通过配置 MCP 服务器，在任何兼容 MCP 的 IDE 或客户端（例如 Gemini CLI、Google Antigravity、Claude Code、Codex 等）中使用 Toolbox。

**预构建工具也方便地提供在 [Google Antigravity MCP Store](https://antigravity.google/docs/mcp) 中，只需单击即可安装。**

1. 在你的客户端的 MCP 配置文件中添加以下内容（通常为 `mcp.json` 或 `claude_desktop_config.json`）：

    ```json
    {
      "mcpServers": {
        "toolbox-postgres": {
          "command": "npx",
          "args": [
            "-y",
            "@toolbox-sdk/server",
            "--prebuilt=postgres",
            "--stdio"
          ]
        }
      }
    }
    ```

2. 设置适当的环境变量以进行连接，请参阅[预构建工具参考](https://mcp-toolbox.dev/documentation/configuration/prebuilt-configs/)。

当你使用 `--prebuilt=<数据库>` 标志运行 Toolbox 时，你将立即获得与该数据库交互的标准工具。 

目前支持的数据库包括：
- **Google Cloud：** AlloyDB、BigQuery、Cloud SQL（PostgreSQL、MySQL、SQL Server）、Spanner、Firestore、Knowledge Catalog（原 Dataplex）。
- **其他数据库：** PostgreSQL、MySQL、SQL Server、Oracle、MongoDB、Redis、Elasticsearch、CockroachDB、ClickHouse、Couchbase、Neo4j、Snowflake、Trino 等。

有关所有支持数据库中可用工具及其功能的完整列表，请参阅[预构建工具参考](https://mcp-toolbox.dev/documentation/configuration/prebuilt-configs/)。

*有关 Docker 或二进制文件等不同执行方式，请参阅[安装与运行 Toolbox 服务器](#install--run-the-toolbox-server)部分。*


> [!TIP]
> 对于寻求托管解决方案的用户，[Google Cloud MCP Servers](https://cloud.google.com/blog/products/databases/managed-mcp-servers-for-google-cloud-databases) 
> 提供了带有预构建工具的托管 MCP 体验；你可在[此处了解两者的区别](https://mcp-toolbox.dev/dev/reference/faq/)。

---

## 快速入门：自定义工具

Toolbox 也可用作自定义工具框架。
配置 Toolbox 的主要方式是通过 `tools.yaml` 文件。如果你有多个配置文件，可以使用 `--config tools.yaml` 标志指定要加载的文件。

你可以在[资源](https://mcp-toolbox.dev/documentation/configuration/)部分找到所有资源类型的详细参考文档。

### 数据源 (Sources)

你的 `tools.yaml` 中的 `sources` 部分定义了 Toolbox 应访问哪些数据源。大多数工具至少需要一个用于执行的数据源。

```yaml
kind: source
name: my-pg-source
type: postgres
host: 127.0.0.1
port: 5432
database: toolbox_db
user: toolbox_user
password: my-password
```

有关配置不同类型数据源的更多详细信息，请参阅[Sources](https://mcp-toolbox.dev/documentation/configuration/sources/)。

### 工具 (Tools)

`tools.yaml` 中的 `tools` 部分定义了智能体可以采取的操作：它是什么类型的工具、影响哪些数据源、使用什么参数等。

```yaml
kind: tool
name: search-hotels-by-name
type: postgres-sql
source: my-pg-source
description: Search for hotels based on name.
parameters:
  - name: name
    type: string
    description: The name of the hotel.
statement: SELECT * FROM hotels WHERE name ILIKE '%' || $1 || '%';
```

有关配置不同类型工具的更多详细信息，请参阅[Tools](https://mcp-toolbox.dev/documentation/configuration/tools/)。

### 工具集 (Toolsets)

你的 `tools.yaml` 中的 `toolsets` 部分允许你定义希望一起加载的工具组。这对于基于智能体或应用定义不同分组非常有用。

```yaml
kind: toolset
name: my_first_toolset
tools:
    - my_first_tool
    - my_second_tool
---
kind: toolset
name: my_second_toolset
tools:
    - my_second_tool
    - my_third_tool
```

### 提示词 (Prompts)

你的 `tools.yaml` 中的 `prompts` 部分定义了可用于与 LLM 交互的提示词模板。

```yaml
kind: prompt
name: code_review
description: "Asks the LLM to analyze code quality and suggest improvements."
messages:
  - content: >
         Please review the following code for quality, correctness,
         and potential improvements: \n\n{{.code}}
arguments:
  - name: "code"
    description: "The code to review"
```

有关配置提示词的更多详细信息，请参阅[Prompts](https://mcp-toolbox.dev/documentation/configuration/prompts/)。

---

## 安装与运行 Toolbox 服务器

你可以直接使用[配置文件](#quick-start-custom-tools)运行 Toolbox：

```sh
npx @toolbox-sdk/server --config tools.yaml
```

此命令将以你的配置文件运行最新版本的 Toolbox 服务器。

> [!NOTE]
> 此方法侧重于便利性而非性能。 
> 如需更标准且可靠的安装方式，请按照[安装与运行 Toolbox 服务器](#install--run-the-toolbox-server)中的描述使用二进制文件或容器镜像。

### 安装 Toolbox

如需最新版本，请访问[发布页面][releases]，并根据你的操作系统和 CPU 架构使用以下说明进行安装。

[releases]: https://github.com/googleapis/mcp-toolbox/releases

<details open>
<summary>二进制文件</summary>

以二进制文件形式安装 Toolbox：

<!-- {x-release-please-start-version} -->
> <details>
> <summary>Linux (AMD64)</summary>
>
> 在 Linux (AMD64) 上以二进制文件形式安装 Toolbox：
>
> ```sh
> # see releases page for other versions
> export VERSION=1.2.0
> curl -L -o toolbox https://storage.googleapis.com/mcp-toolbox-for-databases/v$VERSION/linux/amd64/toolbox
> chmod +x toolbox
> ```
>
> </details>
> <details>
> <summary>macOS (Apple Silicon)</summary>
>
> 在 macOS (Apple Silicon) 上以二进制文件形式安装 Toolbox：
>
> ```sh
> # see releases page for other versions
> export VERSION=1.2.0
> curl -L -o toolbox https://storage.googleapis.com/mcp-toolbox-for-databases/v$VERSION/darwin/arm64/toolbox
> chmod +x toolbox
> ```
>
> </details>
> <details>
> <summary>macOS (Intel)</summary>
>
> 在 macOS (Intel) 上以二进制文件形式安装 Toolbox：
>
> ```sh
> # see releases page for other versions
> export VERSION=1.2.0
> curl -L -o toolbox https://storage.googleapis.com/mcp-toolbox-for-databases/v$VERSION/darwin/amd64/toolbox
> chmod +x toolbox
> ```
>
> </details>
> <details>
> <summary>Windows (Command Prompt)</summary>
>
> 在 Windows (命令提示符) 上以二进制文件形式安装 Toolbox：
>
> ```cmd
> :: see releases page for other versions
> set VERSION=1.2.0
> curl -o toolbox.exe "https://storage.googleapis.com/mcp-toolbox-for-databases/v%VERSION%/windows/amd64/toolbox.exe"
> ```
>
> </details>
> <details>
> <summary>Windows (PowerShell)</summary>
>
> 在 Windows (PowerShell) 上以二进制文件形式安装 Toolbox：
>
> ```powershell
> # see releases page for other versions
> $VERSION = "1.2.0"
> curl.exe -o toolbox.exe "https://storage.googleapis.com/mcp-toolbox-for-databases/v$VERSION/windows/amd64/toolbox.exe"
> ```
>
> </details>
</details>

<details>
<summary>容器镜像</summary>
你也可以将 Toolbox 作为容器进行安装：

```sh
# see releases page for other versions
export VERSION=1.2.0
docker pull us-central1-docker.pkg.dev/database-toolbox/toolbox/toolbox:$VERSION
```

</details>

<details>
<summary>Homebrew</summary>

在 macOS 或 Linux 上使用 Homebrew 安装 Toolbox：

```sh
brew install mcp-toolbox
```

</details>

<details>
<summary>从源码编译</summary>

要从源码安装，请确保已[安装最新版本的 Go](https://go.dev/doc/install)，然后运行以下命令：

```sh
go install github.com/googleapis/mcp-toolbox@v1.2.0
```
<!-- {x-release-please-end} -->

</details>
<details>
<summary>Gemini CLI</summary>
查看[Gemini CLI 扩展](https://geminicli.com/extensions/)以将特定数据库（如 AlloyDB、BigQuery 和 Cloud SQL）的预构建工具直接安装到 Gemini CLI。

```sh
# Install Gemini CLI
npm install -g @google/gemini-cli
# Install the extension
gemini extensions install https://github.com/gemini-cli-extensions/cloud-sql-postgres
# Run Gemini CLI
gemini
```

通过自然语言与你的自定义工具交互（使用 Gemini CLI）。

```sh
# Install the extension
gemini extensions install https://github.com/gemini-cli-extensions/mcp-toolbox
```
</details>


### 运行 Toolbox

[配置](#quick-start-custom-tools) `tools.yaml` 以定义你的工具，然后执行 `toolbox` 启动服务器：

<details open>
<summary>二进制文件</summary>

通过二进制文件运行 Toolbox：

```sh
./toolbox --config "tools.yaml"
```

> ⓘ Note  
> Toolbox enables dynamic reloading by default. To disable, use the
> `--disable-reload` flag.

</details>

<details>

<summary>容器镜像</summary>

拉取[容器镜像](#install-toolbox)后运行服务器：

```sh
export VERSION=0.24.0 # Use the version you pulled
docker run -p 5000:5000 \
-v $(pwd)/tools.yaml:/app/tools.yaml \
us-central1-docker.pkg.dev/database-toolbox/toolbox/toolbox:$VERSION \
--config "/app/tools.yaml"
```

> ⓘ Note  
> The `-v` flag mounts your local `tools.yaml` into the container, and `-p` maps
> the container's port `5000` to your host's port `5000`.

</details>

<details>

<summary>源码</summary>

要从源码直接运行服务器，请导航至项目根目录并运行：

```sh
go run .
```

> ⓘ Note  
> This command runs the project from source, and is more suitable for development
> and testing. It does **not** compile a binary into your `$GOPATH`. If you want
> to compile a binary instead, refer the [Developer
> Documentation](./DEVELOPER.md#building-the-binary).

</details>

<details>

<summary>Homebrew</summary>

如果你使用 [Homebrew](https://brew.sh/) 安装了 Toolbox，`toolbox` 二进制文件已存在于系统路径中。你可以使用相同的命令启动服务器：

```sh
toolbox --config "tools.yaml"
```

</details>

<details>
<summary>NPM</summary>

无需手动下载二进制文件即可直接运行 Toolbox（需要 Node.js）：
```sh
npx @toolbox-sdk/server --config tools.yaml
```

</details>
<details>
<summary>Gemini CLI</summary>
安装[Gemini CLI 扩展](https://geminicli.com/extensions/)后，预构建工具将在使用时自动可用。

```sh
# Run Gemini CLI
gemini

# List extensions
/extensions list
# List MCP servers
/mcp list
```

</details>


你可以使用 `toolbox help` 查看完整的标志列表！要停止服务器，请发送终止信号（大多数平台为 `ctrl+c`）。

有关部署到不同环境的更详细文档，请参阅[部署 Toolbox](https://mcp-toolbox.dev/documentation/deploy-to/) 部分。

---

## 连接至 Toolbox

当你的 Toolbox 服务器启动并运行后，即可将工具加载到你的 MCP 兼容客户端或应用程序中。 

### MCP 客户端

在你的 MCP 客户端配置中添加以下设置：

```json
{
  "mcpServers": {
    "toolbox": {
      "type": "http",
      "url": "http://127.0.0.1:5000/mcp",
    }
  }
}
```

如需连接到特定的工具集，请将 URL 替换为 `http://127.0.0.1:5000/mcp/{toolset_name}`。


### Toolbox SDK：集成到你的应用中

Toolbox 客户端 SDK 提供了易于使用的构建模块和高级功能，用于将你的自定义应用程序连接到 MCP Toolbox 服务器。以下是各种框架的客户端 SDK 列表：

<details open>
  <summary>Python (<a href="https://github.com/googleapis/mcp-toolbox-sdk-python">Github</a>)</summary>
  <br>
  <blockquote>

  <details open>
    <summary>核心模块 (Core)</summary>

1. 安装 [Toolbox Core SDK][toolbox-core]：

    ```bash
    pip install toolbox-core
    ```

2. 加载工具：

    ```python
    from toolbox_core import ToolboxClient

    # update the url to point to your server
    async with ToolboxClient("http://127.0.0.1:5000") as client:

        # these tools can be passed to your application!
        tools = await client.load_toolset("toolset_name")
    ```

有关使用 Toolbox Core SDK 的更详细说明，请参阅[项目的 README][toolbox-core-readme]。

[toolbox-core]: https://pypi.org/project/toolbox-core/
[toolbox-core-readme]: https://github.com/googleapis/mcp-toolbox-sdk-python/tree/main/packages/toolbox-core/README.md

  </details>
  <details>
    <summary>LangChain / LangGraph</summary>

1. 安装 [Toolbox LangChain SDK][toolbox-langchain]：

    ```bash
    pip install toolbox-langchain
    ```

2. 加载工具：

    ```python
    from toolbox_langchain import ToolboxClient

    # update the url to point to your server
    async with ToolboxClient("http://127.0.0.1:5000") as client:

        # these tools can be passed to your application!
        tools = client.load_toolset()
    ```

    有关使用 Toolbox LangChain SDK 的更详细说明，请参阅[项目的 README][toolbox-langchain-readme]。

    [toolbox-langchain]: https://pypi.org/project/toolbox-langchain/
    [toolbox-langchain-readme]: https://github.com/googleapis/mcp-toolbox-sdk-python/blob/main/packages/toolbox-langchain/README.md

  </details>
  <details>
    <summary>LlamaIndex</summary>

1. 安装 [Toolbox Llamaindex SDK][toolbox-llamaindex]：

    ```bash
    pip install toolbox-llamaindex
    ```

2. 加载工具：

    ```python
    from toolbox_llamaindex import ToolboxClient

    # update the url to point to your server
    async with ToolboxClient("http://127.0.0.1:5000") as client:

        # these tools can be passed to your application!
        tools = client.load_toolset()
    ```

    有关使用 Toolbox Llamaindex SDK 的更详细说明，请参阅[项目的 README][toolbox-llamaindex-readme]。

    [toolbox-llamaindex]: https://pypi.org/project/toolbox-llamaindex/
    [toolbox-llamaindex-readme]: https://github.com/googleapis/genai-toolbox-llamaindex-python/blob/main/README.md

  </details>
</details>
</blockquote>
<details>
  <summary>JavaScript/TypeScript (<a href="https://github.com/googleapis/mcp-toolbox-sdk-js">Github</a>)</summary>
  <br>
  <blockquote>

  <details open>
    <summary>核心模块 (Core)</summary>

1. 安装 [Toolbox Core SDK][toolbox-core-js]：

    ```bash
    npm install @toolbox-sdk/core
    ```

2. 加载工具：

    ```javascript
    import { ToolboxClient } from '@toolbox-sdk/core';

    // update the url to point to your server
    const URL = 'http://127.0.0.1:5000';
    let client = new ToolboxClient(URL);

    // these tools can be passed to your application!
    const tools = await client.loadToolset('toolsetName');
    ```

    有关使用 Toolbox Core SDK 的更详细说明，请参阅[项目的 README][toolbox-core-js-readme]。

    [toolbox-core-js]: https://www.npmjs.com/package/@toolbox-sdk/core
    [toolbox-core-js-readme]: https://github.com/googleapis/mcp-toolbox-sdk-js/blob/main/packages/toolbox-core/README.md

  </details>
  <details>
    <summary>LangChain / LangGraph</summary>

1. 安装 [Toolbox Core SDK][toolbox-core-js]：

    ```bash
    npm install @toolbox-sdk/core
    ```

2. 加载工具：

    ```javascript
    import { ToolboxClient } from '@toolbox-sdk/core';

    // update the url to point to your server
    const URL = 'http://127.0.0.1:5000';
    let client = new ToolboxClient(URL);

    // these tools can be passed to your application!
    const toolboxTools = await client.loadToolset('toolsetName');

    // Define the basics of the tool: name, description, schema and core logic
    const getTool = (toolboxTool) => tool(currTool, {
        name: toolboxTool.getName(),
        description: toolboxTool.getDescription(),
        schema: toolboxTool.getParamSchema()
    });

    // Use these tools in your Langchain/Langraph applications
    const tools = toolboxTools.map(getTool);
    ```

  </details>
  <details>
    <summary>Genkit</summary>

1. 安装 [Toolbox Core SDK][toolbox-core-js]：

    ```bash
    npm install @toolbox-sdk/core
    ```

2. 加载工具：

    ```javascript
    import { ToolboxClient } from '@toolbox-sdk/core';
    import { genkit } from 'genkit';

    // Initialise genkit
    const ai = genkit({
        plugins: [
            googleAI({
                apiKey: process.env.GEMINI_API_KEY || process.env.GOOGLE_API_KEY
            })
        ],
        model: googleAI.model('gemini-2.0-flash'),
    });

    // update the url to point to your server
    const URL = 'http://127.0.0.1:5000';
    let client = new ToolboxClient(URL);

    // these tools can be passed to your application!
    const toolboxTools = await client.loadToolset('toolsetName');

    // Define the basics of the tool: name, description, schema and core logic
    const getTool = (toolboxTool) => ai.defineTool({
        name: toolboxTool.getName(),
        description: toolboxTool.getDescription(),
        schema: toolboxTool.getParamSchema()
    }, toolboxTool)

    // Use these tools in your Genkit applications
    const tools = toolboxTools.map(getTool);
    ```

  </details>
  <details>
    <summary>ADK</summary>

1. 安装 [Toolbox ADK SDK][toolbox-adk-js]：

    ```bash
    npm install @toolbox-sdk/adk
    ```

2. 加载工具：

    ```javascript
    import { ToolboxClient } from '@toolbox-sdk/adk';

    // update the url to point to your server
    const URL = 'http://127.0.0.1:5000';
    let client = new ToolboxClient(URL);

    // these tools can be passed to your application!
    const tools = await client.loadToolset('toolsetName');
    ```

    有关使用 Toolbox ADK SDK 的更详细说明，请参阅[项目的 README][toolbox-adk-js-readme]。

    [toolbox-adk-js]: https://www.npmjs.com/package/@toolbox-sdk/adk
    [toolbox-adk-js-readme]:
       https://github.com/googleapis/mcp-toolbox-sdk-js/blob/main/packages/toolbox-adk/README.md

  </details>
</details>
</blockquote>
<details>
  <summary>Go (<a href="https://github.com/googleapis/mcp-toolbox-sdk-go">Github</a>)</summary>
  <br>
  <blockquote>

  <details>
    <summary>核心模块 (Core)</summary>

1. 安装 [Toolbox Go SDK][toolbox-go]：

    ```bash
    go get github.com/googleapis/mcp-toolbox-sdk-go
    ```

2. 加载工具：

    ```go
    package main

    import (
      "github.com/googleapis/mcp-toolbox-sdk-go/core"
      "context"
    )

    func main() {
      // Make sure to add the error checks
      // update the url to point to your server
      URL := "http://127.0.0.1:5000";
      ctx := context.Background()

      client, err := core.NewToolboxClient(URL)

      // Framework agnostic tools
      tools, err := client.LoadToolset("toolsetName", ctx)
    }
    ```

    有关使用 Toolbox Go SDK 的更详细说明，请参阅[项目的 README][toolbox-core-go-readme]。

    [toolbox-go]: https://pkg.go.dev/github.com/googleapis/mcp-toolbox-sdk-go/core
    [toolbox-core-go-readme]: https://github.com/googleapis/mcp-toolbox-sdk-go/blob/main/core/README.md

  </details>
  <details>
    <summary>LangChain Go</summary>

1. 安装 [Toolbox Go SDK][toolbox-go]：

    ```bash
    go get github.com/googleapis/mcp-toolbox-sdk-go
    ```

2. 加载工具：

    ```go
    package main

    import (
      "context"
      "encoding/json"

      "github.com/googleapis/mcp-toolbox-sdk-go/core"
      "github.com/tmc/langchaingo/llms"
    )

    func main() {
      // Make sure to add the error checks
      // update the url to point to your server
      URL := "http://127.0.0.1:5000"
      ctx := context.Background()

      client, err := core.NewToolboxClient(URL)

      // Framework agnostic tool
      tool, err := client.LoadTool("toolName", ctx)

      // Fetch the tool's input schema
      inputschema, err := tool.InputSchema()

      var paramsSchema map[string]any
      _ = json.Unmarshal(inputschema, &paramsSchema)

      // Use this tool with LangChainGo
      langChainTool := llms.Tool{
        Type: "function",
        Function: &llms.FunctionDefinition{
          Name:        tool.Name(),
          Description: tool.Description(),
          Parameters:  paramsSchema,
        },
      }
    }

    ```

  </details>
  <details>
    <summary>Genkit</summary>

1. 安装 [Toolbox Go SDK][toolbox-go]：

    ```bash
    go get github.com/googleapis/mcp-toolbox-sdk-go
    ```

2. 加载工具：

    ```go
    package main
    import (
      "context"
      "log"

      "github.com/firebase/genkit/go/genkit"
      "github.com/googleapis/mcp-toolbox-sdk-go/core"
      "github.com/googleapis/mcp-toolbox-sdk-go/tbgenkit"
    )

    func main() {
      // Make sure to add the error checks
      // Update the url to point to your server
      URL := "http://127.0.0.1:5000"
      ctx := context.Background()
      g := genkit.Init(ctx)

      client, err := core.NewToolboxClient(URL)

      // Framework agnostic tool
      tool, err := client.LoadTool("toolName", ctx)

      // Convert the tool using the tbgenkit package
      // Use this tool with Genkit Go
      genkitTool, err := tbgenkit.ToGenkitTool(tool, g)
      if err != nil {
        log.Fatalf("Failed to convert tool: %v\n", err)
      }
      log.Printf("Successfully converted tool: %s", genkitTool.Name())
    }
    ```

  </details>
  <details>
    <summary>Go GenAI</summary>

1. 安装 [Toolbox Go SDK][toolbox-go]：

    ```bash
    go get github.com/googleapis/mcp-toolbox-sdk-go
    ```

2. 加载工具：

    ```go
    package main

    import (
      "context"
      "encoding/json"

      "github.com/googleapis/mcp-toolbox-sdk-go/core"
      "google.golang.org/genai"
    )

    func main() {
      // Make sure to add the error checks
      // Update the url to point to your server
      URL := "http://127.0.0.1:5000"
      ctx := context.Background()

      client, err := core.NewToolboxClient(URL)

      // Framework agnostic tool
      tool, err := client.LoadTool("toolName", ctx)

      // Fetch the tool's input schema
      inputschema, err := tool.InputSchema()

      var schema *genai.Schema
      _ = json.Unmarshal(inputschema, &schema)

      funcDeclaration := &genai.FunctionDeclaration{
        Name:        tool.Name(),
        Description: tool.Description(),
        Parameters:  schema,
      }

      // Use this tool with Go GenAI
      genAITool := &genai.Tool{
        FunctionDeclarations: []*genai.FunctionDeclaration{funcDeclaration},
      }
    }
    ```

  </details>
  <details>
    <summary>OpenAI Go</summary>

1. 安装 [Toolbox Go SDK][toolbox-go]：

    ```bash
    go get github.com/googleapis/mcp-toolbox-sdk-go
    ```

2. 加载工具：

    ```go
    package main

    import (
      "context"
      "encoding/json"

      "github.com/googleapis/mcp-toolbox-sdk-go/core"
      openai "github.com/openai/openai-go"
    )

    func main() {
      // Make sure to add the error checks
      // Update the url to point to your server
      URL := "http://127.0.0.1:5000"
      ctx := context.Background()

      client, err := core.NewToolboxClient(URL)

      // Framework agnostic tool
      tool, err := client.LoadTool("toolName", ctx)

      // Fetch the tool's input schema
      inputschema, err := tool.InputSchema()

      var paramsSchema openai.FunctionParameters
      _ = json.Unmarshal(inputschema, &paramsSchema)

      // Use this tool with OpenAI Go
      openAITool := openai.ChatCompletionToolParam{
        Function: openai.FunctionDefinitionParam{
          Name:        tool.Name(),
          Description: openai.String(tool.Description()),
          Parameters:  paramsSchema,
        },
      }

    }
    ```

  </details>
  <details open>
    <summary>ADK Go</summary>

1. 安装 [Toolbox Go SDK][toolbox-go]：

    ```bash
    go get github.com/googleapis/mcp-toolbox-sdk-go
    ```

2. 加载工具：

    ```go
    package main

    import (
      "github.com/googleapis/mcp-toolbox-sdk-go/tbadk"
      "context"
    )

    func main() {
      // Make sure to add the error checks
      // Update the url to point to your server
      URL := "http://127.0.0.1:5000"
      ctx := context.Background()
      client, err := tbadk.NewToolboxClient(URL)
      if err != nil {
        return fmt.Sprintln("Could not start Toolbox Client", err)
      }

      // Use this tool with ADK Go
      tool, err := client.LoadTool("toolName", ctx)
      if err != nil {
        return fmt.Sprintln("Could not load Toolbox Tool", err)
      }
    }
    ```

    有关使用 Toolbox Go SDK 的更详细说明，请参阅[项目的 README][toolbox-core-go-readme]。


  </details>
</details>
</blockquote>
</details>

---

## 其他功能

### 使用 Toolbox UI 测试工具

要启动 Toolbox 的交互式界面，请使用 `--ui` 标志。这允许你测试工具和工具集（包括授权参数等功能）。欲了解更多，请访问[Toolbox UI](https://mcp-toolbox.dev/documentation/configuration/toolbox-ui/)。

```sh
./toolbox --ui
```

### 遥测数据 (Telemetry)

Toolbox 通过 OpenTelemetry 发出追踪和指标数据。使用 `--telemetry-otlp=<endpoint>` 将数据导出到任何兼容 OTLP 的后端（如 Google Cloud Monitoring、Agnost AI 或其他服务）。详见[遥测文档](https://mcp-toolbox.dev/documentation/monitoring/export_telemetry/)。

### 生成智能体技能 (Agent Skills)

`skills-generate` 命令允许你将一个**工具集**转换为符合[Agent Skill 规范](https://agentskills.io/specification)的**智能体技能**。这非常适用于将工具作为可移植的技能包进行分发。

```bash
toolbox --config tools.yaml skills-generate \
  --name "my-skill" \
  --toolset "my_toolset" \
  --description "A skill containing multiple tools"
```

生成后，你可以将该技能安装到 Gemini CLI 中：

```bash
gemini skills install ./skills/my-skill
```

欲了解更多详情，请参阅[生成智能体技能指南](https://mcp-toolbox.dev/documentation/configuration/skills/)。

---

## 版本控制

数据库 MCP Toolbox 遵循[语义化版本控制](https://semver.org/)规范。

公共 API 包含 Toolbox 服务器（CLI、配置清单和预构建工具集）以及客户端 SDK。

- **主版本（Major）**：针对不兼容的 CLI 或配置清单更改等破坏性更新进行递增。
- **次版本（Minor）**：针对新功能（包括预构建工具集修改或 Beta 功能）进行递增。
- **修订版（Patch）**：针对向后兼容的 Bug 修复进行递增。

欲了解更多详情，请参阅我们的[完整版本控制策略](https://mcp-toolbox.dev/reference/versioning/)。

---

## 贡献指南

欢迎贡献代码。请查阅 [CONTRIBUTING](CONTRIBUTING.md) 指南以开始参与。 

如需在本地搭建 Toolbox 开发环境的详细说明，请参阅 [DEVELOPER](DEVELOPER.md) 指南。

请注意，本项目采用贡献者行为准则。参与本项目即表示你同意遵守其条款。详见[贡献者行为准则](CODE_OF_CONDUCT.md)。

---

## 社区交流

加入我们的 [Discord 社区](https://discord.gg/GQrFB3Ec3W)，与开发者们建立联系！