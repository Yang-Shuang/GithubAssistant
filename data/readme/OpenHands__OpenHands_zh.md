<a name="readme-top"></a>

<div align="center">
  <img src="https://raw.githubusercontent.com/OpenHands/docs/main/openhands/static/img/logo.png" alt="Logo" width="200">
  <h1 align="center" style="border-bottom: none">OpenHands：AI 驱动的开发</h1>
</div>


<div align="center">
  <a href="https://github.com/OpenHands/OpenHands/blob/main/LICENSE"><img src="https://img.shields.io/badge/LICENSE-MIT-20B2AA?style=for-the-badge" alt="MIT License"></a>
  <a href="https://docs.google.com/spreadsheets/d/1wOUdFCMyY6Nt0AIqF705KN4JKOWgeI4wUGUP60krXXs/edit?gid=811504672#gid=811504672"><img src="https://img.shields.io/badge/SWEBench-77.6-00cc00?logoColor=FFE165&style=for-the-badge" alt="Benchmark Score"></a>
  <br/>
  <a href="https://docs.openhands.dev/sdk"><img src="https://img.shields.io/badge/Documentation-000?logo=googledocs&logoColor=FFE165&style=for-the-badge" alt="Check out the documentation"></a>
  <a href="https://arxiv.org/abs/2511.03690"><img src="https://img.shields.io/badge/Paper-000?logoColor=FFE165&logo=arxiv&style=for-the-badge" alt="Tech Report"></a>


  <!-- Keep these links. Translations will automatically update with the README. -->
  <a href="https://www.readme-i18n.com/OpenHands/OpenHands?lang=de">Deutsch</a> |
  <a href="https://www.readme-i18n.com/OpenHands/OpenHands?lang=es">Español</a> |
  <a href="https://www.readme-i18n.com/OpenHands/OpenHands?lang=fr">français</a> |
  <a href="https://www.readme-i18n.com/OpenHands/OpenHands?lang=ja">日本語</a> |
  <a href="https://www.readme-i18n.com/OpenHands/OpenHands?lang=ko">한국어</a> |
  <a href="https://www.readme-i18n.com/OpenHands/OpenHands?lang=pt">Português</a> |
  <a href="https://www.readme-i18n.com/OpenHands/OpenHands?lang=ru">Русский</a> |
  <a href="https://www.readme-i18n.com/OpenHands/OpenHands?lang=zh">中文</a>
</div>

<hr>

