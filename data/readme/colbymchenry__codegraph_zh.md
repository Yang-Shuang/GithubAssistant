<div align="center">

# CodeGraph

### 用语义代码智能为 Claude Code、Cursor、Codex、OpenCode、Hermes Agent、Gemini、Antigravity 和 Kiro 赋能

**成本降低约 16% · 工具调用减少约 58% · 100% 本地运行**

### [文档与网站 →](https://colbymchenry.github.io/codegraph/)

[![npm version](https://img.shields.io/npm/v/@colbymchenry/codegraph.svg)](https://www.npmjs.com/package/@colbymchenry/codegraph)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Self-contained](https://img.shields.io/badge/Node.js-bundled%20%C2%B7%20none%20required-brightgreen.svg)](https://nodejs.org/)

[![Windows](https://img.shields.io/badge/Windows-supported-blue.svg)](#supported-platforms)
[![macOS](https://img.shields.io/badge/macOS-supported-blue.svg)](#supported-platforms)
[![Linux](https://img.shields.io/badge/Linux-supported-blue.svg)](#supported-platforms)

[![Claude Code](https://img.shields.io/badge/Claude_Code-supported-blueviolet.svg)](#supported-agents)
[![Cursor](https://img.shields.io/badge/Cursor-supported-blueviolet.svg)](#supported-agents)
[![Codex](https://img.shields.io/badge/Codex-supported-blueviolet.svg)](#supported-agents)
[![opencode](https://img.shields.io/badge/opencode-supported-blueviolet.svg)](#supported-agents)
[![Hermes Agent](https://img.shields.io/badge/Hermes_Agent-supported-blueviolet.svg)](#supported-agents)
[![Gemini](https://img.shields.io/badge/Gemini-supported-blueviolet.svg)](#supported-agents)
[![Antigravity](https://img.shields.io/badge/Antigravity-supported-blueviolet.svg)](#supported-agents)
[![Kiro](https://img.shields.io/badge/Kiro-supported-blueviolet.svg)](#supported-agents)

</div>

## 快速开始

### 1. 安装 CLI

**无需 Node.js** —— 一条命令即可获取适配你操作系统的版本：

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.sh | sh

# Windows (PowerShell)
irm https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.ps1 | iex
```

已安装 Node？改用 npm 即可（兼容任意版本）：

```bash
npm i -g @colbymchenry/codegraph
```

<sub>CodeGraph 内置了独立的运行环境——无需编译，无原生依赖，跨平台表现一致。安装器会将 `codegraph` 加入你的 PATH，但**不会修改当前 Shell** ——请在下一步之前打开新的终端窗口以确保命令生效。</sub>

### 2. 配置 Agent（智能体）

在**新终端**中运行安装器，将 CodeGraph 连接到你使用的 Agent：

```bash
codegraph install
```

<sub>自动检测并配置 Claude Code、Cursor、Codex CLI、opencode、Hermes Agent、Gemini CLI、Antigravity IDE 和 Kiro ——将 CodeGraph MCP Server（模型上下文协议服务器）接入各个 Agent。**这一步才是真正将 CodeGraph 与你的 Agent 连接起来的操作**；仅在第 1 步安装 CLI 并不会自动完成此操作。（快捷方式：`npx @colbymchenry/codegraph` 可一键下载并运行。）</sub>

### 3. 初始化项目

```bash
cd your-project
codegraph init -i
```

<sub>`codegraph init` 仅创建本地的 `.codegraph/` 索引目录；添加 `-i`（即 `--index`）会在同一步骤中构建初始图谱。若不加 `-i`，请随后运行 `codegraph index` 进行填充。</sub>

<div align="center">

![1_C_VYnhpys0UHrOuOgpgoyw](https://github.com/user-attachments/assets/f168182f-4d9a-44e0-94d7-08d018cc8a3a)

</div>

### 卸载

改变主意了？一条命令即可从所有已配置的 Agent 中移除 CodeGraph：

```bash
codegraph uninstall
```

<sub>撤销安装器操作——剥离各 Agent 中的 CodeGraph MCP Server 配置、指令和权限。你的项目索引（`.codegraph/`）将保留不变；如需按项目移除，请使用 `codegraph uninit`。使用 `--target` 可指定移除特定 Agent，或 `--yes` 以非交互方式运行。</sub>

---

## 为什么选择 CodeGraph？

当 Claude Code 探索代码库时，它会派生 **Explore（探索）Agent**，使用 `grep`、`glob` 和 `Read` 扫描文件——每次工具调用都会消耗 Token。

**CodeGraph 为这些 Agent 提供了一个预索引的知识图谱（Knowledge Graph）**——包含符号关系、调用图和代码结构。Agent 可直接查询图谱，而无需扫描文件。

### 基准测试结果

在跨越 7 种语言的 **7 个真实开源代码库**上进行了测试，对比了 Agent（Claude Code，无头模式）在有/无 CodeGraph 的情况下回答同一架构问题的表现。每个单元格的数据为各配置下 **4 次运行的中位数**。_已于 Opus 4.8 (2026-06-02) 及当前版本重新验证（`codegraph_explore` 作为主要工具）。_

> **平均：成本降低 16% · Token 减少 47% · 速度提升 22% · 工具调用减少 58%**

| 代码库 | 语言 | 成本 | Token数 | 耗时 | 工具调用 |
|----------|----------|------|--------|------|------------|
| **VS Code** | TypeScript · ~10k files | 降低 18% | 减少 64% | 快 11% | 减少 81% |
| **Excalidraw** | TypeScript · ~640 | 持平 | 减少 25% | 快 27% | 减少 40% |
| **Django** | Python · ~3k | 降低 8% | 减少 60% | 快 13% | 减少 77% |
| **Tokio** | Rust · ~790 | 持平 | 减少 38% | 快 18% | 减少 57% |
| **OkHttp** | Java · ~645 | 降低 25% | 减少 54% | 快 31% | 减少 50% |
| **Gin** | Go · ~110 | 降低 19% | 减少 23% | 快 24% | 减少 44% |
| **Alamofire** | Swift · ~110 | 降低 40% | 减少 64% | 快 33% | 减少 58% |

CodeGraph 能在**所有代码库（无论大小）中显著减少 Token 消耗、工具调用和实际耗时**。它通过**近乎零的文件读取**来回答问题，而使用无 CodeGraph 的 Agent 则会将预算浪费在 `grep`/`find`/`Read` 的发现过程中。`codegraph_explore` 会完整展示答案——包括你询问的具体机制和方法（即使它们埋藏在数千行的文件中）——同时会将冗余且可互换的实现折叠为函数签名，使返回结果的篇幅仅匹配*答案本身*而非文件数量。**成本在所有场景下均持平或更低**——在小型仓库（Alamofire、OkHttp）上节省最明显；在响应内容最多的仓库（Excalidraw、Tokio）上大致打平，此时 CodeGraph 用少量大型缓存密集型工具调用，替代了无 CodeGraph Agent 的多次 `grep`/`read` 往返请求。

<details>
<summary><strong>各仓库明细对比 — WITH vs WITHOUT（4次运行中位数）</strong></summary>

**VS Code** · ~10k files
| 指标 | WITH cg | WITHOUT cg | Δ |
|---|---|---|---|
| 耗时 | 1m 59s | 2m 13s | 快 11% |
| 文件读取 | 0 | 9 | −9 |
| Grep/Bash | 0 | 11 | −11 |
| 工具调用 | 4 | 21 | 减少 81% |
| Token总数 | 640k | 1.79M | 减少 64% |
| 成本 | $0.68 | $0.83 | 降低 18% |

**Excalidraw** · ~640 files
| 指标 | WITH cg | WITHOUT cg | Δ |
|---|---|---|---|
| 耗时 | 1m 32s | 2m 6s | 快 27% |
| 文件读取 | 0 | 7 | −7 |
| Grep/Bash | 1 | 8 | −7 |
| 工具调用 | 9 | 15 | 减少 40% |
| Token总数 | 1.27M | 1.69M | 减少 25% |
| 成本 | $0.78 | $0.78 | 持平 |

**Django** · ~3k files
| 指标 | WITH cg | WITHOUT cg | Δ |
|---|---|---|---|
| 耗时 | 1m 43s | 1m 58s | 快 13% |
| 文件读取 | 0 | 9 | −9 |
| Grep/Bash | 0 | 5 | −5 |
| 工具调用 | 3 | 13 | 减少 77% |
| Token总数 | 559k | 1.41M | 减少 60% |
| 成本 | $0.57 | $0.62 | 降低 8% |

**Tokio** · ~790 files
| 指标 | WITH cg | WITHOUT cg | Δ |
|---|---|---|---|
| 耗时 | 1m 55s | 2m 20s | 快 18% |
| 文件读取 | 0 | 8 | −8 |
| Grep/Bash | 0 | 6 | −6 |
| 工具调用 | 6 | 14 | 减少 57% |
| Token总数 | 1.08M | 1.73M | 减少 38% |
| 成本 | $0.82 | $0.82 | 持平 |

**OkHttp** · ~645 files
| 指标 | WITH cg | WITHOUT cg | Δ |
|---|---|---|---|
| 耗时 | 1m 1s | 1m 29s | 快 31% |
| 文件读取 | 0 | 4 | −4 |
| Grep/Bash | 2 | 6 | −4 |
| 工具调用 | 5 | 10 | 减少 50% |
| Token总数 | 502k | 1.10M | 减少 54% |
| 成本 | $0.41 | $0.55 | 降低 25% |

**Gin** · ~110 files
| 指标 | WITH cg | WITHOUT cg | Δ |
|---|---|---|---|
| 耗时 | 1m 14s | 1m 37s | 快 24% |
| 文件读取 | 1 | 6 | −5 |
| Grep/Bash | 1 | 2 | −1 |
| 工具调用 | 5 | 9 | 减少 44% |
| Token总数 | 651k | 847k | 减少 23% |
| 成本 | $0.46 | $0.57 | 降低 19% |

**Alamofire** · ~110 files
| 指标 | WITH cg | WITHOUT cg | Δ |
|---|---|---|---|
| 耗时 | 1m 35s | 2m 21s | 快 33% |
| 文件读取 | 0 | 9 | −9 |
| Grep/Bash | 0 | 4 | −4 |
| 工具调用 | 5 | 12 | 减少 58% |
| Token总数 | 766k | 2.10M | 减少 64% |
| 成本 | $0.57 | $0.95 | 降低 40% |

</details>

<details>
<summary><strong>完整基准测试详情</strong></summary>

**方法论。** 每个配置均使用 `claude -p`（Claude Opus 4.8）在无头模式下针对代码库运行，并启用 `--strict-mcp-config`：**WITH** = CodeGraph MCP Server 已启用，**WITHOUT** = 空 MCP 配置。内置的 Read/Grep/Bash 对两者均开放可用。每个仓库提问相同，**每配置 4 次运行，报告中位数**。成本 = 该次运行的 `total_cost_usd`；Token数 = 总处理 Token（含缓存输入 + 输出）；耗时 = 实际墙钟时间；工具调用 = 所有工具调用次数，包括模型派生的任何子 Agent 内部的调用。代码库以 `--depth 1` 克隆，并由同一 CodeGraph 版本建立索引并服务。于 2026-06-02 在当前版本重新验证。这些数值低于之前的 Opus 4.7 验证结果——并非 CodeGraph 性能回退，而是原生基线更强：Opus 4.8 在主线程上更高效地执行 grep/读取，而非扇出到大型 Explore 子 Agent 扫描中，因此无 CodeGraph 配置的表现比过去更精简。各仓库数据会因 without-arm 的扰动程度而波动（中位数已平滑处理，但尾部差异仍存在——例如 Django 的 without-arm 在某一批次曾达到 $2.71/14m）。

**测试问题：**
| 代码库 | 查询内容 |
|----------|-------|
| VS Code | "扩展主机如何与主进程通信？" |
| Excalidraw | "Excalidraw 如何渲染和更新画布元素？" |
| Django | "Django ORM 如何从 QuerySet 构建并执行查询？" |
| Tokio | "tokio 如何在运行时调度并运行异步任务？" |
| OkHttp | "OkHttp 如何通过拦截器链处理请求？" |
| Gin | "gin 如何通过中间件链路由请求？" |
| Alamofire | "Alamofire 如何构建、发送和验证请求？" |

**CodeGraph 胜出的原因：** 索引可用时，Agent 直接给出答案——通常只需一次 `codegraph_explore` 即可返回相关源码并结束任务，往往零文件读取。若无它，Agent 会将大部分预算消耗在发现阶段（find/ls/grep），之后才去阅读正确的代码。CodeGraph 仅在被*直接查询*时发挥作用，因此其指令会引导 Agent 直接作答，而非将探索任务委派给负责读文件的子 Agent——否则子 Agent 仍会读取文件，而 CodeGraph 反而成为额外开销。

</details>

---

## 核心功能

| | |
|---|---|
| **智能上下文构建** | 一次工具调用即可返回入口点、相关符号和代码片段——无需昂贵的探索 Agent |
| **全文搜索（FTS5）** | 基于 FTS5，可瞬间按名称在整个代码库中查找代码 |
| **影响分析** | 在修改前追踪调用者、被调用者及任意符号的完整影响范围 |
| **始终最新** | 文件监听器使用原生 OS 事件（FSEvents/inotify/ReadDirectoryChangesW）配合防抖自动同步——编码时图谱始终保持更新，零配置 |
| **支持 20+ 种语言** | TypeScript, JavaScript, Python, Go, Rust, Java, C#, PHP, Ruby, C, C++, Objective-C, Swift, Kotlin, Dart, Lua, Luau, Svelte, Liquid, Pascal/Delphi |
| **框架感知路由** | 识别 Web 框架的路由文件，并将 URL 模式链接到对应的处理器（覆盖 14 种框架） |
| **混合 iOS / React Native / Expo 桥接** | 弥补静态解析遗漏的跨语言流程：Swift ↔ ObjC 桥接、React Native 旧版 Bridge + TurboModules + Fabric 视图组件、原生 → JS 事件发射器、Expo Modules |
| **100% 本地运行** | 数据不出本机。无需 API Key。无外部服务。仅依赖 SQLite 数据库 |

<details>
<summary><strong>自动同步机制详解——为何你无需手动运行 <code>codegraph sync</code></strong></summary>

当你的 Agent（Claude Code、Cursor、Codex、opencode）启动 `codegraph serve --mcp` 时，三层机制确保索引与代码保持同步——并在编辑完成到下一次同步的短暂间隙中，防止 Agent 收到静默错误的答案：

1. **带防抖的文件监听器。** 原生 FSEvents / inotify / ReadDirectoryChangesW 监听器捕获所有源文件的创建/修改/删除操作，并在防抖窗口（默认 `2000ms`，可通过 `CODEGRAPH_WATCH_DEBOUNCE_MS` 调整，限制在 `[100ms, 60s]`）后触发重新索引。批量编辑将合并为单次同步。

2. **单文件过期提示。** 在短暂的防抖窗口内，若 MCP 工具响应会引用尚未更新的文件，会在回复顶部添加 `⚠️` 提示并列出文件名，告知 Agent 直接 `Read` 该文件。未被引用的待更新文件则作为页脚小字显示。无论哪种情况，Agent 都会收到明确信号——已在 Claude Code 中验证，Agent 甚至会明确表示“正在直接读取文件以获取最新内容”后再打开它。

3. **连接时追赶同步。** MCP Server（重新）连接时，codegraph 会在回答第一个查询前，对工作目录执行快速的 `(size, mtime)` + 内容哈希比对——因此当没有 MCP Server 运行时发生的编辑（如终端中的 `git pull`、其他编辑器的修改、退出的旧 Agent 会话），都会在下次会话的第一个工具调用时被吸收同步。

```
agent writes src/Widget.ts
  → watcher fires (<100ms)
  → debounce (default 2s)
  → sync; Widget.ts is in the index
  → next agent query sees it
```

**随时验证：** 使用 `codegraph_status`（通过 MCP）或 `codegraph status`（CLI）。若有待处理项，你将看到 `### Pending sync:` 部分列出文件名及其修改时间。

少数需要手动运行 `codegraph sync` 的场景：监听器已禁用（沙盒环境或设置了 `CODEGRAPH_NO_DAEMON=1`），或者你在 Agent 会话外通过脚本操作索引，希望在脚本开头进行预同步。

→ 完整深入指南见 [指南 → 索引项目](https://colbymchenry.github.io/codegraph/guides/indexing/#stay-fresh-automatically)。

</details>

---

## 框架感知路由

CodeGraph 会检测 Web 框架的路由文件，并生成通过 `references` 边链接到处理器类或函数的 `route` 节点。查询视图/控制器的调用者时，现在会自动显示绑定该路由的 URL 模式。

| 框架 | 识别的结构特征 |
|---|---|
| **Django** | `urls.py` 中的 `path()`、`re_path()`、`url()`、`include()`（CBV `.as_view()`、点号路径） |
| **Flask** | `@app.route('/path', methods=[...])`、蓝图路由 |
| **FastAPI** | `@app.get(...)`、`@router.post(...)` 及所有标准方法 |
| **Express** | `app.get(...)`、`router.post(...)`（含中间件链） |
| **NestJS** | `@Controller` + `@Get/@Post/...`、GraphQL `@Resolver` + `@Query/@Mutation`、`@MessagePattern`/`@EventPattern`、`@SubscribeMessage` |
| **Laravel** | `Route::get()`、`Route::resource()`、`Controller@action`、元组语法 |
| **Drupal** | `*.routing.yml` 路由（`_controller`、`_form`、实体处理器）；`.module`/`.theme`/`.install`/`.inc` 中的 `hook_*` 实现 |
| **Rails** | `get '/x', to: 'users#index'`、哈希箭头 `=>` 语法 |
| **Spring** | 方法上的 `@GetMapping`、`@PostMapping`、`@RequestMapping` |
| **Gin / chi / gorilla / mux** | `r.GET(...)`、`router.HandleFunc(...)` |
| **Axum / actix / Rocket** | `.route("/x", get(handler))` |
| **ASP.NET** | 动作方法上的 `[HttpGet("/x")]` 特性 |
| **Vapor** | `app.get("x", use: handler)` |
| **React Router** / **SvelteKit** | 路由组件节点 |

---

## 混合 iOS / React Native / Expo 桥接支持

真实的 iOS 和 React Native 代码库通常跨多种语言——Swift 调用者会触发已自动桥接的 Objective-C 选择器，JS 文件通过 React Native Bridge 调用原生模块，JSX 组件委托给原生视图管理器。静态 tree-sitter 提取会在每种语言的边界处停止。CodeGraph 将这些连接打通，使 `trace`、`callers`、`callees` 和 `impact` 能够跨越语言鸿沟实现端到端连通。

| 边界 | JS / Swift 侧 | Native 侧 | 桥接方式 |
|---|---|---|---|
| **Swift → ObjC** | Swift `obj.foo(bar:)` | ObjC selector `-fooWithBar:` | `@objc` 自动桥接规则（含 init/property/protocol 形式）+ Cocoa 介词前缀（`With`/`For`/`By`/`In`/`On`/`At`/…） |
| **ObjC → Swift** | ObjC `[obj fooWithBar:]` | Swift `@objc func foo(bar:)` | 反向桥接名称候选；验证源码中的 `@objc` 暴露情况 |
| **React Native legacy bridge** | JS `NativeModules.X.fn(...)` | ObjC `RCT_EXPORT_METHOD` / `RCT_REMAP_METHOD` · Java/Kotlin `@ReactMethod` | 解析宏/注解声明，构建 JS名称 → 原生方法映射 |
| **React Native TurboModules** | JS `import M from './NativeM'; M.fn(...)` | 匹配 Codegen 规范的原生实现 | 将 `Native<X>.ts` 规范接口视为事实来源 |
| **RN native → JS events** | JS `new NativeEventEmitter(...).addListener('e', cb)` | ObjC `[self sendEventWithName:@"e" body:...]` · Swift `sendEvent(withName: "e", ...)` · Java/Kotlin `.emit("e", ...)` | 按字面事件名键合的跨语言事件通道合成 |
| **Expo Modules** | JS `requireNativeModule('X').fn(...)` | Swift / Kotlin `Module { Name("X"); AsyncFunction("fn") { ... } }` | 解析 Expo DSL 字面量；合成方法节点通过现有名称匹配解决 |
| **Fabric view components** | JSX `<MyView prop={v}/>` | TS Codegen spec + native impl class | Spec → `component` 节点；基于约定的名称+后缀查找（`View`/`ComponentView`/`Manager`/`ViewManager`）桥接至原生 |
| **Legacy Paper view managers** | JSX `<MyView prop={v}/>` | ObjC `RCT_EXPORT_VIEW_PROPERTY` · Java/Kotlin `@ReactProp` | 同 Fabric——Paper 时代的声明同样生成 `component` + `property` 节点 |

**已在真实代码库中验证：**（每种桥接均包含小/中/大型仓库）

| 桥接类型 | Small | Medium | Large |
|---|---|---|---|
| Swift ↔ ObjC | [Charts](https://github.com/danielgindi/Charts) | [realm-swift](https://github.com/realm/realm-swift) | [Wikipedia-iOS](https://github.com/wikimedia/wikipedia-ios) |
| RN legacy bridge | [AsyncStorage](https://github.com/react-native-async-storage/async-storage) | [react-native-svg](https://github.com/software-mansion/react-native-svg) | [react-native-firebase](https://github.com/invertase/react-native-firebase) |
| RN native → JS events | [RNGeolocation](https://github.com/Agontuk/react-native-geolocation-service) | — | react-native-firebase |
| Expo Modules | expo-haptics | expo-camera | expo SDK sweep (7 packages) |
| Fabric / Paper views | [react-native-segmented-control](https://github.com/react-native-segmented-control/segmented-control) | [react-native-screens](https://github.com/software-mansion/react-native-screens) | [react-native-skia](https://github.com/Shopify/react-native-skia) |

每个桥接模块都会生成标记为 `provenance:'heuristic'` 的边，并在 `metadata.synthesizedBy:` 中设置稳定的通道名称（例如 `swift-objc-bridge`、`rn-event-channel`、`fabric-native-impl`、`expo-module-extract`），以便 Agent 一目了然地识别图中某条路径是如何生成的。

---

## 快速开始

### 1. 运行安装器

```bash
npx @colbymchenry/codegraph
```

安装器将执行以下操作：
- 询问要配置哪些 Agent——自动检测已安装的：**Claude Code**、**Cursor**、**Codex CLI**、**opencode**、**Hermes Agent**、**Gemini CLI**、**Antigravity IDE**、**Kiro**
- 提示将 `codegraph` 安装到 PATH（以便 Agent 能启动 MCP Server）
- 询问配置是应用于所有项目还是仅当前项目
- 写入各选定 Agent 的 MCP Server 配置（CodeGraph 的使用指南由 MCP Server 自身提供，因此不会向 `CLAUDE.md` / `AGENTS.md` 等文件中添加说明文件）
- 当 Claude Code 为目标时，自动配置允许权限
- 初始化当前项目（仅限本地安装）

**非交互模式（脚本/CI）：**

```bash
codegraph install --yes                              # 自动检测 Agent，全局安装
codegraph install --target=cursor,claude --yes       # 显式指定目标列表
codegraph install --target=auto --location=local     # 检测到的 Agent，项目本地配置
codegraph install --print-config codex               # 打印片段并退出，不写入文件
```

| Flag | 值 | 默认值 |
|---|---|---|
| `--target` | `auto`, `all`, `none`, 或 csv (`claude,cursor,...`) | prompt |
| `--location` | `global`, `local` | prompt |
| `--yes` | (boolean) | 每步均提示 |
| `--no-permissions` | (boolean) 跳过 Claude 自动允许列表 | 权限开启 |
| `--print-config <id>` | 转储单个 Agent 的片段并退出 | — |

### 2. 重启你的 Agent

重启你的 Agent（Claude Code / Cursor / Codex CLI / opencode / Hermes Agent / Gemini CLI / Antigravity IDE / Kiro）以加载 MCP Server。

### 3. 初始化项目

```bash
cd your-project
codegraph init -i
```

构建按项目的知识图谱索引。单次全局 `codegraph install` 即可在你打开的每个项目中生效——无需按项目重复运行安装器。

至此完成——当存在 `.codegraph/` 目录时，你的 Agent 将自动使用 CodeGraph 工具。

<details>
<summary><strong>手动设置（替代方案）</strong></summary>

**全局安装：**
```bash
npm install -g @colbymchenry/codegraph
```

**添加到 `~/.claude.json`：**
```json
{
  "mcpServers": {
    "codegraph": {
      "type": "stdio",
      "command": "codegraph",
      "args": ["serve", "--mcp"]
    }
  }
}
```

**添加到 `~/.claude/settings.json`（可选，用于自动允许）：**
```json
{
  "permissions": {
    "allow": [
      "mcp__codegraph__codegraph_search",
      "mcp__codegraph__codegraph_explore",
      "mcp__codegraph__codegraph_callers",
      "mcp__codegraph__codegraph_callees",
      "mcp__codegraph__codegraph_impact",
      "mcp__codegraph__codegraph_node",
      "mcp__codegraph__codegraph_status",
      "mcp__codegraph__codegraph_files"
    ]
  }
}
```

</details>

<details>
<summary><strong>Agent 工具使用指南</strong></summary>

CodeGraph 的 MCP Server 会在 MCP `initialize` 响应中**自动**向你的 Agent 交付使用指南——无需管理说明文件，也不会向 `CLAUDE.md` / `AGENTS.md` / `GEMINI.md` 中添加任何内容。简而言之，它会指示 Agent：

- **直接使用 CodeGraph 回答结构类问题**——它本身就是预建索引，因此 `grep`/`read` 循环只是在重复已做的工作。请将返回的源码视为已读取状态。
- **按意图选择工具：** `codegraph_explore` 用于几乎所有场景——“X 是如何工作的”、流程（“X 如何到达 Y”）或区域概览（一次调用即可按文件分组返回相关符号的源码）；`codegraph_search` 仅用于定位符号；`codegraph_callers`/`codegraph_callees` 用于遍历调用链；`codegraph_impact` 在修改前使用；`codegraph_node` 获取特定符号的完整源码（针对歧义名称会返回所有重载）。
- **信任结果——不要再用 `grep` 重复验证**，并在编辑后检查过期提示。
- 若尚未存在 `.codegraph/`，可主动建议运行 `codegraph init -i`。

完整指令文本位于 `src/mcp/server-instructions.ts`——这是唯一权威来源。

</details>

---

## 工作原理

```
┌───────────────────────────────────────────────────────────────────┐
│                            Claude Code                            │
│                                                                   │
│   "请求如何到达数据库？"                                          │
│       直接调用 CodeGraph 工具——无需 Explore 子 Agent              │
│                                 │                                 │
└─────────────────────────────────┬─────────────────────────────────┘
                                  │
                                  ▼
┌───────────────────────────────────────────────────────────────────┐
│                        CodeGraph MCP Server                       │
│                                                                   │
│       explore · search · callers · callees · impact · node        │
│                                 │                                 │
│                                 ▼                                 │
│                       SQLite 知识图谱                             │
│          symbols · edges · files · FTS5 全文搜索                  │
└───────────────────────────────────────────────────────────────────┘
```

1. **提取**——[tree-sitter](https://tree-sitter.github.io/) 将源码解析为抽象语法树（AST）。通过语言特定的查询提取节点（函数、类、方法）和边（调用、导入、继承、实现）。

2. **存储**——所有数据存入本地 SQLite 数据库（`.codegraph/codegraph.db`），并启用 FTS5 全文搜索。

3. **解析**——提取完成后，进行引用解析：函数调用 → 定义、导入 → 源文件、类继承关系及框架特定模式。

4. **自动同步**——MCP Server 使用原生操作系统文件事件监听你的项目。变更会经过防抖处理（2秒静默窗口），仅过滤源文件并增量同步。编码时图谱始终保持最新——无需任何配置。

---

## CLI 参考

```bash
codegraph                         # 运行交互式安装器
codegraph install                 # 显式运行安装器
codegraph uninstall               # 从 Agent 中移除 CodeGraph（install 的逆操作）
codegraph init [path]             # 初始化项目 (--index 同时构建索引)
codegraph uninit [path]           # 从项目中移除 CodeGraph (--force 跳过确认)
codegraph index [path]            # 完整索引 (--force 强制重建, --quiet 减少输出)
codegraph sync [path]             # 增量更新
codegraph status [path]           # 显示统计信息
codegraph query <search>          # 搜索符号 (--kind, --limit, --json)
codegraph files [path]            # 显示文件结构 (--format, --filter, --max-depth, --json)
codegraph callers <symbol>        # 查找调用某函数/方法的代码 (--limit, --json)
codegraph callees <symbol>        # 查找某函数/方法调用的代码 (--limit, --json)
codegraph impact <symbol>         # 分析修改符号影响的代码范围 (--depth, --json)
codegraph affected [files...]     # 查找受变更影响的测试文件（见下文）
codegraph serve --mcp             # 启动 MCP Server
```

### `codegraph affected`

通过传递依赖关系追踪，找出受源文件变更影响的测试文件。

```bash
codegraph affected src/utils.ts src/api.ts         # 以参数形式传入文件
git diff --name-only | codegraph affected --stdin   # 从 git diff 管道输入
codegraph affected src/auth.ts --filter "e2e/*"     # 自定义测试文件匹配模式
```

| Option | 说明 | 默认值 |
|--------|-------------|---------|
| `--stdin` | 从标准输入读取文件列表 | `false` |
| `-d, --depth <n>` | 最大依赖遍历深度 | `5` |
| `-f, --filter <glob>` | 自定义 glob 匹配测试文件 | auto-detect |
| `-j, --json` | 以 JSON 格式输出 | `false` |
| `-q, --quiet` | 仅输出文件路径 | `false` |

**CI/钩子示例：**

```bash
#!/usr/bin/env bash
AFFECTED=$(git diff --name-only HEAD | codegraph affected --stdin --quiet)
if [ -n "$AFFECTED" ]; then
  npx vitest run $AFFECTED
fi
```

---

## MCP 工具

作为 MCP Server 运行时，CodeGraph 向 Claude Code 暴露以下工具：

| Tool | 用途 |
|------|---------|
| `codegraph_explore` | **核心工具。** 一次调用回答几乎所有问题——“X 是如何工作的”、流程（“X 如何到达 Y”）或区域概览，返回相关符号的原始源码（按文件分组）、关系映射及影响范围。可追踪动态分派跳转（回调、React 重渲染、接口→实现），这是 `grep` 无法跟随的。 |
| `codegraph_search` | 按名称在代码库中查找符号 |
| `codegraph_callers` | 查找调用某函数的代码 |
| `codegraph_callees` | 查找某函数调用的代码 |
| `codegraph_impact` | 分析修改符号影响的代码范围 |
| `codegraph_node` | 获取特定符号的详细信息+完整源码（针对歧义名称会返回所有重载） |
| `codegraph_files` | 获取索引的文件结构（比文件系统扫描更快） |
| `codegraph_status` | 检查索引健康状态和统计信息 |

---

## 库集成使用

CodeGraph 支持直接嵌入。npm 包导出了其编程 API，因此 `import` 和 `require` 均可在你的进程中解析到 `CodeGraph` 类——非常适合将其嵌入应用（例如 Electron 主进程）。

```typescript
import CodeGraph from '@colbymchenry/codegraph';
// CommonJS 同样适用：
//   const { CodeGraph } = require('@colbymchenry/codegraph');

const cg = await CodeGraph.init('/path/to/project');
// Or: const cg = await CodeGraph.open('/path/to/project');

await cg.indexAll({
  onProgress: (p) => console.log(`${p.phase}: ${p.current}/${p.total}`)
});

const results = cg.searchNodes('UserService');
const callers = cg.getCallers(results[0].node.id);
const context = await cg.buildContext('fix login bug', { maxNodes: 20, includeCode: true, format: 'markdown' });
const impact = cg.getImpactRadius(results[0].node.id, 2);

cg.watch();   // 文件变更时自动同步
cg.unwatch(); // 停止监听
cg.close();
```

更底层的构建模块也从同一入口点导出，供直接驱动图谱的调用方使用：`DatabaseConnection`、`QueryBuilder`、`getDatabasePath`、`initGrammars` / `loadGrammarsForLanguages` 和 `FileLock`。

**嵌入要求**

- 通过 npm 安装（`npm i @colbymchenry/codegraph`），以便拉取匹配的跨平台包——其中包含编译后的库及其依赖项，与包装器一同下载。
- API 在**你的运行环境**中执行，因此需要内置的 `node:sqlite`（即 **Node 22.5+**）。（当 Electron 捆绑的 Node 版本为 22.5+ 时符合要求）。CLI 和 MCP Server 不受影响——它们使用自包含的打包运行时。
- 包内附带 TypeScript 类型定义。与任何面向 Node 的库一样，请确保保留 `@types/node` 并设置 `skipLibCheck: true`（常见默认值）。

---

## 配置

无需任何配置——CodeGraph 采用零配置设计，**无需编写或同步配置文件**。语言支持根据文件扩展名自动识别；每种语言均无需额外接线配置。

默认跳过以下目录/内容：

- **依赖、构建和缓存目录**——例如 `node_modules`、`vendor`、`dist`、`build`、`target`、`.venv`、`Pods`、`.next` 等（覆盖所有[支持的技术栈](#supported-languages)）——确保图谱仅包含你的代码，而非第三方噪音。即使没有 `.gitignore` 也会生效。
- **`.gitignore` 中的所有内容**——在 Git 仓库中通过 Git 命令识别，在非 Git 项目中直接读取根目录及嵌套的 `.gitignore`。
- **大于 1MB 的文件**——如生成的包、压缩后的 JS、第三方二进制文件等。

若想排除其他内容，请将其加入 `.gitignore`。若要强制纳入默认跳过的目录（例如你确实希望索引某个 vendored 依赖），可添加否定规则 `!vendor/`。这些默认规则统一生效，因此提交依赖或构建目录不会自动将其加入图谱；必须通过 `.gitignore` 的否定规则显式启用。

## 支持的平台

每个版本均提供自包含构建（内置 Node 运行时——无需编译），覆盖三大桌面操作系统，兼容 Intel/AMD (x64) 和 ARM (arm64)：

| Platform | Architectures | Install |
|----------|---------------|---------|
| Windows | x64, arm64 | PowerShell installer or npm |
| macOS | x64, arm64 | shell installer or npm |
| Linux | x64, arm64 | shell installer or npm |

详见 [快速开始](#get-started) 中的单行安装命令。

## 支持的 Agent

交互式安装器会自动检测并配置以下各项——接入 MCP Server（其自身会交付使用指南，因此不会写入说明文件）：

- **Claude Code**
- **Cursor**
- **Codex CLI**
- **opencode**
- **Hermes Agent**
- **Gemini CLI**
- **Antigravity IDE**
- **Kiro**

## 支持的语言

| Language | Extension | Status |
|----------|-----------|--------|
| TypeScript | `.ts`, `.tsx` | Full support |
| JavaScript | `.js`, `.jsx`, `.mjs` | Full support |
| Python | `.py` | Full support |
| Go | `.go` | Full support |
| Rust | `.rs` | Full support |
| Java | `.java` | Full support |
| C# | `.cs` | Full support |
| PHP | `.php` | Full support |
| Ruby | `.rb` | Full support |
| C | `.c`, `.h` | Full support |
| C++ | `.cpp`, `.hpp`, `.cc` | Full support |
| Objective-C | `.m`, `.mm`, `.h` | Partial support (classes, protocols, methods, `@property`, `#import`, message sends; `.mm` ObjC++ may parse incompletely) |
| Swift | `.swift` | Full support |
| Kotlin | `.kt`, `.kts` | Full support |
| Scala | `.scala`, `.sc` | Full support (classes, traits, methods, type aliases, Scala 3 enums) |
| Dart | `.dart` | Full support |
| Svelte | `.svelte` | Full support (script extraction, Svelte 5 runes, SvelteKit routes) |
| Vue | `.vue` | Full support (script + script-setup extraction, Nuxt page/API/middleware routes) |
| Liquid | `.liquid` | Full support |
| Pascal / Delphi | `.pas`, `.dpr`, `.dpk`, `.lpr` | Full support (classes, records, interfaces, enums, DFM/FMX form files) |
| Lua | `.lua` | Full support (functions, methods with receivers, local variables, `require` imports, call edges) |
| Luau | `.luau` | Full support (everything in Lua, plus `type`/`export type` aliases, typed signatures, and Roblox instance-path `require`) |

## 故障排除

**"CodeGraph not initialized"** ——请先在项目目录中运行 `codegraph init`。

**Indexing is slow** ——请检查是否已排除 `node_modules` 及其他大型目录。使用 `--quiet` 可减少输出开销。

**MCP hits `database is locked`** ——当前版本不应出现此问题：CodeGraph 内置了独立的 Node 运行时，并使用 Node 内置的 `node:sqlite`（WAL 模式），该模式下并发读取绝不会阻塞写入。若仍遇到此问题：

- **You're on an old (pre-0.9) install.** Reinstall to get the bundled runtime — `curl -fsSL https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.sh | sh`（macOS/Linux），`irm https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.ps1 | iex`（Windows），或 `npm i -g @colbymchenry/codegraph@latest`。
- **`codegraph status` shows `Journal:` other than `wal`** ——该文件系统无法启用 WAL（网络共享盘和 WSL2 `/mnt` 常见此情况），导致读取会阻塞写入。请将项目（含 `.codegraph/` 文件夹）移至本地磁盘。

**MCP server not connecting** ——请确保项目已初始化/索引，验证 MCP 配置中的路径，并检查命令行能否正常执行 `codegraph serve --mcp`。

**Missing symbols** ——MCP Server 会在保存时自动同步（等待几秒）。必要时手动运行 `codegraph sync`。请确认该文件语言受支持，且未位于 `.gitignore` 或默认排除的目录中（如 `node_modules`、`dist`）。

## Star History

<a href="https://www.star-history.com/?repos=colbymchenry%2Fcodegraph&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=colbymchenry/codegraph&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=colbymchenry/codegraph&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=colbymchenry/codegraph&type=date&legend=top-left" />
 </picture>
</a>

## License

MIT

---

<div align="center">

**专为 AI 编程 Agent 打造 —— Claude Code、Cursor、Codex CLI、opencode、Hermes Agent、Gemini CLI、Antigravity IDE 和 Kiro**

[Report Bug](https://github.com/colbymchenry/codegraph/issues) · [Request Feature](https://github.com/colbymchenry/codegraph/issues)

</div>