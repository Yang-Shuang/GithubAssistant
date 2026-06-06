# gstack

> “我想我大概从12月以来就没敲过几行代码了，这绝对是个巨大的变化。” — [Andrej Karpathy](https://fortune.com/2026/03/21/andrej-karpathy-openai-cofounder-ai-agents-coding-state-of-psychosis-openclaw/)，《No Priors》播客，2026年3月

听到 Karpathy 这么说时，我很想知道这是怎么做到的。一个人怎么能像二十人的团队一样交付产品？Peter Steinberger 几乎是一个人用 AI agent（智能体）构建了 [OpenClaw](https://github.com/openclaw/openclaw) —— 247K GitHub stars。革命已经到来。拥有正确工具的单兵作战者，其推进速度可以超越传统团队。

我是 [Garry Tan](https://x.com/garrytan)，[Y Combinator](https://www.ycombinator.com/) 的总裁兼 CEO。我见证过成千上万的初创公司——Coinbase、Instacart、Rippling——从车库里的两三个人起步。在加入 YC 之前，我是 Palantir 最早的工程/产品经理/设计师之一，联合创立了 Posterous（后被 Twitter 收购），并构建了 Bookface（YC 的内部社交网络）。

**gstack 是我的答案。** 我从事产品开发已经二十年了，而现在正是我交付产品最多的一段时期。在过去60天里：3个生产级服务、40+已上线功能，兼职状态下同时全职运营 YC。以逻辑代码变更计算（而非 AI 会虚增的原始 LOC）——我的2026年速率是 **2013年的 ~810倍**（11,417 vs 14 行/天）。截至4月18日，2026年至今的产出已经是 **2013年全年的240倍**。在统计了40个公开及私有的 `garrytan/*` 仓库后（排除一个 demo 仓库），AI 编写了其中大部分。重点不在于谁敲的代码，而在于最终交付了什么。

> 批评者说原始代码行数在 AI 辅助下会膨胀，这没错。但他们认为归一化后我的生产力下降了，这就错了。我实际上高效得多。完整的方法论、注意事项和复现脚本请见：**[On the LOC Controversy](docs/ON_THE_LOC_CONTROVERSY.md)**（LOC = Lines of Code 代码行数）。

**2026年 —— 1,237次贡献，且仍在增长：**

![GitHub contributions 2026 — 1,237 contributions, massive acceleration in Jan-Mar](docs/images/github-2026.png)

**2013年 —— 我在 YC 构建 Bookface 时（772次贡献）：**

![GitHub contributions 2013 — 772 contributions building Bookface at YC](docs/images/github-2013.png)

同一个人。不同的时代。差异在于工具。

**gstack 是我实现这一目标的方式。** 它将 Claude Code 转变为一个虚拟工程团队——一位重新思考产品的 CEO、一位锁定架构的工程经理、一位拦截 AI 生成垃圾代码的设计师、一位寻找生产环境 bug 的审查员、一位打开真实浏览器进行 QA 测试的主管、一位运行 OWASP + STRIDE 审计的安全官，以及一位负责提交 PR 的发布工程师。23位专家与8款强力工具，全部通过斜杠命令调用，全部基于 Markdown，完全免费，采用 MIT 协议。

这是我的开源软件工厂。我每天都在使用它。分享它是希望这些工具能惠及每个人。

Fork 它。改进它。让它成为你自己的项目。如果你想吐槽这个免费的开源软件——欢迎，但我更希望你先试用一下。

**适用人群：**
- **创始人和 CEO** —— 尤其是仍希望亲自交付产品的技术型创始人
- **首次使用 Claude Code 的用户** —— 用结构化的角色替代空白的提示词
- **技术负责人和资深工程师** —— 对每个 PR 进行严格的审查、QA 和发布自动化

## 快速开始

1. 安装 gstack（约30秒，见下文）
2. 运行 `/office-hours` —— 描述你正在构建的产品
3. 在任何功能构想上运行 `/plan-ceo-review`
4. 在任何包含变更的分支上运行 `/review`
5. 在你的预发环境 URL 上运行 `/qa`
6. 到此为止。你会知道这是否适合你。

## 安装 —— 30秒搞定

**环境要求：** [Claude Code](https://docs.anthropic.com/en/docs/claude-code)、[Git](https://git-scm.com/)、[Bun](https://bun.sh/) v1.0+、[Node.js](https://nodejs.org/)（仅 Windows 需要）

### 步骤 1：在本地安装

打开 Claude Code 并粘贴以下内容。剩下的交给 Claude。

> 安装 gstack：运行 **`git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup`**，然后在 `CLAUDE.md` 中添加一个 “gstack” 区块，内容为：所有网页浏览均使用 gstack 的 `/browse` 技能，绝不使用 `mcp__claude-in-chrome__*` 工具，并列出可用技能：/office-hours, /plan-ceo-review, /plan-eng-review, /plan-design-review, /design-consultation, /design-shotgun, /design-html, /review, /ship, /land-and-deploy, /canary, /benchmark, /browse, /connect-chrome, /qa, /qa-only, /design-review, /setup-browser-cookies, /setup-deploy, /setup-gbrain, /retro, /investigate, /document-release, /codex, /cso, /autoplan, /plan-devex-review, /devex-review, /careful, /freeze, /guard, /unfreeze, /gstack-upgrade, /learn。然后询问用户是否也想将 gstack 添加到当前项目中，以便团队成员也能获得。

### 步骤 2：团队模式 —— 共享仓库的自动更新（推荐）

在你的仓库目录下粘贴以下内容。这将切换到团队模式，初始化仓库以便团队成员自动获取 gstack，并提交变更：

```bash
(cd ~/.claude/skills/gstack && ./setup --team) && ~/.claude/skills/gstack/bin/gstack-team-init required && git add .claude/ CLAUDE.md && git commit -m "require gstack for AI-assisted work"
```

你的仓库中不会包含任何 vendored 文件，无版本漂移，无需手动升级。每次 Claude Code 会话启动时都会进行快速的自动更新检查（限速为每小时一次，网络故障安全，完全静默）。

如果你更倾向于提示而非强制团队成员使用，可将 `required` 替换为 `optional`。

### OpenClaw

OpenClaw 通过 ACP 启动 Claude Code 会话，因此只要 Claude Code 安装了 gstack，所有技能即可直接使用。将此粘贴到你的 OpenClaw agent：

> 安装 gstack：运行 `git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup` 为 Claude Code 安装 gstack。然后在 `AGENTS.md` 中添加一个 “Coding Tasks”（编码任务）区块，内容为：在为编码工作启动 Claude Code 会话时，告知会话使用 gstack 技能。包含以下示例 —— 安全审计：“加载 gstack。运行 /cso”，代码审查：“加载 gstack。运行 /review”，QA 测试 URL：“加载 gstack。运行 /qa https://...”，端到端构建功能：“加载 gstack。运行 /autoplan，执行计划，然后运行 /ship”，构建前先规划：“加载 gstack。运行 /office-hours 然后 /autoplan。保存计划，不要直接实现。”

**设置完成后，只需自然地向你的 OpenClaw agent 描述需求：**

| 你说 | 会发生什么 |
|---------|-------------|
| "Fix the typo in README" | 简单任务 —— Claude Code 会话即可处理，无需 gstack |
| "Run a security audit on this repo" | 启动附带 `Run /cso` 的 Claude Code 会话 |
| "Build me a notifications feature" | 启动附带 /autoplan → 实现 → /ship 的 Claude Code 会话 |
| "Help me plan the v2 API redesign" | 启动附带 /office-hours → /autoplan，并保存计划的 Claude Code 会话 |

有关高级路由分发和 gstack-lite/gstack-full 提示词模板，请参阅 [docs/OPENCLAW.md](docs/OPENCLAW.md)。

### 原生 OpenClaw 技能（通过 ClawHub）

四种直接在 OpenClaw agent 中运行的方法论技能，无需 Claude Code 会话。从 ClawHub 安装：

```
clawhub install gstack-openclaw-office-hours gstack-openclaw-ceo-review gstack-openclaw-investigate gstack-openclaw-retro
```

| Skill | 功能说明 |
|-------|-------------|
| `gstack-openclaw-office-hours` | 通过6个强制性问题进行产品深度剖析 |
| `gstack-openclaw-ceo-review` | 提供战略挑战，支持4种范围模式 |
| `gstack-openclaw-investigate` | 根因调试方法论 |
| `gstack-openclaw-retro` | 每周工程复盘 |

这些是对话式技能。你的 OpenClaw agent 可通过聊天直接运行它们。

### 其他 AI Agent

gstack 兼容10种 AI 编程 agent，不仅限于 Claude Code。安装脚本会自动检测你已安装的 agent：

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/gstack
cd ~/gstack && ./setup
```

或使用 `./setup --host <name>` 指定特定 agent：

| Agent | Flag | Skills install to |
|-------|------|-------------------|
| OpenAI Codex CLI | `--host codex` | `~/.codex/skills/gstack-*/` |
| OpenCode | `--host opencode` | `~/.config/opencode/skills/gstack-*/` |
| Cursor | `--host cursor` | `~/.cursor/skills/gstack-*/` |
| Factory Droid | `--host factory` | `~/.factory/skills/gstack-*/` |
| Slate | `--host slate` | `~/.slate/skills/gstack-*/` |
| Kiro | `--host kiro` | `~/.kiro/skills/gstack-*/` |
| Hermes | `--host hermes` | `~/.hermes/skills/gstack-*/` |
| GBrain (mod) | `--host gbrain` | `~/.gbrain/skills/gstack-*/` |

**想为其他 agent 添加支持？** 请参阅 [docs/ADDING_A_HOST.md](docs/ADDING_A_HOST.md)。只需一个 TypeScript 配置文件，零代码修改。

## 实际运行效果

```
You:    I want to build a daily briefing app for my calendar.
You:    /office-hours
Claude: [asks about the pain — specific examples, not hypotheticals]

You:    Multiple Google calendars, events with stale info, wrong locations.
        Prep takes forever and the results aren't good enough...

Claude: I'm going to push back on the framing. You said "daily briefing
        app." But what you actually described is a personal chief of
        staff AI.
        [extracts 5 capabilities you didn't realize you were describing]
        [challenges 4 premises — you agree, disagree, or adjust]
        [generates 3 implementation approaches with effort estimates]
        RECOMMENDATION: Ship the narrowest wedge tomorrow, learn from
        real usage. The full vision is a 3-month project — start with
        the daily briefing that actually works.
        [writes design doc → feeds into downstream skills automatically]

You:    /plan-ceo-review
        [reads the design doc, challenges scope, runs 10-section review]

You:    /plan-eng-review
        [ASCII diagrams for data flow, state machines, error paths]
        [test matrix, failure modes, security concerns]

You:    Approve plan. Exit plan mode.
        [writes 2,400 lines across 11 files. ~8 minutes.]

You:    /review
        [AUTO-FIXED] 2 issues. [ASK] Race condition → you approve fix.

You:    /qa https://staging.myapp.com
        [opens real browser, clicks through flows, finds and fixes a bug]

You:    /ship
        Tests: 42 → 51 (+9 new). PR: github.com/you/app/pull/42
```

你说“构建一个每日简报应用”。Agent 回复说“你实际上是在构建一个人工首席官 AI”——因为它听懂了你的痛点，而非仅仅照搬你的功能需求。八个命令，端到端闭环。这不仅仅是一个 Copilot（辅助工具），而是一个团队。

## 工作流冲刺

gstack 是一套流程，而非单纯的工具集合。技能按 Sprint（迭代周期）的顺序运行：

**Think → Plan → Build → Review → Test → Ship → Reflect** -> **思考 → 规划 → 构建 → 审查 → 测试 → 发布 → 复盘**

每个技能都为下一个提供输入。`/office-hours` 编写的设计文档会被 `/plan-ceo-review` 读取。`/plan-eng-review` 编写的测试计划会被 `/qa` 接手。`/review` 捕获的 bug 会由 `/ship` 验证是否已修复。没有遗漏，因为每一步都知道前序步骤的内容。

| Skill | Your specialist | What they do |
|-------|----------------|--------------|
| `/office-hours` | **YC Office Hours** | 从这里开始。六个强制性问题在写代码前重构你的产品思路。挑战你的初始框架，质疑前提假设，生成替代实施方案。设计文档会自动传递给下游所有技能。 |
| `/plan-ceo-review` | **CEO / Founder** | 重新审视问题。找出隐藏在需求中的“10星”产品潜力。四种模式：扩展、选择性扩展、维持范围、缩减。 |
| `/plan-eng-review` | **Eng Manager** | 锁定架构、数据流、图表、边界情况和测试用例。将隐藏假设显式化。 |
| `/plan-design-review` | **Senior Designer** | 对每个设计维度进行0-10分评分，解释满分标准，然后修改计划以达到该目标。AI 垃圾代码检测。交互式——每项设计决策仅询问一次用户。 |
| `/plan-devex-review` | **Developer Experience Lead** | 交互式开发者体验（DX）审查：探索开发者画像、对标竞品 TTHW（Time To Hello World）、设计你的“魔法时刻”、逐步追踪摩擦点。三种模式：DX 扩展、DX 打磨、DX 分诊。20-45个强制性问题。 |
| `/design-consultation` | **Design Partner** | 从零构建完整的设计系统。调研市场现状，提出创意风险方案，生成逼真的产品原型。 |
| `/review` | **Staff Engineer** | 找出能通过 CI 但会在生产环境引发故障的 bug。自动修复明显问题。标记完整性缺口。 |
| `/investigate` | **Debugger** | 系统性根因调试。铁律：不调查绝不修复。追踪数据流、测试假设，最多连续失败3次后停止。 |
| `/design-review` | **Designer Who Codes** | 与 `/plan-design-review` 相同的审计流程，随后修复发现的问题。原子化提交，附带前后对比截图。 |
| `/devex-review` | **DX Tester** | 实时开发者体验审查。实际测试你的新手引导：浏览文档、尝试入门流程、计时 TTHW、截取错误画面。与 `/plan-devex-review` 评分进行对比——检验规划是否贴合实际的“回旋镖”机制。 |
| `/design-shotgun` | **Design Explorer** | “给我看选项”。生成4-6个 AI 原型变体，在浏览器中打开对比看板收集反馈并迭代。品味记忆会学习你的偏好。重复直到满意为止，然后交给 `/design-html`。 |
| `/design-html` | **Design Engineer** | 将原型转化为实际可用的生产级 HTML。使用 Pretext 实现计算型文本布局：文本自动重排、高度自适应内容、布局动态响应。30KB，零依赖。检测 React/Svelte/Vue。根据设计类型（落地页/仪表盘/表单）智能路由 API。输出的是可交付产品，而非演示稿。 |
| `/qa` | **QA Lead** | 测试你的应用，发现 bug，通过原子化提交修复并重新验证。为每次修复自动生成回归测试。 |
| `/qa-only` | **QA Reporter** | 方法与 `/qa` 相同，但仅输出报告。纯 Bug 报告，不修改代码。 |
| `/pair-agent` | **Multi-Agent Coordinator** | 与任何 AI agent 共享浏览器。一条命令，一次粘贴，即刻连接。兼容 OpenClaw、Hermes、Codex、Cursor 或任何支持 curl 的工具。每个 agent 独占一个标签页。自动启动 headed 模式以便你全程观看。自动开启 ngrok 隧道供远程 agent 使用。作用域令牌、标签页隔离、限流、行为归属追踪。 |
| `/cso` | **Chief Security Officer** | OWASP Top 10 + STRIDE 威胁模型。零噪音：排除17个误报项，8/10+置信度门槛，独立验证发现结果。每项发现均附带具体的利用场景。 |
| `/ship` | **Release Engineer** | 同步主分支、运行测试、审计覆盖率、推送代码、创建 PR。若未配置测试框架则自动初始化。 |
| `/land-and-deploy` | **Release Engineer** | 合并 PR，等待 CI 并部署，验证生产环境健康状态。从“已批准”到“生产环境验证通过”，仅需一条命令。 |
| `/canary` | **SRE** | 发布后监控循环。监测控制台错误、性能回退和页面故障。 |
| `/benchmark` | **Performance Engineer** | 建立页面加载时间、Core Web Vitals 和资源大小的基线。每个 PR 前后进行对比。 |
| `/document-release` | **Technical Writer** | 更新所有项目文档以匹配最新交付内容。自动捕获过时的 README。 |
| `/retro` | **Eng Manager** | 团队感知的每周复盘。按人员拆解、追踪交付连胜记录、测试健康度趋势和成长机会。`/retro global` 跨所有项目及 AI 工具（Claude Code, Codex, Gemini）运行。 |
| `/browse` | **QA Engineer** | 赋予 Agent “眼睛”。真实 Chromium 浏览器，支持真实点击和截图。每条命令约100ms。`/open-gstack-browser` 启动 GStack Browser（带侧边栏、反机器人隐身模式和自动模型路由）。 |
| `/setup-browser-cookies` | **Session Manager** | 从你的真实浏览器（Chrome, Arc, Brave, Edge）导入 Cookie 到无头会话。测试需认证的页面。 |
| `/autoplan` | **Review Pipeline** | 一条命令，生成完全审查过的计划。自动运行 CEO → 设计 → 工程审查，并内置决策原则。仅将品味相关决策交由你审批。 |
| `/learn` | **Memory** | 管理跨会话的 gstack 学习记录。回顾、搜索、清理和导出项目特定的模式、陷阱和偏好。学习成果在会话间累积，使 gstack 随时间越来越了解你的代码库。 |

### 我该使用哪种审查？

| Building for... | Plan stage (before code) | Live audit (after shipping) |
|-----------------|--------------------------|----------------------------|
| **End users** (UI, web app, mobile) | `/plan-design-review` | `/design-review` |
| **Developers** (API, CLI, SDK, docs) | `/plan-devex-review` | `/devex-review` |
| **Architecture** (data flow, perf, tests) | `/plan-eng-review` | `/review` |
| **All of the above** | `/autoplan` (runs CEO → design → eng → DX, auto-detects which apply) | — |

### 强力工具

| Skill | What it does |
|-------|-------------|
| `/codex` | **Second Opinion（独立意见）** —— OpenAI Codex CLI 的独立代码审查。三种模式：review（通过/失败门槛）、adversarial challenge（对抗性挑战）和 open consultation（开放咨询）。当 `/review` 与 `/codex` 均运行后，提供跨模型分析对比。 |
| `/careful` | **Safety Guardrails（安全护栏）** —— 在执行破坏性命令前发出警告（rm -rf, DROP TABLE, force-push）。输入 "be careful" 激活。可随时覆盖任何警告。 |
| `/freeze` | **Edit Lock（编辑锁定）** —— 将文件编辑限制在单个目录内。防止调试时意外修改范围外的代码。 |
| `/guard` | **Full Safety（完整安全）** —— 一条命令同时启用 `/careful` + `/freeze`。生产环境工作的最高安全防护。 |
| `/unfreeze` | **Unlock（解锁）** —— 移除 `/freeze` 边界限制。 |
| `/open-gstack-browser` | **GStack Browser** —— 启动 GStack Browser，内置侧边栏、反机器人隐身模式、自动模型路由（Sonnet 用于操作，Opus 用于分析）、一键 Cookie 导入及 Claude Code 集成。支持清理页面、智能截图、编辑 CSS 并将信息传回终端。 |
| `/setup-deploy` | **Deploy Configurator（部署配置器）** —— 为 `/land-and-deploy` 提供一次性设置。自动检测你的平台、生产环境 URL 和部署命令。 |
| `/setup-gbrain` | **GBrain Onboarding（GBrain 引导）** —— 5分钟内从零完成 gbrain 运行。支持 PGLite 本地模式、Supabase 已有 URL 接入，或通过 Management API 自动创建新 Supabase 项目。包含 Claude Code MCP 注册及 per-repo 信任三元组（read-write/read-only/deny）。[完整指南](USING_GBRAIN_WITH_GSTACK.md)。 |
| `/sync-gbrain` | **Keep Brain Current（保持知识库更新）** —— 通过 `gbrain sources add` + `gbrain sync --strategy code` 将当前仓库代码重新索引至 gbrain，刷新 CLAUDE.md 中的 `## GBrain Search Guidance` 区块，并在能力检查失败时自动移除过时指引。支持 `--incremental`（默认）、`--full`、`--dry-run`。幂等操作，可安全重复运行。 |
| `/gstack-upgrade` | **Self-Updater（自更新器）** —— 将 gstack 升级至最新版本。自动检测全局或 vendored 安装模式并同步两者，展示变更日志。 |

### 新增独立命令行工具（v0.19）

除斜杠命令技能外，gstack 还提供了独立的 CLI 用于处理不适合在会话内执行的工作流：

| Command | What it does |
|---------|-------------|
| `gstack-model-benchmark` | **Cross-model benchmark（跨模型基准测试）** —— 将同一提示词依次输入 Claude、GPT（通过 Codex CLI）和 Gemini；对比延迟、Token数、成本及（可选的）LLM-judge 质量评分。自动检测各提供商认证，不可用提供商会优雅跳过。支持表格、JSON 或 Markdown 输出。`--dry-run` 可在不消耗 API 调用前验证参数与认证状态。 |
| `gstack-taste-update` | **Design taste learning（设计品味学习）** —— 将 `/design-shotgun` 中的审批与拒绝记录写入持久化的 per-project 品味配置文件。每周衰减5%。反馈至后续变体生成，使系统真正学会你的偏好选择。 |

### 连续检查点模式（默认本地存储，需手动开启）

运行 `gstack-config set checkpoint_mode continuous` 后，技能会在你操作过程中自动提交带有 `WIP:` 前缀和结构化 `[gstack-context]` 正文（包含决策、剩余工作、失败方案）的变更。支持崩溃恢复和上下文切换。`/context-restore` 读取这些提交以重建会话状态。`/ship` 在 PR 合并前会过滤并压缩 WIP 提交（保留非 WIP 提交），以保持 `bisect` 干净。推送操作需通过 `checkpoint_push=true` 手动开启——默认为仅本地，避免每次 WIP 提交都触发 CI。

### 领域技能与原始 CDP 逃生舱口

两项新的浏览器基础功能将随时间增强 gstack agent：

- **`$B domain-skill save`** —— Agent 保存针对特定站点的备注（例如“LinkedIn 的‘申请职位’按钮位于 iframe 中”），下次访问该域名时自动触发。隔离状态 → 成功使用3次后转为活跃 → 可选跨项目推广至全局 `$B domain-skill promote-to-global`。存储位置与 `/learn` 的项目学习文件并列。完整参考： **[docs/domain-skills.md](docs/domain-skills.md)**。
- **`$B cdp <Domain.method>`** —— 针对精心设计的命令未覆盖的罕见场景，提供原始 Chrome DevTools Protocol (CDP) 逃生舱口。默认拒绝：方法必须显式添加到 `browse/src/cdp-allowlist.ts` 并附有一行说明。两级互斥锁将浏览器级 CDP 调用与标签页工作串行化。数据导出类方法的输出会包裹在 UNTRUSTED（不可信）信封中。

> 想要无限制、无白名单、无守护进程的原始 CDP，仅作为 Agent 到 Chrome 的轻量传输层？[browser-use/browser-harness-js](https://github.com/browser-use/browser-harness-js) 采用了不同的理念（Agent 自编写辅助函数 vs gstack 精心设计的命令），适合不想依赖 gstack 安全栈的用户。两者可共存：gstack 的 `$B cdp` 和 harness 均可通过 Playwright 的 `newCDPSession` 附加到同一 Chrome 实例。

**[各技能的深度解析、示例与哲学理念 →](docs/skills.md)**

### Karpathy 提出的四种失败模式？已全部覆盖。

Andrej Karpathy 的 [AI coding rules]（17K stars）精准指出了四种失败模式：错误假设、过度复杂化、正交编辑、命令式优于声明式。gstack 的工作流技能强制落实了全部四项。`/office-hours` 在写代码前将隐藏假设显式化。“困惑协议”阻止 Claude 对架构决策进行猜测。`/review` 捕获不必要的复杂度和旁路修改。`/ship` 通过测试优先执行将任务转化为可验证目标。如果你已在使用 Karpathy 风格的 CLAUDE.md 规则，gstack 就是让它们在完整 Sprint（而非单次提示词）中生效的工作流强制层。

## 并行迭代

单个 Sprint 下 gstack 表现良好。同时运行十个时，才会真正展现威力。

**设计是核心。** `/design-consultation` 从零构建你的设计系统，调研现有方案，提出创意风险，并编写 `DESIGN.md`。但真正的魔法在于“霰弹枪到 HTML”的流水线。

**探索功能依靠 `/design-shotgun`。** 描述你的需求。它使用 GPT Image 生成4-6个 AI 原型变体。随后在浏览器中打开对比看板，将所有变体并排展示。你挑选喜欢的版本，留下反馈（“增加留白”、“标题更醒目”、“去掉渐变”），它会生成新一轮变体。重复直到满意为止。品味记忆会在几轮后生效，开始偏向你真正偏好的风格。不再需要靠文字描述愿景指望 AI 猜中你的心思。你可以看到选项、挑选优秀的版本并视觉化迭代。

**`/design-html` 将其变为现实。** 将已批准的 Mockup（来自 `/design-shotgun`、CEO 规划、设计审查或纯文字描述）转化为生产级 HTML/CSS。不是那种在一个视口宽度下正常、其他地方全崩的 AI HTML。它使用 Pretext 实现计算型文本布局：文本在缩放时真正重排，高度自适应内容，布局动态响应。30KB 开销，零依赖。检测你的框架（React, Svelte, Vue）并输出正确格式。智能 API 路由根据页面类型（落地页、仪表盘、表单或卡片布局）选择不同的 Pretext 模式。输出的是你实际会交付的产品，而非演示稿。

**`/qa` 是巨大的效率突破。** 它让我将并行工作流从6个扩展到12个。Claude Code 说“我看到问题了”，然后真正修复它、生成回归测试并验证——这彻底改变了我的工作方式。Agent 现在有了眼睛。

**智能审查路由。** 就像高效运转的初创公司一样：CEO 不必查看基础设施 bug 修复，后端变更无需设计审查。gstack 会跟踪已运行的审查类型，判断哪些适用，并自动执行最合理的操作。发布前的“审查就绪仪表盘”让你清楚当前进度。

**全面测试。** 如果项目缺少测试框架，`/ship` 会自动从零初始化。每次运行 `/ship` 都会生成覆盖率审计报告。每个 `/qa` 的 bug 修复都会自动生成回归测试。100% 测试覆盖率是目标——让“直觉式编码 (vibe coding)”变得安全，而非盲目冒险（yolo coding）。

**`/document-release` 是你从未拥有过的工程师。** 它读取项目中的所有文档文件，交叉比对代码变更，自动更新所有已过时的内容。README、ARCHITECTURE、CONTRIBUTING、CLAUDE.md、TODOS —— 全部保持最新。现在 `/ship` 会自动调用它——无需额外命令即可保持文档同步。

**真实浏览器模式。** `/open-gstack-browser` 启动 GStack Browser，这是一个内置反机器人隐身技术、自定义品牌标识和侧边栏扩展的 AI 控制 Chromium。Google 和 NYTimes 等网站无需验证码即可正常运行。菜单栏显示“GStack Browser”而非“Chrome for Testing”。你的常规 Chrome 浏览器保持 untouched（不受影响）。所有现有的浏览命令均无缝兼容。`$B disconnect` 返回无头模式。只要窗口未关闭，浏览器就会一直运行……没有空闲超时中断你的工作。

**侧边栏 Agent —— 你的 AI 浏览器助手。** 在 Chrome 侧面板输入自然语言，子 Claude 实例会执行操作。“导航到设置页面并截图。”“用测试数据填写此表单。”“遍历列表中的所有项目并提取价格。”侧边栏自动路由至合适的模型：Sonnet 用于快速操作（点击、导航、截图），Opus 用于阅读和分析。每项任务最多分配5分钟。侧边栏 Agent 在隔离会话中运行，不会干扰你的主 Claude Code 窗口。一键从侧边栏底部导入 Cookie。

**个人自动化。** 侧边栏 Agent 不仅用于开发工作流。示例：“浏览我家孩子的学校家长门户，将所有其他家长的姓名、电话和照片添加到我的 Google 联系人中。”两种认证方式：(1) 在 headed 浏览器中登录一次，会话持久化；或 (2) 点击侧边栏底部的“cookies”按钮从真实 Chrome 导入 Cookie。认证成功后，Claude 导航目录、提取数据并创建联系人。

**提示词注入防御。** 恶意网页会试图劫持你的侧边栏 Agent。gstack 提供分层防御：浏览器内置22MB ML 分类器，在本地扫描每个页面和工具输出；Claude Haiku 转录检查对完整对话结构进行投票；系统提示中的随机金丝雀令牌可捕获跨文本、工具参数、URL 和文件写入的会话数据泄露尝试；裁决组合器要求两个分类器达成一致才会拦截（防止 Stack Overflow 类指令页面上的单模型误报）。侧边栏头部显示盾牌图标指示状态（绿/黄/红）。可通过 `GSTACK_SECURITY_ENSEMBLE=deberta` 选择加入721MB DeBERTa-v3 集成，实现2-of-3投票。紧急关闭开关：`GSTACK_SECURITY_OFF=1`。完整技术栈见 [ARCHITECTURE.md](ARCHITECTURE.md#prompt-injection-defense-sidebar-agent)。

**AI 卡住时的浏览器交接。** 遇到验证码、认证墙或 MFA 提示？执行 `$B handoff`，会在可见的 Chrome 中打开完全相同的页面，保留所有 Cookie 和标签页。解决问题后告诉 Claude 已完成，执行 `$B resume` 即可无缝续接。Agent 甚至在连续失败3次后会自动建议此操作。

**`/pair-agent` 实现跨 Agent 协同。** 你正在使用 Claude Code，同时还在运行 OpenClaw、Hermes 或 Codex。你想让它们共同查看同一个网站？输入 `/pair-agent`，选择你的 agent，GStack Browser 窗口就会打开供你观看。该技能会打印一段指令块。将此粘贴到其他 agent 的聊天中。它会交换一次性设置密钥获取会话令牌，创建自己的标签页并开始浏览。你可以在同一浏览器中看到两个 Agent 各自在独立标签页工作，互不干扰。如果安装了 ngrok，隧道会自动启动，使其他 agent 可运行在完全不同的机器上。同机 agent 则享有零摩擦快捷方式，直接写入凭证。这是不同厂商的 AI Agent 首次通过共享浏览器实现真正安全的协同：作用域令牌、标签页隔离、限流、域名限制和行为归属追踪。

**多 AI 独立意见。** `/codex` 获取来自 OpenAI Codex CLI 的独立审查——一个完全不同的 AI 审视相同的代码变更。三种模式：带通过/失败门槛的代码审查、主动尝试破坏你代码的对抗性挑战，以及保持会话连续性的开放咨询。当 `/review`（Claude）和 `/codex`（OpenAI）都审查了同一分支时，你会获得跨模型分析结果，显示哪些发现是重叠的，哪些是各自独有的。

**按需安全护栏。** 输入“be careful”，`/careful` 会在执行任何破坏性命令前发出警告（rm -rf、DROP TABLE、force-push、git reset --hard）。`/freeze` 在调试时将编辑限制在单个目录内，防止 Claude 意外“修复”无关代码。`/guard` 同时激活两者。`/investigate` 会自动将范围冻结至正在调查的模块。

**主动技能建议。** gstack 会识别你当前所处的阶段——头脑风暴、审查、调试或测试，并推荐合适的技能。不喜欢？输入“stop suggesting”，它会在跨会话中记住你的偏好。

## 并行运行 10-15 个迭代

单个 Sprint 下 gstack 已很强大。同时运行十个时，将带来颠覆性改变。

[Conductor](https://conductor.build) 并行运行多个 Claude Code 会话——每个都在独立的隔离工作区中。一个会话在新构想上运行 `/office-hours`，另一个在 PR 上进行 `/review`，第三个实现功能，第四个对预发环境运行 `/qa`，还有六个在其他分支上工作。全部同时进行。我通常同时运行10-15个并行迭代——这目前是实际可行的上限。

正是 Sprint 结构让并行化成为可能。没有流程，十个 agent 就是十种混乱来源。有了流程（思考、规划、构建、审查、测试、发布），每个 agent 都清楚自己该做什么以及何时停止。你像 CEO 管理团队一样管理它们：关注关键决策，其余的放手运行。

### 语音输入（AquaVoice、Whisper 等）

gstack 技能支持语音友好型触发短语。自然地说出你的需求——“运行安全检查”、“测试网站”、“执行工程审查”——即可激活对应技能。无需记忆斜杠命令名称或缩写。

## 卸载

### 选项 1：运行卸载脚本

如果 gstack 已安装在本地：

```bash
~/.claude/skills/gstack/bin/gstack-uninstall
```

该脚本会处理技能文件、符号链接、全局状态（`~/.gstack/`）、项目级状态、浏览守护进程和临时文件。使用 `--keep-state` 保留配置和分析数据。使用 `--force` 跳过确认提示。

### 选项 2：手动移除（无本地仓库）

如果你未克隆该仓库（例如通过 Claude Code 粘贴安装后删除了副本）：

```bash
# 1. Stop browse daemons
pkill -f "gstack.*browse" 2>/dev/null || true

# 2. Remove per-skill directories whose SKILL.md points into gstack/
find ~/.claude/skills -mindepth 1 -maxdepth 1 -type d ! -name gstack 2>/dev/null |
while IFS= read -r dir; do
  link="$dir/SKILL.md"
  [ -L "$link" ] || continue
  target=$(readlink "$link" 2>/dev/null) || continue
  case "$target" in
    gstack/*|*/gstack/*)
      rm -f "$link"
      rmdir "$dir" 2>/dev/null || true
      ;;
  esac
done

# 3. Remove gstack
rm -rf ~/.claude/skills/gstack

# 4. Remove global state
rm -rf ~/.gstack

# 5. Remove integrations (skip any you never installed)
rm -rf ~/.codex/skills/gstack* 2>/dev/null
rm -rf ~/.factory/skills/gstack* 2>/dev/null
rm -rf ~/.kiro/skills/gstack* 2>/dev/null
rm -rf ~/.openclaw/skills/gstack* 2>/dev/null

# 6. Remove temp files
rm -f /tmp/gstack-* 2>/dev/null

# 7. Per-project cleanup (run from each project root)
rm -rf .gstack .gstack-worktrees .claude/skills/gstack 2>/dev/null
rm -rf .agents/skills/gstack* .factory/skills/gstack* 2>/dev/null
```

### 清理 CLAUDE.md

卸载脚本不会自动编辑 `CLAUDE.md`。在添加过 gstack 的每个项目中，手动删除 `## gstack` 和 `## Skill routing` 区块。

### Playwright

macOS 下的 `~/Library/Caches/ms-playwright/` 目录会保留，因为其他工具可能共享它。如果确认无其他用途可自行删除。

---

**免费、MIT 开源协议。永久免费，无高级版，无需排队。** 我公开了自己构建软件的方法。你可以 Fork 它并打造属于自己的版本。

> **我们正在招聘。** 想以 AI 编程速度交付真实产品，并帮助加固 gstack？来 YC 工作 —— [ycombinator.com/software](https://ycombinator.com/software) 。极具竞争力的薪资与股权。工作地点：旧金山 Dogpatch 区。

## GBrain —— 为你的编程 Agent 提供持久化知识

[GBrain](https://github.com/garrytan/gbrain) 是 AI agent 的持久化知识库——可将其视为你的 agent 在会话间真正保留的记忆。GStack 让你只需一条命令即可从零起步，实现“运行正常、agent 可随时调用”的状态。

```bash
/setup-gbrain
```

三条路径，任选其一：

- **Supabase（已有 URL）** —— 你的云端 agent 已配置好知识库；粘贴 Session Pooler URL，此电脑即可共享同一数据。
- **Supabase（自动创建）** —— 粘贴 Supabase 个人访问令牌；该技能会自动创建新项目，轮询至健康状态，获取 Pooler URL 并交给 `gbrain init`。端到端约需90秒。
- **PGLite（本地）** —— 零账号、零网络依赖，约30秒完成。仅在此 Mac 上隔离运行知识库。非常适合先试后买；后续可通过 `/setup-gbrain --switch` 迁移至 Supabase。

初始化完成后，该技能会提示将 gbrain 注册为 Claude Code 的 MCP 服务器（`claude mcp add gbrain -- gbrain serve`），使 `gbrain search`、`gbrain put_page` 等成为一等公民的类型化工具——而非 bash shell 调用。

**保持知识库更新。** 在任何仓库运行 `/sync-gbrain` 即可将其代码重新索引到 gbrain（默认增量同步，使用 `--full` 进行全量重建，`--dry-run` 预览效果）。该技能会通过 `gbrain sources add` 将当前工作目录注册为联邦源，执行 `gbrain sync --strategy code`，并在项目的 CLAUDE.md 中写入 `## GBrain Search Guidance` 区块，使 agent 优先使用 `gbrain search`/`code-def`/`code-refs` 而非 Grep。如果能力检查失败，该区块会自动移除——避免指向未安装工具的过时指引。

**按远程仓库的信任策略。** 你机器上的每个仓库都会分配以下三级之一：

- `read-write`（读写）—— Agent 可搜索知识库，并从此仓库写回新页面。
- `read-only`（只读）—— Agent 仅可搜索，永不写入（最适合多客户顾问：在 Client B 的仓库中工作时，只能搜索共享知识库，避免用 Client A 的数据污染它）。
- `deny`（拒绝）—— 完全不与 gbrain 交互。

该技能会对每个仓库询问一次。决策会在同一远程仓库的不同工作树和分支间保持持久化。

**GStack 记忆同步（独立功能，复用私有仓库基础设施）。** 可选地将你的 gstack 状态（学习记录、CEO 规划、设计文档、复盘记录、开发者画像）推送至私有 Git 仓库，让你的记忆跨设备跟随。包含一次性隐私提示（全允许/仅保留制品/关闭），以及深度防御型密钥扫描器，在数据离开本地前拦截 AWS 密钥、令牌、PEM 块和 JWT。

```bash
gstack-brain-init
```

**完整指南（涵盖所有场景、参数、辅助工具和排错步骤）：** [USING_GBRAIN_WITH_GSTACK.md](USING_GBRAIN_WITH_GSTACK.md)

其他参考：[docs/gbrain-sync.md](docs/gbrain-sync.md)（同步专项指南） • [docs/gbrain-sync-errors.md](docs/gbrain-sync-errors.md)（错误索引）

## 文档

| Doc | What it covers |
|-----|---------------|
| [Skill Deep Dives](docs/skills.md) | 各技能的哲学理念、示例与工作流（含 Greptile 集成） |
| [Builder Ethos](ETHOS.md) | 构建者理念：煮湖理论、先搜后建、知识三层架构 |
| [Using GBrain with GStack](USING_GBRAIN_WITH_GSTACK.md) | `/setup-gbrain` 的所有路径、参数、辅助工具与排错步骤 |
| [GBrain Sync](docs/gbrain-sync.md) | 跨设备记忆配置、隐私模式与故障排查 |
| [Architecture](ARCHITECTURE.md) | 架构决策与系统内部实现 |
| [Browser Reference](BROWSER.md) | `/browse` 完整命令参考 |
| [Contributing](CONTRIBUTING.md) | 开发环境配置、测试、贡献者模式与开发者模式 |
| [Changelog](CHANGELOG.md) | 各版本更新内容 |

## 隐私与分析数据

gstack 包含**可选（opt-in）**的使用分析数据，以帮助改进项目。具体机制如下：

- **默认关闭。** 除非你明确同意，否则不会向任何地方发送数据。
- **首次运行时**，gstack 会询问是否共享匿名使用数据。你可选择拒绝。
- **发送内容（若开启）：** 技能名称、耗时、成功/失败状态、gstack 版本、操作系统。仅此而已。
- **绝不发送：** 代码、文件路径、仓库名、分支名、提示词或任何用户生成内容。
- **随时更改：** 运行 `gstack-config set telemetry off` 可立即禁用所有数据收集。

数据存储于 [Supabase](https://supabase.com)（开源 Firebase 替代方案）。架构定义在 [`supabase/migrations/`](supabase/migrations/) 中——你可自行验证收集的确切内容。仓库中的 Supabase 发布密钥为公开密钥（类似 Firebase API Key）——行级安全策略已拒绝所有直接访问权限。分析数据通过经过验证的边缘函数流转，强制执行架构检查、事件类型白名单和字段长度限制。

**本地分析始终可用。** 运行 `gstack-analytics` 即可查看基于本地 JSONL 文件的个人使用仪表盘——无需依赖远程数据。

## 故障排查

- **技能未显示？** 执行 `cd ~/.claude/skills/gstack && ./setup`
- **`/browse` 失败？** 执行 `cd ~/.claude/skills/gstack && bun install && bun run build`
- **安装版本过旧？** 运行 `/gstack-upgrade` ——或在 `~/.gstack/config.yaml` 中设置 `auto_upgrade: true`
- **想要更短的命令？** 执行 `cd ~/.claude/skills/gstack && ./setup --no-prefix` —— 将命令从 `/gstack-qa` 切换为 `/qa`。你的选择会在后续升级中自动记忆。
- **想要带命名空间的命令？** 执行 `cd ~/.claude/skills/gstack && ./setup --prefix` —— 将命令从 `/qa` 切换为 `/gstack-qa`。若同时运行其他技能包，此选项非常有用。
- **Codex 提示“因 SKILL.md 无效而跳过加载技能”？** 你的 Codex 技能描述已过期。修复：执行 `cd ~/.codex/skills/gstack && git pull && ./setup --host codex` —— 或对于仓库本地安装：`cd "$(readlink -f .agents/skills/gstack)" && git pull && ./setup --host codex`
- **Windows 用户：** gstack 可通过 Git Bash 或 WSL 在 Windows 11 上运行。除 Bun 外还需安装 Node.js——Bun 在 Windows 上与 Playwright 的管道传输存在已知 Bug（[bun#4253](https://github.com/oven-sh/bun/issues/4253)）。浏览服务会自动降级至 Node.js。请确保 `bun` 和 `node` 均已加入 PATH。
- **Claude 提示无法识别技能？** 请确保项目的 `CLAUDE.md` 包含 gstack 区块。添加以下内容：

```
## gstack
Use /browse from gstack for all web browsing. Never use mcp__claude-in-chrome__* tools.
Available skills: /office-hours, /plan-ceo-review, /plan-eng-review, /plan-design-review,
/design-consultation, /design-shotgun, /design-html, /review, /ship, /land-and-deploy,
/canary, /benchmark, /browse, /open-gstack-browser, /qa, /qa-only, /design-review,
/setup-browser-cookies, /setup-deploy, /setup-gbrain, /sync-gbrain, /retro, /investigate, /document-release,
/codex, /cso, /autoplan, /pair-agent, /careful, /freeze, /guard, /unfreeze, /gstack-upgrade, /learn.
```

## 许可证

MIT。永久免费。去构建些东西吧。