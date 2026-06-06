<picture>
  <img alt="Agent TARS Banner" src="./images/tars.png">
</picture>

<br/>

## 简介

英文 | [简体中文](./README.zh-CN.md)

[![](https://trendshift.io/api/badge/repositories/13584)](https://trendshift.io/repositories/13584)

<b>TARS<sup>\*</sup></b> 是一个多模态 AI Agent 技术栈，目前包含两个项目：[Agent TARS](#agent-tars) 和 [UI-TARS-desktop](#ui-tars-desktop)：

<table>
  <thead>
    <tr>
      <th width="50%" align="center"><a href="#agent-tars">Agent TARS</a></th>
      <th width="50%" align="center"><a href="#ui-tars-desktop">UI-TARS-desktop</a></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">
        <video src="https://github.com/user-attachments/assets/c9489936-afdc-4d12-adda-d4b90d2a869d" width="50%"></video>
      </td>
      <td align="center">
        <video src="https://github.com/user-attachments/assets/e0914ce9-ad33-494b-bdec-0c25c1b01a27" width="50%"></video>
      </td>
    </tr>
    <tr>
      <td align="left">
        <b>Agent TARS</b> 是一款通用多模态 AI Agent 技术栈，它将 GUI Agent（图形用户界面智能体）和视觉能力带入你的终端、计算机、浏览器及各类产品中。
        <br>
        <br>
        它主要提供 <a href="https://agent-tars.com/guide/basic/cli.html" target="_blank">CLI</a> 和 <a href="https://agent-tars.com/guide/basic/web-ui.html" target="_blank">Web UI</a> 供用户使用。
        它旨在通过前沿的多模态大语言模型（LLMs）与各类真实世界 <a href="https://agent-tars.com/guide/basic/mcp.html" target="_blank">MCP</a> 工具的无缝集成，提供更接近人类完成任务的工作流。
      </td>
      <td align="left">
        <b>UI-TARS Desktop</b> 是一款桌面应用程序，基于 <a href="https://github.com/bytedance/UI-TARS" target="_blank">UI-TARS</a> 模型提供原生 GUI Agent。
        <br>
        <br>
        它主要提供本地（<a href="https://github.com/bytedance/UI-TARS-desktop/blob/main/docs/quick-start.md#get-model-and-run-local-operator" target="_blank">local</a>）和远程（<a href="https://github.com/bytedance/UI-TARS-desktop/blob/main/docs/quick-start.md#run-remote-operator" target="_blank">remote</a>）的计算机及浏览器操作符。
      </td>
    </tr>
  </tbody>
</table>

## 目录

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [最新动态](#news)
- [Agent TARS](#agent-tars)
  - [案例展示](#showcase)
  - [核心特性](#core-features)
  - [快速入门](#quick-start)
  - [文档中心](#documentation)
- [UI-TARS Desktop](#ui-tars-desktop)
  - [案例展示](#showcase-1)
  - [功能特性](#features)
  - [快速入门](#quick-start-1)
- [贡献指南](#contributing)
- [开源许可](#license)
- [引用信息](#citation)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## 最新动态

- **\[2025-11-05\]** 🎉 我们很高兴宣布发布 [Agent TARS CLI v0.3.0](https://github.com/bytedance/UI-TARS-desktop/releases/tag/v0.3.0)！此版本为多种工具带来了流式支持（Shell 命令、多文件结构化展示），运行时设置包含工具调用和深度思考的计时统计，以及用于数据流跟踪与调试的事件流查看器。此外，它还独家支持 [AIO agent Sandbox](https://github.com/agent-infra/sandbox) 作为隔离的一体化工具执行环境。
- **\[2025-06-25\]** 我们发布了 Agent TARS Beta 和 Agent TARS CLI —— [介绍 Agent TARS Beta](https://agent-tars.com/blog/2025-06-25-introducing-agent-tars-beta.html)，这是一款多模态 AI Agent，旨在通过丰富的多模态能力（如 GUI Agent、视觉识别）与各类真实世界工具的无缝集成，探索更接近人类完成任务的工作形式。
- **\[2025-06-12\]** - 🎁 我们激动地宣布 UI-TARS Desktop v0.2.0 正式发布！本次更新带来两大全新强大功能：**远程计算机操作符**和**远程浏览器操作符**——完全免费。无需任何配置：只需点击即可远程控制任意计算机或浏览器，体验前所未有的便捷与智能。
- **\[2025-04-17\]** - 🎉 我们很高兴宣布全新 UI-TARS Desktop v0.1.0 应用发布，采用重新设计的 Agent UI。该应用优化了计算机使用体验，新增浏览器操作功能，并支持 [高级 UI-TARS-1.5 模型](https://seed-tars.com/1.5) 以提升性能与控制精度。
- **\[2025-02-20\]** - 📦 发布 [UI TARS SDK](./docs/sdk.md)，这是一款用于构建 GUI 自动化 Agent 的强大跨平台工具包。
- **\[2025-01-23\]** - 🚀 我们更新了中文版 **[云部署](./docs/deployment.md#cloud-deployment)** 章节：[GUI 模型部署教程](https://bytedance.sg.larkoffice.com/docx/TCcudYwyIox5vyxiSDLlgIsTgWf#U94rdCxzBoJMLex38NPlHL21gNb)，补充了关于 ModelScope 平台的新信息。你现在可以使用 ModelScope 平台进行部署。

<br>

## Agent TARS

<p>
    <a href="https://npmjs.com/package/@agent-tars/cli?activeTab=readme"><img src="https://img.shields.io/npm/v/@agent-tars/cli?style=for-the-badge&colorA=1a1a2e&colorB=3B82F6&logo=npm&logoColor=white" alt="npm version" /></a>
    <a href="https://npmcharts.com/compare/@agent-tars/cli?minimal=true"><img src="https://img.shields.io/npm/dm/@agent-tars/cli.svg?style=for-the-badge&colorA=1a1a2e&colorB=0EA5E9&logo=npm&logoColor=white" alt="downloads" /></a>
    <a href="https://nodejs.org/en/about/previous-releases"><img src="https://img.shields.io/node/v/@agent-tars/cli.svg?style=for-the-badge&colorA=1a1a2e&colorB=06B6D4&logo=node.js&logoColor=white" alt="node version"></a>
    <a href="https://discord.gg/HnKcSBgTVx"><img src="https://img.shields.io/badge/Discord-Join%20Community-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord Community" /></a>
    <a href="https://twitter.com/agent_tars"><img src="https://img.shields.io/badge/Twitter-Follow%20%40agent__tars-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="Official Twitter" /></a>
    <a href="https://applink.larkoffice.com/client/chat/chatter/add_by_link?link_token=deen76f4-ea3c-4964-93a3-78f126f39651"><img src="https://img.shields.io/badge/飞书群-加入交流群-00D4AA?style=for-the-badge&logo=lark&logoColor=white" alt="飞书交流群" /></a>
    <a href="https://deepwiki.com/bytedance/UI-TARS-desktop"><img src="https://img.shields.io/badge/DeepWiki-Ask%20AI-8B5CF6?style=for-the-badge&logo=gitbook&logoColor=white" alt="Ask DeepWiki" /></a>
</p>

<b>Agent TARS</b> 是一款通用多模态 AI Agent 技术栈，它将 GUI Agent（图形用户界面智能体）和视觉能力带入你的终端、计算机、浏览器及各类产品中。<br><br>它主要提供 <a href="https://agent-tars.com/guide/basic/cli.html" target="_blank">CLI</a> 和 <a href="https://agent-tars.com/guide/basic/web-ui.html" target="_blank">Web UI</a> 供用户使用。
它旨在通过前沿的多模态大语言模型（LLMs）与各类真实世界 <a href="https://agent-tars.com/guide/basic/mcp.html" target="_blank">MCP</a> 工具的无缝集成，提供更接近人类完成任务的工作流。

### 案例展示

```
Please help me book the earliest flight from San Jose to New York on September 1st and the last return flight on September 6th on Priceline
```

https://github.com/user-attachments/assets/772b0eef-aef7-4ab9-8cb0-9611820539d8

<br>

<table>
  <thead>
    <tr>
      <th width="50%" align="center">预订酒店</th>
      <th width="50%" align="center">借助额外 MCP Server 生成图表</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">
        <video src="https://github.com/user-attachments/assets/c9489936-afdc-4d12-adda-d4b90d2a869d" width="50%"></video>
      </td>
      <td align="center">
        <video src="https://github.com/user-attachments/assets/a9fd72d0-01bb-4233-aa27-ca95194bbce9" width="50%"></video>
      </td>
    </tr>
    <tr>
      <td align="left">
        <b>指令：</b><i>我将于9月1日至9月6日在洛杉矶，预算为5,000美元。请帮我在booking.com上预订距离机场最近的丽思卡尔顿酒店，并为我整理一份交通指南。</i>
      </td>
      <td align="left">
        <b>指令：</b><i>帮我画一张杭州一个月的天气图表。</i>
      </td>
    </tr>
  </tbody>
</table>

更多使用案例，请查看 [#842](https://github.com/bytedance/UI-TARS-desktop/issues/842)。

### 核心特性

- 🖱️ **开箱即用的命令行工具（CLI）** - 支持带界面的 <a href="https://agent-tars.com/guide/basic/web-ui.html">Web UI</a> 和无头模式下的 <a href="https://agent-tars.com/guide/advanced/server.html">服务器</a> <a href="https://agent-tars.com/guide/basic/cli.html">执行方式</a>。
- 🌐 **混合浏览器智能体** - 使用 <a href="https://agent-tars.com/guide/basic/browser.html#visual-grounding">GUI Agent</a>、<a href="https://agent-tars.com/guide/basic/browser.html#dom">DOM</a> 或混合策略来控制浏览器。
- 🔄 **事件流（Event Stream）** - 基于协议驱动的事件流推动 <a href="https://agent-tars.com/beta#context-engineering">上下文工程</a> 和 <a href="https://agent-tars.com/blog/2025-06-25-introducing-agent-tars-beta.html#easy-to-build-applications">Agent UI</a> 的发展。
- 🧰 **MCP 集成** - 核心架构基于 MCP 构建，并支持挂载 <a href="https://agent-tars.com/guide/basic/mcp.html">MCP Server</a> 以连接真实世界工具。

### 快速入门

<img alt="Agent TARS CLI" src="https://agent-tars.com/agent-tars-cli.png">

```bash
# Launch with `npx`.
npx @agent-tars/cli@latest

# Install globally, required Node.js >= 22
npm install @agent-tars/cli@latest -g

# Run with your preferred model provider
agent-tars --provider volcengine --model doubao-1-5-thinking-vision-pro-250428 --apiKey your-api-key
agent-tars --provider anthropic --model claude-3-7-sonnet-latest --apiKey your-api-key
```

访问详细的 <a href="https://agent-tars.com/guide/get-started/quick-start.html">快速入门</a> 指南以获取完整设置说明。

### 文档中心

> 🌟 **探索 Agent TARS 宇宙** 🌟

<table>
  <thead>
    <tr>
      <th width="20%" align="center">分类</th>
      <th width="30%" align="center">资源链接</th>
      <th width="50%" align="left">描述</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">🏠 <strong>核心枢纽</strong></td>
      <td align="center">
        <a href="https://agent-tars.com">
          <img src="https://img.shields.io/badge/Visit-Website-4F46E5?style=for-the-badge&logo=globe&logoColor=white" alt="Website" />
        </a>
      </td>
      <td align="left">通往 Agent TARS 生态系统的门户</td>
    </tr>
      <tr>
      <td align="center">📚 <strong>快速入门</strong></td>
      <td align="center">
        <a href="https://agent-tars.com/guide/get-started/quick-start.html">
          <img src="https://img.shields.io/badge/Get-Started-06B6D4?style=for-the-badge&logo=rocket&logoColor=white" alt="Quick Start" />
        </a>
      </td>
      <td align="left">5分钟快速上手</td>
    </tr>
    <tr>
      <td align="center">🚀 <strong>最新动态</strong></td>
      <td align="center">
        <a href="https://agent-tars.com/beta">
          <img src="https://img.shields.io/badge/Read-Blog-F59E0B?style=for-the-badge&logo=rss&logoColor=white" alt="Blog" />
        </a>
      </td>
      <td align="left">探索前沿功能与愿景</td>
    </tr>
    <tr>
      <td align="center">🛠️ <strong>开发者专区</strong></td>
      <td align="center">
        <a href="https://agent-tars.com/guide/get-started/introduction.html">
          <img src="https://img.shields.io/badge/View-Docs-10B981?style=for-the-badge&logo=gitbook&logoColor=white" alt="Docs" />
        </a>
      </td>
      <td align="left">掌握所有命令与特性</td>
    </tr>
    <tr>
      <td align="center">🎯 <strong>案例展示</strong></td>
      <td align="center">
        <a href="https://github.com/bytedance/UI-TARS-desktop/issues/842">
          <img src="https://img.shields.io/badge/View-Examples-8B5CF6?style=for-the-badge&logo=github&logoColor=white" alt="Examples" />
        </a>
      </td>
      <td align="left">浏览官方与社区构建的使用案例</td>
    </tr>
    <tr>
      <td align="center">🔧 <strong>参考文档</strong></td>
      <td align="center">
        <a href="https://agent-tars.com/api/">
          <img src="https://img.shields.io/badge/API-Reference-EF4444?style=for-the-badge&logo=book&logoColor=white" alt="API" />
        </a>
      </td>
      <td align="left">完整的技术参考资料</td>
    </tr>
  </tbody>
</table>

<br/>
<br/>
<br/>

## UI-TARS Desktop

<p align="center">
  <img alt="UI-TARS" width="260" src="./apps/ui-tars/resources/icon.png">
</p>

UI-TARS Desktop 是一款面向本地计算机的原生 GUI Agent，由 <a href="https://github.com/bytedance/UI-TARS">UI-TARS</a> 和 Seed-1.5-VL/1.6 系列模型驱动。

<div align="center">
<p>
        &nbsp&nbsp 📑 <a href="https://arxiv.org/abs/2501.12326">论文</a> &nbsp&nbsp
        | 🤗 <a href="https://huggingface.co/ByteDance-Seed/UI-TARS-1.5-7B">Hugging Face 模型</a>&nbsp&nbsp
        | &nbsp&nbsp🫨 <a href="https://discord.gg/pTXwYVjfcs">Discord</a>&nbsp&nbsp
        | &nbsp&nbsp🤖 <a href="https://www.modelscope.cn/collections/UI-TARS-bccb56fa1ef640">ModelScope</a>&nbsp&nbsp
<br>
🖥️ 桌面应用 &nbsp&nbsp
| &nbsp&nbsp 👓 <a href="https://github.com/web-infra-dev/midscene">Midscene（浏览器中使用）</a> &nbsp&nbsp
</p>

</div>

### 案例展示

<!-- // FIXME: Choose only two demo, one local computer and one remote computer showcase. -->

|                                                          Instruction                                                           |                                                Local Operator                                                |                                               Remote Operator                                                |
| :----------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: |
| 请帮我在 VS Code 设置中开启自动保存功能，并将自动保存操作的延迟设置为 500 毫秒。 | <video src="https://github.com/user-attachments/assets/e0914ce9-ad33-494b-bdec-0c25c1b01a27" height="300" /> | <video src="https://github.com/user-attachments/assets/01e49b69-7070-46c8-b3e3-2aaaaec71800" height="300" /> |
|                    你能帮我查看一下 GitHub 上 UI-TARS-Desktop 项目的最新开放 Issue 吗？                     | <video src="https://github.com/user-attachments/assets/3d159f54-d24a-4268-96c0-e149607e9199" height="300" /> | <video src="https://github.com/user-attachments/assets/072fb72d-7394-4bfa-95f5-4736e29f7e58" height="300" /> |

### 功能特性

- 🤖 基于视觉语言模型的自然语言控制
- 🖥️ 支持截图与视觉识别
- 🎯 精确的鼠标和键盘控制
- 💻 跨平台支持（Windows/macOS/浏览器）
- 🔄 实时反馈与状态显示
- 🔐 私密安全 - 完全本地处理

### 快速入门

请参阅 <a href="./docs/quick-start.md">快速入门</a>。

## 贡献指南

请参阅 <a href="./CONTRIBUTING.md">CONTRIBUTING.md</a>。

## 开源许可

本项目采用 Apache License 2.0 许可证授权。

## 引用信息

如果你的研究觉得我们的论文和代码有用，请考虑给一个 Star :star: 并引用 :pencil：

```BibTeX
@article{qin2025ui,
  title={UI-TARS: Pioneering Automated GUI Interaction with Native Agents},
  author={Qin, Yujia and Ye, Yining and Fang, Junjie and Wang, Haoming and Liang, Shihao and Tian, Shizuo and Zhang, Junda and Li, Jiahao and Li, Yunxin and Huang, Shijue and others},
  journal={arXiv preprint arXiv:2501.12326},
  year={2025}
}
```