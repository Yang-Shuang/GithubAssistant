# Gemini CLI

[![Gemini CLI CI](https://github.com/google-gemini/gemini-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/google-gemini/gemini-cli/actions/workflows/ci.yml)
[![Gemini CLI E2E (Chained)](https://github.com/google-gemini/gemini-cli/actions/workflows/chained_e2e.yml/badge.svg)](https://github.com/google-gemini/gemini-cli/actions/workflows/chained_e2e.yml)
[![Version](https://img.shields.io/npm/v/@google/gemini-cli)](https://www.npmjs.com/package/@google/gemini-cli)
[![License](https://img.shields.io/github/license/google-gemini/gemini-cli)](https://github.com/google-gemini/gemini-cli/blob/main/LICENSE)
[![View Code Wiki](https://assets.codewiki.google/readme-badge/static.svg)](https://codewiki.google/github.com/google-gemini/gemini-cli?utm_source=badge&utm_medium=github&utm_campaign=github.com/google-gemini/gemini-cli)

![Gemini CLI Screenshot](/docs/assets/gemini-screenshot.png)

Gemini CLI 是一款开源 AI 智能体，将 Gemini 的强大能力直接带入你的终端。它提供轻量级的 Gemini 访问方式，让你从提示词到模型的交互路径最为直接。

在[文档](https://geminicli.com/docs/)中了解关于 Gemini CLI 的所有信息。

## 🚀 为什么选择 Gemini CLI？

- **🎯 免费套餐**：使用个人 Google 账号，每分钟 60 次请求，每天 1,000 次请求。
- **🧠 强大的 Gemini 3 模型**：访问改进的推理能力与 1M token 上下文窗口。
- **🔧 内置工具**：支持 Google Search 事实核查（Grounding）、文件操作、Shell 命令和网页抓取。
- **🔌 可扩展**：支持 MCP（Model Context Protocol，模型上下文协议），便于自定义集成。
- **💻 终端优先**：专为习惯使用命令行开发的开发者设计。
- **🛡️ 开源**：采用 Apache 2.0 许可证。

## 📦 安装

请参阅[Gemini CLI 的安装、运行与发布说明](https://www.geminicli.com/docs/get-started/installation)以获取推荐的系统规格和详细安装指南。

### 快速安装

#### 使用 npx 直接运行

```bash
# Using npx (no installation required)
npx @google/gemini-cli
```

#### 通过 npm 全局安装

```bash
npm install -g @google/gemini-cli
```

#### 通过 Homebrew 全局安装（macOS/Linux）

```bash
brew install gemini-cli
```

#### 通过 MacPorts 全局安装（macOS）

```bash
sudo port install gemini-cli
```

#### 使用 Anaconda 安装（适用于受限环境）

```bash
# Create and activate a new environment
conda create -y -n gemini_env -c conda-forge nodejs
conda activate gemini_env

# Install Gemini CLI globally via npm (inside the environment)
npm install -g @google/gemini-cli
```

## 发布渠道

有关更多详细信息，请参阅[发布说明](https://www.geminicli.com/docs/changelogs)。

### Preview（预览版）

每周二 UTC 时间 23:59 将发布新的预览版。这些版本尚未经过全面验证，可能包含回归问题或其他已知缺陷。请使用 `preview` 标签进行安装并帮助我们测试。

```bash
npm install -g @google/gemini-cli@preview
```

### Stable（稳定版）

- 每周二 UTC 时间 20:00 发布新的稳定版。这是将上周的 `preview` 版本进行全面推广，并包含所有错误修复和验证结果。请使用 `latest` 标签。

```bash
npm install -g @google/gemini-cli@latest
```

### Nightly（每日构建版）

- 每天 UTC 时间 00:00 发布新版本。这将包含主分支截至发布时的所有更改。请假设其中可能仍有待验证的问题或已知缺陷。请使用 `nightly` 标签。

```bash
npm install -g @google/gemini-cli@nightly
```

## 📋 核心功能

### 代码理解与生成

- 查询和编辑大型代码库
- 利用多模态能力，根据 PDF、图片或草图生成新应用
- 使用自然语言进行调试和问题排查

### 自动化与集成

- 自动化操作任务，如查询 Pull Request 或处理复杂的 rebase
- 使用 MCP 服务器连接新功能，包括[通过 Imagen、Veo 或 Lyria 进行媒体生成](https://github.com/GoogleCloudPlatform/vertex-ai-creative-studio/tree/main/experiments/mcp-genmedia)
- 在脚本中以非交互模式运行，实现工作流自动化

### 高级功能

- 使用内置的[Google Search](https://ai.google.dev/gemini-api/docs/grounding)为你的查询提供实时信息支持（事实核查）
- 会话断点续传功能，可保存并恢复复杂的多轮对话
- 自定义上下文文件（GEMINI.md），为你的项目定制行为逻辑

### GitHub 集成

通过[**Gemini CLI GitHub Action**](https://github.com/google-github-actions/run-gemini-cli)将 Gemini CLI 直接集成到你的 GitHub 工作流中：

- **Pull Request 审查**：提供基于上下文的反馈与建议，实现自动化代码审查
- **Issue 分类与优先级排序**：基于内容分析自动标记和优先处理 GitHub Issue
- **按需协助**：在 Issue 和 Pull Request 中提及 `@gemini-cli`，获取调试、解释或任务委派方面的帮助
- **自定义工作流**：构建自动化、定时及按需触发的定制化工作流，满足团队需求

## 🔐 认证选项

选择最适合你的认证方式：

### 选项 1：使用 Google 账号登录（通过 OAuth 协议）

**✨ 适用场景**：个人开发者以及拥有 Gemini Code Assist 许可证的用户。（详见[配额限制与服务条款](https://cloud.google.com/gemini/docs/quotas)）

**优势：**

- **免费套餐**：每分钟 60 次请求，每天 1,000 次请求
- **Gemini 3 模型**：支持 1M token 上下文窗口
- **无需管理 API Key**：直接使用 Google 账号登录即可
- **自动更新**：始终使用最新版本的模型

#### 启动 Gemini CLI，随后选择“使用 Google 账号登录”，并按提示完成浏览器认证流程

```bash
gemini
```

#### 如果你正在使用组织提供的付费 Code Assist 许可证，请记得设置 Google Cloud 项目

```bash
# Set your Google Cloud Project
export GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"
gemini
```

### 选项 2：Gemini API Key

**✨ 适用场景**：需要精确控制模型或访问付费套餐的开发者

**优势：**

- **免费套餐**：每天 1000 次请求（使用 Gemini 3，包含 flash 和 pro 混合）
- **模型选择**：可指定具体的 Gemini 模型
- **按量计费**：按需升级以获得更高的调用限额

```bash
# Get your key from https://aistudio.google.com/apikey
export GEMINI_API_KEY="YOUR_API_KEY"
gemini
```

### 选项 3：Vertex AI

**✨ 适用场景**：企业团队及生产环境负载

**优势：**

- **企业级功能**：提供高级安全与合规支持
- **可扩展性**：绑定计费账户后可获得更高的速率限制
- **无缝集成**：兼容现有 Google Cloud 基础设施

```bash
# Get your key from Google Cloud Console
export GOOGLE_API_KEY="YOUR_API_KEY"
export GOOGLE_GENAI_USE_VERTEXAI=true
gemini
```

如需使用 Google Workspace 账号或其他认证方式，请参阅[认证指南](https://www.geminicli.com/docs/get-started/authentication)。

## 🚀 快速上手

### 基本用法

#### 在当前目录启动

```bash
gemini
```

#### 包含多个目录

```bash
gemini --include-directories ../lib,../docs
```

#### 使用指定模型

```bash
gemini -m gemini-2.5-flash
```

#### 脚本非交互模式

获取纯文本响应：

```bash
gemini -p "Explain the architecture of this codebase"
```

对于更高级的脚本编写（包括如何解析 JSON 和处理错误），请使用 `--output-format json` 参数获取结构化输出：

```bash
gemini -p "Explain the architecture of this codebase" --output-format json
```

如需实时事件流（适用于监控长时间运行的任务），请使用 `--output-format stream-json` 获取以换行符分隔的 JSON 事件：

```bash
gemini -p "Run tests and deploy" --output-format stream-json
```

### 快速示例

#### 启动新项目

```bash
cd new-project/
gemini
> Write me a Discord bot that answers questions using a FAQ.md file I will provide
```

#### 分析现有代码

```bash
git clone https://github.com/google-gemini/gemini-cli
cd gemini-cli
gemini
> Give me a summary of all of the changes that went in yesterday
```

## 📚 文档中心

### 入门指南

- [**快速开始指南**](https://www.geminicli.com/docs/get-started) - 快速上手运行。
- [**认证配置**](https://www.geminicli.com/docs/get-started/authentication) - 详细的认证设置说明。
- [**配置指南**](https://www.geminicli.com/docs/reference/configuration) - 设置与自定义选项。
- [**键盘快捷键**](https://www.geminicli.com/docs/reference/keyboard-shortcuts) - 提升效率的技巧。

### 核心功能

- [**命令参考**](https://www.geminicli.com/docs/reference/commands) - 所有斜杠命令（`/help`, `/chat` 等）。
- [**自定义命令**](https://www.geminicli.com/docs/cli/custom-commands) - 创建可复用的专属命令。
- [**上下文文件（GEMINI.md）**](https://www.geminicli.com/docs/cli/gemini-md) - 为 Gemini CLI 提供持久化的上下文信息。
- [**会话断点续传**](https://www.geminicli.com/docs/cli/checkpointing) - 保存并恢复对话记录。
- [**Token 缓存**](https://www.geminicli.com/docs/cli/token-caching) - 优化 Token 使用效率。

### 工具与扩展

- [**内置工具概览**](https://www.geminicli.com/docs/reference/tools)
  - [文件系统操作](https://www.geminicli.com/docs/tools/file-system)
  - [Shell 命令](https://www.geminicli.com/docs/tools/shell)
  - [网页抓取与搜索](https://www.geminicli.com/docs/tools/web-fetch)
- [**MCP 服务器集成**](https://www.geminicli.com/docs/tools/mcp-server) - 通过自定义工具进行扩展。
- [**自定义扩展**](https://geminicli.com/docs/extensions/writing-extensions) - 开发并分享你自己的命令。

### 高级主题

- [**无头模式（脚本编写）**](https://www.geminicli.com/docs/cli/headless) - 在自动化工作流中使用 Gemini CLI。
- [**IDE 集成**](https://www.geminicli.com/docs/ide-integration) - VS Code 插件支持。
- [**沙箱与安全**](https://www.geminicli.com/docs/cli/sandbox) - 安全的执行环境。
- [**受信任文件夹**](https://www.geminicli.com/docs/cli/trusted-folders) - 按文件夹控制执行策略。
- [**企业部署指南**](https://www.geminicli.com/docs/cli/enterprise) - 在企业环境中部署与管理。
- [**遥测与监控**](https://www.geminicli.com/docs/cli/telemetry) - 使用情况跟踪。
- [**工具参考**](https://www.geminicli.com/docs/reference/tools) - 内置工具概览。
- [**本地开发**](https://www.geminicli.com/docs/local-development) - 本地开发工具链。

### 故障排除与支持

- [**故障排除指南**](https://www.geminicli.com/docs/resources/troubleshooting) - 常见问题及解决方案。
- [**常见问题解答（FAQ）**](https://www.geminicli.com/docs/resources/faq) - 高频问题汇总。
- 在 CLI 中直接使用 `/bug` 命令报告问题。

### 使用 MCP 服务器

在 `~/.gemini/settings.json` 中配置 MCP 服务器，以便通过自定义工具扩展 Gemini CLI：

```text
> @github List my open pull requests
> @slack Send a summary of today's commits to #dev channel
> @database Run a query to find inactive users
```

请参阅[MCP 服务器集成指南](https://www.geminicli.com/docs/tools/mcp-server)获取详细设置说明。

## 🤝 贡献指南

我们欢迎社区贡献！Gemini CLI 完全开源（采用 Apache 2.0 许可证），并鼓励社区：

- 报告 Bug 并提出功能建议。
- 完善文档内容。
- 提交代码改进。
- 分享你的 MCP 服务器与扩展插件。

请参阅[贡献指南](./CONTRIBUTING.md)了解开发环境配置、编码规范及 Pull Request 提交流程。

查看我们的[官方路线图](https://github.com/orgs/google-gemini/projects/11)，了解计划中的功能与优先级。

## 📖 资源链接

- **[免费课程](https://learn.deeplearning.ai/courses/gemini-cli-code-and-create-with-an-open-source-agent/information)** - 学习基础操作。
- **[官方路线图](./ROADMAP.md)** - 了解后续开发计划。
- **[更新日志](https://www.geminicli.com/docs/changelogs)** - 查看近期重要更新。
- **[NPM 包](https://www.npmjs.com/package/@google/gemini-cli)** - 软件包注册表。
- **[GitHub Issue 反馈](https://github.com/google-gemini/gemini-cli/issues)** - 报告 Bug 或请求新功能。
- **[安全公告](https://github.com/google-gemini/gemini-cli/security/advisories)** - 安全更新通知。

### 卸载指南

请参阅[卸载指南](https://www.geminicli.com/docs/resources/uninstall)获取移除说明。

## 📄 法律声明

- **许可证**：[Apache License 2.0](LICENSE)
- **服务条款**：[条款与隐私政策](https://www.geminicli.com/docs/resources/tos-privacy)
- **安全策略**：[SECURITY.md](SECURITY.md)

<p align="left">
 <a href="https://www.star-history.com/google-gemini/gemini-cli">
  <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/badge?repo=google-gemini/gemini-cli&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/badge?repo=google-gemini/gemini-cli" />
   <img alt="Star History Rank" src="https://api.star-history.com/badge?repo=google-gemini/gemini-cli" />
  </picture>
 </a>
</p>

---

<p align="center">
  Built with ❤️ by Google and the open source community
</p>