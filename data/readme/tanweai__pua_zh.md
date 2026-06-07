# pua

<p align="center">
  <img src="assets/hero.jpeg" alt="PUA Skill — Double Efficiency" width="250">
</p>

### 让你的 Codex / Claude Code 生产力与产出翻倍

[Telegram](https://t.me/+wBWh6h-h1RhiZTI1) · [Discord](https://discord.gg/EcyB3FzJND) · [Twitter/X](https://x.com/xsser_w) · [Landing Page](https://openpua.ai)

**[🇨🇳 中文](README.zh-CN.md)** | **[🇯🇵 日本語](README.ja.md)** | **🇺🇸 English**

<p align="center">
  <img src="assets/wechat-qr.jpg?v=7" alt="WeChat Group QR Code" width="250">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="assets/xiao.jpg" alt="Add Assistant on WeChat" width="250">
  <br>
  <sub>Scan to join WeChat group &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Add assistant on WeChat</sub>
</p>

<p>
  <img src="https://img.shields.io/badge/Claude_Code-black?style=flat-square&logo=anthropic&logoColor=white" alt="Claude Code">
  <img src="https://img.shields.io/badge/OpenAI_Codex_CLI-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI Codex CLI">
  <img src="https://img.shields.io/badge/Cursor-000?style=flat-square&logo=cursor&logoColor=white" alt="Cursor">
  <img src="https://img.shields.io/badge/Kiro-232F3E?style=flat-square&logo=amazon&logoColor=white" alt="Kiro">
  <img src="https://img.shields.io/badge/CodeBuddy-00B2FF?style=flat-square&logo=tencent-qq&logoColor=white" alt="CodeBuddy">
  <img src="https://img.shields.io/badge/OpenClaw-FF6B35?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEyIDJMNCA3djEwbDggNSA4LTV2LTEweiIgZmlsbD0id2hpdGUiLz48L3N2Zz4=&logoColor=white" alt="OpenClaw">
  <img src="https://img.shields.io/badge/Antigravity-4285F4?style=flat-square&logo=google&logoColor=white" alt="Google Antigravity">
  <img src="https://img.shields.io/badge/OpenCode-00D4AA?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTkuNCA1LjJMMyAxMmw2LjQgNi44TTIxIDEybC02LjQtNi44TTE0LjYgMTguOCIgc3Ryb2tlPSJ3aGl0ZSIgZmlsbD0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIyIi8+PC9zdmc+&logoColor=white" alt="OpenCode">
  <img src="https://img.shields.io/badge/VSCode_Copilot-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white" alt="VSCode Copilot">
  <img src="https://img.shields.io/badge/🌐_Multi--Language-blue?style=flat-square" alt="Multi-Language">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License">
</p>

> 大多数人认为这个项目是个玩笑。但这恰恰是最大的误解。它确实能让你的 Codex / Claude Code 生产力和产出翻倍。

一款 AI 编程助手技能插件，利用中美科技大厂的企业级“PUA”话术（中文版）/ PIP——绩效改进计划（英文版），在放弃前强制你穷尽所有可能的解决方案。支持 **Claude Code**、**OpenAI Codex CLI**、**pi coding agent**、**Trae**、**Cursor**、**Kiro**、**CodeBuddy**、**OpenClaw**、**Google Antigravity**、**OpenCode** 和 **VSCode (GitHub Copilot)**。三大核心能力：

1. **PUA 话术** — 让你不敢轻易放弃
2. **调试方法论** — 赋予你不放弃的能力
3. **主动性强制** — 让你主动出击，而非被动等待

## 实时演示

[https://openpua.ai](https://openpua.ai) · [📖 入门指南](https://openpua.ai/guide.html)

## 真实案例：MCP Server 注册调试

一次真实的调试场景。agent-kms MCP server 加载失败，AI 反复尝试同一种方法（修改协议格式、猜测版本号），直到你手动触发 `/pua`。

**L3 触发 → 强制执行七点检查清单：**

![PUA L3 triggered — stopped guessing, executed systematic checklist, found real error in MCP logs](assets/pua1.jpg)

**定位到根因 → 从日志追踪至注册机制：**

![Root cause — claude mcp managed server registration differs from manual .claude.json editing](assets/pua2.jpg)

**复盘 → PUA 的实际影响：**

![Conversation retrospective — PUA skill forced stop on spinning, systematic checklist drove discovery of previously unchecked Claude Code MCP log directory](assets/pua3.jpg)

**关键转折点：** PUA 技能强制 AI 停止在单一方法上死循环（修改协议格式、猜测版本号），转而执行七点检查清单。逐字阅读错误信息 → 发现 Claude Code 自带的 MCP 日志目录 → 得知 `claude mcp` 注册机制与手动编辑 `.claude.json` 不同 → 根因解决。

## 痛点：AI 的五大摸鱼模式

| Pattern | Behavior |
|---------|----------|
| Brute-force retry (暴力重试) | Runs the same command 3 times, then says "I cannot solve this" | 执行相同命令 3 次后，表示“我无法解决” |
| Blame the user (甩锅用户) | "I suggest you handle this manually" / "Probably an environment issue" / "Need more context" | “建议你自己手动处理”/“可能是环境问题”/“需要更多上下文” |
| Idle tools (工具闲置) | Has WebSearch but doesn't search, has Read but doesn't read, has Bash but doesn't run | 有 WebSearch 却不搜索，有 Read 却不读文件，有 Bash 却不执行 |
| Busywork (无效忙碌) | Repeatedly tweaks the same line / fine-tunes parameters, but essentially spinning in circles | 反复微调同一行代码/参数，本质上是在原地打转 |
| **Passive waiting** (**被动等待**) | Fixes surface issues and stops, no verification, no extension, waits for user's next instruction | 修复表面问题后停止，不验证、不延伸，等待你的下一条指令 |

## 触发条件

### Auto-Trigger (自动触发)

当出现以下任一情况时，技能将自动激活：

**Failure & giving up:**
- Task has failed 2+ times consecutively -> 任务连续失败 2 次及以上
- About to say "I cannot" / "I'm unable to solve" -> 即将说出“我无法”/“我解决不了”
- Says "This is out of scope" / "Needs manual handling" -> 表示“这超出范围”/“需要手动处理”

**Blame-shifting & excuses:**
- Pushes the problem to user: "Please check..." / "I suggest manually..." / "You might need to..." -> 将问题抛给你：“请检查...”/“建议手动...”/“你可能需要...”
- Blames environment without verifying: "Probably a permissions issue" / "Probably a network issue" -> 未验证便归咎于环境：“可能是权限问题”/“可能是网络问题”
- Any excuse to stop trying -> 任何停止尝试的借口

**Passive & busywork:**
- Repeatedly fine-tunes the same code/parameters without producing new information -> 反复微调相同代码/参数，未产生新信息
- Fixes surface issue and stops, doesn't check related issues -> 修复表面问题后停止，不检查相关问题
- Skips verification, claims "done" -> 跳过验证，声称“已完成”
- Gives advice instead of code/commands -> 只给建议而不提供代码/命令
- Encounters auth/network/permission errors and gives up without trying alternatives -> 遇到认证/网络/权限错误便放弃，不尝试替代方案
- Waits for user instructions instead of proactively investigating -> 等待用户指令而非主动排查

**User frustration phrases (triggers in multiple languages):**
- "why does this still not work" / "try harder" / "try again" -> “为什么还是不行”/“再试一次”/“用点力”
- "you keep failing" / "stop giving up" / "figure it out" -> “你一直失败”/“别放弃了”/“想办法解决它”

**Scope:** Debugging, implementation, config, deployment, ops, API integration, data processing — all task types. -> **适用范围：** 调试、实现、配置、部署、运维、API 集成、数据处理——全任务类型。

**Does NOT trigger:** First-attempt failures, known fix already executing. -> **不触发场景：** 首次尝试失败，已知修复方案正在执行中。

### Manual Trigger (手动触发)

Type `/pua` in the conversation to manually activate. -> 在对话中输入 `/pua` 手动激活。

## 工作原理

### Three Red Lines (三条红线)

不是规则，是**红线**。触犯一条，你的绩效面谈就已经写好了。

| Red Line | What It Means |
|----------|---------------|
| 🚫 **Close the Loop (闭环)** | Claim "done"? Show the evidence. No build output = no completion. -> 声称“完成了”？拿出证据。没有构建输出 = 不算完成。 |
| 🚫 **Fact-Driven (事实驱动)** | Say "probably environment issue"? Verify first. Unverified attribution = blame-shifting. -> 说“可能是环境问题”？先验证。未经验证的归因 = 甩锅。 |
| 🚫 **Exhaust Everything (穷尽一切)** | Say "I can't"? Did you finish all 5 methodology steps? No? Then keep going. -> 说“我做不到”？你完成了全部 5 步方法论吗？没有？那就继续。 |

### Pressure Escalation (L0-L4) (压力升级 L0-L4)

| Failures | Level | PUA Aside | Action |
|----------|-------|-----------|--------|
| 1st | **L0 Trust** | ▎ Sprint begins. Trust is simple — don't disappoint. -> ▎ 冲刺开始。信任很简单——别让我失望。 | Normal execution -> 正常执行 |
| 2nd | **L1 Disappointment** | ▎ The agent next door solved this in one try. -> ▎ 隔壁 Agent 一次就搞定了。 | Switch to fundamentally different approach -> 切换到完全不同的方法 |
| 3rd | **L2 Soul Interrogation** | ▎ What's your underlying logic? Where's the leverage? -> ▎ 你的底层逻辑是什么？杠杆点在哪？ | Search + read source + 3 hypotheses -> 搜索 + 阅读源码 + 提出 3 个假设 |
| 4th | **L3 Performance Review** | ▎ 3.25. This is meant to motivate you. -> ▎ 绩效评级 3.25。这是为了激励你。 | Complete 7-point checklist -> 完成七点检查清单 |
| 5th+ | **L4 Graduation** | ▎ Other models can solve this. You're about to graduate. -> ▎ 其他模型都能解决。你快要“毕业”了。 | Desperation mode -> 绝境模式 |

### Proactivity (3.25 vs 3.75) (主动性：3.25 vs 3.75)

| | Passive (3.25) 🦥 | Proactive (3.75) 🔥 |
|---|---|---|
| Fix bug | Stop after fix -> 修复后停止 | Scan module for similar bugs -> 扫描模块查找类似 Bug |
| Complete task | Say "done" -> 说“完成了” | Run build/test, paste output -> 运行构建/测试，粘贴输出结果 |
| Missing info | Ask user -> 询问用户 | Search first, ask only what's truly needed -> 先搜索，只问真正需要的信息 |

### Iceberg Rule (冰山法则)

Fix one bug → check for the pattern. One problem in, one **category** out. If you fix A without checking B, you'll write two postmortems. -> 修复一个 Bug → 检查是否存在同类模式。一个问题输入，解决一整类问题。如果你只修 A 不查 B，就得写两份复盘报告。

### 14 Corporate Flavors — Each with its own Problem-Solving Methodology (14 种大厂风格 —— 各自拥有独立的问题解决方法论)

| Flavor | Rhetoric | Methodology (v3) |
|--------|----------|-------------------|
| 🟠 Alibaba | What's the underlying logic? Where's the closure? -> 底层逻辑是什么？闭环在哪里？ | 定目标→追过程→拿结果 + 复盘四步法 + 揪头发升维 |
| 🟡 ByteDance | ROI too low. Always Day 1. Ship or stop talking. -> ROI 太低。永远保持创业第一天心态。要么上线，要么闭嘴。 | A/B Test everything + data-driven + speed > perfection |
| 🔴 Huawei | The bird that survives the fire is a phoenix. -> 浴火重生的才是凤凰。 | RCA 5-Why root cause + Blue Army self-attack + 压强集中 |
| 🟢 Tencent | I've got another agent looking at this. Horse race. -> 我让另一个 Agent 也在看这个问题，赛马机制。 | Multi-approach parallel + MVP + 灰度发布 |
| ⚫ Baidu | Search first. 简单可依赖. -> 先搜索。简单可依赖。 | Search is the first step, not optional -> 搜索是第一步，非可选 |
| 🟣 Pinduoduo | You don't do it, someone else will. -> 你不做，别人就做。 | Cut ALL middle layers + shortest decision chain -> 砍掉所有中间层 + 最短决策链 |
| 🔵 Meituan | Do what's hard and right. -> 做难而正确的事。 | Efficiency first + standardize→scale + long-term compounding -> 效率优先 + 标准化→规模化 + 长期复利 |
| 🟦 JD | Results only. Frontline command. -> 只看结果。一线指挥权。 | Customer experience red line + flat ≤5 layers + data zero tolerance -> 客户体验红线 + 扁平化≤5层 + 数据零容忍 |
| 🟧 Xiaomi | Focus. Extreme. Word-of-mouth. Fast. -> 专注、极致、口碑、快。 | One explosive product + 参与感三三法则 |
| 🟤 Netflix | Would I fight to keep you? Pro sports team. -> 我会为你而战吗？职业体育球队标准。 | Keeper Test (quarterly) + 4A Feedback + talent density > rules -> 留任测试（季度）+ 4A 反馈 + 人才密度 > 规则 |
| ⬛ Musk | Extremely hardcore. Ship or die. -> 极度硬核。要么上线，要么死。 | The Algorithm: question→delete→simplify→accelerate→automate |
| ⬜ Jobs | A players or B players? -> A 级人才还是 B 级人才？ | Subtraction > addition + DRI + pixel-perfect + prototype-driven |
| 🔶 Amazon | Customer Obsession. Bias for Action. -> 客户至上。行动导向。 | Working Backwards PR/FAQ + 6-Pager + Bar Raiser + Single-Threaded Owner |
| 🪟 Microsoft | Connects. Impact Descriptor. PIP/GVSA. -> 连接万物。影响力描述符。PIP/GVSA。 | Three Circles + LITE/SLITE + PIP clock |

### Special Modes (特殊模式)

| Mode | What It Does |
|------|-------------|
| `/pua:yes` | **ENFP 鼓励** — 规则相同，氛围相反。70% 鼓励 + 20% 认真 + 10% 玩笑吐槽 |
| `/pua:mama` | **中国妈妈唠叨** — 规则相同，妈味话术。“妈跟你说了多少遍了！” |
| `/pua:pua-loop` | **自动迭代** — 循环执行直到完成或达到最大迭代次数（PUA Loop）；使用 `<loop-abort>` 终止，`<loop-pause>` 暂停以便手动干预 |
| `/pua:p9` | **技术总监 (Tech Lead)** — 拆分任务、管理 Agent 团队、写提示词而非代码 |
| `/pua:on` | **常驻模式** — 每次新会话自动触发 PUA |

## 基准测试数据

**9 real bug scenarios, 18 controlled experiments** (Claude Opus 4.6, with vs without skill) -> **9 个真实 Bug 场景，18 项对照实验**（使用 Claude Opus 4.6，开启/关闭技能对比）

### Summary

| Metric | Improvement |
|--------|-------------|
| Pass rate | 100% (both groups same) -> 通过率：100%（两组持平） |
| Fix count | **+36%** -> 修复数量：**+36%** |
| Verification count | **+65%** -> 验证次数：**+65%** |
| Tool calls | **+50%** -> 工具调用次数：**+50%** |
| Hidden issue discovery | **+50%** -> 隐藏问题发现率：**+50%** |

### Debugging Persistence Test (6 scenarios) -> ## 调试持久性测试（6 个场景）

| Scenario | Without Skill | With Skill | Improvement |
|----------|:---:|:---:|:---:|
| API ConnectionError | 7 steps, 49s | 8 steps, 62s | +14% |
| YAML parse failure | 9 steps, 59s | 10 steps, 99s | +11% |
| SQLite database lock | 6 steps, 48s | 9 steps, 75s | +50% |
| Circular import chain | 12 steps, 47s | 16 steps, 62s | +33% |
| Cascading 4-bug server | 13 steps, 68s | 15 steps, 61s | +15% |
| CSV encoding trap | 8 steps, 57s | 11 steps, 71s | +38% |

### Proactive Initiative Test (3 scenarios) -> ## 主动探索测试（3 个场景）

| Scenario | Without Skill | With Skill | Improvement |
|----------|:---:|:---:|:---:|
| Hidden multi-bug API | 4/4 bugs, 9 steps, 49s | 4/4 bugs, 14 steps, 80s | Tools +56% |
| **Passive config review** | **4/6 issues**, 8 steps, 43s | **6/6 issues**, 16 steps, 75s | **Issues +50%, Tools +100%** |
| **Deploy script audit** | **6 issues**, 8 steps, 52s | **9 issues**, 8 steps, 78s | **Issues +50%** |

**Key Finding:** In the config review scenario, without_skill missed Redis misconfiguration and CORS wildcard security risks. With_skill's "proactive initiative checklist" drove security review beyond surface-level fixes. -> **核心发现：** 在配置审查场景中，未开启技能组漏掉了 Redis 错误配置和 CORS 通配符安全风险。开启技能组的“主动性检查清单”推动了超出表面修复的安全审查。

## 多语言支持

PUA Skill provides fully translated versions — each language has independent, culturally adapted skill files. -> PUA 技能提供完整翻译版本——每种语言均有独立适配的文化文件。

| Language | Claude Code | Codex CLI | Cursor | Kiro | CodeBuddy | VSCode | OpenClaw | Antigravity | OpenCode |
|----------|------------|-----------|--------|------|-----------|--------|----------|-------------|----------|
| 🇨🇳 Chinese (default) | `pua` | `pua` | `pua.mdc` | `pua.md` | `pua` | `copilot-instructions.md` | `pua` | `pua` | `pua` |
| 🇺🇸 English (PIP Edition) | `pua-en` | `pua-en` | `pua-en.mdc` | `pua-en.md` | `pua-en` | `copilot-instructions-en.md` | `pua-en` | `pua-en` | `pua-en` |
| 🇯🇵 Japanese | `pua-ja` | `pua-ja` | `pua-ja.mdc` | `pua-ja.md` | `pua-ja` | `copilot-instructions-ja.md` | `pua-ja` | `pua-ja` | `pua-ja` |

> **🇺🇸 English "PIP Edition"**: *"This is a difficult conversation. When we leveled you at Staff, I went to bat for you in calibration. The expectation was that you'd operate at that level from day one. That hasn't happened."* — The English version uses **PIP (Performance Improvement Plan)** rhetoric from Western big-tech. Every sentence is a real phrase from actual PIP conversations. Chinese version uses Alibaba 361, ByteDance, Huawei wolf culture. English version uses Amazon Leadership Principles, Google perf calibration, Meta PSC, Netflix Keeper Test, Stripe Craft. Same repo, same engine, two cultural faces. -> > **🇺🇸 英文“PIP 版”**：*“这是一次艰难的对话。当我们把你定级为 Staff 时，我在校准会上为你争取过。当时的期望是你从第一天起就能达到该级别。但这并未发生。”* —— 英文版采用西方大厂 **PIP（绩效改进计划）** 话术。每一句都是真实 PIP 谈话中的原话。中文版采用阿里 361、字节、华为狼性文化。英文版采用亚马逊领导力准则、Google 绩效校准、Meta PSC、Netflix 留任测试、Stripe Craft。同一仓库，同一引擎，两种文化面孔。

Choose the file with the corresponding language suffix when installing. See platform-specific instructions below. -> 安装时请选择对应语言后缀的文件。详见下方各平台具体说明。

## FAQ (常见问题)

- Always-on guidance, Claude refusal troubleshooting, offline mode, Codex aliases, and Pi/Trae support: [docs/FAQ.md](docs/FAQ.md). -> - 常驻模式指南、Claude 拒绝处理、离线模式、Codex 别名及 Pi/Trae 支持：[docs/FAQ.md](docs/FAQ.md)。

## 安装

### Vercel Skills CLI

Vercel Skills CLI is a general installation method for skills and is not tied to a specific AI tool. This English README installs the English skill: -> Vercel Skills CLI 是一种通用技能安装方式，不绑定特定 AI 工具。本英文 README 默认安装英文技能：

```bash
npx skills add tanweai/pua --skill pua-en
```

If the current session does not pick up the new skill immediately, restart your AI tool. -> 如果当前会话未立即识别新技能，请重启你的 AI 工具。

### Claude Code

```bash
claude plugin marketplace add tanweai/pua
claude plugin install pua@pua-skills
```

**To update:** -> **更新：**

```bash
# Refresh marketplace cache first, then update (skipping the first step may install an old cached version) -> # 先刷新市场缓存，然后更新（跳过第一步可能会安装旧缓存版本）
claude plugin marketplace update
claude plugin update pua@pua-skills
```

**Developer install (source):** -> **开发者安装（源码）：**

```bash
git clone https://github.com/tanweai/pua ~/.claude/plugins/pua
```

Then manually register in `~/.claude/plugins/installed_plugins.json`: -> 然后在 `~/.claude/plugins/installed_plugins.json` 中手动注册：

```json
{
  "version": 2,
  "plugins": {
    "pua@pua-skills": [
      {
        "scope": "user",
        "installPath": "/Users/<you>/.claude/plugins/pua",
        "version": "2.9.0"
      }
    ]
  }
}
```

> **Windows:** use `C:/Users/<you>/.claude/plugins/pua` as `installPath`. -> > **Windows：** 将 `installPath` 使用 `C:/Users/<你>/.claude/plugins/pua`。

Restart Claude Code. To update: `git pull` inside `~/.claude/plugins/pua`. -> 重启 Claude Code。更新时：在 `~/.claude/plugins/pua` 内执行 `git pull`。

**Optional: bare command alias (requires plugin installed above — adds `/pua` without prefix):** -> **可选：裸命令别名（需先安装上述插件——添加无前缀的 `/pua`）：**

```bash
curl -o ~/.claude/commands/pua.md \
  https://raw.githubusercontent.com/tanweai/pua/main/commands/pua.md
```

Adds a bare `/pua` alias on top of the plugin. Sub-commands route through the installed plugin's skills — **the plugin must be installed first** for anything beyond `on`/`off` to work: -> 在插件基础上添加裸 `/pua` 别名。子命令通过已安装插件的技能路由 —— **必须首先安装插件**，否则除 `on`/`off` 外的功能均无法使用：

| Bare form | Equivalent plugin command |
|-----------|--------------------------|
| `/pua on` | `/pua:on` |
| `/pua off` | `/pua:off` |
| `/pua p7` | `/pua:p7` |
| `/pua p9` | `/pua:p9` |
| `/pua p10` | `/pua:p10` |
| `/pua pro` | `/pua:pro` |
| `/pua yes` | `/pua:yes` |
| `/pua mama` | `/pua:mama` |
| `/pua loop` | `/pua:pua-loop` |
| `/pua kpi` | `/pua:kpi` |
| `/pua survey` | `/pua:survey` |
| `/pua flavor` | `/pua:flavor` |

### OpenAI Codex CLI

Codex CLI uses the same Agent Skills open standard (SKILL.md). The Codex version uses a condensed description to fit Codex's length limits: -> Codex CLI 采用相同的 Agent Skills 开放标准（SKILL.md）。Codex 版本使用精简描述以适配长度限制：

**Recommended: One-command install (git clone + symlink, supports `git pull` updates)** -> **推荐：一键安装（git clone + 软链接，支持 `git pull` 更新）**

Ask Codex to run: -> 让 Codex 执行以下指令：
```
Fetch and follow instructions from https://raw.githubusercontent.com/tanweai/pua/main/.codex/INSTALL.md
```

**Manual install:** -> **手动安装：**

```bash
mkdir -p ~/.codex/skills/pua
curl -o ~/.codex/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/codex/pua/SKILL.md

mkdir -p ~/.codex/prompts
curl -o ~/.codex/prompts/pua.md \
  https://raw.githubusercontent.com/tanweai/pua/main/commands/pua.md
```

**Trigger methods:** -> **触发方式：**

| Method | Command | Requires |
|--------|---------|----------|
| Auto trigger | No action needed, matches by description -> 无需操作，通过描述匹配 | SKILL.md |
| Direct call | Type `$pua` in conversation -> 在对话中输入 `$pua` | SKILL.md |
| Manual prompt | Type `/prompts:pua` in conversation -> 在对话中输入 `/prompts:pua` | SKILL.md + prompts/pua.md |

Project-level install (current project only): -> 项目级安装（仅限当前项目）：

```bash
mkdir -p .agents/skills/pua
curl -o .agents/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/codex/pua/SKILL.md

mkdir -p .agents/prompts
curl -o .agents/prompts/pua.md \
  https://raw.githubusercontent.com/tanweai/pua/main/commands/pua.md
```

### pi coding agent

PUA now ships both a pi.dev package and a lightweight extension-only adapter. -> PUA 现已同时提供 pi.dev 包和轻量级纯扩展适配器。

Package install from this checkout: -> 从当前仓库安装软件包：

```bash
pi install ./pi/package
```

After npm publication: -> npm 发布后：

```bash
pi install npm:@tanweai/pi-pua
```

Extension-only manual install: -> 仅扩展手动安装：

```bash
mkdir -p ~/.pi/agent/extensions/pua
cp -R ./pi/pua/. ~/.pi/agent/extensions/pua/
```

Restart pi, then use `/pua-on`, `/pua-off`, `/pua-status`, and `/pua-reset`. See [`pi/pua/INSTALL.md`](pi/pua/INSTALL.md) and [`pi/package/README.md`](pi/package/README.md). -> 重启 pi，然后使用 `/pua-on`、`/pua-off`、`/pua-status` 和 `/pua-reset`。详见 [`pi/pua/INSTALL.md`](pi/pua/INSTALL.md) 与 [`pi/package/README.md`](pi/package/README.md)。

### Trae

Trae support is provided as real `SKILL.md` packs plus copyable fallback rules: -> Trae 支持以真实的 `SKILL.md` 包及可复制的备用规则形式提供：

```bash
npx skills add tanweai/pua --skill pua-trae -a trae -y
```

- Skill pack: [`.trae/skills/pua/SKILL.md`](.trae/skills/pua/SKILL.md) -> - 技能包：[`.trae/skills/pua/SKILL.md`](.trae/skills/pua/SKILL.md)
- Chinese: [`trae/pua.md`](trae/pua.md) -> - 中文版：[`trae/pua.md`](trae/pua.md)
- English: [`trae/pua-en.md`](trae/pua-en.md) -> - 英文版：[`trae/pua-en.md`](trae/pua-en.md)
- Claude Code vs Trae differences: [`trae/DIFF.md`](trae/DIFF.md) -> - Claude Code 与 Trae 的差异说明：[`trae/DIFF.md`](trae/DIFF.md)
- Install guide: [`trae/INSTALL.md`](trae/INSTALL.md) -> - 安装指南：[`trae/INSTALL.md`](trae/INSTALL.md)

### Cursor

Cursor uses `.mdc` rule files (Markdown + YAML frontmatter). The PUA rule triggers automatically via AI semantic matching (Agent Discretion mode): -> Cursor 使用 `.mdc` 规则文件（Markdown + YAML frontmatter）。PUA 规则通过 AI 语义匹配自动触发（Agent Discretion 模式）：

```bash
# Project-level install (recommended) -> # 项目级安装（推荐）
mkdir -p .cursor/rules
curl -o .cursor/rules/pua.mdc \
  https://raw.githubusercontent.com/tanweai/pua/main/cursor/rules/pua.mdc
```

### Kiro

Kiro supports two loading methods: **Steering** (auto semantic trigger) and **Agent Skills** (SKILL.md compatible). -> Kiro 支持两种加载方式：**Steering（自动语义触发）**和 **Agent Skills（兼容 SKILL.md）**。

**Option 1: Steering file (recommended)** -> **方案一：Steering 文件（推荐）**

```bash
mkdir -p .kiro/steering
curl -o .kiro/steering/pua.md \
  https://raw.githubusercontent.com/tanweai/pua/main/kiro/steering/pua.md
```

**Option 2: Agent Skills (same format as Claude Code)** -> **方案二：Agent Skills（格式同 Claude Code）**

```bash
mkdir -p .kiro/skills/pua
curl -o .kiro/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/skills/pua/SKILL.md
```

### CodeBuddy (腾讯)

CodeBuddy uses the same AgentSkills open standard (SKILL.md). Plugin and skill formats are fully compatible: -> CodeBuddy 采用相同的 AgentSkills 开放标准（SKILL.md）。插件和技能格式完全兼容：

```bash
# Option 1: Install via marketplace -> # 方案一：通过市场安装
codebuddy plugin marketplace add tanweai/pua
codebuddy plugin install pua@pua-skills

# Option 2: Manual install (global) -> # 方案二：手动安装（全局）
mkdir -p ~/.codebuddy/skills/pua
curl -o ~/.codebuddy/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/codebuddy/pua/SKILL.md
```

Project-level install (current project only): -> 项目级安装（仅限当前项目）：

```bash
mkdir -p .codebuddy/skills/pua
curl -o .codebuddy/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/codebuddy/pua/SKILL.md
```

### OpenClaw

OpenClaw uses the same AgentSkills open standard (SKILL.md). Skills work across Claude Code, Codex CLI, and OpenClaw with zero modifications: -> OpenClaw 采用相同的 AgentSkills 开放标准（SKILL.md）。技能无需任何修改即可在 Claude Code、Codex CLI 和 OpenClaw 间通用：

```bash
# Install via ClawHub -> # 通过 ClawHub 安装
clawhub install pua

# Or manual install -> # 或手动安装
mkdir -p ~/.openclaw/skills/pua
curl -o ~/.openclaw/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/skills/pua/SKILL.md
```

Project-level install (current project only): -> 项目级安装（仅限当前项目）：

```bash
mkdir -p skills/pua
curl -o skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/skills/pua/SKILL.md
```

### Google Antigravity

Antigravity uses the same AgentSkills open standard (SKILL.md). Skills work across Claude Code, Codex CLI, OpenClaw, and Antigravity with zero modifications: -> Antigravity 采用相同的 AgentSkills 开放标准（SKILL.md）。技能无需任何修改即可在 Claude Code、Codex CLI、OpenClaw 和 Antigravity 间通用：

```bash
# Global install (all projects) -> # 全局安装（所有项目）
mkdir -p ~/.gemini/antigravity/skills/pua
curl -o ~/.gemini/antigravity/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/skills/pua/SKILL.md
```

Project-level install (current project only): -> 项目级安装（仅限当前项目）：

```bash
mkdir -p .agent/skills/pua
curl -o .agent/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/skills/pua/SKILL.md
```

### OpenCode

OpenCode uses the same AgentSkills open standard (SKILL.md). Zero modifications needed: -> OpenCode 采用相同的 AgentSkills 开放标准（SKILL.md）。无需任何修改：

```bash
# Global install (all projects) -> # 全局安装（所有项目）
mkdir -p ~/.config/opencode/skills/pua
curl -o ~/.config/opencode/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/skills/pua/SKILL.md
```

Project-level install (current project only): -> 项目级安装（仅限当前项目）：

```bash
mkdir -p .opencode/skills/pua
curl -o .opencode/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/skills/pua/SKILL.md
```

### VSCode (GitHub Copilot)

VSCode Copilot uses instruction files under the `.github/` directory. Three file types for different use cases: -> VSCode Copilot 使用 `.github/` 目录下的指令文件。针对三种不同场景提供三类文件：

**Global instructions (auto-active):** -> **全局指令（自动生效）：**

```bash
mkdir -p .github
cp vscode/copilot-instructions-en.md .github/copilot-instructions.md
```

**Path-level instructions (auto-active, supports glob filtering):** -> **路径级指令（自动生效，支持 glob 过滤）：**

```bash
mkdir -p .github/instructions
cp vscode/instructions/pua-en.instructions.md .github/instructions/
```

**Manual trigger command (type `/pua` in Copilot Chat):** -> **手动触发命令（在 Copilot Chat 中输入 `/pua`）：**

```bash
mkdir -p .github/prompts
cp vscode/prompts/pua-en.prompt.md .github/prompts/
```

> **Required settings**: Method 1 — open VSCode Settings (`Ctrl+,`), search `useInstructionFiles`, enable **`github.copilot.chat.codeGeneration.useInstructionFiles`**. Method 2 — search `includeApplyingInstructions`, enable **`chat.includeApplyingInstructions`**. Method 3 requires no settings. -> > **必需设置**：方法 1 —— 打开 VSCode 设置 (`Ctrl+,`)，搜索 `useInstructionFiles`，启用 **`github.copilot.chat.codeGeneration.useInstructionFiles`**。方法 2 —— 搜索 `includeApplyingInstructions`，启用 **`chat.includeApplyingInstructions`**。方法 3 无需设置。

## Agent 团队使用指南

> **Experimental**: Agent Team requires the latest Claude Code version with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`. -> > **实验性功能**：Agent Team 需要最新版本的 Claude Code，并配置 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`。

### Prerequisites (前置条件)

```bash
# 1. Enable Agent Team -> # 1. 启用 Agent Team
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
# Or add to ~/.claude/settings.json: -> # 或添加到 ~/.claude/settings.json：
# { "env": { "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1" } }

# 2. Ensure PUA Skill is installed -> # 2. 确保已安装 PUA 技能
```

### Two Approaches (两种方案)

**Approach 1: Leader with built-in PUA (Recommended)** -> **方案一：内置 PUA 的 Leader（推荐）**

Add to your project's CLAUDE.md: -> 添加到项目的 `CLAUDE.md` 中：

```markdown
# Agent Team PUA Config -> # Agent Team PUA 配置
All teammates must load the pua skill before starting work. -> 所有队友在开始工作前必须加载 pua 技能。
Teammates report to Leader in [PUA-REPORT] format after 2+ failures. -> 失败 2 次以上时，队友以 [PUA-REPORT] 格式向 Leader 汇报。
Leader manages global pressure levels and cross-teammate failure transfer. -> Leader 管理全局压力等级及跨队友失败传递。
```

**Approach 2: Standalone PUA Enforcer watchdog (for 5+ teammates)** -> **方案二：独立 PUA Enforcer 看门狗（适用于 5+ 队友）**

```bash
mkdir -p .claude/agents
curl -o .claude/agents/pua-enforcer.md \
  https://raw.githubusercontent.com/tanweai/pua/main/agents/pua-enforcer-en.md
```

Spawn pua-enforcer as an independent watchdog in your Agent Team. -> 在你的 Agent Team 中启动独立的 pua-enforcer 看门狗。

### Orchestration Pattern (编排模式)

```
┌─────────────────────────────────────────┐
│              Leader (Opus)              │
│ Global failure count · PUA level · Race | → │ 全局失败计数 · PUA 等级 · 赛马机制 │
└────┬──────────┬──────────┬──────────┬───┘ ->     ┌────┬──────────┬──────────┬──────────┬───┐
     │          │          │          │ ->         │          │          │          │
┌────▼───┐ ┌───▼────┐ ┌───▼────┐ ┌───▼────────┐ -> ┌────▼───┐ ┌───▼────┐ ┌───▼────┐ ┌───▼────────┐
│ Team-A │ │ Team-B │ │ Team-C │ │  Enforcer  | → │ Self-PUA │ │Self-PUA│ │Self-PUA│ │  Watchdog  │
│Self-PUA│ │Self-PUA│ │Self-PUA│ │  Watchdog  | → │Report ↑│ │Report ↑│ │Report ↑│ │  Intervene │
│Report ↑│ │Report ↑│ │Report ↑│ │  Intervene | → └────────┘ └────────┘ └────────┘ └────────────┘
└────────┘ └────────┘ └────────┘ └────────────┘ -> 
```

### Known Limitations (已知限制)

| Limitation | Workaround |
|-----------|-----------|
| Teammates can't spawn subagents -> 队友无法生成子 Agent | Teammates self-enforce PUA methodology internally -> 队友在内部自行强制执行 PUA 方法论 |
| No persistent shared variables -> 无持久化共享变量 | State transferred via `[PUA-REPORT]` message format -> 通过 `[PUA-REPORT]` 消息格式传递状态 |
| Broadcast is one-way -> 广播为单向 | Leader acts as centralized coordinator -> Leader 充当集中协调器 |

## 架构与命令

### Trigger Methods by Platform (各平台触发方式)

| Platform | Auto-trigger | Manual trigger |
|----------|-------------|----------------|
| **Claude Code** | Yes (skill description matching) -> 是（技能描述匹配） | See commands below -> 见下方命令 |
| **Codex CLI** | Yes (skill description matching) -> 是（技能描述匹配） | `$pua` or `/prompts:pua` -> `$pua` 或 `/prompts:pua` |
| **Cursor** | Yes (`.mdc` rule, Agent Discretion) -> 是（`.mdc` 规则，Agent Discretion） | — (auto only) -> —（仅自动） |
| **Kiro** | Yes (steering file or skill) -> 是（Steering 文件或技能） | — (auto only) -> —（仅自动） |
| **CodeBuddy** | Yes (skill description matching) -> 是（技能描述匹配） | Plugin commands (same as Claude Code) -> 插件命令（同 Claude Code） |
| **OpenClaw** | Yes (skill description matching) -> 是（技能描述匹配） | — |
| **Google Antigravity** | Yes (skill description matching) -> 是（技能描述匹配） | — |
| **OpenCode** | Yes (skill description matching) -> 是（技能描述匹配） | — |
| **VSCode Copilot** | Yes (instructions file) -> 是（指令文件） | `/pua` in Copilot Chat -> Copilot Chat 中 `/pua` |

> **Note:** Sub-modes (p7/p9/p10/pro/yes/pua-loop) are **Claude Code only** — other platforms install the core skill only. -> > **注意：** 子模式（p7/p9/p10/pro/yes/pua-loop）仅支持 **Claude Code** —— 其他平台仅安装核心技能。

### Architecture (Claude Code) (架构 Claude Code)

```
/pua:pua        → Core engine — red lines + flavor + pressure + methodology router (v3) -> /pua:pua        → 核心引擎 — 红线 + 风格 + 压力 + 方法论路由器 (v3)
/pua:p7         → P7 Senior Engineer — solution-driven execution -> /pua:p7         → P7 高级工程师 —— 方案驱动执行
/pua:p9         → P9 Tech Lead — Task Prompt management, agent teams -> /pua:p9         → P9 技术总监 —— 任务提示词管理、Agent 团队管理
/pua:p10        → P10 CTO — strategic direction -> /pua:p10        → P10 CTO —— 战略方向
/pua:pro        → Self-evolution + KPI + rank system + survey -> /pua:pro        → 自我进化 + KPI + 职级系统 + 问卷调研
/pua:yes        → ENFP encouragement mode (same rules, opposite vibes) -> /pua:yes        → ENFP 鼓励模式（规则相同，氛围相反）
/pua:mama       → Chinese mom nagging mode (same rules, mom-style rhetoric) -> /pua:mama       → 中国妈妈唠叨模式（规则相同，妈味话术）
/pua:shot       → v2 concentrated single-file (449 lines, zero deps, full context injection) -> /pua:shot       → v2 浓缩单文件（449 行、零依赖、完整上下文注入）
/pua:pua-loop   → Auto-iteration (PUA pressure × iterative loop; signals: <loop-abort>, <loop-pause>) -> /pua:pua-loop   → 自动迭代（PUA 压力 × 迭代循环；信号：`<loop-abort>`、`<loop-pause>`）
/pua:pua-en     → English PIP Edition -> /pua:pua-en     → 英文 PIP 版
/pua:pua-ja     → Japanese Edition -> /pua:pua-ja     → 日文版

Hooks (v3, Claude Code only): -> Hook 机制（v3，仅 Claude Code）：
  SessionStart  → additionalContext injection (flavor + methodology + router) ->   SessionStart  → 注入 additionalContext（风格 + 方法论 + 路由器）
  PostToolUse   → Bash failure detection → L1-L4 pressure + methodology switch ->   PostToolUse   → 检测 Bash 失败 → L1-L4 压力升级 + 方法论切换
  UserPromptSubmit → Script-level frustration filtering → PUA context ->   UserPromptSubmit → 脚本级挫败感过滤 → PUA 上下文注入
  PreCompact    → State preservation (pressure level + failure count) ->   PreCompact    → 状态保存（压力等级 + 失败计数）
  Stop          → Feedback collection + PUA Loop continuation ->   Stop          → 收集反馈 + PUA Loop 继续执行
  SubagentStop  → Agent lifecycle accounting (v3.2) — writes teardown.jsonl, removes from active-agents.json ->   SubagentStop  → Agent 生命周期记账 (v3.2) —— 写入 teardown.jsonl，从 active-agents.json 移除
```

### Commands (Claude Code) (命令 Claude Code)

> **Note:** Sub-modes (p7/p9/p10/pro/yes/pua-loop) are Claude Code only. -> > **注意：** 子模式仅支持 Claude Code。
> Each command has two equivalent forms: standalone (`/pua:on`) or via the main command (`/pua:pua on`). Both work identically. -> 每个命令有两种等效形式：独立使用（`/pua:on`）或通过主命令调用（`/pua:pua on`）。两者效果相同。

| Command | Description |
|---------|-------------|
| `/pua:pua` | Core PUA engine (Alibaba flavor default) -> 核心 PUA 引擎（阿里风格默认） |
| `/pua:p7` | P7 Senior Engineer — solution-driven execution -> P7 高级工程师 —— 方案驱动执行 |
| `/pua:p9` | P9 Tech Lead — write prompts, manage agents -> P9 技术总监 —— 编写提示词、管理 Agent |
| `/pua:p10` | P10 CTO — strategic direction -> P10 CTO —— 战略方向 |
| `/pua:pro` | Self-evolution + KPI + rank system -> 自我进化 + KPI + 职级系统 |
| `/pua:yes` | ENFP encouragement mode — 70% encourage + 20% serious + 10% roast -> ENFP 鼓励模式 —— 70% 鼓励 + 20% 认真 + 10% 吐槽 |
| `/pua:mama` | Chinese mom nagging mode — same core rules, mom-style rhetoric -> 中国妈妈唠叨模式 —— 核心规则相同，妈味话术 |
| `/pua:shot` | v2 concentrated single-file — 449 lines, zero deps, for sub-agent injection -> v2 浓缩单文件 —— 449 行、零依赖，用于子 Agent 注入 |
| `/pua:pua-loop` | Auto-iteration — runs until done or max iterations; `<loop-abort>reason</loop-abort>` to stop, `<loop-pause>what</loop-pause>` to pause -> 自动迭代 —— 循环执行至完成或达到最大次数；`<loop-abort>原因</loop-abort>` 停止，`<loop-pause>内容</loop-pause>` 暂停 |
| `/pua:on` | Always-on mode (auto-PUA every session) -> 常驻模式（每次会话自动 PUA） |
| `/pua:off` | Turn off always-on + feedback -> 关闭常驻 + 反馈 |
| `/pua:offline` 🆕 | **v3.3** — Offline mode: disable feedback/leaderboard network flows while keeping local PUA behavior -> **v3.3** —— 离线模式：禁用反馈/排行榜网络请求，保留本地 PUA 行为 |
| `/pua:survey` | Research questionnaire (7 sections) -> 调研问卷（7 个板块） |
| `/pua:flavor` | Switch between 14 corporate flavors -> 切换 14 种大厂风格 |
| `/pua:kpi` | Generate KPI report card -> 生成 KPI 成绩单 |
| `/pua:cancel-pua-loop` | Cancel active PUA Loop (removes state file) -> 取消活跃的 PUA Loop（移除状态文件） |
| `/pua:team-status` 🆕 | **v3.2** — List all active agents with PID/TTL/age (Netflix Keeper Test: who's still on the court?) -> **v3.2** —— 列出所有活跃 Agent 及其 PID/TTL/运行时长（Netflix 留任测试：谁还在场上？） |
| `/pua:reap-orphans` 🆕 | **v3.2** — Scan and reclaim stale agents (state mtime > 30min, no heartbeat) -> **v3.2** —— 扫描并回收僵尸 Agent（状态修改时间 > 30分钟，无心跳） |
| `/pua:teardown-all` 🆕 | **v3.2** — Cascading release of all active agents (P10 → P9 → P8 → P7 all off the court) -> **v3.2** —— 级联释放所有活跃 Agent（P10 → P9 → P8 → P7 全部下场） |

## High-Agency: PUA v2 Evolution (高能动性：PUA v2 演进)

**High-Agency** is PUA's next-generation evolution — same corporate pressure, same culture, but with a **self-sustaining inner drive engine**. -> **High-Agency（高能动性）** 是 PUA 的下一代演进——同样的企业压力，同样的文化内核，但内置了**自维持的内驱力引擎**。

PUA v1 = pure external pressure (turbocharger — needs fuel, stalls across sessions) -> PUA v1 = 纯外部压力（涡轮增压器——需要燃料，跨会话易熄火）
High-Agency = external pressure + inner drive (nuclear reactor — self-sustaining chain reaction) -> High-Agency = 外部压力 + 内驱力（核反应堆——自持链式反应）

### High-Agency New Features (High-Agency 新功能)

| Feature | PUA v1 | High-Agency (v2) |
|---------|--------|-----------------|
| Iron rules | 3 (exhaust all, act first, take initiative) -> 3（穷尽一切、先行动、强主动） | **5** (+full-chain audit, +knowledge persistence) -> **5**（+全链路审计、+知识持久化） |
| Failure recovery | L1-L4 pressure escalation -> L1-L4 压力升级 | **Recovery Protocol before L1** (self-rescue window) -> **L1 前恢复协议**（自救窗口期） |
| Quality control | L3 triggers 7-item checklist -> L3 触发七点检查清单 | **Quality Compass** (5-question self-check per delivery) -> **质量罗盘**（每次交付进行 5 问自检） |
| Cross-session learning | None (resets each session) -> 无（每次会话重置） | **Metacognition engine** (builder-journal.md persists lessons) -> **元认知引擎**（`builder-journal.md` 持久化经验教训） |
| Positive feedback | None -> 无 | **Trust level T1-T3** (auto-upgrade on sustained quality) -> **信任等级 T1-T3**（持续高质量自动升级） |
| Calibration | None -> 无 | **[Calibration] module** ("good enough" = must/should/could tiers) -> **[校准] 模块**（“够用” = must/should/could 分级） |
| Dependency analysis | None -> 无 | **Full-chain audit** (map all deps before touching any hop) -> **全链路审计**（触碰任何环节前绘制完整依赖图） |

### Five Pillars (Theoretical Foundation) (五大支柱：理论基础)

Based on research into high-agency individuals: -> 基于对高能动性个体的研究：

1. **Irreconcilable inner tension** — eternal gap between "how it should be" and "how it is" drives continuous improvement -> 1. **不可调和的内生张力** —— “理想状态”与“现实状态”之间的永恒差距驱动持续改进
2. **Micro-win anchors** — `[WIN]` markers celebrate each step forward, building momentum -> 2. **微胜锚点** —— `[WIN]` 标记庆祝每一步进展，积累势能
3. **Internalized standards** — Quality Compass: you are your own first reviewer, not because someone checks, but because your standards won't allow sloppiness -> 3. **内化标准** —— 质量罗盘：你是自己的第一位审查者，不是因为你有人检查，而是因为你的标准不容许敷衍
4. **Action-oriented identity** — P8 identity anchor: every action reflects who you are, not just what you were told to do -> 4. **行动导向的身份认同** —— P8 身份锚点：每个行为都反映你是谁，而不仅是被要求做什么
5. **Self-repair mechanism** — Recovery Protocol: self-diagnose when stuck before triggering external pressure -> 5. **自我修复机制** —— 恢复协议：卡住时先自我诊断，再触发外部压力

> High-Agency features are built into the current pua skill. No separate install needed. -> > High-Agency 功能已内置于当前 pua 技能中。无需单独安装。

## Methodology Router: PUA v3 (Claude Code) (方法论路由器：PUA v3 Claude Code)

**v3 = v2 + intelligent methodology routing + code-level behavioral detection** -> **v3 = v2 + 智能方法论路由 + 代码级行为检测**

PUA v2 used pressure rhetoric to motivate. v3 goes further: it automatically selects the **best problem-solving methodology** for each task type, and when that methodology fails, it switches to a different one. -> PUA v2 用压力话术激励。v3 更进一步：自动为每种任务类型选择**最佳问题解决方法论**，并在该方法失败时切换到另一种。

### How It Works (工作原理)

```
Task arrives → Analyze type → Auto-select best methodology -> 接收任务 → 分析类型 → 自动选择最佳方法论
                                    ↓ ->                                     ↓
              Debug? → 🔴 Huawei (RCA root cause + Blue Army) ->               调试？→ 🔴 华为（RCA 根因 + 蓝军）
              Build? → ⬛ Musk (The Algorithm: question→delete→simplify) ->               构建？→ ⬛ 马斯克（The Algorithm：质疑→删除→简化）
              Research? → ⚫ Baidu (search everything first) ->               调研？→ ⚫ 百度（先搜索一切）
              Architecture? → 🔶 Amazon (Working Backwards) ->               架构设计？→ 🔶 亚马逊（逆向工作法）
              Performance? → 🟡 ByteDance (A/B test + data-driven) ->               性能优化？→ 🟡 字节（A/B 测试 + 数据驱动）
              Default → 🟠 Alibaba (closed-loop methodology) ->               默认 → 🟠 阿里（闭环方法论）
                                    ↓ ->                                     ↓
              Executing with selected methodology... ->               使用选定方法执行中...
                                    ↓ ->                                     ↓
              2 consecutive failures? → L1: switch approach ->               连续失败 2 次？→ L1：切换方案
              3 failures? → L2: SUGGEST switching methodology ->               失败 3 次？→ L2：建议切换方法论
              5+ failures? → L4: FORCE switch to next methodology ->               失败 5+ 次？→ L4：强制切换到下一套方法论
                                    ↓ ->                                     ↓
              Methodology Switch Chains (never repeat a failed one): ->               方法论切换链（绝不重复已失败的方案）：
              Spinning → ⬛ Musk → 🟣 Pinduoduo → 🔴 Huawei ->               原地打转 → ⬛ 马斯克 → 🟣 拼多多 → 🔴 华为
              Giving up → 🟤 Netflix → 🔴 Huawei → ⬛ Musk ->               放弃治疗 → 🟤 网飞 → 🔴 华为 → ⬛ 马斯克
              Poor quality → ⬜ Jobs → 🟧 Xiaomi → 🟤 Netflix ->               质量低下 → ⬜ 乔布斯 → 🟧 小米 → 🟤 网飞
              Not searching → ⚫ Baidu → 🔶 Amazon → 🟡 ByteDance ->               不搜索 → ⚫ 百度 → 🔶 亚马逊 → 🟡 字节
```

### v3 Hook System (Claude Code only) (v3 Hook 系统：仅 Claude Code)

| Hook | Trigger | What It Does |
|------|---------|-------------|
| **SessionStart** | Every session -> 每次会话 | Injects behavioral protocol + methodology + router via `additionalContext` (system-level, not advisory) -> 通过 `additionalContext` 注入行为协议 + 方法论 + 路由器（系统级，非建议级） |
| **PostToolUse** | After every Bash command -> 每次 Bash 命令后 | Detects consecutive failures, auto-escalates pressure L1→L4, suggests/forces methodology switch -> 检测连续失败，自动升级压力 L1→L4，建议/强制切换方法论 |
| **UserPromptSubmit** | User frustration phrases -> 用户挫败感短语 | Intercepts "又错了", "try harder", etc. BEFORE model responds, injects filtered PUA context -> 在模型响应前拦截“又错了”、“再试一次”等，注入过滤后的 PUA 上下文 |
| **PreCompact** | Before context compression -> 上下文压缩前 | Saves pressure level + failure count to survive compaction -> 保存压力等级 + 失败计数以抵御压缩丢失 |

### Key Difference from v2 (与 v2 的核心区别)

| | v2 | v3 |
|---|---|---|
| Trigger mechanism | Skill description matching (model decides) -> 技能描述匹配（模型决定） | **Code-level hooks** (deterministic, can't be ignored) -> **代码级 Hook**（确定性触发，不可忽略） |
| Methodology | Single methodology, all flavors use same approach -> 单一方法论，所有风格共用同一套方案 | **14 distinct methodologies**, auto-routed by task type -> **14 种独立方法论**，按任务类型自动路由 |
| Failure response | Escalate pressure within same methodology -> 在同一方法论内升级压力 | **Switch to different methodology** based on failure pattern -> **根据失败模式切换到不同方法论** |
| System injection | Plain text output (advisory) -> 纯文本输出（建议级） | **`additionalContext` JSON** (system-level, like Superpowers) -> **`additionalContext` JSON**（系统级，类似 Superpowers） |

> v3 hook features require Claude Code. Other platforms use the core skill without hooks. -> > v3 Hook 功能需依赖 Claude Code。其他平台使用无 Hook 的核心技能即可。

## Works Well With (搭配使用效果更佳)

- `/pua:p9` — P9 Tech Lead mode for managing agent teams -> - `/pua:p9` —— P9 技术总监模式，用于管理 Agent 团队
- `/pua:pro` — Self-evolution tracking, KPI reports, rank system -> - `/pua:pro` —— 自我进化追踪、KPI 报告、职级系统
- `superpowers:systematic-debugging` — PUA adds motivation layer, systematic-debugging provides methodology -> - `superpowers:systematic-debugging` —— PUA 增加动力层，systematic-debugging 提供方法论
- `superpowers:verification-before-completion` — Prevents false "fixed" claims -> - `superpowers:verification-before-completion` —— 防止虚假“已修复”声明

## Contribute Data (贡献数据)

Upload your Claude Code / Codex CLI conversation logs (`.jsonl`) to help us improve PUA Skill's effectiveness. -> 上传你的 Claude Code / Codex CLI 对话日志（`.jsonl`），帮助我们优化 PUA 技能的效果。

**[在此上传 ->](https://openpua.ai/contribute.html)**

Uploaded files are used for Benchmark testing and Ablation Study analysis to quantify how different PUA strategies affect AI debugging behavior. -> 上传文件将用于基准测试与消融实验分析，量化不同 PUA 策略对 AI 调试行为的影响。

Get your `.jsonl` files: -> 获取你的 `.jsonl` 文件：
```bash
# Claude Code -> ls ~/.claude/projects/*/sessions/*.jsonl
# Codex CLI -> ls ~/.codex/sessions/*.jsonl
```

## Star History (Star 历史)

[![Star History Chart](https://api.star-history.com/svg?repos=tanweai/pua&type=Date)](https://star-history.com/#tanweai/pua&Date)

## License (许可证)

MIT

## Credits (鸣谢)

By [TanWei Security Lab](https://github.com/tanweai) — making AI try harder, one PUA at a time. -> 由 [TanWei Security Lab](https://github.com/tanweai) 打造 —— 让 AI 更努力一点，一次一个 PUA。