<p align="center">
  <img src="docs/logo.svg" alt="Reasonix" width="640"/>
</p>

<p align="center">
  <strong>English</strong>
  &nbsp;·&nbsp;
  <a href="./README.zh-CN.md">简体中文</a>
  &nbsp;·&nbsp;
  <a href="./docs/SPEC.md">Spec</a>
  &nbsp;·&nbsp;
  <a href="https://esengine.github.io/DeepSeek-Reasonix/">Website</a>
  &nbsp;·&nbsp;
  <strong><a href="https://discord.gg/XF78rEME2D">Discord</a></strong>
</p>

> [!IMPORTANT]
> **Reasonix 1.0 采用 Go 语言完全重写** —— 本分支（`main-v2`）为新的默认分支，也是当前的开发主线。早期的 `0.x` TypeScript 版本属于**遗留版本**，保留在 [`v1`](https://github.com/esengine/DeepSeek-Reasonix/tree/v1) 分支上（仅维护）。请参阅 **[迁移指南](./docs/MIGRATING.md)**。安装命令仍为 `npm i -g reasonix` —— `1.0.0`+ 版本提供 Go 编译的二进制文件，`0.x` 为遗留的 TS 构建版。

<p align="center">
  <a href="https://www.npmjs.com/package/reasonix"><img src="https://img.shields.io/npm/v/reasonix.svg?style=flat-square&color=cb3837&labelColor=161b22&logo=npm&logoColor=white" alt="npm version"/></a>
  <a href="https://github.com/esengine/reasonix/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/esengine/reasonix/ci.yml?style=flat-square&label=ci&labelColor=161b22&logo=githubactions&logoColor=white" alt="CI"/></a>
  <a href="./LICENSE"><img src="https://img.shields.io/npm/l/reasonix.svg?style=flat-square&color=8b949e&labelColor=161b22" alt="license"/></a>
  <a href="https://www.npmjs.com/package/reasonix"><img src="https://img.shields.io/npm/dm/reasonix.svg?style=flat-square&color=3fb950&labelColor=161b22&label=downloads" alt="downloads"/></a>
  <a href="https://github.com/esengine/reasonix/stargazers"><img src="https://img.shields.io/github/stars/esengine/reasonix.svg?style=flat-square&color=dbab09&labelColor=161b22&logo=github&logoColor=white" alt="GitHub stars"/></a>
  <a href="https://atomgit.com/esengine/DeepSeek-Reasonix"><img src="https://atomgit.com/esengine/DeepSeek-Reasonix/star/badge.svg" alt="AtomGit stars"/></a>
  <a href="https://github.com/esengine/reasonix/graphs/contributors"><img src="https://img.shields.io/github/contributors/esengine/reasonix.svg?style=flat-square&color=bc8cff&labelColor=161b22&logo=github&logoColor=white" alt="contributors"/></a>
  <a href="https://github.com/esengine/reasonix/discussions"><img src="https://img.shields.io/github/discussions/esengine/reasonix.svg?style=flat-square&color=58a6ff&labelColor=161b22&logo=github&logoColor=white" alt="Discussions"/></a>
  <a href="https://discord.gg/XF78rEME2D"><img src="https://img.shields.io/badge/discord-join-5865F2.svg?style=flat-square&labelColor=161b22&logo=discord&logoColor=white" alt="Discord"/></a>
</p>

<p align="center">
  <a href="https://oosmetrics.com/repo/esengine/reasonix"><img src="https://api.oosmetrics.com/api/v1/badge/achievement/9e931d80-2050-4b10-902e-44970cc133ad.svg" alt="oosmetrics — Top 2 in Agents by velocity"/></a>
  <a href="https://oosmetrics.com/repo/esengine/reasonix"><img src="https://api.oosmetrics.com/api/v1/badge/achievement/556d94b3-61b7-486b-baf2-888b9327deab.svg" alt="oosmetrics — Top 3 in LLMs by velocity"/></a>
  <a href="https://oosmetrics.com/repo/esengine/reasonix"><img src="https://api.oosmetrics.com/api/v1/badge/achievement/0f457d4c-efca-4d15-ad2b-139691ff342c.svg" alt="oosmetrics — Top 3 in CLI by velocity"/></a>
</p>

<br/>

<h3 align="center">面向终端的 DeepSeek 原生 AI 编程 Agent。</h3>
<p align="center">基于配置与插件驱动的开发框架 —— 单个静态 Go 二进制文件，针对 DeepSeek 前缀缓存深度优化，确保长会话中 Token 成本保持低位。</p>

<br/>

> [!IMPORTANT]
> **加入社区 · Community** — 中英双语 Discord 频道，提供安装支持（`#help` / `#求助`）、工作流展示及功能建议。→ **<https://discord.gg/XF78rEME2D>**

<br/>

## 功能特性

- **配置驱动。** 提供商（Provider）、Agent、启用的工具及插件均在 `reasonix.toml` 中声明。无需硬编码模型。
- **多模型与可组合。** DeepSeek (flash/pro) 和 MiMo 作为预设提供；任何兼容 OpenAI 的端点只需添加配置项，无需修改代码。可选择在独立的缓存稳定会话中同时运行两个模型（执行器 + 规划器）。
- **插件驱动。** 外部工具通过 stdio JSON-RPC（MCP 兼容）作为子进程运行。内置工具在编译时自动注册。
- **零摩擦分发。** `CGO_ENABLED=0` 单文件二进制；一条命令即可交叉编译至六个目标平台。唯一依赖为 TOML 解析器。

## 安装

```sh
npm i -g reasonix                  # 支持所有操作系统；拉取预构建原生二进制文件
brew install esengine/reasonix/reasonix   # macOS
```

预构建归档包（`darwin|linux|windows × amd64|arm64`）及 `SHA256SUMS` 校验文件位于每个 [GitHub Release](https://github.com/esengine/DeepSeek-Reasonix/releases)。

### 从源码构建

```sh
make build      # -> bin/reasonix(.exe)
make cross      # -> dist/ (darwin|linux|windows × amd64|arm64)
```

## 快速开始

```sh
reasonix setup                      # 配置向导 → ./reasonix.toml
export DEEPSEEK_API_KEY=sk-...  # 或将其放入 .env（参见 .env.example）
reasonix chat                       # 然后运行 /init 生成 AGENTS.md（项目记忆）
reasonix run "implement the TODOs in main.go"
reasonix run --model mimo-pro "add unit tests for this function"
echo "explain this code" | reasonix run
```

## 配置

解析优先级：**命令行参数 > `./reasonix.toml` > `~/.config/reasonix/config.toml` > 内置默认值**。密钥通过环境变量 `api_key_env` 获取，绝不会存储在配置文件中。

```toml
default_model = "deepseek-flash"   # executor; set [agent].planner_model to add a planner
# language    = "zh"               # ui language; empty = auto-detect from $LANG / $REASONIX_LANG

[agent]
# planner_model = "mimo-pro"          # optional low-frequency planner
# subagent_model = "deepseek-pro"     # optional default for runAs=subagent skills
# subagent_models = { review = "deepseek-pro", security_review = "deepseek-pro" }
auto_plan = "ask"                  # off|ask|on; complex chat tasks start in plan mode
# auto_plan_classifier = "deepseek-flash"   # optional; only borderline tasks call it

[[providers]]
name        = "deepseek-flash"
kind        = "openai"
base_url    = "https://api.deepseek.com"
model       = "deepseek-v4-flash"
api_key_env = "DEEPSEEK_API_KEY"
# also preset: deepseek-pro, mimo-pro (mimo-v2.5-pro), mimo-flash (mimo-v2-flash) @ api.xiaomimimo.com/v1

[tools]
enabled = []   # omit/empty = all built-ins

[skills]
# paths = ["~/my-skills", "../shared/skills"]   # extra custom skill roots
# disabled_skills = ["review"]                  # hide skills until /skill enable <name>

[permissions]
mode  = "ask"                                # writer fallback when no rule matches: ask|allow|deny
deny  = ["bash(rm -rf*)", "bash(git push*)"] # hard-blocked in every mode
allow = ["bash(go test*)"]                   # never prompted

[sandbox]
# workspace_root = ""          # file-writers confined here; empty = current dir
# allow_write    = ["/tmp"]    # extra dirs write_file/edit_file/multi_edit may touch

[[plugins]]
name    = "example"
command = "reasonix-plugin-example"
```

权限控制每次工具调用：`deny` > `ask` > `allow` > 回退机制（读取器始终允许；写入器回退至 `mode`）。`reasonix chat` 会在写入操作前弹出提示（输入 `y` 确认一次 · `a` 本次会话同意 · `n` 拒绝）；`reasonix run` 保持自主运行，但仍会遵守 `deny` 规则。完整架构与契约请参阅 [`docs/SPEC.md`](docs/SPEC.md)。

权限是**策略**（决定允许哪些调用或弹出提示）。**沙箱（sandbox）** 则是**执行层**：文件写入器（`write_file` / `edit_file` / `multi_edit`）会拒绝任何超出 `[sandbox] workspace_root`（默认：当前目录，确保编辑操作留在项目内）的路径，并自动解析符号链接和 `..`，防止通过链接越权。读取操作不受限制。在 macOS 上，`bash` 默认受沙箱隔离（`[sandbox] bash`，基于 Seatbelt）：命令仅能写入上述根目录（加上临时文件和工具链缓存），且仅在 `[sandbox] network` 启用时才能访问网络。其他平台目前回退为无限制运行（详见 `docs/SPEC.md` §9 中的逃逸提示及 Linux 支持计划）。

### 插件（MCP）

Reasonix 是一个 MCP 客户端。`[[plugins]]` 条目的 `type` 字段选择传输方式：
`stdio`（默认）会启动本地子进程（配置 `command`/`args`/`env`）；`http`（Streamable HTTP）连接至远程 `url`，支持可选的静态 `headers`（`${VAR}` / `${VAR:-default}` 会从环境变量展开，确保令牌不出现在文件中）。工具对模型暴露为 `mcp__<server>__<tool>`；声明了 MCP `readOnlyHint: true` 的工具将加入并行调度与权限读取器默认组。

服务器的 **prompts（提示词）** 会作为 `/mcp__<server>__<prompt>` 斜杠命令暴露（命令后跟位置参数）；其 **resources（资源）** 可通过在消息中写入 `@<server>:<uri>` 拉取；`/mcp` 命令列出已连接的服务端及各服务端暴露的内容。运行 `make build` 还会生成 `bin/reasonix-plugin-example` —— 一个可运行的参考 stdio 服务端（包含 `echo`、`wordcount`、`review` 提示词及风格指南资源），你可直接复制使用。

```toml
[[plugins]]                       # local stdio server
name    = "example"
command = "reasonix-plugin-example"

[[plugins]]                       # remote server over Streamable HTTP
name    = "stripe"
type    = "http"
url     = "https://mcp.stripe.com"
headers = { Authorization = "Bearer ${STRIPE_KEY}" }
```

**已有 `.mcp.json`？** 将其放入项目根目录，Reasonix 会直接读取 —— `mcpServers` 规范（`command`/`args`/`env`, `type`/`url`/`headers`, `${VAR}` 展开）与 `[[plugins]]` 逐字段映射。两者配置将合并；若名称冲突，以 `reasonix.toml` 为准。

```json
{
  "mcpServers": {
    "filesystem": { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path"] },
    "stripe": { "type": "http", "url": "https://mcp.stripe.com", "headers": { "Authorization": "Bearer ${STRIPE_KEY}" } }
  }
}
```

**从 `0.x` 升级？** 旧的 `~/.reasonix/config.json` 仍会读取其 `mcpServers`（遵循 `mcpDisabled`）作为最低优先级配置源，因此 MCP 服务端将继续生效 —— 方便时请将其迁移至 `reasonix.toml` 的 `[[plugins]]` 或 `.mcp.json`。

### 斜杠命令

在 `reasonix chat` 中，内置命令（`/compact`, `/new`, `/rewind`, `/tree`, `/branch`, `/switch`, `/todo`, `/model`, `/effort`, `/mcp`, `/memory`, `/help`）在本地运行。
`/tree` 显示已保存的对话分支，`/branch [name]` 分叉当前对话节点，`/branch <turn> [name]` 从较早的检查点分叉，`/switch <id|name>` 加载其他分支。**自定义命令**是位于 `.reasonix/commands/`（项目级）或 `~/.config/reasonix/commands/`（用户级）下的 Markdown 文件 —— `review.md` 变为 `/review`，子目录用于命名空间隔离（如 `git/commit.md` → `/git:commit`）。正文为提示词模板；调用命令时会将其作为一次对话轮次发送。

```markdown
---
description: Review the staged diff
argument-hint: [focus-area]
---
Review the staged diff. Focus on $ARGUMENTS, list bugs with file:line.
```

`$ARGUMENTS` 展开为所有以空格分隔的参数，`$1`…`$N` 对应位置参数。MCP 提示词也会在此处显示为 `/mcp__<server>__<prompt>`。

### @ 引用

在消息中嵌入 `@` 引用，Reasonix 会在发送前将其解析为带标签的上下文块：`@path/to/file`（或 `@dir`）会注入本地文件内容（或目录列表），`@<server>:<uri>` 注入 MCP 资源。仅当路径实际存在时，本地路径才会被视为引用，因此普通的 `@提及` 将保持字面量形式。输入 `/` 或 `@` 可打开自动补全菜单 —— 包含斜杠命令、分层文件导航（每次一级目录，支持进入文件夹）及 MCP 资源。

### 双模型协作（可选）

`reasonix setup` 首次运行保持极简：选择提供商 → 输入密钥（所选提供商的每种规格均启用）。后续只需一行配置即可同时运行两个模型（执行器 + 规划器，独立的缓存稳定会话）—— 将 `planner_model` 设置为任意其他已启用的提供商即可。

```toml
[agent]
planner_model = "deepseek-pro"   # used as the low-frequency planner
```

Agent 技能默认继承执行器模型。设置 `subagent_model` 可在另一配置模型上运行它们，或使用 `subagent_models` 仅覆盖特定技能（如 `review` 或 `security_review`）。

对于交互式前端，`agent.auto_plan = "ask"` 会使看似复杂的任务自动进入规划模式：Reasonix 会先起草一份只读计划，然后在执行编辑或副作用命令前等待批准。`auto_plan_classifier` 可指定廉价提供商如 `deepseek-flash`；它仅对边界输入调用，若分类失败则回退至启发式规则。

## 架构设计

三层可扩展性体系，均通过核心按名称解析的注册表实现：

1. **注册表（Registry）** —— `Provider` 和 `Tool` 为接口；核心代码无硬编码模型切换逻辑。
2. **编译时内置项** —— 提供商（`provider/openai`）与工具（`tool/builtin`）通过 `init()` 自动注册；`main` 函数通过 blank import 引用它们。添加内置项仅需一个文件加一次导入。
3. **运行时插件** —— 配置中声明的可执行文件，通过 stdin/stdout 上的换行符分隔 JSON-RPC 2.0（MCP stdio 约定）进行通信。每个远程工具均适配至 `Tool` 接口。

## 开发状态

已完成：基于注册表的提供商/工具、支持工具调用的 OpenAI 兼容流式传输（429/5xx 限频重试）、内置工具（read_file, write_file, edit_file, multi_edit, bash, ls, glob, grep, web_fetch, task, todo_write, ask）、TOML 配置、交互式 `reasonix setup` 向导、双模型协作（执行器 + 规划器独立缓存会话）、低频上下文压缩、子 Agent（`task`）、基于 bubbletea 的聊天 TUI（支持 Markdown、带控制器审批的规划模式、实时令牌/活动读数、固定任务列表、`ask` 问答选择器、`/compact` `/new` `/tree` `/branch` `/switch` `/todo`）、会话持久化与恢复、每次调用的**权限控制**（允许/询问/拒绝规则；聊天模式下写入前提示，拒绝规则全局硬拦截）、**工作区沙箱**（限制文件写入器于项目内，防符号链接/`..`越权）、MCP 客户端 —— **stdio + Streamable HTTP** 传输、工具（`mcp__server__tool`, `readOnlyHint` 感知）、提示词（斜杠命令）、资源（`@` 引用）及 `/mcp` 管理，通过 `[[plugins]]` 或项目 `.mcp.json` 配置；自定义斜杠命令（`.reasonix/commands/*.md`）、`@file` / `@resource` 引用、可运行的参考插件（`cmd/reasonix-plugin-example`）、核心循环与 CLI。Wails 桌面客户端（`desktop/`）驱动同一内核。下一步：实现 OS 级沙箱隔离 `bash`（macOS Seatbelt / Linux bubblewrap）、Anthropic 原生提供商、MCP OAuth + 遗留 SSE。详见 `docs/SPEC.md` §9。

<br/>

## Star History

<a href="https://www.star-history.com/?repos=esengine%2FDeepSeek-Reasonix&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=esengine/DeepSeek-Reasonix&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=esengine/DeepSeek-Reasonix&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=esengine/DeepSeek-Reasonix&type=date&legend=top-left" />
 </picture>
</a>

<br/>

## 支持

如果 Reasonix 对你有所帮助并希望表达感谢，欢迎捐赠。这只是一杯咖啡的谢意，而非商业合约 —— 捐款不会购买功能优先权或改变 Issue 的处理流程。

- **International** — PayPal: [paypal.me/yuhuahui](https://paypal.me/yuhuahui)
- **国内** — 微信支付（扫码）

<p align="center">
  <img src=".github/sponsor/wechat-pay.jpg" alt="WeChat Pay QR code" width="240"/>
</p>

<br/>

## 鸣谢

以下列出对 Reasonix 影响最深的几位贡献者 —— 依据提交次数与代码量综合衡量。**按字母顺序排列，不分重要性高低。** 完整贡献者图谱请见 [GitHub](https://github.com/esengine/DeepSeek-Reasonix/graphs/contributors)。

- [**ctharvey**](https://github.com/ctharvey)
- [**dimasd-angga**](https://github.com/dimasd-angga) (Dimas D. Angga)
- [**Evan-Pycraft**](https://github.com/Evan-Pycraft)
- [**ForeverYoungPp**](https://github.com/ForeverYoungPp)
- [**GTC2080**](https://github.com/GTC2080) (TaoMu)
- [**kabaka9527**](https://github.com/kabaka9527)
- [**lisniuse**](https://github.com/lisniuse) (Richie)
- [**wade19990814-hue**](https://github.com/wade19990814-hue)
- [**wviana**](https://github.com/wviana) (Wesley Viana)

特别感谢 [**Bernardxu123**](https://github.com/Bernardxu123) 设计项目 Logo，以及 [AIGC Link](https://xhslink.com/m/80ngts127cA) 在小红书上的推广。

<p align="center">
  <a href="https://github.com/esengine/DeepSeek-Reasonix/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=esengine/DeepSeek-Reasonix&max=100&columns=12" alt="Contributors to esengine/DeepSeek-Reasonix" width="860"/>
  </a>
</p>

<br/>

---

<p align="center">
  <sub>MIT — see <a href="./LICENSE">LICENSE</a></sub>
  <br/>
  <sub>Built by the community at <a href="https://github.com/esengine/DeepSeek-Reasonix/graphs/contributors">esengine/DeepSeek-Reasonix</a></sub>
</p>