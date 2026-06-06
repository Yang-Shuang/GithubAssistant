# Open WebUI 👋

![GitHub stars](https://img.shields.io/github/stars/open-webui/open-webui?style=social)
![GitHub forks](https://img.shields.io/github/forks/open-webui/open-webui?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/open-webui/open-webui?style=social)
![GitHub repo size](https://img.shields.io/github/repo-size/open-webui/open-webui)
![GitHub language count](https://img.shields.io/github/languages/count/open-webui/open-webui)
![GitHub top language](https://img.shields.io/github/languages/top/open-webui/open-webui)
![GitHub last commit](https://img.shields.io/github/last-commit/open-webui/open-webui?color=red)
[![Discord](https://img.shields.io/badge/Discord-Open_WebUI-blue?logo=discord&logoColor=white)](https://discord.gg/5rJgQTnV4s)
[![](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=%23fe8e86)](https://github.com/sponsors/tjbck)

![Open WebUI Banner](./banner.png)

**Open WebUI 是一个[可扩展](https://docs.openwebui.com/features/extensibility/plugin)、功能丰富且用户友好的自托管 AI 平台，专为完全离线运行而设计。** 它支持多种 LLM 推理后端（如 **Ollama** 和 **OpenAI 兼容 API**），并内置 RAG 推理引擎，是一款强大的 AI 部署解决方案。

对开源 AI 充满热情？[加入我们 →](https://careers.openwebui.com/)

![Open WebUI Demo](./demo.png)

> [!TIP]  
> **正在寻找[企业版计划](https://docs.openwebui.com/enterprise)？** – **[立即联系我们的销售团队！](https://docs.openwebui.com/enterprise)**
>
> 获取**增强的功能**，包括**自定义主题与品牌标识**、**服务等级协议（SLA）支持**、**长期支持（LTS）版本**以及**更多！**

如需更多信息，请务必查阅我们的[Open WebUI 文档](https://docs.openwebui.com/)。

## Open WebUI 核心功能 ⭐

- 🚀 **轻松部署**：使用 Docker 或 Kubernetes（kubectl、kustomize 或 helm）无缝安装，提供无忧体验。支持带有 `:ollama` 和 `:cuda` 标签的镜像。

- 🤝 **Ollama/OpenAI API 集成**：无缝集成 OpenAI 兼容 API，与 Ollama 模型配合实现多样化对话。可自定义 OpenAI API 地址以连接 **LMStudio、GroqCloud、Mistral、OpenRouter 等**。

- 🛡️ **细粒度权限与用户组**：通过允许管理员创建详细的用户角色和权限，我们确保了一个安全的用户环境。这种细粒度控制不仅提升了安全性，还支持定制化的用户体验，培养用户的归属感与责任感。

- 📱 **响应式设计**：在台式机、笔记本和移动设备上享受无缝流畅的体验。

- 📱 **移动端渐进式网页应用（PWA）**：通过我们的 PWA 在移动设备上获得类原生应用体验，支持本地离线访问并提供无缝的用户界面。

- ✒️🔢 **完整的 Markdown 与 LaTeX 支持**：借助全面的 Markdown 和 LaTeX 功能，提升你的 LLM 交互体验。

- 🎤📹 **免提语音/视频通话**：通过集成的免提语音和视频通话功能实现无缝沟通。支持多种语音转文本服务（Local Whisper、OpenAI、Deepgram、Azure）和文本转语音引擎（Azure、ElevenLabs、OpenAI、Transformers、WebAPI），打造动态交互的聊天环境。

- 🛠️ **模型构建器**：通过 Web 界面轻松创建 Ollama 模型。可创建和添加自定义角色/智能体，定制聊天元素，并通过 [Open WebUI 社区](https://openwebui.com/) 集成无缝导入模型。

- 🐍 **原生 Python 函数调用工具**：在工具工作区内置代码编辑器支持，增强你的 LLM。通过“自带函数（BYOF）”机制，只需添加纯 Python 函数即可实现与 LLM 的无缝集成。

- 💾 **持久化工件存储**：内置键值对存储 API，支持日记、追踪器、排行榜和协作工具等功能。提供跨会话的个人与共享数据作用域。

- 📚 **本地 RAG 集成**：通过支持检索增强生成（RAG）的前沿功能，探索聊天交互的未来。可选配 9 种向量数据库及多种内容提取引擎（Tika、Docling、Document Intelligence、Mistral OCR、PaddleOCR-vl、外部加载器）。可将文档直接载入对话或添加到文档库中，在查询前使用 `#` 命令即可轻松调用。

- 🔍 **RAG 网络搜索**：使用 15 种以上的提供商执行网络搜索，包括 `SearXNG`、`Google PSE`、`Brave Search`、`Kagi`、`Mojeek`、`Tavily`、`Perplexity`、`serpstack`、`serper`、`Serply`、`DuckDuckGo`、`SearchApi`、`SerpApi`、`Bing`、`Jina`、`Exa`、`Sougou`、`Azure AI Search` 和 `Ollama Cloud`，并将结果直接注入你的聊天体验中。

- 🌐 **网页浏览能力**：使用 `#` 命令后接网址，即可将网站无缝集成到聊天体验中。该功能允许你将网页内容直接融入对话，提升交互的丰富性与深度。

- 🎨 **图像生成与编辑集成**：使用多种引擎创建和编辑图像，包括 OpenAI 的 DALL-E、Gemini、ComfyUI（本地）和 AUTOMATIC1111（本地），支持生成及基于提示词的编辑工作流。

- ⚙️ **多模型对话**：轻松同时与多个模型交互，发挥各自独特优势以获得最佳响应。通过并行调用多样化的模型集来增强你的体验。

- 🔐 **基于角色的访问控制（RBAC）**：通过受限权限确保访问安全；仅授权人员可访问你的 Ollama，且模型创建/拉取权限仅限管理员。

- 🗄️ **灵活的数据库与存储选项**：可选择 SQLite（支持可选加密）、PostgreSQL，或配置云存储后端（S3、Google Cloud Storage、Azure Blob Storage）以实现可扩展部署。

- 🔍 **高级向量数据库支持**：从 9 种向量数据库中任选，包括 ChromaDB、PGVector、Qdrant、Milvus、Elasticsearch、OpenSearch、Pinecone、S3Vector 和 Oracle 23ai，以实现最佳 RAG 性能。

- 🔐 **企业级认证**：全面支持 LDAP/Active Directory 集成、SCIM 2.0 自动化配置，以及通过可信头部的 SSO 和 OAuth 提供商。通过 SCIM 2.0 协议提供企业级用户与群组配置，支持与 Okta、Azure AD 和 Google Workspace 等身份提供商无缝集成，实现自动化的用户生命周期管理。

- ☁️ **云原生集成**：原生支持 Google Drive 和 OneDrive/SharePoint 文件选择器，实现从企业云存储无缝导入文档。

- 📊 **生产环境可观测性**：内置 OpenTelemetry 支持，涵盖链路追踪、指标和日志，可与现有可观测性栈结合实现全面监控。

- ⚖️ **水平可扩展性**：基于 Redis 的会话管理与 WebSocket 支持，适用于负载均衡器后的多工作进程及多节点部署。

- 🌐🌍 **多语言支持**：通过国际化（i18n）支持，以你偏好的语言体验 Open WebUI。欢迎加入我们扩展支持的语言！我们正积极寻求贡献者！

- 🧩 **Pipelines 与 Open WebUI 插件支持**：使用 [Pipelines 插件框架](https://github.com/open-webui/pipelines) 将自定义逻辑和 Python 库无缝集成到 Open WebUI。启动你的 Pipelines 实例，将 OpenAI URL 设置为 Pipelines URL，即可探索无限可能。[示例](https://github.com/open-webui/pipelines/tree/main/examples) 包括**函数调用**、用户**速率限制**以控制访问、使用 Langfuse 等工具进行**用量监控**、通过 LibreTranslate 实现**实时翻译**的多语言支持、**有害消息过滤**等更多功能。

- 🌟 **持续更新**：我们致力于通过定期更新、修复和新功能来不断完善 Open WebUI。

想了解 Open WebUI 的更多功能？请查阅我们的[Open WebUI 文档](https://docs.openwebui.com/features)获取全面概览！

---

我们衷心感谢各位赞助商的慷慨支持。你们的贡献帮助我们维护和改进项目，确保我们能继续为社区提供高质量的工作成果。非常感谢！

## 如何安装 🚀

### 通过 Python pip 安装 🐍

你可以通过 Python 包管理器 pip 安装 Open WebUI。在继续之前，请确保使用 **Python 3.11** 以避免兼容性问题。

1. **安装 Open WebUI**：
   打开终端并运行以下命令来安装 Open WebUI：

   ```bash
   pip install open-webui
   ```

2. **运行 Open WebUI**：
   安装完成后，你可以通过执行以下命令启动 Open WebUI：

   ```bash
   open-webui serve
   ```

这将启动 Open WebUI 服务器，你可通过 [http://localhost:8080](http://localhost:8080) 访问。

### 使用 Docker 快速开始 🐳

> [!NOTE]  
> **请注意**，在某些 Docker 环境中可能需要额外配置。如果遇到连接问题，我们的[Open WebUI 文档](https://docs.openwebui.com/)已为你准备好详细指南。

> [!WARNING]
> 使用 Docker 安装 Open WebUI 时，请务必在命令中包含 `-v open-webui:/app/backend/data`。此步骤至关重要，可确保数据库正确挂载并防止数据丢失。

> [!TIP]  
> 如果你希望将 Open WebUI 与 Ollama 或 CUDA 加速功能结合使用，建议使用我们带有 `:cuda` 或 `:ollama` 标签的官方镜像。要启用 CUDA，必须在你的 Linux/WSL 系统上安装 [Nvidia CUDA 容器工具包](https://docs.nvidia.com/dgx/nvidia-container-runtime-upgrade/)。

### 默认配置安装

- **如果 Ollama 在你的本地计算机上**，请使用以下命令：

  ```bash
  docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
  ```

- **如果 Ollama 位于不同的服务器上**，请使用以下命令：

  要连接到另一台服务器上的 Ollama，请将 `OLLAMA_BASE_URL` 更改为该服务器的地址：

  ```bash
  docker run -d -p 3000:8080 -e OLLAMA_BASE_URL=https://example.com -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
  ```

- **要以支持 Nvidia GPU 的方式运行 Open WebUI**，请使用以下命令：

  ```bash
  docker run -d -p 3000:8080 --gpus all --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:cuda
  ```

### 仅使用 OpenAI API 的安装

- **如果你仅使用 OpenAI API**，请使用以下命令：

  ```bash
  docker run -d -p 3000:8080 -e OPENAI_API_KEY=your_secret_key -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
  ```

### 安装集成 Ollama 的 Open WebUI

此安装方法使用单个容器镜像，将 Open WebUI 与 Ollama 捆绑在一起，允许通过单条命令完成精简部署。请根据你的硬件配置选择合适的命令：

- **支持 GPU**：
  利用 GPU 资源运行以下命令：

  ```bash
  docker run -d -p 3000:8080 --gpus=all -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
  ```

- **仅使用 CPU**：
  如果你不使用 GPU，请使用此命令：

  ```bash
  docker run -d -p 3000:8080 -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
  ```

两条命令均提供开箱即用的免配置安装体验，确保你能迅速启动 Open WebUI 和 Ollama。

安装完成后，你可通过 [http://localhost:3000](http://localhost:3000) 访问 Open WebUI。祝你使用愉快！😄

### 其他安装方法

我们提供多种安装替代方案，包括非 Docker 原生安装方法、Docker Compose、Kustomize 和 Helm。请访问我们的[Open WebUI 文档](https://docs.openwebui.com/getting-started/)或加入[Discord 社区](https://discord.gg/5rJgQTnV4s)获取全面指南。

### 故障排除

遇到连接问题？我们的[Open WebUI 文档故障排除指南](https://docs.openwebui.com/troubleshooting/)可助你解决。如需进一步帮助并加入活跃的社区，请访问[Open WebUI Discord](https://discord.gg/5rJgQTnV4s)。

#### Open WebUI：服务器连接错误

如果遇到连接问题，通常是因为 WebUI Docker 容器无法在容器内部访问位于 127.0.0.1:11434 (host.docker.internal:11434) 的 Ollama 服务器。请在 docker 命令中使用 `--network=host` 标志来解决此问题。注意端口会从 3000 变为 8080，访问链接将变为：`http://localhost:8080`。

**示例 Docker 命令**：

```bash
docker run -d --network=host -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

### 保持 Docker 安装为最新版本

请参阅[Open WebUI 文档](https://docs.openwebui.com/getting-started/updating)中的更新指南。

### 使用开发分支（Dev）🌙

> [!WARNING]
> `:dev` 分支包含最新的不稳定功能和更改。请自行承担风险使用，因为它可能包含错误或不完整的功能。

如果你想尝试最新的尖端功能且能接受偶尔的不稳定性，可以像这样使用 `:dev` 标签：

```bash
docker run -d -p 3000:8080 -v open-webui:/app/backend/data --name open-webui --add-host=host.docker.internal:host-gateway --restart always ghcr.io/open-webui/open-webui:dev
```

### 离线模式

如果你在离线环境中运行 Open WebUI，可以将环境变量 `HF_HUB_OFFLINE` 设置为 `1`，以防止尝试从互联网下载模型。

```bash
export HF_HUB_OFFLINE=1
```

## 下一步计划 🌟

在[Open WebUI 文档](https://docs.openwebui.com/roadmap/)中查看我们路线图上的即将推出的功能。

## 许可证 📜

本项目包含受多种许可证约束的代码。当前代码库包括在 Open WebUI 许可证下授权且附加保留“Open WebUI”品牌标识要求的组件，以及先前贡献者在其各自原始许可证下的代码。有关许可证变更的详细记录及各部分代码的适用条款，请参阅 [LICENSE_HISTORY](./LICENSE_HISTORY)。完整的最新许可详情请查看 [LICENSE](./LICENSE) 和 [LICENSE_HISTORY](./LICENSE_HISTORY) 文件。

## 支持 💬

如果你有任何问题、建议或需要帮助，请提交 Issue 或加入我们的
[Open WebUI Discord 社区](https://discord.gg/5rJgQTnV4s)与我们交流！🤝

## Star 历史

<a href="https://star-history.com/#open-webui/open-webui&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=open-webui/open-webui&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=open-webui/open-webui&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=open-webui/open-webui&type=Date" />
  </picture>
</a>

---

由 [Timothy Jaeryang Baek](https://github.com/tjbck) 创建 —— 让我们一起让 Open WebUI 更加出色！💪