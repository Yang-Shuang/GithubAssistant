# baoyu-skills

English | [中文](./README.zh.md)

Baoyu 提供的技能（Skills）集合，用于借助 AI Agent（如 Claude Code、Codex 等）提升日常工作效率。

## 前置条件

- 已安装 Node.js 环境
- 能够运行 `npx bun` 命令

## 安装

> **提示**：本仓库包含 20+ 项技能。仅安装你实际需要的技能——批量安装所有技能会在每次运行时为你的 AI Agent 增加不必要的上下文开销。

### 快速安装（推荐）

```bash
npx skills add jimliu/baoyu-skills
```

### 发布到 ClawHub / OpenClaw

本仓库现在支持将每个 `skills/baoyu-*` 目录单独发布为 ClawHub 技能。

```bash
# 预览将要发布的内容
./scripts/sync-clawhub.sh --dry-run

# 发布 ./skills 下所有已更改的技能
./scripts/sync-clawhub.sh --all
```

ClawHub 以独立方式安装技能，而非作为单一市场捆绑包。发布后，用户可以安装特定技能，例如：

```bash
clawhub install baoyu-image-gen
clawhub install baoyu-markdown-to-html
```

根据 ClawHub 注册表规则，发布到 ClawHub 的技能将以 `MIT-0` 协议开源。

### 注册为插件市场

在 Agent 中运行以下命令：

```bash
/plugin marketplace add JimLiu/baoyu-skills
```

### 安装技能

**选项 1：通过浏览界面**

1. 选择 **Browse and install plugins**（浏览并安装插件）
2. 选择 **baoyu-skills**
3. 选择 **baoyu-skills** 插件
4. 选择 **Install now**（立即安装）

**选项 2：直接安装**

```bash
# 安装市场的单一插件
/plugin install baoyu-skills@baoyu-skills
```

**选项 3：让 Agent 帮你安装**

只需告诉 Agent：

> Please install Skills from github.com/JimLiu/baoyu-skills

### 可用插件

市场目前暴露了一个统一插件，确保每项技能仅注册一次。

| 插件 | 描述 | 包含内容 |
|--------|-------------|----------|
| **baoyu-skills** | 日常工作效率提升的内容生成、AI 后端与工具 | 本仓库中的所有技能，下文按内容技能、AI 生成技能和实用工具分类组织 |

## 更新技能

将技能更新至最新版本：

1. 在 Agent 中运行 `/plugin`
2. 切换到 **Marketplaces**（市场）选项卡（使用方向键或 Tab）
3. 选择 **baoyu-skills**
4. 选择 **Update marketplace**（更新市场）

你也可以启用自动更新以获取最新版本。

![更新技能](./screenshots/update-plugins.png)

## 可用技能

技能分为三大类：

### 内容生成技能

用于内容创作与发布的技能。

#### baoyu-xhs-images

小红书图片卡片系列生成器。将内容拆解为 1-10 张卡通风格图片卡片，支持 **风格 × 排版** 系统与可选调色板覆盖。

```bash
# 自动选择风格与排版
/baoyu-xhs-images posts/ai-future/article.md

# 指定风格
/baoyu-xhs-images posts/ai-future/article.md --style notion

# 指定排版
/baoyu-xhs-images posts/ai-future/article.md --layout dense

# 组合风格与排版
/baoyu-xhs-images posts/ai-future/article.md --style notion --layout list

# 覆盖调色板
/baoyu-xhs-images posts/ai-future/article.md --style notion --palette macaron

# 直接输入内容
/baoyu-xhs-images 今日星座运势

# 非交互模式（跳过所有确认，适用于定时任务）
/baoyu-xhs-images posts/ai-future/article.md --yes
/baoyu-xhs-images posts/ai-future/article.md --yes --preset knowledge-card
```

**风格**（视觉美学）：`cute`（默认）、`fresh`、`warm`、`bold`、`minimal`、`retro`、`pop`、`notion`、`chalkboard`、`study-notes`、`screen-print`、`sketch-notes`

**调色板**（可选颜色覆盖）：`macaron`、`warm`、`neon`

**风格预览**：

| | | |
|:---:|:---:|:---:|
| ![cute](./screenshots/xhs-images-styles/cute.webp) | ![fresh](./screenshots/xhs-images-styles/fresh.webp) | ![warm](./screenshots/xhs-images-styles/warm.webp) |
| cute | fresh | warm |
| ![bold](./screenshots/xhs-images-styles/bold.webp) | ![minimal](./screenshots/xhs-images-styles/minimal.webp) | ![retro](./screenshots/xhs-images-styles/retro.webp) |
| bold | minimal | retro |
| ![pop](./screenshots/xhs-images-styles/pop.webp) | ![notion](./screenshots/xhs-images-styles/notion.webp) | ![chalkboard](./screenshots/xhs-images-styles/chalkboard.webp) |
| pop | notion | chalkboard |

**排版**（信息密度）：
| 排版 | 密度 | 适用场景 |
|--------|---------|----------|
| `sparse` | 1-2 pts | 封面、引言 |
| `balanced` | 3-4 pts | 常规内容 |
| `dense` | 5-8 pts | 知识卡片、速查表 |
| `list` | 4-7 items | 清单、排行榜 |
| `comparison` | 2 sides | 前后对比、优缺点 |
| `flow` | 3-6 steps | 流程、时间线 |

**排版预览**：

| | | |
|:---:|:---:|:---:|
| ![sparse](./screenshots/xhs-images-layouts/sparse.webp) | ![balanced](./screenshots/xhs-images-layouts/balanced.webp) | ![dense](./screenshots/xhs-images-layouts/dense.webp) |
| sparse | balanced | dense |
| ![list](./screenshots/xhs-images-layouts/list.webp) | ![comparison](./screenshots/xhs-images-layouts/comparison.webp) | ![flow](./screenshots/xhs-images-layouts/flow.webp) |
| list | comparison | flow |

#### baoyu-infographic

生成专业信息图，支持 21 种排版类型与 21 种视觉风格。分析内容、推荐排版×风格组合，并生成可直接发布的信息图。

```bash
# 根据内容自动推荐组合
/baoyu-infographic path/to/content.md

# 指定排版
/baoyu-infographic path/to/content.md --layout pyramid

# 指定风格（默认：craft-handmade）
/baoyu-infographic path/to/content.md --style technical-schematic

# 同时指定两者
/baoyu-infographic path/to/content.md --layout funnel --style corporate-memphis

# 设置宽高比（命名预设或自定义 W:H）
/baoyu-infographic path/to/content.md --aspect portrait
/baoyu-infographic path/to/content.md --aspect 3:4
```

**选项**：
| 选项 | 描述 |
|--------|-------------|
| `--layout <name>` | 信息排版（20 种可选） |
| `--style <name>` | 视觉风格（17 种可选，默认：craft-handmade） |
| `--aspect <ratio>` | 命名预设：landscape (16:9), portrait (9:16), square (1:1)。自定义：任意 W:H 比例（如 3:4, 4:3, 2.35:1） |
| `--lang <code>` | 输出语言（en, zh, ja 等） |

**排版**（信息结构）：

| 排版 | 适用场景 |
|--------|----------|
| `bridge` | 问题-解决方案、跨越差距 |
| `circular-flow` | 循环、周期性流程 |
| `comparison-table` | 多因素对比 |
| `do-dont` | 正确 vs 错误做法 |
| `equation` | 公式拆解、输入输出 |
| `feature-list` | 产品功能、要点列表 |
| `fishbone` | 根因分析 |
| `funnel` | 转化流程、过滤 |
| `grid-cards` | 多主题、概览 |
| `iceberg` | 表面 vs 隐藏层面 |
| `journey-path` | 用户旅程、里程碑 |
| `layers-stack` | 技术栈、分层架构 |
| `mind-map` | 头脑风暴、概念映射 |
| `nested-circles` | 影响力层级、范围 |
| `priority-quadrants` | 艾森豪威尔矩阵、2x2 |
| `pyramid` | 层级结构、马斯洛需求 |
| `scale-balance` | 优缺点权衡 |
| `timeline-horizontal` | 历史、 chronological 事件 |
| `tree-hierarchy` | 组织架构图、分类法 |
| `venn` | 重叠概念 |

