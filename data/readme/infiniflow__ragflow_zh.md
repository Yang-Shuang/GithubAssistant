<div align="center">
<a href="https://cloud.ragflow.io/">
<img src="web/src/assets/logo-with-text.svg" width="520" alt="ragflow logo">
</a>
</div>

<p align="center">
  <a href="./README.md"><img alt="README in English" src="https://img.shields.io/badge/English-DBEDFA"></a>
  <a href="./README_zh.md"><img alt="简体中文版自述文件" src="https://img.shields.io/badge/简体中文-DFE0E5"></a>
  <a href="./README_tzh.md"><img alt="繁體版中文自述文件" src="https://img.shields.io/badge/繁體中文-DFE0E5"></a>
  <a href="./README_ja.md"><img alt="日本語のREADME" src="https://img.shields.io/badge/日本語-DFE0E5"></a>
  <a href="./README_ko.md"><img alt="한국어" src="https://img.shields.io/badge/한국어-DFE0E5"></a>
  <a href="./README_fr.md"><img alt="README en Français" src="https://img.shields.io/badge/Français-DFE0E5"></a>
  <a href="./README_id.md"><img alt="Bahasa Indonesia" src="https://img.shields.io/badge/Bahasa Indonesia-DFE0E5"></a>
  <a href="./README_pt_br.md"><img alt="Português(Brasil)" src="https://img.shields.io/badge/Português(Brasil)-DFE0E5"></a>
  <a href="./README_ar.md"><img alt="README in Arabic" src="https://img.shields.io/badge/Arabic-DFE0E5"></a>
  <a href="./README_tr.md"><img alt="Türkçe README" src="https://img.shields.io/badge/Türkçe-DFE0E5"></a>
</p>

<p align="center">
    <a href="https://x.com/intent/follow?screen_name=infiniflowai" target="_blank">
        <img src="https://img.shields.io/twitter/follow/infiniflow?logo=X&color=%20%23f5f5f5" alt="follow on X(Twitter)">
    </a>
    <a href="https://cloud.ragflow.io" target="_blank">
        <img alt="Static Badge" src="https://img.shields.io/badge/Get-Started-4e6b99">
    </a>
    <a href="https://hub.docker.com/r/infiniflow/ragflow" target="_blank">
        <img src="https://img.shields.io/docker/pulls/infiniflow/ragflow?label=Docker%20Pulls&color=0db7ed&logo=docker&logoColor=white&style=flat-square" alt="docker pull infiniflow/ragflow:v0.25.4">
    </a>
    <a href="https://github.com/infiniflow/ragflow/releases/latest">
        <img src="https://img.shields.io/github/v/release/infiniflow/ragflow?color=blue&label=Latest%20Release" alt="Latest Release">
    </a>
    <a href="https://github.com/infiniflow/ragflow/blob/main/LICENSE">
        <img height="21" src="https://img.shields.io/badge/License-Apache--2.0-ffffff?labelColor=d4eaf7&color=2e6cc4" alt="license">
    </a>
    <a href="https://deepwiki.com/infiniflow/ragflow">
        <img alt="Ask DeepWiki" src="https://deepwiki.com/badge.svg">
    </a>
</p>

<h4 align="center">
  <a href="https://cloud.ragflow.io">云托管服务</a> |
  <a href="https://ragflow.io/docs/dev/">文档</a> |
  <a href="https://github.com/infiniflow/ragflow/issues/12241">路线图</a> |
  <a href="https://discord.gg/NjYzJD3GM3">Discord</a>
</h4>

<div align="center" style="margin-top:20px;margin-bottom:20px;">
<img src="https://raw.githubusercontent.com/infiniflow/ragflow-docs/refs/heads/image/image/ragflow-octoverse.png" width="1200"/>
</div>

<div align="center">
<a href="https://trendshift.io/repositories/9064" target="_blank"><img src="https://trendshift.io/api/badge/repositories/9064" alt="infiniflow%2Fragflow | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</div>

<details open>
<summary><b>📕 目录</b></summary>

