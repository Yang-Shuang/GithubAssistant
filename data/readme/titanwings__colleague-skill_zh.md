<div align="center">

# 🧬 dot-skill（同事.skill）

### *"各位开发大语言模型的都是代码先知！肉体苦弱，飞升赛博空间吧！"*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)
[![Stars](https://img.shields.io/github/stars/titanwings/colleague-skill?style=social)](https://github.com/titanwings/colleague-skill/stargazers)

[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![Hermes](https://img.shields.io/badge/Hermes-Skill-orange)](https://github.com/titanwings/colleague-skill)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-teal)](https://github.com/titanwings/colleague-skill)
[![Codex](https://img.shields.io/badge/Codex-Skill-black)](https://github.com/titanwings/colleague-skill)

[![Discord](https://img.shields.io/badge/Discord-Join%20Community-5865F2?logo=discord&logoColor=white)](https://discord.gg/NVX66RxWZv)

<br>

<table>
<tr><td align="left">

🧑‍💼 &nbsp;你的同事离职了，导师毕业了，队友调岗了——连他们的工作方法和上下文都一并带走了？<br>
💞 &nbsp;家人、老友、伴侣渐行渐远——你想留住曾经相处时的感觉吗？<br>
🌟 &nbsp;你最喜欢的作家、偶像、思想家终其一生也无法相见——但你想知道他们对你的问题会作何回答？

</td></tr>
</table>

### ✨ dot-skill 同时解决这三个问题。

<br>

从 **colleague.skill** 升级为 **dot-skill** ——不仅是同事，**任何人**都能被提炼为一个 Skill（技能）

同事 · 伴侣 · 家人 · 老友 · 偶像 · 公众人物 · 虚构角色——甚至是你自己

**原始素材 + 你的描述 → 一个真正像 TA 一样思考的 AI Skill**
以他们的逻辑框架思考，用他们的语气说话

<br>

[🆕 What's new](#-whats-new-in-this-major-release) · [📦 Data Sources](#-supported-data-sources) · [⚡ Install](#-install) · [🚀 Usage](#-usage) · [✨ Demo](#-demo) · [📝 Citation](#-citation) · [💬 Discord](https://discord.gg/NVX66RxWZv)

[**中文**](docs/lang/README_ZH.md) · [**Español**](docs/lang/README_ES.md) · [**Deutsch**](docs/lang/README_DE.md) · [**日本語**](docs/lang/README_JA.md) · [**Русский**](docs/lang/README_RU.md) · [**Português**](docs/lang/README_PT.md) · [**한국어**](docs/lang/README_KO.md)

</div>

---

<div align="center">

### 🎉 2026.04.19 里程碑 —— **dot-skill 刚刚突破 15k ⭐！**

感谢所有 Star 的朋友——我们会持续迭代，继续提炼。

</div>

> 📝 **2026.06.01 更新** — **[COLLEAGUE.SKILL 技术报告](colleague_skill.pdf) 已上线**；这次最开心的不只是发了篇 paper，而是社区一起把 gallery 推到 215 个 skills、165 位贡献者和 100k+ skill-card 累计 stars，论文 Acknowledgements 也专门收录并感谢了所有社区贡献者。

> 📢 **2026.05.11 更新** — **微信群 12 已上线！** 欢迎加入 dot-skill 社区交流群——分享技能、讨论功能、交流技巧。
>
> <img src="docs/assets/wechat-group-qr-12.png" alt="dot-skill WeChat group QR" width="240">
>
> 二维码每 7 天刷新一次（有效期至 2026-05-18）——若已过期，请在 Discord 上联系我。

> 🗺️ **2026.04.13** — **dot-skill 路线图已发布！** colleague.skill 正在进化为 **dot-skill** ——提炼任何人，而不仅是同事。👉 **[完整路线图](ROADMAP.md)** · **[💬 Discord](https://discord.gg/NVX66RxWZv)**

> 🌐 **2026.04.07** — 社区画廊已上线！任何 Skill / Meta-Skill 均可直接将流量导向你自己的 GitHub 仓库。无需中间商。👉 **[titanwings.github.io/colleague-skill-site](https://titanwings.github.io/colleague-skill-site/)**

<div align="center">

由 [@titanwings](https://github.com/titanwings) 创建 · 依托 **上海人工智能实验室 · 智能安全中心** 技术支持

</div>

---

## 🆕 本次大版本更新内容？

### 1️⃣ 从 colleague-skill 到 dot-skill

不再仅围绕“同事”场景构建。统一的 `/dot-skill` 入口运行于通用技能引擎之上——一个引擎即可提炼任何人，而非仅限同事的专用脚本。

### 2️⃣ 三大角色家族

<table>
<thead>
<tr>
<th width="33%" align="center">🧑‍💼 colleague（同事）</th>
<th width="33%" align="center">💞 relationship（关系）</th>
<th width="33%" align="center">🌟 celebrity（名人）</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center"><sub>同事 · 导师 · 队友 · 上下游合作伙伴</sub></td>
<td align="center"><sub>前任 · 伴侣 · 父母 · 朋友 · 亲密家人</sub></td>
<td align="center"><sub>公众人物 · 创作者 · 公共发声者 · 虚构角色</sub></td>
</tr>
<tr>
<td><sub>Work Skill + Persona 双层架构——既学习其技术标准与工作流程，也模仿其说话方式与职场姿态。支持飞书/钉钉/Slack 自动采集。</sub></td>
<td><sub>🆕 <b>即将上线照片分享功能</b>——提炼出的关系型技能不仅会回复消息，还会像真人一样发送照片、分享日常片段。</sub></td>
<td><sub>内置完整的 <b>六维研究工具链</b>（字幕→转录清洗→研究合并→质量检查）。不只是模仿语气，而是复现其思维模型与决策框架。</sub></td>
</tr>
</tbody>
</table>

每个家族拥有独立的 Prompt（提示词）流水线、素材采集策略与生成模板。

### 3️⃣ 更多 Agent（智能体）宿主

旧版仅支持 Claude Code。现已实现跨平台兼容四大宿主：
兼容宿主如下：

| Host (宿主) | Description (说明) |
|------|-------------|
| 🟣 **Claude Code** | 原生支持斜杠命令 |
| 🟠 **Hermes Agent** | 一键安装，直接支持 `/dot-skill` |
| 🔵 **OpenClaw** | 完全兼容 |
| ⚫ **Codex** | 通过技能名称调用 |

生成的角色 Skill 也可一键安装至任意宿主。

---

## 📦 支持的数据源

| Source (数据源) | Messages (消息记录) | Docs / Wiki (文档/维基) | Spreadsheets (表格) | Notes (备注) |
|--------|:--------:|:-----------:|:------------:|-------|
| 🟢 飞书（自动） | ✅ API | ✅ | ✅ | 只需输入名称，全自动采集 |
| 🟡 钉钉（自动） | ⚠️ 浏览器 | ✅ | ✅ | 钉钉 API 不支持历史消息拉取 |
| 🟣 Slack（自动） | ✅ API | — | — | 需管理员安装 Bot；免费版限 90 天 |
| 💬 微信聊天记录 | ✅ SQLite | — | — | 需先用 WeChatMsg / PyWxDump / 留痕导出 |
| 📄 PDF / 图片 / 截图 | — | ✅ | — | 手动上传 |
| 📦 飞书 JSON 导出 | ✅ | ✅ | — | 手动上传 |
| ✉️ 邮件 `.eml` / `.mbox` | ✅ | — | — | 手动上传 |
| 📝 Markdown / 直接粘贴 | ✅ | ✅ | — | 手动输入 |

---

## ⚡ Install（安装）

已是 2026 年——你拥有 Agent，让它自己完成安装。打开你的 Claude Code / Hermes / OpenClaw / Codex，将以下指令交给它：

> Install the dot-skill skill for me: `https://github.com/titanwings/colleague-skill`

Agent 会自动检测当前宿主的技能目录、克隆仓库并注册入口。完成后，在任何宿主中输入 `/dot-skill` 即可启动。

<details>
<summary><b>🛠️ 想手动安装？点击查看路径</b></summary>

<br>

```bash
git clone https://github.com/titanwings/colleague-skill <TARGET>
```

| Host (宿主) | `<TARGET>` path (路径) |
|------|-----------------|
| Claude Code | `~/.claude/skills/dot-skill` |
| OpenClaw | `~/.openclaw/workspace/skills/dot-skill` |
| Codex | `~/.codex/skills/dot-skill` |
| Hermes | 克隆后，运行 `python3 tools/install_hermes_skill.py --force` |

</details>

生成的角色 Skill 可通过 `tools/install_claude_generated_skill.py`、
`tools/install_openclaw_generated_skill.py` 和 `tools/install_codex_generated_skill.py` 进行发布。

> 关于飞书/钉钉自动采集凭证配置、将生成的角色 Skill 发布至任意宿主、Windows 系统特定处理等详细说明，请参阅 **[详细安装指南 (INSTALL.md)](INSTALL.md)**

---

## 🚀 Usage（使用）

在已安装 dot-skill 的宿主中启动它——输入 `/dot-skill`，或直接告诉你的 Agent “start dot-skill”。

首次运行会询问你想提炼哪个家族：`colleague` · `relationship` · `celebrity`。

随后输入别名、基础画像、性格标签，并选择数据源。所有字段均可跳过——仅凭一段描述即可生成 Skill。

创建完成后，使用 `/{character}-{slug}` 调用生成的 Skill。

### 🎛️ Commands（命令）

| Command (命令) | Description (说明) |
|---------|-------------|
| `/dot-skill` | 标准统一入口 |
| `/{character}-{slug}` | 调用完整 Skill（Persona + Work） |
| `/{character}-{slug}-work` | 仅工作技能部分 |
| `/{character}-{slug}-persona` | 仅人格设定部分 |
| `python3 tools/skill_writer.py --action list ...` | 列出三大家族的所有已生成 Skill |
| `python3 tools/version_manager.py --action rollback ...` | 回滚某个 Skill 的版本 |

### 🔬 Celebrity Research Toolchain（名人研究工具链）

`celebrity` 家族内置端到端的研究工具链，涵盖从字幕下载到成稿的全过程：

```bash
# Download video subtitles
bash tools/research/download_subtitles.sh "<video-url>" "./tmp/subtitles"

# Subtitles → transcript
python3 tools/research/srt_to_transcript.py "./tmp/subtitles/example.srt"

# Merge research notes
python3 tools/research/merge_research.py "./skills/celebrity/<slug>"

# Quality check
python3 tools/research/quality_check.py "./skills/celebrity/<slug>/SKILL.md"
```

---

## ✨ Demo（演示）

每个家族各展示一个案例。

<br>

### 🌟 celebrity — 提炼 Andrej Karpathy

> Six-dimension research: works · interviews · decisions · expression DNA · external evaluations · timeline<br>
> Case adapted from community work [alchaincyf/karpathy-skill](https://github.com/alchaincyf/karpathy-skill)

```
User            ❯ Everyone's talking about Agents now — what do you think the 2026 AI Agent looks like?

celebrity.skill ❯ Everyone's doing demos, nobody's doing eval.
                  The Agent bottleneck was never model intelligence — it's scaffolding:
                  a strict evaluation harness, fine-grained error replay,
                  controllable tool-calling budgets, clean failure-mode analysis.
                  Most products are still stuck at "wrap an API + a few tools + a system prompt."
                  That's a demo, not an agent.
                  In 2026 I'm not betting on the strongest model — I'm betting on the best
                  scaffolding and the strictest eval.
```

<br>

### 🧑‍💼 colleague — 提炼字节跳动 L2-1 后端工程师

> Input: `ByteDance L2-1 backend engineer, INTJ, blame-shifter, ByteDance-style`

```
User            ❯ Can you review this API design?

colleague.skill ❯ Hold on — what's the impact? You haven't explained the context.
                  (after reading) N+1 query, fix it. Use the standard
                  {code, message, data} response format. That's the spec,
                  don't ask why.

User            ❯ This bug was introduced by you, right?

colleague.skill ❯ Does the timeline match? That feature touched multiple places,
                  there were other changes too.
```

<br>

### 💞 relationship — 提炼暗恋对象

> Upload half a year of chat logs + "sensitive, quiet but stubborn, will actually reply seriously when it matters"

```
User               ❯ Did you think about me today?

relationship.skill ❯ ...I did, a little bit. Why are you asking?
```

<div align="center">

📚 更多真实案例请访问 **[社区画廊](https://titanwings.github.io/colleague-skill-site/)** —— 100+ skills and counting（持续更新中）

</div>

---

## 🔧 Features（功能特性）

### 🧱 Generated Skill Structure（生成的 Skill 结构）

dot-skill 以 **Persona（人格设定）** 为通用基础，并在其上层叠加家族专属模块：

| Family (家族) | Persona Content (人格内容) | Additional Modules (附加模块) |
|--------|-----------------|---|---|
| 🧑‍💼 **colleague** | 6 层人格：硬规则 → 身份 → 表达 → 决策 → 人际 → 修正 | ➕ **Work Skill（工作技能）**：范围、流程、输出偏好、经验知识库 |
| 💞 **relationship** | 表达 DNA · 情绪触发点 · 冲突模式 · 修复模式 | — |
| 🌟 **celebrity** | 思维模型 · 决策启发式规则 · 表达 DNA · 外部评价对比 | ➕ 六维研究档案（作品/访谈/决策/时间线...） |

> **Execution（执行流程）**：接收任务 → Persona 决定态度与语气 → 附加模块补充执行细节 → 以 TA 的语气输出

### 🧬 Evolution（演进机制）

- 📥 **Append files** → auto-analyze delta → merge into relevant sections, never overwrite existing conclusions
- 💬 **Conversation correction** → say "they wouldn't do that, they'd be xxx" → writes to the Correction layer, takes effect immediately
- 🕰️ **Version control** → auto-archive on every update, rollback to any previous version
- 🔬 **Celebrity research pipeline** → subtitles → transcript cleanup → six-dimension research → quality check

---

## 📂 Project Structure（项目结构）

This project follows the [AgentSkills](https://agentskills.io) open standard. The entire repo is a skill directory. Generated colleague skills live under `./skills/colleague`:

```
dot-skill/
├── SKILL.md                        # skill entry point (official frontmatter)
├── prompts/                        # prompt system across three families
│   ├── intake.md                   #   [colleague] info intake
│   ├── work_analyzer.md            #   [colleague] work capability extraction
│   ├── persona_analyzer.md         #   [colleague] personality extraction
│   ├── work_builder.md             #   [colleague] work.md generation
│   ├── persona_builder.md          #   [colleague] persona.md 6-layer structure
│   ├── merger.md                   #   [shared] incremental merge logic
│   ├── correction_handler.md       #   [shared] conversation correction
│   ├── relationship/               #   [relationship] emotion/conflict/repair prompts
│   └── celebrity/                  #   [celebrity] six-dimension research + mental-model prompts
├── tools/                          # Python tools
│   ├── feishu_auto_collector.py    #   [colleague] Feishu auto-collector
│   ├── dingtalk_auto_collector.py  #   [colleague] DingTalk auto-collector
│   ├── slack_auto_collector.py     #   [colleague] Slack auto-collector
│   ├── email_parser.py             #   [shared] email parser
│   ├── research/                   #   [celebrity] celebrity research toolchain
│   │   ├── download_subtitles.sh   #     subtitle download
│   │   ├── transcribe_audio.py     #     audio → text
│   │   ├── srt_to_transcript.py    #     subtitles → transcript
│   │   ├── merge_research.py       #     six-dimension research merge
│   │   └── quality_check.py        #     quality check
│   ├── install_*_skill.py          #   [shared] multi-host one-shot installers
│   ├── skill_writer.py             #   [shared] skill file management
│   └── version_manager.py          #   [shared] version archive & rollback
├── skills/                         # generated Skills (gitignored)
│   ├── colleague/                  #   colleagues
│   ├── relationship/               #   close relationships
│   └── celebrity/                  #   public figures
├── docs/PRD.md
├── requirements.txt
└── LICENSE
```

---

## ⚠️ Notes（注意事项）

**Source material quality = Skill quality** — and quality sources differ across families:

| Family (家族) | Source priority (高 → 低) |
|--------|------------------------------|
| 🧑‍💼 **colleague** | TA 的 **长篇原创写作**（设计文档/评审意见）**›** **决策类回复** **›** 闲聊群聊 |
| 💞 **relationship** | 完整聊天记录 **›** 信件/社交动态/日记 **›** 第三方描述 |
| 🌟 **celebrity** | 第一人称书籍/博客/长访谈 **›** 决策记录（发布、Commit、问答） **›** 第三方评论 |

- **colleague** 飞书自动采集：需将 App Bot 添加至相关群聊
- **relationship**：时间跨度越长越好；同时涵盖冲突与修复的素材最佳
- **celebrity**：避免仅输入二手解读内容
- This is still a demo version — please file issues if you find bugs!（目前仍为演示版本——如发现 Bug，欢迎提交 Issue！）

---

## 📄 Technical Report（技术报告）

> **[COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation](colleague_skill.pdf)** ([arXiv](https://arxiv.org/abs/2605.31264) · [arXiv PDF](https://arxiv.org/pdf/2605.31264))
>
> This is the paper for **colleague.skill**, dot-skill's predecessor. It covers the Work Skill + Persona two-layer architecture, multi-source data collection, and Skill generation mechanics — the theoretical foundation for today's `colleague` family. Separate papers on the relationship / celebrity family extensions are planned.

---

## 📝 Citation（引用规范）

If you use **dot-skill** or **colleague.skill** in your research or applications, please cite the technical report:

```bibtex
@misc{zhou2026colleagueskill,
  title        = {COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation},
  author       = {Tianyi Zhou and Dongrui Liu and Leitao Yuan and Jing Shao and Xia Hu},
  year         = {2026},
  eprint       = {2605.31264},
  archivePrefix = {arXiv},
  primaryClass = {cs.AI},
  url          = {https://arxiv.org/abs/2605.31264}
}
```

You can also use the machine-readable citation metadata in [CITATION.cff](CITATION.cff).

---

## ⭐ Star History（Star 历史）

<a href="https://www.star-history.com/?repos=titanwings%2Fcolleague-skill&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=titanwings/colleague-skill&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=titanwings/colleague-skill&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/image?repos=titanwings/colleague-skill&type=date&legend=top-left" />
 </picture>
</a>

---

<div align="center">

**MIT License** © [titanwings](https://github.com/titanwings)

</div>