**排版预览**：

| | | |
|:---:|:---:|:---:|
| ![bridge](./screenshots/infographic-layouts/bridge.webp) | ![circular-flow](./screenshots/infographic-layouts/circular-flow.webp) | ![comparison-table](./screenshots/infographic-layouts/comparison-table.webp) |
| bridge | circular-flow | comparison-table |
| ![do-dont](./screenshots/infographic-layouts/do-dont.webp) | ![equation](./screenshots/infographic-layouts/equation.webp) | ![feature-list](./screenshots/infographic-layouts/feature-list.webp) |
| do-dont | equation | feature-list |
| ![fishbone](./screenshots/infographic-layouts/fishbone.webp) | ![funnel](./screenshots/infographic-layouts/funnel.webp) | ![grid-cards](./screenshots/infographic-layouts/grid-cards.webp) |
| fishbone | funnel | grid-cards |
| ![iceberg](./screenshots/infographic-layouts/iceberg.webp) | ![journey-path](./screenshots/infographic-layouts/journey-path.webp) | ![layers-stack](./screenshots/infographic-layouts/layers-stack.webp) |
| iceberg | journey-path | layers-stack |
| ![mind-map](./screenshots/infographic-layouts/mind-map.webp) | ![nested-circles](./screenshots/infographic-layouts/nested-circles.webp) | ![priority-quadrants](./screenshots/infographic-layouts/priority-quadrants.webp) |
| mind-map | nested-circles | priority-quadrants |
| ![pyramid](./screenshots/infographic-layouts/pyramid.webp) | ![scale-balance](./screenshots/infographic-layouts/scale-balance.webp) | ![timeline-horizontal](./screenshots/infographic-layouts/timeline-horizontal.webp) |
| pyramid | scale-balance | timeline-horizontal |
| ![tree-hierarchy](./screenshots/infographic-layouts/tree-hierarchy.webp) | ![venn](./screenshots/infographic-layouts/venn.webp) | |
| tree-hierarchy | venn | |

**风格**（视觉美学）：

| 风格 | 描述 |
|-------|-------------|
| `craft-handmade`（默认） | 手绘插画、纸艺美学 |
| `claymation` | 3D 黏土人偶、趣味定格动画 |
| `kawaii` | 日式可爱风、大眼睛、柔和色彩 |
| `storybook-watercolor` | 柔和水彩插画、奇幻风格 |
| `chalkboard` | 黑板彩色粉笔字 |
| `cyberpunk-neon` | 暗色背景霓虹光效、未来感 |
| `bold-graphic` | 漫画风格、半色调网点、高对比度 |
| `aged-academia` | 复古科学风、棕褐色素描 |
| `corporate-memphis` | 扁平矢量人物、鲜艳填充 |
| `technical-schematic` | 工程蓝图、等轴测 3D、技术图纸 |
| `origami` | 折纸形态、几何风格 |
| `pixel-art` | 复古 8-bit、怀旧游戏风 |
| `ui-wireframe` | 灰度线框、界面原型 |
| `subway-map` | 地铁线路图、彩色线条 |
| `ikea-manual` | 极简线条、组装说明书风格 |
| `knolling` | 平铺整理、俯视视角 |
| `lego-brick` | 乐高积木构造、趣味风 |

**风格预览**：

| | | |
|:---:|:---:|:---:|
| ![craft-handmade](./screenshots/infographic-styles/craft-handmade.webp) | ![claymation](./screenshots/infographic-styles/claymation.webp) | ![kawaii](./screenshots/infographic-styles/kawaii.webp) |
| craft-handmade | claymation | kawaii |
| ![storybook-watercolor](./screenshots/infographic-styles/storybook-watercolor.webp) | ![chalkboard](./screenshots/infographic-styles/chalkboard.webp) | ![cyberpunk-neon](./screenshots/infographic-styles/cyberpunk-neon.webp) |
| storybook-watercolor | chalkboard | cyberpunk-neon |
| ![bold-graphic](./screenshots/infographic-styles/bold-graphic.webp) | ![aged-academia](./screenshots/infographic-styles/aged-academia.webp) | ![corporate-memphis](./screenshots/infographic-styles/corporate-memphis.webp) |
| bold-graphic | aged-academia | corporate-memphis |
| ![technical-schematic](./screenshots/infographic-styles/technical-schematic.webp) | ![origami](./screenshots/infographic-styles/origami.webp) | ![pixel-art](./screenshots/infographic-styles/pixel-art.webp) |
| technical-schematic | origami | pixel-art |
| ![ui-wireframe](./screenshots/infographic-styles/ui-wireframe.webp) | ![subway-map](./screenshots/infographic-styles/subway-map.webp) | ![ikea-manual](./screenshots/infographic-styles/ikea-manual.webp) |
| ui-wireframe | subway-map | ikea-manual |
| ![knolling](./screenshots/infographic-styles/knolling.webp) | ![lego-brick](./screenshots/infographic-styles/lego-brick.webp) | |
| knolling | lego-brick | |

#### baoyu-diagram

从源材料生成可直接发布的 SVG 图表——流程图、序列/协议图、结构/架构图与直观示意图。分析输入内容以推荐图表类型及拆分策略，确认后一次性生成所有图表。Claude 会遵循统一的设计系统直接编写真实的 SVG 代码。输出为自包含的 `.svg` 文件，内置样式并支持自动暗色模式。

```bash
# 主题字符串 — 技能将分析并提出方案
/baoyu-diagram "how JWT authentication works"
/baoyu-diagram "Kubernetes architecture" --type structural
/baoyu-diagram "OAuth 2.0 flow"          --type sequence

# 文件路径 — 技能读取、分析并提出方案
/baoyu-diagram path/to/article.md

# 指定语言与输出路径
/baoyu-diagram "微服务架构" --lang zh
/baoyu-diagram "build pipeline" --out docs/build-pipeline.svg
```

**选项**：
| 选项 | 描述 |
|--------|-------------|
| `--type <name>` | `flowchart`, `sequence`, `structural`, `illustrative`, `class`, `auto`（默认）。跳过类型推荐。 |
| `--lang <code>` | 输出语言（en, zh, ja, ...） |
| `--out <path>` | 输出文件路径。生成聚焦于最重要方面的单一图表。 |

**图表类型**：

| 类型 | 读者需求 | 触发关键词 |
|------|-------------|------------------------|
| `flowchart` | 按顺序带我走一遍步骤 | walk through, steps, process, lifecycle, workflow, state machine |
| `sequence` | 谁在何时与谁通信 | protocol, handshake, auth flow, OAuth, TCP, request/response |
| `structural` | 展示内部结构如何组织 | architecture, components, topology, layout, what's inside |
| `illustrative` | 给我直观理解——画出机制 | how does X work, explain X, intuition for, why does X do Y |
| `class` | 类型有哪些及它们的关系 | class diagram, UML, inheritance, interface, schema |

这不是图像生成技能——不会调用任何 LLM 图像模型。Claude 手动编写 SVG 代码并计算布局数学，因此每张图表都严格遵循设计系统。内嵌 `<style>` 块包含 `@media (prefers-color-scheme: dark)`，使同一文件在嵌入时能正确适配亮色与暗色模式。

#### baoyu-cover-image

为文章生成封面图，支持 5 个维度：类型 × 调色板 × 渲染 × 文字 × 情绪。结合 11 种调色板与 7 种渲染风格，提供 77 种独特组合。

```bash
# 根据内容自动选择所有维度
/baoyu-cover-image path/to/article.md

# 快速模式：跳过确认，使用自动选择
/baoyu-cover-image path/to/article.md --quick

# 指定维度（5D 系统）
/baoyu-cover-image path/to/article.md --type conceptual --palette cool --rendering digital
/baoyu-cover-image path/to/article.md --text title-subtitle --mood bold

# 风格预设（向后兼容简写）
/baoyu-cover-image path/to/article.md --style blueprint

# 指定宽高比（默认：16:9）
/baoyu-cover-image path/to/article.md --aspect 2.35:1

# 仅视觉元素（无标题文字）
/baoyu-cover-image path/to/article.md --no-title
```

