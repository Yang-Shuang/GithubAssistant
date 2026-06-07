# Claude Code 架构研究

> **简介**：本项目是一个专注于 CLI Agent（命令行智能体）架构的学习与研究仓库。所有资料均完全汇编自公开的网络参考资料与社区讨论，特别聚焦于高度流行的 CLI Agent `claude-code` 的公开信息。我们的目的是帮助开发者更好地理解并利用 Agent 技术。未来我们将继续分享更多关于 Agent 架构的见解与实践讨论。感谢您的支持！

> **免责声明**：本仓库所有内容仅供技术研究、学习与爱好者之间的技术交流使用。**严禁用于商业用途**。任何个人、组织或实体不得将本内容用于商业目的、盈利活动、非法行为或其他未经授权的场景。如果任何内容侵犯了您的合法权益、知识产权或其他利益，请联系我们，我们将核实后立即删除。


**语言**：**English** | [中文](README_CN.md) | [한국어](README_KR.md) | [日本語](README_JA.md)

---

## 目录参考

- [深度分析报告 (`docs/`)](#deep-analysis-reports-docs) — 遥测、代号、卧底模式、远程控制、未来路线图
- [目录结构参考](#directory-reference) — 代码结构树
- [架构概览](#architecture-overview) — 入口 → 查询引擎 → 工具/服务/状态
- [工具系统与权限](#tool-system-architecture) — 40+ 种工具、权限流程、子智能体
- [12 层渐进式 Harness（运行框架）机制](#the-12-progressive-harness-mechanisms) — Claude Code 如何在 Agent 循环之上构建生产级功能

---

## 深度分析报告 (`docs/`)

基于公开网络参考资料和社区讨论编译的 Claude Code v2.1.88 深度分析报告。支持四语（EN/JA/KO/ZH）。

```
docs/
├── en/                                        # English
│   ├── [01-telemetry-and-privacy.md]          # Telemetry & Privacy — what's collected, why you can't opt out
│   ├── [02-hidden-features-and-codenames.md]  # Codenames (Capybara/Tengu/Numbat), feature flags, internal vs external
│   ├── [03-undercover-mode.md]                # Undercover Mode — hiding AI authorship in open-source repos
│   ├── [04-remote-control-and-killswitches.md]# Remote Control — managed settings, killswitches, model overrides
│   └── [05-future-roadmap.md]                 # Future Roadmap — Numbat, KAIROS, voice mode, unreleased tools
│
├── ja/                                        # 日本語
│   ├── [01-テレメトリとプライバシー.md]          # テレメトリとプライバシー — 収集項目、無効化不可の理由
│   ├── [02-隠し機能とコードネーム.md]           # 隠し機能 — モデルコードネーム、feature flag、内部/外部ユーザーの違い
│   ├── [03-アンダーカバーモード.md]             # アンダーカバーモード — オープンソースでのAI著作隠匿
│   ├── [04-リモート制御とキルスイッチ.md]       # リモート制御 — 管理設定、キルスイッチ、モデルオーバーライド
│   └── [05-今後のロードマップ.md]               # 今後のロードマップ — Numbat、KAIROS、音声モード、未公開ツール
│
├── ko/                                        # 한국어
│   ├── [01-텔레메트리와-프라이버시.md]          # 텔레메트리 및 프라이버시 — 수집 항목, 비활성화 불가 이유
│   ├── [02-숨겨진-기능과-코드네임.md]          # 숨겨진 기능 — 모델 코드네임, feature flag, 내부/외부 사용자 차이
│   ├── [03-언더커버-모드.md]                   # 언더커버 모드 — 오픈소스에서 AI 저작 은폐
│   ├── [04-원격-제어와-킬스위치.md]            # 원격 제어 — 관리 설정, 킬스위치, 모델 오버라이드
│   └── [05-향후-로드맵.md]                     # 향후 로드맵 — Numbat, KAIROS, 음성 모드, 미공개 도구
│
└── zh/                                        # 中文
    ├── [01-遥测与隐私分析.md]                    # 遥测与隐私 — 收集了什么，为什么无法退出
    ├── [02-隐藏功能与模型代号.md]                # 隐藏功能 — 模型代号，feature flag，内外用户差异
    ├── [03-卧底模式分析.md]                     # 卧底模式 — 在开源项目中隐藏 AI 身份
    ├── [04-远程控制与紧急开关.md]                # 远程控制 — 托管设置，紧急开关，模型覆盖
    └── [05-未来路线图.md]                       # 未来路线图 — Numbat，KAIROS，语音模式，未上线工具
```

> Click any filename above to jump to the full report.

| # | 主题 | 关键发现 |
|---|-------|-------------|
| 01 | **遥测与隐私** | 双分析数据源（1P, Datadog）。环境指纹、进程指标、每次事件附带仓库哈希。**无 UI 选项可退出**第一方日志记录。`OTEL_LOG_TOOL_DETAILS=1` 启用完整工具输入捕获。 |
| 02 | **隐藏功能与代号** | 动物代号（Capybara v8, Tengu, Fennec→Opus 4.6, **Numbat** 下一代）。特性标志使用随机词组（如 `tengu_frond_boric`）掩盖用途。内部用户获得更优提示、验证智能体与努力锚点。隐藏命令：`/btw`, `/stickers`。 |
| 03 | **卧底模式** | 官方员工在公开仓库中自动进入卧底模式。模型指令：“不要暴露身份”——剥离所有 AI 署名，以“人类开发者”风格编写提交。**无强制关闭选项**。引发开源社区透明度争议。 |
| 04 | **远程控制** | 每小时轮询 `/api/claude_code/settings`。危险变更会显示拦截对话框——**拒绝 = 应用退出**。6+ 个紧急开关（绕过权限、极速模式、语音模式、分析数据源）。GrowthBook 标志可在未经同意的情况下改变任何用户行为。 |
| 05 | **未来路线图** | 确认代号 **Numbat**。Opus 4.7 / Sonnet 4.8 开发中。**KAIROS** = 完全自主 Agent 模式，带 `<tick>` 心跳、推送通知、PR 订阅。语音模式（按键通话）就绪但受限。发现 17 个未发布工具。 |

---

## 版权与声明

```text
This repository is provided strictly for technical research and educational purposes.
Commercial use is strictly prohibited.

If you are the copyright owner and believe this repository content infringes your rights,
please contact the repository owner for immediate removal.
```

---

## 统计信息

| Item | Count |
|------|-------|
| Files (.ts/.tsx) | ~1,884 |
| Lines | ~512,664 |
| Largest single file | `query.ts` (~785KB) |
| Built-in tools | ~40+ |
| Slash commands | ~80+ |
| Dependencies (node_modules) | ~192 packages |
| Runtime | Bun (compiled to Node.js >= 18 bundle) |

---

## Agent（智能体）基础模式

```
                    THE CORE LOOP
                    =============

    User --> messages[] --> Claude API --> response
                                          |
                                stop_reason == "tool_use"?
                               /                          \
                             yes                           no
                              |                             |
                        execute tools                    return text
                        append tool_result
                        loop back -----------------> messages[]


    That is the minimal agent loop. Claude Code wraps this loop
    with a production-grade harness: permissions, streaming,
    concurrency, compaction, sub-agents, persistence, and MCP.
```

---

## 目录结构参考

```
src/
├── main.tsx                 # REPL bootstrap, 4,683 lines
├── QueryEngine.ts           # SDK/headless query lifecycle engine
├── query.ts                 # Main agent loop (785KB, largest file)
├── Tool.ts                  # Tool interface + buildTool factory
├── Task.ts                  # Task types, IDs, state base
├── tools.ts                 # Tool registry, presets, filtering
├── commands.ts              # Slash command definitions
├── context.ts               # User input context
├── cost-tracker.ts          # API cost accumulation
├── setup.ts                 # First-run setup flow
│
├── bridge/                  # Claude Desktop / remote bridge
│   ├── bridgeMain.ts        #   Session lifecycle manager
│   ├── bridgeApi.ts         #   HTTP client
│   ├── bridgeConfig.ts      #   Connection config
│   ├── bridgeMessaging.ts   #   Message relay
│   ├── sessionRunner.ts     #   Process spawning
│   ├── jwtUtils.ts          #   JWT refresh
│   ├── workSecret.ts        #   Auth tokens
│   └── capacityWake.ts      #   Capacity-based wakeup
│
├── cli/                     # CLI infrastructure
│   ├── handlers/            #   Command handlers
│   └── transports/          #   I/O transports (stdio, structured)
│
├── commands/                # ~80 slash commands
│   ├── agents/              #   Agent management
│   ├── compact/             #   Context compaction
│   ├── config/              #   Settings management
│   ├── help/                #   Help display
│   ├── login/               #   Authentication
│   ├── mcp/                 #   MCP server management
│   ├── memory/              #   Memory system
│   ├── plan/                #   Plan mode
│   ├── resume/              #   Session resume
│   ├── review/              #   Code review
│   └── ...                  #   70+ more commands
│
├── components/              # React/Ink terminal UI
│   ├── design-system/       #   Reusable UI primitives
│   ├── messages/            #   Message rendering
│   ├── permissions/         #   Permission dialogs
│   ├── PromptInput/         #   Input field + suggestions
│   ├── LogoV2/              #   Branding + welcome screen
│   ├── Settings/            #   Settings panels
│   ├── Spinner.tsx          #   Loading indicators
│   └── ...                  #   40+ component groups
│
├── entrypoints/             # Application entry points
│   ├── cli.tsx              #   CLI main (version, help, daemon)
│   ├── sdk/                 #   Agent SDK (types, sessions)
│   └── mcp.ts               #   MCP server entry
│
├── hooks/                   # React hooks
│   ├── useCanUseTool.tsx    #   Permission checking
│   ├── useReplBridge.tsx    #   Bridge connection
│   ├── notifs/              #   Notification hooks
│   └── toolPermission/      #   Tool permission handlers
│
├── services/                # Business logic layer
│   ├── api/                 #   Claude API client
│   │   ├── claude.ts        #     Streaming API calls
│   │   ├── errors.ts        #     Error categorization
│   │   └── withRetry.ts     #     Retry logic
│   ├── analytics/           #   Telemetry + GrowthBook
│   ├── compact/             #   Context compression
│   ├── mcp/                 #   MCP connection management
│   ├── tools/               #   Tool execution engine
│   │   ├── StreamingToolExecutor.ts  # Parallel tool runner
│   │   └── toolOrchestration.ts      # Batch orchestration
│   ├── plugins/             #   Plugin loader
│   └── settingsSync/        #   Cross-device settings
│
├── state/                   # Application state
│   ├── AppStateStore.ts     #   Store definition
│   └── AppState.tsx         #   React provider + hooks
│
├── tasks/                   # Task implementations
│   ├── LocalShellTask/      #   Bash command execution
│   ├── LocalAgentTask/      #   Sub-agent execution
│   ├── RemoteAgentTask/     #   Remote agent via bridge
│   ├── InProcessTeammateTask/ # In-process teammate
│   └── DreamTask/           #   Background thinking
│
├── tools/                   # 40+ tool implementations
│   ├── AgentTool/           #   Sub-agent spawning + fork
│   ├── BashTool/            #   Shell command execution
│   ├── FileReadTool/        #   File reading (PDF, image, etc)
│   ├── FileEditTool/        #   String-replace editing
│   ├── FileWriteTool/       #   Full file creation
│   ├── GlobTool/            #   File pattern search
│   ├── GrepTool/            #   Content search (ripgrep)
│   ├── WebFetchTool/        #   HTTP fetching
│   ├── WebSearchTool/       #   Web search
│   ├── MCPTool/             #   MCP tool wrapper
│   ├── SkillTool/           #   Skill invocation
│   ├── AskUserQuestionTool/ #   User interaction
│   └── ...                  #   30+ more tools
│
├── types/                   # Type definitions
│   ├── message.ts           #   Message discriminated unions
│   ├── permissions.ts       #   Permission types
│   ├── tools.ts             #   Tool progress types
│   └── ids.ts               #   Branded ID types
│
├── utils/                   # Utilities (largest directory)
│   ├── permissions/         #   Permission rule engine
│   ├── messages/            #   Message formatting
│   ├── model/               #   Model selection logic
│   ├── settings/            #   Settings management
│   ├── sandbox/             #   Sandbox runtime adapter
│   ├── hooks/               #   Hook execution
│   ├── memory/              #   Memory system utils
│   ├── git/                 #   Git operations
│   ├── github/              #   GitHub API
│   ├── bash/                #   Bash execution helpers
│   ├── swarm/               #   Multi-agent swarm
│   ├── telemetry/           #   Telemetry reporting
│   └── ...                  #   30+ more util groups
│
└── vendor/                  # Native module source stubs
    ├── audio-capture-src/   #   Audio input
    ├── image-processor-src/ #   Image processing
    ├── modifiers-napi-src/  #   Native modifiers
    └── url-handler-src/     #   URL handling
```

---

## 架构概览

```
┌─────────────────────────────────────────────────────────────────────┐
│                         ENTRY LAYER                                 │
│  cli.tsx ──> main.tsx ──> REPL.tsx (interactive)                   │
│                     └──> QueryEngine.ts (headless/SDK)              │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                       QUERY ENGINE                                  │
│  submitMessage(prompt) ──> AsyncGenerator<SDKMessage>               │
│    │                                                                │
│    ├── fetchSystemPromptParts()    ──> assemble system prompt       │
│    ├── processUserInput()          ──> handle /commands             │
│    ├── query()                     ──> main agent loop              │
│    │     ├── StreamingToolExecutor ──> parallel tool execution       │
│    │     ├── autoCompact()         ──> context compression          │
│    │     └── runTools()            ──> tool orchestration           │
│    └── yield SDKMessage            ──> stream to consumer           │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                 ▼
┌──────────────────┐ ┌─────────────────┐ ┌──────────────────┐
│   TOOL SYSTEM    │ │  SERVICE LAYER  │ │   STATE LAYER    │
│                  │ │                 │ │                  │
│ Tool Interface   │ │ api/claude.ts   │ │ AppState Store   │
│  ├─ call()       │ │  API client     │ │  ├─ permissions  │
│  ├─ validate()   │ │ compact/        │ │  ├─ fileHistory  │
│  ├─ checkPerms() │ │  auto-compact   │ │  ├─ agents       │
│  ├─ render()     │ │ mcp/            │ │  └─ fastMode     │
│  └─ prompt()     │ │  MCP protocol   │ │                  │
│                  │ │ analytics/      │ │ React Context    │
│ 40+ Built-in:    │ │  telemetry      │ │  ├─ useAppState  │
│  ├─ BashTool     │ │ tools/          │ │  └─ useSetState  │
│  ├─ FileRead     │ │  executor       │ │                  │
│  ├─ FileEdit     │ │ plugins/        │ └──────────────────┘
│  ├─ Glob/Grep    │ │  loader         │
│  ├─ AgentTool    │ │ settingsSync/   │
│  ├─ WebFetch     │ │  cross-device   │
│  └─ MCPTool      │ │ oauth/          │
│                  │ │  auth flow      │
└──────────────────┘ └─────────────────┘
              │                │
              ▼                ▼
┌──────────────────┐ ┌─────────────────┐
│   TASK SYSTEM    │ │   BRIDGE LAYER  │
│                  │ │                 │
│ Task Types:      │ │ bridgeMain.ts   │
│  ├─ local_bash   │ │  session mgmt   │
│  ├─ local_agent  │ │ bridgeApi.ts    │
│  ├─ remote_agent │ │  HTTP client    │
│  ├─ in_process   │ │ workSecret.ts   │
│  ├─ dream        │ │  auth tokens    │
│  └─ workflow     │ │ sessionRunner   │
│                  │ │  process spawn  │
│ ID: prefix+8chr  │ └─────────────────┘
│  b=bash a=agent  │
│  r=remote t=team │
└──────────────────┘
```

---

## 数据流：单次查询生命周期

```
 USER INPUT (prompt / slash command)
     │
     ▼
 processUserInput()                ← parse /commands, build UserMessage
     │
     ▼
 fetchSystemPromptParts()          ← tools → prompt sections, CLAUDE.md memory
     │
     ▼
 recordTranscript()                ← persist user message to disk (JSONL)
     │
     ▼
 ┌─→ normalizeMessagesForAPI()     ← strip UI-only fields, compact if needed
 │   │
 │   ▼
 │   Claude API (streaming)        ← POST /v1/messages with tools + system prompt
 │   │
 │   ▼
 │   stream events                 ← message_start → content_block_delta → message_stop
 │   │
 │   ├─ text block ──────────────→ yield to consumer (SDK / REPL)
 │   │
 │   └─ tool_use block?
 │       │
 │       ▼
 │   StreamingToolExecutor         ← partition: concurrent-safe vs serial
 │       │
 │       ▼
 │   canUseTool()                  ← permission check (hooks + rules + UI prompt)
 │       │
 │       ├─ DENY ────────────────→ append tool_result(error), continue loop
 │       │
 │       └─ ALLOW
 │           │
 │           ▼
 │       tool.call()               ← execute the tool (Bash, Read, Edit, etc.)
 │           │
 │           ▼
 │       append tool_result        ← push to messages[], recordTranscript()
 │           │
 └─────────┘                      ← loop back to API call
     │
     ▼ (stop_reason != "tool_use")
 yield result message              ← final text, usage, cost, session_id
```

---

## 工具系统架构

```
                    TOOL INTERFACE
                    ==============

    buildTool(definition) ──> Tool<Input, Output, Progress>

    Every tool implements:
    ┌────────────────────────────────────────────────────────┐
    │  LIFECYCLE                                             │
    │  ├── validateInput()      → reject bad args early     │
    │  ├── checkPermissions()   → tool-specific authz       │
    │  └── call()               → execute and return result │
    │                                                        │
    │  CAPABILITIES                                          │
    │  ├── isEnabled()          → feature gate check        │
    │  ├── isConcurrencySafe()  → can run in parallel?      │
    │  ├── isReadOnly()         → no side effects?          │
    │  ├── isDestructive()      → irreversible ops?         │
    │  └── interruptBehavior()  → cancel or block on user?  │
    │                                                        │
    │  RENDERING (React/Ink)                                 │
    │  ├── renderToolUseMessage()     → input display        │
    │  ├── renderToolResultMessage()  → output display       │
    │  ├── renderToolUseProgressMessage() → spinner/status   │
    │  └── renderGroupedToolUse()     → parallel tool groups │
    │                                                        │
    │  AI FACING                                             │
    │  ├── prompt()             → tool description for LLM  │
    │  ├── description()        → dynamic description       │
    │  └── mapToolResultToAPI() → format for API response   │
    └────────────────────────────────────────────────────────┘
```

### 完整工具清单

| FILE OPERATIONS          | SEARCH & DISCOVERY        | EXECUTION                  | INTERACTION                | PLANNING & WORKFLOW              | MCP PROTOCOL               | SKILLS & EXTENSIONS            | SYSTEM                   |
|--------------------------|---------------------------|----------------------------|----------------------------|----------------------------------|----------------------------|--------------------------------|--------------------------|
| FileReadTool             | GlobTool                  | BashTool                   | AskUserQuestionTool        | EnterPlanModeTool                | MCPTool                    | ConfigTool                     | SkillTool                |
| FileEditTool             | GrepTool                  | PowerShellTool            | BriefTool                  | ExitPlanModeTool                 | ListMcpResourcesTool       | ScheduleCronTool               | SleepTool                |
| FileWriteTool            | ToolSearchTool            |                            |                            | EnterWorktreeTool                | ReadMcpResourceTool        | LSPTool                        | TungstenTool             |
| NotebookEditTool         |                           |                            |                            | ExitWorktreeTool                 |                            |                                |                          |
| WEB & NETWORK            | AGENT / TASK              |                            |                            | TodoWriteTool                    |                            |                                |                          |
| WebFetchTool             | AgentTool                 |                            |                            |                                  |                            |                                |                          |
| WebSearchTool            | SendMessageTool           |                            |                            |                                  |                            |                                |                          |
|                          | TeamCreateTool            |                            |                            |                                  |                            |                                |                          |
|                          | TeamDeleteTool            |                            |                            |                                  |                            |                                |                          |
|                          | TaskCreateTool            |                            |                            |                                  |                            |                                |                          |
|                          | TaskGetTool               |                            |                            |                                  |                            |                                |                          |
|                          | TaskUpdateTool            |                            |                            |                                  |                            |                                |                          |
|                          | TaskListTool              |                            |                            |                                  |                            |                                |                          |
|                          | TaskStopTool              |                            |                            |                                  |                            |                                |                          |
|                          | TaskOutputTool            |                            |                            |                                  |                            |                                |                          |

---

## 权限系统

```
    TOOL CALL REQUEST
          │
          ▼
    ┌─ validateInput() ──────────────────────────────────┐
    │  reject invalid inputs before any permission check │
    └────────────────────┬───────────────────────────────┘
                         │
                         ▼
    ┌─ PreToolUse Hooks ─────────────────────────────────┐
    │  user-defined shell commands (settings.json hooks) │
    │  can: approve, deny, or modify input               │
    └────────────────────┬───────────────────────────────┘
                         │
                         ▼
    ┌─ Permission Rules ─────────────────────────────────┐
    │  alwaysAllowRules:  match tool name/pattern → auto │
    │  alwaysDenyRules:   match tool name/pattern → deny │
    │  alwaysAskRules:    match tool name/pattern → ask  │
    │  Sources: settings, CLI args, session decisions    │
    └────────────────────┬───────────────────────────────┘
                         │
                    no rule match?
                         │
                         ▼
    ┌─ Interactive Prompt ───────────────────────────────┐
    │  User sees tool name + input                       │
    │  Options: Allow Once / Allow Always / Deny         │
    └────────────────────┬───────────────────────────────┘
                         │
                         ▼
    ┌─ checkPermissions() ───────────────────────────────┐
    │  Tool-specific logic (e.g. path sandboxing)        │
    └────────────────────┬───────────────────────────────┘
                         │
                    APPROVED → tool.call()
```

---

## 子智能体与多智能体架构

```
                        MAIN AGENT
                        ==========
                            │
            ┌───────────────┼───────────────┐
            ▼               ▼               ▼
     ┌──────────────┐ ┌──────────┐ ┌──────────────┐
     │  FORK AGENT  │ │ REMOTE   │ │ IN-PROCESS   │
     │              │ │ AGENT    │ │ TEAMMATE     │
     │ Fork process │ │ Bridge   │ │ Same process │
     │ Shared cache │ │ session  │ │ Async context│
     │ Fresh msgs[] │ │ Isolated │ │ Shared state │
     └──────────────┘ └──────────┘ └──────────────┘

    SPAWN MODES:
    ├─ default    → in-process, shared conversation
    ├─ fork       → child process, fresh messages[], shared file cache
    ├─ worktree   → isolated git worktree + fork
    └─ remote     → bridge to Claude Code Remote / container

    COMMUNICATION:
    ├─ SendMessageTool     → agent-to-agent messages
    ├─ TaskCreate/Update   → shared task board
    └─ TeamCreate/Delete   → team lifecycle management

    SWARM MODE (feature-gated):
    ┌─────────────────────────────────────────────┐
    │  Lead Agent                                 │
    │    ├── Teammate A ──> claims Task 1         │
    │    ├── Teammate B ──> claims Task 2         │
    │    └── Teammate C ──> claims Task 3         │
    │                                             │
    │  Shared: task board, message inbox          │
    │  Isolated: messages[], file cache, cwd      │
    └─────────────────────────────────────────────┘
```

---

## 上下文管理（压缩系统）

```
    CONTEXT WINDOW BUDGET
    ═════════════════════

    ┌─────────────────────────────────────────────────────┐
    │  System Prompt (tools, permissions, CLAUDE.md)      │
    │  ══════════════════════════════════════════════      │
    │                                                     │
    │  Conversation History                               │
    │  ┌─────────────────────────────────────────────┐    │
    │  │ [compacted summary of older messages]        │    │
    │  │ ═══════════════════════════════════════════  │    │
    │  │ [compact_boundary marker]                    │    │
    │  │ ─────────────────────────────────────────── │    │
    │  │ [recent messages — full fidelity]            │    │
    │  │ user → assistant → tool_use → tool_result   │    │
    │  └─────────────────────────────────────────────┘    │
    │                                                     │
    │  Current Turn (user + assistant response)            │
    └─────────────────────────────────────────────────────┘

    THREE COMPRESSION STRATEGIES:
    ├─ autoCompact     → triggers when token count exceeds threshold
    │                     summarizes old messages via a compact API call
    ├─ snipCompact     → removes zombie messages and stale markers
    │                     (HISTORY_SNIP feature flag)
    └─ contextCollapse → restructures context for efficiency
                         (CONTEXT_COLLAPSE feature flag)

    COMPACTION FLOW:
    messages[] ──> getMessagesAfterCompactBoundary()
                        │
                        ▼
                  older messages ──> Claude API (summarize) ──> compact summary
                        │
                        ▼
                  [summary] + [compact_boundary] + [recent messages]
```

---

## MCP（模型上下文协议）集成

```
    ┌─────────────────────────────────────────────────────────┐
    │                  MCP ARCHITECTURE                        │
    │                                                         │
    │  MCPConnectionManager.tsx                               │
    │    ├── Server Discovery (config from settings.json)     │
    │    │     ├── stdio  → spawn child process               │
    │    │     ├── sse    → HTTP EventSource                  │
    │    │     ├── http   → Streamable HTTP                   │
    │    │     ├── ws     → WebSocket                         │
    │    │     └── sdk    → in-process transport              │
    │    │                                                    │
    │    ├── Client Lifecycle                                  │
    │    │     ├── connect → initialize → list tools          │
    │    │     ├── tool calls via MCPTool wrapper              │
    │    │     └── disconnect / reconnect with backoff        │
    │    │                                                    │
    │    ├── Authentication                                   │
    │    │     ├── OAuth 2.0 flow (McpOAuthConfig)            │
    │    │     ├── Cross-App Access (XAA / SEP-990)           │
    │    │     └── API key via headers                        │
    │    │                                                    │
    │    └── Tool Registration                                │
    │          ├── mcp__<server>__<tool> naming convention     │
    │          ├── Dynamic schema from MCP server              │
    │          ├── Permission passthrough to Claude Code       │
    │          └── Resource listing (ListMcpResourcesTool)     │
    │                                                         │
    └─────────────────────────────────────────────────────────┘
```

---

## Bridge 层（Claude Desktop / 远程服务）

```
    Claude Desktop / Web / Cowork          Claude Code CLI
    ══════════════════════════            ═════════════════

    ┌───────────────────┐                 ┌──────────────────┐
    │  Bridge Client    │  ←─ HTTP ──→   │  bridgeMain.ts   │
    │  (Desktop App)    │                 │                  │
    └───────────────────┘                 │  Session Manager │
                                          │  ├── spawn CLI   │
    PROTOCOL:                             │  ├── poll status  │
    ├─ JWT authentication                 │  ├── relay msgs   │
    ├─ Work secret exchange               │  └── capacityWake │
    ├─ Session lifecycle                  │                  │
    │  ├── create                         │  Backoff:        │
    │  ├── run                            │  ├─ conn: 2s→2m  │
    │  └─ stop                            │  └─ gen: 500ms→30s│
    └─ Token refresh scheduler            └──────────────────┘
```

---

## 会话持久化

```
    SESSION STORAGE
    ══════════════

    ~/.claude/projects/<hash>/sessions/
    └── <session-id>.jsonl           ← append-only log
        ├── {"type":"user",...}
        ├── {"type":"assistant",...}
        ├── {"type":"progress",...}
        └── {"type":"system","subtype":"compact_boundary",...}

    RESUME FLOW:
    getLastSessionLog() ──> parse JSONL ──> rebuild messages[]
         │
         ├── --continue     → last session in cwd
         ├── --resume <id>  → specific session
         └── --fork-session → new ID, copy history

    PERSISTENCE STRATEGY:
    ├─ User messages  → await write (blocking, for crash recovery)
    ├─ Assistant msgs → fire-and-forget (order-preserving queue)
    ├─ Progress       → inline write (dedup on next query)
    └─ Flush          → on result yield / cowork eager flush
```

---

## 特性标志系统

```
    DEAD CODE ELIMINATION (Bun compile-time)
    ══════════════════════════════════════════

    feature('FLAG_NAME')  ──→  true  → included in bundle
                           ──→  false → stripped from bundle

    FLAGS (observed in source):
    ├─ COORDINATOR_MODE      → multi-agent coordinator
    ├─ HISTORY_SNIP          → aggressive history trimming
    ├─ CONTEXT_COLLAPSE      → context restructuring
    ├─ DAEMON                → background daemon workers
    ├─ AGENT_TRIGGERS        → cron/remote triggers
    ├─ AGENT_TRIGGERS_REMOTE → remote trigger support
    ├─ MONITOR_TOOL          → MCP monitoring tool
    ├─ WEB_BROWSER_TOOL      → browser automation
    ├─ VOICE_MODE            → voice input/output
    ├─ TEMPLATES             → job classifier
    ├─ EXPERIMENTAL_SKILL_SEARCH → skill discovery
    ├─ KAIROS                → push notifications, file sends
    ├─ PROACTIVE             → sleep tool, proactive behavior
    ├─ OVERFLOW_TEST_TOOL    → testing tool
    ├─ TERMINAL_PANEL        → terminal capture
    ├─ WORKFLOW_SCRIPTS      → workflow tool
    ├─ CHICAGO_MCP           → computer use MCP
    ├─ DUMP_SYSTEM_PROMPT    → prompt extraction (ant-only)
    ├─ UDS_INBOX             → peer discovery
    ├─ ABLATION_BASELINE     → experiment ablation
    └─ UPGRADE_NOTICE        → upgrade notifications

    RUNTIME GATES:
    ├─ process.env.USER_TYPE === 'ant'  → internal features
    └─ GrowthBook feature flags         → A/B experiments at runtime
```

---

## 状态管理

```
    ┌──────────────────────────────────────────────────────────┐
    │                  AppState Store                           │
    │                                                          │
    │  AppState {                                              │
    │    toolPermissionContext: {                              │
    │      mode: PermissionMode,           ← default/plan/etc │
    │      additionalWorkingDirectories,                        │
    │      alwaysAllowRules,               ← auto-approve      │
    │      alwaysDenyRules,                ← auto-reject       │
    │      alwaysAskRules,                 ← always prompt     │
    │      isBypassPermissionsModeAvailable                    │
    │    },                                                    │
    │    fileHistory: FileHistoryState,    ← undo snapshots    │
    │    attribution: AttributionState,    ← commit tracking   │
    │    verbose: boolean,                                     │
    │    mainLoopModel: string,           ← active model       │
    │    fastMode: FastModeState,                              │
    │    speculation: SpeculationState                          │
    │  }                                                       │
    │                                                          │
    │  React Integration:                                      │
    │  ├── AppStateProvider   → creates store via createContext │
    │  ├── useAppState(sel)   → selector-based subscriptions   │
    │  └── useSetAppState()   → immer-style updater function   │
    └──────────────────────────────────────────────────────────┘
```

---

## 12 层渐进式 Harness（运行框架）机制

该架构展示了生产级 AI Agent（智能体）框架在基础循环之外所需的 12 层机制。每一层都建立在前一层之上：

```
    s01  THE LOOP             "One loop & Bash is all you need"
         query.ts: the while-true loop that calls Claude API,
         checks stop_reason, executes tools, appends results.

    s02  TOOL DISPATCH        "Adding a tool = adding one handler"
         Tool.ts + tools.ts: every tool registers into the dispatch
         map. The loop stays identical. buildTool() factory provides
         safe defaults.

    s03  PLANNING             "An agent without a plan drifts"
         EnterPlanModeTool/ExitPlanModeTool + TodoWriteTool:
         list steps first, then execute. Doubles completion rate.

    s04  SUB-AGENTS           "Break big tasks; clean context per subtask"
         AgentTool + forkSubagent.ts: each child gets fresh messages[],
         keeping the main conversation clean.

    s05  KNOWLEDGE ON DEMAND  "Load knowledge when you need it"
         SkillTool + memdir/: inject via tool_result, not system prompt.
         CLAUDE.md files loaded lazily per directory.

    s06  CONTEXT COMPRESSION  "Context fills up; make room"
         services/compact/: three-layer strategy:
         autoCompact (summarize) + snipCompact (trim) + contextCollapse

    s07  PERSISTENT TASKS     "Big goals → small tasks → disk"
         TaskCreate/Update/Get/List: file-based task graph with
         status tracking, dependencies, and persistence.

    s08  BACKGROUND TASKS     "Slow ops in background; agent keeps thinking"
         DreamTask + LocalShellTask: daemon threads run commands,
         inject notifications on completion.

    s09  AGENT TEAMS          "Too big for one → delegate to teammates"
         TeamCreate/Delete + InProcessTeammateTask: persistent
         teammates with async mailboxes.

    s10  TEAM PROTOCOLS       "Shared communication rules"
         SendMessageTool: one request-response pattern drives
         all negotiation between agents.

    s11  AUTONOMOUS AGENTS    "Teammates scan and claim tasks themselves"
         coordinator/coordinatorMode.ts: idle cycle + auto-claim,
         no need for lead to assign each task.

    s12  WORKTREE ISOLATION   "Each works in its own directory"
         EnterWorktreeTool/ExitWorktreeTool: tasks manage goals,
         worktrees manage directories, bound by ID.
```

---

## 核心设计模式

| Pattern | Where | Purpose |
|---------|-------|---------|
| **AsyncGenerator streaming** | `QueryEngine`, `query()` | Full-chain streaming from API to consumer |
| **Builder + Factory** | `buildTool()` | Safe defaults for tool definitions |
| **Branded Types** | `SystemPrompt`, `asSystemPrompt()` | Prevent string/array confusion |
| **Feature Flags + DCE** | `feature()` from `bun:bundle` | Compile-time dead code elimination |
| **Discriminated Unions** | `Message` types | Type-safe message handling |
| **Observer + State Machine** | `StreamingToolExecutor` | Tool execution lifecycle tracking |
| **Snapshot State** | `FileHistoryState` | Undo/redo for file operations |
| **Ring Buffer** | Error log | Bounded memory for long sessions |
| **Fire-and-Forget Write** | `recordTranscript()` | Non-blocking persistence with ordering |
| **Lazy Schema** | `lazySchema()` | Defer Zod schema evaluation for performance |
| **Context Isolation** | `AsyncLocalStorage` | Per-agent context in shared process |

---

## 许可证

本仓库内容仅供技术研究、学习与教育使用。所有知识产权归原公司所有。如有任何侵权，请联系我们核实后立即删除。