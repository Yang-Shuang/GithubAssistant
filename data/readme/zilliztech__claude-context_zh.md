![](assets/claude-context.png)

> 🆕 **正在寻找为 Claude Code 提供持久化记忆的方案？** 请查看 [memsearch Claude Code 插件](https://github.com/zilliztech/memsearch#for-claude-code-users) —— 这是一个基于 Markdown 的内存系统，为你的 AI Agent 跨会话提供长期记忆。

### 将你的整个代码库作为 Claude 的上下文

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Node.js](https://img.shields.io/badge/Node.js-20%2B-green.svg)](https://nodejs.org/)
[![Documentation](https://img.shields.io/badge/Documentation-📚-orange.svg)](docs/)
[![VS Code Marketplace](https://img.shields.io/visual-studio-marketplace/v/zilliz.semanticcodesearch?label=VS%20Code%20Extension&logo=visual-studio-code)](https://marketplace.visualstudio.com/items?itemName=zilliz.semanticcodesearch)
[![npm - core](https://img.shields.io/npm/v/@zilliz/claude-context-core?label=%40zilliz%2Fclaude-context-core&logo=npm)](https://www.npmjs.com/package/@zilliz/claude-context-core)
[![npm - mcp](https://img.shields.io/npm/v/@zilliz/claude-context-mcp?label=%40zilliz%2Fclaude-context-mcp&logo=npm)](https://www.npmjs.com/package/@zilliz/claude-context-mcp)
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/zilliz_universe.svg?style=social&label=Follow%20%40Zilliz)](https://twitter.com/zilliz_universe)
[![DeepWiki](https://img.shields.io/badge/DeepWiki-AI%20Docs-purple.svg?logo=gitbook&logoColor=white)](https://deepwiki.com/zilliztech/claude-context)
<a href="https://discord.gg/mKc3R95yE5"><img height="20" src="https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white" alt="discord" /></a>
<a href="https://trendshift.io/repositories/15064"><img src="https://trendshift.io/api/badge/repositories/15064" alt="zilliztech/claude-context | Trendshift" width="250" height="55" /></a>
</div>

**Claude Context** 是一个 MCP（模型上下文协议）插件，为 Claude Code 和其他 AI 编程 Agent 添加了语义代码搜索功能，使它们能够获取来自你整个代码库的深度上下文。

🧠 **将你的整个代码库作为上下文**：Claude Context 使用语义搜索从数百万行代码中查找所有相关代码。无需多轮发现过程，直接将结果带入 Claude 的上下文中。

💰 **大型代码库更具成本效益**：与其为每次请求将整个目录加载到 Claude 中（这可能会非常昂贵），Claude Context 会高效地将你的代码库存储在向量数据库中，并仅在上下文中使用相关代码，从而控制成本。

---

## 🚀 演示

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf2uIf2c5zowp-iOMOqsefHbY_EwNGiutkxtNXcZVJ8RI6SN9DsCcsc3amXIhOZx9VcKFJQLSAqM-2pjU9zoGs1r8GCTUL3JIsLpLUGAm1VQd5F2o5vpEajx2qrc77iXhBu1zWj?key=qYdFquJrLcfXCUndY-YRBQ)

模型上下文协议（Model Context Protocol，简称 MCP）允许你将 Claude Context 与你喜爱的 AI 编程助手集成，例如 Claude Code。

## 快速开始

### 前置条件

<details>
<summary>在 Zilliz Cloud 上获取免费向量数据库 👈</summary>

Claude Context 需要一个向量数据库。你可以在 [Zilliz Cloud](https://cloud.zilliz.com/signup?utm_source=github&utm_medium=referral&utm_campaign=2507-codecontext-readme) 注册以获取 API Key。

![](assets/signup_and_get_apikey.png)

复制你的 Personal Key，用于替换配置示例中的 `your-zilliz-cloud-api-key`。
</details>

<details>
<summary>获取用于嵌入模型的 OpenAI API Key</summary>

你需要一个 OpenAI API Key 来运行嵌入模型。你可以在 [OpenAI](https://platform.openai.com/api-keys) 注册获取。  

你的 API Key 格式如下：始终以 `sk-` 开头。  
复制你的密钥，并在下方的配置示例中将其作为 `your-openai-api-key` 使用。

</details>

### 为 Claude Code 配置 MCP

**系统要求：**

- Node.js >= 20.0.0

#### 配置

使用命令行界面添加 Claude Context MCP 服务器：

```bash
claude mcp add claude-context \
  -e OPENAI_API_KEY=sk-your-openai-api-key \
  -e MILVUS_ADDRESS=your-zilliz-cloud-public-endpoint \
  -e MILVUS_TOKEN=your-zilliz-cloud-api-key \
  -- npx @zilliz/claude-context-mcp@latest
```

有关 MCP 服务器管理的更多详细信息，请参阅 [Claude Code MCP 文档](https://docs.anthropic.com/en/docs/claude-code/mcp)。

### 其他 MCP 客户端配置

<details>
<summary><strong>OpenAI Codex CLI</strong></summary>

Codex CLI 使用 TOML 配置文件：

1. 创建或编辑 `~/.codex/config.toml` 文件。

2. 添加以下配置：

```toml
# IMPORTANT: the top-level key is `mcp_servers` rather than `mcpServers`.
[mcp_servers.claude-context]
command = "npx"
args = ["@zilliz/claude-context-mcp@latest"]
env = { "OPENAI_API_KEY" = "your-openai-api-key", "MILVUS_TOKEN" = "your-zilliz-cloud-api-key" }
# Optional: override the default 10s startup timeout
startup_timeout_ms = 20000
```

3. 保存文件并重启 Codex CLI 以应用更改。

</details>

<details>
<summary><strong>Gemini CLI</strong></summary>

Gemini CLI 需要通过 JSON 文件进行手动配置：

1. 创建或编辑 `~/.gemini/settings.json` 文件。
2. 添加以下配置：

```json
{
  "mcpServers": {
    "claude-context": {
      "command": "npx",
      "args": ["@zilliz/claude-context-mcp@latest"],
      "env": {
        "OPENAI_API_KEY": "your-openai-api-key",
        "MILVUS_TOKEN": "your-zilliz-cloud-api-key"
      }
    }
  }
}
```

3. 保存文件并重启 Gemini CLI 以应用更改。

</details>

<details>
<summary><strong>Qwen Code</strong></summary>

创建或编辑 `~/.qwen/settings.json` 文件，并添加以下配置：

```json
{
  "mcpServers": {
    "claude-context": {
      "command": "npx",
      "args": ["@zilliz/claude-context-mcp@latest"],
      "env": {
        "OPENAI_API_KEY": "your-openai-api-key",
        "MILVUS_ADDRESS": "your-zilliz-cloud-public-endpoint",
        "MILVUS_TOKEN": "your-zilliz-cloud-api-key"
      }
    }
  }
}
```

</details>

<details>
<summary><strong>Cursor</strong></summary>

前往：`Settings` -> `Cursor Settings` -> `MCP` -> `Add new global MCP server`

将以下配置粘贴到 Cursor 的 `~/.cursor/mcp.json` 文件中是推荐的做法。你也可以通过在项目文件夹中创建 `.cursor/mcp.json` 来为特定项目安装。更多信息请参阅 [Cursor MCP 文档](https://cursor.com/docs/context/mcp)。

```json
{
  "mcpServers": {
    "claude-context": {
      "command": "npx",
      "args": ["-y", "@zilliz/claude-context-mcp@latest"],
      "env": {
        "OPENAI_API_KEY": "your-openai-api-key",
        "MILVUS_ADDRESS": "your-zilliz-cloud-public-endpoint",
        "MILVUS_TOKEN": "your-zilliz-cloud-api-key"
      }
    }
  }
}
```

</details>

<details>
<summary><strong>Void</strong></summary>

前往：`Settings` -> `MCP` -> `Add MCP Server`

将以下配置添加到你的 Void MCP 设置中：

```json
{
  "mcpServers": {
    "code-context": {
      "command": "npx",
      "args": ["-y", "@zilliz/claude-context-mcp@latest"],
      "env": {
        "OPENAI_API_KEY": "your-openai-api-key",
        "MILVUS_ADDRESS": "your-zilliz-cloud-public-endpoint",
        "MILVUS_TOKEN": "your-zilliz-cloud-api-key"
      }
    }
  }
}
```

</details>

<details>
<summary><strong>Claude Desktop</strong></summary>

添加到你的 Claude Desktop 配置中：

```json
{
  "mcpServers": {
    "claude-context": {
      "command": "npx",
      "args": ["@zilliz/claude-context-mcp@latest"],
      "env": {
        "OPENAI_API_KEY": "your-openai-api-key",
        "MILVUS_ADDRESS": "your-zilliz-cloud-public-endpoint",
        "MILVUS_TOKEN": "your-zilliz-cloud-api-key"
      }
    }
  }
}
```

</details>

<details>
<summary><strong>Windsurf</strong></summary>

Windsurf 支持通过 JSON 文件进行 MCP 配置。将以下配置添加到你的 Windsurf MCP 设置中：

```json
{
  "mcpServers": {
    "claude-context": {
      "command": "npx",
      "args": ["-y", "@zilliz/claude-context-mcp@latest"],
      "env": {
        "OPENAI_API_KEY": "your-openai-api-key",
        "MILVUS_ADDRESS": "your-zilliz-cloud-public-endpoint",
        "MILVUS_TOKEN": "your-zilliz-cloud-api-key"
      }
    }
  }
}
```

</details>

<details>
<summary><strong>VS Code</strong></summary>

Claude Context MCP 服务器可通过支持 MCP 的扩展在 VS Code 中使用。将以下配置添加到你的 VS Code MCP 设置中：

```json
{
  "mcpServers": {
    "claude-context": {
      "command": "npx",
      "args": ["-y", "@zilliz/claude-context-mcp@latest"],
      "env": {
        "OPENAI_API_KEY": "your-openai-api-key",
        "MILVUS_ADDRESS": "your-zilliz-cloud-public-endpoint",
        "MILVUS_TOKEN": "your-zilliz-cloud-api-key"
      }
    }
  }
}
```

</details>

<details>
<summary><strong>Cherry Studio</strong></summary>

Cherry Studio 允许通过其设置界面进行可视化的 MCP 服务器配置。虽然它不直接支持手动 JSON 配置，但你可以通过 GUI 添加新服务器：

1. 导航至 **Settings → MCP Servers → Add Server**。
2. 填写服务器详细信息：
   - **Name**（名称）: `claude-context`
   - **Type**（类型）: `STDIO`
   - **Command**（命令）: `npx`
   - **Arguments**（参数）: `["-y", "@zilliz/claude-context-mcp@latest"]`
   - **Environment Variables**（环境变量）:
     - `OPENAI_API_KEY`: `your-openai-api-key`
     - `MILVUS_ADDRESS`: `your-zilliz-cloud-public-endpoint`
     - `MILVUS_TOKEN`: `your-zilliz-cloud-api-key`
3. 保存配置以激活服务器。

</details>

<details>
<summary><strong>Cline</strong></summary>

Cline 使用 JSON 配置文件来管理 MCP 服务器。要集成提供的 MCP 服务器配置：

1. 打开 Cline，点击顶部导航栏中的 **MCP Servers** 图标。

2. 选择 **Installed**（已安装）选项卡，然后点击 **Advanced MCP Settings**。

3. 在 `cline_mcp_settings.json` 文件中，添加以下配置：

```json
{
  "mcpServers": {
    "claude-context": {
      "command": "npx",
      "args": ["@zilliz/claude-context-mcp@latest"],
      "env": {
        "OPENAI_API_KEY": "your-openai-api-key",
        "MILVUS_ADDRESS": "your-zilliz-cloud-public-endpoint",
        "MILVUS_TOKEN": "your-zilliz-cloud-api-key"
      }
    }
  }
}
```

4. 保存文件。

</details>

<details>
<summary><strong>Augment</strong></summary>

要在 Augment Code 中配置 Claude Context MCP，你可以使用图形界面或手动配置。

#### **A. 使用 Augment Code UI**

1. 点击汉堡菜单（三条横线）。

2. 选择 **Settings**。

3. 导航到 **Tools** 部分。

4. 点击 **+ Add MCP** 按钮。

5. 输入以下命令：

   ```
   npx @zilliz/claude-context-mcp@latest
   ```

6. 为 MCP 命名：**Claude Context**。

7. 点击 **Add** 按钮。

------

#### **B. 手动配置**

1. 按 Cmd/Ctrl Shift P 或前往 Augment 面板中的汉堡菜单
2. 选择 Edit Settings
3. 在 Advanced（高级）下，点击 settings.json 中的 Edit
4. 将服务器配置添加到 `augment.advanced` 对象下的 `mcpServers` 数组中

```json
"augment.advanced": { 
  "mcpServers": [ 
    { 
      "name": "claude-context", 
      "command": "npx", 
      "args": ["-y", "@zilliz/claude-context-mcp@latest"],
      "env": {
        "OPENAI_API_KEY": "your-openai-api-key",
        "MILVUS_ADDRESS": "your-zilliz-cloud-public-endpoint",
        "MILVUS_TOKEN": "your-zilliz-cloud-api-key"
      }
    }
  ]
}
```

</details>

<details>
<summary><strong>Roo Code</strong></summary>

Roo Code 使用 JSON 配置文件管理 MCP 服务器：

1. 打开 Roo Code，导航至 **Settings → MCP Servers → Edit Global Config**。

2. 在 `mcp_settings.json` 文件中，添加以下配置：

```json
{
  "mcpServers": {
    "claude-context": {
      "command": "npx",
      "args": ["@zilliz/claude-context-mcp@latest"],
      "env": {
        "OPENAI_API_KEY": "your-openai-api-key",
        "MILVUS_ADDRESS": "your-zilliz-cloud-public-endpoint",
        "MILVUS_TOKEN": "your-zilliz-cloud-api-key"
      }
    }
  }
}
```

3. 保存文件以激活服务器。

</details>

<details>
<summary><strong>Zencoder</strong></summary>

Zencoder 在其 JetBrains 和 VS Code 插件版本中均支持 MCP 工具和服务器。

1. 前往 Zencoder 菜单 (...)
2. 从下拉菜单中选择 `Tools`
3. 点击 `Add Custom MCP`
4. 添加名称（即 `Claude Context`）及下方的服务器配置，并确保点击 `Install` 按钮

```json
{
    "command": "npx",
    "args": ["@zilliz/claude-context-mcp@latest"],
    "env": {
      "OPENAI_API_KEY": "your-openai-api-key",
      "MILVUS_ADDRESS": "your-zilliz-cloud-public-endpoint",
      "MILVUS_TOKEN": "your-zilliz-cloud-api-key"
    }
}

```

5. 点击 `Install` 按钮保存服务器。

</details>

<details>
<summary><strong>LangChain/LangGraph</strong></summary>

有关 LangChain/LangGraph 集成示例，请参阅 [此示例](https://github.com/zilliztech/claude-context/blob/643796a0d30e706a2a0dff3d55621c9b5d831807/evaluation/retrieval/custom.py#L88)。

</details>

<details>
<summary><strong>Other MCP Clients</strong></summary>

该服务器使用 stdio 传输协议并遵循标准 MCP 协议。你可以通过运行以下命令将其集成到任何支持 MCP 的客户端中：

```bash
npx @zilliz/claude-context-mcp@latest
```

</details>

---

### 在你的代码库中使用

1. **打开 Claude Code**

   ```
   cd your-project-directory
   claude
   ```

2. **索引你的代码库**：

   ```
   Index this codebase
   ```

3. **检查索引状态**：

   ```
   Check the indexing status
   ```

4. **开始搜索**：

   ```
   Find functions that handle user authentication
   ```

🎉 **大功告成！** 你现在已在 Claude Code 中拥有了语义代码搜索功能。

---

### 环境变量配置

有关更详细的 MCP 环境变量配置，请参阅我们的[环境变量指南](docs/getting-started/environment-variables.md)。

### 使用不同的嵌入模型

若要配置自定义嵌入模型（例如 OpenAI 的 `text-embedding-3-large` 或 VoyageAI 的 `voyage-code-3`），请参阅[MCP 配置示例](packages/mcp/README.md#embedding-provider-configuration)，其中包含各提供商的详细设置说明。

### 文件包含与排除规则

有关文件包含与排除规则的详细说明及自定义方法，请参阅我们的[文件包含与排除规则](docs/dive-deep/file-inclusion-rules.md)。

### 可用工具

#### 1. `index_codebase`

对代码库目录进行索引以支持混合搜索（BM25 + 稠密向量）。

#### 2. `search_code`

使用自然语言查询和混合搜索（BM25 + 稠密向量）在已索引的代码库中进行搜索。

#### 3. `clear_index`

清除特定代码库的搜索索引。

#### 4. `get_indexing_status`

获取代码库当前的索引状态。显示正在索引的代码库的进度百分比，以及已完成索引的代码库的状态信息。

---

## 📊 评估

我们的受控评估表明，在检索质量相当的情况下，Claude Context MCP 可实现约 40% 的 Token 节省。这在生产环境中意味着显著的成本和时间节约。这也说明，在有限的 Token 上下文长度约束下，使用 Claude Context 能够获得更好的检索和回答效果。

![MCP Efficiency Analysis](assets/mcp_efficiency_analysis_chart.png)

有关详细的评估方法和结果，请参阅 [evaluation 目录](evaluation/)。

---

## 🏗️ 架构

![](assets/Architecture.png)

### 🔧 实现细节

- 🔍 **混合代码搜索**：提问如 *"find functions that handle user authentication"*，即可通过先进的混合搜索（BM25 + 稠密向量）即时获取相关且上下文丰富的代码。
- 🧠 **上下文感知**：探索大型代码库，理解代码库各部分之间的关系，即使跨越数百万行代码也能准确关联。
- ⚡ **增量索引**：使用 Merkle 树仅对更改的文件进行高效重新索引。
- 🧩 **智能代码分块**：基于抽象语法树（AST）分析代码以进行分块处理。
- 🗄️ **可扩展性**：与 Zilliz Cloud 集成以实现可扩展的向量搜索，无论你的代码库有多大都能轻松应对。
- 🛠️ **可定制**：支持配置文件扩展名、忽略模式以及嵌入模型。

### 核心组件

Claude Context 是一个 monorepo（单体仓库），包含三个主要包：

- **`@zilliz/claude-context-core`**：核心索引引擎，集成嵌入模型与向量数据库
- **VSCode Extension**：面向 Visual Studio Code 的语义代码搜索扩展
- **`@zilliz/claude-context-mcp`**：面向 AI Agent 集成的模型上下文协议服务器

### 支持的技术栈

- **嵌入提供商（Embedding Providers）**：[OpenAI](https://openai.com), [VoyageAI](https://voyageai.com), [Ollama](https://ollama.com), [Gemini](https://gemini.google.com)
- **向量数据库**：[Milvus](https://milvus.io) 或 [Zilliz Cloud](https://zilliz.com/cloud)（全托管的向量即服务）
- **代码分割器（Code Splitters）**：基于 AST 的分块器（带自动回退机制）、LangChain 字符级分块器
- **编程语言**：TypeScript, JavaScript, Python, Java, C++, C#, Go, Rust, PHP, Ruby, Swift, Kotlin, Scala, Markdown
- **开发工具**：VSCode, Model Context Protocol

---

## 📦 Claude Context 的其他使用方式

虽然推荐使用 MCP 方式与 AI 助手配合使用，但你也可以直接使用或通过 VSCode 扩展使用。

### 使用核心包构建应用

`@zilliz/claude-context-core` 包提供了代码索引和语义搜索的基础功能。

```typescript
import { Context, MilvusVectorDatabase, OpenAIEmbedding } from '@zilliz/claude-context-core';

// Initialize embedding provider
const embedding = new OpenAIEmbedding({
    apiKey: process.env.OPENAI_API_KEY || 'your-openai-api-key',
    model: 'text-embedding-3-small'
});

// Initialize vector database
const vectorDatabase = new MilvusVectorDatabase({
    address: process.env.MILVUS_ADDRESS || 'your-zilliz-cloud-public-endpoint',
    token: process.env.MILVUS_TOKEN || 'your-zilliz-cloud-api-key'
});

// Create context instance
const context = new Context({
    embedding,
    vectorDatabase
});

// Index your codebase with progress tracking
const stats = await context.indexCodebase('./your-project', (progress) => {
    console.log(`${progress.phase} - ${progress.percentage}%`);
});
console.log(`Indexed ${stats.indexedFiles} files, ${stats.totalChunks} chunks`);

// Perform semantic search
const results = await context.semanticSearch('./your-project', 'vector database operations', 5);
results.forEach(result => {
    console.log(`File: ${result.relativePath}:${result.startLine}-${result.endLine}`);
    console.log(`Score: ${(result.score * 100).toFixed(2)}%`);
    console.log(`Content: ${result.content.substring(0, 100)}...`);
});
```

### VS Code 扩展

将 Claude Context 直接集成到你的 IDE 中。提供直观的语义代码搜索和导航界面。

1. **直达链接**：[从 VS Code Marketplace 安装](https://marketplace.visualstudio.com/items?itemName=zilliz.semanticcodesearch)
2. **手动搜索**：
    - 在 VSCode 中打开扩展视图（Ctrl+Shift+X 或 Mac 上的 Cmd+Shift+X）
    - 搜索 "Semantic Code Search"
    - 点击 Install

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdtCtT9Qi6o5mGVoxzX50r8Nb6zDFcjvTQR7WZ-xMbEsHEPPhSYAFVJ7q4-rETzxJ8wy1cyZmU8CmtpNhAU8PGOqVnE2kc2HCn1etDg97Qsh7m89kBjG4ZT7XBgO4Dp7BfFZx7eow?key=qYdFquJrLcfXCUndY-YRBQ)
---

## 🛠️ 开发指南

### 搭建开发环境

#### 前置条件

- Node.js 20.x, 22.x, or 24.x
- pnpm（推荐包管理器）

#### 跨平台设置

```bash
# Clone repository
git clone https://github.com/zilliztech/claude-context.git
cd claude-context

# Install dependencies
pnpm install

# Build all packages
pnpm build

# Start development mode
pnpm dev
```

#### Windows 特定设置

在 Windows 上，请确保你已安装：

- **Git for Windows**（含正确的换行符配置）
- **Node.js**（通过官方安装程序或包管理器安装）
- **pnpm**（全局安装）: `npm install -g pnpm`

```powershell
# Windows PowerShell/Command Prompt
git clone https://github.com/zilliztech/claude-context.git
cd claude-context

# Configure git line endings (recommended)
git config core.autocrlf false

# Install dependencies
pnpm install

# Build all packages (uses cross-platform scripts)
pnpm build

# Start development mode
pnpm dev
```

### 构建

```bash
# Build all packages (cross-platform)
pnpm build

# Build specific package
pnpm build:core
pnpm build:vscode
pnpm build:mcp

# Performance benchmarking
pnpm benchmark
```

#### Windows 构建说明

- 所有构建脚本均使用 rimraf 实现跨平台兼容
- 启用了构建缓存以加速后续构建
- 可使用 PowerShell 或命令提示符，两者效果相同

### 运行示例

```bash
# Development with file watching
cd examples/basic-usage
pnpm dev
```

---

## 📖 示例

查看 `/examples` 目录获取完整使用示例：

- **基础用法**：简单的索引与搜索示例

---

## ❓ 常见问题解答 (FAQ)

**常见问题：**

- **[Claude Context 决定嵌入哪些文件？](docs/troubleshooting/faq.md#q-what-files-does-claude-context-decide-to-embed)**
- **[我可以使用完全本地化的部署方案吗？](docs/troubleshooting/faq.md#q-can-i-use-a-fully-local-deployment-setup)**
- **[它是否支持多项目/多代码库？](docs/troubleshooting/faq.md#q-does-it-support-multiple-projects--codebases)**
- **[Claude Context 与其他编程工具相比如何？](docs/troubleshooting/faq.md#q-how-does-claude-context-compare-to-other-coding-tools-like-serena-context7-or-deepwiki)**

❓ 如需详细解答及更多排查技巧，请参阅我们的 [FAQ 指南](docs/troubleshooting/faq.md)。

🔧 **遇到问题？** 访问我们的[故障排除指南](docs/troubleshooting/troubleshooting-guide.md)获取逐步解决方案。

📚 **需要更多帮助？** 查看我们的[完整文档](docs/)以获取详细指南和排查技巧。

---

## 🤝 贡献指南

我们欢迎你的贡献！请参阅我们的 [Contributing Guide](CONTRIBUTING.md) 了解如何开始。

**各包特定的贡献指南：**

- [Core Package Contributing](packages/core/CONTRIBUTING.md)
- [MCP Server Contributing](packages/mcp/CONTRIBUTING.md)  
- [VSCode Extension Contributing](packages/vscode-extension/CONTRIBUTING.md)

---

## 🗺️ 路线图

- [x] 基于 AST（抽象语法树）的代码分析以增强理解能力
- [x] 支持更多嵌入提供商
- [ ] 基于 Agent 的交互式搜索模式
- [x] 增强的代码分块策略
- [ ] 搜索结果排序优化
- [ ] 完善的 Chrome 扩展

---

## 📄 许可证

本项目采用 MIT License 开源协议 - 详情请参阅 [LICENSE](LICENSE) 文件。

---

## 🔗 相关链接

- [GitHub Repository](https://github.com/zilliztech/claude-context)
- [VSCode Marketplace](https://marketplace.visualstudio.com/items?itemName=zilliz.semanticcodesearch)
- [Milvus Documentation](https://milvus.io/docs)
- [Zilliz Cloud](https://zilliz.com/cloud)