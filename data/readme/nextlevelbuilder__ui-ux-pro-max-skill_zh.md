# [UI UX Pro Max](https://uupm.cc)
 
<p align="center">
  <a href="https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/releases"><img src="https://img.shields.io/github/v/release/nextlevelbuilder/ui-ux-pro-max-skill?style=for-the-badge&color=blue" alt="GitHub Release"></a>
  <img src="https://img.shields.io/badge/reasoning_rules-161-green?style=for-the-badge" alt="161 Reasoning Rules">
  <img src="https://img.shields.io/badge/UI_styles-67-purple?style=for-the-badge" alt="67 UI Styles">
  <img src="https://img.shields.io/badge/python-3.x-yellow?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.x">
  <a href="https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/LICENSE"><img src="https://img.shields.io/github/license/nextlevelbuilder/ui-ux-pro-max-skill?style=for-the-badge&color=green" alt="License"></a>
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/uipro-cli"><img src="https://img.shields.io/npm/v/uipro-cli?style=flat-square&logo=npm&label=CLI" alt="npm"></a>
  <a href="https://www.npmjs.com/package/uipro-cli"><img src="https://img.shields.io/npm/dm/uipro-cli?style=flat-square&label=downloads" alt="npm downloads"></a>
  <a href="https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/stargazers"><img src="https://img.shields.io/github/stars/nextlevelbuilder/ui-ux-pro-max-skill?style=flat-square&logo=github" alt="GitHub stars"></a>
  <a href="https://paypal.me/uiuxpromax"><img src="https://img.shields.io/badge/PayPal-Support%20Development-00457C?style=flat-square&logo=paypal&logoColor=white" alt="PayPal"></a>
</p>

一款提供设计智能的 AI 技能，助力你在多平台与框架下构建专业的 UI/UX。

<p align="center">
  <a href="https://uupm.cc">
    <img src="screenshots/website.png" alt="UI UX Pro Max" width="800">
  </a>
</p>

<p align="center">
  <b>如果你觉得这个项目有用，请考虑支持我们：</b><br><br>
  <a href="https://paypal.me/uiuxpromax"><img src="https://img.shields.io/badge/PayPal-Donate-00457C?style=for-the-badge&logo=paypal&logoColor=white" alt="PayPal Donate"></a>
</p>

<p align="center">
  <i>其他项目</i><br>
  <a href="https://nextlevelbuilder.io">NextLevelBuilder.io</a> | <a href="https://goclaw.sh">GoClaw.sh</a> | <a href="https://claudekit.cc">ClaudeKit.cc</a> | <a href="https://tose.sh">TOSE.sh</a>
</p>

## v2.0 新功能

### 智能设计系统生成

v2.0 的核心功能是**设计系统生成器（Design System Generator）**——一个基于 AI 的推理引擎，能在几秒内分析你的项目需求并生成完整、量身定制的设计系统。

```
+----------------------------------------------------------------------------------------+
|  TARGET: Serenity Spa - RECOMMENDED DESIGN SYSTEM                                      |
+----------------------------------------------------------------------------------------+
|                                                                                        |
|  PATTERN: Hero-Centric + Social Proof                                                  |
|     Conversion: Emotion-driven with trust elements                                     |
|     CTA: Above fold, repeated after testimonials                                       |
|     Sections:                                                                          |
|       1. Hero                                                                          |
|       2. Services                                                                      |
|       3. Testimonials                                                                  |
|       4. Booking                                                                       |
|       5. Contact                                                                       |
|                                                                                        |
|  STYLE: Soft UI Evolution                                                              |
|     Keywords: Soft shadows, subtle depth, calming, premium feel, organic shapes        |
|     Best For: Wellness, beauty, lifestyle brands, premium services                     |
|     Performance: Excellent | Accessibility: WCAG AA                                    |
|                                                                                        |
|  COLORS:                                                                               |
|     Primary:    #E8B4B8 (Soft Pink)                                                    |
|     Secondary:  #A8D5BA (Sage Green)                                                   |
|     CTA:        #D4AF37 (Gold)                                                         |
|     Background: #FFF5F5 (Warm White)                                                   |
|     Text:       #2D3436 (Charcoal)                                                     |
|     Notes: Calming palette with gold accents for luxury feel                           |
|                                                                                        |
|  TYPOGRAPHY: Cormorant Garamond / Montserrat                                           |
|     Mood: Elegant, calming, sophisticated                                              |
|     Best For: Luxury brands, wellness, beauty, editorial                               |
|     Google Fonts: https://fonts.google.com/share?selection.family=...                  |
|                                                                                        |
|  KEY EFFECTS:                                                                          |
|     Soft shadows + Smooth transitions (200-300ms) + Gentle hover states                |
|                                                                                        |
|  AVOID (Anti-patterns):                                                                |
|     Bright neon colors + Harsh animations + Dark mode + AI purple/pink gradients       |
|                                                                                        |
|  PRE-DELIVERY CHECKLIST:                                                               |
|     [ ] No emojis as icons (use SVG: Heroicons/Lucide)                                 |
|     [ ] cursor-pointer on all clickable elements                                       |
|     [ ] Hover states with smooth transitions (150-300ms)                               |
|     [ ] Light mode: text contrast 4.5:1 minimum                                        |
|     [ ] Focus states visible for keyboard nav                                          |
|     [ ] prefers-reduced-motion respected                                               |
|     [ ] Responsive: 375px, 768px, 1024px, 1440px                                       |
|                                                                                        |
+----------------------------------------------------------------------------------------+
```

