# GBrain

**搜索给你原始页面，GBrain 给你答案。** 它是你的 AI Agent 一直缺失的大脑层——唯一一个在单一模块中完成综合、图遍历和差距分析的组件。你可以在它之上运行完整的自主 Agent，或者只需一条命令就将其接入 Claude Code 或 Codex 作为增强型检索层；无论哪种方式，你的编程 Agent 都不会再对非代码内容“失忆”了。

我是 Y Combinator 的总裁兼 CEO Garry Tan。我构建 GBrain 是为了运行我自己的 AI Agent。它是我的 OpenClaw 和 Hermes 部署背后的生产级大脑：**146,646 个页面、24,585 个人、5,339 家公司**，以及 66 个自主运行的 cron 任务。当我睡觉时，我的 Agent 会摄入会议记录、邮件、推文、语音通话和原创想法。它会丰富遇到的每个人和公司信息。它会在夜间修复自身的引用并整合记忆。我醒来时会比睡前更聪明——你也会如此。

**现在它也能作为公司大脑运行。** 团队中的每个人都会获得独立的大脑切片，权限按登录账号隔离。当你进行查询时，你只能看到自己有权查看的内容——绝不会暴露他人的笔记或其他团队的数据。我们 fuzz-tested（模糊测试）了所有读取大脑的方式（搜索、列表、查找、多源读取），零数据泄露。将 GBrain 作为团队的共享机构记忆部署吧——这正是 YC 在《初创企业需求书》(Request for Startups) 中刚刚提出的 [company-brain](https://www.ycombinator.com/rfs#company-brain) 形态。如果你正在该领域开发，不妨直接基于此构建。**[教程：将 GBrain 设置为你的公司大脑 →](docs/tutorials/company-brain.md)**

许多个人知识系统只提供关键词匹配和 `grep`。GBrain 具备这些功能，并额外添加了两个无人能同时提供的特性：

- **提供实际答案的综合层。** 跨人物、公司、交易和想法的综合性、引用完善的文本。不是“这里有 10 个提及你查询的片段”，而是带有明确引用的真实答案，并明确指出大脑目前还不知道什么。差距分析（gap analysis）正是改变你使用大脑方式的关键部分。
- **自构建知识图谱。** 每次写入页面都会提取实体引用，并以零 LLM 调用创建类型化边（`attended`, `works_at`, `invested_in`, `founded`, `advises`）。询问“谁在 Acme AI 工作？”或“Bob 本季度投资了什么？”，你将获得纯向量搜索无法触及的答案。基准测试显示：在 240 页的 Opus 生成丰富文本语料库上，**P@5 为 49.1%，R@5 为 97.9%**；相较于禁用图变体以及 ripgrep-BM25 + 纯向量 RAG，**P@5 提升了 31.4 个百分点**。完整的 BrainBench 评分卡位于兄弟仓库 [gbrain-evals](https://github.com/garrytan/gbrain-evals)。

构建一个包含 10 万页的大脑，是为了将其作为战略护城河。为了永不丢失上下文。为了查询你脑海中的内容而无需重新阅读。大脑层让这条护城河变得可用，24/7 的梦境周期（dream cycle）则让它保持敏锐。两者均运行在你的硬件、数据库和你的密钥之上。

与其让聊天中的 Agent 苦苦工作，不如交付一个 24/7 运行的守护进程来摄入、丰富和整合数据。GBrain 正是这样一个通用化的守护进程。安装仅需 30 分钟。你的 Agent 负责执行任务。随着我的个人 Agent 越来越聪明， yours（你的）也会如此。

> **约 30 分钟即可搭建完全可用的大脑。** 数据库在 2 秒内就绪（使用 PGLite，无需服务器）。你只需回答关于 API 密钥的问题。

> **LLM：** 获取 [`llms.txt`](llms.txt) 查看文档地图，或 [`llms-full.txt`](llms-full.txt) 在单次请求中内联核心文档。**Agent：** 从 [`AGENTS.md`](AGENTS.md) 开始（如果你使用 Claude Code，则从 [`CLAUDE.md`](CLAUDE.md) 开始）。

## 实际效果

假设你明天要和 Alice 开会。你想在进入会议室时，记得她负责什么、你们上次何时交谈过以及还有哪些待办事项未解决。以下是你会输入的内容和会得到的回复。

**你提问：**

> “明天见 Alice 之前，我需要知道什么？”

**大多数个人知识工具只会返回一页列表。** 类似这样：

```
1. people/alice — Alice runs engineering at Acme...
2. meetings/2026-03-15-alice-q1 — Q1 product review with Alice...
3. meetings/2026-01-08-acme-kickoff — Kickoff meeting with Acme team...
4. customers/acme — Acme is a series-B fintech we work with...
5. notes/2026-04-22 — Quick chat with Alice about pricing...
```

现在你需要自己打开并阅读这五个页面才能真正做好准备。工具找到了正确的材料，但没有替你完成工作。

**GBrain 会返回带来源的答案：**

```
Alice runs engineering at Acme (a series-B fintech). You last spoke
on April 22 in a quick pricing chat. Three things are still open
from that conversation:

1. She owes you the security review for the new tier
   (deadline was May 1; no update since).
2. You committed to pricing for a 500-seat tier
   (you sent it April 25; no response yet).
3. She mentioned they're hiring a CISO; you said you'd intro
   someone from your network.

Heads up: nothing's been added to the brain about Alice or Acme
since April 22, six weeks ago. She may have replied through email
or Slack DM, channels the brain doesn't see. Worth asking her to
catch up before assuming any of this is still current.
```

每个主张都有对应的来源页面。结尾的“提醒”告诉你大脑目前还不知道什么，这样你可以直接向 Alice 询问，而不是感到意外。刚才的大脑已经替你完成了会前准备。

这就是搜索引擎和大脑的区别。搜索找到页面，而大脑替你阅读并撰写答案。

## 安装

GBrain 专为由 AI Agent 安装和运行而设计。最快的路径是让 Agent 替你完成。下面的 CLI 和 MCP 路径适用于希望手动配置的用户。

### 让 Agent 帮你安装（推荐）

如果你还没有运行 AI Agent 平台，可以从以下两者之一开始。它们都设计为读取并执行 GBrain 的安装协议：

- **[OpenClaw](https://github.com/openclawagents/openclaw)** — 部署 [AlphaClaw on Render](https://render.com/deploy?repo=https://github.com/chrysb/alphaclaw)（一键，8GB+ RAM）
- **[Hermes](https://github.com/openclawagents/hermes)** — 在 [Railway](https://github.com/praveen-ks-2001/hermes-agent-template) 上部署（一键）

然后将以下内容粘贴到你的 Agent 中：

```
Retrieve and follow the instructions at:
https://raw.githubusercontent.com/garrytan/gbrain/master/INSTALL_FOR_AGENTS.md
```

Agent 会安装 GBrain、创建大脑、询问你的 API 密钥、加载 43 项技能、配置梦境周期，并完成端到端验证。约 30 分钟。你回答问题，它负责工作。

> **从未设置过 AI Agent 平台？** [personal-brain tutorial](docs/tutorials/personal-brain.md) 将带你走完整个流程——选择 OpenClaw 或 Hermes、部署它、指向 INSTALL_FOR_AGENTS.md、获取 API 密钥，并验证首次查询。如果上述内容对你来说都是新的，请从这里开始。

### 快速入门：Claude Code 或 Codex

已经在运行 Claude Code 或 Codex？根据你的需求有两种接入方式。

**仅为编程 Agent 提供记忆（推荐起点）。** 启动本地大脑并通过两条命令连接——零服务器、零 token、零隧道：

```bash
gbrain init --pglite                     # 2-second local brain (no Docker)
claude mcp add gbrain -- gbrain serve    # or: codex mcp add gbrain -- gbrain serve
```

**已在远程主机上拥有大脑**（OpenClaw、Hermes 或任何 `gbrain serve --http`）？用一条命令将你的笔记本 Agent 指向它——`--install` 会完成接线并在交接前进行 token 冒烟测试：

```bash
gbrain connect https://your-host/mcp --token gbrain_xxx --install               # Claude Code
gbrain connect https://your-host/mcp --token gbrain_xxx --agent codex --install # Codex
```

**[→ 完整指南：为你的编程 Agent 赋予记忆](docs/tutorials/connect-coding-agent.md)** — 涵盖上述两种路径的端到端流程，以及你需要粘贴到 `CLAUDE.md` / `AGENTS.md` 中的大脑优先协议和四个能真正改变你工作习惯的习惯。

### 将完整的自主设置安装到你现有的 Agent 中

想要全套功能——本地大脑、43 项技能、夜间自动丰富的梦境周期？将其粘贴到 Codex、Claude Code、Cursor 或其他编程 Agent 中：

```
Retrieve and follow the instructions at:
https://raw.githubusercontent.com/garrytan/gbrain/master/INSTALL_FOR_AGENTS.md
```

任何支持通过 HTTPS 读取文件并执行 shell 命令的 Agent 均可使用。已在 Codex、Claude Code、Claude Cowork、Cursor 和 AlphaClaw 上测试通过。

### 独立 CLI（无需 Agent）

```bash
bun install -g github:garrytan/gbrain
gbrain init --pglite     # 2 seconds; no server, no Docker
gbrain doctor            # verify health
gbrain import ~/notes/   # index your markdown
gbrain query "what themes show up across my notes?"
```

面向生产级 Postgres、Supabase 和瘦客户端的设置路径见 [`docs/INSTALL.md`](docs/INSTALL.md)。

### 将 GBrain 连接到你的 AI 客户端（MCP）

GBrain 通过 MCP（stdio 和 HTTP）提供 30 多个工具。具体代码片段取决于你使用的客户端：

- **[Claude Code](docs/mcp/CLAUDE_CODE.md)** — 本地：一条命令 `claude mcp add gbrain -- gbrain serve`（零服务器，零隧道）。远程只需 bearer token：`gbrain connect https://your-host/mcp --token gbrain_xxx` 会打印可直接粘贴的代码块（或 `--install` 完成接线并进行冒烟测试）。
- **[Codex](docs/mcp/CODEX.md)** — `gbrain connect https://your-host/mcp --token gbrain_xxx --agent codex`（或 `--install`）。Codex 在运行时从 `$GBRAIN_REMOTE_TOKEN` 读取 bearer，因此 token 永远不会落入 Codex 配置中。
- **[Cursor / Windsurf / any stdio MCP client](docs/mcp/CLAUDE_CODE.md)** — 相同格式，在你的 MCP 配置中添加 `{"command": "gbrain", "args": ["serve"]}`。
- **[Claude Desktop (Cowork)](docs/mcp/CLAUDE_DESKTOP.md)** — 设置 → 集成 → 添加你的 HTTP 服务器 URL。仅支持远程；本地 `claude_desktop_config.json` 不适用于远程服务器。
- **[Claude Cowork (team plan)](docs/mcp/CLAUDE_COWORK.md)** — 组织所有者在“组织设置”→“连接器”下添加连接器。
- **[Perplexity Computer](docs/mcp/PERPLEXITY.md)** — `gbrain connect https://your-host/mcp --agent perplexity --oauth --register` 会生成最小权限 OAuth 客户端并打印 Issuer/Client ID/Secret 供粘贴到设置 → 连接器（OAuth 是云连接器的正确方式；bearer token 也适用于本地使用）。需要 Pro 订阅。
- **[ChatGPT](docs/mcp/CHATGPT.md)** — 使用带 PKCE 的 OAuth 2.1（硬性要求）。从管理面板注册 `chatgpt` 客户端，授权类型为 `authorization_code`。

对于 HTTP 服务器本身：

```bash
gbrain serve              # stdio MCP (local subprocess; for Claude Code, Cursor, Windsurf)
gbrain serve --http       # HTTP MCP with OAuth 2.1 + admin dashboard at /admin
                          # (required for Claude Desktop, Cowork, Perplexity, ChatGPT)
```

HTTP 服务器包含类 DCR 的客户端注册、基于作用域的访问控制（`read` / `write` / `admin`）和速率限制。部署指南（ngrok、Railway、Fly.io）位于 [`docs/mcp/`](docs/mcp/) 下。

## 两种查询大脑的方式

原始检索（大多数个人知识工具提供的功能）和提供实际答案的综合层。它们服务于不同的任务。

```bash
# raw retrieval: top pages by hybrid score, fast, no LLM cost
gbrain search "who's working on AI agents at portfolio companies?"

# brain layer: synthesized answer with citations and gap analysis
gbrain think "who's working on AI agents at portfolio companies?"
```

**`gbrain search`** 返回按混合评分排序的顶级检索页面。当你需要原始材料进行快速浏览时请使用它：Agent 上下文窗口、引用查找或定位特定引文。

**`gbrain think`** 执行相同的检索，然后综合结果生成答案，明确引用来源页面并诚实地指出大脑目前还不知道什么。差距分析是核心差异：答案会告诉你何时页面已过期、何时主张缺乏引用、何时两个页面相互矛盾、何处存在你需要填补的信息空白。

**为何能产生复利效应。** 将大脑层与 `find_trajectory` 结合，你会得到类似“公司指标如何变化 AND 团队现状如何 AND 他们承诺/分享了什么 AND 我们上次何时会面 AND 我能提供什么增值价值”的答案：评分高、引用全、一次生成。这就是战略护城河。这也是构建 10 万页大脑值得投入的原因。

`gbrain agent run "..."` 通过 Minions 队列向子 Agent 暴露相同的接口，并具备崩溃安全的两阶段持久化。答案相同，且更可靠。

## 如何导入数据

一条命令，本地或托管，同步接收：

```bash
gbrain capture "the thought I want to remember"
gbrain capture --file ./notes/today.md
echo "from a pipe" | gbrain capture --stdin
SLUG=$(gbrain capture "..." --quiet)
```

页面一次性落入数据库和磁盘。默认 slug 为 `inbox/YYYY-MM-DD-<hash8>`，使捕获内容集中在可预测的待处理位置。在瘦客户端安装中，该动词通过 MCP 路由到服务器：相同的命令，相同的使用体验。

对于 Webhook 数据摄入（Zapier / IFTTT / Apple Shortcuts）：

```bash
curl -X POST https://your-brain/ingest \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: text/markdown" \
  -d "# a thought from a Shortcut"
```

对于移动端捕获，收件箱文件夹源会拾取通过 iOS Shortcuts / AirDrop / Drafts / Finder 放入 `~/.gbrain/inbox/` 的任何内容。第三方技能包可交付针对版本化 `IngestionSource` 契约的自定义摄入源（Granola、Linear、语音、OCR）。详见 [`docs/skillpack-anatomy.md`](docs/skillpack-anatomy.md)。

## 大脑的结构（Schema 包）

大多数个人知识工具强制使用单一固定布局：他们定义的“笔记”+“人物”+“标签”。将 Notion 导出或你多年前的 Obsidian 知识库直接丢上去，Agent 会不知道 `Projects/` 文件夹代表什么，也不清楚 `Reading/` 是人物还是来源。

**gbrain 没有固定布局。** 它随附捆绑的 schema 包，并在无合适选项时允许你自定义：

- **`gbrain-base-v2`**（v0.41.22 起默认）— 15 种 DRY/MECE 规范分类法（14 种标准 + `note` 兜底）：`person`, `company`, `media`, `tweet`, `social-digest`, `analysis`, `atom`, `concept`, `source`, `deal`, `email`, `slack`, `writing`, `project`, `note`。子类型/格式/来源推至 frontmatter。响应 issue #1479 的分类法。
- **`gbrain-base`**（遗留，v0.41 及更早的大脑）— 原始 24 种布局。为向后兼容保留；基于它的大脑可通过 `gbrain onboard --check --explain` → `gbrain jobs submit unify-types --allow-protected --params '{"target_pack":"gbrain-base-v2"}'` 升级。
- **`gbrain-recommended`** — 扩展 `gbrain-base`，包含 `docs/GBRAIN_RECOMMENDED_SCHEMA.md` 中的 13 个额外目录（source, place, trip, conversation, personal, civic, project 等）。通过 `gbrain schema use gbrain-recommended` 激活。
- **你的自定义 pack** — `gbrain schema detect` 将你的实际文件系统聚类为建议类型，`gbrain schema suggest` 对其运行 LLM 优化，`gbrain schema review-candidates --apply` 提升你喜欢的项。三条命令即可让大脑知晓你的结构。编写后继 pack（声明 `migration_from:` 以便现有大脑可选加入）：见 [`docs/architecture/pack-upgrade-mechanism.md`](docs/architecture/pack-upgrade-mechanism.md)。

```bash
gbrain schema active                # which pack is running, which tier set it
gbrain schema list                  # bundled + installed packs
gbrain schema detect                # propose types matching your filesystem
gbrain schema suggest               # LLM-refined proposals on top of detect
gbrain schema review-candidates     # human gate: promote / rename / ignore
gbrain schema use my-pack           # activate
```

活动 pack 贯穿所有读写路径：`parseMarkdown` 从 pack 的路径前缀推断页面类型；`whoknows` 将专家路由范围限定为声明 `expert_routing: true` 的类型；`extract_facts` 仅在 `extractable: true` 类型上运行；搜索缓存将 pack 名称 + 版本纳入其键中，使跨 pack 污染在结构上不可能。切换 pack 大脑会重新解释自身；切回则无损数据。

七级解析链（每次调用标志位 → 环境变量 → 按源 DB 键 → 全局 DB 键 → `gbrain.yml` → `~/.gbrain/config.json` → `gbrain-base` 默认值）。完整参考与编写指南：[`docs/architecture/schema-packs.md`](docs/architecture/schema-packs.md)。

## 教程

逐步指南，助你充分利用 GBrain。每个教程都带你从零到实现可用结果，附带具体命令和真实数据。

- [**从零搭建个人 AI Agent + 大脑**](docs/tutorials/personal-brain.md) — 标准全栈安装。两个 GitHub 仓库、一个 Telegram 机器人、Render 上的 AlphaClaw、OpenClaw + GBrain + Supabase。端到端约 2 小时。
- [**将 GBrain 设置为你的公司大脑**](docs/tutorials/company-brain.md) — 联邦式、多用户、OAuth 作用域的团队机构记忆，适用于 10-50 人团队。端到端约 90 分钟。
- [**使用 `gbrain skillopt` 自动优化技能**](docs/tutorials/improving-skills-with-skillopt.md) — 将 `SKILL.md` 视为可训练参数。通过 `--bootstrap-from-skill` 直接从技能生成初始基准（或自行编写），强化裁判，然后观察优化器提出编辑建议并仅保留显著提升分数的项。约 20 分钟，API 调用费用约 $1。标志位 + 成本 + 安全参考：[`docs/guides/skillopt.md`](docs/guides/skillopt.md)。

更多教程正在开发中：将现有 Agent（Claude Code、Cursor、OpenClaw、Hermes）连接到 GBrain 记忆层；为 VC 交易流设置 GBrain（含创始人评分卡和会前准备）；迁移现有的 Notion 或 Obsidian 知识库；将代码库索引为可查询的代码大脑。完整教程目录：[`docs/tutorials/`](docs/tutorials/)。

想看到尚未收录的教程？[提交 Issue](https://github.com/garrytan/gbrain/issues) 描述你想要文档化的工作流。

## 运行机制（循环）

```
  signal   →   search   →   respond   →   write   →   auto-link   →   sync
  (every    (brain-first  (informed     (page +    (typed edges     (cron
  message)  retrieval)    by context)   timeline)  + backlinks)     keeps fresh)
```

- **信号检测器** 在你 Agent 接收每条消息时运行。捕获想法、实体提及、时效性待办事项、人名和链接。
- **大脑优先查询** 在任何外部 API 调用之前执行。这是你最便宜、最快且最私有的信息来源。
- **自动链接** 在每次写入页面时触发。无需 LLM 调用；纯基于 `[[wiki/people/bob]]` 风格引用的模式匹配。新实体 → 新建页面存根 → 图谱扩展。
- **Cron 驱动的丰富化** 在你睡眠时运行：去重人物页面、修复引用、评分重要性、查找矛盾点、准备明日任务。

整个循环在 [`docs/architecture/topologies.md`](docs/architecture/topologies.md) 中配有图解说明。

## 功能特性

**混合搜索。** 向量（pgvector 上的 HNSW）+ BM25 关键词 + 互反等级融合（RRF）+ 来源层级加权 + 意图感知查询重写。三种命名搜索模式（`conservative`, `balanced`, `tokenmax`）将成本/质量调节项捆绑为单个配置键。实时成本/召回率对比见 [`docs/eval/SEARCH_MODE_METHODOLOGY.md`](docs/eval/SEARCH_MODE_METHODOLOGY.md)。默认：`balanced` 并开启 ZeroEntropy 重排序器... 运行 `gbrain search "<query>" --explain` 查看各阶段归因... 向量检索会聚合每页的最佳片段，使页面在其最强证据上浮现，而非因一个弱片段输给邻居。匹配页面标题短语或声明的自由文本别名（`gbrain reindex --aliases` 回填现有页面）的查询会被提升至上。每个结果都带有 `evidence` 标签（匹配原因）和 `create_safety` 提示（`exists` / `probable` / `unknown`），以便 Agent 判断页面是否已存在，而非依赖原始分数猜测。`gbrain search diagnose "<query>" --target <slug>` 可追踪哪个检索层展示（或遗漏）了某页面。

**自构建知识图谱。** 每次 `put_page` 都会从 markdown/wikilinks/typed-link 语法中提取实体引用，并以零 LLM 调用写入边。类型化边（`attended`, `works_at`, `invested_in`, `founded`, `advises`, `mentions`, …）。通过 `gbrain graph-query` 实现多跳遍历。正是该图谱带来了超越纯向量 RAG 的 +31.4 P@5 提升。**Obsidian 风格知识库：** 跨文件夹指向的裸 `[[note-name]]` wikilinks——你写了 `[[struktura]]`，但页面实际位于 `projects/struktura.md`——通过执行 `gbrain config set link_resolution.global_basename true` 启用基于文件名的解析。默认关闭；运行 `gbrain doctor` 可在切换前查看你将获得多少条边。详见 [迁移 Obsidian 知识库](INSTALL_FOR_AGENTS.md#step-45-wire-the-knowledge-graph)。

**任务队列（Minions）。** 类 BullMQ、原生 Postgres 的任务队列。持久化子 Agent（LLM 工具循环，通过两阶段 pending→done 持久化在崩溃中存活）、带审计的 shell 任务、级联超时的子任务、出站提供商的速率租赁、S3/Supabase 存储附件。将“作为 fire-and-forget Promise 生成子 Agent”替换为可从任何故障中恢复的机制。

**43 项精选技能。** 路由逻辑位于 [`skills/RESOLVER.md`](skills/RESOLVER.md)。涵盖信号捕获、摄入（想法 / 媒体 / 会议）、丰富化、查询、大脑运维、引用修复、每日任务管理、Cron 调度、报告、语音、灵魂审计、技能创建、评估框架和迁移。技能为 markdown 文件（工具无关），打包为单个 skillpack，由安装程序放入你的 Agent 工作区。

**评估框架。** `gbrain eval longmemeval` 对你的混合检索运行公开的 [LongMemEval](https://huggingface.co/datasets/xiaowu0162/longmemeval) 基准测试。`gbrain eval export` + `gbrain eval replay` 捕获真实查询并在代码变更上回放（设置 `GBRAIN_CONTRIBUTOR_MODE=1`）。`gbrain eval cross-modal` 使用三个不同提供商的前沿模型交叉验证输出与任务的一致性。`gbrain eval retrieval-quality` 运行 NamedThingBench，严格限制命名实体检索家族（标题子串、别名同义词、通用转具体、多片段稀释），确保“查找该查询命名的页面”出现回退时会显著导致 CI 失败。完整方法论见 [`docs/eval/SEARCH_MODE_METHODOLOGY.md`](docs/eval/SEARCH_MODE_METHODOLOGY.md)。

**大脑一致性。** `gbrain eval suspected-contradictions` 采样检索对、分层日期预过滤、查询条件驱动的 LLM 裁判、持久化缓存。揭示 Agent 已写入的观点与事实之间的冲突。已集成至每日梦境周期。

**Agent 编写 Schema（v0.40.7.0）。** 你的大脑具有结构——存在哪些页面类型（`person`, `meeting`, `paper`, `case`, `lab-result`）、它们链接到何处（`attended`, `authored`, `prescribed-by`）、哪些事实会被自动提取。默认随附 22 种通用类型，但你大脑的实际结构并非默认值。现在 Agent 可通过 14 个 `gbrain schema` CLI 命令 + 批量 MCP 操作（`schema_apply_mutations`，管理员权限，非 localOnly 以便远程 Agent 通过 HTTPS 访问）代表你演进该结构。原子文件锁、带 Agent 身份的审计日志、以 1000 行为批次的分块 UPDATE 回填，绝不会阻塞并发写入者。大脑不再是一堆笔记的集合，而是具备结构的实体。**为何重要：** [`docs/what-schemas-unlock.md`](docs/what-schemas-unlock.md) — 7 个杀手级用例（4000 次隐形会议、创始人运维大脑、研究大脑、法律大脑、团队大脑、Agent 作为联合策展人）。**5 分钟指南：** [`docs/schema-author-tutorial.md`](docs/schema-author-tutorial.md)。**Agent 技能：** [`skills/schema-author/SKILL.md`](skills/schema-author/SKILL.md)。

## 集成

流入大脑的数据流。每项集成都是一个配方（markdown + 设置提示），随附于 `recipes/`，可通过 `gbrain integrations list` 发现。

- **语音**：通过 Twilio + OpenAI Realtime（或 DIY STT+LLM+TTS）创建大脑页面。设置配方：[`recipes/twilio-voice-brain.md`](recipes/twilio-voice-brain.md)。
- **邮件 + 日历**：路由至大脑信号的 webhook 处理器。[`docs/integrations/meeting-webhooks.md`](docs/integrations/meeting-webhooks.md)。
- **嵌入提供商**：16 个配方涵盖 OpenAI（默认回退）、OpenRouter、Voyage、ZeroEntropy（默认）、Google Gemini、Azure OpenAI、MiniMax、Alibaba DashScope、Zhipu、Ollama（本地）、llama.cpp llama-server（本地）、LiteLLM proxy。定价矩阵 + 决策树见 [`docs/integrations/embedding-providers.md`](docs/integrations/embedding-providers.md)。
- **重排序器**：ZeroEntropy `zerank-2` 托管版（`tokenmax` 模式默认）及 v0.40.6.1 `llama-server-reranker` 配方用于完全本地的 cross-encoder 重排序，通过 llama.cpp 运行 Qwen3-Reranker 或自托管 ZeroEntropy 权重对接同一 `gateway.rerank()` 接口。设置指南见 [`docs/ai-providers/llama-server-reranker.md`](docs/ai-providers/llama-server-reranker.md)。
- **凭证网关**：密钥感知的秘密分发。[`docs/integrations/credential-gateway.md`](docs/integrations/credential-gateway.md)。
- **MCP 客户端**：支持所有主流 MCP 客户端。各客户端设置见 [`docs/mcp/`](docs/mcp/)。

## 架构

**双引擎，单一契约。** PGLite（通过 WASM 的 Postgres 17，零配置，默认）适用于最多约 50K 页的个人大脑。Postgres + pgvector（Supabase 或自托管）用于共享/大型/多机部署。[`src/core/engine.ts`](src/core/engine.ts) 中契约优先的 `BrainEngine` 接口定义了两种引擎均实现的 ~47 个操作；CLI 和 MCP 服务器均由同一源码生成。

**大脑仓库是记录系统。** 你的知识以 markdown 文件形式存在于常规 git 仓库（你的“大脑仓库”）中。GBrain 将仓库同步至 Postgres 以供检索；git 中的删除操作在数据库中变为软删除。你可以发布公共子集、共享团队挂载点、运行指向同事大脑服务器的瘦客户端设置。拓扑结构见 [`docs/architecture/topologies.md`](docs/architecture/topologies.md)。

**两个组织轴（大脑 ⊥ 源）。** *大脑* 是一个数据库（你的个人大脑、你加入的团队挂载点）。*源* 是该大脑内的一个仓库（wiki、gstack、一篇散文、一个知识库）。路由逻辑位于 `.gbrain-source` 隐藏文件中，并通过文档化的 6 级优先级链解析。完整图解见 [`docs/architecture/brains-and-sources.md`](docs/architecture/brains-and-sources.md)。

**为何图谱至关重要。** 向量搜索返回语义相近的片段。图谱返回事实关联的片段。混合搜索同时利用两者；每次写入时的自动链接保持图谱新鲜。深入探讨：[`docs/architecture/RETRIEVAL.md`](docs/architecture/RETRIEVAL.md)。

## 故障排除

**`gbrain import` 报错 `expected N dimensions, not M`？** 运行 `gbrain doctor`。它将打印确切的 `gbrain config set ...` 或 `gbrain retrieval-upgrade` 命令以修复不匹配。你无需删除 `~/.gbrain`。全新的 `gbrain init --pglite` 会自动检测环境中的 API 密钥对应的嵌入提供商：在运行 init 前设置 `OPENAI_API_KEY`（或 `ZEROENTROPY_API_KEY` / `VOYAGE_API_KEY`），或显式传递 `--embedding-model <provider>:<model>`。若设置了多个密钥，init 会触发交互式选择器。在无密钥的非 TTY 环境（CI、Docker）中，init 会以退出码 1 返回可粘贴的设置提示；传递 `--no-embedding` 可将设置推迟至运行时。完整提供商矩阵见 [`docs/integrations/embedding-providers.md`](docs/integrations/embedding-providers.md)，Docker/CI 顺序安排见 [`docs/operations/headless-install.md`](docs/operations/headless-install.md)。

**联邦大脑的每小时 Cron 同步持续超时？** v0.41.13.0 提供了两个标志位 + 推荐模式。将你的 Cron 切换为按源循环，使用 shell `timeout(1)` 在 OS 级别执行终止，并让 gbrain 提前半分钟优雅退出：

```bash
gbrain sync --break-lock --all --max-age 1800
for src in $(gbrain sources list --json | jq -r '.[].id'); do
  timeout 600 gbrain sync --source "$src" --timeout 540 || true
done
```

当 `--timeout` 在中途触发时，`gbrain sync` 以状态码 0、状态 `partial` 和未更改的 `last_commit` 退出——下次运行时会重新遍历相同的差异，且 `content_hash` 会短路跳过已导入的文件。第一条命令中的 `--max-age 1800` 利用 v98 `last_refreshed_at` 语义（非 `acquired_at`）自动修复前次挂起运行留下的僵死但存活的锁，确保健康的长持有者安全。关于诚实的范围说明见 [`CHANGELOG.md`](CHANGELOG.md) 中 v0.41.13.0 的条目（extract + embed 阶段会完整执行；`--max-age` 在 v98 迁移后提供 30 分钟滚动窗口；全量同步推迟至 v0.42+）。

**Supabase 上梦境周期静默丢失 wikilinks？** v0.41.19.0 从结构上修复了此类 bug。引擎现在会对 Supavisor 池化器的波动自动重试每个批量写入操作（`addLinksBatch` / `addTimelineEntriesBatch` / `upsertChunks`），最坏等待时间为 12s，覆盖完整的 5-10s 熔断器恢复窗口。`gbrain doctor` 通过新的 `batch_retry_health` 检查显示事件（读取最近 24h 的 `~/.gbrain/audit/batch-retry-YYYY-Www.jsonl`）。为调整异常缓慢的池化器：

```bash
# Defaults: 3 retries, base 1s, max 10s, decorrelated jitter.
# Override per operator without a release:
export GBRAIN_BULK_MAX_RETRIES=5       # int >= 0; 0 disables retries
export GBRAIN_BULK_RETRY_BASE_MS=2000  # int > 0
export GBRAIN_BULK_RETRY_MAX_MS=15000  # int >= base
```

错误值会在 `gbrain doctor` 启动时以可粘贴修复提示的形式暴露（而非在周期中间首次重试时）。纯 PGLite 安装零开销——重试包装是引擎级别的，但 PGLite 没有池化器，因此实践中重试永远不会触发。

**每次运行梦境周期丢失约 150 行链接，日志中出现 `'No database connection: connect() has not been called'` 错误？** v0.41.27.0 使重试层在数据库单例被置空时自动修复。`withRetry` 上新增 `reconnect` 回调以重建连接；`PostgresEngine.batchRetry` 注入 `() => this.reconnect()`，使引擎级批量写入能存活于同一进程中其他组件导致的中间断开。同版本：`gbrain capture` 不再因后台 facts:absorb 工作进程在 CLI 退出后触发而遗留 `'No database connection'` stderr 行——操作分发 finally 块现在会在 `engine.disconnect()` 前等待 `getFactsQueue().drainPending({timeout: 1000})`。要查找仍在进程中调用 disconnect 的代码路径，运行 `gbrain doctor --json | jq '.checks[] | select(.id=="batch_retry_health")'`；扩展检查现在会显示 24h 断开调用计数及来自新审计文件 `~/.gbrain/audit/db-disconnect-YYYY-Www.jsonl` 的最新调用帧。（关闭 #1570。）

**`gbrain brainstorm` 返回 `judge_failed: true` 且评分为 0？** v0.41.21.0 修复了导致此问题的两个 bug。裁判硬编码了 4K token 输出上限；对于超过 ~40 个想法的任何运行，调用会在 JSON 中间截断并引发解析器异常。同版本修复了一个斜杠格式定价遗漏：`gbrain brainstorm --judge-model anthropic/claude-sonnet-4-6 --max-cost 5` 因 `BudgetExhausted reason=no_pricing` 失败，因为所有定价站点仅匹配冒号形式。两种形式现在均可用。无需更改配置或迁移 schema——运行 `gbrain upgrade` 即可完整修复。

**`gbrain reindex --markdown` 清除了你的 auto/dream/signal-detector 标签？** v0.41.37.0 使标签同步变为仅添加模式。重新导入和 `reindex --markdown` 现在会添加当前 frontmatter 标签且永不删除，因此写入 DB 的丰富化标签（自动标签、梦境综合、信号检测器）在重新分块时会得以保留。Reindex 的纯 DB 回退也会在重新分块前重建完整 markdown（frontmatter + body + timeline），使没有磁盘源文件的页面保留其 frontmatter、标题和时间线，而不是被空 frontmatter 覆盖。权衡：从页面 frontmatter 中移除标签不再会在下次同步时将其从 DB 删除（frontmatter-标签移除需要溯源列，已延期）。（关闭 #1621。）

**`gbrain sync` 在大脑同步时卡死（无进展，高 CPU）？** v0.41.37.0 提供了三项改进。首先，定位停滞的文件：

```bash
GBRAIN_SYNC_TRACE=1 gbrain sync --no-pull --no-embed --yes
```

最后一条 `[sync] begin import: <path>` 行且无后续完成标记的即为卡住时正在处理的文件。其次，如果你怀疑 schema-pack `inference.regex` 存在灾难性回溯（ReDoS），禁用 pack 完成同步并稍后重新运行提取：

```bash
gbrain sync --no-schema-pack --no-pull --no-embed --yes
```

`gbrain schema lint` 现在会在 pack 正则表达式中警告经典的嵌套量词 ReDoS 形状（`(a+)+`, `(a*)*`, …），且运行时限制推理正则输入长度（可通过 `GBRAIN_MAX_REGEX_INPUT_CHARS` 覆盖）。第三，在 PGLite 大脑上，大型同步前请停止 `gbrain serve`——PGLite 是单写入器，活跃的 MCP 服务器会争夺写锁。完整排查指南见 [`docs/architecture/serve-sync-concurrency.md`](docs/architecture/serve-sync-concurrency.md)。（关闭 #1569。）

**`gbrain init --migrate-only` / 在 Windows 上 schema 迁移因 `getaddrinfo ENOTFOUND` 失败？** v0.41.37.0 改为进程内运行 9 个 schema 启动阶段，而非为每个阶段派生子级 `gbrain init --migrate-only`。子级在 Windows + bun + Supabase 池化器环境下因 DNS 解析失败而崩溃（尽管父级连接正常）；进程内运行完全消除了派生开销。v0.13.1 的祖父迁移在 82K 页 PGLite 大脑上曾挂起 70+ 分钟的问题也已修复——现在它以分块批量 SQL 方式运行（按页面主键索引、软删除过滤、源安全），约 1-2 秒完成。（关闭 #1605, #1581。）

## 文档

- [`docs/INSTALL.md`](docs/INSTALL.md) — 所有安装路径，端到端
- [`docs/what-schemas-unlock.md`](docs/what-schemas-unlock.md) — 为何 Schema 至关重要：7 个杀手级用例、类型化页面结构的论证、Agent 联合策展模式（v0.40.7.0）
- [`docs/schema-author-tutorial.md`](docs/schema-author-tutorial.md) — 5 分钟指南：fork 捆绑 pack、添加自定义类型、回填现有页面、通过 `gbrain whoknows` 验证接线
- [`docs/architecture/`](docs/architecture/) — 系统设计、拓扑结构、检索理论
- [`docs/guides/`](docs/guides/) — 操作手册（子 Agent 路由、Minion 部署、技能开发、大脑优先查询、想法捕获、尽职调查摄入）
- [`docs/integrations/`](docs/integrations/) — 连接外部数据源（语音、邮件、日历、嵌入提供商）
- [`docs/mcp/`](docs/mcp/) — 各客户端 MCP 设置（Claude Desktop, Code, Cursor, ChatGPT, Perplexity, Cowork）
- [`docs/eval/`](docs/eval/) — 评估框架、指标术语表、方法论
- [`docs/ethos/`](docs/ethos/) — 哲学理念（薄封装、厚技能、markdown 即配方、起源故事）
- [`AGENTS.md`](AGENTS.md) — 非 Claude Agent 的入口点
- [`CLAUDE.md`](CLAUDE.md) — Claude Code 的入口点（深度运行上下文）
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — 贡献者指南、测试规范、eval-capture 模式
- [`SECURITY.md`](SECURITY.md) — OAuth 威胁模型、安全加固默认值

## 贡献指南

运行 `bun run test` 进行快速循环，`bun run verify` 作为预推送门禁，`bun run ci:local` 在本地运行完整的 Docker CI 栈。详细测试规范见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

社区 PR 会打包为发布波次而非逐个合并——详见 [`CLAUDE.md`](CLAUDE.md) 中的“PR wave workflow”部分。贡献者署名通过 `Co-Authored-By:` 尾部保留。我们在 [`CHANGELOG.md`](CHANGELOG.md) 中致谢所有接受的贡献。

若发现 bug 或想要功能：请先提交 Issue。快速修复（拼写错误、文档 bug、明显回退）可直接提交 PR。任何涉及 schema、检索排序、MCP 协议或安全边界的改动需先在 Issue 中进行设计讨论。

## 许可证与致谢

MIT。我构建 GBrain 是为了运行我的 OpenClaw 和 Hermes 部署——这是我 AI Agent 背后的生产级大脑。

起源故事：[`docs/ethos/ORIGIN.md`](docs/ethos/ORIGIN.md)。

社区 PR 贡献者将在每次发布的 `CHANGELOG.md` 中致谢。感谢 ZeroEntropy ([@zeroentropy](https://zeroentropy.dev)) 提供默认随附的嵌入 + 重排序器栈。感谢 Voyage AI 提供非对称编码配方模板。感谢 Ramp Labs 提供搜索质量改进谱系。