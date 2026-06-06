<div align="center">
  
<a href="https://vectify.ai/pageindex" target="_blank">
  <img src="https://github.com/user-attachments/assets/46201e72-675b-43bc-bfbd-081cc6b65a1d" alt="PageIndex Banner" />
</a>

<br/>
<br/>

<p align="center">
  <a href="https://trendshift.io/repositories/14736" target="_blank"><img src="https://trendshift.io/api/badge/repositories/14736" alt="VectifyAI%2FPageIndex | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

# PageIndex：无向量、基于推理的 RAG（检索增强生成）

<p align="center"><b>基于推理的 RAG ◦ 无需向量数据库，无需分块 ◦ 上下文感知检索 ◦ 拟人化体验</b></p>

<h4 align="center">
  <a href="https://vectify.ai">🌐 官网</a>&nbsp; • &nbsp;
  <a href="https://chat.pageindex.ai">🖥️ 对话平台</a>&nbsp; • &nbsp;
  <a href="https://pageindex.ai/developer">🔌 MCP & API</a>&nbsp; • &nbsp;
  <a href="https://docs.pageindex.ai">📖 文档</a>&nbsp; • &nbsp;
  <a href="https://discord.com/invite/VuXuf29EUj">💬 Discord</a>&nbsp; • &nbsp;
  <a href="https://ii2abc2jejf.typeform.com/to/tK3AXl8T">✉️ 联系我们</a>&nbsp;
</h4>
  
</div>


<details open>
<summary><h2>📢 更新日志</h2></summary>

