![Banner image](https://user.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n - 面向技术团队的安全工作流自动化平台

n8n 是一款工作流自动化平台，让技术团队既能享受无代码的快速部署，又能获得编写代码的灵活性。凭借 400 多种集成、原生 AI 能力以及公平代码（fair-code）许可证，n8n 让你能够构建强大的自动化流程，同时完全掌控你的数据和部署环境。

![n8n.io - Screenshot](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-screenshot-readme.png)

## 核心能力

- **按需编写代码**：可编写 JavaScript/Python 代码、添加 npm 包，或使用可视化界面
- **原生 AI 平台**：基于 LangChain 构建 AI Agent 工作流，支持使用自有数据和模型
- **完全掌控**：通过公平代码许可证自行托管，或使用我们的 [云服务](https://app.n8n.cloud/login)
- **企业级就绪**：支持高级权限管理、单点登录（SSO）及物理隔离部署
- **活跃社区**：提供 400 多种集成和 900 多个开箱即用的 [模板](https://n8n.io/workflows)

## 快速开始

使用 [npx](https://docs.n8n.io/hosting/installation/npm/) 可立即体验 n8n（需安装 [Node.js](https://nodejs.org/en/)）：

```
npx n8n
```

或使用 [Docker](https://docs.n8n.io/hosting/installation/docker/) 进行部署：

```
docker volume create n8n_data
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

访问编辑器地址：http://localhost:5678

## 资源链接

- 📚 [文档](https://docs.n8n.io)
- 🔧 [400+ 集成](https://n8n.io/integrations)
- 💡 [示例工作流](https://n8n.io/workflows)
- 🤖 [AI 与 LangChain 指南](https://docs.n8n.io/advanced-ai/)
- 👥 [社区论坛](https://community.n8n.io)
- 📖 [社区教程](https://community.n8n.io/c/tutorials/28)

## 技术支持

需要帮助？我们的社区论坛是获取技术支持并与其它用户交流的绝佳场所：
[community.n8n.io](https://community.n8n.io)

## 许可证

n8n 采用 [公平代码（fair-code）模式](https://faircode.io)，基于 [可持续使用许可证](https://github.com/n8n-io/n8n/blob/master/LICENSE.md) 和 [n8n 企业许可证](https://github.com/n8n-io/n8n/blob/master/LICENSE_EE.md) 分发。

- **源码可见**：源代码始终公开透明
- **支持自托管**：可部署在任何环境
- **高度可扩展**：支持添加自定义节点和功能

如需更多功能与支持，请洽 [企业许可证](mailto:license@n8n.io)。

有关许可模式的更多信息，请参阅 [文档](https://docs.n8n.io/sustainable-use-license/)。

## 贡献指南

发现了 Bug 🐛 或有新功能想法 ✨？请查阅我们的 [贡献指南](https://github.com/n8n-io/n8n/blob/master/CONTRIBUTING.md)，获取环境配置指南与最佳实践。

## 加入我们

想要塑造自动化的未来？查看我们的 [招聘页面](https://n8n.io/careers)，加入我们吧！

## n8n 是什么意思？

**简短回答：** 意为“节点自动化”（nodemation），发音为 n-eight-n。

**详细解答：** “我经常被问到这个问题（比我预期的还要频繁），所以决定在这里统一回复。当初我为项目寻找免费域名时，很快发现所有想到的好名字都已经被注册了。最终我选择了 nodemation。其中‘node-’代表它使用节点视图（Node-View）并基于 Node.js 构建；‘-mation’取自 automation（自动化），这也是该项目旨在解决的问题。不过我觉得这个名字太长了，每次在 CLI 中敲这么长一串很不方便。于是我就把它缩写成了 n8n。” —— **Jan Oberhauser，n8n.io 创始人兼 CEO**