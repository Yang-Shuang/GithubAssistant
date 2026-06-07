<p align="center">
  <h1 align="center">Claude Code Game Studios</h1>
  <p align="center">
    将单个 Claude Code 会话转变为完整的游戏开发工作室。
    <br />
    49 个 Agent。73 项技能。一支协同工作的 AI 团队。
  </p>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
  <a href=".claude/agents"><img src="https://img.shields.io/badge/agents-49-blueviolet" alt="49 Agents"></a>
  <a href=".claude/skills"><img src="https://img.shields.io/badge/skills-73-green" alt="73 Skills"></a>
  <a href=".claude/hooks"><img src="https://img.shields.io/badge/hooks-12-orange" alt="12 Hooks"></a>
  <a href=".claude/rules"><img src="https://img.shields.io/badge/rules-11-red" alt="11 Rules"></a>
  <a href="https://docs.anthropic.com/en/docs/claude-code"><img src="https://img.shields.io/badge/built%20for-Claude%20Code-f5f5f5?logo=anthropic" alt="Built for Claude Code"></a>
  <a href="https://www.buymeacoffee.com/donchitos3"><img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Support%20this%20project-FFDD00?logo=buymeacoffee&logoColor=black" alt="Buy Me a Coffee"></a>
  <a href="https://github.com/sponsors/Donchitos"><img src="https://img.shields.io/badge/GitHub%20Sponsors-Support%20this%20project-ea4aaa?logo=githubsponsors&logoColor=white" alt="GitHub Sponsors"></a>
</p>

---

## 为什么需要这个项目

使用 AI 独立开发游戏功能强大，但单个聊天会话缺乏结构。没人会阻止你硬编码魔法数字（Magic Numbers）、跳过设计文档或写出结构混乱的代码（Spaghetti Code）。没有 QA 审查环节，没有设计评审，也没有人问“这真的符合游戏的整体愿景吗？”

**Claude Code Game Studios** 通过为你的 AI 会话提供真实工作室的结构来解决这个问题。你得到的不再是一个通用助手，而是按工作室层级组织的 49 个专业 Agent——守护愿景的导演、负责各自领域的部门主管，以及执行具体工作的专家。每个 Agent 都有明确的职责、升级路径和质量关卡（Quality Gates）。

结果：你依然掌握所有决策权，但现在你拥有一个能提出正确问题、尽早发现错误并保持项目从头脑风暴到发布全程有序的团队。

---

## 目录

