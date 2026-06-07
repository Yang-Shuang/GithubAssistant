<a href="https://www.surfsense.com/"><img width="1584" height="396" alt="readme_banner" src="https://github.com/user-attachments/assets/9361ef58-1753-4b6e-b275-5020d8847261" /></a>



<div align="center">
<a href="https://discord.gg/ejRNvftDp9">
<img src="https://img.shields.io/discord/1359368468260192417" alt="Discord">
</a>
<a href="https://www.reddit.com/r/SurfSense/">
<img src="https://img.shields.io/reddit/subreddit-subscribers/SurfSense?style=social" alt="Reddit">
</a>
</div>

<div align="center">

[English](README.md) | [Español](README.es.md) | [Português](README.pt-BR.md) | [हिन्दी](README.hi.md) | [简体中文](README.zh-CN.md)

</div>
<div align="center">
<a href="https://trendshift.io/repositories/13606" target="_blank"><img src="https://trendshift.io/api/badge/repositories/13606" alt="MODSetter%2FSurfSense | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</div>

# SurfSense

NotebookLM 是目前市面上最好用、最实用的 AI 平台之一，但一旦你开始频繁使用，就会逐渐感受到它的局限性：

1. 单个笔记本中可添加的源（Sources）数量受限。
2. 你可拥有的笔记本总数有限制。
3. 单个源不能超过 50 万词且超过 200MB。
4. 你被锁定在 Google 服务生态（LLM、使用模型等）中，无法自定义配置。
5. 外部数据源和服务集成有限。
6. NotebookLM Agent 专为学习和研究优化，但你可以利用源数据做更多事情。
7. 缺乏多人协作支持。

...以及更多限制。

**SurfSense 正是为了解决这些问题而专门打造的。** SurfSense 赋能你：

- **掌控你的数据流** - 保持数据的私密性与安全性。
- **无数据限制** - 添加无限数量的源和笔记本。
- **拒绝厂商锁定（Vendor Lock-in）** - 自由配置任意 LLM、图像、TTS 和 STT 模型。
- **25+ 外部数据源** - 从 Google Drive、OneDrive、Dropbox、Notion 及其他众多外部服务中添加你的数据源。
- **实时多人协作支持** - 在共享笔记本中与团队成员轻松协同工作。
- **AI 文件分类** - 利用 AI 按来源、日期和主题自动将文档组织成智能文件夹层级结构。
- **AI 自动化与 Agent（智能体）** - 按计划运行 AI Agent，或在文档落入指定文件夹的瞬间触发它们，然后将结果写回 Notion、Slack、Linear 和 Drive。只需在聊天中描述需求即可构建无代码自动化流程。
- **桌面客户端** - 通过 Quick Assist、General Assist、Screenshot Assist 和本地文件夹同步功能，在任何应用中获取 AI 辅助。

...更多功能即将上线。



## Video Agent Sample

https://github.com/user-attachments/assets/012a7ffa-6f76-4f06-9dda-7632b470057a



## Podcast Agent Sample

https://github.com/user-attachments/assets/a0a16566-6967-4374-ac51-1b3e07fbecd7


## 如何使用 SurfSense

### 云端版（Cloud）

