<p align="center">
  <img src="https://em-content.zobj.net/source/apple/391/rock_1faa8.png" width="120" />
</p>

<h1 align="center">caveman</h1>

<p align="center">
  <strong>为什么要用那么多 token，寥寥几个就能搞定呢？</strong>
</p>

<p align="center">
  <a href="https://github.com/JuliusBrussee/caveman/stargazers"><img src="https://img.shields.io/github/stars/JuliusBrussee/caveman?style=flat&color=yellow" alt="Stars"></a>
  <a href="https://github.com/JuliusBrussee/caveman/commits/main"><img src="https://img.shields.io/github/last-commit/JuliusBrussee/caveman?style=flat" alt="Last Commit"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/JuliusBrussee/caveman?style=flat" alt="License"></a>
</p>

<p align="center">
  <a href="#before--after">效果对比</a> •
  <a href="#install">安装指南</a> •
  <a href="#what-you-get">功能特性</a> •
  <a href="#benchmarks">性能基准测试</a> •
  <a href="./INSTALL.md">完整安装教程</a>
</p>

---

一款适用于 [Claude Code](https://docs.anthropic.com/en/docs/claude-code) 的技能（Skill）/插件（同样支持 Codex、Gemini、Cursor、Windsurf、Cline、Copilot 等 30+ 款工具），让 AI Agent 以“原始人”风格对话——**削减约 75% 的输出 token**，同时保持完整的技术准确性。脑子依然很大，嘴巴变小了。

## Before / After（效果对比）

<table>
<tr>
<td width="50%">

### 🗣️ Normal Claude (69 tokens)

> "The reason your React component is re-rendering is likely because you're creating a new object reference on each render cycle. When you pass an inline object as a prop, React's shallow comparison sees it as a different object every time, which triggers a re-render. I'd recommend using useMemo to memoize the object."

</td>
<td width="50%">

### 🪨 Caveman Claude (19 tokens)

> "New object ref each render. Inline object prop = new ref = re-render. Wrap in `useMemo`."

</td>
</tr>
<tr>
<td>

### 🗣️ Normal Claude

> "Sure! I'd be happy to help you with that. The issue you're experiencing is most likely caused by your authentication middleware not properly validating the token expiry. Let me take a look and suggest a fix."

</td>
<td>

### 🪨 Caveman Claude

> "Bug in auth middleware. Token expiry check use `<` not `<=`. Fix:"

</td>
</tr>
</table>

**修复方案相同。字数减少 75%。脑子依然很大。**

```
┌─────────────────────────────────────┐
│  TOKENS SAVED          ████████ 75% │
│  TECHNICAL ACCURACY    ████████ 100%│
│  SPEED INCREASE        ████████ ~3x │
│  VIBES                 ████████ OOG │
└─────────────────────────────────────┘
```

选择你的精简等级—— `lite`（去除废话）、`full`（默认原始人风格）、`ultra`（电报体）或 `wenyan`（文言文，更短）。一条命令切换。成本直线下降。

## Install（安装指南）

一行命令。适配所有 Agent。逐个安装即可。

```bash
# macOS / Linux / WSL / Git Bash
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash

# Windows (PowerShell 5.1+)
irm https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.ps1 | iex
```

耗时约 30 秒。需要 Node ≥18。可跳过未安装的 Agent。重复运行安全无忧。

**触发方式：**输入 `/caveman` 或说出“像原始人一样说话”。使用“普通模式”即可停止。

仅单 Agent、手动命令或任意其他 30+ 款工具 → [**INSTALL.md**](./INSTALL.md)。
安装出错？打开 Agent，输入 *“阅读 CLAUDE.md 和 INSTALL.md，帮我安装 caveman。”* Agent 会自行修复。

## What You Get（功能特性）

| Skill | What |
|---|---|
| `/caveman [lite\|full\|ultra\|wenyan]` | **压缩每次回复。** 设置将持续到会话结束。 |
| `/caveman-commit` | **生成符合规范的 Commit 信息**，主题行 ≤50 字符。重“原因”轻“内容”。 |
| `/caveman-review` | **单行 PR 评论：** `L42: 🔴 bug: user null. Add guard.`（保留示例） |
| `/caveman-stats` | **实时会话 Token 用量** + 累计节省量 + 美元换算。可通过 `--share` 生成可推特的统计行。 |
| `/caveman-compress <file>` | **重写记忆文件**（如 `CLAUDE.md`）为原始人风格。每次会话削减约 46% 的输入 Token。代码/链接/路径按字节完整保留。 |
| `caveman-shrink` | **MCP 中间件。** 包装任意 MCP Server，压缩工具描述。[npm 包地址](https://www.npmjs.com/package/caveman-shrink)。 |
| `cavecrew-*` | **原始人子 Agent**（调查员/构建者/审查员）。比原版减少约 60% Token，主上下文窗口维持更久。 |

**状态栏徽章** —— Claude Code 会显示 `[CAVEMAN] ⛏ 12.4k`（累计节省 Token）。每次运行 `/caveman-stats` 后更新。设置环境变量 `CAVEMAN_STATUSLINE_SAVINGS=0` 可隐藏该提示。

每次会话自动激活：Claude Code、Codex、Gemini（内置）。Cursor / Windsurf / Cline / Copilot 可通过 `--with-init` 获取常驻规则文件。其他 Agent 需每轮会话使用 `/caveman` 触发。完整功能矩阵见 [INSTALL.md](./INSTALL.md#what-you-get)。

## Benchmarks（性能基准测试）

数据源自 Claude API 实际调用。在 10 个提示词测试中，平均**输出减少 65%**（范围 22%-87%）。

<!-- BENCHMARK-TABLE-START -->
| Task | Normal | Caveman | Saved |
|------|-------:|--------:|------:|
| Explain React re-render bug | 1180 | 159 | 87% |
| Fix auth middleware token expiry | 704 | 121 | 83% |
| Set up PostgreSQL connection pool | 2347 | 380 | 84% |
| Explain git rebase vs merge | 702 | 292 | 58% |
| Refactor callback to async/await | 387 | 301 | 22% |
| Architecture: microservices vs monolith | 446 | 310 | 30% |
| Review PR for security issues | 678 | 398 | 41% |
| Docker multi-stage build | 1042 | 290 | 72% |
| Debug PostgreSQL race condition | 1200 | 232 | 81% |
| Implement React error boundary | 3454 | 456 | 87% |
| **Average** | **1214** | **294** | **65%** |
<!-- BENCHMARK-TABLE-END -->

原始数据与复现脚本位于 [`benchmarks/`](./benchmarks/)。三臂评估框架（基线 / 精简版 / 技能插件）位于 [`evals/`](./evals/) —— caveman 是与 `Answer concisely.` 对比，而非冗长的默认输出，因此数据更真实客观。

**caveman-compress 实际效果**（真实记忆文件）：

| File | Original | Compressed | Saved |
|---|---:|---:|---:|
| `claude-md-preferences.md` | 706 | 285 | **59.6%** |
| `project-notes.md` | 1145 | 535 | **53.3%** |
| `claude-md-project.md` | 1122 | 636 | **43.3%** |
| `todo-list.md` | 627 | 388 | **38.1%** |
| `mixed-with-code.md` | 888 | 560 | **36.9%** |
| **Average** | **898** | **481** | **46%** |

> [!IMPORTANT]
> 原始人仅影响输出 Token —— 思考/推理 Token 不受影响。它不会让脑子变小，只是让*嘴巴*变小了。最大收益在于**可读性与速度**，节省成本算是额外福利。

一篇发表于 2026 年 3 月的论文《[Brevity Constraints Reverse Performance Hierarchies in Language Models](https://arxiv.org/abs/2604.00025)》指出，限制大模型生成简短回复**在特定基准测试中准确率提升了 26 个百分点**。冗长并不总是更好。有时字越少 = 越准确。

## How It Work（工作原理）

1. 将技能文件安装至 Agent。
2. 技能指令要求 Agent：去除废话，保留实质内容，使用短语/碎片化表达。
3. 针对 Claude Code，Hook 还会在每次会话写入一个极小的标记文件 —— Agent 检测到该文件后，从第一条消息起自动切换原始人模式。无需手动输入 `/caveman`。
4. 统计命令读取 Claude Code 会话日志，计算节省的 Token 数，并写入状态栏。
5. caveman-compress 子技能重写记忆文件（如 CLAUDE.md、项目笔记），使每次会话以更小的上下文启动。永久节省 Token，而非仅针对单次回复。

维护者详细信息（Hook 架构、文件所有权、CI 同步机制）详见 [CLAUDE.md](./CLAUDE.md)。

## Lobster, Meet Rock 🦞🪨

[**OpenClaw**](https://openclaw.ai) 是一款自托管网关。一台服务器，内置多个 Agent（Claude Code、Codex、Pi、OpenCode），可接入你的 Slack / Discord / iMessage / Telegram 等任意平台。标语：*“龙虾之道。”* 龙虾很强。龙虾很聪明。但话也太多。

caveman 教龙虾学会简洁 —— 使用相同的标准安装器，仅作用于单个 Agent：

```bash
# macOS / Linux / WSL
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash -s -- --only openclaw

# Windows (PowerShell): no Node? install Node ≥18 first, then
npx -y github:JuliusBrussee/caveman -- --only openclaw
```

只会发生两件事，不多不少：

1. **技能文件部署**至 `~/.openclaw/workspace/skills/caveman/SKILL.md` —— 包含符合规范的 frontmatter（`version`、`always: true`），可通过 `openclaw skills list` 发现。该技能不会自动注入（OpenClaw 按需加载）—— 因此我们需要执行第 2 步。
2. **SOUL.md 提示注入。** 将一段带标记的极小代码块追加至 `~/.openclaw/workspace/SOUL.md`。OpenClaw 会在*每一轮*对话中将 SOUL.md 作为“项目上下文”注入（单文件限制 12K，总计 60K —— 该代码块远低于限额）。从第一条消息起龙虾就保持简洁。无需每轮输入 `/caveman`。不再啰嗦催促。

```
~/.openclaw/workspace/
├── skills/caveman/SKILL.md   ← full ruleset, on-demand load
└── SOUL.md                    ← <!-- caveman-begin --> ... <!-- caveman-end -->
                                  ↑ auto-inject every turn
```

自定义工作区路径？在命令前设置 `OPENCLAW_WORKSPACE=/your/path`。卸载：使用相同的单行命令并添加 `--uninstall` —— 技能文件夹将被删除，SOUL.md 中的代码块会被干净地移除，你的其他工作区内容保持原样。重复运行安全幂等（frontmatter 不会重复添加，标记代码块不会重复生成）。

龙虾钳子依然锋利。嘴巴现在变小了。脑子依然很大。

## Caveman Ecosystem（生态工具）

三款工具。一种理念：**让 Agent 用更少的资源做更多的事**。

| Repo | What |
|------|------|
| [**caveman**](https://github.com/JuliusBrussee/caveman) *(you here)* | **输出压缩** —— *为什么要用那么多 token，寥寥几个就能搞定呢？* |
| [**cavemem**](https://github.com/JuliusBrussee/cavemem) | **跨 Agent 记忆共享** —— *为什么 Agent 要遗忘，明明可以记住？* |
| [**cavekit**](https://github.com/JuliusBrussee/cavekit) | **规范驱动构建循环** —— *为什么让 Agent 瞎猜，明明可以直接知道？* |

组合使用：cavekit 驱动构建流程，caveman 压缩 Agent *说的内容*，cavemem 压缩 Agent *记住的内容*。一块石头。两块石头。三块石头。搞定。

## Links（相关链接）

- [INSTALL.md](./INSTALL.md) —— 完整安装矩阵、所有参数及单 Agent 配置详情
- [CONTRIBUTING.md](./CONTRIBUTING.md) —— 贡献代码指南（如何提交补丁）
- [CLAUDE.md](./CLAUDE.md) —— 维护者手册（文件所有权、Hook 架构、CI 流程）
- [docs/](./docs/) —— 扩展指南（Windows 安装等）
- [Issues](https://github.com/JuliusBrussee/caveman/issues) —— 提交 Bug、功能建议或异常行为反馈

## Star This Repo（给个 Star）

caveman 帮你节省 Token，为你省下真金白银。点个 Star 零成本。公平交易。⭐

[![Star History Chart](https://api.star-history.com/svg?repos=JuliusBrussee/caveman&type=Date)](https://star-history.com/#JuliusBrussee/caveman&Date)

## Also by Julius Brussee（作者其他项目）

- **[Revu](https://github.com/JuliusBrussee/revu-swift)** —— 基于本地优先的 macOS 学习应用，内置 FSRS 间隔重复算法。[revu.cards](https://revu.cards)

## License（开源协议）

MIT —— 如旷野上的群居猛犸象般自由（免费）。