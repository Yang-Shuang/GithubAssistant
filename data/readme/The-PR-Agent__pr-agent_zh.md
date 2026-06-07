<br />

<div align="center">


<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://codium.ai/images/pr_agent/logo-dark.png" width="330">
  <source media="(prefers-color-scheme: light)" srcset="https://codium.ai/images/pr_agent/logo-light.png" width="330">
  <img src="https://codium.ai/images/pr_agent/logo-light.png" alt="logo" width="330">

</picture>
<br>
The Original Open-Source PR Reviewer
<br><br>
<a href="https://github.com/the-pr-agent/pr-agent/commits/main">
<img alt="GitHub" src="https://img.shields.io/github/last-commit/the-pr-agent/pr-agent/main?style=for-the-badge" height="20">
</a>
</div>

---

本仓库包含开源 PR Agent 项目。它并非 Qodo 的免费套餐版。

在我们的网站上试用免费版本。

👉[立即开始](https://www.qodo.ai/get-started/)

PR-Agent 是一款开源、由 AI 驱动的代码审查工具，也是 Qodo 旗下由社区维护的遗留项目。它与 Qodo 的主要 AI 代码审查产品不同，后者提供更丰富、上下文感知的体验。Qodo 现在提供与 GitHub、GitLab、Bitbucket 和 Azure DevOps 无缝集成的免费套餐版，用于高质量自动化审查。


## PR-Agent 重大更新

PR-Agent 有了新家！

经过多年与社区共同打磨这款工具，Qodo 已将 PR-Agent 捐赠给开源社区——我们对接下来的发展充满期待。

该项目现已迁至 GitHub 上的 `PR-Agent` 组织名下，完全由社区所有并维护，欢迎贡献代码及新增维护者。

其他变更包括： 
- 文档已迁移至 www.pr-agent.ai
- Qodo Merge（Qodo 1.0）作为 PR-Agent 的企业版托管服务，现已重新品牌化并演进为 Qodo（Qodo 2.0），一个完整的 AI 代码审查平台。


## 目录

- [快速开始](#快速开始)
- [为什么选择 PR-Agent？](#为什么选择-pr-agent)
- [功能特性](#功能特性)
- [效果演示](#效果演示)
- [工作原理](#工作原理)
- [数据隐私](#数据隐私)
- [贡献指南](#贡献指南)

## 快速开始

> [!NOTE]
> **Docker Hub 命名空间迁移。** 版本 `0.34.2` 及之后的镜像已发布至 [`pragent/pr-agent`](https://hub.docker.com/r/pragent/pr-agent)。旧版发行版（最高至 `v0.31`）仍保留在旧的 [`codiumai/pr-agent`](https://hub.docker.com/r/codiumai/pr-agent) 命名空间下作为归档镜像——该处不再推送新镜像。升级至 `0.34.2+` 时，请更新任何硬编码的 `image:` / `docker pull` / `uses: docker://` 引用。

### 🚀 PR-Agent 快速上手

#### 1. GitHub Action（推荐）
通过简单的工作流文件为你的仓库添加自动化 PR 审查：
```yaml
# .github/workflows/pr-agent.yml
name: PR Agent
on:
  pull_request:
    types: [opened, synchronize]
jobs:
  pr_agent_job:
    runs-on: ubuntu-latest
    steps:
    - name: PR Agent action step
      uses: the-pr-agent/pr-agent@main
      env:
        OPENAI_KEY: ${{ secrets.OPENAI_KEY }}
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```
[完整 GitHub Action 配置指南](https://docs.pr-agent.ai/installation/github/#run-as-a-github-action)

#### 2. CLI 使用（本地开发）
在本地仓库运行 PR-Agent：
```bash
pip install pr-agent
export OPENAI_KEY=your_key_here
pr-agent --pr_url https://github.com/owner/repo/pull/123 review
```
[完整 CLI 配置指南](https://docs.pr-agent.ai/usage-guide/automations_and_usage/#local-repo-cli)

#### 3. 其他平台
- [GitLab webhook 配置](https://docs.pr-agent.ai/installation/gitlab/)
- [BitBucket 应用安装](https://docs.pr-agent.ai/installation/bitbucket/)
- [Azure DevOps 配置](https://docs.pr-agent.ai/installation/azure/)

[//]: # (## News and Updates)

[//]: # ()
[//]: # (## Aug 8, 2025)

[//]: # ()
[//]: # ()
[//]: # ()
[//]: # (## Jul 1, 2025)

[//]: # (You can now receive automatic feedback from Qodo Merge in your local IDE after each commit. Read more about it [here]&#40;https://github.com/qodo-ai/agents/tree/main/agents/qodo-merge-post-commit&#41;.)

[//]: # ()
[//]: # ()
[//]: # (## Jun 21, 2025)

[//]: # ()
[//]: # (v0.30 was [released]&#40;https://github.com/the-pr-agent/pr-agent/releases&#41;)

[//]: # ()
[//]: # ()
[//]: # (## Apr 30, 2025)

[//]: # ()
[//]: # (A new feature is now available in the `/improve` tool for Qodo Merge 💎 - Chat on code suggestions.)

[//]: # ()
[//]: # (<img width="512" alt="image" src="https://codium.ai/images/pr_agent/improve_chat_on_code_suggestions_ask.png" />)

[//]: # ()
[//]: # (Read more about it [here]&#40;https://docs.pr-agent.ai/tools/improve/#chat-on-code-suggestions&#41;.)

[//]: # ()
[//]: # ()

## 为什么选择 PR-Agent？

### 🎯 专为真实开发团队打造

**快速且经济**：每个工具（`/review`、`/improve`、`/ask`）仅需一次 LLM 调用即可完成任务（约 30 秒，成本低廉）。

**支持任意大小的 PR**：我们的 [PR 压缩策略](https://docs.pr-agent.ai/core-abilities/#pr-compression-strategy) 可高效处理小型和大型 PR。

**高度可定制**：基于 JSON 的提示词配置允许你通过[配置文件](pr_agent/settings/configuration.toml)轻松自定义审查类别和行为。

**跨平台支持**： 
- **代码托管平台**：GitHub、GitLab、BitBucket、Azure DevOps、Gitea
- **部署方式**：CLI、GitHub Actions、Docker、私有化部署、Webhook
- **AI 模型**：OpenAI GPT、Claude、Deepseek 等

**开源优势**：
- 完全掌控你的数据和基础设施
- 根据你的团队需求自定义提示词和行为
- 无厂商锁定风险
- 社区驱动开发

## 功能特性

<div style="text-align:left;">

PR-Agent 提供全面的 Pull Request（PR）功能，并与多种 Git 平台集成：

|                                                         |                                                                                        | GitHub | GitLab | Bitbucket | Azure DevOps | Gitea |
|---------------------------------------------------------|----------------------------------------------------------------------------------------|:------:|:------:|:---------:|:------------:|:-----:|
| [工具](https://docs.pr-agent.ai/tools/)         | [描述](https://docs.pr-agent.ai/tools/describe/)                            |   ✅   |   ✅   |    ✅     |      ✅      |  ✅   |
|                                                         | [审查](https://docs.pr-agent.ai/tools/review/)                                |   ✅   |   ✅   |    ✅     |      ✅      |  ✅   |
|                                                         | [优化](https://docs.pr-agent.ai/tools/improve/)                              |   ✅   |   ✅   |    ✅     |      ✅      |  ✅   |
|                                                         | [提问](https://docs.pr-agent.ai/tools/ask/)                                      |   ✅   |   ✅   |    ✅     |      ✅      |       |
|                                                         | ⮑ [针对代码行提问](https://docs.pr-agent.ai/tools/ask/#ask-lines)            |   ✅   |   ✅   |           |              |       |
|                                                         | [帮助文档](https://docs.pr-agent.ai/tools/help_docs/?h=auto#auto-approval)     |   ✅   |   ✅   |    ✅     |              |       |
|                                                         | [更新变更日志](https://docs.pr-agent.ai/tools/update_changelog/)            |   ✅   |   ✅   |    ✅     |      ✅      |       |
|                                                         |                                                                                                                     |        |        |           |              |       |
| [使用方式](https://docs.pr-agent.ai/usage-guide/)   | [CLI](https://docs.pr-agent.ai/usage-guide/automations_and_usage/#local-repo-cli)                            |   ✅   |   ✅   |    ✅     |      ✅      |  ✅   |
|                                                         | [应用 / webhook](https://docs.pr-agent.ai/usage-guide/automations_and_usage/#github-app)                      |   ✅   |   ✅   |    ✅     |      ✅      |  ✅   |
|                                                         | [标签机器人](https://github.com/the-pr-agent/pr-agent#try-it-now)                                                     |   ✅   |        |           |              |       |
|                                                         | [Actions](https://docs.pr-agent.ai/installation/github/#run-as-a-github-action)                              |   ✅   |   ✅   |    ✅     |      ✅      |       |
|                                                         |                                                                                                                     |        |        |           |              |       |
| [核心能力](https://docs.pr-agent.ai/core-abilities/) | [自适应且感知 Token 的文件补丁适配](https://docs.pr-agent.ai/core-abilities/compression_strategy/) |   ✅   |   ✅   |    ✅     |      ✅      |       |
|                                                         | [动态上下文](https://docs.pr-agent.ai/core-abilities/dynamic_context/)                                  |   ✅   |   ✅   |    ✅     |      ✅      |       |
|                                                         | [获取 Ticket 上下文](https://docs.pr-agent.ai/core-abilities/fetching_ticket_context/)                  |   ✅    |  ✅    |     ✅     |              |       |
|                                                         | [交互性](https://docs.pr-agent.ai/core-abilities/interactivity/)                                      |   ✅   |  ✅   |           |              |       |
|                                                         | [本地与全局元数据](https://docs.pr-agent.ai/core-abilities/metadata/)                               |   ✅   |   ✅   |    ✅     |      ✅      |       |
|                                                         | [多模型支持](https://docs.pr-agent.ai/usage-guide/changing_a_model/)                            |   ✅   |   ✅   |    ✅     |      ✅      |       |
|                                                         | [PR 压缩](https://docs.pr-agent.ai/core-abilities/compression_strategy/)                              |   ✅   |   ✅   |    ✅     |      ✅      |       |
|                                                         | [自我反思](https://docs.pr-agent.ai/core-abilities/self_reflection/)                                  |   ✅   |   ✅   |    ✅     |      ✅      |       |

[//]: # (- Support for additional git providers is described in [here]&#40;./docs/Full_environments.md&#41;)
___

## 效果演示

</div>
<h4><a href="https://github.com/the-pr-agent/pr-agent/pull/530">/describe</a></h4>
<div align="center">
<p float="center">
<img src="https://www.codium.ai/images/pr_agent/describe_new_short_main.png" width="512">
</p>
</div>
<hr>

<h4><a href="https://github.com/the-pr-agent/pr-agent/pull/732#issuecomment-1975099151">/review</a></h4>
<div align="center">
<p float="center">
<kbd>
<img src="https://www.codium.ai/images/pr_agent/review_new_short_main.png" width="512">
</kbd>
</p>
</div>
<hr>

<h4><a href="https://github.com/the-pr-agent/pr-agent/pull/732#issuecomment-1975099159">/improve</a></h4>
<div align="center">
<p float="center">
<kbd>
<img src="https://www.codium.ai/images/pr_agent/improve_new_short_main.png" width="512">
</kbd>
</p>
</div>

<hr>

## 工作原理

下图展示了 PR-Agent 工具及其工作流程：

![PR-Agent Tools](https://www.qodo.ai/images/pr_agent/diagram-v0.9.png)

## 数据隐私

### 私有化部署的 PR-Agent

- 如果你使用自己的 OpenAI API Key 托管 PR-Agent，数据传输仅发生在你与 OpenAI 之间。你可以在此处阅读他们的 API 数据隐私政策：
https://openai.com/enterprise-privacy

## 贡献指南

如需为项目做出贡献，请首先阅读我们的[贡献指南](https://github.com/the-pr-agent/pr-agent/blob/b09eec265ef7d36c232063f76553efb6b53979ff/CONTRIBUTING.md)。


## ❤️ 社区支持

此次开源发布是 Qodo（现代 AI 驱动代码协作的发起者）向社区的贡献。我们很乐意分享它，并激励全球开发者。

该项目现已迎来首位外部维护者 Naor（[@naorpeled](https://github.com/naorpeled)），目前正逐步捐赠给一个开源基金会。