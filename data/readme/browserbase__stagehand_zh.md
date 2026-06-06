<div id="toc" align="center" style="margin-bottom: 0;">
  <ul style="list-style: none; margin: 0; padding: 0;">
    <a href="https://stagehand.dev">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="media/dark_logo.png" />
        <img alt="Stagehand" src="media/light_logo.png" width="200" style="margin-right: 30px;" />
      </picture>
    </a>
  </ul>
</div>
<p align="center">
  <strong>AI 浏览器自动化框架</strong><br>
  <a href="https://docs.stagehand.dev">阅读文档</a>
</p>

<p align="center">
  <a href="https://github.com/browserbase/stagehand/tree/main?tab=MIT-1-ov-file#MIT-1-ov-file">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="media/dark_license.svg" />
      <img alt="MIT License" src="media/light_license.svg" />
    </picture>
  </a>
  <a href="https://stagehand.dev/discord">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="media/dark_discord.svg" />
      <img alt="Discord Community" src="media/light_discord.svg" />
    </picture>
  </a>
</p>

<p align="center">
	<a href="https://trendshift.io/repositories/12122" target="_blank"><img src="https://trendshift.io/api/badge/repositories/12122" alt="browserbase%2Fstagehand | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

<p align="center">
  <a href="https://deepwiki.com/browserbase/stagehand">
    <img alt="Ask DeepWiki" src="https://deepwiki.com/badge.svg" />
  </a>
</p>

<p align="center">
如果你正在寻找 Python 实现版本，可以在 <a href="https://github.com/browserbase/stagehand-python">这里</a>找到它。
</p>

<div align="center" style="display: flex; align-items: center; justify-content: center; gap: 4px; margin-bottom: 0;">
  <b>Vibe 编码（自然语言编程）</b>
  <span style="font-size: 1.05em;">使用 </span>
  <a href="https://director.ai" style="display: flex; align-items: center;">
    <span>Director</span>
  </a>
  <span> 驱动 Stagehand</span>
  <span> </span>
  <picture>
    <img alt="Director" src="media/director_icon.svg" width="25" />
  </picture>
</div>

## 什么是 Stagehand？

Stagehand 是一个浏览器自动化框架，支持使用自然语言和代码来控制网页浏览器。通过结合 AI 的强大能力与代码的精确性，Stagehand 使网页自动化变得灵活、易于维护且真正可靠。

## 为什么选择 Stagehand？

大多数现有的浏览器自动化工具要么要求你在 Selenium、Playwright 或 Puppeteer 等框架中编写底层代码，要么使用在生产环境中表现不可预测的高级智能体（Agent）。通过让开发者自由选择哪些逻辑用代码编写、哪些用自然语言描述（并弥合两者之间的差距），Stagehand 成为生产环境浏览器自动化的理想选择。

1. **在何时使用代码与自然语言之间做出选择**：当你需要导航至陌生页面时，可使用 AI；当你对具体操作目标非常明确时，则使用代码。
2. **从 AI 驱动转向可重复的工作流**：Stagehand 允许你在执行前预览 AI 操作，并帮助你轻松缓存可重复的操作以节省时间和 Token（令牌）。
3. **编写一次，永久运行**：Stagehand 的自动缓存结合自愈机制会记住之前的操作，在无大语言模型（LLM）推理的情况下直接运行；当网站发生变更导致自动化中断时，它也知道何时重新引入 AI。

## 快速开始

只需一行代码即可开始使用 Stagehand，或查阅我们的 [Quickstart Guide](https://docs.stagehand.dev/v3/first-steps/quickstart) 获取更多信息：

```bash
npx create-browser-app
```

## 示例

以下是如何使用 Stagehand 构建一个示例浏览器自动化脚本：

```typescript
// Stagehand's CDP engine provides an optimized, low level interface to the browser built for automation
const page = stagehand.context.pages()[0];
await page.goto("https://github.com/browserbase");

// Use act() to execute individual actions
await stagehand.act("click on the stagehand repo");

// Use agent() for multi-step tasks
const agent = stagehand.agent();
await agent.execute("Get to the latest PR");

// Use extract() to get structured data from the page
const { author, title } = await stagehand.extract(
  "extract the author and title of the PR",
  z.object({
    author: z.string().describe("The username of the PR author"),
    title: z.string().describe("The title of the PR"),
  }),
);
```

## 文档

访问 [docs.stagehand.dev](https://docs.stagehand.dev) 查看完整文档。


### 从源码构建与运行

```bash
git clone https://github.com/browserbase/stagehand.git
cd stagehand
pnpm install
pnpm run build
pnpm run example # run the blank script at ./examples/example.ts
```

当你拥有大语言模型（LLM）提供商的 API Key 以及 Browserbase 凭据时，Stagehand 能发挥最佳性能。要将这些配置添加到你的项目中，请运行：

```bash
cp .env.example .env
nano .env # Edit the .env file to add API keys
```

### 从分支安装

你可以使用 [gitpkg](https://github.com/EqualMa/gitpkg) 直接从 GitHub 分支安装并构建 Stagehand。

在你的项目 `package.json` 中设置：
```json
"@browserbasehq/stagehand": "https://gitpkg.now.sh/browserbase/stagehand/packages/core?<branchName>",
```


## 贡献指南

> [!NOTE]
> 我们高度重视对 Stagehand 的贡献！如有任何疑问或需要支持，请加入我们的 [Discord community](https://stagehand.dev/discord)。

总体而言，我们按优先级顺序专注于提升可靠性、可扩展性、速度和成本效益。如果你有兴趣参与贡献，**修复 Bug 和进行小幅改进是最佳的切入点**。对于更复杂的特性开发，我们强烈建议你在开始之前先在我们的 [Discord community](https://stagehand.dev/discord) 联系 [Miguel Gonzalez](https://x.com/miguel_gonzf) 或 [Paul Klein](https://x.com/pk_iv)，以确保你的贡献与我们的目标保持一致。


<!-- For more information, please see our [Contributing Guide](https://docs.stagehand.dev/examples/contributing). -->

## 致谢

我们要感谢以下为 Stagehand 做出重大贡献的人士：
- [Paul Klein](https://github.com/pkiv)
- [Sean McGuire](https://github.com/seanmcguire12)
- [Miguel Gonzalez](https://github.com/miguelg719)
- [Sameel Arif](https://github.com/sameelarif)
- [Thomas Katwan](https://github.com/tkattkat)
- [Filip Michalsky](https://github.com/filip-michalsky)
- [Anirudh Kamath](https://github.com/kamath)
- [Jeremy Press](https://x.com/jeremypress)
- [Navid Pour](https://github.com/navidpour)

## 许可证

采用 MIT 许可证。

Copyright 2025 Browserbase, Inc.