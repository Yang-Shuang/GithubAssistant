<div align="center">
<img src="media/banner.png" alt="planning-with-files" width="100%">
</div>

# 基于文件的规划 (Planning with Files)

> **像 Manus 一样工作** —— Meta 以 **20 亿美元**收购的 AI Agent（智能体）公司。

[![Benchmark](https://img.shields.io/badge/Benchmark-96.7%25_pass_rate-brightgreen)](docs/evals.md)
[![A/B Verified](https://img.shields.io/badge/A%2FB_Blind-3%2F3_wins-brightgreen)](docs/evals.md)
[![SkillCheck Validated](https://img.shields.io/badge/SkillCheck-Validated-4c1)](https://getskillcheck.com)
[![Security Verified](https://img.shields.io/badge/Security-Audited_%26_Fixed_v2.21.0-blue)](docs/evals.md)

[![Skills Playground](https://skillsplayground.com/badges/installs/othmanadi-planning-with-files-planning-with-files.svg)](https://skillsplayground.com/skills/othmanadi-planning-with-files-planning-with-files/)
[![Downloads](https://skill-history.com/badge/othmanadi/planning-with-files.svg)](https://skill-history.com/othmanadi/planning-with-files)
[![Version](https://img.shields.io/badge/version-2.43.0-brightgreen)](https://github.com/OthmanAdi/planning-with-files/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Closed Issues](https://img.shields.io/github/issues-closed/OthmanAdi/planning-with-files?color=success)](https://github.com/OthmanAdi/planning-with-files/issues?q=is%3Aissue+is%3Aclosed)
[![Closed PRs](https://img.shields.io/github/issues-pr-closed/OthmanAdi/planning-with-files?color=success)](https://github.com/OthmanAdi/planning-with-files/pulls?q=is%3Apr+is%3Aclosed)

<details>
<summary><strong>💬 作者寄语</strong></summary>

感谢所有星标、分叉并分享此技能的朋友。该项目在不到 24 小时内迅速走红，社区的支持令人惊叹。

如果这项技能能帮你更高效地工作，那就是我最大的心愿。

</details>

<details>
<summary><strong>🌍 社区贡献与衍生项目</strong></summary>

### Forks & Extensions（分叉与扩展）

| Fork | Author | 功能说明 |
|------|--------|-----------------|
| [devis](https://github.com/st01cs/devis) | [@st01cs](https://github.com/st01cs) | 面试优先工作流，提供 `/devis:intv` 和 `/devis:impl` 命令，支持强制激活 |
| [multi-manus-planning](https://github.com/kmichels/multi-manus-planning) | [@kmichels](https://github.com/kmichels) | 多项目支持，SessionStart git 同步 |
| [plan-cascade](https://github.com/Taoidle/plan-cascade) | [@Taoidle](https://github.com/Taoidle) | 多级任务编排、并行执行、多智能体协作 |
| [agentfund-skill](https://github.com/RioTheGreat-ai/agentfund-skill) | [@RioTheGreat-ai](https://github.com/RioTheGreat-ai) | AI Agent 众筹，基于 Base 链的里程碑托管机制 |
| [openclaw-github-repo-commander](https://github.com/wd041216-bit/openclaw-github-repo-commander) | [@wd041216-bit](https://github.com/wd041216-bit) | 面向 OpenClaw 的 7 阶段 GitHub 仓库审计、优化与清理工作流 |

### Used in the Wild（实际应用）

| Project | 项目说明 |
|---------|-----------|
| [lincolnwan/Planning-with-files-copilot-agent](https://github.com/lincolnwan/Planning-with-files-copilot-agent) | 围绕 planning-with-files 技能构建的完整 Copilot Agent 仓库 |
| [cooragent/ClarityFinance](https://github.com/cooragent/ClarityFinance) | AI 金融智能体框架 —— 明确采用 Planning-with-Files 架构 |
| [oeftimie/vv-claude-harness](https://github.com/oeftimie/vv-claude-harness) | 基于 Manus 风格持久化 Markdown 规划构建的 Claude Code 运行环境 |
| [jessepwj/CCteam-creator](https://github.com/jessepwj/CCteam-creator) | 使用文件驱动规划的 AI Agent 团队编排技能 |

### Skill Registries & Hubs（技能注册中心）

| Registry | 项目说明 |
|----------|-----------|
| [buzhangsan/skill-manager](https://github.com/buzhangsan/skill-manager) | 双语 (EN/中文) 技能枢纽，索引 31,000+ Claude Code 技能 —— planning-with-files 支持一键安装。 |

*构建了衍生项目？[提交 Issue](https://github.com/OthmanAdi/planning-with-files/issues) 以便收录！*

</details>

<details>
<summary><strong>🤝 Contributors（贡献者）</strong></summary>

查看所有为该项目做出贡献的人员名单，请查阅 [CONTRIBUTORS.md](./CONTRIBUTORS.md)。

</details>

<details>
<summary><strong>📦 Releases & Session Recovery（版本更新与会话恢复）</strong></summary>

### 当前版本：v2.43.0

| Version | Highlights（核心更新） |
|---------|------------|
| **v2.43.0** | **CONTRIBUTING.md + OpenCode 文档修复 + `.continue`/`.gemini`/`.kiro` 变体同步至一致版本** (PR #171 by @Skulli485, issue #172 by @luyanfeng, issues #159/#160/#161)：仓库根目录首次引入 `CONTRIBUTING.md`，GitHub PR 创建流程会自动提示。修复了手动安装块中引用重复路径 (`planning-with-files/planning-with-files/SKILL.md`) 的问题，将 `docs/opencode.md` Quick Install 切换为 \`npx skills add\`。将三个历史滞后的 IDE SKILL.md 变体同步至 v2.43.0：`.continue` (落后 9 个版本)、`.gemini` (落后 9 个版本)、`.kiro` (落后 11 个版本)，同时保留各 IDE 特定的 frontmatter、钩子形状及 Kiro Agent Skill 布局。 |
| **v2.42.0** | **POSIX `init-session.sh` 移植 + plugin-vs-skill 安装透明度说明 + Topic Handoff 文档** (PR #169 and PR #170 by @carterusedulm2-maker)：`init-session.sh` 及其 7 个镜像文件将 `[[ ]]` bashism 替换为 POSIX `[ ]`，使 `tests/test_init_session_slug.py` 可在 `dash` (Ubuntu) 下通过 `sh` 调用时干净运行。SKILL.md 新增安装范围说明：`/plugin install` 会附带 `/plan-goal` 和 `/plan-loop` 的 `commands/` 文件夹，但 `npx skills add`（及 ClawHub）不会。文档内补充了两种包装器的备用流程，使纯技能会话可通过直接调用 Claude Code 原生 `/goal` 和 `/loop` 原语实现相同效果。`docs/quickstart.md` 和 `docs/workflow.md` 新增可选的 Topic Handoff Pattern（用于超长运行任务，在 `progress.md` 旁生成 `handoffs/<topic>.md`）。 |
| **v2.41.0** | **Windows exec-bit 测试跳过 + attestation-locking 文档** (PR #167 by @gauravvojha, Issue #166; PR #168 by @CleanDev-Fix, Issue #165)：`test_script_permissions.py` 现在会在 Windows 上通过类级 `pytest.mark.skipif(sys.platform == "win32")` 跳过测试，因为 NTFS 不存储 POSIX 可执行位；修复了自 v2.34.1 以来存在的 2 个 Windows exec-bit 失败问题。新增独立文档页 `docs/attestation-locking.md`，详细说明 `attest-plan.sh` 写入路径、原子临时重命名保证、可选的 `flock` 建议锁，以及并行会话推荐的 slug-mode 工作流。 |
| **v2.40.1** | **Pi adapter SKILL.md 同步缺口 + npm scope 修正** (PR #158 by @TomXPRIME)：`.pi` SKILL.md 在 v2.39.0 后滞后于 Claude Code 主版本；v2.40.1 向后移植了 Rule 7（完成后继续）、安全边界章节、扩展的 Scripts 章节（涵盖 `set-active-plan.sh`/`resolve-plan-dir.sh`/`attest-plan.sh` 及并行任务工作流），以及“向 task_plan.md 写入 Web 内容”的反模式行。Pi npm 包从非 scoped 的 `pi-planning-with-files` 重命名为 `@tomxprime/planning-with-files`，以匹配作者命名空间；安装文档同步更新。保留 Author、仓库、许可证和 Bug 报告 URL。 |
| **v2.40.0** | **Slug-mode 解析修复 + perf cache + KV-cache 清理 + Pi 误报修复** (9 项来自 v2.40 R&D 实验)：钩子解析顺序反转，使 slug-mode 优先于 legacy root；`.active_plan` 目标目录及内容通过安全标识符正则校验；`check-complete.sh` 现在尊重 `$PLAN_ID` 和 `.active_plan`；Pi 扩展 `isDangerousBashCommand` 替换为单词边界正则数组，避免误报 benign `git push origin <branch>`；mtime-keyed SHA-256 cache 降低 Windows Git Bash 下的 attestation-hook 延迟；`progress.md` 尾部时间戳标准化以保证 KV-cache 前缀稳定性；`resolve-plan-dir.sh` mtime 解析通过 python+perl fallback 实现 GNU/BSD/macOS/Alpine/Git Bash 跨平台兼容；`attest-plan.sh` 使用原子临时重命名配合可选 `flock` 修复并发写入竞态。130 pass / 2 pre-existing Windows exec-bit fails，新增 +20 测试用例。 |
| **v2.39.0** | **Pi Coding Agent full hook parity extension + Codex hooks flag fix** (PR #157 by @TomXPRIME, Issue #154 by @DLI1996)：`.pi` adapter 提供捆绑的 TypeScript 扩展，将八个 Pi 生命周期事件映射到与 Claude Code 技能相同的行为，采用四模式系统 (`auto`/`parity`/`cache-safe`/`notify`) 自动检测 DeepSeek 并保持 KV-cache 前缀稳定。Pi 运行时读取相同的 `.attestation` 文件（由 canonical v2.37 `attest-plan.sh` 写入），因此只需验证一次即可在两个运行时锁定计划。四个斜杠命令 (`/plan-status`, `/plan-attest`, `/plan-goal`, `/plan-loop`) 镜像其 Claude Code 对应项。另外，`docs/codex.md` 将 `codex_hooks = true` 替换为 `hooks = true` 以匹配 OpenAI 当前规范键，并添加别名说明以避免旧配置用户被迫迁移。 |
| **v2.38.1** | **Claude Code skill picker 中 Description 字段乱码** (via Discussion #153 by @bmyury)：钩子命令嵌入了 `'---BEGIN PLAN DATA---'` 计划注入分隔符；Claude Code 的技能发现加载器在第一个 `---` 处拆分 frontmatter，并将截断的值读取为 description。已全局替换为 `===BEGIN PLAN DATA===` / `===END PLAN DATA===`（涵盖 canonical SKILL.md、五种语言变体、`.codebuddy/.codex/.cursor` adapter 镜像及 `clawhub-upload`）。钩子执行与篡改验证未受影响；仅显示元数据。 |
| **v2.38.0** | **Claude Code turn-loop integration + OpenCode SQLite fix**：新增 PreCompact 钩子在 `/compact` 和 autoCompact 时触发，在压缩完成前提醒刷新进度，并在验证后打印当前 Plan-SHA256。新增 `/plan-goal` 斜杠命令与 Claude Code `/goal` (v2.1.139, May 12 2026) 组合：从当前计划推导终止条件。新增 `/plan-loop` 与 `/loop` (v2.1.72+) 组合：默认 10 分钟 tick 重新读取规划文件并运行 check-complete。新增 `templates/loop.md` 用于裸 `/loop` 的规划感知默认值。会话恢复重写以适配 OpenCode 的 SQLite 迁移。Codex 获得 `PermissionRequest` adapter，在权限提示时展示计划上下文。 |
| **v2.37.0** | **Hash attestation + parity bumper** (closes #150, #151)：`/plan-attest` 使用 SHA-256 锁定 `task_plan.md`；钩子在检测到篡改时阻止注入。`scripts/bump-version.py` + parity test 修复了 v2.34.1、v2.36.0、v2.36.2 和 v2.36.3 中“遗漏某个变体”的回归类问题。(感谢 @oaabahussain!) |
| **v2.36.3** | **并行规划脚本正式随技能发布**：`resolve-plan-dir.sh` 和 `set-active-plan.sh` 在 v2.36.0 安装时缺失；现已包含于 canonical + 所有 IDE 镜像中，并更新 SKILL.md 文档。 |
| **v2.36.2** | **Canonical script sync** (PR #149)：`skills/planning-with-files/scripts/init-session.sh` 在 v2.36.0 缺失 slug mode；现已与 IDE 镜像同步并添加回归测试。(感谢 @voidborne-d!) |
| **v2.36.1** | **安全加固**：移除 Stop hook cache 搜索，ExecutionPolicy Bypass 改为 RemoteSigned，新增注入分隔符。(Gen Agent Trust Hub FAIL 已解决) |
| **v2.36.0** | **并行计划隔离 + Codex 会话隔离** (closes #146, #148)：`init-session.sh` slug mode、`set-active-plan.sh`、`resolve-plan-dir.sh`，所有 Codex 钩子通过解析器路由，会话附加门控。**Hermes docs** (closes #147)：在 `docs/hermes.md` 添加集成说明。新增 34 个测试用例。(感谢 @githubYiheng, @09ashishkapoor, @shawnli1874!) |
| **v2.35.1** | **Shebang 移植修复**：将钩子脚本中的 `/bin/bash` 改为 `/usr/bin/env bash`，修复 NixOS 及其他系统中 bash 不在 `/bin/bash` 时的兼容性问题。(感谢 @Emin017!) |
| **v2.35.0** | **Hermes adapter + NLPM audit hardening**：支持 Hermes platform 17 (感谢 @bailob!)，NLPM audit 修复 Python PATH 解析、会话恢复注入上限、Pi PowerShell 语法 (感谢 @xiaolai!) |
| **v2.34.1** | **Stop hook Windows 移植修复** (closes #133)：`export SD=` 在 Windows Git Bash 钩子上下文中失败；fallback path 对插件缓存结构不正确。已在全局 13 个 SKILL.md 变体中修复。(感谢 @nazeshinjite!) |
| **v2.34.0** | **Codex hooks fully restored** (closes #132)：`.codex/hooks.json` + lifecycle scripts 回归（SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, Stop）。新增 Tessl CI 用于 SKILL.md 质量审查。修复 Exec bit。补充 4 位缺失贡献者。(感谢 @Leon-Algo, @popey!) |
| **v2.33.0** | **多语言扩展**：新增阿拉伯语、德语和西班牙语技能变体 (感谢社区贡献者！) |
| **v2.32.0** | Codex 会话恢复重写 (感谢 @ebrevdo!)，Loaditout A级安全徽章，Stop hook Git Bash 修复 |
| **v2.31.0** | Codex hooks.json 集成与完整生命周期钩子 (感谢 @Leon-Algo!) |
| **v2.30.1** | Fix: Codex 脚本可执行位恢复 (感谢 @Leon-Algo!) |
| **v2.30.0** | `CLAUDE_SKILL_DIR` 变量，IDE 配置移至 per-IDE branches，plugin.json 从 2.23.0 升级 |
| **v2.29.0** | Analytics workflow template：新增 `--template analytics` flag 用于数据探索会话 (感谢 @mvanhorn!) |
| **v2.28.0** | 繁体中文 (zh-TW) 技能变体 (感谢 @waynelee2048!) |
| **v2.26.2** | Fix: 钩子命令中的 `---` 破坏 YAML frontmatter 解析，现已正常注册 |
| **v2.26.1** | Fix: `/clear` 后会话恢复、Windows 路径清理与内容注入 (感谢 @tony-stark-eth!) |
| **v2.26.0** | IDE audit：Factory hooks, Copilot errorOccurred hook, Gemini hooks, bug fixes |
| **v2.18.2** | Mastra Code hooks fix (hooks.json + docs accuracy) |
| **v2.18.1** | Copilot 乱码字符完全修复 |
| **v2.18.0** | BoxLite sandbox runtime integration |
| **v2.17.0** | Mastra Code support + all IDE SKILL.md spec fixes |
| **v2.16.1** | Copilot 乱码字符修复：PS1 UTF-8 encoding + bash ensure_ascii (感谢 @Hexiaopi!) |
| **v2.16.0** | GitHub Copilot hooks support (感谢 @lincolnwan!) |
| **v2.27.0** | Kiro Agent Skill layout (感谢 @EListenX!) |
| **v2.15.1** | Session catchup false-positive fix (感谢 @gydx6!) |
| **v2.15.0** | `/plan:status` 命令，OpenCode compatibility fix |
| **v2.14.0** | Pi Agent support, OpenClaw docs update, Codex path fix |
| **v2.11.0** | `/plan` 命令以简化自动补全 |
| **v2.10.0** | Kiro steering files support |
| **v2.7.0** | Gemini CLI support |
| **v2.2.0** | Session recovery, Windows PowerShell, OS-aware hooks |

[View all releases](https://github.com/OthmanAdi/planning-with-files/releases) · [CHANGELOG](CHANGELOG.md)

> 并行计划隔离 (`.planning/YYYY-MM-DD-slug/` 目录) 和 Codex 会话隔离功能于 v2.36.0 发布。`experimental/isolated-planning` branch 为早期原型；master 现已成为规范版本位置。

---

### Session Recovery（会话恢复）

当你的上下文填满并运行 `/clear` 时，此技能会**自动恢复**你之前的会话。

**工作原理：**
1. 检查活跃 IDE 的会话存储中是否存在之前会话的数据（Claude Code 为 `~/.claude/projects/`，Codex 为 `~/.codex/sessions/`）
2. 查找规划文件上次更新的时间
3. 提取在此之后发生的对话内容（可能已丢失上下文）
4. 显示恢复报告以便你同步

**进阶技巧：** 禁用 auto-compact 以在清除前最大化保留上下文：
```json
{ "autoCompact": false }
```

</details>

<details>
<summary><strong>🛠️ Supported IDEs (17+ Platforms)（支持的集成环境）</strong></summary>

#### Enhanced Support (hooks + lifecycle automation)（增强支持：钩子 + 生命周期自动化）

这些 IDE 拥有专用的钩子配置，会在工具调用前自动重新读取你的计划、提醒更新进度，并在停止前验证完成状态：

| IDE | Installation Guide | Integration |
|-----|-------------------|-------------|
| Claude Code | [Installation](docs/installation.md) | Plugin + SKILL.md + Hooks |
| Cursor | [Cursor Setup](docs/cursor.md) | Skills + [hooks.json](https://cursor.com/docs/hooks) |
| GitHub Copilot | [Copilot Setup](docs/copilot.md) | [Hooks](https://docs.github.com/en/copilot/reference/hooks-configuration) (incl. errorOccurred) |
| Mastra Code | [Mastra Setup](docs/mastra.md) | Skills + [Hooks](https://mastra.ai/docs/mastra-code/configuration) |
| Gemini CLI | [Gemini Setup](docs/gemini.md) | Skills + [Hooks](https://geminicli.com/docs/hooks/) |
| Kiro | [Kiro Setup](docs/kiro.md) | [Agent Skills](https://kiro.dev/docs/skills/) |
| Codex | [Codex Setup](docs/codex.md) | [Skills + Hooks](https://developers.openai.com/codex/skills) |
| Hermes Agent | [Hermes Setup](docs/hermes.md) | Skill + Project Plugin |
| CodeBuddy | [CodeBuddy Setup](docs/codebuddy.md) | [Skills + Hooks](https://www.codebuddy.ai/docs/cli/skills) |
| FactoryAI Droid | [Factory Setup](docs/factory.md) | [Skills + Hooks](https://docs.factory.ai/cli/configuration/skills) |
| OpenCode | [OpenCode Setup](docs/opencode.md) | Skills + Custom session storage |

#### Standard Agent Skills Support（标准智能体技能支持）

这些 IDE 实现了 [Agent Skills](https://agentskills.io) 开放规范。使用 `npx skills add` 安装 —— 安装程序会自动将技能放置到各 IDE 的发现路径中：

| IDE | Installation Guide | Skill Discovery Path |
|-----|-------------------|---------------------|
| Continue | [Continue Setup](docs/continue.md) | `.continue/skills/` + [.prompt files](https://docs.continue.dev/customize/deep-dives/prompts) |
| Pi Agent | [Pi Agent Setup](docs/pi-agent.md) | `.pi/skills/` ([npm package](https://www.npmjs.com/package/@mariozechner/pi-coding-agent)) |
| OpenClaw | [OpenClaw Setup](docs/openclaw.md) | `.openclaw/skills/` ([docs](https://docs.openclaw.ai/tools/skills)) |
| Antigravity | [Antigravity Setup](docs/antigravity.md) | `.agent/skills/` ([docs](https://codelabs.developers.google.com/getting-started-with-antigravity-skills)) |
| Kilocode | [Kilocode Setup](docs/kilocode.md) | `.kilocode/skills/` ([docs](https://kilo.ai/docs/agent-behavior/skills)) |
| AdaL CLI (Sylph AI) | [AdaL Setup](docs/adal.md) | `.adal/skills/` ([docs](https://docs.sylph.ai/features/plugins-and-skills)) |

> **Note:** 如果你的 IDE 使用传统的 Rules 系统而非 Skills，请查看 [`legacy-rules-support`](https://github.com/OthmanAdi/planning-with-files/tree/legacy-rules-support) branch。

</details>

<details>
<summary><strong>🧱 Sandbox Runtimes (1 Platform)（沙箱运行时）</strong></summary>

| Runtime | Status | Guide | Notes |
|---------|--------|-------|-------|
| BoxLite | ✅ Documented | [BoxLite Setup](docs/boxlite.md) | 在硬件隔离的微虚拟机中运行 Claude Code + planning-with-files |

> **Note:** BoxLite 是沙箱运行时，而非 IDE。技能通过 [ClaudeBox](https://github.com/boxlite-ai/claudebox)（BoxLite 官方的 Claude Code 集成层）加载。

</details>

---

一个 Claude Code 插件，将你的工作流转变为使用持久化 Markdown 文件进行规划、进度跟踪和知识存储——这正是让 Manus 价值数十亿美元的核心模式。

[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-blue)](https://code.claude.com/docs/en/plugins)
[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-green)](https://code.claude.com/docs/en/skills)
[![Cursor Skills](https://img.shields.io/badge/Cursor-Skills-purple)](https://docs.cursor.com/context/skills)
[![Kilocode Skills](https://img.shields.io/badge/Kilocode-Skills-orange)](https://kilo.ai/docs/agent-behavior/skills)
[![Gemini CLI](https://img.shields.io/badge/Gemini%20CLI-Skills-4285F4)](https://geminicli.com/docs/cli/skills/)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skills-FF6B6B)](https://openclaw.ai)
[![Kiro](https://img.shields.io/badge/Kiro-Agent_Skill-00D4AA)](https://kiro.dev/docs/skills/)
[![AdaL CLI](https://img.shields.io/badge/AdaL%20CLI-Skills-9B59B6)](https://docs.sylph.ai/features/plugins-and-skills)
[![Pi Agent](https://img.shields.io/badge/Pi%20Agent-Skills-FF4081)](https://pi.dev)
[![GitHub Copilot](https://img.shields.io/badge/GitHub%20copilot-Hooks-000000)](https://docs.github.com/en/copilot/reference/hooks-configuration)
[![Mastra Code](https://img.shields.io/badge/Mastra%20Code-Skills-00BCD4)](https://code.mastra.ai)
[![Hermes](https://img.shields.io/badge/Hermes-Agent_Skill-5C7CFA)](docs/hermes.md)
[![BoxLite](https://img.shields.io/badge/BoxLite-Sandbox-6C3483)](https://boxlite.ai)

## Quick Install（快速安装）

```bash
npx skills add OthmanAdi/planning-with-files --skill planning-with-files -g
```

<details>
<summary><strong>🌐 Available in 5 other languages（支持其他 5 种语言）</strong></summary>

**🇸🇦 العربية / Arabic**
```bash
npx skills add OthmanAdi/planning-with-files --skill planning-with-files-ar -g
```

**🇩🇪 Deutsch / German**
```bash
npx skills add OthmanAdi/planning-with-files --skill planning-with-files-de -g
```

**🇪🇸 Español / Spanish**
```bash
npx skills add OthmanAdi/planning-with-files --skill planning-with-files-es -g
```

**🇨🇳 中文版 / Chinese (Simplified)**
```bash
npx skills add OthmanAdi/planning-with-files --skill planning-with-files-zh -g
```

**🇹🇼 正體中文版 / Chinese (Traditional)**
```bash
npx skills add OthmanAdi/planning-with-files --skill planning-with-files-zht -g
```

</details>

Works with Claude Code, Cursor, Codex, Gemini CLI, and 40+ agents supporting the [Agent Skills](https://agentskills.io) spec.

<details>
<summary><strong>🔧 Claude Code Plugin (Advanced Features)（Claude Code 插件高级功能）</strong></summary>

用于获取 Claude Code 专属功能（如 `/plan` 自动补全命令）：

```
/plugin marketplace add OthmanAdi/planning-with-files
/plugin install planning-with-files@planning-with-files
```

</details>

That's it! Now use one of these commands in Claude Code:

| Command | Autocomplete | Description |
|---------|--------------|-------------|
| `/planning-with-files:plan` | Type `/plan` | 开始规划会话 (v2.11.0+) |
| `/planning-with-files:status` | Type `/plan:status` | 一目了然地显示规划进度 (v2.15.0+) |
| `/planning-with-files:start` | Type `/planning` | 原始启动命令 |

**Alternative:** 如果你希望直接使用 `/planning-with-files`（无前缀），可将技能复制到本地文件夹：

**macOS/Linux:**
```bash
cp -r ~/.claude/plugins/cache/planning-with-files/planning-with-files/*/skills/planning-with-files ~/.claude/skills/
```

**Windows (PowerShell):**
```powershell
Copy-Item -Recurse -Path "$env:USERPROFILE\.claude\plugins\cache\planning-with-files\planning-with-files\*\skills\planning-with-files" -Destination "$env:USERPROFILE\.claude\skills\"
```

See [docs/installation.md](docs/installation.md) for all installation methods.

## Why This Skill?（为什么选择此技能？）

2025 年 12 月 29 日，[Meta 以 20 亿美元收购 Manus](https://techcrunch.com/2025/12/29/meta-just-bought-manus-an-ai-startup-everyone-has-been-talking-about/)。在短短 8 个月内，Manus 从发布到营收突破 1 亿美元。他们的秘诀？**上下文工程 (Context Engineering)**。

> “Markdown 是我磁盘上的‘工作记忆’。由于我采用迭代方式处理信息且活跃上下文有限，Markdown 文件充当了笔记草稿、进度检查点以及最终交付物构建模块的角色。”
> — Manus AI

## The Problem（核心痛点）

Claude Code（及大多数 AI Agent）存在以下问题：

- **易失性记忆** —— TodoWrite 工具在上下文重置时消失
- **目标漂移** —— 经过 50+ 次工具调用后，原始目标被遗忘
- **隐藏错误** —— 失败未被记录，导致相同错误反复发生
- **上下文塞满** —— 所有内容强行挤入上下文而非持久化存储

## The Solution: 3-File Pattern（解决方案：三文件模式）

针对每个复杂任务，创建三个文件：

```
task_plan.md      → 跟踪阶段与进度
findings.md       → 存储研究与发现结果
progress.md       → 会话日志与测试结果
```

### The Core Principle（核心原则）

```
Context Window = RAM (易失、有限)
Filesystem = Disk (持久化、无限)

→ 任何重要内容都应写入磁盘。
```

## The Manus Principles（Manus 核心原则）

| Principle | Implementation |
|-----------|----------------|
| Filesystem as memory | 存储于文件中，而非上下文中 |
| Attention manipulation | 决策前重新读取计划（通过钩子实现） |
| Error persistence | 在计划文件中记录失败 |
| Goal tracking | 复选框显示进度 |
| Completion verification | Stop hook 检查所有阶段完成状态 |

## Usage（使用方式）

安装后，AI Agent 将：

1. **询问你的任务** —— 如果未提供描述信息
2. **创建 `task_plan.md`, `findings.md` 和 `progress.md`** —— 位于你的项目目录中
3. **在重大决策前重新读取计划** —— 通过 PreToolUse hook
4. **提醒你在文件写入后更新状态** —— 通过 PostToolUse hook
5. **将发现结果存储于 `findings.md`** —— 而非塞满上下文
6. **记录错误** —— 供后续参考
7. **在停止前验证完成状态** —— 通过 Stop hook

Invoke with:
- `/planning-with-files:plan` - 输入 `/plan` 可在自动补全中找到 (v2.11.0+)
- `/planning-with-files:start` - 输入 `/planning` 可在自动补全中找到
- `/planning-with-files` - 仅当你已将技能复制到 `~/.claude/skills/` 时使用

See [docs/quickstart.md](docs/quickstart.md) for the full 5-step guide.

## Benchmark Results（基准测试结果）

使用 Anthropic 的 [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) 框架 (v2.22.0) 进行正式评估。10 个并行子智能体，5 种任务类型，30 项客观可验证断言，3 次盲测 A/B 对比。

| Test | with_skill | without_skill |
|------|-----------|---------------|
| Pass rate (30 assertions) | **96.7%** (29/30) | 6.7% (2/30) |
| 3-file pattern followed | 5/5 evals | 0/5 evals |
| Blind A/B wins | **3/3 (100%)** | 0/3 |
| Avg rubric score | **10.0/10** | 6.8/10 |

[Full methodology and results](docs/evals.md) · [Technical write-up](docs/article.md)

## Key Rules（核心规则）

1. **先创建计划** —— 切勿在缺少 `task_plan.md` 的情况下开始
2. **两动作原则** —— 每次执行 view/browser 操作后保存发现结果
3. **记录所有错误** —— 它们有助于避免重复犯错
4. **绝不重复失败** —— 跟踪尝试次数，调整方法

## When to Use（适用场景）

**Use this pattern for:** (适用于)
- Multi-step tasks (3+ steps) - 多步骤任务（3 步及以上）
- Research tasks - 研究类任务
- Building/creating projects - 构建/创建项目
- Tasks spanning many tool calls - 涉及大量工具调用的任务

**Skip for:** (可跳过)
- Simple questions - 简单问题
- Single-file edits - 单文件编辑
- Quick lookups - 快速查询

## File Structure（文件结构）

```
planning-with-files/
├── commands/                # Plugin commands
│   ├── plan.md              # /planning-with-files:plan command (v2.11.0+)
│   ├── plan-ar.md           # Arabic /plan command (v2.33.0+)
│   ├── plan-de.md           # German /plan command (v2.33.0+)
│   ├── plan-es.md           # Spanish /plan command (v2.33.0+)
│   └── start.md             # /planning-with-files:start command
├── templates/               # Root-level templates (for CLAUDE_PLUGIN_ROOT)
├── scripts/                 # Root-level scripts (for CLAUDE_PLUGIN_ROOT)
├── docs/                    # Documentation
│   ├── installation.md
│   ├── quickstart.md
│   ├── workflow.md
│   ├── troubleshooting.md
│   ├── gemini.md            # Gemini CLI setup
│   ├── cursor.md
│   ├── windows.md
│   ├── kilocode.md
│   ├── codex.md
│   ├── opencode.md
│   ├── mastra.md             # Mastra Code setup
│   └── boxlite.md            # BoxLite sandbox setup
├── examples/                # Integration examples
│   └── boxlite/             # BoxLite quickstart
│       ├── README.md
│       └── quickstart.py
├── planning-with-files/     # Plugin skill folder
│   ├── SKILL.md
│   ├── templates/
│   └── scripts/
├── skills/                  # Skill variants
│   ├── planning-with-files/     # English (default)
│   │   ├── SKILL.md
│   │   ├── examples.md
│   │   ├── reference.md
│   │   ├── templates/
│   │   └── scripts/
│   │       ├── init-session.sh
│   │       ├── check-complete.sh
│   │       ├── init-session.ps1   # Windows PowerShell
│   │       └── check-complete.ps1 # Windows PowerShell
│   ├── planning-with-files-ar/   # Arabic (v2.33.0+)
│   │   ├── SKILL.md
│   │   ├── templates/
│   │   └── scripts/
│   ├── planning-with-files-de/   # German (v2.33.0+)
│   │   ├── SKILL.md
│   │   ├── templates/
│   │   └── scripts/
│   ├── planning-with-files-es/   # Spanish (v2.33.0+)
│   │   ├── SKILL.md
│   │   ├── templates/
│   │   └── scripts/
│   ├── planning-with-files-zh/   # Chinese Simplified (v2.25.0+)
│   └── planning-with-files-zht/  # Chinese Traditional (v2.28.0+)
├── .gemini/                 # Gemini CLI skills + hooks
│   ├── settings.json        # Hook configuration (v2.26.0)
│   ├── hooks/               # Hook scripts (SessionStart, BeforeTool, AfterTool, BeforeModel, SessionEnd)
│   └── skills/
│       └── planning-with-files/
├── .codex/                  # Codex CLI skills + hooks
│   └── skills/
├── .opencode/               # OpenCode skills (custom session storage)
│   └── skills/
├── .claude-plugin/          # Plugin manifest
├── .cursor/                 # Cursor skills + hooks
│   ├── hooks.json           # Hook configuration
│   ├── hooks/               # Hook scripts (bash + PowerShell)
│   └── skills/
├── .codebuddy/              # CodeBuddy skills + hooks
│   └── skills/
├── .factory/                # FactoryAI Droid skills + hooks (v2.26.0)
│   └── skills/
├── .pi/                     # Pi Agent skills (npm package)
│   └── skills/
│       └── planning-with-files/
├── .continue/               # Continue.dev skills + prompt files
│   ├── prompts/             # .prompt file for slash commands
│   └── skills/
├── .github/                 # GitHub Copilot hooks (incl. errorOccurred)
│   └── hooks/
│       ├── planning-with-files.json  # Hook configuration
│       └── scripts/         # Hook scripts (bash + PowerShell)
├── .mastracode/             # Mastra Code skills + hooks
│   └── skills/
├── .kiro/                   # Kiro Agent Skills (v2.27.0+)
│   └── skills/
├── CHANGELOG.md
├── CITATION.cff
├── LICENSE
└── README.md
```

## Documentation（文档）

All platform setup guides and documentation are in the [docs/](./docs/) folder.

## Acknowledgments（致谢）

- **Manus AI** — 率先开创上下文工程模式
- **Anthropic** — 提供 Claude Code、Agent Skills 及 Plugin 系统
- **Lance Martin** — 提供详细的 Manus 架构分析
- Based on [Context Engineering for AI Agents](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)

## Contributing（贡献指南）

欢迎贡献！请：
1. Fork the repository (分叉仓库)
2. Create a feature branch (创建功能分支)
3. Submit a pull request (提交 Pull Request)

## License（许可证）

MIT License — feel free to use, modify, and distribute.

---

**Author:** [Ahmad Othman Ammar Adi](https://github.com/OthmanAdi)

## Star History

<a href="https://repostars.dev/?repos=OthmanAdi%2Fplanning-with-files&theme=copper"><img src="https://repostars.dev/api/embed?repo=OthmanAdi%2Fplanning-with-files&theme=copper" width="100%" alt="Star History Chart" /></a>