- 🔥 [**智能体无向量 RAG**](https://github.com/VectifyAI/PageIndex/blob/main/examples/agentic_vectorless_rag_demo.py) —— 一个使用自托管 PageIndex 和 OpenAI Agents SDK 的简单 *智能体、无向量 RAG* [示例]（见 [#agentic-vectorless-rag-an-example](#agentic-vectorless-rag-示例)）。
- [**将 PageIndex 扩展至数百万文档**](https://pageindex.ai/blog/pageindex-filesystem) —— *PageIndex 文件系统* 是一个文件级树状层级，使 PageIndex 能够对整个语料库（而不仅是单个文档）进行推理，从而实现海量规模的文档搜索。
- [PageIndex 对话平台](https://chat.pageindex.ai) —— 面向专业长文档的拟人化文档分析智能体[平台](https://chat.pageindex.ai)。也可通过 [MCP](https://pageindex.ai/developer) 或 [API](https://pageindex.ai/developer) 接入。
- [PageIndex 框架](https://pageindex.ai/blog/pageindex-intro) —— 深入解析 PageIndex：一种智能体、上下文内树状索引，使大语言模型（LLM）能够对长文档执行基于推理的上下文感知检索。

 <!-- **🧪 Cookbooks:**
- [Vectorless RAG](https://docs.pageindex.ai/cookbook/vectorless-rag-pageindex): A minimal, hands-on example of reasoning-based RAG using PageIndex. No vectors, no chunking, and human-like retrieval.
- [Vision-based Vectorless RAG](https://docs.pageindex.ai/cookbook/vision-rag-pageindex): OCR-free, vision-only RAG with PageIndex's reasoning-native retrieval workflow that works directly over PDF page images. -->

</details>

---

# 📑 PageIndex 简介

你是否对专业长文档的向量数据库检索准确率感到困扰？传统的基于向量的 RAG 依赖语义*相似度*而非真正的*相关性*。但**相似度 ≠ 相关性** —— 检索真正需要的是**相关性**，而这需要**推理**。在处理需要领域知识和多步推理的专业文档时，相似性搜索往往力不从心——会遗漏相关但不相似的內容，却返回相似却不相关的結果。

受 AlphaGo 启发，我们提出了 **[PageIndex](https://vectify.ai/pageindex)** —— 一种**无向量、基于推理的 RAG**系统。它从长文档中构建**分层树状索引**，并利用大语言模型（LLM）**在该索引上进行推理**，以实现智能体驱动、上下文感知的检索。该检索过程可追溯且可解释，无需向量数据库或分块处理。
PageIndex 通过*树状搜索*模拟了专家如何从复杂文档中导航并提取知识，使大语言模型能够*思考*和*推理*出最相关的文档部分。检索分为两步：

1. 生成文档的“目录”**树状结构索引**
2. 通过**树状搜索**执行基于推理的检索

<div align="center">
  <a href="https://pageindex.ai/blog/pageindex-intro" target="_blank" title="The PageIndex Framework">
    <img src="https://docs.pageindex.ai/images/cookbook/vectorless-rag.png" width="70%">
  </a>
</div>

### 🎯 核心特性

与传统基于向量的 RAG 相比，**PageIndex** 具备以下特性：
- **无需向量数据库**：利用文档结构和 LLM 推理进行检索，而非向量相似度搜索。
- **无需分块（Chunking）**：文档按自然章节组织，而非人工切分的文本块。
- **更强的可追溯性与可解释性**：检索由推理驱动，并基于明确的页码和章节引用，使每个结果都可追溯、可理解——彻底告别不透明、近似度高的向量“直觉式检索”。
- **上下文感知检索**：检索依赖于你的完整上下文（如对话历史和领域知识），并能轻松融入新上下文。
- **拟人化检索**：模拟专家如何从复杂文档中导航并提取知识。

PageIndex 驱动的基于推理的 RAG 系统在 FinanceBench 基准测试中取得了**最先进的（SOTA）**[98.7% 准确率](https://github.com/VectifyAI/Mafin2.5-FinanceBench)，在专业文档分析方面大幅超越基于向量的 RAG 解决方案（[博客文章](https://vectify.ai/blog/Mafin2.5)）。

### 📍 探索 PageIndex

欲了解更多详情，请参阅 [PageIndex 框架](https://pageindex.ai/blog/pageindex-intro) 的详细介绍。查看本 GitHub 仓库获取开源代码，并参考 [Cookbooks](https://docs.pageindex.ai/cookbook)、[教程](https://docs.pageindex.ai/tutorials) 和 [博客](https://pageindex.ai/blog) 获取更多使用指南与示例。

PageIndex 服务提供类 ChatGPT 的[对话平台](https://chat.pageindex.ai)，也可通过 [MCP](https://pageindex.ai/developer) 或 [API](https://pageindex.ai/developer) 进行集成。

### 🛠️ 部署选项
- **自托管** —— 使用本开源仓库在本地运行（采用标准 PDF 解析）。
- **云服务** —— 生产级流水线，提供增强的 OCR、树状结构构建与检索功能以获得最佳效果。可通过我们的[对话平台](https://chat.pageindex.ai/) 即时体验，或通过 [MCP](https://pageindex.ai/developer) / [API](https://pageindex.ai/developer) 集成。
- **企业版** —— 支持私有化或本地部署。[联系我们](https://ii2abc2jejf.typeform.com/to/tK3AXl8T) 或[预约演示](https://calendly.com/pageindex/meet) 了解详情。

### 🧪 快速上手
- 🔥 [**智能体无向量 RAG**](examples/agentic_vectorless_rag_demo.py) (**最新**) —— 一个使用自托管 PageIndex 和 OpenAI Agents SDK 的简单但完整的 **智能体无向量 RAG** [示例]（见 [#agentic-vectorless-rag-an-example](#agentic-vectorless-rag-示例)）。
- 尝试 [Vectorless RAG](https://github.com/VectifyAI/PageIndex/blob/main/cookbook/pageindex_RAG_simple.ipynb) Notebook —— 使用 PageIndex 进行基于推理的 RAG 的*最小化、可运行*示例。
- 查看 [Vision-based Vectorless RAG](https://github.com/VectifyAI/PageIndex/blob/main/cookbook/vision_RAG_pageindex.ipynb) —— 无需 OCR；一个基于视觉且原生支持推理的 RAG 流水线，可直接处理页面图像。
  
<div align="center">
  <a href="https://github.com/VectifyAI/PageIndex/blob/main/examples/agentic_vectorless_rag_demo.py" target="_blank" rel="noopener">
    <img src="https://img.shields.io/badge/View_on_GitHub-Agentic_Vectorless_RAG-blue?style=for-the-badge&logo=github" alt="View on GitHub: Agentic Vectorless RAG" />
  </a>
  <br/>
  <a href="https://colab.research.google.com/github/VectifyAI/PageIndex/blob/main/cookbook/pageindex_RAG_simple.ipynb" target="_blank" rel="noopener">
    <img src="https://img.shields.io/badge/Open_In_Colab-Vectorless_RAG-orange?style=for-the-badge&logo=googlecolab" alt="Open in Colab: Vectorless RAG" />
  </a>
  &nbsp;&nbsp;
  <a href="https://colab.research.google.com/github/VectifyAI/PageIndex/blob/main/cookbook/vision_RAG_pageindex.ipynb" target="_blank" rel="noopener">
    <img src="https://img.shields.io/badge/Open_In_Colab-Vision_RAG-orange?style=for-the-badge&logo=googlecolab" alt="Open in Colab: Vision RAG" />
  </a>
</div>

---

# 🌲 PageIndex 树状结构

PageIndex 可将长篇 PDF 文档转换为语义**树状结构**，类似于*“目录”*，但针对大语言模型（LLM）进行了优化。它非常适合用于：财务报告、监管文件、学术教材、法律或技术手册，以及任何超出 LLM 上下文长度限制的文档。

以下是一个示例 PageIndex 树状结构。更多示例[文档](https://github.com/VectifyAI/PageIndex/tree/main/examples/documents) 和生成的[树状结构](https://github.com/VectifyAI/PageIndex/tree/main/examples/documents/results) 请见仓库。

```jsonc
...
{
  "title": "Financial Stability",
  "node_id": "0006",
  "start_index": 21,
  "end_index": 22,
  "summary": "The Federal Reserve ...",
  "nodes": [
    {
      "title": "Monitoring Financial Vulnerabilities",
      "node_id": "0007",
      "start_index": 22,
      "end_index": 28,
      "summary": "The Federal Reserve's monitoring ..."
    },
    {
      "title": "Domestic and International Cooperation and Coordination",
      "node_id": "0008",
      "start_index": 28,
      "end_index": 31,
      "summary": "In 2023, the Federal Reserve collaborated ..."
    }
  ]
}
...
```

你可通过本开源仓库生成 PageIndex 树状结构；或使用我们的 [API](https://pageindex.ai/developer)，借助增强的 OCR 与树状结构构建流水线获取更高质量的结果。

---

# ⚙️ 包使用指南

> **注意**：本软件包采用标准 PDF 解析。对于包含复杂排版的 PDF，你的[云服务](https://pageindex.ai/developer)（通过 MCP 和 API）提供增强的 OCR、树状结构构建与检索功能。

请按照以下步骤从 PDF 文档生成 PageIndex 树：

### 1. 安装依赖项

```bash
pip3 install --upgrade -r requirements.txt
```

### 2. 设置你的 LLM API 密钥

在项目根目录创建 `.env` 文件并填入你的 LLM API 密钥。通过 [LiteLLM](https://docs.litellm.ai/docs/providers) 支持多模型接入：

```bash
OPENAI_API_KEY=your_openai_key_here
```

### 3. 为你的 PDF 生成 PageIndex 结构

```bash
python3 run_pageindex.py --pdf_path /path/to/your/document.pdf
```

<details>
<summary>可选参数</summary>
<br>
你可通过附加的可选参数自定义处理流程：

```
--model                 使用的 LLM 模型（默认值：gpt-4o-2024-11-20）
--toc-check-pages       检查目录的页码数（默认值：20）
--max-pages-per-node    每个节点的最大页数（默认值：10）
--max-tokens-per-node   每个节点的最大 Token 数（默认值：20000）
--if-add-node-id        是否添加节点 ID（是/否，默认：是）
--if-add-node-summary   是否添加节点摘要（是/否，默认：是）
--if-add-doc-description 是否添加文档描述（是/否，默认：是）
```
</details>

<details>
<summary>Markdown 支持</summary>
<br>
我们还为 PageIndex 提供了 Markdown 格式支持。你可以使用 `--md_path` 参数为 Markdown 文件生成树状结构。

```bash
python3 run_pageindex.py --md_path /path/to/your/document.md
```

> **注意**：在此模式下，我们使用 “#” 来判定节点标题及其层级。例如，“##” 为第2级，“###” 为第3级，依此类推。请确保你的 Markdown 文件格式正确。如果你的 Markdown 文件是从 PDF 或 HTML 转换而来，我们不建议使用此模式，因为大多数现有转换工具无法保留原始层级结构。建议改用我们的 [PageIndex OCR](https://pageindex.ai/blog/ocr) 将 PDF 转换为 Markdown 后再使用此模式。
</details>

## Agentic Vectorless RAG：示例

如需一个简单的端到端 *智能体无向量 RAG* 示例（使用自托管 PageIndex 与 OpenAI Agents SDK），请参阅 [`examples/agentic_vectorless_rag_demo.py`](examples/agentic_vectorless_rag_demo.py)。

```bash
# Install optional dependency
pip3 install openai-agents

# Run the demo
python3 examples/agentic_vectorless_rag_demo.py
```

<!--
# ☁️ Improved Tree Generation with PageIndex OCR

This repo is designed for generating PageIndex tree structure for simple PDFs, but many real-world use cases involve complex PDFs that are hard to parse by classic Python tools. However, extracting high-quality text from PDF documents remains a non-trivial challenge. Most OCR tools only extract page-level content, losing the broader document context and hierarchy.

To address this, we introduced PageIndex OCR — the first long-context OCR model designed to preserve the global structure of documents. PageIndex OCR significantly outperforms other leading OCR tools, such as those from Mistral and Contextual AI, in recognizing true hierarchy and semantic relationships across document pages.

- Experience next-level OCR quality with PageIndex OCR at our [Dashboard](https://dash.pageindex.ai/).
- Integrate PageIndex OCR seamlessly into your stack via our [API](https://docs.pageindex.ai/quickstart).

<p align="center">
  <img src="https://github.com/user-attachments/assets/eb35d8ae-865c-4e60-a33b-ebbd00c41732" width="80%">
</p>
-->

---

# 📈 案例研究：PageIndex 领跑金融问答基准测试

[Mafin 2.5](https://vectify.ai/mafin) 是一款由 **PageIndex** 驱动的金融文档分析用基于推理的 RAG 系统。它在 [FinanceBench](https://arxiv.org/abs/2311.11944) 基准测试中取得了最先进的（SOTA）[**98.7% 准确率**](https://vectify.ai/blog/Mafin2.5)，显著优于传统基于向量的 RAG 系统。

PageIndex 的分层索引与推理驱动检索功能，使其能够从复杂的财务报告（如美国证监会备案文件和财报披露）中精准导航并提取相关上下文。

查看完整的 [基准测试结果](https://github.com/VectifyAI/Mafin2.5-FinanceBench) 和我们的 [博客文章](https://vectify.ai/blog/Mafin2.5)，了解详细的对比数据与性能指标。

<div align="center">
  <a href="https://github.com/VectifyAI/Mafin2.5-FinanceBench">
    <img src="https://github.com/user-attachments/assets/571aa074-d803-43c7-80c4-a04254b782a3" width="70%">
  </a>
</div>

---

# 🧭 资源链接

* 📝 [博客](https://pageindex.ai/blog)：技术文章、研究见解与产品更新。
* 🔧 [开发者中心](https://pageindex.ai/developer)：MCP 配置、API 文档及集成指南。
* 🧪 [示例手册](https://docs.pageindex.ai/cookbook)：可运行的实操示例与高级用例。
* 📖 [教程](https://docs.pageindex.ai/tutorials)：实用指南与策略，涵盖 *文档搜索* 和 *树状搜索*。

---

# ⭐ 支持我们

如果你喜欢我们的项目，请给我们点个 Star 🌟！感谢你的支持！  

<p>
  <img src="https://github.com/user-attachments/assets/eae4ff38-48ae-4a7c-b19f-eab81201d794" width="80%">
</p>

引用格式如下：
```
Mingtian Zhang, Yu Tang and PageIndex Team,
"PageIndex: Next-Generation Vectorless, Reasoning-based RAG",
PageIndex Blog, Sep 2025.
```

<details>
<summary>或使用 BibTeX 引用。</summary>

```bibtex
@article{zhang2025pageindex,
  author = {Mingtian Zhang and Yu Tang and PageIndex Team},
  title = {PageIndex: Next-Generation Vectorless, Reasoning-based RAG},
  journal = {PageIndex Blog},
  year = {2025},
  month = {September},
  note = {https://pageindex.ai/blog/pageindex-intro},
}
```
</details>


### 🌐 生态系统

PageIndex 生态系统的其他开源项目：[OpenKB](https://github.com/VectifyAI/OpenKB) 是一款将文档编译为互联维基的 LLM 知识库。[ChatIndex](https://github.com/VectifyAI/ChatIndex) 将树状索引与检索能力引入长对话历史。[ConDB](https://github.com/VectifyAI/ConDB) 是一款专为基于树的检索设计的 KV-cache 原生上下文数据库。[PageIndex MCP](https://github.com/VectifyAI/pageindex-mcp) 是 PageIndex 的 MCP 服务器。

### 联系我们

<div align="center">

[![Website](https://img.shields.io/badge/Website-2D72CF?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHBhdGggZmlsbD0iI2ZmZiIgZD0iTTEyIDEgMSAxMWgyLjV2MTJoNnYtN2g1djdoNlYxMUgyM3oiLz48L3N2Zz4%3D)](https://pageindex.ai)&nbsp;
[![Twitter](https://img.shields.io/badge/Twitter-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/PageIndexAI)&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHBhdGggZmlsbD0iI2ZmZiIgZD0iTTIwLjQ1IDIwLjQ1aC0zLjU1di01LjU3YzAtMS4zMy0uMDMtMy4wNC0xLjg1LTMuMDQtMS44NSAwLTIuMTQgMS40NS0yLjE0IDIuOTR2NS42N0g5LjM1VjloMy40MXYxLjU2aC4wNWMuNDgtLjkgMS42NC0xLjg1IDMuMzctMS44NSAzLjYgMCA0LjI3IDIuMzcgNC4yNyA1LjQ2djYuMjh6TTUuMzQgNy40M2EyLjA2IDIuMDYgMCAxIDEgMC00LjEzIDIuMDYgMi4wNiAwIDAgMSAwIDQuMTN6TTcuMTIgMjAuNDVIMy41NlY5aDMuNTZ2MTEuNDV6TTIyLjIyIDBIMS43N0MuNzkgMCAwIC43NyAwIDEuNzN2MjAuNTRDMCAyMy4yMy43OSAyNCAxLjc3IDI0aDIwLjQ1QzIzLjIgMjQgMjQgMjMuMjMgMjQgMjIuMjdWMS43M0MyNCAuNzcgMjMuMiAwIDIyLjIyIDB6Ii8%2BPC9zdmc%2B)](https://www.linkedin.com/company/vectify-ai/)&nbsp;
[![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/invite/VuXuf29EUj)&nbsp;
[![Book a Demo](https://img.shields.io/badge/Book_a_Demo-6E7E96?style=for-the-badge&logo=googlecalendar&logoColor=white)](https://calendly.com/pageindex/meet)&nbsp;
[![Contact Us](https://img.shields.io/badge/Contact_Us-3B82F6?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjIgNCAyMCAxNiI%2BPHBhdGggZmlsbD0iI2ZmZiIgZD0iTTIwIDHINGMtMS4xIDAtMiAuOS0yIDJ2MTJjMCAxLjEuOSAyIDIgMGgyMGMxLjEgMCAyLS45IDItMlY2YzAtMS4xLS45LTItMi0yeiBtMCAtNGwtOCA1bC04LTV2Nmw4IDUgOC01eiIvPjwvc3ZnPg==)](https://ii2abc2jejf.typeform.com/to/tK3AXl8T)

</div>

---

© 2026 [Vectify AI](https://vectify.ai)