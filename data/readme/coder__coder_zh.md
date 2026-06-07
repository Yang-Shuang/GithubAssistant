<!-- markdownlint-disable MD041 -->
<div align="center">
  <a href="https://coder.com#gh-light-mode-only">
    <img src="./docs/images/logo-black.png" alt="Coder Logo Light" style="width: 128px">
  </a>
  <a href="https://coder.com#gh-dark-mode-only">
    <img src="./docs/images/logo-white.png" alt="Coder Logo Dark" style="width: 128px">
  </a>

  <h1>
  自托管云开发环境与 AI 代理
  </h1>

  <a href="https://coder.com#gh-light-mode-only">
    <img src="./docs/images/banner-black.png" alt="Coder Banner Light" style="width: 650px">
  </a>
  <a href="https://coder.com#gh-dark-mode-only">
    <img src="./docs/images/banner-white.png" alt="Coder Banner Dark" style="width: 650px">
  </a>

  <br>
  <br>

[快速开始](#quickstart) | [文档](https://coder.com/docs) | [为什么选择 Coder](https://coder.com/why) | [高级版](https://coder.com/pricing#compare-plans)

[![discord](https://img.shields.io/discord/747933592273027093?label=discord)](https://discord.gg/coder)
[![release](https://img.shields.io/github/v/release/coder/coder)](https://github.com/coder/coder/releases/latest)
[![godoc](https://pkg.go.dev/badge/github.com/coder/coder.svg)](https://pkg.go.dev/github.com/coder/coder)
[![Go Report Card](https://goreportcard.com/badge/github.com/coder/coder/v2)](https://goreportcard.com/report/github.com/coder/coder/v2)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/9511/badge)](https://www.bestpractices.dev/projects/9511)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/coder/coder/badge)](https://scorecard.dev/viewer/?uri=github.com%2Fcoder%2Fcoder)
[![license](https://img.shields.io/github/license/coder/coder)](./LICENSE)

</div>

[Coder](https://coder.com) 是一个自托管的云开发环境与 AI 编程代理平台。工作区通过 Terraform 定义，通过安全的 Wireguard® 隧道连接，并在闲置时自动关闭。Coder Agent 运行原生 AI 编程代理，其循环逻辑在自有基础设施的控制平面执行，工作区内无需存放 API 密钥。

- 使用 Terraform 定义云开发环境
  - EC2 虚拟机、Kubernetes Pod、Docker 容器等
- 自动关闭闲置资源以节省成本
- 秒级完成开发者入职，而非数天
- 将编程任务委派给运行在自有基础设施上的 AI 代理
  - 支持接入任意模型（Anthropic、OpenAI、Google、Bedrock、自托管等）
  - 工作区内不存储大语言模型（LLM）凭据，每次操作均验证用户身份
  - 集中的模型治理、成本追踪与审计日志

<p align="center">
  <img src="./docs/images/hero-image.png" alt="Coder platform showing templates and a running workspace">
</p>

## 快速开始

体验 Coder 最便捷的方式是在本地机器上安装它，并使用 Docker 尝试配置云开发环境（支持 Linux、macOS 和 Windows）。

```shell
# First, install Coder
curl -L https://coder.com/install.sh | sh

# Start the Coder server (caches data in ~/.cache/coder)
coder server

# Navigate to http://localhost:3000 to create your initial user,
# create a Docker template and provision a workspace
```

## 安装

在 Linux 和 macOS 上安装 Coder 最简单的方法是使用[安装脚本](https://github.com/coder/coder/blob/main/install.sh)。对于 Windows，请使用 GitHub Releases 中最新的 `..._installer.exe` 文件。

```shell
curl -L https://coder.com/install.sh | sh
```

你可以使用 `--dry-run` 参数运行安装脚本，以查看将要执行的命令而不实际执行它们。运行安装脚本时加上 `--help` 可查看更多可用参数。

> 请参阅[安装指南](https://coder.com/docs/install)了解其他安装方法。

安装完成后，你可以通过一条命令启动生产环境部署：

```shell
# Automatically sets up an external access URL on *.try.coder.app
coder server

# Requires a PostgreSQL instance (version 13 or higher) and external access URL
coder server --postgres-url <url> --access-url <url>
```

使用 `coder --help` 可获取参数和环境变量列表。完整的教程请参阅[安装指南](https://coder.com/docs/install)。

## 文档中心

浏览[文档中心](https://coder.com/docs)，或访问以下特定章节：

- [**工作区（Workspaces）**](https://coder.com/docs/workspaces)：包含软件开发所需的 IDE、依赖项和配置信息的工作空间
- [**模板（Templates）**](https://coder.com/docs/templates)：使用 Terraform 编写，描述工作区的底层基础设施
- [**Coder Agent**](https://coder.com/docs/ai-coder/agents)：将编程任务委派给运行在自有基础设施上的 AI 代理
- [**管理指南（Administration）**](https://coder.com/docs/admin)：了解如何运维 Coder
- [**高级版（Premium）**](https://coder.com/pricing#compare-plans)：了解专为大型团队设计的付费功能
- [**集成开发环境（IDEs）**](https://coder.com/docs/ides)：将现有编辑器连接到工作区

## 支持

如果你有任何问题、遇到 Bug 或有功能建议，欢迎随时[提交 Issue](https://github.com/coder/coder/issues/new)。

[加入我们的 Discord](https://discord.gg/coder)，参与新功能反馈并与使用 Coder 的社区成员交流！

## 集成工具

我们正在持续开发新的集成。如需添加，请提交 Issue 进行请求。欢迎在官方或社区仓库中贡献代码。

### 官方集成

- [**Coder Registry**](https://registry.coder.com)：适用于常见开发环境的模板、模块和集成工具
- [**VS Code Extension**](https://marketplace.visualstudio.com/items?itemName=coder.coder-remote)：一键在 VS Code 中打开任意 Coder 工作区
- [**JetBrains Toolbox Plugin**](https://plugins.jetbrains.com/plugin/26968-coder)：一键从 JetBrains Toolbox 打开任意 Coder 工作区
- [**JetBrains Gateway Plugin**](https://plugins.jetbrains.com/plugin/19620-coder)：一键在 JetBrains Gateway 中打开任意 Coder 工作区
- [**Dev Containers**](https://github.com/coder/envbuilder)：使用 `devcontainer.json` 基于 Docker、Kubernetes 和 OpenShift 构建开发环境
- [**Kubernetes Log Stream**](https://github.com/coder/coder-logstream-kube)：将 Kubernetes Pod 事件实时推送到 Coder 启动日志中
- [**Self-Hosted VS Code Extension Marketplace**](https://github.com/coder/code-marketplace)：一个适用于受限或物理隔离网络的私有扩展市场，可与 [code-server](https://github.com/coder/code-server) 集成。
- [**GitHub Actions**](https://github.com/marketplace/actions/setup-coder)：在 GitHub 工作流中一键配置 Coder CLI 的操作

### 社区贡献

- [**Community Templates**](https://registry.coder.com/templates)：由社区贡献的、托管于 Coder Registry 的工作区模板
- [**Community Modules**](https://registry.coder.com/modules)：用于扩展 Coder 模板的社区贡献模块
- [**Provision Coder with Terraform**](https://github.com/ElliotG/coder-oss-tf)：通过 Terraform 在 Google GKE、Azure AKS、AWS EKS、DigitalOcean DOKS、IBMCloud K8s、OVHCloud K8s 和 Scaleway K8s Kapsule 上部署 Coder
- [**Coder Template GitHub Action**](https://github.com/marketplace/actions/update-coder-template)：用于更新 Coder 模板的 GitHub Action
- [**Discord**](https://discord.gg/coder)：与社区交流并提供新功能反馈

## 贡献代码

我们欢迎所有新贡献者加入。如果你是初次接触 Coder 代码库，请查看[贡献指南](https://coder.com/docs/CONTRIBUTING)开始你的贡献之旅。

## 招聘

如果你有兴趣加入我们的团队，请访问[招聘页面](https://jobs.ashbyhq.com/coder?utm_source=github&utm_medium=readme&utm_campaign=unknown)提交申请。