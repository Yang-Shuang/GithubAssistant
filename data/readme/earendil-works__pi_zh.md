<p align="center">
  <a href="https://pi.dev">
    <img alt="pi logo" src="https://pi.dev/logo-auto.svg" width="128">
  </a>
</p>
<p align="center">
  <a href="https://discord.com/invite/3cU7Bz4UPx"><img alt="Discord" src="https://img.shields.io/badge/discord-community-5865F2?style=flat-square&logo=discord&logoColor=white" /></a>
</p>
<p align="center">
  <a href="https://pi.dev">pi.dev</a> domain graciously donated by
  <br /><br />
  <a href="https://exe.dev"><img src="packages/coding-agent/docs/images/exy.png" alt="Exy mascot" width="48" /><br />exe.dev</a>
</p>

> 默认情况下，新贡献者提交的新 Issue 和 Pull Request（PR）将自动关闭。维护者会每日审查这些自动关闭的 Issue。详情请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

# Pi Agent Harness Monorepo

这里是 Pi Agent Harness 项目的所在地，包含我们自扩展的编码代理。

* **[@earendil-works/pi-coding-agent](packages/coding-agent)**：交互式编码代理 CLI 工具
* **[@earendil-works/pi-agent-core](packages/agent)**：支持工具调用与状态管理的代理运行时环境
* **[@earendil-works/pi-ai](packages/ai)**：统一的多提供商大语言模型（LLM）API 接口（支持 OpenAI、Anthropic、Google 等）

了解更多关于 Pi 的信息：

* [访问 pi.dev](https://pi.dev)，项目官网，内含演示示例
* [阅读文档](https://pi.dev/docs/latest)，你也可以直接询问代理让它为你解释

## 分享你的开源编码代理会话记录

如果你使用 Pi 或其他编码代理进行开源开发，欢迎分享你的会话记录。

公开的开源（OSS）会话数据有助于利用真实任务、工具调用、失败案例及修复过程来改进编码代理，而非仅依赖简单的测试基准（benchmarks）。

完整说明请参阅 [X 平台上的这篇帖子](https://x.com/badlogicgames/status/2037811643774652911)。

要发布会话记录，请使用 [`badlogic/pi-share-hf`](https://github.com/badlogic/pi-share-hf)。阅读其 `README.md` 获取设置说明。你只需要一个 Hugging Face 账号、Hugging Face CLI 工具以及 `pi-share-hf`。

你也可以观看 [这段视频](https://x.com/badlogicgames/status/2041151967695634619)，视频中演示了我如何发布自己的 `pi-mono` 会话记录。

我会定期在此处发布自己的 `pi-mono` 工作会话：

- [Hugging Face 上的 badlogicgames/pi-mono 数据集](https://huggingface.co/datasets/badlogicgames/pi-mono)

## 全部软件包

| Package | Description |
|---------|-------------|
| **[@earendil-works/pi-ai](packages/ai)** | 统一的多提供商大语言模型（LLM）API 接口（支持 OpenAI、Anthropic、Google 等） |
| **[@earendil-works/pi-agent-core](packages/agent)** | 支持工具调用与状态管理的代理运行时环境 |
| **[@earendil-works/pi-coding-agent](packages/coding-agent)** | 交互式编码代理 CLI 工具 |
| **[@earendil-works/pi-tui](packages/tui)** | 带有差分渲染功能的终端 UI（TUI）库 |

如需了解 Slack/聊天自动化与工作流，请参阅 [earendil-works/pi-chat](https://github.com/earendil-works/pi-chat)。

## 贡献指南

贡献规范请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)，项目特定规则（适用于人类与代理）请参阅 [AGENTS.md](AGENTS.md)。

## 开发环境

```bash
npm install --ignore-scripts  # 安装所有依赖项，不运行生命周期脚本
npm run build        # 构建所有软件包
npm run check        # 代码检查、格式化与类型检查
./test.sh            # 运行测试（若无 API Key 将跳过依赖 LLM 的测试）
./pi-test.sh         # 从源码运行 Pi（可在任意目录下执行）
```

## 供应链安全加固

我们将 npm 依赖项的变更视为已审查的代码更改。

- 直接外部依赖项固定为精确版本。内部工作区软件包保留版本范围限制。
- `.npmrc` 配置了 `save-exact=true` 和 `min-release-age=2`，以避免在 npm 解析依赖时遇到同日发布的新版本。
- `package-lock.json` 是依赖关系的权威来源。除非设置了环境变量 `PI_ALLOW_LOCKFILE_CHANGE=1`，否则 pre-commit 钩子会阻止意外提交锁文件。
- `npm run check` 用于验证已固定的直接依赖项、原生 TypeScript 导入兼容性以及生成的编码代理 shrinkwrap（精简锁定）文件。
- 发布的 CLI 软件包包含 `packages/coding-agent/npm-shrinkwrap.json`，该文件由根锁文件生成，用于为 npm 用户固定传递依赖项。
- 发布冒烟测试使用 `npm run release:local` 在仓库外部构建、打包，并创建隔离的 npm 和 Bun 安装环境，随后再打发布标签。
- 本地发布安装、文档中的 npm 安装以及 `pi update --self` 命令在支持的情况下均使用 `--ignore-scripts`。
- CI 环境通过 `npm ci --ignore-scripts` 安装依赖，并配置定时 GitHub Workflow 运行 `npm audit --omit=dev` 及 `npm audit signatures --omit=dev`。
- shrinkwrap 生成过程对依赖项的生命周期脚本设有明确的白名单；新添加的包含生命周期脚本的依赖项在未经审查前会导致检查失败。

## 许可证

MIT