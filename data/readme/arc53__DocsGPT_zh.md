<h1 align="center">
  DocsGPT  🦖
</h1>

<p align="center">
  <strong>面向智能体、助手与企业搜索的私有 AI</strong>
</p>

<p align="left">
  <strong><a href="https://www.docsgpt.cloud/">DocsGPT</a></strong> 是一款开源 AI 平台，用于构建智能体与助手。核心功能包括 Agent Builder、深度研究工具、文档分析（支持 PDF、Office、网页内容与音频）、多模型支持（可选择提供商或本地运行），以及为智能体提供可执行工具和集成的丰富 API 连接能力。可在任意环境部署，完全掌控隐私安全。
</p>

<div align="center">
  
  <a href="https://github.com/arc53/DocsGPT">![link to main GitHub showing Stars number](https://img.shields.io/github/stars/arc53/docsgpt?style=social)</a>
  <a href="https://github.com/arc53/DocsGPT">![link to main GitHub showing Forks number](https://img.shields.io/github/forks/arc53/docsgpt?style=social)</a>
  <a href="https://github.com/arc53/DocsGPT/blob/main/LICENSE">![link to license file](https://img.shields.io/github/license/arc53/docsgpt)</a>
  <a href="https://www.bestpractices.dev/projects/9907"><img src="https://www.bestpractices.dev/projects/9907/badge"></a>
  <a href="https://discord.gg/vN7YFfdMpj">![link to discord](https://img.shields.io/discord/1070046503302877216)</a>
  <a href="https://x.com/docsgptai">![X (formerly Twitter) URL](https://img.shields.io/twitter/follow/docsgptai)</a>

<a href="https://docs.docsgpt.cloud/quickstart">⚡️ 快速开始</a> • <a href="https://app.docsgpt.cloud/">☁️ 云端版本</a> • <a href="https://discord.gg/vN7YFfdMpj">💬 Discord</a>
<br>
<a href="https://docs.docsgpt.cloud/">📖 文档</a> • <a href="https://github.com/arc53/DocsGPT/blob/main/CONTRIBUTING.md">👫 贡献指南</a> • <a href="https://blog.docsgpt.cloud/">🗞 博客</a>
<br>

</div>


<div align="center">
  <br>
<img src="https://d3dg1063dc54p9.cloudfront.net/videos/demo-26.gif" alt="video-example-of-docs-gpt" width="800" height="480">
</div>
<h3 align="left">
  <strong>核心功能：</strong>
</h3>
<ul align="left">
    <li><strong>🗂️ 广泛的格式支持：</strong>读取 PDF、DOCX、CSV、XLSX、EPUB、MD、RST、HTML、MDX、JSON、PPTX、图片，以及 MP3、WAV、M4A、OGG 和 WebM 等音频文件。</li>
    <li><strong>🎙️ 语音工作流：</strong>将语音输入录制到聊天中，在后端转录音频，并将会议录音或语音备忘作为可搜索的知识库内容导入。</li>
    <li><strong>🌐 网页与数据集成：</strong>支持从 URL、站点地图（Sitemap）、Reddit、GitHub 及网络爬虫中摄取数据。</li>
    <li><strong>✅ 可靠的答案：</strong>获取准确且无幻觉的回复，源引用可在简洁的用户界面中查看。</li>
    <li><strong>🔑 简化的 API 密钥管理：</strong>生成与你的设置、文档和模型关联的密钥，简化聊天机器人及集成环境的配置。</li>
    <li><strong>🔗 可执行工具链：</strong>连接 API、工具和第三方服务，以启用大语言模型（LLM）的实际行动能力。</li>
    <li><strong>🧩 预置集成组件：</strong>使用现成的 HTML/React 聊天小部件、搜索工具、Discord/Telegram 机器人等。</li>
    <li><strong>🔌 灵活的部署方式：</strong>兼容主流大语言模型（OpenAI、Google、Anthropic）及本地模型（Ollama、llama_cpp）。</li>
    <li><strong>🏢 安全且可扩展：</strong>支持 Kubernetes，可在私有环境中安全运行，专为企业级可靠性设计。</li>
</ul>

## 路线图
- [x] 带条件节点的智能体工作流构建器 ( February 2026 )
- [x] SharePoint 与 Confluence 连接器 ( March – April 2026 )
- [x] 研究模式 ( March 2026 )
- [x] 用户数据迁移至 PostgreSQL ( April 2026 )
- [x] OpenTelemetry 可观测性支持 ( April 2026 )
- [x] 自带模型（Bring Your Own Model, BYOM）( April 2026 )
- [ ] 智能体定时调度（基于 RedBeat）( Q2 2026 )

你可以在[此处](https://github.com/orgs/arc53/projects/2)查看完整路线图。欢迎随时提交贡献或创建 Issue，这将帮助我们持续改进 DocsGPT！

### 生产环境支持 / 企业帮助：

我们非常乐意在您将 DocsGPT 部署到生产环境时提供个性化支持。

[获取演示 :wave:](https://www.docsgpt.cloud/contact)⁠

[发送邮件 :email:](mailto:support@docsgpt.cloud?subject=DocsGPT%20support%2Fsolutions)

## 加入灯塔计划 🌟

面向所有开发者与生成式 AI（GenAI）创新者！**DocsGPT 灯塔计划**旨在连接在实际场景中积极部署或扩展 DocsGPT 的技术负责人。你将直接与我们的团队协作，共同规划产品路线图、获取优先技术支持，并利用独家社区洞察构建企业级解决方案。

[了解更多并申请 →](https://docs.google.com/forms/d/1KAADiJinUJ8EMQyfTXUIGyFbqINNClNR3jBNWq7DgTE)

## 快速开始

> [!Note]
> 请确保你已安装 [Docker](https://docs.docker.com/engine/install/)

更详细的[快速开始](https://docs.docsgpt.cloud/quickstart)指南请参阅我们的文档

1. **克隆代码仓库：**

   ```bash
   git clone https://github.com/arc53/DocsGPT.git
   cd DocsGPT
   ```

**适用于 macOS 和 Linux：**

2. **运行安装脚本：**

   ```bash
   ./setup.sh
   ```

**适用于 Windows：**

2. **运行 PowerShell 安装脚本：**

   ```powershell
   PowerShell -ExecutionPolicy Bypass -File .\setup.ps1
   ```

任一脚本都会引导你完成 DocsGPT 的配置。提供五种选项：使用公共 API、本地运行、连接本地推理引擎、使用云端 API 提供商，或本地构建 Docker 镜像。脚本将根据你的选择自动配置 `.env` 文件并处理必要的下载与安装。

**访问 http://localhost:5173/**

要停止 DocsGPT，请在 `DocsGPT` 目录下打开终端并运行：

```bash
docker compose -f deployment/docker-compose.yaml down
```

（或使用运行安装脚本后显示的特定 `docker compose down` 命令）。

> [!Note]
> 如需开发环境配置指南，请参阅[开发环境指南](https://docs.docsgpt.cloud/Deploying/Development-Environment)。

## 贡献指南

有关如何参与贡献的详细信息，请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 文件。我们欢迎提交 Issue、提问以及 Pull Request。

## 架构

![Architecture chart](https://github.com/user-attachments/assets/fc6a7841-ddfc-45e6-b5a0-d05fe648cbe2)

## 项目结构

- Application - Flask 应用（主应用程序）。
- Extensions - 扩展组件，如 React 小部件或 Discord 机器人。
- Frontend - 前端使用 <a href="https://vitejs.dev/">Vite</a> 和 <a href="https://react.dev/">React</a>。
- Scripts - 杂项脚本。

## 行为准则

作为成员、贡献者与领导者，我们承诺为所有人提供一个免受骚扰的社区环境，无论其年龄、体型、显性或隐性残疾状况、种族、性别特征、性别认同与表达、经验水平、教育背景、社会经济地位、国籍、个人外貌、宗教信仰或性取向如何。有关更多参与信息，请参阅 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) 文件。

## 感谢我们的贡献者 ⚡

<a href="https://github.com/arc53/DocsGPT/graphs/contributors" alt="View Contributors">
  <img src="https://contrib.rocks/image?repo=arc53/DocsGPT" alt="Contributors" />
</a>

## 许可证

源代码采用 [MIT](https://opensource.org/license/mit/) 许可证，详见 [LICENSE](LICENSE) 文件。

## 本项目由以下合作伙伴支持：

<p>
  <a href="https://www.digitalocean.com/?utm_medium=opensource&utm_source=DocsGPT">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>
<p>
  <a href="https://get.neon.com/docsgpt">
    <img width="201" alt="color" src="https://github.com/user-attachments/assets/7d9813b7-0e6d-403f-b5af-68af066b326f" />
  </a>
  
</p>