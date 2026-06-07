# Claude Code 的 Codex 插件

在 Claude Code 内部使用 Codex 进行代码审查或委派任务。

本插件面向希望在你现有工作流中轻松上手使用 Codex 的 Claude Code 用户。

<video src="./docs/plugin-demo.webm" controls muted playsinline autoplay></video>

## 主要功能

- `/codex:review`：执行标准的只读代码审查
- `/codex:adversarial-review`：执行可引导（steerable）的对抗性审查
- `/codex:rescue`、`/codex:status`、`/codex:result` 和 `/codex:cancel`：用于委派任务及管理后台作业

## 环境要求

- **ChatGPT 订阅（含免费版）或 OpenAI API Key。**
  - 使用量将计入你的 Codex 配额限制。[了解更多](https://developers.openai.com/codex/pricing)。
- **Node.js 18.18 或更高版本**

## 安装步骤

在 Claude Code 中添加市场插件：

```bash
/plugin marketplace add openai/codex-plugin-cc
```

安装插件：

```bash
/plugin install codex@openai-codex
```

重新加载插件：

```bash
/reload-plugins
```

然后运行：

```bash
/codex:setup
```

`/codex:setup` 会提示你 Codex 是否已就绪。如果未安装 Codex 且系统中有 npm，它可主动为你提供安装选项。

如果你希望手动安装 Codex，请使用：

```bash
npm install -g @openai/codex
```

如果已安装但尚未登录，请运行：

```bash
!codex login
```

安装完成后，你应该能看到以下内容：

- 下方列出的斜杠命令
- `/agents` 中的 `codex:codex-rescue` 子代理（subagent）

一个简单的初次使用示例如下：

```bash
/codex:review --background
/codex:status
/codex:result
```

## 使用方法

### `/codex:review`

对你的当前工作执行标准的 Codex 代码审查。其提供的代码审查质量与直接在 Codex 中运行 `/review` 相同。

> [!NOTE]
> 代码审查（尤其是涉及多文件变更时）可能需要一些时间。通常建议在后台运行。

当你需要以下场景时使用：

- 审查当前未提交的更改
- 将你的分支与基础分支（如 `main`）进行对比审查

使用 `--base <ref>` 进行分支审查。该命令同样支持 `--wait` 和 `--background`。它不支持引导控制，也不接受自定义焦点文本（focus text）。当你希望对特定决策或风险领域提出质疑时，请使用 [`/codex:adversarial-review`](#codexadversarial-review)。

示例：

```bash
/codex:review
/codex:review --base main
/codex:review --background
```

此命令为只读操作，不会执行任何更改。在后台运行时，你可以使用 [`/codex:status`](#codexstatus) 查看进度，或使用 [`/codex:cancel`](#codexcancel) 取消正在进行的任务。

### `/codex:adversarial-review`

运行一项**可引导的**审查，对已选定的实现方案和设计提出质疑。

可用于压力测试各项假设、权衡取舍（tradeoffs）、故障模式，以及评估是否有更安全或更简单的替代方案。

它使用与 `/codex:review` 相同的审查目标选择逻辑，包括通过 `--base <ref>` 进行分支审查。同样支持 `--wait` 和 `--background`。与 `/codex:review` 不同，它在参数后可附加额外的焦点文本（focus text）。

当你需要以下场景时使用：

- 在发布前对整体方向提出质疑的审查，而不仅仅是检查代码细节
- 专注于设计选择、权衡取舍、隐藏假设及替代方案的审查
- 针对特定风险领域（如身份验证、数据丢失、回滚机制、竞态条件或系统可靠性）进行压力测试

示例：

```bash
/codex:adversarial-review
/codex:adversarial-review --base main challenge whether this was the right caching and retry design
/codex:adversarial-review --background look for race conditions and question the chosen approach
```

此命令为只读操作，不会自动修复代码。

### `/codex:rescue`

通过 `codex:codex-rescue` 子代理将任务委派给 Codex。

当你希望 Codex 帮你完成以下操作时使用：

- 排查 Bug
- 尝试修复问题
- 继续之前的 Codex 任务
- 使用更小模型进行更快或更经济的迭代处理

> [!NOTE]
> 根据任务复杂度和所选模型，这些操作可能耗时较长。通常建议强制将任务置于后台运行或将代理移至后台。

该命令支持 `--background`、`--wait`、`--resume` 和 `--fresh`。若省略 `--resume` 和 `--fresh`，插件可主动提供继续当前仓库最新救援线程的选项。

示例：

```bash
/codex:rescue investigate why the tests started failing
/codex:rescue fix the failing test with the smallest safe patch
/codex:rescue --resume apply the top fix from the last run
/codex:rescue --model gpt-5.4-mini --effort medium investigate the flaky integration test
/codex:rescue --model spark fix the issue quickly
/codex:rescue --background investigate the regression
```

你也可以直接通过自然语言请求将任务委派给 Codex：

```text
Ask Codex to redesign the database connection to be more resilient.
```

**注意事项：**

- 若未指定 `--model` 或 `--effort`，Codex 将使用其默认配置。
- 若输入 `spark`，插件会自动将其映射为 `gpt-5.3-codex-spark`
- 后续的救援请求可继续执行当前仓库中最新的 Codex 任务

### `/codex:status`

显示当前仓库正在运行及最近的 Codex 作业。

示例：

```bash
/codex:status
/codex:status task-abc123
```

用于以下场景：

- 查看后台任务的进度
- 查看最新完成的作业
- 确认任务是否仍在运行

### `/codex:result`

显示已完成作业的最终存储输出。若可用，还会包含 Codex 会话 ID（session ID），以便你直接在 Codex 中通过 `codex resume <session-id>` 重新打开该次运行记录。

示例：

```bash
/codex:result
/codex:result task-abc123
```

### `/codex:cancel`

取消正在运行的后台 Codex 作业。

示例：

```bash
/codex:cancel
/codex:cancel task-abc123
```

### `/codex:setup`

检查 Codex 是否已安装并完成身份验证。如果未安装且系统中有 npm，它可主动为你提供安装选项。

你还可以使用 `/codex:setup` 管理可选的审查门禁（review gate）功能。

#### 启用审查门禁

```bash
/codex:setup --enable-review-gate
/codex:setup --disable-review-gate
```

启用审查门背后，插件会通过 `Stop` 钩子（hook）基于 Claude 的响应执行定向 Codex 审查。若该审查发现问题，将阻止停止操作，以便让 Claude 优先处理这些问题。

> [!WARNING]
> 审查门禁可能导致 Claude/Codex 循环运行时间过长，并可能快速消耗配额限制。仅在你计划主动监控会话时启用此功能。

## 典型工作流

### 发布前审查

```bash
/codex:review
```

### 将问题委派给 Codex

```bash
/codex:rescue investigate why the build is failing in CI
```

### 启动耗时任务

```bash
/codex:adversarial-review --background
/codex:rescue --background investigate the flaky test
```

随后通过以下方式跟进：

```bash
/codex:status
/codex:result
```

## Codex 集成说明

本插件封装了 [Codex 应用服务器](https://developers.openai.com/codex/app-server)。它使用你环境中已安装的全局 `codex` 二进制文件，并[采用相同的配置逻辑](https://developers.openai.com/codex/config-basic)。

### 常用配置

若想更改插件默认使用的推理强度（reasoning effort）或模型，可在用户级或项目级的 `config.toml` 中进行定义。例如，若要在特定项目中始终对 `gpt-5.4-mini` 使用 `high` 强度，可在启动 Claude 的目录根目录下添加 `.codex/config.toml` 文件并写入以下内容：

```toml
model = "gpt-5.4-mini"
model_reasoning_effort = "high"
```

你的配置将按以下优先级生效：

- 用户级配置在 `~/.codex/config.toml`
- 项目级覆盖配置在 `.codex/config.toml`
- 项目级覆盖配置仅在[项目受信任时](https://developers.openai.com/codex/config-advanced#project-config-files-codexconfigtoml)加载

查看 Codex 文档以获取更多[配置选项](https://developers.openai.com/codex/config-reference)。

### 将工作移交至 Codex

委派的任务以及任何[停止门禁（stop gate）](#what-does-the-review-gate-do)运行记录，均可直接在 Codex 中通过 `codex resume` 恢复。你可以传入从 `/codex:result` 或 `/codex:status` 获取的具体会话 ID（session ID），或直接从列表中选择。

这样你就可以在 Codex 中审查其工作成果，或直接继续处理该任务。

## 常见问题 (FAQ)

### 使用该插件是否需要单独的 Codex 账号？

如果该机器已登录过 Codex，则当前账号即可直接使用。本插件依赖你本地的 Codex CLI 认证状态。

如果你目前仅使用 Claude Code 且尚未接触过 Codex，则需通过 ChatGPT 账号或 API Key 登录 Codex。[Codex 已包含在你的 ChatGPT 订阅中](https://developers.openai.com/codex/pricing/)，且 [`codex login`](https://developers.openai.com/codex/cli/reference/#codex-login) 同时支持 ChatGPT 和 API Key 登录方式。运行 `/codex:setup` 检查 Codex 是否就绪，若未就绪请使用 `!codex login` 进行登录。

### 该插件是否使用独立的 Codex 运行时？

不会。本插件通过本机本地的 [Codex CLI](https://developers.openai.com/codex/cli/) 和 [Codex 应用服务器](https://developers.openai.com/codex/app-server/) 进行任务委派。

这意味着：

- 使用与你直接运行相同的 Codex 安装版本
- 复用本地认证状态
- 使用相同的仓库检出（checkout）及本机本地环境

### 它会沿用我现有的 Codex 配置吗？

会的。如果你已使用过 Codex，插件将自动读取相同的[配置](#common-configurations)。

### 我可以继续使用现有的 API Key 或 Base URL 设置吗？

可以。由于本插件调用的是你本地的 Codex CLI，因此你的现有登录方式和配置依然有效。

若需将内置的 OpenAI 提供商指向其他端点（endpoint），请在你的 [Codex 配置](https://developers.openai.com/codex/config-advanced/#config-and-state-locations) 中设置 `openai_base_url`。