# CodeWhale

> 基于 DeepSeek V4 的终端编程智能体。通过 `codewale` 命令运行，流式输出推理块（reasoning blocks），在审批门控下编辑本地工作区，并包含一种自动模式，可为每一轮交互自动选择模型与思维层级。

[简体中文 README](README.zh-CN.md)
[日本語 README](README.ja-JP.md)
[Tiếng Việt README](README.vi.md)


## Install

`codewhale` 作为一对独立的 Rust 发布二进制文件安装：调度命令 `codewhale` 和用于交互式会话的配套运行时 `codewhale-tui`。npm 和 Docker 会自动为你安装这两个组件；使用 Cargo 或手动安装时，必须将两个二进制文件放在同一目录（通常是 `PATH` 环境变量包含的路径）。该 npm 包仅为这些发布二进制文件的安装器/包装器；智能体并不运行在 Node.js 上。

```bash
# 1. npm — 如果你已使用 Node，这是最简单的方案。该包会从 GitHub Releases 下载匹配的预构建 Rust 二进制文件。
npm install -g codewhale

# 2. Cargo — 无需 Node。需要 Rust 1.88+（crates 使用了 2024 edition；旧版工具链会报错 "feature `edition2024` is required"）。请先运行 `rustup update`，或使用下方的非 Cargo 安装路径。
cargo install codewhale-cli --locked   # `codewhale`（入口点）
cargo install codewhale-tui     --locked   # `codewhale-tui`（TUI 二进制文件）

# 3. Homebrew — 仅保留用于遗留兼容。
#    tap/formula 仍使用旧的 deepseek-tui 名称。新安装请优先选择 npm、Cargo、Docker 或直接下载，直到 formula 完成重命名。
brew tap Hmbown/deepseek-tui
brew install deepseek-tui

# 4. Direct download — GitHub Releases 平台归档文件。
#    https://github.com/Hmbown/CodeWhale/releases
#    归档包包含 codewhale 和 codewhale-tui 及安装脚本。
#    独立二进制文件也附带提供；请保持两个文件在一起。

# 5. Docker — 预构建发布镜像。
docker volume create codewhale-home
docker run --rm -it \
  -e DEEPSEEK_API_KEY="$DEEPSEEK_API_KEY" \
  -v codewhale-home:/home/codewhale/.codewhale \
  -v "$PWD:/workspace" \
  -w /workspace \
  ghcr.io/hmbown/codewhale:latest
```