### 设计系统生成原理

```
┌─────────────────────────────────────────────────────────────────┐
│  1. USER REQUEST                                                │
│     "Build a landing page for my beauty spa"                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  2. MULTI-DOMAIN SEARCH (5 parallel searches)                   │
│     • Product type matching (161 categories)                    │
│     • Style recommendations (67 styles)                         |
│     • Color palette selection (161 palettes)                    |
│     • Landing page patterns (24 patterns)                       |
│     • Typography pairing (57 font combinations)                 |
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  3. REASONING ENGINE                                            │
│     • Match product → UI category rules                         |
│     • Apply style priorities (BM25 ranking)                     |
│     • Filter anti-patterns for industry                         |
│     • Process decision rules (JSON conditions)                  |
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  4. COMPLETE DESIGN SYSTEM OUTPUT                               │
│     Pattern + Style + Colors + Typography + Effects             |
│     + Anti-patterns to avoid + Pre-delivery checklist           |
└─────────────────────────────────────────────────────────────────┘
```

### 161 条行业专属推理规则

该推理引擎包含以下领域的专用规则：

| Category | Examples |
|----------|----------|
| **科技与 SaaS** | SaaS, Micro SaaS, B2B Service, Developer Tool / IDE, AI/Chatbot Platform, Cybersecurity Platform |
| **金融** | Fintech/Crypto, Banking, Insurance, Personal Finance Tracker, Invoice & Billing Tool |
| **医疗健康** | Medical Clinic, Pharmacy, Dental, Veterinary, Mental Health, Medication Reminder |
| **电子商务** | General, Luxury, Marketplace (P2P), Subscription Box, Food Delivery |
| **服务行业** | Beauty/Spa, Restaurant, Hotel, Legal, Home Services, Booking & Appointment |
| **创意产业** | Portfolio, Agency, Photography, Gaming, Music Streaming, Photo/Video Editor |
| **生活方式** | Habit Tracker, Recipe & Cooking, Meditation, Weather, Diary, Mood Tracker |
| **新兴科技** | Web3/NFT, Spatial Computing, Quantum Computing, Autonomous Drone Fleet |

每条规则均包含：
- **推荐布局模式（Recommended Pattern）** - 落地页结构建议
- **风格优先级（Style Priority）** - 最佳匹配的 UI 风格
- **色彩氛围（Color Mood）** - 符合行业调性的配色方案
- **字体气质（Typography Mood）** - 匹配品牌个性的字体组合
- **核心动效（Key Effects）** - 推荐动画与交互效果
- **反模式（Anti-Patterns）** - 应避免的做法（例如：“银行类应用禁止使用 AI 紫/粉色渐变”）

## 功能特性

- **67 种 UI 风格** - Glassmorphism、Claymorphism、Minimalism、Brutalism、Neumorphism、Bento Grid、Dark Mode、AI-Native UI 等
- **161 套色彩方案** - 行业专属配色，与 161 种产品类型精准对应（1:1）
- **57 组字体搭配** - 精选排版组合，附带 Google Fonts 引用链接
- **25 种图表类型** - 针对仪表盘与分析页面的推荐方案
- **15 种技术栈** - React, Next.js, Astro, Vue, Nuxt.js, Nuxt UI, Svelte, SwiftUI, React Native, Flutter, HTML+Tailwind, shadcn/ui, Jetpack Compose, Angular, Laravel
- **99 条 UX 规范** - 最佳实践、反模式及无障碍（Accessibility）规则
- **161 条推理规则** - 行业专属设计系统生成（v2.0 新增）

