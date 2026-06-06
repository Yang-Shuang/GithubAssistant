# 语言：英语 | [Português (Brasil)](docs/pt-BR/README.md) | [简体中文](README.zh-CN.md) | [繁體中文](docs/zh-TW/README.md) | [日本語](docs/ja-JP/README.md) | [한국어](docs/ko-KR/README.md) | [Türkçe](docs/tr/README.md) | [Русский](docs/ru/README.md) | [Tiếng Việt](docs/vi-VN/README.md)

# Everything Claude Code

![Everything Claude Code — the performance system for AI agent harnesses](assets/hero.png)

[![Stars](https://img.shields.io/github/stars/affaan-m/everything-claude-code?style=flat)](https://github.com/affaan-m/everything-claude-code/stargazers)
[![Forks](https://img.shields.io/github/forks/affaan-m/everything-claude-code?style=flat)](https://github.com/affaan-m/everything-claude-code/network/members)
[![Contributors](https://img.shields.io/github/contributors/affaan-m/everything-claude-code?style=flat)](https://github.com/affaan-m/everything-claude-code/graphs/contributors)
[![npm ecc-universal](https://img.shields.io/npm/dw/ecc-universal?label=ecc-universal%20weekly%20downloads&logo=npm)](https://www.npmjs.com/package/ecc-universal)
[![npm ecc-agentshield](https://img.shields.io/npm/dw/ecc-agentshield?label=ecc-agentshield%20weekly%20downloads&logo=npm)](https://www.npmjs.com/package/ecc-agentshield)
[![GitHub App Install](https://img.shields.io/badge/GitHub%20App-150%20installs-2ea44f?logo=github)](https://github.com/marketplace/ecc-tools)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Shell](https://img.shields.io/badge/-Shell-4EAA25?logo=gnu-bash&logoColor=white)
![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
![Go](https://img.shields.io/badge/-Go-00ADD8?logo=go&logoColor=white)
![Java](https://img.shields.io/badge/-Java-ED8B00?logo=openjdk&logoColor=white)
![Perl](https://img.shields.io/badge/-Perl-39457E?logo=perl&logoColor=white)
![Markdown](https://img.shields.io/badge/-Markdown-000000?logo=markdown&logoColor=white)

> **14万+ 星标** | **2.1万+ Forks** | **170+ 贡献者** | **12+ 语言生态** | **Anthropic Hackathon 获奖项目**

---

<div align="center">

**Language / 语言 / 語言 / Dil / Язык / Ngôn ngữ**

[**English**](README.md) | [Português (Brasil)](docs/pt-BR/README.md) | [简体中文](README.zh-CN.md) | [繁體中文](docs/zh-TW/README.md) | [日本語](docs/ja-JP/README.md) | [한국어](docs/ko-KR/README.md)
 | [Türkçe](docs/tr/README.md) | [Русский](docs/ru/README.md) | [Tiếng Việt](docs/vi-VN/README.md)

</div>

---

**AI Agent 工具链的性能优化系统。来自 Anthropic Hackathon 获奖者。**

不仅仅是配置文件。这是一个完整的系统：技能（skills）、本能（instincts）、记忆优化、持续学习、安全扫描，以及以研究为先的开发方式。经过超过 10 个月高强度日常使用构建真实产品而演进的生产就绪型 Agent、技能、Hooks（钩子）、规则、MCP 配置和遗留命令适配器（legacy command shims）。

适用于 **Claude Code**、**Codex**、**Cursor**、**OpenCode**、**Gemini**、**GitHub Copilot** 及其他 AI Agent 工具链。

ECC v2.0.0-rc.1 在可复用层之上增加了公开的 Hermes Operator 工作流：先从 [Hermes setup guide](docs/HERMES-SETUP.md) 开始，然后查阅 [rc.1 release notes](docs/releases/2.0.0-rc.1/release-notes.md) 和 [cross-harness architecture](docs/architecture/cross-harness.md)。

---

## The Guides（指南）

本仓库仅包含源代码。指南部分解释了所有内容。

<table>
<tr>
<td width="33%">
<a href="https://x.com/affaanmustafa/status/2012378465664745795">
<img src="./assets/images/guides/shorthand-guide.png" alt="The Shorthand Guide to Everything Claude Code" />
</a>
</td>
<td width="33%">
<a href="https://x.com/affaanmustafa/status/2014040193557471352">
<img src="./assets/images/guides/longform-guide.png" alt="The Longform Guide to Everything Claude Code" />
</a>
</td>
<td width="33%">
<a href="https://x.com/affaanmustafa/status/2033263813387223421">
<img src="./assets/images/security/security-guide-header.png" alt="The Shorthand Guide to Everything Agentic Security" />
</a>
</td>
</tr>
<tr>
<td align="center"><b>简明指南（Shorthand Guide）</b><br/>安装、基础概念与哲学。<b>请先阅读此部分。</b></td>
<td align="center"><b>详细指南（Longform Guide）</b><br/>Token 优化、记忆持久化、评估（evals）、并行处理。</td>
<td align="center"><b>安全指南（Security Guide）</b><br/>攻击向量、沙箱隔离、数据清洗、CVE、AgentShield。</td>
</tr>
</table>

| Topic | What You'll Learn |
|-------|-------------------|
| Token Optimization | 模型选择、系统提示词精简、后台进程管理 |
| Memory Persistence | 自动跨会话保存/加载上下文的 Hooks（钩子） |
| Continuous Learning | 从会话中自动提取模式并转化为可复用技能 |
| Verification Loops | 检查点与持续评估对比、评分器类型、pass@k 指标 |
| Parallelization | Git worktrees、级联方法、何时扩展实例 |
| Subagent Orchestration | 上下文问题、迭代检索模式 |

---

## What's New（更新日志）

### v2.0.0-rc.1 — Surface Refresh, Operator Workflows, and ECC 2.0 Alpha (Apr 2026)

- **Dashboard GUI** — 全新的基于 Tkinter 的桌面应用（`ecc_dashboard.py` 或 `npm run dashboard`），支持深色/浅色主题切换、字体自定义，以及页眉和任务栏的项目 Logo。
- **Public surface synced to the live repo** — metadata、catalog counts、plugin manifests 和面向安装方的文档现已与实际开源代码库一致：55 个 agents、208 个 skills 和 72 个遗留命令适配器。
- **Operator and outbound workflow expansion** — `brand-voice`、`social-graph-ranker`、`connections-optimizer`、`customer-billing-ops`、`ecc-tools-cost-audit`、`google-workspace-ops`、`project-flow-ops` 和 `workspace-surface-audit` 完善了 Operator 工作流。
- **Media and launch tooling** — `manim-video`、`remotion-video-creation` 以及升级的社交发布工具，使技术解释器和发布内容成为同一系统的一部分。
- **Framework and product surface growth** — `nestjs-patterns`、更丰富的 Codex/OpenCode 安装入口，以及扩展的跨工具链打包方式，使该仓库不仅限于 Claude Code。
- **ECC 2.0 alpha is in-tree** — `ecc2/` 中的 Rust 控制面原型现已支持本地构建，并暴露了 `dashboard`、`start`、`sessions`、`status`、`stop`、`resume` 和 `daemon` 命令。目前处于 Alpha 可用状态，尚未正式发布。
- **Operator status snapshots** — `ecc status --markdown --write status.md` 将本地状态存储转换为可移植的交接文档，涵盖就绪状态、活跃会话、技能运行健康度、安装健康度、待处理治理事件以及来自 Linear/GitHub/交接系统的关联工作项。使用 `ecc work-items upsert ...` 进行手动录入，`ecc work-items sync-github --repo owner/repo` 同步 PR/Issue 队列状态，并使用 `ecc status --exit-code` 在就绪度需要关注时使自动化流程失败。
- **Ecosystem hardening** — AgentShield、ECC Tools 成本管控、计费门户工作以及网站刷新持续围绕核心插件推进，避免分散到独立的孤岛中。

### v1.9.0 — Selective Install & Language Expansion (Mar 2026)

- **Selective install architecture** — 基于 Manifest（清单）的安装管道，使用 `install-plan.js` 和 `install-apply.js` 进行针对性组件安装。状态存储跟踪已安装内容并支持增量更新。
- **6 new agents** — `typescript-reviewer`、`pytorch-build-resolver`、`java-build-resolver`、`java-reviewer`、`kotlin-reviewer`、`kotlin-build-resolver` 将语言覆盖扩展至 10 种。
- **New skills** — `pytorch-patterns`（深度学习工作流）、`documentation-lookup`（API 参考研究）、`bun-runtime` 和 `nextjs-turbopack`（现代 JS 工具链），以及 8 个运维领域技能和 `mcp-server-patterns`。
- **Session & state infrastructure** — SQLite 状态存储与查询 CLI、用于结构化记录的会话适配器、技能演进基础架构以实现自我优化技能。
- **Orchestration overhaul** — Harness（工具链）审计评分实现确定性，编排状态和启动器兼容性加固，观察者循环防护增加至 5 层守卫。
- **Observer reliability** — 修复内存爆炸问题（节流与尾部采样）、沙箱访问修复、懒加载逻辑及重入守卫。
- **12 language ecosystems** — Java、PHP、Perl、Kotlin/Android/KMP、C++ 和 Rust 的新规则加入现有的 TypeScript、Python、Go 和通用规则中。
- **Community contributions** — 韩语和中文翻译、biome hook 优化、视频处理技能、运维技能、PowerShell 安装器、Antigravity IDE 支持。
- **CI hardening** — 修复 19 项测试失败，强制执行目录计数、验证安装清单，全量测试套件通过。

### v1.8.0 — Harness Performance System (Mar 2026)

- **Harness-first release** — ECC 现在明确定位为 Agent 工具链性能系统，而不仅仅是配置包。
- **Hook reliability overhaul** — SessionStart 根目录回退、Stop-phase 会话摘要，以及基于脚本的 Hooks（钩子）替代了脆弱的内联单行命令。
- **Hook runtime controls** — `ECC_HOOK_PROFILE=minimal|standard|strict` 和 `ECC_DISABLED_HOOKS=...` 用于在不编辑 Hook 文件的情况下进行运行时门控。
- **New harness commands** — `/harness-audit`、`/loop-start`、`/loop-status`、`/quality-gate`、`/model-route`。
- **NanoClaw v2** — 模型路由、技能热加载、会话分支/搜索/导出/压缩/指标。
- **Cross-harness parity** — Claude Code、Cursor、OpenCode 和 Codex app/CLI 的行为一致性得到收紧。
- **997 internal tests passing** — Hook/运行时重构和兼容性更新后，全量套件通过。

### v1.7.0 — Cross-Platform Expansion & Presentation Builder (Feb 2026)

- **Codex app + CLI support** — 直接支持基于 `AGENTS.md` 的 Codex、安装器目标适配及 Codex 文档
- **`frontend-slides` skill** — 零依赖 HTML 演示文稿构建器，附带 PPTX 转换指南和严格的视口适配规则
- **5 new generic business/content skills** — `article-writing`、`content-engine`、`market-research`、`investor-materials`、`investor-outreach`
- **Broader tool coverage** — Cursor、Codex 和 OpenCode 支持收紧，确保同一仓库可干净地跨所有主流工具链发布
- **992 internal tests** — 插件、Hooks（钩子）、技能及打包的验证与回归覆盖范围扩大

### v1.6.0 — Codex CLI, AgentShield & Marketplace (Feb 2026)

- **Codex CLI support** — 新增 `/codex-setup` 命令，为 OpenAI Codex CLI 兼容性生成 `codex.md`
- **7 new skills** — `search-first`、`swift-actor-persistence`、`swift-protocol-di-testing`、`regex-vs-llm-structured-text`、`content-hash-cache-pattern`、`cost-aware-llm-pipeline`、`skill-stocktake`
- **AgentShield integration** — `/security-scan` 技能直接从 Claude Code 运行 AgentShield；1282 项测试，102 条规则
- **GitHub Marketplace** — ECC Tools GitHub App 已在 [github.com/marketplace/ecc-tools](https://github.com/marketplace/ecc-tools) 上线，提供免费/专业/企业版
- **30+ community PRs merged** — 来自 6 种语言的 30 位贡献者提交合并
- **978 internal tests** — Agent、技能、命令、Hooks（钩子）和规则的验证套件扩展

### v1.4.1 — Bug Fix (Feb 2026)

- **Fixed instinct import content loss** — `parse_instinct_file()` 在 `/instinct-import` 期间静默丢弃了 frontmatter（Action、Evidence、Examples 部分）之后的所有内容。([#148](https://github.com/affaan-m/everything-claude-code/issues/148), [#161](https://github.com/affaan-m/everything-claude-code/pull/161))

### v1.4.0 — Multi-Language Rules, Installation Wizard & PM2 (Feb 2026)

- **Interactive installation wizard** — 新增 `configure-ecc` 技能，提供带合并/覆盖检测的引导式安装
- **PM2 & multi-agent orchestration** — 6 个新命令（`/pm2`、`/multi-plan`、`/multi-execute`、`/multi-backend`、`/multi-frontend`、`/multi-workflow`）用于管理复杂的多服务工作流
- **Multi-language rules architecture** — 规则从扁平文件重构为 `common/` + `typescript/` + `python/` + `golang/` 目录。仅安装你需要的语言
- **Chinese (zh-CN) translations** — 所有 agents、commands、skills 和规则的完整翻译（80+ 个文件）
- **GitHub Sponsors support** — 通过 GitHub Sponsors 赞助该项目
- **Enhanced CONTRIBUTING.md** — 每种贡献类型的详细 PR 模板

### v1.3.0 — OpenCode Plugin Support (Feb 2026)

- **Full OpenCode integration** — 12 个 agents、24 个 commands、16 个 skills，通过 OpenCode 插件系统（20+ 事件类型）支持 Hooks
- **3 native custom tools** — run-tests, check-coverage, security-audit
- **LLM documentation** — `llms.txt` 提供全面的 OpenCode 文档

### v1.2.0 — Unified Commands & Skills (Feb 2026)

- **Python/Django support** — Django patterns、security、TDD 和 verification skills
- **Java Spring Boot skills** — Patterns、security、TDD 和 verification for Spring Boot
- **Session management** — `/sessions` 命令用于会话历史管理
- **Continuous learning v2** — 基于 Instinct（本能）的学习，支持置信度评分、导入/导出、演进

完整更新日志请参阅 [Releases](https://github.com/affaan-m/everything-claude-code/releases)。

---

## Quick Start（快速开始）

在 2 分钟内完成安装并运行：

### Pick one path only（仅选择一种路径）

大多数 Claude Code 用户应**恰好使用一种**安装路径：

- **推荐默认：** 安装 Claude Code 插件，然后仅复制你实际需要的规则文件夹。
- **仅在以下情况使用手动安装器：** 你想要更细粒度的控制、希望完全避开插件路径，或你的 Claude Code 版本在解析自托管市场条目时遇到问题。
- **不要叠加安装方法。** 最常见的损坏设置是：先执行 `/plugin install`，然后执行 `install.sh --profile full` 或 `npx ecc-install --profile full`。

如果你已经叠加了多次安装且内容重复，请直接跳转到 [Reset / Uninstall ECC](#reset--uninstall-ecc)。

### Low-context / no-hooks path（低上下文/无 Hooks 路径）

如果 Hooks（钩子）感觉过于全局化，或者你只需要 ECC 的规则、Agents、Commands 和核心工作流技能，请跳过插件并使用最小手动配置：

```bash
./install.sh --profile minimal --target claude
```

```powershell
.\install.ps1 --profile minimal --target claude
# or
npx ecc-install --profile minimal --target claude
```

此配置文件有意排除了 `hooks-runtime`。

如果你需要正常的核心配置但希望关闭 Hooks，请使用：

```bash
./install.sh --profile core --without baseline:hooks --target claude
```

仅当你需要运行时强制执行时才稍后添加 Hooks：

```bash
./install.sh --target claude --modules hooks-runtime
```

### Find the right components first（先找到合适的组件）

如果你不确定要安装哪个 ECC 配置文件或组件，可以从任何项目中询问内置顾问：

```bash
npx ecc consult "security reviews" --target claude
```

它将返回匹配的组件、相关配置和预览/安装命令。如果要在安装前检查确切的文件计划，请使用预览命令。

对于生产级 ML/MLOps 工作流，请保持安装为显式开启且按组件范围限定：

```bash
npx ecc consult "mlops training model deployment" --target claude
npx ecc install --profile minimal --target claude --with capability:machine-learning
```

### Step 1: Install the Plugin (Recommended)（步骤 1：安装插件（推荐））

> NOTE: The plugin is convenient, but the OSS installer below is still the most reliable path if your Claude Code build has trouble resolving self-hosted marketplace entries.

```bash
# Add marketplace
/plugin marketplace add https://github.com/affaan-m/everything-claude-code

# Install plugin
/plugin install ecc@ecc
```

### Naming + Migration Note（命名与迁移说明）

ECC 现在有三个公开标识符，它们不可互换：

- GitHub source repo: `affaan-m/everything-claude-code`
- Claude marketplace/plugin identifier: `ecc@ecc`
- npm package: `ecc-universal`

这是有意为之的。Anthropic 市场/插件安装由规范化的插件标识符键控，因此 ECC 使用 `ecc@ecc` 以保持工具名称和斜杠命令命名空间足够短以符合严格的桌面/API 验证器限制。较旧的帖子可能仍显示前一个长版市场标识符；请仅将其视为遗留别名。此外，npm 包保持为 `ecc-universal`，因此 npm 安装和市场安装故意使用不同的名称。

### Step 2: Install Rules Only If You Need Them（步骤 2：仅在需要时安装规则）

> WARNING: **Important:** Claude Code plugins cannot distribute `rules` automatically.
>
> If you already installed ECC via `/plugin install`, **do not run `./install.sh --profile full`, `.\install.ps1 --profile full`, or `npx ecc-install --profile full` afterward**. The plugin already loads ECC skills, commands, and hooks. Running the full installer after a plugin install copies those same surfaces into your user directories and can create duplicate skills plus duplicate runtime behavior.
>
> For plugin installs, manually copy only the `rules/` directories you want under `~/.claude/rules/ecc/`. Start with `rules/common` plus one language or framework pack you actually use. Do not copy every rules directory unless you explicitly want all of that context in Claude.
>
> Use the full installer only when you are doing a fully manual ECC install instead of the plugin path.
>
> If your local Claude setup was wiped or reset, that does not mean you need to repurchase ECC. Start with `node scripts/ecc.js list-installed`, then run `node scripts/ecc.js doctor` and `node scripts/ecc.js repair` before reinstalling anything. That usually restores ECC-managed files without rebuilding your setup. If the problem is account or marketplace access for ECC Tools, handle billing/account recovery separately.

```bash
# Clone the repo first
git clone https://github.com/affaan-m/everything-claude-code.git
cd everything-claude-code

# Install dependencies (pick your package manager)
npm install        # or: pnpm install | yarn install | bun install

# Plugin install path: copy only ECC rules into an ECC-owned namespace
mkdir -p ~/.claude/rules/ecc
cp -R rules/common ~/.claude/rules/ecc/
cp -R rules/typescript ~/.claude/rules/ecc/

# Fully manual ECC install path (use this instead of /plugin install)
# ./install.sh --profile full
```

```powershell
# Windows PowerShell

# Plugin install path: copy only ECC rules into an ECC-owned namespace
New-Item -ItemType Directory -Force -Path "$HOME/.claude/rules/ecc" | Out-Null
Copy-Item -Recurse rules/common "$HOME/.claude/rules/ecc/"
Copy-Item -Recurse rules/typescript "$HOME/.claude/rules/ecc/"

# Fully manual ECC install path (use this instead of /plugin install)
# .\install.ps1 --profile full
# npx ecc-install --profile full
```

手动安装说明请参阅 `rules/` 文件夹中的 README。当手动复制规则时，请复制整个语言目录（例如 `rules/common` 或 `rules/golang`），而不是其中的文件，以便相对引用继续正常工作且文件名不会冲突。

### Fully manual install (Fallback)（完全手动安装（备选））

仅在你有意跳过插件路径时使用：

```bash
./install.sh --profile full
```

```powershell
.\install.ps1 --profile full
# or
npx ecc-install --profile full
```

如果你选择此路径，到此为止。不要同时运行 `/plugin install`。

### Reset / Uninstall ECC（重置/卸载 ECC）

如果感觉 ECC 重复、侵入或损坏，请不要在其自身之上反复重新安装。

- **Plugin path：** 从 Claude Code 中移除插件，然后删除你手动复制到 `~/.claude/rules/ecc/` 下的特定规则文件夹。
- **Manual installer / CLI path：** 从仓库根目录预览卸载：

```bash
node scripts/uninstall.js --dry-run
```

然后移除 ECC 管理的文件：

```bash
node scripts/uninstall.js
```

你也可以使用生命周期包装器：

```bash
node scripts/ecc.js list-installed
node scripts/ecc.js doctor
node scripts/ecc.js repair
node scripts/ecc.js uninstall --dry-run
```

ECC 仅移除其安装状态中记录的文件。它不会删除未安装的无关文件。

如果你叠加了多种方法，请按以下顺序清理：

1. 移除 Claude Code 插件安装。
2. 从仓库根目录运行 ECC 卸载命令以移除由安装状态管理的文件。
3. 删除你手动复制且不再需要的任何额外规则文件夹。
4. 使用单一路径重新安装一次。

### Step 3: Start Using（步骤 3：开始使用）

```bash
# Skills are the primary workflow surface.
# Existing slash-style command names still work while ECC migrates off commands/.

# Plugin install uses the canonical namespaced form
/ecc:plan "Add user authentication"

# Manual install keeps the shorter slash form:
# /plan "Add user authentication"

# Check available commands
/plugin list ecc@ecc
```

**就是这样！** 你现在可以访问 60 个 agents、228 个 skills 和 75 个遗留命令适配器。

### Dashboard GUI（仪表盘图形界面）

启动桌面仪表盘以可视化探索 ECC 组件：

```bash
npm run dashboard
# or
python3 ./ecc_dashboard.py
```

**Features：**
- 标签页界面：Agents、Skills、Commands、Rules、Settings
- 深色/浅色主题切换
- 字体自定义（家族与大小）
- 页眉和任务栏中的项目 Logo
- 跨所有组件的搜索与过滤

### Multi-model commands require additional setup（多模型命令需要额外设置）

> WARNING: `multi-*` commands are **not** covered by the base plugin/rules install above.
>
> To use `/multi-plan`, `/multi-execute`, `/multi-backend`, `/multi-frontend`, and `/multi-workflow`, you must also install the `ccg-workflow` runtime.
>
> Initialize it with `npx ccg-workflow`.
>
> That runtime provides the external dependencies these commands expect, including:
> - `~/.claude/bin/codeagent-wrapper`
> - `~/.claude/.ccg/prompts/*`
>
> Without `ccg-workflow`, these `multi-*` commands will not run correctly.

---

## Cross-Platform Support（跨平台支持）

该插件现已全面支持 **Windows、macOS 和 Linux**，并与主要 IDE（Cursor、OpenCode、Antigravity）及 CLI 工具链紧密集成。所有 Hooks（钩子）和脚本均已重写为 Node.js 以实现最大兼容性。

### Package Manager Detection（包管理器检测）

该插件自动检测你首选的包管理器（npm、pnpm、yarn 或 bun），优先级如下：

1. **环境变量：** `CLAUDE_PACKAGE_MANAGER`
2. **项目配置：** `.claude/package-manager.json`
3. **package.json：** `packageManager` 字段
4. **锁文件：** 从 package-lock.json、yarn.lock、pnpm-lock.yaml 或 bun.lockb 检测
5. **全局配置：** `~/.claude/package-manager.json`
6. **回退：** 第一个可用的包管理器

设置你首选的包管理器：

```bash
# Via environment variable
export CLAUDE_PACKAGE_MANAGER=pnpm

# Via global config
node scripts/setup-package-manager.js --global pnpm

# Via project config
node scripts/setup-package-manager.js --project bun

# Detect current setting
node scripts/setup-package-manager.js --detect
```

或在 Claude Code 中使用 `/setup-pm` 命令。

### Hook Runtime Controls（Hook 运行时控制）

使用运行时标志调整严格程度或临时禁用特定 Hooks：

```bash
# Hook strictness profile (default: standard)
export ECC_HOOK_PROFILE=standard

# Comma-separated hook IDs to disable
export ECC_DISABLED_HOOKS="pre:bash:tmux-reminder,post:edit:typecheck"

# Cap SessionStart additional context (default: 8000 chars)
export ECC_SESSION_START_MAX_CHARS=4000

# Disable SessionStart additional context entirely for low-context/local-model setups
export ECC_SESSION_START_CONTEXT=off
```

---

## What's Inside（内部结构）

本仓库是一个 **Claude Code 插件** — 可直接安装或手动复制组件。

```
everything-claude-code/
|-- .claude-plugin/   # Plugin and marketplace manifests
|   |-- plugin.json         # Plugin metadata and component paths
|   |-- marketplace.json    # Marketplace catalog for /plugin marketplace add
|
|-- agents/           # 60 specialized subagents for delegation
|   |-- planner.md           # Feature implementation planning
|   |-- architect.md         # System design decisions
|   |-- tdd-guide.md         # Test-driven development
|   |-- code-reviewer.md     # Quality and security review
|   |-- security-reviewer.md # Vulnerability analysis
|   |-- build-error-resolver.md
|   |-- e2e-runner.md        # Playwright E2E testing
|   |-- refactor-cleaner.md  # Dead code cleanup
|   |-- doc-updater.md       # Documentation sync
|   |-- docs-lookup.md       # Documentation/API lookup
|   |-- chief-of-staff.md    # Communication triage and drafts
|   |-- loop-operator.md     # Autonomous loop execution
|   |-- harness-optimizer.md # Harness config tuning
|   |-- cpp-reviewer.md      # C++ code review
|   |-- cpp-build-resolver.md # C++ build error resolution
|   |-- fsharp-reviewer.md   # F# functional code review
|   |-- go-reviewer.md       # Go code review
|   |-- go-build-resolver.md # Go build error resolution
|   |-- python-reviewer.md   # Python code review
|   |-- database-reviewer.md # Database/Supabase review
|   |-- typescript-reviewer.md # TypeScript/JavaScript code review
|   |-- java-reviewer.md     # Java/Spring Boot code review
|   |-- java-build-resolver.md # Java/Maven/Gradle build errors
|   |-- kotlin-reviewer.md   # Kotlin/Android/KMP code review
|   |-- kotlin-build-resolver.md # Kotlin/Gradle build errors
|   |-- harmonyos-app-resolver.md # HarmonyOS/ArkTS app development
|   |-- rust-reviewer.md     # Rust code review
|   |-- rust-build-resolver.md # Rust build error resolution
|   |-- pytorch-build-resolver.md # PyTorch/CUDA training errors
|   |-- mle-reviewer.md      # Production ML pipeline, eval, serving, and monitoring review
|
|-- skills/           # Workflow definitions and domain knowledge
|   |-- coding-standards/           # Language best practices
|   |-- clickhouse-io/              # ClickHouse analytics, queries, data engineering
|   |-- backend-patterns/           # API, database, caching patterns
|   |-- frontend-patterns/          # React, Next.js patterns
|   |-- frontend-slides/            # HTML slide decks and PPTX-to-web presentation workflows (NEW)
|   |-- article-writing/            # Long-form writing in a supplied voice without generic AI tone (NEW)
|   |-- content-engine/             # Multi-platform social content and repurposing workflows (NEW)
|   |-- market-research/            # Source-attributed market, competitor, and investor research (NEW)
|   |-- investor-materials/         # Pitch decks, one-pagers, memos, and financial models (NEW)
|   |-- investor-outreach/          # Personalized fundraising outreach and follow-up (NEW)
|   |-- continuous-learning/        # Legacy v1 Stop-hook pattern extraction
|   |-- continuous-learning-v2/     # Instinct-based learning with confidence scoring
|   |-- iterative-retrieval/        # Progressive context refinement for subagents
|   |-- strategic-compact/          # Manual compaction suggestions (Longform Guide)
|   |-- tdd-workflow/               # TDD methodology
|   |-- security-review/            # Security checklist
|   |-- eval-harness/               # Verification loop evaluation (Longform Guide)
|   |-- verification-loop/          # Continuous verification (Longform Guide)
|   |-- videodb/                   # Video and audio: ingest, search, edit, generate, stream (NEW)
|   |-- golang-patterns/            # Go idioms and best practices
|   |-- golang-testing/             # Go testing patterns, TDD, benchmarks
|   |-- cpp-coding-standards/         # C++ coding standards from C++ Core Guidelines (NEW)
|   |-- cpp-testing/                # C++ testing with GoogleTest, CMake/CTest (NEW)
|   |-- django-patterns/            # Django patterns, models, views (NEW)
|   |-- django-security/            # Django security best practices (NEW)
|   |-- django-tdd/                 # Django TDD workflow (NEW)
|   |-- django-verification/        # Django verification loops (NEW)
|   |-- laravel-patterns/           # Laravel architecture patterns (NEW)
|   |-- laravel-security/           # Laravel security best practices (NEW)
|   |-- laravel-tdd/                # Laravel TDD workflow (NEW)
|   |-- laravel-verification/       # Laravel verification loops (NEW)
|   |-- python-patterns/            # Python idioms and best practices (NEW)
|   |-- python-testing/             # Python testing with pytest (NEW)
|   |-- quarkus-patterns/            # Java Quarkus patterns (NEW)
|   |-- quarkus-security/            # Quarkus security (NEW)
|   |-- quarkus-tdd/                 # Quarkus TDD (NEW)
|   |-- quarkus-verification/        # Quarkus verification (NEW)
|   |-- springboot-patterns/        # Java Spring Boot patterns (NEW)
|   |-- springboot-security/        # Spring Boot security (NEW)
|   |-- springboot-tdd/             # Spring Boot TDD (NEW)
|   |-- springboot-verification/    # Spring Boot verification (NEW)
|   |-- configure-ecc/              # Interactive installation wizard (NEW)
|   |-- security-scan/              # AgentShield security auditor integration (NEW)
|   |-- java-coding-standards/     # Java coding standards (NEW)
|   |-- jpa-patterns/              # JPA/Hibernate patterns (NEW)
|   |-- postgres-patterns/         # PostgreSQL optimization patterns (NEW)
|   |-- nutrient-document-processing/ # Document processing with Nutrient API (NEW)
|   |-- docs/examples/project-guidelines-template.md  # Template for project-specific skills
|   |-- database-migrations/         # Migration patterns (Prisma, Drizzle, Django, Go) (NEW)
|   |-- api-design/                  # REST API design, pagination, error responses (NEW)
|   |-- deployment-patterns/         # CI/CD, Docker, health checks, rollbacks (NEW)
|   |-- docker-patterns/            # Docker Compose, networking, volumes, container security (NEW)
|   |-- e2e-testing/                 # Playwright E2E patterns and Page Object Model (NEW)
|   |-- content-hash-cache-pattern/  # SHA-256 content hash caching for file processing (NEW)
|   |-- cost-aware-llm-pipeline/     # LLM cost optimization, model routing, budget tracking (NEW)
|   |-- regex-vs-llm-structured-text/ # Decision framework: regex vs LLM for text parsing (NEW)
|   |-- swift-actor-persistence/     # Thread-safe Swift data persistence with actors (NEW)
|   |-- swift-protocol-di-testing/   # Protocol-based DI for testable Swift code (NEW)
|   |-- search-first/               # Research-before-coding workflow (NEW)
|   |-- skill-stocktake/            # Audit skills and commands for quality (NEW)
|   |-- liquid-glass-design/         # iOS 26 Liquid Glass design system (NEW)
|   |-- foundation-models-on-device/ # Apple on-device LLM with FoundationModels (NEW)
|   |-- swift-concurrency-6-2/       # Swift 6.2 Approachable Concurrency (NEW)
|   |-- mle-workflow/               # Production ML data contracts, evals, deployment, monitoring (NEW)
|   |-- perl-patterns/             # Modern Perl 5.36+ idioms and best practices (NEW)
|   |-- perl-security/             # Perl security patterns, taint mode, safe I/O (NEW)
|   |-- perl-testing/              # Perl TDD with Test2::V0, prove, Devel::Cover (NEW)
|   |-- autonomous-loops/           # Autonomous loop patterns: sequential pipelines, PR loops, DAG orchestration (NEW)
|   |-- plankton-code-quality/      # Write-time code quality enforcement with Plankton hooks (NEW)
|
|-- commands/         # Maintained slash-entry compatibility; prefer skills/
|   |-- plan.md             # /plan - Implementation planning
|   |-- code-review.md      # /code-review - Quality review
|   |-- build-fix.md        # /build-fix - Fix build errors
|   |-- refactor-clean.md   # /refactor-clean - Dead code removal
|   |-- quality-gate.md     # /quality-gate - Verification gate
|   |-- learn.md            # /learn - Extract patterns mid-session (Longform Guide)
|   |-- learn-eval.md       # /learn-eval - Extract, evaluate, and save patterns (NEW)
|   |-- checkpoint.md       # /checkpoint - Save verification state (Longform Guide)
|   |-- setup-pm.md         # /setup-pm - Configure package manager
|   |-- go-review.md        # /go-review - Go code review (NEW)
|   |-- go-test.md          # /go-test - Go TDD workflow (NEW)
|   |-- go-build.md         # /go-build - Fix Go build errors (NEW)
|   |-- skill-create.md     # /skill-create - Generate skills from git history (NEW)
|   |-- instinct-status.md  # /instinct-status - View learned instincts (NEW)
|   |-- instinct-import.md  # /instinct-import - Import instincts (NEW)
|   |-- instinct-export.md  # /instinct-export - Export instincts (NEW)
|   |-- evolve.md           # /evolve - Cluster instincts into skills
|   |-- prune.md            # /prune - Delete expired pending instincts (NEW)
|   |-- pm2.md              # /pm2 - PM2 service lifecycle management (NEW)
|   |-- multi-plan.md       # /multi-plan - Multi-agent task decomposition (NEW)
|   |-- multi-execute.md    # /multi-execute - Orchestrated multi-agent workflows (NEW)
|   |-- multi-backend.md    # /multi-backend - Backend multi-service orchestration (NEW)
|   |-- multi-frontend.md   # /multi-frontend - Frontend multi-service orchestration (NEW)
|   |-- multi-workflow.md   # /multi-workflow - General multi-service workflows (NEW)
|   |-- sessions.md         # /sessions - Session history management
|   |-- test-coverage.md    # /test-coverage - Test coverage analysis
|   |-- update-docs.md      # /update-docs - Update documentation
|   |-- update-codemaps.md  # /update-codemaps - Update codemaps
|   |-- python-review.md    # /python-review - Python code review (NEW)
|-- legacy-command-shims/   # Opt-in archive for retired shims such as /tdd and /eval
|   |-- tdd.md              # /tdd - Prefer the tdd-workflow skill
|   |-- e2e.md              # /e2e - Prefer the e2e-testing skill
|   |-- eval.md             # /eval - Prefer the eval-harness skill
|   |-- verify.md           # /verify - Prefer the verification-loop skill
|   |-- orchestrate.md      # /orchestrate - Prefer dmux-workflows or multi-workflow
|
|-- rules/            # Always-follow guidelines (copy to ~/.claude/rules/ecc/)
|   |-- README.md            # Structure overview and installation guide
|   |-- common/              # Language-agnostic principles
|   |   |-- coding-style.md    # Immutability, file organization
|   |   |-- git-workflow.md    # Commit format, PR process
|   |   |-- testing.md         # TDD, 80% coverage requirement
|   |   |-- performance.md     # Model selection, context management
|   |   |-- patterns.md        # Design patterns, skeleton projects
|   |   |-- hooks.md           # Hook architecture, TodoWrite
|   |   |-- agents.md          # When to delegate to subagents
|   |   |-- security.md        # Mandatory security checks
|   |-- typescript/          # TypeScript/JavaScript specific
|   |-- python/              # Python specific
|   |-- golang/              # Go specific
|   |-- swift/               # Swift specific
|   |-- php/                 # PHP specific (NEW)
|   |-- arkts/               # HarmonyOS / ArkTS specific
|
|-- hooks/            # Trigger-based automations
|   |-- README.md                 # Hook documentation, recipes, and customization guide
|   |-- hooks.json                # All hooks config (PreToolUse, PostToolUse, Stop, etc.)
|   |-- memory-persistence/       # Session lifecycle hooks (Longform Guide)
|   |-- strategic-compact/        # Compaction suggestions (Longform Guide)
|
|-- scripts/          # Cross-platform Node.js scripts (NEW)
|   |-- lib/                     # Shared utilities
|   |   |-- utils.js             # Cross-platform file/path/system utilities
|   |   |-- package-manager.js   # Package manager detection and selection
|   |-- hooks/                   # Hook implementations
|   |   |-- session-start.js     # Load context on session start
|   |   |-- session-end.js       # Save state on session end
|   |   |-- pre-compact.js       # Pre-compaction state saving
|   |   |-- suggest-compact.js   # Strategic compaction suggestions
|   |   |-- evaluate-session.js  # Extract patterns from sessions
|   |-- setup-package-manager.js # Interactive PM setup
|
|-- tests/            # Test suite (NEW)
|   |-- lib/                     # Library tests
|   |-- hooks/                   # Hook tests
|   |-- run-all.js               # Run all tests
|
|-- contexts/         # Dynamic system prompt injection contexts (Longform Guide)
|   |-- dev.md              # Development mode context
|   |-- review.md           # Code review mode context
|   |-- research.md         # Research/exploration mode context
|
|-- examples/         # Example configurations and sessions
|   |-- CLAUDE.md             # Example project-level config
|   |-- user-CLAUDE.md        # Example user-level config
|   |-- saas-nextjs-CLAUDE.md   # Real-world SaaS (Next.js + Supabase + Stripe)
|   |-- go-microservice-CLAUDE.md # Real-world Go microservice (gRPC + PostgreSQL)
|   |-- django-api-CLAUDE.md      # Real-world Django REST API (DRF + Celery)
|   |-- laravel-api-CLAUDE.md     # Real-world Laravel API (PostgreSQL + Redis) (NEW)
|   |-- rust-api-CLAUDE.md        # Real-world Rust API (Axum + SQLx + PostgreSQL) (NEW)
|
|-- mcp-configs/      # MCP server configurations
|   |-- mcp-servers.json    # GitHub, Supabase, Vercel, Railway, etc.
|
|-- ecc_dashboard.py  # Desktop GUI dashboard (Tkinter)
|
|-- assets/           # Assets for dashboard
|   |-- images/
|       |-- ecc-logo.png
|
|-- marketplace.json  # Self-hosted marketplace config (for /plugin marketplace add)
```

---

## Ecosystem Tools（生态系统工具）

### Skill Creator（技能创建器）

两种从你的仓库生成 Claude Code 技能的方法：

#### Option A: Local Analysis (Built-in)（选项 A：本地分析（内置））

使用 `/skill-create` 命令进行无需外部服务的本地分析：

```bash
/skill-create                    # Analyze current repo
/skill-create --instincts        # Also generate instincts for continuous-learning-v2
```

这会在本地分析你的 git 历史并生成 SKILL.md 文件。

#### Option B: GitHub App (Advanced)（选项 B：GitHub App（高级））

用于高级功能（10k+ commits、自动 PR、团队共享）：

[Install GitHub App](https://github.com/apps/skill-creator) | [ecc.tools](https://ecc.tools)

```bash
# Comment on any issue:
/skill-creator analyze

# Or auto-triggers on push to default branch
```

两种选项均创建：
- **SKILL.md files** - 即插即用的 Claude Code 技能
- **Instinct collections** - 用于 continuous-learning-v2
- **Pattern extraction** - 从你的提交历史中学习

### AgentShield — Security Auditor（安全审计器）

> Built at the Claude Code Hackathon (Cerebral Valley x Anthropic, Feb 2026). 1282 tests, 98% coverage, 102 static analysis rules.

扫描你的 Claude Code 配置中的漏洞、错误配置和注入风险。

```bash
# Quick scan (no install needed)
npx ecc-agentshield scan

# Auto-fix safe issues
npx ecc-agentshield scan --fix

# Deep analysis with three Opus 4.6 agents
npx ecc-agentshield scan --opus --stream

# Generate secure config from scratch
npx ecc-agentshield init
```

**What it scans：** CLAUDE.md、settings.json、MCP configs、hooks、agent definitions，以及 skills（5 个类别）— 密钥检测（14 种模式）、权限审计、Hook 注入分析、MCP server 风险画像和 Agent 配置审查。

**The `--opus` flag** — 在红队/蓝队/审计员管道中运行三个 Claude Opus 4.6 agents。攻击者寻找利用链，防御者评估保护措施，审计员综合两者生成优先级风险评估。这是对抗性推理，而不仅仅是模式匹配。

**Output formats：** Terminal（A-F 分级着色）、JSON（CI pipelines）、Markdown、HTML。严重发现时退出码为 2 以用于构建门禁。

在 Claude Code 中使用 `/security-scan` 运行它，或通过 [GitHub Action](https://github.com/affaan-m/agentshield) 添加到 CI。

[GitHub](https://github.com/affaan-m/agentshield) | [npm](https://www.npmjs.com/package/ecc-agentshield)

### Continuous Learning v2（持续学习 v2）

基于 Instinct（本能）的学习系统会自动学习你的模式：

```bash
/instinct-status        # Show learned instincts with confidence
/instinct-import <file> # Import instincts from others
/instinct-export        # Export your instincts for sharing
/evolve                 # Cluster related instincts into skills
```

完整文档请参阅 `skills/continuous-learning-v2/`。
仅当你明确需要遗留 v1 Stop-hook 已学技能流时才保留 `continuous-learning/`。

---

## Requirements（要求）

### Claude Code CLI Version（Claude Code CLI 版本）

**最低版本：v2.1.0 或更高**

由于插件系统处理 Hooks（钩子）的方式发生变化，此插件需要 Claude Code CLI v2.1.0+。

检查你的版本：
```bash
claude --version
```

### Important: Hooks Auto-Loading Behavior（重要提示：Hooks 自动加载行为）

> WARNING: **For Contributors:** Do NOT add a `"hooks"` field to `.claude-plugin/plugin.json`. This is enforced by a regression test.

Claude Code v2.1+ **会自动加载** 任何已安装插件中的 `hooks/hooks.json`。在 `plugin.json` 中显式声明会导致重复检测错误：

```
Duplicate hooks file detected: ./hooks/hooks.json resolves to already-loaded file
```

**History：** 这导致本仓库反复出现修复/回滚周期（[#29](https://github.com/affaan-m/everything-claude-code/issues/29)、[#52](https://github.com/affaan-m/everything-claude-code/issues/52)、[#103](https://github.com/affaan-m/everything-claude-code/issues/103)）。行为在 Claude Code 版本之间发生变化，导致混淆。我们现在有回归测试来防止此问题再次出现。

---

## Installation（安装）

### Option 1: Install as Plugin (Recommended)（选项 1：作为插件安装（推荐））

使用本仓库的最简单方式 - 作为 Claude Code 插件安装：

```bash
# Add this repo as a marketplace
/plugin marketplace add https://github.com/affaan-m/everything-claude-code

# Install the plugin
/plugin install ecc@ecc
```

或直接添加到你的 `~/.claude/settings.json`：

```json
{
  "extraKnownMarketplaces": {
    "ecc": {
      "source": {
        "source": "github",
        "repo": "affaan-m/everything-claude-code"
      }
    }
  },
  "enabledPlugins": {
    "ecc@ecc": true
  }
}
```

这将使你立即访问所有 commands、agents、skills 和 hooks。

> **Note:** The Claude Code plugin system does not support distributing `rules` via plugins ([upstream limitation](https://code.claude.com/docs/en/plugins-reference)). You need to install rules manually:
>
> ```bash
> # Clone the repo first
> git clone https://github.com/affaan-m/everything-claude-code.git
>
> # Option A: User-level rules (applies to all projects)
> mkdir -p ~/.claude/rules/ecc
> cp -r everything-claude-code/rules/common ~/.claude/rules/ecc/
> cp -r everything-claude-code/rules/typescript ~/.claude/rules/ecc/   # pick your stack
> cp -r everything-claude-code/rules/python ~/.claude/rules/ecc/
> cp -r everything-claude-code/rules/golang ~/.claude/rules/ecc/
> cp -r everything-claude-code/rules/php ~/.claude/rules/ecc/
>
> # Option B: Project-level rules (applies to current project only)
> mkdir -p .claude/rules/ecc
> cp -r everything-claude-code/rules/common .claude/rules/ecc/
> cp -r everything-claude-code/rules/typescript .claude/rules/ecc/     # pick your stack
> ```

---

### Option 2: Manual Installation（选项 2：手动安装）

如果你更喜欢对安装内容进行手动控制：

```bash
# Clone the repo
git clone https://github.com/affaan-m/everything-claude-code.git

# Copy agents to your Claude config
cp everything-claude-code/agents/*.md ~/.claude/agents/

# Copy rules directories (common + language-specific)
mkdir -p ~/.claude/rules/ecc
cp -r everything-claude-code/rules/common ~/.claude/rules/ecc/
cp -r everything-claude-code/rules/typescript ~/.claude/rules/ecc/   # pick your stack
cp -r everything-claude-code/rules/python ~/.claude/rules/ecc/
cp -r everything-claude-code/rules/golang ~/.claude/rules/ecc/
cp -r everything-claude-code/rules/php ~/.claude/rules/ecc/
cp -r everything-claude-code/rules/arkts ~/.claude/rules/ecc/

# Copy skills first (primary workflow surface)
# Recommended (new users): core/general skills only
mkdir -p ~/.claude/skills/ecc
cp -r everything-claude-code/.agents/skills/* ~/.claude/skills/ecc/
cp -r everything-claude-code/skills/search-first ~/.claude/skills/ecc/

# Optional: add niche/framework-specific skills only when needed
# for s in django-patterns django-tdd laravel-patterns springboot-patterns quarkus-patterns; do
# cp -r everything-claude-code/skills/$s ~/.claude/skills/ecc/
# done

# Optional: keep maintained slash-command compatibility during migration
mkdir -p ~/.claude/commands
cp everything-claude-code/commands/*.md ~/.claude/commands/

# Retired shims live in legacy-command-shims/commands/.
# Copy individual files from there only if you still need old names such as /tdd.
```

#### Install hooks（安装 Hooks）

不要将原始仓库 `hooks/hooks.json` 复制到 `~/.claude/settings.json` 或 `~/.claude/hooks/hooks.json`。该文件面向插件/仓库，旨在通过 ECC 安装器安装或作为插件加载，因此直接复制不是受支持的手动安装路径。

使用安装器仅安装 Claude Hook（钩子）运行时，以便正确重写命令路径：

```bash
# macOS / Linux
bash ./install.sh --target claude --modules hooks-runtime
```

```powershell
# Windows PowerShell
pwsh -File .\install.ps1 --target claude --modules hooks-runtime
```

这会将解析后的 Hooks 写入 `~/.claude/hooks/hooks.json`，并保留任何现有的 `~/.claude/settings.json` 不变。

如果你通过 `/plugin install` 安装了 ECC，请勿将这些 Hooks 复制到 settings.json。Claude Code v2.1+ 已自动加载插件 `hooks/hooks.json`，在 `settings.json` 中重复它们会导致重复执行和跨平台 Hook（钩子）冲突。

Windows 注意：Claude 配置目录是 `%USERPROFILE%\\.claude`，而不是 `~/claude`。

#### Configure MCPs（配置 MCP）

Claude 插件安装故意不自动启用 ECC 的捆绑 MCP server definitions。这避免了在严格的第三方网关上使用过长的插件 MCP 工具名称，同时保留手动 MCP 设置可用。

使用 Claude Code 的 `/mcp` 命令或 CLI 管理的 MCP 设置进行实时 Claude Code 服务器更改。对 Claude Code 运行时禁用使用 `/mcp`；Claude Code 会将这些选择持久化到 `~/.claude.json` 中。

对于仓库本地 MCP 访问，将所需的 MCP server definitions 从 `mcp-configs/mcp-servers.json` 复制到项目范围的 `.mcp.json` 中。

如果你已经运行自己的 ECC 捆绑 MCP 副本，请设置：

```bash
export ECC_DISABLED_MCPS="github,context7,exa,playwright,sequential-thinking,memory"
```

ECC 管理的安装和 Codex 同步流程将跳过或移除这些捆绑服务器，而不是重新添加重复项。`ECC_DISABLED_MCPS` 是 ECC 安装/同步过滤器，而非实时 Claude Code 开关。

**Important：** 请将 `YOUR_*_HERE` 占位符替换为你实际的 API keys。

---

## Key Concepts（核心概念）

### Agents（代理）

Subagents（子代理）处理具有有限范围的委托任务。示例：

```markdown
---
name: code-reviewer
description: Reviews code for quality, security, and maintainability
tools: ["Read", "Grep", "Glob", "Bash"]
model: opus
---

You are a senior code reviewer...
```

### Skills（技能）

Skills 是主要的工作流表面。它们可以直接调用、自动建议，并被 agents 复用。ECC 在迁移期间仍提供维护的 `commands/`，而退休的短名称适配器仅存在于 `legacy-command-shims/` 中以供显式启用。新工作流开发应首先落地于 `skills/`。

```markdown
# TDD Workflow

1. Define interfaces first
2. Write failing tests (RED)
3. Implement minimal code (GREEN)
4. Refactor (IMPROVE)
5. Verify 80%+ coverage
```

### Hooks（钩子）

Hooks 在工具事件触发时执行。示例 - 警告 console.log：

```json
{
  "matcher": "tool == \"Edit\" && tool_input.file_path matches \"\\\\.(ts|tsx|js|jsx)$\"",
  "hooks": [{
    "type": "command",
    "command": "#!/bin/bash\ngrep -n 'console\\.log' \"$file_path\" && echo '[Hook] Remove console.log' >&2"
  }]
}
```

### Rules（规则）

Rules 是始终遵循的指南，组织为 `common/`（语言无关）+ 特定语言目录：

```
rules/
  common/          # Universal principles (always install)
  typescript/      # TS/JS specific patterns and tools
  python/          # Python specific patterns and tools
  golang/          # Go specific patterns and tools
  swift/           # Swift specific patterns and tools
  php/             # PHP specific patterns and tools
  arkts/           # HarmonyOS / ArkTS patterns and constraints
```

安装和结构详情请参阅 [`rules/README.md`](rules/README.md)。

---

## Which Agent Should I Use?（我应该使用哪个 Agent？）

不确定从哪里开始？使用此快速参考。Skills 是规范化的工作流表面；维护的斜杠入口为命令优先的工作流程保留可用。

| I want to... | Use this surface | Agent used |
|--------------|-----------------|------------|
| Plan a new feature | `/ecc:plan "Add auth"` | planner |
| Design system architecture | `/ecc:plan` + architect agent | architect |
| Write code with tests first | `tdd-workflow` skill | tdd-guide |
| Review code I just wrote | `/code-review` | code-reviewer |
| Fix a failing build | `/build-fix` | build-error-resolver |
| Run end-to-end tests | `e2e-testing` skill | e2e-runner |
| Find security vulnerabilities | `/security-scan` | security-reviewer |
| Remove dead code | `/refactor-clean` | refactor-cleaner |
| Update documentation | `/update-docs` | doc-updater |
| Review Go code | `/go-review` | go-reviewer |
| Review Python code | `/python-review` | python-reviewer |
| Review F# code | *(invoke `fsharp-reviewer` directly)* | fsharp-reviewer |
| Review TypeScript/JavaScript code | *(invoke `typescript-reviewer` directly)* | typescript-reviewer |
| Develop HarmonyOS apps | *(invoke `harmonyos-app-resolver` directly)* | harmonyos-app-resolver |
| Audit database queries | *(auto-delegated)* | database-reviewer |
| Review production ML changes | `mle-workflow` skill + `mle-reviewer` agent | mle-reviewer |

### Common Workflows（常见工作流）

斜杠形式仅在它们仍属于维护的命令表面时显示。退休的短名称适配器如 `/tdd` 和 `/eval` 仅存在于 `legacy-command-shims/` 中以供显式启用。

**Starting a new feature：**
```
/ecc:plan "Add user authentication with OAuth"
                                              → planner creates implementation blueprint
tdd-workflow skill                            → tdd-guide enforces write-tests-first
/code-review                                  → code-reviewer checks your work
```

**Fixing a bug：**
```
tdd-workflow skill                            → tdd-guide: write a failing test that reproduces it
                                              → implement the fix, verify test passes
/code-review                                  → code-reviewer: catch regressions
```

**Preparing for production：**
```
/security-scan                                → security-reviewer: OWASP Top 10 audit
e2e-testing skill                             → e2e-runner: critical user flow tests
/test-coverage                                → verify 80%+ coverage
```

---

## FAQ（常见问题）

<details>
<summary><b>How do I check which agents/commands are installed?</b></summary>

```bash
/plugin list ecc@ecc
```

This shows all available agents, commands, and skills from the plugin.
</details>

<details>
<summary><b>My hooks aren't working / I see "Duplicate hooks file" errors</b></summary>

这是最常见的问题。**请勿**向 `.claude-plugin/plugin.json` 添加 `"hooks"` 字段。Claude Code v2.1+ 会自动加载已安装插件中的 `hooks/hooks.json`。显式声明会导致重复检测错误。请参阅 [#29](https://github.com/affaan-m/everything-claude-code/issues/29)、[#52](https://github.com/affaan-m/everything-claude-code/issues/52)、[#103](https://github.com/affaan-m/everything-claude-code/issues/103)。
</details>

<details>
<summary><b>Can I use ECC with Claude Code on a custom API endpoint or model gateway?</b></summary>

可以。ECC 不会硬编码 Anthropic-hosted transport settings。它通过 Claude Code 的正常 CLI/plugin surface 在本地运行，因此适用于：

- Anthropic-hosted Claude Code
- 使用 `ANTHROPIC_BASE_URL` 和 `ANTHROPIC_AUTH_TOKEN` 的官方 Claude Code gateway setups
- 兼容的自定义 endpoints（支持 Anthropic API Claude Code 期望的协议）

最小示例：

```bash
export ANTHROPIC_BASE_URL=https://your-gateway.example.com
export ANTHROPIC_AUTH_TOKEN=your-token
claude
```

如果你的网关 remaps model names，请在 Claude Code 中配置此设置，而不是在 ECC 中。一旦 `claude` CLI 已正常工作，ECC 的 hooks、skills、commands 和 rules 与 model-provider（模型提供商）无关。

官方参考：
- [Claude Code LLM gateway docs](https://docs.anthropic.com/en/docs/claude-code/llm-gateway)
- [Claude Code model configuration docs](https://docs.anthropic.com/en/docs/claude-code/model-config)

</details>

<details>
<summary><b>My context window is shrinking / Claude is running out of context</b></summary>

过多的 MCP servers 会消耗你的上下文。每个 MCP tool description 都会从你的 200k 窗口中占用 tokens，可能将其减少到约 70k。SessionStart context 默认限制为 8000 个字符；对于本地模型或低上下文设置，可通过 `ECC_SESSION_START_MAX_CHARS=4000` 降低它，或通过 `ECC_SESSION_START_CONTEXT=off` 禁用它。

**Fix：** 使用 `/mcp` 从 Claude Code 中禁用未使用的 MCPs。Claude Code 会将这些运行时选择写入 `~/.claude.json`；`.claude/settings.json` 和 `.claude/settings.local.json` 对于已加载的 MCP servers 不是可靠的开关。

保持启用不超过 10 个 MCPs，活跃工具不超过 80 个。
</details>

<details>
<summary><b>Can I use only some components (e.g., just agents)?</b></summary>

可以。使用选项 2（手动安装）并仅复制你需要的内容：

```bash
# Just agents
cp everything-claude-code/agents/*.md ~/.claude/agents/

# Just rules
mkdir -p ~/.claude/rules/ecc/
cp -r everything-claude-code/rules/common ~/.claude/rules/ecc/
```

每个组件完全独立。
</details>

<details>
<summary><b>Does this work with Cursor / OpenCode / Codex / Antigravity / GitHub Copilot?</b></summary>

可以。ECC 是跨平台的：
- **Cursor**：`.cursor/` 中的预翻译配置。请参阅 [Cursor IDE Support](#cursor-ide-support)。
- **Gemini CLI**：通过 `.gemini/GEMINI.md` 和共享安装器管道的实验性项目本地支持。
- **OpenCode**：`.opencode/` 中的完整插件支持。请参阅 [OpenCode Support](#opencode-support)。
- **Codex**：对 macOS app 和 CLI 的一流支持，带有适配器漂移守卫和 SessionStart 回退。请参阅 PR [#257](https://github.com/affaan-m/everything-claude-code/pull/257)。
- **GitHub Copilot (VS Code)**：通过 `.github/copilot-instructions.md`、`.vscode/settings.json` 和 `.github/prompts/` 的指令和提示层。请参阅 [GitHub Copilot Support](#github-copilot-support)。
- **Antigravity**：为工作流、技能和扁平化规则在 `.agent/` 中紧密集成设置。请参阅 [Antigravity Guide](docs/ANTIGRAVITY-GUIDE.md)。
- **JoyCode / CodeBuddy**：命令、agents、skills 和扁平化规则的 project-local 选择性安装适配器。请参阅 [JoyCode Adapter Guide](docs/JOYCODE-GUIDE.md)。
- **Qwen CLI**：commands、agents、skills、rules 和 Qwen 配置的 home-directory 选择性安装适配器。请参阅 [Qwen CLI Adapter Guide](docs/QWEN-GUIDE.md)。
- **Non-native harnesses**：Grok 及类似接口的 manual fallback path。请参阅 [Manual Adaptation Guide](docs/MANUAL-ADAPTATION-GUIDE.md)。
- **Claude Code**：Native — 这是主要目标。
</details>

<details>
<summary><b>How do I contribute a new skill or agent?</b></summary>

请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。简短版本：
1. Fork the repo
2. Create your skill in `skills/your-skill-name/SKILL.md` (with YAML frontmatter)
3. Or create an agent in `agents/your-agent.md`
4. Submit a PR with a clear description of what it does and when to use it
</details>

---

## Running Tests（运行测试）

该插件包含全面的测试套件：

```bash
# Run all tests
node tests/run-all.js

# Run individual test files
node tests/lib/utils.test.js
node tests/lib/package-manager.test.js
node tests/hooks/hooks.test.js
```

---

## Contributing（贡献）

**欢迎并鼓励贡献。**

本仓库旨在成为社区资源。如果你有：
- 有用的 agents 或 skills
- 巧妙的 hooks
- 更好的 MCP configurations
- 改进的 rules

请贡献！请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 获取指南。

### Ideas for Contributions（贡献想法）

- Language-specific skills (Rust, C#, Kotlin, Java) — Go、Python、Perl、Swift、TypeScript 和 HarmonyOS/ArkTS 已包含
- Framework-specific configs (Rails, FastAPI) — Django、NestJS、Spring Boot 和 Laravel 已包含
- DevOps agents (Kubernetes, Terraform, AWS, Docker)
- Testing strategies (different frameworks, visual regression)
- Domain-specific knowledge (ML, data engineering, mobile)

### Community Ecosystem Notes（生态系统备注）

这些不与 ECC 捆绑，也不由本仓库审计，但如果你正在探索更广泛的 Claude Code skills 生态系统，它们值得了解：

- [claude-seo](https://github.com/AgriciDaniel/claude-seo) — SEO-focused skill and agent collection
- [claude-ads](https://github.com/AgriciDaniel/claude-ads) — Ad-audit and paid-growth workflow collection
- [claude-cybersecurity](https://github.com/AgriciDaniel/claude-cybersecurity) — Security-oriented skill and agent collection

---

## Cursor IDE Support（Cursor IDE 支持）

ECC 提供适用于 Cursor IDE 的支持，Hooks、Rules、Agents、Skills、Commands 和 MCP configs 已针对 Cursor 的项目布局进行了适配。

### Quick Start (Cursor)（快速开始（Cursor））

```bash
# macOS/Linux
./install.sh --target cursor typescript
./install.sh --target cursor python golang swift php
```

```powershell
# Windows PowerShell
.\install.ps1 --target cursor typescript
.\install.ps1 --target cursor python golang swift php
```

### What's Included（包含内容）

| Component | Count | Details |
|-----------|-------|---------|
| Hook Events | 15 | sessionStart, beforeShellExecution, afterFileEdit, beforeMCPExecution, beforeSubmitPrompt, and 10 more |
| Hook Scripts | 16 | Thin Node.js scripts delegating to `scripts/hooks/` via shared adapter |
| Rules | 34 | 9 common (alwaysApply) + 25 language-specific (TypeScript, Python, Go, Swift, PHP) |
| Agents | 48 | `.cursor/agents/ecc-*.md` when installed; prefixed to avoid collisions with user or marketplace agents |
| Skills | Shared + Bundled | `.cursor/skills/` for translated additions |
| Commands | Shared | `.cursor/commands/` if installed |
| MCP Config | Shared | `.cursor/mcp.json` if installed |

### Cursor Loading Notes（Cursor 加载备注）

ECC 不会将根 `AGENTS.md` 安装到 `.cursor/`。Cursor 将嵌套的 `AGENTS.md` 文件视为目录上下文，因此将 ECC 的仓库身份复制到主机项目中会污染该项目。

Cursor-native loading behavior can vary by Cursor build. ECC installs agents as `.cursor/agents/ecc-*.md`; if your Cursor build does not expose project agents, those files still work as explicit reference definitions instead of hidden global prompt context.

### Hook Architecture (DRY Adapter Pattern)（Hook 架构（DRY 适配器模式））

Cursor 拥有**比 Claude Code 更多的 hook events**（20 vs 8）。`.cursor/hooks/adapter.js` 模块将 Cursor 的 stdin JSON 转换为 Claude Code 格式，允许现有的 `scripts/hooks/*.js` 被复用而无需重复。

```
Cursor stdin JSON → adapter.js → transforms → scripts/hooks/*.js
                                              (shared with Claude Code)
```

Key hooks：
- **beforeShellExecution** — Blocks dev servers outside tmux (exit 2), git push review
- **afterFileEdit** — Auto-format + TypeScript check + console.log warning
- **beforeSubmitPrompt** — Detects secrets (sk-, ghp_, AKIA patterns) in prompts
- **beforeTabFileRead** — Blocks Tab from reading .env, .key, .pem files (exit 2)
- **beforeMCPExecution / afterMCPExecution** — MCP audit logging

### Rules Format（规则格式）

Cursor rules use YAML frontmatter with `description`, `globs`, and `alwaysApply`:

```yaml
---
description: "TypeScript coding style extending common rules"
globs: ["**/*.ts", "**/*.tsx", "**/*.js", "**/*.jsx"]
alwaysApply: false
---
```

---

## Codex macOS App + CLI Support（Codex macOS 应用 + CLI 支持）

ECC 为 macOS app 和 CLI 提供 **一流的 Codex 支持**，包含参考配置、Codex 特定的 AGENTS.md supplement 和共享 skills。

### Quick Start (Codex App + CLI)（快速开始（Codex 应用 + CLI））

```bash
# Run Codex CLI in the repo — AGENTS.md and .codex/ are auto-detected
codex

# Automatic setup: sync ECC assets (AGENTS.md, skills, MCP servers) into ~/.codex
npm install && bash scripts/sync-ecc-to-codex.sh
# or: pnpm install && bash scripts/sync-ecc-to-codex.sh
# or: yarn install && bash scripts/sync-ecc-to-codex.sh
# or: bun install && bash scripts/sync-ecc-to-codex.sh

# Or manually: copy the reference config to your home directory
cp .codex/config.toml ~/.codex/config.toml
```

同步脚本使用 **add-only** 策略安全地将 ECC MCP servers 合并到你现有的 `~/.codex/config.toml` 中 — 它永远不会移除或修改你现有的服务器。运行 `--dry-run` 预览更改，或 `--update-mcp` 强制刷新 ECC servers 到最新的推荐配置。

对于 Context7，ECC 使用规范的 Codex section name `[mcp_servers.context7]`，同时仍启动 `@upstash/context7-mcp` package。如果你已经有遗留的 `[mcp_servers.context7-mcp]` entry，`--update-mcp` 会将其迁移到规范 section name。

Codex macOS app：
- Open this repository as your workspace.
- The root `AGENTS.md` is auto-detected.
- `.codex/config.toml` and `.codex/agents/*.toml` work best when kept project-local.
- The reference `.codex/config.toml` intentionally does not pin `model` or `model_provider`, so Codex uses its own current default unless you override it.
- Optional: copy `.codex/config.toml` to `~/.codex/config.toml` for global defaults; keep the multi-agent role files project-local unless you also copy `.codex/agents/`.

### What's Included（包含内容）

| Component | Count | Details |
|-----------|-------|---------|
| Config | 1 | `.codex/config.toml` — top-level approvals/sandbox/web_search, MCP servers, notifications, profiles |
| AGENTS.md | 2 | Root (universal) + `.codex/AGENTS.md` (Codex-specific supplement) |
| Skills | 32 | `.agents/skills/` — SKILL.md + agents/openai.yaml per skill |
| MCP Servers | 6 | GitHub, Context7, Exa, Memory, Playwright, Sequential Thinking (7 with Supabase via `--update-mcp` sync) |
| Profiles | 2 | `strict` (read-only sandbox) and `yolo` (full auto-approve) |
| Agent Roles | 3 | `.codex/agents/` — explorer, reviewer, docs-researcher |

### Skills（技能）

位于 `.agents/skills/` 的 skills 由 Codex 自动加载：

Canonical Anthropic skills such as `claude-api`, `frontend-design`, and `skill-creator` are intentionally not re-bundled here. Install those from [`anthropics/skills`](https://github.com/anthropics/skills) when you want the official versions.

| Skill | Description |
|-------|-------------|
| agent-introspection-debugging | Debug agent behavior, routing, and prompt boundaries |
| agent-sort | Sort agent catalogs and assignment surfaces |
| api-design | REST API design patterns |
| article-writing | Long-form writing from notes and voice references |
| backend-patterns | API design, database, caching |
| brand-voice | Source-derived writing style profiles from real content |
| bun-runtime | Bun as runtime, package manager, bundler, and test runner |
| coding-standards | Universal coding standards |
| content-engine | Platform-native social content and repurposing |
| crosspost | Multi-platform content distribution across X, LinkedIn, Threads |
| deep-research | Multi-source research with synthesis and source attribution |
| dmux-workflows | Multi-agent orchestration using tmux pane manager |
| documentation-lookup | Up-to-date library and framework docs via Context7 MCP |
| e2e-testing | Playwright E2E tests |
| eval-harness | Eval-driven development |
| everything-claude-code | Development conventions and patterns for the project |
| exa-search | Neural search via Exa MCP for web, code, company research |
| fal-ai-media | Unified media generation for images, video, and audio |
| frontend-patterns | React/Next.js patterns |
| frontend-slides | HTML presentations, PPTX conversion, visual style exploration |
| investor-materials | Decks, memos, models, and one-pagers |
| investor-outreach | Personalized outreach, follow-ups, and intro blurbs |
| market-research | Source-attributed market and competitor research |
| mcp-server-patterns | Build MCP servers with Node/TypeScript SDK |
| nextjs-turbopack | Next.js 16+ and Turbopack incremental bundling |
| product-capability | Translate product goals into scoped capability maps |
| security-review | Comprehensive security checklist |
| strategic-compact | Context management |
| tdd-workflow | Test-driven development with 80%+ coverage |
| verification-loop | Build, test, lint, typecheck, security |
| video-editing | AI-assisted video editing workflows with FFmpeg and Remotion |
| x-api | X/Twitter API integration for posting and analytics |

### Key Limitation（关键限制）

Codex does **not yet provide Claude-style hook execution parity**. ECC enforcement there is instruction-based via `AGENTS.md`, optional `model_instructions_file` overrides, and sandbox/approval settings.

### Multi-Agent Support（多 Agent 支持）

Current Codex builds support stable multi-agent workflows.

- Enable `features.multi_agent = true` in `.codex/config.toml`
- Define roles under `[agents.<name>]`
- Point each role at a file under `.codex/agents/`
- Use `/agent` in the CLI to inspect or steer child agents

ECC ships three sample role configs：

| Role | Purpose |
|------|---------|
| `explorer` | Read-only codebase evidence gathering before edits |
| `reviewer` | Correctness, security, and missing-test review |
| `docs_researcher` | Documentation and API verification before release/docs changes |

---

## OpenCode Support（OpenCode 支持）

ECC 提供 **完整的 OpenCode 支持**，包括 plugins 和 hooks。

### Quick Start（快速开始）

```bash
# Install OpenCode
npm install -g opencode

# Run in the repository root
opencode
```

The configuration is automatically detected from `.opencode/opencode.json`.

### Feature Parity（功能对等性）

| Feature | Claude Code | OpenCode | Status |
|---------|-------------|----------|--------|
| Agents | PASS: 60 agents | PASS: 12 agents | **Claude Code leads** |
| Commands | PASS: 75 commands | PASS: 35 commands | **Claude Code leads** |
| Skills | PASS: 228 skills | PASS: 37 skills | **Claude Code leads** |
| Hooks | PASS: 8 event types | PASS: 11 events | **OpenCode has more!** |
| Rules | PASS: 29 rules | PASS: 13 instructions | **Claude Code leads** |
| MCP Servers | PASS: 14 servers | PASS: Full | **Full parity** |
| Custom Tools | PASS: Via hooks | PASS: 6 native tools | **OpenCode is better** |

### Hook Support via Plugins（通过插件的 Hook 支持）

OpenCode's plugin system is MORE sophisticated than Claude Code with 20+ event types：

| Claude Code Hook | OpenCode Plugin Event |
|-----------------|----------------------|
| PreToolUse | `tool.execute.before` |
| PostToolUse | `tool.execute.after` |
| Stop | `session.idle` |
| SessionStart | `session.created` |
| SessionEnd | `session.deleted` |

**Additional OpenCode events：** `file.edited`、`file.watcher.updated`、`message.updated`、`lsp.client.diagnostics`、`tui.toast.show` 等。

### Maintained Slash Entries（维护的斜杠入口）

| Command | Description |
|---------|-------------|
| `/plan` | Create implementation plan |
| `/code-review` | Review code changes |
| `/build-fix` | Fix build errors |
| `/refactor-clean` | Remove dead code |
| `/learn` | Extract patterns from session |
| `/checkpoint` | Save verification state |
| `/quality-gate` | Run the maintained verification gate |
| `/update-docs` | Update documentation |
| `/update-codemaps` | Update codemaps |
| `/test-coverage` | Analyze coverage |
| `/go-review` | Go code review |
| `/go-test` | Go TDD workflow |
| `/go-build` | Fix Go build errors |
| `/python-review` | Python code review (PEP 8, type hints, security) |
| `/multi-plan` | Multi-model collaborative planning |
| `/multi-execute` | Multi-model collaborative execution |
| `/multi-backend` | Backend-focused multi-model workflow |
| `/multi-frontend` | Frontend-focused multi-model workflow |
| `/multi-workflow` | Full multi-model development workflow |
| `/pm2` | Auto-generate PM2 service commands |
| `/sessions` | Manage session history |
| `/skill-create` | Generate skills from git |
| `/instinct-status` | View learned instincts |
| `/instinct-import` | Import instincts |
| `/instinct-export` | Export instincts |
| `/evolve` | Cluster instincts into skills |
| `/promote` | Promote project instincts to global scope |
| `/projects` | List known projects and instinct stats |
| `/prune` | Delete expired pending instincts (30d TTL) |
| `/learn-eval` | Extract and evaluate patterns before saving |
| `/setup-pm` | Configure package manager |
| `/harness-audit` | Audit harness reliability, eval readiness, and risk posture |
| `/loop-start` | Start controlled agentic loop execution pattern |
| `/loop-status` | Inspect active loop status and checkpoints |
| `/quality-gate` | Run quality gate checks for paths or entire repo |
| `/model-route` | Route tasks to models by complexity and budget |

### Plugin Installation（插件安装）

**Option 1: Use directly**
```bash
cd everything-claude-code
opencode
```

**Option 2: Install as npm package**
```bash
npm install ecc-universal
```

Then add to your `opencode.json`：
```json
{
  "plugin": ["ecc-universal"]
}
```

That npm plugin entry enables ECC's published OpenCode plugin module (hooks/events and plugin tools).
It does **not** automatically add ECC's full command/agent/instruction catalog to your project config.

For the full ECC OpenCode setup, either：
- run OpenCode inside this repository, or
- copy the bundled `.opencode/` config assets into your project and wire the `instructions`, `agent`, and `command` entries in `opencode.json`

### Documentation（文档）

- **Migration Guide**：`.opencode/MIGRATION.md`
- **OpenCode Plugin README**：`.opencode/README.md`
- **Consolidated Rules**：`.opencode/instructions/INSTRUCTIONS.md`
- **LLM Documentation**：`llms.txt` (complete OpenCode docs for LLMs)

---

## GitHub Copilot Support（GitHub Copilot 支持）

ECC 为 VS Code 提供 **GitHub Copilot 支持**，通过 Copilot Chat 的原生指令和提示文件系统 — 无需额外工具。

### What's Included（包含内容）

| Component | File | Purpose |
|-----------|------|---------|
| Core instructions | `.github/copilot-instructions.md` | Always-loaded rules: coding style, security, testing, git workflow |
| VS Code settings | `.vscode/settings.json` | Per-task instruction files for code gen, test gen, review, and commit messages |
| Plan prompt | `.github/prompts/plan.prompt.md` | Phased implementation planning |
| TDD prompt | `.github/prompts/tdd.prompt.md` | Red-Green-Improve cycle |
| Code review prompt | `.github/prompts/code-review.prompt.md` | Quality and security review |
| Security review prompt | `.github/prompts/security-review.prompt.md` | Deep OWASP-aligned security analysis |
| Build fix prompt | `.github/prompts/build-fix.prompt.md` | Systematic build and CI error resolution |
| Refactor prompt | `.github/prompts/refactor.prompt.md` | Dead code cleanup and simplification |

### Quick Start (GitHub Copilot)（快速开始（GitHub Copilot））

The files are already in place — open any repo that contains this project and GitHub Copilot Chat will automatically pick up `.github/copilot-instructions.md`.
The committed `.vscode/settings.json` enables `chat.promptFiles` so VS Code can load the reusable prompts from `.github/prompts/`.

To use the workflow prompts in Copilot Chat：
1. Open the Copilot Chat panel in VS Code.
2. Click the **paperclip / attach** icon and select **Prompt...**, or type `/` and choose a prompt.
3. Select the prompt (e.g. `plan`, `tdd`, `code-review`).

### How It Works（工作原理）

GitHub Copilot in VS Code reads two types of files automatically：

- **`.github/copilot-instructions.md`** — repository-level instructions, always injected into every Copilot Chat request. Contains ECC's core coding standards, security checklist, testing requirements, and git workflow.
- **`.github/prompts/*.prompt.md`** — reusable prompt files users invoke on demand. Each prompt walks Copilot through a specific ECC workflow (plan → TDD → review → ship).

The **`.vscode/settings.json`** adds per-task instruction overlays so Copilot receives the right context depending on whether you are generating code, writing tests, reviewing a selection, or drafting a commit message.

### Feature Coverage（功能覆盖）

| ECC Feature | Copilot equivalent |
|-------------|-------------------|
| Coding standards | Always-on via `copilot-instructions.md` |
| Security checklist | Always-on + `security-review` prompt |
| Testing / TDD | Always-on + `tdd` prompt |
| Implementation planning | `plan` prompt |
| Code review | `code-review` prompt |
| Build error resolution | `build-fix` prompt |
| Refactoring | `refactor` prompt |
| Commit message format | Per-task instruction in `settings.json` |
| Hooks / automation | Not supported (Copilot has no hook system) |
| Agents / delegation | Not supported (Copilot has no subagent API) |

### Limitations（限制）

GitHub Copilot does not have a hook system or a subagent API, so ECC's hook automations (auto-format, TypeScript check, session persistence, dev-server guard) and agent delegation are unavailable. The instruction and prompt layer still brings the full ECC coding philosophy — standards, security, TDD, and workflow — into every Copilot Chat session.

---

## Cross-Tool Feature Parity（跨工具功能对等性）

ECC 是 **首个最大化利用每个主要 AI 编码工具的插件**。以下是各工具链的对比：

| Feature | Claude Code | Cursor IDE | Codex CLI | OpenCode | GitHub Copilot |
|---------|------------|------------|-----------|----------|----------------|
| **Agents** | 60 | Shared (AGENTS.md) | Shared (AGENTS.md) | 12 | N/A |
| **Commands** | 75 | Shared | Instruction-based | 35 | 6 prompts |
| **Skills** | 228 | Shared | 10 (native format) | 37 | Via instructions |
| **Hook Events** | 8 types | 15 types | None yet | 11 types | None |
| **Hook Scripts** | 20+ scripts | 16 scripts (DRY adapter) | N/A | Plugin hooks | N/A |
| **Rules** | 34 (common + lang) | 34 (YAML frontmatter) | Instruction-based | 13 instructions | 1 always-on file |
| **Custom Tools** | Via hooks | Via hooks | N/A | 6 native tools | N/A |
| **MCP Servers** | 14 | Shared (mcp.json) | 7 (auto-merged via TOML parser) | Full | N/A |
| **Config Format** | settings.json | hooks.json + rules/ | config.toml | opencode.json | copilot-instructions.md + settings.json |
| **Context File** | CLAUDE.md + AGENTS.md | AGENTS.md | AGENTS.md | AGENTS.md | copilot-instructions.md |
| **Secret Detection** | Hook-based | beforeSubmitPrompt hook | Sandbox-based | Hook-based | Instruction-based |
| **Auto-Format** | PostToolUse hook | afterFileEdit hook | N/A | file.edited hook | N/A |
| **Version** | Plugin | Plugin | Reference config | 2.0.0-rc.1 | Instruction layer |

**Key architectural decisions：**
- **AGENTS.md** at root is the universal cross-tool file (read by Claude Code, Cursor, Codex, and OpenCode — GitHub Copilot uses `.github/copilot-instructions.md` instead)
- **DRY adapter pattern** lets Cursor reuse Claude Code's hook scripts without duplication
- **Skills format** (SKILL.md with YAML frontmatter) works across Claude Code, Codex, and OpenCode
- Codex's lack of hooks is compensated by `AGENTS.md`, optional `model_instructions_file` overrides, and sandbox permissions

---

## Background（背景）

I've been using Claude Code since the experimental rollout. Won the Anthropic x Forum Ventures hackathon in Sep 2025 with [@DRodriguezFX](https://x.com/DRodriguezFX) — built [zenith.chat](https://zenith.chat) entirely using Claude Code.

These configs are battle-tested across multiple production applications.

---

## Token Optimization（Token 优化）

如果你不管理 token 消耗，Claude Code 的使用可能会很昂贵。这些设置可在不牺牲质量的情况下显著降低成本。

### Recommended Settings（推荐设置）

添加到 `~/.claude/settings.json`：

```json
{
  "model": "sonnet",
  "env": {
    "MAX_THINKING_TOKENS": "10000",
    "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "50"
  }
}
```

| Setting | Default | Recommended | Impact |
|---------|---------|-------------|--------|
| `model` | opus | **sonnet** | ~60% cost reduction; handles 80%+ of coding tasks |
| `MAX_THINKING_TOKENS` | 31,999 | **10,000** | ~70% reduction in hidden thinking cost per request |
| `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` | 95 | **50** | Compacts earlier — better quality in long sessions |

Switch to Opus only when you need deep architectural reasoning：
```
/model opus
```

### Daily Workflow Commands（日常工作流命令）

| Command | When to Use |
|---------|-------------|
| `/model sonnet` | Default for most tasks |
| `/model opus` | Complex architecture, debugging, deep reasoning |
| `/clear` | Between unrelated tasks (free, instant reset) |
| `/compact` | At logical task breakpoints (research done, milestone complete) |
| `/cost` | Monitor token spending during session |

### Strategic Compaction（策略性压缩）

`strategic-compact` skill（包含在此插件中）建议在逻辑断点处使用 `/compact`，而不是依赖 95% 上下文时的自动压缩。完整决策指南请参阅 `skills/strategic-compact/SKILL.md`。

**When to compact：**
- After research/exploration, before implementation
- After completing a milestone, before starting the next
- After debugging, before continuing feature work
- After a failed approach, before trying a new one

**When NOT to compact：**
- Mid-implementation (you'll lose variable names, file paths, partial state)

### Context Window Management（上下文窗口管理）

**Critical：** 不要同时启用所有 MCPs。每个 MCP tool description 都会从你的 200k 窗口中占用 tokens，可能将其减少到约 70k。

- Keep under 10 MCPs enabled per project
- Keep under 80 tools active
- Use `/mcp` to disable unused Claude Code MCP servers; those runtime choices persist in `~/.claude.json`
- Use `ECC_DISABLED_MCPS` only to filter ECC-generated MCP configs during install/sync flows

### Agent Teams Cost Warning（Agent 团队成本警告）

Agent Teams spawns multiple context windows. Each teammate consumes tokens independently. Only use for tasks where parallelism provides clear value (multi-module work, parallel reviews). For simple sequential tasks, subagents are more token-efficient.

---

## WARNING: Important Notes（警告：重要提示）

### Token Optimization（Token 优化）

Hitting daily limits? See the **[Token Optimization Guide](docs/token-optimization.md)** for recommended settings and workflow tips.

Quick wins：

```json
// ~/.claude/settings.json
{
  "model": "sonnet",
  "env": {
    "MAX_THINKING_TOKENS": "10000",
    "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "50",
    "CLAUDE_CODE_SUBAGENT_MODEL": "haiku"
  }
}
```

Use `/clear` between unrelated tasks, `/compact` at logical breakpoints, and `/cost` to monitor spending.

### Customization（自定义）

These configs work for my workflow. You should：
1. Start with what resonates
2. Modify for your stack
3. Remove what you don't use
4. Add your own patterns

---

## Community Projects（社区项目）

基于或受 Everything Claude Code 启发的项目：

| Project | Description |
|---------|-------------|
| [EVC](https://github.com/SaigonXIII/evc) | Marketing agent workspace — 42 commands for content operators, brand governance, and multi-channel publishing. [Visual overview](https://saigonxiii.github.io/evc). |
| [trading-skills](https://github.com/VictorVVedtion/trading-skills) | 68 trading-themed Claude Code skills with pre-trade review prompts and risk gates inspired by market operators. |

Built something with ECC? Open a PR to add it here.

---

## Sponsors（赞助商）

本项目免费且开源。赞助者帮助维持其发展和增长。

[**Become a Sponsor**](https://github.com/sponsors/affaan-m) | [Sponsor Tiers](SPONSORS.md) | [Sponsorship Program](SPONSORING.md)

---

## Star History（星标历史）

[![Star History Chart](https://api.star-history.com/svg?repos=affaan-m/everything-claude-code&type=Date)](https://star-history.com/#affaan-m/everything-claude-code&Date)

---

## Links（链接）

- **Shorthand Guide (Start Here):** [The Shorthand Guide to Everything Claude Code](https://x.com/affaanmustafa/status/2012378465664745795)
- **Longform Guide (Advanced):** [The Longform Guide to Everything Claude Code](https://x.com/affaanmustafa/status/2014040193557471352)
- **Security Guide:** [Security Guide](./the-security-guide.md) | [Thread](https://x.com/affaanmustafa/status/2033263813387223421)
- **Follow：** [@affaanmustafa](https://x.com/affaanmustafa)

---

## License（许可证）

MIT - Use freely, modify as needed, contribute back if you can.

---

**Star this repo if it helps. Read both guides. Build something great.**