🙌 欢迎来到 OpenHands，这是一个专注于 AI 驱动开发的[社区](COMMUNITY.md)。我们非常欢迎你[加入我们的 Slack 频道](https://dub.sh/openhands)。

你可以通过以下几种方式使用 OpenHands：

### OpenHands Software Agent SDK
该 SDK 是一个可组合的 Python 库，包含了我们所有的智能体技术。它是驱动上述所有功能的核心引擎。

你可以在代码中定义智能体，然后在本地运行，或将其扩展至云端数以千计的智能体实例。

[查看文档](https://docs.openhands.dev/sdk) 或 [浏览源码](https://github.com/OpenHands/software-agent-sdk/)

### OpenHands CLI
CLI 是使用 OpenHands 最简单的方式。如果你曾使用过 Claude Code 或 Codex，你会对这种体验感到熟悉。你可以使用 Claude、GPT 或其他任何大语言模型（LLM）来驱动它。

[查看文档](https://docs.openhands.dev/openhands/usage/run-openhands/cli-mode) 或 [浏览源码](https://github.com/OpenHands/OpenHands-CLI)

### OpenHands Local GUI
使用本地图形界面在笔记本电脑上运行智能体。它内置了 REST API 和一个单页 React 应用。如果你曾使用过 Devin 或 Jules，你会对这种体验感到熟悉。

[查看文档](https://docs.openhands.dev/openhands/usage/run-openhands/local-setup) 或在此仓库中浏览源码。

### OpenHands Cloud
这是运行在托管基础设施上的 OpenHands 图形界面部署版本。

你可以通过[使用 GitHub 或 GitLab 账号登录](https://app.all-hands.dev)免费试用基于 Minimax 模型的版本。

OpenHands Cloud 包含以下源码可用（source-available）的功能与集成：
- 支持 Slack、Jira 和 Linear 集成
- 多用户支持
- 基于角色的访问控制（RBAC）及权限管理
- 协作功能（例如对话共享）

### OpenHands Enterprise
大型企业可通过 Kubernetes 在我们的协助下，在自有 VPC 中自行托管部署 OpenHands Cloud。OpenHands Enterprise 同样支持与上述的 CLI 和 SDK 配合使用。

OpenHands Enterprise 采用源码可用模式——你可以在本仓库的 `enterprise/` 目录中查看完整源代码，但若需运行超过一个月，则必须购买许可证。

企业级合同还提供延长技术支持及研发团队访问权限。

了解更多请访问 [openhands.dev/enterprise](https://openhands.dev/enterprise)

### Everything Else

欢迎查看我们的 [产品路线图](https://github.com/orgs/openhands/projects/1)，如果你有任何期待的功能，也随时可以[提交 Issue](https://github.com/OpenHands/OpenHands/issues)！

你可能也会对我们的 [评估基础设施](https://github.com/OpenHands/benchmarks)、[Chrome 浏览器扩展](https://github.com/OpenHands/openhands-chrome-extension/)或[心智理论（Theory of Mind）模块](https://github.com/OpenHands/ToM-SWE)感兴趣。

除本仓库的 `enterprise/` 目录外（详见 [企业许可证](enterprise/LICENSE)），我们的所有项目均遵循 MIT 开源协议。核心 `openhands` 和 `agent-server` Docker 镜像也完全采用 MIT 许可。

如果你需要任何帮助，或只是想聊聊天，[欢迎来我们的 Slack 频道](https://dub.sh/openhands)找我们。

<hr>

### Thank You to Our Contributors

<div align="center">

[![OpenHands Contributors](https://assets.openhands.dev/readme/openhands-openhands-contributors.svg)](https://github.com/OpenHands/OpenHands/graphs/contributors)

</div>

<hr>

### Trusted by Engineers at

<div align="center">
  <br/><br/>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://assets.openhands.dev/logos/external/white/tiktok.svg">
    <img src="https://assets.openhands.dev/logos/external/black/tiktok.svg" alt="TikTok" height="17" hspace="5">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://assets.openhands.dev/logos/external/white/vmware.svg">
    <img src="https://assets.openhands.dev/logos/external/black/vmware.svg" alt="VMware" height="17" hspace="5">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://assets.openhands.dev/logos/external/white/roche.svg">
    <img src="https://assets.openhands.dev/logos/external/black/roche.svg" alt="Roche" height="17" hspace="5">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://assets.openhands.dev/logos/external/white/amazon.svg">
    <img src="https://assets.openhands.dev/logos/external/black/amazon.svg" alt="Amazon" height="17" hspace="5">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://assets.openhands.dev/logos/external/white/c3-ai.svg">
    <img src="https://assets.openhands.dev/logos/external/black/c3-ai.svg" alt="C3 AI" height="17" hspace="5">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://assets.openhands.dev/logos/external/white/netflix.svg">
    <img src="https://assets.openhands.dev/logos/external/black/netflix.svg" alt="Netflix" height="17" hspace="5">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://assets.openhands.dev/logos/external/white/mastercard.svg">
    <img src="https://assets.openhands.dev/logos/external/black/mastercard.svg" alt="Mastercard" height="17" hspace="5">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://assets.openhands.dev/logos/external/white/red-hat.svg">
    <img src="https://assets.openhands.dev/logos/external/black/red-hat.svg" alt="Red Hat" height="17" hspace="5">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://assets.openhands.dev/logos/external/white/mongodb.svg">
    <img src="https://assets.openhands.dev/logos/external/black/mongodb.svg" alt="MongoDB" height="17" hspace="5">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://assets.openhands.dev/logos/external/white/apple.svg">
    <img src="https://assets.openhands.dev/logos/external/black/apple.svg" alt="Apple" height="17" hspace="5">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://assets.openhands.dev/logos/external/white/nvidia.svg">
    <img src="https://assets.openhands.dev/logos/external/black/nvidia.svg" alt="NVIDIA" height="17" hspace="5">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://assets.openhands.dev/logos/external/white/google.svg">
    <img src="https://assets.openhands.dev/logos/external/black/google.svg" alt="Google" height="17" hspace="5">
  </picture>
</div>

</div>