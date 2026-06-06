<a href="https://www.warp.dev">
    <img width="1024" alt="Warp Agentic Development Environment product preview" src="https://github.com/user-attachments/assets/9976b2da-2edd-4604-a36c-8fd53719c6d4" />
</a>
&nbsp;
<p align="center">
  <a href="https://www.warp.dev"><img height="20" alt="Built with Warp" src="https://raw.githubusercontent.com/warpdotdev/brand-assets/main/Github/Built-With-Warp-Export@2x.png" /></a>
  &nbsp;
  <a href="https://oz.warp.dev"><img height="20" alt="Powered by Oz" src="https://raw.githubusercontent.com/warpdotdev/brand-assets/main/Github/Powered-By-Oz-Export@2x.png" /></a>
</p>

<p align="center">
  <a href="https://www.warp.dev">官网</a>
  ·
  <a href="https://www.warp.dev/code">代码</a>
  ·
  <a href="https://www.warp.dev/agents">智能体</a>
  ·
  <a href="https://www.warp.dev/terminal">终端</a>
  ·
  <a href="https://www.warp.dev/drive">Drive</a>
  ·
  <a href="https://docs.warp.dev">文档</a>
  ·
  <a href="https://www.warp.dev/blog/how-warp-works">Warp 工作原理</a>
</p>

> [!NOTE]
> OpenAI 是新开源 Warp 仓库的创始赞助商，新的智能体管理工作流由 GPT 模型提供支持。

<h1></h1>

## About

[Warp](https://www.warp.dev) 是一款源于终端的智能体开发环境。你可以使用 Warp 内置的编码智能体，也可以接入你自己的 CLI 智能体（如 Claude Code、Codex、Gemini CLI 等）。

## Installation

你可以[下载 Warp](https://www.warp.dev/download)，并查阅我们的[文档](https://docs.warp.dev/)以获取针对特定平台的安装说明。

## Warp Contributions Overview Dashboard

访问 [build.warp.dev](https://build.warp.dev) 可：
- 观看数千个 Oz 智能体进行问题分类、编写规范、实现变更以及审查 PR（Pull Request）
- 查看顶级贡献者和正在开发中的功能
- 使用 GitHub 账号登录以跟踪你自己的 Issue
- 点击进入 Web 端 Warp 终端中的活跃智能体会话

## Oz for OSS

正在维护热门开源项目？[申请 Oz 积分](https://tally.so/r/LZWxqG)以探索 [Oz for OSS](https://github.com/warpdotdev/oz-for-oss)。

Oz for OSS 是我们的合作伙伴计划，旨在将本仓库中使用的相同智能体开源管理工作流引入精选的合作伙伴仓库。我们将直接与项目维护者合作，实施适用于每个项目的 Issue 分类、PR 审查、社区管理和贡献者协调等工作流。

## Licensing

Warp 的 UI 框架（即 `warpui_core` 和 `warpui` crate）采用 [MIT 许可证](LICENSE-MIT)。

本仓库中的其余代码采用 [AGPL v3 许可证](LICENSE-AGPL)。

## Open Source & Contributing

Warp 的客户端代码库已开源并托管于本仓库。我们欢迎社区贡献，并设计了一套轻量级工作流以帮助新贡献者快速上手。如需完整贡献流程指南，请阅读我们的 [CONTRIBUTING.md](CONTRIBUTING.md) 文档。

> [!TIP]
> **Chat with contributors and the Warp team** in the [`#oss-contributors`](https://warpcommunity.slack.com/archives/C0B0LM8N4DB) Slack channel — a good place for ad-hoc questions, design discussion, and pairing with maintainers. New here? [Join the Warp Slack community](https://go.warp.dev/join-preview) first, then jump into `#oss-contributors`.

### Issue to PR

提交前，请先[搜索现有 Issue](https://github.com/warpdotdev/warp/issues?q=is%3Aissue+is%3Aopen+sort%3Areactions-%2B1-desc)以确认是否已有相关 Bug 或功能请求。若未找到相关内容，请使用我们的模板[提交新 Issue](https://github.com/warpdotdev/warp/issues/new/choose)。安全漏洞应按照 [CONTRIBUTING.md](CONTRIBUTING.md#reporting-security-issues) 中的说明进行私下报告。

Issue 提交后，Warp 维护者将对其进行审查并可能添加就绪标签：[`ready-to-spec`](https://github.com/warpdotdev/warp/issues?q=is%3Aissue+is%3Aopen+label%3Aready-to-spec) 表示设计已开放，贡献者可据此编写详细规范；[`ready-to-implement`](https://github.com/warpdotdev/warp/issues?q=is%3Aissue+is%3Aopen+label%3Aready-to-implement) 表示设计方案已确定，欢迎提交代码 PR。任何人都可以认领带有标签的 Issue——若希望某个 Issue 被考虑添加就绪标签，请在该 Issue 下 **@oss-maintainers**。

### Building the Repo Locally

从源码构建并运行 Warp：

```bash
./script/bootstrap   # platform-specific setup
./script/run         # build and run Warp
./script/presubmit   # fmt, clippy, and tests
```

完整的工程指南（包括编码规范、测试方法及平台特定说明）请参阅 [WARP.md](WARP.md)。

## Joining the Team

有兴趣加入团队？请查看我们的[招聘职位](https://www.warp.dev/careers)。

## Support and Questions

1. 查阅我们的[文档](https://docs.warp.dev/)以获取 Warp 功能的全面指南。
2. 加入我们的 [Slack Community](https://go.warp.dev/join-preview)与其他用户交流，并获取 Warp 团队的支持——贡献者主要活跃在 [`#oss-contributors`](https://warpcommunity.slack.com/archives/C0B0LM8N4DB)。
3. 尝试我们的[Preview build](https://www.warp.dev/download-preview)以测试最新的实验性功能。
4. 在任何 Issue 下 **@oss-maintainers** 即可将问题升级至团队处理——例如，当你在使用自动化智能体时遇到问题。

## Code of Conduct

我们要求大家保持尊重与同理心。Warp 遵循[行为准则](CODE_OF_CONDUCT.md)。如需举报违规行为，请发送邮件至 warp-coc@warp.dev。

## Open Source Dependencies

我们想特别致谢以下助力 Warp 起步的[开源依赖项](https://docs.warp.dev/help/licenses)：

- [Tokio](https://github.com/tokio-rs/tokio)
- [NuShell](https://github.com/nushell/nushell)
- [Fig Completion Specs](https://github.com/withfig/autocomplete)
- [Warp Server Framework](https://github.com/seanmonstar/warp)
- [Alacritty](https://github.com/alacritty/alacritty)
- [Hyper HTTP library](https://github.com/hyperium/hyper)
- [FontKit](https://github.com/servo/font-kit)
- [Core-foundation](https://github.com/servo/core-foundation-rs)
- [Smol](https://github.com/smol-rs/smol)