> 在中国大陆地区，可通过 `--registry=https://registry.npmmirror.com` 加速 npm 安装路径，或使用下方的 [Cargo 镜像](#china--mirror-friendly-installation)。
>
> **下载安全提示**：官方发布二进制文件托管于 `https://github.com/Hmbown/CodeWhale/releases`。手动下载时，请验证 SHA-256 校验和清单，避免使用名称相似的仓库或搜索结果中的镜像站。详见 [下载安全与校验和](docs/INSTALL.md#2-download-safety-and-checksums)。

已安装？请使用与你的安装路径匹配的更新器：

```bash
codewhale update                         # 发布二进制文件更新器
npm install -g codewhale@latest      # npm 包装器
brew update && brew upgrade deepseek-tui  # 仅适用于遗留 Homebrew 安装
cargo install codewhale-cli --locked --force
cargo install codewhale-tui     --locked --force
```

> `codewhale update` 现已支持 `--proxy` 参数，可通过代理进行更新。例如：`codewhale update --proxy https://localhost:7897`

[![CI](https://github.com/Hmbown/CodeWhale/actions/workflows/ci.yml/badge.svg)](https://github.com/Hmbown/CodeWhale/actions/workflows/ci.yml)
[![npm](https://img.shields.io/npm/v/codewhale)](https://www.npmjs.com/package/codewhale)
[![crates.io](https://img.shields.io/crates/v/codewhale-cli?label=crates.io)](https://crates.io/crates/codewhale-cli)
[DeepWiki project index](https://deepwiki.com/Hmbown/CodeWhale)

![codewhale screenshot](assets/screenshot.png)

---

## What Is It?

模型回答一个问题，智能体完成一项任务。区别在于**控制框架（harness）**——一套规则、证据与反馈系统，用于确保模型始终聚焦而不偏离目标。

CodeWhale 正是这套框架，围绕 DeepSeek V4 构建，并遵循以下三大理念：

| 理念 | 运作方式 |
|---|---|
| **始于信任** | 每一轮交互均以“A”（可能性）开始——先探索可能，再追求确定；重打磨工艺，而非图方便。 |
| **权责清晰** | 拥有成文宪法及九级权限体系。用户当前意图优先于过时指令，验证结果优先于模型自信。 |
| **递归优化** | V4 参与了框架的编写。随着框架不断完善，V4 的表现愈发高效——并进一步协助优化框架。每一轮交互都在更强的基础上开始。 |

它开源、原生支持终端，并以配套的 `codewhale` / `codewhale-tui` Rust 二进制对形式打包。

## How the Harness Works

智能体模型需大规模处理冲突信息：用户意图、项目规则、系统默认值、工具输出和过期记忆在同一轮中争夺权威性。作为裁判的 LLM 需要明确的管辖权——当来源发生分歧时，以哪个为准？

CodeWhale 通过**宪法**（`prompts/base.md`）解决此问题。它是一份正式的法律层级文件——第七条将九个权限等级从宪法自身条款排列至上一轮会话交接记录。用户当前消息优先于过时项目指令，实时工具输出优先于主观假设，验证结果优先于模型自信。每一轮交互中，模型都会继承清晰的权威链条，无需猜测应遵循哪条指令。

前六条定义了模型的身份、职责与代理权限（第七条为层级结构本身）：验证强制要求（第五条——每项操作必须留下证据，绝不凭直觉宣告成功）、协作传承（第六条——为下一轮智能体保持更整洁的工作区与真实的交接记录），以及真理优先条款（第二条——不可协商；即使用户请求也不能覆盖对真相的坚守）。

DeepSeek V4 的前缀缓存（prefix caching）使这一机制得以落地。宪法内容冗长详细，但一旦缓存命中，每轮成本仅为冷启动读取的约百分之一。模型会递归引用该文件——通过 RLM 会话进行探查、扫描与查询——按需回顾信息，而非依赖单次死记硬背。其表现更像开卷考试而非闭卷。

由于权威结构明确，失败不会被掩盖。非零退出码、轮次间传来的 rust-analyzer 类型错误、沙箱拒绝访问——这些都会作为修正向量反馈给模型。模型利用自身的偏差进行自我纠正。

三种模式控制操作空间。Plan（规划）为只读模式；Agent（智能体）将破坏性操作置于审批门控后；YOLO 在可信工作区中自动批准所有操作。macOS Seatbelt 为当前活跃沙箱；Linux Landlock 已检测但尚未强制执行；Windows 沙箱功能暂未公开。

Fin（关闭思维链的廉价 Flash 调用）负责每轮的模型自动路由。默认使用 `--model auto`。

每一轮都会在你的仓库 `.git` 之外记录一个侧边 Git（side-git）快照。通过 `/restore` 和 `revert_turn` 可回滚工作区。

子智能体并发运行（上限 20）。`agent_open` 立即返回；结果以完成哨兵形式内联到达，并附带摘要。完整记录通过有界句柄保留在 `agent_eval` 之后。详见 [docs/SUBAGENTS.md](docs/SUBAGENTS.md)。

其余功能界面包括：每次编辑后的 LSP 诊断（rust-analyzer、pyright、typescript-language-server、gopls、clangd、jdtls、vue-language-server）、用于批量分析的 RLM 会话、MCP 协议、HTTP/SSE 运行时 API、持久化任务队列、Zed 的 ACP 适配器、SWE-bench 导出，以及带缓存命中/未命中明细的实时成本追踪。

---

## The Harness

`codewhale`（调度 CLI）→ `codewhale-tui`（配套二进制文件）→ ratatui 界面 ↔ 异步引擎 ↔ OpenAI 兼容流式客户端。工具调用通过类型化注册表路由（shell、文件操作、git、网页、子智能体、MCP、RLM），结果流回转录记录。引擎管理会话状态、轮次追踪、持久化任务队列，以及一个 LSP 子系统——该子系统会在下一轮推理步骤前将编辑后诊断信息注入模型上下文。

完整架构详解见 [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)。

### Sub-agents: Concurrent Background Execution

CodeWhale 可分发多个并行运行的子智能体——如同一个并发任务队列：

- **非阻塞启动**。`agent_open` 立即返回。子进程获得全新的上下文与工具注册表并独立运行，父进程继续工作。
- **后台执行**。子智能体并发执行（默认上限 10，可配置为 20）。引擎管理连接池——无需轮询循环。
- **完成通知**。子智能体完成后，运行时会向父进程转录记录中注入 `<codewhale:subagent.done>` 哨兵。人类可读的摘要（包含子进程的发现、变更文件及任何风险）位于哨兵所在行的上一行。父模型读取该摘要并整合结果，无需额外调用工具。
- **有界结果检索**。完整的子进程转录记录通过 `transcript_handle` 保留，可通过 `agent_eval` 访问。当摘要信息不足时，父进程调用 `handle_read` 获取切片、行范围或 JSONPath 投影——在保持父上下文精简的同时不丢失细节。

子智能体完整参考见 [docs/SUBAGENTS.md](docs/SUBAGENTS.md)。

---

## Quickstart

```bash
npm install -g codewhale
codewhale --version
codewhale --model auto
```

预编译二进制对及平台归档文件已发布，支持 **Linux x64**、**Linux ARM64**（v0.8.8+）、**macOS x64**、**macOS ARM64** 和 **Windows x64**。其他目标架构（musl、riscv64、FreeBSD 等）请参阅 [从源码安装](#install-from-source) 或 [docs/INSTALL.md](docs/INSTALL.md)。

首次启动时，系统将提示你输入 [DeepSeek API 密钥](https://platform.deepseek.com/api_keys)。密钥将保存至 `~/.codewhale/config.toml`（兼容旧版 `~/.deepseek/config.toml`），因此可在任意目录下使用而无需系统凭据弹窗。

你也可以提前设置：

```bash
codewhale auth set --provider deepseek   # 保存至 ~/.codewhale/config.toml
codewhale auth status                    # 显示当前凭证来源

export DEEPSEEK_API_KEY="YOUR_KEY"      # 环境变量替代方案；非交互式 shell 请使用 ~/.zshenv
codewhale

codewhale doctor                         # 验证设置
```

如果 `codewhale doctor` 提示被拒绝的密钥来自 `DEEPSEEK_API_KEY`，请从 shell 启动文件中移除该过期导出，重新打开终端，或运行 `codewhale auth set --provider deepseek`。使用 `codewhale auth status` 可查看配置、系统钥匙串和环境变量来源状态，且不会打印密钥明文。保存的配置密钥优先级高于钥匙串和环境变量，也更便于轮换。

> 若要轮换或移除已保存的密钥：`codewhale auth clear --provider deepseek`。

### Tencent Cloud / CNB Remote-First Path

如需一个可随时从手机控制的常驻工作区，可使用腾讯原生方案：CNB 镜像/源码、腾讯云香港轻量应用服务器、飞书/Lark 长连接桥接，以及可选的 EdgeOne 作为显式公共 HTTPS 边缘节点。运行时 API 绑定于 localhost；EdgeOne 不用于暴露 `/v1/*`。

请先阅读 [docs/TENCENT_CLOUD_REMOTE_FIRST.md](docs/TENCENT_CLOUD_REMOTE_FIRST.md)，随后使用 [docs/TENCENT_LIGHTHOUSE_HK.md](docs/TENCENT_LIGHTHOUSE_HK.md) 进行服务器运维。

### Auto Mode

当你希望 `codewhale` 决定每一轮需要多少模型算力与推理能力时，使用 `codewhale --model auto` 或 `/model auto`。

自动模式同时控制两项设置：
- **模型**：`deepseek-v4-flash` 或 `deepseek-v4-pro`
- **思维层级**：`off`（关闭）、`high`（高）或 `max`（最大）

在实际请求发送前，应用会先发起一次关闭思维链的轻量 `deepseek-v4-flash` 路由调用。该路由器会检查最新请求与近期上下文，随后为实际请求选择具体的模型和思维层级。简短/简单的任务可保持在 Flash 并关闭思维；编程、调试、发布工作、架构设计、安全审查或模糊的多步任务则可升级至 Pro 及更高思维层级。

`auto` 为 `codewhale` 本地设置。上游 API 永远不会收到 `model: "auto"`；它仅接收为该轮实际选定的模型与思维配置。TUI 会显示所选路由，成本追踪按实际运行的模型计费。若路由器调用失败或返回无效答案，应用将回退至本地启发式策略。除非你为子智能体指定了明确模型，否则它们默认继承自动模式。

若需可重复的基准测试、严格的成本上限或特定的提供商/模型映射，请使用固定模型或固定思维层级。

### Linux ARM64 (Raspberry Pi, Asahi, Graviton, HarmonyOS PC)

自 v0.8.8 起，`npm i -g codewhale` 可在基于 glibc 的 ARM64 Linux 上运行。你也可以从 [Releases 页面](https://github.com/Hmbown/CodeWhale/releases) 下载预编译二进制文件，并将其并排放置于你的 `PATH` 中。

### China / Mirror-friendly Installation

若在中国大陆地区 GitHub 或 npm 下载缓慢，可使用 Cargo 注册表镜像：

```toml
# ~/.cargo/config.toml
[source.crates-io]
replace-with = "tuna"

[source.tuna]
registry = "sparse+https://mirrors.tuna.tsinghua.edu.cn/crates.io-index/"
```

随后安装两个二进制文件（调度器在运行时委托给 TUI）：

```bash
cargo install codewhale-cli --locked   # 提供 `codewhale`
cargo install codewhale-tui     --locked   # 提供 `codewhale-tui`
codewhale --version
```

预编译二进制文件也可从 [GitHub Releases](https://github.com/Hmbown/CodeWhale/releases) 下载。使用环境变量 `DEEPSEEK_TUI_RELEASE_BASE_URL` 指定镜像发布资产地址。

### Windows (Scoop)

[Scoop](https://scoop.sh) 是一款 Windows 包管理器。`codewhale` 软件包已收录于 Scoop 主存储库，但其清单更新独立进行，可能滞后于 GitHub/npm/Cargo 的发布。请先运行 `scoop update`，随后通过 `codewhale --version` 验证已安装版本：

```bash
scoop update
scoop install codewhale
codewhale --version
```

若需在 Scoop 清单更新前获取最新版本，请使用 npm 或直接下载 GitHub Release。


<details id="install-from-source">
<summary>从源码安装</summary>

支持任意 Tier-1 Rust 目标架构——包括 musl、riscv64、FreeBSD 及较旧的 ARM64 发行版。

```bash
# Linux build deps (Debian/Ubuntu/RHEL):
#   sudo apt-get install -y build-essential pkg-config libdbus-1-dev
#   sudo dnf install -y gcc make pkgconf-pkg-config dbus-devel

git clone https://github.com/Hmbown/CodeWhale.git
cd CodeWhale

cargo install --path crates/cli --locked   # 需要 Rust 1.88+；提供 `codewhale`
cargo install --path crates/tui --locked   # 提供 `codewhale-tui`
```

必须同时安装两个二进制文件。交叉编译与平台特定说明：[docs/INSTALL.md](docs/INSTALL.md)。

</details>

### Other API Providers

完整内置提供商注册表（含模型 ID、认证变量、基础 URL 及能力边界）详见 [docs/PROVIDERS.md](docs/PROVIDERS.md)。

```bash
# NVIDIA NIM
codewhale auth set --provider nvidia-nim --api-key "YOUR_NVIDIA_API_KEY"
codewhale --provider nvidia-nim

# AtlasCloud
codewhale auth set --provider atlascloud --api-key "YOUR_ATLASCLOUD_API_KEY"
codewhale --provider atlascloud
codewhale --provider atlascloud --model vendor/model-id

# Wanjie Ark
codewhale auth set --provider wanjie-ark --api-key "YOUR_WANJIE_API_KEY"
codewhale --provider wanjie-ark --model deepseek-reasoner

# OpenRouter
codewhale auth set --provider openrouter --api-key "YOUR_OPENROUTER_API_KEY"
codewhale --provider openrouter --model deepseek/deepseek-v4-pro
codewhale --provider openrouter --model arcee-ai/trinity-large-thinking
codewhale --provider openrouter --model minimax/minimax-m3

Arcee AI 提供对其强大的 Trinity 模型的直接 API 访问，包括具备推理能力的 Trinity-Large Thinking。本节提供全面的设置说明与模型对比。

## Configuration

### API Key
主要认证方式为 `ARCEE_API_KEY` 环境变量或 `~/.codewhale/config.toml` 中的 `[providers.arcee]` 配置节：

```toml
[providers.arcee]
# api_key = "your-arcee-api-key"
# base_url = "https://api.arcee.ai/api/v1"
# model = "trinity-large-thinking"  # or "trinity-large-preview", "trinity-mini"
```

### Environment Variables

- `ARCEE_API_KEY`: Your Arcee API key (required) -> `- **`ARCEE_API_KEY``**: Arcee API 密钥（必填）`
- `ARCEE_BASE_URL`: Custom base URL (optional, defaults to `https://api.arcee.ai/api/v1`) -> `- **`ARCEE_BASE_URL``**: 自定义基础 URL（可选，默认为 `https://api.arcee.ai/api/v1`）`
- `ARCEE_MODEL`: Default model to use (optional, defaults to `trinity-large-thinking`) -> `- **`ARCEE_MODEL``**: 默认使用模型（可选，默认为 `trinity-large-thinking`）`

### Model Support

CodeWhale supports three Arcee models:
-> ### 模型支持
CodeWhale 支持三款 Arcee 模型：

| Model | Reasoning | Context Window | Max Output | Best For |
|--------|-----------|----------------|------------|----------|
| `trinity-large-thinking` | ✅ Yes | 262,144 tokens | 262,144 tokens | Complex reasoning, coding, math | -> | **`trinity-large-thinking`** | ✅ 支持 | 262,144 tokens | 262,144 tokens | 复杂推理、编程、数学 |
| `trinity-large-preview` | ❌ No | 262,144 tokens | 4,096 tokens | High-accuracy non-reasoning tasks | -> | **`trinity-large-preview`** | ❌ 不支持 | 262,144 tokens | 4,096 tokens | 高精度非推理任务 |
| `trinity-mini` | ❌ No | 128,000 tokens | 4,096 tokens | Faster, cost-effective tasks | -> | **`trinity-mini`** | ❌ 不支持 | 128,000 tokens | 4,096 tokens | 快速、高性价比任务 |

**Note:** The `trinity-large-thinking` model supports reasoning (thinking mode) and can handle very large contexts, making it ideal for complex programming tasks. The other models do not support reasoning but offer larger context windows than many other providers.
-> **注意**：`trinity-large-thinking` 模型支持推理（思维模式），可处理超大上下文，非常适合复杂的编程任务。其他模型不支持推理，但提供比许多其他提供商更大的上下文窗口。
codewhale auth set --provider arcee --api-key "YOUR_ARCEE_API_KEY"
codewhale --provider arcee --model trinity-large-thinking
codewhale --provider arcee --model trinity-large-preview

# Xiaomi MiMo
codewhale auth set --provider xiaomi-mimo --api-key "YOUR_XIAOMI_KEY"
codewhale --provider xiaomi-mimo --model mimo-v2.5-pro
codewhale --provider xiaomi-mimo --model mimo-v2.5
codewhale --provider xiaomi-mimo speech "Hello from MiMo" --model tts -o hello.wav

# Novita
codewhale auth set --provider novita --api-key "YOUR_NOVITA_API_KEY"
codewhale --provider novita --model deepseek/deepseek-v4-pro

# Fireworks
codewhale auth set --provider fireworks --api-key "YOUR_FIREWORKS_API_KEY"
codewhale --provider fireworks --model deepseek-v4-pro

# SiliconFlow
codewhale auth set --provider siliconflow --api-key "YOUR_SILICONFLOW_API_KEY"
codewhale --provider siliconflow --model deepseek-ai/DeepSeek-V4-Pro

# Generic OpenAI-compatible endpoint
codewhale auth set --provider openai --api-key "YOUR_OPENAI_COMPATIBLE_API_KEY"
OPENAI_BASE_URL="https://openai-compatible.example/v4" codewhale --provider openai --model glm-5

# Custom DeepSeek-compatible endpoint
DEEPSEEK_BASE_URL="https://your-provider.example/v1" \
  DEEPSEEK_MODEL="deepseek-ai/DeepSeek-V4-Pro" \
  codewhale --provider deepseek

# Self-hosted SGLang
SGLANG_BASE_URL="http://localhost:30000/v1" codewhale --provider sglang --model deepseek-v4-flash

# Self-hosted vLLM
VLLM_BASE_URL="http://localhost:8000/v1" codewhale --provider vllm --model deepseek-v4-flash
# Trusted LAN vLLM over HTTP
DEEPSEEK_ALLOW_INSECURE_HTTP=1 VLLM_BASE_URL="http://192.168.0.110:8000/v1" codewhale --provider vllm --model deepseek-v4-flash

# Self-hosted Ollama
ollama pull codewhale-coder:1.3b
codewhale --provider ollama --model codewhale-coder:1.3b
```

在 TUI 内，输入 `/provider` 打开提供商选择器，输入 `/model` 打开本地模型/思维选择器。`/provider openrouter` 和 `/model <id>` 可直接切换；当活动提供商支持模型列表时，`/models` 会显式获取并列出实时 API 模型。

---

## Release Notes

特定版本的变更详见 [CHANGELOG.md](CHANGELOG.md)。本 README 聚焦于当前安装路径、核心工作流、提供商配置、运行时接口及扩展点。

---

## Usage

```bash
codewhale                                         # interactive TUI -> `codewhale`（交互式 TUI）
codewhale "explain this function"                 # one-shot prompt -> 一次性提示词
codewhale exec --auto --output-format stream-json "fix this bug"  # NDJSON backend stream -> NDJSON 后端流式输出
codewhale exec --resume <SESSION_ID> "follow up"  # continue a non-interactive session -> 继续非交互式会话
codewhale --model deepseek-v4-flash "summarize"   # model override -> 模型覆盖
codewhale --model auto "fix this bug"             # auto-select model + thinking -> 自动选择模型与思维层级
codewhale --yolo                                  # auto-approve tools -> 自动批准工具调用
codewhale auth set --provider deepseek            # save API key -> 保存 API 密钥
codewhale doctor                                  # check setup & connectivity -> 检查设置与连通性
codewhale doctor --json                           # machine-readable diagnostics -> 机器可读诊断信息
codewhale setup --status                          # read-only setup status -> 只读安装状态
codewhale setup --tools --plugins                 # scaffold tool/plugin dirs -> 生成工具/插件目录脚手架
codewhale models                                  # list live API models -> 列出实时 API 模型
codewhale sessions                                # list saved sessions with timestamps -> 列出带时间戳的已保存会话
codewhale resume --last                           # resume the most recent session in this workspace -> 恢复当前工作区最新会话
codewhale resume <SESSION_ID>                     # resume a specific session by UUID -> 按 UUID 恢复指定会话
codewhale fork <SESSION_ID>                       # fork a saved session into a sibling path -> 将已保存会话分叉为同级路径
codewhale serve --http                            # HTTP/SSE API server -> HTTP/SSE API 服务器
codewhale serve --mobile                          # LAN mobile control page; token-gated by default -> LAN 移动端控制页；默认受令牌保护
codewhale serve --acp                             # ACP stdio adapter for Zed/custom agents -> Zed/自定义代理的 ACP stdio 适配器
codewhale run pr <N>                              # fetch PR and pre-seed review prompt -> 获取 PR 并预置审查提示词
codewhale mcp list                                # list configured MCP servers -> 列出已配置的 MCP 服务器
codewhale mcp validate                            # validate MCP config/connectivity -> 验证 MCP 配置/连通性
codewhale mcp-server                              # run dispatcher MCP stdio server -> 运行调度器 MCP stdio 服务器
codewhale update                                  # check for and apply binary updates -> 检查并应用二进制更新
```

在交互式 TUI 编辑器中，以 `!` 开头可运行 Shell 命令（经过标准审批、沙箱与输出流程），例如 `! cargo test -p codewhale-tui sidebar`。

### Branching Conversations

保存的会话支持有意设计的分支功能。`codewhale fork <SESSION_ID>` 将现有已保存会话复制为新的同级会话，在元数据中记录父会话 ID，并打开该分支以便你探索替代方向而不污染原始路径。会话选择器与 `codewhale sessions` 会用父 ID 标记已分叉的会话。

`codewhale sessions` 列出跨工作区的已保存会话，并包含最后更新时间戳。`codewhale resume --last` 和 `codewhale --continue` 为当前工作区选择最新会话；从其他目录恢复工作时请传入显式会话 ID。

在 TUI 中，连续按两次 Esc（Esc-Esc）可回退当前转录记录至之前的用户提示词，并将其放回编辑器供修改。`/restore` 和 `revert_turn` 是独立的工作区回滚工具：它们从侧边 Git 快照恢复文件，但不重写对话历史。

发布构建的 Docker 镜像已推送至 GHCR：

```bash
docker volume create codewhale-home

docker run --rm -it \
  -e DEEPSEEK_API_KEY="$DEEPSEEK_API_KEY" \
  -v codewhale-home:/home/codewhale/.codewhale \
  -v "$PWD:/workspace" \
  -w /workspace \
  ghcr.io/hmbown/codewhale:latest
```

固定标签、本地镜像构建、卷所有权说明及非交互式流水线用法详见 [docs/DOCKER.md](docs/DOCKER.md)。

### Zed / ACP

DeepSeek 可作为自定义智能体客户端协议（Agent Client Protocol）服务器运行，供通过标准 I/O 启动本地 ACP 代理的编辑器使用。在 Zed 中，添加自定义代理服务器：

```json
{
  "agent_servers": {
    "DeepSeek": {
      "type": "custom",
      "command": "codewhale",
      "args": ["serve", "--acp"],
      "env": {}
    }
  }
}
```

首个 ACP 切片支持通过你现有的 DeepSeek 配置/API 密钥创建新会话和响应提示词。目前尚未通过 ACP 暴露工具支持的编辑与检查点回放功能。

社区维护的适配器：[acp-codewhale-adapter](https://github.com/rockeverm3m/acp-codewhale-adapter) 为需要在内置 Zed 切片之外使用工具支持型 ACP 工作流的用户，将 `codewhale exec --auto` 桥接至 `cc-connect`。

### Keyboard Shortcuts

| Key | Action |
|---|---|
| `Tab` | Complete `/` or `@` entries; while running, queue draft as follow-up; otherwise cycle mode -> **`Tab`**：补全 `/` 或 `@` 条目；运行中作为后续提示排队；否则切换模式 |
| `Shift+Tab` | Cycle reasoning-effort: off → high → max -> **`Shift+Tab`**：循环推理强度：关闭 → 高 → 最大 |
| `F1` | Searchable help overlay -> **`F1`**：可搜索的帮助覆盖层 |
| `Esc` | Back / dismiss -> **`Esc`**：返回 / 关闭 |
| `Ctrl+K` | Command palette -> **`Ctrl+K`**：命令面板 |
| `Ctrl+R` | Resume an earlier session -> **`Ctrl+R`**：恢复早期会话 |
| `Alt+R` | Search prompt history and recover cleared drafts -> **`Alt+R`**：搜索提示词历史并恢复已清除的草稿 |
| `Ctrl+S` | Stash current draft (`/stash list`, `/stash pop` to recover) -> **`Ctrl+S`**：暂存当前草稿（使用 `/stash list`、`/stash pop` 恢复） |
| `@path` | Attach file/directory context in composer -> **`@路径`**：在编辑器中附加文件/目录上下文 |
| `↑` (at composer start) | Select attachment row for removal -> **`↑`**（位于编辑器起始处）：选择附件行以便移除 |

完整快捷键目录：[docs/KEYBINDINGS.md](docs/KEYBINDINGS.md)。

---

## Modes

| Mode | Behavior |
| --- | --- |
| **Plan** 🔍 | Read-only investigation — model explores and proposes a plan before making changes; multi-step investigations use `checklist_write` -> **规划（Plan）** 🔍：只读调查——模型在修改前探索并提出方案；多步调查使用 `checklist_write` |
| **Agent** 🤖 | Default interactive mode — multi-step tool use with approval gates; substantial work is tracked with `checklist_write` -> **智能体（Agent）** 🤖：默认交互模式——带审批门控的多步工具调用；重要工作通过 `checklist_write` 追踪 |
| **YOLO** ⚡ | Auto-approve all tools in a trusted workspace; multi-step work still keeps a visible checklist -> **YOLO** ⚡：在可信工作区中自动批准所有工具；多步工作仍保留可见清单 |

---

## Configuration

用户配置：`~/.codewhale/config.toml`（兼容旧版 `~/.deepseek/config.toml`）。项目覆盖配置：`<workspace>/.codewhale/config.toml`（兼容旧版 `<workspace>/.deepseek/config.toml`）（禁止设置：`api_key`、`base_url`、`provider`、`mcp_config_path`）。所有选项详见 [config.example.toml](config.example.toml)。

可通过 `/statusline` 或配置中的 `[tui].status_items` 裁剪 TUI 底部状态栏。当前底部自定义选项内置于 `mode`、`model`、`status`、`git_branch`、`tokens` 和 `cache` 等芯片中；芯片顺序由 `config.toml` 中 `status_items` 的键顺序控制。交互式选择器会写入标准顺序。多行布局、自定义颜色及外部命令小部件不属于当前状态栏功能。

自定义 DeepSeek 兼容端点通常无需新建提供商。保持 `provider = "deepseek"` 并设置 `[providers.deepseek].base_url` / `model`，或使用 `provider = "openai"` 对接通用 OpenAI 兼容网关。请将 `provider`、`api_key` 和 `base_url` 放在用户配置或环境变量中；项目覆盖配置无法设置这些字段。

关键环境变量：

| Variable | Purpose |
|---|---|
| `DEEPSEEK_API_KEY` | API key -> **API 密钥** |
| `DEEPSEEK_BASE_URL` | API base URL -> **API 基础 URL** |
| `DEEPSEEK_HTTP_HEADERS` | Optional custom model request headers, e.g. `X-Model-Provider-Id=your-model-provider` -> **可选自定义模型请求头**，例如 `X-Model-Provider-Id=your-model-provider` |
| `DEEPSEEK_MODEL` | Default model -> **默认模型** |
| `DEEPSEEK_STREAM_IDLE_TIMEOUT_SECS` | Stream idle timeout in seconds, default `300`, clamped to `1..=3600` -> **流式空闲超时时间（秒）**，默认 `300`，限制在 `1..=3600` 范围内 |
| `CODEWHALE_PROVIDER` / `DEEPSEEK_PROVIDER` | `deepseek` (default), `nvidia-nim`, `openai`, `atlascloud`, `wanjie-ark`, `volcengine`, `openrouter`, `xiaomi-mimo`, `novita`, `fireworks`, `siliconflow`, `arcee`, `moonshot`, `sglang`, `vllm`, `ollama` -> **提供商标识**（默认 `deepseek`，支持 `nvidia-nim`, `openai`, `atlascloud`, `wanjie-ark`, `volcengine`, `openrouter`, `xiaomi-mimo`, `novita`, `fireworks`, `siliconflow`, `arcee`, `moonshot`, `sglang`, `vllm`, `ollama`） |
| `DEEPSEEK_PROFILE` | Config profile name -> **配置配置文件名称** |
| `DEEPSEEK_MEMORY` | Set to `on` to enable user memory -> 设为 `on` 以启用用户记忆功能 |
| `DEEPSEEK_ALLOW_INSECURE_HTTP=1` | Allow non-local `http://` API base URLs on trusted networks -> 在可信网络中允许非本地 `http://` API 基础 URL |
| `NVIDIA_API_KEY` / `OPENAI_API_KEY` / `ATLASCLOUD_API_KEY` / `WANJIE_ARK_API_KEY` / `VOLCENGINE_API_KEY` / `OPENROUTER_API_KEY` / `XIAOMI_MIMO_API_KEY` / `XIAOMI_API_KEY` / `MIMO_API_KEY` / `NOVITA_API_KEY` / `FIREWORKS_API_KEY` / `SILICONFLOW_API_KEY` / `ARCEE_API_KEY` / `MOONSHOT_API_KEY` / `KIMI_API_KEY` / `SGLANG_API_KEY` / `VLLM_API_KEY` / `OLLAMA_API_KEY` | Provider auth -> **各类密钥变量**（如 `NVIDIA_API_KEY`, `OPENAI_API_KEY` 等）：提供商认证凭据 |
| `OPENAI_BASE_URL` / `OPENAI_MODEL` | Generic OpenAI-compatible endpoint and model ID -> **通用 OpenAI 兼容端点与模型 ID** |
| `ATLASCLOUD_BASE_URL` / `ATLASCLOUD_MODEL` | AtlasCloud endpoint and model override -> **AtlasCloud 端点与模型覆盖** |
| `WANJIE_ARK_BASE_URL` / `WANJIE_ARK_MODEL` | Wanjie Ark endpoint and model override -> **Wanjie Ark 端点与模型覆盖** |
| `OPENROUTER_BASE_URL` | OpenRouter endpoint override -> **OpenRouter 端点覆盖** |
| `XIAOMI_MIMO_BASE_URL` / `MIMO_BASE_URL` / `XIAOMI_MIMO_MODEL` / `MIMO_MODEL` | Xiaomi MiMo endpoint and model override -> **Xiaomi MiMo 端点与模型覆盖** |
| `NOVITA_BASE_URL` | Novita endpoint override -> **Novita 端点覆盖** |
| `FIREWORKS_BASE_URL` | Fireworks endpoint override -> **Fireworks 端点覆盖** |
| `SILICONFLOW_BASE_URL` / `SILICONFLOW_MODEL` | SiliconFlow endpoint and model override -> **SiliconFlow 端点与模型覆盖** |
| `ARCEE_BASE_URL` / `ARCEE_MODEL` | Arcee AI endpoint and model override -> **Arcee AI 端点与模型覆盖** |
| `SGLANG_BASE_URL` | Self-hosted SGLang endpoint -> **自托管 SGLang 端点** |
| `SGLANG_MODEL` | Self-hosted SGLang model ID -> **自托管 SGLang 模型 ID** |
| `VLLM_BASE_URL` | Self-hosted vLLM endpoint -> **自托管 vLLM 端点** |
| `VLLM_MODEL` | Self-hosted vLLM model ID -> **自托管 vLLM 模型 ID** |
| `OLLAMA_BASE_URL` | Self-hosted Ollama endpoint -> **自托管 Ollama 端点** |
| `OLLAMA_MODEL` | Self-hosted Ollama model tag -> **自托管 Ollama 模型标签** |
| `NO_ANIMATIONS=1` | Force accessibility mode at startup -> 启动时强制启用无障碍模式 |
| `SSL_CERT_FILE` | Custom CA bundle for corporate proxies -> 企业代理自定义 CA 证书包 |

可在 `settings.toml` 中设置 `locale`，使用 `/config locale zh-Hans`，或依赖 `LC_ALL`/`LANG` 来选择 UI 界面及发送给 V4 模型的备用语言。自然语言推理与回复仍以最新用户消息为准，因此即使系统区域设置为英文，中文用户的输入仍将保持中文。详见 [docs/CONFIGURATION.md](docs/CONFIGURATION.md) 和 [docs/MCP.md](docs/MCP.md)。

---

## Models & Pricing

| Model | Context | Input (cache hit) | Input (cache miss) | Output |
|---|---|---|---|---|
| `deepseek-v4-pro` | 1M | $0.003625 / 1M | $0.435 / 1M | $0.87 / 1M | -> **`deepseek-v4-pro`**：上下文窗口 100万 tokens；输入（缓存命中）$0.003625/1M；输入（未命中）$0.435/1M；输出 $0.87/1M |
| `deepseek-v4-flash` | 1M | $0.0028 / 1M | $0.14 / 1M | $0.28 / 1M | -> **`deepseek-v4-flash`**：上下文窗口 100万 tokens；输入（缓存命中）$0.0028/1M；输入（未命中）$0.14/1M；输出 $0.28/1M |

DeepSeek 平台默认指向 `https://api.deepseek.com/beta`，以便在不额外配置的情况下测试 Beta 限制型 API 功能。设置 `base_url = "https://api.deepseek.com"` 可退出该行为。

旧版别名 `deepseek-chat` / `deepseek-reasoner` 映射至 `deepseek-v4-flash`，并将于 2026 年 7 月 24 日后停用。NVIDIA NIM 变体遵循你的 NVIDIA 账户条款。

> [!Note]
> DeepSeek 定价页现已将上述 V4 Pro 费率列为永久价格：随着促销窗口于 UTC 2026年5月31日 15:59 关闭，此前 75% 的折扣已折算为一次性基础费率调整。TUI 成本估算器已采用这些数值，因此无需行为变更。未来任何价格变动请查阅官方 [DeepSeek 定价页](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)。

---

## Publishing Your Own Skill

`codewhale` 会从工作区目录（`.agents/skills` → `skills` → `.opencode/skills` → `.claude/skills` → `.cursor/skills`）和全局目录（`~/.agents/skills` → `~/.claude/skills` → `~/.codewhale/skills` → `~/.deepseek/skills`）发现技能。每个技能是一个包含 `SKILL.md` 文件的目录：

```text
~/.agents/skills/my-skill/
└── SKILL.md
```

必须包含以下元数据（Frontmatter）：

```markdown
---
name: my-skill
description: Use this when DeepSeek should follow my custom workflow.
---

# My Skill
Instructions for the agent go here.
```

命令包括：`/skills`（列出）、`/skill <name>`（激活）、`/skill new`（生成脚手架）、`/skill install github:<owner>/<repo>`（社区安装）、`/skill update` / `uninstall` / `trust`。GitHub 社区安装无需后端服务。已安装的技能会出现在模型可见的会话上下文中；当你的任务匹配其描述时，智能体可通过 `load_skill` 工具自动选择相关技能。

首次启动还会安装内置的系统级常用工作流技能：`skill-creator`, `delegate`, `v4-best-practices`, `plugin-creator`, `skill-installer`, `mcp-builder`, `documents`, `presentations`, `spreadsheets`, `pdf`, and `feishu`。它们位于 `~/.codewhale/skills`（或旧版 `~/.deepseek/skills`）下，并采用版本化管理，以便在升级时添加新捆绑包，同时不会重建用户刻意删除的技能。

---

## Documentation

| Doc | Topic |
|---|---|
| [GUIDE.md](docs/GUIDE.md) | First-run user guide -> 首次使用用户指南 |
| [ARCHITECTURE.md](docs/ARCHITECTURE.md) | Codebase internals -> 代码库内部架构 |
| [CONFIGURATION.md](docs/CONFIGURATION.md) | Full config reference -> 完整配置参考 |
| [PROVIDERS.md](docs/PROVIDERS.md) | Provider IDs, auth, model defaults, and capability metadata -> 提供商 ID、认证、模型默认值及能力元数据 |
| [MODES.md](docs/MODES.md) | Plan / Agent / YOLO modes -> 规划 / 智能体 / YOLO 模式说明 |
| [MCP.md](docs/MCP.md) | Model Context Protocol integration -> 模型上下文协议集成 |
| [RUNTIME_API.md](docs/RUNTIME_API.md) | HTTP/SSE API server and mobile control page -> HTTP/SSE API 服务器与移动端控制页 |
| [INSTALL.md](docs/INSTALL.md) | Platform-specific install guide -> 平台特定安装指南 |
| [DOCKER.md](docs/DOCKER.md) | GHCR image, volumes, and Docker usage -> GHCR 镜像、卷管理与 Docker 用法 |
| [CNB_MIRROR.md](docs/CNB_MIRROR.md) | CNB mirror and China-friendly install notes -> CNB 镜像与中国区友好安装说明 |
| [TENCENT_CLOUD_REMOTE_FIRST.md](docs/TENCENT_CLOUD_REMOTE_FIRST.md) | Tencent/CNB/Lighthouse/Feishu remote-first path -> 腾讯/CNB/轻量应用服务器/飞书远程优先方案 |
| [TENCENT_LIGHTHOUSE_HK.md](docs/TENCENT_LIGHTHOUSE_HK.md) | Lighthouse Hong Kong server setup -> 香港轻量应用服务器部署手册 |
| [MEMORY.md](docs/MEMORY.md) | User memory feature guide -> 用户记忆功能指南 |
| [SUBAGENTS.md](docs/SUBAGENTS.md) | Sub-agent role taxonomy and lifecycle -> 子智能体角色分类与生命周期 |
| [KEYBINDINGS.md](docs/KEYBINDINGS.md) | Full shortcut catalog -> 完整快捷键目录 |
| [RELEASE_RUNBOOK.md](docs/RELEASE_RUNBOOK.md) | Release process -> 发布流程手册 |
| [LOCALIZATION.md](docs/LOCALIZATION.md) | UI locale matrix & switching -> UI 区域设置矩阵与切换说明 |
| [OPERATIONS_RUNBOOK.md](docs/OPERATIONS_RUNBOOK.md) | Ops & recovery -> 运维与故障恢复手册 |

完整更新日志：[CHANGELOG.md](CHANGELOG.md)。

---

## Thanks

- **[DeepSeek](https://github.com/deepseek-ai)** — thank you for the models and support that power every turn. 感谢 DeepSeek 提供模型与支持，让每一次交互成为可能。
- **[DataWhale](https://github.com/datawhalechina)** 🐋 — thank you for your support and for welcoming us into the Whale Brother family. 感谢 DataWhale 的支持，并欢迎我们加入“鲸兄弟”大家庭。
- **[OpenWarp](https://github.com/zerx-lab/warp)** — 感谢你优先支持 codewhale 并协作打造更优的终端智能体体验。
- **[Open Design](https://github.com/nexu-io/open-design)** — 感谢你在设计导向型智能体工作流方面的支持与协作。

本项目由日益壮大的贡献者社区共同推动：

- **[merchloubna70-dot](https://github.com/merchloubna70-dot)** — 28 个 PR，涵盖功能、修复与 VS Code 扩展脚手架 (#645–#681)
- **[WyxBUPT-22](https://github.com/WyxBUPT-22)** — Markdown 表格、粗体/斜体及水平线渲染 (#579)
- **[loongmiaow-pixel](https://github.com/loongmiaow-pixel)** — Windows + 中国区安装文档 (#578)
- **[20bytes](https://github.com/20bytes)** — 用户记忆文档与帮助文本润色 (#569)
- **[staryxchen](https://github.com/staryxchen)** — glibc 兼容性预检 (#556)
- **[Vishnu1837](https://github.com/Vishnu1837)** — glibc 兼容性改进及 SIGINT/SIGTERM 下的终端恢复 (#565, #1586)
- **[shentoumengxin](https://github.com/shentoumengxin)** — Shell `cwd` 边界验证 (#524)
- **[toi500](https://github.com/toi500)** — Windows 粘贴修复报告
- **[xsstomy](https://github.com/xsstomy)** — 终端启动重绘报告
- **[melody0709](https://github.com/melody0709)** — 斜杠前缀 Enter 激活报告
- **[lloydzhou](https://github.com/lloydzhou)** and **[jeoor](https://github.com/jeoor)** — 压缩成本报告；lloydzhou 还贡献了确定性环境上下文 (#813, #922) 与 KV prefix-cache 稳定化 (#1080)
- **[Agent-Skill-007](https://github.com/Agent-Skill-007)** — README 清晰度优化 (#685)
- **[woyxiang](https://github.com/woyxiang)** — Windows 安装文档 (#696)
- **[wangfeng](mailto:wangfengcsu@qq.com)** — 定价/折扣信息更新 (#692)
- **[zichen0116](https://github.com/zichen0116)** — CODE_OF_CONDUCT.md (#686)
- **[dfwqdyl-ui](https://github.com/dfwqdyl-ui)** — model ID 大小写兼容性报告 (#729)
- **[Oliver-ZPLiu](https://github.com/Oliver-ZPLiu)** — 过期 `working...` 状态 bug 报告、Windows 剪贴板回退、MCP Streamable HTTP 会话修复及 Homebrew tap 自动化 (#738, #850, #1643, #1631)
- **[reidliu41](https://github.com/reidliu41)** — resume 提示、工作区信任持久化、Ollama 提供商支持、思维块流式输出终结、CI 缓存加固、流式包装及 DeepSeek 模型补全 (#863, #870, #921, #1078, #1603, #1628, #1601)
- **[xieshutao](https://github.com/xieshutao)** — 纯 Markdown 技能回退 (#869)
- **[GK012](https://github.com/GK012)** — npm wrapper `--version` 回退 (#885)
- **[y0sif](https://github.com/y0sif)** — 直接子智能体完成后的父轮次循环唤醒 (#901)
- **[mac119](https://github.com/mac119)** and **[leo119](https://github.com/leo119)** — `codewhale update` 命令文档 (#838, #917)
- **[dumbjack](https://github.com/dumbjack)** / **浩淼的mac** — 命令安全空字节加固 (#706, #918)
- **macworkers** — 使用新会话 ID 的分叉确认 (#600, #919)
- **zero** and **[zerx-lab](https://github.com/zerx-lab)** — 通知条件配置与更丰富的 OSC 9 通知体 (#820, #920)
- **[chnjames](https://github.com/chnjames)** — 缓存 @mention 补全、配置恢复优化及 Windows UTF-8 Shell 输出 (#849, #927, #982, #1018)
- **[angziii](https://github.com/angziii)** — 配置安全、异步清理、Docker 加固及命令安全修复 (#822, #824, #827, #831, #833, #835, #837)
- **[elowen53](https://github.com/elowen53)** — UTF-8 解码与确定性测试覆盖 (#825, #840)
- **[wdw8276](https://github.com/wdw8276)** — 自定义会话标题的 `/rename` 命令 (#836)
- **[banqii](https://github.com/banqii)** — `.cursor/skills` 发现路径支持 (#817)
- **[junskyeed](https://github.com/junskyeed)** — API 请求的动态 `max_tokens` 计算 (#826)
- **Hafeez Pizofreude** — `fetch_url` 中的 SSRF 防护与 Star History 图表
- **Unic (YuniqueUnic)** — 基于 Schema 的配置 UI（TUI + Web）
- **Jason** — SSRF 安全加固
- **[axobase001](https://github.com/axobase001)** — 孤立快照清理、npm install 守卫、会话遥测修复、模型范围缓存清除、符号链接技能支持、npm 镜像逃逸指南、子任务代理保留、移动端运行时控制、Docker toolbox 文档、大输出收据及活动详情上下文 (#975, #1032, #1047, #1049, #1052, #1019, #1051, #1056, #1608, #1968, #2296, #2297, #2298)
- **[MengZ-super](https://github.com/MengZ-super)** — `/theme` 命令基础与 SSE gzip/brotli 解压缩 (#1057, #1061)
- **[DI-HUO-MING-YI](https://github.com/DI-HUO-MING-YI)** — Plan-mode 只读沙箱安全修复 (#1077)
- **[bevis-wong](https://github.com/bevis-wong)** — 精确粘贴 Enter 自动提交复现器 (#1073)
- **[Duducoco](https://github.com/Duducoco)** and **[AlphaGogoo](https://github.com/AlphaGogoo)** — skills slash-menu 与 `/skills` 覆盖修复 (#1068, #1083)
- **[ArronAI007](https://github.com/ArronAI007)** — macOS Terminal.app 和 ConHost 窗口调整伪影修复 (#993)
- **[THINKER-ONLY](https://github.com/THINKER-ONLY)** — OpenRouter 与自定义端点 model-ID 保留 (#1066)
- **[Jefsky](https://github.com/Jefsky)** — DeepSeek 端点修正报告 (#1079, #1084)
- **[wlon](https://github.com/wlon)** — NVIDIA NIM 提供商 API-key 偏好诊断 (#1081)
- **[Horace Liu](https://github.com/liuhq)** — Nix 包支持与安装文档 (#1173)
- **[jieshu666](https://github.com/jieshu666)** — 终端重绘闪烁减少 (#1563)
- **[gordonlu](https://github.com/gordonlu)** — Windows Enter / CSI-u 输入修复 (#1612)
- **[mdrkrg](https://github.com/mdrkrg)** — API 密钥缺失时的首次启动崩溃修复 (#1598)
- **[Aitensa](https://github.com/Aitensa)** — Diff 与 pager 输出的 CJK 换行传播 (#1622)
- **[qiyan233](https://github.com/qiyan233)** — 旧版 DeepSeek CN 提供商别名兼容性 (#1645)
- **[zlh124](https://github.com/zlh124)** — WSL2/headless 启动报告、clipboard-init 修复、CodeWhale tab-title 优化、本地化上下文菜单标签及审批对话框修复 (#1772, #1773, #2319, #2320, #2325)
- **[aboimpinto](https://github.com/aboimpinto)** — Windows alt-screen 日志、Home/End 编辑器及运行时日志跟随后续 (#1774, #1776, #1748, #1749, #1782, #1783)
- **[LeoLin990405](https://github.com/LeoLin990405)** — 提供商模型透传、推理重放、仅思维轮次及 Windows 引用修复 (#1740, #1743, #1742, #1744)
- **[nightt5879](https://github.com/nightt5879)** — Ctrl+C 提示恢复、提供商注册表漂移文档、工具搜索默认值、底部 Git 分支显示及启动提示交互性 (#1764, #2274, #2344, #2347, #2373)
- **[donglovejava](https://github.com/donglovejava)** — @file 粘贴整合、CJK panic 修复、用户反馈、RLM 路由、edit_file 重试、隐藏工作树发现跳过、IME 编辑器路由及即时 Shell 伴侣工具 (#2154-#2168, #2302, #2329, #2330, #2331)
- **[encyc](https://github.com/encyc)** — 底部与会话 token 明细分解 (#2152)
- **[saieswar237](https://github.com/saieswar237)** — 审查流水线文档 (#2178)
- **[sximelon](https://github.com/sximelon)** — Enter 粘贴抑制、键处理程序提取 (#2174, #2042)
- **[nanookclaw](https://github.com/nanookclaw)** — doctor 输出中的搜索提供商 (#2135)
- **[Sskift](https://github.com/Sskift)** — CLI 默认环境变量覆盖防护与状态栏底部清除 (#2119, #2248)
- **[xin1104](https://github.com/xin1104)** — Homebrew codewhale 二进制安装 (#2105)
- **[mrluanma](https://github.com/mrluanma)** — Metaso 搜索提供商 (#2059)
- **[Lellansin](https://github.com/Lellansin)** — 跳过主目录配置合并 (#2055)
- **[zhuangbiaowei](https://github.com/zhuangbiaowei)** — 更新发布通道与遗留 MCP SSE 修复 (#2145, #2301)
- **[cy2311](https://github.com/cy2311)** — CodeWhale Windows `.bat` 启动器 (#1861)
- **[LING71671](https://github.com/LING71671)** — 有效成本货币上下文、自定义提供商文档及核心工具分类提示词块 (#1902, #2287, #2292)
- **[dzyuan](https://github.com/dzyuan)** — Volcengine 提供商支持（DeepSeek V4 Pro/Flash 模型）(#1993)
- **[mvanhorn](https://github.com/mvanhorn)** — 实时请求形状测试工厂与全局 `~/.agents/AGENTS.md` 回退 (#2107, #2236)
- **[malsony](https://github.com/malsony)** — Matrix 风格主题与主题选择器改进 (#2129)
- **[gaord](https://github.com/gaord)** — 外部 GUI 运行时事件桥、会话详情序列化及 skills API 发现对齐 (#2133, #2265, #2285)
- **[yuanchenglu](https://github.com/yuanchenglu)** — 飞书单聊模型切换 (#2149)
- **[HUQIANTAO](https://github.com/HUQIANTAO)** — Xiaomi 余额/状态工作、停滞轮次恢复、审批意图摘要、移动端烟雾测试/QR 支持、Claude 主题及广泛文档/测试/CI 覆盖 (#2257, #2267, #2283, #2384, #2385, #2389, #2403, #2440-#2458, #2460)
- **[h3c-hexin](https://github.com/h3c-hexin)** — 网页搜索 URL 解码、提示词/指令覆盖钩子、子智能体指导、SSRF 假 IP 信任配置及提示词缓存友好环境放置 (#2245, #2311, #2313, #2314, #2354, #2355, #2356)
- **[AresNing](https://github.com/AresNing)** — 首次使用指南与消息提交钩子转换设计整合至维护中的钩子路径 (#2278, #2318, #2434)
- **[Implementist](https://github.com/Implementist)** — Volcengine Ark 搜索提供商与可靠性加固 (#2426, #2429, #2439)
- **[lihuan215](https://github.com/lihuan215)** — Unix socket 钩子 sink 设计整合至可选钩子事件路径 (#2333, #2430)
- **[AdityaVG13](https://github.com/AdityaVG13)** — Xiaomi MiMo 提供商支持 (#2246)
- **[New2Niu](https://github.com/New2Niu)** — macOS 显示通知 (#2260)
- **[AiurArtanis](https://github.com/AiurArtanis)** — Solarized Light 主题 (#2270)
- **[Lee-take](https://github.com/Lee-take)** — 任务迁移与会话环境隔离修复 (#2272)
- **[LeoAlex0](https://github.com/LeoAlex0)** — 消息计数与工具输出缓存保留的会话持久化修复 (#2388, #2395)
- **[jimmyzhuu](https://github.com/jimmyzhuu)** — `web_search` 的百度 AI Search 后端 (#2371)
- **[rockyzhang](https://github.com/rockyzhang)** — RISC-V 预编译二进制支持 (#2383)
- **[mo-vic](https://github.com/mo-vic)** — 智能体驱动上下文修剪的 `/purge` 斜杠命令 (#2387)
- **[hufanexplore](https://github.com/hufanexplore)** — Java 与 Vue 语言服务器默认配置 (#2367)
- **[hoclaptrinh33](https://github.com/hoclaptrinh33)** — 越南语本地化支持 (#2358)
- **[AccMoment](https://github.com/AccMoment)** — update 命令的代理选项 (#2281)
- **[idling11](https://github.com/idling11)** — 持久化 SlopLedger 与 `/hunt` 重命名/奖杯卡工作 (#2161, #2306)
- **[cyq1017](https://github.com/cyq1017)** — 运行时事件信封、渲染 diff 调试日志及确定性编辑器历史刷新 (#2252, #2332, #2375)
- **[hongqitai](https://github.com/hongqitai)** — 状态模式父条目支持与 clippy/fmt 清理 (#2308, #2432)
- **[BryonGo](https://github.com/BryonGo)** — effective-model 压缩预算修复 (#2437)

塑造 v0.8.48 的报告、复现与验证工作也值得公开致谢：**[@buko](https://github.com/buko)**, **[@yyyCode](https://github.com/yyyCode)**, **[@gaslebinh-glitch](https://github.com/gaslebinh-glitch)**, **[@Dr3259](https://github.com/Dr3259)**, **[@lpeng1711694086-lang](https://github.com/lpeng1711694086-lang)**, **[@VerrPower](https://github.com/VerrPower)**, **[@yan-zay](https://github.com/yan-zay)**, **[@jretz](https://github.com/jretz)**, **[@Neo-millunnium](https://github.com/Neo-millunnium)**, **[@caeserchen](https://github.com/caeserchen)**, **[@T-Phuong-Nguyen](https://github.com/T-Phuong-Nguyen)**, **[@zhyuzhyu](https://github.com/zhyuzhyu)**, **[@0gl20shk0sbt36](https://github.com/0gl20shk0sbt36)**, **[@hatakes](https://github.com/hatakes)**, **[@goodvecn-dev](https://github.com/goodvecn-dev)**, **[@bevis-wong](https://github.com/bevis-wong)**, **[@PurplePulse](https://github.com/PurplePulse)**, and **[@nbiish](https://github.com/nbiish)**.

---

## Contributing

参见 [CONTRIBUTING.md](CONTRIBUTING.md)。欢迎提交 PR——可浏览[开放议题](https://github.com/Hmbown/CodeWhale/issues)寻找适合初学者的贡献点。

支持本项目：[请我喝杯咖啡](https://www.buymeacoffee.com/hmbown)。

> [!Note]
> *本人与 DeepSeek Inc. 无隶属关系。*

## License

[MIT](LICENSE)

## Star History

[![Star History Chart](https://api.star-history.com/chart?repos=Hmbown/CodeWhale&type=date&legend=top-left)](https://www.star-history.com/?repos=Hmbown%2FCodeWhale&type=date&logscale=&legend=top-left)