1. 访问 [surfsense.com](https://www.surfsense.com) 并登录。

<p align="center"><img src="surfsense_web/public/homepage/hero_tutorial/LoginFlowGif.gif" alt="Login" /></p>

2. 连接你的数据源并完成同步。启用定期同步以保持连接器持续更新。

<p align="center"><img src="surfsense_web/public/homepage/hero_tutorial/ConnectorFlowGif.gif" alt="Connectors" /></p>

3. 等待数据索引完成后，上传文档。

<p align="center"><img src="surfsense_web/public/homepage/hero_tutorial/DocUploadGif.gif" alt="Upload Documents" /></p>

4. 一切索引完成后即可开始提问（使用场景）：

   **桌面客户端增强功能**（在云端版基础上提供原生扩展，非独立功能集）

   - General Assist（通用辅助）：通过全局快捷键在任何应用中瞬间启动 SurfSense。

   <p align="center"><img src="surfsense_web/public/homepage/hero_tutorial/general_assist.gif" alt="General Assist" /></p>

   - Quick Assist（快速辅助）：选中任意位置的文本，然后让 AI 进行解释、重写或执行操作。

   <p align="center"><img src="surfsense_web/public/homepage/hero_tutorial/quick_assist.gif" alt="Quick Assist" /></p>

   - Screenshot Assist（截图辅助）：截取屏幕任意区域，并询问 AI 其中的内容。

   <p align="center"><img src="surfsense_web/public/homepage/hero_tutorial/screenshot_assist.gif" alt="Screenshot Assist" /></p>

   - Watch Local Folder（监听本地文件夹）：自动将本地文件夹同步至你的知识库。非常适合配合 Obsidian 使用。

   <p align="center"><img src="surfsense_web/public/homepage/hero_tutorial/folder_watch.gif" alt="Watch Local Folder" /></p>

   **成果生成中心（Deliverable Studio）**

   - AI Report Generator（AI 报告生成器）：生成带引用的研究报告，并导出为 PDF、DOCX、HTML、LaTeX、EPUB、ODT 或纯文本。

   <p align="center"><img src="surfsense_web/public/homepage/hero_tutorial/ReportGenGif_compressed.gif" alt="AI Report Generator" /></p>

   - AI Podcast Generator（AI 播客生成器）：在 20 秒内将任意文档或文件夹转化为双主持人 AI 播客。

   <p align="center"><img src="surfsense_web/public/homepage/hero_tutorial/PodcastGenGif.gif" alt="AI Podcast Generator" /></p>

   - AI Presentation & Video Maker（AI 演示与视频制作）：基于你的数据源创建可编辑的幻灯片和带旁白的视频概述。

   <p align="center"><img src="surfsense_web/public/homepage/hero_tutorial/video_gen_gif.gif" alt="AI Presentation and Video Maker" /></p>

   - AI Image Generator（AI 图像生成器）：直接从聊天记录和文档中生成高质量图片。

   <p align="center"><img src="surfsense_web/public/homepage/hero_tutorial/ImageGenGif.gif" alt="AI Image Generator" /></p>

   - AI Resume Builder（AI 简历定制）：根据你的现有简历和目标职位描述进行匹配，轻松通过 ATS（招聘管理系统）筛选。
     可尝试以下提示词：

     - “根据这份职位描述优化我的简历，确保能通过 ATS 筛选并争取到面试机会。”
     - “提取该职位的关键字并优化我的简历以提高 ATS 通过率。”
     - “重写我的简历要点，突出该岗位所需的核心技能。”
     - “对比我的简历与该职位描述，列出需要补充的差距。”
     - “基于我的简历和这份职位描述，为我撰写一封匹配的求职信。”

   **搜索与聊天（Search & Chat）**

   - 对话你的 PDF 与文档：针对所有文件提问，获取带内联引用的回答。

   <p align="center"><img src="surfsense_web/public/homepage/hero_tutorial/BQnaGif_compressed.gif" alt="Chat With Your PDFs and Docs" /></p>

   - AI 搜索（带引用）：在你的整个知识库中进行混合语义与关键词检索。

   <p align="center"><img src="surfsense_web/public/homepage/hero_tutorial/BSNCGif.gif" alt="AI Search With Citations" /></p>

   - 协作式 AI 聊天：与团队成员在共享空间中实时进行 AI 对话。

   <p align="center"><img src="surfsense_web/public/homepage/hero_realtime/RealTimeChatGif.gif" alt="Collaborative AI Chat" /></p>

   - 评论与 @提及：在任何 AI 消息下发表评论或标记团队成员。

   <p align="center"><img src="surfsense_web/public/homepage/hero_realtime/RealTimeCommentsFlow.gif" alt="Comments and Mentions" /></p>

   **连接器与集成（Connectors & Integrations）**

   - 连接并同步你的工具：将 Notion、Slack、Google Drive、Gmail、GitHub、Linear 等 25+ 数据源同步至一个可统一检索的知识库。

   <p align="center"><img src="surfsense_web/public/homepage/hero_tutorial/ConnectorFlowGif.gif" alt="Connect and Sync Your Tools" /></p>

   - 对话已上传文件：拖入 PDF、Office 文档、图片和音频，即刻支持检索与问答。

   <p align="center"><img src="surfsense_web/public/homepage/hero_tutorial/DocUploadGif.gif" alt="Chat With Uploaded Files" /></p>

   - 连接器写回（Connector Write-Back）：让 Agent 将结果直接发布至 Notion、Slack、Linear 和 Drive。
     可尝试以下提示词：

     - “将此研究摘要发布到我的 Notion 工作区。”
     - “将这些会议待办事项发送到我们的团队 Slack 频道。”
     - “根据此错误报告创建一个 Jira 工单。”
     - “基于此功能请求在 Linear 中创建一个问题（Issue）。”
     - “将此生成的报告保存为文档至 Google Drive。”

   - Obsidian 与知识库同步：保持你的 Obsidian 库与个人知识库实时一致。

   **自动化工作流（Automations）**

   - 定时 AI 工作流：按计划运行 Agent，例如每日简报、每周摘要或定期报告。
     可尝试以下提示词：

     - “每天早上向我发送一份知识库中新文档的每日简报邮件。”
     - “每周五从我的 Slack 和 Gmail 生成一份周报状态汇总。”
     - “每月执行一次竞争对手分析报告并保存至我的工作区。”
     - “将我的 GitHub 和 Linear 活动总结为每日站会更新内容。”
     - “为我追踪的主题创建每周研究报告。”

   - 事件触发自动化：当文档落入指定文件夹时立即触发 Agent，并将结果推送至你的工具。
     可尝试以下提示词：

     - “当 PDF 进入我的 Research 文件夹时，生成一份带引用的 AI 摘要。”
     - “当新增会议记录时，自动将其整理为包含待办事项的会议纪要。”
     - “当上传发票时，提取供应商、总金额和到期日并输出为表格。”
     - “当合同进入 Legal 文件夹时，标记关键条款和续约日期。”
     - “当简历添加到 Candidates 文件夹时，根据职位描述进行自动初筛。”

   - 聊天构建自动化：用自然语言描述你的需求，SurfSense 会自动为你生成自动化流程。
     可尝试以下提示词：

     - “创建一个 AI Agent，每天早上向我发送新 Notion 页面的摘要邮件。”
     - “创建一项无代码自动化流程，每周将研究报告摘要发布到 Slack。”
     - “设置一个 AI 会议记录员，自动将新笔记整理为正式会议纪要。”
     - “建立一个工作流：从会议笔记中提取待办事项并分配负责人。”
     - “自动化每日邮件简报，整合我的 Gmail 和 Google Drive 内容。”


### 自托管版（Self Hosted）

在自有基础设施上运行 SurfSense，实现完全的数据控制与隐私保护。

**前置条件：** 必须已安装并运行 [Docker Desktop](https://www.docker.com/products/docker-desktop/)。

#### Linux/MacOS 用户：

```bash
curl -fsSL https://raw.githubusercontent.com/MODSetter/SurfSense/main/docker/scripts/install.sh | bash
```

#### Windows 用户：

```bash
irm https://raw.githubusercontent.com/MODSetter/SurfSense/main/docker/scripts/install.ps1 | iex
```

安装脚本会自动配置 [Watchtower](https://github.com/nicholas-fedor/watchtower) 以实现每日自动更新。如需跳过，请添加 `--no-watchtower` 参数。

关于 Docker Compose、手动部署及其他选项，请参阅[官方文档](https://www.surfsense.com/docs/)。

### 桌面客户端（Desktop App）

SurfSense 同时提供桌面客户端，将 AI 辅助能力带入你电脑上的每一个应用。请从[最新版本发布页](https://github.com/MODSetter/SurfSense/releases/latest)下载。

桌面客户端包含以下核心功能：

- **General Assist（通用辅助）** — 通过全局快捷键在任何应用中瞬间启动 SurfSense。
- **Quick Assist（快速辅助）** — 选中任意文本，让 AI 解释、重写或执行操作。
- **Screenshot Assist（截图辅助）** — 截取屏幕区域并附加至聊天，确保回答始终基于你的知识库上下文。
- **Watch Local Folder（监听本地文件夹）** — 监控本地文件夹变动，自动同步文件更新至知识库。**使用技巧：** 指向你的 Obsidian vault，即可在 SurfSense 中搜索所有笔记内容。

所有功能均作用于你选择的搜索空间（SearchSpace），确保回答始终扎根于你自己的数据。

### 如何实时协作（Beta）

1. 进入“管理成员”页面并创建邀请链接。

   <p align="center"><img src="https://github.com/user-attachments/assets/40ed7683-5aa6-48a0-a3df-00575528c392" alt="Invite Members" /></p>

2. 团队成员加入后，该搜索空间（SearchSpace）将变为共享状态。

   <p align="center"><img src="https://github.com/user-attachments/assets/ea4e1057-4d2b-4fd2-9ca0-cd19286a285e" alt="Invite Join Flow" /></p>

3. 将聊天设置为共享模式。

   <p align="center"><img src="https://github.com/user-attachments/assets/17b93904-0888-4c3a-ac12-51a24a8ea26a" alt="Make Chat Shared" /></p>

4. 你的团队现在可以实时聊天协作。

   <p align="center"><img src="surfsense_web/public/homepage/hero_realtime/RealTimeChatGif.gif" alt="Realtime Chat" /></p>

5. 添加评论并 @提及团队成员。

   <p align="center"><img src="surfsense_web/public/homepage/hero_realtime/RealTimeCommentsFlow.gif" alt="Realtime Comments" /></p>

## SurfSense vs Google NotebookLM

| Feature | Google NotebookLM | SurfSense |
|---------|-------------------|-----------|
| **单笔记本源数量** | 50（免费版）至 600（Ultra，$249.99/月） | 无限制 |
| **笔记本数量** | 100（免费版）至 500（付费版） | 无限制 |
| **源大小限制** | 每个源不超过 50 万词 / 200MB | 无限制 |
| **定价** | 提供免费版；Pro $19.99/月，Ultra $249.99/月 | 免费开源，支持在自有基础设施上自托管 |
| **LLM 支持** | 仅限 Google Gemini | 通过 OpenAI 规范与 LiteLLM 支持 100+ LLM |
| **Embedding 模型** | 仅限 Google | 6,000+ Embedding 模型，涵盖所有主流重排器（Rerankers） |
| **本地/私有 LLM** | 不支持 | 全面支持（vLLM、Ollama）- 数据完全由你掌控 |
| **可自托管** | 否 | 是 - Docker 单行命令或完整 Docker Compose |
| **开源** | 否 | 是 |
| **外部连接器** | Google Drive, YouTube, 网站 | 27+ 连接器 - 搜索引擎、Google Drive、OneDrive、Dropbox、Slack、Teams、Jira、Notion、GitHub、Discord 及[更多](#external-sources) |
| **文件格式支持** | PDFs, Docs, Slides, Sheets, CSV, Word, EPUB, images, web URLs, YouTube | 50+ 格式 - 文档、图像、视频（通过 LlamaCloud、Unstructured 或 Docling (本地)） |
| **搜索** | 语义搜索 | 混合搜索 - 语义 + 全文检索，支持分层索引与倒数排名融合算法（RRF） |
| **带引用回答** | 是 | 是 - Perplexity 风格的带引用回复 |
| **Agent 架构** | 否 | 是 - 基于 [LangChain Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview) 构建，支持规划、子 Agent 及文件系统访问 |
| **实时多人协作** | 共享笔记本（含 Viewer/Editor 角色）（无实时聊天） | RBAC（基于角色的访问控制），含 Owner / Admin / Editor / Viewer 角色，支持实时聊天与评论线程 |
| **视频生成** | 通过 Veo 3 生成电影级视频概述（仅限 Ultra） | 已提供（注：此处 NotebookLM 表现更佳，SurfSense 正在持续优化中） |
| **演示文稿生成** | 外观更精美但不可编辑 | 可创建可编辑的幻灯片演示文稿 |
| **播客生成** | 音频概述，支持自定义主持人与语言 | 已提供，支持多种 TTS 提供商（注：此处 NotebookLM 表现更佳，SurfSense 正在持续优化中） |
| **AI 文件分类** | 否 | LLM 驱动自动分类至来源、日期、类别和子类别文件夹 |
| **AI 自动化与 Agent** | 否 | 计划任务 AI 工作流、文档事件触发器，以及聊天构建的无代码自动化流程（支持写回 Notion, Slack, Linear & Jira） |
| **桌面客户端** | 否 | 原生应用，内置 General Assist, Quick Assist, Screenshot Assist 及本地文件夹同步功能 |
| **浏览器扩展** | 否 | 跨浏览器扩展，可保存任意网页（含需认证的页面） |

<details>
<summary><b>外部数据源完整列表</b></summary>
<a id="external-sources"></a>

搜索引擎（SearXNG, Tavily, LinkUp, Baidu Search） · Google Drive · OneDrive · Dropbox · Slack · Microsoft Teams · Linear · Jira · ClickUp · Confluence · BookStack · Notion · Gmail · YouTube 视频 · GitHub · Discord · Airtable · Google Calendar · Luma · Circleback · Elasticsearch · Obsidian，更多数据源持续接入中。

</details>


## 功能反馈与未来规划

**SurfSense 正在积极开发中。** 虽然尚未达到生产环境成熟度，但你可以帮助我们加速完善进程。

加入 [SurfSense Discord](https://discord.gg/ejRNvftDp9)，共同塑造 SurfSense 的未来！

## 路线图（Roadmap）

随时了解我们的开发进展与即将上线的功能！  
查看我们的公开路线图并贡献你的想法或反馈：

**路线讨论：** [SurfSense 2026 Roadmap](https://github.com/MODSetter/SurfSense/discussions/565)

**看板管理：** [SurfSense Project Board](https://github.com/users/MODSetter/projects/3)


## 贡献指南（Contribute）

欢迎任何形式的贡献，从点亮 Star、提交 Bug 报告到后端代码优化。请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 开始参与开发。

感谢所有 SurfSense 的贡献者：

<a href="https://github.com/MODSetter/SurfSense/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=MODSetter/SurfSense" />
</a>

## Star 增长历史

<a href="https://www.star-history.com/#MODSetter/SurfSense&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=MODSetter/SurfSense&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=MODSetter/SurfSense&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=MODSetter/SurfSense&type=Date" />
 </picture>
</a>

---
---
<p align="center">
    <img 
      src="https://github.com/user-attachments/assets/329c9bc2-6005-4aed-a629-700b5ae296b4" 
      alt="Catalyst Project" 
      width="200"
    />
</p>

---
---