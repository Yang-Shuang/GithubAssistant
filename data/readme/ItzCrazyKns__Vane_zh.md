# Vane 🔍

[![GitHub Repo stars](https://img.shields.io/github/stars/ItzCrazyKns/Vane?style=social)](https://github.com/ItzCrazyKns/Vane/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ItzCrazyKns/Vane?style=social)](https://github.com/ItzCrazyKns/Vane/network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/ItzCrazyKns/Vane?style=social)](https://github.com/ItzCrazyKns/Vane/watchers)
[![Docker Pulls](https://img.shields.io/docker/pulls/itzcrazykns1337/vane?color=blue)](https://hub.docker.com/r/itzcrazykns1337/vane)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/ItzCrazyKns/Vane/blob/master/LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/ItzCrazyKns/Vane?color=green)](https://github.com/ItzCrazyKns/Vane/commits/master)
[![Discord](https://dcbadge.limes.pink/api/server/26aArMy8tT?style=flat)](https://discord.gg/26aArMy8tT)

Vane 是一款**注重隐私的 AI 问答引擎**，完全运行在你的本地硬件上。它将互联网的海量知识与对**本地 LLM**（Ollama）及云服务提供商（OpenAI、Claude、Groq）的支持相结合，在确保搜索完全私密的同时，提供带有**引用来源**的准确答案。

![preview](.assets/vane-screenshot.png)

想了解其架构和运行原理？你可以在[这里](https://github.com/ItzCrazyKns/Vane/tree/master/docs/architecture/README.md)阅读。

## ✨ 功能特性

🤖 **支持所有主流 AI 提供商** - 通过 Ollama 使用本地 LLM，或连接 OpenAI、Anthropic Claude、Google Gemini、Groq 等。根据你的需求自由搭配模型。

⚡ **智能搜索模式** - 需要快速答案时选择极速模式（Speed Mode），日常搜索选择均衡模式（Balanced Mode），深度研究则选择质量模式（Quality Mode）。

🧭 **自选数据来源** - 搜索网页、讨论区或学术论文。更多来源和集成正在开发中。

🧩 **小组件（Widgets）** - 当相关时自动弹出的实用 UI 卡片，例如天气、计算器、股票价格及其他快捷查询。

🔍 **基于 SearxNG 的网页搜索** - 访问多个搜索引擎的同时保护你的身份隐私。即将支持 Tavily 和 Exa，以提供更佳结果。

📷 **图片和视频搜索** - 在文本结果之外查找视觉内容。搜索不再局限于文章。

📄 **文件上传** - 上传文档并向它提问。PDF、文本文档、图片，Vane 都能理解。

🌐 **指定域名搜索** - 当你明确目标网站时，可将搜索限制在特定域名下。非常适合技术文档或学术论文检索。

💡 **智能建议** - 输入时获取智能搜索建议，帮助你构建更精准的查询语句。

📚 **发现（Discover）** - 浏览全天有趣的文章和热门内容。无需主动搜索即可保持资讯更新。

🕒 **搜索历史** - 所有搜索记录均本地保存，随时可回顾你的探索成果。研究数据永不丢失。

✨ **更多功能即将上线** - 我们正根据社区反馈积极开发新功能。加入我们的 Discord 帮助塑造 Vane 的未来！

## Sponsors

Vane 的开发得益于赞助商的慷慨支持。他们的贡献有助于保持本项目免费、开源且对所有人开放。

<div align="center">
  
  
<a href="https://www.warp.dev/perplexica">
  <img alt="Warp Terminal" src=".assets/sponsers/warp.png" width="100%">
</a>

### **✨ [尝试 Warp - AI 驱动终端 →](https://www.warp.dev/vane)**

Warp 正通过 AI 功能、现代 UX 和极速性能革新开发工作流。被全球顶尖公司的开发者广泛使用。

</div>

---

同时感谢以下合作伙伴的慷慨支持：

<table>
  <tr>
    <td width="100" align="center">
      <a href="https://dashboard.exa.ai" target="_blank">
        <img src=".assets/sponsers/exa.png" alt="Exa" width="80" height="80" style="border-radius: .75rem;" />
      </a>
    </td>
    <td>
      <a href="https://dashboard.exa.ai">Exa</a> • 专为大语言模型打造的完美网页搜索 API - 提供网页搜索、爬虫、深度研究和问答功能
    </td>
  </tr>
</table>

## Installation

安装 Vane 主要有两种方式：使用 Docker 和不用 Docker。强烈推荐使用 Docker。

### Getting Started with Docker (Recommended)

Vane 可通过 Docker 轻松运行。只需执行以下命令：

```bash
docker run -d -p 3000:3000 -v vane-data:/home/vane/data --name vane itzcrazykns1337/vane:latest
```

此命令将拉取并启动内置 SearxNG 搜索引擎的 Vane 容器。运行后，打开浏览器访问 http://localhost:3000。随后你可以在设置界面直接配置你的选项（API 密钥、模型等）。

**Note**: 该镜像已同时包含 Vane 和 SearxNG，因此无需额外配置。`-v` 参数用于创建持久化卷以保存数据和上传的文件。

#### Using Vane with Your Own SearxNG Instance

如果你已经运行了 SearxNG，可以使用 Vane 的精简版（slim）：

```bash
docker run -d -p 3000:3000 -e SEARXNG_API_URL=http://your-searxng-url:8080 -v vane-data:/home/vane/data --name vane itzcrazykns1337/vane:slim-latest
```

**Important**: 请确保你的 SearxNG 实例已配置：

- JSON format enabled in the settings -> 设置中启用了 JSON 格式输出
- Wolfram Alpha search engine enabled -> 启用了 Wolfram Alpha 搜索引擎

将 `http://your-searxng-url:8080` 替换为你的实际 SearxNG URL。然后在 http://localhost:3000 的设置界面配置 AI 提供商选项。

#### Advanced Setup (Building from Source)

如果你偏好从源码构建或需要更多控制权：

1. Ensure Docker is installed and running on your system. -> 确保你的系统已安装并运行 Docker。
2. Clone the Vane repository:

   ```bash
   git clone https://github.com/ItzCrazyKns/Vane.git
   ```

3. After cloning, navigate to the directory containing the project files. -> 克隆完成后，进入包含项目文件的目录。

4. Build and run using Docker:

   ```bash
   docker build -t vane .
   docker run -d -p 3000:3000 -v vane-data:/home/vane/data --name vane vane
   ```

5. Access Vane at http://localhost:3000 and configure your settings in the setup screen. -> 访问 http://localhost:3000，并在设置界面配置你的选项。

**Note**: After the containers are built, you can start Vane directly from Docker without having to open a terminal. -> **注意**：容器构建完成后，你可以直接在 Docker 中启动 Vane，无需打开终端。

### Non-Docker Installation

1. Install SearXNG and allow `JSON` format in the SearXNG settings. Make sure Wolfram Alpha search engine is also enabled. -> 安装 SearXNG，并在设置中允许 `JSON` 格式输出。确保也启用了 Wolfram Alpha 搜索引擎。
2. Clone the repository:

   ```bash
   git clone https://github.com/ItzCrazyKns/Vane.git
   cd Vane
   ```

3. Install dependencies:

   ```bash
   npm i
   ```

4. Build the application:

   ```bash
   npm run build
   ```

5. Start the application:

   ```bash
   npm run start
   ```

6. Open your browser and navigate to http://localhost:3000 to complete the setup and configure your settings (API keys, models, SearxNG URL, etc.) in the setup screen. -> 打开浏览器访问 http://localhost:3000，完成设置并在配置界面中调整你的选项（API 密钥、模型、SearxNG URL 等）。

**Note**: Using Docker is recommended as it simplifies the setup process, especially for managing environment variables and dependencies. -> **注意**：推荐使用 Docker，因为它能简化安装流程，尤其是在管理环境变量和依赖项方面。

有关更新等操作更多信息，请参阅[安装文档](https://github.com/ItzCrazyKns/Vane/tree/master/docs/installation)。

### Troubleshooting

#### Local OpenAI-API-Compliant Servers

如果 Vane 提示你未配置任何聊天模型提供商，请确保：

1. Your server is running on `0.0.0.0` (not `127.0.0.1`) and on the same port you put in the API URL. -> 你的服务器正在 `0.0.0.0`（而非 `127.0.0.1`）上运行，且端口号与 API URL 中填写的一致。
2. You have specified the correct model name loaded by your local LLM server. -> 你已正确指定了本地 LLM 服务器加载的模型名称。
3. You have specified the correct API key, or if one is not defined, you have put _something_ in the API key field and not left it empty. -> 你已输入正确的 API 密钥；如果未定义密钥，请在 API 密钥字段中填写任意内容（切勿留空）。

#### Ollama Connection Errors

如果遇到 Ollama 连接错误，通常是因为后端无法连接到 Ollama 的 API。你可以通过以下方式解决：

1. **Check your Ollama API URL:** Ensure that the API URL is correctly set in the settings menu. -> **检查你的 Ollama API URL**：确保在设置菜单中正确设置了 API URL。
2. **Update API URL Based on OS:** -> **根据操作系统更新 API URL：**

   - **Windows:** Use `http://host.docker.internal:11434` -> - **Windows**：使用 `http://host.docker.internal:11434`
   - **Mac:** Use `http://host.docker.internal:11434` -> - **Mac**：使用 `http://host.docker.internal:11434`
   - **Linux:** Use `http://<private_ip_of_host>:11434` -> - **Linux**：使用 `http://<主机私有IP>:11434`

   Adjust the port number if you're using a different one. -> 如果你使用了其他端口，请相应调整。

3. **Linux Users - Expose Ollama to Network:** -> **Linux 用户 - 将 Ollama 暴露至网络：**

   - Inside `/etc/systemd/system/ollama.service`, you need to add `Environment="OLLAMA_HOST=0.0.0.0:11434"`. (Change the port number if you are using a different one.) Then reload the systemd manager configuration with `systemctl daemon-reload`, and restart Ollama by `systemctl restart ollama`. For more information see [Ollama docs](https://github.com/ollama/ollama/blob/main/docs/faq.md#setting-environment-variables-on-linux) -> 在 `/etc/systemd/system/ollama.service` 文件中，添加 `Environment="OLLAMA_HOST=0.0.0.0:11434"`。（若使用其他端口请相应更改。）随后执行 `systemctl daemon-reload` 重载 systemd 管理器配置，并通过 `systemctl restart ollama` 重启 Ollama。更多信息请参阅 [Ollama 文档](https://github.com/ollama/ollama/blob/main/docs/faq.md#setting-environment-variables-on-linux)

   - Ensure that the port (default is 11434) is not blocked by your firewall. -> 确保端口（默认为 11434）未被防火墙拦截。

#### Lemonade Connection Errors

如果遇到 Lemonade 连接错误，通常是因为后端无法连接到 Lemonade 的 API。你可以通过以下方式解决：

1. **Check your Lemonade API URL:** Ensure that the API URL is correctly set in the settings menu. -> **检查你的 Lemonade API URL**：确保在设置菜单中正确设置了 API URL。
2. **Update API URL Based on OS:** -> **根据操作系统更新 API URL：**

   - **Windows:** Use `http://host.docker.internal:8000` -> - **Windows**：使用 `http://host.docker.internal:8000`
   - **Mac:** Use `http://host.docker.internal:8000` -> - **Mac**：使用 `http://host.docker.internal:8000`
   - **Linux:** Use `http://<private_ip_of_host>:8000` -> - **Linux**：使用 `http://<主机私有IP>:8000`

   Adjust the port number if you're using a different one. -> 如果你使用了其他端口，请相应调整。

3. **Ensure Lemonade Server is Running:** -> **确保 Lemonade 服务器正在运行：**

   - Make sure your Lemonade server is running and accessible on the configured port (default is 8000). -> 确认你的 Lemonade 服务器正在运行，且可通过配置的端口（默认为 8000）访问。
   - Verify that Lemonade is configured to accept connections from all interfaces (`0.0.0.0`), not just localhost (`127.0.0.1`). -> 验证 Lemonade 已配置为接受来自所有接口（`0.0.0.0`）的连接，而不仅限于本地回环地址（`127.0.0.1`）。
   - Ensure that the port (default is 8000) is not blocked by your firewall. -> 确保端口（默认为 8000）未被防火墙拦截。

## Using as a Search Engine

如果你希望将 Vane 作为 Google 或 Bing 等传统搜索引擎的替代品，或者想为浏览器的搜索栏添加快捷访问方式，请按照以下步骤操作：

1. Open your browser's settings. -> 打开浏览器设置。
2. Navigate to the 'Search Engines' section. -> 进入“搜索引擎”部分。
3. Add a new site search with the following URL: `http://localhost:3000/?q=%s`. Replace `localhost` with your IP address or domain name, and `3000` with the port number if Vane is not hosted locally. -> 添加新的站点搜索，URL 为：`http://localhost:3000/?q=%s`。如果 Vane 未托管在本地，请将 `localhost` 替换为你的 IP 地址或域名，将 `3000` 替换为端口号。
4. Click the add button. Now, you can use Vane directly from your browser's search bar. -> 点击添加按钮。现在你可以直接在浏览器的搜索栏中使用 Vane 了。

## Using Vane's API

Vane 还提供了 API，方便开发者将其强大的搜索引擎集成到自己的应用中。你可以运行搜索、调用多个模型并获取查询答案。

有关更多详情，请查阅完整文档[这里](https://github.com/ItzCrazyKns/Vane/tree/master/docs/API/SEARCH.md)。

## Expose Vane to network

Vane 基于 Next.js 运行并处理所有 API 请求。在同一局域网下即可直接使用，即使配置了端口转发也能保持可访问性。

## One-Click Deployment

[![Deploy to Sealos](https://raw.githubusercontent.com/labring-actions/templates/main/Deploy-on-Sealos.svg)](https://usw.sealos.io/?openapp=system-template%3FtemplateName%3Dperplexica)
[![Deploy to RepoCloud](https://d16t0pc4846x52.cloudfront.net/deploylobe.svg)](https://repocloud.io/details/?app_id=267)
[![Run on ClawCloud](https://raw.githubusercontent.com/ClawCloud/Run-Template/refs/heads/main/Run-on-ClawCloud.svg)](https://template.run.claw.cloud/?referralCode=U11MRQ8U9RM4&openapp=system-fastdeploy%3FtemplateName%3Dperplexica)
[![Deploy on Hostinger](https://assets.hostinger.com/vps/deploy.svg)](https://www.hostinger.com/vps/docker-hosting?compose_url=https://raw.githubusercontent.com/ItzCrazyKns/Vane/refs/heads/master/docker-compose.yaml)

## Upcoming Features

- [ ] 添加更多小组件、集成和数据源
- [ ] 支持创建自定义 Agent（名称待定，T.B.D.）
- [ ] 添加身份验证功能

## Support Us

如果你觉得 Vane 有用，欢迎在 GitHub 上给我们点个 Star。这能帮助更多人发现 Vane，并支持新功能的开发。非常感谢你的支持！

### Donations

我们也接受捐赠以维持项目运营。如果你想做出贡献，可以通过以下选项进行捐赠。感谢你的支持！

| Ethereum                                              |
| ----------------------------------------------------- |
| Address: `0xB025a84b2F269570Eb8D4b05DEdaA41D8525B6DD` |

## Contribution

Vane 的构建理念是：AI 和大语言模型应当让每个人都能轻松使用。如果你发现 Bug 或有改进建议，请通过 GitHub Issues 分享。有关如何为 Vane 做出贡献的更多信息，请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 文件。

## Help and Support

如果你有任何问题或反馈，欢迎随时联系我们。你可以在 GitHub 上创建 Issue，或加入我们的 Discord 服务器。在那里你可以与其他用户交流、分享使用体验与评价，并获得更个性化的帮助。[点击这里](https://discord.gg/EFwsmQDgAu) 加入 Discord 服务器。如需讨论常规支持范围以外的事务，欢迎在 Discord 上私信我 `itzcrazykns`。

感谢你探索 Vane——这款旨在提升搜索体验的 AI 驱动搜索引擎。我们正不断努力优化 Vane 并扩展其功能。你的反馈和贡献对我们至关重要，帮助我们让 Vane 变得更好。别忘了常回来看看更新和新功能！