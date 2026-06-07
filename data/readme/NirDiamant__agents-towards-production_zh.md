<div align="center">

# 迈向生产环境的 AI Agent（Agents Towards Production）

### _将 AI Agent 转化为实际产品的开源指南。_

**Agents Towards Production** 是你构建可投入生产的 GenAI（生成式人工智能）Agent 的首选资源，助力项目从原型顺利扩展至企业级应用。教程涵盖有状态工作流、向量记忆、实时网络搜索 API、Docker 部署、FastAPI 端点、安全护栏、GPU 扩缩容、浏览器自动化、模型微调、多 Agent 协同、可观测性、评估以及 UI 开发等内容。

### ⭐ **如果你觉得本项目有价值，请点亮⭐ Star 帮助更多人发现这些教程！** 

<!-- SEO Keywords: generative ai agents, production deployment, langgraph, langchain, rag, retrieval augmented generation, memory, observability, guardrails, gpu deployment, orchestration, multi agent, prompt engineering, tutorials, guide -->

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/nir-diamant-759323134/)
[![Twitter](https://img.shields.io/twitter/follow/NirDiamantAI?label=Follow%20@NirDiamantAI&style=social)](https://twitter.com/NirDiamantAI)
[![Discord](https://img.shields.io/badge/Discord-Join%20our%20community-7289da?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/cA6Aa4uyDX)
[![Sponsor](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=ff69b4)](https://github.com/sponsors/NirDiamant)
[![DiamantAI Collective is hiring](https://img.shields.io/badge/%F0%9F%92%BC%20Hiring-DiamantAI%20Collective-7c3aed?style=flat-square)](https://europe-west1-atp-views-tracker.cloudfunctions.net/working-analytics?notebook=main-readme--hiring-badge&click=top-badge-hiring&target=https%3A%2F%2Fdiamant-ai.com%2Fjobs&text=Hiring%20Badge)

</div>

---

<div align="center">

## 📖 DiamantAI 系列书籍

<a href="https://europe-west1-rag-techniques-views-tracker.cloudfunctions.net/rag-techniques-tracker?notebook=agents-towards-production--readme&click=book-buy-amazon-image&target=https%3A%2F%2Fwww.amazon.com%2Fdp%2FB0D76734SZ%3Ftag%3Ddiamantai-atp-20&text=Best%20Seller%20Image"><img src="images/rag_book_best_seller.png" alt="RAG Made Simple - Amazon bestseller in Generative AI" width="500"></a>

**[《RAG Made Simple》（简化 RAG）](https://europe-west1-rag-techniques-views-tracker.cloudfunctions.net/rag-techniques-tracker?notebook=agents-towards-production--readme&click=book-buy-amazon-title&target=https%3A%2F%2Fwww.amazon.com%2Fdp%2FB0D76734SZ%3Ftag%3Ddiamantai-atp-20&text=RAG%20Made%20Simple)** - RAG 系统的生产环境参考指南
一本涵盖 22 种 RAG（检索增强生成）技术的 400 页可视化指南。如果你正在交付需要检索和基于真实数据进行推理的 Agent，本书正是本仓库中这些模式的底层结构化参考。
*已售出 1,500+ 册 · 发布时登顶亚马逊生成式 AI 畅销榜第一 · ⭐ 4.4 星*
**Kindle $9.99 · 平装版 $24.99 · Kindle Unlimited 免费阅读**

👉 [**在 Amazon 获取《RAG Made Simple》**](https://europe-west1-rag-techniques-views-tracker.cloudfunctions.net/rag-techniques-tracker?notebook=agents-towards-production--readme&click=book-buy-amazon-cta&target=https%3A%2F%2Fwww.amazon.com%2Fdp%2FB0D76734SZ%3Ftag%3Ddiamantai-atp-20&text=Get%20RAG%20Made%20Simple)

---

**[《Prompt Engineering: Master the Art of AI Interaction》（提示词工程：掌握 AI 交互艺术）](https://europe-west1-rag-techniques-views-tracker.cloudfunctions.net/rag-techniques-tracker?notebook=agents-towards-production--readme&click=book-buy-pe&target=https%3A%2F%2Fwww.amazon.com%2Fdp%2FB0DZ85RPB5%3Ftag%3Ddiamantai-atp-20&text=Prompt%20Engineering)** - 提示词基础
深入讲解 22 种实战提示词技巧。作为《RAG Made Simple》的配套书籍，它决定了你的生产级 Agent 行为是否可靠。

👉 [**在 Amazon 查看《Prompt Engineering》**](https://europe-west1-rag-techniques-views-tracker.cloudfunctions.net/rag-techniques-tracker?notebook=agents-towards-production--readme&click=book-buy-pe-cta&target=https%3A%2F%2Fwww.amazon.com%2Fdp%2FB0DZ85RPB5%3Ftag%3Ddiamantai-atp-20&text=See%20Prompt%20Engineering)

</div>

---

<div align="center">


> **28 个生产级教程**，涵盖有状态工作流、向量记忆、网络搜索 API、Docker 部署、安全护栏、GPU 扩缩容、多 Agent 协同等内容。

<div align="center">

---

<img src="images/collective-banner.png" alt="DiamantAI Collective - AI engineering jobs" width="600">

</div>

## 💎 教程赞助方

<p align="center"><em>
为本仓库贡献分步教程的公司。<br>
点击标志即可打开对应教程。使用 Ctrl‑/⌘‑单击可保持当前页面不关闭。
</em></p>

<!-- ─────────── 1st row – 4 sponsors ─────────── -->
<table align="center" cellpadding="20"
       style="table-layout:fixed; width:100%; border-collapse:collapse;">
<tr align="center" valign="top">

  <!-- LangChain -->
  <td width="200" valign="bottom">
    <a href="tutorials/LangGraph-agent" title="Open LangChain tutorial">
      <picture>
        <source media="(prefers-color-scheme: dark)"
                srcset="assets/repos_images/sponsors_logos/trimmed_padded/trimmed_padded_langchain_white.png">
        <img src="assets/repos_images/sponsors_logos/trimmed_padded/trimmed_padded_langchain.png"
             height="44" style="max-width:180px;" alt="LangChain - AI agent framework and workflow orchestration platform for building production-ready language model applications">
      </picture>
    </a><br>
    <sub><span style="white-space:nowrap;">Agent（智能体）框架与工作流</span><br>
      <a href="https://langchain.com">
        <img src="assets/repos_images/visit-site-badge.svg" width="56" height="16" alt="Visit LangChain AI agent framework website">
      </a>
    </sub>
  </td>

  <!-- Redis -->
  <td width="200" valign="bottom">
    <a href="tutorials/agent-memory-with-redis" title="Open Redis tutorial">
      <picture>
        <source media="(prefers-color-scheme: dark)"
                srcset="assets/repos_images/sponsors_logos/trimmed_padded/trimmed_padded_Redis_white.svg">
        <img src="assets/repos_images/sponsors_logos/trimmed_padded/trimmed_padded_Redis.png"
             height="44" style="max-width:180px;" alt="Redis - In-memory database and vector storage for AI agent memory, caching, and real-time data processing">
      </picture>
    </a><br>
    <sub><span style="white-space:nowrap;">记忆与向量数据库</span><br>
      <a href="https://redis.io/try-free/?utm_source=nir&utm_medium=cpa&utm_campaign=2025-05-ai_in_production-influencer-nir&utm_content=sd-software_download-7013z000001WaRY">
        <img src="assets/repos_images/visit-site-badge.svg" width="56" height="16" alt="Visit Redis in-memory database and vector storage website">
      </a>
    </sub>
  </td>

  <!-- Contextual AI -->
  <td width="200" valign="bottom">
    <a href="tutorials/agent-RAG-with-Contextual" title="Open Contextual AI tutorial">
      <picture>
        <source media="(prefers-color-scheme: dark)"
                srcset="assets/repos_images/sponsors_logos/trimmed_padded/trimmed_padded_contextual_white.png">
        <img src="assets/repos_images/sponsors_logos/trimmed_padded/trimmed_padded_contextual_black.png"
             height="44" style="max-width:180px;" alt="Contextual AI - Production-ready RAG platform for building enterprise-grade retrieval augmented generation systems">
      </picture>
    </a><br>
    <sub><span style="white-space:nowrap;">RAG 与知识管理</span><br>
      <a href="https://app.contextual.ai/?utm_campaign=agents-towards-production&utm_source=diamantai&utm_medium=github&utm_content=notebook">
        <img src="assets/repos_images/visit-site-badge.svg" width="56" height="16" alt="Visit Contextual AI RAG platform website">
      </a>
    </sub>
  </td>

  <!-- Bright Data -->
  <td width="200" valign="bottom">
    <a href="tutorials/agent-with-brightdata" title="Open Bright Data tutorial">
      <picture>
        <source media="(prefers-color-scheme: dark)"
                srcset="assets/repos_images/sponsors_logos/trimmed_padded/trimmed_padded_brightdata_white.svg">
        <img src="assets/repos_images/sponsors_logos/trimmed_padded/trimmed_padded_brightdata.png"
             height="44" style="max-width:180px;" alt="Bright Data - Web scraping and data collection platform for AI training and agent data gathering">
      </picture>
    </a><br>
    <sub><span style="white-space:nowrap;">网络数据平台</span><br>
      <a href="https://brightdata.com/ai?utm_source=brand&utm_campaign=brnd-mkt_github_nirdiamant_logo">
        <img src="assets/repos_images/visit-site-badge.svg" width="56" height="16" alt="Visit Bright Data web scraping platform website">
      </a>
    </sub>
  </td>
  
  
</tr>
</table>

<!-- ─────────── 2nd row – 3 sponsors ─────────── -->
<table align="center" cellpadding="20"
       style="table-layout:fixed; width:100%; margin-top:16px; border-collapse:collapse;">
<tr align="center" valign="top">

  <!-- Tavily -->
  <td width="200" valign="bottom">
    <a href="tutorials/agent-with-tavily-web-access" title="Open Tavily tutorial">
      <picture>
        <source media="(prefers-color-scheme: dark)"
                srcset="assets/repos_images/sponsors_logos/trimmed_padded/trimmed_padded_tavily_white.png">
        <img src="assets/repos_images/sponsors_logos/trimmed_padded/trimmed_padded_tavily.png"
             height="44" style="max-width:180px;" alt="Tavily - Real-time web search API for AI agents with intelligent content extraction and summarization">
      </picture>
    </a><br>
    <sub><span style="white-space:nowrap;">实时网络搜索 API</span><br>
      <a href="https://app.tavily.com/home/?utm_source=github&utm_medium=referral&utm_campaign=nir_diamant">
        <img src="assets/repos_images/visit-site-badge.svg" width="56" height="16" alt="Visit Tavily real-time web search API website">
      </a>
    </sub>
  </td>

  <!-- Arcade -->
  <td width="200" valign="bottom">
    <a href="tutorials/arcade-secure-tool-calling" title="Open Arcade tutorial">
      <picture>
        <source media="(prefers-color-scheme: dark)"
                srcset="assets/repos_images/sponsors_logos/trimmed_padded/trimmed_padded_arcade_white_tight.png">
        <img src="assets/repos_images/sponsors_logos/trimmed_padded/trimmed_padded_arcade_black.png"
             height="44" style="max-width:180px;" alt="Arcade - Multi-user tool calling platform for secure OAuth2 authentication and human-in-the-loop safety controls">
      </picture>
    </a><br>
    <sub><span style="white-space:nowrap;">MCP 运行时环境</span><br>
      <a href="https://docs.arcade.dev/en/home?utm_source=github&utm_medium=paid_sponsorship&utm_campaign=agents_toward_prod&utm_content=readme_placement">
        <img src="assets/repos_images/visit-site-badge.svg" width="56" height="16" alt="Visit Arcade multi-user tool integration platform website">
      </a>
    </sub>
  </td>

  <!-- JetBrains -->
  <td width="200" valign="bottom">
    <a href="tutorials/kotlin-agent-with-koog" title="Open JetBrains Koog tutorial">
      <picture>
        <source media="(prefers-color-scheme: dark)"
                srcset="assets/repos_images/sponsors_logos/trimmed_padded/trimmed_padded_jetbrains_white.svg">
        <img src="assets/repos_images/sponsors_logos/trimmed_padded/trimmed_padded_jetbrains.png"
             height="44" style="max-width:180px;" alt="JetBrains - Creator of Kotlin and the Koog AI agent framework for building intelligent applications on the JVM">
      </picture>
    </a><br>
    <sub><span style="white-space:nowrap;">Kotlin AI Agent（智能体）框架</span><br>
      <a href="https://kotlinlang.org/?utm_source=github&utm_medium=influencers&utm_campaign=kotlin_nir_supporter_1">
        <img src="assets/repos_images/visit-site-badge.svg" width="56" height="16" alt="Visit Kotlin website">
      </a>
    </sub>
  </td>

</tr>
</table>

<!-- ─────────── 3rd row – 3 sponsors ─────────── -->
<table align="center" cellpadding="20"
       style="table-layout:fixed; width:100%; margin-top:16px; border-collapse:collapse;">
<tr align="center" valign="top">

  <!-- Mem0 -->
  <td width="200" valign="bottom">
    <a href="tutorials/agent-memory-with-mem0" title="Open Mem0 tutorial">
      <picture>
        <source media="(prefers-color-scheme: dark)"
                srcset="assets/repos_images/sponsors_logos/trimmed_padded/Mem0%20Word%20Logo.png">
        <img src="assets/repos_images/sponsors_logos/trimmed_padded/Mem0 Word Logo Dark.png"
             height="44" style="max-width:180px;" alt="Mem0 - Self-improving memory system for AI agents with hybrid vector and graph storage">
      </picture>
    </a><br>
    <sub><span style="white-space:nowrap;">自我进化的 AI 记忆系统</span><br>
      <a href="https://mem0.dev/github/nir">
        <img src="assets/repos_images/visit-site-badge.svg" width="56" height="16" alt="Visit Mem0 AI memory platform website">
      </a>
    </sub>
  </td>

  <!-- RunPod -->
  <td width="200" valign="bottom">
    <a href="tutorials/runpod-gpu-deploy" title="Open RunPod tutorial">
      <picture>
        <source media="(prefers-color-scheme: dark)"
                srcset="assets/repos_images/sponsors_logos/trimmed_padded/trimmed_padded_runpod_white.svg">
        <img src="assets/repos_images/sponsors_logos/trimmed_padded/trimmed_padded_runpod.svg"
             height="44" style="max-width:180px;" alt="RunPod - GPU cloud computing platform for training and deploying AI models and agents at scale">
      </picture>
    </a><br>
    <sub><span style="white-space:nowrap;">GPU 云计算</span><br>
      <a href="https://get.runpod.io/nirdiamant">
        <img src="assets/repos_images/visit-site-badge.svg" width="56" height="16" alt="Visit RunPod GPU cloud computing website">
      </a>
    </sub>
  </td>

</tr>
</table>

## 💎 通用赞助方

<p align="center"><em>
通过合作与资源支持本项目的公司。<br>
点击标志即可访问其官网。
</em></p>

<!-- ─────────── General sponsors ─────────── -->
<table align="center" cellpadding="20"
       style="table-layout:fixed; width:100%; border-collapse:collapse;">
<tr align="center" valign="top">

  <!-- CodeRabbit -->
  <td width="200" valign="bottom">
    <a href="https://coderabbit.link/nir" title="Visit CodeRabbit">
      <picture>
        <source media="(prefers-color-scheme: dark)"
                srcset="assets/repos_images/sponsors_logos/trimmed_padded/coderabbit_Dark_Type_Mark.png">
        <img src="assets/repos_images/sponsors_logos/trimmed_padded/coderabbit_Light_Type_Mark_Orange.png"
             height="44" style="max-width:180px;" alt="CodeRabbit - AI-powered code review and automated pull request analysis">
      </picture>
    </a><br>
    <sub><span style="white-space:nowrap;">AI 代码审查</span><br>
      <a href="https://coderabbit.link/nir">
        <img src="assets/repos_images/visit-site-badge.svg" width="56" height="16" alt="Visit CodeRabbit AI code review platform">
      </a>
    </sub>
  </td>

</table>

<div align="center">

### 💎 成为赞助方

**取得联系：**

[![Website](https://img.shields.io/badge/Website-DiamantAI.com-green?style=for-the-badge&logo=globe)](https://www.diamant-ai.com/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/nir-diamant-759323134/)

</div>

</div>



<div align="center">

## 📫 获取最新动态！

<table>
<tr>
<td align="center" style="padding:15px;background-color:#f8f9fa;border-right:1px solid #eaecef">🚀<br/><b>前沿动态</b></td>
<td align="center" style="padding:15px;background-color:#f8f9fa;border-right:1px solid #eaecef">💡<br/><b>专家见解</b></td>
<td align="center" style="padding:15px;background-color:#f8f9fa">🎯<br/><b>顶级内容（前 0.1%）</b></td>
</tr>
</table>

[![Subscribe to DiamantAI Newsletter](assets/repos_images/subscribe-button.svg)](https://diamantai.substack.com/?r=336pe4&utm_campaign=pub-share-checklist)

_加入超过 50,000 名 AI 爱好者的行列，获取独特的前沿洞察与免费教程！_  
**此外，订阅者还可独家抢先体验并享受本人书籍及即将上线课程的专属 33% 折扣优惠！**

[![DiamantAI's newsletter](assets/repos_images/substack_image.png)](https://diamantai.substack.com/?r=336pe4&utm_campaign=pub-share-checklist)

</div>

---

<div align="center">

## 💬 加入我们的社区

与 GenAI（生成式 AI）和 Agent 开发保持同步：

### r/EducationalAI

[![Reddit](https://img.shields.io/badge/Reddit-Join%20r/EducationalAI-ff4500?style=for-the-badge&logo=reddit&logoColor=white)](https://www.reddit.com/r/EducationalAI/)

_加入我们不断壮大的社区，共同探讨前沿 AI 研究、Agent 开发及生产级实践经验！_

</div>

---


---

## ✨ 简介
**Agents Towards Production** 是你构建 GenAI Agent（生成式人工智能智能体）技术栈中每个核心模块的实战指南。  
所有知识均通过可运行的教程呈现，涵盖编排、记忆、可观测性、部署、安全等内容。每个教程都位于独立文件夹中，提供开箱即用的 Notebook 或代码文件，让你能在几分钟内从概念验证走向可用的 Agent。

---

## 🏗️ AI Agent（智能体）架构

<div align="center">

![AI Agent Architecture - Production-ready AI agent development workflow showing orchestration, memory, tools, security, observability, evaluation, and deployment components](assets/repos_images/ai_architecture_diagram.svg)

*该图展示了构建生产级 Agent 的完整流程。本仓库中的教程将逐步涵盖这些核心组件。*

</div>

---

## 📚 教程

### 🔌 工具集成

<table width="100%">
  <tr style="background-color:#f8f9fa">
    <th width="30%">教程</th>
    <th width="50%">描述</th>
    <th width="20%">查看</th>
  </tr>
  <tr>
    <td>安全工具调用（Arcade）<img src="https://img.shields.io/badge/NEW-brightgreen" height="16"></td>
    <td>让 Agent 能够安全地调用外部工具（如 Gmail、Slack、Notion），结合 OAuth2 认证与人机协同审批机制。学习具备用户隔离与审批工作流的生产级工具集成方案。</td>
    <td align="center">
      <a href="tutorials/arcade-secure-tool-calling"><img src="https://img.shields.io/badge/GitHub-View-blue" height="20"></a>
    </td>
  </tr>
</table>

### 📊 数据处理

<table width="100%">
  <tr style="background-color:#f8f9fa">
    <th width="30%">教程</th>
    <th width="50%">描述</th>
    <th width="20%">查看</th>
  </tr>
  <tr>
    <td>AI Agent 网络数据采集（Bright Data）<img src="https://img.shields.io/badge/NEW-brightgreen" height="16"></td>
    <td>构建能够利用企业级爬取基础设施大规模收集和处理网页数据的 Agent。学习如何集成代理网络、处理验证码，并从复杂网站中提取结构化数据。</td>
    <td align="center">
      <a href="https://github.com/NirDiamant/agents-towards-production/tree/main/tutorials/agent-with-brightdata"><img src="https://img.shields.io/badge/GitHub-View-blue" height="20"></a>
    </td>
  </tr>
  <tr>
    <td>Agent 实时网络数据集成（Tavily）</td>
    <td>让 Agent 能够访问、搜索并提取实时网页数据。构建将实时网络信息与私有知识库相结合的工作流，适用于研究、监控和提供最新推荐等场景。</td>
    <td align="center">
      <a href="https://github.com/NirDiamant/agents-towards-production/tree/main/tutorials/agent-with-tavily-web-access"><img src="https://img.shields.io/badge/GitHub-View-blue" height="20"></a>
    </td>
  </tr>
</table>

### 🔍 RAG（检索增强生成）与知识管理

<table width="100%">
  <tr style="background-color:#f8f9fa">
    <th width="30%">教程</th>
    <th width="50%">描述</th>
    <th width="20%">查看</th>
  </tr>
  <tr>
    <td>基于 Contextual AI 的生产级 RAG Agent</td>
    <td>利用 Contextual AI 的托管平台在 15 分钟内构建企业级 RAG（检索增强生成）系统。学习文档处理、智能索引、Agent 部署，以及使用 LMUnit 测试框架进行自动化评估与金融文档分析。</td>
    <td align="center">
      <a href="tutorials/agent-RAG-with-Contextual"><img src="https://img.shields.io/badge/GitHub-View-blue" height="20"></a>
    </td>
  </tr>
</table>

### 🧠 记忆模块

<table width="100%">
  <tr style="background-color:#f8f9fa">
    <th width="30%">教程</th>
    <th width="50%">描述</th>
    <th width="20%">查看</th>
  </tr>
  <tr>
    <td>Agent 记忆：双轨记忆与语义搜索（Redis）</td>
    <td>为 Agent 实现短期与长期双轨记忆、语义搜索及持久化状态，使其能够记住用户偏好并从对话中学习。</td>
    <td align="center">
      <a href="https://github.com/NirDiamant/agents-towards-production/tree/main/tutorials/agent-memory-with-redis"><img src="https://img.shields.io/badge/GitHub-View-blue" height="20"></a>
    </td>
  </tr>
  <tr>
    <td>基于 Mem0 的自我进化记忆：混合向量与图存储<img src="https://img.shields.io/badge/NEW-brightgreen" height="16"></td>
    <td>构建具备自我进化记忆的 AI Agent，自动提取洞察、解决冲突，并在每次交互中持续演进。学习结合用于语义回忆的向量搜索与用于关系映射的图数据库的混合记忆架构。</td>
    <td align="center">
      <a href="https://github.com/NirDiamant/agents-towards-production/tree/main/tutorials/agent-memory-with-mem0"><img src="https://img.shields.io/badge/GitHub-View-blue" height="20"></a>
    </td>
  </tr>
  <tr>
    <td>基于 Cognee 的 AI 记忆系统</td>
    <td>构建能够向 Python 创始人学习并优化你开发工作流的智能 AI 记忆系统。将分散的开发数据转化为带有上下文洞察的统一知识图谱。</td>
    <td align="center">
      <a href="https://github.com/NirDiamant/agents-towards-production/tree/main/tutorials/ai-memory-with-cognee"><img src="https://img.shields.io/badge/GitHub-View-blue" height="20"></a>
    </td>
  </tr>
</table>

### 🚀 部署方案

<table width="100%">
  <tr style="background-color:#f8f9fa">
    <th width="30%">教程</th>
    <th width="50%">描述</th>
    <th width="20%">查看</th>
  </tr>
  <tr>
    <td>AWS Bedrock AgentCore：托管式 Agent 部署<img src="https://img.shields.io/badge/NEW-brightgreen" height="16"></td>
    <td>在 AWS Bedrock AgentCore 运行时环境中部署和管理 AI Agent。学习如何将本地 Agent 转化为具备自动基础设施、请求追踪和标准化通信模式的生产级托管服务。</td>
    <td align="center">
      <a href="https://github.com/NirDiamant/agents-towards-production/tree/main/tutorials/aws_agentcore"><img src="https://img.shields.io/badge/GitHub-View-blue" height="20"></a>
    </td>
  </tr>
  <tr>
    <td>使用 Docker 容器化 Agent</td>
    <td>将 Agent 容器化以实现跨环境便携性与可扩展性。学习在不同环境中运行 Agent 的基础架构模式。</td>
    <td align="center">
      <a href="https://github.com/NirDiamant/agents-towards-production/tree/main/tutorials/docker-intro"><img src="https://img.shields.io/badge/GitHub-View-blue" height="20"></a>
    </td>
  </tr>
  <tr>
    <td>使用 Ollama 部署本地大语言模型（LLM）</td>
    <td>在本地运行并与大语言模型交互。用本地私有化模型替代云端 API，以保障隐私、控制成本并实现低延迟的 Agent 工作流。</td>
    <td align="center">
      <a href="https://github.com/NirDiamant/agents-towards-production/tree/main/tutorials/on-prem-llm-ollama"><img src="https://img.shields.io/badge/GitHub-View-blue" height="20"></a>
    </td>
  </tr>
</table>

### 👥 多 Agent 协同

<table width="100%">
  <tr style="background-color:#f8f9fa">
    <th width="30%">教程</th>
    <th width="50%">描述</th>
    <th width="20%">查看</th>
  </tr>

  <tr>
    <td>基于 A2A（Agent-to-Agent）协议的多 Agent 通信</td>
    <td>使用开放通信协议模拟可互操作的协同 Agent 工作流与消息交换。</td>
    <td align="center">
      <a href="https://github.com/NirDiamant/agents-towards-production/tree/main/tutorials/a2a"><img src="https://img.shields.io/badge/GitHub-View-blue" height="20"></a>
    </td>
  </tr>
</table>

### 🚀 GPU 部署

<table width="100%">
  <tr style="background-color:#f8f9fa">
    <th width="30%">教程</th>
    <th width="50%">描述</th>
    <th width="20%">查看</th>
  </tr>
  <tr>
    <td>面向 AI Agent 的可扩展 GPU 部署（RunPod）</td>
    <td>在可扩展的 GPU 基础设施上部署 AI Agent。学习配置高性价比、高性能的环境以应对高负载的 Agent 任务。</td>
    <td align="center">
      <a href="https://github.com/NirDiamant/agents-towards-production/tree/main/tutorials/runpod-gpu-deploy"><img src="https://img.shields.io/badge/GitHub-View-blue" height="20"></a>
    </td>
  </tr>
</table>

### 🔒 安全机制

<table width="100%">
  <tr style="background-color:#f8f9fa">
    <th width="30%">教程</th>
    <th width="50%">描述</th>
    <th width="20%">查看</th>
  </tr>
  <tr>
    <td>全面的 Agent 安全防护（LlamaFirewall）</td>
    <td>为 Agent 实施全面的安全护栏，覆盖输入、输出及工具调用。涵盖提示词注入防御、行为对齐与工具访问控制。</td>
    <td align="center">
      <a href="https://github.com/NirDiamant/agents-towards-production/tree/main/tutorials/agent-security-with-llamafirewall"><img src="https://img.shields.io/badge/GitHub-View-blue" height="20"></a>
    </td>
  </tr>
  <tr>
    <td>实战级 Agent 安全评估（Apex）</td>
    <td>动手实践针对 AI Agent 的提示词注入攻击、防御策略及自动化安全测试。</td>
    <td align="center">
      <a href="tutorials/agent-security-apex"><img src="https://img.shields.io/badge/GitHub-View-blue" height="20"></a>
    </td>
  </tr>
</table>

### 👥 多 Agent 协同

<table width="100%">
  <tr style="background-color:#f8f9fa">
    <th width="30%">教程</th>
    <th width="50%">描述</th>
    <th width="20%">查看</th>
  </tr>

  <tr>
    <td>基于 A2A（Agent-to-Agent）协议的多 Agent 通信</td>
    <td>使用开放通信协议模拟可互操作的协同 Agent 工作流与消息交换。</td>
    <td align="center">
      <a href="https://github.com/NirDiamant/agents-towards-production/tree/main/tutorials/a2a"><img src="https://img.shields.io/badge/GitHub-View-blue" height="20"></a>
    </td>
  </tr>
</table>

### 🧩 Agent（智能体）框架

<table width="100%">
  <tr style="background-color:#f8f9fa">
    <th width="30%">教程</th>
    <th width="50%">描述</th>
    <th width="20%">查看</th>
  </tr>
  <tr>
    <td>通过模型上下文协议（MCP）集成工具与 API</td>
    <td>使用标准化协议将 Agent 与外部工具和 API 对接。示例：为高级 Agent 工作流实现无缝的工具与 API 集成。</td>
    <td align="center">
      <a href="https://github.com/NirDiamant/agents-towards-production/tree/main/tutorials/agent-with-mcp"><img src="https://img.shields.io/badge/GitHub-View-blue" height="20"></a>
    </td>
  </tr>
  <tr>
    <td>基于 LangGraph 的有状态 Agent 工作流</td>
    <td>使用有向图架构设计复杂的有状态 Agent 工作流。示例：包含分类、实体提取和摘要的多步文本分析流水线。</td>
    <td align="center">
      <a href="https://github.com/NirDiamant/agents-towards-production/tree/main/tutorials/LangGraph-agent"><img src="https://img.shields.io/badge/GitHub-View-blue" height="20"></a>
    </td>
  </tr>
  <tr>
    <td>使用 FastAPI 将 Agent 部署为 API</td>
    <td>创建并部署高性能的 Agent API，同时支持同步调用与流式响应端点。</td>
    <td align="center">
      <a href="https://github.com/NirDiamant/agents-towards-production/tree/main/tutorials/fastapi-agent"><img src="https://img.shields.io/badge/GitHub-View-blue" height="20"></a>
    </td>
  </tr>
  <tr>
    <td>使用 Koog 在 <a href="https://europe-west1-atp-views-tracker.cloudfunctions.net/working-analytics?notebook=agents-towards-production--readme&click=kotlinlang&target=https%3A%2F%2Fkotlinlang.org%2F%3Futm_source%3Dgithub%26utm_medium%3Dinfluencers%26utm_campaign%3Dkotlin_nir_supporter_1&text=Kotlin">Kotlin</a> 中构建 AI Agent（新增）</td>
    <td>借助 JetBrains 的 Koog 框架，在不到 30 分钟内从零开始构建你的第一个 Kotlin AI Agent。逐步掌握从 Hello World 到工具调用及结构化输出的完整流程。</td>
    <td align="center">
      <a href="https://github.com/NirDiamant/agents-towards-production/tree/main/tutorials/kotlin-agent-with-koog"><img src="https://img.shields.io/badge/GitHub-View-blue" height="20"></a>
    </td>
  </tr>
</table>

### 🛠️ 模型定制

<table width="100%">
  <tr style="background-color:#f8f9fa">
    <th width="30%">教程</th>
    <th width="50%">描述</th>
    <th width="20%">查看</th>
  </tr>
  <tr>
    <td>面向领域专长与效率的 AI Agent 微调</td>
    <td>学习如何针对特定 Agent 行为、领域专业知识以及高效低成本响应进行大模型微调。涵盖数据准备、训练、评估及集成到 Agent 工作流的全过程。</td>
    <td align="center">
      <a href="https://github.com/NirDiamant/agents-towards-production/tree/main/tutorials/fine-tuning-agents"><img src="https://img.shields.io/badge/GitHub-View-blue" height="20"></a>
    </td>
  </tr>
</table>

### 🔍 追踪与调试

<table width="100%">
  <tr style="background-color:#f8f9fa">
    <th width="30%">教程</th>
    <th width="50%">描述</th>
    <th width="20%">查看</th>
  </tr>
  <tr>
    <td>基于 LangSmith 的 Agent 追踪与调试</td>
    <td>为 AI 系统添加全面的可观测性。捕获详细调用链、决策节点与时序数据，用于调试、监控及系统性提升 Agent 性能。</td>
    <td align="center">
      <a href="https://github.com/NirDiamant/agents-towards-production/tree/main/tutorials/tracing-with-langsmith"><img src="https://img.shields.io/badge/GitHub-View-blue" height="20"></a>
    </td>
  </tr>
</table>

### 📊 评估体系

<table width="100%">
  <tr style="background-color:#f8f9fa">
    <th width="30%">教程</th>
    <th width="50%">描述</th>
    <th width="20%">查看</th>
  </tr>
  <tr>
    <td>自动化 Agent 评估与行为分析（IntellAgent）</td>
    <td>通过行为分析、性能指标及可操作洞察实现 Agent 评估自动化，持续提升 Agent 质量。</td>
    <td align="center">
      <a href="https://github.com/NirDiamant/agents-towards-production/tree/main/tutorials/agent-evaluation-intellagent"><img src="https://img.shields.io/badge/GitHub-View-blue" height="20"></a>
    </td>
  </tr>
</table>

### 🖥️ UI 与前端开发

<table width="100%">
  <tr style="background-color:#f8f9fa">
    <th width="30%">教程</th>
    <th width="50%">描述</th>
    <th width="20%">查看</th>
  </tr>
  <tr>
    <td>使用 Streamlit 构建聊天机器人 UI</td>
    <td>搭建新手友好的聊天机器人 Web 应用，包含对话界面、文件上传功能与会话状态管理，适用于交互式 Agent 演示。</td>
    <td align="center">
      <a href="https://github.com/NirDiamant/agents-towards-production/tree/main/tutorials/agent-with-streamlit-ui"><img src="https://img.shields.io/badge/GitHub-View-blue" height="20"></a>
    </td>
  </tr>
</table>

---

## 🚀 快速开始

利用我们经过实战检验的模式与实现方案，将你的 AI Agent 创意转化为生产级系统。

### 📖 在线浏览
直接在 GitHub 上探索教程，了解生产级实现方案、架构决策及集成模式。每个教程均包含完整的文档和代码，你无需任何本地环境配置即可直接学习并适配到你的具体需求中。

### 🛠️ 克隆与构建
下载本仓库以在本地运行教程、尝试不同配置、自定义实现逻辑，并将经过验证的模式直接整合到你自己的 Agent 开发工作流中。

<div align="left">

#### 快速上手

**1. 获取代码**

```bash
git clone https://github.com/NirDiamant/agents-towards-production.git
cd agents-towards-production
```

**2. 安装依赖项**
导航至目标教程目录并配置环境：

```bash
# 示例：多工具 Agent 编排
cd tutorials/agentic-applications-by-xpander.ai
pip install -r meeting-recorder-agent/requirements.txt
```

**3. 部署与测试**
通过其推荐的方式运行教程：

```bash
# 运行交互式 Notebook 进行实验
jupyter notebook tutorial.ipynb

# 执行生产脚本以进行集成测试
python app.py
```

</div>

---

## 📚 推荐阅读

*本列表包含亚马逊联盟营销链接。作为亚马逊关联会员，我将从符合条件的购买中赚取佣金。以下每本书均为本人亲阅并真心推荐给该领域工程师的佳作。本仓库的配套书籍已在本文档顶部单独列出。*

- [Build a Large Language Model (From Scratch)](https://europe-west1-atp-views-tracker.cloudfunctions.net/working-analytics?notebook=agents-towards-production--readme&click=amazon-product&target=https%3A%2F%2Fwww.amazon.com%2Fdp%2F1633437167%3Ftag%3Ddiamantai-atp-20&text=Build%20a%20Large%20Language%20Model%20%28From%20Scratch%29) by Sebastian Raschka. Build a GPT-style model end to end in PyTorch. -> 由 Sebastian Raschka 撰写。使用 PyTorch 从零开始完整构建类 GPT 模型。
- [AI Engineering: Building Applications with Foundation Models](https://europe-west1-atp-views-tracker.cloudfunctions.net/working-analytics?notebook=agents-towards-production--readme&click=amazon-product&target=https%3A%2F%2Fwww.amazon.com%2Fdp%2F1098166302%3Ftag%3Ddiamantai-atp-20&text=AI%20Engineering%3A%20Building%20Applications%20with%20Foundation%20Models) by Chip Huyen. Canonical reference for productionizing foundation-model apps. -> 由 Chip Huyen 撰写。将基础模型应用投入生产的权威参考指南。
- [Hands-On Large Language Models](https://europe-west1-atp-views-tracker.cloudfunctions.net/working-analytics?notebook=agents-towards-production--readme&click=amazon-product&target=https%3A%2F%2Fwww.amazon.com%2Fdp%2F1098150961%3Ftag%3Ddiamantai-atp-20&text=Hands-On%20Large%20Language%20Models) by Jay Alammar and Maarten Grootendorst. Visual, practical LLM walkthroughs. -> 由 Jay Alammar 和 Maarten Grootendorst 撰写。图文并茂的 LLM（大语言模型）实战指南。
- [Natural Language Processing with Transformers](https://europe-west1-atp-views-tracker.cloudfunctions.net/working-analytics?notebook=agents-towards-production--readme&click=amazon-product&target=https%3A%2F%2Fwww.amazon.com%2Fdp%2F1098136799%3Ftag%3Ddiamantai-atp-20&text=Natural%20Language%20Processing%20with%20Transformers) by Lewis Tunstall, Leandro von Werra, and Thomas Wolf. From the Hugging Face team. -> 由 Lewis Tunstall、Leandro von Werra 和 Thomas Wolf 撰写。Hugging Face 团队出品。
- [Designing Machine Learning Systems](https://europe-west1-atp-views-tracker.cloudfunctions.net/working-analytics?notebook=agents-towards-production--readme&click=amazon-product&target=https%3A%2F%2Fwww.amazon.com%2Fdp%2F1098107969%3Ftag%3Ddiamantai-atp-20&text=Designing%20Machine%20Learning%20Systems) by Chip Huyen. ML systems in production, still the standard reference. -> 由 Chip Huyen 撰写。生产级机器学习系统设计的标准参考书。

## 💼 申请开放的 AI 工程岗位

**AI 优先型公司正通过 DiamantAI Collective 进行招聘。**

[![See open jobs and apply](https://img.shields.io/badge/%E2%9E%A1%EF%B8%8F%20%20See%20open%20jobs%20and%20apply-7c3aed?style=for-the-badge)](https://europe-west1-atp-views-tracker.cloudfunctions.net/working-analytics?notebook=main-readme--jobs-panel&click=jobs-panel-see-all-roles&target=https%3A%2F%2Fdiamant-ai.com%2Fjobs&text=See%20open%20jobs%20and%20apply)

---

## 🤝 贡献指南

我们欢迎所有支持 Agent（智能体）开发的工具、基础设施和框架的贡献。这包括监控服务、部署平台、安全工具、数据库、API 以及其他使生产级 Agent 系统得以运行的横向服务。

更多详情请参阅我们的 [贡献指南](CONTRIBUTING.md)。

---

## ⚠️ 免责声明

**仅限教育用途。** 作者不对任何使用、滥用或后果承担任何责任。我们不对文中提及的第三方公司、工具或服务进行背书、核实或担保。对由此产生的损害、损失、安全漏洞或欺诈行为概不负责。

**你的责任：** 请自行开展尽职调查，验证合法性，在隔离环境中测试并确保符合法律法规。安全工具必须在获得适当授权的前提下合规使用。

使用本仓库即表示你同意此免责声明。

---

## 📜 许可证

本项目采用自定义非商业许可证，详情请参阅 [LICENSE](LICENSE) 文件。

---

<div align="center">

### ⭐️ 如果你觉得本仓库有帮助，欢迎点亮 Star！

<br>

![](https://europe-west1-atp-views-tracker.cloudfunctions.net/working-analytics?notebook=main-readme)


<p><i>关键词：AI Agent（智能体）、生产级部署、LLM（大语言模型）、工作流编排、多 Agent 系统、记忆模块、监控、安全机制、可观测性、Agent 框架、基础设施、无服务器架构、企业级 AI、工具集成</i></p>

</div>