**五个维度**：
- **类型**：`hero`, `conceptual`, `typography`, `metaphor`, `scene`, `minimal`
- **调色板**：`warm`, `elegant`, `cool`, `dark`, `earth`, `vivid`, `pastel`, `mono`, `retro`, `duotone`, `macaron`
- **渲染**：`flat-vector`, `hand-drawn`, `painterly`, `digital`, `pixel`, `chalk`, `screen-print`
- **文字**：`none`, `title-only`（默认）, `title-subtitle`, `text-rich`
- **情绪**：`subtle`, `balanced`（默认）, `bold`

#### baoyu-slide-deck

从内容生成专业幻灯片图片。创建包含风格指令的详细大纲，然后逐页生成幻灯片图像。

```bash
# 从 markdown 文件生成
/baoyu-slide-deck path/to/article.md

# 指定风格与受众
/baoyu-slide-deck path/to/article.md --style corporate
/baoyu-slide-deck path/to/article.md --audience executives

# 目标幻灯片数量
/baoyu-slide-deck path/to/article.md --slides 15

# 仅生成大纲（不生成图像）
/baoyu-slide-deck path/to/article.md --outline-only

# 指定语言
/baoyu-slide-deck path/to/article.md --lang zh
```

**选项**：

| 选项 | 描述 |
|--------|-------------|
| `--style <name>` | 视觉风格：预设名称或 `custom` |
| `--audience <type>` | 目标受众：beginners, intermediate, experts, executives, general |
| `--lang <code>` | 输出语言（en, zh, ja 等） |
| `--slides <number>` | 目标幻灯片数量（推荐 8-25，最大 30） |
| `--outline-only` | 仅生成大纲，跳过图像 |
| `--prompts-only` | 生成大纲+提示词，跳过图像 |
| `--images-only` | 从现有提示词生成图像 |
| `--regenerate <N>` | 重新生成指定幻灯片：`3` 或 `2,5,8` |

**风格系统**：

风格由 4 个维度构建：**纹理** × **情绪** × **排版字体** × **密度**

| 维度 | 选项 |
|-----------|---------|
| 纹理 | clean, grid, organic, pixel, paper |
| 情绪 | professional, warm, cool, vibrant, dark, neutral |
| 排版字体 | geometric, humanist, handwritten, editorial, technical |
| 密度 | minimal, balanced, dense |

**预设**（预配置维度组合）：

| 预设 | 维度组合 | 适用场景 |
|--------|------------|----------|
| `blueprint`（默认） | grid + cool + technical + balanced | 架构、系统设计 |
| `chalkboard` | organic + warm + handwritten + balanced | 教育、教程 |
| `corporate` | clean + professional + geometric + balanced | 融资演示文稿、提案 |
| `minimal` | clean + neutral + geometric + minimal | 高管简报 |
| `sketch-notes` | organic + warm + handwritten + balanced | 教育、教程 |
| `watercolor` | organic + warm + humanist + minimal | 生活方式、健康 |
| `dark-atmospheric` | clean + dark + editorial + balanced | 娱乐、游戏 |
| `notion` | clean + neutral + geometric + dense | 产品演示、SaaS |
| `bold-editorial` | clean + vibrant + editorial + balanced | 产品发布、主题演讲 |
| `editorial-infographic` | clean + cool + editorial + dense | 技术解析、研究 |
| `fantasy-animation` | organic + vibrant + handwritten + minimal | 教育叙事 |
| `intuition-machine` | clean + cool + technical + dense | 技术文档、学术 |
| `pixel-art` | pixel + vibrant + technical + balanced | 游戏、开发者大会 |
| `scientific` | clean + cool + technical + dense | 生物、化学、医学 |
| `vector-illustration` | clean + vibrant + humanist + balanced | 创意、儿童内容 |
| `vintage` | paper + warm + editorial + balanced | 历史、传承 |

**风格预览**：

| | | |
|:---:|:---:|:---:|
| ![blueprint](./screenshots/slide-deck-styles/blueprint.webp) | ![chalkboard](./screenshots/slide-deck-styles/chalkboard.webp) | ![bold-editorial](./screenshots/slide-deck-styles/bold-editorial.webp) |
| blueprint | chalkboard | bold-editorial |
| ![corporate](./screenshots/slide-deck-styles/corporate.webp) | ![dark-atmospheric](./screenshots/slide-deck-styles/dark-atmospheric.webp) | ![editorial-infographic](./screenshots/slide-deck-styles/editorial-infographic.webp) |
| corporate | dark-atmospheric | editorial-infographic |
| ![fantasy-animation](./screenshots/slide-deck-styles/fantasy-animation.webp) | ![intuition-machine](./screenshots/slide-deck-styles/intuition-machine.webp) | ![minimal](./screenshots/slide-deck-styles/minimal.webp) |
| fantasy-animation | intuition-machine | minimal |
| ![notion](./screenshots/slide-deck-styles/notion.webp) | ![pixel-art](./screenshots/slide-deck-styles/pixel-art.webp) | ![scientific](./screenshots/slide-deck-styles/scientific.webp) |
| notion | pixel-art | scientific |
| ![sketch-notes](./screenshots/slide-deck-styles/sketch-notes.webp) | ![vector-illustration](./screenshots/slide-deck-styles/vector-illustration.webp) | ![vintage](./screenshots/slide-deck-styles/vintage.webp) |
| sketch-notes | vector-illustration | vintage |
| ![watercolor](./screenshots/slide-deck-styles/watercolor.webp) | | |
| watercolor | | |

生成后，幻灯片将自动合并为 `.pptx` 和 `.pdf` 文件以便分享。

#### baoyu-comic

知识漫画创作工具，支持灵活的艺术风格 × 语气组合。创建原创教育漫画，包含详细的分镜布局与顺序图像生成。

```bash
# 从源材料（自动选择艺术+语气）
/baoyu-comic posts/turing-story/source.md

# 指定艺术风格与语气
/baoyu-comic posts/turing-story/source.md --art manga --tone warm
/baoyu-comic posts/turing-story/source.md --art ink-brush --tone dramatic

# 使用预设（包含特殊规则）
/baoyu-comic posts/turing-story/source.md --style ohmsha
/baoyu-comic posts/turing-story/source.md --style wuxia

# 指定布局与宽高比
/baoyu-comic posts/turing-story/source.md --layout cinematic
/baoyu-comic posts/turing-story/source.md --aspect 16:9

# 指定语言
/baoyu-comic posts/turing-story/source.md --lang zh

# 直接输入内容
/baoyu-comic "The story of Alan Turing and the birth of computer science"
```

**选项**：
| 选项 | 值 |
|--------|--------|
| `--art` | `ligne-claire`（默认）, `manga`, `realistic`, `ink-brush`, `chalk` |
| `--tone` | `neutral`（默认）, `warm`, `dramatic`, `romantic`, `energetic`, `vintage`, `action` |
| `--style` | `ohmsha`, `wuxia`, `shoujo`（带特殊规则的预设） |
| `--layout` | `standard`（默认）, `cinematic`, `dense`, `splash`, `mixed`, `webtoon` |
| `--aspect` | `3:4`（默认，竖屏）, `4:3`（横屏）, `16:9`（宽屏） |
| `--lang` | `auto`（默认）, `zh`, `en`, `ja` 等 |

**艺术风格**（渲染技法）：

| 艺术风格 | 描述 |
|-----------|-------------|
| `ligne-claire` | 均匀线条、平涂色彩，欧洲漫画传统（丁丁历险记、逻辑学漫画） |
| `manga` | 大眼睛、日漫规范、表情丰富 |
| `realistic` | 数字绘画、写实比例、精致细腻 |
| `ink-brush` | 中国水墨笔触、晕染效果 |
| `chalk` | 黑板美学、手绘温度感 |

**语气**（氛围/情绪）：

| 语气 | 描述 |
|------|-------------|
| `neutral` | 平衡、理性、教育向 |
| `warm` | 怀旧、亲切、治愈系 |
| `dramatic` | 高对比度、强烈张力、有冲击力 |
| `romantic` | 柔和、唯美、装饰性元素 |
| `energetic` | 明亮、动态、令人兴奋 |
| `vintage` | 历史感、做旧、时代考据 |
| `action` | 速度线、冲击特效、战斗场面 |

