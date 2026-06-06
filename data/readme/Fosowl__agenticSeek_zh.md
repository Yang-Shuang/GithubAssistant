# AgenticSeek：Manus AI 的私有化本地替代方案。

<p align="center">
<img align="center" src="./media/agentic_seek_logo.png" width="300" height="300" alt="Agentic Seek Logo">
<p>

  English | [中文](./README_CHS.md) | [繁體中文](./README_CHT.md) | [Français](./README_FR.md) | [日本語](./README_JP.md) | [Português (Brasil)](./README_PTBR.md) | [Español](./README_ES.md) | [Türkçe](./README_TR.md)

*一款**完全本地化运行的 Manus AI 替代方案**。这款支持语音的 AI 助手能够自主浏览网页、编写代码并规划任务，同时将所有数据保留在你的设备上。它专为本地推理模型优化，完全运行于你的硬件之上，确保绝对隐私且零云端依赖。*

[![Visit AgenticSeek](https://img.shields.io/static/v1?label=Website&message=AgenticSeek&color=blue&style=flat-square)](https://fosowl.github.io/agenticSeek.html) ![License](https://img.shields.io/badge/license-GPL--3.0-green) [![Discord](https://img.shields.io/badge/Discord-Join%20Us-7289DA?logo=discord&logoColor=white)](https://discord.gg/8hGDaME3TC) [![Twitter](https://img.shields.io/twitter/url/https/twitter.com/fosowl.svg?style=social&label=Update%20%40Fosowl)](https://x.com/Martin993886460) [![GitHub stars](https://img.shields.io/github/stars/Fosowl/agenticSeek?style=social)](https://github.com/Fosowl/agenticSeek/stargazers)

### 为什么选择 AgenticSeek？

* 🔒 **完全本地化与隐私保护** — 所有功能均在你的设备上运行，无需云端，不共享数据。你的文件、对话和搜索记录均保持私密。
* 🌐 **智能网页浏览** — AgenticSeek 可自主上网——进行搜索、阅读、提取信息、填写表单等，全程免手动操作。
* 💻 **自主编程助手** — 需要代码？它能独立编写、调试并运行 Python、C、Go、Java 等语言的程序，无需人工干预。
* 🧠 **智能 Agent（代理）选择** — 你只需提问，它会自动匹配最适合该任务的 agent。就像拥有一支随时待命的专家团队。
* 📋 **规划与执行复杂任务** — 从旅行计划到复杂项目，它能将大任务拆解为步骤，并调用多个 AI agent 协同完成。
* 🎙️ **语音支持** — 提供简洁、快速且充满未来感的语音转文字功能，让你像与科幻电影中的个人 AI 对话一样自然。（开发中）

### **演示**

> *你能搜索 agenticSeek 项目，了解所需技能，然后打开 CV_candidates.zip，并告诉我谁最匹配该项目吗？*

https://github.com/user-attachments/assets/b8ca60e9-7b3b-4533-840e-08f9ac426316

免责声明：此演示（包括出现的所有文件，如 CV_candidates.zip）均为虚构。我们并非企业机构，正在寻找开源贡献者而非候选人。

> 🙏 本项目最初为个人副业启动，目前无明确路线图且零资金赞助。因登上 GitHub Trending，项目发展远超预期。非常感谢大家的贡献、反馈与耐心。

## 前置条件

开始前，请确保已安装以下软件：

*   **Git**：用于克隆代码仓库。[下载 Git](https://git-scm.com/downloads)
*   **Python 3.10.x**：强烈建议使用 Python 3.10.x 版本。使用其他版本可能导致依赖错误。[下载 Python 3.10](https://www.python.org/downloads/release/python-3100/)（请选择 3.10.x 系列）
*   **Docker Engine 与 Docker Compose**：用于运行捆绑服务（如 SearxNG）。
    *   安装 Docker Desktop（内置 Docker Compose V2）：[Windows](https://docs.docker.com/desktop/install/windows-install/) | [Mac](https://docs.docker.com/desktop/install/mac-install/) | [Linux](https://docs.docker.com/desktop/install/linux-install/)
    *   或在 Linux 上分别安装 Docker Engine 和 Docker Compose：[Docker Engine](https://docs.docker.com/engine/install/) | [Docker Compose](https://docs.docker.com/compose/install/)（请确保安装的是 Compose V2，例如 `sudo apt-get install docker-compose-plugin`）。

### 1. **克隆仓库并初始化配置**

```sh
git clone https://github.com/Fosowl/agenticSeek.git
cd agenticSeek
mv .env.example .env
```

### 2. 修改 `.env` 文件内容

```sh
SEARXNG_BASE_URL="http://searxng:8080" # http://127.0.0.1:8080 if running on host
REDIS_BASE_URL="redis://redis:6379/0"
WORK_DIR="/Users/mlg/Documents/workspace_for_ai"
OLLAMA_PORT="11434"
LM_STUDIO_PORT="1234"
CUSTOM_ADDITIONAL_LLM_PORT="11435"
OPENAI_API_KEY='optional'
DEEPSEEK_API_KEY='optional'
OPENROUTER_API_KEY='optional'
TOGETHER_API_KEY='optional'
GOOGLE_API_KEY='optional'
ANTHROPIC_API_KEY='optional'
```

根据需要更新 `.env` 文件中的值：

- **SEARXNG_BASE_URL**：除非以 CLI 模式在宿主机运行，否则请保持原样。
- **REDIS_BASE_URL**：请保持原样
- **WORK_DIR**：你本地机器上的工作目录路径。AgenticSeek 将能够读取并与这些文件交互。
- **OLLAMA_PORT**：Ollama 服务的端口号。
- **LM_STUDIO_PORT**：LM Studio 服务的端口号。
- **CUSTOM_ADDITIONAL_LLM_PORT**：其他自定义 LLM 服务的端口。

**对于选择本地运行 LLM（大型语言模型）的用户，API Key 完全是可选的。**这正是本项目的主要目的。如果你的硬件足够强大，请留空即可。

### 3. **启动 Docker**

确保你的系统已安装并正在运行 Docker。你可以通过以下命令启动：

- **Linux/macOS：**
    打开终端并运行：
    ```sh
    sudo systemctl start docker
    ```
    或从应用程序菜单中启动 Docker Desktop。

- **Windows：**
    从开始菜单启动 Docker Desktop。

你可以通过执行以下命令验证 Docker 是否正在运行：
```sh
docker info
```
如果看到关于 Docker 安装的信息，说明运行正常。

请参阅下方的[本地服务提供商列表](#list-of-local-providers)以获取摘要。

下一步：[在本地运行 AgenticSeek](#start-services-and-run)

*如遇问题，请参阅[故障排除](#troubleshooting)部分。*
*如果你的硬件无法在本地运行 LLM，请参阅[使用 API 运行的设置](#setup-to-run-with-an-api)。*
*如需详细的 `config.ini` 说明，请参阅[配置部分](#config)。*

---

## 在本地机器上运行 LLM 的设置

**硬件要求：**

要在本地运行 LLM，你需要充足的硬件支持。最低要求是能够运行 Magistral、Qwen 或 Deepseek 14B 的 GPU。详细模型/性能建议请参阅 FAQ。

**配置你的本地服务提供商**

启动你的本地服务（例如使用 Ollama）：

除非你希望在宿主机上以 CLI 模式运行 AgenticSeek，否则请导出或设置服务的监听地址：

```sh
export OLLAMA_HOST=0.0.0.0:11434
```

然后启动你的服务：

```sh
ollama serve
```

请参阅下方支持的本地服务提供商列表。

**更新 `config.ini`**

修改 `config.ini` 文件，将 `provider_name` 设置为支持的服务商，并将 `provider_model` 设置为你服务商支持的 LLM。我们推荐使用推理模型，如 *Magistral* 或 *Deepseek*。

所需硬件请参阅 README 末尾的 **FAQ**。

```sh
[MAIN]
is_local = True # Whenever you are running locally or with remote provider.
provider_name = ollama # or lm-studio, openai, etc..
provider_model = deepseek-r1:14b # choose a model that fit your hardware
provider_server_address = 127.0.0.1:11434
agent_name = Jarvis # name of your AI
recover_last_session = True # whenever to recover the previous session
save_session = True # whenever to remember the current session
speak = False # text to speech
listen = False # Speech to text, only for CLI, experimental
jarvis_personality = False # Whenever to use a more "Jarvis" like personality (experimental)
languages = en zh # The list of languages, Text to speech will default to the first language on the list
[BROWSER]
headless_browser = True # leave unchanged unless using CLI on host.
stealth_mode = True # Use undetected selenium to reduce browser detection
```

**注意：**

- `config.ini` 文件格式不支持注释。请勿直接复制粘贴示例配置，否则会导致错误。请手动修改 `config.ini` 文件中的设置，并删除所有注释。
- 如果使用 LM-Studio 运行 LLM，请勿将 `provider_name` 设置为 `openai`，应设为 `lm-studio`。
- 部分服务商（如 LM-Studio）要求 IP 地址前必须带有 `http://`。例如：`http://127.0.0.1:1234`

**本地服务提供商列表**

| Provider  | Local? | Description                                               |
|-----------|--------|-----------------------------------------------------------|
| ollama    | Yes    | Run LLMs locally with ease using ollama as a LLM provider |
| lm-studio  | Yes    | Run LLM locally with LM studio (set `provider_name` to `lm-studio`)|
| openai    | Yes     |  Use openai compatible API (eg: llama.cpp server)  |

下一步：[启动服务并运行 AgenticSeek](#Start-services-and-Run)

*如遇问题，请参阅**已知问题**部分。*
*如果你的硬件无法在本地运行 LLM，请参阅[使用 API 运行的设置](#setup-to-run-with-an-api)。*
*如需详细的 `config.ini` 说明，请参阅[配置部分](#config)。*

## 使用 API 运行的设置

此设置使用外部云端 LLM 服务提供商。你需要从所选服务中获取 API Key。

**1. 选择 API 服务商并获取 API Key：**

请参阅下方的[API 服务商列表](#list-of-api-providers)。访问其网站注册并获取 API Key。

**2. 将 API Key 设置为环境变量：**


*   **Linux/macOS：**
    打开终端并使用 `export` 命令。建议将其添加到 shell 的配置文件（如 `~/.bashrc`、`~/.zshrc`）中以实现持久化。
    ```sh
    export PROVIDER_API_KEY="your_api_key_here"
    # Replace PROVIDER_API_KEY with the specific variable name, e.g., OPENAI_API_KEY, GOOGLE_API_KEY
    ```
    以 TogetherAI 为例：
    ```sh
    export TOGETHER_API_KEY="xxxxxxxxxxxxxxxxxxxxxx"
    ```
*   **Windows：**
    *   **命令提示符（仅当前会话有效）：**
        ```cmd
        set PROVIDER_API_KEY=your_api_key_here
        ```
    *   **PowerShell（仅当前会话有效）：**
        ```powershell
        $env:PROVIDER_API_KEY="your_api_key_here"
        ```
    *   **永久生效：** 在 Windows 搜索栏中搜索“环境变量”，点击“编辑系统环境变量”，然后点击“环境变量...”按钮。添加新的用户变量，名称为对应值（如 `OPENAI_API_KEY`），值为你的 Key。

    *(更多详情请参阅 FAQ：[如何设置 API Key？](#how-do-i-set-api-keys)）*


**3. 更新 `config.ini`：**
```ini
[MAIN]
is_local = False
provider_name = openai # Or google, deepseek, togetherAI, huggingface
provider_model = gpt-3.5-turbo # Or gemini-1.5-flash, deepseek-chat, mistralai/Mixtral-8x7B-Instruct-v0.1 etc.
provider_server_address = # Typically ignored or can be left blank when is_local = False for most APIs
# ... other settings ...
```
*注意：* 请确保 `config.ini` 的值末尾没有多余空格。

**API 服务商列表**

| Provider     | `provider_name` | Local? | Description                                       | API Key Link (Examples)                     |
|--------------|-----------------|--------|---------------------------------------------------|---------------------------------------------|
| OpenAI       | `openai`        | No     | Use ChatGPT models via OpenAI's API.              | [platform.openai.com/signup](https://platform.openai.com/signup) |
| Google Gemini| `google`        | No     | Use Google Gemini models via Google AI Studio.    | [aistudio.google.com/keys](https://aistudio.google.com/keys) |
| Deepseek     | `deepseek`      | No     | Use Deepseek models via their API.                | [platform.deepseek.com](https://platform.deepseek.com) |
| Hugging Face | `huggingface`   | No     | Use models from Hugging Face Inference API.       | [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) |
| TogetherAI   | `togetherAI`    | No     | Use various open-source models via TogetherAI API.| [api.together.ai/settings/api-keys](https://api.together.ai/settings/api-keys) |
| OpenRouter   | `openrouter`    | No     | Use OpenRouter Models| [https://openrouter.ai/](https://openrouter.ai/) |
| MiniMax      | `minimax`       | No     | Use MiniMax models (e.g., MiniMax-M2.7, MiniMax-M2.5).| [platform.minimax.io](https://platform.minimax.io/user-center/basic-information) |

*注意：*
*   不建议使用 `gpt-4o` 或其他 OpenAI 模型进行复杂的网页浏览和任务规划，因为当前的提示词优化主要针对 Deepseek 等模型。
*   在使用 Gemini 时，代码编写/Bash 任务可能会遇到问题，因为它可能不会严格遵循为 Deepseek 优化的格式提示词。
*   当 `is_local = False` 时，`config.ini` 中的 `provider_server_address` 通常不起作用，因为 API 端点通常已硬编码在相应服务商的库中。

下一步：[启动服务并运行 AgenticSeek](#Start-services-and-Run)

*如遇问题，请参阅**已知问题**部分。*
*如需详细的配置文件说明，请参阅**配置**部分。*

---

## 启动服务并运行

默认情况下，AgenticSeek 完全在 Docker 中运行。

**选项 1：** 在 Docker 中运行并使用 Web 界面：

启动所需服务。这将启动 `docker-compose.yml` 中的所有服务，包括：
    - searxng
    - redis（searxng 必需）
    - frontend
    - backend（使用 Web 界面时使用 `full` 参数时启动）

```sh
./start_services.sh full # MacOS
start start_services.cmd full # Window
```

**注意：** 此步骤将下载并加载所有 Docker 镜像，可能需要长达 30 分钟。启动服务后，请等待后端服务完全运行（日志中应显示 **backend: "GET /health HTTP/1.1" 200 OK**）后再发送任何消息。首次运行时，后端服务可能需要 5 分钟才能启动。

访问 `http://localhost:3000/` 即可看到 Web 界面。

*服务启动故障排除：* 如果这些脚本失败，请确保 Docker Engine 正在运行且正确安装了 Docker Compose（V2，`docker compose`）。检查终端输出中的错误信息。请参阅 [FAQ：运行 AgenticSeek 或其脚本时出现错误怎么办？](#faq-troubleshooting)

**选项 2：** CLI 模式：

若要以 CLI 界面运行，需在宿主机上安装依赖包：

```sh
./install.sh
./install.bat # windows
```

然后你必须将 `config.ini` 中的 SEARXNG_BASE_URL 修改为：

```sh
SEARXNG_BASE_URL="http://localhost:8080"
```

启动所需服务。这将启动 `docker-compose.yml` 中的部分服务，包括：
    - searxng
    - redis（searxng 必需）
    - frontend

```sh
./start_services.sh # MacOS
start start_services.cmd # Window
```

运行：`uv run python -m ensurepip` 以确保 uv 已启用 pip。

使用 CLI：`uv run cli.py`


---

## 使用方法

确保服务已通过 `./start_services.sh full` 启动并运行，然后访问 `localhost:3000` 进入 Web 界面。

你也可以在配置中设置 `listen = True` 来使用语音转文字功能。仅适用于 CLI 模式。

要退出，只需说/输入 `goodbye`。

以下是一些示例用法：

> *用 Python 写一个贪吃蛇游戏！*

> *在网络上搜索法国雷恩市的顶级咖啡馆，并将包含地址的三个结果列表保存为 rennes_cafes.txt。*

> *编写一个 Go 程序计算阶乘，将其保存为 workspace 中的 factorial.go。*

> *在我的 summer_pictures 文件夹中搜索所有 JPG 文件，用今天的日期重命名它们，并将重命名后的文件列表保存到 photos_list.txt。*

> *在网上搜索 2024 年流行的科幻电影并挑选三部今晚观看。将列表保存为 movie_night.txt。*

> *在网络上搜索 2025 年的最新 AI 新闻文章，选取三篇，编写一个 Python 脚本抓取它们的标题和摘要。将脚本保存为 /home/projects 下的 news_scraper.py，并将摘要保存到 ai_news.txt。*

> *周五，在网络上搜索免费的股票价格 API，使用 supersuper7434567@gmail.com 注册，然后编写一个 Python 脚本通过该 API 每日获取特斯拉股价，并将结果保存到 stock_prices.csv。*

*注意：表单填写功能仍处于实验阶段，可能会失败。*


输入查询后，AgenticSeek 会自动为该任务分配最合适的 agent。

由于目前仍是早期原型，agent 路由系统可能无法始终根据你的查询准确分配 agent。

因此，你需要明确表达你的需求以及希望 AI 如何操作。例如，如果你想让它进行网页搜索，不要说：

`你知道哪些适合独自旅行的好国家吗？`

而应这样问：

`进行网页搜索，找出最适合独自旅行的国家。`

---

## **在自有服务器上运行 LLM 的设置**

如果你有一台性能强劲的电脑或服务器，但想从笔记本电脑上使用它，可以选择使用我们自定义的 LLM 服务器在远程服务器上运行模型。

在你将运行 AI 模型的“服务器”上获取 IP 地址：

```sh
ip a | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | cut -d/ -f1 # local ip
curl https://ipinfo.io/ip # public ip
```

注意：Windows 或 macOS 用户请分别使用 `ipconfig` 或 `ifconfig` 查找 IP 地址。

克隆仓库并进入 `server/` 文件夹。


```sh
git clone --depth 1 https://github.com/Fosowl/agenticSeek.git
cd agenticSeek/llm_server/
```

安装服务器特定依赖：

```sh
pip3 install -r requirements.txt
```

运行服务器脚本。

```sh
python3 app.py --provider ollama --port 3333
```

你可以选择使用 `ollama` 或 `llamacpp` 作为 LLM 服务。


现在在你的个人电脑上：

修改 `config.ini` 文件，将 `provider_name` 设为 `server`，将 `provider_model` 设为 `deepseek-r1:xxb`。
将 `provider_server_address` 设置为运行模型的机器的 IP 地址。

```sh
[MAIN]
is_local = False
provider_name = server
provider_model = deepseek-r1:70b
provider_server_address = http://x.x.x.x:3333
```


下一步：[启动服务并运行 AgenticSeek](#Start-services-and-Run)

---

## 语音转文字 (Speech-to-Text)

**注意：** 目前语音转文字功能仅在 CLI 模式下可用。

请注意，当前语音转文字仅支持英语。

语音转文字功能默认处于禁用状态。要启用它，请在 `config.ini` 文件中将 `listen` 选项设置为 True：

```
listen = True
```

启用后，语音转文字功能会在开始处理输入前监听触发词（即 agent 名称）。你可以通过修改 *config.ini* 文件中的 `agent_name` 值来自定义 agent 名称：

```
agent_name = Friday
```

为了获得最佳识别效果，建议将 agent 名称设置为常见的英文名字（如 "John" 或 "Emma"）

当你看到转录文本开始显示时，大声说出 agent 的名称以唤醒它（例如，“Friday”）。

清晰地读出你的查询内容。

在请求末尾加上确认短语以提示系统继续执行。确认短语示例包括：
```
"do it", "go ahead", "execute", "run", "start", "thanks", "would ya", "please", "okay?", "proceed", "continue", "go on", "do that", "go it", "do you understand?"
```

## 配置 (Config)

示例配置：
```
[MAIN]
is_local = True
provider_name = ollama
provider_model = deepseek-r1:32b
provider_server_address = http://127.0.0.1:11434 # Example for Ollama; use http://127.0.0.1:1234 for LM-Studio
agent_name = Friday
recover_last_session = False
save_session = False
speak = False
listen = False

jarvis_personality = False
languages = en zh # List of languages for TTS and potentially routing.
[BROWSER]
headless_browser = False
stealth_mode = False
```

**`config.ini` 设置说明**：

*   **[MAIN] 部分：**
    *   `is_local`：使用本地 LLM 服务商（Ollama、LM-Studio、本地 OpenAI 兼容服务器）或自托管服务器选项时设为 `True`。使用云端 API（OpenAI、Google 等）时设为 `False`。
    *   `provider_name`：指定 LLM 服务商。
        *   本地选项：`ollama`、`lm-studio`、`openai`（用于本地 OpenAI 兼容服务器）、`server`（用于自托管服务器设置）。
        *   API 选项：`openai`、`google`、`deepseek`、`huggingface`、`togetherAI`。
    *   `provider_model`：所选服务商的具体模型名称或 ID（例如 Ollama 的 `deepseekcoder:6.7b`，OpenAI API 的 `gpt-3.5-turbo`，TogetherAI 的 `mistralai/Mixtral-8x7B-Instruct-v0.1`）。
    *   `provider_server_address`：你的 LLM 服务商的地址。
        *   本地服务商：例如 Ollama 的 `http://127.0.0.1:11434`，LM-Studio 的 `http://127.0.0.1:1234`。
        *   `server` 服务商类型：你的自托管 LLM 服务器地址（例如 `http://your_server_ip:3333`）。
        *   云端 API（`is_local = False`）：通常会被忽略或留空，因为 API 端点通常由客户端库处理。
    *   `agent_name`：AI 助手的名称（例如 Friday）。如果启用语音转文字，将用作触发词。
    *   `recover_last_session`：尝试恢复上次会话状态设为 `True`，从头开始设为 `False`。
    *   `save_session`：保存当前会话状态以便后续恢复设为 `True`，否则为 `False`。
    *   `speak`：启用文字转语音输出设为 `True`，禁用设为 `False`。
    *   `listen`：启用语音转文字输入（仅限 CLI 模式）设为 `True`，禁用设为 `False`。
    *   `work_dir`：**关键**：AgenticSeek 读写文件的目录。**请确保此路径在你的系统中有效且可访问。**
    *   `jarvis_personality`：使用更偏向“Jarvis”风格的系统提示词（实验性）设为 `True`，标准提示词设为 `False`。
    *   `languages`：逗号分隔的语言列表（例如 `en, zh, fr`）。用于 TTS 语音选择（默认为第一个），并可辅助 LLM 路由。为避免降低路由效率，请避免设置过多或过于相似的语言。
*   **[BROWSER] 部分：**
    *   `headless_browser`：在无可见窗口的情况下运行自动化浏览器（推荐用于 Web 界面或非交互使用）设为 `True`。显示浏览器窗口（适用于 CLI 模式或调试）设为 `False`。
    *   `stealth_mode`：启用使浏览器自动化更难被检测的措施。可能需要手动安装 anticaptcha 等浏览器扩展。


本节总结了支持的 LLM 服务商类型。请在 `config.ini` 中进行配置。

**本地服务商（在自有硬件上运行）：**

| Provider Name in `config.ini` | `is_local` | Description                                                                 | Setup Section                                                    |
|-------------------------------|------------|-----------------------------------------------------------------------------|------------------------------------------------------------------|
| `ollama`                      | `True`     | Use Ollama to serve local LLMs.                                             | [Setup for running LLM locally](#setup-for-running-llm-locally-on-your-machine) |
| `lm-studio`                   | `True`     | Use LM-Studio to serve local LLMs.                                          | [Setup for running LLM locally](#setup-for-running-llm-locally-on-your-machine) |
| `openai` (for local server)   | `True`     | Connect to a local server that exposes an OpenAI-compatible API (e.g., llama.cpp). | [Setup for running LLM locally](#setup-for-running-llm-locally-on-your-machine) |
| `server`                      | `False`    | Connect to the AgenticSeek self-hosted LLM server running on another machine. | [Setup to run the LLM on your own server](#setup-to-run-the-llm-on-your-own-server) |

**API 服务商（基于云端）：**

| Provider Name in `config.ini` | `is_local` | Description                                      | Setup Section                                       |
|-------------------------------|------------|--------------------------------------------------|-----------------------------------------------------|
| `openai`                      | `False`    | Use OpenAI's official API (e.g., GPT-3.5, GPT-4). | [Setup to run with an API](#setup-to-run-with-an-api) |
| `google`                      | `False`    | Use Google's Gemini models via API.              | [Setup to run with an API](#setup-to-run-with-an-api) |
| `deepseek`                    | `False`    | Use Deepseek's official API.                     | [Setup to run with an API](#setup-to-run-with-an-api) |
| `huggingface`                 | `False`    | Use Hugging Face Inference API.                  | [Setup to run with an API](#setup-to-run-with-an-api) |
| `togetherAI`                  | `False`    | Use TogetherAI's API for various open models.    | [Setup to run with an API](#setup-to-run-with-an-api) |

---
## 故障排除 (Troubleshooting)

如果遇到任何问题，本节提供相关指导。

# 已知问题

## ChromeDriver 相关问题

**错误示例：** `SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version XXX`

### 根本原因

出现 ChromeDriver 版本不兼容通常是因为：
1. 已安装的 ChromeDriver 版本与你的 Chrome 浏览器版本不匹配
2. 在 Docker 环境中，`undetected_chromedriver` 可能会下载自己的 ChromeDriver 版本，从而绕过挂载的二进制文件

### 解决步骤

#### 1. 检查你的 Chrome 版本

打开 Google Chrome → `设置 > 关于 Chrome` 查看版本号（例如：“Version 134.0.6998.88”）

#### 2. 下载匹配的 ChromeDriver

**适用于 Chrome 115 及以上版本：** 使用 [Chrome for Testing API](https://googlechromelabs.github.io/chrome-for-testing/)
- 访问 Chrome for Testing 可用性仪表板
- 查找你的 Chrome 版本或最接近的可用匹配项
- 下载适合你操作系统的 ChromeDriver（Docker 环境请选择 Linux64）

**适用于较旧的 Chrome 版本：** 使用[传统 ChromeDriver 下载页面](https://chromedriver.chromium.org/downloads)

![Download ChromeDriver from Chrome for Testing](./media/chromedriver_readme.png)

#### 3. 安装 ChromeDriver（任选一种方法）

**方法 A：项目根目录（推荐用于 Docker）**
```bash
# Place the downloaded chromedriver binary in your project root
cp path/to/downloaded/chromedriver ./chromedriver
chmod +x ./chromedriver  # Make executable on Linux/macOS
```

**方法 B：系统 PATH**
```bash
# Linux/macOS
sudo mv chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver

# Windows: Place chromedriver.exe in a folder that's in your PATH
```

#### 4. 验证安装
```bash
# Test the ChromeDriver version
./chromedriver --version
# OR if in PATH:
chromedriver --version
```

### Docker 特定说明

⚠️ **Docker 用户重要提示：**
- Docker 卷挂载方式可能与隐身模式（`undetected_chromedriver`）不兼容
- **解决方案**：将 ChromeDriver 放置在项目根目录，命名为 `./chromedriver`
- 应用程序会自动检测并使用该二进制文件
- 日志中应显示：`"Using ChromeDriver from project root: ./chromedriver"`

### 故障排除技巧

1. **仍然出现版本不匹配？**
   - 验证 ChromeDriver 是否可执行：`ls -la ./chromedriver`
   - 检查 ChromeDriver 版本：`./chromedriver --version`
   - 确保它与你的 Chrome 浏览器版本匹配

2. **Docker 容器问题？**
   - 检查后端日志：`docker logs backend`
   - 查找以下消息：`"Using ChromeDriver from project root"`
   - 如果未找到，请验证文件是否存在且可执行

3. **Chrome for Testing 版本**
   - 尽可能使用精确匹配的版本
   - 对于版本 134.0.6998.88，请使用 ChromeDriver 134.0.6998.165（最接近的可用版本）
   - 主版本号必须匹配（134 = 134）

### 版本兼容性矩阵

| Chrome Version | ChromeDriver Version | Status |
|----------------|---------------------|---------|
| 134.0.6998.x   | 134.0.6998.165     | ✅ Works |
| 133.0.6943.x   | 133.0.6943.141     | ✅ Works |
| 132.0.6834.x   | 132.0.6834.159     | ✅ Works |

*如需最新兼容性信息，请访问 [Chrome for Testing 仪表板](https://googlechromelabs.github.io/chrome-for-testing/)*

`Exception: Failed to initialize browser: Message: session not created: This version of ChromeDriver only supports Chrome version 113
Current browser version is 134.0.6998.89 with binary path`

如果浏览器与 ChromeDriver 版本不匹配，就会出现此问题。

你需要前往以下页面下载最新版本：

https://developer.chrome.com/docs/chromedriver/downloads

如果你使用的是 Chrome 115 或更高版本，请前往：

https://googlechromelabs.github.io/chrome-for-testing/

并下载匹配你操作系统的 ChromeDriver 版本。

![alt text](./media/chromedriver_readme.png)

如果本节内容不完整，请提交 Issue。

## 从 Docker 后端连接 Ollama 失败

```
An error occurred: Provider ollama failed:
Ollama connection failed at http://host.docker.internal:11434. Check if the server is running.
```

前端显示 `Error: Unable to get a response.`，后端在 `/query` 返回 HTTP 500。

*   **原因：** 当 AgenticSeek 在 Docker 中运行时，后端通过 `host.docker.internal` 访问宿主机的 Ollama。Docker 模式下仅使用 `provider_server_address` 的**端口**；主机部分会被 `.env` 中的 `DOCKER_INTERNAL_URL` 替换。因此失败并非配置拼写错误——而是宿主机上的 Ollama 仅绑定在 `127.0.0.1:11434`，拒绝来自 Docker 桥接网络的连接。
*   **请勿**在 `config.ini` 中修改 `provider_server_address = 127.0.0.1:11434`——容器内会忽略主机部分。
*   **解决方案：** 在宿主机上设置 `OLLAMA_HOST=0.0.0.0:11434` 使 Ollama 绑定到所有接口：

    手动运行 `ollama serve`：
    ```bash
    OLLAMA_HOST=0.0.0.0:11434 ollama serve
    ```

    **永久解决方案：**

    systemd（Linux）：
    ```bash
    sudo systemctl edit ollama
    ```
    添加：
    ```
    [Service]
    Environment="OLLAMA_HOST=0.0.0.0:11434"
    ```
    然后执行：
    ```bash
    sudo systemctl daemon-reload
    sudo systemctl restart ollama
    ```

    macOS（Ollama.app）：
    ```bash
    launchctl setenv OLLAMA_HOST "0.0.0.0:11434"
    ```
    然后退出并重新启动 Ollama 应用。

*   在后端容器内验证：
    ```bash
    docker compose exec backend curl -sS http://host.docker.internal:11434/api/tags
    ```
    你应该会收到一个包含模型列表的 JSON。

*   **仅限 Linux 的注意事项：** 仅当 docker-compose 映射时，`host.docker.internal` 才能在容器内解析。请确保 `docker-compose.yml` 中的后端服务包含：
    ```yaml
    extra_hosts:
      - "host.docker.internal:host-gateway"
    ```
    在 Docker Desktop（macOS / Windows）上可开箱即用。

*   **防火墙：** 如果启用了 `ufw` / `firewalld`，请允许 Docker 桥接网络访问 11434：
    ```bash
    sudo ufw allow from 172.16.0.0/12 to any port 11434
    ```

## Connection Adapters 相关问题

```
Exception: Provider lm-studio failed: HTTP request failed: No connection adapters were found for '127.0.0.1:1234/v1/chat/completions'` (Note: port may vary)
```

*   **原因：** `config.ini` 中 `lm-studio`（或其他类似的本地 OpenAI 兼容服务器）的 `provider_server_address` 缺少 `http://` 前缀，或指向了错误的端口。
*   **解决方案：**
    *   确保地址包含 `http://`。LM-Studio 通常默认为 `http://127.0.0.1:1234`。
    *   修正 `config.ini`：`provider_server_address = http://127.0.0.1:1234`（或你实际的 LM-Studio 服务器端口）。

## 未提供 SearxNG 基础 URL

```
raise ValueError("SearxNG base URL must be provided either as an argument or via the SEARXNG_BASE_URL environment variable.")
ValueError: SearxNG base URL must be provided either as an argument or via the SEARXNG_BASE_URL environment variable.`
```

如果你在运行 CLI 模式时使用了错误的 SearxNG 基础 URL，可能会出现此问题。

`SEARXNG_BASE_URL` 应根据你是在 Docker 中还是宿主机上运行来设置：

**在宿主机运行**： `SEARXNG_BASE_URL="http://localhost:8080"`

**完全在 Docker 中运行（Web 界面）**： `SEARXNG_BASE_URL="http://searxng:8080"`

## 常见问题 (FAQ)

**问：我需要什么样的硬件？**

| Model Size  | GPU  | Comment                                               |
|-----------|--------|-----------------------------------------------------------|
| 7B        | 8GB Vram | ⚠️ Not recommended. Performance is poor, frequent hallucinations, and planner agents will likely fail. |
| 14B        | 12 GB VRAM (e.g. RTX 3060) | ✅ Usable for simple tasks. May struggle with web browsing and planning tasks. |
| 32B        | 24+ GB VRAM (e.g. RTX 4090) | 🚀 Success with most tasks, might still struggle with task planning |
| 70B+        | 48+ GB Vram | 💪 Excellent. Recommended for advanced use cases. |

**问：遇到错误该怎么办？**

确保本地服务正在运行（执行 `ollama serve`），你的 `config.ini` 与服务商匹配，且依赖已安装。如果尝试后仍无效，欢迎提交 Issue。

**问：它真的能 100% 本地运行吗？**

是的，使用 Ollama、lm-studio 或 server 服务商时，所有语音转文字、LLM 和文字转语音模型均可在本地运行。非本地选项（如 OpenAI 或其他 API）为可选配置。

**问：既然我有 Manus，为什么还要用 AgenticSeek？**

与 Manus 不同，AgenticSeek 优先考虑对外部系统的独立性，让你拥有更多控制权、隐私保护，并避免 API 费用。

**问：项目背后的团队是谁？**

该项目由我创建，并得到了两位来自 GitHub 开源社区的朋友（担任维护者和贡献者）的支持。我们只是一群充满热情的个人开发者，并非初创公司或隶属于任何组织。
除我的个人账号（https://x.com/Martin993886460）外，X 平台上任何其他的 AgenticSeek 账号均为冒充。

## 参与贡献 (Contribute)

我们正在寻找开发者来改进 AgenticSeek！请查看开放 Issue 或讨论区。

[贡献指南](./docs/CONTRIBUTING.md)


## 赞助商：(Sponsors:)

想要通过航班搜索、旅行规划或抢购最佳购物优惠等功能提升 AgenticSeek 的能力吗？建议结合 SerpApi 打造自定义工具，解锁更多类 Jarvis 的功能。借助 SerpApi，你可以在完全掌控的前提下为代理执行专业任务加速赋能。

<a href="https://serpapi.com/"><img src="./media/banners/sponsor_banner_serpapi.png" height="350" alt="SerpApi Banner" ></a>

请参阅 [Contributing.md](./docs/CONTRIBUTING.md) 了解如何集成自定义工具！

### **赞助支持者**：(Patron sponsor:)

- [tatra-labs](https://github.com/tatra-labs)

## 维护者：(Maintainers:)

 > [Fosowl](https://github.com/Fosowl) | Paris Time
 > [antoineVIVIES](https://github.com/antoineVIVIES) | Taipei Time

## 特别感谢：(Special Thanks:)

 > [tcsenpai](https://github.com/tcsenpai) and [plitc](https://github.com/plitc) For helping with backend dockerization

[![Star History Chart](https://api.star-history.com/svg?repos=Fosowl/agenticSeek&type=Date)](https://www.star-history.com/#Fosowl/agenticSeek&Date)