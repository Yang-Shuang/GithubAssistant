<!-- markdownlint-disable MD030 -->

<p align="center">
<img src="https://github.com/FlowiseAI/Flowise/blob/main/images/flowise_white.svg#gh-light-mode-only">
<img src="https://github.com/FlowiseAI/Flowise/blob/main/images/flowise_dark.svg#gh-dark-mode-only">
</p>

<div align="center">

[![Release Notes](https://img.shields.io/github/release/FlowiseAI/Flowise)](https://github.com/FlowiseAI/Flowise/releases)
[![Discord](https://img.shields.io/discord/1087698854775881778?label=Discord&logo=discord)](https://discord.gg/jbaHfsRVBW)
[![Twitter Follow](https://img.shields.io/twitter/follow/FlowiseAI?style=social)](https://twitter.com/FlowiseAI)
[![GitHub star chart](https://img.shields.io/github/stars/FlowiseAI/Flowise?style=social)](https://star-history.com/#FlowiseAI/Flowise)
[![GitHub fork](https://img.shields.io/github/forks/FlowiseAI/Flowise?style=social)](https://github.com/FlowiseAI/Flowise/fork)

英文 | [繁體中文](./i18n/README-TW.md) | [简体中文](./i18n/README-ZH.md) | [日本語](./i18n/README-JA.md) | [한국어](./i18n/README-KR.md)

</div>

<h3>可视化构建 AI 智能体（AI Agent）</h3>
<a href="https://github.com/FlowiseAI/Flowise">
<img width="100%" src="https://github.com/FlowiseAI/Flowise/blob/main/images/flowise_agentflow.gif?raw=true"></a>

## 📚 目录

-   [⚡ 快速开始](#-quick-start)
-   [🐳 Docker](#-docker)
-   [👨‍💻 开发者](#-developers)
-   [🌱 环境变量](#-env-variables)
-   [📖 文档](#-documentation)
-   [🌐 自托管部署](#-self-host)
-   [☁️ Flowise Cloud](#️-flowise-cloud)
-   [🙋 帮助与支持](#-support)
-   [🙌 贡献指南](#-contributing)
-   [📄 许可证](#-license)

## ⚡ 快速开始

下载并安装 [NodeJS](https://nodejs.org/en/download) >= 20.0.0

1. 安装 Flowise
    ```bash
    npm install -g flowise
    ```
2. 启动 Flowise

    ```bash
    npx flowise start
    ```

3. 打开 [http://localhost:3000](http://localhost:3000)

## 🐳 Docker

### Docker Compose

1. 克隆 Flowise 项目
2. 进入项目根目录下的 `docker` 文件夹
3. 复制 `.env.example` 文件，粘贴到同一位置并重命名为 `.env` 文件
4. `docker compose up -d`
5. 打开 [http://localhost:3000](http://localhost:3000)
6. 你可以通过 `docker compose stop` 停止容器

### Docker 镜像

1. 在本地构建镜像：

    ```bash
    docker build --no-cache -t flowise .
    ```

2. 运行镜像：

    ```bash
    docker run -d --name flowise -p 3000:3000 flowise
    ```

3. 停止容器：

    ```bash
    docker stop flowise
    ```

## 👨‍💻 开发者

Flowise 采用单体仓库架构，包含以下核心模块：

-   `server`：用于提供 API 逻辑的 Node.js 后端服务
-   `ui`：React 前端界面
-   `components`：第三方节点集成库
-   `api-documentation`：基于 Express 自动生成 Swagger-UI API 文档

### 环境要求

-   安装 [PNPM](https://pnpm.io/installation)
    ```bash
    npm i -g pnpm
    ```

### 项目配置与启动

1. 克隆仓库：

    ```bash
    git clone https://github.com/FlowiseAI/Flowise.git
    ```

2. 进入仓库目录：

    ```bash
    cd Flowise
    ```

3. 安装所有模块的依赖项：

    ```bash
    pnpm install
    ```

4. 构建全部代码：

    ```bash
    pnpm build
    ```

    <details>
    <summary>退出码 134（JavaScript 堆内存溢出）</summary>  
    如果在运行上述 `build` 脚本时遇到此错误，请尝试增加 Node.js 堆内存大小后重新运行：

    ```bash
    # macOS / Linux / Git Bash
    export NODE_OPTIONS="--max-old-space-size=4096"

    # Windows PowerShell
    $env:NODE_OPTIONS="--max-old-space-size=4096"

    # Windows CMD
    set NODE_OPTIONS=--max-old-space-size=4096
    ```

    然后执行：

    ```bash
    pnpm build
    ```

    </details>

5. 启动应用：

    ```bash
    pnpm start
    ```

    你现在可以通过访问 [http://localhost:3000](http://localhost:3000) 来使用应用。

6. 开发环境构建：

    -   在 `packages/ui` 目录下创建 `.env` 文件，并配置 `VITE_PORT`（参考 `.env.example`）
    -   在 `packages/server` 目录下创建 `.env` 文件，并配置 `PORT`（参考 `.env.example`）
    -   运行：

        ```bash
        pnpm dev
        ```

    代码的任何更改都会自动在 [http://localhost:8080](http://localhost:8080) 热重载应用。

## 🌱 环境变量

Flowise 支持通过多种环境变量来配置你的实例。你可以在 `packages/server` 文件夹内的 `.env` 文件中指定以下变量。阅读[更多说明](https://github.com/FlowiseAI/Flowise/blob/main/CONTRIBUTING.md#-env-variables)

## 📖 文档

你可以在此查看 Flowise 官方[文档](https://docs.flowiseai.com/)

## 🌐 自托管部署

将 Flowise 以自托管方式部署到你现有的基础设施中，我们支持多种[部署方案](https://docs.flowiseai.com/configuration/deployment)：

-   [AWS](https://docs.flowiseai.com/configuration/deployment/aws)
-   [Azure](https://docs.flowiseai.com/configuration/deployment/azure)
-   [Digital Ocean](https://docs.flowiseai.com/configuration/deployment/digital-ocean)
-   [GCP](https://docs.flowiseai.com/configuration/deployment/gcp)
-   [Alibaba Cloud](https://computenest.console.aliyun.com/service/instance/create/default?type=user&ServiceName=Flowise社区版)
-   <details>
      <summary>其他平台</summary>

    -   [Railway](https://docs.flowiseai.com/configuration/deployment/railway)

        [![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/pn4G8S?referralCode=WVNPD9)

    -   [Northflank](https://northflank.com/stacks/deploy-flowiseai)

        [![Deploy to Northflank](https://assets.northflank.com/deploy_to_northflank_smm_36700fb050.svg)](https://northflank.com/stacks/deploy-flowiseai)

    -   [Render](https://docs.flowiseai.com/configuration/deployment/render)

        [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://docs.flowiseai.com/configuration/deployment/render)

    -   [HuggingFace Spaces](https://docs.flowiseai.com/configuration/deployment/hugging-face)

        <a href="https://huggingface.co/spaces/FlowiseAI/Flowise"><img src="https://huggingface.co/datasets/huggingface/badges/raw/main/open-in-hf-spaces-sm.svg" alt="HuggingFace Spaces"></a>

    -   [Elestio](https://elest.io/open-source/flowiseai)

        [![Deploy on Elestio](https://elest.io/images/logos/deploy-to-elestio-btn.png)](https://elest.io/open-source/flowiseai)

    -   [Sealos](https://template.sealos.io/deploy?templateName=flowise)

        [![Deploy on Sealos](https://sealos.io/Deploy-on-Sealos.svg)](https://template.sealos.io/deploy?templateName=flowise)

    -   [RepoCloud](https://repocloud.io/details/?app_id=29)

        [![Deploy on RepoCloud](https://d16t0pc4846x52.cloudfront.net/deploy.png)](https://repocloud.io/details/?app_id=29)

      </details>

## ☁️ Flowise Cloud

立即前往 [Flowise Cloud](https://flowiseai.com/) 开始使用。

## 🙋 帮助与支持

欢迎在[讨论区](https://github.com/FlowiseAI/Flowise/discussions)中提出任何问题、反馈问题或请求新功能。

## 🙌 贡献指南

感谢以下出色的贡献者：

<a href="https://github.com/FlowiseAI/Flowise/graphs/contributors">
<img src="https://contrib.rocks/image?repo=FlowiseAI/Flowise" />
</a><br><br>

请参阅[贡献指南](CONTRIBUTING.md)。如有任何疑问或问题，请通过 [Discord](https://discord.gg/jbaHfsRVBW) 联系我们。

[![Star History Chart](https://api.star-history.com/svg?repos=FlowiseAI/Flowise&type=Timeline)](https://star-history.com/#FlowiseAI/Flowise&Date)

## 📄 许可证

本仓库中的源代码遵循 [Apache License Version 2.0](LICENSE.md) 协议开源。