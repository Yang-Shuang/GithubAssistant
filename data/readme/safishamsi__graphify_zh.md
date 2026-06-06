<p align="center">
  <a href="https://graphifylabs.ai"><img src="https://raw.githubusercontent.com/safishamsi/graphify/v4/docs/logo-text.svg" width="260" height="64" alt="Graphify"/></a>
</p>

<p align="center">
  🇺🇸 <a href="README.md">English</a> | 🇨🇳 <a href="docs/translations/README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="docs/translations/README.ja-JP.md">日本語</a> | 🇰🇷 <a href="docs/translations/README.ko-KR.md">한국어</a> | 🇩🇪 <a href="docs/translations/README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="docs/translations/README.fr-FR.md">Français</a> | 🇪🇸 <a href="docs/translations/README.es-ES.md">Español</a> | 🇮🇳 <a href="docs/translations/README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="docs/translations/README.pt-BR.md">Português</a> | 🇷🇺 <a href="docs/translations/README.ru-RU.md">Русский</a> | 🇸🇦 <a href="docs/translations/README.ar-SA.md">العربية</a> | 🇮🇹 <a href="docs/translations/README.it-IT.md">Italiano</a> | 🇵🇱 <a href="docs/translations/README.pl-PL.md">Polski</a> | 🇳🇱 <a href="docs/translations/README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="docs/translations/README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="docs/translations/README.uk-UA.md">Українська</a> | 🇻🇳 <a href="docs/translations/README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="docs/translations/README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="docs/translations/README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="docs/translations/README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="docs/translations/README.ro-RO.md">Română</a> | 🇨🇿 <a href="docs/translations/README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="docs/translations/README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="docs/translations/README.da-DK.md">Dansk</a> | 🇳🇴 <a href="docs/translations/README.no-NO.md">Norsk</a> | 🇭🇺 <a href="docs/translations/README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="docs/translations/README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="docs/translations/README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="docs/translations/README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="docs/translations/README.fil-PH.md">Filipino</a>
</p>

<p align="center">
  <a href="https://www.ycombinator.com/companies/graphify"><img src="https://img.shields.io/badge/Y%20Combinator-S26-F0652F?style=flat&logo=ycombinator&logoColor=white" alt="YC S26"/></a>
  <a href="https://safishamsi.gumroad.com/l/qetvlo"><img src="https://img.shields.io/badge/Book-The%20Memory%20Layer-2ea44f?style=flat&logo=gitbook&logoColor=white" alt="The Memory Layer"/></a>
  <a href="https://github.com/safishamsi/graphify/actions/workflows/ci.yml"><img src="https://github.com/safishamsi/graphify/actions/workflows/ci.yml/badge.svg?branch=v8" alt="CI"/></a>
  <a href="https://pypi.org/project/graphifyy/"><img src="https://img.shields.io/pypi/v/graphifyy" alt="PyPI"/></a>
  <a href="https://pepy.tech/project/graphifyy"><img src="https://img.shields.io/pepy/dt/graphifyy?color=blue&label=downloads" alt="Downloads"/></a>
  <a href="https://github.com/sponsors/safishamsi"><img src="https://img.shields.io/badge/sponsor-safishamsi-ea4aaa?logo=github-sponsors" alt="Sponsor"/></a>
  <a href="https://www.linkedin.com/in/safi-shamsi"><img src="https://img.shields.io/badge/LinkedIn-Safi%20Shamsi-0077B5?logo=linkedin" alt="LinkedIn"/></a>
  <a href="https://x.com/graphifyy"><img src="https://img.shields.io/badge/X-graphifyy-000000?logo=x&logoColor=white" alt="X"/></a>
</p>

<p align="center">
  <a href="https://star-history.com/#safishamsi/graphify&Date">
    <img src="https://api.star-history.com/svg?repos=safishamsi/graphify&type=Date" alt="Star History Chart" width="370"/>
  </a>
</p>

在你的 AI 编程助手中输入 `/graphify`，它会将你的整个项目（代码、文档、PDF、图片、视频）映射为一个知识图谱。你可以通过查询来检索信息，而不是在文件中盲目搜索。

兼容 Claude Code、Codex、OpenCode、Kilo Code、Cursor、Gemini CLI、GitHub Copilot CLI、VS Code Copilot Chat、Aider、Amp、OpenClaw、Factory Droid、Trae、Hermes、Kimi Code、Kiro、Pi、Devin CLI 以及 Google Antigravity。

