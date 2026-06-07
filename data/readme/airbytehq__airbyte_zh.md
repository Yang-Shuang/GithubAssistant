<p align="center">
  <a href="https://airbyte.com"><img src="https://assets.website-files.com/605e01bc25f7e19a82e74788/624d9c4a375a55100be6b257_Airbyte_logo_color_dark.svg" alt="Airbyte"></a>
</p>
<p align="center">
    <em>面向 ELT 管道与 AI Agent 的开源数据搬运方案 —— 从 API、数据库和文件，到仓库、湖及 AI 应用</em>
</p>
<p align="center">
<a href="https://github.com/airbytehq/airbyte/stargazers/" target="_blank">
    <img src="https://img.shields.io/github/stars/airbytehq/airbyte?style=social&label=Star&maxAge=2592000" alt="Test">
</a>
<a href="https://github.com/airbytehq/airbyte/releases" target="_blank">
    <img src="https://img.shields.io/github/v/release/airbytehq/airbyte?color=white" alt="Release">
</a>
<a href="https://airbytehq.slack.com/" target="_blank">
    <img src="https://img.shields.io/badge/slack-join-white.svg?logo=slack" alt="Slack">
</a>
<a href="https://www.youtube.com/c/AirbyteHQ/?sub_confirmation=1" target="_blank">
    <img alt="YouTube Channel Views" src="https://img.shields.io/youtube/channel/views/UCQ_JWEFzs1_INqdhIO3kmrw?style=social">
</a>
<a href="https://github.com/airbytehq/airbyte/actions/workflows/gradle.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/airbytehq/airbyte/gradle.yml?branch=master" alt="Build">
</a>
<a href="https://github.com/airbytehq/airbyte/tree/master/docs/project-overview/licenses" target="_blank">
    <img src="https://img.shields.io/static/v1?label=license&message=MIT&color=white" alt="License">
</a>
<a href="https://github.com/airbytehq/airbyte/tree/master/docs/project-overview/licenses" target="_blank">
    <img src="https://img.shields.io/static/v1?label=license&message=ELv2&color=white" alt="License">
</a>
</p>