### 可用风格（共 67 种）

<details>
<summary><b>通用风格（49 种）</b></summary>

| # | Style | Best For |
|---|-------|----------|
| 1 | Minimalism & Swiss Style | Enterprise apps, dashboards, documentation |
| 2 | Neumorphism | Health/wellness apps, meditation platforms |
| 3 | Glassmorphism | Modern SaaS, financial dashboards |
| 4 | Brutalism | Design portfolios, artistic projects |
| 5 | 3D & Hyperrealism | Gaming, product showcase, immersive |
| 6 | Vibrant & Block-based | Startups, creative agencies, gaming |
| 7 | Dark Mode (OLED) | Night-mode apps, coding platforms |
| 8 | Accessible & Ethical | Government, healthcare, education |
| 9 | Claymorphism | Educational apps, children's apps, SaaS |
| 10 | Aurora UI | Modern SaaS, creative agencies |
| 11 | Retro-Futurism | Gaming, entertainment, music platforms |
| 12 | Flat Design | Web apps, mobile apps, startup MVPs |
| 13 | Skeuomorphism | Legacy apps, gaming, premium products |
| 14 | Liquid Glass | Premium SaaS, high-end e-commerce |
| 15 | Motion-Driven | Portfolio sites, storytelling platforms |
| 16 | Micro-interactions | Mobile apps, touchscreen UIs |
| 17 | Inclusive Design | Public services, education, healthcare |
| 18 | Zero Interface | Voice assistants, AI platforms |
| 19 | Soft UI Evolution | Modern enterprise apps, SaaS |
| 20 | Neubrutalism | Gen Z brands, startups, Figma-style |
| 21 | Bento Box Grid | Dashboards, product pages, portfolios |
| 22 | Y2K Aesthetic | Fashion brands, music, Gen Z |
| 23 | Cyberpunk UI | Gaming, tech products, crypto apps |
| 24 | Organic Biophilic | Wellness apps, sustainability brands |
| 25 | AI-Native UI | AI products, chatbots, copilots |
| 26 | Memphis Design | Creative agencies, music, youth brands |
| 27 | Vaporwave | Music platforms, gaming, portfolios |
| 28 | Dimensional Layering | Dashboards, card layouts, modals |
| 29 | Exaggerated Minimalism | Fashion, architecture, portfolios |
| 30 | Kinetic Typography | Hero sections, marketing sites |
| 31 | Parallax Storytelling | Brand storytelling, product launches |
| 32 | Swiss Modernism 2.0 | Corporate sites, architecture, editorial |
| 33 | HUD / Sci-Fi FUI | Sci-fi games, space tech, cybersecurity |
| 34 | Pixel Art | Indie games, retro tools, creative |
| 35 | Bento Grids | Product features, dashboards, personal |
| 36 | Spatial UI (VisionOS) | Spatial computing apps, VR/AR |
| 37 | E-Ink / Paper | Reading apps, digital newspapers |
| 38 | Gen Z Chaos / Maximalism | Gen Z lifestyle, music artists |
| 39 | Biomimetic / Organic 2.0 | Sustainability tech, biotech, health |
| 40 | Anti-Polish / Raw Aesthetic | Creative portfolios, artist sites |
| 41 | Tactile Digital / Deformable UI | Modern mobile apps, playful brands |
| 42 | Nature Distilled | Wellness brands, sustainable products |
| 43 | Interactive Cursor Design | Creative portfolios, interactive |
| 44 | Voice-First Multimodal | Voice assistants, accessibility apps |
| 45 | 3D Product Preview | E-commerce, furniture, fashion |
| 46 | Gradient Mesh / Aurora Evolved | Hero sections, backgrounds, creative |
| 47 | Editorial Grid / Magazine | News sites, blogs, magazines |
| 48 | Chromatic Aberration / RGB Split | Music platforms, gaming, tech |
| 49 | Vintage Analog / Retro Film | Photography, music/vinyl brands |

</details>

<details>
<summary><b>落地页风格（8 种）</b></summary>

| # | Style | Best For |
|---|-------|----------|
| 1 | Hero-Centric Design | Products with strong visual identity |
| 2 | Conversion-Optimized | Lead generation, sales pages |
| 3 | Feature-Rich Showcase | SaaS, complex products |
| 4 | Minimal & Direct | Simple products, apps |
| 5 | Social Proof-Focused | Services, B2C products |
| 6 | Interactive Product Demo | Software, tools |
| 7 | Trust & Authority | B2B, enterprise, consulting |
| 8 | Storytelling-Driven | Brands, agencies, nonprofits |

