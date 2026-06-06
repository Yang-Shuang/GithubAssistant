# promptfoo：LLM 评估与红队测试（Red Teaming）

<p align="center">
  <a href="https://npmjs.com/package/promptfoo"><img src="https://img.shields.io/npm/v/promptfoo" alt="npm"></a>
  <a href="https://npmjs.com/package/promptfoo"><img src="https://img.shields.io/npm/dm/promptfoo" alt="npm"></a>
  <a href="https://github.com/promptfoo/promptfoo/actions/workflows/main.yml"><img src="https://img.shields.io/github/actions/workflow/status/promptfoo/promptfoo/main.yml" alt="GitHub Workflow Status"></a>
  <a href="https://github.com/promptfoo/promptfoo/blob/main/LICENSE"><img src="https://img.shields.io/github/license/promptfoo/promptfoo" alt="MIT license"></a>
  <a href="https://discord.gg/promptfoo"><img src="https://img.shields.io/discord/1146610656779440188?logo=discord&label=promptfoo" alt="Discord"></a>
</p>

<p align="center">
  <code>promptfoo</code> 是一个用于评估和红队测试（Red Teaming）LLM 应用的命令行工具及库。告别试错法，开始交付安全、可靠的 AI 应用。
</p>

<p align="center">
  <a href="https://www.promptfoo.dev">网站</a> ·
  <a href="https://www.promptfoo.dev/docs/getting-started/">快速开始</a> ·
  <a href="https://www.promptfoo.dev/docs/red-team/">红队测试</a> ·
  <a href="https://www.promptfoo.dev/docs/">文档</a> ·
  <a href="https://discord.gg/promptfoo">Discord</a>
</p>

> promptfoo 现已成为 OpenAI 旗下项目。promptfoo 保持开源并采用 MIT 许可证。阅读[公司更新公告](https://www.promptfoo.dev/blog/promptfoo-joining-openai/)。

## 快速开始

npm 和 npx 使用需要 [Node.js](https://nodejs.org/en/download) `^20.20.0` 或 `>=22.22.0`。

```sh
npm install -g promptfoo
promptfoo init --example getting-started
```

也可通过 `brew install promptfoo` 和 `pip install promptfoo` 安装。你还可以直接使用 `npx promptfoo@latest` 运行任意命令，无需本地安装。

大多数 LLM（大语言模型）提供商需要 API Key（API 密钥）。请将其设置为环境变量：

```sh
export OPENAI_API_KEY=sk-abc123
```

进入示例目录后，运行评估并查看结果：

```sh
cd getting-started
promptfoo eval
promptfoo view
```

更多详情请参阅[快速开始](https://www.promptfoo.dev/docs/getting-started/)（评估）或[红队测试](https://www.promptfoo.dev/docs/red-team/)（漏洞扫描）。

## promptfoo 能做什么？

- **测试你的提示词和模型**：使用 [自动化评估](https://www.promptfoo.dev/docs/getting-started/)
- **保障 LLM 应用安全**：通过 [红队测试（Red Teaming）](https://www.promptfoo.dev/docs/red-team/) 与漏洞扫描
- **并排比较模型**：支持 OpenAI、Anthropic、Azure、Bedrock、Ollama 及[更多](https://www.promptfoo.dev/docs/providers/)
- **在 [CI/CD](https://www.promptfoo.dev/docs/integrations/ci-cd/) 中自动化执行检查**
- **审查 Pull Request**：使用 [代码扫描](https://www.promptfoo.dev/docs/code-scanning/) 排查与 LLM 相关的安全和合规问题
- **与团队共享评估结果**

实际运行效果如下：

<img src="site/static/img/claude-vs-gpt-example@2x.png" alt="prompt evaluation matrix - web viewer" width="700">

命令行界面同样支持：

<img src="https://www.promptfoo.dev/img/docs/self-grading.gif" alt="promptfoo command line" width="700">

它还能生成 [安全漏洞报告](https://www.promptfoo.dev/docs/red-team/)：

<img src="https://www.promptfoo.dev/img/redteam-dashboard@2x.jpg" alt="gen ai red team" width="700">

## 为什么选择 promptfoo？

- **面向开发者**：运行速度快，支持实时重载和缓存等功能
- **隐私安全**：LLM 评估完全在本地运行——你的提示词永远不会离开本机
- **灵活兼容**：支持任意 LLM API 或编程语言
- **经过实战检验**：已支撑日活超千万用户的 LLM 应用投入生产环境使用
- **数据驱动**：基于指标数据做出决策，而非凭直觉
- **开源开放**：采用 MIT 许可证，拥有活跃的社区生态

## 了解更多

- [快速开始](https://www.promptfoo.dev/docs/getting-started/)
- [完整文档](https://www.promptfoo.dev/docs/intro/)
- [红队测试指南](https://www.promptfoo.dev/docs/red-team/)
- [CLI 使用手册](https://www.promptfoo.dev/docs/usage/command-line/)
- [Node.js 包说明](https://www.promptfoo.dev/docs/usage/node-package/)
- [支持的模型列表](https://www.promptfoo.dev/docs/providers/)
- [代码扫描指南](https://www.promptfoo.dev/docs/code-scanning/)

## 参与贡献

我们欢迎所有形式的贡献！请查阅我们的[贡献指南](https://www.promptfoo.dev/docs/contributing/)开始参与。

加入我们的 [Discord 社区](https://discord.gg/promptfoo)获取帮助与进行交流讨论。

<a href="https://github.com/promptfoo/promptfoo/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=promptfoo/promptfoo" />
</a>