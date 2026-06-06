<div align="center">
<img width="800" alt="header image" src="assets/web-preview.png">
<h3 align="center">Onlook</h3>
  <p align="center">
    设计师专用的 Cursor
    <br />
    <a href="https://docs.onlook.com"><strong>探索文档 »</strong></a>
    <br />
  </p>
  <p align="center">
    👨‍💻👩‍💻👨‍💻
    <a href="https://www.ycombinator.com/companies/onlook/jobs/e4gHv1n-founding-engineer-fullstack">我们在旧金山招聘工程师！</a>
    👩‍💻👨‍💻👩‍💻
  </p>
    <br />
    <a href="https://youtu.be/RSX_3EaO5eU?feature=shared">查看演示</a>
    ·
    <a href="https://github.com/onlook-dev/onlook/issues/new?labels=bug&template=bug-report---.md">报告 Bug</a>
    ·
    <a href="https://github.com/onlook-dev/onlook/issues/new?labels=enhancement&template=feature-request---.md">请求新功能</a>
  </p>
  <!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Apache License][license-shield]][license-url] -->

[![Discord][discord-shield]][discord-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Twitter][twitter-shield]][twitter-url]

[中文](https://www.readme-i18n.com/onlook-dev/onlook?lang=zh) |
[Español](https://www.readme-i18n.com/onlook-dev/onlook?lang=es) |
[Deutsch](https://www.readme-i18n.com/onlook-dev/onlook?lang=de) |
[français](https://www.readme-i18n.com/onlook-dev/onlook?lang=fr) |
[Português](https://www.readme-i18n.com/onlook-dev/onlook?lang=pt) |
[Русский](https://www.readme-i18n.com/onlook-dev/onlook?lang=ru) |
[日本語](https://www.readme-i18n.com/onlook-dev/onlook?lang=ja) |
[한국어](https://www.readme-i18n.com/onlook-dev/onlook?lang=ko)

</div>

# 一款开源、视觉优先的代码编辑器

使用 AI 在 Next.js + TailwindCSS 中创建网站、原型和设计稿。通过可视化编辑器直接在浏览器 DOM（文档对象模型）中进行编辑。结合代码实现实时设计。它是 Bolt.new、Lovable、V0、Replit Agent、Figma Make、Webflow 等工具的开源替代方案。

### 🚧 🚧 🚧 Onlook 仍在开发中 🚧 🚧 🚧

我们正在积极寻找贡献者，共同将 Onlook for Web 打造为卓越的提示词驱动构建（prompt-to-build）体验。查看 [开放议题](https://github.com/onlook-dev/onlook/issues) 获取完整的功能建议（及已知问题）列表，并加入我们的 [Discord](https://discord.gg/hERDfFZCsH)，与数百位开发者共同协作。

## 使用 Onlook 你可以：

- [x] 秒级创建 Next.js 应用
  - [x] 从文本或图片开始
  - [x] 使用预置模板
  - [ ] 从 Figma 导入
  - [ ] 从 GitHub 仓库导入
  - [ ] 向 GitHub 仓库提交 PR（Pull Request）
- [x] 可视化编辑应用
  - [x] 使用类 Figma 界面
  - [x] 实时预览应用
  - [x] 管理品牌资产与 Tokens
  - [x] 创建页面并导航至页面
  - [x] 浏览图层
  - [x] 管理项目图片
  - [x] 检测并使用组件 – _此前位于 [Onlook Desktop](https://github.com/onlook-dev/desktop)_
  - [ ] 拖拽式组件面板
  - [x] 使用分支功能进行设计实验
- [x] 开发工具
  - [x] 实时代码编辑器
  - [x] 保存与从检查点恢复
  - [x] 通过 CLI（命令行界面）运行命令
  - [x] 连接应用市场
- [x] 秒级部署应用
  - [x] 生成可分享链接
  - [x] 绑定自定义域名    
- [ ] 团队协作
  - [x] 实时编辑
  - [ ] 留下评论
- [ ] 高级 AI 功能
  - [x] 一次性排队多条消息
  - [ ] 将图片用作参考及项目资产
  - [ ] 在项目中设置并使用 MCP（模型上下文协议）
  - [ ] 允许 Onlook 将自身作为工具调用，用于创建分支与迭代
- [ ] 高级项目支持
  - [ ] 支持非 Next.js 项目
  - [ ] 支持非 TailwindCSS 项目

![Onlook-GitHub-Example](https://github.com/user-attachments/assets/642de37a-72cc-4056-8eb7-8eb42714cdc4)

## 快速开始

使用我们的 [托管应用](https://onlook.com) 或 [本地运行](https://docs.onlook.com/developers/running-locally)。

### 使用方法

Onlook 可运行于任何 Next.js + TailwindCSS 项目。将你的项目导入 Onlook，或在编辑器中从零开始创建。

使用 AI 对话来创建或编辑你正在处理的项目。随时右键点击任意元素，即可在代码中定位该元素的确切位置。

<img width="600" alt="image" src="https://github.com/user-attachments/assets/4ad9f411-b172-4430-81ef-650f4f314666" />

<br>

绘制新的 `div` 元素，并通过拖拽操作在其父容器内重新排列它们的位置。

<img width="600" alt="image" src="assets/insert-div.png">

<br>

将代码与网站设计并排预览。

<img width="600" alt="image" src="assets/code-connect.png">

<br>

使用 Onlook 的编辑器工具栏调整 TailwindCSS 样式、直接操作对象，以及尝试不同的布局方案。

<img width="600" alt="image" src="assets/text-styling.png" />

## 文档

完整文档请访问 [docs.onlook.com](https://docs.onlook.com)

如需了解如何参与贡献，请查阅文档中的 [为 Onlook 做贡献](https://docs.onlook.com/developers)。

## 工作原理

<img width="676" alt="architecture" src="assets/architecture.png">

1. 创建应用时，我们将代码加载至 Web 容器中
2. 容器运行并提供代码服务
3. 编辑器接收预览链接并在 iFrame（内联框架）中展示
4. 编辑器读取并索引来自容器的代码
5. 我们对代码进行插桩处理（Instrumentation），以建立页面元素与代码位置的映射关系
6. 编辑元素时，先在 iFrame 中修改，随后同步更新到代码中
7. 我们的 AI 对话同样具备代码访问权限及工具，用于理解与编辑代码

理论上，该架构可扩展至任何以声明式方式渲染 DOM 元素的语言或框架（例如 jsx/tsx/html）。目前我们专注于使其与 Next.js 和 TailwindCSS 完美配合。

完整流程请参阅我们的 [架构文档](https://docs.onlook.com/developers/architecture)。

### 技术栈

#### 前端

- [Next.js](https://nextjs.org/) - 全栈框架
- [TailwindCSS](https://tailwindcss.com/) - 样式库
- [tRPC](https://trpc.io/) - 服务端接口

#### 数据库

- [Supabase](https://supabase.com/) - 认证、数据库与存储
- [Drizzle](https://orm.drizzle.team/) - ORM（对象关系映射）工具

#### AI / 大模型

- [AI SDK](https://ai-sdk.dev/) - LLM 客户端
- [OpenRouter](https://openrouter.ai/) - LLM 模型提供商
- [Morph Fast Apply](https://morphllm.com) - 快速应用模型提供商
- [Relace](https://relace.ai) - 快速应用模型提供商

#### 沙箱与托管

- [CodeSandbox SDK](https://codesandbox.io/docs/sdk) - 开发沙箱
- [Freestyle](https://www.freestyle.sh/) - 托管服务

#### 运行时

- [Bun](https://bun.sh/) - Monorepo、运行时与打包工具
- [Docker](https://www.docker.com/) - 容器管理

## 参与贡献

![image](https://github.com/user-attachments/assets/ecc94303-df23-46ae-87dc-66b040396e0b)

如果你有改进建议，请 Fork 本仓库并创建 Pull Request。你也可以直接 [提交 Issue](https://github.com/onlook-dev/onlook/issues)。

详细操作指南与行为准则请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。

#### 贡献者

<a href="https://github.com/onlook-dev/onlook/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=onlook-dev/onlook" />
</a>

## 联系方式

![image](https://github.com/user-attachments/assets/60684b68-1925-4550-8efd-51a1509fc953)

- 团队：[Discord](https://discord.gg/hERDfFZCsH) - [Twitter](https://twitter.com/onlookdev) - [LinkedIn](https://www.linkedin.com/company/onlook-dev/) - [Email](mailto:contact@onlook.com)
- 项目地址： https://github.com/onlook-dev/onlook
- 官网： https://onlook.com

## 许可证

本项目基于 Apache 2.0 许可证分发。更多信息请参阅 [LICENSE.md](LICENSE.md)。

<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/onlook-dev/studio.svg?style=for-the-badge
[contributors-url]: https://github.com/onlook-dev/onlook/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/onlook-dev/studio.svg?style=for-the-badge
[forks-url]: https://github.com/onlook-dev/onlook/network/members
[stars-shield]: https://img.shields.io/github/stars/onlook-dev/studio.svg?style=for-the-badge
[stars-url]: https://github.com/onlook-dev/onlook/stargazers
[issues-shield]: https://img.shields.io/github/issues/onlook-dev/studio.svg?style=for-the-badge
[issues-url]: https://github.com/onlook-dev/onlook/issues
[license-shield]: https://img.shields.io/github/license/onlook-dev/studio.svg?style=for-the-badge
[license-url]: https://github.com/onlook-dev/onlook/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/company/onlook-dev
[twitter-shield]: https://img.shields.io/badge/-Twitter-black?logo=x&colorB=555
[twitter-url]: https://x.com/onlookdev
[discord-shield]: https://img.shields.io/badge/-Discord-black?logo=discord&colorB=555
[discord-url]: https://discord.gg/hERDfFZCsH
[React.js]: https://img.shields.io/badge/react-%2320232a.svg?logo=react&logoColor=%2361DAFB
[React-url]: https://reactjs.org/
[TailwindCSS]: https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?logo=tailwind-css&logoColor=white
[Tailwind-url]: https://tailwindcss.com/
[Electron.js]: https://img.shields.io/badge/Electron-191970?logo=Electron&logoColor=white
[Electron-url]: https://www.electronjs.org/
[Vite.js]: https://img.shields.io/badge/vite-%23646CFF.svg?logo=vite&logoColor=white
[Vite-url]: https://vitejs.dev/
[product-screenshot]: assets/brand.png
[weave-shield]: https://img.shields.io/endpoint?url=https%3A%2F%2Fapp.workweave.ai%2Fapi%2Frepository%2Fbadge%2Forg_pWcXBHJo3Li2Te2Y4WkCPA33%2F820087727&cacheSeconds=3600&labelColor=#131313
[weave-url]: https://app.workweave.ai/reports/repository/org_pWcXBHJo3Li2Te2Y4WkCPA33/820087727