</details>

<details>
<summary><b>BI/数据分析仪表盘风格（10 种）</b></summary>

| # | Style | Best For |
|---|-------|----------|
| 1 | Data-Dense Dashboard | Complex data analysis |
| 2 | Heat Map & Heatmap Style | Geographic/behavior data |
| 3 | Executive Dashboard | C-suite summaries |
| 4 | Real-Time Monitoring | Operations, DevOps |
| 5 | Drill-Down Analytics | Detailed exploration |
| 6 | Comparative Analysis Dashboard | Side-by-side comparisons |
| 7 | Predictive Analytics | Forecasting, ML insights |
| 8 | User Behavior Analytics | UX research, product analytics |
| 9 | Financial Dashboard | Finance, accounting |
| 10 | Sales Intelligence Dashboard | Sales teams, CRM |

</details>

## 安装指南

### 通过 Claude 市场安装（适用于 Claude Code）

在 Claude Code 中只需两条命令即可直接安装：

```
/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
/plugin install ui-ux-pro-max@ui-ux-pro-max-skill
```

### 使用 CLI 安装（推荐）

```bash
# Install CLI globally
npm install -g uipro-cli

# Go to your project
cd /path/to/your/project

# Install for your AI assistant
uipro init --ai claude      # Claude Code
uipro init --ai cursor      # Cursor
uipro init --ai windsurf    # Windsurf
uipro init --ai antigravity # Antigravity
uipro init --ai copilot     # GitHub Copilot
uipro init --ai kiro        # Kiro
uipro init --ai codex       # Codex CLI
uipro init --ai qoder       # Qoder
uipro init --ai roocode     # Roo Code
uipro init --ai gemini      # Gemini CLI
uipro init --ai trae        # Trae
uipro init --ai opencode    # OpenCode
uipro init --ai continue    # Continue
uipro init --ai codebuddy   # CodeBuddy
uipro init --ai droid       # Droid (Factory)
uipro init --ai kilocode    # KiloCode
uipro init --ai warp        # Warp
uipro init --ai augment     # Augment
uipro init --ai all         # All assistants
```

### 全局安装（适用于所有项目）

```bash
uipro init --ai claude --global   # Install to ~/.claude/skills/
uipro init --ai cursor --global   # Install to ~/.cursor/skills/
```

### 其他 CLI 命令

```bash
uipro versions              # List available versions
uipro update                # Update to latest version
uipro init --offline        # Skip GitHub download, use bundled assets
uipro uninstall             # Remove skill (auto-detect platform)
uipro uninstall --ai claude # Remove specific platform
uipro uninstall --global    # Remove from global install
```

## 环境要求

搜索脚本需要 Python 3.x。

```bash
# Check if Python is installed
python3 --version

# macOS
brew install python3

# Ubuntu/Debian
sudo apt update && sudo apt install python3

# Windows
winget install Python.Python.3.12
```

## 使用指南

### 技能模式（自动激活）

**支持的平台：** Claude Code, Cursor, Windsurf, Antigravity, Codex CLI, Continue, Gemini CLI, OpenCode, Qoder, CodeBuddy, Droid (Factory), KiloCode, Warp, Augment

当你提出 UI/UX 相关需求时，该技能会自动激活。只需自然对话即可：

```
Build a landing page for my SaaS product
```

> **Trae**：请先切换到 **SOLO** 模式。该技能将在你提出 UI/UX 需求时自动激活。

### 工作流模式（斜杠命令）

**支持的平台：** Kiro, GitHub Copilot, Roo Code, KiloCode

使用斜杠命令调用该技能：

```
/ui-ux-pro-max Build a landing page for my SaaS product
```

### 示例提示词

```
Build a landing page for my SaaS product

Create a dashboard for healthcare analytics

Design a portfolio website with dark mode

Make a mobile app UI for e-commerce

Build a fintech banking app with dark theme
```

### 工作原理

1. **提出需求** - 描述你的任何 UI/UX 任务（构建、设计、创建、实现、审查、修复或优化）
2. **生成设计系统** - AI 自动通过推理引擎生成完整的设计系统
3. **智能推荐** - 根据你的产品类型和需求，匹配最合适的风格、色彩与字体
4. **代码生成** - 按照最佳实践实现 UI，并正确应用色彩、字体、间距等
5. **交付前检查** - 验证是否符合常见的 UI/UX 反模式规范

### 支持的技术栈

该技能提供以下技术栈的专属指南：

