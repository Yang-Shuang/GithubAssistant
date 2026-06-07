<div align="center">

<img src="assets/images/bar.jpg" width="880" alt="GenericAgent Banner"/>

# GenericAgent

**一个极简、可自我进化的自主 Agent 框架**

*约 3K 行种子代码 · 9 个原子工具 · 约百行的 Agent Loop*

<p>

  <a href="https://arxiv.org/abs/2604.17091"><img src="https://img.shields.io/badge/Technical_Report-PDF-EA4335?style=flat-square&logo=adobeacrobatreader&logoColor=white" alt="Technical Report"/></a>
  <a href="https://github.com/JinyiHan99/GA-Technical-Report"><img src="https://img.shields.io/badge/Code_%26_Data-Reproduction-181717?style=flat-square&logo=github" alt="Reproduction Repo"/></a>
  <a href="https://datawhalechina.github.io/hello-generic-agent/"><img src="https://img.shields.io/badge/Tutorial-Datawhale-blue?style=flat-square" alt="Tutorial"/></a>
  <a href="https://fudankw.cn/sophub"><img src="https://img.shields.io/badge/Skill_Hub-Sophub-purple?style=flat-square" alt="Sophub"/></a>
</p>

<p>
  <a href="https://trendshift.io/repositories/25944" target="_blank"><img src="https://trendshift.io/api/badge/repositories/25944" alt="Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