**预设**（艺术+语气+特殊规则）：

| 预设 | 等效组合 | 特殊规则 |
|--------|-----------|---------------|
| `ohmsha` | manga + neutral | 视觉隐喻、禁止头部特写对话、道具揭示 |
| `wuxia` | ink-brush + action | 气劲特效、战斗画面、氛围元素 |
| `shoujo` | manga + romantic | 装饰性元素、眼部细节、浪漫节奏 |

**布局**（分镜排列）：
| 布局 | 每页分镜数 | 适用场景 |
|--------|-------------|----------|
| `standard` | 4-6 | 对话推进、叙事流 |
| `cinematic` | 2-4 | 戏剧性瞬间、全景镜头 |
| `dense` | 6-9 | 技术解析、时间线 |
| `splash` | 1-2 large | 关键节点、重大揭示 |
| `mixed` | 3-7 varies | 复杂叙事、情感弧线 |
| `webtoon` | 3-5 vertical | Ohmsha 教程、手机阅读 |

**布局预览**：

| | | |
|:---:|:---:|:---:|
| ![standard](./screenshots/comic-layouts/standard.webp) | ![cinematic](./screenshots/comic-layouts/cinematic.webp) | ![dense](./screenshots/comic-layouts/dense.webp) |
| standard | cinematic | dense |
| ![splash](./screenshots/comic-layouts/splash.webp) | ![mixed](./screenshots/comic-layouts/mixed.webp) | ![webtoon](./screenshots/comic-layouts/webtoon.webp) |
| splash | mixed | webtoon |

#### baoyu-article-illustrator

智能文章插画技能，采用类型 × 风格 × 调色板三维方法。分析文章结构、识别需要视觉辅助的位置并生成插图。

```bash
# 根据内容自动选择类型与风格
/baoyu-article-illustrator path/to/article.md

# 指定类型与风格
/baoyu-article-illustrator path/to/article.md --type flowchart --style notion

# 覆盖调色板
/baoyu-article-illustrator path/to/article.md --style vector-illustration --palette macaron
```

**类型**（信息结构）：

| 类型 | 描述 | 适用场景 |
|------|-------------|----------|
| `infographic` | 数据可视化、图表、指标展示 | 技术文章、数据分析 |
| `scene` | 氛围插画、情绪渲染 | 叙事类、个人故事 |
| `flowchart` | 流程图、步骤可视化 | 教程、工作流 |
| `comparison` | 左右对比、前后差异 | 产品对比 |
| `framework` | 概念图、关系图谱 | 方法论、架构设计 |
| `timeline` | 时间线推进 | 历史回顾、项目进度 |

**风格**（渲染方式）：

| 风格 | 描述 | 适用场景 |
|-------|-------------|----------|
| `notion`（默认） | 极简手绘线条风 | 知识分享、SaaS、效率工具 |
| `elegant` | 精致、高级感 | 商业、思想领导力 |
| `warm` | 亲切、易接近 | 个人成长、生活方式 |
| `minimal` | 超干净、禅意风格 | 哲学、极简主义 |
| `blueprint` | 技术图纸风 | 架构、系统设计 |
| `watercolor` | 柔和艺术感与自然温度 | 生活方式、旅行、创意 |
| `editorial` | 杂志级信息图风格 | 技术解析、新闻报道 |
| `scientific` | 学术精准图表 | 生物、化学、技术文档 |

**调色板**（可选颜色覆盖）：

| 调色板 | 描述 | 适用场景 |
|---------|-------------|----------|
| `macaron` | 暖奶油底色上的柔和马卡龙色块（蓝、薄荷、薰衣草、蜜桃） | 教育、知识科普、教程 |
| `warm` | 暖土色调搭配柔桃背景，无冷色系 | 品牌、产品、生活方式 |
| `neon` | 深紫底色上的鲜艳霓虹光效 | 游戏、复古、流行文化 |

**风格预览**：

| | | |
|:---:|:---:|:---:|
| ![notion](./screenshots/article-illustrator-styles/notion.webp) | ![elegant](./screenshots/article-illustrator-styles/elegant.webp) | ![warm](./screenshots/article-illustrator-styles/warm.webp) |
| notion | elegant | warm |
| ![minimal](./screenshots/article-illustrator-styles/minimal.webp) | ![blueprint](./screenshots/article-illustrator-styles/blueprint.webp) | ![watercolor](./screenshots/article-illustrator-styles/watercolor.webp) |
| minimal | blueprint | watercolor |
| ![editorial](./screenshots/article-illustrator-styles/editorial.webp) | ![scientific](./screenshots/article-illustrator-styles/scientific.webp) | |
| editorial | scientific | |

#### baoyu-post-to-x

将内容与文章发布到 X（Twitter）。支持带图片的普通帖子与 X Articles（长文 Markdown）。使用真实 Chrome 配合 CDP 绕过反自动化检测。

纯文本输入视为普通帖子。Markdown 文件视为 X Articles。脚本会将内容填入浏览器，由你手动审核并发布。

```bash
# 发布文字
/baoyu-post-to-x "Hello from AI Agent!"

# 发布带图片的帖子
/baoyu-post-to-x "Check this out" --image photo.png

# 发布 X Article
/baoyu-post-to-x --article path/to/article.md
```

#### baoyu-post-to-wechat

将内容发布到微信公众号。提供两种模式：

**图文（贴图）** - 多张图片配简短标题/内容：

```bash
/baoyu-post-to-wechat 贴图 --markdown article.md --images ./photos/
/baoyu-post-to-wechat 贴图 --markdown article.md --image img1.png --image img2.png --image img3.png
/baoyu-post-to-wechat 贴图 --title "标题" --content "内容" --image img1.png --submit
```

**文章（文章）** - 完整 markdown/HTML 支持富文本排版：

```bash
/baoyu-post-to-wechat 文章 --markdown article.md
/baoyu-post-to-wechat 文章 --markdown article.md --theme grace
/baoyu-post-to-wechat 文章 --html article.html
```

**发布方式**：

| 方式 | 速度 | 要求 |
|--------|-------|--------------|
| API（推荐） | 快 | API 凭证（需在微信后台配置本地 IP 白名单） |
| 浏览器 | 慢 | Chrome、登录会话 |
| 远程 API | 快 | API 凭证 + SSH 可达服务器（IP 已在微信白名单中） |

**API 配置**（用于更快发布）：

```bash
# 添加到 .baoyu-skills/.env（项目级）或 ~/.baoyu-skills/.env（用户级）
WECHAT_APP_ID=your_app_id
WECHAT_APP_SECRET=your_app_secret
```

获取凭证步骤：
1. 访问 https://developers.weixin.qq.com/platform/
2. 进入：我的业务 → 公众号 → 开发密钥
3. 创建开发密钥并复制 AppID/AppSecret
4. 将本机 IP 加入白名单

**浏览器方式**（无需 API 配置）：需安装 Google Chrome。首次运行会打开浏览器进行扫码登录（会话持久化）。

**远程 API 方式**（适用于微信 IP 白名单未包含你本地机器的情况）：通过 SSH SOCKS5 动态端口转发将微信 API 调用隧道传输至白名单服务器。不会向远程主机写入任何文件，且 `AppSecret` 绝不会离开本地进程。在 EXTEND.md 中添加：

```yaml
# 可选：仅当微信 IP 白名单未包含本机时设置
remote_publish_host: server.example.com
remote_publish_user: deploy
remote_publish_identity_file: ~/.ssh/id_ed25519
```

然后使用 `--remote` 发布（或设置 `default_publish_method: remote-api`）。认证仅支持 SSH 密钥；仅识别已配置的 `remote_publish_*` 键。

**多账号支持**：通过 `EXTEND.md` 管理多个微信公众号：

```bash
mkdir -p .baoyu-skills/baoyu-post-to-wechat
```

创建 `.baoyu-skills/baoyu-post-to-wechat/EXTEND.md`：

```yaml
# 全局设置（所有账号共享）
default_theme: default
default_color: blue

# 账号列表
accounts:
  - name: My Tech Blog
    alias: tech-blog
    default: false
    default_publish_method: api
    default_author: Author Name
    need_open_comment: 1
    only_fans_can_comment: 0
    app_id: your_wechat_app_id
    app_secret: your_wechat_app_secret
  - name: AI Newsletter
    alias: ai-news
    default_publish_method: browser
    default_author: AI Newsletter
    need_open_comment: 1
    only_fans_can_comment: 0
```

