## 欢迎使用你的全新 SaaS 应用！🎉

<div style="display: flex; gap: 16px; align-items: center;">
  <a href="https://www.producthunt.com/products/open-saas?embed=true&utm_source=badge-top-post-topic-badge&utm_medium=badge&utm_source=badge-open&#0045;saas&#0045;2&#0045;0" target="_blank">
    <img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-topic-badge.svg?post_id=1023519&theme=neutral&period=weekly&topic_id=237&t=1760520428563" alt="Open&#0032;SaaS&#0032;2&#0046;0 - Free&#0044;&#0032;open&#0045;source&#0032;SaaS&#0032;starter&#0032;kit&#0032;with&#0032;superpowers | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" />
  </a>
  <a href="https://www.producthunt.com/products/open-saas?embed=true&utm_source=badge-top-post-badge&utm_medium=badge&utm_source=badge-open&#0045;saas&#0045;2&#0045;0" target="_blank">
    <img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=1023519&theme=neutral&period=daily&t=1760520428563" alt="Open&#0032;SaaS&#0032;2&#0046;0 - Free&#0044;&#0032;open&#0045;source&#0032;SaaS&#0032;starter&#0032;kit&#0032;with&#0032;superpowers | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" />
  </a>
</div>

https://github.com/user-attachments/assets/3856276b-23e9-455e-a564-b5f26f4f0e98

你决定使用 Open SaaS 模板来构建一个 SaaS 应用。这是个很棒的选择！

该模板具备以下特点：

1. 完全开源
2. 免费使用和分发
3. 开箱即用，内置大量功能！
4. 已准备好与你常用的 AI 编程工具或代理（如 Claude Code、Cursor、Codex、OpenCode 等）配合使用

🧑‍💻 在这里查看实际运行效果：[OpenSaaS.sh](https://opensaas.sh)
📚 查阅文档：[Open SaaS Docs](https://docs.opensaas.sh)

## 核心技术与内置组件

该模板基于一系列强大的工具与框架构建，包括：

- 🐝 [Wasp](https://wasp.sh) - 一款具备“超能力”的全栈框架，基于 React、Node.js 和 Prisma
- 🚀 [Astro](https://starlight.astro.build/) - Astro 官方轻量级文档与博客模板 “Starlight”
- 💸 [Stripe](https://stripe.com)、[Polar.sh](https://polar.sh) 或 [Lemon Squeezy](https://lemonsqueezy.com/) - 用于商品管理与支付处理
- 💅 [ShadCN UI](https://tailwindcss.com) - 提供组件与样式支持（还包含管理后台面板！）
- 🤖 [AI-Ready](https://docs.opensaas.sh/) - 为 AI 辅助编程（如 Claude Code、Cursor 或你喜爱的其他工具）定制的插件、技能与规则集
- 📈 [Plausible](https://plausible.io) 或 [Google](https://analytics.google.com/) 分析工具
- 🤖 [OpenAI](https://openai.com) - OpenAI API，并附带函数调用示例
- 📦 [AWS S3](https://aws.amazon.com/s3/) - 用于文件上传存储
- 📧 [SendGrid](https://sendgrid.com)、[MailGun](https://mailgun.com) 或 SMTP - 用于邮件发送服务
- 🧪 [Playwright](https://playwright.dev) - 基于 Playwright 的端到端测试

由于我们采用 Wasp 作为全栈框架，可以充分利用其特性以极快的速度构建 SaaS 应用，其中包括：

- 🔐 [全栈身份认证 (Authentication)](https://wasp.sh/docs/auth/overview) - 仅需几行代码即可实现邮箱验证与第三方社交登录。
- ⛑ [端到端类型安全 (Type Safety)](https://wasp.sh/docs/data-model/operations/overview) - 为后端函数定义类型后，前端将自动推断对应类型，无需安装或配置任何第三方库。此外还包含类型安全的链接路由！
- 🤖 [定时任务 (Jobs)](https://wasp.sh/docs/advanced/jobs) - 只需在配置文件中定义函数，即可在后台运行 Cron 任务或设置队列。
- 🚀 [一键部署 (One-command Deploy)](https://wasp.sh/docs/advanced/deployment/overview) - 通过 CLI 执行一条命令即可轻松将数据库、服务端与客户端部署至 [Railway](https://railway.app) 或 [Fly.io](https://fly.io)。也可手动部署到你选择的任意其他托管服务。

如果你在开发过程中遇到困难或需要帮助，还可以随时加入 Wasp 活跃且乐于助人的社区。

- 🤝 [Wasp Discord](https://discord.gg/aCamt5wCpS)

## 快速上手

### 简易步骤

首先，在 macOS、Linux 或带有 WSL 的 Windows 上安装最新版 [Wasp](https://wasp.sh/)，请运行以下命令：

```bash
npm i -g @wasp.sh/wasp-cli
```

接着，使用以下命令创建一个新的 SaaS 应用：

```bash
wasp new -t saas
```

该命令会在当前目录下生成一份 **Open SaaS 模板的干净副本**，你可以立即开始构建自己的 SaaS 应用！

### 详细指南

关于如何上手及使用该模板的所有细节，请查阅 [Open SaaS 官方文档](https://docs.opensaas.sh)。

我们已将所有内容进行了详尽说明，涵盖安装步骤、拉取模板更新、服务集成指南、SEO 优化、部署流程等。🚀

## 获取帮助与提供反馈

你可以通过以下两种方式获取帮助或提交反馈（我们会尽力快速响应！）：

1. [在 GitHub 创建 Issue](https://github.com/wasp-lang/open-saas/issues)
2. [Wasp Discord 社区](https://discord.gg/aCamt5wCpS) —— 请将问题发送至 `#🙋questions` 频道

## 开发工具

### 代码质量工具

本仓库内置了完善的代码质量检查工具，帮助你维持统一的代码规范：

#### Prettier（代码格式化）

Prettier 已配置为自动对所有 JavaScript、TypeScript 及其他支持的文件进行格式化。

```bash
# Check if files are formatted correctly
npm run prettier:check

# Automatically format all files
npm run prettier:format
```

#### ESLint（代码静态检查）

ESLint 已配置支持 TypeScript 与 React，用于捕获潜在 Bug 并强制执行代码质量标准。

```bash
# Run ESLint to check for issues
npm run lint

# Automatically fix fixable issues
npm run lint:fix
```

ESLint 配置包含以下内容：

- 基于 `@typescript-eslint` 的 TypeScript 支持
- React 与 React Hooks 的代码检查规则
- 针对 SaaS 应用优化的合理默认配置
- 自动支持 CommonJS (.cjs)、ES Modules (.mjs) 以及 TypeScript 文件

Prettier 与 ESLint 的检查任务已集成至 CI/CD 流水线中，以自动保障代码质量。

关于用于维护衍生项目（如 opensaas.sh 和 template-test）的其他开发工具信息，请参阅 [tools/README.md](./tools/README.md)。

## 参与贡献

我们已尽力将 SaaS 应用的核心功能尽可能多地集成到该模板中，但仍可能存在部分缺失的功能或特性。

如果你愿意帮忙完善细节、填补空白，我们非常欢迎你的贡献！更多详情请查阅 [CONTRIBUTING.md](/CONTRIBUTING.md)。