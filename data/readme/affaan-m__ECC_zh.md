**语言：** 英语 | [Português (Brasil)](docs/pt-BR/README.md) | [简体中文](README.zh-CN.md) | [繁體中文](docs/zh-TW/README.md) | [日本語](docs/ja-JP/README.md) | [한국어](docs/ko-KR/README.md) | [Türkçe](docs/tr/README.md) | [Русский](docs/ru/README.md) | [Tiếng Việt](docs/vi-VN/README.md) | [ไทย](docs/th/README.md) | [Deutsch](docs/de-DE/README.md)

# ECC

![ECC - the harness-native operator system for agentic work](assets/hero.png)

[![Stars](https://img.shields.io/github/stars/affaan-m/ECC?style=flat)](https://github.com/affaan-m/ECC/stargazers)
[![Forks](https://img.shields.io/github/forks/affaan-m/ECC?style=flat)](https://github.com/affaan-m/ECC/network/members)
[![Contributors](https://img.shields.io/github/contributors/affaan-m/ECC?style=flat)](https://github.com/affaan-m/ECC/graphs/contributors)
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

> **182K+ stars** | **28K+ forks** | **170+ contributors** | **12+ language ecosystems** | **Cross-harness agent workflows**

---

<div align="center">

**Language / 语言 / 語言 / Dil / Язык / Ngôn ngữ**

[**English**](README.md) | [Português (Brasil)](docs/pt-BR/README.md) | [简体中文](README.zh-CN.md) | [繁體中文](docs/zh-TW/README.md) | [日本語](docs/ja-JP/README.md) | [한국어](docs/ko-KR/README.md)
 | [Türkçe](docs/tr/README.md) | [Русский](docs/ru/README.md) | [Tiếng Việt](docs/vi-VN/README.md) | [ไทย](docs/th/README.md) | [Deutsch](docs/de-DE/README.md)

</div>

---

**面向智能体工作的原生工具链操作系统。基于真实世界的多工具链工程工作流构建。**

不只是配置文件。一套完整体系：技能（skills）、直觉（instincts）、内存优化、持续学习、安全扫描与优先研究开发。经过 10 个多月高强度日常使用，已打磨出生产就绪的智能体、技能、钩子（hook）、规则、MCP 配置及遗留命令适配器。

兼容 **Codex**、**Claude Code**、**Cursor**、**OpenCode**、**Gemini**、**Zed**、**GitHub Copilot** 及其他 AI 智能体工具链。

ECC v2.0.0-rc.1 在此基础上增加了公开的 Hermes 操作者工作流：请先查阅 [Hermes 设置指南](docs/HERMES-SETUP.md)，随后查看 [rc.1 发行说明](docs/releases/2.0.0-rc.1/release-notes.md) 与 [跨工具链架构](docs/architecture/cross-harness.md)。

---

<table>
<tr>
<td width="25%" align="center">
  <a href="https://ecc.tools/pricing">
    <strong> ECC Pro</strong><br />
    <sub>Private repos · GitHub App · $19/seat/mo</sub>
  </a>
</td>
<td width="25%" align="center">
  <a href="https://github.com/sponsors/affaan-m">
    <strong> Sponsor</strong><br />
    <sub>Fund the OSS · From $5/mo</sub>
  </a>
</td>
<td width="25%" align="center">
  <a href="https://github.com/affaan-m/ECC/discussions">
    <strong>Community</strong>
    <br />
    <sub>Discussions · Q&amp;A · Show &amp; Tell</sub>
  </a>
</td>
<td width="25%" align="center">
  <a href="https://github.com/apps/ecc-tools">
    <strong> GitHub App</strong><br />
    <sub>Install · PR audits · Free tier</sub>
  </a>
</td>
</tr>
</table>

<sub>**开源保持免费。** 本仓库永久采用 MIT 协议。ECC Pro 是用于私有仓库的托管 GitHub App。<a href="https://github.com/sponsors/affaan-m">赞助商</a>与<a href="https://ecc.tools/pricing">Pro 订阅用户</a>为开发提供资金——这也是为何单一维护者能每周向 7 种工具链同步更新的原因。</sub>

---

## The Guides

本仓库仅包含源代码。所有详细说明请参阅配套指南。

<table>
<tr>
<td width="33%">
<a href="https://x.com/affaanmustafa/status/2012378465664745795">
<img src="./assets/images/guides/shorthand-guide.png" alt="The Shorthand Guide to ECC" />
</a>
</td>
<td width="33%">
<a href="https://x.com/affaanmustafa/status/2014040193557471352">
<img src="./assets/images/guides/longform-guide.png" alt="The Longform Guide to ECC" />
</a>
</td>
<td width="33%">
<a href="https://x.com/affaanmustafa/status/2033263813387223421">
<img src="./assets/images/security/security-guide-header.png" alt="The Shorthand Guide to Everything Agentic Security" />
</a>
</td>
</tr>
<tr>
<td align="center"><b>速览指南（Shorthand Guide）</b><br/>安装、基础架构与理念。<b>请先阅读此项。</b></td>
<td align="center"><b>深度指南（Longform Guide）</b><br/>Token 优化、内存持久化、评估测试、并行化处理。</td>
<td align="center"><b>安全指南（Security Guide）</b><br/>攻击向量、沙箱隔离、数据清洗、CVE 漏洞、AgentShield。</td>
</tr>
</table>

| Topic | What You'll Learn |
|-------|-------------------|
| Token Optimization | 模型选择、系统提示词精简、后台进程处理 |
| Memory Persistence | 自动跨会话保存/加载上下文的钩子（hook） |
| Continuous Learning | 从会话中自动提取模式并转化为可复用技能 |
| Verification Loops | 检查点与连续评估、评分器类型、pass@k 指标 |
| Parallelization | Git worktrees、级联方法、何时扩展实例 |
| Subagent Orchestration | 上下文问题、迭代检索模式 |

---

## What's New

### v2.0.0-rc.1 — Surface Refresh, Operator Workflows, and ECC 2.0 Alpha (Apr 2026)

- **Dashboard GUI** — 基于 Tkinter 的新桌面应用 (`ecc_dashboard.py` 或 `npm run dashboard`)，支持深色/浅色主题切换、字体自定义及页眉/任务栏项目 Logo。
- **Public surface synced to the live repo** — 元数据、目录计数、插件清单及安装文档现已与实际开源内容一致：63 个智能体、249 项技能、79 个遗留命令适配器。
- **Operator and outbound workflow expansion** — `brand-voice`、`social-graph-ranker`、`connections-optimizer`、`customer-billing-ops`、`ecc-tools-cost-audit`、`google-workspace-ops`、`project-flow-ops` 和 `workspace-surface-audit` 补齐了操作者赛道。
- **Media and launch tooling** — `manim-video`、`remotion-video-creation` 及升级的社交媒体发布界面使技术说明与发布内容融入同一体系。
- **Framework and product surface growth** — `nestjs-patterns`、更丰富的 Codex/OpenCode 安装入口，以及扩展的跨工具链打包保持仓库在 Claude Code 之外的可用性。
- **Itô prediction-market skill pack** — `ito-market-intelligence`、`ito-basket-compare`、`ito-trade-planner`、`ito-data-atlas-agent`、`prediction-market-oracle-research` 和 `prediction-market-risk-review` 新增公开非建议型市场/篮子工作流，同时保留实时 Itô API 访问权限的独立计费隔离。
- **Optimization skill pack** — `parallel-execution-optimizer`、`benchmark-optimization-loop`、`data-throughput-accelerator`、`latency-critical-systems` 和 `recursive-decision-ledger` 将重复的速度/递归提示转化为有界的基准测试、吞吐量与决策账本工作流。
- **ECC 2.0 alpha is in-tree** — `ecc2/` 中的 Rust 控制平面原型现已支持本地构建，并提供 `dashboard`、`start`、`sessions`、`status`、`stop`、`resume` 和 `daemon` 命令。目前为 Alpha 版本，尚未正式发布。
- **Operator status snapshots** — `ecc status --markdown --write status.md` 将本地状态存储转换为可移植交接文件，涵盖就绪状态、活跃会话、技能运行健康度、安装健康度、待处理治理事件及来自 Linear/GitHub/handoffs 的关联工作项。配合 `ecc work-items upsert ...` 可实现手动录入，使用 `ecc work-items sync-github --repo owner/repo` 同步 PR/Issue 队列状态，并通过 `ecc status --exit-code` 在就绪度需关注时中断自动化流程。
- **Ecosystem hardening** — AgentShield、ECC Tools 成本控制及账单门户等工作持续围绕核心插件推进，避免形成孤立模块。

### v1.9.0 — Selective Install & Language Expansion (Mar 2026)

- **Selective install architecture** — 基于清单的安装管道，使用 `install-plan.js` 和 `install-apply.js` 实现定向组件安装。状态存储记录已安装内容并支持增量更新。
- **6 new agents** — `typescript-reviewer`、`pytorch-build-resolver`、`java-build-resolver`、`java-reviewer`、`kotlin-reviewer`、`kotlin-build-resolver` 将语言覆盖扩展至 10 种。
- **New skills** — 用于深度学习工作流的 `pytorch-patterns`，用于 API 参考研究的 `documentation-lookup`，用于现代 JS 工具链的 `bun-runtime` 和 `nextjs-turbopack`，以及 8 项运营领域技能和 `mcp-server-patterns`。
- **Session & state infrastructure** — 带查询 CLI 的 SQLite 状态存储、结构化记录的会话适配器、自我改进技能的演进基础。
- **Orchestration overhaul** — 使工具链审计评分确定化，加固编排状态与启动器兼容性，通过 5 层防护防止观察者循环（observer loop）。
- **Observer reliability** — 修复内存爆炸问题（节流与尾部采样）、沙箱访问修复、延迟启动逻辑及重入保护。
- **12 language ecosystems** — Java、PHP、Perl、Kotlin/Android/KMP、C++ 和 Rust 的新规则加入现有的 TypeScript、Python、Go 及通用规则中。
- **Community contributions** — 韩语与中文翻译、biome hook 优化、视频处理技能、运营技能、PowerShell 安装器、Antigravity IDE 支持。
- **CI hardening** — 修复 19 项测试失败，强制执行目录计数、验证安装清单，全量测试套件通过。

### v1.8.0 — Harness Performance System (Mar 2026)

- **Harness-first release** — ECC 现明确定位为智能体工具链性能系统，而不仅是配置包。
- **Hook reliability overhaul** — SessionStart 根回退、Stop 阶段会话摘要，以及基于脚本的钩子取代易碎的行内单行命令。
- **Hook runtime controls** — `ECC_HOOK_PROFILE=minimal|standard|strict` 和 `ECC_DISABLED_HOOKS=...` 用于运行时门控，无需编辑钩子文件。
- **New harness commands** — `/harness-audit`、`/loop-start`、`/loop-status`、`/quality-gate`、`/model-route`。
- **NanoClaw v2** — 模型路由、技能热加载、会话分支/搜索/导出/压缩/指标。
- **Cross-harness parity** — 在 Claude Code、Cursor、OpenCode 和 Codex app/CLI 间收紧行为一致性。
- **997 internal tests passing** — 钩子/运行时重构与兼容性更新后，全量套件通过。

### v1.7.0 — Cross-Platform Expansion & Presentation Builder (Feb 2026)

- **Codex app + CLI support** — 直接基于 `AGENTS.md` 的 Codex 支持、安装器目标定位及 Codex 文档
- **`frontend-slides` skill** — 零依赖 HTML 演示构建器，附带 PPTX 转换指南与严格视口适配规则
- **5 new generic business/content skills** — `article-writing`、`content-engine`、`market-research`、`investor-materials`、`investor-outreach`
- **Broader tool coverage** — 收紧 Cursor、Codex 和 OpenCode 支持，确保同一仓库可干净地跨所有主流工具链分发
- **992 internal tests** — 扩展插件、钩子、技能与打包的验证及回归覆盖

### v1.6.0 — Codex CLI, AgentShield & Marketplace (Feb 2026)

- **Codex CLI support** — 新增 `/codex-setup` 命令生成 `codex.md` 以兼容 OpenAI Codex CLI
- **7 new skills** — `search-first`、`swift-actor-persistence`、`swift-protocol-di-testing`、`regex-vs-llm-structured-text`、`content-hash-cache-pattern`、`cost-aware-llm-pipeline`、`skill-stocktake`
- **AgentShield integration** — `/security-scan` 技能直接从 Claude Code 运行 AgentShield；1282 项测试，102 条规则
- **GitHub Marketplace** — ECC Tools GitHub App 已在 [github.com/marketplace/ecc-tools](https://github.com/marketplace/ecc-tools) 上线，提供 free/pro/enterprise 层级
- **30+ community PRs merged** — 来自 6 种语言的 30 位贡献者合并 PR
- **978 internal tests** — 扩展智能体、技能、命令、钩子和规则的验证套件

### v1.4.1 — Bug Fix (Feb 2026)

- **Fixed instinct import content loss** — `parse_instinct_file()` 在 `/instinct-import` 期间静默丢弃 frontmatter（Action、Evidence、Examples 部分）之后的所有内容。([#148](https://github.com/affaan-m/ECC/issues/148), [#161](https://github.com/affaan-m/ECC/pull/161))

### v1.4.0 — Multi-Language Rules, Installation Wizard & PM2 (Feb 2026)

- **Interactive installation wizard** — 新增 `configure-ecc` 技能提供带合并/覆盖检测的引导式安装
- **PM2 & multi-agent orchestration** — 6 项新命令（`/pm2`、`/multi-plan`、`/multi-execute`、`/multi-backend`、`/multi-frontend`、`/multi-workflow`）用于管理复杂的多服务工作流
- **Multi-language rules architecture** — 规则从扁平文件重构为 `common/` + `typescript/` + `python/` + `golang/` 目录。仅安装你需要的语言
- **Chinese (zh-CN) translations** — 所有智能体、命令、技能和规则的完整翻译（80+ 文件）
- **GitHub Sponsors support** — 通过 GitHub Sponsors 赞助项目
- **Enhanced CONTRIBUTING.md** — 每种贡献类型的详细 PR 模板

### v1.3.0 — OpenCode Plugin Support (Feb 2026)

- **Full OpenCode integration** — 12 个智能体、24 条命令、16 项技能，通过 OpenCode 插件系统（20+ 事件类型）支持钩子
- **3 native custom tools** — run-tests, check-coverage, security-audit
- **LLM documentation** — `llms.txt` 提供全面的 OpenCode 文档

### v1.2.0 — Unified Commands & Skills (Feb 2026)

- **Python/Django support** — Django patterns、security、TDD 和 verification 技能
- **Java Spring Boot skills** — Patterns、security、TDD 和 verification for Spring Boot
- **Session management** — `/sessions` 命令用于会话历史管理
- **Continuous learning v2** — 基于直觉的学习，支持置信度评分、导入/导出、演进

完整更新日志请参阅 [Releases](https://github.com/affaan-m/ECC/releases)。

---

## Quick Start

2分钟内完成安装与运行：

### Pick one path only

大多数 Claude Code 用户应严格使用以下其中一种安装方式：

- **推荐默认：** 安装 Claude Code 插件，然后仅复制你实际需要的规则文件夹。
- **仅在需要更细粒度控制、希望完全避开插件路径，或你的 Claude Code 版本在解析自托管市场入口时出现问题时使用手动安装器。**
- **不要叠加安装方式。** 最常见的损坏配置是：先执行 `/plugin install`，随后再运行 `install.sh --profile full` 或 `npx ecc-install --profile full`。

如果你已叠加多次安装且出现重复项，请直接跳至 [重置/卸载 ECC](#reset--uninstall-ecc)。

### Low-context / no-hooks path

如果钩子（hooks）感觉过于全局化，或者你只需要 ECC 的规则、智能体、命令和核心工作流技能，请跳过插件并使用最小手动配置：

```bash
./install.sh --profile minimal --target claude
```

```powershell
.\install.ps1 --profile minimal --target claude
# or
npx ecc-install --profile minimal --target claude
```

此配置有意排除了 `hooks-runtime`。

如果你需要正常的核心配置但希望关闭钩子，请使用：

```bash
./install.sh --profile core --without baseline:hooks --target claude
```

仅当你需要运行时强制执行时才后续添加钩子：

```bash
./install.sh --target claude --modules hooks-runtime
```

### Find the right components first

如果你不确定应安装哪个 ECC 配置或组件，可从任意项目询问内置顾问：

```bash
npx ecc consult "security reviews" --target claude
```

它将返回匹配的组件、相关配置及预览/安装命令。若需检查确切文件计划，请在安装前使用预览命令。

对于生产级 ML/MLOps 工作流，请保持安装为可选且按组件范围限定：

```bash
npx ecc consult "mlops training model deployment" --target claude
npx ecc install --profile minimal --target claude --with capability:machine-learning
```

### Step 1: Install the Plugin (Recommended)

> NOTE: 插件很方便，但如果你的 Claude Code 版本在解析自托管市场入口时出现问题，下方的 OSS 安装器仍是更可靠的路径。

```bash
# Add marketplace
/plugin marketplace add https://github.com/affaan-m/ECC

# Install plugin
/plugin install ecc@ecc
```

### Naming + Migration Note

ECC 现在有三个公开标识符，它们不可互换：

- GitHub source repo: `affaan-m/ECC`
- Claude marketplace/plugin identifier: `ecc@ecc`
- npm package: `ecc-universal`

这是有意为之。Anthropic 市场/插件安装由规范插件标识符键控，因此 ECC 使用 `ecc@ecc` 以保持工具名称和斜杠命令命名空间足够短以符合严格的桌面/API 验证器限制。旧文章可能仍显示旧的长市场标识符；请仅将其视为遗留别名。此外，npm 包保持为 `ecc-universal`，因此 npm 安装与市场安装有意使用不同名称。

### Step 2: Install Rules Only If You Need Them

> WARNING: **重要：** Claude Code 插件无法自动分发 `rules`。
>
> 如果你已通过 `/plugin install` 安装了 ECC，**请勿随后运行 `./install.sh --profile full`、`.\install.ps1 --profile full` 或 `npx ecc-install --profile full`**。插件已加载 ECC 技能、命令和钩子。在插件安装后运行完整安装器会将相同内容复制到你的用户目录中，可能导致重复的技能及重复的运行时行为。
>
> 对于插件安装，请手动仅复制你需要的 `rules/` 文件夹至 `~/.claude/rules/ecc/` 下。从 `rules/common` 加上你实际使用的一种语言或框架包开始。除非你明确希望在 Claude 中加载所有上下文，否则不要复制每个 rules 目录。
>
> 仅当你执行完全手动 ECC 安装（而非插件路径）时才使用完整安装器。
>
> 如果你的本地 Claude 设置被清除或重置，并不意味着你需要重新购买 ECC。请先运行 `node scripts/ecc.js list-installed`，然后执行 `node scripts/ecc.js doctor` 和 `node scripts/ecc.js repair` 再重新安装任何内容。这通常能恢复 ECC 管理的文件而无需重建你的配置。如果问题是 ECC Tools 的账户或市场访问权限，请单独处理账单/账户恢复。

```bash
# Clone the repo first
git clone https://github.com/affaan-m/ECC.git
cd ECC

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

手动安装说明请参阅 `rules/` 文件夹中的 README。手动复制规则时，请复制整个语言目录（例如 `rules/common` 或 `rules/golang`），而非其中的文件，以便相对引用继续生效且文件名不冲突。

### Fully manual install (Fallback)

仅在你有意跳过插件路径时使用：

```bash
./install.sh --profile full
```

```powershell
.\install.ps1 --profile full
# or
npx ecc-install --profile full
```

若选择此路径，到此为止即可。请勿同时运行 `/plugin install`。

### Reset / Uninstall ECC

如果感觉 ECC 重复、侵入或损坏，请不要反复在其上重新安装。

- **插件路径：** 从 Claude Code 中移除插件，然后删除你手动复制到 `~/.claude/rules/ecc/` 下的特定规则文件夹。
- **手动安装器/CLI 路径：** 从仓库根目录先预览移除操作：

```bash
node scripts/uninstall.js --dry-run
```

随后移除 ECC 管理的文件：

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
2. 从仓库根目录运行 ECC 卸载命令以移除安装状态管理的文件。
3. 删除你手动复制且不再需要的额外规则文件夹。
4. 使用单一路径重新安装一次。

### Step 3: Start Using

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

**就是这样！** 你现在已拥有访问 63 个智能体、249 项技能和 79 个遗留命令适配器的权限。

### Dashboard GUI

启动桌面仪表盘以可视化探索 ECC 组件：

```bash
npm run dashboard
# or
python3 ./ecc_dashboard.py
```

**Features:**
- Tabbed interface: Agents, Skills, Commands, Rules, Settings
- Dark/Light theme toggle
- Font customization (family & size)
- Project logo in header and taskbar
- Search and filter across all components

### Multi-model commands require additional setup

> WARNING: `multi-*` 命令**不涵盖**在上述基础插件/规则安装中。
>
> 要使用 `/multi-plan`、`/multi-execute`、`/multi-backend`、`/multi-frontend` 和 `/multi-workflow`，你还必须安装 `ccg-workflow` 运行时。
>
> 通过 `npx ccg-workflow` 初始化它。
>
> 该运行时提供这些命令期望的外部依赖项，包括：
> - `~/.claude/bin/codeagent-wrapper`
> - `~/.claude/.ccg/prompts/*`
>
> 缺少 `ccg-workflow` 时，这些 `multi-*` 命令将无法正确运行。

---

## Cross-Platform Support

本插件现已全面支持 **Windows、macOS 和 Linux**，并与主流 IDE（Cursor、Zed、OpenCode、Antigravity）及 CLI 工具链深度集成。所有钩子和脚本均已重写为 Node.js 以实现最大兼容性。

### Package Manager Detection

插件自动检测你首选的包管理器（npm、pnpm、yarn 或 bun），优先级如下：

1. **环境变量**: `CLAUDE_PACKAGE_MANAGER`
2. **项目配置**: `.claude/package-manager.json`
3. **package.json**: `packageManager` 字段
4. **锁文件**: 从 package-lock.json、yarn.lock、pnpm-lock.yaml 或 bun.lockb 检测
5. **全局配置**: `~/.claude/package-manager.json`
6. **回退**: 首个可用的包管理器

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

### Hook Runtime Controls

使用运行时标志调整严格度或临时禁用特定钩子：

```bash
# Hook strictness profile (default: standard)
export ECC_HOOK_PROFILE=standard

# Comma-separated hook IDs to disable
export ECC_DISABLED_HOOKS="pre:bash:tmux-reminder,post:edit:typecheck"

# Cap SessionStart additional context (default: 8000 chars)
export ECC_SESSION_START_MAX_CHARS=4000

# Disable SessionStart additional context entirely for low-context/local-model setups
export ECC_SESSION_START_CONTEXT=off

# Keep context/scope/loop warnings but suppress API-rate cost estimates
export ECC_CONTEXT_MONITOR_COST_WARNINGS=off
```

Windows PowerShell:

```powershell
[Environment]::SetEnvironmentVariable('ECC_CONTEXT_MONITOR_COST_WARNINGS', 'off', 'User')
```

---

## What's Inside

本仓库是一个 **Claude Code 插件** — 可直接安装或手动复制组件。

```
ECC/
|-- .claude-plugin/   # Plugin and marketplace manifests
|   |-- plugin.json         # Plugin metadata and component paths
|   |-- marketplace.json    # Marketplace catalog for /plugin marketplace add
|
|-- agents/           # 63 specialized subagents for delegation
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

## Ecosystem Tools

### Skill Creator

通过两种方式为 Claude Code 生成技能：

#### Option A: Local Analysis (Built-in)

使用 `/skill-create` 命令进行本地分析，无需外部服务：

```bash
/skill-create                    # Analyze current repo
/skill-create --instincts        # Also generate instincts for continuous-learning-v2
```

这将在本地分析你的 git 历史并生成 SKILL.md 文件。

#### Option B: GitHub App (Advanced)

针对高级功能（10k+ commits、自动 PR、团队共享）：

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

### AgentShield — Security Auditor

> Built at the Claude Code Hackathon (Cerebral Valley x Anthropic, Feb 2026). 1282 tests, 98% coverage, 102 static analysis rules.

扫描你的 Claude Code 配置以查找漏洞、错误配置和注入风险。

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

**What it scans:** CLAUDE.md, settings.json, MCP configs, hooks, agent definitions, and skills across 5 categories — secrets detection (14 patterns), permission auditing, hook injection analysis, MCP server risk profiling, and agent config review.

**The `--opus` flag** runs three Claude Opus 4.6 agents in a red-team/blue-team/auditor pipeline. The attacker finds exploit chains, the defender evaluates protections, and the auditor synthesizes both into a prioritized risk assessment. Adversarial reasoning, not just pattern matching.

**Output formats:** Terminal (color-graded A-F), JSON (CI pipelines), Markdown, HTML. Exit code 2 on critical findings for build gates.

在 Claude Code 中使用 `/security-scan` 运行，或通过 [GitHub Action](https://github.com/affaan-m/agentshield) 添加至 CI。

[GitHub](https://github.com/affaan-m/agentshield) | [npm](https://www.npmjs.com/package/ecc-agentshield)

### Continuous Learning v2

基于直觉的学习系统自动学习你的模式：

```bash
/instinct-status        # Show learned instincts with confidence
/instinct-import <file> # Import instincts from others
/instinct-export        # Export your instincts for sharing
/evolve                 # Cluster related instincts into skills
```

完整文档请参阅 `skills/continuous-learning-v2/`。
仅当你明确需要遗留 v1 Stop-hook 学习技能流程时才保留 `continuous-learning/`。

---

## Requirements

### Claude Code CLI Version

**Minimum version: v2.1.0 or later**

由于插件系统处理钩子的方式发生变化，本插件要求 Claude Code CLI v2.1.0+。

检查你的版本：
```bash
claude --version
```

### Important: Hooks Auto-Loading Behavior

> WARNING: **对于贡献者：** 请勿在 `.claude-plugin/plugin.json` 中添加 `"hooks"` 字段。此行为由回归测试强制执行。

Claude Code v2.1+ **自动加载** 任何已安装插件中的 `hooks/hooks.json`（按约定）。在 `plugin.json` 中显式声明会导致重复检测错误：

```
Duplicate hooks file detected: ./hooks/hooks.json resolves to already-loaded file
```

**History:** 这已在该仓库中导致多次修复/回滚循环 ([#29](https://github.com/affaan-m/ECC/issues/29), [#52](https://github.com/affaan-m/ECC/issues/52), [#103](https://github.com/affaan-m/ECC/issues/103))。该行为在 Claude Code 版本间发生变化，导致混淆。我们现在已添加回归测试以防止此问题再次引入。

---

## Installation

### Option 1: Install as Plugin (Recommended)

使用本仓库的最简单方式——作为 Claude Code 插件安装：

```bash
# Add this repo as a marketplace
/plugin marketplace add https://github.com/affaan-m/ECC

# Install the plugin
/plugin install ecc@ecc
```

或直接添加至你的 `~/.claude/settings.json`：

```json
{
  "extraKnownMarketplaces": {
    "ecc": {
      "source": {
        "source": "github",
        "repo": "affaan-m/ECC"
      }
    }
  },
  "enabledPlugins": {
    "ecc@ecc": true
  }
}
```

这将使你即时访问所有命令、智能体、技能和钩子。

> **Note:** Claude Code 插件系统不支持通过插件分发 `rules`（[上游限制](https://code.claude.com/docs/en/plugins-reference)）。你需要手动安装规则：
>
> ```bash
> # Clone the repo first
> git clone https://github.com/affaan-m/ECC.git
> cd ECC
>
> # Option A: User-level rules (applies to all projects)
> mkdir -p ~/.claude/rules/ecc
> cp -r rules/common ~/.claude/rules/ecc/
> cp -r rules/typescript ~/.claude/rules/ecc/   # pick your stack
> cp -r rules/python ~/.claude/rules/ecc/
> cp -r rules/golang ~/.claude/rules/ecc/
> cp -r rules/php ~/.claude/rules/ecc/
>
> # Option B: Project-level rules (applies to current project only)
> mkdir -p .claude/rules/ecc
> cp -r rules/common .claude/rules/ecc/
> cp -r rules/typescript .claude/rules/ecc/     # pick your stack
> ```

---

### Option 2: Manual Installation

如果你偏好手动控制安装内容：

```bash
# Clone the repo
git clone https://github.com/affaan-m/ECC.git
cd ECC

# Copy agents to your Claude config
cp agents/*.md ~/.claude/agents/

# Copy rules directories (common + language-specific)
mkdir -p ~/.claude/rules/ecc
cp -r rules/common ~/.claude/rules/ecc/
cp -r rules/typescript ~/.claude/rules/ecc/   # pick your stack
cp -r rules/python ~/.claude/rules/ecc/
cp -r rules/golang ~/.claude/rules/ecc/
cp -r rules/php ~/.claude/rules/ecc/
cp -r rules/arkts ~/.claude/rules/ecc/

# Copy skills first (primary workflow surface)
# Recommended (new users): core/general skills only
mkdir -p ~/.claude/skills/ecc
cp -r .agents/skills/* ~/.claude/skills/ecc/
cp -r skills/search-first ~/.claude/skills/ecc/

# Optional: add niche/framework-specific skills only when needed
# for s in django-patterns django-tdd laravel-patterns springboot-patterns quarkus-patterns; do
# cp -r skills/$s ~/.claude/skills/ecc/
# done

# Optional: keep maintained slash-command compatibility during migration
mkdir -p ~/.claude/commands
cp commands/*.md ~/.claude/commands/

# Retired shims live in legacy-command-shims/commands/.
# Copy individual files from there only if you still need old names such as /tdd.
```

#### Install hooks

请勿将原始仓库 `hooks/hooks.json` 复制到 `~/.claude/settings.json` 或 `~/.claude/hooks/hooks.json`。该文件面向插件/仓库，应通过 ECC 安装器安装或作为插件加载，因此直接复制不是受支持的手动安装路径。

使用安装器仅安装 Claude 钩子运行时，以便正确重写命令路径：

```bash
# macOS / Linux
bash ./install.sh --target claude --modules hooks-runtime
```

```powershell
# Windows PowerShell
pwsh -File .\install.ps1 --target claude --modules hooks-runtime
```

这会将解析后的钩子写入 `~/.claude/hooks/hooks.json`，且不会触碰任何现有的 `~/.claude/settings.json`。

如果你通过 `/plugin install` 安装了 ECC，请勿将这些钩子复制到 `settings.json`。Claude Code v2.1+ 已自动加载插件的 `hooks/hooks.json`，在 `settings.json` 中重复它们会导致重复执行和跨平台钩子冲突。

Windows note: the Claude config directory is `%USERPROFILE%\\.claude`, not `~/claude`.

#### Configure MCPs

Claude 插件安装有意不自动启用 ECC 的内置 MCP 服务器定义。这避免了在严格的第三方网关上使用过长的插件 MCP 工具名称，同时保留手动 MCP 设置选项。

使用 Claude Code 的 `/mcp` 命令或 CLI 管理的 MCP 设置进行实时 Claude Code 服务器更改。使用 `/mcp` 禁用 Claude Code；Claude Code 将这些选择持久化至 `~/.claude.json`。

对于仓库本地 MCP 访问，将所需的 MCP 服务器定义从 `mcp-configs/mcp-servers.json` 复制到项目范围的 `.mcp.json` 中。

如果你已运行自己的 ECC 内置 MCP 副本，请设置：

```bash
export ECC_DISABLED_MCPS="github,context7,exa,playwright,sequential-thinking,memory"
```

ECC 管理的安装和 Codex 同步流程将跳过或移除这些内置服务器，而不是重新添加重复项。`ECC_DISABLED_MCPS` 是 ECC 安装/同步过滤器，而非实时 Claude Code 开关。

**Important:** Replace `YOUR_*_HERE` placeholders with your actual API keys.

---

## Key Concepts

### Agents

子智能体处理具有有限范围的委托任务。示例：

```markdown
---
name: code-reviewer
description: Reviews code for quality, security, and maintainability
tools: ["Read", "Grep", "Glob", "Bash"]
model: opus
---

You are a senior code reviewer...
```

### Skills

技能是主要的工作流界面。它们可直接调用、自动建议，并被智能体复用。迁移期间 ECC 仍分发维护的 `commands/`，而退役的短名称适配器仅存在于 `legacy-command-shims/` 中以供显式选择加入。新工作流开发应首先落地于 `skills/`。

```markdown
# TDD Workflow

1. Define interfaces first
2. Write failing tests (RED)
3. Implement minimal code (GREEN)
4. Refactor (IMPROVE)
5. Verify 80%+ coverage
```

### Hooks

钩子在工具事件上触发。示例 - 警告 console.log：

```json
{
  "matcher": "tool == \"Edit\" && tool_input.file_path matches \"\\\\.(ts|tsx|js|jsx)$\"",
  "hooks": [{
    "type": "command",
    "command": "#!/bin/bash\ngrep -n 'console\\.log' \"$file_path\" && echo '[Hook] Remove console.log' >&2"
  }]
}
```

### Rules

规则是始终遵循的指南，组织为 `common/`（语言无关）+ 特定语言目录：

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

安装与结构详情请参阅 [`rules/README.md`](rules/README.md)。

---

## Which Agent Should I Use?

不确定从哪里开始？使用此快速参考。技能是规范的工作流界面；维护的斜杠入口仍可用于命令优先工作流。

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

### Common Workflows

下方显示斜杠形式，只要它们仍属于维护的命令界面。退役的短名称适配器（如 `/tdd` 和 `/eval`）仅存在于 `legacy-command-shims/` 中以供显式选择加入。

**Starting a new feature:**
```
/ecc:plan "Add user authentication with OAuth"
                                              → planner creates implementation blueprint
tdd-workflow skill                            → tdd-guide enforces write-tests-first
/code-review                                  → code-reviewer checks your work
```

**Fixing a bug:**
```
tdd-workflow skill                            → tdd-guide: write a failing test that reproduces it
                                              → implement the fix, verify test passes
/code-review                                  → code-reviewer: catch regressions
```

**Preparing for production:**
```
/security-scan                                → security-reviewer: OWASP Top 10 audit
e2e-testing skill                             → e2e-runner: critical user flow tests
/test-coverage                                → verify 80%+ coverage
```

---

## FAQ

<details>
<summary><b>How do I check which agents/commands are installed?</b></summary>

```bash
/plugin list ecc@ecc
```

This shows all available agents, commands, and skills from the plugin.
</details>

<details>
<summary><b>My hooks aren't working / I see "Duplicate hooks file" errors</b></summary>

这是最常见的问题。**请勿在 `.claude-plugin/plugin.json` 中添加 `"hooks"` 字段**。Claude Code v2.1+ 自动加载已安装插件中的 `hooks/hooks.json`。显式声明会导致重复检测错误。请参阅 [#29](https://github.com/affaan-m/ECC/issues/29)、[#52](https://github.com/affaan-m/ECC/issues/52)、[#103](https://github.com/affaan-m/ECC/issues/103)。
</details>

<details>
<summary><b>Can I use ECC with Claude Code on a custom API endpoint or model gateway?</b></summary>

可以。ECC 未硬编码 Anthropic 托管的传输设置。它通过 Claude Code 的正常 CLI/插件界面在本地运行，因此适用于：

- Anthropic-hosted Claude Code
- 使用 `ANTHROPIC_BASE_URL` 和 `ANTHROPIC_AUTH_TOKEN` 的官方 Claude Code 网关设置
- 兼容自定义端点（符合 Anthropic API 规范）

最小示例：

```bash
export ANTHROPIC_BASE_URL=https://your-gateway.example.com
export ANTHROPIC_AUTH_TOKEN=your-token
claude
```

如果你的网关重映射模型名称，请在 Claude Code 中配置此设置而非在 ECC 中。一旦 `claude` CLI 正常工作，ECC 的钩子、技能、命令和规则与模型提供商无关。

官方参考：
- [Claude Code LLM gateway docs](https://docs.anthropic.com/en/docs/claude-code/llm-gateway)
- [Claude Code model configuration docs](https://docs.anthropic.com/en/docs/claude-code/model-config)

</details>

<details>
<summary><b>My context window is shrinking / Claude is running out of context</b></summary>

过多的 MCP 服务器会消耗你的上下文。每个 MCP 工具描述都会从你的 200k 窗口中消耗 token，可能将其缩减至约 70k。默认情况下 SessionStart 上下文限制为 8000 个字符；对于本地模型或低上下文设置，可通过 `ECC_SESSION_START_MAX_CHARS=4000` 降低它，或通过 `ECC_SESSION_START_CONTEXT=off` 禁用它。

**Fix:** Disable unused MCPs from Claude Code with `/mcp`. Claude Code writes those runtime choices to `~/.claude.json`; `.claude/settings.json` and `.claude/settings.local.json` are not reliable toggles for already-loaded MCP servers.

保持启用不超过 10 个 MCP，活跃工具不超过 80 个。
</details>

<details>
<summary><b>Can I use only some components (e.g., just agents)?</b></summary>

可以。使用方案 2（手动安装）并仅复制你需要的内容：

```bash
# Just agents
cp agents/*.md ~/.claude/agents/

# Just rules
mkdir -p ~/.claude/rules/ecc/
cp -r rules/common ~/.claude/rules/ecc/
```

每个组件完全独立。
</details>

<details>
<summary><b>Does this work with Cursor / OpenCode / Codex / Antigravity / GitHub Copilot?</b></summary>

可以。ECC 是跨平台的：
- **Cursor**：`.cursor/` 中的预翻译配置。请参阅 [Cursor IDE Support](#cursor-ide-support)。
- **Gemini CLI**：通过 `.gemini/GEMINI.md` 和共享安装器管道的实验性项目本地支持。
- **OpenCode**：`.opencode/` 中的完整插件支持。请参阅 [OpenCode Support](#opencode-support)。
- **Codex**：macOS 应用与 CLI 的一流支持，包含适配器漂移防护和 SessionStart 回退。请参阅 PR [#257](https://github.com/affaan-m/ECC/pull/257)。
- **GitHub Copilot (VS Code)**：通过 `.github/copilot-instructions.md`、`.vscode/settings.json` 和 `.github/prompts/` 的指令与提示层。请参阅 [GitHub Copilot Support](#github-copilot-support)。
- **Antigravity**：针对工作流、技能和扁平化规则的紧密集成设置。请参阅 [Antigravity Guide](docs/ANTIGRAVITY-GUIDE.md)。
- **JoyCode / CodeBuddy**：命令、智能体、技能和平坦化规则的项目本地选择性安装适配器。请参阅 [JoyCode Adapter Guide](docs/JOYCODE-GUIDE.md)。
- **Qwen CLI**：命令、智能体、技能、规则和 Qwen 配置的目录选择安装适配器。请参阅 [Qwen CLI Adapter Guide](docs/QWEN-GUIDE.md)。
- **Zed**：`.zed/settings.json`、扁平化规则、命令、智能体和技能的项目本地选择性安装适配器。
- **Non-native harnesses**: Grok 及类似接口的手动回退路径。请参阅 [Manual Adaptation Guide](docs/MANUAL-ADAPTATION-GUIDE.md)。
- **Claude Code**：原生支持——这是主要目标。
</details>

<details>
<summary><b>How do I contribute a new skill or agent?</b></summary>

请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。简短版本：
1. Fork 仓库
2. 在 `skills/your-skill-name/SKILL.md`（带 YAML frontmatter）中创建你的技能
3. 或在 `agents/your-agent.md` 中创建智能体
4. 提交 PR，清晰描述其功能及使用场景
</details>

---

## Running Tests

插件包含全面的测试套件：

```bash
# Run all tests
node tests/run-all.js

# Run individual test files
node tests/lib/utils.test.js
node tests/lib/package-manager.test.js
node tests/hooks/hooks.test.js
```

---

## Contributing

**欢迎并鼓励贡献。**

本仓库旨在成为社区资源。如果你有：
- 有用的智能体或技能
- 巧妙的钩子（hooks）
- 更好的 MCP 配置
- 改进的规则

请贡献！请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 获取指南。

### Ideas for Contributions

- Language-specific skills (Rust, C#, Kotlin, Java) — Go, Python, Perl, Swift, TypeScript, and HarmonyOS/ArkTS already included
- Framework-specific configs (Rails, FastAPI) — Django, NestJS, Spring Boot, and Laravel already included
- DevOps agents (Kubernetes, Terraform, AWS, Docker)
- Testing strategies (different frameworks, visual regression)
- Domain-specific knowledge (ML, data engineering, mobile)

### Community Ecosystem Notes

这些不与 ECC 捆绑，也不经本仓库审计，但如果你正在探索更广泛的 Claude Code 技能生态，它们值得关注：

- [claude-seo](https://github.com/AgriciDaniel/claude-seo) — SEO 导向的技能与智能体集合
- [claude-ads](https://github.com/AgriciDaniel/claude-ads) — 广告审计与付费增长工作流集合
- [claude-cybersecurity](https://github.com/AgriciDaniel/claude-cybersecurity) — 安全导向的技能与智能体集合

---

## Cursor IDE Support

ECC 提供适用于 Cursor IDE 的支持，钩子、规则、智能体、技能、命令和 MCP 配置已针对 Cursor 的项目布局进行适配。

### Quick Start (Cursor)

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

### What's Included

| Component | Count | Details |
|-----------|-------|---------|
| Hook Events | 15 | sessionStart, beforeShellExecution, afterFileEdit, beforeMCPExecution, beforeSubmitPrompt, and 10 more |
| Hook Scripts | 16 | Thin Node.js scripts delegating to `scripts/hooks/` via shared adapter |
| Rules | 34 | 9 common (alwaysApply) + 25 language-specific (TypeScript, Python, Go, Swift, PHP) |
| Agents | 48 | `.cursor/agents/ecc-*.md` when installed; prefixed to avoid collisions with user or marketplace agents |
| Skills | Shared + Bundled | `.cursor/skills/` for translated additions |
| Commands | Shared | `.cursor/commands/` if installed |
| MCP Config | Shared | `.cursor/mcp.json` if installed |

### Cursor Loading Notes

ECC 不将根 `AGENTS.md` 安装至 `.cursor/`。Cursor 将嵌套的 `AGENTS.md` 文件视为目录上下文，因此将 ECC 的仓库身份复制到主机项目中会污染该项目。

Cursor-native loading behavior can vary by Cursor build. ECC installs agents as `.cursor/agents/ecc-*.md`; if your Cursor build does not expose project agents, those files still work as explicit reference definitions instead of hidden global prompt context.

### Hook Architecture (DRY Adapter Pattern)

Cursor 拥有**比 Claude Code 更多的钩子事件**（20 vs 8）。`.cursor/hooks/adapter.js` 模块将 Cursor 的 stdin JSON 转换为 Claude Code 格式，允许复用现有的 `scripts/hooks/*.js` 而无需重复。

```
Cursor stdin JSON → adapter.js → transforms → scripts/hooks/*.js
                                              (shared with Claude Code)
```

Key hooks:
- **beforeShellExecution** — Blocks dev servers outside tmux (exit 2), git push review
- **afterFileEdit** — Auto-format + TypeScript check + console.log warning
- **beforeSubmitPrompt** — Detects secrets (sk-, ghp_, AKIA patterns) in prompts
- **beforeTabFileRead** — Blocks Tab from reading .env, .key, .pem files (exit 2)
- **beforeMCPExecution / afterMCPExecution** — MCP audit logging

### Rules Format

Cursor rules use YAML frontmatter with `description`, `globs`, and `alwaysApply`:

```yaml
---
description: "TypeScript coding style extending common rules"
globs: ["**/*.ts", "**/*.tsx", "**/*.js", "**/*.jsx"]
alwaysApply: false
---
```

---

## Codex macOS App + CLI Support

ECC 为 macOS 应用与 CLI 提供 **Codex 的一流支持**，包含参考配置、Codex 专用的 AGENTS.md 补充文件及共享技能。

### Quick Start (Codex App + CLI)

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

同步脚本使用**仅添加（add-only）**策略安全地将 ECC MCP 服务器合并至你现有的 `~/.codex/config.toml` 中——它永远不会移除或修改你的现有服务器。运行 `--dry-run` 预览更改，或 `--update-mcp` 强制刷新 ECC 服务器至最新推荐配置。

对于 Context7，ECC 使用规范的 Codex 部分名称 `[mcp_servers.context7]`，同时仍启动 `@upstash/context7-mcp` 包。如果你已有遗留的 `[mcp_servers.context7-mcp]` 条目，`--update-mcp` 会将其迁移至规范的部分名称。

Codex macOS app:
- Open this repository as your workspace.
- The root `AGENTS.md` is auto-detected.
- `.codex/config.toml` and `.codex/agents/*.toml` work best when kept project-local.
- The reference `.codex/config.toml` intentionally does not pin `model` or `model_provider`, so Codex uses its own current default unless you override it.
- Optional: copy `.codex/config.toml` to `~/.codex/config.toml` for global defaults; keep the multi-agent role files project-local unless you also copy `.codex/agents/`.

### What's Included

| Component | Count | Details |
|-----------|-------|---------|
| Config | 1 | `.codex/config.toml` — top-level approvals/sandbox/web_search, MCP servers, notifications, profiles |
| AGENTS.md | 2 | Root (universal) + `.codex/AGENTS.md` (Codex-specific supplement) |
| Skills | 32 | `.agents/skills/` — SKILL.md + agents/openai.yaml per skill |
| MCP Servers | 6 | GitHub, Context7, Exa, Memory, Playwright, Sequential Thinking (7 with Supabase via `--update-mcp` sync) |
| Profiles | 2 | `strict` (read-only sandbox) and `yolo` (full auto-approve) |
| Agent Roles | 3 | `.codex/agents/` — explorer, reviewer, docs-researcher |

### Skills

Skills at `.agents/skills/` are auto-loaded by Codex:

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

### Key Limitation

Codex does **not yet provide Claude-style hook execution parity**. ECC enforcement there is instruction-based via `AGENTS.md`, optional `model_instructions_file` overrides, and sandbox/approval settings.

### Multi-Agent Support

Current Codex builds support stable multi-agent workflows.

- Enable `features.multi_agent = true` in `.codex/config.toml`
- Define roles under `[agents.<name>]`
- Point each role at a file under `.codex/agents/`
- Use `/agent` in the CLI to inspect or steer child agents

ECC ships three sample role configs:

| Role | Purpose |
|------|---------|
| `explorer` | Read-only codebase evidence gathering before edits |
| `reviewer` | Correctness, security, and missing-test review |
| `docs_researcher` | Documentation and API verification before release/docs changes |

---

## Zed Support

ECC 通过保守的 `.zed` 适配器为 Zed 提供项目支持，涵盖项目本地设置、扁平化规则、智能体、命令和技能。

```bash
./install.sh --profile minimal --target zed
```

```powershell
.\install.ps1 --profile minimal --target zed
```

该适配器将 ECC 管理的文件写入 `.zed/` 下，并将 BYOK/OpenRouter 凭证保留在仓库外。通过 Zed 自身的设置 UI 或你的本地用户配置设置 Zed 账户或 API 密钥。

---

## OpenCode Support

ECC 提供 **完整的 OpenCode 支持**，包括插件与钩子。

### Quick Start

```bash
# Install OpenCode
npm install -g opencode

# Run in the repository root
opencode
```

配置自动从 `.opencode/opencode.json` 检测。

### Feature Parity

| Feature | Claude Code         | OpenCode | Status |
|---------|---------------------|----------|--------|
| Agents | PASS: 63 agents     | PASS: 12 agents | **Claude Code leads** |
| Commands | PASS: 79 commands   | PASS: 35 commands | **Claude Code leads** |
| Skills | PASS: 249 skills    | PASS: 37 skills | **Claude Code leads** |
| Hooks | PASS: 8 event types | PASS: 11 events | **OpenCode has more!** |
| Rules | PASS: 29 rules      | PASS: 13 instructions | **Claude Code leads** |
| MCP Servers | PASS: 14 servers    | PASS: Full | **Full parity** |
| Custom Tools | PASS: Via hooks     | PASS: 6 native tools | **OpenCode is better** |

### Hook Support via Plugins

OpenCode's plugin system is MORE sophisticated than Claude Code with 20+ event types:

| Claude Code Hook | OpenCode Plugin Event |
|-----------------|----------------------|
| PreToolUse | `tool.execute.before` |
| PostToolUse | `tool.execute.after` |
| Stop | `session.idle` |
| SessionStart | `session.created` |
| SessionEnd | `session.deleted` |

**Additional OpenCode events**: `file.edited`, `file.watcher.updated`, `message.updated`, `lsp.client.diagnostics`, `tui.toast.show`, and more.

### Maintained Slash Entries

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

### Plugin Installation

**Option 1: Use directly**
```bash
cd ECC
opencode
```

**Option 2: Install as npm package**
```bash
npm install ecc-universal
```

Then add to your `opencode.json`:
```json
{
  "plugin": ["ecc-universal"]
}
```

That npm plugin entry enables ECC's published OpenCode plugin module (hooks/events and plugin tools).
It does **not** automatically add ECC's full command/agent/instruction catalog to your project config.

For the full ECC OpenCode setup, either:
- run OpenCode inside this repository, or
- copy the bundled `.opencode/` config assets into your project and wire the `instructions`, `agent`, and `command` entries in `opencode.json`

### Documentation

- **Migration Guide**: `.opencode/MIGRATION.md`
- **OpenCode Plugin README**: `.opencode/README.md`
- **Consolidated Rules**: `.opencode/instructions/INSTRUCTIONS.md`
- **LLM Documentation**: `llms.txt` (complete OpenCode docs for LLMs)

---

## GitHub Copilot Support

ECC 提供适用于 VS Code 的 **GitHub Copilot 支持**，通过 Copilot Chat 的原生指令与提示文件系统——无需额外工具。

### What's Included

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

### Quick Start (GitHub Copilot)

The files are already in place — open any repo that contains this project and GitHub Copilot Chat will automatically pick up `.github/copilot-instructions.md`.
The committed `.vscode/settings.json` enables `chat.promptFiles` so VS Code can load the reusable prompts from `.github/prompts/`.

To use the workflow prompts in Copilot Chat:
1. Open the Copilot Chat panel in VS Code.
2. Click the **paperclip / attach** icon and select **Prompt...**, or type `/` and choose a prompt.
3. Select the prompt (e.g. `plan`, `tdd`, `code-review`).

### How It Works

GitHub Copilot in VS Code reads two types of files automatically:

- **`.github/copilot-instructions.md`** — repository-level instructions, always injected into every Copilot Chat request. Contains ECC's core coding standards, security checklist, testing requirements, and git workflow.
- **`.github/prompts/*.prompt.md`** — reusable prompt files users invoke on demand. Each prompt walks Copilot through a specific ECC workflow (plan → TDD → review → ship).

The **`.vscode/settings.json`** adds per-task instruction overlays so Copilot receives the right context depending on whether you are generating code, writing tests, reviewing a selection, or drafting a commit message.

### Feature Coverage

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

### Limitations

GitHub Copilot does not have a hook system or a subagent API, so ECC's hook automations (auto-format, TypeScript check, session persistence, dev-server guard) and agent delegation are unavailable. The instruction and prompt layer still brings the full ECC coding philosophy — standards, security, TDD, and workflow — into every Copilot Chat session.

---

## Cross-Tool Feature Parity

ECC 是**首个最大化利用所有主流 AI 编码工具的插件**。以下是各工具链的对比：

| Feature | Claude Code           | Cursor IDE | Codex CLI | OpenCode | GitHub Copilot |
|---------|-----------------------|------------|-----------|----------|----------------|
| **Agents** | 63                    | Shared (AGENTS.md) | Shared (AGENTS.md) | 12 | N/A |
| **Commands** | 79                    | Shared | Instruction-based | 35 | 6 prompts |
| **Skills** | 249                   | Shared | 10 (native format) | 37 | Via instructions |
| **Hook Events** | 8 types               | 15 types | None yet | 11 types | None |
| **Hook Scripts** | 20+ scripts           | 16 scripts (DRY adapter) | N/A | Plugin hooks | N/A |
| **Rules** | 34 (common + lang)    | 34 (YAML frontmatter) | Instruction-based | 13 instructions | 1 always-on file |
| **Custom Tools** | Via hooks             | Via hooks | N/A | 6 native tools | N/A |
| **MCP Servers** | 14                    | Shared (mcp.json) | 7 (auto-merged via TOML parser) | Full | N/A |
| **Config Format** | settings.json         | hooks.json + rules/ | config.toml | opencode.json | copilot-instructions.md + settings.json |
| **Context File** | CLAUDE.md + AGENTS.md | AGENTS.md | AGENTS.md | AGENTS.md | copilot-instructions.md |
| **Secret Detection** | Hook-based            | beforeSubmitPrompt hook | Sandbox-based | Hook-based | Instruction-based |
| **Auto-Format** | PostToolUse hook      | afterFileEdit hook | N/A | file.edited hook | N/A |
| **Version** | Plugin | Plugin | Reference config | 2.0.0-rc.1 | Instruction layer |

**Key architectural decisions:**
- **AGENTS.md** at root is the universal cross-tool file (read by Claude Code, Cursor, Codex, and OpenCode — GitHub Copilot uses `.github/copilot-instructions.md` instead)
- **DRY adapter pattern** lets Cursor reuse Claude Code's hook scripts without duplication
- **Skills format** (SKILL.md with YAML frontmatter) works across Claude Code, Codex, and OpenCode
- Codex's lack of hooks is compensated by `AGENTS.md`, optional `model_instructions_file` overrides, and sandbox permissions

---

## Background

I've been using Claude Code since the experimental rollout. Won the Anthropic x Forum Ventures hackathon in Sep 2025 with [@DRodriguezFX](https://x.com/DRodriguezFX) — built [zenith.chat](https://zenith.chat) entirely using Claude Code.

These configs are battle-tested across multiple production applications.

---

## Token Optimization

Claude Code usage can be expensive if you don't manage token consumption. These settings significantly reduce costs without sacrificing quality.

### Recommended Settings

Add to `~/.claude/settings.json`:

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
| `ECC_CONTEXT_MONITOR_COST_WARNINGS` | on | **off for subscription users** | Suppresses agent-facing API-rate estimate warnings while keeping context/scope/loop warnings |

Switch to Opus only when you need deep architectural reasoning:
```
/model opus
```

### Daily Workflow Commands

| Command | When to Use |
|---------|-------------|
| `/model sonnet` | Default for most tasks |
| `/model opus` | Complex architecture, debugging, deep reasoning |
| `/clear` | Between unrelated tasks (free, instant reset) |
| `/compact` | At logical task breakpoints (research done, milestone complete) |
| `/cost` | Monitor token spending during session |

If you use a Claude subscription and the context monitor's API-rate estimates are not useful, set `ECC_CONTEXT_MONITOR_COST_WARNINGS=off`. This only suppresses the agent-facing cost warnings; it does not disable context exhaustion, scope, or loop warnings.

### Strategic Compaction

The `strategic-compact` skill (included in this plugin) suggests `/compact` at logical breakpoints instead of relying on auto-compaction at 95% context. See `skills/strategic-compact/SKILL.md` for the full decision guide.

**When to compact:**
- After research/exploration, before implementation
- After completing a milestone, before starting the next
- After debugging, before continuing feature work
- After a failed approach, before trying a new one

**When NOT to compact:**
- Mid-implementation (you'll lose variable names, file paths, partial state)

### Context Window Management

**Critical:** Don't enable all MCPs at once. Each MCP tool description consumes tokens from your 200k window, potentially reducing it to ~70k.

- Keep under 10 MCPs enabled per project
- Keep under 80 tools active
- Use `/mcp` to disable unused Claude Code MCP servers; those runtime choices persist in `~/.claude.json`
- Use `ECC_DISABLED_MCPS` only to filter ECC-generated MCP configs during install/sync flows

### Agent Teams Cost Warning

Agent Teams spawns multiple context windows. Each teammate consumes tokens independently. Only use for tasks where parallelism provides clear value (multi-module work, parallel reviews). For simple sequential tasks, subagents are more token-efficient.

---

## WARNING: Important Notes

### Token Optimization

Hitting daily limits? See the **[Token Optimization Guide](docs/token-optimization.md)** for recommended settings and workflow tips.

Quick wins:

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

### Customization

These configs work for my workflow. You should:
1. Start with what resonates
2. Modify for your stack
3. Remove what you don't use
4. Add your own patterns

---

## Community Projects

Projects built on or inspired by ECC:

| Project | Description |
|---------|-------------|
| [EVC](https://github.com/SaigonXIII/evc) | Marketing agent workspace — 42 commands for content operators, brand governance, and multi-channel publishing. [Visual overview](https://saigonxiii.github.io/evc). |
| [trading-skills](https://github.com/VictorVVedtion/trading-skills) | 68 trading-themed Claude Code skills with pre-trade review prompts and risk gates inspired by market operators. |

Built something with ECC? Open a PR to add it here.

---

## Sponsors

This project is free and open source. Sponsors help keep it maintained and growing.

[**Become a Sponsor**](https://github.com/sponsors/affaan-m) | [Sponsor Tiers](SPONSORS.md) | [Sponsorship Program](SPONSORING.md)

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date)](https://star-history.com/#affaan-m/ECC&Date)

---

## Links

- **Shorthand Guide (Start Here):** [The Shorthand Guide to Everything Claude Code](https://x.com/affaanmustafa/status/2012378465664745795)
- **Longform Guide (Advanced):** [The Longform Guide to Everything Claude Code](https://x.com/affaanmustafa/status/2014040193557471352)
- **Security Guide:** [Security Guide](./the-security-guide.md) | [Thread](https://x.com/affaanmustafa/status/2033263813387223421)
- **Follow:** [@affaanmustafa](https://x.com/affaanmustafa)

---

## License

MIT - Use freely, modify as needed, contribute back if you can.

---

**Star this repo if it helps. Read both guides. Build something great.**