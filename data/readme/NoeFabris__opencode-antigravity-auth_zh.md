# 适用于 OpenCode 的 Antigravity + Gemini CLI OAuth 插件

[![npm version](https://img.shields.io/npm/v/opencode-antigravity-auth.svg)](https://www.npmjs.com/package/opencode-antigravity-auth)
[![npm beta](https://img.shields.io/npm/v/opencode-antigravity-auth/beta.svg?label=beta)](https://www.npmjs.com/package/opencode-antigravity-auth)
[![npm downloads](https://img.shields.io/npm/dw/opencode-antigravity-auth.svg)](https://www.npmjs.com/package/opencode-antigravity-auth)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![X (Twitter)](https://img.shields.io/badge/X-@dopesalmon-000000?style=flat&logo=x)](https://x.com/dopesalmon)

通过 OAuth 让 OpenCode 向 **Antigravity**（Google 的 IDE）进行身份验证，以便你使用 Antigravity 的速率限制（rate limits），并通过你的 Google 凭证访问 `gemini-3.1-pro` 和 `claude-opus-4-6-thinking` 等模型。

## 功能特性

- **Claude Opus 4.6、Sonnet 4.6** 以及 **Gemini 3.1 Pro/Flash**（通过 Google OAuth）
- **多账户支持** — 添加多个 Google 账户，速率受限时自动轮换
- **双配额系统** — 从一个插件同时访问 Antigravity 和 Gemini CLI 的配额
- **思考型模型** — Claude 和 Gemini 3 的可配置扩展思考（extended thinking）预算
- **Google Search grounding** — 为 Gemini 模型启用网页搜索（自动或始终开启）
- **自动恢复** — 自动处理会话错误和工具故障
- **插件兼容** — 可与其他 OpenCode 插件并行工作（如 oh-my-opencode、dcp 等）

---

<details open>
<summary><b>⚠️ 服务条款警告 — 安装前必读</b></summary>

> [!CAUTION]
> 使用此插件（以及任何 Antigravity 代理工具）违反 Google 的服务条款。许多用户报告其 Google 账户被**封禁**或**影子封禁**（限制访问且无明确通知）。
>
> **使用本插件即表示你确认：**
> - 此为未经 Google 官方认可的第三方工具
> - 你的账户可能被暂停或永久封禁
> - 你将自行承担使用该插件相关的所有风险

</details>

---

## 安装

<details open>
<summary><b>面向用户</b></summary>

**选项 A：让 LLM 智能体帮你完成**

将此内容粘贴到任意 LLM agent（Claude Code、OpenCode、Cursor 等）中：

```
Install the opencode-antigravity-auth plugin and add the Antigravity model definitions to ~/.config/opencode/opencode.json by following: https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/dev/README.md
```

**选项 B：手动设置**

1. **添加插件**到 `~/.config/opencode/opencode.json`：

   ```json
   {
     "plugin": ["opencode-antigravity-auth@latest"]
   }
   ```

   > 想要抢先体验新功能？请改用 `opencode-antigravity-auth@beta`。

2. **登录**你的 Google 账户：

   ```bash
   opencode auth login
   ```

3. **添加模型** — 任选其一：
   - 运行 `opencode auth login` → Google → OAuth with Google (Antigravity) → 选择 **"Configure models in opencode.json"**（自动配置所有模型）
   - 或手动复制下方的[完整配置](#models)

4. **使用它：**

   ```bash
   opencode run "Hello" --model=google/antigravity-claude-opus-4-6-thinking --variant=max
   ```

</details>

<details>
<summary><b>面向 LLM 智能体</b></summary>

### 逐步操作指南

1. 编辑 OpenCode 配置文件 `~/.config/opencode/opencode.json`
   
   > **注意**：此路径适用于所有平台。在 Windows 上，`~` 会解析为你的用户主目录（例如 `C:\Users\YourName`）。

2. 将插件添加到 `plugin` 数组中

3. 从[完整模型配置](#models)部分添加模型定义

4. 设置 `provider` 为 `"google"` 并选择一个模型

### 验证安装

```bash
opencode run "Hello" --model=google/antigravity-claude-opus-4-6-thinking --variant=max
```

</details>

---

## 模型

### 模型参考

**Antigravity 配额**（Claude 和 Gemini 的默认路由）：

| Model | Variants | Notes |
|-------|----------|-------|
| `antigravity-gemini-3-pro` | low, high | 带思考功能的 Gemini 3 Pro |
| `antigravity-gemini-3.1-pro` | low, high | 带思考功能的 Gemini 3.1 Pro（依赖灰度发布） |
| `antigravity-gemini-3-flash` | minimal, low, medium, high | 带思考功能的 Gemini 3 Flash |
| `antigravity-claude-sonnet-4-6` | — | Claude Sonnet 4.6 |
| `antigravity-claude-opus-4-6-thinking` | low, max | 带扩展思考的 Claude Opus 4.6 |

**Gemini CLI 配额**（独立于 Antigravity；当 `cli_first` 为 true 或作为回退时使用）：

| Model | Notes |
|-------|-------|
| `gemini-2.5-flash` | Gemini 2.5 Flash |
| `gemini-2.5-pro` | Gemini 2.5 Pro |
| `gemini-3-flash-preview` | Gemini 3 Flash（预览版） |
| `gemini-3-pro-preview` | Gemini 3 Pro（预览版） |
| `gemini-3.1-pro-preview` | Gemini 3.1 Pro（预览版，依赖灰度发布） |
| `gemini-3.1-pro-preview-customtools` | Gemini 3.1 Pro Preview Custom Tools（预览版，依赖灰度发布） |

> **路由行为：**
> - **Antigravity优先（默认）**：Gemini 模型跨账户使用 Antigravity 配额。
> - **CLI优先 (`cli_first: true`)**：Gemini 模型优先使用 Gemini CLI 配额。
> - 当某个 Gemini 配额池耗尽时，插件会自动回退到另一个配额池。
> - Claude 和图像模型始终使用 Antigravity。
> 模型名称会自动为目标 API 进行转换（例如 `antigravity-gemini-3-flash` → CLI 的 `gemini-3-flash-preview`）。

**使用变体：**
```bash
opencode run "Hello" --model=google/antigravity-claude-opus-4-6-thinking --variant=max
```

关于变体配置和思考级别的详细信息，请参阅 [docs/MODEL-VARIANTS.md](docs/MODEL-VARIANTS.md)。

<details>
<summary><b>完整模型配置（可直接复制粘贴）</b></summary>

将其添加到你的 `~/.config/opencode/opencode.json` 中：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["opencode-antigravity-auth@latest"],
  "provider": {
    "google": {
      "models": {
        "antigravity-gemini-3-pro": {
          "name": "Gemini 3 Pro (Antigravity)",
          "limit": { "context": 1048576, "output": 65535 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] },
          "variants": {
            "low": { "thinkingLevel": "low" },
            "high": { "thinkingLevel": "high" }
          }
        },
        "antigravity-gemini-3.1-pro": {
          "name": "Gemini 3.1 Pro (Antigravity)",
          "limit": { "context": 1048576, "output": 65535 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] },
          "variants": {
            "low": { "thinkingLevel": "low" },
            "high": { "thinkingLevel": "high" }
          }
        },
        "antigravity-gemini-3-flash": {
          "name": "Gemini 3 Flash (Antigravity)",
          "limit": { "context": 1048576, "output": 65536 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] },
          "variants": {
            "minimal": { "thinkingLevel": "minimal" },
            "low": { "thinkingLevel": "low" },
            "medium": { "thinkingLevel": "medium" },
            "high": { "thinkingLevel": "high" }
          }
        },
        "antigravity-claude-sonnet-4-6": {
          "name": "Claude Sonnet 4.6 (Antigravity)",
          "limit": { "context": 200000, "output": 64000 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] }
        },
        "antigravity-claude-opus-4-6-thinking": {
          "name": "Claude Opus 4.6 Thinking (Antigravity)",
          "limit": { "context": 200000, "output": 64000 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] },
          "variants": {
            "low": { "thinkingConfig": { "thinkingBudget": 8192 } },
            "max": { "thinkingConfig": { "thinkingBudget": 32768 } }
          }
        },
        "gemini-2.5-flash": {
          "name": "Gemini 2.5 Flash (Gemini CLI)",
          "limit": { "context": 1048576, "output": 65536 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] }
        },
        "gemini-2.5-pro": {
          "name": "Gemini 2.5 Pro (Gemini CLI)",
          "limit": { "context": 1048576, "output": 65536 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] }
        },
        "gemini-3-flash-preview": {
          "name": "Gemini 3 Flash Preview (Gemini CLI)",
          "limit": { "context": 1048576, "output": 65536 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] }
        },
        "gemini-3-pro-preview": {
          "name": "Gemini 3 Pro Preview (Gemini CLI)",
          "limit": { "context": 1048576, "output": 65535 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] }
        },
        "gemini-3.1-pro-preview": {
          "name": "Gemini 3.1 Pro Preview (Gemini CLI)",
          "limit": { "context": 1048576, "output": 65535 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] }
        },
        "gemini-3.1-pro-preview-customtools": {
          "name": "Gemini 3.1 Pro Preview Custom Tools (Gemini CLI)",
          "limit": { "context": 1048576, "output": 65535 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] }
        }
      }
    }
  }
}
```

> **向后兼容：** 带有 `antigravity-` 前缀的旧版模型名称（例如 `antigravity-gemini-3-flash`）仍然有效。插件会自动处理 Antigravity 和 Gemini CLI API 之间的模型名称转换。

</details>

---

## 多账户设置

添加多个 Google 账户以获得更高的综合配额。当一个账户速率受限时，插件会在账户间自动轮换。

```bash
opencode auth login  # 再次运行以添加更多账户
```

**账户管理选项（通过 `opencode auth login`）：**
- **Configure models** — 在 opencode.json 中自动配置所有插件模型
- **Check quotas** — 查看每个账户的剩余 API 配额
- **Manage accounts** — 启用/禁用特定账户用于轮换

关于负载均衡、双配额池和账户存储的详细信息，请参阅 [docs/MULTI-ACCOUNT.md](docs/MULTI-ACCOUNT.md)。

---

## 故障排除

> **快速重置：** 大多数问题可以通过删除 `~/.config/opencode/antigravity-accounts.json` 并重新运行 `opencode auth login` 来解决。

### 配置路径（全平台）

OpenCode 在**所有平台**（包括 Windows）上使用 `~/.config/opencode/`。

| File | Path |
|------|------|
| Main config | `~/.config/opencode/opencode.json` |
| Accounts | `~/.config/opencode/antigravity-accounts.json` |
| Plugin config | `~/.config/opencode/antigravity.json` |
| Debug logs | `~/.config/opencode/antigravity-logs/` |

> **Windows 用户**：`~` 会解析为你的用户主目录（例如 `C:\Users\YourName`）。请勿使用 `%APPDATA%`。

> **自定义路径**：设置 `OPENCODE_CONFIG_DIR` 环境变量以使用自定义位置。

> **Windows 迁移**：如果从插件 v1.3.x 或更早版本升级，插件会自动在 `%APPDATA%\opencode\` 中找到你的现有配置并使用它。新安装默认使用 `~/.config/opencode/`。

---

### 多账户认证问题

如果你遇到多个账户的认证问题：

1. 删除账户文件：
   ```bash
   rm ~/.config/opencode/antigravity-accounts.json
   ```
2. 重新进行身份验证：
   ```bash
   opencode auth login
   ```

---

### 403 Permission Denied (`rising-fact-p41fc`)

**错误：**
```
Permission 'cloudaicompanion.companions.generateChat' denied on resource 
'//cloudaicompanion.googleapis.com/projects/rising-fact-p41fc/locations/global'
```

**原因：** 当未找到有效项目时，插件会回退到默认 project ID。这适用于 Antigravity，但对 Gemini CLI 模型会失败。

**解决方案：**
1. 前往 [Google Cloud Console](https://console.cloud.google.com/)
2. 创建或选择一个项目
3. 启用 **Gemini for Google Cloud API** (`cloudaicompanion.googleapis.com`)
4. 在账户文件中添加 `projectId`：
   ```json
   {
     "accounts": [
       {
         "email": "your@email.com",
         "refreshToken": "...",
         "projectId": "your-project-id"
       }
     ]
   }
   ```

> **注意**：在多账户设置中，请对每个账户执行此操作。

---

### Gemini Model Not Found

在你的 `google` provider 配置中添加以下内容：

```json
{
  "provider": {
    "google": {
      "npm": "@ai-sdk/google",
      "models": { ... }
    }
  }
}
```

---

### Gemini 3 Models 400 Error ("Unknown name 'parameters'")

**错误：**
```
Invalid JSON payload received. Unknown name "parameters" at 'request.tools[0]'
```

**原因：**
- 工具 schema 与 Gemini 严格的 protobuf 验证不兼容
- MCP servers 存在格式错误的 schemas
- 插件版本回退（regression）

**解决方案：**
1. **更新到最新 beta 版：**
   ```json
   { "plugin": ["opencode-antigravity-auth@beta"] }
   ```

2. **逐个禁用 MCP servers** 以找出问题来源

3. **添加 npm override：**
   ```json
   { "provider": { "google": { "npm": "@ai-sdk/google" } } }
   ```

---

### MCP Servers Causing Errors

部分 MCP servers 的 schema 与 Antigravity 严格的 JSON 格式不兼容。

**常见症状：**
```bash
Invalid function name must start with a letter or underscore
```

有时显示为：
```bash
GenerateContentRequest.tools[0].function_declarations[12].name: Invalid function name must start with a letter or underscore
```

这通常意味着某个 MCP 工具名称以数字开头（例如 `1mcp` 键如 `1mcp_*`）。将 MCP 键重命名为字母开头（例如 `gw`），或为 Antigravity 模型禁用该 MCP 条目。

**诊断步骤：**
1. 在配置中禁用所有 MCP servers
2. 逐个启用直到错误重现
3. 在 [GitHub issue](https://github.com/NoeFabris/opencode-antigravity-auth/issues) 中报告具体的 MCP 问题

---

### "All Accounts Rate-Limited" (But Quota Available)

**原因：** `clearExpiredRateLimits()` 在混合模式（hybrid mode）中存在级联 bug（已在近期 beta 版修复）。

**解决方案：**
1. 更新到最新 beta 版本
2. 如果问题持续，删除账户文件并重新认证
3. 尝试在 `antigravity.json` 中将 `account_selection_strategy` 切换为 `"sticky"`

---

### Session Recovery

如果你在会话期间遇到错误：
1. 输入 `continue` 触发恢复机制
2. 如果被阻止，使用 `/undo` 回退到错误前状态
3. 重试操作

---

### Using with Oh-My-OpenCode

**重要：** 禁用内置 Google auth 以防止冲突：

```json
// ~/.config/opencode/oh-my-opencode.json
{
  "google_auth": false,
  "agents": {
    "frontend-ui-ux-engineer": { "model": "google/antigravity-gemini-3-pro" },
    "document-writer": { "model": "google/antigravity-gemini-3-flash" }
  }
}
```

---

### Infinite `.tmp` Files Created

**原因：** 当账户速率受限时，如果插件无限重试，会创建大量临时文件。

**解决方法：**
1. 停止 OpenCode
2. 清理：`rm ~/.config/opencode/*.tmp`
3. 添加更多账户或等待速率限制过期

---

### OAuth Callback Issues

<details>
<summary><b>Safari OAuth Callback Fails (macOS)</b></summary>

**症状：**
- Google 登录成功后显示 "fail to authorize"
- Safari 提示 "Safari can't open the page"

**原因：** Safari 的 "HTTPS-Only Mode"（仅 HTTPS 模式）会阻止 `http://localhost` 回调。

**解决方案：**

1. **使用 Chrome 或 Firefox**（最简单）：
   复制 OAuth URL 并粘贴到其他浏览器中打开。

2. **临时禁用 HTTPS-Only Mode：**
   - Safari > Settings (⌘,) > Privacy
   - 取消勾选 "Enable HTTPS-Only Mode"
   - 运行 `opencode auth login`
   - 认证完成后重新启用

</details>

<details>
<summary><b>Port Conflict (Address Already in Use)</b></summary>

**macOS / Linux：**
```bash
# Find process using the port
lsof -i :51121

# Kill if stale
kill -9 <PID>

# Retry
opencode auth login
```

**Windows (PowerShell)：**
```powershell
netstat -ano | findstr :51121
taskkill /PID <PID> /F
opencode auth login
```

</details>

<details>
<summary><b>Docker / WSL2 / Remote Development</b></summary>

OAuth 回调要求浏览器能够访问运行 OpenCode 的机器的 `localhost`。

**WSL2：**
- 使用 VS Code 的端口转发，或
- 配置 Windows → WSL 端口转发

**SSH / Remote：**
```bash
ssh -L 51121:localhost:51121 user@remote
```

**Docker / Containers：**
- OAuth with localhost redirect 在容器中不起作用
- 等待 30s 进行手动 URL 流程，或使用 SSH 端口转发

</details>

---

### Configuration Key Typo: `plugin` not `plugins`

正确的键是 `plugin`（单数）：

```json
{
  "plugin": ["opencode-antigravity-auth@beta"]
}
```

**不是** `"plugins"`（会导致 "Unrecognized key" 错误）。

---

### Migrating Accounts Between Machines

将 `antigravity-accounts.json` 复制到新机器时：
1. 确保已安装插件：`"plugin": ["opencode-antigravity-auth@beta"]`
2. 复制 `~/.config/opencode/antigravity-accounts.json`
3. 如果出现 "API key missing" 错误，说明 refresh token 可能无效 — 请重新进行身份验证

## Known Plugin Interactions
关于负载均衡、双配额池和账户存储的详细信息，请参阅 [docs/MULTI-ACCOUNT.md](docs/MULTI-ACCOUNT.md)。

---

## 插件兼容性

### @tarquinen/opencode-dcp

DCP 会创建缺少思考块（thinking blocks）的合成助手消息。**将此插件排在 DCP 之前：**

```json
{
  "plugin": [
    "opencode-antigravity-auth@latest",
    "@tarquinen/opencode-dcp@latest"
  ]
}
```

### oh-my-opencode

在 `oh-my-opencode.json` 中禁用内置 auth 并覆盖 agent models：

```json
{
  "google_auth": false,
  "agents": {
    "frontend-ui-ux-engineer": { "model": "google/antigravity-gemini-3-pro" },
    "document-writer": { "model": "google/antigravity-gemini-3-flash" },
    "multimodal-looker": { "model": "google/antigravity-gemini-3-flash" }
  }
}
```

> **提示：** 当启动并行子 agent（subagents）时，在 `antigravity.json` 中启用 `pid_offset_enabled: true` 以将会话分配到不同账户。

### 无需安装的插件

- **gemini-auth plugins** — 不需要。本插件已处理所有 Google OAuth。

---

## 配置

创建 `~/.config/opencode/antigravity.json` 用于可选设置：

```json
{
  "$schema": "https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/main/assets/antigravity.schema.json"
}
```

大多数用户无需进行任何配置 — 默认值即可良好运行。

### Model Behavior

| Option | Default | What it does |
|--------|---------|--------------|
| `keep_thinking` | `false` | 跨轮次保留 Claude 的思考过程。**警告：** 启用可能会降低模型稳定性。 |
| `session_recovery` | `true` | 自动从工具错误中恢复 |
| `cli_first` | `false` | 优先将 Gemini 模型路由到 Gemini CLI（Claude 和图像模型仍保留在 Antigravity）。 |

### Account Rotation

| Your Setup | Recommended Config |
|------------|-------------------|
| **1 account** | `"account_selection_strategy": "sticky"` |
| **2-5 accounts** | 默认值 (`"hybrid"`) 效果很好 |
| **5+ accounts** | `"account_selection_strategy": "round-robin"` |
| **Parallel agents** | 添加 `"pid_offset_enabled": true` |

### Quota Protection

| Option | Default | What it does |
|--------|---------|--------------|
| `soft_quota_threshold_percent` | `90` | 当配额使用率超过此百分比时跳过该账户。防止 Google 惩罚完全耗尽配额的账户。设置为 `100` 可禁用。 |
| `quota_refresh_interval_minutes` | `15` | 后台配额刷新间隔。成功 API 请求后，如果缓存时间早于此间隔则刷新配额缓存。设置为 `0` 可禁用。 |
| `soft_quota_cache_ttl_minutes` | `"auto"` | 配额缓存被视为有效的时间长度。`"auto"` = max(2 × refresh interval, 10 minutes)。设置数字（1-120）为固定 TTL。 |

> **工作原理：** 配额缓存在 API 请求后自动刷新（当早于 `quota_refresh_interval_minutes` 时），也可通过 `opencode auth login` 中的 "Check quotas" 手动触发。阈值检查使用 `soft_quota_cache_ttl_minutes` 判断缓存新鲜度 — 如果缓存过期，该账户被视为“未知”并允许访问（fail-open）。当**所有**账户均超过阈值时，插件会等待最早的配额重置时间（类似速率限制行为）。如果等待时间超过 `max_rate_limit_wait_seconds`，则会立即报错。

### Rate Limit Scheduling

控制插件处理速率限制的方式：

| Option | Default | What it does |
|--------|---------|--------------|
| `scheduling_mode` | `"cache_first"` | `"cache_first"` = 等待同一账户（保留 prompt cache），`"balance"` = 立即切换，`"performance_first"` = 轮询（round-robin） |
| `max_cache_first_wait_seconds` | `60` | 在 cache_first 模式下切换账户前等待的最大秒数 |
| `failure_ttl_seconds` | `3600` | 超过此秒数后重置失败计数（防止旧故障永久惩罚账户） |

**何时使用各模式：**
- **cache_first**（默认）：最适合长对话。等待同一账户恢复，保留你的 prompt cache。
- **balance**：最适合快速任务。速率受限时立即切换账户以最大化可用性。
- **performance_first**：最适合大量短请求。在所有账户间均匀分配负载。

### App Behavior

| Option | Default | What it does |
|--------|---------|--------------|
| `quiet_mode` | `false` | 隐藏 toast notifications（提示通知） |
| `debug` | `false` | 启用调试文件日志记录（`~/.config/opencode/antigravity-logs/`） |
| `debug_tui` | `false` | 在 TUI log panel 中显示调试日志（独立于 `debug`） |
| `auto_update` | `true` | 自动更新插件 |

所有选项详见 [docs/CONFIGURATION.md](docs/CONFIGURATION.md)。

**环境变量：**
```bash
OPENCODE_CONFIG_DIR=/path/to/config opencode  # Custom config directory
OPENCODE_ANTIGRAVITY_DEBUG=1 opencode         # Enable debug file logging
OPENCODE_ANTIGRAVITY_DEBUG=2 opencode         # Verbose debug file logging
OPENCODE_ANTIGRAVITY_DEBUG_TUI=1 opencode     # Enable TUI log panel debug output
```

---

## 故障排除指南

请参阅完整的 [Troubleshooting Guide](docs/TROUBLESHOOTING.md) 以获取常见问题的解决方案，包括：

- Auth problems and token refresh（认证问题与令牌刷新）
- "Model not found" errors（“模型未找到”错误）
- Session recovery（会话恢复）
- Gemini CLI permission errors（Gemini CLI 权限错误）
- Safari OAuth issues（Safari OAuth 问题）
- Plugin compatibility（插件兼容性）
- Migration guides（迁移指南）

---

## 文档

- [Configuration](docs/CONFIGURATION.md) — All configuration options（所有配置选项）
- [Multi-Account](docs/MULTI-ACCOUNT.md) — Load balancing, dual quota pools, account storage（负载均衡、双配额池、账户存储）
- [Model Variants](docs/MODEL-VARIANTS.md) — Thinking budgets and variant system（思考预算与变体系统）
- [Troubleshooting](docs/TROUBLESHOOTING.md) — Common issues and fixes（常见问题与修复）
- [Architecture](docs/ARCHITECTURE.md) — How the plugin works（插件工作原理）
- [API Spec](docs/ANTIGRAVITY_API_SPEC.md) — Antigravity API reference（Antigravity API 参考）

---

## 支持

如果本插件为你节省了时间，请考虑支持其开发：

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/S6S81QBOIR)

---

## Credits

- [opencode-gemini-auth](https://github.com/jenslys/opencode-gemini-auth) by [@jenslys](https://github.com/jenslys)
- [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI)

## License

MIT License. See [LICENSE](LICENSE) for details.

<details>
<summary><b>Legal</b></summary>

### Intended Use

- Personal / internal development only（仅限个人/内部开发）
- Respect internal quotas and data handling policies（遵守内部配额与数据处理策略）
- Not for production services or bypassing intended limits（不用于生产服务或绕过预期限制）

### Warning

By using this plugin, you acknowledge:

- **Terms of Service risk** — This approach may violate ToS of AI model providers（服务条款风险 — 此方法可能违反 AI 模型提供商的服务条款）
- **Account risk** — Providers may suspend or ban accounts（账户风险 — 提供商可能会暂停或封禁账户）
- **No guarantees** — APIs may change without notice（无保证 — API 可能在未通知的情况下更改）
- **Assumption of risk** — You assume all legal, financial, and technical risks（风险自担 — 你将承担所有法律、财务和技术风险）

### Disclaimer

- Not affiliated with Google. This is an independent open-source project.（与 Google 无关。本项目为独立开源项目。）
- "Antigravity", "Gemini", "Google Cloud", and "Google" are trademarks of Google LLC.（“Antigravity”、“Gemini”、“Google Cloud”和“Google”均为 Google LLC 的商标。）

</details>