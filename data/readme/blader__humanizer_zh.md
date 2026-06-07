# Humanizer

一款适用于 Claude Code 和 OpenCode 的 Skill（技能），用于去除文本中的人工智能生成痕迹，使其读起来更自然、更像人类书写。

## Installation

### Claude Code

直接克隆到 Claude Code 的 Skill 目录：

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/blader/humanizer.git ~/.claude/skills/humanizer
```

如果你已克隆该仓库，也可手动复制技能文件：

```bash
mkdir -p ~/.claude/skills/humanizer
cp SKILL.md ~/.claude/skills/humanizer/
```

### OpenCode

直接克隆到 OpenCode 的 Skill 目录：

```bash
mkdir -p ~/.config/opencode/skills
git clone https://github.com/blader/humanizer.git ~/.config/opencode/skills/humanizer
```

如果你已克隆该仓库，也可手动复制技能文件：

```bash
mkdir -p ~/.config/opencode/skills/humanizer
cp SKILL.md ~/.config/opencode/skills/humanizer/
```

> **Note:** OpenCode also scans `~/.claude/skills/` for compatibility, so if you use both tools, a single clone into `~/.claude/skills/humanizer/` is enough.
> > **注意：** OpenCode 也会扫描 `~/.claude/skills/` 目录以保持兼容，因此如果你同时使用这两个工具，只需将仓库克隆到 `~/.claude/skills/humanizer/` 即可。

## Usage

### Claude Code

```
/humanizer

[paste your text here]
```

### OpenCode

```
/humanizer

[paste your text here]
```

或者你也可以直接在任一工具中要求模型进行拟人化处理：

```
Please humanize this text: [your text]
```

### Voice Calibration (文风校准)

为了匹配你的个人写作风格，请提供一段你自己的写作样本：

```
/humanizer

Here's a sample of my writing for voice matching:
[paste 2-3 paragraphs of your own writing]