- [包含内容](#whats-included)
- [工作室层级](#studio-hierarchy)
- [斜杠命令](#slash-commands)
- [快速开始](#getting-started)
- [升级指南](#upgrading)
- [项目结构](#project-structure)
- [工作原理](#how-it-works)
- [设计理念](#design-philosophy)
- [自定义配置](#customization)
- [平台支持](#platform-support)
- [社区交流](#community)
- [支持本项目](#supporting-this-project)
- [许可证](#license)

---

## 包含内容

| 类别 | 数量 | 说明 |
|----------|-------|-------------|
| **Agents (智能体)** | 49 | 涵盖设计、编程、美术、音频、叙事、QA 和生产管理的专用子 Agent |
| **Skills (技能/命令)** | 73 | 覆盖工作流各阶段的斜杠命令（`/start`, `/design-system`, `/create-epics`, `/create-stories`, `/dev-story`, `/story-done` 等） |
| **Hooks (钩子脚本)** | 12 | 在提交、推送、资源变更、会话生命周期、Agent 审计追踪和漏洞检测时自动执行验证 |
| **Rules (规则)** | 11 | 编辑游戏逻辑、引擎、AI、UI、网络等代码时强制执行的按路径限定的编码规范 |
| **Templates (模板)** | 41 | GDD（游戏设计文档）、UX 规范、ADR（架构决策记录）、冲刺计划、HUD 设计、无障碍标准等文档模板 |

## 工作室层级

Agent 按三个层级组织，与现实中的游戏工作室运作方式一致：

```
Tier 1 — Directors (Opus)
  creative-director    technical-director    producer

Tier 2 — Department Leads (Sonnet)
  game-designer        lead-programmer       art-director
  audio-director       narrative-director    qa-lead
  release-manager      localization-lead

Tier 3 — Specialists (Sonnet/Haiku)
  gameplay-programmer  engine-programmer     ai-programmer
  network-programmer   tools-programmer      ui-programmer
  systems-designer     level-designer        economy-designer
  technical-artist     sound-designer        writer
  world-builder        ux-designer           prototyper
  performance-analyst  devops-engineer       analytics-engineer
  security-engineer    qa-tester             accessibility-specialist
  live-ops-designer    community-manager
```

### 引擎专家

模板包含了三大主流引擎的 Agent 集。请根据你的项目选择对应的配置：

| 引擎 | 主管 Agent | 子专业领域 |
|--------|-----------|-----------------|
| **Godot 4** | `godot-specialist` | GDScript、着色器（Shaders）、GDExtension |
| **Unity** | `unity-specialist` | DOTS/ECS、着色器/VFX、Addressables、UI Toolkit |
| **Unreal Engine 5** | `unreal-specialist` | GAS、蓝图（Blueprints）、网络同步（Replication）、UMG/CommonUI |

## 斜杠命令

在 Claude Code 中输入 `/` 即可调用全部 73 项技能：

**入门与导航**
`/start` `/help` `/project-stage-detect` `/setup-engine` `/adopt`

**游戏设计**
`/brainstorm` `/map-systems` `/design-system` `/quick-design` `/review-all-gdds` `/propagate-design-change`

**美术与资源**
`/art-bible` `/asset-spec` `/asset-audit`

**用户体验与界面设计**
`/ux-design` `/ux-review`

**架构设计**
`/create-architecture` `/architecture-decision` `/architecture-review` `/create-control-manifest`

**任务管理与冲刺**
`/create-epics` `/create-stories` `/dev-story` `/sprint-plan` `/sprint-status` `/story-readiness` `/story-done` `/estimate`

**评审与分析**
`/design-review` `/code-review` `/balance-check` `/content-audit` `/scope-check` `/perf-profile` `/tech-debt` `/gate-check` `/consistency-check` `/security-audit`

**质量保证与测试**
`/qa-plan` `/smoke-check` `/soak-test` `/regression-suite` `/test-setup` `/test-helpers` `/test-evidence-review` `/test-flakiness` `/skill-test` `/skill-improve`

**生产管理**
`/milestone-review` `/retrospective` `/bug-report` `/bug-triage` `/reverse-document` `/playtest-report`

**发布管理**
`/release-checklist` `/launch-checklist` `/changelog` `/patch-notes` `/hotfix` `/day-one-patch`

**创意与内容**
`/prototype` `/onboard` `/localize`

**团队编排**（协调多个 Agent 处理单一功能）
`/team-combat` `/team-narrative` `/team-ui` `/team-release` `/team-polish` `/team-audio` `/team-level` `/team-live-ops` `/team-qa`

## 快速开始

### 前置条件

- [Git](https://git-scm.com/)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (`npm install -g @anthropic-ai/claude-code`)
- **推荐安装**：[jq](https://jqlang.github.io/jq/)（用于钩子脚本验证）和 Python 3（用于 JSON 格式验证）

如果缺少可选工具，所有钩子脚本都会优雅降级——不会导致程序崩溃，只是会失去相应的验证功能。

### 环境配置

1. **克隆或使用为模板**：
   ```bash
   git clone https://github.com/Donchitos/Claude-Code-Game-Studios.git my-game
   cd my-game
   ```

2. **打开 Claude Code** 并启动会话：
   ```bash
   claude
   ```

3. **运行 `/start`** ——系统会询问你当前的进度（无想法、模糊概念、明确设计或已有代码），并引导你进入对应的工作流。不会做任何预设假设。

   如果你已经清楚需求，也可以直接跳转到特定技能：
   - `/brainstorm` — 从零探索游戏创意
   - `/setup-engine godot 4.6` — 配置你的引擎（若已明确需求）
   - `/project-stage-detect` — 分析现有项目

## 升级指南

正在使用旧版模板？请参阅 [UPGRADING.md](UPGRADING.md)，获取逐步迁移指南、版本变更详解，以及哪些文件可以直接覆盖、哪些需要手动合并的说明。

## 项目结构

```
CLAUDE.md                           # Master configuration
.claude/
  settings.json                     # Hooks, permissions, safety rules
  agents/                           # 49 agent definitions (markdown + YAML frontmatter)
  skills/                           # 73 slash commands (subdirectory per skill)
  hooks/                            # 12 hook scripts (bash, cross-platform)
  rules/                            # 11 path-scoped coding standards
  statusline.sh                     # Status line script (context%, model, stage, epic breadcrumb)
  docs/
    workflow-catalog.yaml           # 7-phase pipeline definition (read by /help)
    templates/                      # 41 document templates
src/                                # Game source code
assets/                             # Art, audio, VFX, shaders, data files
design/                             # GDDs, narrative docs, level designs
docs/                               # Technical documentation and ADRs
tests/                              # Test suites (unit, integration, performance, playtest)
tools/                              # Build and pipeline tools
prototypes/                         # Throwaway prototypes (isolated from src/)
production/                         # Sprint plans, milestones, release tracking
```

## 工作原理

### Agent 协作机制

Agent 遵循结构化的委托模型：

1. **垂直委托** ——导演向主管委派任务，主管向专家委派
2. **横向咨询** ——同级 Agent 可相互咨询，但无权做出跨领域的强制性决策
3. **冲突解决** ——分歧将上报至共同上级（设计类问题由 `creative-director` 裁决，技术类由 `technical-director` 裁决）
4. **变更同步** ——跨部门变更由 `producer` 统一协调
5. **领域边界** ——未经明确委托，Agent 不会修改其职责范围外的文件

### 协同工作，而非全自动

这**不是**一个自动驾驶系统。每个 Agent 都遵循严格的协作协议：

1. **提问** ——提出方案前先询问你的意见
2. **提供选项** ——展示 2-4 个备选方案及其优缺点
3. **你来做主** ——最终决策权始终在你手中
4. **草稿预览** ——定稿前会先展示工作草案
5. **审批确认** ——未经你的批准，不会执行任何写入操作

你始终掌控全局。Agent 提供的是结构化和专业知识，而非自主权。

### 自动化安全机制

**钩子（Hooks）**会在每次会话时自动运行：

| 钩子脚本 | 触发时机 | 功能说明 |
|------|---------|--------------|
| `validate-commit.sh` | PreToolUse (Bash) | 检查硬编码值、TODO 格式、JSON 有效性及设计文档章节——若非 `git commit` 命令则提前退出 |
| `validate-push.sh` | PreToolUse (Bash) | 警告向受保护分支推送代码的行为——若非 `git push` 命令则提前退出 |
| `validate-assets.sh` | PostToolUse (Write/Edit) | 验证命名规范与 JSON 结构——若文件不在 `assets/` 目录下则跳过 |
| `session-start.sh` | Session open | 显示当前分支及最近提交记录，便于快速定位上下文 |
| `detect-gaps.sh` | Session open | 检测全新项目（建议运行 `/start`）或在代码/原型存在时提示缺失的设计文档 |
| `pre-compact.sh` | Before compaction | 保存会话进度笔记 |
| `post-compact.sh` | After compaction | 提醒 Claude 从 `active.md` 恢复会话状态 |
| `notify.sh` | Notification event | 通过 PowerShell 发送 Windows 桌面通知 |
| `session-stop.sh` | Session close | 归档 `active.md` 至会话日志，并记录 Git 操作历史 |
| `log-agent.sh` | Agent spawned | 审计追踪开始——记录子 Agent 调用信息 |
| `log-agent-stop.sh` | Agent stops | 审计追踪结束——完成子 Agent 记录 |
| `validate-skill-change.sh` | PostToolUse (Write/Edit) | 提示在修改 `.claude/skills/` 后运行 `/skill-test` |

> **注意**：`validate-commit.sh`、`validate-assets.sh` 和 `validate-skill-change.sh` 会在每次调用 Bash/Write 工具时触发，并在命令或文件路径不相关时立即退出（返回码 0）。这是钩子脚本的正常行为——不会影响性能。

`settings.json` 中的**权限规则**会自动放行安全操作（如 `git status`、测试运行）并拦截危险操作（如强制推送、`rm -rf`、读取 `.env` 文件）。

### 按路径限定的编码规范

根据文件位置自动强制执行以下编码标准：

| 路径 | 强制规范 |
|------|----------|
| `src/gameplay/**` | 数据驱动数值、正确使用 delta time（时间增量）、禁止引用 UI |
| `src/core/**` | 热点路径零内存分配、线程安全、API 稳定性保障 |
| `src/ai/**` | 性能预算限制、可调试性设计、参数数据化 |
| `src/networking/**` | 服务器权威架构、版本化消息协议、安全性要求 |
| `src/ui/**` | 不持有游戏状态、支持本地化、符合无障碍标准 |
| `design/gdd/**` | 必须包含 8 个核心章节、公式格式规范、边界情况覆盖 |
| `tests/**` | 测试命名规范、覆盖率要求、Fixture 模式使用 |
| `prototypes/**` | 放宽标准要求、需附带 README、明确记录假设验证 |

## 设计理念

本模板基于专业的游戏开发实践：

- **MDA Framework（机制-动态-美学框架）** ——用于游戏设计的核心分析模型
- **Self-Determination Theory（自我决定理论）** ——通过自主性、胜任感、归属感设计玩家动机
- **Flow State Design（心流状态设计）** ——挑战与技能平衡以维持玩家投入度
- **Bartle Player Types（巴特尔玩家类型学）** ——用于受众定位与验证
- **Verification-Driven Development（测试驱动开发）** ——先编写测试，再进行实现

## 自定义配置

这是一个**模板**，而非封闭框架。所有内容均支持自定义：

- **增删 Agent** ——删除不需要的文件，为你的领域添加新 Agent
- **编辑 Agent 提示词** ——调整行为逻辑，注入项目专属知识
- **修改技能（Skills）** ——调整工作流以匹配团队流程
- **添加规则（Rules）** ——为项目的目录结构创建新的路径限定规范
- **调优钩子（Hooks）** ——调整验证严格度，新增检查项
- **选择引擎** ——使用 Godot、Unity 或 Unreal Agent 集（或不使用）
- **设置评审强度** ——`full`（全部导演关卡）、`lean`（仅阶段关卡）或 `solo`（无）。在 `/start` 时设定，或修改 `production/review-mode.txt`。也可在任何技能命令后追加 `--review solo` 临时覆盖。

## 平台支持

主要开发与测试环境为搭载 Git Bash 的 **Windows 10**。所有钩子脚本均采用 POSIX 兼容模式（使用 `grep -E` 而非 `grep -P`）并为缺失工具提供降级方案，因此应在 macOS 和 Linux 上正常运行。`notify.sh` 钩子通过 PowerShell 发送 Windows 桌面通知，在其他平台上为无操作（no-op）——macOS/Linux 的桌面通知功能尚未接入。跨平台测试仍在进行中；如遇特定平台报错，请提交 Issue。

## 社区交流

- **讨论区（Discussions）** ——用于提问、分享想法及展示你的作品：[GitHub Discussions](https://github.com/Donchitos/Claude-Code-Game-Studios/discussions)
- **问题反馈（Issues）** ——提交 Bug 报告与功能建议：[Bug reports and feature requests](https://github.com/Donchitos/Claude-Code-Game-Studios/issues)

---

## 支持本项目

Claude Code Game Studios 免费且开源。如果它为你节省了时间或助力游戏顺利上线，欢迎考虑赞助以支持持续开发：

<p>
  <a href="https://www.buymeacoffee.com/donchitos3"><img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me a Coffee"></a>
  &nbsp;
  <a href="https://github.com/sponsors/Donchitos"><img src="https://img.shields.io/badge/GitHub%20Sponsors-ea4aaa?style=for-the-badge&logo=githubsponsors&logoColor=white" alt="GitHub Sponsors"></a>
</p>

- **[Buy Me a Coffee](https://www.buymeacoffee.com/donchitos3)** — 一次性捐赠支持
- **[GitHub Sponsors](https://github.com/sponsors/Donchitos)** — 通过 GitHub 的长期赞助计划

赞助资金将用于维护技能库、开发新 Agent、跟进 Claude Code 及引擎 API 更新，以及响应社区问题。

---

*专为 Claude Code 打造。持续维护与扩展中——欢迎通过 [GitHub Discussions](https://github.com/Donchitos/Claude-Code-Game-Studios/discussions) 参与贡献。*

## 许可证

MIT 开源协议。详情请参阅 [LICENSE](LICENSE)。