- 💡 [什么是 RAGFlow？](#-what-is-ragflow)
- 🎮 [快速开始](#-get-started)
- 🔥 [最新更新](#-latest-updates)
- 🌟 [核心功能](#-key-features)
- 🔎 [系统架构](#-system-architecture)
- 🎬 [本地部署](#-self-hosting)
- 🔧 [配置说明](#-configurations)
- 🛠️ [构建 Docker 镜像](#-build-a-docker-image)
- 🔨 [从源码启动服务进行开发](#-launch-service-from-source-for-development)
- 📚 [文档中心](#-documentation)
- 📜 [路线图](#-roadmap)
- 🤝 [社区交流](#-community)
- 🙌 [贡献指南](#-contributing)

</details>

## 💡 什么是 RAGFlow？

[RAGFlow](https://ragflow.io/) 是一款领先的开源检索增强生成（[RAG](https://ragflow.io/basics/what-is-rag)）引擎，它将前沿的 RAG 技术与 Agent（智能体）能力深度融合，为大型语言模型（LLM）打造更卓越的上下文层。它提供了一套精简高效的 RAG 工作流，可适配各种规模的企业需求。依托整合的[上下文引擎](https://ragflow.io/basics/what-is-agent-context-engine)和预置 Agent 模板，RAGFlow 使开发者能够以极高的效率和精度，将复杂数据转化为高保真、可直接投入生产的 AI 系统。

## 🎮 快速开始

访问 [https://cloud.ragflow.io](https://cloud.ragflow.io) 体验我们的云托管服务。

<div align="center" style="margin-top:20px;margin-bottom:20px;">
<img src="https://raw.githubusercontent.com/infiniflow/ragflow-docs/refs/heads/image/image/chunking.gif" width="1200"/>
<img src="https://raw.githubusercontent.com/infiniflow/ragflow-docs/refs/heads/image/image/agentic-dark.gif" width="1200"/>
</div>

## 🔥 最新更新

- 2026-04-24 支持 DeepSeek v4。
- 2026-03-24 [OpenClaw 上的 RAGFlow 技能](https://clawhub.ai/yingfeng/ragflow-skill) — 提供通过 OpenClaw 访问 RAGFlow 数据集的官方技能。
- 2025-12-26 支持为 AI Agent（智能体）配置“记忆”功能。
- 2025-11-19 支持 Gemini 3 Pro。
- 2025-11-12 支持从 Confluence、S3、Notion、Discord、Google Drive 同步数据。
- 2025-10-23 支持使用 MinerU & Docling 作为文档解析方法。
- 2025-10-15 支持可编排的数据摄入（Ingestion）管道。
- 2025-08-08 支持 OpenAI 最新的 GPT-5 系列模型。
- 2025-08-01 支持 Agent 工作流和 MCP。
- 2025-05-23 为 Agent 添加了 Python/JavaScript 代码执行组件。
- 2025-05-05 支持跨语言查询。
- 2025-03-19 支持使用多模态模型解析 PDF 或 DOCX 文件中的图像内容。

## 🎉 持续关注

⭐️ 给本仓库点星（Star），第一时间获取激动人心的新功能与改进！订阅发布通知，不错过任何更新！🌟

<div align="center" style="margin-top:20px;margin-bottom:20px;">
<img src="https://github.com/user-attachments/assets/18c9707e-b8aa-4caf-a154-037089c105ba" width="1200"/>
</div>

## 🌟 核心功能

### 🍭 **“精准解析，高质量输出”**

- 基于[深度文档理解](./deepdoc/README.md)技术，从格式复杂的非结构化数据中提取知识。
- 在海量（理论上无限）Token 的数据中精准定位“大海捞针”。

### 🍱 **基于模板的分块策略**

- 智能且可解释。
- 提供丰富的模板选项供选择。

### 🌱 **溯源引用，减少幻觉**

- 可视化文本分块过程，支持人工干预调整。
- 快速查看关键参考文献与可追溯的引用来源，确保回答有据可依。

### 🍔 **兼容异构数据源**

- 支持 Word、PPT、Excel、TXT、图片、扫描件、结构化数据、网页等多种格式。

### 🛀 **全自动免运维的 RAG 工作流**

- 精简高效的 RAG 编排，兼顾个人开发者与企业级业务需求。
- 支持灵活配置 LLM（大型语言模型）与 Embedding 模型。
- 多重召回机制结合融合重排序算法。
- 直观的 API 接口，实现与企业业务的无缝集成。

## 🔎 系统架构

<div align="center" style="margin-top:20px;margin-bottom:20px;">
<img src="https://github.com/user-attachments/assets/31b0dd6f-ca4f-445a-9457-70cb44a381b2" width="1000"/>
</div>

## 🎬 本地部署

### 📝 环境要求

- CPU ≥ 4 核
- 内存 ≥ 16 GB
- 磁盘空间 ≥ 50 GB
- Docker ≥ 24.0.0 且 Docker Compose ≥ v2.26.1
- [gVisor](https://gvisor.dev/docs/user_guide/install/)：仅在使用 RAGFlow 的代码执行器（沙箱）功能时需要。

> [!TIP]
> 如果你尚未在本地机器（Windows、Mac 或 Linux）上安装 Docker，请参阅[Docker Engine 安装指南](https://docs.docker.com/engine/install/)。

### 🚀 启动服务

1. 确保 `vm.max_map_count` ≥ 262144：

   > 检查 `vm.max_map_count` 的值：
   >
   > ```bash
   > $ sysctl vm.max_map_count
   > ```
   >
   > 如果值低于要求，请将其重置为至少 262144。
   >
   > ```bash
   > # 此处我们以设置为 262144 为例：
   > $ sudo sysctl -w vm.max_map_count=262144
   > ```
   >
   > 此更改在系统重启后会被重置。为确保永久生效，请在 **/etc/sysctl.conf** 中相应添加或更新 `vm.max_map_count` 的值：
   >
   > ```bash
   > vm.max_map_count=262144
   > ```
   >

2. 克隆代码仓库：

   ```bash
   $ git clone https://github.com/infiniflow/ragflow.git
   ```
3. 使用预构建的 Docker 镜像启动服务器：

> [!CAUTION]
> 所有 Docker 镜像均针对 x86 平台编译。目前我们暂不提供 ARM64 平台的 Docker 镜像。
> 如果你使用的是 ARM64 平台，请按照[此指南](https://ragflow.io/docs/dev/build_docker_image)构建兼容你系统的 Docker 镜像。

> 以下命令将下载 RAGFlow `v0.25.4` 版本的 Docker 镜像。不同版本说明如下表所示。若要下载非 `v0.25.4` 的版本，请在使用 `docker compose` 启动服务前，在 **docker/.env** 文件中相应更新 `RAGFLOW_IMAGE` 变量。

```bash
   $ cd ragflow/docker

   # git checkout v0.25.4
   # 可选：使用稳定标签（参见发布页：https://github.com/infiniflow/ragflow/releases）
   # 此步骤确保代码中的 **entrypoint.sh** 文件与 Docker 镜像版本匹配。

   # 使用 CPU 执行 DeepDoc 任务：
   $ docker compose -f docker-compose.yml up -d

   # 若需使用 GPU 加速 DeepDoc 任务：
   # sed -i '1i DEVICE=gpu' .env
   # docker compose -f docker-compose.yml up -d
```

> 注：在 `v0.22.0` 之前，我们提供带 Embedding 模型和不带的两种镜像。详情如下表：

| RAGFlow 镜像标签 | 镜像大小 (GB) | 包含 Embedding 模型？ | 稳定性        |
|-------------------|-----------------|-----------------------|----------------|
| v0.21.1           | &approx;9       | ✔️                    | 稳定版         |
| v0.21.1-slim      | &approx;2       | ❌                     | 稳定版         |

> 自 `v0.22.0` 起，我们仅发布精简版（slim），且不再在镜像标签中附加 **-slim** 后缀。

4. 服务启动后检查状态：

   ```bash
   $ docker logs -f docker-ragflow-cpu-1
   ```

   _以下输出确认系统已成功启动：_

   ```bash

         ____   ___    ______ ______ __
        / __ \ /   |  / ____// ____// /____  _      __
       / /_/ // /| | / / __ / /_   / // __ \| | /| / /
      / _, _// ___ |/ /_/ // __/  / // /_/ /| |/ |/ /
     /_/ |_|/_/  |_|\____//_/    /_/ \____/ |__/|__/

    * Running on all addresses (0.0.0.0)
   ```

   > 如果跳过此步骤直接登录 RAGFlow，浏览器可能会提示 `network abnormal`（网络异常）错误，因为此时你的 RAGFlow 可能尚未完全初始化。
   >
5. 在 Web 浏览器中输入服务器 IP 地址并登录 RAGFlow。

   > 使用默认配置时，你只需输入 `http://IP_OF_YOUR_MACHINE`（**无需**填写端口号），因为默认的 HTTP 服务端口为 `80`。
   >
6. 在 [service_conf.yaml.template](./docker/service_conf.yaml.template) 中，于 `user_default_llm` 字段选择所需的 LLM 厂商，并在 `API_KEY` 字段填入对应的 API 密钥。

   > 更多信息请参阅[LLM API 密钥配置](https://ragflow.io/docs/dev/llm_api_key_setup)。
   >

   _一切准备就绪，开始使用吧！_

## 🔧 配置说明

关于系统配置，你需要管理以下文件：

- [.env](./docker/.env): 保存系统的基础设置，如 `SVR_HTTP_PORT`、`MYSQL_PASSWORD` 和 `MINIO_PASSWORD`。
- [service_conf.yaml.template](./docker/service_conf.yaml.template): 配置后端服务。该文件中的环境变量将在 Docker 容器启动时自动填充。容器内设置的任何环境变量均可直接使用，使你能够根据部署环境自定义服务行为。
- [docker-compose.yml](./docker/docker-compose.yml): 系统依赖此文件进行启动编排。

> [./docker/README](./docker/README.md) 文件详细说明了环境变量与服务配置，这些内容可作为 `${ENV_VARS}` 引用至 [service_conf.yaml.template](./docker/service_conf.yaml.template) 文件中。

如需修改默认 HTTP 服务端口（80），请前往 [docker-compose.yml](./docker/docker-compose.yml) 将 `80:80` 改为 `<YOUR_SERVING_PORT>:80`。

上述配置更新后，需重启所有容器方可生效：

> ```bash
> $ docker compose -f docker-compose.yml up -d
> ```

### 🔄 将文档引擎从 Elasticsearch 切换至 Infinity

RAGFlow 默认使用 Elasticsearch 存储全文与向量数据。若要切换为 [Infinity](https://github.com/infiniflow/infinity/)，请执行以下步骤：

1. 停止所有运行中的容器：

   ```bash
   $ docker compose -f docker/docker-compose.yml down -v
   ```

> [!WARNING]
> `-v` 将删除 Docker 容器卷（volumes），现有数据会被清空。

2. 在 **docker/.env** 中将 `DOC_ENGINE` 设置为 `infinity`。
3. 启动容器：

   ```bash
   $ docker compose -f docker-compose.yml up -d
   ```

> [!WARNING]
> 目前尚未正式支持在 Linux/arm64 机器上切换至 Infinity。

## 🛠️ 构建 Docker 镜像

该镜像大小约为 2 GB，并依赖外部 LLM 与 Embedding 服务。

```bash
git clone https://github.com/infiniflow/ragflow.git
cd ragflow/
docker build --platform linux/amd64 -f Dockerfile -t infiniflow/ragflow:nightly .
```

若你使用了代理，可传递代理参数：

```bash
docker build --platform linux/amd64 \
  --build-arg http_proxy=http://YOUR_PROXY:PORT \
  --build-arg https_proxy=http://YOUR_PROXY:PORT \
  -f Dockerfile -t infiniflow/ragflow:nightly .
```

## 🔨 从源码启动服务进行开发

1. 安装 `uv` 和 `pre-commit`，若已安装可跳过此步：

   ```bash
   pipx install uv pre-commit
   ```
2. 克隆源代码并安装 Python 依赖项：

   ```bash
   git clone https://github.com/infiniflow/ragflow.git
   cd ragflow/
   uv sync --python 3.12 # install RAGFlow dependent python modules
   uv run python3 download_deps.py
   pre-commit install
   ```
3. 使用 Docker Compose 启动依赖服务（MinIO、Elasticsearch、Redis 和 MySQL）：

   ```bash
   docker compose -f docker/docker-compose-base.yml up -d
   ```

   向 `/etc/hosts` 添加以下行，将 **docker/.env** 中指定的所有主机名解析为 `127.0.0.1`：

   ```
   127.0.0.1       es01 infinity mysql minio redis sandbox-executor-manager
   ```
4. 若无法访问 HuggingFace，请设置环境变量 `HF_ENDPOINT` 使用镜像站点：

   ```bash
   export HF_ENDPOINT=https://hf-mirror.com
   ```
5. 若操作系统未预装 jemalloc，请按以下方式安装：

   ```bash
   # Ubuntu
   sudo apt-get install libjemalloc-dev
   # CentOS
   sudo yum install jemalloc
   # OpenSUSE
   sudo zypper install jemalloc
   # macOS
   sudo brew install jemalloc
   ```
6. 启动后端服务：

   ```bash
   source .venv/bin/activate
   export PYTHONPATH=$(pwd)
   bash docker/launch_backend_service.sh
   ```
7. 安装前端依赖项：

   ```bash
   cd web
   npm install
   ```
8. 启动前端服务：

   ```bash
   npm run dev
   ```

   _以下输出确认系统已成功启动：_

   ![](https://github.com/user-attachments/assets/0daf462c-a24d-4496-a66f-92533534e187)
9. 开发完成后，停止 RAGFlow 前后端服务：

   ```bash
   pkill -f "ragflow_server.py|task_executor.py"
   ```

## 📚 文档中心

- [快速入门](https://ragflow.io/docs/dev/)
- [配置说明](https://ragflow.io/docs/dev/configurations)
- [更新日志](https://ragflow.io/docs/dev/release_notes)
- [使用指南](https://ragflow.io/docs/category/user-guides)
- [开发指南](https://ragflow.io/docs/category/developer-guides)
- [参考文档](https://ragflow.io/docs/dev/category/references)
- [常见问题](https://ragflow.io/docs/dev/faq)

## 📜 路线图

详见[RAGFlow 2026 年路线图](https://github.com/infiniflow/ragflow/issues/12241)

## 🤝 社区交流

- [Discord](https://discord.gg/NjYzJD3GM3)
- [X](https://x.com/infiniflowai)
- [GitHub Discussions](https://github.com/orgs/infiniflow/discussions)

## 🙌 贡献指南

RAGFlow 因开源协作而蓬勃发展。秉承这一精神，我们欢迎来自社区的多样化贡献。若有意参与，请先查阅我们的[贡献指南](https://ragflow.io/docs/dev/contributing)。