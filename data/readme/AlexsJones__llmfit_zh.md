# llmfit

<p align="center">
  <img src="assets/icon.svg" alt="llmfit icon" width="128" height="128">
</p>

<p align="center">
  <b>English</b> ·
  <a href="README.zh.md">中文</a>
</p>

<p align="center">
  <a href="https://github.com/AlexsJones/llmfit/actions/workflows/ci.yml"><img src="https://github.com/AlexsJones/llmfit/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://crates.io/crates/llmfit"><img src="https://img.shields.io/crates/v/llmfit.svg" alt="Crates.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
  <a href="https://about.signpath.io"><img src="https://img.shields.io/badge/SignPath-signed-brightgreen?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0id2hpdGUiIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTEwLjA2NyA0LjU2N2wtNC43MzQgNC43MzMtMS40LTEuNGExIDEgMCAwIDAtMS40MTQgMS40MTRsMi4xIDIuMWExIDEgMCAwIDAgMS40MTQgMGw1LjQ0LTUuNDRhMSAxIDAgMCAwLTEuNDE0LTEuNDE0eiIvPjwvc3ZnPg==" alt="Signed with SignPath"></a>
</p>

> **新增：[社区排行榜](#community-leaderboard-b)** — 浏览真实用户的实际性能数据。按 `b` 可查看任意显卡（不仅限于你的设备）的实测 tok/s、TTFT 和显存占用。使用 `H` 从 27+ 硬件预设（RTX 5090 到 Apple M1）中选择，在购买或组装前对比真实数据。

**数百个模型与提供商。一条命令即可找出适合你硬件运行的模型。**

一款终端工具，可根据系统的内存、CPU 和显卡为 LLM 模型进行容量匹配。它会自动检测你的硬件，从质量、速度、适配度和上下文维度对每个模型进行评分，并告诉你哪些能在你的机器上真正流畅运行。

默认提供交互式 TUI（终端用户界面），也支持经典 CLI 模式。支持多显卡配置、MoE（混合专家）架构、动态量化选择、速度估算，以及本地运行时提供商（Ollama、llama.cpp、MLX、Docker Model Runner、LM Studio）。

**新增：[社区排行榜](#community-leaderboard-b) (`b`)** — 查看其他使用相同硬件用户的实测 tok/s、TTFT 和显存占用。该功能由 [localmaxxing.com](https://localmaxxing.com) 提供支持，填补了理论估算与实际性能之间的差距。

此外还有：[下载管理器](#download-manager-d) (`D`)、[高级配置](#advanced-configuration-a) (`A`) 和 [硬件模拟](#hardware-simulation-s)。按 `D` 管理下载、查看历史记录、删除模型及配置下载目录。按 `A` 调整 TPS 效率、运行模式系数与评分权重。按 `S` 模拟不同硬件环境。

> **相关项目：**
> - [sympozium](https://github.com/sympozium-ai/sympozium/) — 在 Kubernetes 中管理 Agent。
> - [llmserve](https://github.com/AlexsJones/llmserve) — 用于部署本地 LLM 模型的简易 TUI。选择模型、选择后端，一键服务化。
> - [llama-panel](https://github.com/AlexsJones/llama-panel) — 原生 macOS 应用，用于管理本地 `llama-server` 实例。

![demo](assets/demo.gif)

---

## 安装

### Windows
```sh
scoop install llmfit
```

如果未安装 Scoop，请参照 [Scoop 安装指南](https://scoop.sh/)。

### macOS / Linux

#### Homebrew

预编译二进制文件（推荐，适用于所有 macOS/Linux 版本）：
```sh
brew install AlexsJones/llmfit/llmfit
```

或通过 homebrew-core 公式安装（在 macOS 无预编译包时从源码构建）：
```sh
brew install llmfit
```

#### MacPorts
```sh
port install llmfit
```

#### 快速安装
```sh
curl -fsSL https://llmfit.axjns.dev/install.sh | sh
```

从 GitHub 下载最新发行版二进制文件并安装至 `/usr/local/bin`（若无 sudo 权限则安装到 `~/.local/bin`）。

**无需 sudo 安装至 `~/.local/bin`：**
```sh
curl -fsSL https://llmfit.axjns.dev/install.sh | sh -s -- --local
```

### uv / pip
安装或更新 llmfit：
```sh
uv tool install -U llmfit
```

免安装运行：
```sh
uvx llmfit
```

你也可以使用 pip 或 uv 等工具以常规方式将 llmfit 作为 Python 包进行安装。

### Docker / Podman
```sh
docker run ghcr.io/alexsjones/llmfit
```
此命令会输出 `llmfit recommend` 的 JSON 结果。你可以使用 `jq` 进一步查询该 JSON。
```
podman run ghcr.io/alexsjones/llmfit recommend --use-case coding | jq '.models[].name'
```

### 从源码构建
```sh
git clone https://github.com/AlexsJones/llmfit.git
cd llmfit
cargo build --release
# binary is at target/release/llmfit
```

---

## 使用方法

### TUI（默认）

```sh
llmfit
```

启动交互式终端界面。顶部会显示你的系统配置（CPU、内存、显卡名称、显存、后端）。模型列表按综合评分排序，支持滚动浏览。每行展示模型的评分、预估 tok/s、适配你硬件的最佳量化方式、运行模式、内存占用及用例分类。

| 按键                        | 操作                                                                |
|----------------------------|-----------------------------------------------------------------------|
| `Up` / `Down` 或 `j` / `k` | 上下导航模型                                                       |
| `/`                        | 进入搜索模式（支持按名称、提供商、参数量、用例进行模糊匹配） |
| `Esc` 或 `Enter`           | 退出搜索模式                                                      |
| `Ctrl-U`                   | 清除搜索                                                          |
| `f`                        | 循环切换适配过滤器：全部、可运行、完美、良好、边缘              |
| `a`                        | 循环切换可用性过滤器：全部、GGUF 可用、已安装                 |
| `s`                        | 循环切换排序列：评分、参数量、内存占比、上下文、日期、用例           |
| `v`                        | 进入可视化模式（多选模型）                            |
| `V`                        | 进入选择模式（基于列的过滤）                            |
| `t`                        | 循环切换颜色主题（自动保存）                               |
| `p`                        | 打开选定模型的规划模式（硬件需求规划）                 |
| `P`                        | 打开提供商过滤器弹窗（输入文本模糊过滤）          |
| `U`                        | 打开用例过滤器弹窗                                            |
| `C`                        | 打开能力过滤器弹窗                                          |
| `L`                        | 打开许可证过滤器弹窗                                             |
| `R`                        | 打开运行时/后端过滤器弹窗（llama.cpp、MLX、vLLM）             |
| `S`                        | 打开硬件模拟弹窗（覆盖内存/显存/CPU）                |
| `A`                        | 打开高级配置弹窗（调整效率、运行模式系数） |
| `b`                        | 打开社区排行榜视图（localmaxxing.com）                    |
| `I`                        | 打开推理基准测试视图（使用你的模型进行本地质量评分）        |
| `h`                        | 打开帮助弹窗（所有按键绑定）                                    |
| `m`                        | 标记选定模型用于对比                                       |
| `c`                        | 打开对比视图（已标记 vs 当前选中）                                |
| `x`                        | 清除对比标记                                                    |
| `i`                        | 切换优先排序已安装模型（针对检测到的任意运行时提供商）        |
| `d`                        | 下载选定模型（多个可用时弹出提供商选择器） |
| `D`                        | 打开下载管理器（历史记录、删除、配置）                     |
| `r`                        | 刷新从运行时提供商安装的模型                       |
| `Enter`                    | 切换选中模型的详情视图                                 |
| `PgUp` / `PgDn`            | 按 10 行滚动                                                          |
| `g` / `G`                  | 跳转至顶部 / 底部                                                  |
| `q`                        | 退出                                                                  |

### 类 Vim 模式

TUI 采用类 Vim 的模式，显示在左下角状态栏。当前模式决定哪些按键生效。

#### 普通模式 (Normal)

默认模式。用于导航、搜索、过滤和打开视图。上方表格中的所有按键均在此模式下有效。

#### 可视化模式 (`v`)

选择连续范围的模型进行批量对比。按 `v` 锚定当前行，然后使用 `j`/`k` 或方向键扩展选区。选中行会高亮显示。

| 按键                 | 操作                                                 |
|---------------------|--------------------------------------------------------|
| `j` / `k` 或方向键 | 向上/向下扩展选区                               |
| `c`                 | 对比所有选中模型（打开多模型对比视图） |
| `m`                 | 标记当前模型用于双模型对比               |
| `Esc` 或 `v`        | 退出可视化模式                                       |

多模型对比视图以表格形式展示，行为属性（评分、tok/s、适配度、内存占比、参数量、模式、上下文、量化等），列为模型。最佳值会高亮显示。若选中的模型过多无法一屏显示，可使用 `h`/`l` 或方向键水平滚动。

#### 选择模式 (`V`)

基于列的操作。按 `V`（Shift+v）进入选择模式，然后使用 `h`/`l` 或方向键在列标题间移动。当前激活的列会高亮显示。按 `Enter` 或 `Space` 触发该列的当前操作。

| 列                        | 过滤操作                                                             |
|----------------------------|-----------------------------------------------------------------------|
| Inst                          | 循环切换可用性过滤器                                                 |
| Model                         | 进入搜索模式                                                         |
| Provider                      | 打开提供商弹窗                                                       |
| Params                        | 打开参数量级选择器（<3B、3-7B、7-14B、14-30B、30-70B、70B+） |
| Score, tok/s, Mem%, Ctx, Date | 按该列排序                                                       |
| Quant                         | 打开量化选择器                                                   |
| Mode                          | 打开运行模式选择器（GPU、MoE、CPU+GPU、CPU）                              |
| Fit                           | 循环切换适配过滤器                                                          |
| Use Case                      | 打开用例选择器                                                       |

在选择模式下仍可使用行导航功能，以便实时查看操作效果：支持 `j`/`k`、方向键、`Ctrl-U`、`Ctrl-D`、`PageUp`、`PageDown`、`Home` 和 `End`。按 `Esc` 返回普通模式。

### TUI 规划模式 (`p`)

规划模式反转了常规的适配分析逻辑：它不再问“什么模型适合我的硬件？”，而是估算“运行此模型配置需要什么硬件？”

在选中行上按 `p`，然后：

| 按键                    | 操作                                                    |
|------------------------|-----------------------------------------------------------|
| `Tab` / `j` / `k`      | 在不同可编辑字段间移动（上下文、量化、目标 TPS） |
| `Left` / `Right`       | 在当前字段内移动光标                              |
| 输入                   | 编辑当前字段                                        |
| `Backspace` / `Delete` | 删除字符                                         |
| `Ctrl-U`               | 清空当前字段                                       |
| `Esc` 或 `q`           | 退出规划模式                                            |

规划模式会提供以下估算数据：
- 最低及推荐显存/内存/CPU 核心数
- 可行的运行路径（纯 GPU、CPU 卸载、仅 CPU）
- 达到更佳适配目标所需的硬件升级增量

### 硬件模拟 (`S`)

按 `S` 打开硬件模拟弹窗。覆盖内存、显存和 CPU 核心数，查看哪些模型能适配不同的目标硬件配置。所有模型的评分、适配等级和速度估算都会立即根据模拟参数重新计算。

![Hardware Simulation](assets/simulation.png)

| 按键                    | 操作                                  |
|------------------------|-----------------------------------------|
| `Tab` / `j` / `k`      | 在内存、显存、CPU 字段间切换    |
| 输入数字            | 编辑选中字段                 |
| `Enter`               | 应用模拟配置                        |
| `Ctrl-R`              | 重置为实际检测到的硬件         |
| `Esc`                 | 取消并关闭                        |

激活模拟后，系统栏和状态栏会显示 `SIM` 标识。整个模型列表将反映模拟硬件的配置，直到你重置为止。

### 高级配置 (`A`)

按 `A` 打开高级配置弹窗。此面板允许你调整 TPS 估算、运行模式惩罚和综合评分背后的参数——旨在解决 [issue #449](https://github.com/AlexsJones/llmfit/issues/449) 中提到的某些模型（如 Qwen3 30B）tok/s 被高估的问题。

所有更改将立即生效，并重新计算模型列表评分。按 `Esc` 接受或 `Ctrl-R` 恢复默认值后关闭。

| 字段              | 描述                                                             | 默认值 |
|--------------------|-------------------------------------------------------------------------|---------|
| **效率因子**     | 基于带宽的 TPS 全局效率系数。用于核算系统开销 | `0.55`  |
| **GPU 系数**     | 纯 GPU 推理的速度乘数                                 | `1.0`   |
| **CPU 卸载**    | 权重溢出至系统内存时的速度乘数                       | `0.5`   |
| **MoE 专家切换**    | MoE 架构中专家切换的速度乘数                | `0.8`   |
| **张量并行 (Tensor Par)**     | 张量并行推理的速度乘数                          | `0.9`   |
| **仅 CPU**       | 纯 CPU 执行的速度乘数                                 | `0.3`   |
| **上下文上限**    | 用于内存估算的最大上下文长度（留空则使用默认值） | `auto`  |

| 按键                    | 操作                                  |
|------------------------|-----------------------------------------|
| `Tab` / `j` / `k`      | 在不同字段间切换                   |
| 输入数字或 `.`      | 编辑选中字段                 |
| `Left` / `Right`       | 在字段内移动光标            |
| `Backspace` / `Delete` | 删除字符                       |
| `Ctrl-U`               | 清空当前字段                 |
| `Enter`                | 应用更改并重新计算所有评分|
| `Esc` / `q`            | 关闭而不应用                  |

### 下载管理器 (`D`)

按 `D` 打开下载管理器视图。此全屏视图会替换主模型列表，并提供三个区域：

- **当前下载** — 显示正在进行的下载任务，包含进度条、模型名称和状态消息。
- **配置** — 显示（并允许编辑）GGUF 模型目录。配置的目录路径会在跨会话间保持持久化。
- **历史记录** — 可浏览的过往下载列表（按时间倒序），包含模型名称、提供商、状态和日期。失败的下载可从历史中移除，成功的下载可从提供商处删除。

使用 `Tab` / `Shift-Tab` 在区域间切换焦点。

| 按键                    | 操作                                           |
|------------------------|--------------------------------------------------|
| `Tab` / `Shift-Tab`   | 循环切换焦点：当前下载 → 配置 → 历史记录           |
| `j` / `k` 或方向键   | 浏览历史记录列表（当聚焦于历史记录时）  |
| `x`                   | 删除选中模型（会弹出确认提示）  |
| `y` / `n`             | 确认或删除                        |
| `e`                   | 编辑下载目录（当聚焦于配置时）     |
| `Enter`               | 确认目录修改                            |
| `Esc` / `D` / `q`    | 关闭并返回模型列表               |

对于失败的下载（如 404 错误），按 `x` 可从历史记录中移除条目。对于成功的下载，则会从提供商处删除该模型（支持 Ollama 和 llama.cpp）。

### 社区排行榜 (`b`)

按 `b` 打开社区排行榜视图。不再仅依赖 llmfit 的理论速度估算，此视图展示了其他使用相同硬件用户的**实际性能数据**——实测 tok/s、首 token 时间（TTFT）和峰值显存占用。

![Community Leaderboard](assets/benchmark.jpeg)

数据来源于 [localmaxxing.com](https://localmaxxing.com) 社区基准数据库。打开视图时，llmfit 会自动检测你的硬件（显卡型号、显存档位、Apple Silicon 芯片系列、操作系统）并查询匹配结果。

| 列       | 描述                                              |
|--------------|----------------------------------------------------------|
| **模型**    | HuggingFace 模型 ID                                     |
| **后端/引擎**   | 使用的推理运行时（llama.cpp、vLLM、Ollama、MLX...） |
| **量化**    | 量化格式（Q4_K_M、Q8_0 等）                |
| **tok/s**    | 实测输出 token 生成速度                   |
| **总吞吐量 (Total t/s)**| 总吞吐率（提示词 + 生成）                   |
| **TTFT**     | 首 token 时间（延迟）                            |
| **显存 (VRAM)**     | 推理期间的峰值内存占用                       |
| **上下文 (Ctx)**      | 基准测试中使用的上下文长度                     |
| **用户**     | 提交者（带 `*` 表示已验证用户）               |

| 按键                    | 操作                                  |
|------------------------|-----------------------------------------|
| `j` / `k` 或方向键   | 浏览结果                        |
| `H`                    | 打开硬件选择器（浏览任意显卡）   |
| `r`                    | 刷新 / 重新从 API 获取数据             |
| `b` / `q` / `Esc`     | 关闭并返回模型列表         |

按 `H` 打开硬件选择器——一个包含 27 款主流显卡和芯片的可浏览列表（从 RTX 5090 到纯 CPU，以及 Apple Silicon M1–M4 变体、AMD RX/MI 系列和 NVIDIA 数据中心卡）。选择一个即可立即加载该硬件的基准数据，即使你当前并未使用它。选择“我的硬件（自动检测）”可返回你自己的系统配置。

#### API 密钥设置

公开基准测试无需认证即可使用。如需完整访问权限，请提供你的 [localmaxxing.com](https://localmaxxing.com) API 密钥：

```sh
# 通过环境变量（推荐）
export LOCALMAXXING_API_KEY="bhk_your_key_here"
llmfit

# 或通过 CLI 参数
llmfit --api-key "bhk_your_key_here"
```

| 变量 | 描述 |
|---|---|
| `LOCALMAXXING_API_KEY` | localmaxxing.com API 的 Bearer Token |

### 推理基准测试 (`I`)

按大写 `I` 打开推理基准测试视图。此功能会对你本地运行的提供商（Ollama、vLLM 和 MLX）进行**实时推理基准测试**——通过真实的推理请求测量首 token 时间（TTFT）、每秒 token 数（TPS）和总延迟。

与社区排行榜（展示其他用户的众包数据）不同，推理基准测试直接在你的实际硬件上使用你的实际模型进行测量。

#### TUI 使用方法

| 按键 | 操作 |
|-----|--------|
| `I` | 打开推理基准测试（自动检测提供商并运行测试） |
| `I`（再次） | 在基准视图内重新运行测试 |
| `j` / `k` 或方向键 | 浏览模型结果 |
| `Enter` | 打开选中模型的详情视图 |
| `r` | 切换至路由矩阵视图 |
| `q` / `Esc` | 关闭基准视图 |

结果会缓存至 `~/.config/llmfit/bench-cache.json`，下次打开时即时加载。

#### CLI 使用方法

```sh
# 自动检测提供商并运行基准测试
llmfit bench

# 对所有已发现的模型在所有运行的提供商上运行基准测试
llmfit bench --all

# 通过 Ollama 对特定模型进行基准测试
llmfit bench --provider ollama llama3.2

# 覆盖端点 URL
llmfit bench --provider ollama --url http://my-server:11434 llama3.2

# 覆盖 vLLM 端点
llmfit bench --provider vllm --url http://localhost:8000

# 输出 JSON（用于脚本处理）
llmfit bench --json

# 运行质量基准测试（基于角色的路由评分）
llmfit bench --quality

# 输出路由矩阵
llmfit bench --quality --routing
```

#### 环境变量

| 变量 | 默认值 | 描述 |
|---|---|---|
| `OLLAMA_HOST` | `http://localhost:11434` | Ollama API 基础 URL |
| `VLLM_PORT` | `8000` | vLLM 服务器端口（用作 `http://localhost:$VLLM_PORT`） |

### 主题

按 `t` 循环切换 10 种内置颜色主题。你的选择会自动保存至 `~/.config/llmfit/theme`，并在下次启动时恢复。

| 主题                    | 描述                                       |
|--------------------------|---------------------------------------------------|
| **Default**              | llmfit 原始配色                            |
| **Dracula**              | 深紫色背景搭配柔和亮色点缀        |
| **Solarized**            | Ethan Schoonover 的 Solarized Dark 调色板         |
| **Nord**                 | 北极冷色调蓝灰风格                      |
| **Monokai**              | Monokai Pro 暖色系语法配色                    |
| **Gruvbox**              | 复古大地色调与温暖土色搭配        |
| **Catppuccin Latte**     | 🌻 浅色主题 — 和谐柔和的亮色反转      |
| **Catppuccin Frappé**    | 🪴 低对比度暗色 —  muted、内敛美学   |
| **Catppuccin Macchiato** | 🌺 中对比度暗色 — 温和舒缓的色调  |
| **Catppuccin Mocha**     | 🌿 最深变体 — 舒适且色彩丰富点缀 |

### Web 仪表盘

在非 JSON 模式下运行 `llmfit` 时，它会自动在后台启动一个 Web 仪表盘（监听 `0.0.0.0:8787`）。在同一网络下的任意浏览器中打开即可访问：

```
http://<your-machine-ip>:8787
```

可通过环境变量覆盖主机或端口：

```sh
LLMFIT_DASHBOARD_HOST=0.0.0.0 LLMFIT_DASHBOARD_PORT=9000 llmfit
```

| 变量 | 默认值 | 描述 |
|---|---|---|
| `LLMFIT_DASHBOARD_HOST` | `0.0.0.0` | 绑定仪表盘服务器的网络接口 |
| `LLMFIT_DASHBOARD_PORT` | `8787` | 绑定仪表盘服务器的端口号 |

若要禁用自动启动的仪表盘，请添加 `--no-dashboard` 参数：

```sh
llmfit --no-dashboard
```

### CLI 模式

使用 `--cli` 或任意子命令即可获取经典的表格输出：

```sh
# 按适配度排序的所有模型列表
llmfit --cli

# 仅完美适配的模型，前 5 个
llmfit fit --perfect -n 5

# 显示检测到的系统配置
llmfit system

# 列出数据库中的所有模型
llmfit list

# 按名称、提供商或大小搜索
llmfit search "llama 8b"

# 单个模型的详细视图
llmfit info "Mistral-7B"

# Top 5 推荐（JSON，供 Agent/脚本消费）
llmfit recommend --json --limit 5

# 按用例过滤的推荐
llmfit recommend --json --use-case coding --limit 3

# 强制指定运行时（绕过 Apple Silicon 上的自动 MLX 选择）
llmfit recommend --force-runtime llamacpp
llmfit recommend --force-runtime llamacpp --use-case coding --limit 3

# 规划特定模型配置所需的硬件
llmfit plan "Qwen/Qwen3-4B-MLX-4bit" --context 8192
llmfit plan "Qwen/Qwen3-4B-MLX-4bit" --context 8192 --quant mlx-4bit
llmfit plan "Qwen/Qwen3-4B-MLX-4bit" --context 8192 --target-tps 25 --json

# 作为节点级 REST API 运行（供集群调度器/聚合器使用）
llmfit serve --host 0.0.0.0 --port 8787
```

### REST API (`llmfit serve`)

`llmfit serve` 会启动一个 HTTP API，暴露与 TUI/CLI 相同的适配/评分数据，包括节点过滤和最佳模型选择功能。

```sh
# 健康检查
curl http://localhost:8787/health

# 节点硬件信息
curl http://localhost:8787/api/v1/system

# 带过滤器的完整适配列表
curl "http://localhost:8787/api/v1/models?min_fit=marginal&runtime=llamacpp&sort=score&limit=20"

# 关键调度端点：此节点可运行的最佳模型
curl "http://localhost:8787/api/v1/models/top?limit=5&min_fit=good&use_case=coding"

# 按模型名称/提供商文本搜索
curl "http://localhost:8787/api/v1/models/Mistral?runtime=any"
```

`models`/`models/top` 支持的查询参数：

- `limit`（或 `n`）：返回的最大行数
- `perfect`: `true|false`（设为 `true` 时强制仅显示完美适配模型）
- `min_fit`: `perfect|good|marginal|too_tight`
- `runtime`: `any|mlx|llamacpp`
- `use_case`: `general|coding|reasoning|chat|multimodal|embedding`
- `provider`: 提供商文本过滤（子串匹配）
- `search`: 跨名称/提供商/大小/用例的自由文本过滤
- `sort`: `score|tps|params|mem|ctx|date|use_case`
- `include_too_tight`: 包含不可运行的行（默认 `/top` 为 `false`，`/models` 为 `true`）
- `max_context`: 单次请求的上下文上限（用于内存估算）
- `force_runtime`: `mlx|llamacpp|vllm` — 在分析期间覆盖自动运行时选择

在本地验证 API 行为：

```sh
# 自动启动服务器并运行端点/模式/过滤器断言测试
python3 scripts/test_api.py --spawn

# 或测试已运行的服务器
python3 scripts/test_api.py --base-url http://127.0.0.1:8787
```

### 硬件参数覆盖

部分系统的硬件自动检测可能失败（例如 `nvidia-smi` 损坏、虚拟机、直通配置），或者你可能希望评估模型在不同目标硬件上的适配情况。使用 `--memory`、`--ram` 和 `--cpu-cores` 覆盖检测到的值：

```sh
# 覆盖显卡显存
llmfit --memory=32G

# 覆盖系统内存
llmfit --ram=128G

# 覆盖 CPU 核心数
llmfit --cpu-cores=16

# 组合覆盖以模拟目标硬件
llmfit --memory=24G --ram=64G --cpu-cores=8 fit
llmfit --memory=24G --ram=64G system --json

# 适用于所有模式：TUI、CLI 和子命令
llmfit --memory=24G --cli
llmfit --memory=24G fit --perfect -n 5
llmfit --ram=64G recommend --json
```

`--memory` 和 `--ram` 接受的单位后缀为：`G`/`GB`/`GiB`（吉字节）、`M`/`MB`/`MiB`（兆字节）、`T`/`TB`/`TiB`（太字节）。不区分大小写。若未检测到 GPU，使用 `--memory` 会创建一个虚拟显卡条目，以便对 GPU 推理进行评分。在统一内存系统（Apple Silicon）上，`--ram` 也会更新显存；如需独立覆盖显存，请使用 `--memory`。

### 估算上下文长度上限

使用 `--max-context` 限制用于内存估算的上下文长度（不改变模型官方宣称的最大上下文）：

```sh
# 在 4K 上下文下估算内存适配情况
llmfit --max-context 4096 --cli

# 适用于子命令
llmfit --max-context 8192 fit --perfect -n 5
llmfit --max-context 16384 recommend --json --limit 5
```

若未设置 `--max-context`，llmfit 在有可用时会使用 `OLLAMA_CONTEXT_LENGTH`。

### JSON 输出

对任意子命令添加 `--json` 即可获取机器可读的输出：

```sh
llmfit --json system     # 硬件配置（JSON）
llmfit --json fit -n 10  # Top 10 适配模型（JSON）
llmfit recommend --json  # Top 5 推荐（recommend 默认即为 JSON）
llmfit plan "Qwen/Qwen2.5-Coder-0.5B-Instruct" --context 8192 --json
```

`plan` 的 JSON 输出包含以下稳定字段：请求参数（上下文、量化、目标 TPS）、估算的最小/推荐硬件、各路径可行性（GPU、CPU 卸载、仅 CPU）及升级增量。

---

## 工作原理

1. **硬件检测** —— 通过 `sysinfo` 读取总内存/可用内存，统计 CPU 核心数，并探测显卡：
   - **NVIDIA** —— 多显卡支持（通过 `nvidia-smi`）。聚合所有检测到的显卡显存。若报告失败，则根据显卡型号名称估算显存。
   - **AMD** —— 通过 `rocm-smi` 检测。
   - **Intel Arc** —— 独立显卡通过 sysfs，核显通过 `lspci`。
   - **Apple Silicon** —— 通过 `system_profiler` 获取统一内存。显存等于系统总内存。
   - **昇腾 (Ascend)** —— 通过 `npu-smi` 检测。
   - **后端检测** —— 自动识别加速后端（CUDA、Metal、ROCm、SYCL、CPU ARM、CPU x86、昇腾）以进行速度估算。

2. **模型数据库** —— 数百个模型源自 HuggingFace API，存储于 `data/hf_models.json` 并在编译时嵌入。内存需求基于参数量及量化层级（Q8_0 至 Q2_K）计算得出。显存是 GPU 推理的主要限制因素；系统内存则是仅 CPU 执行的备选方案。

   **MoE 支持** —— 自动检测采用混合专家架构的模型（Mixtral、DeepSeek-V2/V3）。每个 token 仅激活部分专家，因此实际显存需求远低于总参数量所示。例如，Mixtral 8x7B 总参数为 46.7B，但每 token 仅激活约 12.9B，配合专家卸载可将显存从 23.9 GB 降至约 6.6 GB。

3. **动态量化** —— llmfit 不假设固定量化格式，而是尝试寻找适配你硬件的最佳质量量化方案。它会从 Q8_0（最高质量）向下遍历至 Q2_K（最压缩），选择能放入可用内存的最高质量版本。若全上下文长度下无模型可运行，则会在半上下文长度下再次尝试。

4. **多维度评分** —— 每个模型在四个维度（每项 0–100）上进行评分：

   | 维度       | 衡量内容                                                               |
   |-------------|--------------------------------------------------------------------------------|
   | **质量 (Quality)** | 参数量、模型家族声誉、量化惩罚、任务对齐度 |
   | **速度 (Speed)**   | 基于后端、参数量和量化的预估每秒 token 数                |
   | **适配度 (Fit)**     | 内存利用率效率（甜点区：可用内存的 50–80%）         |
   | **上下文 (Context)** | 上下文窗口能力 vs 用例目标                           |

   各维度按用例类别（通用、编程、推理、对话、多模态、嵌入）赋予不同权重后合并为综合得分。例如，对话类给速度更高权重（0.35），而推理类给质量更高权重（0.55）。模型按综合得分排序，无法运行的模型（Too Tight/太紧）始终排在末尾。

5. **速度估算** —— LLM 推理中的 token 生成受限于内存带宽：每个 token 都需要从显存中完整读取一次模型权重。当识别到显卡型号时，llmfit 会使用其实际内存带宽来估算吞吐量：

   公式：`(带宽_GB_s / 模型大小_GB) × 效率因子`

   效率因子（0.55）及各模式速度乘数可通过高级配置弹窗（TUI 中按 `A`）调整。默认值已考虑内核开销、KV-cache 读取及内存控制器影响。该方法经 llama.cpp 官方基准测试 ([Apple Silicon](https://github.com/ggml-org/llama.cpp/discussions/4167), [NVIDIA T4](https://github.com/ggml-org/llama.cpp/discussions/4225)) 及实际测量验证。

   带宽查找表覆盖约 80 款显卡，涵盖 NVIDIA（消费级+数据中心）、AMD（RDNA + CDNA）和 Apple Silicon 系列。

   对于未识别的显卡，llmfit 会回退到各后端的固定速度常数：

   | 后端         | 速度常数 |
   |--------------|----------------|
   | CUDA         | 220            |
   | Metal        | 160            |
   | ROCm         | 180            |
   | SYCL         | 100            |
   | CPU (ARM)    | 90             |
   | CPU (x86)    | 70             |
   | NPU (昇腾) | 390            |

   回退公式：`K / params_b × quant_speed_multiplier`，各模式惩罚系数可通过高级配置弹窗（按 `A`）调整。

6. **适配分析** —— 评估每个模型的内存兼容性：

   **运行模式：**
   - **GPU** —— 模型完全放入显存。推理速度快。
   - **MoE** —— 混合专家架构配合专家卸载。激活的专家在显存中，未激活的在内存中。
   - **CPU+GPU** —— 显存不足，部分权重溢出至系统内存并配合 GPU 卸载。
   - **CPU** —— 无 GPU。模型完全加载至系统内存。

   **适配等级：**
   - **完美 (Perfect)** —— 满足推荐显存/内存要求（需 GPU 加速）。
   - **良好 (Good)** —— 有充足余量。MoE 卸载或 CPU+GPU 模式下最佳可实现状态。
   - **边缘 (Marginal)** —— 适配紧凑，或仅支持纯 CPU 执行（CPU-only 始终归于此档）。
   - **太紧 (Too Tight)** —— 显存或系统内存均不足，无法运行。

---

## 模型数据库

模型列表由 `scripts/scrape_hf_models.py` 生成，这是一个独立的 Python 脚本（仅使用标准库，无 pip 依赖），通过查询 HuggingFace REST API 获取。涵盖数百个模型与提供商，包括 Meta Llama、Mistral、Qwen、Google Gemma、Microsoft Phi、DeepSeek、IBM Granite、Allen Institute OLMo、xAI Grok、Cohere、BigCode、01.ai、Upstage、TII Falcon、HuggingFace、Zhipu GLM、Moonshot Kimi、Baidu ERNIE 等。爬虫会自动通过模型配置（`num_local_experts`, `num_experts_per_tok`）及已知架构映射检测 MoE 架构。

模型类别涵盖通用、编程（CodeLlama, StarCoder2, WizardCoder, Qwen2.5-Coder, Qwen3-Coder）、推理（DeepSeek-R1, Orca-2）、多模态/视觉（Llama 3.2 Vision, Llama 4 Scout/Maverick, Qwen2.5-VL）、对话、企业级（IBM Granite）及嵌入（nomic-embed, bge）。

完整列表见 [MODELS.md](MODELS.md)。

模型数据库在编译时嵌入，因此**终端用户**只需升级 llmfit 自身（`brew upgrade llmfit`、`scoop update llmfit` 或下载新版发行版）即可获取更新。以下命令仅供**贡献者**从源码刷新数据库使用：

要刷新模型数据库：

```sh
# 自动化更新（推荐）
make update-models

# 或直接运行脚本
./scripts/update_models.sh

# 或手动执行
python3 scripts/scrape_hf_models.py
cargo build --release
```

爬虫会写入 `data/hf_models.json`，并通过 `include_str!` 编译进二进制文件。自动化更新脚本会备份现有数据、验证 JSON 输出并重新构建二进制文件。

默认情况下，爬虫会从 [unsloth](https://huggingface.co/unsloth) 和 [bartowski](https://huggingface.co/bartowski) 等提供商处获取已知的 GGUF 下载源以丰富模型数据。结果会缓存至 `data/gguf_sources_cache.json`（7天 TTL）以避免重复调用 API。使用 `--no-gguf-sources` 可跳过此步骤以获得更快的抓取速度。

---

## 项目结构

```
src/
  main.rs         -- CLI 参数解析、入口点、TUI 启动
  hardware.rs     -- 系统内存/CPU/GPU 检测（多显卡、后端识别）
  models.rs       -- 模型数据库、量化层级、动态量化选择
  fit.rs          -- 多维度评分（Q/S/F/C）、速度估算、MoE 卸载
  providers.rs    -- 运行时提供商集成（Ollama、llama.cpp、MLX、Docker Model Runner、LM Studio）、安装检测、拉取/下载
  display.rs      -- 经典 CLI 表格渲染 + JSON 输出
  tui_app.rs      -- TUI 应用状态、过滤器、导航逻辑
  tui_ui.rs       -- TUI 渲染（ratatui）
  tui_events.rs   -- TUI 键盘事件处理（crossterm）
data/
  hf_models.json  -- 模型数据库（206 个模型）
skills/
  llmfit-advisor/ -- OpenClaw Skill，用于提供硬件感知的模型推荐
scripts/
  scrape_hf_models.py        -- HuggingFace API 爬虫脚本
  update_models.sh            -- 自动化数据库更新脚本
  install-openclaw-skill.sh   -- 安装 OpenClaw Skill
Makefile           -- 构建与维护命令
```

---

## 发布到 crates.io

`Cargo.toml` 已包含所需元数据（描述、许可证、仓库地址）。要发布：

```sh
# 先进行 Dry Run 以检查问题
cargo publish --dry-run

# 正式发布（需要 crates.io API Token）
cargo login
cargo publish
```

发布前请确保：

- `Cargo.toml` 中的版本号正确（每次发行时递增）。
- 仓库根目录存在 `LICENSE` 文件。若缺失可创建：

```sh
# MIT 许可证：
curl -sL https://opensource.org/license/MIT -o LICENSE
# 或自行编写。Cargo.toml 中已声明 license = "MIT"。
```

- `data/hf_models.json` 已提交。该文件在编译时嵌入，必须存在于发布的 crate 中。

发布更新：

```sh
# 递增版本号
# 编辑 Cargo.toml: version = "0.2.0"
cargo publish
```

---

## 依赖项

| Crate                  | 用途                                          |
|------------------------|--------------------------------------------------|
| `clap`                 | 基于 derive macro 的 CLI 参数解析          |
| `sysinfo`              | 跨平台内存和 CPU 检测             |
| `serde` / `serde_json` | JSON 反序列化（用于模型数据库）          |
| `tabled`               | CLI 表格格式化                             |
| `colored`              | CLI 彩色输出                               |
| `ureq`                 | HTTP 客户端（用于运行时/提供商 API 集成） |
| `ratatui`              | 终端 UI 框架                            |
| `crossterm`            | ratatui 的终端输入/输出后端        |

---

## 运行时提供商集成

llmfit 支持多种本地运行时提供商：

- **Ollama**（基于守护进程/API 拉取）
- **llama.cpp**（直接从 HuggingFace 下载 GGUF + 本地缓存检测）
- **MLX**（Apple Silicon / mlx-community 模型缓存 + 可选服务器）—— MLX 下载映射至 HuggingFace 上的 `mlx-community/*` 仓库，而非原始发布者
- **Docker Model Runner**（Docker Desktop 内置的模型服务功能）
- **LM Studio**（本地模型服务器，提供 REST API 用于模型管理与下载）

当模型有多个兼容的可用提供商时，在 TUI 中按 `d` 会弹出提供商选择器。

### Ollama 集成

llmfit 与 [Ollama](https://ollama.com) 深度集成，可检测你已安装的模型并直接从 TUI 下载新模型。

#### 环境要求
- **必须安装且正在运行 Ollama**（通过 `ollama serve` 或桌面客户端）
- llmfit 默认连接 `http://localhost:11434`（Ollama 的默认 API 端口）
- 无需额外配置——只要 Ollama 在运行，llmfit 即可自动检测

#### 远程 Ollama 实例
要连接运行在其他机器或端口上的 Ollama，请设置 `OLLAMA_HOST` 环境变量：

```sh
# 连接到指定 IP 和端口的 Ollama
OLLAMA_HOST="http://192.168.1.100:11434" llmfit

# 通过主机名连接  
OLLAMA_HOST="http://ollama-server:666" llmfit

# 适用于所有 TUI 和 CLI 命令
OLLAMA_HOST="http://192.168.1.100:11434" llmfit --cli
OLLAMA_HOST="http://192.168.1.100:11434" llmfit fit --perfect -n 5
```

此功能适用于以下场景：
- 在一台机器上运行 llmfit，而 Ollama 在另一台（如 GPU 服务器+笔记本客户端）提供服务
- 连接使用自定义端口的 Docker 容器内的 Ollama
- 通过反向代理或负载均衡器访问 Ollama

#### 工作原理
启动时，llmfit 会查询 `GET /api/tags` 以列出你已安装的 Ollama 模型。每个已安装模型在 TUI 的 **Inst** 列中显示绿色 **✓**。状态栏会显示 `Ollama: ✓ (N installed)`。

选中模型并按 `d` 时，llmfit 会向 Ollama 发送 `POST /api/pull` 以下载该模型。该行会高亮显示并带有动态进度指示器，实时展示下载进度。完成后，模型立即可用于 Ollama。

若 Ollama 未运行，将跳过相关操作；TUI 仍支持其他可用提供商（如 llama.cpp）。

### llama.cpp 集成

llmfit 在 TUI 和 CLI 中均与 [llama.cpp](https://github.com/ggml-org/llama.cpp) 集成作为运行时/下载提供商。

要求：
- `llama-cli` 或 `llama-server` 需在 `PATH` 中可用（用于运行时检测）
- 需具备访问 HuggingFace 的网络权限以下载 GGUF 文件

工作原理：
- llmfit 将 HF 模型映射至已知的 GGUF 仓库（支持启发式回退）
- 将 GGUF 文件下载至本地 llama.cpp 模型缓存目录
- 当本地存在匹配的 GGUF 文件时，标记为已安装

#### 环境变量
| 变量 | 默认值 | 描述 |
|---|---|---|
| `LLAMA_CPP_PATH` | *(无)* | 包含 llama.cpp 二进制文件的目录（`llama-cli`, `llama-server`）。优先于系统 `PATH` 查找。 |
| `LLAMA_SERVER_PORT` | `8080` | 探测运行中的 `llama-server` 健康端点以进行运行时检测时使用的端口。 |

若 llama.cpp 安装在非标准路径下，请设置 `LLAMA_CPP_PATH` 以便 llmfit 定位，无需将其加入系统 `PATH`。

### Docker Model Runner 集成

llmfit 与 [Docker Model Runner](https://docs.docker.com/desktop/features/model-runner/)（Docker Desktop 内置的模型服务功能）集成。

要求：
- 启用 Model Runner 功能的 Docker Desktop
- 默认端点：`http://localhost:12434`

工作原理：
- llmfit 查询 `GET /engines` 以列出 Docker Model Runner 中可用的模型
- 使用类 Ollama 的标签映射将模型匹配至 HF 数据库（Docker Model Runner 采用 `ai/<tag>` 命名规范）
- 在 TUI 中按 `d` 会通过 `docker model pull` 拉取模型

#### 远程 Docker Model Runner 实例
要连接其他主机或端口上的 Docker Model Runner，请设置 `DOCKER_MODEL_RUNNER_HOST` 环境变量：

```sh
DOCKER_MODEL_RUNNER_HOST="http://192.168.1.100:12434" llmfit
```

### LM Studio 集成

llmfit 与 [LM Studio](https://lmstudio.ai)（内置模型下载功能的本地模型服务器）集成。

要求：
- 必须运行 LM Studio 并启用本地服务器功能
- 默认端点：`http://127.0.0.1:1234`

工作原理：
- llmfit 查询 `GET /v1/models` 以列出 LM Studio 中可用的模型
- 在 TUI 中按 `d` 会通过 `POST /api/v1/models/download` 触发下载
- 通过轮询 `GET /api/v1/models/download-status` 跟踪下载进度
- LM Studio 直接接受 HuggingFace 模型名称，因此无需进行名称映射

#### 远程 LM Studio 实例
要连接其他主机或端口上的 LM Studio，请设置 `LMSTUDIO_HOST` 环境变量：

```sh
LMSTUDIO_HOST="http://192.168.1.100:1234" llmfit
```

### 模型名称映射

llmfit 数据库使用 HuggingFace 模型名称（如 `Qwen/Qwen2.5-Coder-14B-Instruct`），而 Ollama 采用其自身的命名规范（如 `qwen2.5-coder:14b`）。llmfit 维护了两者之间精确的映射表，以确保安装检测和拉取操作能正确解析到对应模型。每个映射均为严格一对一——例如 `qwen2.5-coder:14b` 仅映射至 Coder 系列模型，而非基础的 `qwen2.5:14b`。

---

## 平台支持

- **Linux** —— 完整支持。显卡检测通过 `nvidia-smi`（NVIDIA）、`rocm-smi`（AMD）、sysfs/`lspci`（Intel Arc）和 `npu-smi`（昇腾）。
- **macOS (Apple Silicon)** —— 完整支持。通过 `system_profiler` 检测统一内存。显存等于系统总内存（共享池）。模型通过 Metal GPU 加速运行。
- **macOS (Intel)** —— 内存和 CPU 检测正常。若安装 `nvidia-smi` 可检测独立显卡。
- **Windows** —— 内存和 CPU 检测正常。若已安装，可通过 `nvidia-smi` 检测 NVIDIA 显卡。
- **Android / Termux / PRoot** —— CPU 和内存检测通常可用，但目前不支持 GPU 自动检测。移动 GPU（如 Adreno）通常无法通过 llmfit 使用的桌面/服务器探测接口可见。

### 显卡支持

| 厂商                 | 检测方法              | 显存报告                 |
|------------------------|-------------------------------|--------------------------------|
| NVIDIA                 | `nvidia-smi`                  | 精确独立显存           |
| AMD                    | `rocm-smi`                    | 已检测（显存可能未知） |
| Intel Arc (独立)   | sysfs (`mem_info_vram_total`) | 精确独立显存           |
| Intel Arc (核显) | `lspci`                       | 共享系统内存           |
| Apple Silicon          | `system_profiler`             | 统一内存 (= 系统总内存)  |
| Ascend                 | `npu-smi`                     | 已检测（显存可能未知） |

若自动检测失败或报告值不正确，请使用 `--memory`、`--ram` 或 `--cpu-cores` 进行覆盖（见上方 [硬件参数覆盖](#hardware-overrides)）。

### Android / Termux 注意事项
在 **Termux + PRoot** 等 Android 环境中，llmfit 通常无法通过标准 Linux 检测路径（`nvidia-smi`、`rocm-smi`、DRM/sysfs、`lspci` 等）识别移动 GPU。在当前实现下，“未检测到显卡”属正常现象。

若仍希望在统一内存手机或平板上获得类显卡推荐，请使用手动内存覆盖：

```sh
llmfit --memory=8G fit -n 20
llmfit recommend --json --memory=8G --limit 10
```

此方法仅用于推荐/评分的临时替代方案；它不提供真正的 Android GPU 运行时检测功能。

---

## 贡献指南

欢迎提交贡献，尤其是新增模型。

### 提交 PR 前
请在推送更改前运行 `cargo fmt`。大多数 CI 检查失败均由代码未格式化引起：

```sh
cargo fmt
```

### 添加模型
1. 将模型的 HuggingFace 仓库 ID（如 `meta-llama/Llama-3.1-8B`）添加到 `scripts/scrape_hf_models.py` 中的 `TARGET_MODELS` 列表。
2. 若模型需要权限验证（需 HuggingFace 认证才能访问元数据），请在同一脚本的 `FALLBACKS` 列表中补充回退条目，包含参数量和上下文长度。
3. 运行自动化更新脚本：
   ```sh
   make update-models
   # 或: ./scripts/update_models.sh
   ```
4. 验证更新的模型列表：`./target/release/llmfit list`
5. 通过运行 `python3 << 'EOF' < scripts/...` 更新 [MODELS.md](MODELS.md)（生成脚本见提交历史）
6. 提交 Pull Request。

当前列表详见 [MODELS.md](MODELS.md)，架构细节见 [AGENTS.md](AGENTS.md)。

---

## OpenClaw 集成

llmfit 附带一个 [OpenClaw](https://github.com/openclaw/openclaw) Skill，使 Agent 能够推荐适配硬件的本地模型并自动配置 Ollama/vLLM/LM Studio 提供商。

### 安装 Skill
```sh
# 从 llmfit 仓库安装
./scripts/install-openclaw-skill.sh

# 或手动安装
cp -r skills/llmfit-advisor ~/.openclaw/skills/
```

安装完成后，你可向你的 OpenClaw Agent 提问：
- “我可以运行哪些本地模型？”
- “为我的硬件推荐一个编程模型”
- “使用最适合我显卡的模型配置 Ollama”

Agent 会在后台调用 `llmfit recommend --json`，解析结果后提供建议，并询问你是否将最优模型选择写入你的 `openclaw.json`。

### 工作原理
该 Skill 教导 OpenClaw Agent 执行以下操作：
1. 通过 `llmfit --json system` 检测你的硬件
2. 通过 `llmfit recommend --json` 获取排序后的推荐列表
3. 将 HuggingFace 模型名称映射为 Ollama/vLLM/LM Studio 标签
4. 配置 `openclaw.json` 中的 `models.providers.ollama.models`

完整 Skill 定义见 [skills/llmfit-advisor/SKILL.md](skills/llmfit-advisor/SKILL.md)。

---

## 替代方案

如果你寻求不同的方案，可尝试 [llm-checker](https://github.com/Pavelevich/llm-checker) ——一款集成 Ollama 的 Node.js CLI 工具，可直接拉取并基准测试模型。它采用更直接的方式：通过 Ollama 在你的硬件上实际运行模型进行测试，而非仅依赖规格估算。如果你已安装 Ollama 并希望实测性能表现，这是一个不错的选择。注意：该工具不支持 MoE（混合专家）架构——所有模型均被视为稠密模型，因此对 Mixtral 或 DeepSeek-V3 等模型的内存估算将反映总参数量，而非实际激活的子集大小。

---

## 许可证

MIT