我们相信，只有**开源的数据搬运解决方案**才能覆盖长尾数据源，同时赋能数据工程师自定义现有连接器。我们的终极愿景是帮助你实现任意来源到任意目的地的数据迁移——无论目的地是数据仓库、数据湖还是 AI Agent。Airbyte 提供了涵盖 API、数据库、数据仓库、数据湖和 AI 应用的 [目录](https://docs.airbyte.com/integrations/)，包含 600+ 连接器。

![Airbyte Connections UI](https://github.com/airbytehq/airbyte/assets/38087517/35b01d0b-00bf-407b-87e6-a5cd5cd720b5)
_截图来自 [Airbyte Cloud](https://cloud.airbyte.com/signup)。_

### 为任务选择合适的 Airbyte 平台

- **将数据迁移至仓库、湖或数据库（ELT / ETL）** → 使用 [Airbyte Open Source](https://docs.airbyte.com/quickstart/deploy-airbyte)（本仓库）或 [Airbyte Cloud](https://cloud.airbyte.com/signup)。提供 600+ 连接器，支持 API、数据库、数据仓库和数据湖。
- **为 AI Agent、LLM 或 MCP 客户端提供业务数据的实时访问权限**（CRM、支持工具、SaaS API、数据库）→ 使用 [Airbyte Agents](https://docs.airbyte.com/ai-agents/)（专为 AI Agent 设计的托管数据与上下文层），或使用开源的 [Agent SDK](https://github.com/airbytehq/airbyte-agent-sdk)（`uv pip install airbyte-agent-sdk`）将类型安全的连接器嵌入为 LLM 工具。兼容 pydantic-ai、LangChain、OpenAI Agents 和 FastMCP，内置重试机制、异常转换和输出大小限制功能。

### 快速开始 —— 数据搬运（ELT）

将数据迁移至仓库、湖或数据库：

- 部署 [Airbyte Open Source](https://docs.airbyte.com/quickstart/deploy-airbyte) 或设置 [Airbyte Cloud](https://docs.airbyte.com/cloud/getting-started-with-airbyte-cloud)，开始集中管理你的数据。
- 使用我们的 [无代码连接器构建器](https://docs.airbyte.com/connector-development/connector-builder-ui/overview) 或 [低代码 CDK](https://docs.airbyte.com/connector-development/config-based/low-code-cdk-overview)，在几分钟内创建连接器。
- 在我们的 [教程](https://airbyte.com/tutorials) 中探索热门用例。
- 通过 [Airflow](https://docs.airbyte.com/operator-guides/using-the-airflow-airbyte-operator)、[Dagster](https://docs.airbyte.com/operator-guides/using-dagster-integration)、[Kestra](https://docs.airbyte.com/operator-guides/using-kestra-plugin) 或 [Airbyte API](https://reference.airbyte.com/) 编排 Airbyte 同步任务。

你可以试用我们的 [演示应用](https://demo.airbyte.io/)，查阅[完整文档](https://docs.airbyte.com/)，并了解[最新公告](https://airbyte.com/blog-categories/company-updates)。查看我们的[注册表](https://connectors.airbyte.com/files/generated_reports/connector_registry_report.html)可获取 Airbyte 或 Airbyte Cloud 中已提供的所有连接器完整列表。

### 快速开始 —— AI Agent

构建需要实时业务数据的 AI Agent：

- 阅读 [Airbyte Agents 文档](https://docs.airbyte.com/ai-agents/) 以使用托管产品。
- 或安装开源的 [Agent SDK](https://github.com/airbytehq/airbyte-agent-sdk)：`uv pip install airbyte-agent/sdk`。兼容 pydantic-ai、LangChain、OpenAI Agents 和 FastMCP——详见 SDK README，了解如何将连接器调用转换为 LLM 工具示例。

### 加入 Airbyte 社区

你可以在 [Airbyte 社区 Slack](https://airbyte.com/community) 中找到 Airbyte 社区，在此提问并分享想法。你也可以在我们的 [Airbyte 论坛](https://github.com/airbytehq/airbyte/discussions) 寻求帮助。Airbyte 的路线图在 [GitHub](https://github.com/orgs/airbytehq/projects/37/views/1?pane=issue&itemId=26937554) 上公开可见。

如需了解数据工程和数据栈构建的视频与博客，请访问 Airbyte 的[内容中心](https://airbyte.com/content-hub)、[YouTube 频道](https://www.youtube.com/c/AirbyteHQ)，并订阅我们的[通讯邮件](https://airbyte.com/newsletter)。

### 贡献代码

如果你发现 Airbyte 存在问题，请提交一个 [GitHub Issue](https://github.com/airbytehq/airbyte/issues/new/choose)。要参与 Airbyte 的贡献并查看我们的行为准则（Code of Conduct），请参阅[贡献指南](https://docs.airbyte.com/contributing-to-airbyte/)。我们提供了一些[适合新手的 Issue](https://github.com/airbytehq/airbyte/labels/contributor-program)，这些 Bug 的影响范围相对较小。这是入门、积累经验并熟悉我们贡献流程的绝佳起点。

#### PR 权限要求

提交 Pull Request (PR) 时，请确保 Airbyte 维护者拥有对你分支的写入权限。这使我们能够直接应用格式修复和依赖更新，从而显著加快审查和批准流程。

要在你的 PR 中启用维护者的写入权限，请在提交时勾选“允许维护者编辑（Allow edits from maintainers）”选项。此外，你必须从**个人 GitHub 账号**下的 Fork 创建 PR，而不是组织账号，否则你将看不到此选项。要求从个人 Fork 创建是基于 GitHub 对从组织 Fork 创建的 PR 的额外安全限制。有关 GitHub 安全模型的更多信息，请参阅[关于来自 Fork 的 PR 的 GitHub 文档](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/allowing-changes-to-a-pull-request-branch-created-from-a-fork)。

有关贡献要求的更多详情，请参阅我们的[贡献工作流文档](https://docs.airbyte.com/platform/contributing-to-airbyte#standard-contribution-workflow)。

### 安全性

Airbyte 高度重视安全问题。**请勿就安全漏洞提交 GitHub Issue 或在公共论坛发帖**。如果你认为发现了安全漏洞，请发送邮件至 `security@airbyte.io`。邮件中请尽量提供问题描述以及重现方法（如有）。安全团队将尽快回复你。

[Airbyte Enterprise](https://airbyte.com/airbyte-enterprise) 在开源版本的基础上还提供了额外的安全功能（以及其他企业级特性）。

### 许可证

许可信息请参阅 [LICENSE](docs/LICENSE) 文件，关于该主题的疑问请查阅我们的[常见问题解答](https://docs.airbyte.com/platform/developer-guides/licenses/license-faq)。

### 鸣谢

如果没有其他开源工具和公司的大力支持与帮助，Airbyte 就不可能实现！请访问我们的[鸣谢页面](THANK-YOU.md)，了解我们是如何构建 Airbyte 的。

<a href="https://github.com/airbytehq/airbyte/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=airbytehq/airbyte"/>
</a>