| 配置账号数 | 行为 |
|---------------------|----------|
| 无 `accounts` 块 | 单账号模式（向后兼容） |
| 1 个账号 | 自动选择，不提示 |
| 2+ 个账号 | 提示选择，或使用 `--account <alias>` |
| 1 个账号设置 `default: true` | 预设为默认账号 |

每个账号拥有独立的 Chrome 配置文件以实现独立登录会话（浏览器方式）。API 凭证可在 EXTEND.md 中内联配置，或通过 `.env` 使用别名前缀键配置（例如 `WECHAT_TECH_BLOG_APP_ID`）。

#### baoyu-post-to-weibo

将内容发布到微博。支持带文字、图片与视频的普通帖子，以及 Markdown 输入的头条文章。使用真实 Chrome 配合 CDP 绕过反自动化检测。

**普通帖子** - 文字+图片/视频（最多 18 个文件）：

```bash
# 发布文字
/baoyu-post-to-weibo "Hello Weibo!"

# 发布带图片的帖子
/baoyu-post-to-weibo "Check this out" --image photo.png

# 发布带视频的帖子
/baoyu-post-to-weibo "Watch this" --video clip.mp4
```

**头条文章（头条文章）** - 长文 Markdown：

```bash
# 发布文章
/baoyu-post-to-weibo --article article.md

# 设置封面图
/baoyu-post-to-weibo --article article.md --cover cover.jpg
```

**文章选项**：
| 选项 | 描述 |
|--------|-------------|
| `--cover <path>` | 封面图片路径 |
| `--title <text>` | 覆盖标题（最多 32 字符） |
| `--summary <text>` | 覆盖摘要（最多 44 字符） |

**注意**：脚本会将内容填入浏览器。由你手动审核并发布。首次使用需手动微博登录（会话持久化）。

### AI 生成技能

AI 驱动的生成后端。

#### baoyu-image-gen

基于 OpenAI GPT Image 2、Azure OpenAI、Google、OpenRouter、DashScope（阿里云通义万相）、MiniMax、Jimeng（即梦）、Seedream（豆包）与 Replicate API 的 AI SDK 图像生成工具。支持文生图、参考图、宽高比、自定义尺寸、批量生成与质量预设。

```bash
# 基础生成（自动检测提供商）
/baoyu-image-gen --prompt "A cute cat" --image cat.png

# 设置宽高比
/baoyu-image-gen --prompt "A landscape" --image landscape.png --ar 16:9

# 高质量（2k）
/baoyu-image-gen --prompt "A banner" --image banner.png --quality 2k

# 指定提供商
/baoyu-image-gen --prompt "A cat" --image cat.png --provider openai --model gpt-image-2

# Azure OpenAI（模型 = 部署名称）
/baoyu-image-gen --prompt "A cat" --image cat.png --provider azure --model gpt-image-2

# OpenRouter
/baoyu-image-gen --prompt "A cat" --image cat.png --provider openrouter

# OpenRouter 带参考图
/baoyu-image-gen --prompt "Make it blue" --image out.png --provider openrouter --model google/gemini-3.1-flash-image --ref source.png

# DashScope（阿里云通义万相）
/baoyu-image-gen --prompt "一只可爱的猫" --image cat.png --provider dashscope

# DashScope 自定义尺寸
/baoyu-image-gen --prompt "为咖啡品牌设计一张 21:9 横幅海报，包含清晰中文标题" --image banner.png --provider dashscope --model qwen-image-2.0-pro --size 2048x872

# Z.AI GLM-Image
/baoyu-image-gen --prompt "一张带清晰中文标题的科技海报" --image out.png --provider zai

# MiniMax
/baoyu-image-gen --prompt "A fashion editorial portrait by a bright studio window" --image out.jpg --provider minimax

# MiniMax 带主体参考图
/baoyu-image-gen --prompt "A girl stands by the library window, cinematic lighting" --image out.jpg --provider minimax --model image-01 --ref portrait.png --ar 16:9

# Replicate（默认：google/nano-banana-2）
/baoyu-image-gen --prompt "A cat" --image cat.png --provider replicate

# Replicate Seedream 4.5
/baoyu-image-gen --prompt "A studio portrait" --image portrait.png --provider replicate --model bytedance/seedream-4.5 --ar 3:2

# Replicate Wan 2.7 Image Pro
/baoyu-image-gen --prompt "A concept frame" --image frame.png --provider replicate --model wan-video/wan-2.7-image-pro --size 2048x1152

# Jimeng（即梦）
/baoyu-image-gen --prompt "一只可爱的猫" --image cat.png --provider jimeng

# Seedream（豆包）
/baoyu-image-gen --prompt "一只可爱的猫" --image cat.png --provider seedream

# 带参考图（Google, OpenAI, Azure OpenAI, OpenRouter, Replicate, MiniMax, 或 Seedream 5.0/4.5/4.0）
/baoyu-image-gen --prompt "Make it blue" --image out.png --ref source.png

# 批量模式
/baoyu-image-gen --batchfile batch.json --jobs 4 --json
```

**选项**：
| 选项 | 描述 |
|--------|-------------|
| `--prompt`, `-p` | 提示词文本 |
| `--promptfiles` | 从文件读取提示词（拼接） |
| `--image` | 输出图像路径（必填） |
| `--batchfile` | JSON 批量文件，用于多图生成 |
| `--jobs` | 批量模式工作线程数 |
| `--provider` | `google`, `openai`, `azure`, `openrouter`, `dashscope`, `zai`, `minimax`, `jimeng`, `seedream`, 或 `replicate` |
| `--model`, `-m` | 模型 ID 或部署名称。Azure 使用部署名；OpenRouter 使用完整模型 ID；Z.AI 使用 `glm-image`；MiniMax 使用 `image-01` / `image-01-live` |
| `--ar` | 宽高比（如 `16:9`, `1:1`, `4:3`） |
| `--size` | 尺寸（如 `1024x1024`；`gpt-image-2` 支持有效自定义尺寸，最大边长 3840px） |
| `--quality` | `normal` 或 `2k`（默认：`2k`） |
| `--imageSize` | Google/OpenRouter 使用 `1K`, `2K`, 或 `4K` |
| `--imageApiDialect` | OpenAI 兼容网关使用 `openai-native` 或 `ratio-metadata` |
| `--ref` | 参考图像（支持 Google, OpenAI, Azure OpenAI, OpenRouter, Replicate 系列, MiniMax, 或 Seedream 5.0/4.5/4.0） |
| `--n` | 每次请求生成数量（`replicate` 当前需指定 `--n 1`） |
| `--json` | JSON 格式输出 |

