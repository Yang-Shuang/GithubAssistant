<p align="center">
<a href="https://www.infracost.io"><img src=".github/assets/logo.svg" alt="Infracost" width="300" /></a>
</p>

<p align="center"><b>面向工程师、AI 编程代理和 CI/CD 的云成本智能分析工具。</b></p>

<p align="center">Infracost 为 Terraform、Terragrunt、CloudFormation 和 AWS CDK 提供云成本估算与 FinOps（财务与运营）最佳实践——<b>在更改部署之前</b>即可查看。你可以在终端、编辑器、AI 编程代理或拉取请求中直接查看成本。</p>

<p align="center">
<a href="https://www.infracost.io/docs/"><img alt="Docs" src="https://img.shields.io/badge/docs-get%20started-brightgreen"/></a>
<img alt="Docker pulls" src="https://img.shields.io/docker/pulls/infracost/infracost?style=plastic"/>
<a href="https://www.infracost.io/community-chat"><img alt="Community Slack channel" src="https://img.shields.io/badge/chat-slack-%234a154b"/></a>
<a href="https://twitter.com/intent/tweet?text=Get%20cost%20estimates%20for%20Terraform%20in%20pull%20requests!&url=https://www.infracost.io&hashtags=cloud,cost,terraform"><img alt="tweet" src="https://img.shields.io/twitter/url/http/shields.io.svg?style=social"/></a>
</p>

## Infracost 开发者工具箱

Infracost 随处可用，完美契合工程师编写基础设施代码的工作流——无论是终端、编辑器、AI 编程代理还是 CI/CD 流水线。所有入口均共享同一引擎、相同的价格数据与 FinOps 策略，因此你只需配置一次，即可在所有地方生效。

### 快速开始

**1. 安装 CLI**

macOS (Homebrew):

```sh
brew install infracost
```

Linux:

```sh
curl -fsSL https://raw.githubusercontent.com/infracost/cli/master/scripts/install.sh | sh
```

Windows (Chocolatey):

```sh
choco install infracost
```

或直接前往 [GitHub Releases](https://github.com/infracost/cli/releases/latest) 下载最新版本。

**2. 运行初始化配置**

```sh
infracost setup
```

交互式引导将指导你完成身份验证、连接编辑器、配置 AI 代理技能以及接入 CI/CD。这是让 Infracost 工具箱所有模块为你团队工作的最快方式。

选择你的团队需要的入口点：

### Infracost CLI

[**`infracost/cli`**](https://github.com/infracost/cli) 是核心组件。将其指向一个 Terraform、Terragrunt、CloudFormation 或 AWS CDK 项目，即可获取详细的成本拆解与 FinOps 建议。交互式引导配置可一次性为你设置好编辑器、AI 代理和 CI/CD 集成。

请按照 [**快速入门指南**](https://www.infracost.io/docs/#quick-start) 完成安装与身份验证，然后：

```sh
infracost scan
```

<img src=".github/assets/infracost-scan.gif" alt="Infracost scan in action" width="600" />

若要深入了解某次扫描结果——例如完整的资源级拆解、成本驱动因素及策略详情——请使用 `infracost inspect` 命令。

<img src=".github/assets/infracost-inspect.gif" alt="Infracost inspect in action" width="600" />

### AI 编程代理集成

[**`infracost/agent-skills`**](https://github.com/infracost/agent-skills) 将 Infracost 接入 Claude Code、Cursor 及其他 AI 编程代理，使它们在生成基础设施代码时能够推理云成本与你的 FinOps 策略。目前已提供三项技能：

- **`iac-generation`** — 确保生成的 IaC 符合你的标签、区域和预算策略
- **`scan`** — 分析现有项目中的成本与策略违规情况
- **`price-lookup`** — 回答“`us-east-1` 区域的 `m7i.xlarge` 实例多少钱？”等问题，无需编写任何代码即可查询

<img src=".github/assets/infracost-ai-agent.gif" alt="Infracost running inside an AI coding agent" width="600" />

### IDE 扩展插件

在编辑 `.tf`、`.hcl`、CloudFormation 和 AWS CDK 文件时，即可查看成本视图、行内提示、悬停详情与 FinOps 诊断信息。

| 编辑器 | 仓库地址 |
| ------ | -------- |
| VS Code, Cursor, Windsurf | [`infracost/vscode-infracost`](https://github.com/infracost/vscode-infracost) |
| JetBrains (IntelliJ, GoLand, PyCharm, WebStorm, Rider…) | [`infracost/jetbrains-infracost`](https://github.com/infracost/jetbrains-infracost) |
| Neovim | [`infracost/infracost.nvim`](https://github.com/infracost/infracost.nvim) |
| Zed | [`infracost/zed-infracost`](https://github.com/infracost/zed-infracost) |

所有扩展均由 [**Infracost 语言服务器（Language Server）**](https://github.com/infracost/lsp) 驱动——这是一个标准的 LSP 服务，因此任何支持 LSP 的编辑器均可与 Infracost 集成。

<img src=".github/assets/infracost-ide.png" alt="Infracost in VS Code showing inline FinOps issues, cost details, and a resource panel" width="900" />

### CI/CD 集成

作为现有工作流的一部分，将成本差异对比与策略检查结果直接发布到拉取请求中。请通过 [CI/CD 集成指南](https://www.infracost.io/docs/integrations/cicd/) 进行配置。

<img src=".github/assets/github_actions_screenshot.png" alt="Infracost cost diff comment on a pull request" width="700" />

## Infracost Cloud

[**Infracost Cloud**](https://www.infracost.io/docs/infracost_cloud/get_started/) 是整合所有功能的 SaaS 仪表盘。团队负责人、经理与 FinOps 从业者可一次性定义 [标签策略](https://www.infracost.io/docs/infracost_cloud/tagging_policies/) 和 [安全护栏（Guardrails）](https://www.infracost.io/docs/infracost_cloud/guardrails/)，并在 CLI、编辑器扩展、代理技能及 CI/CD 中统一强制执行——同时提供跨项目及每个 PR 的支出变动全景视图。

<img src=".github/assets/infracost_cloud_dashboard_chart.png" alt="Infracost Cloud dashboard" width="600" />

## 支持的云服务商与资源类型

Infracost 支持 [AWS](https://www.infracost.io/docs/supported_resources/aws)、[Azure](https://www.infracost.io/docs/supported_resources/azure) 和 [Google Cloud](https://www.infracost.io/docs/supported_resources/google) 下的 **1,100** 多种资源，并可估算 [按量计费类资源](https://www.infracost.io/docs/usage_based_resources)（如 S3 和 Lambda）。

## 关于本仓库

本仓库是 Infracost 项目的入口，也是跟踪项目动态的最佳位置——**请 Star 和 Watch 以获取整个生态系统的版本更新通知**。

作为 **Infracost 2.0** 发布的一部分，代码库已重构为上述链接的独立仓库；部分模块可能会随时间逐步合并回此处。除非特定仓库有独立的 Issue 跟踪器，否则整个项目的讨论与问题反馈仍保留在此处。

## 社区支持

加入我们的 [社区 Slack 频道](https://www.infracost.io/community-chat)，深入了解成本估算与 Infracost，并与其他用户和贡献者建立联系。

如果遇到任何问题或有反馈意见，请在 [GitHub Discussions](https://github.com/infracost/infracost/discussions) 中开启讨论。

感谢所有贡献者——欢迎提交 Bug 报告、代码、反馈与创意。

<a href="https://github.com/infracost/infracost/graphs/contributors">
<img src="https://contrib.rocks/image?repo=infracost/infracost" />
</a>

## 许可证

[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)