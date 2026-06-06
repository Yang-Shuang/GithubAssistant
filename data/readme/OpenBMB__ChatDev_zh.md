# ChatDev 2.0 - DevAll

<p align="center">
  <img src="frontend/public/media/logo.png" alt="DevAll Logo" width="500"/>
</p>


<p align="center">
  <strong>一个用于“开发一切”的零代码多智能体平台</strong>
</p>

<p align="center">
  【<a href="./README.md">English</a> | <a href="./README-zh.md">简体中文</a>】
</p>
<p align="center">
    【📚 <a href="#developers">开发者</a> | 👥 <a href="#primary-contributors">贡献者</a>｜⭐️ <a href="https://github.com/OpenBMB/ChatDev/tree/chatdev1.0">ChatDev 1.0 (旧版)</a>】
</p>

## 📖 概述
ChatDev 已从专用的软件开发多智能体系统演进为一个全面的**多智能体编排平台**。

- <a href="https://github.com/OpenBMB/ChatDev/tree/main">**ChatDev 2.0 (DevAll)**</a> 是一个用于“开发一切”的**零代码多智能体平台**。它通过简单的配置赋能你快速构建并运行定制化的多智能体系统。无需编写代码，你即可定义智能体（Agent）、工作流和任务，以编排数据可视化、3D生成和深度研究等复杂场景。
- <a href="https://github.com/OpenBMB/ChatDev/tree/chatdev1.0">**ChatDev 1.0 (旧版)**</a> 作为一个**虚拟软件公司**运行。它利用参与专业功能研讨会的各类智能体（如 CEO、CTO、程序员）来自动化整个软件开发生命周期——包括设计、编码、测试和文档编写。它为通信式智能体协作提供了基础范式。

