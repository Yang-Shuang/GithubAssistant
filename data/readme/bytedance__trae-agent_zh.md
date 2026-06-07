# Trae Agent

[![arXiv:2507.23370](https://img.shields.io/badge/TechReport-arXiv%3A2507.23370-b31a1b)](https://arxiv.org/abs/2507.23370)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Pre-commit](https://github.com/bytedance/trae-agent/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/bytedance/trae-agent/actions/workflows/pre-commit.yml)
[![Unit Tests](https://github.com/bytedance/trae-agent/actions/workflows/unit-test.yml/badge.svg)](https://github.com/bytedance/trae-agent/actions/workflows/unit-test.yml)
[![Discord](https://img.shields.io/discord/1320998163615846420?label=Join%20Discord&color=7289DA)](https://discord.gg/VwaQ4ZBHvC)

**Trae Agent** 是一款基于大语言模型（LLM）的通用软件工程任务智能体。它提供了强大的命令行界面（CLI），能够理解自然语言指令，并使用各类工具与 LLM 提供商执行复杂的软件工作流。

有关技术细节，请参阅[我们的技术报告](https://arxiv.org/abs/2507.23370)。

**项目状态：** 该项目仍在积极开发中。如果你愿意帮助我们改进 Trae Agent，请参阅 [docs/roadmap.md](docs/roadmap.md) 和 [CONTRIBUTING](CONTRIBUTING.md)。

**与其他 CLI 智能体的区别：** Trae Agent 提供了透明、模块化的架构，研究人员和开发者可以轻松地对其进行修改、扩展和分析，使其成为**研究 AI 智能体架构、进行消融实验以及开发新型智能体能力**的理想平台。这种**面向研究的友好设计**使学术界和开源社区能够贡献并基于该基础框架进行构建，从而在快速发展的 AI 智能体领域促进创新。

## ✨ 功能特性

- 🌊 **Lakeview**：为智能体步骤提供简短而精炼的摘要生成
- 🤖 **多 LLM 支持**：兼容 OpenAI、Anthropic、Doubao、Azure、OpenRouter、Ollama 及 Google Gemini API
- 🛠️ **丰富的工具生态**：文件编辑、Bash 执行、顺序推理（sequential thinking）等
- 🎯 **交互模式**：支持迭代开发的对话式界面
- 📊 **轨迹记录**：详细记录所有智能体操作，便于调试与分析
- ⚙️ **灵活配置**：基于 YAML 的配置体系，支持环境变量覆盖
- 🚀 **轻松安装**：通过 pip 即可快速完成安装

## 🚀 安装

### 环境要求
- UV (https://docs.astral.sh/uv/)
- 所选提供商的 API Key（OpenAI、Anthropic、Google Gemini、OpenRouter 等）

### 配置步骤

```bash
git clone https://github.com/bytedance/trae-agent.git
cd trae-agent
uv sync --all-extras
source .venv/bin/activate
```

## ⚙️ 配置

### YAML 配置（推荐）

1. 复制示例配置文件：
   ```bash
   cp trae_config.yaml.example trae_config.yaml
   ```

2. 使用你的 API 凭据和偏好设置编辑 `trae_config.yaml`：

```yaml
agents:
  trae_agent:
    enable_lakeview: true
    model: trae_agent_model  # the model configuration name for Trae Agent
    max_steps: 200  # max number of agent steps
    tools:  # tools used with Trae Agent
      - bash
      - str_replace_based_edit_tool
      - sequentialthinking
      - task_done

model_providers:  # model providers configuration
  anthropic:
    api_key: your_anthropic_api_key
    provider: anthropic
  openai:
    api_key: your_openai_api_key
    provider: openai

models:
  trae_agent_model:
    model_provider: anthropic
    model: claude-sonnet-4-20250514
    max_tokens: 4096
    temperature: 0.5
```

**注意：** `trae_config.yaml` 文件已被加入 `.gitignore` 以保护你的 API Key。

### 使用自定义 Base URL
在某些情况下，我们需要为 API 使用自定义地址。只需在 `provider` 后添加 `base_url` 字段即可，以下配置为例：

```
openai:
    api_key: your_openrouter_api_key
    provider: openai
    base_url: https://openrouter.ai/api/v1
```
**注意：** 字段格式仅使用空格。不允许使用制表符（\t）。

### 环境变量（备选方案）

你也可以通过环境变量配置 API Key，并将其存储在 `.env` 文件中：

```bash
export OPENAI_API_KEY="your-openai-api-key"
export OPENAI_BASE_URL="your-openai-base-url"
export ANTHROPIC_API_KEY="your-anthropic-api-key"
export ANTHROPIC_BASE_URL="your-anthropic-base-url"
export GOOGLE_API_KEY="your-google-api-key"
export GOOGLE_BASE_URL="your-google-base-url"
export OPENROUTER_API_KEY="your-openrouter-api-key"
export OPENROUTER_BASE_URL="https://openrouter.ai/api/v1"
export DOUBAO_API_KEY="your-doubao-api-key"
export DOUBAO_BASE_URL="https://ark.cn-beijing.volces.com/api/v3/"
```

### MCP 服务（可选）

要启用模型上下文协议（Model Context Protocol，简称 MCP）服务，请在配置中添加 `mcp_servers` 部分：

```yaml
mcp_servers:
  playwright:
    command: npx
    args:
      - "@playwright/mcp@0.0.27"
```

**配置优先级：** 命令行参数 > 配置文件 > 环境变量 > 默认值

**旧版 JSON 配置：** 如果使用较旧的 JSON 格式，请参阅 [docs/legacy_config.md](docs/legacy_config.md)。我们建议迁移至 YAML。

## 📖 使用方法

### 基础命令

```bash
# Simple task execution
trae-cli run "Create a hello world Python script"

# Check configuration
trae-cli show-config

# Interactive mode
trae-cli interactive
```

### 各提供商示例

```bash
# OpenAI
trae-cli run "Fix the bug in main.py" --provider openai --model gpt-4o

# Anthropic
trae-cli run "Add unit tests" --provider anthropic --model claude-sonnet-4-20250514

# Google Gemini
trae-cli run "Optimize this algorithm" --provider google --model gemini-2.5-flash

# OpenRouter (access to multiple providers)
trae-cli run "Review this code" --provider openrouter --model "anthropic/claude-3-5-sonnet"
trae-cli run "Generate documentation" --provider openrouter --model "openai/gpt-4o"

# Doubao
trae-cli run "Refactor the database module" --provider doubao --model doubao-seed-1.6

# Ollama (local models)
trae-cli run "Comment this code" --provider ollama --model qwen3
```

### 高级选项

```bash
# Custom working directory
trae-cli run "Add tests for utils module" --working-dir /path/to/project

# Save execution trajectory
trae-cli run "Debug authentication" --trajectory-file debug_session.json

# Force patch generation
trae-cli run "Update API endpoints" --must-patch

# Interactive mode with custom settings
trae-cli interactive --provider openai --model gpt-4o --max-steps 30
```

## Docker 模式命令
### 准备工作
**重要提示**：请确保你的环境中已正确配置 Docker。

### 使用方法
```bash
# Specify a Docker image to run the task in a new container
trae-cli run "Add tests for utils module" --docker-image python:3.11

# Specify a Docker image to run the task in a new container and mount the directory
trae-cli run "write a script to print helloworld" --docker-image python:3.12 --working-dir test_workdir/

# Attach to an existing Docker container by ID (`--working-dir` is invalid with `--docker-container-id`)
trae-cli run "Update API endpoints" --docker-container-id 91998a56056c

# Specify an absolute path to a Dockerfile to build an environment
trae-cli run "Debug authentication" --dockerfile-path test_workspace/Dockerfile

# Specify a path to a local Docker image file (tar archive) to load
trae-cli run "Fix the bug in main.py" --docker-image-file test_workspace/trae_agent_custom.tar

# Remove the Docker container after finishing the task (keep default)
trae-cli run "Add tests for utils module" --docker-image python:3.11 --docker-keep false
```

### 交互模式命令

在交互模式下，你可以使用以下指令：
- 输入任意任务描述即可执行它
- `status` - 显示智能体信息
- `help` - 显示可用命令
- `clear` - 清屏
- `exit` 或 `quit` - 结束会话

## 🛠️ 高级功能

### 可用工具

Trae Agent 提供了全面的软件工程任务工具箱，包括文件编辑、Bash 执行、结构化思考（structured thinking）和任务完成。有关所有可用工具及其功能的详细信息，请参阅 [docs/tools.md](docs/tools.md)。

### 轨迹记录

Trae Agent 会自动记录详细的执行轨迹，便于调试与分析：

```bash
# Auto-generated trajectory file
trae-cli run "Debug the authentication module"
# Saves to: trajectories/trajectory_YYYYMMDD_HHMMSS.json

# Custom trajectory file
trae-cli run "Optimize database queries" --trajectory-file optimization_debug.json
```

轨迹文件包含大语言模型交互记录、智能体步骤、工具使用情况以及执行元数据。更多详情请参阅 [docs/TRAJECTORY_RECORDING.md](docs/TRAJECTORY_RECORDING.md)。

## 🔧 开发指南

### 贡献代码

关于贡献指南，请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。

### 常见问题排查

**导入错误：**
```bash
PYTHONPATH=. trae-cli run "your task"
```

**API Key 问题：**
```bash
# Verify API keys
echo $OPENAI_API_KEY
trae-cli show-config
```

**命令未找到：**
```bash
uv run trae-cli run "your task"
```

**权限错误：**
```bash
chmod +x /path/to/your/project
```

## 📄 许可证

本项目采用 MIT 许可证开源，详情请参阅 [LICENSE](LICENSE) 文件。

## ✍️ 引用

```bibtex
@article{traeresearchteam2025traeagent,
      title={Trae Agent: An LLM-based Agent for Software Engineering with Test-time Scaling},
      author={Trae Research Team and Pengfei Gao and Zhao Tian and Xiangxin Meng and Xinchen Wang and Ruida Hu and Yuanan Xiao and Yizhou Liu and Zhao Zhang and Junjie Chen and Cuiyun Gao and Yun Lin and Yingfei Xiong and Chao Peng and Xia Liu},
      year={2025},
      eprint={2507.23370},
      archivePrefix={arXiv},
      primaryClass={cs.SE},
      url={https://arxiv.org/abs/2507.23370},
}
```

## 🙏 致谢

感谢 Anthropic 开发了 [anthropic-quickstart](https://github.com/anthropics/anthropic-quickstarts) 项目，该项目的工具生态为我们提供了宝贵的参考。