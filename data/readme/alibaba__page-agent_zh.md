# Page Agent

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://img.alicdn.com/imgextra/i4/O1CN01qKig1P1FnhpFKNdi6_!!6000000000532-2-tps-1280-256.png">
  <img alt="Page Agent Banner" src="https://img.alicdn.com/imgextra/i1/O1CN01NCMKXj1Gn4tkFTsxf_!!6000000000666-2-tps-1280-256.png">
</picture>

[![License: MIT](https://img.shields.io/badge/License-MIT-auto.svg)](https://opensource.org/licenses/MIT) [![TypeScript](https://img.shields.io/badge/%3C%2F%3E-TypeScript-%230074c1.svg)](http://www.typescriptlang.org/) [![Bundle Size](https://img.shields.io/bundlephobia/minzip/page-agent)](https://bundlephobia.com/package/page-agent) [![Downloads](https://img.shields.io/npm/dt/page-agent.svg)](https://www.npmjs.com/package/page-agent) [![GitHub stars](https://img.shields.io/github/stars/alibaba/page-agent.svg)](https://github.com/alibaba/page-agent)

运行在网页中的图形界面（GUI）智能代理。使用自然语言控制网页界面。

🌐 **英文** | [中文](./docs/README-zh.md)

<a href="https://alibaba.github.io/page-agent/" target="_blank"><b>🚀 演示</b></a> | <a href="https://alibaba.github.io/page-agent/docs/introduction/overview" target="_blank"><b>📖 文档</b></a> | <a href="https://news.ycombinator.com/item?id=47264138" target="_blank"><b>📢 HN 讨论</b></a> | <a href="https://x.com/simonluvramen" target="_blank"><b>𝕏 关注 X (Twitter)</b></a>

<video id="demo-video" src="https://github.com/user-attachments/assets/a1f2eae2-13fb-4aae-98cf-a3fc1620a6c2" controls crossorigin muted></video>

---

## ✨ 核心特性

- **🎯 轻松集成**
    - 无需安装浏览器扩展、Python 或无头浏览器。
    - 仅需在页面内注入 JavaScript，所有操作均在你的网页中完成。
- **📖 基于文本的 DOM 操作**
    - 无需截图。不需要多模态大语言模型（LLM）或特殊权限。
- **🧠 支持自定义接入 LLM**
- **🐙 可选的 [Chrome 扩展](https://alibaba.github.io/page-agent/docs/features/chrome-extension)**，用于多页面任务。
    - 以及一个 [MCP 服务器（测试版）](https://alibaba.github.io/page-agent/docs/features/mcp-server)，以便从外部进行控制

## 💡 使用场景

- **SaaS AI 智能助手** —— 仅需几行代码，即可在你的产品中集成 AI 智能助手。无需重写后端。
- **智能表单填写** —— 将需要 20 次点击的工作流简化为一句指令。非常适合企业资源计划（ERP）、客户关系管理（CRM）及后台管理系统。
- **无障碍访问** —— 通过自然语言让任何 Web 应用实现无障碍操作。支持语音命令、屏幕阅读器，零门槛使用。
- **多页面智能代理** —— 借助 [Chrome 扩展](https://alibaba.github.io/page-agent/docs/features/chrome-extension)，让你的网页智能代理跨越多个浏览器标签页进行操作。
- **MCP 协议支持** —— 允许你的智能代理客户端直接控制浏览器。

## 🚀 快速开始

### 一行代码集成

使用我们免费的演示大语言模型（LLM）体验 PageAgent 的最快方式：

```html
<script src="{URL}" crossorigin="true"></script>
```

> **⚠️ 仅供技术评估使用。** 该演示 CDN 使用了我们免费的 [测试版 LLM API](https://alibaba.github.io/page-agent/docs/features/models#free-testing-api)。使用即表示你同意其[条款与隐私政策](https://github.com/alibaba/page-agent/blob/main/docs/terms-and-privacy.md)。

| Mirrors | URL                                                                                |
| ------- | ---------------------------------------------------------------------------------- |
| Global  | https://cdn.jsdelivr.net/npm/page-agent@1.8.2/dist/iife/page-agent.demo.js         |
| China   | https://registry.npmmirror.com/page-agent/1.8.2/files/dist/iife/page-agent.demo.js |

添加 `?autoInit=false` 参数加载脚本，将不会自动创建演示代理。随后可通过 `new window.PageAgent(...)` 手动实例化它。

### NPM 安装

```bash
npm install page-agent
```

```javascript
import { PageAgent } from 'page-agent'

const agent = new PageAgent({
    model: 'qwen3.5-plus',
    baseURL: 'https://dashscope.aliyuncs.com/compatible-mode/v1',
    apiKey: 'YOUR_API_KEY',
    language: 'en-US',
})

await agent.execute('Click the login button')
```

更多编程式用法，请参阅 [📖 文档](https://alibaba.github.io/page-agent/docs/introduction/overview)。

## 🌟 优秀项目展示

使用 PageAgent 构建了有趣的项目？欢迎添加到这里！提交 Pull Request（PR）分享你的作品。

> 这些均为社区项目，我们未对其进行维护或背书。请酌情使用。

| Project  | Description                                                 |
| -------- | ----------------------------------------------------------- |
| _Yours?_ | [Open a PR](https://github.com/alibaba/page-agent/pulls) 🙌 |

## 🤝 参与贡献

我们欢迎社区的贡献！请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 了解贡献规范，以及 [docs/developer-guide.md](docs/developer-guide.md) 获取本地开发工作流指南。

请阅读维护者关于项目原则与当前状态的[说明](https://github.com/alibaba/page-agent/issues/349)。

完全由**机器人或人工智能（AI）**生成且缺乏实质性人工参与的贡献将**不予接受**。

## ⚖️ 许可证

[MIT License](LICENSE)

## 👏 致谢

本项目基于**[`browser-use`](https://github.com/browser-use/browser-use)**的优秀工作构建。

`PageAgent` 专为**客户端网页增强**设计，而非服务端自动化。

```
DOM processing components and prompt are derived from browser-use:

Browser Use <https://github.com/browser-use/browser-use>
Copyright (c) 2024 Gregor Zunic
Licensed under the MIT License

We gratefully acknowledge the browser-use project and its contributors for their
excellent work on web automation and DOM interaction patterns that helped make
this project possible.
```

---

**如果你觉得 PageAgent 有用，请给本仓库点个 ⭐ Star！**