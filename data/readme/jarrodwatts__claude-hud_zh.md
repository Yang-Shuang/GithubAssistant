# Claude HUD

一个用于 Claude Code 的插件，实时显示当前状态——上下文使用情况、活跃工具、运行中的 Agent（智能体）以及待办事项进度。始终显示在你的输入框下方。

[![License](https://img.shields.io/github/license/jarrodwatts/claude-hud?v=2)](LICENSE)
[![Stars](https://img.shields.io/github/stars/jarrodwatts/claude-hud)](https://github.com/jarrodwatts/claude-hud/stargazers)

![Claude HUD in action](claude-hud-preview-5-2.png)

> 🌐 English | [中文文档](README.zh.md)

## 安装

在 Claude Code 实例中，运行以下命令：

**步骤 1：添加市场仓库**
```
/plugin marketplace add jarrodwatts/claude-hud
```

**步骤 2：安装插件**

<details>
<summary><strong>⚠️ Linux 用户：请先点击此处</strong></summary>

在 Linux 系统中，`/tmp` 通常是一个独立的文件系统（tmpfs），这会导致插件安装失败并报错：
```
EXDEV: cross-device link not permitted
```

**解决方法**：在安装前设置 `TMPDIR`：
```bash
mkdir -p ~/.cache/tmp && TMPDIR=~/.cache/tmp claude
```

然后在该会话中运行下方的安装命令。这是 [Claude Code 的平台限制](https://github.com/anthropics/claude-code/issues/14799)。

</details>

```
/plugin install claude-hud
```

之后，重新加载插件：

```
/reload-plugins
```


**步骤 3：配置状态栏（statusline）**
```
/claude-hud:setup
```

<details>
<summary><strong>⚠️ Windows 用户：如果提示未找到 JavaScript 运行时请点击此处</strong></summary>

在 Windows 上，Claude HUD 安装仅支持 Node.js LTS 作为运行环境。如果提示未找到任何 JavaScript 运行时，请先为你的 Shell 安装 Node.js：
```powershell
winget install OpenJS.NodeJS.LTS
```
然后重启你的 Shell 并再次运行 `/claude-hud:setup`。

</details>

完成！重启 Claude Code 以加载新的 `statusLine`（状态栏）配置，HUD 就会显示。在 Windows 上，请确保在完成设置并写入新 `statusLine` 配置后完全重启 Claude Code。

---

## 什么是 Claude HUD？

Claude HUD 让你更清晰地了解 Claude Code 会话中的实时状态。

| 你看到的内容 | 为什么重要 |
|--------------|----------------|
| **项目路径** | 明确当前所在的项目（可配置显示 1-3 级目录） |
| **上下文健康度** | 在窗口满载前精确掌握剩余空间，避免为时已晚 |
| **工具活动** | 实时观察 Claude 读取、编辑和搜索文件的过程 |
| **Agent 追踪** | 查看哪些子 Agent（智能体）正在运行以及它们在做什么 |
| **待办进度** | 实时跟踪任务完成情况 |

## 显示效果

### 默认（2 行）
```
[Opus] │ my-project git:(main*)
Context █████░░░░░ 45% │ Usage ██░░░░░░░░ 25% (1h 30m / 5h)
```
- **第 1 行** — 模型名称、提供商标签（如识别到则显示，例如 `Bedrock`、`Vertex`）、项目路径、Git 分支
- **第 2 行** — 上下文进度条（绿 → 黄 → 红）及用量速率限制

### 可选行（通过 `/claude-hud:configure` 启用）
```
◐ Edit: auth.ts | ✓ Read ×3 | ✓ Grep ×2        ← 工具活动
◐ explore [haiku]: Finding auth code (2m 15s)    ← Agent 状态
▸ Fix authentication bug (2/5)                   ← 待办进度
```

---

## 工作原理

Claude HUD 基于 Claude Code 原生的 **statusline（状态栏）API** ——无需额外窗口，不依赖 tmux，在任何终端中均可正常工作。

```
Claude Code → stdin JSON → claude-hud → stdout → 显示在你的终端中
           ↘ transcript JSONL（工具、Agent、待办事项日志）
```

**核心特性：**
- 使用 Claude Code 原生 Token 数据（非估算值）
- 随 Claude Code 报告的上下文窗口大小自动缩放，包括最新的 1M 上下文会话
- 解析日志记录以获取工具/Agent 活动信息
- 每约 ~300ms 更新一次

---

## 配置说明

随时自定义你的 HUD：

```
/claude-hud:configure
```

引导式流程可处理布局、语言和常用显示开关。高级覆盖设置（如自定义颜色和阈值）会保留在配置文件中，但你也可以通过直接编辑配置文件进行设置：

- **首次设置**：选择一个预设方案（Full/Essential/Minimal），选择标签语言，然后微调各个元素
- **随时自定义**：切换项目显隐、调整 Git 显示样式、更换布局或更改标签语言
- **保存前预览**：在提交更改前精确查看 HUD 的最终效果

### 预设方案

| 预设 | 显示内容 |
|--------|--------------|
| **Full（完整）** | 全部启用——工具、Agent、待办事项、Git、用量、持续时间 |
| **Essential（基础）** | 活动行 + Git 状态，信息精简无冗余 |
| **Minimal（极简）** | 仅核心内容——模型名称和上下文进度条 |

选择预设后，你可单独开启或关闭各个元素。

### 手动配置

直接编辑 `~/.claude/plugins/claude-hud/config.json` 可设置高级选项，例如 `colors.*`、
`pathLevels`、`maxWidth`、阈值覆盖、`display.timeFormat` 和 `display.promptCacheTtlSeconds`。运行 `/claude-hud:configure`
会保留这些手动设置，同时允许你修改 `language`、布局和常用的引导式开关。

“中文 HUD 标签”需显式开启。除非你在 `/claude-hud:configure` 中选择 `中文` 或在配置中设置 `language`，否则默认保持英文。短别名 `zh` 依然有效，新的引导式配置会写入标准值 `zh-Hans`。

### 选项说明

| 选项 | 类型 | 默认值 | 描述 |
|--------|------|---------|-------------|
| `language` | `en` \| `zh` \| `zh-Hans` | `en` | HUD 标签语言。默认为英文；设置为 `zh` 或 `zh-Hans` 可启用简体中文标签。 |
| `lineLayout` | string | `expanded` | 布局：`expanded`（多行）或 `compact`（单行） |
| `pathLevels` | 1-3 | 1 | 项目路径中显示的目录层级数 |
| `maxWidth` | number \| `null` | `null` | 仅在终端宽度检测完全失败时使用的可选回退宽度 |
| `forceMaxWidth` | boolean | false | 当设置了 `maxWidth` 时，即使检测到更小的终端宽度也强制使用它 |
| `elementOrder` | string[] | `["project","context","usage","promptCache","memory","environment","tools","agents","todos","sessionTime"]` | 展开模式下的元素顺序。省略某项将在展开模式下隐藏该元素。现有配置将保留其显式顺序直至更新。 |
| `display.mergeGroups` | string[][] | `[["context","usage"]]` | 在展开模式下，相邻时应共享同一行的元素组。设置为 `[]` 可禁用合并行功能。 |
| `gitStatus.enabled` | boolean | true | 是否在 HUD 中显示 Git 分支 |
| `gitStatus.showDirty` | boolean | true | 是否对未提交的更改显示 `*` |
| `gitStatus.showAheadBehind` | boolean | false | 是否显示与远程仓库的领先/落后数量（格式为 `↑N ↓N`） |
| `gitStatus.pushWarningThreshold` | number | 0 | 当未推送提交数达到此阈值时，将领先计数着色为警告色（设为 `0` 则禁用） |
| `gitStatus.pushCriticalThreshold` | number | 0 | 同上，但使用严重错误颜色 |
| `gitStatus.showFileStats` | boolean | false | 是否显示文件变更统计 `!M +A ✘D ?U` |
| `gitStatus.branchOverflow` | `truncate` \| `wrap` | `truncate` | 保持当前截断行为，或允许 Git 区块在可能时换行到独立边界 |
| `display.showModel` | boolean | true | 是否显示模型名称（如 `[Opus]`） |
| `display.showAddedDirs` | boolean | true | 是否显示通过 `/add-dir` 添加的额外工作区目录（例如 `+sparkle +lib-foo`）；空数组则不渲染。两种布局下最多显示 5 个目录（超出部分以 `+N more` 显示），且基名截断为 24 字符并附加 `…` |
| `display.addedDirsLayout` | `inline` \| `line` | `inline` | `inline`：将目录紧跟项目名称，每个目录前加 `+name` 前缀；`line`：在独立的 `Added dirs: name1, name2` 行渲染（无前缀，逗号分隔） |
| `display.showContextBar` | boolean | true | 是否显示可视化上下文进度条 `████░░░░░░` |
| `display.contextValue` | `percent` \| `tokens` \| `remaining` \| `both` | `percent` | 上下文显示格式（如 `45%`、`45k/200k`、剩余 `55%`，或 `45% (45k/200k)`） |
| `display.showConfigCounts` | boolean | false | 是否显示 CLAUDE.md、规则、MCP、Hooks 的数量统计 |
| `display.showCost` | boolean | false | 是否显示会话成本（优先使用 Claude Code 原生的 `cost.total_cost_usd`，若不可用则回退到本地估算） |
| `display.showOutputStyle` | boolean | false | 是否从设置文件中读取并显示当前生效的 Claude Code `outputStyle`（格式为 `style: <name>`） |
| `display.showDuration` | boolean | false | 是否显示会话持续时间 `⏱️ 5m` |
| `display.showSpeed` | boolean | false | 是否显示输出 Token 速度 `out: 42.1 tok/s` |
| `display.showUsage` | boolean | true | 是否在可用时显示 Claude 订阅用户的用量限制 |
| `display.usageValue` | `percent` \| `remaining` | `percent` | 用量显示格式（已用百分比如 `25%`，或剩余百分比如 `75%`） |
| `display.usageBarEnabled` | boolean | true | 是否以可视化进度条而非纯文本形式展示用量 |
| `display.usageCompact` | boolean | false | 是否以更短的文本形式显示用量（例如 `5h: 25% (1h 30m)`）；该选项优先级高于 `display.usageBarEnabled` |
| `display.showResetLabel` | boolean | true | 是否在用量倒计时前显示 `resets in` 前缀 |
| `display.timeFormat` | `relative` \| `absolute` \| `both` \| `elapsed` \| `elapsedAndAbsolute` | `relative` | 用量窗口时间的显示方式：仅倒计时（如 `resets in 2h 30m`）、绝对时间/时钟时间（如 `resets at 14:30`）、两者兼有、已过时间百分比（如 `53% elapsed`），或已过时间加绝对时间 |
| `display.sevenDayThreshold` | 0-100 | 80 | 当用量达到此阈值时显示 7 天用量统计（设为 `0` 表示始终显示） |
| `display.externalUsagePath` | string | `""` | 可选的本地用量快照文件路径，仅在 stdin 缺少 `rate_limits` 时使用 |
| `display.externalUsageWritePath` | string | `""` | 可选的绝对 `.json` 路径（需位于已存在的目录中）。当 stdin 存在 `rate_limits` 时，ClaudeHUD 会写入私有快照供其他本地工具使用。忽略相对路径、非 json 文件及缺失父目录的情况 |
| `display.externalUsageFreshnessMs` | number | `300000` | 外部用量快照被忽略前允许的最大年龄（毫秒） |
| `display.showTokenBreakdown` | boolean | true | 上下文使用率较高时（85%+）是否显示 Token 明细 |
| `display.showTools` | boolean | false | 是否显示工具活动行 |
| `display.toolNameMaxLength` | number | `0` | 工具名称最大显示长度。`0` 表示保留完整名称；截断时 MCP 名称可能仅显示最后一段 |
| `display.toolsMaxVisible` | number | `4` | 工具行上最多显示的已完成工具数量。`0` 表示无限制 |
| `display.showAgents` | boolean | false | 是否显示 Agent（智能体）活动行 |
| `display.showTodos` | boolean | false | 是否显示待办事项进度行 |
| `display.showSessionName` | boolean | false | 是否显示会话 Slug 或通过 `/rename` 设置的自定义标题 |
| `display.showSessionStartDate` | boolean | false | 是否显示会话开始时间戳（来自日志记录） |
| `display.showLastResponseAt` | boolean | false | 是否显示距离上次助手回复的时间间隔 |
| `display.showClaudeCodeVersion` | boolean | false | 是否显示已安装的 Claude Code 版本（例如 `CC v2.1.81`） |
| `display.showMemoryUsage` | boolean | false | 是否在展开布局中显示近似系统内存占用行 |
| `display.showPromptCache` | boolean | false | 是否基于日志记录中最后一次助手回复的时间戳，显示提示词缓存倒计时 |
| `display.promptCacheTtlSeconds` | number | `300` | 提示词缓存过期时间（秒）。Pro 版本请保持默认；Max 版本建议设为 `3600` |
| `colors.context` | color value | `green` | 上下文进度条和百分比的基础颜色 |
| `colors.usage` | color value | `brightBlue` | 用量进度条及低于警告阈值的百分比基础色 |
| `colors.warning` | color value | `yellow` | 上下文阈值和用量警告文本的警告色 |
| `colors.usageWarning` | color value | `brightMagenta` | 接近阈值的用量进度条和百分比警告色 |
| `colors.critical` | color value | `red` | 达到限制状态及严重阈值的危险色 |
| `colors.model` | color value | `cyan` | 模型徽章（如 `[Opus]`）的颜色 |
| `colors.project` | color value | `yellow` | 项目路径的颜色 |
| `colors.git` | color value | `magenta` | Git 包装文本（如 `git:(` 和 `)`）的颜色 |
| `colors.gitBranch` | color value | `cyan` | Git 分支及状态文本的颜色 |
| `colors.label` | color value | `dim` | 标签和次要元数据（如 `Context`、`Usage`、计数和进度文本）的颜色 |
| `colors.custom` | color value | `208` | 可选自定义行的颜色 |
| `colors.barFilled` | string | `█` | 用于进度条已填充部分的字符 |
| `colors.barEmpty` | string | `░` | 用于进度条空白部分的字符 |

`colors.barFilled` 和 `colors.barEmpty` 接受单个可见字形（grapheme）字符。控制字符、不可见格式字符（双向控制符、零宽连接符、变体选择器）、段落分隔符及非字符将被拒绝。宽字符（Emoji、中日韩文字）可能会因终端差异影响进度条对齐效果。

支持的颜色名称：`dim`, `red`, `green`, `yellow`, `magenta`, `cyan`, `brightBlue`, `brightMagenta`。也可使用 256 色编号 (`0-255`) 或十六进制值 (`#rrggbb`)。

`display.showMemoryUsage` 为完全可选功能，仅在 `expanded`（展开）布局中渲染。它报告本地机器的近似系统内存占用情况，而非 Claude Code 内部或特定进程内的精确内存压力。该数值可能高估实际压力，因为可回收的操作系统缓存和缓冲区仍可能被计入已用内存。

`display.showCost` 为完全可选功能。ClaudeHUD 优先使用 Claude Code 通过 stdin 提供的原生 `cost.total_cost_usd` 字段（若可用）。如果该字段在直接 Anthropic 会话中缺失或无效，ClaudeHUD 会回退到现有的基于本地日志的估算值，以确保旧版负载下的成本行仍可使用。由于会话中的原生字段直到第一次 API 响应后才出现，因此成本显示可能会在那之前保持隐藏。对于已知的路由提供商（如 Bedrock 和 Vertex AI），ClaudeHUD 也会隐藏成本显示，因为云提供商计费的会话可能报告 `$0.00` 或省略该字段，尽管会话并非字面意义上的免费。

`display.showPromptCache` 为完全可选功能。启用后，ClaudeHUD 会查看本地日志记录中最后一次助手回复的时间戳，并实时显示提示词缓存过期倒计时。默认 TTL 为 5 分钟（`300` 秒）。若希望使用 1 小时的 Max 风格窗口，可设置 `display.promptCacheTtlSeconds` 为 `3600`。如果日志记录尚未包含助手时间戳，则缓存元素保持隐藏。

### 用量限制说明

当 Claude Code 通过 stdin 提供订阅用户的 `rate_limits`（速率限制）数据时，用量显示**默认启用**。它会在第 2 行与上下文进度条并列展示你的速率限制消耗情况。

将 `display.usageValue` 设置为 `remaining` 可改为显示剩余配额而非已用配额。警告颜色和 7 天阈值检查仍基于底层已用百分比计算。

ClaudeHUD 优先使用官方 statusline stdin 负载数据。如果缺少 `rate_limits`，你可以通过设置 `display.externalUsagePath` 为其他工具（如代理）写入的 JSON 快照来启用本地旁路回退。当两个源都存在时，stdin 始终优先。

回退快照必须足够新鲜（符合 `display.externalUsageFreshnessMs`），并包含有效的 `updated_at`，以及 `five_hour` 窗口、`seven_day` 窗口或 `balance_label`。`balance_label` 是可选的预付费提供商余额说明文本；显示前会进行修剪、长度限制和清理处理。无效 JSON、过期文件或无效时间戳将被静默忽略。

如果你希望 ClaudeHUD 将官方 stdin `rate_limits` 写入本地快照供其他工具使用，请设置 `display.externalUsageWritePath`。路径必须是绝对的、以 `.json` 结尾，且位于已存在的目录中。ClaudeHUD 会以私有权限写入文件，并静默忽略无效路径。

免费/仅周额度账户会单独显示周窗口，而不是显示占位符 `5h: --`。

当用量超过 `display.sevenDayThreshold`（默认 80%）时会出现 7 天百分比：

```
Context █████░░░░░ 45% │ Usage ██░░░░░░░░ 25% (1h 30m / 5h) | ██████████ 85% (2d / 7d)
```

要禁用，请将 `display.showUsage` 设置为 `false`。

重置时间默认使用相对倒计时。将 `display.timeFormat` 设置为 `absolute` 可显示时钟时间，`both` 同时显示两种形式，`elapsed` 显示你在每个用量窗口中的进度百分比，或 `elapsedAndAbsolute` 显示已过时间及绝对重置时间。该设置目前仅支持手动配置；`/claude-hud:configure` 会保留它而不进行修改。

如果你希望更短的用量倒计时格式（如 `(3h 17m)` 而非 `(resets in 3h 17m)`），请将 `display.showResetLabel` 设置为 `false`。

如果你想要仅用量的短文本形式（例如 `5h: 25% (1h 30m)`），请将 `display.usageCompact` 设置为 `true`。紧凑用量优先级高于 `display.usageBarEnabled`。

**要求：**
- Claude Code 必须在当前会话的 stdin 中包含订阅用户的 `rate_limits` 数据
- API Key 独占用户不可用此功能

**故障排除：** 如果用量未显示：
- 确保你使用的是 Claude 订阅账户登录（而非 API Key）
- 检查配置中 `display.showUsage` 是否未被设置为 `false`
- API 用户不会看到用量显示（他们按 Token 计费，无速率限制）
- AWS Bedrock 模型会显示 `Bedrock` 并隐藏用量限制（用量由 AWS 管理）
- Google Vertex AI 模型会显示 `Vertex` 并隐藏成本估算（定价与 Anthropic 直接调用不同）
- Claude Code 可能在会话中第一次模型响应后才填充 `rate_limits`
- 某些 Claude Code 构建版本和订阅层级可能仍会在首次响应后省略 `rate_limits`
- 如果你配置了 `display.externalUsagePath`，ClaudeHUD 会先尝试该本地快照再隐藏用量
- ClaudeHUD 绝不会回退到凭据抓取或未记录的 API 调用

示例回退快照：

```json
{
  "updated_at": "2026-04-20T12:00:00.000Z",
  "five_hour": {
    "used_percentage": 42,
    "resets_at": "2026-04-20T15:00:00.000Z"
  },
  "seven_day": {
    "used_percentage": 84,
    "resets_at": "2026-04-27T12:00:00.000Z"
  }
}
```

### 配置示例

```json
{
  "language": "zh",
  "lineLayout": "expanded",
  "pathLevels": 2,
  "elementOrder": ["project", "tools", "context", "usage", "memory", "environment", "agents", "todos", "sessionTime"],
  "gitStatus": {
    "enabled": true,
    "showDirty": true,
    "showAheadBehind": true,
    "showFileStats": true
  },
  "display": {
    "showTools": true,
    "showAgents": true,
    "showTodos": true,
    "showConfigCounts": true,
    "showDuration": true,
    "showMemoryUsage": true
  },
  "colors": {
    "context": "cyan",
    "usage": "cyan",
    "warning": "yellow",
    "usageWarning": "magenta",
    "critical": "red",
    "model": "cyan",
    "project": "yellow",
    "git": "magenta",
    "gitBranch": "cyan",
    "label": "dim",
    "custom": "#FF6600"
  }
}
```

### 显示效果示例

**1 级（默认）：** `[Opus] │ my-project git:(main)`

**2 级：** `[Opus] │ apps/my-project git:(main)`

**3 级：** `[Opus] │ dev/apps/my-project git:(main)`

**含未提交指示器：** `[Opus] │ my-project git:(main*)`

**含领先/落后状态：** `[Opus] │ my-project git:(main ↑2 ↓1)`

**含文件统计：** `[Opus] │ my-project git:(main* !3 +1 ?2)`
- `!` = 已修改文件，`+` = 新增/暂存，`✘` = 已删除，`?` = 未跟踪
- 数量为 0 的项会被省略以保持显示整洁

### 故障排除

**配置未生效？**
- 检查 JSON 语法错误：无效 JSON 会静默回退到默认值
- 确保值为有效类型：`pathLevels` 必须为 1、2 或 3；`lineLayout` 必须为 `expanded` 或 `compact`；`maxWidth` 必须为正数
- 删除配置文件并运行 `/claude-hud:configure` 重新生成

**Git 状态缺失？**
- 确认你当前处于 Git 仓库中
- 检查配置中 `gitStatus.enabled` 是否未被设置为 `false`

**工具/Agent/待办行缺失？**
- 这些默认隐藏——需在配置中启用 `showTools`、`showAgents`、`showTodos`
- 它们仅在有活动数据时才会显示

**设置完成后 HUD 未出现？**
- 重启 Claude Code 以加载新的 statusLine 配置
- macOS 用户需完全退出 Claude Code，并在终端重新运行 `claude`

---

## 环境要求

- Claude Code v1.0.80+
- macOS/Linux：Node.js 18+ 或 Bun
- Windows：Node.js 18+

---

## 开发指南

```bash
git clone https://github.com/jarrodwatts/claude-hud
cd claude-hud
npm ci && npm run build
npm test
```

详见 [CONTRIBUTING.md](CONTRIBUTING.md) 获取贡献指南。

---

## 开源许可

MIT —— 详见 [LICENSE](LICENSE)

---

## 星标历史

[![Star History Chart](https://api.star-history.com/svg?repos=jarrodwatts/claude-hud&type=Date)](https://star-history.com/#jarrodwatts/claude-hud&Date)