```
/graphify .
```

完成。你将获得三个文件：

```
graphify-out/
├── graph.html       在任何浏览器中打开 — 点击节点、过滤、搜索
├── GRAPH_REPORT.md  核心摘要：关键概念、意外关联、建议问题
└── graph.json       完整图谱数据 — 随时查询，无需重新读取文件
```

如需生成带有 Mermaid 调用流程图的易读架构页面，请运行：

```bash
graphify export callflow-html
```

---

## 前置要求

| Requirement | Minimum | Check | Install |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(推荐)* | any | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(备选)* | any | `pipx --version` | `pip install pipx` |

**macOS 快速安装（Homebrew）：**
```bash
brew install python@3.12 uv
```

**Windows 快速安装：**
```powershell
winget install astral-sh.uv
```

**Ubuntu/Debian：**
```bash
sudo apt install python3.12 python3-pip pipx
# or install uv:
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## 安装

> **官方包说明：** PyPI 上的正式包名为 `graphifyy`（双 y）。PyPI 上其他 `graphify*` 开头的包均与此无关。CLI 命令仍为 `graphify`。

**步骤 1 — 安装包：**

```bash
# 推荐（uv 会自动将 graphify 加入 PATH）：
uv tool install graphifyy

# 备选方案：
pipx install graphifyy
pip install graphifyy  # 可能需要手动配置 PATH — 见下方说明
```

**步骤 2 — 向你的 AI 助手注册技能（Skill）：**

```bash
graphify install
```

完成。打开你的 AI 助手并输入 `/graphify .`

若要将助手技能安装到当前仓库而非用户配置文件中，请添加 `--project` 参数：

```bash
graphify install --project
graphify install --project --platform codex
```

项目级安装会将文件写入当前目录下，例如 `.claude/skills/graphify/SKILL.md` 或 `.agents/skills/graphify/SKILL.md`（附带一个按需加载的 `references/` 侧车文件），并输出提示哪些文件可以提交。支持项目级安装的跨平台命令同样接受此参数，例如 `graphify claude install --project` 或 `graphify codex install --project`。

> **PowerShell 注意事项：** 请使用 `graphify .` 而非 `/graphify .` — 在 PowerShell 中前导斜杠会被识别为路径分隔符。

> **提示找不到命令？** 请使用 `uv tool install graphifyy` 或 `pipx install graphifyy` — 两者均会自动将 CLI 加入 PATH。若使用原生 `pip`，请将 `~/.local/bin`（Linux）或 `~/Library/Python/3.x/bin`（Mac）添加到你的 PATH，或直接运行 `python -m graphify`。

> **尽量避免在 Mac/Windows 上使用 `pip install`**。技能会在运行时从 `graphify-out/.graphify_python` 解析 Python。如果该路径指向的环境与 `pip` 安装包的环境不同，你将遇到 `ModuleNotFoundError: No module named 'graphify'`。使用 `uv tool install` 和 `pipx install` 会将包隔离在独立环境中，从而完全避免此问题。

### 选择你的平台

| Platform | Install command |
|----------|----------------|
| Claude Code (Linux/Mac) | `graphify install` |
| Claude Code (Windows) | `graphify install --platform windows` |
| Codex | `graphify install --platform codex` |
| OpenCode | `graphify install --platform opencode` |
| Kilo Code | `graphify install --platform kilo` |
| GitHub Copilot CLI | `graphify install --platform copilot` |
| VS Code Copilot Chat | `graphify vscode install` |
| Aider | `graphify install --platform aider` |
| OpenClaw | `graphify install --platform claw` |
| Factory Droid | `graphify install --platform droid` |
| Trae | `graphify install --platform trae` |
| Trae CN | `graphify install --platform trae-cn` |
| Gemini CLI | `graphify install --platform gemini` |
| Hermes | `graphify install --platform hermes` |
| Kimi Code | `graphify install --platform kimi` |
| Amp | `graphify amp install` |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify install --platform pi` |
| Cursor | `graphify cursor install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

> Codex 用户：还需在 `~/.codex/config.toml` 的 `[features]` 下添加 `multi_agent = true`。Codex 使用 `$graphify` 而非 `/graphify`。

### 可选扩展组件

按需安装所需功能：

| Extra | What it adds | Install |
|---|---|---|
| `pdf` | PDF 提取 | `uv tool install "graphifyy[pdf]"` |
| `office` | `.docx` and `.xlsx` 支持 | `uv tool install "graphifyy[office]"` |
| `google` | Google Sheets 渲染 | `uv tool install "graphifyy[google]"` |
| `video` | 视频/音频转录 (faster-whisper + yt-dlp) | `uv tool install "graphifyy[video]"` |
| `mcp` | MCP stdio server | `uv tool install "graphifyy[mcp]"` |
| `neo4j` | Neo4j 推送支持 | `uv tool install "graphifyy[neo4j]"` |
| `svg` | SVG 图谱导出 | `uv tool install "graphifyy[svg]"` |
| `leiden` | Leiden 社区检测 (仅 Python < 3.13) | `uv tool install "graphifyy[leiden]"` |
| `ollama` | Ollama 本地推理 | `uv tool install "graphifyy[ollama]"` |
| `openai` | OpenAI / OpenAI 兼容 API | `uv tool install "graphifyy[openai]"` |
| `gemini` | Google Gemini API | `uv tool install "graphifyy[gemini]"` |
| `anthropic` | Anthropic Claude API (`--backend claude`, uses `ANTHROPIC_API_KEY`) | `uv tool install "graphifyy[anthropic]"` |
| `bedrock` | AWS Bedrock (uses IAM, no API key) | `uv tool install "graphifyy[bedrock]"` |
| `sql` | SQL 模式提取 | `uv tool install "graphifyy[sql]"` |
| `dm` | BYOND DreamMaker `.dm`/`.dme` AST 提取 (若 wheel 不匹配平台，可能需 C 编译器 + `python3-dev`) | `uv tool install "graphifyy[dm]"` |
| `chinese` | 中文查询分词 (jieba) | `uv tool install "graphifyy[chinese]"` |
| `all` | 包含上述所有功能 | `uv tool install "graphifyy[all]"` |

---

## 让助手始终使用知识图谱

在项目中构建好图谱后，运行以下命令之一：

| Platform | Command |
|----------|---------|
| Claude Code | `graphify claude install` |
| Codex | `graphify codex install` |
| OpenCode | `graphify opencode install` |
| Kilo Code | `graphify kilo install` |
| GitHub Copilot CLI | `graphify copilot install` |
| VS Code Copilot Chat | `graphify vscode install` |
| Aider | `graphify aider install` |
| OpenClaw | `graphify claw install` |
| Factory Droid | `graphify droid install` |
| Trae | `graphify trae install` |
| Trae CN | `graphify trae-cn install` |
| Cursor | `graphify cursor install` |
| Gemini CLI | `graphify gemini install` |
| Hermes | `graphify hermes install` |
| Kimi Code | `graphify install --platform kimi` |
| Amp | `graphify amp install` |
| Kiro IDE/CLI | `graphify kiro install` |
| Pi coding agent | `graphify pi install` |
| Devin CLI | `graphify devin install` |
| Google Antigravity | `graphify antigravity install` |

这将写入一个小型配置文件，指示你的助手在回答代码库相关问题时查阅知识图谱——优先使用作用域查询（如 `graphify query "<问题>"`），而不是阅读完整报告或搜索原始文件。对于支持有效载荷挂钩的平台（Claude Code、Gemini CLI），会在搜索类工具调用前自动触发挂钩（在 Claude Code 上，还会在使用 Read/Glob 工具逐个读取源文件之前），引导助手优先使用图谱路径。在其他平台（Codex、OpenCode、Cursor 等）上，持久化指令文件（`AGENTS.md`、`.cursor/rules/` 等）提供相同的“查询优先”指引。`GRAPH_REPORT.md` 仍可用于广泛的架构审查。

若要一次性从所有平台移除 Graphify：运行 `graphify uninstall`（添加 `--purge` 参数还会删除 `graphify-out/`）。或使用各平台的独立命令，例如 `graphify claude uninstall`。

---

**Kilo Code** 会将 Graphify 技能安装至 `~/.config/kilo/skills/graphify/SKILL.md`，并将原生 `/graphify` 命令安装至 `~/.config/kilo/command/graphify.md`。`graphify kilo install` 还会写入 `AGENTS.md` 以及原生的 **`tool.execute.before` 插件**（`.kilo/plugins/graphify.js` + `.kilo/kilo.json` 或 `.kilo/kilo.jsonc` 注册），使 Kilo 通过原生 `.kilo` 配置获得始终在线的图谱提醒行为。

**Cursor** 会写入 `.cursor/rules/graphify.mdc`，其中包含 `alwaysApply: true` — Cursor 会自动将其加入每次对话，无需额外挂钩。

## 报告内容说明

- **God nodes（核心节点）** — 项目中连接最密集的实体。所有信息流均汇聚于此。
- **Surprising connections（意外关联）** — 跨越不同文件或模块的实体链接。按“出乎意料”程度排序。
- **The "why"（设计意图）** — 行内注释（`# NOTE:`、`# WHY:`、`# HACK:`）、文档字符串以及文档中的设计理由会被提取为独立节点，并指向其解释的代码。
- **Suggested questions（建议问题）** — 图谱独有的 4–5 个高价值查询问题。
- **Confidence tags（置信度标签）** — 每条推断关系均标记为 `EXTRACTED`、`INFERRED` 或 `AMBIGUOUS`。你始终清楚哪些是明确提取的，哪些是模型推测的。

