# /last30days

<p align="center">
  <a href="https://github.com/mvanhorn/last30days-skill">
    <img src="https://img.shields.io/badge/%231-Repository%20Of%20The%20Day-6f42c1?style=for-the-badge&logo=github&label=GITHUB%20TRENDING" alt="GitHub Trending #1 Repository Of The Day" />
  </a>
  <br/>
  <a href="https://trendshift.io/repositories/21997" target="_blank">
    <img src="https://trendshift.io/api/badge/repositories/21997" alt="mvanhorn/last30days-skill | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/>
  </a>
</p>

**一个由 AI 智能体主导的搜索引擎，评分依据是投票数、点赞数和真金白银——而非编辑推荐。**

本 README 跟踪当前 v3 流水线。运行时技能规范位于 [skills/last30days/SKILL.md](skills/last30days/SKILL.md)，它是最新命令和设置行为的权威来源。

**Claude Code（推荐——通过市场自动更新）：**
```
/plugin marketplace add mvanhorn/last30days-skill
/plugin install last30days
```

**Codex、Cursor、Copilot、Gemini CLI，或任意 50+ [Agent Skills](https://agentskills.io) 托管平台：**
```
npx skills add mvanhorn/last30days-skill -g
```
（使用 `-g` 进行全局安装，适用于所有项目。若需限制为当前项目范围，可移除该参数。）

更多安装选项（claude.ai 网页版、OpenClaw、手动安装）见下方的 [安装](#install) 章节。

零配置即可使用。Reddit、HN（Hacker News）、Polymarket 和 GitHub 开箱即用。运行一次后，设置向导将在 30 秒内解锁 X、YouTube、TikTok 等更多数据源。

---

Reddit 投票数、X（原 Twitter）点赞量、YouTube 字幕稿、TikTok 互动数据、由真金白银和内幕信息支撑的 Polymarket 赔率。每天有数百万人通过他们的注意力和钱包进行投票。/last30days 并行搜索所有这些平台，根据真实用户的实际参与度进行评分，并由 AI 智能体法官将其综合成一份简报。

Google 聚合编辑内容。/last30days 搜索的是大众（人群）。

你无法在其他地方获得这种搜索体验，因为没有任何单一 AI 能同时访问所有这些平台的数据。Google 搜索触及不到 Reddit 评论或 X 帖子。ChatGPT 与 Reddit 有合作，但无法搜索 X 或 TikTok。Gemini 拥有 YouTube 数据，但没有 Reddit。Claude 原生环境下这些都没有。每个平台都是封闭的“围墙花园”，拥有各自的 API、令牌和认证系统。但你可以自带密钥（API keys）和浏览器会话（browser sessions），突然之间，一个 AI 智能体就能一次性搜索所有这些平台，相互对比评分，并告诉你什么才是真正重要的内容。

这就是它的核心突破。不是某一款更好的搜索引擎，而是十几个原本互不相通的平台，通过一个智能体实现了桥接。

```
/last30days Peter Steinberger
```

你明天有个会议。你去 Google 搜索他。结果只找到他 2023 年的 LinkedIn 资料。而 /last30days 给你的是他本月实际在做什么：加入 OpenAI 的 Codex 团队、对抗 Anthropic 对第三方智能体的封禁、在 GitHub 上以 85% 的合并率合入了 23 个 PR（Pull Request）、正在开发用于跨设备智能体控制的 "LobsterOS"，以及 r/ClaudeCode 帖子获得 569 票投票，讨论他究竟是英雄还是“令人难以忍受的人”。这些信息散落在 X 帖子、Reddit 话题、YouTube 字幕稿和 GitHub 提交记录中。Google 上根本找不到这些内容。

## 为什么会有这个项目

我最初开发它是为了跟上 AI 领域的节奏。一切每天都在变化，Reddit 和 X 上的技术极客总是第一时间掌握最新动态。我需要更好的提示词（prompts），而训练数据总是落后于社区已经摸索出的经验数月之久。

但它逐渐演变成了更大的东西。现在，我会在销售会议前运行它，以了解某家企业过去 30 天的真实情况；在开会前阅读某人最近的推文和播客字幕稿；在去迪士尼世界旅行前查看哪些游乐设施关闭、社区对 Genie+ 的评价如何；在我着手开发任何项目前，先了解人们实际遇到了哪些问题。

如果你要见一位 CEO，你读过他们过去 30 天的所有推文和 YouTube 字幕稿吗？我读过了。

## 数据源：由大众评分

| Source | What the people tell you |
|--------|--------------------------|
| **Reddit** | 未经过滤的真实观点。带有投票数的前排评论，通过公共 JSON 免费获取。Google 埋没的真实意见。 |
| **X / Twitter** | 热门观点、专家长文、突发反应。第一时间知晓，第一时间争论。 |
| **YouTube** | 45 分钟的深度解析。全文字幕稿中搜索那 5 句真正值得引用的核心内容。 |
| **TikTok** | 触达 360 万人的创作者观点，这些内容你在 Google 上永远找不到。 |
| **Instagram Reels** | 带有语音字幕的网红视角。视觉文化信号。 |
| **Hacker News** | 开发者共识。825 分，899 条评论。技术人群真正争论的地方。 |
| **Polymarket** | 不是观点，是赔率。由真金白银支撑。专辑销量 96% 的置信度，收购传闻仅 4%。 |
| **GitHub** | 针对人物：PR（合并请求）速度、按星标排序的头号仓库、发行说明。针对主题：Issue 和讨论区。 |
| **Digg** | Digg AI 1000 排行榜的精选故事集群（~1000 个高信号 X 账号），附带可归因的内联引用（无需 X 认证）。当 `digg-pp-cli` 在 PATH 中时自动启用。 |
| **Threads** | Twitter 之后的文本层。创作者和品牌方的对话。 |
| **Pinterest** | 视觉发现。产品与创意的 Pin、收藏和评论。 |
| **Bluesky** | 去中心化社交层。来自后 Twitter 迁移潮的 AT Protocol 帖子。 |
| **Perplexity** | 通过 Sonar Pro 提供带引用的落地网页搜索。 |
| **Web** | 编辑报道、博客对比。众多信号之一，并非唯一来源。 |

社区贡献者持续添加更多数据源。Truth Social、小红书（RED）等已接入引擎，未来还将有更多支持。

一个获得 1500 票投票的 Reddit 帖子比一篇无人阅读的博客文章信号更强。一条 360 万播放量的 TikTok 视频能告诉你更多文化相关性，而非新闻稿。由 6.6 万美元交易量支撑的 Polymarket 赔率比评论员的猜测更不容置疑。

综合排序依据是真实用户的实际参与度。关注社交热度（Social relevancy），而非 SEO（搜索引擎优化）排名。

## 实际应用场景

**会议前。** `/last30days Peter Steinberger` - 加入 OpenAI 的 Codex 团队，对抗 Anthropic 对第三方智能体的封禁，GitHub 上以 85% 合并率合入了 23 个 PR，正在开发用于跨设备智能体控制的 LobsterOS。r/ClaudeCode：“自从 OpenClaw 发布以来，大家就知道如果你通过 API 以外的任何方式运行它，迟早会被封号”（227 票投票）。这些信息在 LinkedIn 上根本看不到。

**新品/新动态发布时。** `/last30days Kanye West` - 英国封锁其签证，Wireless Festival 取消，赞助商撤离。但专辑《BULLY》在 Billboard 榜排名第 2。Fantano 结束“ yay sabbatical”回来评测它（65 万播放）。SoFi Homecoming 请来了 Lauryn Hill 和 Travis Scott 演唱 44 首歌。Polymarket：“Kanye 会再次发推吗？” 86% 是。23 个 Reddit 话题，17 个 YouTube 视频，8.6 万票投票。

**工具对比。** `/last30days OpenClaw vs Hermes vs Paperclip` - “它们不是竞争对手，而是分层架构。” OpenClaw 是执行器（35.1 万 GitHub 星标，已上线），Hermes 是自改进大脑（3.1 万星标），Paperclip 是组织架构图（4.9 万星标）。星标数直接从 GitHub API 实时获取，而非过时的博客文章。附带架构、内存、安全性、最佳适用场景的对比表格。@IMJustinBrooke：“OpenClaw = Charmander，Hermes = Charizard。”

**理解世界局势。** `/last30days Iran vs USA` - 战争第 38 天。特朗普要求伊朗重新开放霍尔木兹海峡的周二最后期限。两架美国战机被击落。油价达 126 美元/桶。IEA（国际能源署）称其为“全球石油市场历史上最大的供应中断”。Polymarket：12 月 31 日前停火概率 74%。27 条 X 帖子，10 个 YouTube 视频，20 个预测市场数据。

**出行前。** `/last30days Universal Epic Universe` - 扩建工程已开工。“Project 680”许可已提交。烟花表演已通过基础设施审批但尚未官宣。排队时间：Mine-Cart Madness 平均等待 148 分钟。暂无年票，本地居民表示不满。Stardust Racers 因翻新至 4 月 5 日关闭。

**快速学习新技能。** `/last30days Nano Banana Pro prompting` - JSON 结构化提示词正在取代标签堆砌（tag soup）。@pictsbyai 的嵌套格式可防止“概念溢出”。先编辑后生成优于重新生成。随后它会基于社区验证有效的内容，为你编写生产级提示词。

## v3 版本更新内容

### 可分享的 HTML 简报

请求生成 HTML 简报，技能将保存一个自包含的、支持深色模式且适合打印的文件。你可以直接将其拖入 Slack、邮件或 Notion。无原始 Markdown 泄露风险。使用内联 CSS，Inter 和 JetBrains Mono 字体回退至系统默认字体。不含 JavaScript。离线可用。

```
/last30days OpenClaw --emit=html
```

or just ask in plain language: (保持原文)
```
/last30days OpenClaw, give me a shareable HTML brief
/last30days Cursor IDE for slack
/last30days Anthropic earnings export as html
```

技能仍会在聊天中输出综合结果，同时保存简报到 `${LAST30DAYS_MEMORY_DIR}/{topic}-brief.html`（默认为 `~/Documents/Last30Days/`）。聊天回复末尾会附带文件路径，方便你使用 `open` 命令打开或拖入消息。

文件内容包含：徽章、内联元数据行、模型完整输出及所有引用来源、引擎页脚（✅ All agents reported back! tree），以及注明主题和重新运行方法的 colophon。数据质量警告（如降级运行、证据薄弱等）保留在引擎的 stderr 日志中，绝不会泄露到可分享的产物里。

对于无需模型介入的直接 CLI 使用，引擎还接受 `--synthesis-file PATH` 参数，可将任意 Markdown 综合结果转换为 HTML。

### 智能搜索：杀手级功能

v3 引擎不仅搜索你的主题，还会在开始搜索前自动判断*去哪里*搜索。输入 "OpenClaw"，引擎会通过 [@j-sperling](https://github.com/j-sperling) 新构建的 Python 预研究大脑（pre-research brain）解析出 @steipete（Peter Steinberger，创建者）、r/openclaw、r/ClaudeCode，以及正确的 YouTube 频道和 TikTok 标签。旧引擎搜索关键词，新引擎先理解主题，再搜索相关人群和社区。

这就是为什么 v3 能发现 v2 无法找到的内容。“Paperclip”解析出 @dotta。“Dave Morin”解析出 @davemorin、@OpenClaw 及 TWiST 播客。“Peter Steinberger”在 X 上解析为 @steipete，在 GitHub 上解析为 steipete。双向解析：人物到公司、产品到创始人、名字到 GitHub 个人资料。正确的子版块（subreddits）、账号句柄（handles）和标签（hashtags）会在发出任何 API 请求前全部解析完毕。

### Best Takes（最佳观点/神评论）

Reddit 和 X 的用户很有趣。旧引擎因为只按相关性评分，埋没了他们的精华内容。v3 引入了第二个评判器，在相关性之外额外对幽默感、机智程度和病毒式传播潜力进行打分。Tommy Lloyd 的“我的迈克尔·乔丹是史蒂夫·科尔”在“亚利桑那篮球”的相关性上得分不高，但趣味性满分。现在每个简报末尾都会增加一个“最佳观点（Best Takes）”板块——收录最巧妙的金句、最具病毒传播力的引用和让你想分享研究的反应。内置功能，无需切换开关。

### 跨源聚类合并

当同一故事出现在 Reddit、X 和 YouTube 上时，v3 会将它们合并为一个集群，而不是显示三个独立条目。基于实体的重叠检测即使标题用词不同也能匹配成功。

### 单次遍历对比

“CLI vs MCP”以前需要运行三次串行流程（12+ 分钟）。v3 使用一次遍历，同时对两侧进行实体感知子查询。深度不变，耗时仅 3 分钟。

### 自动发现竞品对比

`/last30days OpenAI --competitors` 会指示托管推理模型通过 WebSearch（网页搜索）发现前两名同行（Anthropic、xAI），对每个实体运行 Step 0.55，并调用引擎传入 `"OpenAI vs Anthropic vs xAI"` 以及每个实体的 `--competitors-plan` JSON。引擎并行展开 3 条完整流水线，为每个实体保存一个 `*-raw.md` 文件，并将它们合并为三方对比。相同机制也支持直接运行 `/last30days "OpenAI vs Anthropic vs xAI"`。

### GitHub 人物模式

当主题为某个人物时，引擎会从关键词搜索切换为作者范围查询（author-scoped queries）。不再是“谁在 Issue 正文中提到了这个名字”，而是回答：他们正在交付什么？成果落地在哪里？

`/last30days Peter Steinberger --github-user=steipete` 显示跨 3 个仓库合入了 22 个 PR，合并率为 85%。包含自有项目的 README 摘要、星标数和顶级功能请求。本月发布的发行说明。综合器将其与 X 帖子和 Reddit 话题编织成连贯的叙事。

### ELI5（通俗解释）模式

在任何研究运行后输入“eli5 on”。综合结果将以通俗易懂的语言重写。无专业术语。数据、来源和引用完全相同——只是更清晰。“亚利桑那队靠身体对抗获胜”替代了“亚利桑那队的进攻核心是内线得分（命中率超 50%，全国第九）”。输入“eli5 off”可恢复原样。

### v3 其他更新

- **免费获取 Reddit 评论。** 公共 JSON 提供帖子及带投票数的顶级评论。无需 API 密钥，无需 ScrapeCreators。开箱即用。
- **真正可用的 YouTube 字幕稿。** 候选池扩大至音乐视频的 3 倍，以覆盖带有字幕的访谈/评测类内容。
- **TikTok、Instagram、Threads。** 设置 `SCRAPECREATORS_API_KEY` 后自动激活——同一密钥，每次调用费用相同。可通过 `EXCLUDE_SOURCES=tiktok,instagram,threads`（任意逗号分隔的子集）屏蔽其中任何一项。
- **Pinterest。** 按查询开启（视觉 Pin、用途较窄）：模型传递 `--search=pinterest` 以启用需要它的运行。需 `SCRAPECREATORS_API_KEY`。
- **YouTube + TikTok 评论。** 通过 `INCLUDE_SOURCES=youtube_comments,tiktok_comments` 持久开启，因为每个视频会在基础搜索之外额外调用 N 次 ScrapeCreators。以与 Reddit 相同的方式展示带投票数的顶级评论。
- **Perplexity Sonar。** 通过 OpenRouter 提供带引用的落地网页搜索。添加 `OPENROUTER_API_KEY` 并设置 `INCLUDE_SOURCES=perplexity`（它是独立的付费 API——默认关闭以避免意外扣费）。
- **Polymarket 噪声过滤。** 常见词消歧防止“Apple”匹配到“Will Apple release a car?”。
- **高容错 Reddit。** 超时预算和运行时降级机制。单个缓慢的帖子不会导致整个任务失败。
- **趣味评判器 v2。** 将幽默评分内置于叙事中。Reddit 最巧妙的金句会自然融入综合结果，而非单独堆砌在一个板块里。
- **显示赔率而非金额。** % 概率才是核心。界面已移除美元交易量显示。
- **单作者上限。** 每位作者最多展示 3 条内容，防止单一声音主导你的简报。
- **实体消歧。** 引擎解析出账号句柄后，综合器会信任它们。不会再出现马略卡度假村压过华盛顿体育俱乐部的情况。
- **OpenClaw 一等公民支持。** 自动解析以支持引擎侧预研究。设备认证实现无摩擦的 ScrapeCreators 注册。
- **通过 1,012 项测试。**

## 安装

| Surface | Install | Updates |
|---------|---------|---------|
| **Claude Code**（推荐） | `/plugin marketplace add mvanhorn/last30days-skill` | 自动通过市场更新，或运行 `claude plugin update last30days@last30days-skill` |
| **Codex、Cursor、Copilot、Gemini CLI、GitHub Copilot，或任意 50+ [Agent Skills](https://agentskills.io) 托管平台** | `npx skills add mvanhorn/last30days-skill -g` | `npx skills update last30days -g` |
| **claude.ai**（网页版） | [下载 `last30days.skill`](https://github.com/mvanhorn/last30days-skill/releases/latest/download/last30days.skill)，并通过设置 > 功能 > 技能 > + 上传 | 重新下载并上传 |
| **OpenClaw** | `clawhub install last30days-official` | `clawhub update last30days-official` |

### Claude Code（推荐）

```
/plugin marketplace add mvanhorn/last30days-skill
```

推荐，因为 Claude Code 市场会自动为你处理更新——插件缓存采用版本控制，新发布时自动刷新。运行 `claude plugin update last30days@last30days-skill` 可强制检查更新。

如果你更倾向于在 Claude Code 上使用 agent-skills 安装路径，同样支持：

```
npx skills add mvanhorn/last30days-skill -g -a claude-code
```

原生插件和 `npx skills` 安装可以共存。请注意 Claude Code 不会跨安装方式去重：如果你同时启用了市场插件和 `npx skills` 副本，`/last30days` 会显示两个条目。每台机器请只使用一种安装方式。

### Codex、Cursor、Copilot、Gemini CLI 及其他 Agent Skills 宿主平台

通过开放的 [Agent Skills](https://agentskills.io) CLI 安装——支持 50+ 运行环境（harnesses），包括 `codex`、`cursor`、`github-copilot`、`gemini-cli`、`claude-code`、`windsurf`、`cline`、`continue`、`roo`、`aider-desk`、`opencode`、`goose` 等（完整列表见 [vercel-labs/skills repo](https://github.com/vercel-labs/skills)）。

```bash
npx skills add mvanhorn/last30days-skill -g
```

`-g`（全局）标志将安装到你的用户目录，使技能在所有项目中可用。若不使用 `-g`，`npx skills` 会按项目本地安装至 `./.skills/`（随仓库提交）。对于这种“探索世界”的工具，全局安装才是你想要的。

默认情况下，它会为你检测到的运行环境进行安装。若要指定特定环境（或多个）：

```bash
npx skills add mvanhorn/last30days-skill -g -a codex
npx skills add mvanhorn/last30days-skill -g -a cursor
npx skills add mvanhorn/last30days-skill -g -a gemini-cli
npx skills add mvanhorn/last30days-skill -g -a codex -a cursor
```

后续更新：

```bash
npx skills update last30days -g
```

或通过 `npx skills` 更新所有已全局安装的插件：

```bash
npx skills update -g
```

使用 `npx skills list -g` 和 `npx skills remove last30days -g` 列出和移除。

### claude.ai（网页版）

1. [下载 `last30days.skill`](https://github.com/mvanhorn/last30days-skill/releases/latest/download/last30days.skill)
2. 前往 [claude.ai Settings > Capabilities > Skills](https://claude.ai/settings/capabilities)
3. 点击技能面板中的 `+` 按钮并拖入文件

首先启用“Code execution and file creation”——没有它技能无法运行。

### OpenClaw

```bash
clawhub install last30days-official
```

### 手动安装（开发者）

```bash
git clone https://github.com/mvanhorn/last30days-skill.git
ln -s "$(pwd)/last30days-skill/skills/last30days" ~/.claude/skills/last30days
```

符号链接可使安装随你的工作目录同步更新，无需重新复制。对于 `claude.ai`，需从源码构建 `.skill` 文件：运行 `bash skills/last30days/scripts/build-skill.sh` 生成 `dist/last30days.skill`。

Reddit（含评论）、Hacker News、Polymarket 和 GitHub 开箱即用，零配置。运行一次 `/last30days`，设置向导将在 30 秒内解锁更多数据源。

## 自带密钥（BYOK）

这些平台之间互不关联。X 不知道 Reddit 的看法，YouTube 看不到 TikTok 的数据。但你可以自带 API 密钥和浏览器令牌，突然之间你就能一次性访问所有平台。

| Sources | What you need | Cost |
|---------|---------------|------|
| **Reddit（含评论）+ HN + Polymarket + GitHub** | Nothing | Free |
| **X / Twitter** | Log into x.com in any browser | Free |
| **YouTube** | `brew install yt-dlp` | Free |
| **Bluesky** | App password from bsky.app | Free |
| **TikTok + Instagram + Threads + Pinterest + YouTube 评论** | ScrapeCreators key | 100 free credits, then PAYG |
| **Perplexity Sonar** | OpenRouter key | Pay as you go |
| **网页搜索** | Brave Search key | 2,000 free queries/month |

### macOS Keychain（可选）

在 macOS 上，你可以将密钥存储在系统钥匙串中，而非 `.env` 文件。技能会自动读取它们，并作为最低优先级源使用——若发生冲突，`.env` 文件和进程环境变量仍优先生效。

```bash
# Interactive setup — prompts for each known key, skip with empty input
skills/last30days/scripts/setup-keychain.sh

# Or store a single key by hand
security add-generic-password -a "$USER" -s last30days-XAI_API_KEY -w "xai-..."

# Inspect / clean up
skills/last30days/scripts/setup-keychain.sh --list
skills/last30days/scripts/setup-keychain.sh --delete XAI_API_KEY
```

项目以当前用户的服务名 `last30days-<KEY>` 存储。在非 Darwin 平台上，加载器为无操作（no-op），因此 Linux/Windows 用户的行为不会改变。

完整的数据源密钥矩阵、推理提供商优先级和网页搜索后端优先级说明，请参阅 [CONFIGURATION.md](CONFIGURATION.md)。

## 配置

第一天你可能最想知道的两件事：

**研究文件的保存位置。** `LAST30DAYS_MEMORY_DIR` 默认为 `~/Documents/Last30Days/`（Windows：`C:\Users\<you>\Documents\Last30Days\`）。可通过在 shell 中设置该环境变量为任意路径，或在每次运行时使用 `--save-dir <path>` 进行覆盖。使用 `--save-suffix=<name>` 可将同一主题的不同变体分开保存（例如按客户区分）。每次运行会生成 `<slug>-raw[-suffix].md` 文件。

**跨次运行的趋势监控。** 默认模式为每次运行生成全新的 Markdown 快照。若要随时间累积发现结果，可添加 `--store` 将其持久化到 SQLite 数据库中，随后使用 [`scripts/watchlist.py`](skills/last30days/scripts/watchlist.py) 进行定时运行（支持在新发现时通过 Slack/Webhook 推送），以及使用 [`scripts/briefing.py`](skills/last30days/scripts/briefing.py) 生成每日/每周摘要。完整的周期模式详见 [CONFIGURATION.md](CONFIGURATION.md#trend-monitoring-store--watchlist--briefings)。

按客户封装的脚本、自定义分类-同行子版块，以及用于进行中的自定义功能的实验性 beta 频道，均在 [CONFIGURATION.md](CONFIGURATION.md) 中详细记录。

## 工作原理

1. **你输入一个主题。** 人物、公司、产品、技术、“X vs Y”。任何内容均可。
2. **智能体解析关键实体。** 查找 X 账号（包括创始人）、GitHub 仓库、子版块、TikTok 标签和 YouTube 频道。对于“Kanye West”，它会定位 r/hiphopheads、@kanyewest 以及 YouTube 上的“bully review”。对于“OpenClaw”，它解析出 GitHub 上的 openclaw/openclaw 并获取实时星标数。
3. **并行搜索所有数据源。** 多查询扩展。结果按参与度、相关性和新鲜度评分。
4. **无人能及的深度。** 完整提取反应类视频的字幕稿。获取带投票数的顶级 Reddit 评论、TikTok 字幕和 Polymarket 赔率。不只是标题和链接。
5. **同一故事，自动合并。** 在 Reddit 宣布、X 讨论、TikTok 报价的同一事件=一个集群，而非三个独立条目。
6. **综合为一份简报。** 基于具体数据。标明来源引用。按真实用户参与度排序。不是“这是我找到的”，而是“这才是真正重要的”。
7. **然后它成为你的专家。** 运行一次后，你的 Claude 会话将掌握社区的所有知识。可追问后续问题。让它编写提示词、起草邮件、规划行程、设计系统——全部基于当下的真实情况。

## 用户评价

> "我发现了一个 Claude Code 技能，它能针对 Reddit、X、YouTube 和 HN 过去 30 天的内容研究任何主题。然后为你生成提示词。在撰写每篇内容前，我都要手动搜索 Reddit 和 X。一个标签页一个标签页地翻，一条帖子一条帖子地看。这部分耗时 90 分钟。这个技能彻底消除了它。" -@itsjasonai

> "这一个技能取代了我整个研究流程。你给它一个主题，它会抓取 Reddit、X 和网页上人们实际在讨论的内容。不是旧博客文章。而是过去 30 天的真实对话。" -@itswilsoncharles

> "今天 GitHub 趋势前 10 的仓库中有 5 个是 Claude 工具。第 1 名：mvanhorn/last30days-skill" -@yieldhunter95

## 开源

MIT 许可证。无追踪，无分析。你的研究数据仅保留在本地机器上。通过 1,012 项测试。

基于 Python 3.12+、yt-dlp、Node.js（内置用于 X 搜索的 Bird 客户端）和 ScrapeCreators API 构建。v3 引擎架构由 [@j-sperling](https://github.com/j-sperling) 设计。

版本历史记录请参阅 [CHANGELOG.md](CHANGELOG.md)。

## Star History

<a href="https://star-history.com/#mvanhorn/last30days-skill&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=mvanhorn/last30days-skill&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=mvanhorn/last30days-skill&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=mvanhorn/last30days-skill&type=Date" />
  </picture>
</a>

---

**@slashlast30days** · [github.com/mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)