| Category | Stacks |
|----------|--------|
| **Web（HTML）** | HTML + Tailwind (default) |
| **React 生态** | React, Next.js, shadcn/ui |
| **Vue 生态** | Vue, Nuxt.js, Nuxt UI |
| **Angular** | Angular |
| **PHP** | Laravel (Blade, Livewire, Inertia.js) |
| **其他 Web 框架** | Svelte, Astro |
| **iOS** | SwiftUI |
| **Android** | Jetpack Compose |
| **跨平台开发** | React Native, Flutter |

在提示词中提及你偏好的技术栈即可，若不指定则默认使用 HTML + Tailwind。

## 设计系统命令（高级用法）

如需直接调用设计系统生成器：

> **注意：** 如果你是通过 Continue 安装的，请将下方命令中的 `.claude/skills/` 替换为 `.continue/skills/`。对于 Droid (Factory)，请使用 `.factory/skills/`。

```bash
# Generate design system with ASCII output
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "beauty spa wellness" --design-system -p "Serenity Spa"

# Generate with Markdown output
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "fintech banking" --design-system -f markdown

# Domain-specific search
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "glassmorphism" --domain style
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "elegant serif" --domain typography
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "dashboard" --domain chart

# Stack-specific guidelines
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "form validation" --stack react
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "responsive layout" --stack html-tailwind
```

### 持久化设计系统（主文件 + 覆盖模式）

将你的设计系统保存到文件中，以支持**跨会话的层级检索**：

```bash
# Generate and persist to design-system/MASTER.md
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "SaaS dashboard" --design-system --persist -p "MyApp"

# Also create a page-specific override file
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "SaaS dashboard" --design-system --persist -p "MyApp" --page "dashboard"
```

这将生成如下 `design-system/` 目录结构：

```
design-system/
├── MASTER.md           # Global Source of Truth (colors, typography, spacing, components)
└── pages/
    └── dashboard.md    # Page-specific overrides (only deviations from Master)
```

**层级检索机制：**
1. 构建特定页面（例如“结账页”）时，首先检查 `design-system/pages/checkout.md`
2. 若该页面文件存在，其规则将**覆盖**主文件（Master）中的设置
3. 若不存在，则仅使用 `design-system/MASTER.md`

**上下文感知检索提示词：**
```
I am building the [Page Name] page. Please read design-system/MASTER.md.
Also check if design-system/pages/[page-name].md exists.
If the page file exists, prioritize its rules.
If not, use the Master rules exclusively.
Now, generate the code...
```

## 架构与贡献指南

### 面向用户

代码库已重构为基于**模板的生成系统**。所有平台专属文件（`.cursor/`、`.windsurf/`、`.kiro/`、`.factory/` 等）现均由 CLI 动态生成。

**请务必使用 CLI 进行安装：**

```bash
npm install -g uipro-cli
uipro init --ai <platform>
```

这能确保你获取最新的模板，并获得与你 AI 助手匹配的正确文件结构。

### 面向贡献者

如果你想为本项目做出贡献：

```bash
# 1. Clone the repository
git clone https://github.com/nextlevelbuilder/ui-ux-pro-max-skill.git
cd ui-ux-pro-max-skill

# 2. Understand the structure
src/ui-ux-pro-max/           # Source of truth (data, scripts, templates)
cli/                         # CLI installer (generates files from templates)
.claude/                     # Local dev/test for Claude Code skill
.factory/                    # Local dev/test for Droid (Factory) skill

# 3. Make changes in src/ui-ux-pro-max/
# - data/*.csv              → Database files
# - scripts/*.py            → Search engine & design system
# - templates/              → Platform-specific templates

# 4. Sync to CLI and test locally
cp -r src/ui-ux-pro-max/data/* cli/assets/data/
cp -r src/ui-ux-pro-max/scripts/* cli/assets/scripts/
cp -r src/ui-ux-pro-max/templates/* cli/assets/templates/

# 5. Build and test CLI
cd cli && bun run build
node dist/index.js init --ai claude --offline  # Test in a temp folder

# 6. Create PR (never push directly to main)
git checkout -b feat/your-feature
git commit -m "feat: description"
git push -u origin feat/your-feature
gh pr create
```

详细开发指南请参阅 [CLAUDE.md](CLAUDE.md)。

## ⭐ Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=nextlevelbuilder/ui-ux-pro-max-skill&type=Date)](https://star-history.com/#nextlevelbuilder/ui-ux-pro-max-skill&Date)

## 许可证

本项目采用 [MIT 许可证](LICENSE)。