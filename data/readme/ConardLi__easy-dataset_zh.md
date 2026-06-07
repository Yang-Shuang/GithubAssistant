<div align="center">

![](./public//imgs/bg2.png)

<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/ConardLi/easy-dataset">
<img alt="GitHub Downloads (all assets, all releases)" src="https://img.shields.io/github/downloads/ConardLi/easy-dataset/total">
<img alt="GitHub Release" src="https://img.shields.io/github/v/release/ConardLi/easy-dataset">
<img src="https://img.shields.io/badge/license-AGPL--3.0-green.svg" alt="AGPL 3.0 License"/>
<img alt="GitHub contributors" src="https://img.shields.io/github/contributors/ConardLi/easy-dataset">
<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/ConardLi/easy-dataset">
<a href="https://arxiv.org/abs/2507.04009v1" target="_blank">
  <img src="https://img.shields.io/badge/arXiv-2507.04009-b31b1b.svg" alt="arXiv:2507.04009">
</a>

<a href="https://trendshift.io/repositories/13944" target="_blank"><img src="https://trendshift.io/api/badge/repositories/13944" alt="ConardLi%2Feasy-dataset | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

**一款专为大语言模型（LLM）微调数据集打造的强大工具**

[简体中文](./README.zh-CN.md) | [英文](./README.md) | [Türkçe](./README.tr.md)

[功能特性](#features) • [快速开始](#local-run) • [文档中心](https://docs.easy-dataset.com/ed/en) • [参与贡献](#contributing) • [开源协议](#license)

如果你喜欢这个项目，请给它一个 Star⭐️，或者给作者买杯咖啡 => [捐赠](./public/imgs/aw.jpg) ❤️!

</div>

## 项目概述

Easy Dataset 是一款专为构建大语言模型（LLM）数据集而设计的应用程序。它拥有直观的界面，内置强大的文档解析工具、智能分割算法以及数据清洗与增强能力。该应用可将各种格式的领域特定文档转换为高质量的结构化数据集，适用于模型微调、检索增强生成（RAG）及模型性能评估等场景。

![](./public/imgs/arc3.png)

## 最新动态

🎉🎉 Easy Dataset 1.7.0 版本全新上线评测功能！你可以轻松将领域文档转换为评测数据集（测试集），并自动运行多维度评测任务。此外，内置了人工盲测系统，助你轻松满足垂直领域模型评测、微调后模型性能评估以及 RAG 召回率评估等需求。教程：[https://www.bilibili.com/video/BV1CRrVB7Eb4/](https://www.bilibili.com/video/BV1CRrVB7Eb4/)

## 功能特性

### 📄 文档处理与数据生成

- **智能文档解析**：支持 PDF、Markdown、DOCX、TXT、EPUB 等多种格式的智能识别
- **智能文本分割**：提供多种分割算法（基于 Markdown 结构、递归分隔符、固定长度、代码感知分块），支持自定义可视化分割
- **智能问题生成**：自动从文本片段中提取相关问题，支持预设模板与批量生成
- **领域标签树**：基于文档结构智能构建全局领域标签树，具备自动打标能力
- **答案生成**：调用大模型（LLM）API 生成完整答案与思维链（Chain of Thought / COT），并支持 AI 优化
- **数据清洗**：智能清理文本噪声，提升数据质量

### 🔄 多种数据集类型

- **单轮问答数据集**：标准问对答格式，适用于基础微调
- **多轮对话数据集**：支持自定义角色与场景，适配对话式交互格式
- **图文问答数据集**：从图片生成视觉问答数据，支持多种导入方式（目录、PDF、ZIP）
- **数据蒸馏**：无需上传文档，直接基于领域主题生成标签树与问题

### 📊 模型评测系统

- **评测数据集**：支持生成判断题、单选题、多选题、简答题及开放性问题
- **自动化模型评测**：使用裁判模型（Judge Model）自动评估模型回答质量，支持自定义评分规则
- **人工盲测（Arena）**：双盲对比两个模型的回答结果，确保客观公正的评测
- **AI 质量评估**：自动生成数据集的质量评分与过滤筛选

### 🛠️ 高级功能

- **自定义提示词（Prompt）**：支持项目级别的全局 Prompt 模板配置（问题生成、答案生成、数据清洗等）
- **GA 对生成**：体裁-受众（Genre-Audience）配对生成，丰富数据多样性
- **任务管理中心**：后台批量处理任务，支持实时监控与中断操作
- **资源监控面板**：统计 Token 消耗、追踪 API 调用情况、分析模型性能
- **模型测试沙盒**：支持最多同时对比 3 个模型的表现

### 📤 导出与集成

- **多格式导出**：支持 Alpaca、ShareGPT、Multilingual-Thinking 等格式，提供 JSON/JSONL 文件类型
- **均衡导出**：可按标签配置导出数量，实现数据集分布平衡
- **LLaMA Factory 集成**：一键生成 LLaMA Factory 配置文件
- **Hugging Face 上传**：支持直接将数据集上传至 Hugging Face Hub

### 🤖 模型支持

- **广泛兼容**：兼容所有遵循 OpenAI 格式的大语言模型 API
- **多服务商支持**：支持 OpenAI、MiniMax、Ollama（本地部署）、智谱 AI、阿里百炼、OpenRouter 等
- **视觉模型支持**：兼容 Gemini、Claude 等多模态模型，用于 PDF 解析与图文问答

### 🌐 用户体验

- **友好界面**：现代化直观交互设计，兼顾技术人员与非技术用户的使用习惯
- **多语言支持**：完整支持中文、英文、土耳其语及葡萄牙语 🇹🇷
- **数据集广场**：发现并探索公开的数据集资源
- **桌面客户端**：提供 Windows、macOS 及 Linux 版本

## 快速演示

https://github.com/user-attachments/assets/6ddb1225-3d1b-4695-90cd-aa4cb01376a8

## 本地运行

### 下载客户端

<table style="width: 100%">
  <tr>
    <td width="20%" align="center">
      <b>Windows</b>
    </td>
    <td width="30%" align="center" colspan="2">
      <b>macOS</b>
    </td>
    <td width="20%" align="center">
      <b>Linux</b>
    </td>
  </tr>
  <tr style="text-align: center">
    <td align="center" valign="middle">
      <a href='https://github.com/ConardLi/easy-dataset/releases/latest'>
        <img src='./public/imgs/windows.png' style="height:24px; width: 24px" />
        <br />
        <b>Setup.exe</b>
      </a>
    </td>
    <td align="center" valign="middle">
      <a href='https://github.com/ConardLi/easy-dataset/releases/latest'>
        <img src='./public/imgs/mac.png' style="height:24px; width: 24px" />
        <br />
        <b>Intel</b>
      </a>
    </td>
    <td align="center" valign="middle">
      <a href='https://github.com/ConardLi/easy-dataset/releases/latest'>
        <img src='./public/imgs/mac.png' style="height:24px; width: 24px" />
        <br />
        <b>M</b>
      </a>
    </td>
    <td align="center" valign="middle">
      <a href='https://github.com/ConardLi/easy-dataset/releases/latest'>
        <img src='./public/imgs/linux.png' style="height:24px; width: 24px" />
        <br />
        <b>AppImage</b>
      </a>
    </td>
  </tr>
</table>

### 通过 NPM 安装运行

1. 克隆仓库：

```bash
   git clone https://github.com/ConardLi/easy-dataset.git
   cd easy-dataset
```

2. 安装依赖：

```bash
   npm install
```

3. 启动开发服务器：

```bash
   npm run build

   npm run start
```

4. 打开浏览器并访问 `http://localhost:1717`

### 使用官方 Docker 镜像

1. 克隆仓库：

```bash
git clone https://github.com/ConardLi/easy-dataset.git
cd easy-dataset
```

2. 修改 `docker-compose.yml` 文件：

```yml
services:
  easy-dataset:
    image: ghcr.io/conardli/easy-dataset
    container_name: easy-dataset
    ports:
      - '1717:1717'
    volumes:
      - ./local-db:/app/local-db
      - ./prisma:/app/prisma
    restart: unless-stopped
```

> **注意**：建议将当前代码仓库目录下的 `local-db` 和 `prisma` 文件夹作为挂载路径，以保持与通过 NPM 启动时的数据库路径一致。

> **注意**：首次启动时会自动初始化数据库文件，无需手动执行 `npm run db:push`。

3. 使用 docker-compose 启动服务：

```bash
docker-compose up -d
```

4. 打开浏览器并访问 `http://localhost:1717`

### 使用本地 Dockerfile 构建镜像

如需自行构建镜像，请使用项目根目录下的 Dockerfile：

1. 克隆仓库：

```bash
git clone https://github.com/ConardLi/easy-dataset.git
cd easy-dataset
```

2. 构建 Docker 镜像：

```bash
docker build -t easy-dataset .
```

3. 运行容器：

```bash
docker run -d \
  -p 1717:1717 \
  -v ./local-db:/app/local-db \
  -v ./prisma:/app/prisma \
  --name easy-dataset \
  easy-dataset
```

> **注意**：建议将当前代码仓库目录下的 `local-db` 和 `prisma` 文件夹作为挂载路径，以保持与通过 NPM 启动时的数据库路径一致。

> **注意**：首次启动时会自动初始化数据库文件，无需手动执行 `npm run db:push`。

4. 打开浏览器并访问 `http://localhost:1717`

## 文档教程

- 查看本项目演示视频：[Easy Dataset 演示视频](https://www.bilibili.com/video/BV1y8QpYGE57/)
- 查阅所有功能与 API 的详细文档，请访问我们的[官方文档站点](https://docs.easy-dataset.com/ed/en)
- 查看本项目相关论文：[Easy Dataset: A Unified and Extensible Framework for Synthesizing LLM Fine-Tuning Data from Unstructured Documents](https://arxiv.org/abs/2507.04009v1)

## 社区实践

- [使用 Easy Dataset 完整生成测试集与模型评测](https://www.bilibili.com/video/BV1CRrVB7Eb4/)
- [Easy Dataset × LLaMA Factory：让大模型高效学习领域知识](https://buaa-act.feishu.cn/wiki/GVzlwYcRFiR8OLkHbL6cQpYin7g)
- [Easy Dataset 实战指南：如何构建高质量数据集？](https://www.bilibili.com/video/BV1MRMnz1EGW)
- [Easy Dataset 核心功能更新解读](https://www.bilibili.com/video/BV1fyJhzHEb7/)
- [大模型微调数据集：基础知识科普](https://docs.easy-dataset.com/zhi-shi-ke-pu)

## 参与贡献

我们欢迎社区贡献！如果你想为 Easy Dataset 做出贡献，请遵循以下步骤：

1. Fork（复刻）本仓库
2. 创建新分支（`git checkout -b feature/amazing-feature`）
3. 进行修改
4. 提交更改（`git commit -m 'Add some amazing feature'`）
5. 推送到分支（`git push origin feature/amazing-feature`）
6. 提交 Pull Request（请提交至 `DEV` 分支）

请确保测试用例已适当更新，并遵循现有的代码规范。

## 加入讨论组与联系作者

https://docs.easy-dataset.com/geng-duo/lian-xi-wo-men

## 开源协议

本项目采用 AGPL 3.0 许可证进行授权 - 详情请参阅 [LICENSE](LICENSE) 文件。

## 引用说明

如果本作品对你有所帮助，请引用如下：

```bibtex
@misc{miao2025easydataset,
  title={Easy Dataset: A Unified and Extensible Framework for Synthesizing LLM Fine-Tuning Data from Unstructured Documents},
  author={Ziyang Miao and Qiyu Sun and Jingyuan Wang and Yuchen Gong and Yaowei Zheng and Shiqi Li and Richong Zhang},
  year={2025},
  eprint={2507.04009},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  url={https://arxiv.org/abs/2507.04009}
}
```

## Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=ConardLi/easy-dataset&type=Date)](https://www.star-history.com/#ConardLi/easy-dataset&Date)

<div align="center">
  <sub>由 ❤️ 构建 • 关注我：<a href="./public/imgs/weichat.jpg">微信公众号</a>｜<a href="https://space.bilibili.com/474921808">B站</a>｜<a href="https://juejin.cn/user/3949101466785709">掘金</a>｜<a href="https://www.zhihu.com/people/wen-ti-chao-ji-duo-de-xiao-qi">知乎</a>｜<a href="https://www.youtube.com/@garden-conard">Youtube</a></sub>
</div>