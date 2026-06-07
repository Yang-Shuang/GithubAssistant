<div align="center">

<img src="docs/images/bytebot-logo.png" width="500" alt="Bytebot Logo">

# Bytebot：开源 AI 桌面智能体（Desktop Agent）

<a href="https://trendshift.io/repositories/14624" target="_blank"><img src="https://trendshift.io/api/badge/repositories/14624" alt="bytebot-ai%2Fbytebot | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

**一个拥有自己电脑、能为你完成各类任务的 AI**

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/deploy/bytebot?referralCode=L9lKXQ)

[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://github.com/bytebot-ai/bytebot/tree/main/docker)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)
[![Discord](https://img.shields.io/discord/1232768900274585720?color=7289da&label=discord)](https://discord.com/invite/d9ewZkWPTP)

[🌐 官网](https://bytebot.ai) • [📚 文档](https://docs.bytebot.ai) • [💬 Discord](https://discord.com/invite/d9ewZkWPTP) • [𝕏 Twitter](https://x.com/bytebot_ai)

<!-- Keep these links. Translations will automatically update with the README. -->
[Deutsch](https://zdoc.app/de/bytebot-ai/bytebot) | 
[Español](https://zdoc.app/es/bytebot-ai/bytebot) | 
[français](https://zdoc.app/fr/bytebot-ai/bytebot) | 
[日本語](https://zdoc.app/ja/bytebot-ai/bytebot) | 
[한국어](https://zdoc.app/ko/bytebot-ai/bytebot) | 
[Português](https://zdoc.app/pt/bytebot-ai/bytebot) | 
[Русский](https://zdoc.app/ru/bytebot-ai/bytebot) | 
[中文](https://zdoc.app/zh/bytebot-ai/bytebot)
</div>

---

https://github.com/user-attachments/assets/f271282a-27a3-43f3-9b99-b34007fdd169

https://github.com/user-attachments/assets/72a43cf2-bd87-44c5-a582-e7cbe176f37f

## 什么是桌面智能体（Desktop Agent）？

桌面智能体是一个拥有自己电脑的 AI。与仅基于浏览器的智能体或传统的 RPA 工具不同，Bytebot 配备了一个完整的虚拟桌面环境，在其中它可以：

- 使用任何应用程序（浏览器、邮件客户端、办公工具、IDE）
- 利用自己的文件系统下载并整理文件
- 通过密码管理器登录网站和应用
- 读取并处理文档、PDF 和电子表格
- 跨不同程序完成复杂的多步骤工作流

你可以把它想象成一位拥有自己电脑的虚拟员工，它能像人类一样看到屏幕、移动鼠标、敲击键盘并完成任务。

## 为什么让 AI 拥有自己的电脑？

当 AI 能够访问完整的桌面环境时，它将解锁仅靠浏览器智能体或 API 集成无法实现的能力：

### 完整的任务自主权

给 Bytebot 下达类似“从我们的供应商门户下载所有发票并将其整理到一个文件夹中”的任务，它将：

- 打开浏览器
- 导航至各个门户网站
- 处理身份验证（包括通过密码管理器完成双因素认证/2FA）
- 将文件下载至本地文件系统
- 将它们整理到指定文件夹中

### 文档处理

直接将文件上传到 Bytebot 的桌面，它可以：

- 将完整的 PDF 内容载入上下文
- 从复杂文档中提取数据
- 跨多个文件交叉核对信息
- 基于分析结果创建新文档
- 处理 API 无法访问的文件格式

### 使用真实应用程序

Bytebot 不仅限于网页界面。它可以：

- 使用桌面应用，如文本编辑器、VS Code 或邮件客户端
- 运行脚本和命令行工具
- 按需安装新软件
- 为特定工作流配置应用程序

## 快速入门

### 2 分钟部署

**选项 1：Railway（最简单）**
[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/deploy/bytebot?referralCode=L9lKXQ)

只需点击并添加你的 AI 提供商 API 密钥。

**选项 2：Docker Compose**

```bash
git clone https://github.com/bytebot-ai/bytebot.git
cd bytebot

# Add your AI provider key (choose one)
echo "ANTHROPIC_API_KEY=sk-ant-..." > docker/.env
# Or: echo "OPENAI_API_KEY=sk-..." > docker/.env
# Or: echo "GEMINI_API_KEY=..." > docker/.env

docker-compose -f docker/docker-compose.yml up -d

# Open http://localhost:9992
```

[完整部署指南 →](https://docs.bytebot.ai/quickstart)

## 工作原理

Bytebot 由四个集成组件构成：

1. **虚拟桌面**：预装应用程序的完整 Ubuntu Linux 环境
2. **AI 智能体（Agent）**：理解你的任务并控制桌面以完成它们
3. **任务界面**：用于创建任务和观看 Bytebot 运行过程的 Web UI
4. **API**：用于编程化任务创建和桌面控制的 REST 端点

### 核心功能

- **自然语言任务**：只需描述你需要完成的内容
- **文件上传**：将文件拖拽到任务中供 Bytebot 处理
- **实时桌面视图**：实时观看 Bytebot 的工作过程
- **接管模式（Takeover Mode）**：当你需要协助或配置某些内容时接管控制权
- **密码管理器支持**：安装 1Password、Bitwarden 等以实现自动认证
- **持久化环境**：安装的程序将保留，供后续任务使用

## 示例任务

### 基础示例

```
"Go to Wikipedia and create a summary of quantum computing"
"Research flights from NYC to London and create a comparison document"
"Take screenshots of the top 5 news websites"
```

### 文档处理

```
"Read the uploaded contracts.pdf and extract all payment terms and deadlines"
"Process these 5 invoice PDFs and create a summary report"
"Download and analyze the latest financial report and answer: What were the key risks mentioned?"
```

### 多应用程序工作流

```
"Download last month's bank statements from our three banks and consolidate them"
"Check all our vendor portals for new invoices and create a summary report"
"Log into our CRM, export the customer list, and update records in the ERP system"
```

## 编程控制

### 通过 API 创建任务

```python
import requests

# Simple task
response = requests.post('http://localhost:9991/tasks', json={
    'description': 'Download the latest sales report and create a summary'
})

# Task with file upload
files = {'files': open('contracts.pdf', 'rb')}
response = requests.post('http://localhost:9991/tasks',
    data={'description': 'Review these contracts for important dates'},
    files=files
)
```

### 直接控制桌面

```bash
# Take a screenshot
curl -X POST http://localhost:9990/computer-use \
  -H "Content-Type: application/json" \
  -d '{"action": "screenshot"}'

# Click at specific coordinates
curl -X POST http://localhost:9990/computer-use \
  -H "Content-Type: application/json" \
  -d '{"action": "click_mouse", "coordinate": [500, 300]}'
```

[完整 API 文档 →](https://docs.bytebot.ai/api-reference/introduction)

## 设置你的桌面智能体

### 1. 部署 Bytebot

使用上述任一部署方法让 Bytebot 运行起来。

### 2. 配置桌面

在 UI 中使用“桌面”选项卡来：

- 安装你需要的额外程序
- 设置用于认证的密码管理器
- 按你的偏好配置应用程序
- 登录希望 Bytebot 访问的网站

### 3. 开始下达任务

用自然语言创建任务，并观看 Bytebot 使用配置好的桌面完成任务。

## 应用场景

### 业务流程自动化

- 发票处理与数据提取
- 多系统数据同步
- 从多个来源生成报告
- 跨平台合规性检查

### 开发与测试

- 自动化 UI 测试
- 跨浏览器兼容性检查
- 带截图的文档生成
- 代码部署验证

### 研究与分析

- 跨网站竞品分析
- 从多源收集数据
- 文档分析与摘要生成
- 市场调研汇编

## 架构

Bytebot 基于以下技术构建：

- **桌面环境**：Ubuntu 22.04，搭载 XFCE、Firefox、VS Code 等工具
- **智能体（Agent）**：协调 AI 与桌面操作的 NestJS 服务
- **前端 UI**：用于任务管理的 Next.js 应用
- **AI 支持**：兼容 Anthropic Claude、OpenAI GPT、Google Gemini
- **部署方式**：Docker 容器，便于自行托管

## 为什么选择自行托管？

- **数据隐私**：所有运行均在你的基础设施上进行
- **完全控制**：按需自定义桌面环境
- **无限制使用**：使用你自己的 AI API 密钥，不受平台限制
- **高度灵活**：安装任意软件，访问任意系统

## 高级功能

### 多 AI 提供商支持

通过我们的 [LiteLLM 集成](https://docs.bytebot.ai/deployment/litellm)使用任意 AI 提供商：

- Azure OpenAI
- AWS Bedrock
- 通过 Ollama 运行本地模型
- 100+ 其他提供商

### 企业级部署

使用 Helm 在 Kubernetes 上部署：

```bash
# Clone the repository
git clone https://github.com/bytebot-ai/bytebot.git
cd bytebot

# Install with Helm
helm install bytebot ./helm \
  --set agent.env.ANTHROPIC_API_KEY=sk-ant-...
```

[企业部署指南 →](https://docs.bytebot.ai/deployment/helm)

## 社区与支持

- **Discord**：[加入我们的社区](https://discord.com/invite/d9ewZkWPTP)获取帮助与讨论
- **文档**：在 [docs.bytebot.ai](https://docs.bytebot.ai) 查阅全面指南
- **GitHub Issues**：报告 Bug 与提交功能建议

## 贡献代码

我们欢迎任何形式的贡献！无论是：

- 🐛 Bug 修复
- ✨ 新功能开发
- 📚 文档改进
- 🌐 翻译工作

请遵循以下步骤：

1. 先查看现有的 [Issues](https://github.com/bytebot-ai/bytebot/issues)
2. 针对重大变更请先创建 Issue 进行讨论
3. 提交附带清晰描述的 PR
4. 加入我们的 [Discord](https://discord.com/invite/d9ewZkWPTP) 交流想法

## 许可证

Bytebot 基于 Apache 2.0 开源协议发布。

---

<div align="center">

**给你的 AI 一台专属电脑，看看它能做什么。**

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/deploy/bytebot?referralCode=L9lKXQ)

<sub>由 [Tantl Labs](https://tantl.com) 与开源社区共同构建</sub>

</div>