**环境变量**（配置方法见 [环境配置](#environment-configuration)）：
| 变量 | 描述 | 默认值 |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI API 密钥 | - |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API 密钥 | - |
| `OPENROUTER_API_KEY` | OpenRouter API 密钥 | - |
| `GOOGLE_API_KEY` | Google API 密钥 | - |
| `GEMINI_API_KEY` | `GOOGLE_API_KEY` 别名 | - |
| `DASHSCOPE_API_KEY` | DashScope API 密钥（阿里云） | - |
| `ZAI_API_KEY` | Z.AI API 密钥 | - |
| `BIGMODEL_API_KEY` | Z.AI API 密钥向后兼容别名 | - |
| `MINIMAX_API_KEY` | MiniMax API 密钥 | - |
| `REPLICATE_API_TOKEN` | Replicate API Token | - |
| `JIMENG_ACCESS_KEY_ID` | Jimeng 火山引擎访问密钥 | - |
| `JIMENG_SECRET_ACCESS_KEY` | Jimeng 火山引擎秘密密钥 | - |
| `ARK_API_KEY` | Seedream 火山引擎 ARK API 密钥 | - |
| `OPENAI_IMAGE_MODEL` | OpenAI 模型 | `gpt-image-2` |
| `AZURE_OPENAI_DEPLOYMENT` | Azure 默认部署名称 | - |
| `AZURE_OPENAI_IMAGE_MODEL` | Azure 向后兼容别名（部署/模型） | `gpt-image-2` |
| `OPENROUTER_IMAGE_MODEL` | OpenRouter 模型 | `google/gemini-3.1-flash-image` |
| `GOOGLE_IMAGE_MODEL` | Google 模型 | `gemini-3-pro-image` |
| `DASHSCOPE_IMAGE_MODEL` | DashScope 模型 | `qwen-image-2.0-pro` |
| `ZAI_IMAGE_MODEL` | Z.AI 模型 | `glm-image` |
| `BIGMODEL_IMAGE_MODEL` | Z.AI 向后兼容别名 | `glm-image` |
| `MINIMAX_IMAGE_MODEL` | MiniMax 模型 | `image-01` |
| `REPLICATE_IMAGE_MODEL` | Replicate 模型 | `google/nano-banana-2` |
| `JIMENG_IMAGE_MODEL` | Jimeng 模型 | `jimeng_t2i_v40` |
| `SEEDREAM_IMAGE_MODEL` | Seedream 模型 | `doubao-seedream-5-0-260128` |
| `OPENAI_BASE_URL` | 自定义 OpenAI 端点 | - |
| `OPENAI_IMAGE_API_DIALECT` | OpenAI 兼容图像 API 方言（`openai-native` 或 `ratio-metadata`） | `openai-native` |
| `OPENAI_IMAGE_USE_CHAT` | 使用 `/chat/completions` 进行 OpenAI 图像生成 | `false` |
| `AZURE_OPENAI_BASE_URL` | Azure 资源或部署端点 | - |
| `AZURE_API_VERSION` | Azure 图像 API 版本 | `2025-04-01-preview` |
| `OPENROUTER_BASE_URL` | 自定义 OpenRouter 端点 | `https://openrouter.ai/api/v1` |
| `OPENROUTER_HTTP_REFERER` | OpenRouter 归属可选应用/站点 URL | - |
| `OPENROUTER_TITLE` | OpenRouter 归属可选应用名称 | - |
| `GOOGLE_BASE_URL` | 自定义 Google 端点 | - |
| `DASHSCOPE_BASE_URL` | 自定义 DashScope 端点 | - |
| `ZAI_BASE_URL` | 自定义 Z.AI 端点 | `https://api.z.ai/api/paas/v4` |
| `BIGMODEL_BASE_URL` | Z.AI 向后兼容别名端点 | - |
| `MINIMAX_BASE_URL` | 自定义 MiniMax 端点 | `https://api.minimaxi.com` |
| `REPLICATE_BASE_URL` | 自定义 Replicate 端点 | - |
| `JIMENG_BASE_URL` | 自定义 Jimeng 端点 | `https://visual.volcengineapi.com` |
| `JIMENG_REGION` | Jimeng 区域 | `cn-north-1` |
| `SEEDREAM_BASE_URL` | 自定义 Seedream 端点 | `https://ark.cn-beijing.volces.com/api/v3` |
| `BAOYU_IMAGE_GEN_MAX_WORKERS` | 覆盖批量工作线程上限 | `10` |
| `BAOYU_IMAGE_GEN_<PROVIDER>_CONCURRENCY` | 覆盖提供商并发数 | 按提供商而定 |
| `BAOYU_IMAGE_GEN_<PROVIDER>_START_INTERVAL_MS` | 覆盖提供商请求启动间隔 | 按提供商而定 |

**提供商说明**：
- Azure OpenAI：`--model` 指 Azure 部署名称，而非底层模型家族。
- DashScope：自定义 `--size`、`21:9` 及强中英文文字渲染推荐使用 `qwen-image-2.0-pro`。
- Z.AI：海报、图表与含大量中/英文的图像推荐使用 `glm-image`。不支持参考图。
- MiniMax：`image-01` 支持文档化的自定义 `width` / `height`；`image-01-live` 延迟更低，配合 `--ar` 使用效果最佳。
- MiniMax 参考图以 `subject_reference` 形式发送；当前 API 专为角色/肖像一致性优化。
- Jimeng 不支持参考图。
- Seedream 参考图仅支持 Seedream 5.0 / 4.5 / 4.0，不支持 3.0。
- Replicate 默认使用 `google/nano-banana-2`。`baoyu-image-gen` 仅在以下模型启用 Replicate 高级选项：`google/nano-banana*`, `bytedance/seedream-4.5`, `bytedance/seedream-5-lite`, `wan-video/wan-2.7-image`, `wan-video/wan-2.7-image-pro`。
- Replicate 当前每次请求仅保存一张输出图像。若指定 `--n > 1`，会在本地拦截而非静默丢弃多余结果。
- Replicate 模型行为因家族而异：nano-banana 使用 `--quality` / `--ar`；Seedream 使用已验证的 `--size` / `--ar`；Wan 使用已验证的 `--size`（`--ar` 会在本地转换为具体尺寸）。

**提供商自动选择逻辑**：
1. 若指定了 `--provider` → 使用该提供商
2. 若提供了 `--ref` 但未指定提供商 → 依次尝试 Google、OpenAI、Azure、OpenRouter、Replicate、Seedream，最后 MiniMax
3. 若仅有一个 API 密钥可用 → 使用该提供商
4. 若有多个提供商可用 → 默认优先顺序：Google, OpenAI, Azure, OpenRouter, DashScope, Z.AI, MiniMax, Replicate, Jimeng, Seedream

#### baoyu-danger-gemini-web

与 Gemini Web 交互以生成文本与图像。

**文本生成：**

```bash
/baoyu-danger-gemini-web "Hello, Gemini"
/baoyu-danger-gemini-web --prompt "Explain quantum computing"
```

**图像生成：**

```bash
/baoyu-danger-gemini-web --prompt "A cute cat" --image cat.png
/baoyu-danger-gemini-web --promptfiles system.md content.md --image out.png
```

### 实用工具技能

用于内容处理的实用工具。

#### baoyu-youtube-transcript

下载 YouTube 视频字幕/转录稿与封面图。支持多语言、翻译、章节标记与说话人识别。缓存原始数据以便快速重新格式化。

```bash
# 默认：带时间戳的 markdown
/baoyu-youtube-transcript https://www.youtube.com/watch?v=VIDEO_ID

# 指定语言（优先级顺序）
/baoyu-youtube-transcript https://youtu.be/VIDEO_ID --languages zh,en,ja

# 包含章节与说话人识别
/baoyu-youtube-transcript https://youtu.be/VIDEO_ID --chapters --speakers

# SRT 字幕格式
/baoyu-youtube-transcript https://youtu.be/VIDEO_ID --format srt

# 列出可用转录稿
/baoyu-youtube-transcript https://youtu.be/VIDEO_ID --list
```

**选项**：
| 选项 | 描述 | 默认值 |
|--------|-------------|---------|
| `<url-or-id>` | YouTube URL 或视频 ID | 必填 |
| `--languages <codes>` | 语言代码，逗号分隔 | `en` |
| `--format <fmt>` | 输出格式：`text`, `srt` | `text` |
| `--translate <code>` | 翻译至指定语言 | |
| `--chapters` | 从视频描述提取章节分割 | |
| `--speakers` | 说话人识别（需 AI 后处理） | |
| `--no-timestamps` | 禁用时间戳 | |
| `--list` | 列出可用转录稿 | |
| `--refresh` | 强制重新抓取，忽略缓存 | |

#### baoyu-url-to-markdown

通过 Chrome CDP 获取任意 URL 并转换为干净的 Markdown。保存渲染后的 HTML 快照与 markdown 文件并存，并在 Defuddle 失败时自动回退至传统提取器。

```bash
# 自动模式（默认）- 页面加载时捕获
/baoyu-url-to-markdown https://example.com/article

# 等待模式 - 适用于需登录的页面
/baoyu-url-to-markdown https://example.com/private --wait

# 保存至指定文件
/baoyu-url-to-markdown https://example.com/article -o output.md
```

**捕获模式**：
| 模式 | 描述 | 适用场景 |
|------|-------------|----------|
| 自动（默认） | 页面加载后立即捕获 | 公开页面、静态内容 |
| 等待 (`--wait`) | 等待用户信号后再捕获 | 需登录页、动态内容 |

**选项**：
| 选项 | 描述 |
|--------|-------------|
| `<url>` | 待抓取 URL |
| `-o <path>` | 输出文件路径 |
| `--wait` | 等待用户信号后再捕获 |
| `--timeout <ms>` | 页面加载超时时间（默认：30000） |

#### baoyu-danger-x-to-markdown

将 X（Twitter）内容转换为 Markdown 格式。支持推文线程与 X Articles。

```bash
# 转换推文为 markdown
/baoyu-danger-x-to-markdown https://x.com/username/status/123456

# 保存至指定文件
/baoyu-danger-x-to-markdown https://x.com/username/status/123456 -o output.md

# JSON 输出
/baoyu-danger-x-to-markdown https://x.com/username/status/123456 --json

# 下载媒体文件（图片/视频）至本地
/baoyu-danger-x-to-markdown https://x.com/username/status/123456 --download-media
```

**支持的 URL：**
- `https://x.com/<user>/status/<id>`
- `https://twitter.com/<user>/status/<id>`
- `https://x.com/i/article/<id>`

**认证方式**：使用环境变量（`X_AUTH_TOKEN`, `X_CT0`）或 Chrome 登录进行 Cookie 认证。

#### baoyu-compress-image

压缩图像以减小文件大小，同时保持画质。

```bash
/baoyu-compress-image path/to/image.png
/baoyu-compress-image path/to/images/ --quality 80
```

#### baoyu-format-markdown

格式化纯文本或 Markdown 文件，自动添加 Frontmatter、标题、摘要、标题层级、加粗、列表与代码块。

```bash
# 格式化 markdown 文件
/baoyu-format-markdown path/to/article.md

# 指定输出格式
/baoyu-format-markdown path/to/draft.md
```

**工作流**：
1. 读取源文件并分析内容结构
2. 检查/创建 YAML Frontmatter（title, slug, summary, coverImage）
3. 处理标题：使用现有、从 H1 提取或生成候选
4. 应用排版：标题层级、加粗、列表、代码块、引用
5. 保存至 `{filename}-formatted.md`
6. 运行排版脚本：ASCII→全角引号、CJK 间距调整、自动纠错

**Frontmatter 字段**：
| 字段 | 处理方式 |
|-------|------------|
| `title` | 使用现有值、提取 H1，或生成候选标题 |
| `slug` | 从文件路径推断或根据标题生成 |
| `summary` | 生成吸引人的摘要（100-150 字符） |
| `coverImage` | 检查同目录下是否存在 `imgs/cover.png` |

**排版规则**：
| 元素 | 格式 |
|---------|-------------|
| 标题 | `#`, `##`, `###` 层级结构 |
| 重点内容 | `**加粗**` |
| 并列项 | `-` 无序列表或 `1.` 有序列表 |
| 代码/命令 | `` `行内` `` 或 ` ```块``` ` |
| 引用 | `>` 区块引用 |

#### baoyu-markdown-to-html

将 Markdown 文件转换为带样式的 HTML，支持微信兼容主题、语法高亮与可选的外部链接底部引用。

```bash
# 基础转换
/baoyu-markdown-to-html article.md

# 主题+颜色
/baoyu-markdown-to-html article.md --theme grace --color red

# 将普通外部链接转换为底部引用
/baoyu-markdown-to-html article.md --cite
```

#### baoyu-translate

在语言间翻译文章与文档，提供三种模式：快速（直接翻译）、标准（分析后翻译）与精校（完整出版级工作流含审核与润色）。

```bash
# 标准模式（默认）- 先分析再翻译
/translate article.md --to zh-CN

# 快速模式 - 直接翻译
/translate article.md --mode quick --to ja

# 精校模式 - 完整工作流含审核与润色
/translate article.md --mode refined --to zh-CN

# 翻译 URL
/translate https://example.com/article --to zh-CN

# 指定目标受众
/translate article.md --to zh-CN --audience technical

# 指定风格
/translate article.md --to zh-CN --style humorous

# 附加术语表
/translate article.md --to zh-CN --glossary my-terms.md
```

**选项**：
| 选项 | 描述 |
|--------|-------------|
| `<source>` | 文件路径、URL 或内联文本 |
| `--mode <mode>` | `quick`, `normal`（默认）, `refined` |
| `--from <lang>` | 源语言（省略则自动检测） |
| `--to <lang>` | 目标语言（默认：`zh-CN`） |
| `--audience <type>` | 目标读者画像（默认：`general`） |
| `--style <style>` | 翻译风格（默认：`storytelling`） |
| `--glossary <file>` | 附加术语表文件 |

**模式说明**：
| 模式 | 步骤 | 适用场景 |
|------|-------|----------|
| 快速 | 直接翻译 | 短文本、非正式内容 |
| 标准 | 分析 → 翻译 | 文章、博客帖子 |
| 精校 | 分析 → 翻译 → 审核 → 润色 | 出版级文档 |

完成标准模式后，你可回复“继续润色”或“refine”以继续审核与润色步骤。

**受众预设**：
| 值 | 描述 |
|-------|-------------|
| `general` | 普通读者（默认）— 通俗语言、较多译者注 |
| `technical` | 开发者/工程师 — 常见技术术语少注解 |
| `academic` | 研究者/学者 — 正式语体、精确术语 |
| `business` | 商务人士 — 商业友好语气 |

也支持自定义受众描述，例如 `--audience "对 AI 感兴趣的普通读者"`。

**风格预设**：
| 值 | 描述 |
|-------|-------------|
| `storytelling` | 引人入胜的叙事流（默认）— 过渡流畅、措辞生动 |
| `formal` | 专业、结构化 — 中立语气，无口语化表达 |
| `technical` | 精准、文档风格 — 简洁、术语密集 |
| `literal` | 贴近原文结构 — 最小化结构调整 |
| `academic` | 学术严谨 — 正式语体，允许复杂从句 |
| `business` | 简洁、结果导向 — 行动导向、高管友好 |
| `humorous` | 保留并适配幽默 — 机智风趣、重现喜剧效果 |
| `conversational` | 随意、口语化 — 亲切自然，如向朋友解释 |
| `elegant` | 文学性、打磨过的散文 — 审美精致、精心雕琢 |

也支持自定义风格描述，例如 `--style "诗意且抒情"`。

**功能特性**：
- 通过 EXTEND.md 使用自定义术语表（内置 EN→ZH 术语表）
- 受众感知翻译，可调节注释深度
- 长文档自动分块（4000+ 词），配合并行子代理翻译
- 修辞语言按语义而非逐字翻译
- 文化/领域特定参考提供译者注
- 输出目录保留所有中间文件

#### baoyu-wechat-summary

将微信群聊亮点总结为结构化摘要。使用 [wx-cli](https://github.com/jackwener/wx-cli) 从群消息中提取主题、引用与统计数据。跨运行保持按群历史与按用户画像记录。支持普通版与毒舌版，并回答聊天中 `@bot` 提出的问题。

```bash
# 总结某群最近消息
/baoyu-wechat-summary 相亲相爱一家人 最近 1 天

# 每周摘要
/baoyu-wechat-summary AI 技术群 最近 7 天

# 增量模式（自上次摘要以来）
/baoyu-wechat-summary 相亲相爱一家人

# 毒舌版
/baoyu-wechat-summary 相亲相爱一家人 最近 3 天 毒舌版
```

**环境要求**：
- 已安装 [wx-cli](https://github.com/jackwener/wx-cli)（`npm install -g @jackwener/wx-cli`）
- macOS 上运行并登录微信 4.x

**功能特性**：
- 带归属与引用的主题提取
- 消息排行榜与按用户画像
- 增量模式（接续上次摘要断点）
- 大批量支持多日范围分割
- 普通版与毒舌版摘要
- 从历史摘要回填用户画像

#### baoyu-electron-extract

从任意已安装 Electron 应用的 `app.asar` 中提取资源与 JavaScript。当 `.js.map` 文件嵌入 `sourcesContent` 时，还原原始源码树（含 TypeScript/JSX）；否则使用 Prettier 原地格式化压缩后的 JS/CSS。始终跳过 `node_modules`。支持 macOS 与 Windows；其他平台需传递 `--asar <path>`。

```bash
# 按应用名提取（默认输出：~/Downloads/Codex-electron-extract/）
/baoyu-electron-extract Codex

# 按绝对路径提取（.app bundle、安装目录或 .asar 文件）
/baoyu-electron-extract "/Applications/Visual Studio Code.app"
/baoyu-electron-extract --asar /Applications/Codex.app/Contents/Resources/app.asar Codex

# 自定义输出目录
/baoyu-electron-extract Codex --output ~/work/codex-source

# 仅预览发现结果，不写入任何内容
/baoyu-electron-extract Codex --dry-run

# 覆盖已存在的输出目录
/baoyu-electron-extract Codex --force
```

**选项**：
| 选项 | 描述 | 默认值 |
|--------|-------------|---------|
| `<app>` | 应用名称或绝对路径（除非 `--asar`） | — |
| `--output`, `-o` | 输出目录 | `~/Downloads/<AppName>-electron-extract` |
| `--asar` | 覆盖解析的 `.asar` 路径 | auto-discovered |
| `--force`, `-f` | 允许写入非空的现有输出目录 | false |
| `--skip-format` | 跳过 Prettier 格式化 | false |
| `--skip-restore` | 跳过 source-map 还原 | false |
| `--no-unpacked` | 不复制 `app.asar.unpacked/` 旁路文件 | false |
| `--dry-run` | 打印解析路径并退出，不写入 | false |
| `--json` | 在 stdout 输出一行 JSON 摘要 | false |

**输出布局**：`extract-report.json`（统计、警告、路径）、`extracted/`（原始 asar，无 map 时原地格式化）、`extracted.unpacked/`（原生模块，若存在）与 `restored/`（从 `.js.map` 文件重建的源码树）。

## 环境配置

部分技能需要 API 密钥或自定义配置。环境变量可设置在 `.env` 文件中：

**加载优先级**（高优先级覆盖低优先级）：
1. CLI 环境变量（例如 `OPENAI_API_KEY=xxx /baoyu-image-gen ...`）
2. `process.env`（系统环境）
3. `<cwd>/.baoyu-skills/.env`（项目级）
4. `~/.baoyu-skills/.env`（用户级）

**配置步骤**：

```bash
# 创建用户级配置目录
mkdir -p ~/.baoyu-skills

# 创建 .env 文件
cat > ~/.baoyu-skills/.env << 'EOF'
# OpenAI
OPENAI_API_KEY=sk-xxx
OPENAI_IMAGE_MODEL=gpt-image-2
# OPENAI_BASE_URL=https://api.openai.com/v1
# OPENAI_IMAGE_USE_CHAT=false

# Azure OpenAI
AZURE_OPENAI_API_KEY=xxx
AZURE_OPENAI_BASE_URL=https://your-resource.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-image-2
# AZURE_API_VERSION=2025-04-01-preview

# OpenRouter
OPENROUTER_API_KEY=sk-or-xxx
OPENROUTER_IMAGE_MODEL=google/gemini-3.1-flash-image
# OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
# OPENROUTER_HTTP_REFERER=https://your-app.example.com
# OPENROUTER_TITLE=Your App Name

# Google
GOOGLE_API_KEY=xxx
GOOGLE_IMAGE_MODEL=gemini-3-pro-image
# GOOGLE_BASE_URL=https://generativelanguage.googleapis.com/v1beta

# DashScope（阿里云通义万相）
DASHSCOPE_API_KEY=sk-xxx
DASHSCOPE_IMAGE_MODEL=qwen-image-2.0-pro
# DASHSCOPE_BASE_URL=https://dashscope.aliyuncs.com/api/v1

# Z.AI
ZAI_API_KEY=xxx
ZAI_IMAGE_MODEL=glm-image
# ZAI_BASE_URL=https://api.z.ai/api/paas/v4

# MiniMax
MINIMAX_API_KEY=xxx
MINIMAX_IMAGE_MODEL=image-01
# MINIMAX_BASE_URL=https://api.minimaxi.com

# Replicate
REPLICATE_API_TOKEN=r8_xxx
REPLICATE_IMAGE_MODEL=google/nano-banana-2
# REPLICATE_BASE_URL=https://api.replicate.com

# Jimeng（即梦）
JIMENG_ACCESS_KEY_ID=xxx
JIMENG_SECRET_ACCESS_KEY=xxx
JIMENG_IMAGE_MODEL=jimeng_t2i_v40
# JIMENG_BASE_URL=https://visual.volcengineapi.com
# JIMENG_REGION=cn-north-1

# Seedream（豆包）
ARK_API_KEY=xxx
SEEDREAM_IMAGE_MODEL=doubao-seedream-5-0-260128
# SEEDREAM_BASE_URL=https://ark.cn-beijing.volces.com/api/v3
EOF
```

**项目级配置**（用于团队共享）：

```bash
mkdir -p .baoyu-skills
# 将 .baoyu-skills/.env 加入 .gitignore 避免提交密钥
echo ".baoyu-skills/.env" >> .gitignore
```

## 自定义

所有技能均支持通过 `EXTEND.md` 文件进行自定义。创建扩展文件以覆盖默认风格、添加自定义配置或定义专属预设。

**扩展路径检查顺序**（按优先级）：
1. `.baoyu-skills/<skill-name>/EXTEND.md` - 项目级（适用于团队/项目特定设置）
2. `~/.baoyu-skills/<skill-name>/EXTEND.md` - 用户级（适用于个人偏好）

**示例**：为 `baoyu-cover-image` 自定义品牌配色：

```bash
mkdir -p .baoyu-skills/baoyu-cover-image
```

然后创建 `.baoyu-skills/baoyu-cover-image/EXTEND.md`：

```markdown
## Custom Palettes

### corporate-tech
- Primary colors: #1a73e8, #4A90D9
- Background: #F5F7FA
- Accent colors: #00B4D8, #48CAE4
- Decorative hints: Clean lines, subtle gradients
- Best for: SaaS, enterprise, technical
```

扩展内容将在技能执行前加载，并覆盖默认配置。

## 免责声明

### baoyu-danger-gemini-web

本技能使用 Gemini Web API（逆向工程）。

**警告**：本项目通过浏览器 Cookie 访问非官方 API。请自行承担风险。

- 首次运行会打开浏览器进行 Google 认证
- Cookie 会被缓存以供后续运行使用
- 不保证 API 稳定性或可用性

**支持的浏览器**（自动检测）：Google Chrome, Chrome Canary/Beta, Chromium, Microsoft Edge

**代理配置**：若需通过代理访问 Google 服务（例如在中国大陆），可内联设置环境变量：

```bash
HTTP_PROXY=http://127.0.0.1:7890 HTTPS_PROXY=http://127.0.0.1:7890 /baoyu-danger-gemini-web "Hello"
```

### baoyu-danger-x-to-markdown

本技能使用逆向工程的 X（Twitter）API。

**警告**：这不是官方 API。请自行承担风险。

- 若 X 更改 API，可能随时失效且无通知
- 若检测到 API 使用情况，可能导致账号限制
- 首次使用需确认知情同意
- 认证通过环境变量或 Chrome 登录实现

## 致谢

本项目受以下开源项目启发并基于其构建：

- [x-article-publisher-skill](https://github.com/wshuyi/x-article-publisher-skill) by [@wshuyi](https://github.com/wshuyi) — X 文章发布技能的灵感来源
- [doocs/md](https://github.com/doocs/md) by [@doocs](https://github.com/doocs) — Markdown 转 HTML 的核心实现逻辑
- [High-density Infographic Prompt](https://waytoagi.feishu.cn/wiki/YG0zwalijihRREkgmPzcWRInnUg) by AJ@WaytoAGI — 信息图技能的灵感来源
- [qiaomu-mondo-poster-design](https://github.com/joeseesun/qiaomu-mondo-poster-design) by [@joeseesun](https://github.com/joeseesun)（乔木）— Mondo 风格的灵感来源
- [architecture-diagram-generator](https://github.com/Cocoon-AI/architecture-diagram-generator) by [@Cocoon-AI](https://github.com/Cocoon-AI) — 图表技能设计系统的灵感来源

## License

MIT

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=JimLiu/baoyu-skills&type=Date)](https://www.star-history.com/#JimLiu/baoyu-skills&Date)