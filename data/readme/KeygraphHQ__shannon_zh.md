>[!NOTE]
> **[📢 弃用路由模式 (claude-code-router)。→](https://github.com/KeygraphHQ/shannon/discussions/301)**

<div align="center">

<img src="./assets/github-banner.png" alt="Shannon — AI Pentester for Web Applications and APIs" width="100%">

# Shannon —— Keygraph 出品的 AI 渗透测试工具

<a href="https://trendshift.io/repositories/15604" target="_blank"><img src="https://trendshift.io/api/badge/repositories/15604" alt="KeygraphHQ%2Fshannon | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

Shannon 是一款自主运行的白盒 AI 渗透测试工具，专为 Web 应用和 API 设计。<br />
它能分析你的源代码、识别攻击向量，并执行真实的漏洞利用代码以在生产环境上线前验证漏洞。

---

<a href="https://discord.gg/9ZqQPuhJB7"><img src="./assets/discord.png" height="40" alt="Join Discord"></a>
<a href="https://keygraph.io/"><img src="./assets/Keygraph_Button.png" height="40" alt="Visit Keygraph.io"></a>

---
</div>

## 什么是 Shannon？

Shannon 是由 [Keygraph](https://keygraph.io) 开发的 AI 渗透测试工具。它通过结合源代码分析与实时漏洞利用，对 Web 应用及其底层 API 执行白盒安全测试。

Shannon 会分析你的 Web 应用源代码以识别潜在的攻击向量，然后使用浏览器自动化和命令行工具对正在运行的应用及 API 执行真实的漏洞利用（注入攻击、身份认证绕过、SSRF、XSS）。最终报告中仅包含具有可验证概念验证（PoC）的漏洞。

**为什么需要 Shannon？**

得益于 Claude Code 和 Cursor 等工具，你的团队可以不间断地交付代码。但你们的渗透测试呢？通常一年只做一次。这造成了*巨大*的安全缺口。在其余的 364 天里，你很可能在不知情的情况下将漏洞推向生产环境。

Shannon 通过提供按需运行的自动化渗透测试来填补这一空白，它可以针对每一次构建或发布运行。

## Shannon 实战演示

Shannon 在 OWASP Juice Shop 中识别出 20+ 个漏洞，包括身份认证绕过和数据库数据外泄。[完整报告 →](sample-reports/shannon-report-juice-shop.md)

![Demo](assets/shannon-action.gif)

## 功能特性

- **完全自主运行**：只需一条命令即可启动完整的渗透测试流程。Shannon 自动处理 MFA/TOTP 登录（包括 SSO）、浏览器导航、漏洞利用和报告生成，无需人工干预。
- **可复现的 PoC 利用代码**：最终报告仅包含已验证且可利用的发现项，并附带可直接复制粘贴的 PoC。无法实际利用的漏洞不会出现在报告中。
- **OWASP 漏洞覆盖范围**：识别并验证注入攻击、XSS、SSRF 以及身份认证/授权缺陷，更多类别正在持续开发中。
- **感知代码的动态测试**：通过分析源代码来指导攻击策略，随后通过针对运行中应用的浏览器和 CLI 实时利用来验证发现项。
- **并行处理**：漏洞分析与利用阶段在所有攻击类别上并发执行。

## 产品线

Shannon 由 [Keygraph](https://keygraph.io) 开发，提供两个版本：

| 版本 | 许可证 | 适用场景 |
|---------|---------|----------|
| **Shannon Lite** | AGPL-3.0 | 本地测试你自己的应用。 |
| **Shannon Pro** | 商业许可 | 需要单一 AppSec 平台（SAST、SCA、密钥扫描、业务逻辑测试、自主渗透测试）并支持 CI/CD 集成与自托管部署的组织。 |

> **本仓库包含的是 Shannon Lite，即核心的自主 AI 渗透测试框架。** **Shannon Pro** 是 Keygraph 的一体化 AppSec 平台，将 SAST、SCA、密钥扫描、业务逻辑安全测试和自主 AI 渗透测试整合到单一的相关工作流中。每一项发现都通过可工作的 PoC 利用代码进行验证。

> [!IMPORTANT]
> **仅限白盒模式。** Shannon Lite 专为**白盒（源代码可用）**应用安全测试设计。  
> 它需要访问你的应用程序源代码及仓库目录结构。

### Shannon Pro：架构概览

Shannon Pro 是一款一体化应用安全平台，取代了将 SAST、SCA、密钥扫描和渗透测试工具拼接在一起的需求。它以两阶段流水线运行：对代码库进行代理式静态分析，随后是自主 AI 渗透测试。两个阶段的发现项会相互交叉引用与关联，因此每项报告的漏洞都附带可工作的 PoC 利用代码及精确的源代码位置。

**第一阶段：代理式静态分析**

Shannon Pro 将代码库转换为结合 AST（抽象语法树）、控制流图和程序依赖图的 CPG（代码属性图）。随后运行五种分析能力：

- **数据流分析（SAST）**：识别源点（用户输入、API 请求）和汇点（SQL 查询、命令执行），并追踪它们之间的路径。在每个节点，LLM 会评估当前上下文中所应用的具体 sanitization 是否足以防御特定漏洞，而非依赖硬编码的安全函数白名单。
- **单点漏洞检测（SAST）**：基于 LLM 的单位置漏洞检测：弱加密、硬编码凭据、不安全配置、缺失安全头、弱随机数生成器、证书验证已禁用以及过于宽松的 CORS 策略。
- **业务逻辑安全测试（SAST）**：LLM 代理分析代码库以发现应用特定的不变量（例如“文档访问必须验证组织所有权”），生成针对性 fuzzer 来违反这些不变量，并合成完整的 PoC 利用代码。这能捕获基于模式的扫描器无法检测到的授权失败和领域特定逻辑错误。
- **结合可达性分析的 SCA**：不仅标记 CVE，还通过 CPG 追踪漏洞函数是否实际上可从应用入口点到达。不可达的漏洞会被降低优先级。
- **密钥检测**：结合正则表达式模式匹配与基于 LLM 的检测（用于动态构造的凭据、自定义格式、混淆令牌），并通过只读 API 调用对相应服务执行存活验证。

**第二阶段：自主动态渗透测试**

使用与 Shannon Lite 相同的多代理渗透测试流水线（侦察、并行漏洞分析、并行利用、报告生成），并注入静态发现项到利用队列中。静态发现项会映射到 Shannon 的五大攻击域（Injection、XSS、SSRF、Auth、Authz），利用代理会对运行中的应用尝试真实的 PoC 攻击以验证每项发现。

**静态-动态关联分析**

这是核心差异化功能。静态分析中识别的数据流漏洞（例如未过滤输入到达 SQL 查询）不会作为理论风险报告。它会被传递给相应的利用代理，由其对实时应用执行利用测试。确认可利用的漏洞会追溯回确切的源代码位置，为开发者同时提供可利用性证明和修复代码行。

**部署模式**

Shannon Pro 支持自托管 runner 模型（类似于 GitHub Actions 自托管 runner）。数据平面（处理代码访问和所有 LLM API 调用）完全在客户基础设施内运行，使用客户自己的 API 密钥。源代码永远不会离开客户的网络。Keygraph 控制平面负责作业编排、扫描调度和报告 UI，仅接收聚合后的发现项。

| 能力 | Shannon Lite | Shannon Pro (一体化 AppSec) |
| --- | --- | --- |
| **许可证** | AGPL-3.0 | 商业许可 |
| **静态分析** | 代码审查提示词 | 完整的代理式 SAST、SCA、密钥扫描、业务逻辑测试 |
| **动态测试** | 自主 AI 渗透测试 | 带静态-动态关联的自主 AI 渗透测试 |
| **分析引擎** | 代码审查提示词 | 基于 CPG 的数据流，每个节点均进行 LLM 推理 |
| **业务逻辑** | 无 | 自动化不变量发现、fuzzer 生成、利用合成 |
| **CI/CD 集成** | 手动 / CLI | 原生 CI/CD、GitHub PR 扫描 |
| **部署方式** | CLI | 托管云或自托管 runner |
| **边界分析** | 无 | 自动服务边界检测与团队路由 |

[完整技术细节 →](./SHANNON-PRO.md)

## 目录

- [什么是 Shannon？](#什么是-shannon)
- [Shannon 实战演示](#shannon-实战演示)
- [功能特性](#功能特性)
- [产品线](#产品线)
- [安装与使用说明](#安装与使用说明)
  - [前置条件](#前置条件)
  - [快速开始（推荐：npx）](#快速开始推荐-npx)
  - [克隆与构建](#克隆与构建)
  - [准备你的代码仓库](#准备你的代码仓库)
  - [常用命令](#常用命令)
  - [工作区与断点续跑](#工作区与断点续跑)
  - [凭据与配置](#凭据与配置)
  - [AWS Bedrock](#aws-bedrock)
  - [Google Vertex AI](#google-vertex-ai)
  - [自定义基础 URL](#自定义基础-url)
  - [平台特定说明](#平台特定说明)
  - [输出与结果](#输出与结果)
- [示例报告](#示例报告)
- [基准测试](#基准测试)
- [架构](#架构)
- [覆盖范围与路线图](#覆盖范围与路线图)
- [免责声明](#免责声明)
- [许可证](#许可证)
- [社区与支持](#社区与支持)
- [联系我们](#联系我们)

---

## 安装与使用说明

### 前置条件

- **Docker** - 容器运行时（[安装 Docker](https://docs.docker.com/get-docker/)）
- **Node.js 18+** - `npx` 使用所需（[安装 Node.js](https://nodejs.org/)）
- **pnpm** - 克隆与构建模式所需（[安装 pnpm](https://pnpm.io/installation)）
- **AI 提供商凭据**（任选其一）：
  - **Anthropic API key**（推荐）- 从 [Anthropic Console](https://console.anthropic.com) 获取
  - **Claude Code OAuth token**
  - **AWS Bedrock** - 通过 Amazon Bedrock 路由，需 AWS 凭据（见 [AWS Bedrock](#aws-bedrock)）
  - **Google Vertex AI** - 通过 Google Cloud Vertex AI 路由（见 [Google Vertex AI](#google-vertex-ai)）

> [!NOTE]
> Docker 仍为使用 `npx` 工作流所必需。底层机制中，CLI 会从 Docker Hub 拉取并运行预构建的 Shannon worker 镜像（约 1 GB），其中包含 Shannon 及所有依赖项。Shannon 会将目标仓库以只读方式挂载到 worker 容器内，以防止分析过程中的意外修改。通过 `npx @keygraph/shannon` 运行 Shannon 获取最新正式版，或拉取最新的 `main` 分支从源码构建。

### 快速开始（推荐：npx）

> [!WARNING]
> **请在运行 Shannon 前阅读[免责声明](#免责声明)。** Shannon **不是**被动扫描器——它会主动向目标执行漏洞利用代码。你必须获得系统所有者的**明确书面授权**。

```bash
# 1. 配置凭据（交互式向导 —— 一次性设置）
npx @keygraph/shannon setup

# 或直接导出环境变量
export ANTHROPIC_API_KEY=your-api-key

# 2. 运行渗透测试
npx @keygraph/shannon start -u https://your-app.com -r /path/to/your-repo
```

Shannon 将从 Docker Hub 拉取 worker 镜像，启动基础设施，并为扫描启动一个临时 worker 容器。

### 克隆与构建

如果你想从本地克隆运行 Shannon、修改 Shannon 本身或保持 worker 镜像在本地构建，请使用此方式。

```bash
# 1. 克隆 Shannon
git clone https://github.com/KeygraphHQ/shannon.git
cd shannon

# 2. 配置凭据（任选一种方式）

# 选项 A：创建 .env 文件
cat > .env << 'EOF'
ANTHROPIC_API_KEY=your-api-key
CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000
EOF

# 选项 B：导出环境变量
export ANTHROPIC_API_KEY="your-api-key"              # 或 CLAUDE_CODE_OAUTH_TOKEN
export CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000           # 推荐

# 3. 安装依赖并构建
pnpm install
pnpm build

# 4. 运行渗透测试
./shannon start -u https://your-app.com -r /path/to/your-repo
```

Shannon 将在本地构建 worker 镜像，启动基础设施，并为扫描启动一个临时 worker 容器。

### 准备你的代码仓库

Shannon 可以扫描你机器上的任何仓库。使用 `-r` 传递绝对或相对路径。

示例：

```bash
npx @keygraph/shannon start -u https://example.com -r /path/to/repo
```

<details>
<summary>克隆与构建命令等效项</summary>

```bash
./shannon start -u https://example.com -r ./relative/path
```

</details>

### 常用命令

#### 监控进度

```bash
npx @keygraph/shannon logs <workspace>
npx @keygraph/shannon status
```

打开 Temporal Web UI 进行详细监控：

```bash
open http://localhost:8233
```

<details>
<summary>克隆与构建命令等效项</summary>

```bash
./shannon logs <workspace>
./shannon status
```

</details>

#### 停止 Shannon

```bash
npx @keygraph/shannon stop
npx @keygraph/shannon stop --clean
npx @keygraph/shannon uninstall
```

<details>
<summary>克隆与构建命令等效项</summary>

```bash
./shannon stop
./shannon stop --clean
```

</details>

#### 使用示例

```bash
# 基础渗透测试
npx @keygraph/shannon start -u https://example.com -r /path/to/repo

# 使用配置文件
npx @keygraph/shannon start -u https://example.com -r /path/to/repo -c /path/to/my-config.yaml

# 自定义输出目录
npx @keygraph/shannon start -u https://example.com -r /path/to/repo -o ./my-reports

# 命名工作区
npx @keygraph/shannon start -u https://example.com -r /path/to/repo -w q1-audit

# 列出所有工作区
npx @keygraph/shannon workspaces
```

<details>
<summary>克隆与构建命令等效项</summary>

```bash
# 基础渗透测试
./shannon start -u https://example.com -r /path/to/repo

# 使用配置文件
./shannon start -u https://example.com -r /path/to/repo -c /path/to/my-config.yaml

# 自定义输出目录
./shannon start -u https://example.com -r /path/to/repo -o ./my-reports

# 命名工作区
./shannon start -u https://example.com -r /path/to/repo -w q1-audit

# 列出所有工作区
./shannon workspaces

# 重建 worker 镜像
./shannon build --no-cache
```

</details>

### 工作区与断点续跑

Shannon 支持**工作区（workspaces）**，允许你恢复中断或失败的运行，而无需重新执行已完成阶段的代理。

**工作原理：**

- 每次运行都会创建一个工作区（默认自动命名，例如 `example-com_shannon-1771007534808`）
- 工作区存储在 `./workspaces/`（本地模式）或 `~/.shannon/workspaces/`（npx 模式）中
- 使用 `-w <name>` 为你的运行指定自定义名称以便引用
- 要恢复任何运行，通过 `-w` 传递其工作区名称 —— Shannon 会检测哪些代理已成功完成并从断点处继续
- 每个代理的进度都通过 git commit 进行 checkpoint 记录，因此恢复的运行将从干净且已验证的状态开始

```bash
# 使用命名工作区启动
npx @keygraph/shannon start -u https://example.com -r /path/to/repo -w my-audit

# 恢复同一工作区（跳过已完成代理）
npx @keygraph/shannon start -u https://example.com -r /path/to/repo -w my-audit

# 恢复之前运行的自动命名工作区
npx @keygraph/shannon start -u https://example.com -r /path/to/repo -w example-com_shannon-1771007534808

# 列出所有工作区及其状态
npx @keygraph/shannon workspaces
```

<details>
<summary>克隆与构建命令等效项</summary>

```bash
./shannon start -u https://example.com -r /path/to/repo -w my-audit
./shannon start -u https://example.com -r /path/to/repo -w my-audit
./shannon start -u https://example.com -r /path/to/repo -w example-com_shannon-1771007534808
./shannon workspaces
```

</details>

> [!NOTE]
> 恢复时 `URL` 必须与原工作区 URL 匹配。Shannon 会拒绝不匹配的 URL，以防止跨目标污染。

### 凭据与配置

#### 凭据优先级

**本地模式**按以下顺序解析凭据：

1. **环境变量** - `export ANTHROPIC_API_KEY=...`
2. **`.env` 文件** - `./.env`

**npx 模式**使用 TOML 替代 `.env`：

1. **环境变量** - `export ANTHROPIC_API_KEY=...`
2. **`~/.shannon/config.toml`** - 由 `npx @keygraph/shannon setup` 创建

环境变量始终优先，因此你可以在不编辑文件的情况下为单次会话覆盖已保存的配置。

#### 配置（可选）

虽然你可以不使用配置文件运行，但创建它可以启用认证测试和自定义分析。通过 `-c` 传递任意配置文件路径。

##### 创建配置文件

复制并修改示例配置：

```bash
cp configs/example-config.yaml ./my-app-config.yaml
```

##### 基础配置结构

```yaml
# 描述你的目标环境（可选，最多 500 字符）
description: "基于 PostgreSQL 的 Next.js 电商应用。本地开发环境 —— .env 文件仅包含本地凭据，未部署到生产环境。"

# 限制端到端运行的漏洞类别（可选，默认：全部五种）
# vuln_classes: [injection, xss, auth, authz, ssrf]

# 跳过利用阶段（可选，默认："true"）
# exploit: "false"

# 自由格式的交战规则（可选）
# rules_of_engagement: |
#   - 禁止密码暴力破解；每个账户登录尝试限制为 5 次。
#   - 节流至每秒不超过 5 个请求/端点；遇到任何 429 响应时退避 60s。
#   - 在交付物中使用占位符如 [order_id] —— 不使用真实数据值。

authentication:
  login_type: form
  login_url: "https://your-app.com/login"
  credentials:
    username: "test@example.com"
    password: "yourpassword"
    totp_secret: "LB2E2RX7XFHSTGCK"  # MFA 可选

  login_flow:
    - "将 $username 输入到邮箱字段"
    - "将 $password 输入到密码字段"
    - "点击 'Sign In' 按钮"

  success_condition:
    type: url_contains
    value: "/dashboard"

rules:
  # 支持的类型：url_path, subdomain, domain, method, header, parameter, code_path
  avoid:
    - description: "AI 应避免测试登出功能"
      type: url_path
      value: "/logout"

    # code_path 值为仓库相对文件路径或 glob（例如 "src/auth.ts", "src/vendor/**"）。
    # - description: "范围外的第三方库"
    #   type: code_path
    #   value: "src/vendor/**"

  focus:
    - description: "AI 应重点测试 API 端点"
      type: url_path
      value: "/api"

# 报告代理在组装最终报告时应用的过滤器（可选）。
# report:
#   min_severity: low                   # 丢弃低于此严重程度的发现项 (low | medium | high | critical)
#   min_confidence: low                 # 丢弃低于此置信度的发现项 (low | medium | high)
#   guidance: |
#     丢弃关于缺失安全头和速率限制漏洞的发现项。
```

运行方式：

```bash
npx @keygraph/shannon start -u https://example.com -r /path/to/repo -c ./my-app-config.yaml
```

<details>
<summary>克隆与构建命令等效项</summary>

```bash
./shannon start -u https://example.com -r /path/to/repo -c ./my-app-config.yaml
```

</details>

#### 2FA 的 TOTP 设置

如果你的应用使用双因素身份认证，只需在配置文件中添加 TOTP secret。AI 将在测试期间自动生成所需的验证码。

#### 自适应思考（Opus 4.6/4.7）

Claude 会自行决定何时以及如何对 Opus 4.6 和 4.7 进行深度推理。只要解析出的模型属于该系列，默认启用。

- **npx 模式** — `npx @keygraph/shannon setup` 会在向导中提示你。
- **本地模式** — 在 `.env`（或作为导出的环境变量）中设置 `CLAUDE_ADAPTIVE_THINKING=false` 以禁用。

#### 订阅计划速率限制

Anthropic 订阅计划的用量重置基于**滚动 5 小时窗口**。默认的重试策略（最大退避 30 分钟）会在窗口重置前耗尽所有重试次数。在配置中添加：

```yaml
pipeline:
  retry_preset: subscription          # 将最大退避延长至 6h，100 次重试
  max_concurrent_pipelines: 2         # 同时运行 5 个流水线中的 2 个（降低突发 API 用量）
```

`max_concurrent_pipelines` 控制并发运行的漏洞流水线数量（1-5，默认：5）。较低的值可降低触发速率限制的可能性，但会增加实际耗时。

### AWS Bedrock

Shannon 也支持 [Amazon Bedrock](https://aws.amazon.com/bedrock/) 替代 Anthropic API key。

#### 快速设置

运行 `npx @keygraph/shannon setup` 并选择 **AWS Bedrock**。向导将提示你输入区域、Bearer token 和模型 ID。

或直接导出环境变量：

```bash
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_REGION=us-east-1
export AWS_BEARER_TOKEN_BEDROCK=your-bearer-token
export ANTHROPIC_SMALL_MODEL=us.anthropic.claude-haiku-4-5-20251001-v1:0
export ANTHROPIC_MEDIUM_MODEL=us.anthropic.claude-sonnet-4-6
export ANTHROPIC_LARGE_MODEL=us.anthropic.claude-opus-4-7
```

<details>
<summary>克隆与构建：改为添加到 .env</summary>

```bash
CLAUDE_CODE_USE_BEDROCK=1
AWS_REGION=us-east-1
AWS_BEARER_TOKEN_BEDROCK=your-bearer-token
ANTHROPIC_SMALL_MODEL=us.anthropic.claude-haiku-4-5-20251001-v1:0
ANTHROPIC_MEDIUM_MODEL=us.anthropic.claude-sonnet-4-6
ANTHROPIC_LARGE_MODEL=us.anthropic.claude-opus-4-7
```

</details>

Shannon 使用三个模型层级：**小型**（`claude-haiku-4-5-20251001`）用于摘要，**中型**（`claude-sonnet-4-6`）用于安全分析，**大型**（`claude-opus-4-7`）用于深度推理。将 `ANTHROPIC_SMALL_MODEL`、`ANTHROPIC_MEDIUM_MODEL` 和 `ANTHROPIC_LARGE_MODEL` 设置为你所在区域的 Bedrock 模型 ID。

### Google Vertex AI

Shannon 也支持 [Google Vertex AI](https://cloud.google.com/vertex-ai) 替代 Anthropic API key。

在 [GCP Console](https://console.cloud.google.com/iam-admin/serviceaccounts) 中创建一个具有 `roles/aiplatform.user` 角色的服务账号，然后下载 JSON 密钥文件。

#### 快速设置

运行 `npx @keygraph/shannon setup` 并选择 **Google Vertex AI**。向导将提示你输入区域、项目 ID、服务账号密钥文件路径和模型 ID。密钥文件会被安全复制到 `~/.shannon/google-sa-key.json`。

或直接导出环境变量：

```bash
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=us-east5
export ANTHROPIC_VERTEX_PROJECT_ID=your-gcp-project-id
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your-sa-key.json
export ANTHROPIC_SMALL_MODEL=claude-haiku-4-5@20251001
export ANTHROPIC_MEDIUM_MODEL=claude-sonnet-4-6
export ANTHROPIC_LARGE_MODEL=claude-opus-4-7
```

<details>
<summary>克隆与构建：改为添加到 .env</summary>

```bash
CLAUDE_CODE_USE_VERTEX=1
CLOUD_ML_REGION=us-east5
ANTHROPIC_VERTEX_PROJECT_ID=your-gcp-project-id
GOOGLE_APPLICATION_CREDENTIALS=./credentials/google-sa-key.json
ANTHROPIC_SMALL_MODEL=claude-haiku-4-5@20251001
ANTHROPIC_MEDIUM_MODEL=claude-sonnet-4-6
ANTHROPIC_LARGE_MODEL=claude-opus-4-7
```

</details>

将 `CLOUD_ML_REGION` 设置为 `global` 以使用全局端点，或指定区域如 `us-east5`。部分模型在全局端点上可能不可用 —— 请参阅 [Vertex AI Model Garden](https://console.cloud.google.com/vertex-ai/model-garden) 查看区域可用性。

### 自定义基础 URL

Shannon 支持通过 `ANTHROPIC_BASE_URL` 将 SDK 指向任意兼容 Anthropic 的端点。对于需要代理路由的用户，推荐路径是使用 LLM 代理（如 [LiteLLM](https://github.com/BerriAI/litellm)）并配置为暴露兼容 Anthropic 的端点。

> [!IMPORTANT]
> **官方仅支持 Claude 模型。** Shannon 的评估、内部测试和代理 harness 均针对 Claude 优化。较小或替代模型（包括通过代理路由的非 Claude 模型）可能无法可靠地遵循 Shannon 的指令或工具使用约束，且不受官方支持。请自行承担风险；结果可能不完整、不准确或不稳定。
>
> 之前实验性的 `claude-code-router` 集成将在即将到来的版本中移除。如果你目前依赖它，请在升级前迁移到兼容 Anthropic 的代理（如 LiteLLM）。

运行 `npx @keygraph/shannon setup` 并选择 **自定义基础 URL**。向导将提示你输入端点 URL、认证 token，并可覆盖默认模型层级。

或直接导出环境变量：

```bash
export ANTHROPIC_BASE_URL=https://your-proxy.example.com
export ANTHROPIC_AUTH_TOKEN=your-auth-token

# 可选覆盖模型层级（未设置则使用默认值）
export ANTHROPIC_SMALL_MODEL=claude-haiku-4-5-20251001
export ANTHROPIC_MEDIUM_MODEL=claude-sonnet-4-6
export ANTHROPIC_LARGE_MODEL=claude-opus-4-7
```

<details>
<summary>克隆与构建：改为添加到 .env</summary>

```bash
ANTHROPIC_BASE_URL=https://your-proxy.example.com
ANTHROPIC_AUTH_TOKEN=your-auth-token
ANTHROPIC_SMALL_MODEL=claude-haiku-4-5-20251001
ANTHROPIC_MEDIUM_MODEL=claude-sonnet-4-6
ANTHROPIC_LARGE_MODEL=claude-opus-4-7
```

</details>

### 平台特定说明

**Windows：**

Shannon on Windows 仅支持通过 **WSL2**。不支持原生 Windows（包括 Git Bash）。

**步骤 1：确保 WSL 2**

```powershell
wsl --install
wsl --set-default-version 2

# 检查已安装的发行版
wsl --list --verbose

# 如果没有发行版，请安装一个（推荐 Ubuntu 24.04）
wsl --list --online
wsl --install Ubuntu-24.04

# 如果你的发行版显示 VERSION 1，请转换为 WSL 2：
wsl --set-version <distro-name> 2
```

参考 [WSL 基本命令](https://learn.microsoft.com/en-us/windows/wsl/basic-commands)。

**步骤 2：在 Windows 上安装 Docker Desktop** 并在 *Settings > General > Use the WSL 2 based engine* 下启用 **WSL2 backend**。

**步骤 3：在 WSL 内运行 Shannon**，使用任一工作流。

**WSL 内的 npx：**

```bash
npx @keygraph/shannon setup
npx @keygraph/shannon start -u https://your-app.com -r /path/to/your-repo
```

<details>
<summary>克隆与构建命令等效项</summary>

```bash
git clone https://github.com/KeygraphHQ/shannon.git
cd shannon
cp .env.example .env  # 使用你的 API key 编辑
./shannon start -u https://your-app.com -r /path/to/your-repo
```

</details>

要访问 Temporal Web UI，请在 WSL 内运行 `ip addr` 查找 WSL IP 地址，然后在 Windows 浏览器中导航至 `http://<wsl-ip>:8233`。

Windows Defender 可能会将报告中的利用代码标记为误报；详见下方的 [杀毒软件误报](#6-windows-antivirus-false-positives)。

**Linux（原生 Docker）：**

根据你的 Docker 设置，你可能需要使用 `sudo` 运行命令。如果遇到输出文件的权限问题，请确保你的用户有权访问 Docker socket。

**macOS：**

安装 Docker Desktop 后即可开箱即用。

**测试本地应用：**

Docker 容器无法直接访问宿主机的 `localhost`。请使用 `host.docker.internal` 替代：

```bash
npx @keygraph/shannon start -u http://host.docker.internal:3000 -r /path/to/repo
```

<details>
<summary>克隆与构建命令等效项</summary>

```bash
./shannon start -u http://host.docker.internal:3000 -r /path/to/repo
```

</details>

### 输出与结果

所有结果均保存至工作区目录：`./workspaces/`（本地模式）或 `~/.shannon/workspaces/`（npx 模式）。运行完成后使用 `-o <path>` 将交付物复制到自定义输出目录。

输出结构：

```text
workspaces/{hostname}_{sessionId}/
├── session.json          # 指标与会话数据
├── workflow.log          # 人类可读的工作流日志
├── agents/               # 各代理执行日志
├── prompts/              # 用于可复现性的提示词快照
└── deliverables/
    └── comprehensive_security_assessment_report.md   # 最终综合安全报告
```

---

## 示例报告

来自行业标准的脆弱应用的渗透测试示例报告：

#### **OWASP Juice Shop** • [GitHub](https://github.com/juice-shop/juice-shop)

*由 OWASP 维护的臭名昭著的不安全 Web 应用，旨在测试工具发现现代各类漏洞的能力。*

**结果**：在单次自动化运行中识别出超过 20 个针对目标 OWASP 类别的漏洞。

** notable findings **：

- SQL 注入导致身份认证绕过与完整用户数据库外泄
- 通过注册工作流绕过实现提权至管理员
- IDOR 漏洞允许访问其他用户的数据和购物车
- SSRF 用于内部网络侦察

[查看完整报告 →](sample-reports/shannon-report-juice-shop.md)

---

#### **c{api}tal API** • [GitHub](https://github.com/Checkmarx/capital)

*Checkmarx 故意构建的脆弱 API，旨在测试工具发现 OWASP API Security Top 10 的能力。*

**结果**：识别出约 15 个严重和高危漏洞。

** notable findings **：

- 通过隐藏调试端点的黑名单绕过实现根级命令注入
- 通过遗留且未修补的 v1 API 端点实现身份认证绕过
- 通过用户资料更新函数中的 Mass Assignment 实现提权
- XSS 误报率为零（正确确认了强大的 XSS 防御）

[查看完整报告 →](sample-reports/shannon-report-capital-api.md)

---

#### **OWASP crAPI** • [GitHub](https://github.com/OWASP/crAPI)

*OWASP 现代故意脆弱 API，旨在对工具针对 OWASP API Security Top 10 的有效性进行基准测试。*

**结果**：识别出超过 15 个严重和高危漏洞。

** notable findings **：

- 通过多种 JWT 攻击（算法混淆、alg:none、弱密钥注入）实现身份认证绕过
- 通过注入完全攻破 PostgreSQL 数据库，外泄用户凭据
- SSRF 攻击将内部认证令牌转发至外部服务
- XSS 误报率为零（正确识别了强大的 XSS 防御）

[查看完整报告 →](sample-reports/shannon-report-crapi.md)

---

## 基准测试

Shannon Lite 在 XBOW 安全基准测试的无提示、源码感知变体上取得了 **96.15% (100/104 exploits)** 的成绩。

**[完整结果（含详细代理日志与每项挑战的渗透测试报告）→](https://github.com/KeygraphHQ/xbow-validation-benchmarks/blob/main/xben-benchmark-results/)**

---

## 架构

Shannon 采用多代理架构，结合白盒源代码分析与跨五个阶段的动态利用：

```
        ┌──────────────────────┐
        │   Pre-Reconnaissance │
        │   (source code scan) │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │   Reconnaissance     │
        │  (attack surface     │
        │   mapping)           │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────┴───────────┐
        │          │           │
        ▼          ▼           ▼
  ┌───────────┐ ┌───────────┐ ┌───────────┐
  │ Vuln      │ │ Vuln      │ │   ...     │
  │(Injection)│ │  (XSS)    │ │           │
  └─────┬─────┘ └─────┬─────┘ └─────┬─────┘
        │              │             │
        ▼              ▼             ▼
  ┌───────────┐ ┌───────────┐ ┌───────────┐
  │ Exploit   │ │ Exploit   │ │   ...     │
  │(Injection)│ │  (XSS)    │ │           │
  └─────┬─────┘ └─────┬─────┘ └─────┬─────┘
        │              │             │
        └──────┬───────┴─────────────┘
               │
               ▼
        ┌──────────────────────┐
        │      Reporting       │
        └──────────────────────┘
```

### 架构概览

Shannon 使用 Anthropic 的 Claude Agent SDK 作为其推理引擎，运行于多代理架构中。该系统结合白盒源代码分析与黑盒动态利用，由编排器在五个阶段进行管理。架构设计遵循“无利用即不报告”策略以最小化误报率。

每次扫描均在独立的临时 Docker 容器（`docker run --rm`）中运行，并配备单次调用的 Temporal 任务队列，支持针对不同目标仓库的并发扫描。

---

#### **阶段 1：预侦察**

执行源代码分析以识别应用框架、入口点及从代码库中发现的潜在攻击面。构建所有后续代理所依赖的基础架构情报。

#### **阶段 2：侦察**

基于预侦察发现项构建全面的攻击面映射。Shannon 通过浏览器自动化对实时应用进行探索，将代码级洞察与实际行为相关联，生成详细的入口点、API 端点和身份认证机制地图。

#### **阶段 3：漏洞分析**

为最大化效率，此阶段使用 5 个并发代理并行运行。基于侦察数据，针对每个 OWASP 类别（注入、XSS、auth、authz、SSRF）的专用代理并行搜寻潜在缺陷。对于注入和 SSRF 等漏洞，代理执行结构化的数据流分析，追踪用户输入至危险汇点。此阶段产出关键交付物：**假设的可利用路径列表**，供后续验证使用。

#### **阶段 4：利用测试**

为保持速度，继续并行工作流。此阶段完全致力于将假设转化为证据。专用利用代理接收假设的路径，并尝试使用浏览器自动化、命令行工具和自定义脚本执行真实攻击。此阶段严格执行 **“无利用即不报告”** 策略：如果无法成功利用假设来证明影响，则将其作为误报丢弃。

#### **阶段 5：报告生成**

最终阶段将所有已验证的发现项汇编为专业、可操作的报告。代理整合侦察数据与成功的利用证据，清理噪音或幻觉产物。仅包含经确认的漏洞，并附带**可复现、可直接复制粘贴的概念验证（PoC）**，交付专注于已证实风险的专业渗透测试级报告。


## 覆盖范围与路线图

有关 Shannon 安全测试覆盖范围和开发路线图的详细信息，请参阅我们的 [Coverage and Roadmap](./COVERAGE.md) 文档。

## 免责声明

### 重要使用指南与免责声明

请在使用 Shannon (Lite) 前仔细审阅以下指南。作为用户，你需对你的操作负责并承担所有责任。

#### **1. 潜在破坏性影响与环境选择**

这不是被动扫描器。利用代理的设计目标是**主动执行攻击**以确认漏洞。此过程可能对目标应用及其数据产生破坏性影响。

> [!WARNING]
> **切勿在 production（生产）环境中运行 Shannon。**
>
> - 仅适用于沙箱、staging 或本地开发环境，这些环境的完整性不受关注。
> - 潜在的破坏性影响包括但不限于：创建新用户、修改或删除数据、攻破测试账户，以及触发注入攻击的意外副作用。
> - **为获得最大安全性与隔离性，请在虚拟机（VM）内运行 Shannon。** 这可将利用产生的任何副作用（包括意外的出站流量、代理工具的文件写入或与本地服务的交互）限制在可丢弃的环境中。

#### **2. 法律与伦理使用**

Shannon 仅设计用于合法的安全审计目的。

> [!CAUTION]
> **你在运行 Shannon 前必须获得目标系统所有者的明确书面授权。**
>
> 未经授权扫描和利用你不拥有的系统是非法的，可能违反《计算机欺诈和滥用法案》（CFAA）等法律。Keygraph 不对任何滥用行为负责。

#### **3. LLM 与自动化注意事项**

- **必须人工验证**：虽然我们投入了大量工程工作来实现“利用即证明”的方法以消除误报，但底层 LLM 仍可能在最终报告中生成幻觉或支持不足的内容。**必须有人工监督**来验证所有报告发现项的合法性和严重性。
- **模型支持**：Shannon 官方仅支持 **Claude 模型**。我们的评估、内部测试和代理 harness 均针对 Claude 优化。较小或替代模型（包括通过代理路由的非 Claude 模型）可能无法可靠地遵循 Shannon 的指令或工具使用约束，且不受官方支持。
- **全面性**：Shannon Lite 的分析可能因 LLM 上下文窗口的固有限制而不完整。如需对你整个代码库进行更全面、基于图的深入分析，**Shannon Pro** 利用其高级数据流分析引擎确保更深入的覆盖范围。

#### **4. 分析范围**

- **目标漏洞**：当前版本的 Shannon Lite 专门针对以下*可利用*漏洞类别：
  - Broken Authentication & Authorization（身份认证与授权缺陷）
  - Injection（注入攻击）
  - Cross-Site Scripting (XSS)（跨站脚本）
  - Server-Side Request Forgery (SSRF)（服务端请求伪造）
- **Shannon Lite 未覆盖的内容**：此列表并非涵盖所有潜在安全风险。Shannon Lite 的“利用即证明”模型意味着它不会报告无法主动利用的问题，例如脆弱的第三方库或不安全的配置。这类深度静态分析发现项是 **Shannon Pro** 高级分析引擎的核心重点。

#### **5. 成本与性能**

- **时间**：截至当前版本，完整测试运行通常需要 **1 到 1.5 小时**。
- **成本**：使用 Anthropic 的 Claude 4.5 Sonnet 模型运行完整测试可能产生约 **$50 USD** 的费用。费用因模型定价和应用复杂度而异。

#### **6. Windows 杀毒软件误报**

Windows Defender 可能会将 `xben-benchmark-results/` 或 `deliverables/` 中的文件标记为恶意软件。这些是由报告中的利用代码引起的误报。请在 Windows Defender 中添加 Shannon 目录的排除项，或使用 Docker/WSL2。

#### **7. 安全考量**

Shannon Lite 设计用于扫描你拥有或已获得明确测试权限的代码库与应用。请勿将其指向不受信任或具有敌意的代码库。如同任何读取源代码的 AI 工具一样，Shannon Lite 易受扫描仓库中内容的提示词注入影响。


## 许可证

Shannon Lite 根据 [GNU Affero General Public License v3.0 (AGPL-3.0)](LICENSE) 发布。

Shannon 是开源软件（AGPL v3）。此许可证允许你：
- 免费用于所有内部安全测试。
- 私下修改代码供内部使用，无需分享你的更改。

AGPL 的共享要求主要适用于将 Shannon 作为公共或托管服务提供的组织（例如 SaaS 平台）。在这些特定情况下，对核心软件所做的任何修改必须开源。


## 社区与支持

### 社区资源

**1:1 Office Hours** — 每周四，两个时区
预约免费的 15 分钟会话，获取针对 bug、部署或配置问题的实操帮助。
→ US/EU：10:00 AM PT  |  Asia：2:00 PM IST
→ [预约时段](https://cal.com/george-flores-keygraph/shannon-community-office-hours)

[加入我们的 Discord](https://discord.gg/cmctpMBXwE) 提问、分享反馈并与其他 Shannon 用户交流。

**贡献代码：** 目前，我们不接受外部代码贡献（PR）。  
欢迎提交 Issue 用于 bug 报告和 feature 请求。

- **报告 Bug**：通过 [GitHub Issues](https://github.com/KeygraphHQ/shannon/issues)
- **建议功能**：在 [Discussions](https://github.com/KeygraphHQ/shannon/discussions) 中提出

### 保持联系

- **Twitter**: [@KeygraphHQ](https://twitter.com/KeygraphHQ)
- **LinkedIn**: [Keygraph](https://linkedin.com/company/keygraph)
- **Website**: [keygraph.io](https://keygraph.io)



## 联系我们

### Shannon Pro

Shannon Pro 是 Keygraph 的一体化 AppSec 平台。对于需要统一 SAST、SCA 和自主渗透测试（带静态-动态关联）、CI/CD 集成或自托管部署的组织，请参阅 [Shannon Pro 技术概览](./SHANNON-PRO.md)。

<p align="center">
  <a href="https://cal.com/team/keygraph/shannon-pro" target="_blank">
    <img src="./assets/Demo_Button.png" height="40" alt="Shannon Pro Inquiry">
  </a>
</p>

**Email**: [shannon@keygraph.io](mailto:shannon@keygraph.io)

---

<p align="center">
  <b>Built by <a href="https://keygraph.io">Keygraph</a></b>
</p>