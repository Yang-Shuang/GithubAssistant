<h1 align="center">gws</h1>

**一个面向所有 Google Workspace 的 CLI —— 为人类和 AI Agent 而生。**<br>
驱动 Drive、Gmail、Calendar 以及所有 Workspace API。零样板代码。结构化 JSON 输出。内置 40+ 个 Agent 技能。

> [!NOTE]
> 这并非 Google 官方支持的产品。

<p>
  <a href="https://www.npmjs.com/package/@googleworkspace/cli"><img src="https://img.shields.io/npm/v/@googleworkspace/cli" alt="npm version"></a>
  <a href="https://github.com/googleworkspace/cli/blob/main/LICENSE"><img src="https://img.shields.io/github/license/googleworkspace/cli" alt="license"></a>
  <a href="https://github.com/googleworkspace/cli/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/googleworkspace/cli/ci.yml?branch=main&label=CI" alt="CI status"></a>
  <a href="https://www.npmjs.com/package/@googleworkspace/cli"><img src="https://img.shields.io/npm/unpacked-size/@googleworkspace/cli" alt="install size"></a>
</p>
<br>

⬇️ **[下载适用于你操作系统的最新版本](https://github.com/googleworkspace/cli/releases)**

`gws` 不附带静态命令列表。它在运行时读取 Google 的 [Discovery Service（发现服务）](https://developers.google.com/discovery)，并动态构建整个命令集。当 Google Workspace 新增 API 端点或方法时，`gws` 会自动识别并支持。

> [!IMPORTANT]
> 本项目正在积极开发中。在向 v1.0 迈进的过程中，可能会出现破坏性更新（breaking changes）。

## Contents

- [前置条件](#prerequisites)
- [安装](#installation)
- [快速开始](#quick-start)
- [为什么选择 gws？](#why-gws)
- [身份验证](#authentication)
- [AI Agent 技能](#ai-agent-skills)
- [高级用法](#advanced-usage)
- [环境变量](#environment-variables)
- [退出码](#exit-codes)
- [架构设计](#architecture)
- [故障排除](#troubleshooting)
- [开发指南](#development)

## Prerequisites

- **Node.js 18+** —— 用于运行 `npm install`（或从 [GitHub Releases](https://github.com/googleworkspace/cli/releases) 下载预编译二进制文件）
- **一个 Google Cloud 项目** —— 用于生成 OAuth 凭据。你可以通过 [Google Cloud Console](https://console.cloud.google.com/)、[`gcloud` CLI](https://cloud.google.com/sdk/docs/install)，或使用 `gws auth setup` 命令来创建。
- **一个可访问 Google Workspace 的 Google 账号**

## Installation

推荐安装方式是前往 **[GitHub Releases](https://github.com/googleworkspace/cli/releases)** 页面下载适用于你操作系统和架构的预编译二进制文件。解压归档文件，并将 `gws` 二进制文件放入你的 `$PATH` 环境变量中。

为方便起见，你也可以使用 `npm` 自动从 GitHub Releases 下载对应的二进制文件：

```bash
npm install -g @googleworkspace/cli
```

Or build from source:

```bash
cargo install --git https://github.com/googleworkspace/cli --locked
```

A Nix flake is also available at `github:googleworkspace/cli`

```bash
nix run github:googleworkspace/cli
```

On macOS and Linux, you can also install via [Homebrew](https://brew.sh/):

```bash
brew install googleworkspace-cli
```

## Quick Start

```bash
gws auth setup     # walks you through Google Cloud project config
gws auth login     # subsequent OAuth login
gws drive files list --params '{"pageSize": 5}'
```

## Why gws?

**面向人类用户** —— 告别对着 REST API 文档写 `curl` 命令的日子。`gws` 为每个资源提供 `--help`，支持 `--dry-run` 预览请求，并自动处理分页。

**面向 AI Agent** —— 所有响应均为结构化 JSON。配合内置的 Agent 技能使用，你的大语言模型（LLM）即可无需自定义工具直接管理 Workspace。

```bash
# List the 10 most recent files
gws drive files list --params '{"pageSize": 10}'

# Create a spreadsheet
gws sheets spreadsheets create --json '{"properties": {"title": "Q1 Budget"}}'

# Send a Chat message
gws chat spaces messages create \
  --params '{"parent": "spaces/xyz"}' \
  --json '{"text": "Deploy complete."}' \
  --dry-run

# Introspect any method's request/response schema
gws schema drive.files.list

# Stream paginated results as NDJSON
gws drive files list --params '{"pageSize": 100}' --page-all | jq -r '.files[].name'
```

## Authentication

该 CLI 支持多种身份验证工作流，可在你的笔记本电脑、CI 环境或服务器上正常运行。

### Which setup should I use?

| I have… | Use |
|---|---|
| `gcloud` installed and authenticated | [`gws auth setup`](#interactive-local-desktop) (fastest) |
| A GCP project but no `gcloud` | [Manual OAuth setup](#manual-oauth-setup-google-cloud-console) |
| An existing OAuth access token | [`GOOGLE_WORKSPACE_CLI_TOKEN`](#pre-obtained-access-token) |
| Existing Credentials | [`GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE`](#service-account-server-to-server) |

### Interactive (local desktop)

凭据在静态存储时已加密（AES-256-GCM），密钥保存在你的操作系统密钥环中（当 `GOOGLE_WORKSPACE_CLI_KEYRING_BACKEND=file` 时为 `~/.config/gws/.encryption_key`）。

```bash
gws auth setup       # one-time: creates a Cloud project, enables APIs, logs you in
gws auth login       # subsequent scope selection and login
```

> `gws auth setup` requires the [`gcloud` CLI](https://cloud.google.com/sdk/docs/install)。如果你没有安装 `gcloud`，请使用下方的[手动设置流程](#manual-oauth-setup-google-cloud-console)代替。

> [!WARNING]
> **测试模式下的作用域限制：** 如果你的 OAuth 应用未经验证（处于测试模式），Google 会将同意范围限制在约 25 个 scope。`recommended` 预设包含 85+ 个 scope，**对于未验证的应用会失败**（尤其是 `@gmail.com` 账号）。请改为选择单个服务以过滤作用域选择器：
> ```bash
> gws auth login -s drive,gmail,sheets
> ```


### Manual OAuth setup (Google Cloud Console)

当 `gws auth setup` 无法自动化创建项目/客户端，或你需要显式控制时使用此流程。

1. Open Google Cloud Console in the target project:
   - OAuth consent screen: `https://console.cloud.google.com/apis/credentials/consent?project=<PROJECT_ID>`
   - Credentials: `https://console.cloud.google.com/apis/credentials?project=<PROJECT_ID>`
2. Configure OAuth branding/audience if prompted:
   - App type: **External** (testing mode is fine)
3. Add your account under **Test users**
4. Create an OAuth client:
   - Type: **Desktop app**
5. Download the client JSON and save it to:
   - `~/.config/gws/client_secret.json`

> [!IMPORTANT]
> **你必须将自己添加为测试用户。** 在 OAuth consent screen 中，点击 **Test users → Add users** 并输入你的 Google 账号邮箱。否则登录将因通用的“Access blocked”错误而失败。

Then run:

```bash
gws auth login
```

### Browser-assisted auth (human or agent)

你可以通过手动操作或浏览器自动化完成 OAuth 流程。

- **手动流程**：运行 `gws auth login`，打开打印出的 URL，批准作用域。
- **Agent 辅助流程**：Agent 打开 URL，选择账号，处理同意提示，并在 localhost 回调成功后交还控制权。

如果同意页面显示 **“Google hasn't verified this app”**（测试模式），请点击 **Continue**。如果出现作用域复选框，请在继续前勾选所需的作用域或点击 **Select all**。

### Headless / CI (export flow)

1. Complete interactive auth on a machine with a browser.
2. Export credentials:
   ```bash
   gws auth export --unmasked > credentials.json
   ```
3. On the headless machine:
   ```bash
   export GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE=/path/to/credentials.json
   gws drive files list   # just works
   ```

### Service Account (server-to-server)

指向你的密钥文件；无需登录。

```bash
export GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE=/path/to/service-account.json
gws drive files list
```

### Pre-obtained Access Token

当其他工具（例如 `gcloud`）已为你的环境生成令牌时非常有用。

```bash
export GOOGLE_WORKSPACE_CLI_TOKEN=$(gcloud auth print-access-token)
```

### Precedence

| Priority | Source                 | Set via                                 |
| -------- | ---------------------- | --------------------------------------- |
| 1        | Access token           | `GOOGLE_WORKSPACE_CLI_TOKEN`            |
| 2        | Credentials file       | `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE` |
| 3        | Encrypted credentials  | `gws auth login`                        |
| 4        | Plaintext credentials  | `~/.config/gws/credentials.json`        |

环境变量也可以设置在 `.env` 文件中。

## AI Agent Skills

该仓库内置了 100+ 个 Agent 技能（`SKILL.md` 文件）—— 每个支持的 API 对应一个，此外还有针对常见工作流的高级辅助工具，以及为 Gmail、Drive、Docs、Calendar 和 Sheets 精心策划的 50 套配方。完整列表请参阅 [Skills Index](docs/skills.md)。

```bash
# Install all skills at once
npx skills add https://github.com/googleworkspace/cli

# Or pick only what you need
npx skills add https://github.com/googleworkspace/cli/tree/main/skills/gws-drive
npx skills add https://github.com/googleworkspace/cli/tree/main/skills/gws-gmail
```

<details>
<summary>OpenClaw setup</summary>

```bash
# Symlink all skills (stays in sync with repo)
ln -s $(pwd)/skills/gws-* ~/.openclaw/skills/

# Or copy specific skills
cp -r skills/gws-drive skills/gws-gmail ~/.openclaw/skills/
```

The `gws-shared` skill includes an `install` block so OpenClaw auto-installs the CLI via `npm` if `gws` isn't on PATH.

</details>

## Gemini CLI Extension

1. Authenticate the CLI first:

   ```bash
   gws auth setup
   ```

2. Install the extension into the Gemini CLI:
   ```bash
   gemini extensions install https://github.com/googleworkspace/cli
   ```

安装此扩展后，你的 Gemini CLI Agent 将直接访问所有 `gws` 命令和 Google Workspace Agent 技能。由于 `gws` 会安全地处理自身的身份验证，你只需在使用 Agent 前对终端进行一次身份验证，扩展便会自动继承你的凭据。

## Advanced Usage

### Multipart Uploads

```bash
gws drive files create --json '{"name": "report.pdf"}' --upload ./report.pdf
```

### Pagination

| Flag                | Description                                    | Default |
| ------------------- | ---------------------------------------------- | ------- |
| `--page-all`        | Auto-paginate, one JSON line per page (NDJSON) | off     |
| `--page-limit <N>`  | Max pages to fetch                             | 10      |
| `--page-delay <MS>` | Delay between pages                            | 100 ms  |

### Google Sheets — Shell Escaping

Sheets ranges use `!` which bash interprets as history expansion. Always wrap values in **single quotes**:

```bash
# Read cells A1:C10 from "Sheet1"
gws sheets spreadsheets values get \
  --params '{"spreadsheetId": "SPREADSHEET_ID", "range": "Sheet1!A1:C10"}'

# Append rows
gws sheets spreadsheets values append \
  --params '{"spreadsheetId": "ID", "range": "Sheet1!A1", "valueInputOption": "USER_ENTERED"}' \
  --json '{"values": [["Name", "Score"], ["Alice", 95]]}'
```

### Helper Commands

部分服务在自动生成的 Discovery 命令集之外，还附带了手工编写的辅助命令。辅助命令以 `+` 为前缀，以便视觉上区分且永远不会与 Discovery 生成的方法名冲突。

时间感知辅助工具（`+agenda`, `+standup-report`, `+weekly-digest`, `+meeting-prep`）会自动使用你的 **Google 账号时区**（从 Calendar Settings API 获取，缓存 24 小时）。可通过 `--timezone`/`--tz` 覆盖（在 `+agenda` 上），或设置全局 `--timezone` 标志以显式控制。

运行 `gws <service> --help` 可同时查看 Discovery 方法和辅助命令。

```bash
gws gmail --help      # shows +send, +reply, +reply-all, +forward, +triage, +watch …
gws calendar --help   # shows +insert, +agenda …
gws drive --help      # shows +upload …
```

**Full helper reference:**

| Service | Command | Description |
|---------|---------|-------------|
| `gmail` | `+send` | Send an email |
| `gmail` | `+reply` | Reply to a message (handles threading automatically) |
| `gmail` | `+reply-all` | Reply-all to a message |
| `gmail` | `+forward` | Forward a message to new recipients |
| `gmail` | `+triage` | Show unread inbox summary (sender, subject, date) |
| `gmail` | `+watch` | Watch for new emails and stream them as NDJSON |
| `sheets` | `+append` | Append a row to a spreadsheet |
| `sheets` | `+read` | Read values from a spreadsheet |
| `docs` | `+write` | Append text to a document |
| `chat` | `+send` | Send a message to a space |
| `drive` | `+upload` | Upload a file with automatic metadata |
| `calendar` | `+insert` | Create a new event |
| `calendar` | `+agenda` | Show upcoming events (uses Google account timezone; override with `--timezone`) |
| `script` | `+push` | Replace all files in an Apps Script project with local files |
| `workflow` | `+standup-report` | Today's meetings + open tasks as a standup summary |
| `workflow` | `+meeting-prep` | Prepare for your next meeting: agenda, attendees, and linked docs |
| `workflow` | `+email-to-task` | Convert a Gmail message into a Google Tasks entry |
| `workflow` | `+weekly-digest` | Weekly summary: this week's meetings + unread email count |
| `workflow` | `+file-announce` | Announce a Drive file in a Chat space |
| `events` | `+subscribe` | Subscribe to Workspace events and stream them as NDJSON |
| `events` | `+renew` | Renew/reactivate Workspace Events subscriptions |
| `modelarmor` | `+sanitize-prompt` | Sanitize a user prompt through a Model Armor template |
| `modelarmor` | `+sanitize-response` | Sanitize a model response through a Model Armor template |
| `modelarmor` | `+create-template` | Create a new Model Armor template |

**Examples:**

```bash
# Send an email
gws gmail +send --to alice@example.com --subject "Hello" --body "Hi there"

# Reply to a message
gws gmail +reply --message-id MESSAGE_ID --body "Thanks!"

# Append a row to a spreadsheet
gws sheets +append --spreadsheet SPREADSHEET_ID --values "Alice,95"

# Show today's calendar agenda
gws calendar +agenda

# Upload a file to Drive
gws drive +upload ./report.pdf --name "Q1 Report"

# Morning standup summary
gws workflow +standup-report

# Show today's agenda in a specific timezone
gws calendar +agenda --today --timezone America/New_York
```

### Model Armor (Response Sanitization)

Integrate [Google Cloud Model Armor](https://cloud.google.com/security/products/model-armor) to scan API responses for prompt injection before they reach your agent.

```bash
gws gmail users messages get --params '...' \
  --sanitize "projects/P/locations/L/templates/T"
```

| Variable                                 | Description                  |
| ---------------------------------------- | ---------------------------- |
| `GOOGLE_WORKSPACE_CLI_SANITIZE_TEMPLATE` | Default Model Armor template |
| `GOOGLE_WORKSPACE_CLI_SANITIZE_MODE`     | `warn` (default) or `block`  |

## Environment Variables

所有变量均为可选。复制粘贴模板请参阅 [`.env.example`](.env.example)。

| Variable | Description |
|---|---|
| `GOOGLE_WORKSPACE_CLI_TOKEN` | Pre-obtained OAuth2 access token (highest priority) |
| `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE` | Path to OAuth credentials JSON (user or service account) |
| `GOOGLE_WORKSPACE_CLI_CLIENT_ID` | OAuth client ID (alternative to `client_secret.json`) |
| `GOOGLE_WORKSPACE_CLI_CLIENT_SECRET` | OAuth client secret (paired with `CLIENT_ID`) |
| `GOOGLE_WORKSPACE_CLI_CONFIG_DIR` | Override config directory (default: `~/.config/gws`) |
| `GOOGLE_WORKSPACE_CLI_SANITIZE_TEMPLATE` | Default Model Armor template |
| `GOOGLE_WORKSPACE_CLI_SANITIZE_MODE` | `warn` (default) or `block` |
| `GOOGLE_WORKSPACE_CLI_LOG` | Log level for stderr (e.g., `gws=debug`). Off by default. |
| `GOOGLE_WORKSPACE_CLI_LOG_FILE` | Directory for JSON log files with daily rotation. Off by default. |
| `GOOGLE_WORKSPACE_PROJECT_ID` | GCP project ID override for quota/billing and fallback for helper commands |

环境变量也可设置在 `.env` 文件中（通过 [dotenvy](https://crates.io/crates/dotenvy) 加载）。

## Exit Codes

`gws` 使用结构化的退出码，使脚本无需解析错误输出即可根据失败类型进行分支处理。

| Code | Meaning | Example cause |
|------|---------|---------------|
| `0` | Success | Command completed normally |
| `1` | API error | Google returned a 4xx/5xx response |
| `2` | Auth error | Credentials missing, expired, or invalid |
| `3` | Validation error | Bad arguments, unknown service, invalid flag |
| `4` | Discovery error | Could not fetch the API schema document |
| `5` | Internal error | Unexpected failure |

```bash
gws drive files list --params '{"fileId": "bad"}'
echo $?   # 1 — API error

gws unknown-service files list
echo $?   # 3 — validation error (unknown service)
```

## Architecture

`gws` 采用**两阶段解析**策略：

1. Read `argv[1]` to identify the service (e.g. `drive`)
2. Fetch the service's Discovery Document (cached 24 h)
3. Build a `clap::Command` tree from the document's resources and methods
4. Re-parse the remaining arguments
5. Authenticate, build the HTTP request, execute

所有输出（成功结果、错误信息、下载元数据）均为结构化 JSON。

## Troubleshooting

### "Access blocked" or 403 during login

Your OAuth app is in **testing mode** and your account is not listed as a test user.

**Fix:** Open the [OAuth consent screen](https://console.cloud.google.com/apis/credentials/consent) in your GCP project → **Test users** → **Add users** → enter your Google account email. Then retry `gws auth login`.

### "Google hasn't verified this app"

Expected when your app is in testing mode. Click **Advanced** → **Go to \<app name\> (unsafe)** to proceed. This is safe for personal use; verification is only required to publish the app to other users.

### Too many scopes / consent screen error

Unverified (testing mode) apps are limited to ~25 OAuth scopes. The `recommended` scope preset includes many scopes and will exceed this limit.

**Fix:** Select only the scopes you need:

```bash
gws auth login --scopes drive,gmail,calendar
```

### `gcloud` CLI not found

`gws auth setup` requires the `gcloud` CLI to automate project creation. You have three options:

1. [Install gcloud](https://cloud.google.com/sdk/docs/install) and use `gcloud` directly.
2. Re-run `gws auth setup` which wraps `gcloud` calls.
3. Skip `gcloud` entirely — set up OAuth credentials manually in the [Cloud Console](#manual-oauth-setup-google-cloud-console)

### `redirect_uri_mismatch`

The OAuth client was not created as a **Desktop app** type. In the [Credentials](https://console.cloud.google.com/apis/credentials) page, delete the existing client, create a new one with type **Desktop app**, and download the new JSON.

### API not enabled — `accessNotConfigured`

If a required Google API is not enabled for your GCP project, you will see a
403 error with reason `accessNotConfigured`:

```json
{
  "error": {
    "code": 403,
    "message": "Gmail API has not been used in project 549352339482 ...",
    "reason": "accessNotConfigured",
    "enable_url": "https://console.developers.google.com/apis/api/gmail.googleapis.com/overview?project=549352339482"
  }
}
```

`gws` also prints an actionable hint to **stderr**:

```
💡 API not enabled for your GCP project.
   Enable it at: https://console.developers.google.com/apis/api/gmail.googleapis.com/overview?project=549352339482
   After enabling, wait a few seconds and retry your command.
```

**Steps to fix:**

1. Click the `enable_url` link (or copy it from the `enable_url` JSON field).
2. In the GCP Console, click **Enable**.
3. Wait ~10 seconds, then retry your `gws` command.

> [!TIP]
> 你也可以运行 `gws auth setup`，它会引导你自动启用项目所需的所有 API。

## Development

```bash
cargo build                       # dev build
cargo clippy -- -D warnings       # lint
cargo test                        # unit tests
./scripts/coverage.sh             # HTML coverage report → target/llvm-cov/html/
```

## License

Apache-2.0

## Disclaimer

> [!CAUTION]
> 这并非 Google 官方支持的产品。