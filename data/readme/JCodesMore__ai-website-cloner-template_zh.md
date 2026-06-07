# AI 网站克隆模板

<a href="https://github.com/JCodesMore/ai-website-cloner-template/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT License" /></a> <a href="https://github.com/JCodesMore/ai-website-cloner-template/stargazers"><img src="https://img.shields.io/github/stars/JCodesMore/ai-website-cloner-template?style=flat" alt="Stars" /></a> <a href="https://discord.gg/hrTSX5yTpB"><img src="https://img.shields.io/discord/1400896964597383279?label=discord" alt="Discord" /></a>

一个可复用的模板，用于借助 AI 编程代理将任意网站逆向工程为干净、现代的 Next.js 代码库。 

**推荐：使用 [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (Opus 4.7 模型) 以获得最佳效果** — 但也兼容多种 AI 编程代理。

指向目标 URL，运行 `/clone-website`，你的 AI 代理将检查网站、提取设计令牌（tokens）与资源文件、编写组件规范，并调度并行构建器以重建各个页面区块。

## Demo

[![Watch the demo](docs/design-references/comparison.png)](https://youtu.be/O669pVZ_qr0)

> 点击上图在 YouTube 观看完整演示。

## Quick Start

> **重要提示：** 请首先使用 GitHub 的 **使用此模板 (Use this template)** 按钮创建你自己的副本。请勿直接克隆此模板仓库用于你的网站项目，也请勿在此提交包含你生成网站的 Pull Request。

1. **基于此模板创建你自己的仓库**

   在此项目的 GitHub 页面上，点击 **使用此模板**，然后点击 **创建新仓库**。

   为你的新仓库命名，选择公开或私有属性，然后单击 **创建仓库**。如果 GitHub 显示 **包含所有分支 (Include all branches)** 选项，你可以忽略它。

   这将为你提供一个独立的工作项目，确保你的网站修改保留在你的账户中，而不会回传到主模板仓库。

2. **在本地打开你的新仓库**

   GitHub 创建副本后，打开该新仓库。点击 **代码 (Code)** 按钮，使用你偏好的编程工具打开或克隆你的新仓库。

   如果使用终端，命令如下：

   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-NEW-REPOSITORY.git
   cd YOUR-NEW-REPOSITORY
   ```

3. **安装依赖项**
   ```bash
   npm install
   ```
4. **启动你的 AI 代理** — 推荐使用 Claude Code：
   ```bash
   claude --chrome
   ```
5. **运行技能指令**：
   ```
   /clone-website <target-url1> [<target-url2> ...]
   ```
6. **自定义**（可选）— 基础克隆完成后，按需进行修改

> 使用其他代理？打开 `AGENTS.md` 查看项目说明 —— 大多数代理会自动读取该文件。

## Supported Platforms

| Agent                                                         | Status                     |
| ------------------------------------------------------------- | -------------------------- |
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code) | **推荐** — Opus 4.7        |
| [Codex CLI](https://github.com/openai/codex)                  | 已支持                     |
| [OpenCode](https://opencode.ai/)                              | 已支持                     |
| [GitHub Copilot](https://github.com/features/copilot)         | 已支持                     |
| [Cursor](https://cursor.com/)                                 | 已支持                     |
| [Windsurf](https://codeium.com/windsurf)                      | 已支持                     |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli)     | 已支持                     |
| [Cline](https://github.com/cline/cline)                       | 已支持                     |
| [Roo Code](https://github.com/RooCodeInc/Roo-Code)            | 已支持                     |
| [Continue](https://continue.dev/)                             | 已支持                     |
| [Amazon Q](https://aws.amazon.com/q/developer/)               | 已支持                     |
| [Augment Code](https://www.augmentcode.com/)                  | 已支持                     |
| [Aider](https://aider.chat/)                                  | 已支持                     |

## Prerequisites

- [Node.js](https://nodejs.org/) 24+
- An AI coding agent (see [Supported Platforms](#supported-platforms))

## Tech Stack

- **Next.js 16** — App Router, React 19, TypeScript strict
- **shadcn/ui** — Radix primitives + Tailwind CSS v4
- **Tailwind CSS v4** — oklch design tokens
- **Lucide React** — default icons (replaced by extracted SVGs during cloning)

## How It Works

The `/clone-website` skill runs a multi-phase pipeline:

1. **Reconnaissance** — screenshots, design token extraction, interaction sweep (scroll, click, hover, responsive)
2. **Foundation** — updates fonts, colors, globals, downloads all assets
3. **Component Specs** — writes detailed spec files (`docs/research/components/`) with exact computed CSS values, states, behaviors, and content
4. **Parallel Build** — dispatches builder agents in git worktrees, one per section/component
5. **Assembly & QA** — merges worktrees, wires up the page, runs visual diff against the original

Each builder agent receives the full component specification inline — exact `getComputedStyle()` values, interaction models, multi-state content, responsive breakpoints, and asset paths. No guessing.

## Use Cases

- **Platform migration** — rebuild a site you own from WordPress/Webflow/Squarespace into a modern Next.js codebase
- **Lost source code** — your site is live but the repo is gone, the developer left, or the stack is legacy. Get the code back in a modern format
- **Learning** — deconstruct how production sites achieve specific layouts, animations, and responsive behavior by working with real code

## Not Intended For

- **Phishing or impersonation** — this project must not be used for deceptive purposes, impersonation, or any activity that breaks the law.
- **Passing off someone's design as your own** — logos, brand assets, and original copy belong to their owners.
- **Violating terms of service** — some sites explicitly prohibit scraping or reproduction. Check first.

## Project Structure

```
src/
  app/              # Next.js routes
  components/       # React components
    ui/             # shadcn/ui primitives
    icons.tsx       # Extracted SVG icons
  lib/utils.ts      # cn() utility
  types/            # TypeScript interfaces
  hooks/            # Custom React hooks
public/
  images/           # Downloaded images from target
  videos/           # Downloaded videos from target
  seo/              # Favicons, OG images
docs/
  research/         # Extraction output & component specs
  design-references/ # Screenshots
scripts/
  sync-agent-rules.sh  # Regenerate agent instruction files
  sync-skills.mjs      # Regenerate /clone-website for all platforms
AGENTS.md           # Agent instructions (single source of truth)
CLAUDE.md           # Claude Code config (imports AGENTS.md)
GEMINI.md           # Gemini CLI config (imports AGENTS.md)
```

## Commands

```bash
npm run dev    # Start dev server
npm run build  # Production build
npm run lint   # ESLint check
npm run typecheck # TypeScript check
npm run check  # Run lint + typecheck + build
```

### If using docker

```bash
docker compose up app --build # build and run the app
docker compose up dev --build # run the app in dev mode on port 3001
```

## Updating for Other Platforms

Two source-of-truth files power all platform support. Edit the source, then run the sync script:

| What                   | Source of truth                         | Sync command                       |
| ---------------------- | --------------------------------------- | ---------------------------------- |
| Project instructions   | `AGENTS.md`                             | `bash scripts/sync-agent-rules.sh` |
| `/clone-website` skill | `.claude/skills/clone-website/SKILL.md` | `node scripts/sync-skills.mjs`     |

Each script regenerates the platform-specific copies automatically. Agents that read the source files natively need no regeneration.


## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=JCodesMore/ai-website-cloner-template&type=Date)](https://star-history.com/#JCodesMore/ai-website-cloner-template&Date)

## License

MIT