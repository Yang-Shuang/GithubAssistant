# claude-code最佳实践
从氛围编程到智能体工程 —— 实践让 Claude 更完美

![updated with Claude Code](https://img.shields.io/badge/updated_with_Claude_Code-v2.1.161%20(Jun%2003%2C%202026%209%3A47%20AM%20PKT)-white?style=flat&labelColor=555) <a href="https://github.com/shanraisshan/claude-code-best-practice/stargazers"><img src="https://img.shields.io/github/stars/shanraisshan/claude-code-best-practice?style=flat&label=%E2%98%85&labelColor=555&color=white" alt="GitHub Stars"></a><br>

[![Best Practice](!/tags/best-practice.svg)](best-practice/) [![Implemented](!/tags/implemented.svg)](implementation/) [![Orchestration Workflow](!/tags/orchestration-workflow.svg)](orchestration-workflow/orchestration-workflow.md) [![Claude](!/tags/claude.svg)](https://code.claude.com/docs) [![Boris](!/tags/boris-cherny.svg)](#-tips-and-tricks) [![Community](!/tags/community.svg)](#-subscribe) ![Click on these badges below to see the actual sources](!/tags/click-badges.svg)<br>
<img src="!/tags/a.svg" height="14"> = 代理 (Agents) · <img src="!/tags/c.svg" height="14"> = 命令 (Commands) · <img src="!/tags/s.svg" height="14"> = 技能 (Skills)

<p align="center">
  <img src="!/claude-jumping.svg" alt="Claude Code mascot jumping" width="120" height="100"><br>
  <a href="https://github.com/trending"><img src="!/root/github-trending-day.svg" alt="GitHub Trending #1 Repository Of The Day"></a>
</p>

<p align="center">
  <img src="!/root/boris-slider.gif" alt="Boris Cherny on Claude Code" width="600"><br>
  Boris Cherny 在 X (<a href="https://x.com/bcherny/status/2007179832300581177">推文 1</a> · <a href="https://x.com/bcherny/status/2017742741636321619">推文 2</a> · <a href="https://x.com/bcherny/status/2021699851499798911">推文 3</a>)
</p>

> [!TIP]
> 访问 [**如何使用 (How to Use)**](#how-to-use) 部分以充分利用本仓库。

## 🧠 概念 (CONCEPTS)

| 特性 | 位置 | 描述 |
|---------|----------|-------------|
| <img src="!/tags/a.svg" height="14"> [**子代理 (Subagents)**](https://code.claude.com/docs/en/sub-agents) | `.claude/agents/<name>.md` | [![Best Practice](!/tags/best-practice.svg)](best-practice/claude-subagents.md) [![Implemented](!/tags/implemented.svg)](implementation/claude-subagents-implementation.md) |
| <img src="!/tags/c.svg" height="14"> [**命令 (Commands)**](https://code.claude.com/docs/en/slash-commands) | `.claude/commands/<name>.md` | [![Best Practice](!/tags/best-practice.svg)](best-practice/claude-commands.md) [![Implemented](!/tags/implemented.svg)](implementation/claude-commands-implementation.md) |
| <img src="!/tags/s.svg" height="14"> [**技能 (Skills)**](https://code.claude.com/docs/en/skills) | `.claude/skills/<name>/SKILL.md` | [![Best Practice](!/tags/best-practice.svg)](best-practice/claude-skills.md) [![Implemented](!/tags/implemented.svg)](implementation/claude-skills-implementation.md) [官方技能](https://github.com/anthropics/skills/tree/main/skills) · [Monorepo 专用技能](reports/claude-skills-for-larger-mono-repos.md) |
| [**工作流 (Workflows)**](https://code.claude.com/docs/en/common-workflows) | [`.claude/commands/weather-orchestrator.md`](.claude/commands/weather-orchestrator.md) | [![Orchestration Workflow](!/tags/orchestration-workflow.svg)](orchestration-workflow/orchestration-workflow.md) |
| [**钩子 (Hooks)**](https://code.claude.com/docs/en/hooks) | `.claude/hooks/` | [![Best Practice](!/tags/best-practice.svg)](https://github.com/shanraisshan/claude-code-hooks) [![Implemented](!/tags/implemented.svg)](https://github.com/shanraisshan/claude-code-hooks) [指南](https://code.claude.com/docs/en/hooks-guide) |
| [**MCP 服务器 (MCP Servers)**](https://code.claude.com/docs/en/mcp) | `.claude/settings.json`, `.mcp.json` | [![Best Practice](!/tags/best-practice.svg)](best-practice/claude-mcp.md) [![Implemented](!/tags/implemented.svg)](.mcp.json) |
| [**插件 (Plugins)**](https://code.claude.com/docs/en/plugins) | 可分发包 | [市场](https://code.claude.com/docs/en/discover-plugins) · [创建市场](https://code.claude.com/docs/en/plugin-marketplaces) |
| [**设置 (Settings)**](https://code.claude.com/docs/en/settings) | `.claude/settings.json` | [![Best Practice](!/tags/best-practice.svg)](best-practice/claude-settings.md) [![Implemented](!/tags/implemented.svg)](.claude/settings.json) [权限 (Permissions)](https://code.claude.com/docs/en/permissions) · [模型配置](https://code.claude.com/docs/en/model-config) · [输出样式](https://code.claude.com/docs/en/output-styles) · [沙盒隔离](https://code.claude.com/docs/en/sandboxing) · [快捷键](https://code.claude.com/docs/en/keybindings) · [自动模式配置](https://code.claude.com/docs/en/auto-mode-config) |
| [**状态栏 (Status Line)**](https://code.claude.com/docs/en/statusline) | `.claude/settings.json` | [![Best Practice](!/tags/best-practice.svg)](https://github.com/shanraisshan/claude-code-status-line) [![Implemented](!/tags/implemented.svg)](.claude/settings.json) |
| [**记忆 (Memory)**](https://code.claude.com/docs/en/memory) | `CLAUDE.md`, `.claude/rules/`, `~/.claude/rules/`, `~/.claude/projects/<project>/memory/` | [![Best Practice](!/tags/best-practice.svg)](best-practice/claude-memory.md) [![Implemented](!/tags/implemented.svg)](CLAUDE.md) [自动记忆](https://code.claude.com/docs/en/memory) · [自动记忆深度解析](reports/claude-agent-memory.md) · [规则](https://code.claude.com/docs/en/memory#organize-rules-with-clauderules) |
| [**检查点机制 (Checkpointing)**](https://code.claude.com/docs/en/checkpointing) | 自动（文件编辑追踪） |  |
| [**CLI 启动参数 (CLI Startup Flags)**](https://code.claude.com/docs/en/cli-reference) | `claude [flags]` | [![Best Practice](!/tags/best-practice.svg)](best-practice/claude-cli-startup-flags.md) [交互模式](https://code.claude.com/docs/en/interactive-mode) · [环境变量 (Env Vars)](https://code.claude.com/docs/en/env-vars) |
| **AI 术语** | | [![Best Practice](!/tags/best-practice.svg)](https://github.com/shanraisshan/claude-code-codex-cursor-gemini/blob/main/reports/ai-terms.md) |
| [**最佳实践 (Best Practices)**](https://code.claude.com/docs/en/best-practices) | | [提示工程 (Prompt Engineering)](https://github.com/anthropics/prompt-eng-interactive-tutorial) · [扩展 Claude Code](https://code.claude.com/docs/en/features-overview) |

### 🔥 热门功能

| 特性 | 位置 | 描述 |
|---------|----------|-------------|
| [**Ultrareview (超审查)**](https://code.claude.com/docs/en/ultrareview) ![beta](!/tags/beta.svg) | `/code-review ultra`, `claude ultrareview [target]` | [任务追踪](https://code.claude.com/docs/en/ultrareview#track-a-running-review) |
| [**Devcontainers (开发容器)**](https://code.claude.com/docs/en/devcontainer) | `.devcontainer/` |  |
| [**Channels (频道)**](https://code.claude.com/docs/en/channels) ![beta](!/tags/beta.svg) | `--channels`, 基于插件 | [参考文档](https://code.claude.com/docs/en/channels-reference) |
| [**Ultraplan (超规划)**](https://code.claude.com/docs/en/ultraplan) ![beta](!/tags/beta.svg) | `/ultraplan` |  |
| [**无闪烁模式 (No Flicker Mode)**](https://code.claude.com/docs/en/fullscreen) ![beta](!/tags/beta.svg) | `/tui fullscreen`, `CLAUDE_CODE_NO_FLICKER=1` | [![Best Practice](!/tags/best-practice.svg)](https://x.com/bcherny/status/2039421575422980329) |
| [**自动模式 (Auto Mode)**](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode) ![beta](!/tags/beta.svg) | `--permission-mode auto`, `Shift+Tab` | [![Best Practice](!/tags/best-practice.svg)](https://x.com/claudeai/status/2036503582166393240) [博客](https://claude.com/blog/auto-mode) |
| [**Power-ups (增强功能)**](best-practice/claude-power-ups.md) | `/powerup` | [![Best Practice](!/tags/best-practice.svg)](best-practice/claude-power-ups.md) |
| [**快速模式 (Fast Mode)**](https://code.claude.com/docs/en/fast-mode) ![beta](!/tags/beta.svg) | `/fast`, `"fastMode": true` |  |
| [**Computer Use (电脑使用)**](https://code.claude.com/docs/en/computer-use) ![beta](!/tags/beta.svg) | `computer-use` MCP server | [桌面端](https://code.claude.com/docs/en/desktop#let-claude-use-your-computer) |
| [**Agent SDK**](https://code.claude.com/docs/en/agent-sdk/overview) | `npm` / `pip` package | [快速入门](https://code.claude.com/docs/en/agent-sdk/quickstart) · [示例](https://github.com/anthropics/claude-agent-sdk-demos) |
| [**Ralph Wiggum 循环**](https://github.com/anthropics/claude-code/tree/main/plugins/ralph-wiggum) | plugin | [![Best Practice](!/tags/best-practice.svg)](https://github.com/ghuntley/how-to-ralph-wiggum) [![Implemented](!/tags/implemented.svg)](https://github.com/shanraisshan/ralph-wiggum-self-evolving-loop) |
| [**Chrome (浏览器)**](https://code.claude.com/docs/en/chrome) ![beta](!/tags/beta.svg) | `--chrome`, extension | [![Best Practice](!/tags/best-practice.svg)](reports/claude-in-chrome-v-chrome-devtools-mcp.md) |
| [**Claude Code Web (网页版)**](https://code.claude.com/docs/en/claude-code-on-the-web) ![beta](!/tags/beta.svg) | `claude.ai/code` | [例程 (Routines)](https://code.claude.com/docs/en/routines) |
| [**Slack**](https://code.claude.com/docs/en/slack) | Slack 中的 `@Claude` |  |
| [**代码审查 (Code Review)**](https://code.claude.com/docs/en/code-review) ![beta](!/tags/beta.svg) | GitHub App (managed) | [![Best Practice](!/tags/best-practice.svg)](https://x.com/claudeai/status/2031088171262554195) [博客](https://claude.com/blog/code-review) [本地 /code-review](https://code.claude.com/docs/en/commands) |
| [**GitHub Actions**](https://code.claude.com/docs/en/github-actions) | `.github/workflows/` | [GitLab CI/CD](https://code.claude.com/docs/en/gitlab-ci-cd) |
| [**远程控制 (Remote Control)**](https://code.claude.com/docs/en/remote-control) | `/remote-control`, `/rc` | [![Best Practice](!/tags/best-practice.svg)](https://x.com/noahzweben/status/2032533699116355819) [无头模式 (Headless Mode)](https://code.claude.com/docs/en/headless) |
| [**深度链接 (Deep Links)**](https://code.claude.com/docs/en/deep-links) | `claude-cli://open?repo=…&q=…` |  |
| [**动态工作流 (Dynamic Workflows)**](https://code.claude.com/docs/en/workflows) ![beta](!/tags/beta.svg) | `/workflows`, `ultracode` keyword, `/effort ultracode`, `.claude/workflows/` | [深度研究 (Deep Research)](https://code.claude.com/docs/en/workflows#run-a-bundled-workflow) |
| [**代理团队 (Agent Teams)**](https://code.claude.com/docs/en/agent-teams) ![beta](!/tags/beta.svg) | 内置 (环境变量) | [![Best Practice](!/tags/best-practice.svg)](https://x.com/bcherny/status/2019472394696683904) [![Implemented](!/tags/implemented.svg)](implementation/claude-agent-teams-implementation.md) |
| [**代理视图 (Agent View)**](https://code.claude.com/docs/en/agent-view) ![beta](!/tags/beta.svg) | `claude agents`, `--bg`, `/bg` |  |
| [**定时任务 (Scheduled Tasks)**](https://code.claude.com/docs/en/scheduled-tasks) | `/loop`, `/schedule`, cron tools | [![Best Practice](!/tags/best-practice.svg)](https://x.com/bcherny/status/2030193932404150413) [![Implemented](!/tags/implemented.svg)](implementation/claude-scheduled-tasks-implementation.md) [桌面端定时任务](https://code.claude.com/docs/en/desktop-scheduled-tasks) · [公告](https://x.com/noahzweben/status/2036129220959805859) |
| [**例程 (Routines)**](https://code.claude.com/docs/en/routines) ![beta](!/tags/beta.svg) | `claude.ai/code/routines`, `/schedule` | [桌面端任务](https://code.claude.com/docs/en/desktop-scheduled-tasks) |
| [**Tasks (任务)**](reports/claude-global-vs-project-settings.md#tasks-system) | `/tasks`, `~/.claude/tasks/` | [![Best Practice](!/tags/best-practice.svg)](reports/claude-global-vs-project-settings.md) [Ultrareview 追踪](https://code.claude.com/docs/en/ultrareview#track-a-running-review) |
| [**目标 (Goal)**](https://code.claude.com/docs/en/goal) | `/goal <condition>`, `/goal clear` | [![Implemented](!/tags/implemented.svg)](implementation/claude-goal-implementation.md) |
| [**语音听写 (Voice Dictation)**](https://code.claude.com/docs/en/voice-dictation) ![beta](!/tags/beta.svg) | `/voice` | [![Best Practice](!/tags/best-practice.svg)](https://x.com/trq212/status/2028628570692890800) |
| [**内置技能 (Bundled Skills)**](https://code.claude.com/docs/en/skills#bundled-skills) | `/code-review`, `/batch` | [![Best Practice](!/tags/best-practice.svg)](https://x.com/bcherny/status/2027534984534544489) |
| [**Git Worktrees (工作树)**](https://code.claude.com/docs/en/worktrees) | `--worktree`/`-w`, `.worktreeinclude`, `EnterWorktree`/`ExitWorktree`, `isolation: "worktree"`, `WorktreeCreate`/`WorktreeRemove` hooks | [![Best Practice](!/tags/best-practice.svg)](https://x.com/bcherny/status/2025007393290272904) |

<p align="center">
  <img src="!/claude-jumping.svg" alt="section divider" width="60" height="50">
</p>

<a id="orchestration-workflow"></a>

## <a href="orchestration-workflow/orchestration-workflow.md"><img src="!/tags/orchestration-workflow-hd.svg" alt="Orchestration Workflow"></a>

查看 [orchestration-workflow](orchestration-workflow/orchestration-workflow.md) 以获取 <img src="!/tags/c.svg" height="14"> **命令** → <img src="!/tags/a.svg" height="14"> **代理 (Agent)** → <img src="!/tags/s.svg" height="14"> **技能** 模式的实现细节。

<p align="center">
  <img src="orchestration-workflow/orchestration-workflow.svg" alt="Command Skill Agent Architecture Flow" width="100%">
</p>

<p align="center">
  <img src="orchestration-workflow/orchestration-workflow.gif" alt="Orchestration Workflow Demo" width="600">
</p>

![How to Use](!/tags/how-to-use.svg)

```bash
claude
/weather-orchestrator
```

<p align="center">
  <img src="!/claude-jumping.svg" alt="section divider" width="60" height="50">
</p>

## ⚙️ 开发工作流 (DEVELOPMENT WORKFLOWS)

所有主要的工作流都收敛于相同的架构模式：**研究 → 计划 → 执行 → 审查 → 发布**

| 名称 | ★ | 工作流 | <img src="!/tags/a.svg" height="14"> | <img src="!/tags/c.svg" height="14"> | <img src="!/tags/s.svg" height="14"> |
|------|---|----------|---|---|---|
| [Superpowers](https://github.com/obra/superpowers) | 216k | <img src="https://img.shields.io/badge/brainstorming-ddf4ff" alt="brainstorming" align="middle"> → <img src="https://img.shields.io/badge/using--git--worktrees-ddf4ff" alt="using-git-worktrees" align="middle"> → <img src="https://img.shields.io/badge/writing--plans-ddf4ff" alt="writing-plans" align="middle"> → <img src="https://img.shields.io/badge/subagent--driven--development-ddf4ff" alt="subagent-driven-development" align="middle"> → <img src="https://img.shields.io/badge/implementer--subagent-fff3b0" alt="implementer-subagent" align="middle"> → <img src="https://img.shields.io/badge/spec--reviewer--subagent-fff3b0" alt="spec-reviewer-subagent" align="middle"> → <img src="https://img.shields.io/badge/code--quality--reviewer--subagent-fff3b0" alt="code-quality-reviewer-subagent" align="middle"> → <img src="https://img.shields.io/badge/test--driven--development-fff3b0" alt="test-driven-development" align="middle"> → <img src="https://img.shields.io/badge/requesting--code--review-ddf4ff" alt="requesting-code-review" align="middle"> → <img src="https://img.shields.io/badge/receiving--code--review-fff3b0" alt="receiving-code-review" align="middle"> → <img src="https://img.shields.io/badge/finishing--a--development--branch-ddf4ff" alt="finishing-a-development-branch" align="middle"> | 0 | 0 | 14 |
| [Everything Claude Code](https://github.com/affaan-m/everything-claude-code) | 204k | <img src="https://img.shields.io/badge/%2Fecc:plan-ddf4ff" alt="/ecc:plan" align="middle"> → <img src="https://img.shields.io/badge/%2Ftdd-ddf4ff" alt="/tdd" align="middle"> → <img src="https://img.shields.io/badge/%2Fcode--review-ddf4ff" alt="/code-review" align="middle"> → <img src="https://img.shields.io/badge/%2Fsecurity--scan-ddf4ff" alt="/security-scan" align="middle"> → <img src="https://img.shields.io/badge/%2Fe2e-ddf4ff" alt="/e2e" align="middle"> → <img src="https://img.shields.io/badge/merge-ddf4ff" alt="merge" align="middle"> | 63 | 121 | 300+ |
| [Matt Pocock Skills](https://github.com/mattpocock/skills) | 115k | <img src="https://img.shields.io/badge/%2Fgrill--me-ddf4ff" alt="/grill-me" align="middle"> → <img src="https://img.shields.io/badge/%2Fgrill--with--docs-ddf4ff" alt="/grill-with-docs" align="middle"> → <img src="https://img.shields.io/badge/%2Fto--prd-ddf4ff" alt="/to-prd" align="middle"> → <img src="https://img.shields.io/badge/%2Fto--issues-ddf4ff" alt="/to-issues" align="middle"> → <img src="https://img.shields.io/badge/%2Ftdd-ddf4ff" alt="/tdd" align="middle"> → <img src="https://img.shields.io/badge/%2Ftdd--red-fff3b0" alt="/tdd-red" align="middle"> → <img src="https://img.shields.io/badge/%2Ftdd--green-fff3b0" alt="/tdd-green" align="middle"> → <img src="https://img.shields.io/badge/%2Ftdd--refactor-fff3b0" alt="/tdd-refactor" align="middle"> → <img src="https://img.shields.io/badge/%2Fdiagnose-fff3b0" alt="/diagnose" align="middle"> → <img src="https://img.shields.io/badge/%2Fimprove--codebase--architecture-ddf4ff" alt="/improve-codebase-architecture" align="middle"> → <img src="https://img.shields.io/badge/%2Fhandoff-ddf4ff" alt="/handoff" align="middle"> | 0 | 0 | 28 |
| [Spec Kit](https://github.com/github/spec-kit) | 108k | <img src="https://img.shields.io/badge/%2Fspeckit.constitution-ddf4ff" alt="/speckit.constitution" align="middle"> → <img src="https://img.shields.io/badge/%2Fspeckit.specify-ddf4ff" alt="/speckit.specify" align="middle"> → <img src="https://img.shields.io/badge/%2Fspeckit.clarify-ddf4ff" alt="/speckit.clarify" align="middle"> → <img src="https://img.shields.io/badge/%2Fspeckit.plan-ddf4ff" alt="/speckit.plan" align="middle"> → <img src="https://img.shields.io/badge/%2Fspeckit.tasks-ddf4ff" alt="/speckit.tasks" align="middle"> → <img src="https://img.shields.io/badge/%2Fspeckit.taskstoissues-ddf4ff" alt="/speckit.taskstoissues" align="middle"> → <img src="https://img.shields.io/badge/%2Fspeckit.implement-ddf4ff" alt="/speckit.implement" align="middle"> → <img src="https://img.shields.io/badge/%2Fspeckit.analyze-ddf4ff" alt="/speckit.analyze" align="middle"> → <img src="https://img.shields.io/badge/%2Fspeckit.checklist-ddf4ff" alt="/speckit.checklist" align="middle"> | 0 | 9 | 0 |
| [gstack](https://github.com/garrytan/gstack) | 106k | <img src="https://img.shields.io/badge/%2Foffice--hours-ddf4ff" alt="/office-hours" align="middle"> → <img src="https://img.shields.io/badge/%2Fplan--ceo--review-ddf4ff" alt="/plan-ceo-review" align="middle"> → <img src="https://img.shields.io/badge/%2Fplan--eng--review-fff3b0" alt="/plan-eng-review" align="middle"> → <img src="https://img.shields.io/badge/%2Fplan--design--review-fff3b0" alt="/plan-design-review" align="middle"> → <img src="https://img.shields.io/badge/%2Fplan--devex--review-fff3b0" alt="/plan-devex-review" align="middle"> → <img src="https://img.shields.io/badge/%2Fspec-ddf4ff" alt="/spec" align="middle"> → <img src="https://img.shields.io/badge/%2Fdesign--consultation-fff3b0" alt="/design-consultation" align="middle"> → <img src="https://img.shields.io/badge/%2Freview-ddf4ff" alt="/review" align="middle"> → <img src="https://img.shields.io/badge/%2Fqa-ddf4ff" alt="/qa" align="middle"> → <img src="https://img.shields.io/badge/%2Fship-ddf4ff" alt="/ship" align="middle"> → <img src="https://img.shields.io/badge/%2Fland--and--deploy-ddf4ff" alt="/land-and-deploy" align="middle"> → <img src="https://img.shields.io/badge/%2Fcanary-ddf4ff" alt="/canary" align="middle"> → <img src="https://img.shields.io/badge/%2Fretro-ddf4ff" alt="/retro" align="middle"> | 0 | 0 | 61 |
| [Get Shit Done](https://github.com/gsd-build/get-shit-done) | 64k | <img src="https://img.shields.io/badge/%2Fgsd--new--project-ddf4ff" alt="/gsd-new-project" align="middle"> → <img src="https://img.shields.io/badge/%2Fgsd--spec--phase-ddf4ff" alt="/gsd-spec-phase" align="middle"> → <img src="https://img.shields.io/badge/%2Fgsd--plan--phase-ddf4ff" alt="/gsd-plan-phase" align="middle"> → <img src="https://img.shields.io/badge/%2Fgsd--execute--phase-ddf4ff" alt="/gsd-execute-phase" align="middle"> → <img src="https://img.shields.io/badge/%2Fgsd--code--review-fff3b0" alt="/gsd-code-review" align="middle"> → <img src="https://img.shields.io/badge/%2Fgsd--validate--phase-fff3b0" alt="/gsd-validate-phase" align="middle"> → <img src="https://img.shields.io/badge/%2Fgsd--ship-ddf4ff" alt="/gsd-ship" align="middle"> → <img src="https://img.shields.io/badge/%2Fgsd--extract--learnings-ddf4ff" alt="/gsd-extract-learnings" align="middle"> | 33 | 67 | 0 |
| [OpenSpec](https://github.com/Fission-AI/OpenSpec) | 52k | <img src="https://img.shields.io/badge/%2Fopsx:propose-ddf4ff" alt="/opsx:propose" align="middle"> → <img src="https://img.shields.io/badge/%2Fopsx:apply-fff3b0" alt="/opsx:apply" align="middle"> → <img src="https://img.shields.io/badge/%2Fopsx:verify-fff3b0" alt="/opsx:verify" align="middle"> → <img src="https://img.shields.io/badge/%2Fopsx:archive-ddf4ff" alt="/opsx:archive" align="middle"> → <img src="https://img.shields.io/badge/%2Fopsx:bulk--archive-ddf4ff" alt="/opsx:bulk-archive" align="middle"> | 0 | 9 | 0 |
| [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | 49k | <img src="https://img.shields.io/badge/bmad--product--brief-ddf4ff" alt="bmad-product-brief" align="middle"> → <img src="https://img.shields.io/badge/bmad--prfaq-fff3b0" alt="bmad-prfaq" align="middle"> → <img src="https://img.shields.io/badge/bmad--create--prd-ddf4ff" alt="bmad-create-prd" align="middle"> → <img src="https://img.shields.io/badge/bmad--validate--prd-fff3b0" alt="bmad-validate-prd" align="middle"> → <img src="https://img.shields.io/badge/bmad--create--architecture-ddf4ff" alt="bmad-create-architecture" align="middle"> → <img src="https://img.shields.io/badge/bmad--check--implementation--readiness-ddf4ff" alt="bmad-check-implementation-readiness" align="middle"> → <img src="https://img.shields.io/badge/bmad--create--epics--and--stories-ddf4ff" alt="bmad-create-epics-and-stories" align="middle"> → <img src="https://img.shields.io/badge/bmad--dev--story-fff3b0" alt="bmad-dev-story" align="middle"> → <img src="https://img.shields.io/badge/bmad--code--review-fff3b0" alt="bmad-code-review" align="middle"> → <img src="https://img.shields.io/badge/bmad--qa--generate--e2e--tests-ddf4ff" alt="bmad-qa-generate-e2e-tests" align="middle"> → <img src="https://img.shields.io/badge/bmad--retrospective-ddf4ff" alt="bmad-retrospective" align="middle"> | 6 | 0 | 42 |
| [oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | 36k | <img src="https://img.shields.io/badge/team--plan-ddf4ff" alt="team-plan" align="middle"> → <img src="https://img.shields.io/badge/team--prd-ddf4ff" alt="team-prd" align="middle"> → <img src="https://img.shields.io/badge/team--exec-ddf4ff" alt="team-exec" align="middle"> → <img src="https://img.shields.io/badge/team--verify-ddf4ff" alt="team-verify" align="middle"> → <img src="https://img.shields.io/badge/team--fix-fff3b0" alt="team-fix" align="middle"> → <img src="https://img.shields.io/badge/team--verify-fff3b0" alt="team-verify" align="middle"> | 19 | 0 | 39 |
| [agent-skills](https://github.com/addyosmani/agent-skills) | 27k | <img src="https://img.shields.io/badge/%2Fspec-ddf4ff" alt="/spec" align="middle"> → <img src="https://img.shields.io/badge/%2Fplan-ddf4ff" alt="/plan" align="middle"> → <img src="https://img.shields.io/badge/%2Fbuild-ddf4ff" alt="/build" align="middle"> → <img src="https://img.shields.io/badge/%2Ftest-ddf4ff" alt="/test" align="middle"> → <img src="https://img.shields.io/badge/%2Freview-ddf4ff" alt="/review" align="middle"> → <img src="https://img.shields.io/badge/%2Fship-ddf4ff" alt="/ship" align="middle"> | 3 | 7 | 21 |
| [Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin) | 19k | <img src="https://img.shields.io/badge/%2Fce--strategy-ddf4ff" alt="/ce-strategy" align="middle"> → <img src="https://img.shields.io/badge/%2Fce--brainstorm-ddf4ff" alt="/ce-brainstorm" align="middle"> → <img src="https://img.shields.io/badge/%2Fce--ideate-fff3b0" alt="/ce-ideate" align="middle"> → <img src="https://img.shields.io/badge/%2Fce--plan-ddf4ff" alt="/ce-plan" align="middle"> → <img src="https://img.shields.io/badge/%2Fce--work-ddf4ff" alt="/ce-work" align="middle"> → <img src="https://img.shields.io/badge/%2Fce--debug-fff3b0" alt="/ce-debug" align="middle"> → <img src="https://img.shields.io/badge/%2Fce--code--review-ddf4ff" alt="/ce-code-review" align="middle"> → <img src="https://img.shields.io/badge/%2Fce--compound-ddf4ff" alt="/ce-compound" align="middle"> → <img src="https://img.shields.io/badge/%2Fce--update-fff3b0" alt="/ce-update" align="middle"> → <img src="https://img.shields.io/badge/%2Fce--release--notes-ddf4ff" alt="/ce-release-notes" align="middle"> | 47 | 4 | 39 |
| [HumanLayer](https://github.com/humanlayer/humanlayer) | 11k | <img src="https://img.shields.io/badge/%2Fresearch__codebase-ddf4ff" alt="/research_codebase" align="middle"> → <img src="https://img.shields.io/badge/%2Fcreate__plan-ddf4ff" alt="/create_plan" align="middle"> → <img src="https://img.shields.io/badge/%2Fvalidate__plan-fff3b0" alt="/validate_plan" align="middle"> → <img src="https://img.shields.io/badge/%2Fiterate__plan-fff3b0" alt="/iterate_plan" align="middle"> → <img src="https://img.shields.io/badge/%2Fimplement__plan-ddf4ff" alt="/implement_plan" align="middle"> → <img src="https://img.shields.io/badge/%2Flocal__review-ddf4ff" alt="/local_review" align="middle"> → <img src="https://img.shields.io/badge/%2Fcreate__handoff-ddf4ff" alt="/create_handoff" align="middle"> → <img src="https://img.shields.io/badge/%2Fcommit-ddf4ff" alt="/commit" align="middle"> → <img src="https://img.shields.io/badge/%2Fdescribe__pr-ddf4ff" alt="/describe_pr" align="middle"> | 6 | 27 | 0 |

> *注意：黄色标签表示子循环 —— 在父步骤内部重复的步骤（例如，每个任务、每个故事或直到验证条件通过）。*

### 其他
- [RPI](development-workflows/rpi/rpi-workflow.md) [![Implemented](!/tags/implemented.svg)](development-workflows/rpi/rpi-workflow.md)
- [Ralph Wiggum Loop](https://www.youtube.com/watch?v=eAtvoGlpeRU) [![Implemented](!/tags/implemented.svg)](https://github.com/shanraisshan/ralph-wiggum-self-evolving-loop)
- [Andrej Karpathy (OpenAI 创始成员) 工作流](https://x.com/karpathy/status/2015883857489522876)
- [Peter Steinberger (OpenClaw 创建者) 工作流](https://youtu.be/8lF7HmQ_RgY?t=2582)
- Boris Cherny (Claude Code 创建者) 工作流 — [13 个技巧](tips/claude-boris-13-tips-03-jan-26.md) · [10 个技巧](tips/claude-boris-10-tips-01-feb-26.md) · [12 个技巧](tips/claude-boris-12-tips-12-feb-26.md) · [2 个技巧](tips/claude-boris-2-tips-25-mar-26.md) · [15 个技巧](tips/claude-boris-15-tips-30-mar-26.md) · [6 个技巧](tips/claude-boris-6-tips-16-apr-26.md) [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny)
- Thariq (Anthropic) 工作流 — [技能](tips/claude-thariq-tips-17-mar-26.md) · [会话管理](tips/claude-thariq-tips-16-apr-26.md) [![Thariq](!/tags/thariq.svg)](https://x.com/trq212)

<p align="center">
  <img src="!/claude-jumping.svg" alt="section divider" width="60" height="50">
</p>

## 🔀 跨模型工作流 (CROSS-MODEL WORKFLOWS)

将 Claude Code 与其他模型（Codex、Gemini、GPT、Kimi、DeepSeek、本地模型等）结合使用 —— 通过三种机制：

- **插件 (Plugin)** — 其他模型的 CLI 在 Claude Code 内部运行（如 `/codex:review` 这样的斜杠命令）
- **MCP** — Claude Code 通过 Model Context Protocol 将另一个模型作为工具调用
- **路由器 (Router)** — Claude Code 的 API 端点被替换为不同的提供商

方法论：[跨模型工作流 (Claude Code + Codex)](development-workflows/cross-model-workflow/cross-model-workflow.md) [![Implemented](!/tags/implemented.svg)](development-workflows/cross-model-workflow/cross-model-workflow.md) — 手动双终端流程，在 Claude 中进行计划，在 Codex 中进行 QA-审查。

| 名称 | ★ | 类型 | 桥接至 | 功能描述 |
|------|---|------|------------|--------------|
| [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router) | 34k | Router (路由器) | OpenRouter, DeepSeek, Ollama, Gemini, Kimi, Qwen, Groq, +更多 | 将 Claude Code 的 API 路由到任何兼容的提供商，支持按任务选择模型 |
| [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | 32k | Router (路由器) | Gemini CLI, Codex, Claude Code, Antigravity | 将每个 CLI 包装为 OpenAI/Gemini/Claude/Codex 兼容的 API 服务 |
| [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | 18k | Plugin (插件) | Codex / GPT-5 | 官方 OpenAI 插件：在 Claude Code 中使用 `/codex:review`, `/codex:adversarial-review`, `/codex:rescue` |
| [BeehiveInnovations/pal-mcp-server](https://github.com/BeehiveInnovations/pal-mcp-server) | 12k | MCP (多模型服务器) | Gemini, OpenAI, Azure, Grok, Ollama, OpenRouter (50+ models) | 多模型 MCP 服务器（原 `zen-mcp-server`） — 将其他模型作为 Claude 工具调用 |

<p align="center">
  <img src="!/claude-jumping.svg" alt="section divider" width="60" height="50">
</p>

## 🧰 技能合集 (SKILL COLLECTIONS)

主要以其为 `SKILL.md` 文件精选库而闻名的仓库（区别于上述完整的工作流方法论）。按星标降序排列。

| 名称 | ★ | <img src="!/tags/s.svg" height="14"> |
|------|---|---|
| [anthropics/skills](https://github.com/anthropics/skills) | 145k | 17 |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 113k | 25 |
| [wshobson/agents](https://github.com/wshobson/agents) | 36k | 155 |
| [impeccable](https://github.com/pbakaus/impeccable) | 27k | 1 (含 7 个设计领域引用) |
| [agent-skills](https://github.com/addyosmani/agent-skills) | 27k | 21 |
| [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 27k | 143 |
| [awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 24k | 1,424+ (精选列表) |
| [claude-skills](https://github.com/alirezarezvani/claude-skills) | 15k | 246 (跨 9 个领域) |
| [shanraisshan/draw-json-architecture-skill](https://github.com/shanraisshan/draw-json-architecture-skill) | 0 | 1 |

<p align="center">
  <img src="!/claude-jumping.svg" alt="section divider" width="60" height="50">
</p>

## 🤖 代理合集 (AGENT COLLECTIONS)

主要以其为子代理定义（`.claude/agents/*.md`）的精选库而闻名的仓库。按星标降序排列。

| 名称 | ★ | <img src="!/tags/a.svg" height="14"> |
|------|---|---|
| [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | 107k | 144 |
| [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | 21k | 156 |

<p align="center">
  <img src="!/claude-jumping.svg" alt="section divider" width="60" height="50">
</p>

## 💡 技巧与窍门 (TIPS AND TRICKS) (83)

🚫👶 = 不要像保姆一样盯着（不要 micromanage）

[提示词 (Prompting)](#tips-prompting) · [计划 (Planning)](#tips-planning) · [上下文 (Context)](#tips-context) · [会话管理 (Session)](#tips-session) · [CLAUDE.md + .claude/rules](#tips-claudemd) · [代理 (Agents)](#tips-agents) · [命令 (Commands)](#tips-commands) · [技能 (Skills)](#tips-skills) · [钩子 (Hooks)](#tips-hooks) · [工作流 (Workflows)](#tips-workflows) · [高级技巧 (Advanced)](#tips-workflows-advanced) · [Git / PR](#tips-git-pr) · [调试 (Debugging)](#tips-debugging) · [实用工具 (Utilities)](#tips-utilities) · [日常使用 (Daily)](#tips-daily)

![Community](!/tags/community.svg)

<a id="tips-prompting"></a>■ **提示词技巧 (Prompting) (3)**

| 技巧 | 来源 |
|-----|--------|
| 挑战 Claude —— “针对这些变更拷问我，在我通过你的测试之前不要创建 PR。”或者“向我证明这行得通”，让 Claude 对比 main 和你分支之间的差异 🚫👶 | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2017742752566632544) |
| 在修复效果一般之后 —— “基于你现在所知的一切，放弃这个方案并实现优雅的解决方案” 🚫👶 | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2017742752566632544) |
| Claude 能自己修复大多数 bug —— 粘贴 bug，说“fix”，不要微观管理它是如何修复的 🚫👶 | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2017742750473720121) |

<a id="tips-planning"></a>■ **计划/规格说明 (Planning/Specs) (7)**

| 技巧 | 来源 |
|-----|--------|
| 始终从 [plan mode](https://code.claude.com/docs/en/common-workflows)（计划模式）开始 | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2007179845336527000) |
| 从一个最小的规格说明或提示词开始，让 Claude 使用 [AskUserQuestion](https://code.claude.com/docs/en/cli-reference) 工具采访你，然后开启一个新会话来执行该规格说明 | [![Thariq](!/tags/thariq.svg)](https://x.com/trq212/status/2005315275026260309) |
| 始终制定分阶段的计划，每个阶段包含多个测试（单元测试、自动化测试、集成测试） | [![Dex](!/tags/community-dex.svg)](videos/claude-dex-mlops-community-24-mar-26.md) [![Video](!/tags/video.svg)](https://youtu.be/YwZR6tc7qYg?t=1032) |
| 将 PRD（产品需求文档）分解为垂直切片（Tracer Bullets），跨越所有层级（数据库 + 服务 + UI）—— AI 默认倾向于水平分阶段（先数据库阶段，再 API 阶段，最后前端阶段），这会延迟端到端反馈直到最后一个阶段。源自《精益软件开发》 🚫👶 | [![Matt](!/tags/community-matt.svg)](videos/claude-matt-pocock-24-apr-26.md) [![Video](!/tags/video.svg)](https://youtu.be/-QFHIoCo-Ko) |
| 启动第二个 Claude 实例以 Staff Engineer（高级工程师）的角色审查你的计划，或使用 [跨模型](development-workflows/cross-model-workflow/cross-model-workflow.md) 进行审查 | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2017742745365057733) |
| 在移交工作之前编写详细的规格说明并减少歧义 —— 你描述得越具体，输出效果越好 | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2017742752566632544) |
| 原型 > PRD —— 构建 20-30 个版本，而不是编写规格说明，因为构建成本低，所以多试几次 🚫👶 | [![Boris](!/tags/boris-cherny.svg)](https://youtu.be/julbw1JuAz0?t=3630) [![Video](!/tags/video.svg)](https://youtu.be/julbw1JuAz0?t=3630) |

<a id="tips-context"></a>■ **上下文管理 (Context) (5)**

| 技巧 | 来源 |
|-----|--------|
| 在 1M 上下文的模型上，大约 ~300-400k tokens 时会出现**上下文退化 (context rot)** —— 不要让会话漂移超过这个界限用于对智能敏感的工作 | [![Thariq](!/tags/thariq.svg)](tips/claude-thariq-tips-16-apr-26.md) |
| **低效区 (dumb zone)** 在上下文使用率达到 ~40% 时出现 —— “你会达到结果退化的那个点”。新手：“尽量保持在 40% 以下，如果上升到 60%，考虑结束会话”。老手：“激进地将其控制在 30% 以下” —— 仅在简单任务时才推向 60%。切换任务时使用手动 [/compact](https://code.claude.com/docs/en/interactive-mode) 或 [/clear](https://code.claude.com/docs/en/cli-reference) 重置 | [![Dex](!/tags/community-dex.svg)](videos/claude-dex-mlops-community-24-mar-26.md) [![Video](!/tags/video.svg)](https://youtu.be/YwZR6tc7qYg?t=1541) |
| **回滚优于修正 (rewind > correct)** —— 双击 Esc 或 [/rewind](https://code.claude.com/docs/en/checkpointing) 回到失败尝试之前，利用你学到的东西重新提示，而不是让失败的尝试和修正污染上下文 🚫👶 | [![Thariq](!/tags/thariq.svg)](tips/claude-thariq-tips-16-apr-26.md) |
| 带有提示的 [/compact](https://code.claude.com/docs/en/interactive-mode)（例如：专注于身份验证重构，丢弃测试调试）优于让自动压缩触发 —— 由于上下文退化，模型在自动压缩时处于最不智能的状态 | [![Thariq](!/tags/thariq.svg)](tips/claude-thariq-tips-16-apr-26.md) |
| 使用子代理进行上下文管理 —— 问自己“我是否需要再次使用这个工具输出，还是只需要结论？”—— 20 次文件读取 + 12 次 grep + 3 个死胡同都留在子代理的上下文中，只有最终报告返回 🚫👶 | [![Thariq](!/tags/thariq.svg)](tips/claude-thariq-tips-16-apr-26.md) |

<a id="tips-session"></a>■ **会话管理 (Session Management) (6)**

| 技巧 | 来源 |
|-----|--------|
| 每一步都是一个分支点 —— Claude 结束一步后，根据你需要携带多少现有上下文，选择 Continue、/rewind、/clear、/compact 或 Subagent | [![Thariq](!/tags/thariq.svg)](tips/claude-thariq-tips-16-apr-26.md) |
| 新任务 = 新会话 —— 相关任务（例如，为你刚刚构建的内容编写文档）可以重用上下文以提高效率，但真正的新任务值得开启一个新会话 | [![Thariq](!/tags/thariq.svg)](tips/claude-thariq-tips-16-apr-26.md) |
| 在回滚之前使用“从此时开始总结 (summarize from here)”让 Claude 编写交接消息 —— 就像是你未来的自己写给上一轮 Claude 的笔记 | [![Thariq](!/tags/thariq.svg)](tips/claude-thariq-tips-16-apr-26.md) |
| /compact vs /clear — compact 是有损但有利于保持势头（任务中途，模糊细节可以接受）；/clear + 简短说明更费事，但你完全控制携带的内容（高风险的下一步） | [![Thariq](!/tags/thariq.svg)](tips/claude-thariq-tips-16-apr-26.md) |
| 对于长时间运行的会话使用回顾 (recaps) —— Claude 做了什么以及接下来做什么的简短摘要，当你几分钟或几小时后回来时很有用。在 /config 中禁用 recaps | [![Boris](!/tags/boris-cherny.svg)](tips/claude-boris-6-tips-16-apr-26.md) |
| [/rename](https://code.claude.com/docs/en/cli-reference) 重要会话（例如 [TODO - refactor task]）并在以后 [/resume](https://code.claude.com/docs/en/cli-reference) —— 当同时运行多个 Claude 实例时，标记每个实例 | [![Cat](!/tags/cat-wu.svg)](https://every.to/podcast/how-to-use-claude-code-like-the-people-who-built-it) |

<a id="tips-claudemd"></a>■ **CLAUDE.md + .claude/rules (8)**

| 技巧 | 来源 |
|-----|--------|
| [CLAUDE.md](https://code.claude.com/docs/en/memory) 应针对每个文件控制在 [200 行以下](https://code.claude.com/docs/en/memory#write-effective-instructions)。[humanlayer 中的 60 行](https://www.humanlayer.dev/blog/writing-a-good-claude-md)（[仍不保证 100% 有效](https://www.reddit.com/r/ClaudeCode/comments/1qn9pb9/claudemd_says_must_use_agent_claude_ignores_it_80/)） | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2007179840848597422) [![Dex](!/tags/community-dex.svg)](https://www.humanlayer.dev/blog/writing-a-good-claude-md) |
| .claude/rules/*.md 像 CLAUDE.md 一样自动加载到每个会话中 —— 添加 paths: YAML frontmatter 以仅在 Claude 触及匹配 glob 的文件时延迟加载它们 | [![Claude](!/tags/claude.svg)](https://code.claude.com/docs/en/memory#organize-rules-with-clauderules) |
| 在 [\<important if="..."\> 标签](https://www.hlyr.dev/blog/stop-claude-from-ignoring-your-claude-md)中包装特定领域的 CLAUDE.md 规则，以防止 Claude 随着文件变长而忽略它们 | [![Dex](!/tags/community-dex.svg)](https://www.hlyr.dev/blog/stop-claude-from-ignoring-your-claude-md) |
| 对 monorepo 使用 [多个 CLAUDE.md](best-practice/claude-memory.md) —— 祖先 + 后代加载机制 | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2016339448863355206) |
| 使用 [.claude/rules/](https://code.claude.com/docs/en/memory#organize-rules-with-clauderules) 来拆分大型指令 | [![Claude](!/tags/claude.svg)](https://code.claude.com/docs/en/memory#organize-rules-with-clauderules) |
| 任何开发人员都应该能够启动 Claude，说“运行测试”，然后第一次就成功 —— 如果不行，说明你的 CLAUDE.md 缺少关键的设置/构建/测试命令 | [![Dex](!/tags/community-dex.svg)](https://x.com/dexhorthy/status/2034713765401551053) |
| 保持代码库整洁并完成迁移 —— 部分迁移的框架会让模型感到困惑，从而可能选择错误的模式 | [![Boris](!/tags/boris-cherny.svg)](https://youtu.be/julbw1JuAz0?t=1112) [![Video](!/tags/video.svg)](https://youtu.be/julbw1JuAz0?t=1112) |
| 使用 [settings.json](best-practice/claude-settings.md) 来强制执行行为（署名、权限、模型） —— 当 attribution.commit: "" 是确定性时，不要在 CLAUDE.md 中写“NEVER add Co-Authored-By” | [![davila7](!/tags/community-davila7.svg)](https://x.com/dani_avila7/status/2036182734310195550) |

<a id="tips-agents"></a><img src="!/tags/a.svg" height="14"> **代理 (Agents) (4)**

| 技巧 | 来源 |
|-----|--------|
| 拥有特定功能的 [子代理](https://code.claude.com/docs/en/sub-agents)（额外上下文）配合 [技能](https://code.claude.com/docs/en/skills)（渐进式披露），而不是通用的 QA、后端工程师 | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2007179850139000872) |
| 说“使用子代理”来投入更多算力解决问题 —— 将任务卸载以保持主上下文干净整洁 🚫👶 | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2017742755737555434) |
| 使用带有 tmux 的 [代理团队](https://code.claude.com/docs/en/agent-teams) 和 [git worktrees](https://x.com/bcherny/status/2025007393290272904) 进行并行开发 | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2025007393290272904) |
| 使用 [测试时间算力 (test time compute)](https://code.claude.com/docs/en/sub-agents) —— 分离的上下文窗口会使结果更好；一个代理可能会引入 bug，而另一个（相同模型）可以发现它们 | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2031151689219321886) |

<a id="tips-commands"></a><img src="!/tags/c.svg" height="14"> **命令 (Commands) (3)**

| 技巧 | 来源 |
|-----|--------|
| 对你的工作流使用 [命令](https://code.claude.com/docs/en/slash-commands)，而不是 [子代理](https://code.claude.com/docs/en/sub-agents) | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2007179847949500714) |
| 对你每天多次执行的“内循环”工作流使用 [斜杠命令](https://code.claude.com/docs/en/slash-commands) —— 节省重复提示，命令存储在 .claude/commands/ 中并检入 git | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2007179847949500714) |
| 如果你每天做某事超过一次，将其变成 [技能](https://code.claude.com/docs/en/skills) 或 [命令](https://code.claude.com/docs/en/slash-commands) —— 构建 /techdebt、context-dump 或 analytics 命令 | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2017742748984742078) |

<a id="tips-skills"></a><img src="!/tags/s.svg" height="14"> **技能 (Skills) (9)**

| 技巧 | 来源 |
|-----|--------|
| 使用 [context: fork](https://code.claude.com/docs/en/skills) 在隔离的子代理中运行技能 —— 主上下文只看到最终结果，看不到中间工具调用。agent 字段允许你设置子代理类型 | [![Lydia](!/tags/lydia.svg)](https://x.com/lydiahallie/status/2033603164398883042) |
| 对 monorepo 使用 [子文件夹中的技能](reports/claude-skills-for-larger-mono-repos.md) | [![Claude](!/tags/claude.svg)](https://code.claude.com/docs/en/skills) |
| 技能是文件夹，不是文件 —— 使用 references/, scripts/, examples/ 子目录进行 [渐进式披露](https://code.claude.com/docs/en/skills) | [![Thariq](!/tags/thariq.svg)](https://x.com/trq212/status/2033949937936085378) |
| 在每个技能中构建一个“注意事项 (Gotchas)”部分 —— 最高信号的内容，随着时间的推移添加 Claude 的失败点 | [![Thariq](!/tags/thariq.svg)](https://x.com/trq212/status/2033949937936085378) |
| 技能描述字段是一个触发器，而不是摘要 —— 为模型编写它（“我什么时候应该触发？”） | [![Thariq](!/tags/thariq.svg)](https://x.com/trq212/status/2033949937936085378) |
| 不要在技能中陈述显而易见的东西 —— 专注于将 Claude 推离默认行为的内容 🚫👶 | [![Thariq](!/tags/thariq.svg)](https://x.com/trq212/status/2033949937936085378) |
| 不要在技能中把 Claude 当火车轨道一样限制 —— 给出目标和约束，而不是规定性的逐步指令 🚫👶 | [![Thariq](!/tags/thariq.svg)](https://x.com/trq212/status/2033949937936085378) |
| 在技能中包含脚本和库，以便 Claude 进行组合而不是重建样板代码 | [![Thariq](!/tags/thariq.svg)](https://x.com/trq212/status/2033949937936085378) |
| 在 SKILL.md 中嵌入 !command 以将动态 shell 输出注入提示 —— Claude 在调用时运行它，模型只看到结果 | [![Lydia](!/tags/lydia.svg)](https://x.com/lydiahallie/status/2034337963820327017) |

<a id="tips-hooks"></a>■ **钩子 (Hooks) (5)**

| 技巧 | 来源 |
|-----|--------|
| 在技能中使用 [按需钩子](https://code.claude.com/docs/en/skills) —— /careful 阻止破坏性命令，/freeze 阻止目录外的编辑 | [![Thariq](!/tags/thariq.svg)](https://x.com/trq212/status/2033949937936085378) |
| 使用 PreToolUse 钩子来 [测量技能使用情况](https://code.claude.com/docs/en/skills)，以找出热门或触发不足的技能 | [![Thariq](!/tags/thariq.svg)](https://x.com/trq212/status/2033949937936085378) |
| 使用 [PostToolUse 钩子](https://code.claude.com/docs/en/hooks) 自动格式化代码 —— Claude 生成格式良好的代码，钩子处理最后 10% 以避免 CI 失败 | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2007179852047335529) |
| 通过钩子将 [权限请求](https://code.claude.com/docs/en/hooks) 路由到 Opus —— 让它扫描攻击并自动批准安全的操作 🚫👶 | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2017742755737555434) |
| 使用 [Stop 钩子](https://code.claude.com/docs/en/hooks) 在每一步结束时推动 Claude 继续工作或验证其工作 | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2021701059253874861) |

<a id="tips-workflows"></a>■ **工作流 (Workflows) (5)**

| 技巧 | 来源 |
|-----|--------|
| 使用 [/model](https://code.claude.com/docs/en/model-config) 选择模型和推理，[/context](https://code.claude.com/docs/en/interactive-mode) 查看上下文使用情况，[/usage](https://code.claude.com/docs/en/costs) 检查计划限制，[/extra-usage](https://code.claude.com/docs/en/interactive-mode) 配置溢出计费，[/config](https://code.claude.com/docs/en/settings) 配置设置 —— 在 plan mode 使用 Opus，在编码时使用 Sonnet 以兼得两者之长 | [![Cat](!/tags/cat-wu.svg)](https://x.com/_catwu/status/1955694117264261609) |
| 始终开启 [thinking mode](https://code.claude.com/docs/en/model-config) true（以查看推理过程）并在 [/config](https://code.claude.com/docs/en/settings) 中设置 [Output Style (输出样式)](https://code.claude.com/docs/en/output-styles) 为 Explanatory（以查看详细输出和 ★ Insight 框），以便更好地理解 Claude 的决策 | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2007179838864666847) |
| 在提示词中使用 ultrathink 关键字以进行 [高努力推理](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#tips-and-best-practices) | [![Claude](!/tags/claude.svg)](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#tips-and-best-practices) |
| /focus 模式隐藏所有中间工作，只显示最终结果 —— 信任模型运行正确的命令并只看结果（通过 /focus 切换） | [![Boris](!/tags/boris-cherny.svg)](tips/claude-boris-6-tips-16-apr-26.md) |
| 使用 Opus 4.7 的自适应思考调整努力水平 —— low 用于速度和减少 token，max 用于最高智能（滑块：low · medium · high · xhigh · max） | [![Boris](!/tags/boris-cherny.svg)](tips/claude-boris-6-tips-16-apr-26.md) |

<a id="tips-workflows-advanced"></a>■ **高级工作流 (Workflows Advanced) (9)**

| 技巧 | 来源 |
|-----|--------|
| 大量使用 ASCII 图表来理解你的架构 | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2017742759218794768) |
| 对本地循环监控（最长 7 天）使用 [/loop](https://code.claude.com/docs/en/scheduled-tasks) · 对云基循环任务（即使你的机器关闭也能运行）使用 [/schedule](https://code.claude.com/docs/en/routines) | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2038454341884154269) |
| 对长时间运行的自主任务使用 [Ralph Wiggum 插件](https://github.com/shanraisshan/ralph-wiggum-self-evolving-loop) | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2007179858435281082) |
| 使用带有通配符语法的 [/permissions](https://code.claude.com/docs/en/permissions)（Bash(npm run *), Edit(/docs/**）），而不是 dangerously-skip-permissions | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2007179854077407667) |
| 使用 [/sandbox](https://code.claude.com/docs/en/sandboxing) 通过文件和网络隔离来减少权限提示 —— 内部减少了 84% | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2021700506465579443) [![Cat](!/tags/cat-wu.svg)](https://creatoreconomy.so/p/inside-claude-code-how-an-ai-native-actually-works-cat-wu) |
| 投资 [产品验证](https://code.claude.com/docs/en/skills) 技能（signup-flow-driver, checkout-verifier） —— 值得花一周时间完善它们 | [![Thariq](!/tags/thariq.svg)](https://x.com/trq212/status/2033949937936085378) |
| 使用 [auto mode (自动模式)](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode) 代替 dangerously-skip-permissions —— 基于模型的分类器决定每个命令是否安全并自动批准，如果存在风险则暂停并询问。Shift+Tab 循环切换 Ask → Plan → Auto 模式 🚫👶 | [![Boris](!/tags/boris-cherny.svg)](tips/claude-boris-6-tips-16-apr-26.md) |
| 使用 /less-permission-prompts 技能扫描会话历史，查找反复提示的 bash/MCP 安全命令，然后获取推荐的白名单粘贴到 [设置](best-practice/claude-settings.md) 中 | [![Boris](!/tags/boris-cherny.svg)](tips/claude-boris-6-tips-16-apr-26.md) |
| 构建一个 /go 技能，它 (1) 通过 bash/browser/computer use 进行端到端测试 (2) 运行 /simplify (3) 提交 PR —— 这样当你回来时，你就知道代码是有效的 🚫👶 | [![Boris](!/tags/boris-cherny.svg)](tips/claude-boris-6-tips-16-apr-26.md) |

<a id="tips-git-pr"></a>■ **Git / PR (5)**

| 技巧 | 来源 |
|-----|--------|
| 保持 PR 小而专注 —— [p50 为 118 行](tips/claude-boris-2-tips-25-mar-26.md)（一天内 141 个 PR，更改了 4.5K 行代码），一个 PR 对应一个功能，更容易审查和回滚 | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2038552880018538749) |
| 始终对 PR 进行 [squash merge (变基合并)](tips/claude-boris-2-tips-25-mar-26.md) —— 干净的线性历史，每个功能一个提交，易于 git revert 和 git bisect | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2038552880018538749) |
| 频繁 commit —— 尝试每小时至少 commit 一次，任务完成后立即 commit | ![Shayan](!/tags/community-shayan.svg) |
| 在同事的 PR 上 tag [@claude](https://github.com/apps/claude) 以自动生成重复审查反馈的 lint 规则 —— 让自己从代码审查中解脱出来 🚫👶 | [![Boris](!/tags/boris-cherny.svg)](https://youtu.be/julbw1JuAz0?t=2715) [![Video](!/tags/video.svg)](https://youtu.be/julbw1JuAz0?t=2715) |
| 使用 [/code-review](https://code.claude.com/docs/en/code-review) 进行多代理 PR 分析 —— 在合并之前捕获 bug、安全漏洞和回归 | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2031089411820228645) |

<a id="tips-debugging"></a>■ **调试 (Debugging) (6)**

| 技巧 | 来源 |
|-----|--------|
| 养成习惯，每当你在任何问题上卡住时，截图并与 Claude 分享 | ![Shayan](!/tags/community-shayan.svg) |
| 使用 mcp（[Chrome 中的 Claude](https://code.claude.com/docs/en/chrome), [Playwright](https://github.com/microsoft/playwright-mcp), [Chrome DevTools](https://developer.chrome.com/blog/chrome-devtools-mcp)）让 Claude 自行查看 chrome 控制台日志 | [![Claude](!/tags/claude.svg)](https://code.claude.com/docs/en/chrome) |
| 始终要求 Claude 将终端（你想要看到日志的）作为后台任务运行，以便更好地调试 | ![Shayan](!/tags/community-shayan.svg) |
| 使用 [/doctor](https://code.claude.com/docs/en/cli-reference) 诊断安装、身份验证和配置问题 | ![Shayan](!/tags/community-shayan.svg) |
| 对 QA 使用 [跨模型](development-workflows/cross-model-workflow/cross-model-workflow.md)，例如使用 [Codex](https://github.com/shanraisshan/codex-cli-best-practice) 进行计划和实施审查 | ![Shayan](!/tags/community-shayan.svg) |
| 智能体搜索（glob + grep）优于 RAG —— Claude Code 尝试并弃用了向量数据库，因为代码会脱节且权限复杂 | [![Boris](!/tags/boris-cherny.svg)](https://youtu.be/julbw1JuAz0?t=3095) [![Video](!/tags/video.svg)](https://youtu.be/julbw1JuAz0?t=3095) |

<a id="tips-utilities"></a>■ **实用工具 (Utilities) (5)**

| 技巧 | 来源 |
|-----|--------|
| [iTerm](https://iterm2.com/)/[Ghostty](https://ghostty.org/)/[tmux](https://github.com/tmux/tmux) 终端，而不是 IDE（[VS Code](https://code.visualstudio.com/)/[Cursor](https://www.cursor.com/)） | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2017742753971769626) |
| 使用 [/voice](https://code.claude.com/docs/en/voice-dictation) 或 [Wispr Flow](https://wisprflow.ai) 进行语音提示（提高 10 倍生产力） | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2038454362226467112) |
| 使用 [claude-code-hooks](https://github.com/shanraisshan/claude-code-hooks) 获取 Claude 反馈 | ![Shayan](!/tags/community-shayan.svg) |
| 使用 [status line (状态栏)](https://github.com/shanraisshan/claude-code-status-line) 进行上下文感知和快速压缩 | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2021700784019452195) ![Shayan](!/tags/community-shayan.svg) |
| 探索 [settings.json](best-practice/claude-settings.md) 功能，如 [Plans Directory (计划目录)](best-practice/claude-settings.md#plans-directory), [Spinner Verbs (旋转动词)](best-practice/claude-settings.md#display--ux)，以获得个性化体验 | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny/status/2021701145023197516) |

<a id="tips-daily"></a>■ **日常使用 (Daily) (2)**

| 技巧 | 来源 |
|-----|--------|
| [更新](https://code.claude.com/docs/en/setup) Claude Code 每天版本 | ![Shayan](!/tags/community-shayan.svg) |
| 通过阅读 [changelog (更新日志)](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) 开始你的一天 | ![Shayan](!/tags/community-shayan.svg) |

![Boris Cherny + Team](!/tags/claude.svg)

| 文章 / 推文 | 来源 |
|-----------------|--------|
| [从 Opus 4.7 获取更多技巧 (Boris) \| 26年4月16日](tips/claude-boris-6-tips-16-apr-26.md) | [推文](https://x.com/bcherny) |
| [会话管理与 1M 上下文 (Thariq) \| 26年4月16日](tips/claude-thariq-tips-16-apr-26.md) | [推文](https://x.com/trq212) |
| [Claude Code 中 15 个隐藏且未充分利用的功能 (Boris) \| 26年3月30日](tips/claude-boris-15-tips-30-mar-26.md) | [推文](https://x.com/bcherny/status/2038454336355999749) |
| [变基合并与 PR 大小分布 (Boris) \| 26年3月25日](tips/claude-boris-2-tips-25-mar-26.md) | [推文](https://x.com/bcherny/status/2038552880018538749) |
| [构建 Claude Code 的经验教训：我们如何使用技能 (Thariq) \| 26年3月17日](tips/claude-thariq-tips-17-mar-26.md) | [文章](https://x.com/trq212/status/2033949937936085378) |
| [代码审查与测试时间算力 (Boris) \| 26年3月10日](tips/claude-boris-2-tips-10-mar-26.md) | [推文](https://x.com/bcherny/status/2031089411820228645) |
| /loop —— 安排长达 3 天的循环任务 (Boris) \| 2026年3月7日 | [推文](https://x.com/bcherny/status/2030193932404150413) |
| AskUserQuestion + ASCII Markdowns (Thariq) \| 2026年2月28日 | [推文](https://x.com/trq212/status/2027543858289250472) |
| 像代理一样思考 - 构建 Claude Code 的经验教训 (Thariq) \| 2026年2月28日 | [文章](https://x.com/trq212/status/2027463795355095314) |
| Git Worktrees - Boris 使用的 5 种方式 \| 2026年2月21日 | [推文](https://x.com/bcherny/status/2025007393290272904) |
| 构建 Claude Code 的经验教训：提示缓存是一切 (Thariq) \| 2026年2月20日 | [文章](https://x.com/trq212/status/2024574133011673516) |
| [人们定制 Claude 的 12 种方式 (Boris) \| 26年2月12日](tips/claude-boris-12-tips-12-feb-26.md) | [推文](https://x.com/bcherny/status/2021699851499798911) |
| [使用 Claude Code 的 10 个技巧 (Boris) \| 26年2月1日](tips/claude-boris-10-tips-01-feb-26.md) | [推文](https://x.com/bcherny/status/2017742741636321619) |
| [我如何使用 Claude Code —— 来自我出人意料的 vanilla 设置的 13 个技巧 (Boris) \| 26年1月3日](tips/claude-boris-13-tips-03-jan-26.md) | [推文](https://x.com/bcherny/status/2007179832300581177) |
| 让 Claude 使用 AskUserQuestion 工具采访你 (Thariq) \| 2025年12月28日 | [推文](https://x.com/trq212/status/2005315275026260309) |
| 始终使用 plan mode，给 Claude 一个验证途径，使用 /code-review (Boris) \| 2025年12月27日 | [推文](https://x.com/bcherny/status/2004711722926616680) |

#### 来自 Claude Code CLI 二进制文件的技巧

[Spinner Verbs & Tips (从 CLI 二进制文件 v2.1.121 中提取)](reports/claude-spinner-verbs-and-tips.md)

<p align="center">
  <img src="!/claude-jumping.svg" alt="section divider" width="60" height="50">
</p>

## 🎬 视频 / 播客 (VIDEOS / PODCASTS)

| 视频 / 播客 | 来源 | YouTube |
|-----------------|--------|--------|
| 从氛围编程到智能体工程 (Andrej) \| 2026年5月2日 \| AI Engineer | [![Karpathy](!/tags/community-karpathy.svg)](https://x.com/karpathy) | [YouTube](https://www.youtube.com/watch?v=96jN2OCOfLs) |
| 完整演练：AI 编码工作流 (Matt) \| 2026年4月24日 \| Matt Pocock | [![Matt](!/tags/community-matt.svg)](https://x.com/mattpocockuk) | [YouTube](https://youtu.be/-QFHIoCo-Ko) |
| 我们在研究-计划-实施方面错得有多离谱 (Dex) \| 2026年3月24日 \| MLOps Community | [![Dex](!/tags/community-dex.svg)](https://x.com/daborhyde) | [YouTube](https://youtu.be/YwZR6tc7qYg) |
| 与 Boris Cherny 一起构建 Claude Code (Boris) \| 2026年3月4日 \| The Pragmatic Engineer | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny) | [YouTube](https://youtu.be/julbw1JuAz0) |
| Claude Code 负责人：编码问题解决后会发生什么 (Boris) \| 2026年2月19日 \| Lenny's Podcast | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny) | [YouTube](https://youtu.be/We7BZVKbCVw) |
| 深入 Claude Code，与其创建者 Boris Cherny (Boris) \| 2026年2月17日 \| Y Combinator | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny) | [YouTube](https://youtu.be/PQU9o_5rHC4) |
| Boris Cherny (Claude Code 创建者) 谈他的职业生涯是如何成长的 (Boris) \| 2025年12月15日 \| Ryan Peterman | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny) | [YouTube](https://youtu.be/AmdLVWMdjOk) |
| 从构建它的工程师那里了解 Claude Code 的秘密 (Cat) \| 2025年10月29日 \| Every | [![Boris](!/tags/boris-cherny.svg)](https://x.com/bcherny) | [YouTube](https://youtu.be/IDSAMqip6ms) |

<p align="center">
  <img src="!/claude-jumping.svg" alt="section divider" width="60" height="50">
</p>

## 🔔 订阅 (SUBSCRIBE)

| 来源 | 名称 | 徽章 |
|--------|------|-------|
| ![Reddit](https://img.shields.io/badge/-FF4500?style=flat&logo=reddit&logoColor=white) | [r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/), [r/ClaudeCode](https://www.reddit.com/r/ClaudeCode/), [r/Anthropic](https://www.reddit.com/r/Anthropic/) | ![Boris + Team](!/tags/claude.svg) |
| ![X](https://img.shields.io/badge/-000?style=flat&logo=x&logoColor=white) | [Claude](https://x.com/claudeai), [Claude Devs](https://x.com/ClaudeDevs), [Anthropic](https://x.com/AnthropicAI), [Boris](https://x.com/bcherny), [Thariq](https://x.com/trq212), [Cat](https://x.com/_catwu), [Lydia](https://x.com/lydiahallie), [Noah](https://x.com/noahzweben), [Anthony](https://x.com/amorriscode), [Alex](https://x.com/alexalbert__), [Kenneth](https://x.com/neilhtennek) | ![Boris + Team](!/tags/claude.svg) |
| ![X](https://img.shields.io/badge/-000?style=flat&logo=x&logoColor=white) | [Jesse Kriss](https://x.com/obra) ([Superpowers](https://github.com/obra/superpowers)), [Affaan Mustafa](https://x.com/affaanmustafa) ([ECC](https://github.com/affaan-m/everything-claude-code)), [Garry Tan](https://x.com/garrytan) ([gstack](https://github.com/garrytan/gstack)), [Dex Horthy](https://x.com/dexhorthy) ([HumanLayer](https://github.com/humanlayer/humanlayer)), [Kieran Klaassen](https://x.com/kieranklaassen) ([Compound Eng](https://github.com/EveryInc/compound-engineering-plugin)), [Tabish Gilani](https://x.com/0xTab) ([OpenSpec](https://github.com/Fission-AI/OpenSpec)), [Brian McAdams](https://x.com/BMadCode) ([BMAD](https://github.com/bmad-code-org/BMAD-METHOD)), [Lex Christopherson](https://x.com/official_taches) ([GSD](https://github.com/gsd-build/get-shit-done)), [Matt Pocock](https://x.com/mattpocockuk) ([Skills](https://github.com/mattpocock/skills)), [Dani Avila](https://x.com/dani_avila7) ([CC Templates](https://github.com/davila7/claude-code-templates)), [Dan Shipper](https://x.com/danshipper) ([Every](https://every.to/)), [Andrej Karpathy](https://x.com/karpathy) ([AutoResearch](https://x.com/karpathy/status/2015883857489522876)), [Peter Steinberger](https://x.com/steipete) ([OpenClaw](https://x.com/openclaw)), [Sigrid Jin](https://x.com/realsigridjin) ([claw-code](https://github.com/ultraworkers/claw-code)), [Yeachan Heo](https://x.com/bellman_ych) ([oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)) | ![Community](!/tags/community.svg) |
| ![YouTube](https://img.shields.io/badge/-F00?style=flat&logo=youtube&logoColor=white) | [Anthropic](https://www.youtube.com/@anthropic-ai) | ![Boris + Team](!/tags/claude.svg) |
| ![YouTube](https://img.shields.io/badge/-F00?style=flat&logo=youtube&logoColor=white) | [Lenny's Podcast](https://www.youtube.com/@LennysPodcast), [Y Combinator](https://www.youtube.com/@ycombinator), [The Pragmatic Engineer](https://www.youtube.com/@pragmaticengineer), [Ryan Peterman](https://www.youtube.com/@ryanlpeterman), [Every](https://www.youtube.com/@every_media), [MLOps Community](https://www.youtube.com/@MLOps) | ![Community](!/tags/community.svg) |

<p align="center">
  <img src="!/claude-jumping.svg" alt="section divider" width="60" height="50">
</p>

## ☠️ 初创公司 / 企业 (STARTUPS / BUSINESSES)

| Claude | 取代了 |
|-|-|
|[**代码审查 (Code Review)**](https://code.claude.com/docs/en/code-review)|[Greptile](https://greptile.com), [CodeRabbit](https://coderabbit.ai), [Devin Review](https://devin.ai), [OpenDiff](https://opendiff.com), [Cursor BugBot](https://bugbot.dev)|
|[**语音听写 (Voice Dictation)**](https://code.claude.com/docs/en/voice-dictation)|[Wispr Flow](https://wisprflow.ai), [SuperWhisper](https://superwhisper.com/)|
|[**远程控制 (Remote Control)**](https://code.claude.com/docs/en/remote-control)|[OpenClaw](https://openclaw.ai/)
|[**Chrome 中的 Claude (Claude in Chrome)**](https://code.claude.com/docs/en/chrome)|[Playwright MCP](https://github.com/microsoft/playwright-mcp), [Chrome DevTools MCP](https://developer.chrome.com/blog/chrome-devtools-mcp)|
|[**Computer Use (电脑使用)**](https://docs.anthropic.com/en/docs/agents-and-tools/computer-use)|[OpenAI CUA](https://openai.com/index/computer-using-agent/)|
|[**Cowork (协作)**](https://claude.com/blog/cowork-research-preview)|[ChatGPT Agent](https://openai.com/chatgpt/agent/), [Perplexity Computer](https://www.perplexity.ai/computer/), [Manus](https://manus.im)|
|[**Tasks (任务)**](https://x.com/trq212/status/2014480496013803643)|[Beads](https://github.com/steveyegge/beads)
|[**Plan Mode (计划模式)**](https://code.claude.com/docs/en/common-workflows)|[Agent OS](https://github.com/buildermethods/agent-os)|
|[**设计 (Design)**](https://claude.com/design)|[Figma](https://figma.com), [Framer](https://framer.com), [Sketch](https://sketch.com), [v0](https://v0.dev)|
|[**Agent SDK**](https://code.claude.com/docs/en/agent-sdk/overview)|[LangChain](https://langchain.com), [LangGraph](https://www.langchain.com/langgraph), [CrewAI](https://www.crewai.com), [AutoGen](https://github.com/microsoft/autogen), [OpenAI Assistants API](https://platform.openai.com/docs/assistants/overview)|
|[**技能 / 插件 (Skills / Plugins)**](https://code.claude.com/docs/en/plugins)|YC AI wrapper 初创公司 ([reddit](https://reddit.com/r/ClaudeAI/comments/1r6bh4d/claude_code_skills_are_basically_yc_ai_startup/))|

<p align="center">
  <img src="!/claude-jumping.svg" alt="section divider" width="60" height="50">
</p>

<a id="billion-dollar-questions"></a>
![Billion-Dollar Questions](!/tags/billion-dollar-questions.svg)

*如果你有答案，请通过 shanraisshan@gmail.com 告诉我*

**记忆与指令 (Memory & Instructions) (4)**

1. CLAUDE.md 中到底应该放什么 —— 以及应该留下什么？
2. 如果你已经有了一个 CLAUDE.md，是否还需要单独的 constitution.md 或 rules.md？
3. 你应该多久更新一次 CLAUDE.md，以及如何知道它何时变得过时？
4. 为什么 Claude 仍然忽略 CLAUDE.md 的指令 —— 即使它们用全大写的 MUST 强调？ ([reddit](https://reddit.com/r/ClaudeCode/comments/1qn9pb9/claudemd_says_must_use_agent_claude_ignores_it_80/))

**代理、技能与工作流 (Agents, Skills & Workflows) (6)**

1. 什么时候应该使用命令 vs 代理 vs 技能 —— 以及什么时候原生的 Claude Code 更好？
2. 随着模型的改进，你应该多久更新一次你的代理、命令和工作流？
3. 你是否应该有一个通用子代理还是一个特定功能/角色的代理？给你的子代理一个详细的角色设定是否能提高质量，而针对研究/视觉的“完美角色提示词”是什么样的？
4. 你是依赖 Claude Code 内置的 plan mode —— 还是构建你自己的计划命令/代理来强制执行团队的工作流？
5. 如果你有一个个人技能（例如 /implement 带有你的编码风格），你如何将社区技能（例如 /simplify）纳入其中而不产生冲突 —— 当它们意见不一致时谁说了算？
6. 我们到了吗？我们可以将现有的代码库转换为规格说明，删除代码，然后让 AI 仅从这些规格说明中重新生成完全相同的代码吗？

**规格说明与文档 (Specs & Documentation) (3)**

1. 你仓库中的每个功能是否都应该有一个作为 markdown 文件的规格说明？
2. 当实现新功能时，你需要多久更新一次规格说明以防止它们过时？
3. 在实现新功能时，如何处理对其他功能的规格说明的连锁反应？

### 🤔 [代码还重要吗？](https://github.com/shanraisshan/agentic-engineering)

<p align="center">
  <img src="!/claude-jumping.svg" alt="section divider" width="60" height="50">
</p>

## REPORTS (报告)

<p align="center">
  <a href="reports/claude-agent-sdk-vs-cli-system-prompts.md"><img src="https://img.shields.io/badge/Agent_SDK_vs_CLI-555?style=for-the-badge" alt="Agent SDK vs CLI"></a>
  <a href="reports/claude-in-chrome-v-chrome-devtools-mcp.md"><img src="https://img.shields.io/badge/Browser_Automation_MCP-555?style=for-the-badge" alt="Browser Automation MCP"></a>
  <a href="reports/claude-global-vs-project-settings.md"><img src="https://img.shields.io/badge/Global_vs_Project_Settings-555?style=for-the-badge" alt="Global vs Project Settings"></a>
  <a href="reports/claude-skills-for-larger-mono-repos.md"><img src="https://img.shields.io/badge/Skills_in_Monorepos-555?style=for-the-badge" alt="Skills in Monorepos"></a>
  <br>
  <a href="reports/claude-agent-memory.md"><img src="https://img.shields.io/badge/Agent_Memory-555?style=for-the-badge" alt="Agent Memory"></a>
  <a href="reports/claude-advanced-tool-use.md"><img src="https://img.shields.io/badge/Advanced_Tool_Use-555?style=for-the-badge" alt="Advanced Tool Use"></a>
  <a href="reports/claude-usage-and-rate-limits.md"><img src="https://img.shields.io/badge/Usage_&_Rate_Limits-555?style=for-the-badge" alt="Usage & Rate Limits"></a>
  <a href="reports/claude-agent-command-skill.md"><img src="https://img.shields.io/badge/Agents_vs_Commands_vs_Skills-555?style=for-the-badge" alt="Agents vs Commands vs Skills"></a>
  <br>
  <a href="reports/llm-day-to-day-degradation.md"><img src="https://img.shields.io/badge/LLM_Degradation-555?style=for-the-badge" alt="LLM Degradation"></a>
  <a href="reports/why-harness-is-important.md"><img src="https://img.shields.io/badge/Why_Harness_is_Important-555?style=for-the-badge" alt="Why Harness is Important"></a>
  <a href="reports/claude-spinner-verbs-and-tips.md"><img src="https://img.shields.io/badge/Spinner_Verbs_&_Tips-555?style=for-the-badge" alt="Spinner Verbs & Tips"></a>
</p>

<p align="center">
  <img src="!/claude-jumping.svg" alt="section divider" width="60" height="50">
</p>

<a id="how-to-use"></a>

## <img src="!/tags/how-to-use-hd.svg" alt="How to Use"> (如何使用)

通过遵循以下步骤，最大限度地利用本仓库：

1. **将本仓库视为一门课程来阅读，而不是作为一个工作流或技能。** 它首先是参考资料；你稍后会运行一些东西。
2. **不要把 Claude 当作聊天机器人使用。** 学习原语 —— 代理、命令、技能、钩子 —— 并将它们组装成你自己的工作流程。
3. **运行 [`/weather-orchestrator`](orchestration-workflow/orchestration-workflow.md)** 以查看完整的命令 → 代理 → 技能流程。将其用作任何开发工作流的模板，从计划到发布。
4. **工作时注意自定义钩子声音。** 它们的实现位于专门的 [Claude Code Hooks 仓库](https://github.com/shanraisshan/claude-code-hooks)中；其他模式如 [Agent Teams (代理团队)](implementation/claude-agent-teams-implementation.md) 则包含在本仓库的 `implementation/` 目录中。
5. **从 [🔥 Hot (热门功能)](#-hot) 子表中学习高级主题及其实现** —— 例如，[Ralph Wiggum 自我进化循环](https://github.com/shanraisshan/ralph-wiggum-self-evolving-loop)是一个完整的工作仓库，你可以克隆它来查看这些模式之一的端到端演示。
6. **将 Claude 指向你自己项目中的 [技巧与窍门 (tips and tricks)](#-tips-and-tricks-83) 部分**，并要求它建议编辑 —— 特别是如何重构你的 `CLAUDE.md`。每个技巧都源自 Claude 团队或社区。
7. **订阅 [订阅部分](#-subscribe) 中的 Reddit 和 YouTube 频道** 以跟上社区的动态。

**🎬 视频 (Videos)**

<a href="https://www.youtube.com/watch?v=AkAhkalkRY4"><img src="!/thumbnail/video-1.png" alt="Watch on YouTube" width="240"></a>
<a href="https://youtu.be/lPjhM6BBK0Q"><img src="!/thumbnail/video-2.png" alt="Watch on YouTube" width="240"></a>

**📊 演示 (Presentations)**

<a href="https://github.com/shanraisshan/claude-code-best-practice/tree/main/presentation/2026-04-25-gdg-kolachi-cli-claude-code-gemini"><img src="!/thumbnail/presentation-1.png" alt="Claude Code & Gemini CLI — GDG Kolachi" width="240"></a>

<p align="center">
  <img src="!/claude-jumping.svg" alt="section divider" width="60" height="50">
</p>

<p align="center">
  <a href="https://github.com/trending?since=monthly"><img src="!/root/github-trending.png" alt="GitHub Trending" width="1200"></a><br>
  ✨2026年3月在 Github 上 trending✨
</p>

## Star History (星标历史)

[![Star History Chart](https://api.star-history.com/svg?repos=shanraisshan/claude-code-best-practice&type=Date&v=2)](https://star-history.com/#shanraisshan/claude-code-best-practice&Date)

<a href="https://github.com/shanraisshan/claude-code-best-practice/stargazers"><img src="https://img.shields.io/github/stars/shanraisshan/claude-code-best-practice?style=flat&label=%E2%98%85&labelColor=555&color=white" alt="GitHub Stars" align="center"></a> stars and counting

## Other Repos (其他仓库)

<table>
<tr>
<td align="center" width="140">
  <a href="https://github.com/shanraisshan/claude-code-hooks"><img src="!/claude-speaking.svg" alt="Claude Code Hooks" width="64" height="64"></a><br>
  <a href="https://github.com/shanraisshan/claude-code-hooks"><strong>Claude Code<br>Hooks</strong></a>
</td>
<td align="center" width="140">
  <a href="https://github.com/shanraisshan/codex-cli-best-practice"><img src="!/codex-jumping.svg" alt="Codex CLI Best Practice" width="64" height="64"></a><br>
  <a href="https://github.com/shanraisshan/codex-cli-best-practice"><strong>Codex CLI<br>Best Practice</strong></a>
</td>
<td align="center" width="140">
  <a href="https://github.com/shanraisshan/codex-cli-hooks"><img src="!/codex-speaking.svg" alt="Codex CLI Hooks" width="64" height="64"></a><br>
  <a href="https://github.com/shanraisshan/codex-cli-hooks"><strong>Codex CLI<br>Hooks</strong></a>
</td>
<td align="center" width="140">
  <a href="https://github.com/shanraisshan/gemini-cli-best-practice"><img src="!/gemini-jumping.svg" alt="Gemini CLI Best Practice" width="64" height="64"></a><br>
  <a href="https://github.com/shanraisshan/gemini-cli-best-practice"><strong>Gemini CLI<br>Best Practice</strong></a>
</td>
<td align="center" width="140">
  <a href="https://github.com/shanraisshan/gemini-cli-hooks"><img src="!/gemini-speaking.svg" alt="Gemini CLI Hooks" width="64" height="64"></a><br>
  <a href="https://github.com/shanraisshan/gemini-cli-hooks"><strong>Gemini CLI<br>Hooks</strong></a>
</td>
</tr>
</table>

## Developed by (开发者)

![Developed by](!/tags/developed-by.svg)

> | # | 工作流 | 描述 |
> |---|----------|-------------|
> | 1 | /workflows:development-workflows | 通过并行研究所有 10 个工作流仓库，更新 DEVELOPMENT WORKFLOWS 表和跨工作流分析报告 |
> | 2 | /workflows:skill-collections | 通过并行研究所有 5 个技能集合仓库，更新 SKILL COLLECTIONS 表 |
> | 3 | /workflows:agent-collections | 通过并行研究所有代理集合仓库，更新 AGENT COLLECTIONS 表 |
> | 4 | /workflows:best-practice:workflow-concepts | 使用最新的 Claude Code 功能和概念更新 README CONCEPTS 部分 |
> | 5 | /workflows:best-practice:workflow-claude-settings | 跟踪 Claude Code 设置报告更改并找出需要更新的内容 |
> | 6 | /workflows:best-practice:workflow-claude-subagents | 跟踪 Claude Code 子代理报告更改并找出需要更新的内容 |
> | 7 | /workflows:best-practice:workflow-claude-commands | 跟踪 Claude Code 命令报告更改并找出需要更新的内容 |
> | 8 | /workflows:best-practice:workflow-claude-skills | 跟踪 Claude Code 技能报告更改并找出需要更新的内容 |

## Extras (额外资源)

[![Claude for OSS](!/tags/claude-for-oss.svg)](https://claude.com/contact-sales/claude-for-oss)
[![Claude Community Ambassador](!/tags/claude-community-ambassador.svg)](https://claude.com/community/ambassadors)
[![Claude Certified Architect](!/tags/claude-certified-architect.svg)](https://anthropic.skilljar.com/claude-certified-architect-foundations-access-request)
[![Anthropic Academy](!/tags/anthropic-academy.svg)](https://anthropic.skilljar.com/)
[![Join Claude Pakistan community on WhatsApp](!/tags/whatsapp-claude-pakistan.svg)](https://chat.whatsapp.com/BDUV2stIS0c7X5uY7RY6nS)

<p align="center">
  <img src="!/claude-jumping.svg" alt="section divider" width="60" height="50">
</p>

## <img src="!/tags/sponsor-heart.svg" width="22" height="22" align="center"> 赞助我的工作

如果你喜欢我的工作，请我在 [Polar](https://buy.polar.sh/polar_cl_R6wjUESl8RiJD0iVaTyStBUV6WNuYvDmLJ0si1XXj4C) 上喝一杯奶茶 🍵

<a href="https://buy.polar.sh/polar_cl_R6wjUESl8RiJD0iVaTyStBUV6WNuYvDmLJ0si1XXj4C"><img src="!/tags/polar.svg" alt="Polar" width="40" height="40" align="center"></a> <a href="https://buy.polar.sh/polar_cl_R6wjUESl8RiJD0iVaTyStBUV6WNuYvDmLJ0si1XXj4C"><strong>Polar</strong></a>