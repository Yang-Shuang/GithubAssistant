# Google Cloud 上的生成式 AI

> **[Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform)**（Vertex AI 的最新演进版本）已正式发布！
>
> 请查看 [`Google-Cloud-AI/agent-platform`](https://goo.gle/agent-platform-github) 仓库，获取在 Google Cloud 上构建 Agent 的精选资源列表。

<!-- markdownlint-disable MD033 -->

本仓库包含笔记本（notebooks）、代码示例、示例应用及其他资源，展示如何使用 [生成式 AI](https://cloud.google.com/ai/generative-ai) 与 [Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform) 来使用、开发和管理工作流。

## 介绍视频

[![什么是 Gemini Enterprise Agent Platform？](https://img.youtube.com/vi/j8qW5poBkEU/maxresdefault.jpg)](https://goo.gle/agent-platform-video)

<table>
  <tr>
    <th></th>
    <th style="text-align: center;">说明</th>
  </tr>
  <tr>
    <td>
      <img src="https://storage.googleapis.com/github-repo/img/gemini/Spark__Gradient_Alpha_100px.gif" width="45px" alt="Gemini">
      <br>
      <a href="gemini/"><code>gemini/</code></a>
    </td>
    <td>
      通过入门笔记本、用例、函数调用、示例应用等探索 Gemini。
    </td>
  </tr>
  <tr>
    <td>
      <img src="https://www.gstatic.com/images/branding/gcpiconscolors/service_discovery/v1/24px.svg" width="40px" alt="Search">
      <br>
      <a href="search/"><code>search/</code></a>
    </td>
    <td>如果您对使用 <a href="https://cloud.google.com/enterprise-search">Agent Search</a>（Google 托管的解决方案，可帮助您快速为网站和企业数据构建搜索引擎）感兴趣，请使用此文件夹。（原名为 Generative AI App Builder 上的企业搜索）。</td>
  </tr>
  <tr>
    <td>
      <img src="https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/nature_people/default/40px.svg" alt="RAG Grounding">
      <br>
      <a href="rag-grounding/"><code>rag-grounding/</code></a>
    </td>
    <td>如需了解检索增强生成（RAG, Retrieval Augmented Generation）与 Grounding 的相关信息，请查阅此文件夹。该目录收录了聚焦于此主题的其他目录下的笔记本和示例索引。</td>
  </tr>
  <tr>
    <td>
      <img src="https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/image/default/40px.svg" alt="Vision">
      <br>
      <a href="vision/"><code>vision/</code></a>
    </td>
    <td>
      如果您对使用 Imagen 和 Veo 的功能从零开始构建自己的解决方案感兴趣，请使用此文件夹。
    </td>
  </tr>
  <tr>
    <td>
      <img src="https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/mic/default/40px.svg" alt="Speech">
      <br>
      <a href="audio/"><code>audio/</code></a>
    </td>
    <td>
      如果您对使用 Chirp（Google 通用语音模型 USM 的一个版本）的功能从零开始构建自己的解决方案感兴趣，请使用此文件夹。
    </td>
  </tr>
  <tr>
    <td>
      <img src="https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/build/default/40px.svg" alt="Setup Env">
      <br>
      <a href="setup-env/"><code>setup-env/</code></a>
    </td>
    <td>关于如何在 Google Cloud、Gen AI Python SDK 以及 Google Colab 和 Workbench 上配置环境的说明。</td>
  </tr>
  <tr>
    <td>
      <img src="https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/media_link/default/40px.svg" alt="Resources">
      <br>
      <a href="RESOURCES.md"><code>RESOURCES.md</code></a>
    </td>
    <td>有关 Google Cloud 生成式 AI 的学习资源（例如博客、YouTube 播放列表）。</td>
  </tr>
</table>
<!-- markdownlint-enable MD033 -->

## 相关仓库

- ✨ [Agent Development Kit (ADK) Samples](https://github.com/google/adk-samples): 此仓库提供基于 Agent Development Kit 构建的即用型 Agent，旨在加速您的开发流程。这些 Agent 覆盖了从简单对话机器人到复杂多 Agent 工作流的各类常见用例与复杂度。
- [🚀 Agent Starter Pack](https://github.com/GoogleCloudPlatform/agent-starter-pack)
  - 一套面向 Google Cloud 的生产就绪型生成式 AI Agent 模板集合。
  - 通过提供整体、生产就绪的解决方案来加速开发，解决构建和部署 Gen AI Agent 时的常见挑战（部署与运维、评估、定制化、可观测性）。
- [Gemini Cookbook](https://github.com/google-gemini/cookbook/)
- [genai-factory](https://github.com/googleCloudPlatform/genai-factory) - 一套端到端的基础设施蓝图集合，使用 IaC（基础设施即代码）并遵循安全最佳实践，用于在 GCP 上部署生成式 AI 基础设施。
- [Google Cloud Applied AI Engineering](https://github.com/GoogleCloudPlatform/applied-ai-engineering-samples)
- [Vertex AI GenMedia Creative Studio](https://github.com/GoogleCloudPlatform/vertex-ai-creative-studio) - 体验 Google 的生成式媒体基础模型及自定义工作流。
- [MCP Servers for GenMedia](https://goo.gle/vertex-genmedia-mcp) - 为 Agent 赋能，集成生成式媒体工具。
- [Generative AI for Marketing using Google Cloud](https://github.com/GoogleCloudPlatform/genai-for-marketing)
- [Generative AI for Developer Productivity](https://github.com/GoogleCloudPlatform/genai-for-developers)
- Vertex AI Core
  - [Vertex AI Samples](https://github.com/GoogleCloudPlatform/vertex-ai-samples)
  - [MLOps with Vertex AI](https://github.com/GoogleCloudPlatform/mlops-with-vertex-ai)
  - [Developing NLP solutions with T5X and Vertex AI](https://github.com/GoogleCloudPlatform/t5x-on-vertex-ai)
  - [AlphaFold batch inference with Vertex AI Pipelines](https://github.com/GoogleCloudPlatform/vertex-ai-alphafold-inference-pipeline)
  - [Serving Spark ML models using Vertex AI](https://github.com/GoogleCloudPlatform/vertex-ai-spark-ml-serving)
  - [Sensitive Data Protection (Cloud DLP) for Vertex AI Generative Models (PaLM2)](https://github.com/GoogleCloudPlatform/Sensitive-Data-Protection-for-Vertex-AI-PaLM2)
- Conversational AI（对话式 AI）
  - [Contact Center AI Samples](https://github.com/GoogleCloudPlatform/contact-center-ai-samples)
  - [Reimagining Customer Experience 360](https://github.com/GoogleCloudPlatform/dialogflow-ccai-omnichannel)
- Document AI（文档 AI）
  - [Document AI Samples](https://github.com/GoogleCloudPlatform/document-ai-samples)
- Gemini in Google Cloud（Google Cloud 中的 Gemini）
  - [Cymbal Superstore](https://github.com/GoogleCloudPlatform/cymbal-superstore)
- Cloud Databases（云数据库）
  - [Gen AI Databases Retrieval App](https://github.com/GoogleCloudPlatform/genai-databases-retrieval-app)
- Other（其他）
  - [ai-on-gke](https://github.com/GoogleCloudPlatform/ai-on-gke)
  - [ai-infra-cluster-provisioning](https://github.com/GoogleCloudPlatform/ai-infra-cluster-provisioning)
  - [solutions-genai-llm-workshop](https://github.com/GoogleCloudPlatform/solutions-genai-llm-workshop)
  - [terraform-genai-doc-summarization](https://github.com/GoogleCloudPlatform/terraform-genai-doc-summarization)
  - [terraform-genai-knowledge-base](https://github.com/GoogleCloudPlatform/terraform-genai-knowledge-base)
  - [genai-product-catalog](https://github.com/GoogleCloudPlatform/genai-product-catalog)
  - [solutionbuilder-terraform-genai-doc-summarization](https://github.com/GoogleCloudPlatform/solutionbuilder-terraform-genai-doc-summarization)
  - [solutions-viai-edge-provisioning-configuration](https://github.com/GoogleCloudPlatform/solutions-viai-edge-provisioning-configuration)
  - [mis-ai-accelerator](https://github.com/GoogleCloudPlatform/mis-ai-accelerator)
  - [dataflow-opinion-analysis](https://github.com/GoogleCloudPlatform/dataflow-opinion-analysis)
  - [genai-beyond-basics](https://github.com/meteatamel/genai-beyond-basics)
  - [Gemini by Example](https://geminibyexample.com)

## 贡献指南

欢迎提交贡献！请参阅[贡献指南](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/CONTRIBUTING.md)。

## 获取帮助

请使用[Issues 页面](https://github.com/GoogleCloudPlatform/generative-ai/issues)提供建议、反馈或提交 Bug 报告。

## 免责声明

本仓库本身并非 Google 官方支持的产品。本仓库中的代码仅用于演示目的。