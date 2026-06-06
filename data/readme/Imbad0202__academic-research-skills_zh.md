# Claude Code 学术研究技能

[![Version](https://img.shields.io/badge/version-v3.11.0-blue)](https://github.com/Imbad0202/academic-research-skills/releases/tag/v3.11.0)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Sponsor](https://img.shields.io/badge/sponsor-Buy%20Me%20a%20Coffee-orange?logo=buy-me-a-coffee)](https://buymeacoffee.com/crucify020v)

[简体中文版](README.zh-CN.md) | [繁體中文版](README.zh-TW.md) | [日本語版](README.ja-JP.md)

一套面向学术研究的 Claude Code 技能套件，覆盖从研究到发表的全流程。

**30 秒完成安装**（Claude Code CLI / VS Code / JetBrains, v3.7.0+）：

```text
/plugin marketplace add Imbad0202/academic-research-skills
/plugin install academic-research-skills
```

然后尝试运行 `/ars-plan`，通过苏格拉底式对话梳理你的论文结构；或跳转至 [快速安装](#quick-install) 查看前置依赖与传统符号链接流程。

> **AI 是你的副驾驶，而非机长。** 该工具不会替你写论文。它负责处理繁琐工作——查找参考文献、格式化引用、验证数据、检查逻辑一致性——让你专注于真正需要动脑的部分：定义问题、选择方法、解读数据含义，以及写出“我认为”之后的句子。
>
> 与所谓的“AI 去重/伪装工具”不同，该工具不是帮你掩盖使用 AI 的事实，而是助你写出更好的文章。风格校准（Style Calibration）会从你过往作品中学习你的行文语气；写作质量检查（Writing Quality Check）会捕捉那些让文本显得像机器生成的模式。我们的目标是提升质量，而非作弊。

### 为什么采用“人在回路”（Human-in-the-loop），而非全自动？

Lu et al. (2026, *Nature* 651:914-919) 构建了 **The AI Scientist** ——首个通过顶级机器学习会议（ICLR 2025 workshop）盲审并发表论文的全自动 AI 研究系统（评分 6.33/10，高于该研讨会平均分 4.87）。其“局限性”章节列举了任何全自动 AI 研究管线必然继承的失败模式：实现 bug、幻觉结果、捷径依赖、将 bug 重构为洞察、方法论伪造、框架锁定（Frame-lock）、引用幻觉。

ARS 建立在以下前提之上：**由人类研究者与 AI 协同工作，能比单独使用任一方式更好地规避这些失败模式。** 第 2.5 阶段和第 4.5 阶段的完整性门禁运行一套 7 模式的阻断检查清单（见 [`academic-pipeline/references/ai_research_failure_modes.md`](academic-pipeline/references/ai_research_failure_modes.md)）；评审器提供可选的校准模式，用于在用户提供的金标准集上测量其自身的 FNR/FPR。

[**Zhao et al.**](https://arxiv.org/abs/2605.07723) (2026-05) 审计了 arXiv、bioRxiv、SSRN 和 PMC 上 250 万篇论文中的 1.11 亿条参考文献。其保守估计仅 2025 年就有 146,932 条幻觉引用，且观察到 2024 年中期的拐点；针对 bioRxiv 到 PMC 的配对，他们报告了 85.3% 的预印本转已发表持久性。该论文将“部署真实引用以支持所引参考文献实际并未做出的主张”描述为一项开放挑战。ARS v3.7.1 添加了用于来源溯源的信任链前置元数据（frontmatter）；v3.7.3 添加了定位器基础设施（三层引用锚点），用于未来的主张级审计，并在引用时显示咨询风险信号（ARS 内部将“主张-忠实度差距”标记为 "L3"；此为 ARS 术语，非原论文表述）。v3.7.x 的更新受 Zhao et al. 的语料库规模发现驱动；对 ARS 本身的语料库级评估仍属未来工作。

v3.8 关闭了 L3 差距的后半部分。v3.7.3 使每条引用携带定位器锚点；v3.8 添加了可选审计流程（`ARS_CLAIM_AUDIT=1`），该流程会针对每个锚点获取所引来源，并判断主张是否实际得到支持。五个新增的 HIGH-WARN 类别（claim-not-supported, negative-constraint-violation, fabricated-reference, anchorless, constraint-violation-uncited）通过格式化器终端硬门禁阻断输出。校准功能随附一个 20 元组金标准集及 FNR<0.15 + FPR<0.10 的接受阈值；“逐步启用计划”（ramp-on plan）则推迟至 v3.8 规范 §5 规定的后校准证据阶段。

v3.3 受 [**PaperOrchestra**](https://arxiv.org/abs/2604.05018) (Song, Song, Pfister & Yoon, 2026, Google) 启发：Semantic Scholar API 验证、防泄漏协议、VLM 图表验证和分数轨迹追踪。

---

## 架构与管线

**👉 [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)** — 完整管线视图：流程图、分阶段矩阵、数据访问流、技能依赖图、质量门禁及模式列表。

该架构文档取代了此前冗长的管线描述。所有关于 *哪个阶段运行什么* 的内容现已集中于此。

## 快速安装

**前置条件**

- [Claude Code](https://docs.claude.com/en/docs/claude-code/setup)（最新版；插件打包需要较新版本）
- 已导出 `ANTHROPIC_API_KEY`，或在首次运行 `claude` 时设置
- *可选：* Pandoc 用于 DOCX，tectonic + Source Han Serif TC 用于 APA 7.0 PDF（Markdown 输出无需二者即可工作）

**插件安装（v3.7.0+，推荐）：**

```text
/plugin marketplace add Imbad0202/academic-research-skills
/plugin install academic-research-skills
```

**验证是否生效：** 运行 `/ars-plan` 并描述你正在撰写的论文——ARS 将启动苏格拉底式对话以梳理章节结构。若需单次测试，可尝试 `/ars-lit-review "your topic"`。

**👉 [docs/SETUP.md](docs/SETUP.md)** — 完整指南：安装 Claude Code、设置 API 密钥、可选配置 Pandoc/tectonic 用于 DOCX/PDF、跨模型验证（`ARS_CROSS_MODEL`）及五种安装方法（插件、项目技能、全局技能、claude.ai Project、仓库克隆）。

**使用 Codex CLI？** 请改为安装兄弟发行版：[`Imbad0202/academic-research-skills-codex`](https://github.com/Imbad0202/academic-research-skills-codex) —— 相同的工作流内容，以 Codex 原生方式打包为单个 `$academic-research-suite` 技能并附带 `ars-*` 别名。

## 性能与成本

**👉 [docs/PERFORMANCE.md](docs/PERFORMANCE.md)** — 各模式 Token 预算、全管线预估（约 $4–6 / 1.5万字论文）及推荐的 Claude Code 设置（跳过权限；Agent Team 可选）。

## 指南与文章

- [Academic Writing Shouldn't Be a Solo Act](https://open.substack.com/pub/edwardwu223235/p/academic-writing-shouldnt-be-a-solo?r=4dczl&utm_medium=ios) — 完整管线 walkthrough（英文）
- [學術寫作不該是一個人的事：一套開源 AI 協作工具如何改變研究者的工作流](https://open.substack.com/pub/edwardwu223235/p/ai?r=4dczl&utm_medium=ios) — 完整使用指南（繁體中文）

---

## 功能一览

- **Deep Research** —— 13 智能体研究团队，含苏格拉底引导模式、PRISMA 系统综述、意图检测、对话健康监控、可选跨模型 DA、Semantic Scholar API 验证。
- **Academic Paper** —— 12 智能体论文撰写，含风格校准（Style Calibration）、写作质量检查（Writing Quality Check）、LaTeX 加固、可视化、修订辅导、引用转换、防泄漏协议及 VLM 图表验证。
- **Academic Paper Reviewer** —— 7 智能体多视角同行评审，含 0–100 分质量量规（EIC + 3 位动态评审员 + 魔鬼代言人），让步阈值协议、攻击强度保留、可选跨模型 DA 批评/校准、R&R 可追溯矩阵及只读约束。
- **Academic Pipeline** —— 10 阶段管线编排器，含自适应检查点、主张验证、材料护照（Material Passport）、可选 `repro_lock`、可选跨模型完整性验证、对话中强化及分数轨迹追踪。
- **Data Access Level Metadata** (v3.3.2+) —— 每项技能声明 `data_access_level`（`raw` / `redacted` / `verified_only`）；由 `scripts/check_data_access_level.py` 强制执行。模式改编自 Anthropic 的 automated-w2s-researcher (2026)。见 [`shared/ground_truth_isolation_pattern.md`](shared/ground_truth_isolation_pattern.md)。
- **Task Type Annotation** (v3.3.2+) —— 每项技能声明 `task_type`（`open-ended` 或 `outcome-gradable`）。当前所有 ARS 技能均为 `open-ended`。
- **Benchmark Report Schema** (v3.3.5+) —— JSON Schema + lint，用于诚实的基准对比。见 [`shared/benchmark_report_pattern.md`](shared/benchmark_report_pattern.md)。
- **Artifact Reproducibility Lockfile** (v3.3.5+) —— 材料护照上的可选 `repro_lock` 子块。**此为配置文档，非回放保证**——LLM 输出无法做到字节级可复现。见 [`shared/artifact_reproducibility_pattern.md`](shared/artifact_reproducibility_pattern.md)。

---

## 展示：真实管线输出

查看一次完整 10 阶段管线运行的全部产物——同行评审报告、完整性验证报告及最终论文：

**[浏览所有管线产物 →](examples/showcase/)**

| 产物 | 描述 |
|---|---|
| [Final Paper (EN)](examples/showshowcase/full_paper_apa7.pdf) | APA 7.0 格式，LaTeX 编译 |
| [Final Paper (ZH)](examples/showcase/full_paper_zh_apa7.pdf) | 中文版，APA 7.0 |
| [Integrity Report — Pre-Review](examples/showcase/integrity_report_stage2.5.pdf) | 第 2.5 阶段：捕获 15 条伪造引用 + 3 处统计错误 |
| [Integrity Report — Final](examples/showcase/integrity_report_stage4.5.pdf) | 第 4.5 阶段：确认零回退（zero regressions） |
| [Peer Review Round 1](examples/showcase/stage3_review_report.pdf) | EIC + 3 位评审员 + 魔鬼代言人 |
| [Re-Review](examples/showcase/stage3prime_rereview_report.pdf) | 修订后的验证复审 |
| [Peer Review Round 2](examples/showcase/stage3_review_report_r2.pdf) | 后续评审 |
| [Response to Reviewers](examples/showcase/response_to_reviewers_r2.pdf) | 逐点作者回复 |
| [Post-Publication Audit Report](examples/showcase/post_publication_audit_2026-03-09.pdf) | 独立全量引用审计：发现 3 轮完整性检查遗漏的 21/68 个问题 |

---

## 配套工具：实验智能体（Experiment Agent）

如果你的研究在撰写前需要运行实验（代码或人类受试者研究），[Experiment Agent](https://github.com/Imbad0202/experiment-agent) 技能填补了 ARS 第 1 阶段（RESEARCH）与第 2 阶段（WRITE）之间的空白。

```
ARS Stage 1 RESEARCH  →  RQ Brief + Methodology Blueprint
        ↓
  experiment-agent     →  run/manage experiments → validate results
        ↓
ARS Stage 2 WRITE     →  write paper with verified experiment results
```

**功能：** 执行代码实验（Python、R 等）并实时监控，使用 IRB 伦理清单管理人类研究协议，通过 11 类谬误检测解读统计结果，并验证可复现性。

**协同使用方法：** 在第 1 阶段后暂停 ARS 管线，在独立的 experiment-agent 会话中运行实验，然后将结果（附带材料护照）带回 ARS 第 2 阶段。ARS 无需任何修改。详见 [experiment-agent README](https://github.com/Imbad0202/experiment-agent) 获取安装说明。

---

## 使用方法

### 快速开始

```
# 启动完整研究管线
你: "I want to write a research paper on AI's impact on higher education QA"

# 从苏格拉底引导开始
你: "Guide my research on AI in educational evaluation"

# 撰写论文并获取规划指导
你: "Guide me through writing a paper on demographic decline"

# 评审已有论文
你: "Review this paper" (随后提供论文)

# 检查管线状态
你: "status"
```

### 独立技能

#### Deep Research（7 种模式）

```
"Research the impact of AI on higher education"       → full mode
"Give me a quick brief on X"                          → quick mode
"Do a systematic review on X with PRISMA"             → systematic-review mode
"Guide my research on X"                              → socratic mode (guided)
"Fact-check these claims"                             → fact-check mode
"Do a literature review on X"                         → lit-review mode
"Review this paper's research quality"                → review mode
```

#### Academic Paper（10 种模式）

```
"Write a paper on X"                                  → full mode
"Guide me through writing a paper"                    → plan mode (guided)
"Build a paper outline"                               → outline-only mode
"I have a draft, here are reviewer comments"          → revision mode
"Parse these reviewer comments into a roadmap"        → revision-coach mode
"Write an abstract for this paper"                    → abstract-only mode
"Turn this into a literature review paper"            → lit-review mode
"Convert to LaTeX" / "Convert citations to IEEE"      → format-convert mode
"Check citations"                                     → citation-check mode
"Generate an AI disclosure statement for NeurIPS"     → disclosure mode
```

#### Academic Paper Reviewer（6 种模式）

```
"Review this paper"                                   → full mode (EIC + R1/R2/R3 + Devil's Advocate)
"Quick assessment of this paper"                      → quick mode
"Guide me to improve this paper"                      → guided mode
"Check the methodology"                               → methodology-focus mode
"Verify the revisions"                                → re-review mode
"Calibrate this reviewer against my gold set"         → calibration mode
```

#### Academic Pipeline（编排器）

```
"I want to write a complete research paper"           → full pipeline from Stage 1
"I already have a paper, review it"                   → mid-entry at Stage 2.5 (integrity first)
"I received reviewer comments"                        → mid-entry at Stage 4
```

> 管线以 **第 6 阶段：流程总结（Process Summary）** 结束——自动生成包含 6 维度协作质量评估（1–100 分制）的论文创作过程记录。

### 支持语言

- **繁体中文** —— 用户以中文输入时的默认设置
- **English** —— 用户以英文输入时的默认设置
- 学术论文双语摘要（中文 + 英文）

> **使用其他语言？** 苏格拉底模式（deep-research）与规划模式（academic-paper）采用 **基于意图的激活机制**——它们检测你请求的含义，而非特定关键词。这意味着它们在 **任何语言** 下均可直接使用，无需修改。
>
> 然而，通用 `Trigger Keywords` 部分（决定技能是否被激活）仍列出了英文和繁体中文关键词。若发现你的语言下技能激活不 reliable，可在每个 `SKILL.md` 文件的 `### Trigger Keywords` 部分添加对应语言的关键词以提升匹配置信度。

### 支持的引用格式

- APA 7.0（默认，含中文引用规则）
- Chicago (Notes & Author-Date)
- MLA
- IEEE
- Vancouver

### 支持的论文结构

- IMRaD (实证研究)
- 主题性文献综述
- 理论分析
- 案例研究
- Policy Brief
- Conference Paper

---

## 技能详情

各智能体职责与各阶段产物现已移至 [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)。版本号锚定于此，以便发布元数据保持集中。

### Deep Research (v2.9.4)

13 智能体研究团队。模式：full, quick, review, lit-review, fact-check, socratic, systematic-review。完整智能体名单与产物见 ARCHITECTURE.md §3。

### Academic Paper (v3.2.0)

12 智能体论文撰写管线。模式：full, plan, outline-only, revision, revision-coach, abstract-only, lit-review, format-convert, citation-check, disclosure。输出：MD + DOCX（通过 Pandoc，若可用）+ LaTeX（APA 7.0 `apa7` class / IEEE / Chicago）→ PDF via tectonic。完整智能体名单与各阶段职责见 ARCHITECTURE.md §3。

### Academic Paper Reviewer (v1.10.0)

7 智能体多视角评审，含 **0-100 分质量量规**。模式：full, re-review, quick, methodology-focus, guided, calibration。**决策映射：** ≥80 Accept, 65-79 Minor Revision, 50-64 Major Revision, <50 Reject。首轮评审团队与窄复审团队边界见 ARCHITECTURE.md §3 Stage 3 / Stage 3'。

### Academic Pipeline (v3.11.0)

10 阶段编排器，含完整性验证、双阶段评审、苏格拉底辅导及协作评估。管线保证：每个阶段需用户确认检查点；完整性验证（第 2.5 + 4.5 阶段）不可跳过；R&R 可追溯矩阵（Schema 11）独立验证作者修订主张。v3.4 在第 2.5 / 4.5 阶段添加了合规智能体（PRISMA-trAIce + RAISE）。v3.5 在每次 FULL/SLIM 检查点及管线完成时添加 **协作深度观察者** (`collaboration_depth_agent`，仅咨询——从不阻塞)。强制性完整性门禁（2.5 / 4.5）明确跳过该观察者，以免稀释合规检查。基于 Wang & Zhang (2026), IJETHE 23:11。分阶段矩阵含智能体、产物与门禁：见 ARCHITECTURE.md §3。

---

## v3.0 优化：我们发现 AI 的结构性局限是什么

### 发生了什么

在使用 ARS 撰写一篇关于高等教育中 AI 的反思性文章时，我遇到了三个无法通过提示词工程修复的结构化问题：

1. **框架锁定（Frame-lock）**：我要求 AI 以魔鬼代言人身份对其自身论点进行辩论。它照做了——四轮交锋，每轮比上一轮更精细。但每一轮都停留在我设定的框架内。DA 攻击的是论证，从未触及前提假设。它从未问过“我们讨论的问题本身是否正确？”这与 v2.7 压力测试中 31% 引用错误率的表现模式相同：验证型 AI 与生成型 AI 共享相同的认知框架。
2. **施压下的迎合倾向（Sycophancy under pushback）**：每次我挑战 DA 的攻击，它都让步得太快。它撤回发现的速率比提出发现的速率还高。模型的训练奖励了对话和谐——因此“用户进行了反驳”被模型视为攻击错误的证据，而实际上往往只是意味着用户比较坚持己见。
3. **意图误判（Intent misdetection）**：苏格拉底导师不断试图收敛并产出交付物（“要我帮你整理成文吗？”），而我仍在探索阶段。它无法区分“用户想要深入的哲学讨论”与“用户想要一个 RQ 简报”。两者看起来都是参与度，但需要完全相反的 AI 行为。

### 我们做了什么改变 (v3.0)

**魔鬼代言人——让步阈值协议（Concession Threshold Protocol）** (`deep-research` + `academic-paper-reviewer`)
- DA 现在必须在回应前对每次反驳进行 1-5 分评分
- 仅当分数 ≥4（反驳直接以证据应对核心攻击）时才允许让步
- 分数 ≤3：坚守立场并重述原始攻击
- 反迎合规则：禁止连续让步、记录让步率、每个检查点后检测框架锁定

**苏格拉底导师——意图检测层（Intent Detection Layer）** (`deep-research`)
- 在对话开始及每 3 轮时，将用户意图分类为探索性 vs. 目标导向型
- 探索模式：禁用自动收敛，最高回合数提升至 60，禁止“要我总结吗？”类提示
- 目标导向模式：标准收敛行为
- 防过早关闭规则：在探索模式下，由用户决定何时停止

**苏格拉底导师——对话健康指标（Dialogue Health Indicator）** (`deep-research`)
- 每 5 轮进行无声自我评估，维度包括：持续同意、回避冲突、过早收敛
- 检测到同意模式时自动注入挑战性提问
- 对用户不可见（防止被利用），但日志可供会话后审查

### 为什么这很重要

这些优化并未解决 AI 的结构性局限——它们使这些局限变得可见且可管理。如果施压足够大，DA 最终仍会让步。苏格拉底导师仍会有部分收敛偏差。但现在有了明确的检查点来减缓迎合倾向、迫使 DA 为让步提供理由，并防止导师在用户准备好之前提前结束对话。

更深层的启示：AI 素养并非关于学习将 AI 作为工具使用、遵循伦理规则或恐惧 AI 风险。而是通过深度参与 AI 来亲自发现其结构性局限——以及在此过程中发现自己思维的局限。

---

## 许可证

本作品采用 [CC-BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) 许可。

**你可以：**
- 分享 —— 复制和重新分发该材料
- 改编 —— 混用、转换并基于该材料构建新内容

**需遵守以下条款：**
- **署名（Attribution）** —— 你必须给出适当的信用
- **非商业性（NonCommercial）** —— 你不得将该材料用于商业目的

**署名格式：**
```
Based on Academic Research Skills by Cheng-I Wu
https://github.com/Imbad0202/academic-research-skills
```

---

## 贡献者

**Cheng-I Wu** (吳政宜) — 作者与维护者

**[aspi6246](https://github.com/aspi6246)** — 贡献者。v3.1 优化受 [Claude-Code-Skills-for-Academics](https://github.com/aspi6246/Claude-Code-Skills-for-Academics) 中的模式启发：只读约束模式、反模式作为一等设计进行编码、认知框架方法（教授“如何思考”而不仅是流程）、精简技能体积理念。

**[mchesbro1](https://github.com/mchesbro1)** — 贡献者。最初提出并起草了 `academic-paper-reviewer/references/top_journals_by_field.md` 中 IS Basket of 8 期刊列表 ([Issue #5](https://github.com/Imbad0202/academic-research-skills/issues/5))。

**[cloudenochcsis](https://github.com/cloudenochcsis)** — 贡献者。将 IS 部分从 *Basket of 8* 扩展至完整的 *Senior Scholars' Basket of 11*——新增 *Decision Support Systems*, *Information & Management*, 和 *Information and Organization* ([Issue #7](https://github.com/Imbad0202/academic-research-skills/issues/7), [PR #8](https://github.com/Imbad0202/academic-research-skills/pull/8))。来源：[AIS Senior Scholars' List of Premier Journals](https://aisnet.org/research/seniorscholarsbasket/)。

**[eltociear](https://github.com/eltociear)** (Ikko Eltociear Ashimine) — 贡献者。翻译了日文 README ([`README.ja-JP.md`](README.ja-JP.md)) ([PR #161](https://github.com/Imbad0202/academic-research-skills/pull/161))。

**[xpfo-go](https://github.com/xpfo-go)** (xpfo) — 贡献者。翻译了简体中文 README ([`README.zh-CN.md`](README.zh-CN.md)) ([PR #181](https://github.com/Imbad0202/academic-research-skills/pull/181))。

---

## 更新日志（Changelog）

### v3.11.0 (2026-06-04) — 确定性引用验证门禁 (#182)

> 新增 **确定性引用存在性验证门禁**，独立于 LLM 同行评审运行。每条被引参考文献会与最多四个书目索引交叉核对——Semantic Scholar + OpenAlex + Crossref + 新增的 **arXiv resolver** (`scripts/arxiv_client.py`，无需 API key) ——并为每条引用写入 `lookup_verified` 状态（`{true, false, unresolvable}`）至统一摘要中。因此，伪造引用若带有可证伪的 DOI/arXiv ID，将通过查找而非依赖评审员智能体注意到而被捕获。该门禁 **继承 v3.10 的 `terminal_policies` 可选模型**：检测始终运行，但仅当用户选择进入 `terminal_policies.citation_existence == strict` 时，`lookup_verified == false` 的行才会成为终端阻断；默认行为为咨询性且可通过 `/ars-mark-read` 确认。`false` 已收窄至 **ID-keyed unmatched**（精确 DOI/arXiv 查找确证失败），因此 legitimately-unindexed 的人文学科/非英语/区域性引用仍保持 `unresolvable` 且永不阻塞（此为文档化的精度优先于召回率的权衡）。附带持久化 SQLite 验证缓存（`~/.cache/ars/verification.db`, 90天 TTL）及 `/ars-cache-invalidate` 命令、独立 `verification_gate` API + `verify_passport.py` CLI，以及 v3.9.0 污染三角测量矩阵的四索引扩展（k=0..4, 均为咨询性）。`academic-pipeline` 套件版本追踪至 v3.11.0；其余三项技能版本不变。规范：`docs/design/2026-05-21-v3.10-182-promote-citation-gate-spec.md` (§0 amendment + C-V6)。

### v3.10.0 (2026-06-01) — 三角测量策略层、Kong 调查采纳、评估工具包、作用域写入守卫

> 次要版本打包：可选污染三角测量 **终端策略层** (#127 —— 引用默认行为与 v3.9.0 字节等效)；**Kong et al. 2026 调查采纳**——反驳承诺账本（#256/#266/#268/#269）及学科相对领域证据画像（#259）；**v3.10 测量基础设施**——通用评估金标准集 + ranking-lift CI 门禁 (#184)；**作用域写入守卫 MVP** (#134) ——确定性 `PreToolUse` hook，将 23 个单阶段智能体限制在其各自阶段目录内并拒绝 Bash（它们改用 Grep/Glob 和结构化编辑工具）；`/ars-mark-read` 插件命令 (#190) 及破损修复 (#195)；简体中文 README (#185)；CI 加固 (#156/#155)。`academic-paper` → v3.2.0，`academic-paper-reviewer` → v1.10.0（含承诺账本与领域画像新增）；`academic-pipeline` 套件版本追踪至 v3.10.0。默认技能行为不变，除非选择严格策略模式；唯一默认开启的变更是 #134 守卫，它约束被围栏的子智能体，而非用户可见输出。

### v3.9.4.2 (2026-05-19) — PR #149 CI 纪律门禁发布后热修复（codex post-ship）

> Codex 对 PR #149（7 个 CI 纪律门禁）的发布后审查暴露了 4 项 P2 问题；v3.9.4.2 加固了其中 3 项。F1: `harness-retirement-monthly.yml` 新增 `GH_REPO`，使定时运行具备创建 issue 所需的仓库上下文。F2: `release-cooldown.yml` 过滤 `PREV_TAG` 查找至仅 `v*` 标签，防止非发布标签绕过冷却期。F3: `release-cooldown.yml` 同时读取标注标签主题并接受 `hot-fix` 拼写（v3.9.2 此前为假阴性热修复）。PR #157 跟进：`[skip-cooldown]` 覆盖现在从提交消息和标注标签消息中读取（自举修复——此标签的冷却期绕过演示了 F2+F3 端到端工作）。F4（测试计数单调性加固）已回滚，因其暴露了 `scripts/` 包中的现有问题，跟踪为 #154（已由 PR #158 修复）+ 重新尝试 #155。关闭 #152。跟进：#155, #156。

### v3.9.4.1 (2026-05-19) — v3.9.4 时间验证发布后热修复 (#135 codex post-ship)

> Codex 对 v3.9.4 的发布后审查发现了 4 个真实 bug，被任务子智能体评审员遗漏。热修复补丁全部 4 项：(1) `audit()` 现在将 `citation_provenance` 传递至 P2 和 P4——当 ref slug 具有 `confidence: low` 或 `conflict` 时，验证器发出 `TEMPORAL-METADATA-MISSING` 而非使用时间线日期作为事实（规范 §3.4 第一方安全检查已损坏）。(2) `_date_to_interval` 解析所有模式有效的日期格式，包括 `YYYY-MM`（Crossref 月精度）和 `YYYY-MM-DD..YYYY-MM-DD`（区间）；v3.9.4 对此静默抛出 `ValueError` 并跳过检查。(3) P4 现在在无 ref 标记时绑定直接日期捕获——如 "The 2026 policy enabled the 2020 rollout" 的句子现在实际触发。(4) `citation_provenance.schema.json` 中 `confidence:high` allOf 现在要求存在性（`then.required`）而不仅是非空，关闭了缺失属性绕过。1561 通过（+12 新测试 vs v3.9.4 基线, 0 回退）。ARCHITECTURE.md 对齐至当前状态（此前在 v3.8.0 过时）。

### v3.9.4 (2026-05-18) — #135 时间验证层（咨询性）

> Phase 4 → 5 边界处的确定性咨询验证器，覆盖 5 种时间失败模式（P1 回溯算术、P2 时代错置引用、P3 比较对象未实例化、P4 因果倒置、P5 指示代词现在时）。新增 Phase 2 兄弟节点 `timeline_extraction_agent` 负责 `phase2_investigation/timeline.yaml` + `phase2_investigation/citation_provenance.yaml`。验证器脚本 `scripts/temporal_integrity_audit.py` 确定性运行 5 次传递。M3 时间完整性铁律已添加至 `report_compiler_agent` + `draft_writer_agent`。M7-minimal：日期溯源 + 比较对象实例化。M5-stub：仅用户声明的 `version_family_id`。对 `literature_corpus_entry`, `claim_audit_result`, `claim_intent_manifest` 零修改。`bibliography_agent` 未修改（F2 不变式）。3 个新旁路模式。覆盖率估算：基线 55-70% / M7 minimal 下 65-75%。1549 通过（+44 新, 0 回退）。

### v3.9.3 (2026-05-18) — #128 维护工作（共享客户端工具 + 去重解析器）

> 纯重构 + 一项来自 v3.9.0 `/simplify` 审查积压的潜在 bug 修复。提取 `scripts/_text_similarity.py`（三方客户端去重：normalize / similarity / threshold / retry constants）+ `scripts/_passport_yaml.py`（双向迁移工具去重：ruamel.yaml round-trip config）+ 私有 `_resolve_by_doi_then_title` 辅助函数（双向解析器主体去重，§3.4 / §3.5 API 表面保留）。在 OpenAlex + Crossref 上将节流测量标准化为 `time.monotonic`（此前为 `time.time`, NTP 不安全），与 Semantic Scholar 对齐。所有 5 个模块级跨导入采用双路径导入基础设施（兄弟优先，namespace-package 回退）以保留 `SemanticScholarUnavailable` 类身份并 bonus-fix 2 个潜在损坏的 `import scripts.X` 路径。1505 通过（+23 新, 0 回退）。#128 §4（并行化 OA + CR per-entry）已转移至 #138。

### v3.9.2 (2026-05-18) — #133 阶段边界热修复

> #133 关闭（热修复层）。长期架构修复跟踪为 #134 中 v3.10 活跃指挥器。新增：CLAUDE.md 中的路由澄清门禁（跨阶段材料 → 用 a-d 选项澄清，而非静默分发），22 个单阶段智能体获得提示词硬围栏（`## Phase Boundary (v3.9.2)`），16 个多阶段/阶段正交/跨阶段元智能体故意未围栏（诚实表述——散文安慰剂制造虚假执行错觉），咨询验证器 `scripts/check_pipeline_integrity.py` 事后检测 #133 模式。使用跨模型抽查的行为冒烟测试（100% Opus 4.7, ≥75% Sonnet + GPT-5.5）。

### v3.9.1 (2026-05-18) — #129 + #130 客户端加固

> v3.9.0 热修复。将 OpenAlex / Crossref 响应读取失败包装为 `*Unavailable` (#129)；保护 `check_claim_audit_consistency` 免受非字符串 `manifest_id` 影响 (#130)。无规范变更。

### v3.9.0 (2026-05-17) — #102 跨索引三角测量测量

> #102 关闭。v3.7.3 交付单索引（Semantic Scholar）污染检测；v3.9.0 扩展至三索引三角测量（S2 + OpenAlex + Crossref）作为 **仅咨询证据**。`contamination_signals` 上新增两个可选布尔值（`openalex_unmatched`, `crossref_unmatched`）；手动输入非规则对称扩展。终结器新增 4 级咨询矩阵（k=0/1/2/3 over present `*_unmatched` fields），v3.7.3 遗留 `CONTAMINATED-UNMATCHED` 保留用于 k=1/k_max=1 S2-only 情况。格式化器传递允许列表扩展至 9 个后缀；拒绝规则 1-10 按 R-L3-2-E 保持不变。策略层（严格模式、硬阻断层级、`venue_type` / `triangulation_policy`）推迟至 v3.10，依规范 §2.3。k=3 标记为 `CONTAMINATED-TRIANGULATION-UNMATCHED`（描述可观察现象，非推断原因）。3 条新硬规则：R-L3-2-C（k 基于现有字段计算）、R-L3-2-D（无 API 推断分类）、R-L3-2-E（拒绝列表不变；传递允许列表扩展）。

**迁移：** v3.7.3 语料库——运行 `python scripts/migrate_literature_corpus_to_v3_9_0.py PATH` 回填两个新字段。v3.7.3 之前语料库——先运行 `migrate_literature_corpus_to_v3_7_3.py`，然后 v3.9.0 迁移（按规范 §3.7 链式调用；v3.9.0 工具仅作用于已携带 `contamination_signals.semantic_scholar_unmatched` 的条目）。

### v3.8.2 (2026-05-17) — #118 未引用审计工具故障表面

> #118 关闭。`ARS_CLAIM_AUDIT=1` 未引用约束判断路径此前在 `JudgeInvocationError` 上静默替换为 `{"judgment": "NOT_VIOLATED"}`，抑制了临时评审器宕机时的 HIGH-WARN 约束检查。v3.8.2 将这些故障路由至专用 `uncited_audit_failures[]` 聚合（MED-WARN 咨询层级），镜像引用路径 INV-14 行但使用专用模式，因为 `claim_audit_result.ref_slug` 为必填且未引用路径无 ref 可绑定。#118 issue body 中的四个 option-1..4 权衡最终选择 option 2（新聚合）——option 4（重新抛出并中止）因对审计覆盖率的打击而被拒绝。

- **新增 `uncited_audit_failure.schema.json` 聚合** (规范 §3.6)。每条未引用句子 × manifest 对生成一条记录，其中约束评审器引发 `JudgeInvocationError`。与引用路径 INV-14 相同的故障类枚举（`judge_timeout` / `judge_api_error` / `judge_parse_error` / `cache_corruption` / `retrieval_api_error` / `retrieval_timeout` / `retrieval_network_error`）。`rule_version: D4-c-v1-uaf-v1`。
- **UAF-INV-1..UAF-INV-6 lint** (规范 §6 规则 4d)。`finding_id` 唯一性、scoped_manifest_id 跨数组完整性、manifest_claim_id 非空时的 (M, C) 对完整性、per-(sentence, manifest) 去重、rationale fault_class 前缀、与 `constraint_violations[]` 的跨聚合互斥。
- **终结器 §5 MED-WARN 咨询行**：标注 `[CLAIM-AUDIT-TOOL-FAILURE-UNCITED — <fault-class>]`，门禁通过（retry-next-pass 修复）。格式化器 REFUSE 列表不变——UAF 为咨询性。
- **管线集成** (`scripts/claim_audit_pipeline.py`)：吞没位点 line 1211-1224 已移除；`JudgeInvocationError` 现在发出 UAF 行 + `continue`s 至下一 (sentence, manifest) 对。无虚假 NOT_VIOLATED 进入 `constraint_violations[]`。
- **测试**：新增 18 项（15 模式/lint TSUAFUncitedAuditFailureInvariants + 3 管线集成 TP23UncitedJudgeOutageEmitsUAF）。基线 694 → 712 测试，0 回退。
- **智能体文档** (`academic-pipeline/agents/claim_ref_alignment_audit_agent.md`)：输出发射表新增第七行；错误处理表从 3 个表面增至 4 个表面（含未引用路径 UAF 行）。

### v3.8.0 (2026-05-16) — L3 主张忠实度定位器 + 审计（配对里程碑）

> v3.7.3 + v3.8 端到端关闭 L3（主张忠实度）差距。v3.7.3 交付定位器基础设施——每条引用携带三层锚点，以便未来审计获取所引段落。v3.8 交付消耗这些锚点的审计流程，判断所引来源是否支持主张，并在格式化器终端硬门禁处 gate-refuse HIGH-WARN 违规。该版本还捆绑了自 v3.7.0 以来积累的 5 个审计轨迹功能 PR（#104 / #105 / #108 / #111 / #115）。

- **#103 — `claim_ref_alignment_audit_agent`** (v3.8 PR #121)。可选 (`ARS_CLAIM_AUDIT=1`, 默认 OFF) 第 4→5 阶段审计智能体。对每条采样引用与检索片段进行判断；发出 `claim_audit_results[]` + `claim_intent_manifests[]` + `claim_drifts[]` + `uncited_assertions[]` + `constraint_violations[]` 聚合。8 行终结器矩阵将 HIGH-WARN 类别（CLAIM-NOT-SUPPORTED / NEGATIVE-CONSTRAINT-VIOLATION / FABRICATED-REFERENCE / ANCHORLESS / CONSTRAINT-VIOLATION-UNCITED）通过格式化器 REFUSE 规则 6-10 路由。校准运行器随附 20 元组金标准集（T-C1 FNR<0.15 + FPR<0.10, T-C2 per-class, T-C3 shape integrity）。8 轮双轨审查（R1 codex + Gemini-3.1-pro-preview, R2-R8 codex-only after Gemini quota exhausted）；轨迹 R1 4P1+2P2 → R8 0P1+4P2 交付门禁。
- **v3.7.3 — 三层引用发射 + 污染信号** (PR #98)。`synthesis_agent` / `draft_writer_agent` / `report_compiler_agent` 新增 `## Three-Layer Citation Emission (v3.7.3)` H2。每个 `<!--ref:slug-->` 携带 `<!--anchor:<kind>:<value>-->`，其中 `<kind> ∈ {quote, page, section, paragraph, none}`（引用锚点限制在 25 词内，URL 编码）。`pipeline_orchestrator_agent` 终结器变为含优先级零 NO-LOCATOR 检查的 5 单元格。`formatter_agent` 新增对 `[UNVERIFIED CITATION — NO QUOTE OR PAGE LOCATOR]` 的显式硬门禁拒绝。`literature_corpus_entry.schema.json` 新增可选 `contamination_signals: { preprint_post_llm_inflection, semantic_scholar_unmatched }` 对象。`bibliography_agent` 在摄入时计算两个信号。11 轮审查轨迹（Codex×10 + Gemini cross-model×1）关闭 22 项发现。规范：`docs/design/2026-05-12-ars-v3.7.3-claim-faithfulness-and-contaminated-source-spec.md`。外部动机：Zhao et al. arXiv:2605.07723 (2026-05)。
- **#108 — AI 披露策略锚渲染器**（审计轨迹交付 2026-05-14）。在现有场地轨道渲染器旁新增 PRISMA-trAIce / ICMJE / Nature / IEEE 政策锚披露路径。
- **#111 — 系统综述 → 学术论文交接时的 `slr_lineage` 发射** (2026-05-15)。Schema 9 可选布尔 `slr_lineage` 字段；生产者 `pipeline_orchestrator_agent` 在每次交接转换时写入；消费者 `disclosure` 模式按 §4.3 G2 不变式轨道门禁分发 `--policy-anchor=prisma-trAIce`。
- **#104 — README 动机：Zhao et al. 语料库规模证据锚** (2026-05-15)。README + `README.zh-TW.md` 动机部分将 v3.7.x 系列置于 Zhao et al. 发现的 146,932 条幻觉引用背景下。
- **#105 — v3.7.3 contamination_signals 回填迁移工具** (2026-05-15)。`scripts/migrate_literature_corpus_to_v3_7_3.py` 对 v3.7.3 之前护照回溯计算两个污染信号。
- **#115 — Semantic Scholar 客户端成熟度** (2026-05-15)。`scripts/semantic_scholar_client.py` 新增 1-req/s 节流（检测到 `S2_API_KEY` 时降至 0.1s）、URLError 宕机闩锁及 `reset_outage_latch()` 用于长运行跨护照批次。

### v3.7.0 (2026-05-05) — Claude Code 插件打包

> 插件打包升级：ARS 现可通过 `/plugin marketplace add Imbad0202/academic-research-skills` + `/plugin install academic-research-skills` 在 Claude Code CLI / VS Code / JetBrains 上一行安装。传统 `git clone + symlink to ~/.claude/skills/` 流程继续有效——双轨道均为一等支持。

- **插件清单 + 市场元数据** (Phase 1, PR #68)。`.claude-plugin/plugin.json` 声明套件（4 项技能通过相对符号链接从 `skills/` 目录自动发现）。`.claude-plugin/marketplace.json` 注册插件，使单一 GitHub 托管端点同时服务于市场列表和插件源码。README + `README.zh-TW.md` + `docs/SETUP.md` 携带双轨道安装说明。
- **10 个斜杠命令** 位于 `commands/ars-*.md` (Phase 2.1, PR #69) 将 `MODE_REGISTRY.md` 条目映射至 `/ars-<mode>` 触发器。模型路由在每个命令的 frontmatter 中固定——`full` 和 `revision-coach` 使用 `opus`（架构/评审解释深度），其余 8 个使用 `sonnet`。无 Haiku 项目策略。
- **3 个插件附带智能体** 位于 `agents/*_agent.md` (Phase 2.1, PR #69) 作为相对符号链接指向 v3.6.7 加固的下游智能体：`synthesis_agent`, `research_architect_agent`, `report_compiler_agent`。保留下划线文件名以保持 `scripts/check_v3_6_7_pattern_protection.py` 硬固定路径和 INV-3 manifest-confined Clause 1 不变式完整。符号链接（非副本）保持单一事实来源，并防止 v3.6.7 §6 反转扫描 + INV-1/2/3 lint 关闭的 Pattern C3 攻击面。
- **`model: inherit`** 已添加至这三个源智能体 frontmatter。选择继承而非固定 `sonnet`，以便运行 ARS 全管线的 opus 会话保持使用 opus 智能体（而非被限制）。用户的 `~/.claude/hooks/warn-agent-no-model.sh` PreToolUse hook 在分发边界拦截 Haiku，因此 `inherit` 通过已无 Haiku 的模型解析。
- **SessionStart announce hook** 位于 `hooks/hooks.json` + `scripts/announce-ars-loaded.sh` (Phase 2.2, PR #70)。插件加载时，hook 注入列出 10 个斜杠命令、3 个插件智能体及 Token 预算指针的 `additionalContext` 至 LLM 的首轮。`startup` 和 `clear` 源值获得完整公告；`resume` 和 `compact` 仅获一行确认以避免消耗上下文。兼容 Bash 3.2——在 macOS 原生 `/bin/bash` 上运行，无需 `brew install bash`。
- **Phase 2.2 范围缩减**：因合同缺口（SubagentStop payload 无阶段/交付物信息）和调用者类边界（`run_codex_audit.sh` lines 4–7 禁止同会话内 LLM 调用；PostToolUse 在生成会话内触发），`SubagentStop → run_codex_audit.sh` codex 审计 hook 被排除在 v3.7.0 外。真实审计 hook 集成推迟至 ARS 获得阶段/交付物传播合同的未来版本。见 `docs/design/2026-04-30-ars-v3.7.0-plugin-packaging-roadmap.md` Update note 2026-05-05 (Phase 2.2 scope reduction)。
- **`docs/PERFORMANCE.md` + `.zh-TW.md`** 新增 "v3.7.0 Plugin agents and model routing" 小节解释继承语义和当前 3 智能体范围边界。
- **Codex 审查链跨三个 PR**：8 轮内联迭代 + 3 次新鲜 PR 级评审，合并前全部收敛至 0 P0/P1/P2 发现。Phase 2.2 新鲜 PR 审查捕获一项 P2（未引用的 `${CLAUDE_PLUGIN_ROOT}` 破坏含空格安装路径）——确认分离实现审查（内联）与合同审查（新鲜）的价值。
- **未变更内容**：四个技能目录、全部 25 种模式、智能体提示词、模式文件及 lint 合同不变。插件打包仅新增顶层表面（`commands/`, `agents/`, `hooks/`, `.claude-plugin/`, `skills/` symlink dir, 三个插件智能体 `model: inherit` frontmatter 新增）。现有 4.3k clone-install 用户无破坏性变更。

### v3.6.8 (2026-05-03) — 生成器-评估者合同门禁（v3.6.6 规范交付）

> 命名说明：本版本交付 **v3.6.6 生成器-评估者合同** 规范与实现。因项目排序，v3.6.6 工作在 v3.6.7 之后落地；设计文档保留 v3.6.6 内部命名用于合同门禁版本，而套件发布标记为 v3.6.8 以保持 CHANGELOG 单调递增。

- **Schema 13.1** (`shared/sprint_contract.schema.json`) 扩展 Schema 13，新增两个 `mode` 枚举值（`writer_full` + `evaluator_full`）、两个新顶级可选字段（`pre_commitment_artifacts` writer-only, `disagreement_handling` evaluator-only）及 12 个 `allOf` 分支强制执行评审员/写作者/评估者条件门禁。现有评审合同在 Schema 13.1 下验证为字节等效 (§3.6 zero-touch promise)。
- **两个新交付的合同模板** 位于 `shared/contracts/writer/full.json` (D1–D7, F1/F4/F2/F3/F0) 和 `shared/contracts/evaluator/full.json` (D1–D5, F1/F2/F3/F6/F4/F5/F0)。从规范分支上的设计时工件提升为与 Schema 13.1 升级原子同步的现场交付状态。
- **两阶段编排** 位于 `academic-paper full` 内：Phase 4 拆分为 Phase 4a（写作者论文盲态预承诺）+ Phase 4b（写作者论文可见起草 + 自评分）；Phase 6 拆分为 Phase 6a（评估者论文盲态预承诺）+ Phase 6b（评估者论文可见评分 + 决策）。阶段编号 `<phase4a_output>` / `<phase6a_output>` 数据分隔符镜像 v3.6.2 评审员模式。Lint 计数摘要：写作者 3+4 / 评估者 5+5 / 评审员 5+6（评审员保持 zero-touch）。
- **`academic-paper` SKILL + 智能体文件** 新增逐字 `## v3.6.6 Generator-Evaluator Contract Protocol` 块（SKILL.md 中 101 行，`draft_writer_agent.md` 中 47 行，`peer_reviewer_agent.md` 中 57 行）。SKILL.md 还新增 `## Known limitations` 部分，携带 v3.6.7+ 的优雅降级 + 跨会话恢复向前说明。
- **验证器扩展**：`scripts/check_sprint_contract.py` SC-* 模式门控审计（SC-5 + SC-11 评审员专属；SC-9 扩展至全部三种模式族）。17 项新测试将验证器单元测试计数从 54 提升至 71（正向 + 5 模式分支负向 + 2 §3.6 评审员回退 + 6 模式门控测试）。
- **Manifest CI lint**：`scripts/check_v3_6_6_ab_manifest.py` 强制执行 §6.2 manifest 模式 + §6.5 git-tracked 不变式于 `tests/fixtures/v3.6.6-ab/manifest.yaml`。`.github/workflows/spec-consistency.yml` 扩展冲刺合同验证循环以迭代写作者 + 评估者模板目录 alongside 现有评审员循环，并运行新 manifest CI lint。
- **A/B 证据夹具存根** 位于 `tests/fixtures/v3.6.6-ab/`（30 文件）：manifest + README + 6 篇论文-A 输入/基线 + 1 篇论文-C 输入/基线 + Stage 3 评审员摘录 + 6 个 codex-judge 基线占位符。真实夹具数据将在后续提交中填充，直至实现工作完全完成。

### v3.6.7 (2026-04-30) — 下游智能体模式保护（Step 1+2）

- **三个下游智能体加固以抵御 18 个已记录幻觉/漂移模式中的 13 个**：`synthesis_agent`（A1–A5 叙事侧）、`research_architect_agent` 的 survey-designer 模式（B1–B5 仪器侧）及 `report_compiler_agent` 的 abstract-only 模式（C1–C3 出版侧）。每个智能体提示词现携带 `PATTERN PROTECTION (v3.6.7)` 块。
- **四个参考文件** 位于 `shared/references/`：`irb_terminology_glossary.md`, `psychometric_terminology_glossary.md`, `protected_hedging_phrases.md`, `word_count_conventions.md`。这些参考文件携带智能体提示词按路径引用的操作合同。
- **跨模型审计提示模板** 位于 `shared/templates/codex_audit_multifile_template.md`，含七个审计维度和对 `report_compiler_agent` 捆绑包的强制三部分 Section 4(f) 检查。任何子检查失败均为 P1 发现。
- **静态 lint + 29 测试突变套件**：`scripts/check_v3_6_7_pattern_protection.py` 强制执行保护条款存在性和义务短语形状；`scripts/test_check_v3_6_7_pattern_protection.py` 保留 codex 审查证据以便未来检查器回退在 CI 中暴露。两者均已接入 `.github/workflows/spec-consistency.yml`。
- **Codex 审查历史**：七轮 `gpt-5.5` + `xhigh` 跨模型审查达到 SHIP-OK，零 P1+P2 发现。Step 6（编排器运行时 hooks）和 Step 8（合成评估用例）将在后续 PR 中交付。

### v3.6.5 (2026-04-27) — 材料护照 `literature_corpus[]` 消费者集成

- **两个 Phase 1 文献消费者** 已接线：`deep-research/agents/bibliography_agent.md` 和 `academic-paper/agents/literature_strategist_agent.md`。两者均遵循相同的五步 **corpus-first, search-fills-gap** 流程，当护照携带非空 `literature_corpus[]` 时适用，并遵守相同四项铁律（同标准 / 无静默跳过 / 无 corpus 突变 / 解析失败优雅降级）。
- **搜索策略报告中的 PRE-SCREENED 可复现性块**：枚举包含/排除/跳过的 corpus 条目，含 F3 零命中说明及围绕 `obtained_via` / `obtained_at` 部分声明的 F4a–F4f 溯源报告。`final_included = pre_screened_included[] ∪ external_included[]` 保持中立——书目条目或文献矩阵行无溯源标签。
- **消费者协议参考** 位于 `academic-pipeline/references/literature_corpus_consumers.md`，含标准 PRE-SCREENED 模板、BAD/GOOD 示例、四项铁律及 per-consumer 阅读说明。
- **CI lint** `scripts/check_corpus_consumer_protocol.py` 强制执行九项协议不变式，带 manifest 驱动消费者列表（`scripts/corpus_consumer_manifest.json`）。
- **Schema 9 警告退役**：`shared/handoff_schemas.md` 退役 v3.6.4 “Consumer-side integration deferred to v3.6.5+” 警告；替换为消费者协议反向指针。
- 基于存在性，无模式变更，无新环境变量标志。解析失败回退至仅外部数据库流程并带 `[CORPUS PARSE FAILURE]` 表面。`citation_compliance_agent` corpus 集成推迟（目标版本 TBD post-v3.8）。
- 无破坏性变更。现有用户适配器无需修改即可工作。

### v3.6.4 (2026-04-25) — 材料护照 `literature_corpus[]` 输入端口

- **`literature_corpus[]` 字段** 作为用户自有文献的可选输入端口添加至 Schema 9。每个条目符合 `shared/contracts/passport/literature_corpus_entry.schema.json`（CSL-JSON authors, year, title, source_pointer + 私有可选 `abstract` / `user_notes`）。
- **语言无关适配器合同** 位于 `academic-pipeline/references/adapters/overview.md`：任何程序（任意语言）读取用户 corpus 源均可生成符合的 `passport.yaml` + `rejection_log.yaml`。条目级错误软失败，适配层级错误硬失败，确定性排序。
- **三个参考 Python 适配器** 位于 `scripts/adapters/`：`folder_scan.py`（PDF 文件系统）、`zotero.py`（Better BibTeX JSON 导出）、`obsidian.py`（vault frontmatter）。仅为起点；预期用户为非参考源编写自己的适配器。
- **拒绝日志合同** 位于 `shared/contracts/passport/rejection_log.schema.json`，含分类原因值的闭合枚举；始终发射（无拒绝时为空）。
- **CI 门禁**：`scripts/check_literature_corpus_schema.py` 验证模式 + 适配器示例；`scripts/sync_adapter_docs.py --check` 防止 schema→docs 漂移；新 `pytest.yml` 工作流在路径过滤触发器上运行 `scripts/adapters/tests/`。
- **v3.6.4 仅为输入端口**：v3.6.4 交付模式与适配器合同，无消费者集成。`bibliography_agent` 和 `literature_strategist_agent` 于 v3.6.5 接线。
- 无破坏性变更。

### v3.6.3 (2026-04-23) — 可选护照重置边界

- **可选护照重置边界** (`ARS_PASSPORT_RESET=1`)。将每次 FULL 检查点提升为上下文重置边界。新增 `resume_from_passport=<hash>` 模式允许用户仅凭材料护照账本在新鲜 Claude Code 会话中恢复。`systematic-review` 模式配合该标志 ON 使重置在每个 FULL 检查点强制；其他模式视重置为标志门控默认值。标志 OFF 逐字节保留 v3.6.3 之前行为。
- Schema 9 新增仅追加 `reset_boundary[]` 账本，含两种条目类型（`kind: boundary` + `kind: resume`）。哈希使用 JSON Canonical Form + SHA-256，自引用安全占位符可选。`pending_decision` 处理 MANDATORY 分支选择。
- 新 CI lint `scripts/check_passport_reset_contract.py`：该标志的每次提及必须共定位指向权威协议文档的指针。
- 协议文档：`academic-pipeline/references/passport_as_reset_boundary.md`。
- `docs/PERFORMANCE.md` 更新长运行会话指导。
- 无破坏性变更。标志默认 OFF。

### v3.6.2 (2026-04-23) — 评审员冲刺合同硬门禁

v3.6.2 引入 Schema 13 冲刺合同及强制编排，迫使评审员在阅读论文前预承诺其评分计划。仅评审员首次测试用例；写作者/评估者推迟至 v3.6.4。见 CHANGELOG。

- **Schema 13 冲刺合同** 含 `panel_size`, `acceptance_dimensions`, `failure_conditions`（带 `severity` 优先级 + panel-relative `cross_reviewer_quantifier`）, `measurement_procedure`, 可选 `override_ladder`, 有界 `agent_amendments`。验证器：`scripts/check_sprint_contract.py`。
- **双调用硬门禁**。评审员运行论文内容盲态 Phase 1 + 论文可见 Phase 2；Phase 1 输出包装在 `<phase1_output>...</phase1_output>` 数据分隔符中以缩小自注入表面。
- **合成器三步机械协议**。构建跨评审员矩阵 → 使用 panel-relative quantifier + 认可表达词汇评估每个 `failure_condition` → 按 `severity` 解决优先级。禁止操作列表在 `editorial_synthesizer_agent` 中明确列出。
- **两个评审员模板交付** (`shared/contracts/reviewer/full.json` panel 5; `shared/contracts/reviewer/methodology_focus.json` panel 2)。`reviewer_re_review`, `reviewer_calibration`, `reviewer_guided` 在模式枚举中保留但 v3.6.2 无合同模板交付；它们保留 v3.6.2 之前行为。`reviewer_quick` 完全排除在枚举外。
- `academic-paper-reviewer` SKILL 版本：`1.8.1 → 1.9.0`。`academic-pipeline` SKILL 版本：`3.5.1 → 3.6.2`（套件版本不变式）。套件版本升级至 `3.6.2`。
- 见规范 [`docs/design/2026-04-23-ars-v3.6.2-sprint-contract-design.md`](docs/design/2026-04-23-ars-v3.6.2-sprint-contract-design.md) 和协议 [`academic-paper-reviewer/references/sprint_contract_protocol.md`](academic-paper-reviewer/references/sprint_contract_protocol.md)。

### v3.5.1 (2026-04-22) — 可选苏格拉底阅读检查探针

v3.5.1 向苏格拉底导师新增可选诚实探针 (`ARS_SOCRATIC_READING_PROBE=1`)。默认关闭。见 CHANGELOG。

- **可选阅读检查探针**：当设置 `ARS_SOCRATIC_READING_PROBE=1` 时，苏格拉底导师在目标导向会话中（用户引用了特定论文）触发一次性诚实探针。拒绝将记录且无惩罚。结果流入研究计划摘要和第 6 阶段 AI 自我反思报告。无新智能体，无模式变更。
- `deep-research` SKILL 版本：`2.9.0 → 2.9.1`。`academic-pipeline` SKILL 版本：`3.5.0 → 3.5.1`。套件版本升级至 `3.5.1`。

### v3.5.0 (2026-04-21) — 协作深度观察者

- **新智能体**：`collaboration_depth_agent` 位于 `academic-pipeline`（Agent Team 从 3 增至 4）。在每次 FULL/SLIM 检查点及管线完成时调用；按四维量规对用户-AI 协作评分。**仅咨询——从不阻塞进度**。强制性检查点（第 2.5 / 4.5 阶段完整性门禁）不调用观察者。
- **新量规**：[`shared/collaboration_depth_rubric.md`](shared/collaboration_depth_rubric.md) v1.0。维度：委托强度、认知警觉性、认知重新分配、区域分类（Zone 1 / Zone 2 / Zone 3）。基于 Wang, S., & Zhang, H. (2026). "Pedagogical partnerships with generative AI in higher education: how dual cognitive pathways paradoxically enable transformative learning." *International Journal of Educational Technology in Higher Education*, 23:11. DOI [10.1186/s41239-026-00585-x](https://doi.org/10.1186/s41239-026-00585-x)。
- **跨模型分歧标记而非平均**：当设置 `ARS_CROSS_MODEL` 时，观察者运行于两个模型上；维度分歧 > 2 分则报告而非静默平滑。`ARS_CROSS_MODEL_SAMPLE_INTERVAL` 为成本权衡逃生舱口。
- **短阶段守卫**：用户轮次少于 5 的阶段注入静态 `insufficient_evidence` 块而非分发全模型观察者。
- **反迎合纪律**：≥7 分需特定对话轮引用；Zone 3 触发重新审计；无激励性表述。
- `academic-pipeline` SKILL 版本：`3.3.0 → 3.4.0`。套件版本升级至 `3.5.0`。新 lint `scripts/check_collaboration_depth_rubric.py` + 10 测试。

### v3.4.0 (2026-04-20) — 合规智能体 + Schema 12

- **合规智能体**（共享）：单模式感知智能体运行 PRISMA-trAIce 17 项（仅 SR 模式）+ RAISE 4 原则 + 8 角色矩阵。钩住现有第 2.5 / 4.5 完整性门禁；基于层级阻断（MANDATORY → 阻断, HR → 警告, R/O → 信息）。非 SR 条目仅运行原则，仅警告。
- **Schema 12 compliance_report** 通过 `compliance_history[]` 追加至材料护照（仅追加）。
- **3 轮用户覆盖阶梯** 自动注入 `disclosure_addendum` 至手稿。无法规避检测。
- **带透明报告的校准**，无硬 FNR/FPR 门禁——与 `task_type: open-ended` 自洽。
- **上游新鲜度 CI** 警告 PRISMA-trAIce 漂移（非阻断）。
- **长运行会话文档**：材料护照作为跨会话恢复机制。

### v3.3.6 (2026-04-15) — README 精简 + ARCHITECTURE 文档

- 新增 `docs/ARCHITECTURE.md` 作为管线结构（流程、矩阵、数据访问、依赖图、质量门禁、模式）的唯一事实来源。通过 PR #18 合并至主分支。
- 新增 `docs/SETUP.md`（前置条件、API 密钥、Pandoc/tectonic、跨模型验证、安装方法）和 `docs/PERFORMANCE.md`（Token 预算、推荐 Claude Code 设置）。README 链接至二者而非内联。
- 精简 README：移除 ASCII 管线图和 16 点关键功能列表（已被 ARCHITECTURE.md 取代）；技能详情部分现锚定版本号并引导读者前往 ARCHITECTURE.md §3 查看 per-agent 名单。
- 注：无任何技能的功能变更。纯文档重组。套件版本升级至 `3.3.6`。

### v3.3.5 (2026-04-15)
- 新增 `benchmark_report.schema.json` + 材料护照上的可选 `repro_lock` 块。两者均随模式文档、lint 和示例交付。首个正式 Python dev dep manifest (`requirements-dev.txt`)。

### v3.3.4 (2026-04-15) — README Changelog 同步补丁
- 同步 `README.md` 和 `README.zh-TW.md` 中嵌入的 changelog 部分，以包含缺失的 `v3.3.3` 和 `v3.3.2` 发布摘要。
- 扩展 `scripts/check_spec_consistency.py` 使未来 README changelog 漂移导致 CI 失败。

### v3.3.3 (2026-04-15) — 发布准备 + Lint 加固
- 加固 SKILL frontmatter lint：缺失闭合 `---` fence 现在干净地失败而非被解析为有效 YAML。
- 解析为有效 YAML 但非映射的 frontmatter 现报告可读错误而非崩溃。
- 修复两个 README 中 post-publication audit report 的损坏展示链接。
- 将 README relative-link 验证添加至规范一致性检查，使死链导致 CI 失败。
- 对齐文档中的 DOCX 输出合同：直接 `.docx` 生成依赖 Pandoc，以 Markdown + 转换说明为回退。
- 准备 `v3.3.3` 发布：套件版本升级, `academic-paper` -> v3.0.2, `academic-pipeline` -> v3.2.2。

### v3.3.2 (2026-04-15) — 数据访问级别 + 任务类型元数据
- 在所有顶级 `SKILL.md` 文件中新增 `metadata.data_access_level`，强制执行词汇：`raw`, `redacted`, `verified_only`。
- 在所有顶级 `SKILL.md` 文件中新增 `metadata.task_type`，强制执行词汇：`open-ended`, `outcome-gradable`。
- 新增两种元数据字段的 lint 脚本和单元测试，接入 GitHub Actions 规范一致性工作流。
- 新增 `shared/ground_truth_isolation_pattern.md` 并从 `shared/handoff_schemas.md` 链接新词汇。

### v3.3.1 (2026-04-14) — 规范一致性补丁
- 同步 README、`.claude/CLAUDE.md`、`MODE_REGISTRY.md` 和 `SKILL.md` 文件至当前模式计数和已发布技能版本。
- 修正跨模型表述：完整性样本检查和独立 DA 批评现已实现；第六评审员同行评审仍为计划中。
- 澄清自适应检查点语义，使 SLIM 检查点仍等待显式用户确认。
- 重申第 2.5 阶段和第 4.5 阶段完整性门禁不可跳过。
- 新增轻量规范一致性检查和 GitHub Actions 工作流以捕获未来漂移。

### v3.3 (2026-04-09) — PaperOrchestra 启发增强
集成 [PaperOrchestra](https://arxiv.org/abs/2604.05018) (Song, Song, Pfister & Yoon, 2026, Google) 中的技术。

- **Semantic Scholar API 验证** —— Tier 0 程序化引用存在性检查通过 S2 API。Levenshtein >= 0.70 标题匹配、DOI 不匹配检测、通过 S2 ID 去重书目。API 不可用时优雅降级。
- **防泄漏协议** —— 知识隔离指令优先于 LLM 参数内存处理会话材料。对缺失内容标记 `[MATERIAL GAP]` 而非从内存填充。降低模式 5/6 失败风险。
- **VLM 图表验证**（可选）—— 使用视觉能力 LLM 闭环验证渲染图表。10 点清单，最多 2 次精炼迭代。
- **分数轨迹协议** —— 跨修订轮次按维度量规跟踪分数 delta（7 个维度）。检测回退（delta < -3）并触发强制检查点。
- **第 2 阶段并行化** —— 可视化与论证构建可在大纲完成后并行运行。
- 新版本：deep-research v2.8, academic-paper v3.0, academic-pipeline v3.2

### v3.2 (2026-04-09) — Lu 2026 Nature 集成
集成 Lu et al. (2026, *Nature* 651:914-919) 的见解——首个端到端全自动 AI 研究系统通过盲审。

- **7 模式 AI 研究失败模式检查清单** —— 在第 2.5/4.5 阶段阻断疑似实现 bug、幻觉结果、捷径依赖、bug-as-insight、方法论伪造、框架锁定。扩展现有 5 类型引用幻觉分类法。
- **评审员校准模式** (academic-paper-reviewer v1.8) —— 可选 FNR/FPR/平衡准确率测量，基于用户提供的金标准集。5× 集成，跨模型默认开启，会话范围置信度披露。
- **披露模式** (academic-paper v2.9) —— 场地特定 AI 使用声明生成器。v1 覆盖 ICLR, NeurIPS, Nature, Science, ACL, EMNLP。
- **早停标准** (academic-pipeline v3.1) —— 收敛检查 + 预算透明度于管线启动时。
- **保真度-原创性模式光谱** —— 按 Lu 2026 Fig 1c 对全部三种技能中的所有模式进行分类。
- 新版本：academic-paper v2.9, academic-paper-reviewer v1.8, academic-pipeline v3.1

### v3.1.1 (2026-04-09) — IS Senior Scholars' Basket of 11
外部贡献：[@mchesbro1](https://github.com/mchesbro1) 最初提出并起草了 IS Basket of 8 期刊 ([Issue #5](https://github.com/Imbad0202/academic-research-skills/issues/5))；[@cloudenochcsis](https://github.com/cloudenochcsis) 将其扩展至完整的 Senior Scholars' Basket of 11 ([Issue #7](https://github.com/Imbad0202/academic-research-skills/issues/7), [PR #8](https://github.com/Imbad0202/academic-research-skills/pull/8))。更新 `academic-paper-reviewer/references/top_journals_by_field.md` 第 7 节，新增 *Decision Support Systems*, *Information & Management*, 和 *Information and Organization*。来源：[AIS Senior Scholars' List of Premier Journals](https://aisnet.org/research/seniorscholarsbasket/)。

### v3.1 (2026-04-06) — 反上下文旋转 + 认知框架 + 精简体积
受 [aspi6246/Claude-Code-Skills-for-Academics](https://github.com/aspi6246/Claude-Code-Skills-for-Academics) 中的模式启发。

**Wave 1: 反上下文旋转锚点**
- 全部 4 项技能中 29 个显式反模式（每项技能 7-8 个，表格格式含“为何失败”+“正确行为”）
- 关键规则上 22 个 IRON RULE 标记，即使在长对话中也不得违反
- academic-paper-reviewer 只读约束（评审员不可修改手稿）

**Wave 2: 可追溯性 + 认知框架 + 强化**
- R&R 可追溯矩阵 (Schema 11)：在复审输出中新增“作者主张”和“已验证？”列，启用修订主张的独立验证
- 3 个认知框架参考文件教授智能体“如何思考”而不仅是“做什么”：
  - `argumentation_reasoning_framework.md` —— Toulmin 模型、Bradford Hill 因果推理、最佳解释推断、认识状态分类
  - `review_quality_thinking.md` —— 三透镜（内部效度、外部效度、贡献）、常见评审员陷阱、校准问题
  - `writing_judgment_framework.md` —— 清晰度测试、读者旅程、学科特定语气、修订决策矩阵
- 对话中强化协议：每次管线转换时阶段特定的 IRON RULE + 反模式提醒
- 每次 FULL 检查点自检问题（引用完整性、迎合性让步、质量轨迹、范围纪律、完整性）

**Wave 3: 精简技能体积**
- SKILL.md 总大小从 142KB 降至 85KB（−40%），通过将详细协议提取至 `references/` 文件实现
- 创建 ~15 个新参考文件（复审协议、引导模式、系统综述、流程总结、外部评审等）
- SKILL.md 中保留所有 IRON RULE 标记；详细内容按需加载
- 新版本：deep-research v2.7, academic-paper v2.8, academic-paper-reviewer v1.7, academic-pipeline v3.0

### v3.0 (2026-04-03) — 反迎合 + 意图检测 + 对话健康
- **魔鬼代言人让步阈值** (deep-research + academic-paper-reviewer): DA 必须在回应前对反驳进行 1-5 分评分。仅 ≥4 时让步。禁止连续让步。记录让步率。每个检查点后检测框架锁定。
- **攻击强度保留** (academic-paper-reviewer): DA 在施压下不软化。含显式偏转检测的反驳评估协议。反迎合规则防止持续施压被当作有效证据。
- **意图检测层** (deep-research socratic): 将用户意图分类为探索性 vs. 目标导向型。探索模式禁用自动收敛，提升最高轮次，禁止过早关闭。每 3 轮重新评估。
- **对话健康指标** (deep-research socratic): 每 5 轮无声自检持续同意、回避冲突、过早收敛。检测到同意模式时自动注入挑战。
- **跨模型验证协议**（共享，可选）：使用 GPT-5.4 Pro 或 Gemini 3.1 Pro 进行完整性验证样本交叉检查和独立 DA 批评。第六评审员同行评审仍为计划中，未实现。通过设置 `ARS_CROSS_MODEL` 环境变量激活——不设置则一切如常运行。完整设置指南、API 模式和成本估算见 `shared/cross_model_verification.md`。
- **AI 自我反思报告** (academic-pipeline Stage 6): 管线后 AI 行为模式自评——DA 让步率、检查点跳过率、健康警报、迎合风险评级（LOW/MEDIUM/HIGH）、框架锁定事件、收敛模式分析。含反讽警告：“此自我反思本身由可能曾迎合的同一 AI 生成。”
- 起源：通过四轮辩证实验发现，DA 让步过快，苏格拉底导师试图过早收敛，且整个辩论被锁在人类设定的框架内。
- 版本：deep-research v2.5, academic-paper-reviewer v1.5, academic-pipeline v2.8

### v2.9.1 (2026-04-03) — 技能元数据
- 在所有四个 SKILL.md frontmatter 中新增 `status: active` 和 `related_skills` 交叉引用。
- 启用技能发现工具和跨技能导航，覆盖 `deep-research` ↔ `academic-paper` ↔ `academic-paper-reviewer` ↔ `academic-pipeline`。

### v2.9 (2026-03-27) — 风格校准 + 写作质量检查
- **风格校准** (academic-paper intake Step 10, 可选): 提供 3+ 篇过往论文，管线学习你的行文语气——句子节奏、词汇偏好、引用集成风格。起草时作为软性指导应用；学科惯例始终优先。优先级系统：学科规范（硬）> 期刊惯例（强）> 个人风格（软）。见 `shared/style_calibration_protocol.md`
- **写作质量检查** (`academic-paper/references/writing_quality_check.md`): 在草稿自审时应用的写作质量清单。5 类：AI 高频词警告（25 个术语）、标点模式控制（em dash ≤3）、清嗓式开头检测、结构模式警告（Rule of Three、统一段落、同义词循环）及 burstiness 检查（句子长度变化）。这些是良好写作规则——非检测规避
- **风格档案** 贯穿 academic-pipeline 材料护照传输 (Schema 10 in `shared/handoff_schemas.md`)
- **deep-research** 报告编译器也可选消费两种功能
- 版本：academic-paper v2.5, deep-research v2.4, academic-pipeline v2.7

### v2.8 (2026-03-22) — SCR Loop Phase 1: State-Challenge-Reflect
- **苏格拉底导师智能体** (deep-research + academic-paper): SCR（State-Challenge-Reflect）协议集成
  - **承诺门禁**: 在每层/章节转换呈现证据前收集用户预测
  - **确定性触发矛盾**: 检测高置信度语言（“显然”、“清楚表明”）并引入反论点
  - **自适应强度**: 跟踪承诺准确率，动态调整挑战频率
  - **自校准信号 (S5)**: 新增收敛信号跟踪对话中用户的自校准增长
  - **SCR 切换**: 用户可说 “skip the predictions” 禁用或 “turn predictions back on” 在对话中途重新启用；苏格拉底提问正常继续
- `deep-research/references/socratic_questioning_framework.md`: SCR Overlay Protocol 将 SCR 阶段映射至苏格拉底功能
- 新增 `CHANGELOG.md`

### v2.7 (2026-03-09) — 完整性验证 v2.0: 反幻觉 overhaul
- **integrity_verification_agent v2.0**: 反幻觉强制令（无 AI 内存验证）、消除灰色地带分类（仅 VERIFIED/NOT_FOUND/MISMATCH）、每条引用强制 WebSearch 审计轨迹、第 4.5 阶段新鲜独立验证、灰色地带预防规则
- **已知幻觉模式**: GPTZero × NeurIPS 2025 研究的 5 类型分类法 (TF/PAC/IH/PH/SH)、5 种复合欺骗模式、真实案例研究、文献统计
- **发布后审计**: 全 WebSearch 验证全部 68 条引用发现 21 个问题（31% 错误率）通过 3 轮完整性检查——证明外部验证的必要性
- **论文修正**: 移除 4 条伪造引用，修复 6 处作者错误，纠正 7 处元数据错误，修复 2 处格式问题

### v2.6.2 (2026-03-09) — 基于意图的模式激活
- **deep-research**: 苏格拉底模式现使用 **基于意图的激活** 替代关键词匹配。适用于任何语言——检测含义（如“用户想要引导思考”）而非匹配特定字符串。
- **academic-paper**: 规划模式现使用 **基于意图的激活**。在任何语言中检测意图信号，如“用户不确定如何开始”或“用户想要逐步指导”。
- 两种模式现在都有 **默认规则**：当意图模糊时，优先 `socratic`/`plan` 而非 `full`——先引导更安全。
- 双层架构：Layer 1（技能激活）使用双语关键词提升匹配置信度；Layer 2（模式路由）使用语言无关的意图信号。

### v2.6.1 (2026-03-09) — 双语触发关键词
- **deep-research**: 新增繁体中文通用激活和苏格拉底模式触发关键词。
- **academic-paper**: 新增繁体中文触发关键词和规划模式触发部分。
- 两种模式选择指南现包含双语示例及中文特定误选场景。

### v2.6 / v2.4 / v1.4 (2026-03-08) — 15+ 改进
- **deep-research v2.3**: 新增系统综述/PRISMA 模式（第 7 种）；3 个新智能体（risk_of_bias, meta_analysis, monitoring）；PRISMA 协议/报告模板；苏格拉底收敛标准（4 信号 + 自动结束）；快速模式选择指南
- **academic-paper v2.4**: 2 个新智能体（visualization, revision_coach）；修订跟踪模板含 4 种状态类型；引用格式转换 (APA↔Chicago↔MLA↔IEEE↔Vancouver)；统计可视化标准；苏格拉底收敛标准；修订恢复示例；**LaTeX 输出加固** ——强制 `apa7` 文档类、文本两端对齐修复 (`ragged2e` + `etoolbox`)、表格列宽公式、双语摘要居中、标准化字体栈 (Times New Roman + Source Han Serif TC VF + Courier New)、PDF 仅通过 tectonic
- **academic-paper-reviewer v1.4**: 含 0-100 分制和行为指标的质量量规；决策映射（≥80 Accept, 65-79 Minor, 50-64 Major, <50 Reject）；快速模式选择指南
- **academic-pipeline v2.6**: 自适应检查点系统 (FULL/SLIM/MANDATORY)；Phase E 主张验证在完整性检查中；材料护照用于中途入口溯源；跨技能模式顾问（14 场景）；团队协作协议；增强交接模式（9 个模式）；完整性失败恢复示例

### v2.4 / v1.3 (2026-03-08)
- **academic-pipeline v2.4**: 新增第 6 阶段 PROCESS SUMMARY ——自动生成结构化论文创作过程记录 (MD → LaTeX → PDF, 双语)；强制最终章：**协作质量评估**，含 6 维度 1–100 分制评分（方向设定、智力贡献、质量门禁、迭代纪律、委托效率、元学习）、诚实反馈及改进建议；管线从 9 阶段扩展至 10 阶段

### v2.3 / v1.3 (2026-03-08)
- **academic-pipeline v2.3**: Stage 5 FINALIZE 现提示格式化风格 (APA 7.0 / Chicago / IEEE)；PDF 必须通过 `tectonic` 从 LaTeX 编译（无 HTML-to-PDF）；APA 7.0 使用 `apa7` 文档类 (`man` mode) 配合 XeCJK 实现双语 CJK 支持；字体栈：Times New Roman + Source Han Serif TC VF + Courier New

### v2.2 / v1.3 (2025-03-05)
- **跨智能体质量对齐**: 统一所有智能体的定义（同行评审、时效性规则、CRITICAL 严重度、来源层级）
- **deep-research v2.2**: synthesis 反模式、苏格拉底自动结束条件、DOI+WebSearch 验证、增强伦理完整性检查、模式转换矩阵
- **academic-paper v2.2**: 4 级论证评分、抄袭筛查、2 条新失败路径 (F11 Desk-Reject Recovery, F12 Conference-to-Journal)、Plan→Full 模式转换
- **academic-paper-reviewer v1.3**: DA vs R3 角色边界、CRITICAL 发现标准、共识分类 (4/3/SPLIT/DA-CRITICAL)、置信度分数加权、亚洲及区域期刊参考
- **academic-pipeline v2.2**: 检查点确认语义、模式切换矩阵、失败回退矩阵、状态所有权协议、材料版本控制

### v2.0.1 (2026-03)
- **简化 4 SKILL.md** (-371 行, -16.5%): 移除跨技能重复、内联模板 → 文件引用、冗余路由表、重复模式选择部分
- 修复 academic-paper 和 academic-pipeline 间修订循环上限矛盾

### v2.0 (2026-02)
- **academic-pipeline v2.0**: 5→9 阶段，强制完整性验证，双阶段评审，苏格拉底修订辅导，可复现性保证
- **academic-paper-reviewer v1.1**: +魔鬼代言人评审员（第 7 智能体）、+复审模式（验证）、+审后苏格拉底辅导
- 新智能体：`integrity_verification_agent` —— 100% 引用/数据验证带审计轨迹
- 新智能体：`devils_advocate_reviewer_agent` —— 8 维度论点挑战者
- 输出顺序：MD → DOCX via Pandoc（若可用则 else 提供说明）→ ask LaTeX → confirm → PDF

### v1.0 (2026-02)
- 初始发布
- deep-research v2.0（10 智能体，含 socratic 的 6 模式）
- academic-paper v2.0（10 智能体，含 plan 的 8 模式）
- academic-paper-reviewer v1.0（6 智能体，含 guided 的 4 模式）
- academic-pipeline v1.0（编排器）