**[English](#-english) · [中文](#-中文)**

</div>

> 📌 **官方频道** — GitHub 仓库是 GenericAgent 的**唯一**官方来源。
> 我们不与任何使用 GenericAgent 名称的第三方网站有关联。

---

<a id="-english"></a>

## 🌟 项目简介

**GenericAgent** 是一个极简、可自我进化的自主 Agent 框架。核心仅 **约 3K 行代码**，通过 **9 个原子工具 + 约百行的 Agent Loop**，赋予任意 LLM 对本地计算机的系统级控制能力，覆盖浏览器、终端、文件系统、键鼠输入、屏幕视觉及移动设备（ADB）。

> 设计哲学 —— **不预设技能，靠进化获得能力。**

每解决一个新任务，GenericAgent 就将执行路径自动固化为 Skill，供后续直接调用。使用时间越长，沉淀的技能越多，形成一棵完全属于你、从 3K 行种子代码生长出来的专属技能树。

> 🤖 **自举实证** — 本仓库的一切，从安装 Git、`git init` 到每一条 commit message，均由 GenericAgent 自主完成。作者全程未打开过一次终端。

### 📑 目录

- [核心特性](#-核心特性)
- [实例展示](#-实例展示)
- [快速开始](#-快速开始)
- [使用方式](#-使用方式)
- [架构设计](#-架构设计)
- [自我进化机制](#-自我进化机制)
- [与同类产品对比](#-与同类产品对比)
- [评测](#-评测)
- [路线图与最新动态](#-路线图与最新动态)
- [社区与支持](#-社区与支持)
- [许可](#-许可)

---

## 📋 核心特性

| 特性 | 说明 |
| :--- | :--- |
| 🧬 **自我进化** | 每次任务自动沉淀 Skill，能力随使用持续增长，形成专属技能树 |
| 🪶 **极简架构** | ~3K 行核心代码，Agent Loop 约百行，无复杂依赖，部署零负担 |
| ⚡ **强执行力** | 注入真实浏览器（保留登录态），9 个原子工具直接接管系统 |
| 🔌 **高兼容性** | 支持 Claude / Gemini / Kimi / MiniMax 等主流模型，跨平台运行 |
| 💰 **极致省 Token** | 上下文窗口不到 30K，是其他 Agent（200K–1M）的零头；噪声更少、幻觉更低、成功率更高，成本低一个数量级 |

---

## 🎯 实例展示

<table>
  <tr>
    <td align="center" width="50%"><b>🧋 外卖下单</b></td>
    <td align="center" width="50%"><b>📈 量化选股</b></td>
  </tr>
  <tr>
    <td><img src="assets/demo/order_tea.gif" width="100%" alt="外卖下单"></td>
    <td><img src="assets/demo/selectstock.gif" width="100%" alt="量化选股"></td>
  </tr>
  <tr>
    <td><sub><i>"Order me a milk tea"</i> — 自动导航外卖 App，选品并完成结账</sub></td>
    <td><sub><i>"Find GEM stocks with EXPMA golden cross, turnover &gt; 5%"</i> — 量化条件筛股</sub></td>
  </tr>
  <tr>
    <td align="center"><b>🌐 自主网页探索</b></td>
    <td align="center"><b>💰 支出追踪</b></td>
  </tr>
  <tr>
    <td><img src="assets/demo/autonomous_explore.png" width="100%" alt="网页探索"></td>
    <td><img src="assets/demo/alipay_expense.png" width="100%" alt="支付宝支出"></td>
  </tr>
  <tr>
    <td><sub>自主浏览并定时汇总网页信息</sub></td>
    <td><sub><i>"查找近 3 个月超 ¥2K 的支出"</i> — 通过 ADB 驱动支付宝</sub></td>
  </tr>
  <tr>
    <td align="center" colspan="2"><b>💬 批量消息</b></td>
  </tr>
  <tr>
    <td colspan="2" align="center"><img src="assets/demo/wechat_batch.png" width="50%" alt="微信批量"></td>
  </tr>
  <tr>
    <td colspan="2"><sub>批量发送微信消息，完整驱动微信客户端</sub></td>
  </tr>
</table>

---

## 🚀 快速开始

> ⚠️ **Python 版本：** 推荐使用 **Python 3.11 或 3.12**。**请不要使用 Python 3.14**，与 `pywebview` 及部分依赖不兼容。
>
> 📖 详细安装指南：**[installation_zh.md（中文）](docs/installation_zh.md)** · **[installation.md (English)](docs/installation.md)**

### 给 LLM Agent 看的

获取安装指南并照做：

```bash
curl -fsSL https://raw.githubusercontent.com/lsdefine/GenericAgent/refs/heads/main/docs/installation_zh.md
```

### 给人类用户看的

#### 方法一 — 一键安装 *（推荐）*

一键安装会自动准备独立 Python 环境、Git、项目文件和桌面端，不污染系统环境。

**Windows PowerShell**

```powershell
powershell -ExecutionPolicy Bypass -c "irm http://fudankw.cn:9000/files/ga_install.ps1 | iex"
```

**Linux / macOS**

```bash
curl -fsSL http://fudankw.cn:9000/files/ga_install.sh | bash
```

安装完成后，双击启动：

```text
frontends/GenericAgent.exe
```

#### 方法二 — Python 安装 *（开发者）*

```bash
git clone https://github.com/lsdefine/GenericAgent.git
cd GenericAgent
uv venv
uv pip install -e ".[ui]"          # 核心 + UI 依赖
cp mykey_template.py mykey.py      # 填入你的 LLM API Key
python launch.pyw
```

> 💡 GenericAgent 更推荐由 **Agent 在使用中自举环境**，而不是预先手动装完整依赖。

📖 完整引导流程见 [`docs/GETTING_STARTED.md`](docs/GETTING_STARTED.md)
📖 新手图文版：[飞书文档](https://my.feishu.cn/wiki/CGrDw0T76iNFuskmwxdcWrpinPb)
📘 完整入门教程（Datawhale 出品）：[Hello GenericAgent](https://datawhalechina.github.io/hello-generic-agent/) · [GitHub](https://github.com/datawhalechina/hello-generic-agent)

---

## 💻 使用方式

### 前端启动

#### 桌面端

一键安装自带桌面端，双击：

```text
frontends/GenericAgent.exe
```

#### 终端 UI

基于 [Textual](https://github.com/Textualize/textual) 的轻量键盘驱动界面。支持多会话并发、实时流式输出，有终端就能跑。

```bash
python frontends/tuiapp_v2.py
```

<details>
<summary><b>⚠️ Windows 上 TUI 显示异常的排查思路</b></summary>

1. `textual` 版本太旧，先 `pip install -U textual`；
2. PowerShell / cmd 自带终端对 Unicode 和键位的支持比较糟糕，**Windows 上推荐用 Git Bash**，体验明显更稳；
3. 仍然显示异常时，可以让 GA 自己修一遍，参考 Prompt：
   > *"我在 Windows 的 PowerShell / cmd / Git Bash 中使用 `frontends/tuiapp_v2.py` 体验非常差，出现了一堆不兼容问题。请参考 Claude Code 在 Windows 终端的最佳配置，把所有字体和显示不兼容的问题修一遍。"*

</details>

#### Streamlit UI

```bash
python launch.pyw
```

### Bot 接口（IM）

GenericAgent 支持 Telegram、微信、QQ、飞书 / Lark、企业微信、钉钉等 IM 前端。

| 平台 | 启动命令 |
| :--- | :--- |
| Telegram | `python frontends/tgapp.py` |
| 微信 | `python frontends/wechatapp.py` |
| QQ | `python frontends/qqapp.py` |
| 飞书 / Lark | `python frontends/fsapp.py` |
| 企业微信 | `python frontends/wecomapp.py` |
| 钉钉 | `python frontends/dingtalkapp.py` |

> 详细配置直接问 GenericAgent。

### 通用聊天命令

| 命令 | 说明 |
| :--- | :--- |
| `/new` | 开启新对话并清空当前上下文 |
| `/continue` | 列出可恢复会话快照 |
| `/continue N` | 恢复第 `N` 个可恢复会话 |

---

## 🧠 架构设计

GenericAgent 通过 **分层记忆 × 最小工具集 × 自主执行循环** 完成复杂任务，并在执行过程中持续积累经验。

### 1️⃣ 分层记忆系统

> *记忆在任务执行过程中持续沉淀，使 Agent 逐步形成稳定且高效的工作方式。*

| 层级 | 名称 | 说明 |
| :---: | :--- | :--- |
| **L0** | 元规则（Meta Rules） | Agent 的基础行为规则和系统约束 |
| **L1** | 记忆索引（Insight Index） | 极简索引层，用于快速路由与召回 |
| **L2** | 全局事实（Global Facts） | 在长期运行过程中积累的稳定知识 |
| **L3** | 任务 Skills / SOPs | 完成特定任务类型的可复用流程 |
| **L4** | 会话归档（Session Archive） | 从已完成任务中提炼出的归档记录，用于长程召回 |

### 2️⃣ 自主执行循环

> *感知环境状态 → 任务推理 → 调用工具执行 → 经验写入记忆 → 循环*

整个核心循环仅 **约百行代码**（[`agent_loop.py`](agent_loop.py)）。

### 3️⃣ 最小工具集

> *GenericAgent 仅提供 **9 个原子工具**，构成与外部世界交互的基础能力。*

| 工具 | 功能 |
| :--- | :--- |
| `code_run` | 执行任意代码（Python / PowerShell） |
| `file_read` | 读取文件 |
| `file_write` | 写入 / 创建 / 覆盖文件 |
| `file_patch` | 修改文件 |
| `web_scan` | 感知网页内容 |
| `web_execute_js` | 控制浏览器行为 |
| `ask_user` | 人机协作确认 |
| `update_working_checkpoint` | *（记忆）* 短期工作记事板 |
| `start_long_term_update` | *（记忆）* 提炼长期记忆 |

### 4️⃣ 能力扩展机制

> *具备动态创建新工具的能力。*

通过 `code_run`，GenericAgent 可在运行时动态安装 Python 包、编写新脚本、调用外部 API 或控制硬件，将临时能力固化为永久工具。

<div align="center">
  <img src="assets/images/workflow.jpg" alt="GenericAgent 工作流程" width="420"/>
  <br/><em>GenericAgent 工作流程图</em>
</div>

---

## 🧬 自我进化机制

这是 GenericAgent 区别于其他 Agent 框架的根本所在。

```text
[遇到新任务]
    │
    ▼
[自主摸索]   ─►  安装依赖 · 编写脚本 · 调试验证
    │
    ▼
[执行路径固化为 Skill]   ─►  写入记忆层
    │
    ▼
[下次同类任务直接调用]
```

| 你说的一句话 | 第一次做了什么 | 之后每次 |
| :--- | :--- | :--- |
| *"监控股票并提醒我"* | 安装 `mootdx` → 构建选股流程 → 配置定时任务 → 保存 Skill | **一句话启动** |
| *"用 Gmail 发这个文件"* | 配置 OAuth → 编写发送脚本 → 保存 Skill | **直接可用** |

用几周后，你的 Agent 实例将拥有一套任何人都没有的专属技能树，全部从 3K 行种子代码中生长而来。

---

## 📊 与同类产品对比

| 特性 | **GenericAgent** | OpenClaw | Claude Code |
| :--- | :---: | :---: | :---: |
| **代码量** | ~3K 行 | ~530,000 行 | 已开源（体量大） |
| **部署方式** | `pip install` + API Key | 多服务编排 | CLI + 订阅 |
| **浏览器控制** | 注入真实浏览器（保留登录态） | 沙箱 / 无头浏览器 | 通过 MCP 插件 |
| **OS 控制** | 键鼠、视觉、ADB | 多 Agent 委派 | 文件 + 终端 |
| **自我进化** | 自主生长 Skill 和工具 | 插件生态 | 会话间无状态 |
| **出厂配置** | 几个核心文件 + 少量初始 Skills | 数百模块 | 丰富 CLI 工具集 |

---

## 📈 评测

> 📂 完整的评测数据集以及评测结果见：[**JinyiHan99/GA-Technical-Report**](https://github.com/JinyiHan99/GA-Technical-Report/tree/main)

我们从 **五大维度** 评测 GenericAgent：

| # | 维度 | 核心问题 | 使用的基准 |
| :---: | :--- | :--- | :--- |
| 1 | **任务完成度与 Token 效率** | GA 能否以更低成本完成高难度任务？ | SOP-Bench、Lifelong AgentBench、RealFin-Benchmark |
| 2 | **工具使用效率** | 最小原子工具集能否以更低开销替代专用工具集？ | Tool Efficiency Benchmark |
| 3 | **记忆系统有效性** | 精简分层记忆能否超越冗余记忆和基于 Embedding 的检索器？ | SOP-Bench、LoCoMo、20-skill 压力测试 |
| 4 | **自我进化能力** | Agent 能否在无人干预下将经验提炼为可复用的 SOP 与代码？ | 9 轮 LangChain 纵向研究、8 任务跨任务 Web 基准 |
| 5 | **网页浏览能力** | 信息密度驱动设计能否适应开放网页？ | WebCanvas、BrowseComp-ZH、自定义任务 |

以上维度的基线包括 **Claude Code**、**OpenAI CodeX** 和 **OpenClaw**，分别在 *Claude Sonnet 4.6*、*Claude Opus 4.6*、*GPT-5.4* 和 *MiniMax M2.7* 底座上进行评测。

<table>
  <tr>
    <td align="center" width="50%">
      <img src="assets/images/result_radar.png" width="100%" alt="工具使用效率雷达图"/><br/>
      <sub><b>工具使用效率雷达图。</b>GA 在 Token、请求数和工具调用轴上全面领先，同时在四个任务维度上保持质量。</sub>
    </td>
    <td align="center" width="50%">
      <img src="assets/images/result_convergence.png" width="100%" alt="跨任务自我进化收敛曲线"/><br/>
      <sub><b>跨任务自我进化。</b>GA 的第二轮和第三轮执行在 8 个 Web 任务上收敛至稳定的低成本区间。</sub>
    </td>
  </tr>
</table>

---

## 📅 路线图与最新动态

- **2026-05-23** — 🆕 **TUI v3 正式发布**（`frontends/tui_v3.py`）。基于块的滚屏回看 + 正确的 resize 重排，每终端独立配色保证跨终端一致，并与 v2 达成功能对齐。
- **2026-05-18** — 🆕 **Morphling 模式**。项目级能力吞噬 —— 从任意外部仓库抽取目标与测例后，对每个核心组件分别决定调用、重写或舍弃。详见 `memory/morphling_sop.md`。
- **2026-05-17** — 🆕 **Goal Hive 模式**。多 worker 协作版 Goal —— Master/Worker 通过 BBS 协同推进长程目标。详见 `memory/goal_hive_sop.md`。
- **2026-05-15** — 🖥️ **桌面 GUI 发布**。一键安装会自带可直接运行的桌面端（`frontends/GenericAgent.exe`），开发者也可用 `python launch.pyw` 启动。
- **2026-05-14** — 🆕 **Conductor 子 Agent 编排**。派发、监督、自动清理并行子 Agent；与 `/btw` 旁路子 Agent 互补，提供一等公民级的任务委派原语。
- **2026-05-12** — 🆕 **TUI v2 正式发布**（`frontends/tuiapp_v2.py`）。重做视觉风格的 Textual 前端，支持图片粘贴折叠、文件粘贴、块删除、Ctrl+C 复制、历史导航，以及 `/llm` / `/export` / `/continue` 选择器。
- **2026-05-08** — 🆕 **Goal 模式**（`reflect/goal_mode.py`）。时间预算驱动的自驱循环 —— "持续优化 X N 小时"，预算没到不准提前交付。
- **2026-04-21** — 📄 [**技术报告已发布至 arXiv**](https://arxiv.org/abs/2604.17091) — *GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization*。
- **2026-04-11** — 引入 **L4 会话归档记忆**，并接入 scheduler cron 调度。
- **2026-03-23** — 支持个人微信接入作为 Bot 前端。
- **2026-03-10** — [发布百万级 Skill 库](https://mp.weixin.qq.com/s/q2gQ7YvWoiAcwxzaiwpuiQ?scene=1&click_id=7)。
- **2026-03-08** — [发布以 GenericAgent 为核心的"政务龙虾" Dintal Claw](https://mp.weixin.qq.com/s/eiEhwo-j6S-WpLxgBnNxBg)。
- **2026-03-01** — [被机器之心报道](https://mp.weixin.qq.com/s/uVWpTTF5I1yzAENV_qm7yg)。
- **2026-01-16** — GenericAgent **V1.0** 公开版本发布。

---

## ⭐ 社区与支持

如果这个项目对你有帮助，欢迎点一个 **Star!** 🙏

也欢迎加入 **GenericAgent 体验交流群**，一起交流、反馈、共建 👏

<div align="center">
  <table>
    <tr>
      <td align="center"><strong>微信群 20</strong><br/><img src="assets/images/wechat_group20.jpg" alt="微信群 20 二维码" width="240"/></td>
    </tr>
  </table>
</div>

### 🚩 友情链接

感谢 **LinuxDo** 社区的支持！

[![LinuxDo](https://img.shields.io/badge/社区-LinuxDo-blue?style=for-the-badge)](https://linux.do/)

**社区 GUI 客户端** *（独立开源项目）*：

- [chilishark27/ga-manager](https://github.com/chilishark27/ga-manager)
- [wangjc683/galley](https://github.com/wangjc683/galley)
- [FroStorM/A3Agent](https://github.com/FroStorM/A3Agent/tree/workbench)

---

## 📄 许可

基于 **MIT License** 发布，详见 [`LICENSE`](LICENSE)。

> *声明：本项目未构建任何商业站点；除 DintalClaw 外，目前未官方授权任何机构、组织或个人以 GenericAgent 名义从事商业活动。*

---

<a id="-中文"></a>

## 🌟 项目简介

**GenericAgent** 是一个极简、可自我进化的自主 Agent 框架。核心仅 **~3K 行代码**，通过 **9 个原子工具 + ~100 行 Agent Loop**，赋予任意 LLM 对本地计算机的系统级控制能力，覆盖浏览器、终端、文件系统、键鼠输入、屏幕视觉及移动设备（ADB）。

> 设计哲学 —— **不预设技能，靠进化获得能力。**

每解决一个新任务，GenericAgent 就将执行路径自动固化为 Skill，供后续直接调用。使用时间越长，沉淀的技能越多，形成一棵完全属于你、从 3K 行种子代码生长出来的专属技能树。

> 🤖 **自举实证** — 本仓库的一切，从安装 Git、`git init` 到每一条 commit message，均由 GenericAgent 自主完成。作者全程未打开过一次终端。

### 📑 目录

- [核心特性](#-核心特性)
- [实例展示](#-实例展示)
- [快速开始](#-快速开始)
- [使用方式](#-使用方式)
- [架构设计](#-架构设计)
- [自我进化机制](#-自我进化机制)
- [与同类产品对比](#-与同类产品对比)
- [评测](#-评测)
- [路线图与最新动态](#-路线图与最新动态)
- [社区与支持](#-社区与支持)
- [许可](#-许可)

---

## 📋 核心特性

| 特性 | 说明 |
| :--- | :--- |
| 🧬 **自我进化** | 每次任务自动沉淀 Skill，能力随使用持续增长，形成专属技能树 |
| 🪶 **极简架构** | ~3K 行核心代码，Agent Loop 约百行，无复杂依赖，部署零负担 |
| ⚡ **强执行力** | 注入真实浏览器（保留登录态），9 个原子工具直接接管系统 |
| 🔌 **高兼容性** | 支持 Claude / Gemini / Kimi / MiniMax 等主流模型，跨平台运行 |
| 💰 **极致省 Token** | 上下文窗口不到 30K，是其他 Agent（200K–1M）的零头；噪声更少、幻觉更低、成功率更高，成本低一个数量级 |

---

## 🎯 实例展示

<table>
  <tr>
    <td align="center" width="50%"><b>🧋 外卖下单</b></td>
    <td align="center" width="50%"><b>📈 量化选股</b></td>
  </tr>
  <tr>
    <td><img src="assets/demo/order_tea.gif" width="100%" alt="外卖下单"></td>
    <td><img src="assets/demo/selectstock.gif" width="100%" alt="量化选股"></td>
  </tr>
  <tr>
    <td><sub><i>"Order me a milk tea"</i> — 自动导航外卖 App，选品并完成结账</sub></td>
    <td><sub><i>"Find GEM stocks with EXPMA golden cross, turnover &gt; 5%"</i> — 量化条件筛股</sub></td>
  </tr>
  <tr>
    <td align="center"><b>🌐 自主网页探索</b></td>
    <td align="center"><b>💰 支出追踪</b></td>
  </tr>
  <tr>
    <td><img src="assets/demo/autonomous_explore.png" width="100%" alt="网页探索"></td>
    <td><img src="assets/demo/alipay_expense.png" width="100%" alt="支付宝支出"></td>
  </tr>
  <tr>
    <td><sub>自主浏览并定时汇总网页信息</sub></td>
    <td><sub><i>"查找近 3 个月超 ¥2K 的支出"</i> — 通过 ADB 驱动支付宝</sub></td>
  </tr>
  <tr>
    <td align="center" colspan="2"><b>💬 批量消息</b></td>
  </tr>
  <tr>
    <td colspan="2" align="center"><img src="assets/demo/wechat_batch.png" width="50%" alt="微信批量"></td>
  </tr>
  <tr>
    <td colspan="2"><sub>批量发送微信消息，完整驱动微信客户端</sub></td>
  </tr>
</table>

---

## 🚀 快速开始

> ⚠️ **Python 版本：** 推荐使用 **Python 3.11 或 3.12**。**请不要使用 Python 3.14**，与 `pywebview` 及部分依赖不兼容。
>
> 📖 详细安装指南：**[installation_zh.md（中文）](docs/installation_zh.md)** · **[installation.md (English)](docs/installation.md)**

### 给 LLM Agent 看的

获取安装指南并照做：

```bash
curl -fsSL https://raw.githubusercontent.com/lsdefine/GenericAgent/refs/heads/main/docs/installation_zh.md
```

### 给人类用户看的

#### 方法一 — 一键安装 *（推荐）*

一键安装会自动准备独立 Python 环境、Git、项目文件和桌面端，不污染系统环境。

**Windows PowerShell**

```powershell
powershell -ExecutionPolicy Bypass -c "irm http://fudankw.cn:9000/files/ga_install.ps1 | iex"
```

**Linux / macOS**

```bash
curl -fsSL http://fudankw.cn:9000/files/ga_install.sh | bash
```

安装完成后，双击启动：

```text
frontends/GenericAgent.exe
```

#### 方法二 — Python 安装 *（开发者）*

```bash
git clone https://github.com/lsdefine/GenericAgent.git
cd GenericAgent
uv venv
uv pip install -e ".[ui]"          # 核心 + UI 依赖
cp mykey_template.py mykey.py      # 填入你的 LLM API Key
python launch.pyw
```

> 💡 GenericAgent 更推荐由 **Agent 在使用中自举环境**，而不是预先手动装完整依赖。

📖 完整引导流程见 [`docs/GETTING_STARTED.md`](docs/GETTING_STARTED.md)
📖 新手图文版：[飞书文档](https://my.feishu.cn/wiki/CGrDw0T76iNFuskmwxdcWrpinPb)
📘 完整入门教程（Datawhale 出品）：[Hello GenericAgent](https://datawhalechina.github.io/hello-generic-agent/) · [GitHub](https://github.com/datawhalechina/hello-generic-agent)

---

## 💻 使用方式

### 前端启动

#### 桌面端

一键安装自带桌面端，双击：

```text
frontends/GenericAgent.exe
```

#### 终端 UI

基于 [Textual](https://github.com/Textualize/textual) 的轻量键盘驱动界面。支持多会话并发、实时流式输出，有终端就能跑。

```bash
python frontends/tuiapp_v2.py
```

<details>
<summary><b>⚠️ Windows 上 TUI 显示异常的排查思路</b></summary>

1. `textual` 版本太旧，先 `pip install -U textual`；
2. PowerShell / cmd 自带终端对 Unicode 和键位的支持比较糟糕，**Windows 上推荐用 Git Bash**，体验明显更稳；
3. 仍然显示异常时，可以让 GA 自己修一遍，参考 Prompt：
   > *"我在 Windows 的 PowerShell / cmd / Git Bash 中使用 `frontends/tuiapp_v2.py` 体验非常差，出现了一堆不兼容问题。请参考 Claude Code 在 Windows 终端的最佳配置，把所有字体和显示不兼容的问题修一遍。"*

</details>

#### Streamlit UI

```bash
python launch.pyw
```

### Bot 接口（IM）

GenericAgent 支持 Telegram、微信、QQ、飞书 / Lark、企业微信、钉钉等 IM 前端。

| 平台 | 启动命令 |
| :--- | :--- |
| Telegram | `python frontends/tgapp.py` |
| 微信 | `python frontends/wechatapp.py` |
| QQ | `python frontends/qqapp.py` |
| 飞书 / Lark | `python frontends/fsapp.py` |
| 企业微信 | `python frontends/wecomapp.py` |
| 钉钉 | `python frontends/dingtalkapp.py` |

> 详细配置直接问 GenericAgent。

### 通用聊天命令

| 命令 | 说明 |
| :--- | :--- |
| `/new` | 开启新对话并清空当前上下文 |
| `/continue` | 列出可恢复会话快照 |
| `/continue N` | 恢复第 `N` 个可恢复会话 |

---

## 🧠 架构设计

GenericAgent 通过 **分层记忆 × 最小工具集 × 自主执行循环** 完成复杂任务，并在执行过程中持续积累经验。

### 1️⃣ 分层记忆系统

> *记忆在任务执行过程中持续沉淀，使 Agent 逐步形成稳定且高效的工作方式。*

| 层级 | 名称 | 说明 |
| :---: | :--- | :--- |
| **L0** | 元规则（Meta Rules） | Agent 的基础行为规则和系统约束 |
| **L1** | 记忆索引（Insight Index） | 极简索引层，用于快速路由与召回 |
| **L2** | 全局事实（Global Facts） | 在长期运行过程中积累的稳定知识 |
| **L3** | 任务 Skills / SOPs | 完成特定任务类型的可复用流程 |
| **L4** | 会话归档（Session Archive） | 从已完成任务中提炼出的归档记录，用于长程召回 |

### 2️⃣ 自主执行循环

> *感知环境状态 → 任务推理 → 调用工具执行 → 经验写入记忆 → 循环*

整个核心循环仅 **约百行代码**（[`agent_loop.py`](agent_loop.py)）。

### 3️⃣ 最小工具集

> *GenericAgent 仅提供 **9 个原子工具**，构成与外部世界交互的基础能力。*

| 工具 | 功能 |
| :--- | :--- |
| `code_run` | 执行任意代码（Python / PowerShell） |
| `file_read` | 读取文件 |
| `file_write` | 写入 / 创建 / 覆盖文件 |
| `file_patch` | 修改文件 |
| `web_scan` | 感知网页内容 |
| `web_execute_js` | 控制浏览器行为 |
| `ask_user` | 人机协作确认 |
| `update_working_checkpoint` | *（记忆）* 短期工作记事板 |
| `start_long_term_update` | *（记忆）* 提炼长期记忆 |

### 4️⃣ 能力扩展机制

> *具备动态创建新工具的能力。*

通过 `code_run`，GenericAgent 可在运行时动态安装 Python 包、编写新脚本、调用外部 API 或控制硬件，将临时能力固化为永久工具。

<div align="center">
  <img src="assets/images/workflow.jpg" alt="GenericAgent 工作流程" width="420"/>
  <br/><em>GenericAgent 工作流程图</em>
</div>

---

## 🧬 自我进化机制

这是 GenericAgent 区别于其他 Agent 框架的根本所在。

```text
[遇到新任务]
    │
    ▼
[自主摸索]   ─►  安装依赖 · 编写脚本 · 调试验证
    │
    ▼
[执行路径固化为 Skill]   ─►  写入记忆层
    │
    ▼
[下次同类任务直接调用]
```

| 你说的一句话 | 第一次做了什么 | 之后每次 |
| :--- | :--- | :--- |
| *"监控股票并提醒我"* | 安装 `mootdx` → 构建选股流程 → 配置定时任务 → 保存 Skill | **一句话启动** |
| *"用 Gmail 发这个文件"* | 配置 OAuth → 编写发送脚本 → 保存 Skill | **直接可用** |

用几周后，你的 Agent 实例将拥有一套任何人都没有的专属技能树，全部从 3K 行种子代码中生长而来。

---

## 📊 与同类产品对比

| 特性 | **GenericAgent** | OpenClaw | Claude Code |
| :--- | :---: | :---: | :---: |
| **代码量** | ~3K 行 | ~530,000 行 | 已开源（体量大） |
| **部署方式** | `pip install` + API Key | 多服务编排 | CLI + 订阅 |
| **浏览器控制** | 注入真实浏览器（保留登录态） | 沙箱 / 无头浏览器 | 通过 MCP 插件 |
| **OS 控制** | 键鼠、视觉、ADB | 多 Agent 委派 | 文件 + 终端 |
| **自我进化** | 自主生长 Skill 和工具 | 插件生态 | 会话间无状态 |
| **出厂配置** | 几个核心文件 + 少量初始 Skills | 数百模块 | 丰富 CLI 工具集 |

---

## 📈 评测

> 📂 完整的评测数据集以及评测结果见：[**JinyiHan99/GA-Technical-Report**](https://github.com/JinyiHan99/GA-Technical-Report/tree/main)

我们从 **五大维度** 评测 GenericAgent：

| # | 维度 | 核心问题 | 使用的基准 |
| :---: | :--- | :--- | :--- |
| 1 | **任务完成度与 Token 效率** | GA 能否以更低成本完成高难度任务？ | SOP-Bench、Lifelong AgentBench、RealFin-Benchmark |
| 2 | **工具使用效率** | 最小原子工具集能否以更低开销替代专用工具集？ | Tool Efficiency Benchmark |
| 3 | **记忆系统有效性** | 精简分层记忆能否超越冗余记忆和基于 Embedding 的检索器？ | SOP-Bench、LoCoMo、20-skill 压力测试 |
| 4 | **自我进化能力** | Agent 能否在无人干预下将经验提炼为可复用的 SOP 与代码？ | 9 轮 LangChain 纵向研究、8 任务跨任务 Web 基准 |
| 5 | **网页浏览能力** | 信息密度驱动设计能否适应开放网页？ | WebCanvas、BrowseComp-ZH、自定义任务 |

以上维度的基线包括 **Claude Code**、**OpenAI CodeX** 和 **OpenClaw**，分别在 *Claude Sonnet 4.6*、*Claude Opus 4.6*、*GPT-5.4* 和 *MiniMax M2.7* 底座上进行评测。

<table>
  <tr>
    <td align="center" width="50%">
      <img src="assets/images/result_radar.png" width="100%" alt="工具使用效率雷达图"/><br/>
      <sub><b>工具使用效率雷达图。</b>GA 在 Token、请求数和工具调用轴上全面领先，同时在四个任务维度上保持质量。</sub>
    </td>
    <td align="center" width="50%">
      <img src="assets/images/result_convergence.png" width="100%" alt="跨任务自我进化收敛曲线"/><br/>
      <sub><b>跨任务自我进化。</b>GA 的第二轮和第三轮执行在 8 个 Web 任务上收敛至稳定的低成本区间。</sub>
    </td>
  </tr>
</table>

---

## 📅 路线图与最新动态

- **2026-05-23** — 🆕 **TUI v3 正式发布**（`frontends/tui_v3.py`）。基于块的滚屏回看 + 正确的 resize 重排，每终端独立配色保证跨终端一致，并与 v2 达成功能对齐。
- **2026-05-18** — 🆕 **Morphling 模式**。项目级能力吞噬 —— 从任意外部仓库抽取目标与测例后，对每个核心组件分别决定调用、重写或舍弃。详见 `memory/morphling_sop.md`。
- **2026-05-17** — 🆕 **Goal Hive 模式**。多 worker 协作版 Goal —— Master/Worker 通过 BBS 协同推进长程目标。详见 `memory/goal_hive_sop.md`。
- **2026-05-15** — 🖥️ **桌面 GUI 发布**。一键安装会自带可直接运行的桌面端（`frontends/GenericAgent.exe`），开发者也可用 `python launch.pyw` 启动。
- **2026-05-14** — 🆕 **Conductor 子 Agent 编排**。派发、监督、自动清理并行子 Agent；与 `/btw` 旁路子 Agent 互补，提供一等公民级的任务委派原语。
- **2026-05-12** — 🆕 **TUI v2 正式发布**（`frontends/tuiapp_v2.py`）。重做视觉风格的 Textual 前端，支持图片粘贴折叠、文件粘贴、块删除、Ctrl+C 复制、历史导航，以及 `/llm` / `/export` / `/continue` 选择器。
- **2026-05-08** — 🆕 **Goal 模式**（`reflect/goal_mode.py`）。时间预算驱动的自驱循环 —— "持续优化 X N 小时"，预算没到不准提前交付。
- **2026-04-21** — 📄 [**技术报告已发布至 arXiv**](https://arxiv.org/abs/2604.17091) — *GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization*。
- **2026-04-11** — 引入 **L4 会话归档记忆**，并接入 scheduler cron 调度。
- **2026-03-23** — 支持个人微信接入作为 Bot 前端。
- **2026-03-10** — [发布百万级 Skill 库](https://mp.weixin.qq.com/s/q2gQ7YvWoiAcwxzaiwpuiQ?scene=1&click_id=7)。
- **2026-03-08** — [发布以 GenericAgent 为核心的"政务龙虾" Dintal Claw](https://mp.weixin.qq.com/s/eiEhwo-j6S-WpLxgBnNxBg)。
- **2026-03-01** — [被机器之心报道](https://mp.weixin.qq.com/s/uVWpTTF5I1yzAENV_qm7yg)。
- **2026-01-16** — GenericAgent **V1.0** 公开版本发布。

---

## ⭐ 社区与支持

如果这个项目对你有帮助，欢迎点一个 **Star!** 🙏

也欢迎加入 **GenericAgent 体验交流群**，一起交流、反馈、共建 👏

<div align="center">
  <table>
    <tr>
      <td align="center"><strong>微信群 20</strong><br/><img src="assets/images/wechat_group20.jpg" alt="微信群 20 二维码" width="240"/></td>
    </tr>
  </table>
</div>

### 🚩 友情链接

感谢 **LinuxDo** 社区的支持！

[![LinuxDo](https://img.shields.io/badge/社区-LinuxDo-blue?style=for-the-badge)](https://linux.do/)

**社区 GUI 客户端** *（独立开源项目）*：

- [chilishark27/ga-manager](https://github.com/chilishark27/ga-manager)
- [wangjc683/galley](https://github.com/wangjc683/galley)
- [FroStorM/A3Agent](https://github.com/FroStorM/A3Agent/tree/workbench)

---

## 📄 许可

基于 **MIT License** 发布，详见 [`LICENSE`](LICENSE)。

> *声明：本项目未构建任何商业站点；除 DintalClaw 外，目前未官方授权任何机构、组织或个人以 GenericAgent 名义从事商业活动。*

---

<a id="-中文"></a>

## 🌟 项目简介

**GenericAgent** 是一个极简、可自我进化的自主 Agent 框架。核心仅 **~3K 行代码**，通过 **9 个原子工具 + ~100 行 Agent Loop**，赋予任意 LLM 对本地计算机的系统级控制能力，覆盖浏览器、终端、文件系统、键鼠输入、屏幕视觉及移动设备（ADB）。

> 设计哲学 —— **不预设技能，靠进化获得能力。**

每解决一个新任务，GenericAgent 就将执行路径自动固化为 Skill，供后续直接调用。使用时间越长，沉淀的技能越多，形成一棵完全属于你、从 3K 行种子代码生长出来的专属技能树。

> 🤖 **自举实证** — 本仓库的一切，从安装 Git、`git init` 到每一条 commit message，均由 GenericAgent 自主完成。作者全程未打开过一次终端。

### 📑 目录

- [核心特性](#-核心特性)
- [实例展示](#-实例展示)
- [快速开始](#-快速开始)
- [使用方式](#-使用方式)
- [架构设计](#-架构设计)
- [自我进化机制](#-自我进化机制)
- [与同类产品对比](#-与同类产品对比)
- [评测](#-评测)
- [路线图与最新动态](#-路线图与最新动态)
- [社区与支持](#-社区与支持)
- [许可](#-许可)

---

## 📋 核心特性

| 特性 | 说明 |
| :--- | :--- |
| 🧬 **自我进化** | 每次任务自动沉淀 Skill，能力随使用持续增长，形成专属技能树 |
| 🪶 **极简架构** | ~3K 行核心代码，Agent Loop 约百行，无复杂依赖，部署零负担 |
| ⚡ **强执行力** | 注入真实浏览器（保留登录态），9 个原子工具直接接管系统 |
| 🔌 **高兼容性** | 支持 Claude / Gemini / Kimi / MiniMax 等主流模型，跨平台运行 |
| 💰 **极致省 Token** | 上下文窗口不到 30K，是其他 Agent（200K–1M）的零头；噪声更少、幻觉更低、成功率更高，成本低一个数量级 |

---

## 🎯 实例展示

<table>
  <tr>
    <td align="center" width="50%"><b>🧋 外卖下单</b></td>
    <td align="center" width="50%"><b>📈 量化选股</b></td>
  </tr>
  <tr>
    <td><img src="assets/demo/order_tea.gif" width="100%" alt="外卖下单"></td>
    <td><img src="assets/demo/selectstock.gif" width="100%" alt="量化选股"></td>
  </tr>
  <tr>
    <td><sub><i>"Order me a milk tea"</i> — 自动导航外卖 App，选品并完成结账</sub></td>
    <td><sub><i>"Find GEM stocks with EXPMA golden cross, turnover &gt; 5%"</i> — 量化条件筛股</sub></td>
  </tr>
  <tr>
    <td align="center"><b>🌐 自主网页探索</b></td>
    <td align="center"><b>💰 支出追踪</b></td>
  </tr>
  <tr>
    <td><img src="assets/demo/autonomous_explore.png" width="100%" alt="网页探索"></td>
    <td><img src="assets/demo/alipay_expense.png" width="100%" alt="支付宝支出"></td>
  </tr>
  <tr>
    <td><sub>自主浏览并定时汇总网页信息</sub></td>
    <td><sub><i>"查找近 3 个月超 ¥2K 的支出"</i> — 通过 ADB 驱动支付宝</sub></td>
  </tr>
  <tr>
    <td align="center" colspan="2"><b>💬 批量消息</b></td>
  </tr>
  <tr>
    <td colspan="2" align="center"><img src="assets/demo/wechat_batch.png" width="50%" alt="微信批量"></td>
  </tr>
  <tr>
    <td colspan="2"><sub>批量发送微信消息，完整驱动微信客户端</sub></td>
  </tr>
</table>

---

## 🚀 快速开始

> ⚠️ **Python 版本：** 推荐使用 **Python 3.11 或 3.12**。**请不要使用 Python 3.14**，与 `pywebview` 及部分依赖不兼容。
>
> 📖 详细安装指南：**[installation_zh.md（中文）](docs/installation_zh.md)** · **[installation.md (English)](docs/installation.md)**

### 给 LLM Agent 看的

获取安装指南并照做：

```bash
curl -fsSL https://raw.githubusercontent.com/lsdefine/GenericAgent/refs/heads/main/docs/installation_zh.md
```

### 给人类用户看的

#### 方法一 — 一键安装 *（推荐）*

一键安装会自动准备独立 Python 环境、Git、项目文件和桌面端，不污染系统环境。

**Windows PowerShell**

```powershell
powershell -ExecutionPolicy Bypass -c "irm http://fudankw.cn:9000/files/ga_install.ps1 | iex"
```

**Linux / macOS**

```bash
curl -fsSL http://fudankw.cn:9000/files/ga_install.sh | bash
```

安装完成后，双击启动：

```text
frontends/GenericAgent.exe
```

#### 方法二 — Python 安装 *（开发者）*

```bash
git clone https://github.com/lsdefine/GenericAgent.git
cd GenericAgent
uv venv
uv pip install -e ".[ui]"          # 核心 + UI 依赖
cp mykey_template.py mykey.py      # 填入你的 LLM API Key
python launch.pyw
```

> 💡 GenericAgent 更推荐由 **Agent 在使用中自举环境**，而不是预先手动装完整依赖。

📖 完整引导流程见 [`docs/GETTING_STARTED.md`](docs/GETTING_STARTED.md)
📖 新手图文版：[飞书文档](https://my.feishu.cn/wiki/CGrDw0T76iNFuskmwxdcWrpinPb)
📘 完整入门教程（Datawhale 出品）：[Hello GenericAgent](https://datawhalechina.github.io/hello-generic-agent/) · [GitHub](https://github.com/datawhalechina/hello-generic-agent)

---

## 💻 使用方式

### 前端启动

#### 桌面端

一键安装自带桌面端，双击：

```text
frontends/GenericAgent.exe
```

#### 终端 UI

基于 [Textual](https://github.com/Textualize/textual) 的轻量键盘驱动界面。支持多会话并发、实时流式输出，有终端就能跑。

```bash
python frontends/tuiapp_v2.py
```

<details>
<summary><b>⚠️ Windows 上 TUI 显示异常的排查思路</b></summary>

1. `textual` 版本太旧，先 `pip install -U textual`；
2. PowerShell / cmd 自带终端对 Unicode 和键位的支持比较糟糕，**Windows 上推荐用 Git Bash**，体验明显更稳；
3. 仍然显示异常时，可以让 GA 自己修一遍，参考 Prompt：
   > *"我在 Windows 的 PowerShell / cmd / Git Bash 中使用 `frontends/tuiapp_v2.py` 体验非常差，出现了一堆不兼容问题。请参考 Claude Code 在 Windows 终端的最佳配置，把所有字体和显示不兼容的问题修一遍。"*

</details>

#### Streamlit UI

```bash
python launch.pyw
```

### Bot 接口（IM）

GenericAgent 支持 Telegram、微信、QQ、飞书 / Lark、企业微信、钉钉等 IM 前端。

| 平台 | 启动命令 |
| :--- | :--- |
| Telegram | `python frontends/tgapp.py` |
| 微信 | `python frontends/wechatapp.py` |
| QQ | `python frontends/qqapp.py` |
| 飞书 / Lark | `python frontends/fsapp.py` |
| 企业微信 | `python frontends/wecomapp.py` |
| 钉钉 | `python frontends/dingtalkapp.py` |

> 详细配置直接问 GenericAgent。

### 通用聊天命令

| 命令 | 说明 |
| :--- | :--- |
| `/new` | 开启新对话并清空当前上下文 |
| `/continue` | 列出可恢复会话快照 |
| `/continue N` | 恢复第 `N` 个可恢复会话 |

---

## 🧠 架构设计

GenericAgent 通过 **分层记忆 × 最小工具集 × 自主执行循环** 完成复杂任务，并在执行过程中持续积累经验。

### 1️⃣ 分层记忆系统

> *记忆在任务执行过程中持续沉淀，使 Agent 逐步形成稳定且高效的工作方式。*

| 层级 | 名称 | 说明 |
| :---: | :--- | :--- |
| **L0** | 元规则（Meta Rules） | Agent 的基础行为规则和系统约束 |
| **L1** | 记忆索引（Insight Index） | 极简索引层，用于快速路由与召回 |
| **L2** | 全局事实（Global Facts） | 在长期运行过程中积累的稳定知识 |
| **L3** | 任务 Skills / SOPs | 完成特定任务类型的可复用流程 |
| **L4** | 会话归档（Session Archive） | 从已完成任务中提炼出的归档记录，用于长程召回 |

### 2️⃣ 自主执行循环

> *感知环境状态 → 任务推理 → 调用工具执行 → 经验写入记忆 → 循环*

整个核心循环仅 **约百行代码**（[`agent_loop.py`](agent_loop.py)）。

### 3️⃣ 最小工具集

> *GenericAgent 仅提供 **9 个原子工具**，构成与外部世界交互的基础能力。*

| 工具 | 功能 |
| :--- | :--- |
| `code_run` | 执行任意代码（Python / PowerShell） |
| `file_read` | 读取文件 |
| `file_write` | 写入 / 创建 / 覆盖文件 |
| `file_patch` | 修改文件 |
| `web_scan` | 感知网页内容 |
| `web_execute_js` | 控制浏览器行为 |
| `ask_user` | 人机协作确认 |
| `update_working_checkpoint` | *（记忆）* 短期工作记事板 |
| `start_long_term_update` | *（记忆）* 提炼长期记忆 |

### 4️⃣ 能力扩展机制

> *具备动态创建新工具的能力。*

通过 `code_run`，GenericAgent 可在运行时动态安装 Python 包、编写新脚本、调用外部 API 或控制硬件，将临时能力固化为永久工具。

<div align="center">
  <img src="assets/images/workflow.jpg" alt="GenericAgent 工作流程" width="420"/>
  <br/><em>GenericAgent 工作流程图</em>
</div>

---

## 🧬 自我进化机制

这是 GenericAgent 区别于其他 Agent 框架的根本所在。

```text
[遇到新任务]
    │
    ▼
[自主摸索]   ─►  安装依赖 · 编写脚本 · 调试验证
    │
    ▼
[执行路径固化为 Skill]   ─►  写入记忆层
    │
    ▼
[下次同类任务直接调用]
```

| 你说的一句话 | 第一次做了什么 | 之后每次 |
| :--- | :--- | :--- |
| *"监控股票并提醒我"* | 安装 `mootdx` → 构建选股流程 → 配置定时任务 → 保存 Skill | **一句话启动** |
| *"用 Gmail 发这个文件"* | 配置 OAuth → 编写发送脚本 → 保存 Skill | **直接可用** |

用几周后，你的 Agent 实例将拥有一套任何人都没有的专属技能树，全部从 3K 行种子代码中生长而来。

---

## 📊 与同类产品对比

| 特性 | **GenericAgent** | OpenClaw | Claude Code |
| :--- | :---: | :---: | :---: |
| **代码量** | ~3K 行 | ~530,000 行 | 已开源（体量大） |
| **部署方式** | `pip install` + API Key | 多服务编排 | CLI + 订阅 |
| **浏览器控制** | 注入真实浏览器（保留登录态） | 沙箱 / 无头浏览器 | 通过 MCP 插件 |
| **OS 控制** | 键鼠、视觉、ADB | 多 Agent 委派 | 文件 + 终端 |
| **自我进化** | 自主生长 Skill 和工具 | 插件生态 | 会话间无状态 |
| **出厂配置** | 几个核心文件 + 少量初始 Skills | 数百模块 | 丰富 CLI 工具集 |

---

## 📈 评测

> 📂 完整的评测数据集以及评测结果见：[**JinyiHan99/GA-Technical-Report**](https://github.com/JinyiHan99/GA-Technical-Report/tree/main)

我们从 **五大维度** 评测 GenericAgent：

| # | 维度 | 核心问题 | 使用的基准 |
| :---: | :--- | :--- | :--- |
| 1 | **任务完成度与 Token 效率** | GA 能否以更低成本完成高难度任务？ | SOP-Bench、Lifelong AgentBench、RealFin-Benchmark |
| 2 | **工具使用效率** | 最小原子工具集能否以更低开销替代专用工具集？ | Tool Efficiency Benchmark |
| 3 | **记忆系统有效性** | 精简分层记忆能否超越冗余记忆和基于 Embedding 的检索器？ | SOP-Bench、LoCoMo、20-skill 压力测试 |
| 4 | **自我进化能力** | Agent 能否在无人干预下将经验提炼为可复用的 SOP 与代码？ | 9 轮 LangChain 纵向研究、8 任务跨任务 Web 基准 |
| 5 | **网页浏览能力** | 信息密度驱动设计能否适应开放网页？ | WebCanvas、BrowseComp-ZH、自定义任务 |

以上维度的基线包括 **Claude Code**、**OpenAI CodeX** 和 **OpenClaw**，分别在 *Claude Sonnet 4.6*、*Claude Opus 4.6*、*GPT-5.4* 和 *MiniMax M2.7* 底座上进行评测。

<table>
  <tr>
    <td align="center" width="50%">
      <img src="assets/images/result_radar.png" width="100%" alt="工具使用效率雷达图"/><br/>
      <sub><b>工具使用效率雷达图。</b>GA 在 Token、请求数和工具调用轴上全面领先，同时在四个任务维度上保持质量。</sub>
    </td>
    <td align="center" width="50%">
      <img src="assets/images/result_convergence.png" width="100%" alt="跨任务自我进化收敛曲线"/><br/>
      <sub><b>跨任务自我进化。</b>GA 的第二轮和第三轮执行在 8 个 Web 任务上收敛至稳定的低成本区间。</sub>
    </td>
  </tr>
</table>

---

## 📅 路线图与最新动态

- **2026-05-23** — 🆕 **TUI v3 正式发布**（`frontends/tui_v3.py`）。基于块的滚屏回看 + 正确的 resize 重排，每终端独立配色保证跨终端一致，并与 v2 达成功能对齐。
- **2026-05-18** — 🆕 **Morphling 模式**。项目级能力吞噬 —— 从任意外部仓库抽取目标与测例后，对每个核心组件分别决定调用、重写或舍弃。详见 `memory/morphling_sop.md`。
- **2026-05-17** — 🆕 **Goal Hive 模式**。多 worker 协作版 Goal —— Master/Worker 通过 BBS 协同推进长程目标。详见 `memory/goal_hive_sop.md`。
- **2026-05-15** — 🖥️ **桌面 GUI 发布**。一键安装会自带可直接运行的桌面端（`frontends/GenericAgent.exe`），开发者也可用 `python launch.pyw` 启动。
- **2026-05-14** — 🆕 **Conductor 子 Agent 编排**。派发、监督、自动清理并行子 Agent；与 `/btw` 旁路子 Agent 互补，提供一等公民级的任务委派原语。
- **2026-05-12** — 🆕 **TUI v2 正式发布**（`frontends/tuiapp_v2.py`）。重做视觉风格的 Textual 前端，支持图片粘贴折叠、文件粘贴、块删除、Ctrl+C 复制、历史导航，以及 `/llm` / `/export` / `/continue` 选择器。
- **2026-05-08** — 🆕 **Goal 模式**（`reflect/goal_mode.py`）。时间预算驱动的自驱循环 —— "持续优化 X N 小时"，预算没到不准提前交付。
- **2026-04-21** — 📄 [**技术报告已发布至 arXiv**](https://arxiv.org/abs/2604.17091) — *GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization*。
- **2026-04-11** — 引入 **L4 会话归档记忆**，并接入 scheduler cron 调度。
- **2026-03-23** — 支持个人微信接入作为 Bot 前端。
- **2026-03-10** — [发布百万级 Skill 库](https://mp.weixin.qq.com/s/q2gQ7YvWoiAcwxzaiwpuiQ?scene=1&click_id=7)。
- **2026-03-08** — [发布以 GenericAgent 为核心的"政务龙虾" Dintal Claw](https://mp.weixin.qq.com/s/eiEhwo-j6S-WpLxgBnNxBg)。
- **2026-03-01** — [被机器之心报道](https://mp.weixin.qq.com/s/uVWpTTF5I1yzAENV_qm7yg)。
- **2026-01-16** — GenericAgent **V1.0** 公开版本发布。

---

## ⭐ 社区与支持

如果这个项目对你有帮助，欢迎点一个 **Star!** 🙏

也欢迎加入 **GenericAgent 体验交流群**，一起交流、反馈、共建 👏

<div align="center">
  <table>
    <tr>
      <td align="center"><strong>微信群 20</strong><br/><img src="assets/images/wechat_group20.jpg" alt="微信群 20 二维码" width="240"/></td>
    </tr>
  </table>
</div>

### 🚩 友情链接

感谢 **LinuxDo** 社区的支持！

[![LinuxDo](https://img.shields.io/badge/社区-LinuxDo-blue?style=for-the-badge)](https://linux.do/)

**社区 GUI 客户端** *（独立开源项目）*：

- [chilishark27/ga-manager](https://github.com/chilishark27/ga-manager)
- [wangjc683/galley](https://github.com/wangjc683/galley)
- [FroStorM/A3Agent](https://github.com/FroStorM/A3Agent/tree/workbench)

---

## 📄 许可

基于 **MIT License** 发布，详见 [`LICENSE`](LICENSE)。

> *声明：本项目未构建任何商业站点；除 DintalClaw 外，目前未官方授权任何机构、组织或个人以 GenericAgent 名义从事商业活动。*

---

<a id="-中文"></a>

## 🌟 项目简介

**GenericAgent** 是一个极简、可自我进化的自主 Agent 框架。核心仅 **~3K 行代码**，通过 **9 个原子工具 + ~100 行 Agent Loop**，赋予任意 LLM 对本地计算机的系统级控制能力，覆盖浏览器、终端、文件系统、键鼠输入、屏幕视觉及移动设备（ADB）。

> 设计哲学 —— **不预设技能，靠进化获得能力。**

每解决一个新任务，GenericAgent 就将执行路径自动固化为 Skill，供后续直接调用。使用时间越长，沉淀的技能越多，形成一棵完全属于你、从 3K 行种子代码生长出来的专属技能树。

> 🤖 **自举实证** — 本仓库的一切，从安装 Git、`git init` 到每一条 commit message，均由 GenericAgent 自主完成。作者全程未打开过一次终端。

### 📑 目录

- [核心特性](#-核心特性)
- [实例展示](#-实例展示)
- [快速开始](#-快速开始)
- [使用方式](#-使用方式)
- [架构设计](#-架构设计)
- [自我进化机制](#-自我进化机制)
- [与同类产品对比](#-与同类产品对比)
- [评测](#-评测)
- [路线图与最新动态](#-路线图与最新动态)
- [社区与支持](#-社区与支持)
- [许可](#-许可)

---

## 📋 核心特性

| 特性 | 说明 |
| :--- | :--- |
| 🧬 **自我进化** | 每次任务自动沉淀 Skill，能力随使用持续增长，形成专属技能树 |
| 🪶 **极简架构** | ~3K 行核心代码，Agent Loop 约百行，无复杂依赖，部署零负担 |
| ⚡ **强执行力** | 注入真实浏览器（保留登录态），9 个原子工具直接接管系统 |
| 🔌 **高兼容性** | 支持 Claude / Gemini / Kimi / MiniMax 等主流模型，跨平台运行 |
| 💰 **极致省 Token** | 上下文窗口不到 30K，是其他 Agent（200K–1M）的零头；噪声更少、幻觉更低、成功率更高，成本低一个数量级 |

---

## 🎯 实例展示

<table>
  <tr>
    <td align="center" width="50%"><b>🧋 外卖下单</b></td>
    <td align="center" width="50%"><b>📈 量化选股</b></td>
  </tr>
  <tr>
    <td><img src="assets/demo/order_tea.gif" width="100%" alt="外卖下单"></td>
    <td><img src="assets/demo/selectstock.gif" width="100%" alt="量化选股"></td>
  </tr>
  <tr>
    <td><sub><i>"Order me a milk tea"</i> — 自动导航外卖 App，选品并完成结账</sub></td>
    <td><sub><i>"Find GEM stocks with EXPMA golden cross, turnover &gt; 5%"</i> — 量化条件筛股</sub></td>
  </tr>
  <tr>
    <td align="center"><b>🌐 自主网页探索</b></td>
    <td align="center"><b>💰 支出追踪</b></td>
  </tr>
  <tr>
    <td><img src="assets/demo/autonomous_explore.png" width="100%" alt="网页探索"></td>
    <td><img src="assets/demo/alipay_expense.png" width="100%" alt="支付宝支出"></td>
  </tr>
  <tr>
    <td><sub>自主浏览并定时汇总网页信息</sub></td>
    <td><sub><i>"查找近 3 个月超 ¥2K 的支出"</i> — 通过 ADB 驱动支付宝</sub></td>
  </tr>
  <tr>
    <td align="center" colspan="2"><b>💬 批量消息</b></td>
  </tr>
  <tr>
    <td colspan="2" align="center"><img src="assets/demo/wechat_batch.png" width="50%" alt="微信批量"></td>
  </tr>
  <tr>
    <td colspan="2"><sub>批量发送微信消息，完整驱动微信客户端</sub></td>
  </tr>
</table>

---

## 🚀 快速开始

> ⚠️ **Python 版本：** 推荐使用 **Python 3.11 或 3.12**。**请不要使用 Python 3.14**，与 `pywebview` 及部分依赖不兼容。
>
> 📖 详细安装指南：**[installation_zh.md（中文）](docs/installation_zh.md)** · **[installation.md (English)](docs/installation.md)**

### 给 LLM Agent 看的

获取安装指南并照做：

```bash
curl -fsSL https://raw.githubusercontent.com/lsdefine/GenericAgent/refs/heads/main/docs/installation_zh.md
```

### 给人类用户看的

#### 方法一 — 一键安装 *（推荐）*

一键安装会自动准备独立 Python 环境、Git、项目文件和桌面端，不污染系统环境。

**Windows PowerShell**

```powershell
powershell -ExecutionPolicy Bypass -c "irm http://fudankw.cn:9000/files/ga_install.ps1 | iex"
```

**Linux / macOS**

```bash
curl -fsSL http://fudankw.cn:9000/files/ga_install.sh | bash
```

安装完成后，双击启动：

```text
frontends/GenericAgent.exe
```

#### 方法二 — Python 安装 *（开发者）*

```bash
git clone https://github.com/lsdefine/GenericAgent.git
cd GenericAgent
uv venv
uv pip install -e ".[ui]"          # 核心 + UI 依赖
cp mykey_template.py mykey.py      # 填入你的 LLM API Key
python launch.pyw
```

> 💡 GenericAgent 更推荐由 **Agent 在使用中自举环境**，而不是预先手动装完整依赖。

📖 完整引导流程见 [`docs/GETTING_STARTED.md`](docs/GETTING_STARTED.md)
📖 新手图文版：[飞书文档](https://my.feishu.cn/wiki/CGrDw0T76iNFuskmwxdcWrpinPb)
📘 完整入门教程（Datawhale 出品）：[Hello GenericAgent](https://datawhalechina.github.io/hello-generic-agent/) · [GitHub](https://github.com/datawhalechina/hello-generic-agent)

---

## 💻 使用方式

### 前端启动

#### 桌面端

一键安装自带桌面端，双击：

```text
frontends/GenericAgent.exe
```

#### 终端 UI

基于 [Textual](https://github.com/Textualize/textual) 的轻量键盘驱动界面。支持多会话并发、实时流式输出，有终端就能跑。

```bash
python frontends/tuiapp_v2.py
```

<details>
<summary><b>⚠️ Windows 上 TUI 显示异常的排查思路</b></summary>

1. `textual` 版本太旧，先 `pip install -U textual`；
2. PowerShell / cmd 自带终端对 Unicode 和键位的支持比较糟糕，**Windows 上推荐用 Git Bash**，体验明显更稳；
3. 仍然显示异常时，可以让 GA 自己修一遍，参考 Prompt：
   > *"我在 Windows 的 PowerShell / cmd / Git Bash 中使用 `frontends/tuiapp_v2.py` 体验非常差，出现了一堆不兼容问题。请参考 Claude Code 在 Windows 终端的最佳配置，把所有字体和显示不兼容的问题修一遍。"*

</details>

#### Streamlit UI

```bash
python launch.pyw
```

### Bot 接口（IM）

GenericAgent 支持 Telegram、微信、QQ、飞书 / Lark、企业微信、钉钉等 IM 前端。

| 平台 | 启动命令 |
| :--- | :--- |
| Telegram | `python frontends/tgapp.py` |
| 微信 | `python frontends/wechatapp.py` |
| QQ | `python frontends/qqapp.py` |
| 飞书 / Lark | `python frontends/fsapp.py` |
| 企业微信 | `python frontends/wecomapp.py` |
| 钉钉 | `python frontends/dingtalkapp.py` |

> 详细配置直接问 GenericAgent。

### 通用聊天命令

| 命令 | 说明 |
| :--- | :--- |
| `/new` | 开启新对话并清空当前上下文 |
| `/continue` | 列出可恢复会话快照 |
| `/continue N` | 恢复第 `N` 个可恢复会话 |

---

## 🧠 架构设计

GenericAgent 通过 **分层记忆 × 最小工具集 × 自主执行循环** 完成复杂任务，并在执行过程中持续积累经验。

### 1️⃣ 分层记忆系统

> *记忆在任务执行过程中持续沉淀，使 Agent 逐步形成稳定且高效的工作方式。*

| 层级 | 名称 | 说明 |
| :---: | :--- | :--- |
| **L0** | 元规则（Meta Rules） | Agent 的基础行为规则和系统约束 |
| **L1** | 记忆索引（Insight Index） | 极简索引层，用于快速路由与召回 |
| **L2** | 全局事实（Global Facts） | 在长期运行过程中积累的稳定知识 |
| **L3** | 任务 Skills / SOPs | 完成特定任务类型的可复用流程 |
| **L4** | 会话归档（Session Archive） | 从已完成任务中提炼出的归档记录，用于长程召回 |

### 2️⃣ 自主执行循环

> *感知环境状态 → 任务推理 → 调用工具执行 → 经验写入记忆 → 循环*

整个核心循环仅 **约百行代码**（[`agent_loop.py`](agent_loop.py)）。

### 3️⃣ 最小工具集

> *GenericAgent 仅提供 **9 个原子工具**，构成与外部世界交互的基础能力。*

| 工具 | 功能 |
| :--- | :--- |
| `code_run` | 执行任意代码（Python / PowerShell） |
| `file_read` | 读取文件 |
| `file_write` | 写入 / 创建 / 覆盖文件 |
| `file_patch` | 修改文件 |
| `web_scan` | 感知网页内容 |
| `web_execute_js` | 控制浏览器行为 |
| `ask_user` | 人机协作确认 |
| `update_working_checkpoint` | *（记忆）* 短期工作记事板 |
| `start_long_term_update` | *（记忆）* 提炼长期记忆 |

### 4️⃣ 能力扩展机制

> *具备动态创建新工具的能力。*

通过 `code_run`，GenericAgent 可在运行时动态安装 Python 包、编写新脚本、调用外部 API 或控制硬件，将临时能力固化为永久工具。

<div align="center">
  <img src="assets/images/workflow.jpg" alt="GenericAgent 工作流程" width="420"/>
  <br/><em>GenericAgent 工作流程图</em>
</div>

---

## 🧬 自我进化机制

这是 GenericAgent 区别于其他 Agent 框架的根本所在。

```text
[遇到新任务]
    │
    ▼
[自主摸索]   ─►  安装依赖 · 编写脚本 · 调试验证
    │
    ▼
[执行路径固化为 Skill]   ─►  写入记忆层
    │
    ▼
[下次同类任务直接调用]
```

| 你说的一句话 | 第一次做了什么 | 之后每次 |
| :--- | :--- | :--- |
| *"监控股票并提醒我"* | 安装 `mootdx` → 构建选股流程 → 配置定时任务 → 保存 Skill | **一句话启动** |
| *"用 Gmail 发这个文件"* | 配置 OAuth → 编写发送脚本 → 保存 Skill | **直接可用** |

用几周后，你的 Agent 实例将拥有一套任何人都没有的专属技能树，全部从 3K 行种子代码中生长而来。

---

## 📊 与同类产品对比

| 特性 | **GenericAgent** | OpenClaw | Claude Code |
| :--- | :---: | :---: | :---: |
| **代码量** | ~3K 行 | ~530,000 行 | 已开源（体量大） |
| **部署方式** | `pip install` + API Key | 多服务编排 | CLI + 订阅 |
| **浏览器控制** | 注入真实浏览器（保留登录态） | 沙箱 / 无头浏览器 | 通过 MCP 插件 |
| **OS 控制** | 键鼠、视觉、ADB | 多 Agent 委派 | 文件 + 终端 |
| **自我进化** | 自主生长 Skill 和工具 | 插件生态 | 会话间无状态 |
| **出厂配置** | 几个核心文件 + 少量初始 Skills | 数百模块 | 丰富 CLI 工具集 |

---

## 📈 评测

> 📂 完整的评测数据集以及评测结果见：[**JinyiHan99/GA-Technical-Report**](https://github.com/JinyiHan99/GA-Technical-Report/tree/main)

我们从 **五大维度** 评测 GenericAgent：

| # | 维度 | 核心问题 | 使用的基准 |
| :---: | :--- | :--- | :--- |
| 1 | **任务完成度与 Token 效率** | GA 能否以更低成本完成高难度任务？ | SOP-Bench、Lifelong AgentBench、RealFin-Benchmark |
| 2 | **工具使用效率** | 最小原子工具集能否以更低开销替代专用工具集？ | Tool Efficiency Benchmark |
| 3 | **记忆系统有效性** | 精简分层记忆能否超越冗余记忆和基于 Embedding 的检索器？ | SOP-Bench、LoCoMo、20-skill 压力测试 |
| 4 | **自我进化能力** | Agent 能否在无人干预下将经验提炼为可复用的 SOP 与代码？ | 9 轮 LangChain 纵向研究、8 任务跨任务 Web 基准 |
| 5 | **网页浏览能力** | 信息密度驱动设计能否适应开放网页？ | WebCanvas、BrowseComp-ZH、自定义任务 |

以上维度的基线包括 **Claude Code**、**OpenAI CodeX** 和 **OpenClaw**，分别在 *Claude Sonnet 4.6*、*Claude Opus 4.6*、*GPT-5.4* 和 *MiniMax M2.7* 底座上进行评测。

<table>
  <tr>
    <td align="center" width="50%">
      <img src="assets/images/result_radar.png" width="100%" alt="工具使用效率雷达图"/><br/>
      <sub><b>工具使用效率雷达图。</b>GA 在 Token、请求数和工具调用轴上全面领先，同时在四个任务维度上保持质量。</sub>
    </td>
    <td align="center" width="50%">
      <img src="assets/images/result_convergence.png" width="100%" alt="跨任务自我进化收敛曲线"/><br/>
      <sub><b>跨任务自我进化。</b>GA 的第二轮和第三轮执行在 8 个 Web 任务上收敛至稳定的低成本区间。</sub>
    </td>
  </tr>
</table>

---

## 📅 路线图与最新动态

- **2026-05-23** — 🆕 **TUI v3 正式发布**（`frontends/tui_v3.py`）。基于块的滚屏回看 + 正确的 resize 重排，每终端独立配色保证跨终端一致，并与 v2 达成功能对齐。
- **2026-05-18** — 🆕 **Morphling 模式**。项目级能力吞噬 —— 从任意外部仓库抽取目标与测例后，对每个核心组件分别决定调用、重写或舍弃。详见 `memory/morphling_sop.md`。
- **2026-05-17** — 🆕 **Goal Hive 模式**。多 worker 协作版 Goal —— Master/Worker 通过 BBS 协同推进长程目标。详见 `memory/goal_hive_sop.md`。
- **2026-05-15** — 🖥️ **桌面 GUI 发布**。一键安装会自带可直接运行的桌面端（`frontends/GenericAgent.exe`），开发者也可用 `python launch.pyw` 启动。
- **2026-05-14** — 🆕 **Conductor 子 Agent 编排**。派发、监督、自动清理并行子 Agent；与 `/btw` 旁路子 Agent 互补，提供一等公民级的任务委派原语。
- **2026-05-12** — 🆕 **TUI v2 正式发布**（`frontends/tuiapp_v2.py`）。重做视觉风格的 Textual 前端，支持图片粘贴折叠、文件粘贴、块删除、Ctrl+C 复制、历史导航，以及 `/llm` / `/export` / `/continue` 选择器。
- **2026-05-08** — 🆕 **Goal 模式**（`reflect/goal_mode.py`）。时间预算驱动的自驱循环 —— "持续优化 X N 小时"，预算没到不准提前交付。
- **2026-04-21** — 📄 [**技术报告已发布至 arXiv**](https://arxiv.org/abs/2604.17091) — *GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization*。
- **2026-04-11** — 引入 **L4 会话归档记忆**，并接入 scheduler cron 调度。
- **2026-03-23** — 支持个人微信接入作为 Bot 前端。
- **2026-03-10** — [发布百万级 Skill 库](https://mp.weixin.qq.com/s/q2gQ7YvWoiAcwxzaiwpuiQ?scene=1&click_id=7)。
- **2026-03-08** — [发布以 GenericAgent 为核心的"政务龙虾" Dintal Claw](https://mp.weixin.qq.com/s/eiEhwo-j6S-WpLxgBnNxBg)。
- **2026-03-01** — [被机器之心报道](https://mp.weixin.qq.com/s/uVWpTTF5I1yzAENV_qm7yg)。
- **2026-01-16** — GenericAgent **V1.0** 公开版本发布。

---

## ⭐ 社区与支持

如果这个项目对你有帮助，欢迎点一个 **Star!** 🙏

也欢迎加入 **GenericAgent 体验交流群**，一起交流、反馈、共建 👏

<div align="center">
  <table>
    <tr>
      <td align="center"><strong>微信群 20</strong><br/><img src="assets/images/wechat_group20.jpg" alt="微信群 20 二维码" width="240"/></td>
    </tr>
  </table>
</div>

### 🚩 友情链接

感谢 **LinuxDo** 社区的支持！

[![LinuxDo](https://img.shields.io/badge/社区-LinuxDo-blue?style=for-the-badge)](https://linux.do/)

**社区 GUI 客户端** *（独立开源项目）*：

- [chilishark27/ga-manager](https://github.com/chilishark27/ga-manager)
- [wangjc683/galley](https://github.com/wangjc683/galley)
- [FroStorM/A3Agent](https://github.com/FroStorM/A3Agent/tree/workbench)

---

## 📄 许可

基于 **MIT License** 发布，详见 [`LICENSE`](LICENSE)。

> *声明：本项目未构建任何商业站点；除 DintalClaw 外，目前未官方授权任何机构、组织或个人以 GenericAgent 名义从事商业活动。*

---

<a id="-中文"></a>

## 🌟 项目简介

**GenericAgent** 是一个极简、可自我进化的自主 Agent 框架。核心仅 **~3K 行代码**，通过 **9 个原子工具 + ~100 行 Agent Loop**，赋予任意 LLM 对本地计算机的系统级控制能力，覆盖浏览器、终端、文件系统、键鼠输入、屏幕视觉及移动设备（ADB）。

> 设计哲学 —— **不预设技能，靠进化获得能力。**

每解决一个新任务，GenericAgent 就将执行路径自动固化为 Skill，供后续直接调用。使用时间越长，沉淀的技能越多，形成一棵完全属于你、从 3K 行种子代码生长出来的专属技能树。

> 🤖 **自举实证** — 本仓库的一切，从安装 Git、`git init` 到每一条 commit message，均由 GenericAgent 自主完成。作者全程未打开过一次终端。

### 📑 目录

- [核心特性](#-核心特性)
- [实例展示](#-实例展示)
- [快速开始](#-快速开始)
- [使用方式](#-使用方式)
- [架构设计](#-架构设计)
- [自我进化机制](#-自我进化机制)
- [与同类产品对比](#-与同类产品对比)
- [评测](#-评测)
- [路线图与最新动态](#-路线图与最新动态)
- [社区与支持](#-社区与支持)
- [许可](#-许可)

---

## 📋 核心特性

| 特性 | 说明 |
| :--- | :--- |
| 🧬 **自我进化** | 每次任务自动沉淀 Skill，能力随使用持续增长，形成专属技能树 |
| 🪶 **极简架构** | ~3K 行核心代码，Agent Loop 约百行，无复杂依赖，部署零负担 |
| ⚡ **强执行力** | 注入真实浏览器（保留登录态），9 个原子工具直接接管系统 |
| 🔌 **高兼容性** | 支持 Claude / Gemini / Kimi / MiniMax 等主流模型，跨平台运行 |
| 💰 **极致省 Token** | 上下文窗口不到 30K，是其他 Agent（200K–1M）的零头；噪声更少、幻觉更低、成功率更高，成本低一个数量级 |

---

## 🎯 实例展示

<table>
  <tr>
    <td align="center" width="50%"><b>🧋 外卖下单</b></td>
    <td align="center" width="50%"><b>📈 量化选股</b></td>
  </tr>
  <tr>
    <td><img src="assets/demo/order_tea.gif" width="100%" alt="外卖下单"></td>
    <td><img src="assets/demo/selectstock.gif" width="100%" alt="量化选股"></td>
  </tr>
  <tr>
    <td><sub><i>"Order me a milk tea"</i> — 自动导航外卖 App，选品并完成结账</sub></td>
    <td><sub><i>"Find GEM stocks with EXPMA golden cross, turnover &gt; 5%"</i> — 量化条件筛股</sub></td>
  </tr>
  <tr>
    <td align="center"><b>🌐 自主网页探索</b></td>
    <td align="center"><b>💰 支出追踪</b></td>
  </tr>
  <tr>
    <td><img src="assets/demo/autonomous_explore.png" width="100%" alt="网页探索"></td>
    <td><img src="assets/demo/alipay_expense.png" width="100%" alt="支付宝支出"></td>
  </tr>
  <tr>
    <td><sub>自主浏览并定时汇总网页信息</sub></td>
    <td><sub><i>"查找近 3 个月超 ¥2K 的支出"</i> — 通过 ADB 驱动支付宝</sub></td>
  </tr>
  <tr>
    <td align="center" colspan="2"><b>💬 批量消息</b></td>
  </tr>
  <tr>
    <td colspan="2" align="center"><img src="assets/demo/wechat_batch.png" width="50%" alt="微信批量"></td>
  </tr>
  <tr>
    <td colspan="2"><sub>批量发送微信消息，完整驱动微信客户端</sub></td>
  </tr>
</table>

---

## 🚀 快速开始

> ⚠️ **Python 版本：** 推荐使用 **Python 3.11 或 3.12**。**请不要使用 Python 3.14**，与 `pywebview` 及部分依赖不兼容。
>
> 📖 详细安装指南：**[installation_zh.md（中文）](docs/installation_zh.md)** · **[installation.md (English)](docs/installation.md)**

### 给 LLM Agent 看的

获取安装指南并照做：

```bash
curl -fsSL https://raw.githubusercontent.com/lsdefine/GenericAgent/refs/heads/main/docs/installation_zh.md
```

### 给人类用户看的

#### 方法一 — 一键安装 *（推荐）*

一键安装会自动准备独立 Python 环境、Git、项目文件和桌面端，不污染系统环境。

**Windows PowerShell**

```powershell
powershell -ExecutionPolicy Bypass -c "irm http://fudankw.cn:9000/files/ga_install.ps1 | iex"
```

**Linux / macOS**

```bash
curl -fsSL http://fudankw.cn:9000/files/ga_install.sh | bash
```

安装完成后，双击启动：

```text
frontends/GenericAgent.exe
```

#### 方法二 — Python 安装 *（开发者）*

```bash
git clone https://github.com/lsdefine/GenericAgent.git
cd GenericAgent
uv venv
uv pip install -e ".[ui]"          # 核心 + UI 依赖
cp mykey_template.py mykey.py      # 填入你的 LLM API Key
python launch.pyw
```

> 💡 GenericAgent 更推荐由 **Agent 在使用中自举环境**，而不是预先手动装完整依赖。

📖 完整引导流程见 [`docs/GETTING_STARTED.md`](docs/GETTING_STARTED.md)
📖 新手图文版：[飞书文档](https://my.feishu.cn/wiki/CGrDw0T76iNFuskmwxdcWrpinPb)
📘 完整入门教程（Datawhale 出品）：[Hello GenericAgent](https://datawhalechina.github.io/hello-generic-agent/) · [GitHub](https://github.com/datawhalechina/hello-generic-agent)

---

## 💻 使用方式

### 前端启动

#### 桌面端

一键安装自带桌面端，双击：

```text
frontends/GenericAgent.exe
```

#### 终端 UI

基于 [Textual](https://github.com/Textualize/textual) 的轻量键盘驱动界面。支持多会话并发、实时流式输出，有终端就能跑。

```bash
python frontends/tuiapp_v2.py
```

<details>
<summary><b>⚠️ Windows 上 TUI 显示异常的排查思路</b></summary>

1. `textual` 版本太旧，先 `pip install -U textual`；
2. PowerShell / cmd 自带终端对 Unicode 和键位的支持比较糟糕，**Windows 上推荐用 Git Bash**，体验明显更稳；
3. 仍然显示异常时，可以让 GA 自己修一遍，参考 Prompt：
   > *"我在 Windows 的 PowerShell / cmd / Git Bash 中使用 `frontends/tuiapp_v2.py` 体验非常差，出现了一堆不兼容问题。请参考 Claude Code 在 Windows 终端的最佳配置，把所有字体和显示不兼容的问题修一遍。"*

</details>

#### Streamlit UI

```bash
python launch.pyw
```

### Bot 接口（IM）

GenericAgent 支持 Telegram、微信、QQ、飞书 / Lark、企业微信、钉钉等 IM 前端。

| 平台 | 启动命令 |
| :--- | :--- |
| Telegram | `python frontends/tgapp.py` |
| 微信 | `python frontends/wechatapp.py` |
| QQ | `python frontends/qqapp.py` |
| 飞书 / Lark | `python frontends/fsapp.py` |
| 企业微信 | `python frontends/wecomapp.py` |
| 钉钉 | `python frontends/dingtalkapp.py` |

> 详细配置直接问 GenericAgent。

### 通用聊天命令

| 命令 | 说明 |
| :--- | :--- |
| `/new` | 开启新对话并清空当前上下文 |
| `/continue` | 列出可恢复会话快照 |
| `/continue N` | 恢复第 `N` 个可恢复会话 |

---

## 🧠 架构设计

GenericAgent 通过 **分层记忆 × 最小工具集 × 自主执行循环** 完成复杂任务，并在执行过程中持续积累经验。

### 1️⃣ 分层记忆系统

> *记忆在任务执行过程中持续沉淀，使 Agent 逐步形成稳定且高效的工作方式。*

| 层级 | 名称 | 说明 |
| :---: | :--- | :--- |
| **L0** | 元规则（Meta Rules） | Agent 的基础行为规则和系统约束 |
| **L1** | 记忆索引（Insight Index） | 极简索引层，用于快速路由与召回 |
| **L2** | 全局事实（Global Facts） | 在长期运行过程中积累的稳定知识 |
| **L3** | 任务 Skills / SOPs | 完成特定任务类型的可复用流程 |
| **L4** | 会话归档（Session Archive） | 从已完成任务中提炼出的归档记录，用于长程召回 |

### 2️⃣ 自主执行循环

> *感知环境状态 → 任务推理 → 调用工具执行 → 经验写入记忆 → 循环*

整个核心循环仅 **约百行代码**（[`agent_loop.py`](agent_loop.py)）。

### 3️⃣ 最小工具集

> *GenericAgent 仅提供 **9 个原子工具**，构成与外部世界交互的基础能力。*

| 工具 | 功能 |
| :--- | :--- |
| `code_run` | 执行任意代码（Python / PowerShell） |
| `file_read` | 读取文件 |
| `file_write` | 写入 / 创建 / 覆盖文件 |
| `file_patch` | 修改文件 |
| `web_scan` | 感知网页内容 |
| `web_execute_js` | 控制浏览器行为 |
| `ask_user` | 人机协作确认 |
| `update_working_checkpoint` | *（记忆）* 短期工作记事板 |
| `start_long_term_update` | *（记忆）* 提炼长期记忆 |

### 4️⃣ 能力扩展机制

> *具备动态创建新工具的能力。*

通过 `code_run`，GenericAgent 可在运行时动态安装 Python 包、编写新脚本、调用外部 API 或控制硬件，将临时能力固化为永久工具。

<div align="center">
  <img src="assets/images/workflow.jpg" alt="GenericAgent 工作流程" width="420"/>
  <br/><em>GenericAgent 工作流程图</em>
</div>

---

## 🧬 自我进化机制

这是 GenericAgent 区别于其他 Agent 框架的根本所在。

```text
[遇到新任务]
    │
    ▼
[自主摸索]   ─►  安装依赖 · 编写脚本 · 调试验证
    │
    ▼
[执行路径固化为 Skill]   ─►  写入记忆层
    │
    ▼
[下次同类任务直接调用]
```

| 你说的一句话 | 第一次做了什么 | 之后每次 |
| :--- | :--- | :--- |
| *"监控股票并提醒我"* | 安装 `mootdx` → 构建选股流程 → 配置定时任务 → 保存 Skill | **一句话启动** |
| *"用 Gmail 发这个文件"* | 配置 OAuth → 编写发送脚本 → 保存 Skill | **直接可用** |

用几周后，你的 Agent 实例将拥有一套任何人都没有的专属技能树，全部从 3K 行种子代码中生长而来。

---

## 📊 与同类产品对比

| 特性 | **GenericAgent** | OpenClaw | Claude Code |
| :--- | :---: | :---: | :---: |
| **代码量** | ~3K 行 | ~530,000 行 | 已开源（体量大） |
| **部署方式** | `pip install` + API Key | 多服务编排 | CLI + 订阅 |
| **浏览器控制** | 注入真实浏览器（保留登录态） | 沙箱 / 无头浏览器 | 通过 MCP 插件 |
| **OS 控制** | 键鼠、视觉、ADB | 多 Agent 委派 | 文件 + 终端 |
| **自我进化** | 自主生长 Skill 和工具 | 插件生态 | 会话间无状态 |
| **出厂配置** | 几个核心文件 + 少量初始 Skills | 数百模块 | 丰富 CLI 工具集 |

---

## 📈 评测

> 📂 完整的评测数据集以及评测结果见：[**JinyiHan99/GA-Technical-Report**](https://github.com/JinyiHan99/GA-Technical-Report/tree/main)

我们从 **五大维度** 评测 GenericAgent：

| # | 维度 | 核心问题 | 使用的基准 |
| :---: | :--- | :--- | :--- |
| 1 | **任务完成度与 Token 效率** | GA 能否以更低成本完成高难度任务？ | SOP-Bench、Lifelong AgentBench、RealFin-Benchmark |
| 2 | **工具使用效率** | 最小原子工具集能否以更低开销替代专用工具集？ | Tool Efficiency Benchmark |
| 3 | **记忆系统有效性** | 精简分层记忆能否超越冗余记忆和基于 Embedding 的检索器？ | SOP-Bench、LoCoMo、20-skill 压力测试 |
| 4 | **自我进化能力** | Agent 能否在无人干预下将经验提炼为可复用的 SOP 与代码？ | 9 轮 LangChain 纵向研究、8 任务跨任务 Web 基准 |
| 5 | **网页浏览能力** | 信息密度驱动设计能否适应开放网页？ | WebCanvas、BrowseComp-ZH、自定义任务 |

以上维度的基线包括 **Claude Code**、**OpenAI CodeX** 和 **OpenClaw**，分别在 *Claude Sonnet 4.6*、*Claude Opus 4.6*、*GPT-5.4* 和 *MiniMax M2.7* 底座上进行评测。

<table>
  <tr>
    <td align="center" width="50%">
      <img src="assets/images/result_radar.png" width="100%" alt="工具使用效率雷达图"/><br/>
      <sub><b>工具使用效率雷达图。</b>GA 在 Token、请求数和工具调用轴上全面领先，同时在四个任务维度上保持质量。</sub>
    </td>
    <td align="center" width="50%">
      <img src="assets/images/result_convergence.png" width="100%" alt="跨任务自我进化收敛曲线"/><br/>
      <sub><b>跨任务自我进化。</b>GA 的第二轮和第三轮执行在 8 个 Web 任务上收敛至稳定的低成本区间。</sub>
    </td>
  </tr>
</table>

---

## 📅 路线图与最新动态

- **2026-05-23** — 🆕 **TUI v3 正式发布**（`frontends/tui_v3.py`）。基于块的滚屏回看 + 正确的 resize 重排，每终端独立配色保证跨终端一致，并与 v2 达成功能对齐。
- **2026-05-18** — 🆕 **Morphling 模式**。项目级能力吞噬 —— 从任意外部仓库抽取目标与测例后，对每个核心组件分别决定调用、重写或舍弃。详见 `memory/morphling_sop.md`。
- **2026-05-17** — 🆕 **Goal Hive 模式**。多 worker 协作版 Goal —— Master/Worker 通过 BBS 协同推进长程目标。详见 `memory/goal_hive_sop.md`。
- **2026-05-15** — 🖥️ **桌面 GUI 发布**。一键安装会自带可直接运行的桌面端（`frontends/GenericAgent.exe`），开发者也可用 `python launch.pyw` 启动。
- **2026-05-14** — 🆕 **Conductor 子 Agent 编排**。派发、监督、自动清理并行子 Agent；与 `/btw` 旁路子 Agent 互补，提供一等公民级的任务委派原语。
- **2026-05-12** — 🆕 **TUI v2 正式发布**（`frontends/tuiapp_v2.py`）。重做视觉风格的 Textual 前端，支持图片粘贴折叠、文件粘贴、块删除、Ctrl+C 复制、历史导航，以及 `/llm` / `/export` / `/continue` 选择器。
- **2026-05-08** — 🆕 **Goal 模式**（`reflect/goal_mode.py`）。时间预算驱动的自驱循环 —— "持续优化 X N 小时"，预算没到不准提前交付。
- **2026-04-21** — 📄 [**技术报告已发布至 arXiv**](https://arxiv.org/abs/2604.17091) — *GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization*。
- **2026-04-11** — 引入 **L4 会话归档记忆**，并接入 scheduler cron 调度。
- **2026-03-23** — 支持个人微信接入作为 Bot 前端。
- **2026-03-10** — [发布百万级 Skill 库](https://mp.weixin.qq.com/s/q2gQ7YvWoiAcwxzaiwpuiQ?scene=1&click_id=7)。
- **2026-03-08** — [发布以 GenericAgent 为核心的"政务龙虾" Dintal Claw](https://mp.weixin.qq.com/s/eiEhwo-j6S-WpLxgBnNxBg)。
- **2026-03-01** — [被机器之心报道](https://mp.weixin.qq.com/s/uVWpTTF5I1yzAENV_qm7yg)。
- **2026-01-16** — GenericAgent **V1.0** 公开版本发布。

---

## ⭐ 社区与支持

如果这个项目对你有帮助，欢迎点一个 **Star!** 🙏

也欢迎加入 **GenericAgent 体验交流群**，一起交流、反馈、共建 👏

<div align="center">
  <table>
    <tr>
      <td align="center"><strong>微信群 20</strong><br/><img src="assets/images/wechat_group20.jpg" alt="微信群 20 二维码" width="240"/></td>
    </tr>
  </table>
</div>

### 🚩 友情链接

感谢 **LinuxDo** 社区的支持！

[![LinuxDo](https://img.shields.io/badge/社区-LinuxDo-blue?style=for-the-badge)](https://linux.do/)

**社区 GUI 客户端** *（独立开源项目）*：

- [chilishark27/ga-manager](https://github.com/chilishark27/ga-manager)
- [wangjc683/galley](https://github.com/wangjc683/galley)
- [FroStorM/A3Agent](https://github.com/FroStorM/A3Agent/tree/workbench)

---

## 📄 许可

基于 **MIT License** 发布，详见 [`LICENSE`](LICENSE)。

> *声明：本项目未构建任何商业站点；除 DintalClaw 外，目前未官方授权任何机构、组织或个人以 GenericAgent 名义从事商业活动。*

---

<a id="-中文"></a>

## 🌟 项目简介

**GenericAgent** 是一个极简、可自我进化的自主 Agent 框架。核心仅 **~3K 行代码**，通过 **9 个原子工具 + ~100 行 Agent Loop**，赋予任意 LLM 对本地计算机的系统级控制能力，覆盖浏览器、终端、文件系统、键鼠输入、屏幕视觉及移动设备（ADB）。

> 设计哲学 —— **不预设技能，靠进化获得能力。**

每解决一个新任务，GenericAgent 就将执行路径自动固化为 Skill，供后续直接调用。使用时间越长，沉淀的技能越多，形成一棵完全属于你、从 3K 行种子代码生长出来的专属技能树。

> 🤖 **自举实证** — 本仓库的一切，从安装 Git、`git init` 到每一条 commit message，均由 GenericAgent 自主完成。作者全程未打开过一次终端。

### 📑 目录

- [核心特性](#-核心特性)
- [实例展示](#-实例展示)
- [快速开始](#-快速开始)
- [使用方式](#-使用方式)
- [架构设计](#-架构设计)
- [自我进化机制](#-自我进化机制)
- [与同类产品对比](#-与同类产品对比)
- [评测](#-评测)
- [路线图与最新动态](#-路线图与最新动态)
- [社区与支持](#-社区与支持)
- [许可](#-许可)

---

## 📋 核心特性

| 特性 | 说明 |
| :--- | :--- |
| 🧬 **自我进化** | 每次任务自动沉淀 Skill，能力随使用持续增长，形成专属技能树 |
| 🪶 **极简架构** | ~3K 行核心代码，Agent Loop 约百行，无复杂依赖，部署零负担 |
| ⚡ **强执行力** | 注入真实浏览器（保留登录态），9 个原子工具直接接管系统 |
| 🔌 **高兼容性** | 支持 Claude / Gemini / Kimi / MiniMax 等主流模型，跨平台运行 |
| 💰 **极致省 Token** | 上下文窗口不到 30K，是其他 Agent（200K–1M）的零头；噪声更少、幻觉更低、成功率更高，成本低一个数量级 |

---

## 🎯 实例展示

<table>
  <tr>
    <td align="center" width="50%"><b>🧋 外卖下单</b></td>
    <td align="center" width="50%"><b>📈 量化选股</b></td>
  </tr>
  <tr>
    <td><img src="assets/demo/order_tea.gif" width="100%" alt="外卖下单"></td>
    <td><img src="assets/demo/selectstock.gif" width="100%" alt="量化选股"></td>
  </tr>
  <tr>
    <td><sub><i>"Order me a milk tea"</i> — 自动导航外卖 App，选品并完成结账</sub></td>
    <td><sub><i>"Find GEM stocks with EXPMA golden cross, turnover &gt; 5%"</i> — 量化条件筛股</sub></td>
  </tr>
  <tr>
    <td align="center"><b>🌐 自主网页探索</b></td>
    <td align="center"><b>💰 支出追踪</b></td>
  </tr>
  <tr>
    <td><img src="assets/demo/autonomous_explore.png" width="100%" alt="网页探索"></td>
    <td><img src="assets/demo/alipay_expense.png" width="100%" alt="支付宝支出"></td>
  </tr>
  <tr>
    <td><sub>自主浏览并定时汇总网页信息</sub></td>
    <td><sub><i>"查找近 3 个月超 ¥2K 的支出"</i> — 通过 ADB 驱动支付宝</sub></td>
  </tr>
  <tr>
    <td align="center" colspan="2"><b>💬 批量消息</b></td>
  </tr>
  <tr>
    <td colspan="2" align="center"><img src="assets/demo/wechat_batch.png" width="50%" alt="微信批量"></td>
  </tr>
  <tr>
    <td colspan="2"><sub>批量发送微信消息，完整驱动微信客户端</sub></td>
  </tr>
</table>

---

## 🚀 快速开始

> ⚠️ **Python 版本：** 推荐使用 **Python 3.11 或 3.12**。**请不要使用 Python 3.14**，与 `pywebview` 及部分依赖不兼容。
>
> 📖 详细安装指南：**[installation_zh.md（中文）](docs/installation_zh.md)** · **[installation.md (English)](docs/installation.md)**

### 给 LLM Agent 看的

获取安装指南并照做：

```bash
curl -fsSL https://raw.githubusercontent.com/lsdefine/GenericAgent/refs/heads/main/docs/installation_zh.md
```

### 给人类用户看的

#### 方法一 — 一键安装 *（推荐）*

一键安装会自动准备独立 Python 环境、Git、项目文件和桌面端，不污染系统环境。

**Windows PowerShell**

```powershell
powershell -ExecutionPolicy Bypass -c "irm http://fudankw.cn:9000/files/ga_install.ps1 | iex"
```

**Linux / macOS**

```bash
curl -fsSL http://fudankw.cn:9000/files/ga_install.sh | bash
```

安装完成后，双击启动：

```text
frontends/GenericAgent.exe
```

#### 方法二 — Python 安装 *（开发者）*

```bash
git clone https://github.com/lsdefine/GenericAgent.git
cd GenericAgent
uv venv
uv pip install -e ".[ui]"          # 核心 + UI 依赖
cp mykey_template.py mykey.py      # 填入你的 LLM API Key
python launch.pyw
```

> 💡 GenericAgent 更推荐由 **Agent 在使用中自举环境**，而不是预先手动装完整依赖。

📖 完整引导流程见 [`docs/GETTING_STARTED.md`](docs/GETTING_STARTED.md)
📖 新手图文版：[飞书文档](https://my.feishu.cn/wiki/CGrDw0T76iNFuskmwxdcWrpinPb)
📘 完整入门教程（Datawhale 出品）：[Hello GenericAgent](https://datawhalechina.github.io/hello-generic-agent/) · [GitHub](https://github.com/datawhalechina/hello-generic-agent)

---

## 💻 使用方式

### 前端启动

#### 桌面端

一键安装自带桌面端，双击：

```text
frontends/GenericAgent.exe
```

#### 终端 UI

基于 [Textual](https://github.com/Textualize/textual) 的轻量键盘驱动界面。支持多会话并发、实时流式输出，有终端就能跑。

```bash
python frontends/tuiapp_v2.py
```

<details>
<summary><b>⚠️ Windows 上 TUI 显示异常的排查思路</b></summary>

1. `textual` 版本太旧，先 `pip install -U textual`；
2. PowerShell / cmd 自带终端对 Unicode 和键位的支持比较糟糕，**Windows 上推荐用 Git Bash**，体验明显更稳；
3. 仍然显示异常时，可以让 GA 自己修一遍，参考 Prompt：
   > *"我在 Windows 的 PowerShell / cmd / Git Bash 中使用 `frontends/tuiapp_v2.py` 体验非常差，出现了一堆不兼容问题。请参考 Claude Code 在 Windows 终端的最佳配置，把所有字体和显示不兼容的问题修一遍。"*

</details>

#### Streamlit UI

```bash
python launch.pyw
```

### Bot 接口（IM）

GenericAgent 支持 Telegram、微信、QQ、飞书 / Lark、企业微信、钉钉等 IM 前端。

| 平台 | 启动命令 |
| :--- | :--- |
| Telegram | `python frontends/tgapp.py` |
| 微信 | `python frontends/wechatapp.py` |
| QQ | `python frontends/qqapp.py` |
| 飞书 / Lark | `python frontends/fsapp.py` |
| 企业微信 | `python frontends/wecomapp.py` |
| 钉钉 | `python frontends/dingtalkapp.py` |

> 详细配置直接问 GenericAgent。

### 通用聊天命令

| 命令 | 说明 |
| :--- | :--- |
| `/new` | 开启新对话并清空当前上下文 |
| `/continue` | 列出可恢复会话快照 |
| `/continue N` | 恢复第 `N` 个可恢复会话 |

---

## 🧠 架构设计

GenericAgent 通过 **分层记忆 × 最小工具集 × 自主执行循环** 完成复杂任务，并在执行过程中持续积累经验。

### 1️⃣ 分层记忆系统

> *记忆在任务执行过程中持续沉淀，使 Agent 逐步形成稳定且高效的工作方式。*

| 层级 | 名称 | 说明 |
| :---: | :--- | :--- |
| **L0** | 元规则（Meta Rules） | Agent 的基础行为规则和系统约束 |
| **L1** | 记忆索引（Insight Index） | 极简索引层，用于快速路由与召回 |
| **L2** | 全局事实（Global Facts） | 在长期运行过程中积累的稳定知识 |
| **L3** | 任务 Skills / SOPs | 完成特定任务类型的可复用流程 |
| **L4** | 会话归档（Session Archive） | 从已完成任务中提炼出的归档记录，用于长程召回 |

### 2️⃣ 自主执行循环

> *感知环境状态 → 任务推理 → 调用工具执行 → 经验写入记忆 → 循环*

整个核心循环仅 **约百行代码**（[`agent_loop.py`](agent_loop.py)）。

### 3️⃣ 最小工具集

> *GenericAgent 仅提供 **9 个原子工具**，构成与外部世界交互的基础能力。*

| 工具 | 功能 |
| :--- | :--- |
| `code_run` | 执行任意代码（Python / PowerShell） |
| `file_read` | 读取文件 |
| `file_write` | 写入 / 创建 / 覆盖文件 |
| `file_patch` | 修改文件 |
| `web_scan` | 感知网页内容 |
| `web_execute_js` | 控制浏览器行为 |
| `ask_user` | 人机协作确认 |
| `update_working_checkpoint` | *（记忆）* 短期工作记事板 |
| `start_long_term_update` | *（记忆）* 提炼长期记忆 |

### 4️⃣ 能力扩展机制

> *具备动态创建新工具的能力。*

通过 `code_run`，GenericAgent 可在运行时动态安装 Python 包、编写新脚本、调用外部 API 或控制硬件，将临时能力固化为永久工具。

<div align="center">
  <img src="assets/images/workflow.jpg" alt="GenericAgent 工作流程" width="420"/>
  <br/><em>GenericAgent 工作流程图</em>
</div>

---

## 🧬 自我进化机制

这是 GenericAgent 区别于其他 Agent 框架的根本所在。

```text
[遇到新任务]
    │
    ▼
[自主摸索]   ─►  安装依赖 · 编写脚本 · 调试验证
    │
    ▼
[执行路径固化为 Skill]   ─►  写入记忆层
    │
    ▼
[下次同类任务直接调用]
```

| 你说的一句话 | 第一次做了什么 | 之后每次 |
| :--- | :--- | :--- |
| *"监控股票并提醒我"* | 安装 `mootdx` → 构建选股流程 → 配置定时任务 → 保存 Skill | **一句话启动** |
| *"用 Gmail 发这个文件"* | 配置 OAuth → 编写发送脚本 → 保存 Skill | **直接可用** |

用几周后，你的 Agent 实例将拥有一套任何人都没有的专属技能树，全部从 3K 行种子代码中生长而来。

---

## 📊 与同类产品对比

| 特性 | **GenericAgent** | OpenClaw | Claude Code |
| :--- | :---: | :---: | :---: |
| **代码量** | ~3K 行 | ~530,000 行 | 已开源（体量大） |
| **部署方式** | `pip install` + API Key | 多服务编排 | CLI + 订阅 |
| **浏览器控制** | 注入真实浏览器（保留登录态） | 沙箱 / 无头浏览器 | 通过 MCP 插件 |
| **OS 控制** | 键鼠、视觉、ADB | 多 Agent 委派 | 文件 + 终端 |
| **自我进化** | 自主生长 Skill 和工具 | 插件生态 | 会话间无状态 |
| **出厂配置** | 几个核心文件 + 少量初始 Skills | 数百模块 | 丰富 CLI 工具集 |

---

## 📈 评测

> 📂 完整的评测数据集以及评测结果见：[**JinyiHan99/GA-Technical-Report**](https://github.com/JinyiHan99/GA-Technical-Report/tree/main)

我们从 **五大维度** 评测 GenericAgent：

| # | 维度 | 核心问题 | 使用的基准 |
| :---: | :--- | :--- | :--- |
| 1 | **任务完成度与 Token 效率** | GA 能否以更低成本完成高难度任务？ | SOP-Bench、Lifelong AgentBench、RealFin-Benchmark |
| 2 | **工具使用效率** | 最小原子工具集能否以更低开销替代专用工具集？ | Tool Efficiency Benchmark |
| 3 | **记忆系统有效性** | 精简分层记忆能否超越冗余记忆和基于 Embedding 的检索器？ | SOP-Bench、LoCoMo、20-skill 压力测试 |
| 4 | **自我进化能力** | Agent 能否在无人干预下将经验提炼为可复用的 SOP 与代码？ | 9 轮 LangChain 纵向研究、8 任务跨任务 Web 基准 |
| 5 | **网页浏览能力** | 信息密度驱动设计能否适应开放网页？ | WebCanvas、BrowseComp-ZH、自定义任务 |

以上维度的基线包括 **Claude Code**、**OpenAI CodeX** 和 **OpenClaw**，分别在 *Claude Sonnet 4.6*、*Claude Opus 4.6*、*GPT-5.4* 和 *MiniMax M2.7* 底座上进行评测。

<table>
  <tr>
    <td align="center" width="50%">
      <img src="assets/images/result_radar.png" width="100%" alt="工具使用效率雷达图"/><br/>
      <sub><b>工具使用效率雷达图。</b>GA 在 Token、请求数和工具调用轴上全面领先，同时在四个任务维度上保持质量。</sub>
    </td>
    <td align="center" width="50%">
      <img src="assets/images/result_convergence.png" width="100%" alt="跨任务自我进化收敛曲线"/><br/>
      <sub><b>跨任务自我进化。</b>GA 的第二轮和第三轮执行在 8 个 Web 任务上收敛至稳定的低成本区间。</sub>
    </td>
  </tr>
</table>

---

## 📅 路线图与最新动态

- **2026-05-23** — 🆕 **TUI v3 正式发布**（`frontends/tui_v3.py`）。基于块的滚屏回看 + 正确的 resize 重排，每终端独立配色保证跨终端一致，并与 v2 达成功能对齐。
- **2026-05-18** — 🆕 **Morphling 模式**。项目级能力吞噬 —— 从任意外部仓库抽取目标与测例后，对每个核心组件分别决定调用、重写或舍弃。详见 `memory/morphling_sop.md`。
- **2026-05-17** — 🆕 **Goal Hive 模式**。多 worker 协作版 Goal —— Master/Worker 通过 BBS 协同推进长程目标。详见 `memory/goal_hive_sop.md`。
- **2026-05-15** — 🖥️ **桌面 GUI 发布**。一键安装会自带可直接运行的桌面端（`frontends/GenericAgent.exe`），开发者也可用 `python launch.pyw` 启动。
- **2026-05-14** — 🆕 **Conductor 子 Agent 编排**。派发、监督、自动清理并行子 Agent；与 `/btw` 旁路子 Agent 互补，提供一等公民级的任务委派原语。
- **2026-05-12** — 🆕 **TUI v2 正式发布**（`frontends/tuiapp_v2.py`）。重做视觉风格的 Textual 前端，支持图片粘贴折叠、文件粘贴、块删除、Ctrl+C 复制、历史导航，以及 `/llm` / `/export` / `/continue` 选择器。
- **2026-05-08** — 🆕 **Goal 模式**（`reflect/goal_mode.py`）。时间预算驱动的自驱循环 —— "持续优化 X N 小时"，预算没到不准提前交付。
- **2026-04-21** — 📄 [**技术报告已发布至 arXiv**](https://arxiv.org/abs/2604.17091) — *GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization*。
- **2026-04-11** — 引入 **L4 会话归档记忆**，并接入 scheduler cron 调度。
- **2026-03-23** — 支持个人微信接入作为 Bot 前端。
- **2026-03-10** — [发布百万级 Skill 库](https://mp.weixin.qq.com/s/q2gQ7YvWoiAcwxzaiwpuiQ?scene=1&click_id=7)。
- **2026-03-08** — [发布以 GenericAgent 为核心的"政务龙虾" Dintal Claw](https://mp.weixin.qq.com/s/eiEhwo-j6S-WpLxgBnNxBg)。
- **2026-03-01** — [被机器之心报道](https://mp.weixin.qq.com/s/uVWpTTF5I1yzAENV_qm7yg)。
- **2026-01-16** — GenericAgent **V1.0** 公开版本发布。

---

## ⭐ 社区与支持

如果这个项目对你有帮助，欢迎点一个 **Star!** 🙏

也欢迎加入 **GenericAgent 体验交流群**，一起交流、反馈、共建 👏

<div align="center">
  <table>
    <tr>
      <td align="center"><strong>微信群 20</strong><br/><img src="assets/images/wechat_group20.jpg" alt="微信群 20 二维码" width="240"/></td>
    </tr>
  </table>
</div>

### 🚩 友情链接

感谢 **LinuxDo** 社区的支持！

[![LinuxDo](https://img.shields.io/badge/社区-LinuxDo-blue?style=for-the-badge)](https://linux.do/)

**社区 GUI 客户端** *（独立开源项目）*：

- [chilishark27/ga-manager](https://github.com/chilishark27/ga-manager)
- [wangjc683/galley](https://github.com/wangjc683/galley)
- [FroStorM/A3Agent](https://github.com/FroStorM/A3Agent/tree/workbench)

---

## 📄 许可

基于 **MIT License** 发布，详见 [`LICENSE`](LICENSE)。

> *声明：本项目未构建任何商业站点；除 DintalClaw 外，目前未官方授权任何机构、组织或个人以 GenericAgent 名义从事商业活动。*

---

<a id="-中文"></a>

## 🌟 项目简介

**GenericAgent** 是一个极简、可自我进化的自主 Agent 框架。核心仅 **~3K 行代码**，通过 **9 个原子工具 + ~100 行 Agent Loop**，赋予任意 LLM 对本地计算机的系统级控制能力，覆盖浏览器、终端、文件系统、键鼠输入、屏幕视觉及移动设备（ADB）。

> 设计哲学 —— **不预设技能，靠进化获得能力。**

每解决一个新任务，GenericAgent 就将执行路径自动固化为 Skill，供后续直接调用。使用时间越长，沉淀的技能越多，形成一棵完全属于你、从 3K 行种子代码生长出来的专属技能树。

> 🤖 **自举实证** — 本仓库的一切，从安装 Git、`git init` 到每一条 commit message，均由 GenericAgent 自主完成。作者全程未打开过一次终端。

### 📑 目录

- [核心特性](#-核心特性)
- [实例展示](#-实例展示)
- [快速开始](#-快速开始)
- [使用方式](#-使用方式)
- [架构设计](#-架构设计)
- [自我进化机制](#-自我进化机制)
- [与同类产品对比](#-与同类产品对比)
- [评测](#-评测)
- [路线图与最新动态](#-路线图与最新动态)
- [社区与支持](#-社区与支持)
- [许可](#-许可)

---

## 📋 核心特性

| 特性 | 说明 |
| :--- | :--- |
| 🧬 **自我进化** | 每次任务自动沉淀 Skill，能力随使用持续增长，形成专属技能树 |
| 🪶 **极简架构** | ~3K 行核心代码，Agent Loop 约百行，无复杂依赖，部署零负担 |
| ⚡ **强执行力** | 注入真实浏览器（保留登录态），9 个原子工具直接接管系统 |
| 🔌 **高兼容性** | 支持 Claude / Gemini / Kimi / MiniMax 等主流模型，跨平台运行 |
| 💰 **极致省 Token** | 上下文窗口不到 30K，是其他 Agent（200K–1M）的零头；噪声更少、幻觉更低、成功率更高，成本低一个数量级 |

---

## 🎯 实例展示

<table>
  <tr>
    <td align="center" width="50%"><b>🧋 外卖下单</b></td>
    <td align="center" width="50%"><b>📈 量化选股</b></td>
  </tr>
  <tr>
    <td><img src="assets/demo/order_tea.gif" width="100%" alt="外卖下单"></td>
    <td><img src="assets/demo/selectstock.gif" width="100%" alt="量化选股"></td>
  </tr>
  <tr>
    <td><sub><i>"Order me a milk tea"</i> — 自动导航外卖 App，选品并完成结账</sub></td>
    <td><sub><i>"Find GEM stocks with EXPMA golden cross, turnover &gt; 5%"</i> — 量化条件筛股</sub></td>
  </tr>
  <tr>
    <td align="center"><b>🌐 自主网页探索</b></td>
    <td align="center"><b>💰 支出追踪</b></td>
  </tr>
  <tr>
    <td><img src="assets/demo/autonomous_explore.png" width="100%" alt="网页探索"></td>
    <td><img src="assets/demo/alipay_expense.png" width="100%" alt="支付宝支出"></td>
  </tr>
  <tr>
    <td><sub>自主浏览并定时汇总网页信息</sub></td>
    <td><sub><i>"查找近 3 个月超 ¥2K 的支出"</i> — 通过 ADB 驱动支付宝</sub></td>
  </tr>
  <tr>
    <td align="center" colspan="2"><b>💬 批量消息</b></td>
  </tr>
  <tr>
    <td colspan="2" align="center"><img src="assets/demo/wechat_batch.png" width="50%" alt="微信批量"></td>
  </tr>
  <tr>
    <td colspan="2"><sub>批量发送微信消息，完整驱动微信客户端</sub></td>
  </tr>
</table>

---

## 🚀 快速开始

> ⚠️ **Python 版本：** 推荐使用 **Python 3.11 或 3.12**。**请不要使用 Python 3.14**，与 `pywebview` 及部分依赖不兼容。
>
> 📖 详细安装指南：**[installation_zh.md（中文）](docs/installation_zh.md)** · **[installation.md (English)](docs/installation.md)**

### 给 LLM Agent 看的

获取安装指南并照做：

```bash
curl -fsSL https://raw.githubusercontent.com/lsdefine/GenericAgent/refs/heads/main/docs/installation_zh.md
```

### 给人类用户看的

#### 方法一 — 一键安装 *（推荐）*

一键安装会自动准备独立 Python 环境、Git、项目文件和桌面端，不污染系统环境。

**Windows PowerShell**

```powershell
powershell -ExecutionPolicy Bypass -c "irm http://fudankw.cn:9000/files/ga_install.ps1 | iex"
```

**Linux / macOS**

```bash
curl -fsSL http://fudankw.cn:9000/files/ga_install.sh | bash
```

安装完成后，双击启动：

```text
frontends/GenericAgent.exe
```

#### 方法二 — Python 安装 *（开发者）*

```bash
git clone https://github.com/lsdefine/GenericAgent.git
cd GenericAgent
uv venv
uv pip install -e ".[ui]"          # 核心 + UI 依赖
cp mykey_template.py mykey.py      # 填入你的 LLM API Key
python launch.pyw
```

> 💡 GenericAgent 更推荐由 **Agent 在使用中自举环境**，而不是预先手动装完整依赖。

📖 完整引导流程见 [`docs/GETTING_STARTED.md`](docs/GETTING_STARTED.md)
📖 新手图文版：[飞书文档](https://my.feishu.cn/wiki/CGrDw0T76iNFuskmwxdcWrpinPb)
📘 完整入门教程（Datawhale 出品）：[Hello GenericAgent](https://datawhalechina.github.io/hello-generic-agent/) · [GitHub](https://github.com/datawhalechina/hello-generic-agent)

---

## 💻 使用方式

### 前端启动

#### 桌面端

一键安装自带桌面端，双击：

```text
frontends/GenericAgent.exe
```

#### 终端 UI

基于 [Textual](https://github.com/Textualize/textual) 的轻量键盘驱动界面。支持多会话并发、实时流式输出，有终端就能跑。

```bash
python frontends/tuiapp_v2.py
```

<details>
<summary><b>⚠️ Windows 上 TUI 显示异常的排查思路</b></summary>

1. `textual` 版本太旧，先 `pip install -U textual`；
2. PowerShell / cmd 自带终端对 Unicode 和键位的支持比较糟糕，**Windows 上推荐用 Git Bash**，体验明显更稳；
3. 仍然显示异常时，可以让 GA 自己修一遍，参考 Prompt：
   > *"我在 Windows 的 PowerShell / cmd / Git Bash 中使用 `frontends/tuiapp_v2.py` 体验非常差，出现了一堆不兼容问题。请参考 Claude Code 在 Windows 终端的最佳配置，把所有字体和显示不兼容的问题修一遍。"*

</details>

#### Streamlit UI

```bash
python launch.pyw
```

### Bot 接口（IM）

GenericAgent 支持 Telegram、微信、QQ、飞书 / Lark、企业微信、钉钉等 IM 前端。

| 平台 | 启动命令 |
| :--- | :--- |
| Telegram | `python frontends/tgapp.py` |
| 微信 | `python frontends/wechatapp.py` |
| QQ | `python frontends/qqapp.py` |
| 飞书 / Lark | `python frontends/fsapp.py` |
| 企业微信 | `python frontends/wecomapp.py` |
| 钉钉 | `python frontends/dingtalkapp.py` |

> 详细配置直接问 GenericAgent。

### 通用聊天命令

| 命令 | 说明 |
| :--- | :--- |
| `/new` | 开启新对话并清空当前上下文 |
| `/continue` | 列出可恢复会话快照 |
| `/continue N` | 恢复第 `N` 个可恢复会话 |

---

## 🧠 架构设计

GenericAgent 通过 **分层记忆 × 最小工具集 × 自主执行循环** 完成复杂任务，并在执行过程中持续积累经验。

### 1️⃣ 分层记忆系统

> *记忆在任务执行过程中持续沉淀，使 Agent 逐步形成稳定且高效的工作方式。*

| 层级 | 名称 | 说明 |
| :---: | :--- | :--- |
| **L0** | 元规则（Meta Rules） | Agent 的基础行为规则和系统约束 |
| **L1** | 记忆索引（Insight Index） | 极简索引层，用于快速路由与召回 |
| **L2** | 全局事实（Global Facts） | 在长期运行过程中积累的稳定知识 |
| **L3** | 任务 Skills / SOPs | 完成特定任务类型的可复用流程 |
| **L4** | 会话归档（Session Archive） | 从已完成任务中提炼出的归档记录，用于长程召回 |

### 2️⃣ 自主执行循环

> *感知环境状态 → 任务推理 → 调用工具执行 → 经验写入记忆 → 循环*

整个核心循环仅 **约百行代码**（[`agent_loop.py`](agent_loop.py)）。

### 3️⃣ 最小工具集

> *GenericAgent 仅提供 **9 个原子工具**，构成与外部世界交互的基础能力。*

| 工具 | 功能 |
| :--- | :--- |
| `code_run` | 执行任意代码（Python / PowerShell） |
| `file_read` | 读取文件 |
| `file_write` | 写入 / 创建 / 覆盖文件 |
| `file_patch` | 修改文件 |
| `web_scan` | 感知网页内容 |
| `web_execute_js` | 控制浏览器行为 |
| `ask_user` | 人机协作确认 |
| `update_working_checkpoint` | *（记忆）* 短期工作记事板 |
| `start_long_term_update` | *（记忆）* 提炼长期记忆 |

### 4️⃣ 能力扩展机制

> *具备动态创建新工具的能力。*

通过 `code_run`，GenericAgent 可在运行时动态安装 Python 包、编写新脚本、调用外部 API 或控制硬件，将临时能力固化为永久工具。

<div align="center">
  <img src="assets/images/workflow.jpg" alt="GenericAgent 工作流程" width="420"/>
  <br/><em>GenericAgent 工作流程图</em>
</div>

---

## 🧬 自我进化机制

这是 GenericAgent 区别于其他 Agent 框架的根本所在。

```text
[遇到新任务]
    │
    ▼
[自主摸索]   ─►  安装依赖 · 编写脚本 · 调试验证
    │
    ▼
[执行路径固化为 Skill]   ─►  写入记忆层
    │
    ▼
[下次同类任务直接调用]
```

| 你说的一句话 | 第一次做了什么 | 之后每次 |
| :--- | :--- | :--- |
| *"监控股票并提醒我"* | 安装 `mootdx` → 构建选股流程 → 配置定时任务 → 保存 Skill | **一句话启动** |
| *"用 Gmail 发这个文件"* | 配置 OAuth → 编写发送脚本 → 保存 Skill | **直接可用** |

用几周后，你的 Agent 实例将拥有一套任何人都没有的专属技能树，全部从 3K 行种子代码中生长而来。

---

## 📊 与同类产品对比

| 特性 | **GenericAgent** | OpenClaw | Claude Code |
| :--- | :---: | :---: | :---: |
| **代码量** | ~3K 行 | ~530,000 行 | 已开源（体量大） |
| **部署方式** | `pip install` + API Key | 多服务编排 | CLI + 订阅 |
| **浏览器控制** | 注入真实浏览器（保留登录态） | 沙箱 / 无头浏览器 | 通过 MCP 插件 |
| **OS 控制** | 键鼠、视觉、ADB | 多 Agent 委派 | 文件 + 终端 |
| **自我进化** | 自主生长 Skill 和工具 | 插件生态 | 会话间无状态 |
| **出厂配置** | 几个核心文件 + 少量初始 Skills | 数百模块 | 丰富 CLI 工具集 |

---

## 📈 评测

> 📂 完整的评测数据集以及评测结果见：[**JinyiHan99/GA-Technical-Report**](https://github.com/JinyiHan99/GA-Technical-Report/tree/main)

我们从 **五大维度** 评测 GenericAgent：

| # | 维度 | 核心问题 | 使用的基准 |
| :---: | :--- | :--- | :--- |
| 1 | **任务完成度与 Token 效率** | GA 能否以更低成本完成高难度任务？ | SOP-Bench、Lifelong AgentBench、RealFin-Benchmark |
| 2 | **工具使用效率** | 最小原子工具集能否以更低开销替代专用工具集？ | Tool Efficiency Benchmark |
| 3 | **记忆系统有效性** | 精简分层记忆能否超越冗余记忆和基于 Embedding 的检索器？ | SOP-Bench、LoCoMo、20-skill 压力测试 |
| 4 | **自我进化能力** | Agent 能否在无人干预下将经验提炼为可复用的 SOP 与代码？ | 9 轮 LangChain 纵向研究、8 任务跨任务 Web 基准 |
| 5 | **网页浏览能力** | 信息密度驱动设计能否适应开放网页？ | WebCanvas、BrowseComp-ZH、自定义任务 |

以上维度的基线包括 **Claude Code**、**OpenAI CodeX** 和 **OpenClaw**，分别在 *Claude Sonnet 4.6*、*Claude Opus 4.6*、*GPT-5.4* 和 *MiniMax M2.7* 底座上进行评测。

<table>
  <tr>
    <td align="center" width="50%">
      <img src="assets/images/result_radar.png" width="100%" alt="工具使用效率雷达图"/><br/>
      <sub><b>工具使用效率雷达图。</b>GA 在 Token、请求数和工具调用轴上全面领先，同时在四个任务维度上保持质量。</sub>
    </td>
    <td align="center" width="50%">
      <img src="assets/images/result_convergence.png" width="100%" alt="跨任务自我进化收敛曲线"/><br/>
      <sub><b>跨任务自我进化。</b>GA 的第二轮和第三轮执行在 8 个 Web 任务上收敛至稳定的低成本区间。</sub>
    </td>
  </tr>
</table>

---

## 📅 路线图与最新动态

- **2026-05-23** — 🆕 **TUI v3 正式发布**（`frontends/tui_v3.py`）。基于块的滚屏回看 + 正确的 resize 重排，每终端独立配色保证跨终端一致，并与 v2 达成功能对齐。
- **2026-05-18** — 🆕 **Morphling 模式**。项目级能力吞噬 —— 从任意外部仓库抽取目标与测例后，对每个核心组件分别决定调用、重写或舍弃。详见 `memory/morphling_sop.md`。
- **2026-05-17** — 🆕 **Goal Hive 模式**。多 worker 协作版 Goal —— Master/Worker 通过 BBS 协同推进长程目标。详见 `memory/goal_hive_sop.md`。
- **2026-05-15** — 🖥️ **桌面 GUI 发布**。一键安装会自带可直接运行的桌面端（`frontends/GenericAgent.exe`），开发者也可用 `python launch.pyw` 启动。
- **2026-05-14** — 🆕 **Conductor 子 Agent 编排**。派发、监督、自动清理并行子 Agent；与 `/btw` 旁路子 Agent 互补，提供一等公民级的任务委派原语。
- **2026-05-12** — 🆕 **TUI v2 正式发布**（`frontends/tuiapp_v2.py`）。重做视觉风格的 Textual 前端，支持图片粘贴折叠、文件粘贴、块删除、Ctrl+C 复制、历史导航，以及 `/llm` / `/export` / `/continue` 选择器。
- **2026-05-08** — 🆕 **Goal 模式**（`reflect/goal_mode.py`）。时间预算驱动的自驱循环 —— "持续优化 X N 小时"，预算没到不准提前交付。
- **2026-04-21** — 📄 [**技术报告已发布至 arXiv**](https://arxiv.org/abs/2604.17091) — *GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization*。
- **2026-04-11** — 引入 **L4 会话归档记忆**，并接入 scheduler cron 调度。
- **2026-03-23** — 支持个人微信接入作为 Bot 前端。
- **2026-03-10** — [发布百万级 Skill 库](https://mp.weixin.qq.com/s/q2gQ7YvWoiAcwxzaiwpuiQ?scene=1&click_id=7)。
- **2026-03-08** — [发布以 GenericAgent 为核心的"政务龙虾" Dintal Claw](https://mp.weixin.qq.com/s/eiEhwo-j6S-WpLxgBnNxBg)。
- **2026-03-01** — [被机器之心报道](https://mp.weixin.qq.com/s/uVWpTTF5I1yzAENV_qm7yg)。
- **2026-01-16** — GenericAgent **V1.0** 公开版本发布。

---

## ⭐ 社区与支持

如果这个项目对你有帮助，欢迎点一个 **Star!** 🙏

也欢迎加入 **GenericAgent 体验交流群**，一起交流、反馈、共建 👏

<div align="center">
  <table>
    <tr>
      <td align="center"><strong>微信群 20</strong><br/><img src="assets/images/wechat_group20.jpg" alt="微信群 20 二维码" width="240"/></td>
    </tr>
  </table>
</div>

### 🚩 友情链接

感谢 **LinuxDo** 社区的支持！

[![LinuxDo](https://img.shields.io/badge/社区-LinuxDo-blue?style=for-the-badge)](https://linux.do/)

**社区 GUI 客户端** *（独立开源项目）*：

- [chilishark27/ga-manager](https://github.com/chilishark27/ga-manager)
- [wangjc683/galley](https://github.com/wangjc683/galley)
- [FroStorM/A3Agent](https://github.com/FroStorM/A3Agent/tree/workbench)

---

## 📄 许可

基于 **MIT License** 发布，详见 [`LICENSE`](LICENSE)。

> *声明：本项目未构建任何商业站点；除 DintalClaw 外，目前未官方授权任何机构、组织或个人以 GenericAgent 名义从事商业活动。*
</antml>