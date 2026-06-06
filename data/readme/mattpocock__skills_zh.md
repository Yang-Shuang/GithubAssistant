<p>
  <a href="https://www.aihero.dev/s/skills-newsletter">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skills-repo-dark_2x.png">
      <source media="(prefers-color-scheme: light)" srcset="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skill-repo-light_2x.png">
      <img alt="Skills" src="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skill-repo-light_2x.png" width="369">
    </picture>
  </a>
</p>

# Skills For Real Engineers（面向真实工程师的技能）

[![skills.sh](https://skills.sh/b/mattpocock/skills)](https://skills.sh/mattpocock/skills)

这是我每天用于实际工程开发（而非随性编码 vibe coding）的 Agent 技能。

开发真实应用并不容易。GSD、BMAD 和 Spec-Kit 等方案试图通过接管流程来提供帮助，但在这个过程中它们会剥夺你的控制权，并使流程中产生的 Bug 难以解决。

这些技能设计得小巧、易于调整且可组合（composable）。它们适用于任何模型，基于数十年的工程经验打造。你可以随意修改它们，让它们成为你自己的风格。享受吧！

如果你想及时了解这些技能的更新以及我创建的任何新技能，可以订阅我的通讯（Newsletter），与约 60,000 名其他开发者一起获取最新动态：

[订阅通讯](https://www.aihero.dev/s/skills-newsletter)

## Quickstart (30-second setup) / 快速入门（30秒配置）

1. Run the skills.sh installer:
   运行 `skills.sh` 安装程序：

```bash
npx skills@latest add mattpocock/skills
```

2. Pick the skills you want, and which coding agents you want to install them on. **Make sure you select `/setup-matt-pocock-skills`**.
   选择你想要的技能，以及要将其安装在哪些编码 Agent 上。**请务必选择 `/setup-matt-pocock-skills`**。

3. Run `/setup-matt-pocock-skills` in your agent. It will:
   在你的 Agent 中运行 `/setup-matt-pocock-skills`。它将：
   - Ask you which issue tracker you want to use (GitHub, Linear, or local files)
     询问你想使用哪种问题追踪器（GitHub、Linear 或本地文件）
   - Ask you what labels you apply to ticks when you triage them (`/triage` uses labels)
     询问你在分类处理问题时使用的标签是什么（`/triage` 会使用这些标签）
   - Ask you where you want to save any docs we create
     询问你想将我们创建的文档保存在哪里

4. Bam - you're ready to go.
   搞定——你现在就可以开始使用了。

## Why These Skills Exist / 为什么需要这些技能

I built these skills as a way to fix common failure modes I see with Claude Code, Codex, and other coding agents.
我开发这些技能是为了解决我在 Claude Code、Codex 及其他编码 Agent 中经常看到的常见失效模式。

### #1: The Agent Didn't Do What I Want / #1：Agent 没有按我的预期执行

> "No-one knows exactly what they want"
> David Thomas & Andrew Hunt, [The Pragmatic Programmer](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)
> “没人能确切知道自己想要什么”
> David Thomas & Andrew Hunt，《[敏捷软件开发](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)》

**The Problem**. The most common failure mode in software development is misalignment. You think the dev knows what you want. Then you see what they've built - and you realize it didn't understand you at all.
**问题所在**。软件开发生命周期中最常见的失效模式是对齐偏差。你以为开发者知道你想要什么，但当你看到他们构建的东西时——你意识到它完全误解了你的意图。

This is just the same in the AI age. There is a communication gap between you and the agent. The fix for this is a **grilling session** - getting the agent to ask you detailed questions about what you're building.
在 AI 时代也是如此。你与 Agent 之间存在沟通鸿沟。解决方法是进行一次**深度拷问会话（grilling session）**——让 Agent 就你要构建的内容向你提出详细问题。

**The Fix** is to use:
**解决方案**是使用：
- [`/grill-me`](./skills/productivity/grill-me/SKILL.md) - for non-code uses
  [`/grill-me`](./skills/productivity/grill-me/SKILL.md) ——用于非代码类场景
- [`/grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) - same as [`/grill-me`](./skills/productivity/grill-me/SKILL.md), but adds more goodies (see below)
  [`/grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) ——与 [`/grill-me`](./skills/productivity/grill-me/SKILL.md) 相同，但增加了更多实用功能（详见下文）

These are my most popular skills. They help you align with the agent before you get started, and think deeply about the change you're making. Use them _every_ time you want to make a change.
这是我最受欢迎的技能。它们帮助你在开始之前与 Agent 对齐目标，并深入思考你要进行的变更。每次想要进行修改时都使用它们。

### #2: The Agent Is Way Too Verbose / #2：Agent 过于啰嗦

> With a ubiquitous language, conversations among developers and expressions of the code are all derived from the same domain model.
> Eric Evans, [Domain-Driven-Design](https://www.amazon.co.uk/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)
> “通过通用语言（Ubiquitous Language），开发者之间的对话和代码表达都源自同一个领域模型。”
> Eric Evans，《[领域驱动设计](https://www.amazon.co.uk/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)》

**The Problem**: At the start of a project, devs and the people they're building the software for (the domain experts) are usually speaking different languages.
**问题所在**：在项目初期，开发者和他们为之构建软件的人（领域专家）通常说着不同的“语言”。

I felt the same tension with my agents. Agents are usually dropped into a project and asked to figure out the jargon as they go. So they use 20 words where 1 will do.
我的 Agent 也存在同样的张力。Agent 通常被直接丢进项目中，要求它们在过程中自行摸索专业术语。因此它们会用 20 个字表达原本只需 1 个词就能说清的意思。

**The Fix** for this is a shared language. It's a document that helps agents decode the jargon used in the project.
**解决方案**是建立共享语言（Shared Language）。这是一份帮助 Agent 解读项目中专业术语的文档。

<details>
<summary>Example</summary>
Here's an example [`CONTEXT.md`](https://github.com/mattpocock/course-video-manager/blob/076a5a7a182db0fe1e62971dd7a68bcadf010f1c/CONTEXT.md), from my `course-video-manager` repo. Which one is easier to read?
这里有一个来自我 `course-video-manager` 仓库的 [`CONTEXT.md`](https://github.com/mattpocock/course-video-manager/blob/076a5a7a182db0fe1e62971dd7a68bcadf010f1c/CONTEXT.md) 示例。哪个更容易阅读？
- **BEFORE**: "There's a problem when a lesson inside a section of a course is made 'real' (i.e. given a spot in the file system)"
  - **修改前**：“当课程章节内的课程被设为‘真实’（即分配文件系统位置）时会出现问题”
- **AFTER**: "There's a problem with the materialization cascade"
  - **修改后**：“存在物化级联问题”

This concision pays off session after session.
这种简洁性能在每次会话中带来显著收益。
</details>

This is built into [`/grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md). It's a grilling session, but that helps you build a shared language with the AI, and document hard-to-explain decisions in ADR's.
这已内置于 [`/grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) 中。它是一个拷问会话，但能帮助你与 AI 建立共享语言，并将难以解释的决策记录在架构决策记录（ADR）中。

It's hard to explain how powerful this is. It might be the single coolest technique in this repo. Try it, and see.
很难用言语形容它的强大之处。这可能是本仓库中最酷的技巧之一。试试看，感受一下吧。

> [!TIP]
> A shared language has many other benefits than reducing verbosity:
> 共享语言除了减少啰嗦之外还有许多其他好处：
> - **Variables, functions and files are named consistently**, using the shared language
>   - **变量、函数和文件命名保持一致**，均使用共享语言
> - As a result, the **codebase is easier to navigate** for the agent
>   - 因此，Agent 能更轻松地**浏览代码库**
> - The agent also **spends fewer tokens on thinking**, because it has access to a more concise language
>   - Agent 也**减少了在思考上消耗的 Token**，因为它可以使用更简洁的语言

### #3: The Code Doesn't Work / #3：代码无法正常运行

> "Always take small, deliberate steps. The rate of feedback is your speed limit. Never take on a task that’s too big."
> David Thomas & Andrew Hunt, [The Pragmatic Programmer](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)
> “始终采取小而审慎的步骤。反馈速率就是你的限速器。永远不要接手超出范围的任务。”
> David Thomas & Andrew Hunt，《[敏捷软件开发](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)》

**The Problem**: Let's say that you and the agent are aligned on what to build. What happens when the agent _still_ produces crap?
**问题所在**：假设你和 Agent 在构建目标上已经对齐，但当 Agent _仍然_ 产出垃圾代码时该怎么办？

It's time to look at your feedback loops. Without feedback on how the code it produces actually runs, the agent will be flying blind.
是时候审视你的反馈循环了。如果没有关于生成代码实际运行情况的反馈，Agent 就会盲目工作。

**The Fix**: You need the usual tranche of feedback loops: static types, browser access, and automated tests.
**解决方案**：你需要一套标准的反馈循环工具链：静态类型检查、浏览器访问权限和自动化测试。

For automated tests, a red-green-refactor loop is critical. This is where the agent writes a failing test first, then fixes the test. This helps give the agent a consistent level of feedback that results in far better code.
对于自动化测试，红-绿-重构循环（red-green-refactor loop）至关重要。即 Agent 先编写一个失败的测试，然后修复代码使其通过。这能为 Agent 提供一致级别的反馈，从而产出质量高得多的代码。

I've built a **[`/tdd`](./skills/engineering/tdd/SKILL.md) skill** you can slot into any project. It encourages red-green-refactor and gives the agent plenty of guidance on what makes good and bad tests.
我构建了一个 **[`/tdd`](./skills/engineering/tdd/SKILL.md)** 技能，你可以将其无缝集成到任何项目中。它鼓励红-绿-重构流程，并为 Agent 提供大量关于如何编写优质测试的指导。

For debugging, I've also built a **[`/diagnose`](./skills/engineering/diagnose/SKILL.md)** skill that wraps best debugging practices into a simple loop.
对于调试，我还构建了一个 **[`/diagnose`](./skills/engineering/diagnose/SKILL.md)** 技能，它将最佳调试实践封装在一个简单的循环中。

### #4: We Built A Ball Of Mud / #4：我们构建了一团乱麻（代码泥球）

> "Invest in the design of the system _every day_."
> Kent Beck, [Extreme Programming Explained](https://www.amazon.co.uk/Extreme-Programming-Explained-Embrace-Change/dp/0321278658)
> “每天都要投入精力设计系统。”
> Kent Beck，《[极限编程精粹](https://www.amazon.co.uk/Extreme-Programming-Explained-Embrace-Change/dp/0321278658)》

> "The best modules are deep. They allow a lot of functionality to be accessed through a simple interface."
> John Ousterhout, [A Philosophy Of Software Design](https://www.amazon.co.uk/Philosophy-Of-Software-Design-2nd/dp/173210221X)
> “最好的模块是深层的。它们允许通过简单的接口访问大量功能。”
> John Ousterhout，《[软件设计哲学](https://www.amazon.co.uk/Philosophy-Of-Software-Design-2nd/dp/173210221X)》

**The Problem**: Most apps built with agents are complex and hard to change. Because agents can radically speed up coding, they also accelerate software entropy. Codebases get more complex at an unprecedented rate.
**问题所在**：大多数由 Agent 构建的应用复杂且难以修改。由于 Agent 能大幅加速编码，它们也会加速软件熵增（代码腐化）。代码库的复杂度以前所未有的速度增长。

**The Fix** for this is a radical new approach to AI-powered development: caring about the design of the code.
**解决方案**是对 AI 辅助开发采取一种全新的激进方法：关注代码设计本身。

This is built in to every layer of these skills:
这已内置于这些技能的每一层中：
- [`/to-prd`](./skills/engineering/to-prd/SKILL.md) quizzes you about which modules you're touching before creating a PRD
  [`/to-prd`](./skills/engineering/to-prd/SKILL.md) ——在创建产品需求文档（PRD）前，会就你将触及的模块对你进行提问
- [`/zoom-out`](./skills/engineering/zoom-out/SKILL.md) tells the agent to explain code in the context of the whole system
  [`/zoom-out`](./skills/engineering/zoom-out/SKILL.md) ——指示 Agent 结合整个系统的上下文来解释代码

And crucially, [`/improve-codebase-architecture`](./skills/engineering/improve-codebase-architecture/SKILL.md) helps you rescue a codebase that has become a ball of mud. I recommend running it on your codebase once every few days.
关键在于，[`/improve-codebase-architecture`](./skills/engineering/improve-codebase-architecture/SKILL.md) 能帮助你拯救已经变成一团乱麻的代码库。我建议每隔几天在你的代码库上运行一次它。

### Summary / 总结

Software engineering fundamentals matter more than ever. These skills are my best effort at condensing these fundamentals into repeatable practices, to help you ship the best apps of your career. Enjoy.
软件工程的基本功比以往任何时候都更重要。这些技能是我将上述基本功浓缩为可重复实践的最佳尝试，旨在帮助你打造出职业生涯中最出色的应用。享受吧！

## Reference / 参考文档

### Engineering / 工程类（Engineering）

Skills I use daily for code work.
我日常用于代码工作的技能。

- **[diagnose](./skills/engineering/diagnose/SKILL.md)** — Disciplined diagnosis loop for hard bugs and performance regressions: reproduce → minimise → hypothesise → instrument → fix → regression-test.
  - **[diagnose](./skills/engineering/diagnose/SKILL.md)** ——针对顽固 Bug 和性能回退的规范化诊断循环：复现 → 最小化 → 假设 → 注入指标 → 修复 → 回归测试。
- **[grill-with-docs](./skills/engineering/grill-with-docs/SKILL.md)** — Grilling session that challenges your plan against the existing domain model, sharpens terminology, and updates `CONTEXT.md` and ADRs inline.
  - **[grill-with-docs](./skills/engineering/grill-with-docs/SKILL.md)** ——通过现有领域模型检验你的计划，精炼术语，并内联更新 `CONTEXT.md` 和架构决策记录（ADR）。
- **[triage](./skills/engineering/triage/SKILL.md)** — Triage issues through a state machine of triage roles.
  - **[triage](./skills/engineering/triage/SKILL.md)** ——通过分诊角色状态机进行问题分类。
- **[improve-codebase-architecture](./skills/engineering/improve-codebase-architecture/SKILL.md)** — Find deepening opportunities in a codebase, informed by the domain language in `CONTEXT.md` and the decisions in `docs/adr/`.
  - **[improve-codebase-architecture](./skills/engineering/improve-codebase-architecture/SKILL.md)** ——在代码库中寻找深化机会，参考 `CONTEXT.md` 中的领域语言和 `docs/adr/` 中的决策。
- **[setup-matt-pocock-skills](./skills/engineering/setup-matt-pocock-skills/SKILL.md)** — Scaffold the per-repo config (issue tracker, triage label vocabulary, domain doc layout) that the other engineering skills consume. Run once per repo before using `to-issues`, `to-prd`, `triage`, `diagnose`, `tdd`, `improve-codebase-architecture`, or `zoom-out`.
  - **[setup-matt-pocock-skills](./skills/engineering/setup-matt-pocock-skills/SKILL.md)** ——生成每个仓库所需的配置脚手架（问题追踪器、分诊标签词库、领域文档布局），供其他工程类技能调用。在使用 `to-issues`、`to-prd`、`triage`、`diagnose`、`tdd`、`improve-codebase-architecture` 或 `zoom-out` 之前，每个仓库只需运行一次。
- **[tdd](./skills/engineering/tdd/SKILL.md)** — Test-driven development with a red-green-refactor loop. Builds features or fixes bugs one vertical slice at a time.
  - **[tdd](./skills/engineering/tdd/SKILL.md)** ——采用红-绿-重构循环的测试驱动开发。每次仅构建一个功能或修复一个 Bug（垂直切片）。
- **[to-issues](./skills/engineering/to-issues/SKILL.md)** — Break any plan, spec, or PRD into independently-grabbable GitHub issues using vertical slices.
  - **[to-issues](./skills/engineering/to-issues/SKILL.md)** ——使用垂直切片将任何计划、规范或 PRD 拆分为可独立领取的 GitHub Issue。
- **[to-prd](./skills/engineering/to-prd/SKILL.md)** — Turn the current conversation context into a PRD and submit it as a GitHub issue. No interview — just synthesizes what you've already discussed.
  - **[to-prd](./skills/engineering/to-prd/SKILL.md)** ——将当前对话上下文转化为 PRD 并提交为 GitHub Issue。无需面试——仅综合你已讨论的内容。
- **[zoom-out](./skills/engineering/zoom-out/SKILL.md)** — Tell the agent to zoom out and give broader context or a higher-level perspective on an unfamiliar section of code.
  - **[zoom-out](./skills/engineering/zoom-out/SKILL.md)** ——指示 Agent 拉远视角，为不熟悉的代码段提供更广泛的上下文或更高层面的观点。
- **[prototype](./skills/engineering/prototype/SKILL.md)** — Build a throwaway prototype to flesh out a design — either a runnable terminal app for state/business-logic questions, or several radically different UI variations toggleable from one route.
  - **[prototype](./skills/engineering/prototype/SKILL.md)** ——构建一次性原型以完善设计——可以是用于状态/业务逻辑问题的可运行终端应用，也可以是可从单一路由切换的多种截然不同的 UI 变体。

### Productivity / 效率类（Productivity）

General workflow tools, not code-specific.
通用工作流工具，不局限于代码场景。

- **[caveman](./skills/productivity/caveman/SKILL.md)** — Ultra-compressed communication mode. Cuts token usage ~75% by dropping filler while keeping full technical accuracy.
  - **[caveman](./skills/productivity/caveman/SKILL.md)** ——超压缩通信模式。通过去除冗余填充词，在保持完整技术准确性的同时将 Token 消耗降低约 75%。
- **[grill-me](./skills/productivity/grill-me/SKILL.md)** — Get relentlessly interviewed about a plan or design until every branch of the decision tree is resolved.
  - **[grill-me](./skills/productivity/grill-me/SKILL.md)** ——对计划或设计进行不间断的拷问，直到决策树的每个分支都得到解决。
- **[handoff](./skills/productivity/handoff/SKILL.md)** — Compact the current conversation into a handoff document so another agent can continue the work.
  - **[handoff](./skills/productivity/handoff/SKILL.md)** ——将当前对话压缩为交接文档，以便另一个 Agent 继续工作。
- **[write-a-skill](./skills/productivity/write-a-skill/SKILL.md)** — Create new skills with proper structure, progressive disclosure, and bundled resources.
  - **[write-a-skill](./skills/productivity/write-a-skill/SKILL.md)** ——创建具有合理结构、渐进式披露和捆绑资源的新技能。

### Misc / 其他（Misc）

Tools I keep around but rarely use.
我保留但很少使用的工具。

- **[git-guardrails-claude-code](./skills/misc/git-guardrails-claude-code/SKILL.md)** — Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, etc.) before they execute.
  - **[git-guardrails-claude-code](./skills/misc/git-guardrails-claude-code/SKILL.md)** ——设置 Claude Code 钩子，在 `push`、`reset --hard`、`clean` 等危险 Git 命令执行前进行拦截。
- **[migrate-to-shoehorn](./skills/misc/migrate-to-shoehorn/SKILL.md)** — Migrate test files from `as` type assertions to @total-typescript/shoehorn.
  - **[migrate-to-shoehorn](./skills/misc/migrate-to-shoehorn/SKILL.md)** ——将测试文件中的 `as` 类型断言迁移至 @total-typescript/shoehorn。
- **[scaffold-exercises](./skills/misc/scaffold-exercises/SKILL.md)** — Create exercise directory structures with sections, problems, solutions, and explainers.
  - **[scaffold-exercises](./skills/misc/scaffold-exercises/SKILL.md)** ——创建包含章节、问题、解决方案和解析说明的练习目录结构。
- **[setup-pre-commit](./skills/misc/setup-pre-commit/SKILL.md)** — Set up Husky pre-commit hooks with lint-staged, Prettier, type checking, and tests.
  - **[setup-pre-commit](./skills/misc/setup-pre-commit/SKILL.md)** ——配置包含 lint-staged、Prettier、类型检查和测试的 Husky 预提交钩子。