Now humanize this text:
[paste AI text to humanize]
```

该 Skill 会分析你的句式节奏、用词习惯和个性化表达，并将其应用到重写结果中，而不是生成千篇一律的“干净”文本。

## Overview

本工具基于由 WikiProject AI Cleanup 维护的维基百科指南《[AI 写作特征](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)》。该综合指南源于对数千个 AI 生成文本实例的观察总结。

该 Skill 还包含一次最终的“明显 AI 生成”审查环节以及第二次重写，以捕捉初稿中残留的 AI 写作习惯。

### Key Insight from Wikipedia (来自维基百科的关键洞察)

> "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."
> > “大语言模型使用统计算法来猜测接下来应该出现什么内容。其结果往往倾向于最符合统计学概率、且能适用于最广泛场景的选项。”

## 30 Patterns Detected (with Before/After Examples) (检测到的 30 种模式（含修改前后示例）)

### Content Patterns (内容模式)

| # | Pattern (模式) | Before (AI 原文) | After (拟人化) |
|---|---------|--------|-------|
| 1 | **Significance inflation (重要性夸大)** | "marking a pivotal moment in the evolution of..." | "was established in 1989 to collect regional statistics" |
| 2 | **Notability name-dropping (堆砌知名机构/媒体)** | "cited in NYT, BBC, FT, and The Hindu" | "In a 2024 NYT interview, she argued..." |
| 3 | **Superficial -ing analyses (浅尝辄止的动名词分析)** | "symbolizing... reflecting... showcasing..." | Remove or expand with actual sources |
| 4 | **Promotional language (宣传性用语)** | "nestled within the breathtaking region" | "is a town in the Gonder region" |
| 5 | **Vague attributions (模糊的归因表述)** | "Experts believe it plays a crucial role" | "according to a 2019 survey by..." |
| 6 | **Formulaic challenges (套路化的挑战描述)** | "Despite challenges... continues to thrive" | Specific facts about actual challenges |

### Language Patterns (语言模式)

| # | Pattern (模式) | Before (AI 原文) | After (拟人化) |
|---|---------|--------|-------|
| 7 | **AI vocabulary (AI 常用词汇)** | "Actually... additionally... testament... landscape... showcasing" | "also... remain common" |
| 8 | **Copula avoidance (回避系动词 is/am/are)** | "serves as... features... boasts" | "is... has" |
| 9 | **Negative parallelisms / tailing negations (否定平行结构 / 尾部否定)** | "It's not just X, it's Y", "..., no guessing" | State the point directly |
| 10 | **Rule of three (“三要素”套路)** | "innovation, inspiration, and insights" | Use natural number of items |
| 11 | **Synonym cycling (同义词循环替换)** | "protagonist... main character... central figure... hero" | "protagonist" (repeat when clearest) |
| 12 | **False ranges (虚假的范围列举)** | "from the Big Bang to dark matter" | List topics directly |
| 13 | **Passive voice / subjectless fragments (被动语态 / 无主语句碎片)** | "No configuration file needed" | Name the actor when it helps clarity |

### Style Patterns (风格模式)

| # | Pattern (模式) | Before (AI 原文) | After (拟人化) |
|---|---------|--------|-------|
| 14 | **Em/en dashes (破折号滥用)** | "institutions—not the people—yet this continues—" | Cut them: periods, commas, colons, or parentheses |
| 15 | **Boldface overuse (加粗过度)** | "**OKRs**, **KPIs**, **BMC**" | "OKRs, KPIs, BMC" |
| 16 | **Inline-header lists (行内标题列表)** | "**Performance:** Performance improved" | Convert to prose |
| 17 | **Title Case Headings (标题大小写滥用)** | "Strategic Negotiations And Partnerships" | "Strategic negotiations and partnerships" |
| 18 | **Emojis (表情符号)** | "🚀 Launch Phase: 💡 Key Insight:" | Remove emojis |
| 19 | **Curly quotes (弯引号)** | `said “the project”` | `said “the project”` |
| 26 | **Hyphenated word pairs (连字符词组)** | “cross-functional, data-driven, client-facing” | Drop hyphens on common word pairs |
| 27 | **Persuasive authority tropes (说教式权威套路)** | "At its core, what matters is..." | State the point directly |
| 28 | **Signposting announcements (路标式预告语)** | "Let's dive in", "Here's what you need to know" | Start with the content |
| 29 | **Fragmented headers (碎片化标题)** | "## Performance" + "Speed matters." | Let the heading do the work |
| 30 | **Diff-anchored writing (基于差异的写作)** | "This function was added to replace..." | Describe what it does, not what changed |

### Communication Patterns (交互模式)

| # | Pattern (模式) | Before (AI 原文) | After (拟人化) |
|---|---------|--------|-------|
| 20 | **Chatbot artifacts (聊天机器人痕迹)** | "I hope this helps! Let me know if..." | Remove entirely |
| 21 | **Cutoff disclaimers (截断式免责声明/提示)** | "While details are limited in available sources..." | Find sources or remove |
| 22 | **Sycophantic tone (谄媚语气)** | "Great question! You're absolutely right!" | Respond directly |

### Filler and Hedging (填充词与模糊表述)

| # | Pattern (模式) | Before (AI 原文) | After (拟人化) |
|---|---------|--------|-------|
| 23 | **Filler phrases (填充短语)** | "In order to", "Due to the fact that" | "To", "Because" |
| 24 | **Excessive hedging (过度模糊/保守表述)** | "could potentially possibly" | "may" |
| 25 | **Generic conclusions (泛泛的结论)** | "The future looks bright" | Specific plans or facts |

## Full Example (完整示例)

**Before (AI-sounding):** (修改前（带有 AI 味）：)
> Great question! Here is an essay on this topic. I hope this helps!
>
> AI-assisted coding serves as an enduring testament to the transformative potential of large language models, marking a pivotal moment in the evolution of software development. In today's rapidly evolving technological landscape, these groundbreaking tools—nestled at the intersection of research and practice—are reshaping how engineers ideate, iterate, and deliver, underscoring their vital role in modern workflows.
>
> At its core, the value proposition is clear: streamlining processes, enhancing collaboration, and fostering alignment. It's not just about autocomplete; it's about unlocking creativity at scale, ensuring that organizations can remain agile while delivering seamless, intuitive, and powerful experiences to users. The tool serves as a catalyst. The assistant functions as a partner. The system stands as a foundation for innovation.
>
> Industry observers have noted that adoption has accelerated from hobbyist experiments to enterprise-wide rollouts, from solo developers to cross-functional teams. The technology has been featured in The New York Times, Wired, and The Verge. Additionally, the ability to generate documentation, tests, and refactors showcases how AI can contribute to better outcomes, highlighting the intricate interplay between automation and human judgment.
>
> - 💡 **Speed:** Code generation is significantly faster, reducing friction and empowering developers.
> - 🚀 **Quality:** Output quality has been enhanced through improved training, contributing to higher standards.
> - ✅ **Adoption:** Usage continues to grow, reflecting broader industry trends.
>
> While specific details are limited based on available information, it could potentially be argued that these tools might have some positive effect. Despite challenges typical of emerging technologies—including hallucinations, bias, and accountability—the ecosystem continues to thrive. In order to fully realize this potential, teams must align with best practices.
>
> In conclusion, the future looks bright. Exciting times lie ahead as we continue this journey toward excellence. Let me know if you’d like me to expand on any section!

**After (Humanized):** (修改后（拟人化）：)
> AI coding assistants can speed up the boring parts of the job. They're great at boilerplate: config files and the little glue code you don't want to write. They can also help you sketch a test, but you still have to read it.
>
> The dangerous part is how confident the suggestions look. I've accepted code that compiled and passed lint, then discovered later it missed the point because I stopped paying attention.
>
> If you treat it like autocomplete and review every line, it's useful. If you use it to avoid thinking, it will help you ship bugs faster.
>
> The only real backstop is tests. Without them, you're mostly judging vibes.

## References (参考资料)

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) - Primary source (主要参考来源)
- [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup) - Maintaining organization (维护组织)

## Version History (更新日志)

- **2.7.0** - Added pattern #30 (diff-anchored writing); made em/en dashes a hard cut rather than "overuse"; expanded #21 to cover speculative gap-filling ("maintains a low profile"). 30 patterns total.
- **2.6.0** - Cleanup pass: consolidated the duplicated workflow sections, gated the personality guidance to content where voice is wanted, removed the model-fingerprinting subsection, and condensed the worked example. No change to the 29 patterns.
- **2.5.1** - Added a passive-voice / subjectless-fragment rule, raising the total to 29 patterns (新增被动语态/无主语句规则，总数增至 29 种模式)
- **2.5.0** - Added patterns for persuasive framing, signposting, and fragmented headers; expanded negative parallelisms to cover tailing negations; tightened wording around em dash overuse; fixed frontmatter wording to use "filler phrases" (新增说教式框架、路标提示和碎片化标题的模式；扩展否定平行结构以覆盖尾部否定；收紧关于破折号滥用的表述；修正前置元数据用词，改为使用“填充短语”)
- **2.4.0** - Added voice calibration: match the user's personal writing style from samples (新增文风校准功能：根据用户提供的样本匹配其个人写作风格)
- **2.3.0** - Added pattern #25: hyphenated word pair overuse (新增模式 #25：连字符词组滥用)
- **2.2.0** - Added a final "obviously AI generated" audit + second-pass rewrite prompts (增加最终的“明显 AI 生成”审查环节及第二次重写提示词)
- **2.1.1** - Fixed pattern #18 example (curly quotes vs straight quotes) (修复模式 #18 示例：弯引号与直引号的区分)
- **2.1.0** - Added before/after examples for all 24 patterns (为所有 24 种模式添加修改前后示例)
- **2.0.0** - Complete rewrite based on raw Wikipedia article content (基于维基百科原始文章内容进行彻底重写)
- **1.0.0** - Initial release (首次发布)

## License (许可证)

MIT