---

## 支持的文件类型

| Type | Extensions |
|------|-----------|
| Code (33 languages) | `.py .ts .js .jsx .tsx .mjs .go .rs .java .c .cpp .h .hpp .rb .cs .kt .scala .php .swift .lua .luau .zig .ps1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .csproj .fsproj .vbproj .razor .cshtml` (`.dm`/`.dme` AST 提取需 `uv tool install graphifyy[dm]`) |
| MCP configs | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — 提取服务器节点、包引用、环境变量要求 |
| Docs | `.md .mdx .qmd .html .txt .rst .yaml .yml` |
| Office | `.docx .xlsx` (requires `uv tool install graphifyy[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides` (opt-in; requires `gws` auth and `--google-workspace`; Sheets need `uv tool install graphifyy[google]`) |
| PDFs | `.pdf` |
| Images | `.png .jpg .webp .gif` |
| Video / Audio | `.mp4 .mov .mp3 .wav` 及更多 (requires `uv tool install graphifyy[video]`) |
| YouTube / URLs | any video URL (requires `uv tool install graphifyy[video]`) |

代码通过 tree-sitter 在本地提取，无需 API 调用。其余内容均通过你的 AI 助手的模型 API 处理。

桌面版 Google Drive 的 `.gdoc`、`.gsheet` 和 `.gslides` 文件仅为快捷方式指针，并非文档内容。若要在无头模式下包含原生 Google Docs、Sheets 和 Slides，请安装并认证 [`gws` CLI](https://github.com/googleworkspace/cli)，然后运行：

```bash
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```

你也可以设置 `GRAPHIFY_GOOGLE_WORKSPACE=1`。Graphify 会将快捷方式导出为 Markdown 侧车文件至 `graphify-out/converted/`，随后提取这些文件。

---

## 常用命令

```bash
/graphify .                        # build graph for current folder
/graphify ./docs --update          # re-extract only changed files
/graphify . --cluster-only         # rerun clustering without re-extracting
/graphify . --cluster-only --resolution 1.5      # more granular communities
/graphify . --cluster-only --exclude-hubs 99     # suppress utility super-hubs from god-node rankings
/graphify . --no-viz               # skip the HTML, just the report + JSON
/graphify . --wiki                 # build a markdown wiki from the graph
graphify export callflow-html      # Mermaid architecture/call-flow HTML (auto-regenerates on every git commit if hook is installed)

/graphify query "what connects auth to the database?"
/graphify path "UserService" "DatabasePool"
/graphify explain "RateLimiter"

/graphify add https://arxiv.org/abs/1706.03762   # fetch a paper and add it
/graphify add <youtube-url>                       # transcribe and add a video

graphify hook install              # auto-rebuild on git commit
graphify merge-graphs a.json b.json              # combine two graphs

graphify prs                       # PR dashboard: CI state, review status, worktree mapping
graphify prs 42                    # deep dive on PR #42 with graph impact
graphify prs --triage              # AI ranks your review queue (uses whatever backend is configured)
graphify prs --conflicts           # PRs sharing graph communities — merge-order risk
```

详见下方 [完整命令参考](#full-command-reference)。

---

## 忽略文件规则

在项目根目录创建 `.graphifyignore` — 语法与 `.gitignore` 相同，支持 `!` 取反：

```
# .graphifyignore
node_modules/
dist/
*.generated.py

# only index src/, ignore everything else
*
!src/
!src/**
```

---

## 团队协作配置

建议将 `graphify-out/` 提交至 git，以便团队成员共享同一份知识图谱。

**推荐的 `.gitignore` 添加项：**
```
graphify-out/manifest.json    # mtime-based, breaks after git clone
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

**工作流：**
1. 由一人运行 `/graphify .` 并提交 `graphify-out/`。
2. 其他人拉取代码后，其助手即可立即读取图谱。
3. 运行 `graphify hook install` 可在每次 git commit 后自动重建（仅处理 AST，无 API 成本）。同时会配置 git merge driver，确保 `graph.json` 永远不会残留冲突标记 — 两位开发者并行提交时，其图谱会自动进行并集合并。
4. 当文档或论文更新时，运行 `/graphify --update` 刷新相关节点。

---

## 直接使用知识图谱

```bash
# query the graph from the terminal
graphify query "show the auth flow"
graphify query "what connects DigestAuth to Response?" --graph graphify-out/graph.json

# expose the graph as an MCP server (for repeated tool-call access)
python -m graphify.serve graphify-out/graph.json

# register with Kimi Code:
kimi mcp add --transport stdio graphify -- python -m graphify.serve graphify-out/graph.json
```

MCP Server 为你的助手提供结构化访问权限：`query_graph`、`get_node`、`get_neighbors`、`shortest_path`、`list_prs`、`get_pr_impact`、`triage_prs`。

> **WSL / Linux 注意事项：** Ubuntu 默认提供 `python3` 而非 `python`。建议使用 venv 避免冲突：
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## 环境变量

这些仅用于 **无头/CI 模式提取**（`graphify extract`）。通过 IDE 内的 `/graphify` 技能运行时，模型 API 由你的 IDE 会话提供——无需额外配置密钥。

| Variable | Used for | When required |
|---|---|---|
| `ANTHROPIC_API_KEY` | Claude (Anthropic) backend | `--backend claude` |
| `GEMINI_API_KEY` or `GOOGLE_API_KEY` | Google Gemini backend | `--backend gemini` |
| `OPENAI_API_KEY` | OpenAI or OpenAI-compatible APIs | `--backend openai` |
| `DEEPSEEK_API_KEY` | DeepSeek backend | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Kimi Code backend | `--backend kimi` |
| `OLLAMA_BASE_URL` | Ollama local inference URL | `--backend ollama` (default: `http://localhost:11434`) |
| `OLLAMA_MODEL` | Ollama model name | `--backend ollama` (default: auto-detect) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | Override Ollama KV-cache window size | optional — auto-sized by default |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | Minutes to keep Ollama model loaded | optional — set `0` to unload after each chunk |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — standard credential chain | `--backend bedrock` (no API key, uses IAM) |
| `GRAPHIFY_MAX_WORKERS` | AST parallelism thread count | optional — also `--max-workers` flag |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | Raise output cap for dense corpora | optional — e.g. `32768` for large files |
| `GRAPHIFY_API_TIMEOUT` | HTTP timeout in seconds (default: 600) | optional — also `--api-timeout` flag |
| `GRAPHIFY_FORCE` | Force graph rebuild even with fewer nodes | optional — also `--force` flag |
| `GRAPHIFY_GOOGLE_WORKSPACE` | Auto-enable Google Workspace export | optional — set to `1` |
| `GRAPHIFY_TRIAGE_BACKEND` | Backend for `graphify prs --triage` | optional — auto-detected from available keys |
| `GRAPHIFY_TRIAGE_MODEL` | Model override for triage | optional — e.g. `claude-opus-4-7` |

---

## 隐私说明

- **代码文件** — 通过 tree-sitter 在本地处理。数据不会离开你的设备。
- **视频/音频** — 使用 faster-whisper 在本地转录。数据不会离开你的设备。
- **文档、PDF、图片** — 发送至你的 AI 助手进行语义提取（通过 `/graphify` 技能，使用你 IDE 会话运行的任意模型）。无头模式 `graphify extract` 需要设置以下任一后端：`GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini)、`MOONSHOT_API_KEY` (Kimi)、`ANTHROPIC_API_KEY` (Claude)、`OPENAI_API_KEY` (OpenAI)、`DEEPSEEK_API_KEY` (DeepSeek)、运行中的 Ollama 实例（`OLLAMA_BASE_URL`）、标准凭证链的 AWS 凭据（Bedrock - 无需 API Key，使用 IAM），或 `claude` CLI 二进制文件（Claude Code - 无需 API Key，使用你的 Claude 订阅）。`--dedup-llm` 标志使用相同的密钥。
- **数据驻留** — `graphify extract` 会根据已设置的 API Key 自动检测后端优先级：Gemini → Kimi → Claude → OpenAI → DeepSeek → Bedrock → Ollama。对于有数据驻留要求的代码，请使用 `--backend ollama`（完全本地）或显式传递 `--backend` 参数。Kimi (`MOONSHOT_API_KEY`) 会路由至中国境内的 Moonshot AI 服务器。
- 无遥测、无使用追踪、无数据分析。

---

## 故障排除

**执行 `pip install graphifyy` 后提示 `graphify: command not found`**
pip 会将脚本安装到用户 bin 目录，该路径可能未包含在你的 PATH 中。修复方法：
- macOS：在 `~/.zshrc` 中将 `~/Library/Python/3.x/bin` 添加到你的 PATH
- Linux：在 `~/.bashrc` 中将 `~/.local/bin` 添加到你的 PATH
- 或使用 `uv tool install graphifyy` / `pipx install graphifyy` — 两者均会自动管理 PATH。

**`python -m graphify` 可用但 `graphify` 命令不可用**
你的 shell PATH 未包含 Python 脚本目录。建议改用 `uv` 或 `pipx`，而非原生 `pip`。

**在 PowerShell 中执行 `/graphify .` 提示 "path not recognized"**
PowerShell 将前导斜杠视为路径分隔符。请在 Windows 上使用 `graphify .`（不带斜杠）。

**执行 `--update` 或重建后图谱节点变少**
若重构操作删除了文件，旧节点仍会残留。请传递 `--force`（或设置 `GRAPHIFY_FORCE=1`）以强制覆盖，即使新图谱节点较少。

**同一实体出现重复节点（幽灵重复）**
当语义提取与 AST 提取对节点 ID 格式不一致时会发生此情况。运行完整重新提取以清理：
```bash
graphify extract . --force
```

**Ollama 显存不足 / 上下文窗口超限**
KV-cache 窗口默认自动分配，但可能对你的 GPU 过大。请手动调小：
```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backend ollama --token-budget 4000
```

**图谱 HTML 文件过大导致浏览器无法打开（>5000 节点）**
跳过 HTML 生成，直接使用 JSON：
```bash
graphify cluster-only ./my-project --no-viz
graphify query "..."
```

**两位开发者同时提交后 `graph.json` 出现冲突标记**
运行 `graphify hook install` — 它会配置 git merge driver，自动对 `graph.json` 进行并集合并，彻底避免冲突。

**文档或 PDF 提取返回空节点/边**
文档和 PDF 需要调用 LLM。请检查 API Key 是否已设置且后端正确：
```bash
ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend claude
```

**IDE 中提示技能版本不匹配警告**
你安装的 graphify 版本与技能文件不一致。请更新：
```bash
uv tool upgrade graphifyy
graphify install  # overwrites the skill file
```

---

## 完整命令参考

```
/graphify                          # run on current directory
/graphify ./raw                    # run on a specific folder
/graphify ./raw --mode deep        # more aggressive relationship extraction
/graphify ./raw --update           # re-extract only changed files
/graphify ./raw --directed         # preserve edge direction
/graphify ./raw --cluster-only     # rerun clustering on existing graph
/graphify ./raw --no-viz           # skip HTML visualization
/graphify ./raw --obsidian         # generate Obsidian vault
/graphify ./raw --wiki             # build agent-crawlable markdown wiki
/graphify ./raw --svg              # export graph.svg
/graphify ./raw --graphml          # export for Gephi / yEd
/graphify ./raw --neo4j            # generate cypher.txt for Neo4j
/graphify ./raw --neo4j-push bolt://localhost:7687
/graphify ./raw --watch            # auto-sync as files change
/graphify ./raw --mcp              # start MCP stdio server

/graphify add https://arxiv.org/abs/1706.03762
/graphify add <video-url>
/graphify add https://... --author "Name" --contributor "Name"

/graphify query "what connects attention to the optimizer?"
/graphify query "..." --dfs --budget 1500
/graphify path "DigestAuth" "Response"
/graphify explain "SwinTransformer"

graphify uninstall                 # remove from all platforms in one shot
graphify uninstall --purge         # also delete graphify-out/
graphify uninstall --project --platform codex  # remove project-scoped install files only

graphify hook install              # post-commit + post-checkout hooks
graphify hook uninstall
graphify hook status

# always-on assistant instructions - platform-specific
graphify claude install            # CLAUDE.md + PreToolUse hook (Claude Code)
graphify claude uninstall
graphify codex install             # AGENTS.md + PreToolUse hook in .codex/hooks.json (Codex)
graphify opencode install          # AGENTS.md + tool.execute.before plugin (OpenCode)
graphify kilo install              # native Kilo skill + /graphify command + AGENTS.md + .kilo plugin
graphify kilo uninstall
graphify cursor install            # .cursor/rules/graphify.mdc (Cursor)
graphify cursor uninstall
graphify gemini install            # GEMINI.md + BeforeTool hook (Gemini CLI)
graphify gemini uninstall
graphify copilot install           # skill file (GitHub Copilot CLI)
graphify copilot uninstall
graphify aider install             # AGENTS.md (Aider)
graphify aider uninstall
graphify claw install              # AGENTS.md (OpenClaw)
graphify claw uninstall
graphify droid install             # AGENTS.md (Factory Droid)
graphify droid uninstall
graphify trae install              # AGENTS.md (Trae)
graphify trae uninstall
graphify trae-cn install           # AGENTS.md (Trae CN)
graphify trae-cn uninstall
graphify hermes install             # AGENTS.md + ~/.hermes/skills/ (Hermes)
graphify hermes uninstall
graphify amp install               # skill file (Amp)
graphify amp uninstall
graphify kiro install               # .kiro/skills/ + .kiro/steering/graphify.md (Kiro IDE/CLI)
graphify kiro uninstall
graphify pi install                # skill file (Pi coding agent)
graphify pi uninstall
graphify devin install             # skill file + .windsurf/rules/graphify.md (Devin CLI)
graphify devin uninstall
graphify antigravity install       # .agents/rules + .agents/workflows (Google Antigravity)
graphify antigravity uninstall

graphify extract ./docs                        # headless LLM extraction for CI (no IDE needed)
graphify extract ./docs --backend gemini       # explicit backend: gemini, kimi, claude, openai, deepseek, ollama, bedrock, or claude-cli
graphify extract ./docs --backend gemini --model gemini-3.1-pro-preview
graphify extract ./docs --backend ollama       # local Ollama (set OLLAMA_BASE_URL / OLLAMA_MODEL) - no API key needed for loopback
GRAPHIFY_OLLAMA_NUM_CTX=32768 graphify extract ./docs --backend ollama   # override KV-cache window (auto-sized by default)
GRAPHIFY_OLLAMA_KEEP_ALIVE=0 graphify extract ./docs --backend ollama    # unload model after each chunk (saves VRAM on small GPUs)
graphify extract ./docs --backend bedrock      # AWS Bedrock via IAM - no API key, uses AWS credential chain
graphify extract ./docs --backend claude-cli   # route through Claude Code CLI - no API key, uses your Claude subscription
graphify extract ./docs --max-workers 16       # AST parallelism (also GRAPHIFY_MAX_WORKERS)
graphify extract ./docs --token-budget 30000   # smaller semantic chunks for local/small models
graphify extract ./docs --max-concurrency 2    # fewer parallel LLM calls (useful for local inference)
graphify extract ./docs --api-timeout 900      # longer HTTP timeout for slow local models (default 600s)
graphify extract ./docs --google-workspace     # export .gdoc/.gsheet/.gslides via gws before extraction
graphify extract ./docs --mode deep            # richer semantic extraction via extended system prompt
graphify extract ./docs --no-cluster           # raw extraction only, skip clustering
graphify extract ./docs --force                # overwrite graph.json even if new graph has fewer nodes (use after refactors or to clear ghost duplicates)
graphify extract ./docs --dedup-llm            # LLM tiebreaker for ambiguous entity pairs (uses same API key)
graphify extract ./docs --global --as myrepo   # extract and register into the cross-project global graph
GRAPHIFY_MAX_OUTPUT_TOKENS=32768 graphify extract ./docs --backend claude  # raise output cap for dense corpora

graphify export callflow-html                       # graphify-out/<project>-callflow.html
graphify export callflow-html --max-sections 8      # cap generated architecture sections
graphify export callflow-html --output docs/arch.html
graphify export callflow-html ./some-repo/graphify-out

graphify global add graphify-out/graph.json myrepo   # register a project graph into ~/.graphify/global.json
graphify global remove myrepo                         # remove a project from the global graph
graphify global list                                  # show all registered repos + node/edge counts
graphify global path                                  # print path to the global graph file

graphify prs                              # PR dashboard: CI, review, worktree, graph impact
graphify prs 42                           # deep dive on PR #42
graphify prs --triage                     # AI triage ranking (auto-detects backend from env)
graphify prs --worktrees                  # worktree → branch → PR mapping
graphify prs --conflicts                  # PRs sharing graph communities (merge-order risk)
graphify prs --base main                  # filter to PRs targeting a specific base branch
graphify prs --repo owner/repo            # run against a different GitHub repo
GRAPHIFY_TRIAGE_BACKEND=kimi graphify prs --triage   # use a specific backend for triage

graphify clone https://github.com/karpathy/nanoGPT
graphify merge-graphs a.json b.json --out merged.json
graphify --version                                    # print installed version
graphify watch ./src
graphify check-update ./src
graphify update ./src
graphify update ./src --no-cluster  # skip reclustering, write raw AST graph only
graphify update ./src --force       # overwrite even if new graph has fewer nodes
graphify cluster-only ./my-project
graphify cluster-only ./my-project --graph path/to/graph.json  # custom graph location
graphify cluster-only ./my-project --resolution 1.5            # more, smaller communities
graphify cluster-only ./my-project --exclude-hubs 99           # exclude p99 degree nodes from partitioning
graphify cluster-only ./my-project --no-label                  # keep "Community N" placeholders
graphify cluster-only ./my-project --backend=gemini            # backend for community naming
graphify label ./my-project                                    # (re)name communities with the configured backend
graphify label ./my-project --backend=openai                   # force a specific backend
```

> **社区命名说明：** 在 Agent（Claude Code、Gemini CLI）内部，Agent 会自动为社区命名。当你在裸 CLI 中运行时，`cluster-only` 会使用配置的后端自动命名内置或自定义 OpenAI 兼容提供商——传递 `--no-label` 可保留 `Community N` 占位符，或运行 `graphify label` 按需（重新）生成名称。

---

## 了解更多

- [How it works](docs/how-it-works.md) — 提取流水线、社区检测、置信度评分、基准测试
- [ARCHITECTURE.md](ARCHITECTURE.md) — 模块拆解、如何添加新语言支持
- [Optional integrations](docs/docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite

---

## 基于 Graphify 构建 —— Penpax

[**Penpax**](https://graphifylabs.ai) 是建立在 graphify 之上的常驻层——它将相同的图谱方法应用于你的整个工作流：会议记录、浏览器历史、邮件、文件及代码，并在后台持续更新。

专为跨数百场对话和文档工作的专业人士打造，这些数据通常无法被完整重建。无云端依赖，完全本地运行。

**免费试用即将上线。** [加入等待列表 →](https://graphifylabs.ai)

---

<details>
<summary>贡献指南</summary>

### 开发环境配置

本项目使用 [uv](https://docs.astral.sh/uv/) 管理开发工作流。安装一次后即可：

```bash
git clone https://github.com/safishamsi/graphify.git
cd graphify
git checkout v8                        # active development branch

# Create the project venv and install graphify + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

验证可编辑安装：
```bash
uv run graphify --version
uv run python -c "import graphify; print(graphify.__file__)"
```

### 运行测试

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> macOS 注意事项：测试套件包含 `sample.f90` 和 `sample.F90` 两个 fixture。它们在大小写不敏感的 HFS+ / APFS 文件系统上会产生冲突。若需同时测试两种 Fortran 变体，请在 Linux 或 Docker 容器中运行。

### Git 工作流

- 活跃开发均在 `v8` 分支进行。
- Commit 规范：`fix: <description>` / `feat: <description>` / `docs: <description>`
- 提交 PR 前，请运行 `uv run pytest tests/ -q` 确认测试通过。
- 为新语言提取器添加 fixture 文件至 `tests/fixtures/`，并在 `tests/test_languages.py` 中添加对应测试。

### 贡献方向

**实际案例（Worked examples）** 是最有价值的贡献。对一个真实语料库运行 `/graphify`，将输出保存至 `worked/{slug}/`，撰写一份诚实的 `review.md` 说明图谱做对和做错的地方，然后提交 PR。

**提取 Bug** — 在 Issue 中提供输入文件、缓存条目（`graphify-out/cache/`）以及遗漏或错误的结果。

模块职责与新增语言支持方法详见 [ARCHITECTURE.md](ARCHITECTURE.md)。

</details>