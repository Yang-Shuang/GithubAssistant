<img src="./assets/web-ui.png" alt="Browser Use Web UI" width="full"/>

<br/>

[![GitHub stars](https://img.shields.io/github/stars/browser-use/web-ui?style=social)](https://github.com/browser-use/web-ui/stargazers)
[![Discord](https://img.shields.io/discord/1303749220842340412?color=7289DA&label=Discord&logo=discord&logoColor=white)](https://link.browser-use.com/discord)
[![Documentation](https://img.shields.io/badge/Documentation-📕-blue)](https://docs.browser-use.com)
[![WarmShao](https://img.shields.io/twitter/follow/warmshao?style=social)](https://x.com/warmshao)

本项目基于 [browser-use](https://github.com/browser-use/browser-use) 构建，旨在让网站对 AI Agent（智能体）可访问。

我们在此正式感谢 [WarmShao](https://github.com/warmshao) 对本项目的贡献。

**WebUI：**基于 Gradio 构建，支持大部分 `browser-use` 功能。该界面设计友好，便于与浏览器 Agent 进行交互。

**扩展的 LLM 支持：**我们已集成对多种大型语言模型（Large Language Models, LLMs）的支持，包括：Google、OpenAI、Azure OpenAI、Anthropic、DeepSeek、Ollama 等。未来计划支持更多模型。

**自定义浏览器支持：**你可以使用自己的浏览器配合本工具，无需重新登录网站或处理其他身份验证问题。此功能还支持高清屏幕录制。

**持久化浏览器会话：**你可以选择在 AI 任务之间保持浏览器窗口打开，从而查看 AI 交互的完整历史记录和状态。

<video src="https://github.com/user-attachments/assets/56bc7080-f2e3-4367-af22-6bf2245ff6cb" controls="controls">你的浏览器不支持播放此视频！</video>

## 安装指南

### 方式一：本地安装

阅读[快速入门指南](https://docs.browser-use.com/quickstart#prepare-the-environment)，或按照以下步骤开始使用。

#### 步骤 1：克隆仓库
```bash
git clone https://github.com/browser-use/web-ui.git
cd web-ui
```

#### 步骤 2：配置 Python 环境
我们推荐使用 [uv](https://docs.astral.sh/uv/) 来管理 Python 环境。

使用 uv（推荐）：
```bash
uv venv --python 3.11
```

激活虚拟环境：
- Windows（命令提示符/CMD）：
```cmd
.venv\Scripts\activate
```
- Windows（PowerShell）：
```powershell
.\.venv\Scripts\Activate.ps1
```
- macOS/Linux：
```bash
source .venv/bin/activate
```

#### 步骤 3：安装依赖项
安装 Python 包：
```bash
uv pip install -r requirements.txt
```

在 Playwright 中安装浏览器。 
```bash
playwright install --with-deps
```
或者，你可以通过运行以下命令安装特定浏览器：
```bash
playwright install chromium --with-deps
```

#### 步骤 4：配置环境变量
1. 复制示例环境文件：
- Windows（命令提示符/CMD）：
```bash
copy .env.example .env
```
- macOS/Linux/Windows（PowerShell）：
```bash
cp .env.example .env
```
2. 用你喜欢的文本编辑器打开 `.env`，添加你的 API Key 及其他配置

#### 步骤 5：体验 WebUI
1. **启动 WebUI：**
    ```bash
    python webui.py --ip 127.0.0.1 --port 7788
    ```
2. **访问 WebUI：**打开浏览器并访问 `http://127.0.0.1:7788`。
3. **使用你自己的浏览器（可选）：**
    - 将 `BROWSER_PATH` 设置为浏览器可执行文件的路径，将 `BROWSER_USER_DATA` 设置为浏览器的用户数据目录。如果希望使用本地用户数据，请保持 `BROWSER_USER_DATA` 为空。
      - Windows
        ```env
         BROWSER_PATH="C:\Program Files\Google\Chrome\Application\chrome.exe"
         BROWSER_USER_DATA="C:\Users\YourUsername\AppData\Local\Google\Chrome\User Data"
        ```
        > 注意：在 Windows 系统中，请将 `YourUsername` 替换为你的实际用户名。
      - macOS
        ```env
         BROWSER_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
         BROWSER_USER_DATA="/Users/YourUsername/Library/Application Support/Google/Chrome"
        ```
    - 关闭所有 Chrome 窗口
    - 使用非 Chrome 浏览器（如 Firefox 或 Edge）打开 WebUI。这一步很重要，因为 Agent 运行时持久化浏览器上下文会调用 Chrome 的数据。
    - 在浏览器设置中勾选“Use Own Browser”选项。

### 方式二：Docker 安装

#### 前置条件
- 已安装 Docker 和 Docker Compose
  - [Docker Desktop](https://www.docker.com/products/docker-desktop/)（适用于 Windows/macOS）
  - [Docker Engine](https://docs.docker.com/engine/install/) 和 [Docker Compose](https://docs.docker.com/compose/install/)（适用于 Linux）

#### 步骤 1：克隆仓库
```bash
git clone https://github.com/browser-use/web-ui.git
cd web-ui
```

#### 步骤 2：配置环境变量
1. 复制示例环境文件：
- Windows（命令提示符/CMD）：
```bash
copy .env.example .env
```
- macOS/Linux/Windows（PowerShell）：
```bash
cp .env.example .env
```
2. 用你喜欢的文本编辑器打开 `.env`，添加你的 API Key 及其他配置

#### 步骤 3：Docker 构建与运行
```bash
docker compose up --build
```
对于 ARM64 架构系统（例如搭载 Apple Silicon 芯片的 Mac），请运行以下命令：
```bash
TARGETPLATFORM=linux/arm64 docker compose up --build
```

#### 步骤 4：体验 WebUI 和 VNC
- WebUI：在浏览器中打开 `http://localhost:7788`
- VNC 查看器（用于观看浏览器交互）：打开 `http://localhost:6080/vnc.html`
  - 默认 VNC 密码为："youvncpassword"
  - 可通过在 `.env` 文件中设置 `VNC_PASSWORD` 进行修改

## 更新日志
- [x] **2025/01/26：**感谢 @vvincent1234。现在 browser-use-webui 可以结合 DeepSeek-R1 进行深度思考！
- [x] **2025/01/10：**感谢 @casistack。现已支持 Docker 部署选项，并可在任务之间保持浏览器打开状态。[视频教程演示](https://github.com/browser-use/web-ui/issues/1#issuecomment-2582511750)。
- [x] **2025/01/06：**感谢 @richard-devbot。发布了全新且设计精良的 WebUI。[视频教程演示](https://github.com/warmshao/browser-use-webui/issues/1#issuecomment-2573393113)。