## 🎉 动态
• **2026年1月7日：🚀 我们很高兴地宣布 ChatDev 2.0 (DevAll) 正式发布！** 该版本引入了零代码多智能体编排平台。经典的 ChatDev（v1.x）已移至 [`chatdev1.0`](https://github.com/OpenBMB/ChatDev/tree/chatdev1.0) 分支进行维护。关于 ChatDev 2.0 的更多详情请参阅[我们的官方帖子](https://x.com/OpenBMB/status/2008916790399701335)。

<details>
<summary>历史动态</summary>

• **2025年9月24日：🎉** 我们的论文 [《通过演化编排实现多智能体协作》](https://arxiv.org/abs/2505.19591) 已被 NeurIPS 2025 接收。相关代码已发布于本仓库的 `puppeteer` 分支中。

• **2025年5月26日：🎉** 我们提出了一种新颖的“操纵者（Puppeteer）”风格范式，用于基于大语言模型的智能体协作。通过利用强化学习优化的可学习中央编排器，我们的方法动态激活并排序智能体，以构建高效、上下文感知的推理路径。该方法不仅提升了推理质量，还降低了计算成本，使得复杂任务中的可扩展且适应性强的多智能体合作成为可能。详见论文 [《通过演化编排实现多智能体协作》](https://arxiv.org/abs/2505.19591)。
  <p align="center">
  <img src='./assets/puppeteer.png' width=800>
  </p>

• **2024年6月25日：🎉** 为了促进由大语言模型驱动的多智能体协作🤖🤖及相关领域的发展，ChatDev 团队精心整理了一系列开创性论文📄，并以[开源](https://github.com/OpenBMB/ChatDev/tree/main/MultiAgentEbook)交互式电子书📚格式发布。现在你可以在 [电子书网站](https://thinkwee.top/multiagent_ebook) 上探索最新进展，并下载 [论文列表](https://github.com/OpenBMB/ChatDev/blob/main/MultiAgentEbook/papers.csv)。
  <p align="center">
  <img src='./assets/ebook.png' width=800>
  </p>
  
• **2024年6月12日：** 我们推出了多智能体协作网络（MacNet）🎉，该网络利用有向无环图通过语言交互促进智能体之间有效的任务导向型协作🤖🤖。MacNet 支持跨多种拓扑结构以及超过一千个智能体的协作，且不会超出上下文限制。相比 ChatDev 的链式拓扑结构，MacNet 更具多功能性和可扩展性，可视为其进阶版本。我们的预印本论文发布于 [https://arxiv.org/abs/2406.07155](https://arxiv.org/abs/2406.07155)。该技术已整合至 [macnet](https://github.com/OpenBMB/ChatDev/tree/macnet) 分支，增强了对多样化组织结构的支持，并提供了超越软件开发的更丰富解决方案（例如逻辑推理、数据分析、故事生成等）。
  <p align="center">
  <img src='./assets/macnet.png' width=500>
  </p>

• **2024年5月7日：** 我们引入了“迭代经验优化”（IER）方法，在该方法中，导师智能体与助手智能体通过增强面向捷径的经验来高效适应新任务。该方法涵盖了一系列任务中的经验获取、利用、传播和消除过程，使流程更短更高效。我们的预印本论文发布于 https://arxiv.org/abs/2405.04219，该技术将很快整合到 ChatDev 中。
  <p align="center">
  <img src='./assets/ier.png' width=220>
  </p>

• **2024年1月25日：** 我们已将经验协同学习模块（Experiential Co-Learning Module）整合到 ChatDev 中。请参阅 [经验协同学习指南](wiki.md#co-tracking)。

• **2023年12月28日：** 我们提出了经验协同学习方法，导师与助手智能体在此过程中积累面向捷径的经验以有效解决新任务，从而减少重复错误并提升效率。查看我们的预印本论文 https://arxiv.org/abs/2312.17025，该技术将很快整合到 ChatDev 中。
  <p align="center">
  <img src='./assets/ecl.png' width=860>
  </p>

• **2023年11月15日：** 我们以 SaaS 平台形式推出了 ChatDev，旨在帮助软件开发人员和创新创业者以极低的成本高效构建软件，并降低使用门槛。请访问 https://chatdev.modelbest.cn/ 体验。
  <p align="center">
  <img src='./assets/saas.png' width=560>
  </p>

• **2023年11月2日：** ChatDev 现已支持增量开发功能，允许智能体在现有代码基础上进行开发。尝试运行 ```--config "incremental" --path "[source_code_directory_path]"``` 以启用该功能。
  <p align="center">
  <img src='./assets/increment.png' width=700>
  </p>

• **2023年10月26日：** ChatDev 现已支持通过 Docker 进行安全运行（感谢 [ManindraDeMel](https://github.com/ManindraDeMel) 的贡献）。请参阅 [Docker 启动指南](wiki.md#docker-start)。
  <p align="center">
  <img src='./assets/docker.png' width=400>
  </p>
  
• **2023年9月25日：** 现已开放 **Git** 模式，使程序员 <img src='visualizer/static/figures/programmer.png' height=20> 能够利用 Git 进行版本控制。要启用此功能，只需在 ``ChatChainConfig.json`` 中将 ``"git_management"`` 设置为 ``"True"`` 即可。详见 [指南](wiki.md#git-mode)。
  <p align="center">
  <img src='./assets/github.png' width=600>
  </p>

• **2023年9月20日：** 现已开放 **人机交互（Human-Agent-Interaction）** 模式！你可以扮演评审员 <img src='visualizer/static/figures/reviewer.png' height=20> 的角色，参与 ChatDev 团队的工作并向程序员 <img src='visualizer/static/figures/programmer.png' height=20> 提出建议；尝试运行 ``python3 run.py --task [description_of_your_idea] --config "Human"``。详见 [指南](wiki.md#human-agent-interaction) 和 [示例](WareHouse/Gomoku_HumanAgentInteraction_20230920135038)。
  <p align="center">
  <img src='./assets/Human_intro.png' width=600>
  </p>

• **2023年9月1日：** 现已开放 **艺术（Art）** 模式！你可以激活设计师智能体 <img src='visualizer/static/figures/designer.png' height=20> 来生成软件中使用的图像；尝试运行 ``python3 run.py --task [description_of_your_idea] --config "Art"``。详见 [指南](wiki.md#art) 和 [示例](WareHouse/gomokugameArtExample_THUNLP_20230831122822)。
  
• **2023年8月28日：** 系统正式对外开放。

• **2023年8月17日：** v1.0.0 版本准备发布。

• **2023年7月30日：** 用户现在可以自定义 ChatChain、阶段（Phase）和角色（Role）设置。此外，系统现已支持在线日志模式和回放模式。

• **2023年7月16日：** 与本项目的[预印本论文](https://arxiv.org/abs/2307.07924)已发表。

• **2023年6月30日：** ChatDev 仓库初始版本发布。
</details>


## 🚀 快速开始

### 📋 前置要求

*   **操作系统**：macOS / Linux / WSL / Windows
*   **Python**：3.12+
*   **Node.js**：18+
*   **包管理器**：[uv](https://docs.astral.sh/uv/)

### 📦 安装

1.  **后端依赖**（由 `uv` 管理 Python）：
    ```bash
    uv sync
    ```

2.  **前端依赖**（Vite + Vue 3）：
    ```bash
    cd frontend && npm install
    ```

### 🔑 配置

*   **环境变量**：
    ```bash
    cp .env.example .env
    ```
*   **模型密钥**：在 `.env` 中为你的大语言模型（LLM）提供商设置 `API_KEY` 和 `BASE_URL`。
*   **YAML 占位符**：在配置文件中使用 `${VAR}`（例如 `${API_KEY}`）来引用这些变量。

### ⚡️ 运行应用

#### 使用 Makefile（推荐）

**启动后端和前端**：
```bash
make dev
```

> 随后访问 Web 控制台：**[http://localhost:5173](http://localhost:5173)**。

#### 手动命令

1.  **启动后端**：
    ```bash
    # Run from the project root
    uv run python server_main.py --port 6400 --reload
    ```
    > `--reload` 仅监听服务器的 Python 源码文件夹；`WareHouse/` 下由智能体生成的文件不再触发重启。可通过传递 `--reload-dir` 或 `--reload-exclude`（可重复使用）来自定义。

2.  **启动前端**：
    ```bash
    cd frontend
    VITE_API_BASE_URL=http://localhost:6400 npm run dev
    ```
    > 随后访问 Web 控制台：**[http://localhost:5173](http://localhost:5173)**。 
    
    
    > **💡 提示**：如果前端无法连接后端，默认端口 `6400` 可能已被占用。请将两个服务切换至可用端口，例如：
    >
    > *   **后端**：使用 `--port 6401` 启动
    > *   **前端**：设置 `VITE_API_BASE_URL=http://localhost:6401`

#### 辅助命令

*   **帮助命令**：
    ```bash
    make help
    ```

*   **同步 YAML 工作流到前端**：
    ```bash
    make sync
    ```
    将 `yaml_instance/` 中的所有工作流文件上传至数据库。

*   **验证所有 YAML 工作流**：
    ```bash
    make validate-yamls
    ```
    检查所有 YAML 文件的语法和模式错误。

### 🦞 使用 OpenClaw 运行
OpenClaw 可以通过调用现有的智能体团队或在 ChatDev 内动态创建新的智能体团队，从而与 ChatDev 集成。开始使用：
1. 启动 ChatDev 2.0 后端服务。
2. 为你的 OpenClaw 实例安装所需技能：
    ```bash
    clawdhub install chatdev
    ```

3. 让你的 OpenClaw 创建一个 ChatDev 工作流。例如：

*   **自动化信息采集与内容发布**

  ```
  Create a ChatDev workflow to automatically collect trending information, generate a Xiaohongshu post, and publish it.
  ```

*   **多智能体地缘政治模拟**
  ```
  Create a ChatDev workflow with multiple agents to simulate possible future developments of the Middle East situation.
  ```


### 🐳 使用 Docker 运行
或者，你也可以使用 Docker Compose 运行整个应用程序。此方法简化了依赖管理并提供一致的环境。

1.  **前置要求**：
    *   已安装 [Docker](https://docs.docker.com/get-docker/) 和 [Docker Compose](https://docs.docker.com/compose/install/)。
    *   确保项目根目录下有包含 API 密钥的 `.env` 文件。

2.  **构建与运行**：
    ```bash
    # From the project root
    docker compose up --build
    ```

3.  **访问地址**：
    *   **后端**：`http://localhost:6400`
    *   **前端**：`http://localhost:5173`

> 如果服务崩溃，它们将自动重启；本地文件的更改也会实时反映在容器内，以便进行热更新开发。

---

## 💡 使用方法

### 🖥️ Web 控制台

DevAll 界面为构建和运行提供了无缝体验：

*   **教程**：平台内置全面的逐步指南和文档，帮助你快速上手。
<img src="assets/tutorial-en.png"/> 

*   **工作流**：可视化画布用于设计你的多智能体系统。通过拖拽轻松配置节点参数、定义上下文流程并编排复杂的智能体交互。
<img src="assets/workflow.gif"/>

*   **启动**：发起工作流，监控实时日志，检查中间产物，并提供人机协同反馈（human-in-the-loop）。
<img src="assets/launch.gif"/>

### 🧰 Python SDK
如需自动化和批量处理，请使用我们轻量级的 Python SDK 以编程方式执行工作流并直接获取结果。

```python
from runtime.sdk import run_workflow

# Execute a workflow and get the final node message
result = run_workflow(
    yaml_file="yaml_instance/demo.yaml",
    task_prompt="Summarize the attached document in one sentence.",
    attachments=["/path/to/document.pdf"],
    variables={"API_KEY": "sk-xxxx"} # Override .env variables if needed
)

if result.final_message:
    print(f"Output: {result.final_message.text_content()}")
```

**我们已经发布了 ChatDev Python SDK（PyPI 包名为 `chatdev`）**，你也可以直接在 Python 中运行 YAML 工作流和多智能体任务。安装及版本详情请参阅 [PyPI: chatdev 0.1.0](https://pypi.org/project/chatdev/0.1.0/)。

---

<a id="developers"></a>
## ⚙️ 开发者指南

**如需进行二次开发与扩展，请阅读本节内容。**

通过新增节点、提供者和工具来扩展 DevAll。项目采用模块化结构组织：
*   **核心系统**：`server/` 托管 FastAPI 后端，而 `runtime/` 管理智能体抽象与工具执行。
*   **编排模块**：`workflow/` 处理多智能体逻辑，由 `entity/` 中的配置驱动。
*   **前端**：`frontend/` 包含基于 Vue 3 的 Web 控制台。
*   **扩展性**：`functions/` 用于存放自定义 Python 工具。

相关参考文档：
*   **入门指南**：[启动指南](./docs/user_guide/en/index.md)
*   **核心模块**：[工作流编写](./docs/user_guide/en/workflow_authoring.md)、[记忆机制](./docs/user_guide/en/modules/memory.md) 和 [工具集成](./docs/user_guide/en/modules/tooling/index.md)

---

## 🌟 精选工作流
我们为常见场景提供了强大且开箱即用的模板。所有可运行的工作流配置均位于 `yaml_instance/` 目录中。
*   **演示**：以 `demo_*.yaml` 命名的文件展示了特定功能或模块。
*   **实现案例**：直接命名的文件（例如 `ChatDev_v1.yaml`）为完整的内部开发或重建工作流。具体如下：

### 📋 工作流合集

| 类别 | 工作流                                                                                                    | 案例 | 
| :--- |:------------------------------------------------------------------------------------------------------------| :--- | 
| **📈 数据可视化** | `data_visualization_basic.yaml`<br>`data_visualization_enhanced.yaml`                                       | <img src="assets/cases/data_analysis/data_analysis.gif" width="100%"><br>Prompt: *"Create 4–6 high-quality PNG charts for my large real-estate transactions dataset."* |
| **🛠️ 3D 生成**<br>*(Requires [Blender](https://www.blender.org/) & [blender-mcp](https://github.com/ahujasid/blender-mcp))* | `blender_3d_builder_simple.yaml`<br>`blender_3d_builder_hub.yaml`<br>`blender_scientific_illustration.yaml` | <img src="assets/cases/3d_generation/3d.gif" width="100%"><br>Prompt: *"Please build a Christmas tree."* |
| **🎮 游戏开发** | `GameDev_v1.yaml`<br>`ChatDev_v1.yaml`                                                                      | <img src="assets/cases/game_development/game.gif" width="100%"><br>Prompt: *"Please help me design and develop a Tank Battle game."* |
| **📚 深度研究** | `deep_research_v1.yaml`                                                                                     | <img src="assets/cases/deep_research/deep_research.gif" width="85%"><br>Prompt: *"Research about recent advances in the field of LLM-based agent RL"* |
| **🎓 教学视频** | `teach_video.yaml` (Please run command `uv add manim` before running this workflow)                         | <img src="assets/cases/video_generation/video.gif" width="140%"><br>Prompt: *"讲一下什么是凸优化"* |

---

### 💡 使用指南
对于这些实现案例，你可以使用 **启动（Launch）** 选项卡来运行它们。
1.  **选择**：在 **启动** 选项卡中选择一个工作流。
2.  **上传**：如有需要，上传必要文件（例如数据分析所需的 `.csv` 文件）。
3.  **提示词**：输入你的需求（例如 *“可视化销售趋势”* 或 *“设计一个贪吃蛇游戏”*）。

---

## 🤝 贡献指南

我们欢迎社区的贡献！无论你是修复 bug、添加新的工作流模板，还是分享由 DevAll 生成的高质量案例/产物，我们都非常感谢你的帮助。欢迎随时通过提交 **Issue（问题）** 或 **PR（拉取请求）** 进行贡献。

为 DevAll 做出贡献后，你将在下方的 **贡献者** 名单中获得署名。请查阅我们的[开发者指南](#developers)开始你的贡献之旅！

### 👥 贡献者

#### 核心贡献者

<table>
  <tr>
    <td align="center"><a href="https://github.com/NA-Wen"><img src="https://github.com/NA-Wen.png?size=100" width="64px;" alt=""/><br /><sub><b>NA-Wen</b></sub></a></td>
    <td align="center"><a href="https://github.com/zxrys"><img src="https://github.com/zxrys.png?size=100" width="64px;" alt=""/><br /><sub><b>zxrys</b></sub></a></td>
    <td align="center"><a href="https://github.com/swugi"><img src="https://github.com/swugi.png?size=100" width="64px;" alt=""/><br /><sub><b>swugi</b></sub></a></td>
    <td align="center"><a href="https://github.com/huatl98"><img src="https://github.com/huatl98.png?size=100" width="64px;" alt=""/><br /><sub><b>huatl98</b></sub></a></td>
  </tr>
</table>

#### 贡献者
<table>
  <tr>
    <td align="center"><a href="https://github.com/LaansDole"><img src="https://github.com/LaansDole.png?size=100" width="64px;"/><br /><sub><b>LaansDole</b></sub></a></td>
    <td align="center"><a href="https://github.com/zivkovicp"><img src="https://github.com/zivkovicp.png?size=100" width="64px;"/><br /><sub><b>zivkovicp</b></sub></a></td>
    <td align="center"><a href="https://github.com/ACE-Prism"><img src="https://github.com/ACE-Prism.png?size=100" width="64px;"/><br /><sub><b>ACE-Prism</b></sub></a></td>
    <td align="center"><a href="https://github.com/shiowen"><img src="https://github.com/shiowen.png?size=100" width="64px;"/><br /><sub><b>shiowen</b></sub></a></td>
    <td align="center"><a href="https://github.com/kilo2127"><img src="https://github.com/kilo2127.png?size=100" width="64px;"/><br /><sub><b>kilo2127</b></sub></a></td>
    <td align="center"><a href="https://github.com/AckerlyLau"><img src="https://github.com/AckerlyLau.png?size=100" width="64px;"/><br /><sub><b>AckerlyLau</b></sub></a></td>
    <td align="center"><a href="https://github.com/rainoeelmae"><img src="https://github.com/rainoeelmae.png?size=100" width="64px;"/><br /><sub><b>rainoeelmae</b></sub></a></td>
    <td align="center"><a href="https://github.com/conprour"><img src="https://github.com/conprour.png?size=100" width="64px;"/><br /><sub><b>conprour</b></sub></a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/Br1an67"><img src="https://github.com/Br1an67.png?size=100" width="64px;"/><br /><sub><b>Br1an67</b></sub></a></td>
    <td align="center"><a href="https://github.com/NINE-J"><img src="https://github.com/NINE-J.png?size=100" width="64px;"/><br /><sub><b>NINE-J</b></sub></a></td>
    <td align="center"><a href="https://github.com/Yanghuabei-design"><img src="https://github.com/Yanghuabei-design.png?size=100" width="64px;"/><br /><sub><b>Yanghuabei</b></sub></a></td>
    <td align="center"><a href="https://github.com/nregret"><img src="https://github.com/nregret.png?size=100" width="64px;"/><br /><sub><b>nregret</b></sub></a></td>
    <td align="center"><a href="https://github.com/kartik-mem0"><img src="https://github.com/kartik-mem0.png?size=100" width="64px;"/><br /><sub><b>kartik-mem0</b></sub></a></td>
    <td align="center"><a href="https://github.com/Yanghuabei-design"><img src="https://github.com/Yanghuabei-design.png?size=100" width="64px;"/><br /><sub><b>Yanghuabei-design</b></sub></a></td>
    <td align="center"><a href="https://github.com/benjamin7007"><img src="https://github.com/benjamin7007.png?size=100" width="64px;"/><br /><sub><b>benjamin7007</b></sub></a></td>
    <td align="center"><a href="https://github.com/gouziman"><img src="https://github.com/gouziman.png?size=100" width="64px;"/><br /><sub><b>gouziman</b></sub></a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/hobostay"><img src="https://github.com/hobostay.png?size=100" width="64px;"/><br /><sub><b>hobostay</b></sub></a></td>
    <td align="center"><a href="https://github.com/token2everything"><img src="https://github.com/token2everything.png?size=100" width="64px;"/><br /><sub><b>token2everything</b></sub></a></td>
  </tr>
</table>

## 🙏 致谢

<a href="http://nlp.csai.tsinghua.edu.cn/"><img src="assets/thunlp.png" height=50pt></a>&nbsp;&nbsp;
<a href="https://modelbest.cn/"><img src="assets/modelbest.png" height=50pt></a>&nbsp;&nbsp;
<a href="https://github.com/OpenBMB/AgentVerse/"><img src="assets/agentverse.png" height=50pt></a>&nbsp;&nbsp;
<a href="https://github.com/OpenBMB/RepoAgent"><img src="assets/repoagent.png"  height=50pt></a>
<a href="https://app.commanddash.io/agent?github=https://github.com/OpenBMB/ChatDev"><img src="assets/CommandDash.png" height=50pt></a>
<a href="www.teachmaster.cn"><img src="assets/teachmaster.png" height=50pt></a>
<a href="https://github.com/OpenBMB/AppCopilot"><img src="assets/appcopilot.png" height=50pt></a>

## 🔍 引用格式

```
@article{chatdev,
    title = {ChatDev: Communicative Agents for Software Development},
    author = {Chen Qian and Wei Liu and Hongzhang Liu and Nuo Chen and Yufan Dang and Jiahao Li and Cheng Yang and Weize Chen and Yusheng Su and Xin Cong and Juyuan Xu and Dahai Li and Zhiyuan Liu and Maosong Sun},
    journal = {arXiv preprint arXiv:2307.07924},
    url = {https://arxiv.org/abs/2307.07924},
    year = {2023}
}

@article{colearning,
    title = {Experiential Co-Learning of Software-Developing Agents},
    author = {Chen Qian and Yufan Dang and Jiahao Li and Wei Liu and Zihao Xie and Yifei Wang and Weize Chen and Cheng Yang and Xin Cong and Xiaoyin Che and Zhiyuan Liu and Maosong Sun},
    journal = {arXiv preprint arXiv:2312.17025},
    url = {https://arxiv.org/abs/2312.17025},
    year = {2023}
}

@article{macnet,
    title={Scaling Large-Language-Model-based Multi-Agent Collaboration},
    author={Chen Qian and Zihao Xie and Yifei Wang and Wei Liu and Yufan Dang and Zhuoyun Du and Weize Chen and Cheng Yang and Zhiyuan Liu and Maosong Sun}
    journal={arXiv preprint arXiv:2406.07155},
    url = {https://arxiv.org/abs/2406.07155},
    year={2024}
}

@article{iagents,
    title={Autonomous Agents for Collaborative Task under Information Asymmetry},
    author={Wei Liu and Chenxi Wang and Yifei Wang and Zihao Xie and Rennai Qiu and Yufan Dnag and Zhuoyun Du and Weize Chen and Cheng Yang and Chen Qian},
    journal={arXiv preprint arXiv:2406.14928},
    url = {https://arxiv.org/abs/2406.14928},
    year={2024}
}

@article{puppeteer,
      title={Multi-Agent Collaboration via Evolving Orchestration}, 
      author={Yufan Dang and Chen Qian and Xueheng Luo and Jingru Fan and Zihao Xie and Ruijie Shi and Weize Chen and Cheng Yang and Xiaoyin Che and Ye Tian and Xuantang Xiong and Lei Han and Zhiyuan Liu and Maosong Sun},
      journal={arXiv preprint arXiv:2505.19591},
      url={https://arxiv.org/abs/2505.19591},
      year={2025}
}
```

## 📬 联系方式

如果你有任何问题、反馈或希望与我们取得联系，欢迎随时通过电子邮件 [qianc62@gmail.com](mailto:qianc62@gmail.com) 联系我们。