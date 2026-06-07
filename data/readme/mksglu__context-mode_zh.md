# Context Mode

**上下文问题的另一半。**

[![users](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fmksglu%2Fcontext-mode%40main%2Fstats.json&query=%24.message&label=users&color=brightgreen)](https://www.npmjs.com/package/context-mode) [![npm](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fmksglu%2Fcontext-mode%40main%2Fstats.json&query=%24.npm&label=npm&color=blue)](https://www.npmjs.com/package/context-mode) [![marketplace](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fmksglu%2Fcontext-mode%40main%2Fstats.json&query=%24.marketplace&label=marketplace&color=blue)](https://github.com/mksglu/context-mode) [![GitHub stars](https://img.shields.io/github/stars/mksglu/context-mode?style=flat&color=yellow)](https://github.com/mksglu/context-mode/stargazers) [![GitHub forks](https://img.shields.io/github/forks/mksglu/context-mode?style=flat&color=blue)](https://github.com/mksglu/context-mode/network/members) [![Last commit](https://img.shields.io/github/last-commit/mksglu/context-mode?color=green)](https://github.com/mksglu/context-mode/commits) [![License: ELv2](https://img.shields.io/badge/License-ELv2-blue.svg)](LICENSE)
[![Discord](https://img.shields.io/discord/1478479412700909750?label=Discord&logo=discord&color=5865f2)](https://discord.gg/DCN9jUgN5v)
[![Hacker News #1](https://img.shields.io/badge/Hacker%20News-%231%20%E2%80%A2%20570%2B%20points-ff6600?logo=ycombinator&logoColor=white)](https://news.ycombinator.com/item?id=47193064)

<p align="center">
<sub>被以下团队广泛使用</sub>
<br><br>
<a href="#"><img src="https://img.shields.io/badge/Microsoft-141414?style=flat" alt="Microsoft" /></a>
<a href="#"><img src="https://img.shields.io/badge/Google-141414?style=flat&logo=google&logoColor=white" alt="Google" /></a>
<a href="#"><img src="https://img.shields.io/badge/Meta-141414?style=flat&logo=meta&logoColor=white" alt="Meta" /></a>
<a href="#"><img src="https://img.shields.io/badge/Amazon-141414?style=flat" alt="Amazon" /></a>
<a href="#"><img src="https://img.shields.io/badge/IBM-141414?style=flat" alt="IBM" /></a>
<a href="#"><img src="https://img.shields.io/badge/NVIDIA-141414?style=flat&logo=nvidia&logoColor=white" alt="NVIDIA" /></a>
<a href="#"><img src="https://img.shields.io/badge/ByteDance-141414?style=flat&logo=bytedance&logoColor=white" alt="ByteDance" /></a>
<a href="#"><img src="https://img.shields.io/badge/Stripe-141414?style=flat&logo=stripe&logoColor=white" alt="Stripe" /></a>
<a href="#"><img src="https://img.shields.io/badge/Datadog-141414?style=flat&logo=datadog&logoColor=white" alt="Datadog" /></a>
<a href="#"><img src="https://img.shields.io/badge/Salesforce-141414?style=flat" alt="Salesforce" /></a>
<a href="#"><img src="https://img.shields.io/badge/GitHub-141414?style=flat&logo=github&logoColor=white" alt="GitHub" /></a>
<a href="#"><img src="https://img.shields.io/badge/Red%20Hat-141414?style=flat&logo=redhat&logoColor=white" alt="Red Hat" /></a>
<a href="#"><img src="https://img.shields.io/badge/Supabase-141414?style=flat&logo=supabase&logoColor=white" alt="Supabase" /></a>
<a href="#"><img src="https://img.shields.io/badge/Canva-141414?style=flat" alt="Canva" /></a>
<a href="#"><img src="https://img.shields.io/badge/Notion-141414?style=flat&logo=notion&logoColor=white" alt="Notion" /></a>
<a href="#"><img src="https://img.shields.io/badge/Hasura-141414?style=flat&logo=hasura&logoColor=white" alt="Hasura" /></a>
<a href="#"><img src="https://img.shields.io/badge/Framer-141414?style=flat&logo=framer&logoColor=white" alt="Framer" /></a>
<a href="#"><img src="https://img.shields.io/badge/Cursor-141414?style=flat&logo=cursor&logoColor=white" alt="Cursor" /></a>
</p>

## 问题所在（The Problem）

每次 MCP 工具调用都会将原始数据直接倾倒进你的上下文窗口。一个 Playwright 快照占用 56 KB，20 个 GitHub Issue 占用 59 KB，一条访问日志就占 45 KB。运行 30 分钟后，你上下文中已有 40% 的内容被挤掉。而当 Agent 为了腾出空间而压缩（compact）对话时，它会忘记正在编辑哪些文件、进行中的任务是什么、以及你上次要求了什么。此外，Agent 还会在填充词、客套话和冗长解释上浪费输出 token——从上下文的两端同时消耗容量。

### Context Mode 如何解决这个问题

Context Mode 是一个 MCP Server，它解决了该问题的四个维度：

1. **上下文节省（Context Saving）** — 沙箱工具将原始数据隔离在上下文窗口之外。315 KB 缩减至 5.4 KB，减少 98%。
2. **会话连续性（Session Continuity）** — 每次文件编辑、Git 操作、任务、错误和用户决策都会被记录到 SQLite 中。当对话被压缩时，context-mode 不会将这些数据重新塞回上下文——而是将事件索引到 FTS5 中，并通过 BM25 搜索仅检索相关内容。模型会精准接续你中断的位置。如果你没有执行 `--continue`，上一会话的数据会被立即删除——新会话意味着全新的起点。
3. **用代码思考（Think in Code）** — LLM 应该编写分析逻辑，而不是亲自计算数据。与其读取 50 个文件到上下文中去统计函数数量，Agent 应编写一个脚本来完成计数，并仅通过 `console.log()` 输出结果。一个脚本替代了十次工具调用，节省 100 倍上下文容量。这是所有 16 个平台强制遵循的范式：停止将 LLM 视为数据处理引擎，将其视为代码生成器。

   ```js
   // Before: 47 × Read() = 700 KB.  After: 1 × ctx_execute() = 3.6 KB.
   ctx_execute("javascript", `
     const files = fs.readdirSync('src').filter(f => f.endsWith('.ts'));
     files.forEach(f => console.log(f + ': ' + fs.readFileSync('src/'+f,'utf8').split('\\n').length + ' lines'));
   `);
   ```
4. **不强制散文式输出（No prose-style enforcement）** — context-mode 将原始数据隔离在上下文之外，但从不规定模型如何撰写最终答案。简洁性、完整性、格式——由你的模型决定（或通过你自己的 `CLAUDE.md` / `AGENTS.md` 决定）。已有研究表明，过度强调极简提示词会降低编码/推理基准测试的表现（[Moonshot AI on `kimi-k2.5`](https://github.com/anomalyco/opencode/issues/20258)）——路由模块专注于*数据流向何处*，而非*模型如何说话*。

<a href="https://www.youtube.com/watch?v=QUHrntlfPo4">
  <picture>
    <img src="https://img.youtube.com/vi/QUHrntlfPo4/maxresdefault.jpg" alt="Watch context-mode demo on YouTube" width="100%">
  </picture>
</a>
<p align="center"><a href="https://www.youtube.com/watch?v=QUHrntlfPo4"><img src="https://img.shields.io/badge/%E2%96%B6%EF%B8%8F_Watch_Demo-YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"></a></p>

## 安装（Install）

平台按安装复杂度分组。支持 Hook 的平台会自动执行路由强制；不支持 Hook 的平台只需一次性复制路由文件。

<details open>
<summary><strong>Claude Code</strong> — 插件市场，全自动</summary>

**前置条件：** Claude Code v1.0.33+（`claude --version`）。如果未识别到 `/plugin`，请先更新：`brew upgrade claude-code` 或 `npm update -g @anthropic-ai/claude-code`。

**安装：**

```bash
/plugin marketplace add mksglu/context-mode
/plugin install context-mode@context-mode
```

重启 Claude Code（或运行 `/reload-plugins`）。

**验证：**

```
/context-mode:ctx-doctor
```

所有检查应显示 `[x]`。Doctor 会验证运行时、Hooks、FTS5 和插件注册状态。

**路由：** 自动执行。SessionStart Hook 会在运行时注入路由指令——不会向你的项目写入任何文件。该插件注册了所有 Hooks（PreToolUse, PostToolUse, PreCompact, SessionStart）以及 11 个 MCP 工具：六个沙箱工具（`ctx_batch_execute`, `ctx_execute`, `ctx_execute_file`, `ctx_index`, `ctx_search`, `ctx_fetch_and_index`）和五个元工具（`ctx_stats`, `ctx_doctor`, `ctx_upgrade`, `ctx_purge`, `ctx_insight`）。

| 斜杠命令 | 功能 |
|---|---|
| `/context-mode:ctx-stats` | 上下文节省情况——按工具分类、消耗 token、节省比例。 |
| `/context-mode:ctx-doctor` | 诊断信息——运行时、Hooks、FTS5、插件注册、版本。 |
| `/context-mode:ctx-index` | 将本地文件或目录索引到持久化 FTS5 知识库中。 |
| `/context-mode:ctx-search` | 搜索已索引的内容。 |
| `/context-mode:ctx-upgrade` | 拉取最新版本、重建缓存、迁移数据、修复 Hooks。 |
| `/context-mode:ctx-purge` | 永久删除知识库中的所有索引内容。 |
| `/context-mode:ctx-insight` | 个人分析仪表盘——90 项指标、37 种洞察模式、4 个综合评分（生产力、质量、委托率、上下文健康度）覆盖 23 类事件分类。会打开本地 Web UI。 |

> **注意：** 斜杠命令是 Claude Code 插件功能。在其他平台上，在聊天中键入 `ctx stats`、`ctx doctor`、`ctx index`、`ctx search`、`ctx upgrade` 或 `ctx insight`——模型会自动调用对应的 MCP 工具。详见 [实用命令（Utility Commands）](#utility-commands)。

**状态栏（可选）：** Claude Code 的插件清单无法声明状态栏，因此需手动编辑一次 `~/.claude/settings.json`：

```json
{
  "statusLine": {
    "type": "command",
    "command": "context-mode statusline"
  }
}
```

保存后重启 Claude Code。状态栏会显示 `$ saved this session · $ saved across sessions · % efficient`，让你实时查看节省效果累积。该配置无路径依赖——无论插件缓存位于何处，`context-mode statusline` 都会通过内置 CLI 正确解析。

<details>
<summary>替代方案 — 仅 MCP 安装（无 Hooks 或斜杠命令）</summary>

```bash
claude mcp add context-mode -- npx -y context-mode
```

这将提供全部 11 个 MCP 工具，但不会自动执行路由。模型仍可使用这些工具——只是不会被引导优先使用它们而非原始 Bash/Read/WebFetch。适合在正式采用完整插件前进行试用。

</details>

</details>

<details>
<summary><strong>Gemini CLI</strong> — 一个配置文件，包含 Hooks</summary>

**前置条件：** Node.js >= 22.5（或 Bun），已安装 Gemini CLI。

**安装：**

1. 全局安装 context-mode：

   ```bash
   npm install -g context-mode
   ```

2. 将以下内容添加到 `~/.gemini/settings.json`。该单文件会注册 MCP Server 和所有四个 Hooks：

   ```json
   {
     "mcpServers": {
       "context-mode": {
         "command": "context-mode"
       }
     },
     "hooks": {
       "BeforeTool": [
         {
           "matcher": "run_shell_command|read_file|read_many_files|grep_search|search_file_content|web_fetch|activate_skill|mcp__plugin_context-mode|mcp__context-mode|mcp__(?!.*context-mode)",
           "hooks": [{ "type": "command", "command": "context-mode hook gemini-cli beforetool" }]
         }
       ],
       "AfterTool": [
         {
           "matcher": "",
           "hooks": [{ "type": "command", "command": "context-mode hook gemini-cli aftertool" }]
         }
       ],
       "PreCompress": [
         {
           "matcher": "",
           "hooks": [{ "type": "command", "command": "context-mode hook gemini-cli precompress" }]
         }
       ],
       "SessionStart": [
         {
           "matcher": "",
           "hooks": [{ "type": "command", "command": "context-mode hook gemini-cli sessionstart" }]
         }
       ]
     }
   }
   ```

3. 重启 Gemini CLI。

**验证：**

```
/mcp list
```

你应该能看到 `context-mode: ... - Connected`。

**路由：** 通过 SessionStart Hook 自动执行。可选：复制路由指令以获得完整的模型感知能力：

```bash
cp node_modules/context-mode/configs/gemini-cli/GEMINI.md ./GEMINI.md
```

> **为什么使用 BeforeTool matcher？** 它仅针对会产生大量输出的工具（`run_shell_command`, `read_file`, `read_many_files`, `grep_search`, `search_file_content`, `web_fetch`, `activate_skill`）以及 context-mode 自身的工具（`mcp__plugin_context-mode`）。这避免了在轻量级工具上产生不必要的 Hook 开销，同时拦截所有可能淹没你上下文窗口的工具。

完整配置参考：[`configs/gemini-cli/settings.json`](configs/gemini-cli/settings.json)

</details>

<details>
<summary><strong>VS Code Copilot</strong> — 包含 SessionStart 的 Hooks</summary>

**前置条件：** Node.js >= 22.5（或 Bun），安装 Copilot Chat v0.32+ 的 VS Code。

**安装：**

1. 全局安装 context-mode：

   ```bash
   npm install -g context-mode
   ```

2. 在项目根目录创建 `.vscode/mcp.json`：

   ```json
   {
     "servers": {
       "context-mode": {
         "command": "context-mode"
       }
     }
   }
   ```

3. 创建 `.github/hooks/context-mode.json`：

   ```json
   {
     "hooks": {
       "PreToolUse": [
         { "type": "command", "command": "context-mode hook vscode-copilot pretooluse" }
       ],
       "PostToolUse": [
         { "type": "command", "command": "context-mode hook vscode-copilot posttooluse" }
       ],
       "SessionStart": [
         { "type": "command", "command": "context-mode hook vscode-copilot sessionstart" }
       ]
     }
   }
   ```

4. 重启 VS Code。

**验证：** 打开 Copilot Chat 并键入 `ctx stats`。应能看到 context-mode 工具出现并响应。

**路由：** 通过 SessionStart Hook 自动执行。可选：复制路由指令以获得完整的模型感知能力：

```bash
cp node_modules/context-mode/configs/vscode-copilot/copilot-instructions.md .github/copilot-instructions.md
```

包含 PreCompact 的完整 Hook 配置：[`configs/vscode-copilot/hooks.json`](configs/vscode-copilot/hooks.json)

</details>

<details>
<summary><strong>JetBrains Copilot</strong> — 包含 SessionStart 的 Hooks</summary>

**前置条件：** Node.js >= 22.5（或 Bun），安装 GitHub Copilot 插件 v1.5.57+ 的 JetBrains IDE。

**安装：**

1. 全局安装 context-mode：

   ```bash
   npm install -g context-mode
   ```

2. 通过设置 UI 添加 MCP Server：**Settings > Tools > AI Assistant > Model Context Protocol (MCP) > Add Server**：
   - **Name:** `context-mode`
   - **Command:** `context-mode`

3. 创建 `.github/hooks/context-mode.json`：

   ```json
   {
     "hooks": {
       "PreToolUse": [
         { "type": "command", "command": "context-mode hook jetbrains-copilot pretooluse" }
       ],
       "PostToolUse": [
         { "type": "command", "command": "context-mode hook jetbrains-copilot posttooluse" }
       ],
       "SessionStart": [
         { "type": "command", "command": "context-mode hook jetbrains-copilot sessionstart" }
       ]
     }
   }
   ```

4. 重启 JetBrains IDE。

**验证：** 打开 Copilot Chat 并键入 `ctx stats`。应能看到 context-mode 工具出现并响应。

**路由：** 通过 SessionStart Hook 自动执行。可选：复制路由指令以获得完整的模型感知能力：

```bash
cp node_modules/context-mode/configs/jetbrains-copilot/copilot-instructions.md .github/copilot-instructions.md
```

包含 PreCompact 的完整 Hook 配置：[`configs/jetbrains-copilot/hooks.json`](configs/jetbrains-copilot/hooks.json)

完整设置指南：[`docs/jetbrains-copilot.md`](docs/jetbrains-copilot.md)

</details>

<details>
<summary><strong>Cursor</strong> — 包含 stop 支持的 Hooks</summary>

**前置条件：** Node.js >= 22.5（或 Bun），支持 Agent Mode 的 Cursor。

> **🚧 开发中** — Marketplace 插件正在**等待 Cursor 团队审核**。在正式上架前，请通过选项 A 描述的本地文件夹路径进行安装。追踪 issue：[#485](https://github.com/mksglu/context-mode/issues/485) / [#489](https://github.com/mksglu/context-mode/pull/489)。

### 方案 A — Marketplace 插件（上架后推荐）

Cursor 在 [Marketplace](https://cursor.com/marketplace) 上架 context-mode 后，一键即可安装。该插件会自动注册 MCP、Hooks（`preToolUse`, `postToolUse`, `sessionStart`, `stop`, `afterAgentResponse`）、规则和 Skills。无需手动配置。

**在此之前，请使用本地文件夹路径：**

**Windows (PowerShell)** — Cursor 不遵循 Windows 符号链接/快捷方式，因此使用 `robocopy`：

```powershell
git clone https://github.com/mksglu/context-mode.git
cd context-mode
robocopy . "$env:USERPROFILE\.cursor\plugins\local\context-mode" /MIR `
  /XD node_modules .git build insight web tests scripts .vscode `
  /XF *.log .gitignore *.bundle.mjs.map
```

**macOS / Linux：**

```bash
git clone https://github.com/mksglu/context-mode.git
ln -s "$PWD/context-mode" ~/.cursor/plugins/local/context-mode
```

重启 Cursor。该插件会出现在 **Settings → Plugins** 中，显示为 "Context Mode (Local)"。要拉取更新，重新运行相同的 `robocopy` / `ln -s` 命令即可。

> **注意：** 如果 `.cursor/hooks.json` 已包含来自之前 `Option B` 安装的 context-mode 条目，`context-mode doctor` 会警告重复触发 Hook。请删除其中一个配置以保持事件单次触发。

### 方案 B — 手动安装（现有路径）

1. 全局安装 context-mode：

   ```bash
   npm install -g context-mode
   ```

2. 在项目根目录创建 `.cursor/mcp.json`（或 `~/.cursor/mcp.json` 用于全局配置）：

   ```json
   {
     "mcpServers": {
       "context-mode": {
         "command": "context-mode"
       }
     }
   }
   ```

3. 创建 `.cursor/hooks.json`（或 `~/.cursor/hooks.json` 用于全局配置）：

   ```json
   {
     "version": 1,
     "hooks": {
       "preToolUse": [
         {
           "command": "context-mode hook cursor pretooluse",
           "matcher": "Shell|Read|Grep|WebFetch|Task|MCP:ctx_execute|MCP:ctx_execute_file|MCP:ctx_batch_execute"
         }
       ],
       "postToolUse": [
         {
           "command": "context-mode hook cursor posttooluse"
         }
       ],
       "stop": [
         {
           "command": "context-mode hook cursor stop"
         }
       ]
     }
   }
   ```

   `preToolUse` 的 matcher 是可选的——如果不设置，Hook 将在所有工具上触发。`stop` Hook 在 Agent 回合结束时触发，并可发送跟进消息以继续循环。`afterAgentResponse` 也可用（fire-and-forget，接收完整响应文本）。

4. 复制路由规则文件。Cursor 缺少 SessionStart Hook，因此模型需要规则文件来实现路由感知：

   ```bash
   mkdir -p .cursor/rules
   cp node_modules/context-mode/configs/cursor/context-mode.mdc .cursor/rules/context-mode.mdc
   ```

5. 重启 Cursor 或打开新的 Agent 会话。

**验证：** 打开 Cursor Settings > MCP，确认 "context-mode" 显示为已连接。在 Agent 聊天中键入 `ctx stats`。

**路由：** Hooks 通过 `preToolUse`/`postToolUse`/`stop` 以编程方式强制执行路由。`.cursor/rules/context-mode.mdc` 文件会在会话开始时提供路由指令，因为 Cursor 的 `sessionStart` Hook 目前被其验证器拒绝（[论坛报告](https://forum.cursor.com/t/unknown-hook-type-sessionstart/149566)）。项目级 `.cursor/hooks.json` 会覆盖 `~/.cursor/hooks.json`。

**已知限制：** Cursor 接受 Hook 响应中的 `additional_context`，但未将其暴露给模型（[论坛 #155689](https://forum.cursor.com/t/native-posttooluse-hooks-accept-and-log-additional-context-successfully-but-the-injected-context-is-not-surfaced-to-the-model/155689)）。路由依赖 `.mdc` 规则文件而非 Hook 上下文注入。

完整配置：[`configs/cursor/hooks.json`](configs/cursor/hooks.json) | [`configs/cursor/mcp.json`](configs/cursor/mcp.json) | [`configs/cursor/context-mode.mdc`](configs/cursor/context-mode.mdc)

</details>

<details>
<summary><strong>OpenCode</strong> — 带 Hooks 的 TypeScript 插件</summary>

**前置条件：** Node.js >= 22.5（或 Bun），已安装 OpenCode。

**安装：**

1. 在项目根目录的 `opencode.json` 中添加（或 `~/.config/opencode/opencode.json` 用于全局配置）：

   ```json
   {
     "$schema": "https://opencode.ai/config.json",
     "plugin": ["context-mode"]
   }
   ```

   `plugin` 条目会原生注册全部 11 个 `ctx_*` 工具并启用 Hooks——OpenCode 会在进程内调用 context-mode 的 TypeScript 插件，因此每个会话不会生成多余的 stdio MCP 子进程。

2. *（可选）* 复制路由规则文件。模型需要 `AGENTS.md` 文件来实现路由感知：

   ```bash
   cp node_modules/context-mode/configs/opencode/AGENTS.md AGENTS.md
   ```

   这会告知模型应使用哪些工具以及哪些命令被禁用。如果没有该文件，Hooks 仍会强制执行路由——但模型将不知道*为何*某个命令被拒绝。

3. 重启 OpenCode。

**验证：** 在 OpenCode 会话中键入 `ctx stats`。应能看到 context-mode 工具出现并响应。

**升级注意：** 如果现有配置同时包含 `plugin: ["context-mode"]` 和 `mcp.context-mode`，OpenCode 将注册零个 `ctx_*` 工具——插件路径会正确抑制 MCP 重复项，但遗留的 MCP 条目会导致加载器混淆。运行 `context-mode upgrade` 可移除遗留的 `mcp.context-mode` 条目；其他 MCP Server 配置将被保留。v1.0.140+ 在此情况下会在 stderr 输出诊断信息并提供相同指引。

**路由：** Hooks 通过 `tool.execute.before` 和 `tool.execute.after` 以编程方式强制执行路由。可选的 [`AGENTS.md`](configs/opencode/AGENTS.md) 文件为模型提供路由指令。`experimental.session.compacting` Hook 会在对话压缩时构建恢复快照。`experimental.chat.system.transform` Hook 在会话开始时注入路由块和前一会话快照，实现跨重启的会话连续性。`chat.message` Hook 捕获用户提示与决策（等价于 UserPromptSubmit）。

> **注意：** OpenCode 缺乏真正的 SessionStart Hook（[#14808](https://github.com/sst/opencode/issues/14808), [#5409](https://github.com/sst/opencode/issues/5409)）。该插件使用 `experimental.chat.system.transform` 作为替代方案——它会将路由块和恢复快照注入系统提示。用户提示捕获使用 `chat.message` 而非缺失的 UserPromptSubmit Hook。AGENTS.md/CLAUDE.md/CONTEXT.md 规则会在每个项目首次触发 Hook 时自动捕获。

完整配置：[`configs/opencode/opencode.json`](configs/opencode/opencode.json) | [`configs/opencode/AGENTS.md`](configs/opencode/AGENTS.md)

</details>

<details>
<summary><strong>KiloCode</strong> — 带 Hooks 的 TypeScript 插件</summary>

**前置条件：** Node.js >= 22.5（或 Bun），已安装 KiloCode。

**安装：**

1. 在项目根目录的 `kilo.json` 中添加（或 `~/.config/kilo/kilo.json` 用于全局配置）：

   ```json
   {
     "$schema": "https://app.kilo.ai/config.json",
     "plugin": ["context-mode"]
   }
   ```

   `plugin` 条目会原生注册全部 11 个 `ctx_*` 工具并启用 Hooks——KiloCode 会在进程内调用 context-mode 的 TypeScript 插件，因此每个会话不会生成多余的 stdio MCP 子进程。

2. *（可选）* 复制路由规则文件。KiloCode 共享 OpenCode 的插件架构，因此模型需要 `AGENTS.md` 文件来实现路由感知：

   ```bash
   cp node_modules/context-mode/configs/opencode/AGENTS.md AGENTS.md
   ```

3. 重启 KiloCode。

**验证：** 在 KiloCode 会话中键入 `ctx stats`。应能看到 context-mode 工具出现并响应。

**升级注意：** 如果现有配置同时包含 `plugin: ["context-mode"]` 和 `mcp.context-mode`，KiloCode 将注册零个 `ctx_*` 工具——插件路径会正确抑制 MCP 重复项，但遗留的 MCP 条目会导致加载器混淆。运行 `context-mode upgrade` 可移除遗留的 `mcp.context-mode` 条目；其他 MCP Server 配置将被保留。v1.0.140+ 在此情况下会在 stderr 输出诊断信息并提供相同指引。

**路由：** Hooks 通过 `tool.execute.before` 和 `tool.execute.after` 以编程方式强制执行路由。可选的 [`AGENTS.md`](configs/opencode/AGENTS.md) 文件为模型提供路由指令。`experimental.session.compacting` Hook 会在对话压缩时构建恢复快照。`experimental.chat.system.transform` Hook 在会话开始时注入路由块和前一会话快照，实现跨重启的会话连续性。`chat.message` Hook 捕获用户提示与决策（等价于 UserPromptSubmit）。

> **注意：** KiloCode 共享 OpenCode 的插件架构，使用 OpenCodeAdapter 配合平台特定配置路径（`kilo.json` 替代 `opencode.json`，`~/.config/kilo/` 替代 `~/.config/opencode/`）。与 OpenCode 一样，它缺乏真正的 SessionStart Hook——该插件使用 `experimental.chat.system.transform` 作为替代方案。用户提示捕获使用 `chat.message` 而非缺失的 UserPromptSubmit Hook。AGENTS.md/CLAUDE.md/CONTEXT.md 规则会在每个项目首次触发 Hook 时自动捕获。

</details>

<details>
<summary><strong>OpenClaw / Pi Agent</strong> — 原生网关插件</summary>

**前置条件：** 运行中的 OpenClaw gateway（[>2026.1.29](https://github.com/openclaw/openclaw/pull/9761)），Node.js 22+。

context-mode 作为原生 [OpenClaw](https://github.com/openclaw) 网关插件运行，针对 **Pi Agent** 会话（Read/Write/Edit/Bash 工具）。与其他平台不同，这里没有独立的 MCP Server——插件通过 OpenClaw 的 [plugin API](https://docs.openclaw.ai/tools/plugin) 直接注册到网关运行时。

**安装：**

1. 克隆并安装：

   ```bash
   git clone https://github.com/mksglu/context-mode.git
   cd context-mode
   npm run install:openclaw
   ```

   安装器使用环境变量 `$OPENCLAW_STATE_DIR`（默认：`/openclaw`）。要指定自定义路径：

   ```bash
   npm run install:openclaw -- /path/to/openclaw-state
   ```

   常见位置：**Docker** — `/openclaw`（默认值）。**本地** — `~/.openclaw` 或你设置 `OPENCLAW_STATE_DIR` 的位置。

   安装器处理所有步骤：`npm install`、`npm run build`、`better-sqlite3` 原生重建、在 `runtime.json` 中注册扩展，以及通过 SIGUSR1 重启网关。

2. 打开 Pi Agent 会话。

**验证：** 该插件通过 [`api.on()`](https://docs.openclaw.ai/tools/plugin)（生命周期）和 [`api.registerHook()`](https://docs.openclaw.ai/tools/plugin)（命令）注册了 8 个 Hooks。键入 `ctx stats` 确认工具已加载。

**路由：** 自动执行。所有工具拦截、会话追踪和压缩恢复 Hook 均会自动激活——无需手动配置 Hook 或路由文件。

> **最低版本要求：** OpenClaw >2026.1.29——这包含了 [PR #9761](https://github.com/openclaw/openclaw/pull/9761) 中的 `api.on()` 生命周期修复。在旧版本上，生命周期 Hook 会静默失败。适配器将回退到 DB 快照重建（精度较低但能保留关键状态）。

完整文档：[`docs/adapters/openclaw.md`](docs/adapters/openclaw.md)

</details>

<details>
<summary><strong>Codex CLI</strong> — MCP + Hooks</summary>

**前置条件：** Node.js >= 22.5（或 Bun），已安装 Codex CLI。

**安装：**

1. 添加 context-mode 市场并从 Codex 的插件 UI 安装该插件：

   ```bash
   codex plugin marketplace add mksglu/context-mode
   ```

2. 在 Codex 功能仍处于 gated 阶段时启用插件提供的 Hooks：

   ```toml
   [features]
   plugin_hooks = true
   hooks = true
   ```

   > **特性标志说明：** 当前 Codex 构建版将 Hooks 暴露于 `[features].hooks`（或 `codex --enable hooks`）。优先使用 `[features].hooks`；`[features].codex_hooks` 在当前构建版中仍作为遗留别名被接受。捆绑插件的 Hooks 还需要 `plugin_hooks`，直到 Codex 默认启用插件 Hooks。

   **自定义存储位置：** 如果 Codex 无法写入适配器默认的存储目录，请在启动 Codex 的环境中将 `CONTEXT_MODE_DIR` 设置为绝对可写根路径。会话和统计信息使用 `<root>/sessions`；索引内容使用 `<root>/content`。

   ```bash
   CONTEXT_MODE_DIR="$HOME/.codex-context-mode" codex
   ```

3. 重启 Codex CLI 并通过 `ctx stats` 验证 MCP。

   `ctx stats` 证明插件的 MCP Server 已安装并可访问；但它不能证明 Hooks 已被信任或正在运行。

4. 如果 Codex 提示批准 Hook，请审查并信任 context-mode 插件的 Hooks。只有在两个特性标志均已启用且 Codex 接受了 Hook 命令后，插件 Hooks 才会激活。

Codex 插件清单通过 `.codex-plugin/mcp.json` 提供 MCP，通过 `skills/` 提供 Skills，并通过 `.codex-plugin/hooks.json` 提供捆绑 Hooks。当启用 `plugin_hooks` 并信任插件 Hooks 时，无需手动配置 `[mcp_servers.context-mode]` 块或 `$CODEX_HOME/hooks.json`。

> **Node/PATH 说明：** context-mode 仍需要 Codex 进程能访问到 `node`。该插件移除了手动 Codex 配置，但它不会自动打包 Node 或继承 login-shell PATH 修复。

**Codex 构建版不支持 `plugin_hooks` 时的手动回退方案：**

1. 全局安装 context-mode：

   ```bash
   npm install -g context-mode
   ```

2. 添加到 `~/.codex/config.toml`：

   ```toml
   [features]
   hooks = true

   [mcp_servers.context-mode]
   command = "context-mode"

   [mcp_servers.context-mode.env]
   CONTEXT_MODE_PLATFORM = "codex"
   ```

3. 创建 `$CODEX_HOME/hooks.json`（当 `CODEX_HOME` 未设置时为 `~/.codex/hooks.json`）：

   ```json
   {
     "hooks": {
      "PreToolUse": [{ "matcher": "local_shell|shell|shell_command|exec_command|Bash|Shell|apply_patch|Edit|Write|grep_files|ctx_execute|ctx_execute_file|ctx_batch_execute|ctx_fetch_and_index|ctx_search|ctx_index|mcp__", "hooks": [{ "type": "command", "command": "context-mode hook codex pretooluse" }] }],
       "PostToolUse": [{ "hooks": [{ "type": "command", "command": "context-mode hook codex posttooluse" }] }],
       "SessionStart": [{ "hooks": [{ "type": "command", "command": "context-mode hook codex sessionstart" }] }],
       "PreCompact": [{ "hooks": [{ "type": "command", "command": "context-mode hook codex precompact" }] }],
       "UserPromptSubmit": [{ "hooks": [{ "type": "command", "command": "context-mode hook codex userpromptsubmit" }] }],
       "Stop": [{ "hooks": [{ "type": "command", "command": "context-mode hook codex stop" }] }]
     }
   }
   ```

   `PreToolUse` 目前强制执行拒绝/阻止路由，并已准备好在 Codex 支持输入重写时进行输入改写。`PostToolUse` 捕获会话事件。`PreCompact` 在压缩前构建恢复快照。`SessionStart` 在压缩后恢复状态。`UserPromptSubmit` 捕获用户决策和修正。`Stop` 记录回合结束状态。

   > **注意：** Codex PreToolUse 路由目前仅支持拒绝规则（阻止危险命令）。它仍需上游 `updatedInput` 支持，之后 context-mode 才能重写工具输入；请追踪 [openai/codex#18491](https://github.com/openai/codex/issues/18491)。上下文注入（additionalContext）在 Codex PreToolUse 中不受支持——它通过 PostToolUse 和 SessionStart 工作。此部分已自动处理。
   >
   > `PreCompact` 支持受运行时限制：它在 Codex CLI 0.130.0 中存在，而公共 Hooks 文档可能落后于实际发布的 Hook 事件列表。不发出 `PreCompact` 的旧版 Codex 构建将不会创建压缩前快照。

4. 复制路由指令（即使有 Hooks 也推荐，以获得完整的路由感知）：

   ```bash
   CM_ROOT="$(npm root -g)/context-mode"
   cp "$CM_ROOT/configs/codex/AGENTS.md" ./AGENTS.md
   ```

   全局使用：`CM_ROOT="$(npm root -g)/context-mode"; cp "$CM_ROOT/configs/codex/AGENTS.md" ~/.codex/AGENTS.md`。全局配置适用于所有项目。如果两者都存在，Codex CLI 会合并它们。

5. 重启 Codex CLI。

**验证：** 启动会话并键入 `ctx stats` 以验证 MCP。要验证 Hook 路由，确认 Codex 列出/信任了 context-mode 插件 Hooks，然后运行一个匹配路由规则的命令。

**路由：** 安装插件后 MCP 工具即可工作。仅当启用 `hooks` 和 `plugin_hooks` 且 Codex 信任插件 Hook 命令时，插件 Hook 路由才激活。配置 `$CODEX_HOME/hooks.json` 或 `~/.codex/hooks.json` 时，手动 Hook 路由生效。`AGENTS.md` 文件为模型提供路由指令。

</details>

<details>
<summary><strong>Kimi Code</strong> — MCP + Hooks（TOML 配置，与 Codex 相同的 JSON 传输协议）</summary>

**前置条件：** Node.js >= 22.5（或 Bun），已安装 Kimi Code CLI。

1. 安装 context-mode：

   ```bash
   npm install -g context-mode
   ```

2. 将 context-mode 添加为 MCP Server。添加到 `~/.kimi-code/mcp.json`：

   ```json
   {
     "mcpServers": {
       "context-mode": {
         "command": "context-mode",
         "args": []
       }
     }
   }
   ```

3. 将 Hooks 添加到 `~/.kimi-code/config.toml`：

   ```toml
   [[hooks]]
   event = "PreToolUse"
   matcher = "Bash|Shell|Read|Edit|Write|WebFetch|Agent|ctx_execute|ctx_execute_file|ctx_batch_execute|ctx_fetch_and_index|ctx_search|ctx_index|mcp__"
   command = "context-mode hook kimi pretooluse"
   timeout = 30

   [[hooks]]
   event = "PostToolUse"
   command = "context-mode hook kimi posttooluse"
   timeout = 30

   [[hooks]]
   event = "SessionStart"
   command = "context-mode hook kimi sessionstart"
   timeout = 30

   [[hooks]]
   event = "PreCompact"
   command = "context-mode hook kimi precompact"
   timeout = 30

   [[hooks]]
   event = "UserPromptSubmit"
   command = "context-mode hook kimi userpromptsubmit"
   timeout = 30

   [[hooks]]
   event = "Stop"
   command = "context-mode hook kimi stop"
   timeout = 30
   ```

4. 重启 Kimi Code CLI 并通过 `ctx stats` 验证 MCP。

   > **注意：** Kimi Code 使用与 Codex 相同的 JSON stdin/stdout 传输协议，但接受 PreToolUse 响应中的 `additionalContext`、`updatedInput` 和 `permissionDecision: "ask"`（Codex 拒绝这些）。kimi Hook 会将 `ContentPart[]` 提示数组规范化为字符串以供下游提取器使用。

5. （可选）为你的项目复制路由指令文件：

   ```bash
   cp "$(npm root -g)/context-mode/configs/codex/AGENTS.md" ./AGENTS.md
   ```

   或用于全局配置：

   ```bash
   CM_ROOT="$(npm root -g)/context-mode"; cp "$CM_ROOT/configs/codex/AGENTS.md" ~/.kimi-code/AGENTS.md
   ```

</details>

<details>
<summary><strong>Qwen Code</strong> — MCP + Hooks（与 Claude Code 相同的传输协议）</summary>

**前置条件：** Node.js >= 22.5（或 Bun），已安装 Qwen Code（`npm install -g @qwen-code/qwen-code`）。

1. 安装 context-mode：

   ```bash
   npm install -g context-mode
   ```

2. 将 context-mode 添加为 MCP Server。添加到 `~/.qwen/settings.json`：

   ```json
   {
     "mcpServers": {
       "context-mode": {
         "command": "context-mode",
         "args": []
       }
     }
   }
   ```

3. 添加用于路由强制和会话追踪的 Hooks。添加到 `~/.qwen/settings.json`：

   ```json
   {
     "hooks": {
       "PreToolUse": [{ "matcher": "run_shell_command|read_file|read_many_files|grep_search|web_fetch|agent|mcp__plugin_context-mode_context-mode__ctx_execute|mcp__plugin_context-mode_context-mode__ctx_execute_file|mcp__plugin_context-mode_context-mode__ctx_batch_execute|mcp__(?!.*context-mode)", "hooks": [{ "type": "command", "command": "context-mode hook qwen-code pretooluse" }] }],
       "PostToolUse": [{ "matcher": "", "hooks": [{ "type": "command", "command": "context-mode hook qwen-code posttooluse" }] }],
       "SessionStart": [{ "matcher": "", "hooks": [{ "type": "command", "command": "context-mode hook qwen-code sessionstart" }] }],
       "PreCompact": [{ "matcher": "", "hooks": [{ "type": "command", "command": "context-mode hook qwen-code precompact" }] }],
       "UserPromptSubmit": [{ "matcher": "", "hooks": [{ "type": "command", "command": "context-mode hook qwen-code userpromptsubmit" }] }]
     }
   }
   ```

4. 复制路由指令（推荐以获得完整的路由感知）：

   ```bash
   cp node_modules/context-mode/configs/qwen-code/QWEN.md ./QWEN.md
   ```

   全局使用：`cp node_modules/context-mode/configs/qwen-code/QWEN.md ~/.qwen/QWEN.md`

5. 重启 Qwen Code。

**验证：** 启动会话并键入 `ctx stats`。应能看到 context-mode 工具出现并响应。

**注意：** Qwen Code 使用与 Claude Code 相同的 Hook 传输协议（JSON stdin/stdout，相同的事件名称）。通过 MCP clientInfo（`qwen-cli-mcp-client-*`）或 `QWEN_PROJECT_DIR` 环境变量自动检测。

</details>

<details>
<summary><strong>Antigravity</strong> — 仅 MCP，无 Hooks</summary>

**前置条件：** Node.js >= 22.5（或 Bun），已安装 Antigravity。

**安装：**

1. 全局安装 context-mode：

   ```bash
   npm install -g context-mode
   ```

2. 添加到 `~/.gemini/antigravity/mcp_config.json`：

   ```json
   {
     "mcpServers": {
       "context-mode": {
         "command": "context-mode"
       }
     }
   }
   ```

3. 复制路由指令（Antigravity 不支持 Hook）：

   ```bash
   cp node_modules/context-mode/configs/antigravity/GEMINI.md ./GEMINI.md
   ```

4. 重启 Antigravity。

**验证：** 在 Antigravity 会话中键入 `ctx stats`。应能看到 context-mode 工具出现并响应。

**路由：** 手动执行。`GEMINI.md` 文件是唯一的强制手段（约 60% 合规率）。没有程序拦截。通过 MCP 协议握手自动检测（`clientInfo.name`）——无需手动平台配置。

完整配置：[`configs/antigravity/mcp_config.json`](configs/antigravity/mcp_config.json) | [`configs/antigravity/GEMINI.md`](configs/antigravity/GEMINI.md)

</details>

<details>
<summary><strong>Kiro</strong> — 带引导文件的 Hooks</summary>

**前置条件：** Node.js >= 22.5（或 Bun），启用 MCP 的 Kiro（Settings > 搜索 "MCP"）。

**安装：**

1. 全局安装 context-mode：

   ```bash
   npm install -g context-mode
   ```

2. 在项目中的 `.kiro/settings/mcp.json` 中添加（或 `~/.kiro/settings/mcp.json` 用于全局配置）：

   ```json
   {
     "mcpServers": {
       "context-mode": {
         "command": "context-mode"
       }
     }
   }
   ```

3. 创建 `.kiro/hooks/context-mode.json`：

   ```json
   {
     "name": "context-mode",
     "description": "Context-mode hooks for context window protection",
     "hooks": {
       "preToolUse": [
         { "matcher": "execute_bash|fs_read|@context-mode/ctx_execute|@context-mode/ctx_execute_file|@context-mode/ctx_batch_execute|@(?!context-mode/)", "command": "context-mode hook kiro pretooluse" }
       ],
       "postToolUse": [
         { "matcher": "*", "command": "context-mode hook kiro posttooluse" }
       ]
     }
   }
   ```

4. 复制路由指令。Kiro 的 `agentSpawn`（SessionStart）尚未实现，因此模型需要在会话开始时获取路由文件：

   ```bash
   cp node_modules/context-mode/configs/kiro/KIRO.md ./KIRO.md
   ```

5. 重启 Kiro。

**验证：** 打开 Kiro 面板 > MCP Servers 选项卡，确认 "context-mode" 显示绿色状态指示器。在聊天中键入 `ctx stats`。

**路由：** Hooks 通过 `preToolUse`/`postToolUse` 以编程方式强制执行路由。由于 `agentSpawn`（SessionStart 等价物）尚未连接，`KIRO.md` 文件提供路由指令。工具名显示为 `@context-mode/ctx_batch_execute`、`@context-mode/ctx_search` 等。通过 MCP 协议握手自动检测。

完整配置：[`configs/kiro/mcp.json`](configs/kiro/mcp.json) | [`configs/kiro/agent.json`](configs/kiro/agent.json) | [`configs/kiro/KIRO.md`](configs/kiro/KIRO.md)

</details>

<details>
<summary><strong>Zed</strong> — 仅 MCP，无 Hooks</summary>

**前置条件：** Node.js >= 22.5（或 Bun），已安装 Zed。

**安装：**

1. 全局安装 context-mode：

   ```bash
   npm install -g context-mode
   ```

2. 添加到 `~/.config/zed/settings.json`（Windows: `%APPDATA%\Zed\settings.json`）：

   ```json
   {
     "context_servers": {
       "context-mode": {
         "command": {
           "path": "context-mode"
         }
       }
     }
   }
   ```

   注意：Zed 使用 `"context_servers"` 和 `"command": { "path": "..." }` 语法，与其他平台使用的 `"mcpServers"` 或 `"command": "..."` 不同。

3. 复制路由指令（Zed 不支持 Hook）：

   ```bash
   cp node_modules/context-mode/configs/zed/AGENTS.md ./AGENTS.md
   ```

4. 重启 Zed（或保存 `settings.json`——Zed 会在配置更改时自动重启上下文服务器）。

**验证：** 打开 Agent Panel（`Cmd+Shift+A`），进入设置，检查 "context-mode" 旁边的指示点——绿色表示已激活。在 Agent 聊天中键入 `ctx stats`。

**路由：** 手动执行。`AGENTS.md` 文件是唯一的强制手段（约 60% 合规率）。没有程序拦截。工具名显示为 `mcp:context-mode:ctx_batch_execute`、`mcp:context-mode:ctx_search` 等。通过 MCP 协议握手自动检测。

</details>

<details>
<summary><strong>Pi Coding Agent</strong> — 支持完整 Hooks 的扩展</summary>

**前置条件：** Node.js >= 22.5（或 Bun），已安装 Pi Coding Agent。

**安装：**

1. 全局安装 context-mode：

   ```bash
   npm install -g context-mode
   ```

2. 将包安装到 Pi 中：

   ```bash
   pi install npm:context-mode
   ```

   替代方案——手动添加到 `~/.pi/agent/settings.json`（或 `.pi/settings.json` 用于项目级）：

   ```json
   {
     "packages": ["npm:context-mode"]
   }
   ```

3. 添加到 `~/.pi/agent/mcp.json`（或 `.pi/mcp.json` 用于项目级）：

   ```json
   {
     "mcpServers": {
       "context-mode": {
         "command": "context-mode"
       }
     }
   }
   ```

4. 重启 Pi。

**验证：** 在 Pi 会话中键入 `ctx stats`。应能看到 context-mode 工具出现并响应。

**路由：** 自动执行。该扩展注册了所有关键生命周期事件（`tool_call`, `tool_result`, `session_start`, `session_before_compact`），提供完整的会话连续性和路由强制。

</details>

<details>
<summary><strong>OMP (Oh My Pi)</strong> — 支持完整 Hooks 的插件</summary>

**前置条件：** Node.js >= 22.5（或 Bun），已安装 Oh My Pi。

**安装 — 插件路径（推荐）：**

1. 运行 OMP 插件安装：

   ```bash
   omp plugin install context-mode
   ```

2. 重启 OMP。

3. 验证：

   ```bash
   omp plugin list
   omp plugin doctor
   ```

   两者均应显示 `context-mode` 为 `enabled`。

**安装 — 手动插件路径（如果 `omp plugin install` 不可用）：**

OMP 会加载列在 `~/.omp/plugins/package.json` `dependencies` 下的任何内容，只要其自身的 `package.json` 包含 `omp`（或 `pi`）字段。新插件默认启用——锁文件 `~/.omp/plugins/omp-plugins.lock.json` 仅在需要显式**禁用**插件时才会被检查（加载器会跳过 `runtimeState && !runtimeState.enabled`，参见 [`extensibility/plugins/loader.ts:89-94`](https://github.com/can1357/oh-my-pi/blob/main/packages/coding-agent/src/extensibility/plugins/loader.ts)）。因此手动安装只需两条命令：

```bash
cd ~/.omp/plugins
bun add context-mode    # 或：npm install context-mode
```

然后重启 OMP。无需编辑锁文件，也无需锁定版本——每次加载器运行时都会从新安装的包中读取版本（参见 [`loader.ts:87`](https://github.com/can1357/oh-my-pi/blob/main/packages/coding-agent/src/extensibility/plugins/loader.ts) `manifest.version = pluginPkg.version`）。

**安装 — 仅 MCP 路径（无插件）：**

1. 全局安装 context-mode：

   ```bash
   npm install -g context-mode
   ```

2. 添加到 `~/.omp/agent/mcp.json`（用户作用域）或 `<project>/.omp/mcp.json`（项目作用域）：

   ```json
   {
     "mcpServers": {
       "context-mode": {
         "command": "context-mode"
       }
     }
   }
   ```

3. 复制路由指令：

   ```bash
   cp node_modules/context-mode/configs/omp/SYSTEM.md ~/.omp/agent/SYSTEM.md
   ```

   项目作用域替代方案：`cp ... .omp/SYSTEM.md`。OMP 也会自动发现项目树中的任何 `AGENTS.md`。

4. 重启 OMP。

**验证（任意路径）：** 在 OMP 会话中键入 `ctx stats`。应能看到 context-mode 工具出现并响应。

**路由：** 插件路径——通过四个 `pi.on(...)` 处理器进行程序强制（`tool_call` 返回 `{ block: true, reason }` 用于 `curl`/`wget`/inline-fetch，参见上游 [`hooks/types.ts:566`](https://github.com/can1357/oh-my-pi/blob/main/packages/coding-agent/src/extensibility/hooks/types.ts)，`tool_result` 捕获会话事件，`session_start` 初始化每会话 DB 行，`session_before_compact` 持久化恢复快照）。约 98% 合规率，与 Claude Code Hooks 持平。仅 MCP 路径——基于 `SYSTEM.md` 的规则强制，约 60% 合规率。通过 `PI_CODING_AGENT_DIR` 环境变量或 `~/.omp/` 的存在自动检测。存储根位于 `~/.omp/context-mode/`，因此 OMP 和 Pi 安装永远不会共享会话 DB、内容索引或统计文件。

完整配置：[`configs/omp/mcp.json`](configs/omp/mcp.json) | [`configs/omp/SYSTEM.md`](configs/omp/SYSTEM.md) | 插件源码：[`src/adapters/omp/plugin.ts`](src/adapters/omp/plugin.ts)

</details>

<details>
<summary><strong>构建前置条件（Build Prerequisites）</strong> <sup>(CentOS, RHEL, Alpine)</sup></summary>

Context Mode 在 Node.js 上使用 [better-sqlite3](https://github.com/WiseLibs/better-sqlite3)，它为大多数平台提供预编译原生二进制文件。在 glibc >= 2.31 的系统上（Ubuntu 20.04+, Debian 11+, Fedora 34+, macOS, Windows），`npm install` 无需任何构建工具即可工作。

**Linux + Node.js >= 22.5：** Context Mode 会自动使用内置的 `node:sqlite` 模块替代 `better-sqlite3`。这完全消除了原生插件依赖，避免了由 V8 的 `madvise(MADV_DONTNEED)` 在 Linux 上损坏插件 `.got.plt` 段而导致的 [间歇性 SIGSEGV 崩溃](https://github.com/nodejs/node/issues/62515)。无需任何配置——检测是自动的。**Linux + Node < 22.5 不受支持**（[#564](https://github.com/mksglu/context-mode/issues/564)）——`npm install` 将失败并附带修复指引。

**Bun 用户：** 无需原生编译。Context Mode 会自动检测 Bun 并通过兼容适配器使用内置的 `bun:sqlite` 模块。`better-sqlite3` 及其所有构建依赖项将被完全跳过。

在较旧的 glibc 系统上（CentOS 7/8, RHEL 8, Debian 10），预编译二进制文件无法加载，且 better-sqlite3 **会自动回退到通过 `prebuild-install || node-gyp rebuild --release` 从源码编译**。这需要 C++20 编译器（GCC 10+）、Make 和带有 setuptools 的 Python。

**Windows / 缺失 binding 自动修复：** 如果安装后 `better_sqlite3.node` 最终丢失（例如 `prebuild-install` 不在 cmd.exe PATH 中，或无 MSVC 工具链），postinstall 脚本和运行时钩子会自动重新获取预编译文件并修复 binding——无需手动执行 `npm rebuild` (#408)。

**CentOS 8 / RHEL 8** (glibc 2.28):

```bash
dnf install -y gcc-toolset-10-gcc gcc-toolset-10-gcc-c++ make python3 python3-setuptools
scl enable gcc-toolset-10 'npm install -g context-mode'
```

**CentOS 7 / RHEL 7** (glibc 2.17):

```bash
yum install -y centos-release-scl
yum install -y devtoolset-10-gcc devtoolset-10-gcc-c++ make python3
pip3 install setuptools
scl enable devtoolset-10 'npm install -g context-mode'
```

**Alpine Linux:**

better-sqlite3 v12.8.0+ 中提供了 Alpine 预编译二进制文件（musl）。在 `^12.6.2` 依赖范围内，`npm install` 会解析到最新的 12.x 版本，并在 Alpine 上无需构建工具即可工作。如果你锁定了较旧版本：

```bash
apk add build-base python3 py3-setuptools
npm install -g context-mode
```

</details>

## 工具（Tools）

| 工具 | 功能 | 节省上下文 |
|---|---|---|
| `ctx_batch_execute` | 在单次调用中运行多条命令 + 搜索多个查询。可选开启 `concurrency: 1-8` 用于 I/O 密集型批处理。 | 986 KB → 62 KB |
| `ctx_execute` | 在 12 种语言中运行代码。仅 stdout 进入上下文。 | 56 KB → 299 B |
| `ctx_execute_file` | 沙箱内处理文件。原始内容永不外泄。 | 45 KB → 155 B |
| `ctx_index` | 将 markdown 分块并建立 FTS5 + BM25 索引。 | 60 KB → 40 B |
| `ctx_search` | 在单次调用中通过多个查询搜索已索引内容。 | 按需检索 |
| `ctx_fetch_and_index` | 抓取 URL、分块和索引。缓存会在 TTL 内复用内容（默认 24h，可通过 `ttl: <ms>` 覆盖）。`ttl: 0` 或 `force: true` 可绕过缓存。传入 `requests: [{url, source}, ...]` + `concurrency: 1-8` 可实现并行多 URL 抓取。 | 60 KB → 40 B |
| `ctx_stats` | 显示上下文节省情况、调用次数和会话统计信息。 | — |
| `ctx_doctor` | 诊断安装状态：运行时、Hooks、FTS5、版本。 | — |
| `ctx_upgrade` | 从 GitHub 升级到最新版本，重建缓存，重新配置 Hooks。 | — |
| `ctx_purge` | 永久删除知识库中的所有索引内容。 | — |

## 沙箱工作原理（How the Sandbox Works）

每次 `ctx_execute` 调用都会启动一个隔离的子进程，拥有独立的进程边界。脚本无法访问彼此的内存或状态。子进程运行你的代码、捕获 stdout，且仅该 stdout 进入对话上下文。原始数据——日志文件、API 响应、快照——永远不会离开沙箱。

提供十二种语言运行时：JavaScript, TypeScript, Python, Shell, Ruby, Go, Rust, PHP, Perl, R, Elixir, 和 C#。Bun 会被自动检测，用于实现 JS/TS 执行速度提升 3-5 倍。

经过身份验证的 CLI 可通过凭证透传工作——`gh`, `aws`, `gcloud`, `kubectl`, `docker` 会继承环境变量和配置路径，而不会将其暴露给对话。

当输出超过 5 KB 且提供了 `intent`（意图）时，Context Mode 会切换到基于意图的过滤：它将完整输出索引到知识库中，搜索与你的意图匹配的片段，并仅返回相关匹配项以及用于后续查询的可搜索词汇表。

## 知识库工作原理（How the Knowledge Base Works）

`ctx_index` 工具按标题对 markdown 内容进行分块同时保持代码块完整，然后将其存储在 **SQLite FTS5**（全文检索 5）虚拟表中。SQLite 后端在运行时自动选择：Bun 上使用 `bun:sqlite`，Node.js >= 22.5 上使用 `node:sqlite`，其他情况使用 `better-sqlite3`。搜索使用 **BM25 评分**——一种概率相关性算法，基于词频、逆文档频率和文档长度归一化对文档进行打分。**Porter 词干提取（Stemming）**在索引时应用，因此 "running", "runs" 和 "ran" 会匹配同一个词干。标题和标题在 BM25 评分中权重为 **5倍**，以实现精确的导航查询。

当你调用 `ctx_search` 时，它会返回围绕匹配查询术语聚焦的相关片段——不是完整文档，也不是近似值，而是实际索引内容以及针对你查找内容的智能提取结果。`ctx_fetch_and_index` 将此功能扩展到 URL：抓取、将 HTML 转换为 markdown、分块、索引。原始页面永远不会进入上下文。使用 `contentType` 参数按类型过滤结果（例如 `code` 或 `prose`）。

### 排序：互逆排名融合（Reciprocal Rank Fusion）

搜索运行两种并行策略并使用 **RRF** 合并它们：

- **Porter 词干提取** — FTS5 MATCH 配合 Porter 分词器。"caching" 匹配 "cached", "caches", "cach"。
- **三元组子串（Trigram substring）** — FTS5 trigram 分词器匹配部分字符串。"useEff" 找到 "useEffect"，"authenticat" 找到 "authentication"。

RRF 将两个排名列表合并为单一结果集，因此在两种策略中都表现良好的文档会比仅在一项中表现好的文档排名更高。这取代了旧的级联回退方法（即仅在 Porter 无返回时才使用 trigram 结果）。

### 邻近重排序（Proximity Reranking）

多词查询会获得额外的重排序阶段。查询术语出现位置较近的结果会被提升——`"session continuity"` 会将相邻术语的段落排名高于 "session" 和 "continuity" 相隔数段的页面。

### 模糊修正（Fuzzy Correction）

Levenshtein 距离会在重新搜索前纠正拼写错误。"kuberntes" 变为 "kubernetes"，"autentication" 变为 "authentication"。

### 智能片段提取（Smart Snippets）

搜索结果使用智能提取而非简单截断。与其返回前 N 个字符（可能会遗漏关键部分），Context Mode 会查找你的查询术语在内容中出现的位置，并围绕这些匹配项返回窗口区域。

### TTL 缓存（TTL Cache）

索引内容持久化存储在每项目 SQLite 数据库中 `~/.context-mode/content/`。当对已在其 TTL 窗口内索引过的 URL 调用 `ctx_fetch_and_index` 时，抓取将被完全跳过，模型将直接搜索现有索引。

- **默认 TTL：** 24 小时。可通过 `ttl: <milliseconds>` 按次覆盖（PR #666）。稳定规范可设更长，更新日志可设更短以便频繁重新检查。
- **缓存命中（TTL 内）：** 返回缓存提示符（约 0.3KB）而非重新抓取（48KB+）。模型随后执行 `ctx_search`。
- **缓存未命中（TTL 过期）：** 静默重新抓取。无需用户操作。
- **`ttl: 0`** 或 **`force: true`:** 绕过缓存并强制重新抓取，无论新鲜度如何。
- **14 天清理：** 启动时移除超过 14 天的内容数据库和来源文件。

这意味着 `--continue` 会话会在重启间保留索引文档。无需重新抓取，不浪费上下文 token。

`ctx_stats` 会单独报告缓存性能：命中次数、避免的数据量、节省的网络请求以及包含缓存的总上下文节省量。

### 渐进式节流（Progressive Throttling）

- **第 1-3 次调用：** 正常结果（每次查询返回 2 条）
- **第 4-8 次调用：** 减少结果（每次查询返回 1 条）+ 警告
- **第 9 次及以后：** 阻止——重定向至 `ctx_batch_execute`

## 会话连续性（Session Continuity）

当上下文窗口填满时，Agent 会压缩对话——丢弃旧消息以腾出空间。如果没有会话追踪，模型将忘记正在编辑哪些文件、进行中的任务是什么、已解决的错误有哪些、以及你上次要求了什么。

Context Mode 会在你的会话期间捕获每个有意义的事件，并将它们持久化到每项目 SQLite 数据库中。当对话被压缩（或你使用 `--continue`、`--resume` 或 `/resume` 恢复时），你的工作状态会自动重建——模型会从你上次的提示继续执行，无需重复任何操作。

> 通过 `/resume <picker>` 恢复非最新会话的方式相同：SessionStart Hook 会检测到新发出的会话 ID 对应的空事件表，并回退到该项目最近的未消耗快照（`session_resume` 表）。Picker 选择对话；context-mode 重新水合（rehydrate）之前工作状态。

会话连续性需要 5 个 Hooks 协同工作：

| Hook | 作用 | Claude Code | Gemini CLI | VS Code Copilot | JetBrains Copilot | Cursor | OpenCode | KiloCode | OpenClaw | Codex CLI | Antigravity | Kiro | Zed | Pi | OMP |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **PreToolUse** | 在工具执行前强制沙箱路由 | Yes | -- | -- | -- | Yes | -- | -- | -- | Yes | -- | Yes | -- | ✓ (via tool_call event) | ✓ (via tool_call event) |
| **PostToolUse** | 捕获每次工具调用后的事件 | Yes | Yes | Yes | Yes | Yes | Plugin | Plugin | Plugin | Yes | -- | Yes | -- | ✓ (via tool_result event) | ✓ (via tool_result event) |
| **UserPromptSubmit** | 捕获用户决策和修正 | Yes | -- | -- | -- | -- | Plugin (via chat.message) | Plugin (via chat.message) | -- | Yes | -- | -- | -- | -- | -- |
| **PreCompact** | 在压缩前构建快照 | Yes | Yes | Yes | Yes | -- | Plugin | Plugin | Plugin | Yes | -- | -- | -- | ✓ (via session_before_compact) | ✓ (via session_before_compact) |
| **SessionStart** | 在压缩或恢复后恢复状态 | Yes | Yes | Yes | Yes | -- | ✓ (via experimental.chat.system.transform) | ✓ (via experimental.chat.system.transform) | Plugin | Yes | -- | -- | -- | ✓ (via session_start event) | ✓ (via session_start event) |
| | **会话完整性** | **Full** | **High** | **High** | **High** | **Partial** | **Full** | **Full** | **High** | **Partial** | **--** | **Partial** | **--** | **High** | **High** |

> **注意：** 完整会话连续性（捕获 + 快照 + 恢复）在 **Claude Code**, **Gemini CLI**, **VS Code Copilot**, **JetBrains Copilot**, **OpenCode**, 和 **KiloCode** 上有效。**OpenCode** 和 **KiloCode** 使用 `experimental.chat.system.transform` 作为 SessionStart 替代方案以注入路由块并恢复前一会话，并使用 `chat.message` 捕获用户提示；完整 SessionStart Hook 支持尚未可用（[#14808](https://github.com/sst/opencode/issues/14808), [#5409](https://github.com/sst/opencode/issues/5409)），但前一会话连续性和用户决策捕获已完全工作。**Cursor** 通过 `preToolUse`/`postToolUse` 捕获工具事件，但 `sessionStart` 目前被 Cursor 验证器拒绝（[论坛报告](https://forum.cursor.com/t/unknown-hook-type-sessionstart/149566)），因此压缩后的会话恢复尚不可用。**OpenClaw** 使用原生网关插件 Hooks（`api.on()`）实现完整会话连续性。**Pi Coding Agent** 通过扩展 Hooks（`tool_call`, `tool_result`, `session_start`, `session_before_compact`）提供高会话连续性。**Codex CLI** 通过 PreToolUse, PostToolUse, PreCompact, SessionStart, UserPromptSubmit 和 Stop 提供部分基于 Hook 的会话追踪；MCP 工具可用。**Antigravity**, **Kiro**, 和 **Zed** 在当前版本中无 Hook 支持，因此不可用会话追踪。**OMP (Oh My Pi)** 提供完整的插件化 Hook 支持——`omp plugin install context-mode` 注册 `tool_call`, `tool_result`, `session_start`, 和 `session_before_compact` 处理器及存储根，干净地隔离在 `~/.omp/context-mode/` 下，确保 OMP 和 Pi 安装永不共享状态。

<details>
<summary><strong>捕获内容（What gets captured）</strong></summary>

每次工具调用都会通过 Hooks 提取结构化事件：

| 类别 | 事件 | 优先级 | 由...捕获 |
|---|---|---|---|
| **Files** | read, edit, write, glob, grep | Critical (P1) | PostToolUse |
| **Tasks** | create, update, complete | Critical (P1) | PostToolUse |
| **Plans** | enter, exit, approved, rejected, file write | Critical (P1) | PostToolUse |
| **Rules** | CLAUDE.md / GEMINI.md / AGENTS.md 路径 + 内容 | Critical (P1) | SessionStart |
| **User Prompts** | 每次用户消息（用于恢复最后提示） | Critical (P1) | UserPromptSubmit |
| **Decisions** | 用户修正、偏好（"改用 X", "不要做 Y"） | High (P2) | UserPromptSubmit |
| **Git** | checkout, commit, merge, rebase, stash, push, pull, diff, status | High (P2) | PostToolUse |
| **Errors** | 工具失败、非零退出码 | High (P2) | PostToolUse |
| **Error Resolution** | 跨连续工具调用检测到的错误 → 修复对 | High (P2) | PostToolUse |
| **Constraints** | 发现的限制（"不支持", "权限拒绝"） | High (P2) | PostToolUse |
| **Blockers** | "blocked on", "waiting for", "depends on"——追踪直至解决 | High (P2) | UserPromptSubmit |
| **Rejected Approaches** | 用户拒绝的工具调用（PreToolUse → PostToolUse 标记） | High (P2) | PreToolUse |
| **Environment** | cwd 变更、venv、nvm、conda、worktree、包安装 | High (P2) | PostToolUse |
| **Agent Findings** | 完成的子 Agent 结果（前 500 字符） | High (P2) | PostToolUse |
| **Iteration Loops** | 相同工具调用 3+ 次且输入相似（重试检测） | High (P2) | PostToolUse |
| **Latency** | 超过 5s 的工具调用（工具名 + 持续时间 ms） | Normal (P3) | PreToolUse |
| **MCP Tools** | 所有 `mcp__*` 工具调用及调用次数 | Normal (P3) | PostToolUse |
| **Subagents** | Agent 工具启动和完成 | Normal (P3) | PostToolUse |
| **Skills** | 斜杠命令调用 | Normal (P3) | PostToolUse |
| **External Refs** | URL、GitHub Issue 引用 (#123)、去重 | Normal (P3) | PostToolUse |
| **Role** | 角色/行为指令（"扮演高级工程师"） | Normal (P3) | UserPromptSubmit |
| **Intent** | 会话模式分类（investigate, implement, review） | Low (P4) | UserPromptSubmit |
| **Data** | 大型用户粘贴数据引用 (>1 KB) | Low (P4) | UserPromptSubmit |

</details>

<details>
<summary><strong>会话如何幸存压缩（How sessions survive compaction）</strong></summary>

```
PreCompact fires
  → Read all session events from SQLite
  → Build priority-tiered XML snapshot (≤2 KB)
  → Store snapshot in session_resume table

SessionStart fires (source: "compact")
  → Retrieve stored snapshot
  → Write structured events file → auto-indexed into FTS5
  → Build Session Guide with 15 categories
  → Inject <session_knowledge> directive into context
  → Model continues from last user prompt with full working state
```

快照按优先级分层构建——如果 2 KB 预算紧张，低优先级事件（意图、MCP 工具计数）会首先被丢弃，而关键状态（活动文件、任务、规则、决策）始终保留。

压缩后，模型会收到一份 **Session Guide**——包含可操作部分的结构化叙述：

- **Last Request** — 用户最后提示，使模型无需询问 "我们在做什么？"即可继续
- **Tasks** — 复选框格式及完成状态（`[x]` 已完成, `[ ]` 待处理）
- **Plans** — plan 模式条目、退出、批准和拒绝
- **Key Decisions** — 用户修正和偏好（"改用 X", "不要做 Y"）
- **Files Modified** — 会话期间触碰的所有文件
- **Unresolved Errors** — 未修复的错误，以及错误→修复对
- **Constraints** — 发现的限制和边界
- **Blockers** — 开放和已解决的阻塞项（"blocked on X", "waiting for Y"）
- **Git** — 执行的操作（checkout, commit, push, status）
- **Project Rules** — CLAUDE.md / GEMINI.md / AGENTS.md 路径
- **MCP Tools Used** — 工具名及调用次数
- **Subagent Tasks** — 委托工作摘要 + Agent 发现结果
- **Skills Used** — 调用的斜杠命令
- **Rejected Approaches** — 用户拒绝的工具调用
- **External References** — URL 和 GitHub Issue 引用
- **Environment** — 工作目录、环境变量、worktrees
- **Data References** — 会话期间粘贴的大型数据
- **Session Intent** — 模式分类（implement, investigate, review, discuss）
- **User Role** — 会话期间设置的行为指令

详细事件数据也会索引到 FTS5 中，以便通过 `ctx_search()` 按需检索。

</details>

<details>
<summary><strong>各平台详情（Per-platform details）</strong></summary>

**Claude Code** — 完整会话支持。所有 5 种 Hook 类型均会触发，捕获工具事件、用户决策、构建压缩快照，并在压缩后、`--continue`、`--resume` 或 `/resume` 后恢复状态。

**Gemini CLI** — 高覆盖率。PostToolUse (AfterTool), PreCompact (PreCompress) 和 SessionStart 均会触发。缺少 UserPromptSubmit，因此不捕获用户决策和修正——但文件编辑、Git 操作、错误和任务已完整追踪。

**VS Code Copilot** — 高覆盖率。与 Gemini CLI 相同——PostToolUse, PreCompact 和 SessionStart 均会触发。未捕获用户决策，但所有工具级事件均已记录。

**JetBrains Copilot** — 高覆盖率。具备与 VS Code Copilot 相同的能力——PostToolUse, PreCompact 和 SessionStart 均会触发。使用相同的 Hook 传输协议和响应格式。未捕获用户决策，但所有工具级事件均已记录。

**Cursor** — 部分覆盖率。原生 `preToolUse` 和 `postToolUse` Hooks 捕获工具事件。`sessionStart` 虽由 Cursor 文档化但目前被其验证器拒绝，因此不可用会话恢复。路由指令通过 MCP Server 启动传递。

**OpenCode** — 完整会话支持。TypeScript 插件通过 `tool.execute.after` 捕获 PostToolUse 事件，通过 `chat.message` 捕获用户提示和决策，通过 `experimental.session.compacting` 构建压缩快照，并通过 `experimental.chat.system.transform`（SessionStart 替代方案）恢复前一会话。路由块会在首次 `chat.system.transform` 时注入。AGENTS.md/CLAUDE.md/CONTEXT.md 规则会在首次触发 Hook 时自动捕获。

**KiloCode** — 完整会话支持。通过 OpenCodeAdapter 共享与 OpenCode 相同的插件架构。TypeScript 插件通过 `tool.execute.after` 捕获 PostToolUse 事件，通过 `chat.message` 捕获用户提示和决策，通过 `experimental.session.compacting` 构建压缩快照，并通过 `experimental.chat.system.transform`（SessionStart 替代方案）恢复前一会话。

**OpenClaw / Pi Agent** — 高覆盖率。所有工具生命周期 Hooks（`after_tool_call`, `before_compaction`, `session_start`）均通过原生网关插件触发。未捕获用户决策，但文件编辑、Git 操作、错误和任务已完整追踪。如果旧版网关版本上的压缩 Hook 失败，会回退到 DB 快照重建。参见 [`docs/adapters/openclaw.md`](docs/adapters/openclaw.md)。

**Codex CLI** — MCP 激活，Hooks 需要 `[features].hooks = true`。Hook 脚本（PreToolUse, PostToolUse, PreCompact, SessionStart, UserPromptSubmit, Stop）已实现并测试；`PreCompact` 在发出该事件的 Codex 构建版上仍受运行时限制。PreToolUse 拒绝路由有效；输入重写仍依赖上游 `updatedInput` 支持（[openai/codex#18491](https://github.com/openai/codex/issues/18491)）。

**Antigravity** — 无会话支持。无 Hooks，无事件捕获。需手动将 `GEMINI.md` 复制到项目根目录。通过 MCP 协议握手自动检测（`clientInfo.name`）。

**Zed** — 无会话支持。无 Hooks，无事件捕获。需手动将 `AGENTS.md` 复制到项目根目录。通过 MCP 协议握手自动检测（`clientInfo.name`）。

**Kiro** — 部分覆盖率。原生 `preToolUse` 和 `postToolUse` Hooks 捕获工具事件并强制沙箱路由。`agentSpawn`（Kiro 的 SessionStart 等价物）尚未实现，因此压缩后的会话恢复不可用。需手动将 `KIRO.md` 复制到项目根目录。通过 MCP 协议握手自动检测（`clientInfo.name`）。

**Pi Coding Agent** — 高覆盖率。该扩展注册了所有关键生命周期事件：`tool_call` (PreToolUse), `tool_result` (PostToolUse), `session_start` (SessionStart) 和 `session_before_compact` (PreCompact)。文件编辑、Git 操作、错误和任务已完整追踪。压缩后的会话恢复通过扩展的事件 Hooks 工作。
工具调用输出可通过 Pi 默认快捷键（Ctrl+O）折叠/展开。

**OMP (Oh My Pi)** — 高覆盖率。该插件（通过 `omp plugin install context-mode` 安装）注册了所有关键生命周期事件：`tool_call` (PreToolUse), `tool_result` (PostToolUse), `session_start` (SessionStart) 和 `session_before_compact` (PreCompact)。存储根干净隔离在 `~/.omp/context-mode/`，确保 OMP 和 Pi 安装永不共享状态（issue [#473](https://github.com/mksglu/context-mode/issues/473)）。通过 `PI_CODING_AGENT_DIR` 环境变量或 `~/.omp/` 的存在自动检测。

</details>

## 平台兼容性（Platform Compatibility）

| 特性 | Claude Code | Qwen Code | Gemini CLI | VS Code Copilot | JetBrains Copilot | Cursor | OpenCode | KiloCode | OpenClaw | Codex CLI | Antigravity | Kiro | Zed | Pi | OMP |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MCP Server / 原生工具 | Yes | Yes | Yes | Yes | Yes | Yes | Native plugin | Native plugin | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| PreToolUse Hook | Yes | Yes | Yes | Yes | Yes | Yes | Plugin | Plugin | Plugin | Yes | -- | Yes | -- | Yes (extension) | Plugin |
| PostToolUse Hook | Yes | Yes | Yes | Yes | Yes | Yes | Plugin | Plugin | Plugin | Yes | -- | Yes | -- | Yes (extension) | Plugin |
| SessionStart Hook | Yes | Yes | Yes | Yes | Yes | -- | ✓ (via experimental.chat.system.transform) | ✓ (via experimental.chat.system.transform) | Plugin | Yes | -- | -- | -- | Yes (extension) | Plugin |
| PreCompact Hook | Yes | Yes | Yes | Yes | Yes | -- | Plugin | Plugin | Plugin | Yes | -- | -- | -- | Yes (extension) | Plugin |
| 可修改参数 | Yes | Yes | Yes | Yes | Yes | Yes | Plugin | Plugin | Plugin | -- | -- | -- | -- | Yes (extension) | -- |
| 可阻止工具 | Yes | Yes | Yes | Yes | Yes | Yes | Plugin | Plugin | Plugin | Yes | -- | Yes | -- | Yes (extension) | Plugin |
| 实用命令（ctx） | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes (/ctx-stats, /ctx-doctor) | Yes |
| 斜杠命令 | Yes | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| 插件市场 | Yes | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |

> **OpenCode** 采用 TypeScript 插件范式——Hooks 通过 `tool.execute.before`, `tool.execute.after`, `experimental.session.compacting`, `experimental.chat.system.transform` 和 `chat.message` 作为进程内函数运行，提供完整的路由强制、会话连续性和用户提示捕获。`experimental.chat.system.transform` Hook 充当 SessionStart 替代方案以注入路由块并恢复前一会话。`chat.message` Hook 捕获用户提示和决策（等价于 UserPromptSubmit）。
>
> **KiloCode** 通过 OpenCodeAdapter 共享与 OpenCode 相同的 TypeScript 插件架构，具有平台特定的配置路径（`kilo.json` 替代 `opencode.json`, `~/.config/kilo/` 替代 `~/.config/opencode/`）。Hook 能力与 OpenCode 匹配，包括通过 `experimental.chat.system.transform` 的 SessionStart 替代方案和通过 `chat.message` 的用户提示捕获。
>
> **OpenClaw** 将 context-mode 作为针对 Pi Agent 会话的原生网关插件运行。Hooks 通过 `api.on()`（工具/生命周期）和 `api.registerHook()`（命令）注册。所有工具拦截和压缩 Hooks 均受支持。参见 [`docs/adapters/openclaw.md`](docs/adapters/openclaw.md)。
>
> **Codex CLI** Hooks 需要 `[features].hooks = true`。MCP 工具可用，且 Hook 脚本通过 `$CODEX_HOME/hooks.json` 或 `~/.codex/hooks.json` 激活。PreToolUse 仅支持 `permissionDecision: "deny"`；输入修改仍需上游 `updatedInput` 支持（[openai/codex#18491](https://github.com/openai/codex/issues/18491)）。`additionalContext` 在 PreToolUse 中不受支持（上下文注入通过 PostToolUse 和 SessionStart 工作；codex 格式化程序会自动处理此部分）。PreCompact 会在发出该事件的 Codex 构建版压缩前存储恢复快照，SessionStart 会恢复它们，UserPromptSubmit/Stop 捕获提示和回合结束连续性事件。参见 Codex 安装部分以获取设置说明。**Antigravity** 和 **Zed** 不支持 Hooks。它们完全依赖手动复制的路由指令文件（`AGENTS.md` / `GEMINI.md`）进行强制（约 60% 合规率）。参见各平台安装部分的复制说明。Antigravity 和 Zed 通过 MCP 协议握手自动检测——无需手动平台配置。
>
> **Kiro** 支持原生 `preToolUse` 和 `postToolUse` Hooks 用于路由强制和工具事件捕获。`agentSpawn`（SessionStart 等价物）和 `stop` 尚未连接。需手动将 `KIRO.md` 复制到项目根目录。Kiro 通过 MCP 协议握手自动检测（`clientInfo.name`）。
>
> **Pi Coding Agent** 将 context-mode 作为支持完整 Hooks 的扩展运行。该扩展注册了 `tool_call`, `tool_result`, `session_start`, 和 `session_before_compact` 事件，提供高会话连续性覆盖率。MCP Server 提供全部 11 个 MCP 工具。
>
> **OMP (Oh My Pi)** 通过 `omp plugin install context-mode` 将 context-mode 作为插件运行。该插件注册了 `tool_call`, `tool_result`, `session_start`, 和 `session_before_compact` 事件以实现硬阻断路由和完整会话连续性。存储隔离在 `~/.omp/context-mode/`，确保 OMP 和 Pi 永不共享状态。通过 `PI_CODING_AGENT_DIR`（默认代理目录 `~/.omp/agent`）或 `~/.omp/` 目录自动检测。参见 [issue #473](https://github.com/mksglu/context-mode/issues/473) 了解存储隔离历史。

### 路由强制（Routing Enforcement）

Hooks 以编程方式拦截工具调用——它们可以阻止危险命令并在执行前将其重定向到沙箱。指令文件通过提示引导模型，但无法阻止任何内容。**在支持的平台中务必启用 Hooks。**

> **注意：** 路由指令文件以前会在首次会话启动时自动写入项目目录。此功能已禁用以防止 git 树污染（[#158](https://github.com/mksglu/context-mode/issues/158), [#164](https://github.com/mksglu/context-mode/issues/164)）。支持 Hook 的平台（Claude Code, Gemini CLI, VS Code Copilot, JetBrains Copilot, Cursor, OpenCode, OpenClaw, Codex CLI, OMP via plugin）通过 Hooks 注入路由，无需文件。不支持 Hook 的平台（Zed, Kiro, Antigravity）需要一次性手动复制——参见各平台安装部分。

| 平台 | Hooks | 指令文件 | 启用 Hooks | 未启用 Hooks |
|---|:---:|---|:---:|:---:|
| Claude Code | Yes (auto) | [`CLAUDE.md`](configs/claude-code/CLAUDE.md) | **~98% saved** | ~60% saved |
| Gemini CLI | Yes | [`GEMINI.md`](configs/gemini-cli/GEMINI.md) | **~98% saved** | ~60% saved |
| VS Code Copilot | Yes | [`copilot-instructions.md`](configs/vscode-copilot/copilot-instructions.md) | **~98% saved** | ~60% saved |
| JetBrains Copilot | Yes | [`copilot-instructions.md`](configs/vscode-copilot/copilot-instructions.md) | **~98% saved** | ~60% saved |
| Cursor | Yes | [`context-mode.mdc`](configs/cursor/context-mode.mdc) | **~98% saved** | ~60% saved |
| OpenCode | Plugin | [`AGENTS.md`](configs/opencode/AGENTS.md) | **~98% saved** | ~60% saved |
| OpenClaw | Plugin | [`AGENTS.md`](configs/openclaw/AGENTS.md) | **~98% saved** | ~60% saved |
| Codex CLI | Yes | [`AGENTS.md`](configs/codex/AGENTS.md) | **~98% saved** | ~60% saved |
| Antigravity | -- | [`GEMINI.md`](configs/antigravity/GEMINI.md) | -- | ~60% saved |
| Kiro | Yes | [`KIRO.md`](configs/kiro/KIRO.md) | **~98% saved** | ~60% saved |
| Zed | -- | [`AGENTS.md`](configs/zed/AGENTS.md) | -- | ~60% saved |
| Pi | ✓ | [`AGENTS.md`](configs/pi/AGENTS.md) | **~98% saved** | ~60% saved |
| OMP | Plugin | [`SYSTEM.md`](configs/omp/SYSTEM.md) | **~98% saved** | ~60% saved |

未启用 Hooks 时，一次未路由的 `curl` 或 Playwright 快照就可能将 56 KB 数据倾倒进上下文——足以抹去整个会话节省的量。

完整功能对比参见 [`docs/platform-support.md`](docs/platform-support.md)。

## 实用命令（Utility Commands）

**在任何 AI 会话中** — 直接键入命令即可。LLM 会自动调用 MCP 工具：

```
ctx stats       → context savings, call counts, session report
ctx doctor      → diagnose runtimes, hooks, FTS5, versions
ctx index       → index a local file or directory for later search
ctx search      → search previously indexed content
ctx upgrade     → update from GitHub, rebuild, reconfigure hooks
ctx purge       → permanently delete all indexed content from the knowledge base
ctx insight     → personal analytics dashboard (opens local web UI)
```

**从终端运行** — 无需 AI 会话直接执行：

```bash
context-mode doctor
context-mode index . --source project:my-app
context-mode search "authentication middleware" --source project:my-app
context-mode upgrade
context-mode insight          # opens analytics dashboard in browser
bash scripts/ctx-debug.sh    # full diagnostic report for bug reports
```

调试脚本收集 OS 信息、运行时版本、better-sqlite3 状态、适配器检测、配置文件（已脱敏）、Hook 验证、FTS5/SQLite 测试、执行器测试、进程检查、会话数据库和环境变量，汇总为单个可粘贴的 Markdown 报告。

适用于 **所有平台**。在 Claude Code 上，还提供斜杠命令（`/ctx-stats`, `/ctx-doctor`, `/ctx-index`, `/ctx-search`, `/ctx-upgrade`, `/ctx-purge`, `/ctx-insight`）。

## 基准测试（Benchmarks）

| 场景 | Raw | Context | Saved |
|---|---|---|---|
| Playwright snapshot | 56.2 KB | 299 B | 99% |
| GitHub Issues (20) | 58.9 KB | 1.1 KB | 98% |
| Access log (500 requests) | 45.1 KB | 155 B | 100% |
| Context7 React docs | 5.9 KB | 261 B | 96% |
| Analytics CSV (500 rows) | 85.5 KB | 222 B | 100% |
| Git log (153 commits) | 11.6 KB | 107 B | 99% |
| Test output (30 suites) | 6.0 KB | 337 B | 95% |
| Repo research (subagent) | 986 KB | 62 KB | 94% |

完整会话中：315 KB 原始输出缩减至 5.4 KB。会话时间从约 30 分钟延长至约 3 小时。

[包含 21 个场景的完整基准数据 →](BENCHMARK.md)

## 试用（Try It）

这些提示开箱即用。每次运行后执行 `/context-mode:ctx-stats` 查看节省效果。

**深度仓库研究** — 5 次调用，62 KB 上下文（原始：986 KB，节省 94%）
```
Research https://github.com/modelcontextprotocol/servers — architecture, tech stack,
top contributors, open issues, and recent activity. Then run /context-mode:ctx-stats.
```

**Git 历史分析** — 1 次调用，5.6 KB 上下文
```
Clone https://github.com/facebook/react and analyze the last 500 commits:
top contributors, commit frequency by month, and most changed files.
Then run /context-mode:ctx-stats.
```

**网页抓取** — 1 次调用，3.2 KB 上下文
```
Fetch the Hacker News front page, extract all posts with titles, scores,
and domains. Group by domain. Then run /context-mode:ctx-stats.
```

**大型 JSON API** — 7.5 MB raw → 0.9 KB context (节省 99%)
```
Create a local server that returns a 7.5 MB JSON with 20,000 records and a secret
hidden at index 13000. Fetch the endpoint, find the hidden record, and show me
exactly what's in it. Then run /context-mode:ctx-stats.
```

**文档搜索** — 2 次调用，1.8 KB 上下文
```
Fetch the React useEffect docs, index them, and find the cleanup pattern
with code examples. Then run /context-mode:ctx-stats.
```

**会话连续性** — 压缩恢复与完整状态
```
Start a multi-step task: "Create a REST API with Express — add routes, tests,
and error handling." After 20+ tool calls, type: ctx stats to see the session
event count. When context compacts, the model continues from your last prompt
with tasks, files, and decisions intact — no re-prompting needed.
```

## 隐私与架构（Privacy & Architecture）

Context Mode 不是 CLI 输出过滤器或云端分析仪表盘。它在 MCP 协议层运行——原始数据保留在沙箱子进程中，永远不会进入你的上下文窗口。网页、API 响应、文件分析、Playwright 快照、日志文件——所有内容均在完全隔离的环境中处理。

**没有任何数据离开你的机器。** 无遥测、无云同步、无使用追踪、无需账户。你的代码、提示词、会话数据——全部本地化。SQLite 数据库位于你的主目录中，任务完成后即销毁。

这是 deliberate 的架构选择，而非缺失功能。上下文优化应在源头发生，而不是在按座位订阅背后的仪表盘后处理。隐私优先是我们的理念——每个设计决策均源于此。 [License →](#license)

## 安全（Security）

Context Mode 强制执行你已使用的相同权限规则——但将其扩展到 MCP 沙箱中。如果你阻止了 `sudo`，它也会在 `ctx_execute`, `ctx_execute_file` 和 `ctx_batch_execute` 中被阻止。

**零配置即可。** 如果你未配置任何权限，则不会发生任何变化。仅在你添加规则时激活。

```json
{
  "permissions": {
    "deny": [
      "Bash(sudo *)",
      "Bash(rm -rf /*)",
      "Read(.env)",
      "Read(**/.env*)"
    ],
    "allow": [
      "Bash(git:*)",
      "Bash(npm:*)"
    ]
  }
}
```

将此添加到你的项目 `.claude/settings.json`（或 `~/.claude/settings.json` 用于全局规则）。所有平台均从 Claude Code 的设置格式读取安全策略——即使在 Gemini CLI, VS Code Copilot 和 OpenCode 上也是如此。Codex CLI 的安全执行需要配置 `$CODEX_HOME/hooks.json` 或 `~/.codex/hooks.json` 中的 Codex Hooks。

模式为 `Tool(匹配内容)`，其中 `*` 表示 "任意"。

使用 `&&`, `;` 或 `|` 链接的命令会被拆分——每部分单独检查。`echo hello && sudo rm -rf /tmp` 会被阻止，因为 `sudo` 部分匹配了拒绝规则。

**deny** 始终优于 **allow**。更具体（项目级）的规则覆盖全局规则。

### 网络抓取加固（Network fetch hardening）

默认情况下，`ctx_fetch_and_index` 会阻止危险的 URL 目标：

- **协议：** 仅允许 `http:` 和 `https:`（禁止 `file://`, `gopher://`, `javascript:`, `data:`）。
- **云元数据 + 链接本地地址：** `169.254.0.0/16`（包括 AWS/GCP/Azure IMDS 端点 `169.254.169.254`）即使主机名解析到它也会被硬阻止（DNS 重绑定防御）。
- **组播 / 保留地址：** `224.0.0.0/4`, `0.0.0.0/8`, IPv6 `ff00::/8`, `fe80::/10` 被阻止。
- **回环 + RFC1918**（`localhost`, `127.x`, `10.x`, `172.16-31.x`, `192.168.x`, IPv6 `::1`, `fc00::/7`）**默认允许**，以便本地开发服务器 + 内网抓取继续工作。

对于希望同时阻止私有目标的主机/CI 环境，请设置：

```bash
export CTX_FETCH_STRICT=1
```

这会在始终阻止的范围内额外阻止回环 + RFC1918 + ULA。适用于 context-mode 作为共享服务运行而非在开发者本机运行的场景。

任何 `mcp__*` 工具调用的 `tool_input` 也会在持久化前被脱敏——`hooks/posttooluse.mjs` 中的正则匹配器将 `authorization`, `auth_token`, `access_token`, `refresh_token`, `bearer`, `token`, `secret`, `password`, `passwd`, `pwd`, `api_key` / `apikey` / `x_api_key`, `cookie` / `set-cookie`, `signature`, `private_key`, 和 `client_secret`（不区分大小写，连字符/下划线不敏感）掩码为 `[REDACTED]`，以确保 MCP 参数中的凭证不会进入会话 DB。

### 存储环境变量

| 变量 | 默认值 | 用途 |
|---|---|---|
| `CONTEXT_MODE_DIR` | 适配器默认值，例如 `~/.codex/context-mode` 或 `~/.claude/context-mode` | 自 v1.0.147。context-mode 存储的绝对可写根路径。会话和统计信息使用 `<root>/sessions`；索引内容使用 `<root>/content`。空值或仅包含空白符的值被视为未设置并由 `ctx_doctor` 显示；非空值必须为绝对路径。不支持 `~` 展开。 |

### 路由引导环境变量

| 变量 | 默认值 | 用途 |
|---|---|---|
| `CONTEXT_MODE_EXTERNAL_MCP_NUDGE_EVERY` | `10` | PreToolUse Hook 重新注入 "将大型外部 MCP 负载包装在 `ctx_execute` 中" 引导的周期（按工具调用次数）。原始实现（[#529](https://github.com/mksglu/context-mode/pull/529)）仅在会话开始时触发一次，这在重度 MCP 会话（例如 50+ Jira/Slack/Notion 调用——参见 [#567](https://github.com/mksglu/context-mode/issues/567) 后续问题）的上下文压缩后会丢失。默认设置会在每第 10 次匹配调用时重新触发，使引导保留在模型的近期窗口中。范围 `[1, 100]`；无效值回退到 `10`。设置为 `1` 表示 "每次调用"（最激进——增加约 250 token/调用）或更大值以减少提醒频率。 |

## 贡献（Contributing）

参见 [CONTRIBUTING.md](CONTRIBUTING.md) 了解开发工作流和 TDD 指南。

```bash
git clone https://github.com/mksglu/context-mode.git
cd context-mode && npm install && npm test
```

## License

Licensed under [Elastic License 2.0](LICENSE) (source-available). You can use it, fork it, modify it, and distribute it. Two things you can't do: offer it as a hosted/managed service, or remove the licensing notices. We chose ELv2 over MIT because MIT permits repackaging the code as a competing closed-source SaaS — ELv2 prevents that while keeping the source available to everyone.