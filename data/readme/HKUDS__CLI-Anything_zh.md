# CLI-Anything：让所有软件具备 AI 智能体（Agent）原生能力

<div align="center">
<a href="https://trendshift.io/repositories/22991" target="_blank"><img src="https://trendshift.io/api/badge/repositories/22991" alt="HKUDS%2FCLI-Anything | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</div>

<p align="center">
  <strong>今天的软件服务于人类👨‍💻。明天的用户将是智能体🤖。<br>
CLI-Anything：弥合 AI 智能体与世界软件之间的鸿沟</strong><br>
</p>

**🌐 [CLI-Hub](https://hkuds.github.io/CLI-Anything/)**：执行 `pip install cli-anything-hub`，然后运行 `cli-hub install <name>` —— 浏览、安装并管理所有社区构建的 CLI。想要添加你自己的工具？[提交 PR](https://github.com/HKUDS/CLI-Anything/blob/main/CONTRIBUTING.md)——Hub 会即时更新。

**🎬 [查看演示](#-真实世界演示)**：观看 AI 智能体如何使用生成的 CLI，结合预览、实时预览和轨迹循环生成实际产物——CAD 构建、3D 场景、图表、游戏玩法、字幕等。

**🙋 [成为贡献者或请求开发 CLI]**：[加入我们](https://github.com/HKUDS/CLI-Anything/issues/new?template=contributor-signup.yml)! 注册以构建新的 CLI 框架——审核合并后，你将成为社区贡献者之一！希望 CLI-Anything 支持特定软件或服务？提交一份 [愿望清单请求](https://github.com/HKUDS/CLI-Anything/issues/new?template=cli-wishlist.yml)!

<p align="center">
  <a href="#-快速开始"><img src="https://img.shields.io/badge/Quick_Start-5_min-blue?style=for-the-badge" alt="Quick Start"></a>
  <a href="https://hkuds.github.io/CLI-Anything/"><img src="https://img.shields.io/badge/CLI_Hub-Browse_%26_Install-ff69b4?style=for-the-badge" alt="CLI Hub"></a>
  <a href="#-demonstrations"><img src="https://img.shields.io/badge/Demos-18_Apps-green?style=for-the-badge" alt="Demos"></a>
  <a href="#-test-results"><img src="https://img.shields.io/badge/Tests-2%2C461_Passing-brightgreen?style=for-the-badge" alt="Tests"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache_2.0-yellow?style=for-the-badge" alt="License"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-≥3.10-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/click-≥8.0-green" alt="Click">
  <img src="https://img.shields.io/badge/pytest-100%25_pass-brightgreen" alt="Pytest">
  <img src="https://img.shields.io/badge/coverage-unit_%2B_e2e-orange" alt="Coverage">
  <img src="https://img.shields.io/badge/output-JSON_%2B_Human-blueviolet" alt="Output">
  <a href="https://github.com/HKUDS/.github/blob/main/profile/README.md"><img src="https://img.shields.io/badge/Feishu-Group-E9DBFC?style=flat&logo=feishu&logoColor=white" alt="Feishu"></a>
<a href="https://github.com/HKUDS/.github/blob/main/profile/README.md"><img src="https://img.shields.io/badge/WeChat-Group-C5EAB4?style=flat&logo=wechat&logoColor=white" alt="WeChat"></a>
</p>

**一条命令行**：让任何软件为 Pi、OpenClaw、nanobot、Cursor、Claude Code 等智能体做好准备。 [**中文文档**](README_CN.md) | [**日本語ドキュメント**](README_JA.md) | [**Deutsch**](README_DE.md)

<p align="center">
  <img src="assets/cli-typing.gif" alt="CLI-Anything typing demo" width="800">
</p>

<p align="center">
  <img src="assets/teaser.png" alt="CLI-Anything Teaser" width="800">
</p>

---

## 📰 更新日志

> 感谢社区所有宝贵的贡献！更多更新正在持续发布中...

- **2026-05-30** 🧭 **Hermes skill** 提案 (#320)，新增 CLI-Anything 编排技能，包含安装脚本与 HARNESS fallback 指引。🗺️ **ArcGIS Pro** 已提交至公开注册表 (#318)，作为面向 Windows/ArcPy 的制图、地理处理、要素编辑及 live-Pro MCP 工作流的 CLI。

- **2026-05-27** 🔧 **CLI-Hub** 注册表日期更新现已支持 `python -m pip` 安装命令 (#312)，改进了注册表自动化的包日期检测功能。

- **2026-05-23** 📝 **Obsidian Agent CLI** 已提交至公开注册表 (#307)，提供通过 PyPI 安装的 Obsidian 自动化 CLI，具备持久化智能体记忆工作流及固定技能链接。

- **2026-05-21** 🔒 **Sketch CLI** 的 token-file 处理已加固，防止路径遍历和符号链接逃逸 (#304)。

- **2026-05-20** 📓 **Joplin CLI** 已提交 (#300)，支持笔记本、笔记、待办事项、标签、附件、搜索/同步、导入/导出、服务器/E2EE 辅助工具，附带完整文档、打包技能文档及 134 项测试验证基线。

- **2026-05-20** 🎛️ **Rekordbox CLI** 已合并 (#252)，包含受保护的 SQLCipher 写入路径、强制备份写入、冒烟测试覆盖及根技能同步。📚 **Calibre CLI** 已合并 (#223)，支持库/搜索/元数据/转换/导出工作流，41 项单元测试，真实 Calibre E2E 证据及根技能验证。🧊 **3MF CLI** 已合并 (#209)，支持网格检查、孔洞重缩放、修复、对比及保留三角形属性。🎙️ **MiniMax CLI** 已合并 (#189)，支持聊天/TTS 工作流、JSON 安全的模型/语音列表、REPL 引用处理及冒烟/E2E 覆盖。🎮 **UEAtelier** 加入注册表 (#297)，作为 Unreal Editor MCP 自扩展工作台，提供 Python CLI 代理。

- **2026-05-19** 🛠️ 现有框架完成质量/安全审查 —— **Zoom** 支持从直接 URL 下载录制文件 (#294)，**Obsidian** 搜索现使用 Local REST API 供应商内容类型 (#289)，**LibreOffice** 无头转换在 macOS 上更稳健 (#290)，XML/SVG/ODF/MLT/MusicXML/CSL 解析现已通过 `defusedxml` 路由不受信任的输入 (#296)。

- **2026-05-18** 📈 README 演示刷新，新增 Trendshift 徽章并优化居中项目头部 (#285, #286)，使着陆页更聚焦于发现与项目动态。

- **2026-05-17** 🌐 **CLI-Hub** 注册表处理已加固 (#281) —— 注册表条目现在会在 `_source` 标记前复制，防止缓存或模拟的注册表数据被原地修改。

- **2026-05-16** 🔧 **n8n** 获得了 REPL 横幅崩溃修复（随后合并至主分支）(#280)，恢复了无子命令的交互式启动路径及回归测试覆盖。

<details>
<summary>早期更新 (4月10日–18日)</summary>

- **2026-04-18** 🧩 **所有 SKILL.md 文件现已统一至顶层 `skills/` 目录** —— 每个 CLI 技能均可通过单一标准源安装：`npx skills add HKUDS/CLI-Anything --skill <skill-name> -g -y`。我们新增了根技能验证 CI，同步了贡献/PR 文档及 REPL 技能路径提示至新布局，并围绕新的 `npx skills` 流程刷新了 **CLI-Hub** 安装前端。

- **2026-04-17** 🌐 **CLI-Hub** 获得另一轮安装体验优化 —— 公开注册表元数据与技能覆盖范围收紧，访问计数修正，Web Hub 进一步打磨。🧪 **Shotcut** 渲染输出时长已修复 (#92)。📝 **SKILL** 贡献路径已针对新文档流程修正 (#224)，技能生成器现安全处理空简介 (#203)。

- **2026-04-16** 🗺️ **QGIS CLI** 已合并 (#207) —— 完整的 GIS/地图创作框架落地。🧬 **UniMol Tools CLI** 已合并 (#219)，面向分子建模工作流。🌐 **CLI-Hub** 新增更多公开 CLI，包括 **py4csr**，刷新了生成的元技能，修正了 SKILL 贡献文档，并修复了技能生成中的 `apt-get` 包提取问题 (#204)。

- **2026-04-16** 📈 **Unreal Insights CLI** 扩展 —— 新增后台捕获会话控制 (`capture start/status/snapshot/stop`)、引擎根目录匹配的 `UnrealInsights.exe` 解析/构建流程，并刷新了新编排工作流的文档与测试。

- **2026-04-15** 🌐 **CLI-Hub** 更新至 **v0.2.0** —— PyPI 包现支持来自多个安装源的公开 CLI（`pip`, `npm`, `brew`, bundled/system tools），由新的 `public_registry.json` 提供支持。Hub 前端重新设计，分为 **CLI-Anything CLIs** 和 **Public CLIs** 两个板块，实时端到端检查现在覆盖 pip 与 npm 包的真实安装、更新和卸载流程。

- **2026-04-14** 🧭 **Safari CLI** 已合并 (#212) 并加入 Hub 注册表 —— 通过 `safari-mcp` 实现浏览器自动化。🎬 **Kdenlive** 也获得了 Gen 5 项目输出兼容修复及无效项目生成处理。

- **2026-04-13** 📓 **Obsidian CLI** 已合并 (#211) —— 通过 Local REST API 实现知识管理框架，含 48 项单元测试与 7 项 E2E 测试。⛓️ **Eth2-Quickstart CLI** 已合并 (#195) —— Ethereum 质押节点管理框架。📚 **Zotero CLI** 更新至 v0.4.1 (#201) —— 现从其独立仓库发布，CLI-Hub 新增对远程 `skill_md` URL 的支持。

- **2026-04-11** 🔗 **n8n CLI** 已合并 (#188) —— 面向自托管自动化流的流程自动化框架。🔧 **Exa CLI** 修复 (#205) 添加了 `x-exa-integration` 头部以用于使用量追踪。📦 **CLI-Hub** 新增 PyPI 自动发布工作流与包刷新流水线。

- **2026-04-10** 📦 **CLI-Hub 包管理器** 上线 —— `pip install cli-anything-hub` 即可通过一条命令浏览、搜索、安装、更新和卸载 CLI-Anything 框架及第三方公开 CLI。Web Hub 也发布了首次以安装为导向的前端刷新与“赋能自我”工具卡。

</details>

<details>
<summary>早期更新 (4月1日–9日)</summary>

- **2026-04-09** 🧹 清理与文档优化 (#200) —— 修复 Openscreen 测试小计，将 Openscreen 加入中文 README 与项目结构，并澄清了文档中的 `/cli-anything` 命令语法。

- **2026-04-08** 🎬 **Openscreen CLI** 已合并 (#183) —— 屏幕录制编辑器框架，含 101 项测试。☁️ **CloudAnalyzer CLI** 已合并 (#181) —— 云成本分析框架，含 27 条命令。🌊 **SeaClip / PM2 / ChromaDB** 框架已合并 (#129)。

- **2026-04-07** 🔄 **Dify Workflow CLI** 已合并 (#191) —— 工作流自动化包装器。🔧 **Inkscape** 自动保存修复 (#193, fixes #182)。🛡️ **DomShell 安全加固** (#156) —— 浏览器 URL 验证与 DOM 清理。🥧 **Pi Coding Agent 扩展** 已合并 (#178)。

- **2026-04-06** 🔍 **Exa CLI** 已合并 (#172) —— AI 驱动的网络搜索与问答框架。🎮 **Godot CLI** 已合并 (#140) —— 游戏引擎框架，含完整演示游戏 E2E 流水线。☁️ **CloudAnalyzer** 审查修复与前端改进也已落地。

- **2026-04-03** 🧪 **WireMock CLI** 已合并 (#170) —— API 测试用 HTTP Mock 服务器框架。🥧 **Pi Coding Agent** 扩展支持也已落地，文档新增 CLI 演示录屏。

- **2026-04-01** ⚔️ **Slay the Spire II CLI** 已合并 (#148) —— 卡牌构建 Roguelike 框架。🎥 **VideoCaptioner CLI** 已合并 (#166) —— AI 驱动的视频字幕生成框架。🛰️ **IntelWatch** 加入注册表，面向 B2B OSINT 工作流。

</details>

<details>
<summary>早期更新 (3月23日–30日)</summary>

- **2026-03-30** 🏗️ **CLI-Anything v0.2.0** —— HARNESS.md 渐进式披露重构。详细指南提取至 `guides/` 按需加载。阶段 1–7 现已连续。核心原则与规则合并为单一权威章节。

- **2026-03-29** 📐 Blender 技能文档更新 —— 强制使用绝对渲染路径并修正前置条件。

- **2026-03-28** 🌐 **CLIBrowser** 加入 CLI-Hub 注册表，提供智能体可访问的浏览器自动化支持。

- **2026-03-27** 📚 Zotero SKILL.md 增强面向智能体的约束；修复 REPL 配置与可执行文件解析。

- **2026-03-26** 📖 **Zotero CLI** 框架落地（支持库管理、集合、引用）。Draw.io 自定义 ID Bug 修复 (#132) 及 registry.json 语法修复。

- **2026-03-25** 🎮 **RenderDoc CLI** 合并，用于 GPU 帧捕获分析。FreeCAD 更新至 v1.1。Blender EEVEE 引擎名称修正。Zoom token 权限加固。

- **2026-03-24** 🏭 **FreeCAD CLI** 新增，涵盖 17 个组共 258 条命令。**iTerm2** 与 **Teltonika RMS** 框架加入注册表。

- **2026-03-23** 🤖 发布 **CLI-Hub 元技能** —— 智能体现可自主发现并安装 CLI。**Krita CLI** 框架合并，支持数字绘画。

</details>

<details>
<summary>早期更新 (3月11日–22日)</summary>

- **2026-03-22** 🎵 **MuseScore CLI** 已合并，支持转调、导出与乐器管理。

- **2026-03-21** 🔧 基础设施改进 —— 优化多个 CLI 的测试框架与文档。提升部分后端在 Windows 上的兼容性。

- **2026-03-20** 🌐 **Novita AI** CLI 新增，支持 OpenAI 兼容 API 访问。注册表元数据优化以改善 Hub 发现体验。

- **2026-03-19** 📦 框架包结构优化。SKILL.md 生成改进，提供更完善的命令文档。

- **2026-03-18** 🧪 测试覆盖扩展 —— 多个 CLI 新增 E2E 场景与边界情况验证。

- **2026-03-17** 🌐 发布 **[CLI-Hub](https://hkuds.github.io/CLI-Anything/)** —— 中央注册表，你可通过一条 `pip` 命令浏览、搜索并安装任何 CLI。

- **2026-03-16** 🤖 新增 **SKILL.md 生成** (阶段 6.5) —— 每个生成的 CLI 现附带 AI 可发现技能定义。

- **2026-03-15** 🐾 社区支持 **OpenClaw**！合并 Windows `cygpath` 守卫以支持跨平台运行。

- **2026-03-14** 🔒 修复 GIMP Script-Fu 路径注入漏洞，新增 **日文 README** 翻译。

- **2026-03-13** 🔌 **Qodercli** 插件作为社区贡献正式合并，附带专用安装脚本。

- **2026-03-12** 📦 **Codex skill** 集成落地，将 CLI-Anything 带入另一款 AI 编码平台。

- **2026-03-11** 📞 **Zoom** 视频会议框架作为第 11 个支持应用加入。

</details>

---

## 🤔 为什么是 CLI？

CLI 是人类与 AI 智能体的通用接口：

• **结构化且可组合** - 文本命令匹配 LLM 格式，可链式调用以构建复杂工作流
• **轻量级且通用** - 开销极小，无需依赖即可在所有系统上运行
• **自描述性** - `--help` 标志提供智能体可自动发现的文档
• **已验证的成功** - Claude Code 每日通过 CLI 运行数千个真实工作流
• **面向智能体的设计** - 结构化 JSON 输出消除了解析复杂性
• **确定性且可靠** - 一致的结果使智能体行为可预测

## 🚀 快速开始

CLI-Anything 提供两个同样实用的起点：

| 目标 | 从这里开始 |
|------|------------|
| **立即使用现有 CLI 生态** | 安装 `cli-anything-hub`，浏览注册表并安装现成 CLI。 |
| **构建新的智能体原生 CLI** | 为你的智能体安装 CLI-Anything 插件/技能，然后运行 7 阶段框架生成器。 |

<details open>
<summary><strong>阶段 1：赋能你自己 —— 你的 CLI 工具包</strong></summary>

首先安装 CLI-Hub 包管理器。它允许你通过一条命令浏览、搜索、检查、安装、更新、卸载和启动 CLI-Anything 框架以及第三方公开 CLI。

**PIP**

```bash
pip install cli-anything-hub
```

| 命令 | 功能 |
|---------|--------------|
| `cli-hub list` | 浏览注册表 |
| `cli-hub search <query>` | 按关键词搜索 |
| `cli-hub info <name>` | 检查单个 CLI |
| `cli-hub install <name>` | 从 CLI-Hub 安装 |
| `cli-hub update <name>` | 更新已安装的包 |
| `cli-hub uninstall <name>` | 卸载已安装的包 |
| `cli-hub launch <name> [args...]` | 运行已安装的 CLI |

```bash
# 浏览可用内容
cli-hub list
cli-hub search image

# 立即安装并试用一个 CLI
cli-hub install gimp
cli-hub info gimp
cli-hub launch gimp
```

> 部分 CLI 包装了真实的桌面或后端软件。如果选定的 CLI 需要 GIMP、Blender、LibreOffice 或其他上游工具，请同时安装该上游应用程序。

</details>

<details open>
<summary><strong>阶段 1.5：赋能你的智能体 —— 一条命令完成安装</strong></summary>

为兼容 SKILL 的智能体提供 CLI-Hub 元技能，使其能够发现并安装任务所需的正确 CLI。

**也可通过以下平台获取：** [ClawHub](https://clawhub.ai/yuh-yang/cli-anything-hub), [SkillHub](https://www.skillhub.club/web/skills/itsyuhao-cli-anything-hub), [SkillHub.cn](https://skillhub.cn/skills/cli-hub-meta-skill)

**NPX SKILLS**

```bash
npx skills add HKUDS/CLI-Anything --skill cli-hub-meta-skill -g -y
```

**兼容平台：** OpenClaw, Nanobot, Claude Code, Codex, Antigravity 及其他支持 SKILL 的智能体。

然后输入提示词：

```text
Find appropriate CLI software in CLI-Hub and complete the task: ...
```

</details>

<details open>
<summary><strong>阶段 3：注册表中尚无时，构建新 CLI</strong></summary>

当你需要为尚未通过 CLI-Hub 提供的软件、代码库或内部工具创建新框架时，使用 CLI-Anything 生成器。

**前置条件**

- **Python 3.10+**
- 目标软件或源码仓库可在本地或在线获取
- 支持的 AI 编码智能体：[Claude Code](#-claude-code) | [Pi](#-pi-coding-agent) | [OpenClaw](#-openclaw) | [OpenCode](#-opencode) | [Codex](#-codex) | [Hermes](#-hermes) | [Qodercli](#-qodercli) | [GitHub Copilot CLI](#-github-copilot-cli) | [更多平台](#-more-platforms-coming-soon)

### 选择你的智能体平台

<details open>
<summary><h4 id="-claude-code">⚡ Claude Code</h4></summary>

**步骤 1：添加市场**

CLI-Anything 作为 Claude Code 插件市场托管在 GitHub 上分发。

```bash
# 添加 CLI-Anything 市场
/plugin marketplace add HKUDS/CLI-Anything
```

**步骤 2：安装插件**

```bash
# 从市场安装 cli-anything 插件
/plugin install cli-anything
```

至此完成。该插件现已在你的 Claude Code 会话中可用。

> **Windows 用户注意**：Claude Code 通过 `bash` 运行 Shell 命令。在 Windows 上，请安装 Git for Windows（包含 `bash` 和 `cygpath`）或使用 WSL；否则命令可能会因找不到 `cygpath` 而失败。

**步骤 3：一条命令构建 CLI**

```bash
# /cli-anything <software-path-or-repo>
# 为 GIMP 生成完整 CLI（全部 7 个阶段）
/cli-anything ./gimp
```

Claude Code 版本兼容性说明：
- 使用 `/cli-anything` 作为主要入口。
- 在较旧构建版中，若确认插件已安装并加载后仍无法识别 `/cli-anything`，请尝试遗留表单 `/cli-anything:cli-anything`。
- 辅助命令保持 `:subcommand` 格式（例如 `/cli-anything:refine`）。

若提示 `Unknown skill: cli-anything`，请优先关注插件安装/加载（两种入口均引用同一技能，切换形式无济于事）：
1. 重载插件命令：`/reload-plugins`
2. 验证插件已加载：`/help cli-anything`（应显示 CLI-Anything 帮助/命令）
3. 如需重新安装市场：
   - `/plugin marketplace add HKUDS/CLI-Anything`
   - `/plugin install cli-anything`
4. 确认插件可用后重试入口命令：
   - 推荐：`/cli-anything ./gimp`
   - 仅旧版构建：`/cli-anything:cli-anything ./gimp`

此流程运行完整管线：
1. 🔍 **分析** —— 扫描源码，将 GUI 操作映射至 API
2. 📐 **设计** —— 架构命令组、状态模型、输出格式
3. 🔨 **实现** —— 构建带 REPL、JSON 输出、撤销/重做的 Click CLI
4. 📋 **规划测试** —— 创建含单元+E2E 测试计划的 TEST.md
5. 🧪 **编写测试** —— 实现全面测试套件
6. 📝 **文档化** —— 用结果更新 TEST.md
7. 📦 **发布** —— 生成 `setup.py`，安装至 PATH

**步骤 4（可选）：优化与改进 CLI**

初始构建完成后，你可迭代优化 CLI 以扩展覆盖范围并补充缺失功能：

```bash
# 广泛优化 —— 智能体分析所有能力缺口
/cli-anything:refine ./gimp

# 聚焦优化 —— 针对特定功能领域
/cli-anything:refine ./gimp "I want more CLIs on image batch processing and filters"
```

`refine` 命令会执行软件完整能力与当前 CLI 覆盖范围的差距分析，然后为识别出的缺口实现新命令、测试和文档。你可多次运行以稳步扩展覆盖范围 —— 每次运行均为增量且非破坏性。

<details>
<summary><strong>备选：手动安装</strong></summary>

若你偏好不使用市场：

```bash
# 克隆仓库
git clone https://github.com/HKUDS/CLI-Anything.git

# 将插件复制至 Claude Code 插件目录
cp -r CLI-Anything/cli-anything-plugin ~/.claude/plugins/cli-anything

# 重载插件
/reload-plugins
```

</details>

</details>

<details>
<summary><h4 id="-pi-coding-agent">⚡ Pi Coding Agent</h4></summary>

**步骤 1：安装扩展**

该扩展位于本仓库的 `.pi-extension/cli-anything/`。全局安装后，所有 Pi 项目均可使用 `/cli-anything` 命令：

```bash
# 克隆仓库
git clone https://github.com/HKUDS/CLI-Anything.git
cd CLI-Anything

# 全局安装至 Pi 扩展目录
bash .pi-extension/cli-anything/install.sh
```

卸载方法：

```bash
bash .pi-extension/cli-anything/install.sh --uninstall
```

> **工作原理**：`install.sh` 将扩展文件（包括 HARNESS.md、命令、指南、脚本及 `cli-anything-plugin/` 中的模板）复制至 `~/.pi/agent/extensions/cli-anything/`，Pi 启动时会自动发现。在 Pi 中运行 `/reload` 或重启 Pi 即可激活。

**步骤 2：一条命令构建 CLI**

扩展加载后，以下命令可用：

```bash
# 为 GIMP 生成完整 CLI（全部 7 个阶段）
/cli-anything ./gimp

# 从 GitHub 仓库构建
/cli-anything https://github.com/blender/blender
```

**步骤 3（可选）：优化与改进 CLI**

```bash
# 广泛优化 —— 智能体分析所有能力缺口
/cli-anything:refine ./gimp

# 聚焦优化 —— 针对特定功能领域
/cli-anything:refine ./gimp "batch processing and filters"
```

**可用命令**

| 命令 | 描述 |
|---------|-------------|
| `/cli-anything <path-or-repo>` | 构建完整 CLI 框架 |
| `/cli-anything:refine <path> [focus]` | 优化现有 CLI 框架 |
| `/cli-anything:test <path-or-repo>` | 运行 CLI 框架测试 |
| `/cli-anything:validate <path-or-repo>` | 验证 CLI 框架 |
| `/cli-anything:list [options]` | 列出所有 CLI-Anything 工具 |

</details>

<details>
<summary><h4 id="-opencode">⚡ OpenCode (实验性)</h4></summary>

**步骤 1：安装命令**

> **注意**：请升级至最新版 OpenCode。旧版可能使用不同的命令路径。

将 CLI-Anything 命令与 `HARNESS.md` 一并复制至你的 OpenCode 命令目录：

```bash
# 克隆仓库
git clone https://github.com/HKUDS/CLI-Anything.git

# 全局安装（所有项目可用）
cp CLI-Anything/opencode-commands/*.md ~/.config/opencode/commands/
cp CLI-Anything/cli-anything-plugin/HARNESS.md ~/.config/opencode/commands/

# 或项目级安装
cp CLI-Anything/opencode-commands/*.md .opencode/commands/
cp CLI-Anything/cli-anything-plugin/HARNESS.md .opencode/commands/
```

> **注意**：请升级至最新版 OpenCode。旧版使用 `command/`（单数）而非 `commands/`。若不存在 `commands/`，全局与项目级安装均请使用 `command/`。

> **注意**：`HARNESS.md` 是所有命令引用的方法论规范。它必须与命令位于同一目录。

此操作将新增 5 条斜杠命令：`/cli-anything`, `/cli-anything-refine`, `/cli-anything-test`, `/cli-anything-validate`, 和 `/cli-anything-list`。

**步骤 2：一条命令构建 CLI**

```bash
# 为 GIMP 生成完整 CLI（全部 7 个阶段）
/cli-anything ./gimp

# 从 GitHub 仓库构建
/cli-anything https://github.com/blender/blender
```

该命令作为子任务运行，遵循与 Claude Code 相同的 7 阶段方法论。

**步骤 3（可选）：优化与改进 CLI**

```bash
# 广泛优化 —— 智能体分析所有能力缺口
/cli-anything-refine ./gimp

# 聚焦优化 —— 针对特定功能领域
/cli-anything-refine ./gimp "batch processing and filters"
```

</details>

<details>
<summary><h4 id="-goose">⚡ Goose (桌面 / CLI) <sup><code>实验性</code></sup> <sup><code>社区</code></sup></h4></summary>

**步骤 1：安装 Goose**

使用官方说明为你的操作系统安装 Goose（桌面版或 CLI）。

**步骤 2：配置 CLI 提供者**

配置 Goose 使用如 Claude Code 等 CLI 提供者，并确保该 CLI 已安装并认证。

**步骤 3：在 Goose 会话中使用 CLI-Anything**

配置完成后，启动会话并使用上述与 Claude Code 相同的 CLI-Anything 命令，例如：

```bash
/cli-anything ./gimp
/cli-anything:refine ./gimp "batch processing and filters"
```

> 注意：当 Goose 通过 CLI 提供者运行时，它会使用该提供者的能力与命令格式。
</details>

<details>

<summary><h4 id="-qodercli">⚡ Qodercli <sup><code>社区</code></sup></h4></summary>

**步骤 1：注册插件**

```bash
git clone https://github.com/HKUDS/CLI-Anything.git
bash CLI-Anything/qoder-plugin/setup-qodercli.sh
```

此操作会将 cli-anything 插件注册至 `~/.qoder.json`。注册后启动新的 Qodercli 会话。

**步骤 2：从 Qodercli 使用 CLI-Anything**

```bash
/cli-anything ./gimp
/cli-anything:refine ./gimp "batch processing and filters"
/cli-anything:validate ./gimp
```
</details>

<details>

<summary><h4 id="-openclaw">⚡ OpenClaw <sup><code>社区</code></sup></h4></summary>

**步骤 1：安装技能**

CLI-Anything 提供原生 OpenClaw `SKILL.md` 文件。将其复制至你的 OpenClaw 技能目录：

```bash
# 克隆仓库
git clone https://github.com/HKUDS/CLI-Anything.git

# 安装至全局技能文件夹
mkdir -p ~/.openclaw/skills/cli-anything
cp CLI-Anything/openclaw-skill/SKILL.md ~/.openclaw/skills/cli-anything/SKILL.md
```

**步骤 2：构建 CLI**

现在你可于 OpenClaw 内部调用该技能：

`@cli-anything build a CLI for ./gimp`

该技能遵循与 Claude Code 和 OpenCode 相同的 7 阶段方法论。

</details>

<details>

<summary><h4 id="-codex">⚡ Codex <sup><code>实验性</code></sup> <sup><code>社区</code></sup></h4></summary>

**步骤 1：安装技能**

运行内置安装器：

```bash
# 克隆仓库
git clone https://github.com/HKUDS/CLI-Anything.git

# 安装技能
bash CLI-Anything/codex-skill/scripts/install.sh
```

Windows PowerShell 下请使用：

```powershell
.\CLI-Anything\codex-skill\scripts\install.ps1
```

此操作会将技能安装至 `$CODEX_HOME/skills/cli-anything`（若未设置 `CODEX_HOME` 则为 `~/.codex/skills/cli-anything`）。

安装后重启 Codex 以使其被识别。

**步骤 2：从 Codex 使用 CLI-Anything**

用自然语言描述任务，例如：

```text
Use CLI-Anything to build a harness for ./gimp
Use CLI-Anything to refine ./shotcut for picture-in-picture workflows
Use CLI-Anything to validate ./libreoffice
```

Codex 技能适配了 Claude Code 插件与 OpenCode 命令使用的相同方法论，同时保持生成的 Python 框架格式不变。
</details>

<details>

<summary><h4 id="-hermes">⚡ Hermes <sup><code>实验性</code></sup> <sup><code>社区</code></sup></h4></summary>

**步骤 1：安装技能**

运行内置安装器：

```bash
# 克隆仓库
git clone https://github.com/HKUDS/CLI-Anything.git

# 安装技能
bash CLI-Anything/hermes-skill/scripts/install.sh
```

Windows PowerShell 下请使用：

```powershell
.\CLI-Anything\hermes-skill\scripts\install.ps1
```

此操作会将技能安装至 `$HERMES_HOME/skills/cli-anything-hermes`（若未设置 `HERMES_HOME` 则为 `~/.hermes/skills/cli-anything-hermes`）。

安装后重启 [Hermes Agent](https://github.com/NousResearch/hermes-agent) 以使其被识别。

**步骤 2：从 Hermes 使用 CLI-Anything**

用自然语言描述任务，例如：

```text
Use CLI-Anything to build a harness for ./gimp
Use CLI-Anything to refine ./shotcut for picture-in-picture workflows
Use CLI-Anything to validate ./libreoffice
```

Hermes 技能适配了 Claude Code 插件与 Codex 技能使用的相同方法论，将 Hermes 的 `terminal`, `execute_code`, `delegate_task` 及 `read_file` / `write_file` / `patch` 工具绑定至 7 阶段框架工作流，同时保持生成的 Python 框架格式不变。
</details>

<details>

<summary><h4 id="-github-copilot-cli">⚡ GitHub Copilot CLI <sup><code>社区</code></sup></h4></summary>

**步骤 1：安装插件**

```bash
git clone https://github.com/HKUDS/CLI-Anything.git
cd CLI-Anything
copilot plugin install ./cli-anything-plugin
```

此操作会将 CLI-Anything 插件安装至 GitHub Copilot CLI。该插件现已在你的会话中可用。

**步骤 2：从 GitHub Copilot CLI 使用 CLI-Anything**

```bash
/cli-anything ./gimp
/cli-anything:refine ./gimp "batch processing and filters"
/cli-anything:validate ./gimp
```

</details>

<details>
<summary><h4 id="-more-platforms-coming-soon">🔮 更多平台（即将推出）</h4></summary>

CLI-Anything 设计为跨平台兼容。计划支持更多 AI 编码智能体：

- **Codex** —— 可通过 `codex-skill/` 中的内置技能获取
- **Cursor** —— 即将推出
- **Windsurf** —— 即将推出
- **你最喜欢的工具** —— 欢迎贡献！参见 `opencode-commands/` 目录获取参考实现。

</details>

### 使用生成的 CLI

无论使用何种平台构建，生成的 CLI 工作方式均相同：

```bash
# 安装至 PATH
cd gimp/agent-harness && pip install -e .

# 从任意位置使用
cli-anything-gimp --help
cli-anything-gimp project new --width 1920 --height 1080 -o poster.json
cli-anything-gimp --json layer add -n "Background" --type solid --color "#1a1a2e"

# 进入交互式 REPL
cli-anything-gimp
```

每个仓库内的框架现均在 `skills/cli-anything-<software>/SKILL.md` 拥有标准 [`SKILL.md`](#-skillmd-generation)。这使得单体仓库可通过 `npx skills add HKUDS/CLI-Anything --list` 直接发现。已安装的框架包仍在 `cli_anything/<software>/skills/SKILL.md` 提供兼容副本，REPL 横幅优先使用仓库根目录的标准文件（若存在），否则回退至打包副本。

</details>

---

## 🤖 通过 CLI-Hub 赋能你的智能体

CLI-Hub 让智能体自主发现、安装并使用所需的 CLI。

```bash
npx skills add HKUDS/CLI-Anything --skill cli-hub-meta-skill -g -y
```

**也可通过以下平台获取：** [ClawHub](https://clawhub.ai/yuh-yang/cli-anything-hub), [SkillHub](https://www.skillhub.club/web/skills/itsyuhao-cli-anything-hub), [SkillHub.cn](https://skillhub.cn/skills/cli-hub-meta-skill)

然后输入提示词：

```text
Find appropriate CLI software in CLI-Hub and complete the task: ...
```

元技能会将智能体指向实时 CLI-Hub 目录，在其中它们可选择 CLI、安装它并读取其自身的 `SKILL.md` 以获取特定任务的使用说明。

---

## 💡 CLI-Anything 的愿景：构建智能体原生软件

• 🌐 **通用访问** - 通过结构化 CLI，任何软件均可瞬间被智能体控制。
• 🔗 **无缝集成** - 智能体无需 API、GUI、重建或复杂包装即可控制任意应用。
• 🚀 **面向未来的生态** - 一条命令将人类设计的软件转化为智能体原生工具。

---

## 🔧 何时使用 CLI-Anything

| 类别 | 如何成为智能体原生 |  notable 示例 |
|----------|----------------------|----------|
| **📂 GitHub 仓库** | 通过自动生成 CLI，将任何开源项目转化为可被智能体控制工具 | VSCodium, WordPress, Calibre, Zotero, Joplin, Logseq, Penpot, Super Productivity |
| **🤖 AI/ML 平台** | 通过结构化命令自动化模型训练、推理流水线与超参数调优 | Stable Diffusion WebUI, ComfyUI, Ollama, InvokeAI, Text-generation-webui, Open WebUI, Fooocus, Kohya_ss, AnythingLLM, SillyTavern |
| **📊 数据与分析** | 启用编程式数据处理、可视化与统计分析工作流 | JupyterLab, Apache Superset, Metabase, Redash, DBeaver, KNIME, Orange, OpenSearch Dashboards, Lightdash |
| **💻 开发工具** | 通过命令行界面简化代码编辑、构建、测试与部署流程 | Jenkins, Gitea, Hoppscotch, Portainer, pgAdmin, SonarQube, ArgoCD, OpenLens, Insomnia, Beekeeper Studio, **[iTerm2](https://iterm2.com)** |
| **🎨 创意与媒体** | 以编程方式控制内容创作、编辑与渲染工作流 | Blender, GIMP, OBS Studio, Audacity, Krita, Kdenlive, Shotcut, Inkscape, Darktable, LMMS, Ardour |
| **🎮 游戏开发** | 通过无头引擎接口管理游戏项目、场景、导出与脚本 | **[Godot Engine](https://godotengine.org)**, **[s&box](https://sbox.game)** |
| **🔬 科学计算** | 自动化研究工作流、模拟与复杂计算 | ImageJ, FreeCAD, QGIS, ParaView, Gephi, LibreCAD, Stellarium, KiCad, JASP, Jamovi |
| **🏢 企业与办公** | 将商业应用与生产力工具转化为智能体可访问系统 | NextCloud, GitLab, Grafana, Mattermost, LibreOffice, AppFlowy, NocoDB, Odoo (Community), Plane, ERPNext |
| **📞 通信与协作** | 通过结构化 CLI 自动化会议安排、参与者管理、录制检索与报告生成 | Zoom, Jitsi Meet, BigBlueButton, Mattermost |
| **📐 绘图与可视化** | 以编程方式创建与操作图表、流程图、架构图及视觉文档 | Draw.io (diagrams.net), Mermaid, PlantUML, Excalidraw, yEd |
| **🌐 网络与基础设施** | 通过结构化 CLI 命令管理网络服务、DNS、广告拦截与基础设施 | AdGuardHome |
| **🧪 测试与模拟** | 控制 HTTP Mock 服务器，管理测试桩，录制并回放 API 流量以进行集成测试 | **[WireMock](https://wiremock.org)** |
| **🔬 图形学与 GPU 调试** | 分析 GPU 帧捕获、检查管道状态、导出着色器及对比渲染状态 | RenderDoc |
| **🎬 视频与字幕** | 转录语音、翻译字幕、将样式化字幕烧录至视频 —— 完整字幕流水线 | VideoCaptioner |
| **🔍 AI 原生搜索** | 基于嵌入 API 的结构化内容检索，实现神经与深度网络搜索 | [Exa](https://exa.ai) |
| **✨ AI 内容生成** | 通过 AI 驱动的云 API 生成专业交付物（幻灯片、文档、图表、网站、研究报告） | [AnyGen](https://www.anygen.io), Gamma, Beautiful.ai, Tome |

---

## CLI-Anything 的核心特性

### 智能体与软件之间的鸿沟
AI 智能体擅长推理，但不擅长使用真实的商业软件。当前解决方案是脆弱的 UI 自动化、受限的 API，或丢失了 90% 功能的简化版重新实现。

**CLI-Anything 的解决方案**：将任何专业软件转化为智能体原生工具，且不损失功能。

| **当前痛点** | **CLI-Anything 的修复** |
|----------|----------------------|
| 🤖 "AI 无法使用真实工具" | 直接集成实际软件后端（Blender, LibreOffice, FFmpeg）—— 完整专业功能，零妥协 |
| 💸 "UI 自动化频繁崩溃" | 无需截图、点击或 RPA。纯命令行可靠性配合结构化接口 |
| 📊 "智能体需要结构化数据" | 内置 JSON 输出以实现无缝智能体消费 + 人类可读格式用于调试 |
| 🔧 "自定义集成成本高昂" | 一个 Claude 插件通过成熟的 7 阶段流水线为任何代码库自动生成 CLI |
| ⚡ "原型与生产环境的差距" | 2,280+ 项测试配合真实软件验证。已在 18 款主流应用中经历实战考验 |

---

## 🎯 你可以用 CLI-Anything 做什么？

<table>
<tr>
<td width="33%">

### 🛠️ 让智能体接管你的工作流

无论是专业还是日常用途，只需将代码库丢给 `/cli-anything`。GIMP、Blender、Shotcut 用于创意工作。LibreOffice、OBS Studio 用于日常任务。没有源码？找一个开源替代品然后把 *那个* 也丢进去。你将瞬间获得一个智能体可完全使用的完整 CLI。

</td>
<td width="33%">

### 🔗 将分散的 API 统一为一个 CLI

受够了同时处理碎片化的 Web 服务 API？将文档或 SDK 手册喂给 `/cli-anything`，你的智能体将获得一个**强大、有状态且统一的 CLI**，将这些独立端点包装为连贯的命令组。一个工具替代数十个原始 API 调用 —— 能力更强且节省 Token。

</td>
<td width="33%">

### 🚀 替换或超频 GUI 智能体方法

CLI-Anything 可直接 **取代基于 GUI 的智能体方案** —— 不再需要截图，不再依赖脆弱的像素点击。更有趣的是：一旦你通过 `/cli-anything` 处理了 GUI 软件，你就可以完全通过代码和终端来 **合成智能体任务、评估器和基准测试** —— 全自动、可迭代优化、效率提升数个数量级。

</td>
</tr>
</table>

---

## ✨ ⚙️ CLI-Anything 的工作原理

<table>
<tr>
<td width="50%">

### 🏗️ 全自动化 7 阶段流水线
从代码库分析到 PyPI 发布 —— 插件自动完成架构设计、实现、测试规划、测试编写与文档生成。

</td>
<td width="50%">

### 🎯 真实软件集成
直接调用实际应用程序进行真实渲染。LibreOffice 生成 PDF，Blender 渲染 3D 场景，Audacity 通过 sox 处理音频。**零妥协**，**零玩具实现**。

</td>
</tr>
<tr>
<td width="50%">

### 🔁 智能会话管理
持久化项目状态配合撤销/重做功能，以及统一的 REPL 界面（ReplSkin），在所有 CLI 中提供一致的交互体验。

</td>
<td width="50%">

### 📦 零配置安装
简单的 `pip install -e .` 即可将 cli-anything-<software> 直接加入 PATH。智能体通过标准 `which` 命令发现工具。无需设置，无需包装器。

</td>
</tr>
<tr>
<td width="50%">

### 🧪 生产级测试
多层验证：合成数据的单元测试、真实文件与软件的端到端测试，以及安装命令的 CLI 子进程验证。

</td>
<td width="50%">

### 🐍 干净的包架构
所有 CLI 组织于 `cli_anything.*` 命名空间下 —— 无冲突、可 pip 安装，命名一致：cli-anything-gimp, cli-anything-blender 等。

</td>
</tr>
</table>

### 🤖 SKILL.md 生成

每个生成的 CLI 现均在 `skills/cli-anything-<software>/SKILL.md` 拥有标准 `SKILL.md`。这使得当前单体仓库可直接被 `npx skills` 消费，而安装在包内的兼容副本位于 `cli_anything/<software>/skills/SKILL.md`，保留了已安装框架的行为。

**SKILL.md 提供：**
- **YAML frontmatter**：包含名称与描述，供智能体技能发现使用
- **命令组**：记录所有可用子命令
- **使用示例**：常见工作流演示
- **智能体特定指引**：JSON 输出、错误处理及编程式使用说明

SKILL.md 文件在流水线阶段 6.5 期间通过 `skill_generator.py` 自动生成，该生成器直接从 CLI 的 Click 装饰器、setup.py 和 README 中提取元数据。生成器现写入标准仓库根技能文件并刷新已安装框架使用的包内本地兼容副本。在此仓库内部，REPL 横幅将智能体指向标准根技能路径；`pip install` 后则回退至打包副本。

---

## 🎬 真实世界演示

AI 智能体使用生成的 CLI 生成完整、实用的产物 —— 无需 GUI。

### FreeCAD &mdash; 通过预览、实时预览与轨迹构建“好奇号”漫游车

> **框架：** `cli-anything-freecad` | **预览栈：** `preview` + `preview live` + `trajectory.json` | **产物：** 智能体构建的好奇号风格漫游车

智能体逐步组装灵感源自好奇号的漫游车，同时发布真实的 FreeCAD 预览包、刷新实时预览会话，并记录命令到预览的历史以供后续回放。最终演示展示了产物在最终展示前一步步演进的过程。

<p align="center">
  <img src="assets/demos/freecad-curiosity-preview-trajectory.gif" alt="FreeCAD Curiosity rover demo driven by preview, live preview, and trajectory history" width="860" />
</p>

<p align="center">
  <sub>README GIF 通过速度调整的高质量 ffmpeg palette 工作流从完整本地演示视频生成。</sub>
</p>

### Blender &mdash; 通过预览、实时预览与轨迹构建轨道中继无人机

> **框架：** `cli-anything-blender` | **预览栈：** `preview` + `preview live` + `trajectory.json` | **产物：** 智能体构建的轨道中继无人机

智能体使用 Blender 框架在真实预览循环中生长硬表面轨道中继无人机：每个阶段推送新的渲染支持包，实时会话跟踪当前头部状态，轨迹将每条命令与匹配的视觉状态绑定。演示以完成场景准备就绪进行精致旋转展示结束。

<p align="center">
  <img src="assets/demos/blender-orbital-relay-drone-preview-trajectory.gif" alt="Blender orbital relay drone demo driven by preview, live preview, and trajectory history" width="860" />
</p>

<p align="center">
  <sub>README GIF 通过速度调整的高质量 ffmpeg palette 工作流从完整本地演示视频生成。</sub>
</p>

### Draw.io &mdash; HTTPS 握手图表

> **框架：** `cli-anything-drawio` | **耗时：** ~4 分钟 | **产物：** `.drawio` + `.png`

智能体通过 CLI 命令从零创建完整的 HTTPS 连接生命周期图 —— TCP 三次握手、TLS 协商、加密数据交换与 TCP 四次挥手终止。

<p align="center">
  <img src="assets/demos/drawio-demo.gif" alt="Draw.io CLI demo: building an HTTPS handshake diagram" width="720" />
</p>

<details>
<summary>最终产物</summary>
<p align="center">
  <img src="assets/demos/drawio-https-handshake.png" alt="HTTPS handshake sequence diagram" width="600" />
</p>
</details>

*由 [@zhangxilong-43](https://github.com/zhangxilong-43) 贡献*

### Slay the Spire II &mdash; 游戏自动化

> **框架：** `cli-anything-slay-the-spire-ii` | **产物：** 自动化游戏会话

智能体使用 CLI 框架游玩 Slay the Spire II —— 实时读取游戏状态、选择卡牌、选择路径并做出战略决策。

<p align="center">
  <img src="assets/demos/slay-the-spire-ii-gameplay.gif" alt="Slay the Spire II CLI gameplay demo" width="720" />
</p>

*由 [@TianyuFan0504](https://github.com/TianyuFan0504) 贡献*

### VideoCaptioner &mdash; 自动生成字幕

> **框架：** `cli-anything-videocaptioner` | **产物：** 带字幕的视频帧

智能体使用 VideoCaptioner CLI 自动为视频内容生成并叠加样式化字幕，支持双语文本渲染与自定义格式。

<table align="center">
<tr>
<td align="center"><strong>字幕 A</strong></td>
<td align="center"><strong>字幕 B</strong></td>
</tr>
<tr>
<td><img src="assets/demos/videocaptioner-before.png" alt="Video frame before captioning" width="380" /></td>
<td><img src="assets/demos/videocaptioner-after.png" alt="Video frame after captioning" width="380" /></td>
</tr>
</table>

*由 [@WEIFENG2333](https://github.com/WEIFENG2333) 贡献*

### ArcGIS Pro &mdash; 通过 MCP 桥接的实时智能体制图

> **框架：** [`arcgis-pro`](https://github.com/Jasper0122/CLI-Anything-Arcgis-Pro)（已注册于 [`public_registry.json`](public_registry.json)） | **模式：** live-Pro MCP 桥接 | **产物：** 运行中 ArcGIS Pro 会话中的智能体驱动地图导航

智能体通过 MCP 桥接驱动**实时运行的 ArcGIS Pro 会话** —— 读取项目、将地图缩放至要素图层、执行地理处理并导出布局 —— 每一步都在你注视下于 Pro 内部执行。ArcGIS Pro 是 Esri 的商业 GIS 桌面软件（仅 Windows，需授权），因此它包装了其官方 **ArcPy / ArcGIS Pro SDK** 而非从源码生成 —— 相当于 QGIS 框架的 ArcGIS Pro 对应版本。

<p align="center">
  <img src="assets/demos/arcgis-pro-live-bridge-demo.gif" alt="ArcGIS Pro live-bridge demo: an agent driving a running ArcGIS Pro session over MCP" width="860" />
</p>

<p align="center">
  <sub>README GIF 通过高质量 ffmpeg palette 工作流从完整本地演示视频生成。</sub>
</p>

*由 [@Jasper0122](https://github.com/Jasper0122) 贡献*

*更多 CLI 演示即将推出。*

---

## 🎬 演示概览

### 🎯 通用型
CLI-Anything 适用于任何拥有代码库的软件 —— 无领域限制或架构局限。

### 🏭 专业级测试
已在 18 款多样化复杂应用中完成测试，涵盖创意、生产力、通信、绘图、AI 图像生成、AI 内容生成、网络广告拦截、本地 LLM 推理、原生调试及图形分析等领域，这些领域此前对 AI 智能体均不可访问。

### 🎨 跨领域覆盖
从创意工作流（图像处理、3D 建模、矢量图形）到生产工具（音频、办公、直播、视频编辑）。

### ✅ 完整 CLI 生成
每个应用均获得完整的生产就绪型 CLI 接口 —— 不是演示，而是保留全部能力的综合工具访问。

<table>
<tr>
<th align="center">软件</th>
<th align="center">领域</th>
<th align="center">CLI 命令</th>
<th align="center">后端</th>
<th align="center">测试数</th>
</tr>
<tr>
<td align="center"><strong>🎨 GIMP</strong></td>
<td>图像编辑</td>
<td><code>cli-anything-gimp</code></td>
<td>Pillow + GEGL/Script-Fu</td>
<td align="center">✅ 107</td>
</tr>
<tr>
<td align="center"><strong>🧊 Blender</strong></td>
<td>3D 建模与渲染</td>
<td><code>cli-anything-blender</code></td>
<td>bpy (Python scripting)</td>
<td align="center">✅ 208</td>
</tr>
<tr>
<td align="center"><strong>✏️ Inkscape</strong></td>
<td>矢量图形</td>
<td><code>cli-anything-inkscape</code></td>
<td>Direct SVG/XML manipulation</td>
<td align="center">✅ 202</td>
</tr>
<tr>
<td align="center"><strong>🎵 Audacity</strong></td>
<td>音频制作</td>
<td><code>cli-anything-audacity</code></td>
<td>Python wave + sox</td>
<td align="center">✅ 161</td>
</tr>
<tr>
<td align="center"><strong>🌐 Browser</strong></td>
<td>浏览器自动化</td>
<td><code>cli-anything-browser</code></td>
<td>DOMShell MCP + Accessibility Tree</td>
<td align="center">✅ <a href="browser/agent-harness/">New</a></td>
</tr>
<tr>
<td align="center"><strong>📄 LibreOffice</strong></td>
<td>办公套件 (Writer, Calc, Impress)</td>
<td><code>cli-anything-libreoffice</code></td>
<td>ODF generation + headless LO</td>
<td align="center">✅ 158</td>
</tr>
<tr>
<td align="center"><strong>⚡ <a href="n8n/agent-harness/">n8n</a></strong></td>
<td>工作流自动化</td>
<td><code>cli-anything-n8n</code></td>
<td>n8n REST API v1.1.1</td>
<td align="center">✅ <a href="n8n/agent-harness/">55+ cmds</a></td>
</tr>
<tr>
<td align="center"><strong>📧 <a href="mailchimp/agent-harness/">Mailchimp</a></strong></td>
<td>邮件营销与自动化</td>
<td><code>cli-anything-mailchimp</code></td>
<td>Mailchimp Marketing API v3.0</td>
<td align="center">✅ <a href="mailchimp/agent-harness/">303 cmds</a></td>
</tr>
<tr>
<td align="center"><strong>📚 <a href="zotero/agent-harness/">Zotero</a></strong></td>
<td>文献管理</td>
<td><code>cli-anything-zotero</code></td>
<td>Local SQLite + connector + Local API</td>
<td align="center">✅ <a href="zotero/agent-harness/">New</a></td>
</tr>
<tr>
<td align="center"><strong>📖 <a href="calibre/agent-harness/">Calibre</a></strong></td>
<td>电子书库管理</td>
<td><code>cli-anything-calibre</code></td>
<td>calibredb + ebook-convert + ebook-meta</td>
<td align="center">✅ <a href="calibre/agent-harness/">58</a></td>
</tr>
<tr>
<td align="center"><strong>📓 <a href="joplin/agent-harness/">Joplin</a></strong></td>
<td>笔记与待办事项</td>
<td><code>cli-anything-joplin</code></td>
<td>Joplin terminal CLI subprocess</td>
<td align="center">✅ 134</td>
</tr>
<tr>
<td align="center"><strong>📝 <a href="mubu/agent-harness/">Mubu</a></strong></td>
<td>知识管理与大纲</td>
<td><code>cli-anything-mubu</code></td>
<td>Local Mubu data + sync logs</td>
<td align="center">✅ 96</td>
</tr>
<tr>
<td align="center"><strong>📹 OBS Studio</strong></td>
<td>直播与录制</td>
<td><code>cli-anything-obs-studio</code></td>
<td>JSON scene + obs-websocket</td>
<td align="center">✅ 153</td>
</tr>
<tr>
<td align="center"><strong>📱 <a href="nslogger/agent-harness/">NSLogger</a></strong></td>
<td>iOS/macOS 日志捕获</td>
<td><code>cli-anything-nslogger</code></td>
<td>NSLogger wire protocol + native macOS Bonjour</td>
<td align="center">✅ 139</td>
</tr>
<tr>
<td align="center"><strong>🎞️ Kdenlive</strong></td>
<td>视频编辑</td>
<td><code>cli-anything-kdenlive</code></td>
<td>MLT XML + melt renderer</td>
<td align="center">✅ 155</td>
</tr>
<tr>
<td align="center"><strong>🎬 Shotcut</strong></td>
<td>视频编辑</td>
<td><code>cli-anything-shotcut</code></td>
<td>Direct MLT XML + melt</td>
<td align="center">✅ 154</td>
</tr>
<tr>
<td align="center"><strong>🎬 <a href="openscreen/agent-harness/">Openscreen</a></strong></td>
<td>屏幕录制编辑器</td>
<td><code>cli-anything-openscreen</code></td>
<td>ffmpeg backend</td>
<td align="center">✅ 101</td>
</tr>
<tr>
<td align="center"><strong>📞 Zoom</strong></td>
<td>视频会议</td>
<td><code>cli-anything-zoom</code></td>
<td>Zoom REST API (OAuth2)</td>
<td align="center">✅ 22</td>
</tr>
<tr>
<td align="center"><strong>🎵 MuseScore</strong></td>
<td>音乐记谱</td>
<td><code>cli-anything-musescore</code></td>
<td>mscore CLI (MSCX/MusicXML)</td>
<td align="center">✅ 56</td>
</tr>
<tr>
<td align="center"><strong>📐 Draw.io</strong></td>
<td>图表绘制</td>
<td><code>cli-anything-drawio</code></td>
<td>mxGraph XML + draw.io CLI</td>
<td align="center">✅ 138</td>
</tr>
<tr>
<td align="center"><strong>⛓️ ETH2 QuickStart</strong></td>
<td>DevOps / Ethereum</td>
<td><code>cli-anything-eth2-quickstart</code></td>
<td>eth2-quickstart shell automation + JSON health checks</td>
<td align="center">✅ 18</td>
</tr>
<tr>
<td align="center"><strong>🧜 Mermaid Live Editor</strong></td>
<td>图表绘制</td>
<td><code>cli-anything-mermaid</code></td>
<td>Mermaid state + mermaid.ink renderer</td>
<td align="center">✅ 10</td>
</tr>
<tr>
<td align="center"><strong>✨ AnyGen</strong></td>
<td>AI 内容生成</td>
<td><code>cli-anything-anygen</code></td>
<td>AnyGen REST API (anygen.io)</td>
<td align="center">✅ 50</td>
</tr>
<tr>
<td align="center"><strong>🧠 NotebookLM</strong></td>
<td>AI 研究助手</td>
<td><code>cli-anything-notebooklm</code></td>
<td>NotebookLM CLI wrapper (experimental)</td>
<td align="center">✅ 21</td>
</tr>
<tr>
<td align="center"><strong>🧩 <a href="dify-workflow/agent-harness/">Dify Workflow</a></strong></td>
<td>Dify DSL 编辑</td>
<td><code>cli-anything-dify-workflow</code></td>
<td>Wrapper around the open-source dify-workflow CLI</td>
<td align="center">✅ 11</td>
</tr>
<tr>
<td align="center"><strong>🖼️ ComfyUI</strong></td>
<td>AI 图像生成</td>
<td><code>cli-anything-comfyui</code></td>
<td>ComfyUI REST API</td>
<td align="center">✅ 70</td>
</tr>
<tr>
<td align="center"><strong>🛡️ AdGuard Home</strong></td>
<td>全网广告拦截</td>
<td><code>cli-anything-adguardhome</code></td>
<td>AdGuard Home REST API</td>
<td align="center">✅ 36</td>
</tr>
<tr>
<td align="center"><strong>🦙 Ollama</strong></td>
<td>本地 LLM 推理</td>
<td><code>cli-anything-ollama</code></td>
<td>Ollama REST API</td>
<td align="center">✅ 98</td>
</tr>
<tr>
<td align="center"><strong>🧬 <a href="unimol_tools/agent-harness/">Uni-Mol Tools</a></strong></td>
<td>分子属性预测 (AI4S)</td>
<td><code>cli-anything-unimol-tools</code></td>
<td>Uni-Mol molecular ML backend</td>
<td align="center">✅ 67</td>
</tr>
<tr>
<td align="center"><strong>🎬 <a href="videocaptioner/agent-harness/">VideoCaptioner</a></strong></td>
<td>AI 视频字幕生成</td>
<td><code>cli-anything-videocaptioner</code></td>
<td>videocaptioner CLI (PyPI)</td>
<td align="center">✅ 26</td>
</tr>
<tr>
<td align="center"><strong>🎨 Sketch</strong></td>
<td>UI 设计</td>
<td><code>sketch-cli</code></td>
<td>sketch-constructor (Node.js)</td>
<td align="center">✅ 19</td>
</tr>
<tr>
<td align="center"><strong>🎮 Godot Engine</strong></td>
<td>游戏开发</td>
<td><code>cli-anything-godot</code></td>
<td>Godot 4.x headless subprocess</td>
<td align="center">✅ 24</td>
</tr>
<tr>
<td align="center"><strong>📦 <a href="sbox/agent-harness/">s&amp;box</a></strong></td>
<td>游戏开发</td>
<td><code>cli-anything-sbox</code></td>
<td>Source 2 game engine - direct file I/O on .scene/.prefab/.vmat/.vsnd JSON</td>
<td align="center">✅ 244</td>
</tr>
<tr>
<td align="center"><strong>🐞 <a href="lldb/agent-harness/">LLDB</a></strong></td>
<td>原生调试</td>
<td><code>cli-anything-lldb</code></td>
<td>LLDB Python API</td>
<td align="center">✅ 27</td>
</tr>
<tr>
<td align="center"><strong>🟩 <a href="nsight-graphics/agent-harness/">Nsight Graphics CLI</a></strong></td>
<td>GPU 调试与分析</td>
<td><code>cli-anything-nsight-graphics</code></td>
<td>Official ngfx / ngfx-capture orchestration + GPU Trace summary + replay analysis</td>
<td align="center">✅ 51</td>
</tr>
<tr>
<td align="center"><strong>🔍 <a href="exa/agent-harness/">Exa</a></strong></td>
<td>AI 原生网络搜索</td>
<td><code>cli-anything-exa</code></td>
<td>exa-py SDK</td>
<td align="center">✅ 40</td>
</tr>
<tr>
<td align="center"><strong>📈 <a href="unrealinsights/agent-harness/">Unreal Insights</a></strong></td>
<td>性能分析</td>
<td><code>cli-anything-unrealinsights</code></td>
<td>Background trace sessions + engine-matched UnrealInsights build + headless export</td>
<td align="center">✅ 50</td>
</tr>
<tr>
<td align="center"><strong>☁️ <a href="cloudanalyzer/agent-harness/">CloudAnalyzer</a></strong></td>
<td>点云 / 轨迹 QA</td>
<td><code>cli-anything-cloudanalyzer</code></td>
<td>CloudAnalyzer (Python API)</td>
<td align="center">✅ 14</td>
</tr>
<tr>
<td align="center"><strong>🗺️ <a href="QGIS/agent-harness/">QGIS</a></strong></td>
<td>地理空间分析与制图</td>
<td><code>cli-anything-qgis</code></td>
<td>PyQGIS + qgis_process</td>
<td align="center">✅ 22</td>
</tr>
<tr>
<td align="center"><strong>🔩 <a href="3MF/agent-harness/">3MF</a></strong></td>
<td>3D 打印网格几何编辑器</td>
<td><code>cli-anything-3mf</code></td>
<td>numpy, scipy, trimesh</td>
<td align="center">✅ 50</td>
</tr>
<tr>
<td align="center" colspan="4"><strong>总计</strong></td>
<td align="center"><strong>✅ 2,461</strong></td>
</tr>
</table>

> **全部 2,461 项测试通过率 100%** —— 1,732 项单元测试 + 579 项端到端测试 + 19 项 Node.js 测试。

---

## 📊 测试结果

每个 CLI 框架均经过严格的分层测试以确保生产级可靠性：

| 层级 | 测试内容 | 示例 |
|-------|---------------|---------|
| **单元测试** | 使用合成数据隔离测试每个核心函数 | `test_core.py` —— 项目创建、图层操作、滤镜参数 |
| **E2E 测试（原生）** | 项目文件生成流水线 | 有效 ODF ZIP 结构、正确 MLT XML、SVG 格式良好性 |
| **E2E 测试（真实后端）** | 真实软件调用 + 输出验证 | LibreOffice → PDF（含 `%PDF-` 魔术字节）、Blender → 渲染 PNG |
| **CLI 子进程测试** | 通过 `subprocess.run` 安装命令验证 | `cli-anything-gimp --json project new` → 有效 JSON 输出 |

```
================================ Test Summary ================================
gimp          107 passed  ✅   (64 unit + 43 e2e)
blender       208 passed  ✅   (150 unit + 58 e2e)
inkscape      202 passed  ✅   (148 unit + 54 e2e)
audacity      161 passed  ✅   (107 unit + 54 e2e)
libreoffice   158 passed  ✅   (89 unit + 69 e2e)
mubu           96 passed  ✅   (85 unit + 11 e2e)
obs-studio    153 passed  ✅   (116 unit + 37 e2e)
nslogger      139 passed  ✅   (97 unit + 42 e2e)
kdenlive      155 passed  ✅   (111 unit + 44 e2e)
shotcut       154 passed  ✅   (110 unit + 44 e2e)
zoom           22 passed  ✅   (22 unit + 0 e2e)
drawio        138 passed  ✅   (116 unit + 22 e2e)
eth2-quickstart 18 passed ✅   (18 unit + 3 e2e skipped)
mermaid        10 passed  ✅   (5 unit + 5 e2e)
anygen         50 passed  ✅   (40 unit + 10 e2e)
notebooklm     21 passed  ✅   (21 unit + 0 e2e)
comfyui        70 passed  ✅   (60 unit + 10 e2e)
adguardhome    36 passed  ✅   (24 unit + 12 e2e)
ollama         98 passed  ✅   (87 unit + 11 e2e)
sketch         19 passed  ✅   (19 jest, Node.js)
renderdoc      59 passed  ✅   (45 unit + 14 e2e)
cloudcompare   88 passed  ✅   (49 unit + 39 e2e)
openscreen    101 passed  ✅   (78 unit + 23 e2e)
lldb           27 passed  ✅   (23 unit + 4 e2e)
nsight-graphics 51 passed ✅   (46 unit/CLI + 5 local e2e)
unrealinsights 50 passed  ✅   (49 unit + 1 e2e, 9 backend-gated e2e skipped)
cloudanalyzer  14 passed  ✅   (7 unit + 7 e2e)
3mf            50 passed  ✅   (50 unit)
joplin        134 passed  ✅   (107 unit + 27 e2e, 1 skipped on Windows)
──────────────────────────────────────────────────────────────────────────────
TOTAL        2,461 passed  ✅   100% pass rate
```

---

## 🏗️ CLI-Anything 的架构

<p align="center">
  <img src="assets/architecture.png" alt="CLI-Anything Architecture" width="750">
</p>

### 🎯 核心设计原则

1. **真实软件集成** —— CLI 生成有效项目文件（ODF, MLT XML, SVG）并委托给真实应用程序进行渲染。**我们为软件构建结构化接口，而非替代品**。
2. **灵活的交互模型** —— 每个 CLI 运行于双模式：面向交互式智能体会话的有状态 REPL + 用于脚本/流水线的子命令接口。**运行裸命令 → 进入 REPL 模式**。
3. **一致的用户体验** —— 所有生成的 CLI 共享统一 REPL 界面（repl_skin.py），包含品牌横幅、样式化提示符、命令历史、进度指示器及标准化格式。
4. **智能体原生设计** —— 每条命令内置 `--json` 标志，为机器消费提供结构化数据，同时人类可读表格服务于交互使用。**智能体通过标准 --help 和 which 命令发现能力**。
5. **零妥协依赖** —— 真实软件是硬性要求 —— 无回退方案，无优雅降级。当后端缺失时测试会失败（而非跳过），确保功能真实性。

---

## 📂 项目结构

```
cli-anything/
├── 📄 README.md                          # 你正在查看此文件
├── 📁 assets/                            # 图片与媒体资源
│   ├── icon.png                          # 项目图标
│   └── teaser.png                        # 宣传图
│
├── 🔌 cli-anything-plugin/               # Claude Code 插件
│   ├── HARNESS.md                        # 方法论 SOP（权威来源）
│   ├── README.md                         # 插件文档
│   ├── QUICKSTART.md                     # 5 分钟快速入门
│   ├── PUBLISHING.md                     # 发布指南
│   ├── repl_skin.py                      # 统一 REPL 界面
│   ├── commands/                         # 插件命令定义
│   │   ├── cli-anything.md               # 主构建命令
│   │   ├── refine.md                     # 扩展现有框架覆盖范围
│   │   ├── test.md                       # 测试运行器
│   │   └── validate.md                   # 标准验证
│   └── scripts/
│       └── setup-cli-anything.sh         # 安装脚本
│
├── 🤖 codex-skill/                      # Codex 技能入口点
├── 🧭 hermes-skill/                     # Hermes Agent 技能入口点
├── 🎨 gimp/agent-harness/               # GIMP CLI（107 项测试）
├── 🧊 blender/agent-harness/            # Blender CLI（208 项测试）
├── ✏️ inkscape/agent-harness/            # Inkscape CLI（202 项测试）
├── 🎵 audacity/agent-harness/           # Audacity CLI（161 项测试）
├── 🌐 browser/agent-harness/            # Browser CLI（DOMShell MCP，新增）
├── 📄 libreoffice/agent-harness/        # LibreOffice CLI（158 项测试）
├── 📧 mailchimp/agent-harness/          # Mailchimp Marketing API CLI（303 条命令，36 项单元测试）
├── 📚 zotero/agent-harness/             # Zotero CLI（新增，支持写入导入）
├── 📖 calibre/agent-harness/            # Calibre CLI（58 项测试：38 单元 + 20 E2E）
├── 📓 joplin/agent-harness/             # Joplin CLI（134 项测试：107 单元 + 27 e2e）
├── 📝 mubu/agent-harness/               # Mubu CLI（96 项测试）
├── 📹 obs-studio/agent-harness/         # OBS Studio CLI（153 项测试）
├── 📱 nslogger/agent-harness/           # NSLogger CLI（139 项测试）
├── 🎞️ kdenlive/agent-harness/           # Kdenlive CLI（155 项测试）
├── 🎬 shotcut/agent-harness/            # Shotcut CLI（154 项测试）
├── 📞 zoom/agent-harness/               # Zoom CLI（22 项测试）
├── 🎵 musescore/agent-harness/          # MuseScore CLI（56 项测试）
├── 📐 drawio/agent-harness/             # Draw.io CLI（138 项测试）
├── ⛓️ eth2-quickstart/agent-harness/    # ETH2 QuickStart CLI（18 单元，3 e2e 跳过）
├── 🧜 mermaid/agent-harness/            # Mermaid Live Editor CLI（10 项测试）
├── ✨ anygen/agent-harness/             # AnyGen CLI（50 项测试）
├── 🖼️ comfyui/agent-harness/            # ComfyUI CLI（70 项测试）
├── 🧠 notebooklm/agent-harness/         # NotebookLM CLI（实验性，21 项测试）
├── 🧩 dify-workflow/agent-harness/      # Dify Workflow CLI 包装器（11 项测试）
├── 🛡️ adguardhome/agent-harness/       # AdGuard Home CLI（36 项测试）
├── 🦙 ollama/agent-harness/             # Ollama CLI（98 项测试）
├── 🎮 godot/agent-harness/              # Godot Engine CLI（24 项测试）
├── 📦 sbox/agent-harness/               # s&box CLI（244 项测试：157 单元 + 17 编排器 + 50 e2e + 20 退出码）
├── 🎨 sketch/agent-harness/             # Sketch CLI（19 项测试，Node.js）
├── 🔬 renderdoc/agent-harness/          # RenderDoc CLI（59 项测试）
├── 🟩 nsight-graphics/agent-harness/    # Nsight Graphics CLI（51 项测试）
├── 🐞 lldb/agent-harness/               # LLDB CLI（27 项测试）
├── 📈 unrealinsights/agent-harness/     # Unreal Insights CLI（50 项测试）
├── 🎬 videocaptioner/agent-harness/     # VideoCaptioner CLI（26 项测试）
├── 🎬 openscreen/agent-harness/         # Openscreen CLI —— 屏幕录制编辑器（101 项测试）
├── ☁️ cloudcompare/agent-harness/       # CloudCompare CLI（88 项测试）
├── 🔍 exa/agent-harness/               # Exa CLI（40 项测试）
└── ⛅ cloudanalyzer/agent-harness/      # CloudAnalyzer CLI（14 项测试）
└── 🔩 3MF/agent-harness/               # 3MF Mesh Editor CLI（50+ 项测试）
```

每个 `agent-harness/` 包含一个可安装的 Python 包，位于 `cli_anything.<software>/` 下，内含 Click CLI、核心模块、工具函数（含 `repl_skin.py` 与后端包装器）及全面测试。

---

## 🎯 插件命令

| 命令 | 描述 |
|---------|-------------|
| `/cli-anything <software-path-or-repo>` | 构建完整 CLI 框架 —— 全部 7 个阶段 |
| `/cli-anything:refine <software-path> [focus]` | 优化现有框架 —— 通过差距分析扩展覆盖范围 |
| `/cli-anything:test <software-path-or-repo>` | 运行测试并使用结果更新 TEST.md |
| `/cli-anything:validate <software-path-or-repo>` | 基于 HARNESS.md 标准进行验证 |

### 示例

```bash
# 从本地源码构建 GIMP 完整 CLI
/cli-anything /home/user/gimp

# 从 GitHub 仓库构建
/cli-anything https://github.com/blender/blender

# 优化现有框架 —— 广泛差距分析
/cli-anything:refine /home/user/gimp

# 带特定聚焦领域的优化
/cli-anything:refine /home/user/shotcut "vid-in-vid and picture-in-picture compositing"

# 运行测试并更新 TEST.md
/cli-anything:test /home/user/inkscape

# 基于 HARNESS.md 标准进行验证
/cli-anything:validate /home/user/audacity
```

---

## 🎮 演示：使用生成的 CLI

以下是智能体如何使用 `cli-anything-libreoffice` 的示例：

```bash
# 创建新 Writer 文档
$ cli-anything-libreoffice document new -o report.json --type writer
✓ Created Writer document: report.json

# 添加内容
$ cli-anything-libreoffice --project report.json writer add-heading -t "Q1 Report" --level 1
✓ Added heading: "Q1 Report"

$ cli-anything-libreoffice --project report.json writer add-table --rows 4 --cols 3
✓ Added 4×3 table

# 通过 LibreOffice 无头模式导出为真实 PDF
$ cli-anything-libreoffice --project report.json export render output.pdf -p pdf --overwrite
✓ Exported: output.pdf (42,831 bytes) via libreoffice-headless

# JSON 模式供智能体消费
$ cli-anything-libreoffice --json document info --project report.json
{
  "name": "Q1 Report",
  "type": "writer",
  "pages": 1,
  "elements": 2,
  "modified": true
}
```

### REPL 模式

```
$ cli-anything-blender
╔══════════════════════════════════════════╗
║       cli-anything-blender v1.0.0       ║
║     Blender CLI for AI Agents           ║
╚══════════════════════════════════════════╝

blender> scene new --name ProductShot
✓ Created scene: ProductShot

blender[ProductShot]> object add-mesh --type cube --location 0 0 1
✓ Added mesh: Cube at (0, 0, 1)

blender[ProductShot]*> render execute --output render.png --engine CYCLES
✓ Rendered: render.png (1920×1080, 2.3 MB) via blender --background

blender[ProductShot]> exit
Goodbye! 👋
```

---

## 📖 标准手册：HARNESS.md

HARNESS.md 是我们关于如何通过自动化 CLI 生成使任何软件具备智能体可访问性的权威 SOP。

它编码了通过自动生成流程打磨出的成熟模式与方法论。

该手册提炼了成功构建全部 18 款多样化、生产就绪型框架的关键经验。

### 关键教训

| 教训 | 描述 |
|--------|-------------|
| **使用真实软件** | CLI 必须调用实际应用程序进行渲染。GIMP 不用 Pillow 替代，Blender 不用自定义渲染器。生成有效项目文件 → 调用真实后端。 |
| **渲染鸿沟** | GUI 应用在渲染时应用效果。若你的 CLI 操作项目文件但使用朴素导出工具，效果会被静默丢弃。解决方案：原生渲染器 → 滤镜转换 → 渲染脚本。 |
| **滤镜转换** | 在格式间映射效果（MLT → ffmpeg）时，注意重复滤镜合并、交错流排序、参数空间差异及无法映射的效果。 |
| **时间码精度** | 非整数帧率（29.97fps）会导致累积舍入误差。使用 `round()` 而非 `int()`，显示时使用整数算术，测试中允许 ±1 帧容差。 |
| **输出验证** | 切勿仅因退出码为 0 就信任导出成功。需验证：魔术字节、ZIP/OOXML 结构、像素分析、音频 RMS 电平、时长检查。 |

> 查看完整方法论：[`cli-anything-plugin/HARNESS.md`](cli-anything-plugin/HARNESS.md)

---

## 📦 安装与使用

### CLI-Hub 用户

```bash
# 安装包管理器
pip install cli-anything-hub

# 浏览、搜索、检查并安装 CLI
cli-hub list
cli-hub search <query>
cli-hub info <name>
cli-hub install <name>

# 管理已安装的 CLI
cli-hub update <name>
cli-hub uninstall <name>
cli-hub launch <name> [args...]
```

### 插件用户（Claude Code）

```bash
# 添加市场并安装（推荐）
/plugin marketplace add HKUDS/CLI-Anything
/plugin install cli-anything

# 为拥有代码库的任何软件构建 CLI
/cli-anything <software-name>
```

### 生成的 CLI

```bash
# 安装任意生成的 CLI
cd <software>/agent-harness
pip install -e .

# 验证
which cli-anything-<software>

# 使用
cli-anything-<software> --help
cli-anything-<software>                    # 进入 REPL
cli-anything-<software> --json <command>   # JSON 输出供智能体使用
```

### 运行测试

```bash
# 运行特定 CLI 的测试
cd <software>/agent-harness
python3 -m pytest cli_anything/<software>/tests/ -v

# 强制安装模式（推荐用于验证）
CLI_ANYTHING_FORCE_INSTALLED=1 python3 -m pytest cli_anything/<software>/tests/ -v -s
```

---

## 🤝 贡献指南

我们欢迎贡献！CLI-Anything 设计为可扩展：

- **新软件目标** —— 使用插件为任何拥有代码库的软件生成 CLI，然后通过 [`cli-anything-plugin/PUBLISHING.md`](cli-anything-plugin/PUBLISHING.md) 提交你的框架。
- **方法论改进** —— 向 `HARNESS.md` 提交 PR 以编码新学到的经验
- **插件增强** —— 新增命令、阶段优化、更好的验证机制
- **测试覆盖** —— 更多 E2E 场景、边界情况与工作流测试

### 局限性

- **依赖强大基础模型** —— CLI-Anything 依靠前沿级模型（如 Claude Opus 4.6, Claude Sonnet 4.6, GPT-5.4）以实现可靠的框架生成。较弱或较小的模型可能产生不完整或不正确的 CLI，需要大量手动修正。
- **依赖可用源码** —— 7 阶段流水线分析并基于源码进行生成。当目标软件仅提供需反编译的编译二进制文件时，框架质量与覆盖范围将显著下降。
- **可能需要迭代优化** —— 单次 `/cli-anything` 运行可能无法完全覆盖所有功能。通常需多次运行 `/refine` 才能将 CLI 的性能与覆盖范围推至生产级标准。

### 路线图

- [ ] 支持更多应用类别（CAD, DAW, IDE, EDA, 科学工具）
- [ ] 智能体任务完成率基准测试套件
- [ ] 社区贡献的内部/自定义软件 CLI 框架
- [ ] 集成除 Claude Code 外的其他智能体框架
- [ ] 支持将闭源软件与 Web 服务的 API 打包为 CLI
- [x] 随 CLI 同步生成 SKILL.md，供智能体技能发现与编排使用

---

## 📖 文档

| 文档 | 描述 |
|----------|-------------|
| [`cli-anything-plugin/HARNESS.md`](cli-anything-plugin/HARNESS.md) | 方法论 SOP —— 单一权威来源 |
| [`cli-anything-plugin/README.md`](cli-anything-plugin/README.md) | 插件文档 —— 命令、选项、阶段 |
| [`cli-anything-plugin/QUICKSTART.md`](cli-anything-plugin/QUICKSTART.md) | 5 分钟快速入门指南 |
| [`cli-anything-plugin/PUBLISHING.md`](cli-anything-plugin/PUBLISHING.md) | 分发与发布指南 |

每个生成的框架还包含：
- `<SOFTWARE>.md` —— 针对该应用特有的架构 SOP
- `tests/TEST.md` —— 测试计划与结果文档

---

## ⭐ Star 历史

如果 CLI-Anything 帮助你让软件具备智能体原生能力，请给我们一个 Star！⭐

<div align="center">
  <a href="https://star-history.com/#HKUDS/CLI-Anything&Date">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=HKUDS/CLI-Anything&type=Date&theme=dark" />
      <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=HKUDS/CLI-Anything&type=Date" />
      <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=HKUDS/CLI-Anything&type=Date" />
    </picture>
  </a>
</div>

---

## 📄 许可证

Apache License 2.0 —— 可免费使用、修改与分发。

---

<div align="center">

**CLI-Anything** — *让任何拥有代码库的软件具备智能体原生能力。*

<sub>A methodology for the age of AI agents | 18 professional software demos | 2,280 passing tests</sub>

<br>

<img src="assets/icon.png" alt="CLI-Anything Icon" width="80">

</div>

<p align="center">
  <em> 感谢访问 ✨ CLI-Anything!</em><br><br>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=HKUDS.CLI-Anything&style=for-the-badge&color=00d4ff" alt="Views">
</p>