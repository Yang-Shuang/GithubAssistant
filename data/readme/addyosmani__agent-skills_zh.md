# Agent Skills（代理技能）

**面向 AI 编程代理的生产级工程技能。**

技能（Skills）封装了高级工程师在构建软件时所使用的标准工作流、质量门禁和最佳实践。本套件经过打包，确保 AI 代理能在开发的每个阶段一致地遵循这些规范。

![Addy's Agent Skills](https://addyosmani.com/assets/images/addys-agent-skills.jpg)

---

## Commands（命令）

7 个斜杠命令对应开发生命周期。每个命令都会自动激活相应的技能。

| What you're doing | Command | Key principle |
|-------------------|---------|---------------|
| Define what to build | `/spec` | Spec before code（先写规格说明，再写代码） |
| Plan how to build it | `/plan` | Small, atomic tasks（小型、原子化任务） |
| Build incrementally | `/build` | One slice at a time（每次只处理一个切片） |
| Prove it works | `/test` | Tests are proof（测试即证明） |
| Review before merge | `/review` | Improve code health（提升代码健康度） |
| Simplify the code | `/code-simplify` | Clarity over cleverness（清晰优于炫技） |
| Ship to production | `/ship` | Faster is safer（快即是稳） |

技能也会根据你的操作自动激活——设计 API 会触发 `api-and-interface-design`，构建 UI 会触发 `frontend-ui-engineering`，依此类推。

---

## Quick Start（快速开始）

<details>
<summary><b>Claude Code (recommended)</b></summary>

**Marketplace install:**

```
/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@addy-agent-skills
```

> **SSH errors?** The marketplace clones repos via SSH. If you don't have SSH keys set up on GitHub, either [add your SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) or use the full HTTPS URL to force the HTTPS cloning:
> ```bash
> /plugin marketplace add https://github.com/addyosmani/agent-skills.git
> /plugin install agent-skills@addy-agent-skills
> ```

**Local / development:**

```bash
git clone https://github.com/addyosmani/agent-skills.git
claude --plugin-dir /path/to/agent-skills
```

</details>

<details>
<summary><b>Cursor</b></summary>

将任意 `SKILL.md` 文件复制到 `.cursor/rules/` 目录，或直接引用完整的 `skills/` 目录。详见 [docs/cursor-setup.md](docs/cursor-setup.md)。

</details>

<details>
<summary><b>Gemini CLI</b></summary>

将其安装为原生技能以实现自动发现，或添加到 `GEMINI.md` 中以保留持久上下文。详见 [docs/gemini-cli-setup.md](docs/gemini-cli-setup.md)。

**Install from the repo:**

```bash
gemini skills install https://github.com/addyosmani/agent-skills.git --path skills
```

**Install from a local clone:**

```bash
gemini skills install ./agent-skills/skills/
```

</details>

<details>
<summary><b>Windsurf</b></summary>

将技能内容添加到你的 Windsurf 规则配置中。详见 [docs/windsurf-setup.md](docs/windsurf-setup.md)。

</details>

<details>
<summary><b>OpenCode</b></summary>

通过 `AGENTS.md` 和 `skill` 工具实现代理驱动的技能执行。

详见 [docs/opencode-setup.md](docs/opencode-setup.md)。

</details>

<details>
<summary><b>GitHub Copilot</b></summary>

使用 `agents/` 目录中的代理定义作为 Copilot 角色（personas），并将技能内容放入 `.github/copilot-instructions.md`。详见 [docs/copilot-setup.md](docs/copilot-setup.md)。

</details>

<details>
  <summary><b>Kiro IDE & CLI </b></summary>
  Kiro 的技能位于 `.kiro/skills/` 目录下，可存储在项目级或全局级。Kiro 也支持 Agents.md。详见 Kiro 文档：https://kiro.dev/docs/skills/
</details>

<details>
<summary><b>Codex / Other Agents</b></summary>

技能使用纯 Markdown 格式——任何接受系统提示词或指令文件的代理均可使用。详见 [docs/getting-started.md](docs/getting-started.md)。

</details>



---

## All 23 Skills（全部 23 项技能）

上述命令仅为入口。本套件共包含 23 项技能——22 项生命周期技能加上 1 项元技能（meta-skill）`using-agent-skills`。每项技能均为结构化工作流，包含步骤、验证门禁和反合理化表格。你也可以直接引用任意技能。

### Meta - Discover which skill applies（元技能 - 匹配适用技能）

| Skill | What It Does | Use When |
|-------|-------------|----------|
| [using-agent-skills](skills/using-agent-skills/SKILL.md) | Maps incoming work to the right skill workflow and defines shared operating rules | Starting a session or deciding which skill applies（开始会话时，或需要决定使用哪项技能时） |

### Define - Clarify what to build（定义 - 明确构建目标）

| Skill | What It Does | Use When |
|-------|-------------|----------|
| [interview-me](skills/interview-me/SKILL.md) | One-question-at-a-time interview that extracts what the user actually wants instead of what they think they should want, until ~95% confidence | The ask is underspecified, or the user invokes "interview me" / "grill me"（需求描述模糊，或用户主动调用“interview me”/“grill me”时） |
| [idea-refine](skills/idea-refine/SKILL.md) | Structured divergent/convergent thinking to turn vague ideas into concrete proposals | You have a rough concept that needs exploration（拥有一个需要探索的粗略概念时） |
| [spec-driven-development](skills/spec-driven-development/SKILL.md) | Write a PRD covering objectives, commands, structure, code style, testing, and boundaries before any code | Starting a new project, feature, or significant change（启动新项目、新功能或重大变更时） |

### Plan - Break it down（规划 - 任务拆解）

| Skill | What It Does | Use When |
|-------|-------------|----------|
| [planning-and-task-breakdown](skills/planning-and-task-breakdown/SKILL.md) | Decompose specs into small, verifiable tasks with acceptance criteria and dependency ordering | You have a spec and need implementable units（已有规格说明，需要将其转化为可执行单元时） |

### Build - Write the code（构建 - 编写代码）

| Skill | What It Does | Use When |
|-------|-------------|----------|
| [incremental-implementation](skills/incremental-implementation/SKILL.md) | Thin vertical slices - implement, test, verify, commit. Feature flags, safe defaults, rollback-friendly changes | Any change touching more than one file（任何涉及多个文件的代码修改时） |
| [test-driven-development](skills/test-driven-development/SKILL.md) | Red-Green-Refactor, test pyramid (80/15/5), test sizes, DAMP over DRY, Beyonce Rule, browser testing | Implementing logic, fixing bugs, or changing behavior（实现业务逻辑、修复 Bug 或更改行为时） |
| [context-engineering](skills/context-engineering/SKILL.md) | Feed agents the right information at the right time - rules files, context packing, MCP integrations | Starting a session, switching tasks, or when output quality drops（开始会话、切换任务，或输出质量下降时） |
| [source-driven-development](skills/source-driven-development/SKILL.md) | Ground every framework decision in official documentation - verify, cite sources, flag what's unverified | You want authoritative, source-cited code for any framework or library（需要任何框架或库的权威且带引用的代码时） |
| [doubt-driven-development](skills/doubt-driven-development/SKILL.md) | Adversarial fresh-context review of every non-trivial decision in-flight - CLAIM → EXTRACT → DOUBT → RECONCILE → STOP, with optional user-authorized cross-model escalation | Stakes are high (production, security, irreversible), working in unfamiliar code, or a confident output is cheaper to verify now than to debug later（涉及高风险场景、处理陌生代码，或当前验证比后续调试成本更低时） |
| [frontend-ui-engineering](skills/frontend-ui-engineering/SKILL.md) | Component architecture, design systems, state management, responsive design, WCAG 2.1 AA accessibility | Building or modifying user-facing interfaces（构建或修改面向用户的界面时） |
| [api-and-interface-design](skills/api-and-interface-design/SKILL.md) | Contract-first design, Hyrum's Law, One-Version Rule, error semantics, boundary validation | Designing APIs, module boundaries, or public interfaces（设计 API、模块边界或公开接口时） |

### Verify - Prove it works（验证 - 证明功能正常）

| Skill | What It Does | Use When |
|-------|-------------|----------|
| [browser-testing-with-devtools](skills/browser-testing-with-devtools/SKILL.md) | Chrome DevTools MCP for live runtime data - DOM inspection, console logs, network traces, performance profiling | Building or debugging anything that runs in a browser（构建或调试任何浏览器端运行的内容时） |
| [debugging-and-error-recovery](skills/debugging-and-error-recovery/SKILL.md) | Five-step triage: reproduce, localize, reduce, fix, guard. Stop-the-line rule, safe fallbacks | Tests fail, builds break, or behavior is unexpected（测试失败、构建中断或行为不符合预期时） |

### Review - Quality gates before merge（审查 - 合并前的质量门禁）

| Skill | What It Does | Use When |
|-------|-------------|----------|
| [code-review-and-quality](skills/code-review-and-quality/SKILL.md) | Five-axis review, change sizing (~100 lines), severity labels (Nit/Optional/FYI), review speed norms, splitting strategies | Before merging any change（合并任何代码变更前） |
| [code-simplification](skills/code-simplification/SKILL.md) | Chesterton's Fence, Rule of 500, reduce complexity while preserving exact behavior | Code works but is harder to read or maintain than it should be（代码能正常运行，但可读性或可维护性低于预期时） |
| [security-and-hardening](skills/security-and-hardening/SKILL.md) | OWASP Top 10 prevention, auth patterns, secrets management, dependency auditing, three-tier boundary system | Handling user input, auth, data storage, or external integrations（处理用户输入、身份验证、数据存储或外部集成时） |
| [performance-optimization](skills/performance-optimization/SKILL.md) | Measure-first approach - Core Web Vitals targets, profiling workflows, bundle analysis, anti-pattern detection | Performance requirements exist or you suspect regressions（存在性能要求，或怀疑出现性能回退时） |

### Ship - Deploy with confidence（交付 - 自信部署）

| Skill | What It Does | Use When |
|-------|-------------|----------|
| [git-workflow-and-versioning](skills/git-workflow-and-versioning/SKILL.md) | Trunk-based development, atomic commits, change sizing (~100 lines), the commit-as-save-point pattern | Making any code change (always)（进行任何代码修改时，始终适用） |
| [ci-cd-and-automation](skills/ci-cd-and-automation/SKILL.md) | Shift Left, Faster is Safer, feature flags, quality gate pipelines, failure feedback loops | Setting up or modifying build and deploy pipelines（搭建或修改构建与部署流水线时） |
| [deprecation-and-migration](skills/deprecation-and-migration/SKILL.md) | Code-as-liability mindset, compulsory vs advisory deprecation, migration patterns, zombie code removal | Removing old systems, migrating users, or sunsetting features（移除旧系统、迁移用户或下线功能时） |
| [documentation-and-adrs](skills/documentation-and-adrs/SKILL.md) | Architecture Decision Records, API docs, inline documentation standards - document the *why* | Making architectural decisions, changing APIs, or shipping features（做出架构决策、修改 API 或交付功能时） |
| [shipping-and-launch](skills/shipping-and-launch/SKILL.md) | Pre-launch checklists, feature flag lifecycle, staged rollouts, rollback procedures, monitoring setup | Preparing to deploy to production（准备部署至生产环境时） |

---

## Agent Personas（代理角色）

预配置的专家级角色，用于针对性审查：

| Agent | Role | Perspective |
|-------|------|-------------|
| [code-reviewer](agents/code-reviewer.md) | Senior Staff Engineer | Five-axis code review with "would a staff engineer approve this?" standard（五维度代码审查，标准：“首席工程师会批准此代码吗？”） |
| [test-engineer](agents/test-engineer.md) | QA Specialist | Test strategy, coverage analysis, and the Prove-It pattern（测试策略、覆盖率分析及“证明它”模式） |
| [security-auditor](agents/security-auditor.md) | Security Engineer | Vulnerability detection, threat modeling, OWASP assessment（漏洞检测、威胁建模及 OWASP 评估） |

---

## Reference Checklists（参考清单）

技能按需调用的快速参考资料：

| Reference | Covers |
|-----------|--------|
| [testing-patterns.md](references/testing-patterns.md) | Test structure, naming, mocking, React/API/E2E examples, anti-patterns（测试结构、命名规范、Mock 技巧、React/API/E2E 示例及反模式） |
| [security-checklist.md](references/security-checklist.md) | Pre-commit checks, auth, input validation, headers, CORS, OWASP Top 10（提交前检查、身份验证、输入校验、请求头配置、CORS 策略及 OWASP Top 10） |
| [performance-checklist.md](references/performance-checklist.md) | Core Web Vitals targets, frontend/backend checklists, measurement commands（Core Web Vitals 目标指标、前后端检查清单及测量命令） |
| [accessibility-checklist.md](references/accessibility-checklist.md) | Keyboard nav, screen readers, visual design, ARIA, testing tools（键盘导航、屏幕阅读器支持、视觉设计、ARIA 属性及测试工具） |

---

## How Skills Work（技能工作原理）

每项技能均遵循统一的结构规范：

```
┌─────────────────────────────────────────────────┐
│  SKILL.md                                       │
│                                                 │
│  ┌─ Frontmatter ─────────────────────────────┐  │
│  │ name: lowercase-hyphen-name               │  │
│  │ description: Guides agents through [task].│  │
│  │              Use when…                    │  │
│  └───────────────────────────────────────────┘  │                                                                                                
│  Overview         → What this skill does        │
│  When to Use      → Triggering conditions       │
│  Process          → Step-by-step workflow       │
│  Rationalizations → Excuses + rebuttals         │
│  Red Flags        → Signs something's wrong     │
│  Verification     → Evidence requirements       │
└─────────────────────────────────────────────────┘
```

**核心设计原则：**

- **重流程，轻文本。** 技能是代理需遵循的工作流，而非供其阅读的参考文档。每项技能均包含步骤、检查点与退出标准。
- **防合理化（Anti-rationalization）。** 每项技能均附带一张常见借口表，列出代理常用来跳过步骤的理由（如“我稍后再加测试”），并提供有据可查的反驳论点。
- **验证不可妥协。** 每项技能末尾均明确证据要求——测试通过、构建输出或运行时数据。“看起来没问题”永远不够。
- **渐进式披露（Progressive disclosure）。** `SKILL.md` 作为入口，辅助参考资料仅在需要时加载，以最小化 Token 消耗。

---

## Project Structure（项目结构）

```
agent-skills/
├── skills/                            # 23 skills (22 lifecycle + 1 meta)
│   ├── interview-me/                  #   Define
│   ├── idea-refine/                   #   Define
│   ├── spec-driven-development/       #   Define
│   ├── planning-and-task-breakdown/   #   Plan
│   ├── incremental-implementation/    #   Build
│   ├── context-engineering/           #   Build
│   ├── source-driven-development/     #   Build
│   ├── doubt-driven-development/      #   Build
│   ├── frontend-ui-engineering/       #   Build
│   ├── test-driven-development/       #   Build
│   ├── api-and-interface-design/      #   Build
│   ├── browser-testing-with-devtools/ #   Verify
│   ├── debugging-and-error-recovery/  #   Verify
│   ├── code-review-and-quality/       #   Review
│   ├── code-simplification/          #   Review
│   ├── security-and-hardening/        #   Review
│   ├── performance-optimization/      #   Review
│   ├── git-workflow-and-versioning/   #   Ship
│   ├── ci-cd-and-automation/          #   Ship
│   ├── deprecation-and-migration/     #   Ship
│   ├── documentation-and-adrs/        #   Ship
│   ├── shipping-and-launch/           #   Ship
│   └── using-agent-skills/            #   Meta: how to use this pack
├── agents/                            # 3 specialist personas
├── references/                        # 4 supplementary checklists
├── hooks/                             # Session lifecycle hooks
├── .claude/commands/                  # 7 slash commands (Claude Code)
├── .gemini/commands/                  # 7 slash commands (Gemini CLI)
└── docs/                              # Setup guides per tool
```

---

## Why Agent Skills?（为什么需要 Agent Skills？）

AI 编程代理默认倾向于选择最短路径——这通常意味着跳过规格说明、测试、安全审查，以及那些确保软件可靠性的工程实践。Agent Skills 为代理提供了结构化工作流，强制其遵循高级工程师在生产级代码中一贯坚持的工程纪律。

每项技能都凝结了宝贵的工程判断力：*何时*编写规格说明、*测试什么*、*如何审查*以及*何时交付*。这些并非通用提示词，而是那种带有明确主张、以流程驱动的工作流，正是它们区分了生产级代码与原型级代码。

技能内嵌了 Google 工程文化的最佳实践——包括 [Software Engineering at Google](https://abseil.io/resources/swe-book) 与 Google [engineering practices guide](https://google.github.io/eng-practices/) 中的核心概念。你将在 API 设计中看到 Hyrum 定律，在测试环节发现 Beyonce 规则与测试金字塔，在代码审查中应用变更规模控制与审查速度规范，在简化流程中使用切斯特顿栅栏原则，在 Git 工作流中采用主干开发模式，在 CI/CD 中实践左移测试与功能开关，以及通过专门的废弃技能将代码视为负债。这些并非抽象理论——它们已直接嵌入代理遵循的逐步工作流中。

---

## Contributing（贡献指南）

技能应保持：**具体（specific）**（提供可执行步骤，而非模糊建议）、**可验证（verifiable）**（明确的退出标准与证据要求）、**经实战检验（battle-tested）**（基于真实工作流）以及**精简（minimal）**（仅保留引导代理所需的必要内容）。

格式规范详见 [docs/skill-anatomy.md](docs/skill-anatomy.md)，贡献指南详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## License（许可证）

MIT 协议——欢迎在你的项目、团队和工具中自由使用这些技能。