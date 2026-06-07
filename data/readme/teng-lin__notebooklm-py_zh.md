# notebooklm-py
<p align="left">
  <img src="https://raw.githubusercontent.com/teng-lin/notebooklm-py/main/notebooklm-py.png" alt="notebooklm-py logo" width="128">
</p>

**一个全面的 NotebookLM 技能包与非官方 Python API。** 通过 Python、CLI 以及 Claude Code、Codex 和 OpenClaw 等 AI Agent，全面编程访问 NotebookLM 的功能——包括 Web UI 未暴露的能力。

[![PyPI version](https://img.shields.io/pypi/v/notebooklm-py.svg)](https://pypi.org/project/notebooklm-py/)
[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue)](https://pypi.org/project/notebooklm-py/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/teng-lin/notebooklm-py/actions/workflows/test.yml/badge.svg)](https://github.com/teng-lin/notebooklm-py/actions/workflows/test.yml)
<p>
  <a href="https://trendshift.io/repositories/19116" target="_blank"><img src="https://trendshift.io/api/badge/repositories/19116" alt="teng-lin%2Fnotebooklm-py | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

**源码与开发**：<https://github.com/teng-lin/notebooklm-py>

> **⚠️ 非官方库——使用需谨慎**
>
> 本库使用了**未公开的 Google API**，可能会随时变更。
>
> - **与 Google 无关**——这是一个社区项目
> - **API 可能失效**——Google 可随时更改内部接口
> - **存在速率限制**——高频使用可能会被限速
>
> 最适合用于原型开发、研究和私人项目。调试技巧请参阅 [Troubleshooting](docs/troubleshooting.md)。

## 你可以构建什么

🤖 **AI Agent 工具**——将 NotebookLM 集成到 Claude Code、Codex 及其他大语言模型（LLM）Agent 中。内置根目录 [NotebookLM skill](SKILL.md) 用于 GitHub 和 `npx skills add` 发现，支持本地 `notebooklm skill install` 安装至 Claude Code 和 `.agents` 技能目录，并在 [`AGENTS.md`](AGENTS.md) 提供仓库级 Codex 指导。

📚 **研究自动化**——批量导入来源（URL、PDF、YouTube、Google Drive），运行 Web/Drive 研究查询并自动导入，以编程方式提取洞察。构建可重复的研究流水线。

🎙️ **内容生成**——生成音频概述（播客）、视频、幻灯片演示文稿、测验、抽认卡、信息图、数据表、思维导图和学习指南。完全控制格式、风格和输出。

📥 **下载与导出**——将本地下载所有生成的产物（MP3、MP4、PDF、PNG、CSV、JSON、Markdown）。导出至 Google Docs/Sheets。**Web UI 未提供的功能**：批量下载、多格式测验/抽认卡导出、思维导图 JSON 提取。

## 三种使用方式

| Method | Best For |
|--------|----------|
| **Python API** | Application integration, async workflows, custom pipelines |
| **CLI** | Shell scripts, quick tasks, CI/CD automation |
| **Agent Integration** | Claude Code, Codex, LLM agents, natural language automation |

## 核心功能

### 完整覆盖 NotebookLM 功能

| Category | Capabilities |
|----------|--------------|
| **Notebooks** | Create, list, rename, delete |
| **Sources** | URLs, YouTube, files (PDF, text, Markdown, Word, EPUB, audio, video, images), Google Drive, pasted text; refresh, get guide/fulltext |
| **Chat** | Questions, conversation history, custom personas |
| **Research** | Web and Drive research agents (fast/deep modes) with auto-import |
| **Sharing** | Public/private links, user permissions (viewer/editor), view level control |

### 内容生成（所有产物类型）

| Type | Options | Download Format |
|------|---------|-----------------|
| **Audio Overview** | 4 formats (deep-dive, brief, critique, debate), 3 lengths, 50+ languages | MP3/MP4 |
| **Video Overview** | 3 formats (explainer, brief, cinematic), 9 visual styles, plus a dedicated `cinematic-video` CLI alias | MP4 |
| **Slide Deck** | Detailed or presenter format, adjustable length; individual slide revision | PDF, PPTX |
| **Infographic** | 3 orientations, 3 detail levels | PNG |
| **Quiz** | Configurable quantity and difficulty | JSON, Markdown, HTML |
| **Flashcards** | Configurable quantity and difficulty | JSON, Markdown, HTML |
| **Report** | Briefing doc, study guide, blog post, or custom prompt | Markdown |
| **Data Table** | Custom structure via natural language | CSV |
| **Mind Map** | Interactive hierarchical visualization | JSON |

### 超越 Web UI 的功能

以下功能可通过 API/CLI 使用，但未在 NotebookLM 的 Web 界面中暴露：

- **批量下载**——一次性下载所有指定类型的产物
- **测验/抽认卡导出**——获取结构化 JSON、Markdown 或 HTML（Web UI 仅提供交互式视图）
- **思维导图数据提取**——导出层级 JSON 供可视化工具使用
- **数据表 CSV 导出**——将结构化表格下载为电子表格
- **幻灯片演示文稿转为 PPTX**——下载可编辑的 PowerPoint 文件（Web UI 仅提供 PDF）
- **单页修订**——使用自然语言提示词修改单个幻灯片
- **报告模板自定义**——向内置格式模板追加额外指令
- **保存聊天至笔记**——将问答答案或对话历史保存为笔记本笔记
- **来源全文访问**——检索任意来源的索引文本内容
- **编程方式分享**——无需 UI 即可管理权限
- **多账号配置**——切换 Google 账号而无需重新验证
- **浏览器 Cookie 导入**——复用现有浏览器会话的 Cookie，避免驱动 Playwright

## 安装指南

完整安装指南（涵盖六种角色：Agent、终端用户、库开发者、无头模式、贡献者、高级用户）、可选依赖矩阵及平台说明）位于 **[docs/installation.md](docs/installation.md)**。

**快速开始**（适用于 CLI 用户和 AI Agent）：

```bash
pip install "notebooklm-py[browser]"   # core + Playwright
playwright install chromium             # ~170 MB; no progress bar — be patient (30–90 s)
notebooklm login                        # opens browser for Google sign-in
notebooklm auth check --test --json     # verify: expect "status": "ok"
```

**作为库使用**（嵌入你的应用——无需 Playwright 和 Chromium）：

```bash
pip install notebooklm-py               # ~10 MB; ship a pre-acquired storage_state.json
```

如果在 Linux 上运行 `playwright install chromium` 时出现 `TypeError: onExit is not a function`，请参阅 [Linux 解决方案](docs/troubleshooting.md#linux)。**贡献者**：请查看 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 快速上手

<p align="center">
  <a href="https://asciinema.org/a/767284" target="_blank"><img src="https://asciinema.org/a/767284.svg" width="600" /></a>
  <br>
  <em>16-minute session compressed to 30 seconds</em>
</p>

### CLI

```bash
# 1. Authenticate (opens browser)
notebooklm login
# Or use Microsoft Edge (for orgs that require Edge for SSO)
# notebooklm login --browser msedge
# Or reuse cookies from an already-logged-in browser session
# notebooklm login --browser-cookies chrome
# notebooklm login --browser-cookies 'chrome::Profile 1'  # one Chromium profile
# (combine with --profile to populate a specific profile;
#  use --account / --all-accounts after auth inspect when several
#  Google accounts are signed in)

# 2. Create a notebook and add sources
notebooklm create "My Research"
notebooklm use <notebook_id>
notebooklm source add "https://en.wikipedia.org/wiki/Artificial_intelligence"
notebooklm source add "./paper.pdf"

# 3. Chat with your sources
notebooklm ask "What are the key themes?"
notebooklm ask --prompt-file ./long_question.txt  # Read question from file

# 4. Generate content (use --prompt-file for long prompts)
notebooklm generate audio "make it engaging" --wait
notebooklm generate video --style whiteboard --wait
notebooklm generate cinematic-video "documentary-style summary" --wait
notebooklm generate quiz --difficulty hard
notebooklm generate flashcards --quantity more
notebooklm generate slide-deck
notebooklm generate infographic --orientation portrait
notebooklm generate mind-map
notebooklm generate data-table "compare key concepts"

# 5. Download artifacts
notebooklm download audio ./podcast.mp3
notebooklm download video ./overview.mp4
notebooklm download cinematic-video ./documentary.mp4
notebooklm download quiz --format markdown ./quiz.md
notebooklm download flashcards --format json ./cards.json
notebooklm download slide-deck ./slides.pdf
notebooklm download infographic ./infographic.png
notebooklm download mind-map ./mindmap.json
notebooklm download data-table ./data.csv
```

其他常用 CLI 命令：

```bash
notebooklm auth check --test         # Diagnose auth/cookie issues
notebooklm auth refresh --quiet      # One-shot cookie keepalive (for cron / launchd / systemd)
notebooklm auth refresh --browser-cookies chrome  # Re-extract and repair account routing
notebooklm auth inspect --browser 'chrome::Profile 1'  # Preview one Chromium profile
notebooklm agent show codex          # Print bundled Codex instructions
notebooklm agent show claude         # Print bundled Claude Code skill template
notebooklm language list             # List supported output languages
notebooklm metadata --json           # Export notebook metadata and sources
notebooklm share status              # Inspect sharing state
notebooklm source add-research "AI"  # Start web research and import sources
notebooklm skill status              # Check local agent skill installation
notebooklm profile list              # List all Google account profiles
notebooklm profile switch work       # Switch active account profile
```

当文本过长超出 Shell 命令行限制时，请在 `ask`、基于提示词的 `generate` 命令以及 `source add-research` 中使用 `--prompt-file PATH`。该参数会从文件中读取提示词/查询内容，这与 `source add ./file.pdf`（将文件作为 NotebookLM 来源上传）是独立的两个功能。

### Python API

```python
import asyncio
from notebooklm import NotebookLMClient

async def main():
    async with NotebookLMClient.from_storage() as client:
        # Create notebook and add sources
        nb = await client.notebooks.create("Research")
        await client.sources.add_url(nb.id, "https://example.com", wait=True)

        # Chat with your sources
        result = await client.chat.ask(nb.id, "Summarize this")
        print(result.answer)

        # Generate content (podcast, video, quiz, etc.)
        status = await client.artifacts.generate_audio(nb.id, instructions="make it fun")
        await client.artifacts.wait_for_completion(nb.id, status.task_id)
        await client.artifacts.download_audio(nb.id, "podcast.mp3")

        # Generate quiz and download as JSON
        status = await client.artifacts.generate_quiz(nb.id)
        await client.artifacts.wait_for_completion(nb.id, status.task_id)
        await client.artifacts.download_quiz(nb.id, "quiz.json", output_format="json")

        # Generate mind map and export
        result = await client.artifacts.generate_mind_map(nb.id)
        await client.artifacts.download_mind_map(nb.id, "mindmap.json")

asyncio.run(main())
```

### Agent 配置

**方式 1——通过 CLI 安装**：

```bash
notebooklm skill install
```

将技能包安装至 `~/.claude/skills/notebooklm` 和 `~/.agents/skills/notebooklm`。

**方式 2——通过 `npx` 安装**（基于开放技能生态）：

```bash
npx skills add teng-lin/notebooklm-py
```

直接从 GitHub 拉取标准的 [SKILL.md](SKILL.md)。


## 文档

- **[CLI Reference](docs/cli-reference.md)** - Complete command documentation
- **[Python API](docs/python-api.md)** - Full API reference
- **[Configuration](docs/configuration.md)** - Storage and settings
- **[Release Guide](docs/releasing.md)** - Release checklist and packaging verification
- **[Troubleshooting](docs/troubleshooting.md)** - Common issues and solutions
- **[API Stability](docs/stability.md)** - Versioning policy and stability guarantees

### 贡献者指南

- **[Architecture](docs/architecture.md)** - Architectural overview and design principles
- **[Development Guide](docs/development.md)** - Architecture, testing, and releasing
- **[RPC Development](docs/rpc-development.md)** - Protocol capture and debugging
- **[RPC Reference](docs/rpc-reference.md)** - Payload structures
- **[Changelog](CHANGELOG.md)** - Version history and release notes
- **[Security](SECURITY.md)** - Security policy and credential handling

## 平台支持

| Platform | Status | Notes |
|----------|--------|-------|
| **macOS** | ✅ Tested | Primary development platform |
| **Linux** | ✅ Tested | Fully supported |
| **Windows** | ✅ Tested | Tested in CI |

## Star History

[![Star History Chart](https://api.star-history.com/image?repos=teng-lin/notebooklm-py&type=timeline&legend=top-left)](https://www.star-history.com/?repos=teng-lin%2Fnotebooklm-py&type=timeline&legend=top-left)

## 许可证

MIT License. See [LICENSE](LICENSE) for details.