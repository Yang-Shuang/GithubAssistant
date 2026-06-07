# Frontend Slides

一个用于创建惊艳的 HTML 演示文稿的代码代理（coding agent）技能——支持从零开始制作，或转换 PowerPoint 文件。它被打包为 Claude Code 插件，核心 `SKILL.md` 也可供其他具备文件系统与 Shell 访问权限的代码代理读取。

## 功能说明

**Frontend Slides** 帮助非设计师在无需掌握 CSS 或 JavaScript 的情况下制作精美的网页演示文稿。它采用“展示而非告知”（show, don't tell）的方式：不要求你用文字描述审美偏好，而是生成视觉预览供你挑选心仪的风格。

以下是通过该技能制作的关于此技能的演示文稿示例：

https://github.com/user-attachments/assets/ef57333e-f879-432a-afb9-180388982478

### 核心特性

- **零依赖** —— 单个 HTML 文件内嵌 CSS/JS。无需 npm、构建工具或框架。
- **视觉风格探索** —— 无法准确描述设计偏好？没问题。从生成的视觉预览中挑选即可。
- **PPT 转换** —— 将现有的 PowerPoint 文件转换为网页格式，保留所有图片与内容。
- **拒绝 AI 廉价感（Anti-AI-Slop）** —— 精选独特风格，避免千篇一律的通用 AI 审美（告别白底紫渐变）。
- **Bold 模板包** —— 来自 `beautiful-html-templates` 的可选设计导向型模板，采用渐进式加载机制，确保安全预设仍可作为默认回退选项。
- **生产级质量** —— 符合无障碍标准、固定 16:9 比例、注释完善的代码，支持你自由定制。

## 安装方式

### 通过 Claude Code 自定义市场源安装

直接从该公开 GitHub 仓库进行安装。请将以下两行命令作为两条独立的 Claude Code 消息分别发送，切勿一次性粘贴到提示词中。

```text
/plugin marketplace add https://github.com/zarazhangrui/frontend-slides
```

完成后，运行：

```text
/plugin install frontend-slides@frontend-slides
```

请使用 HTTPS 链接。较短的 `zarazhangrui/frontend-slides` 格式可能导致 Claude Code 尝试使用 SSH，若你的 `known_hosts` 文件中尚未包含 GitHub，则可能会失败。

随后在 Claude Code 中通过输入 `/frontend-slides:frontend-slides` 即可使用。Claude Code 会将插件安装的技能命名空间化为 `/插件名:技能名`。

### Claude Code 手动安装

将技能文件复制到你的 Claude Code 技能目录：

```bash
# Create the skill directory
mkdir -p ~/.claude/skills/frontend-slides/scripts

# Copy the user-facing skill files
cp SKILL.md STYLE_PRESETS.md viewport-base.css html-template.md animation-patterns.md ~/.claude/skills/frontend-slides/
cp -R bold-template-pack ~/.claude/skills/frontend-slides/
cp scripts/extract-pptx.py scripts/deploy.sh scripts/export-pdf.sh ~/.claude/skills/frontend-slides/scripts/
```

或直接克隆仓库：

```bash
git clone https://github.com/zarazhangrui/frontend-slides.git ~/.claude/skills/frontend-slides
```

随后在 Claude Code 中通过输入 `/frontend-slides` 即可使用。独立技能不会进行命名空间处理。

### 其他代码代理

Codex、Kimi Code、OpenCode、Gemini CLI 或其他本地代码代理均可使用相同的底层技能。最简单的用法是将此 GitHub 仓库链接发送给代理，并指示它调用 Frontend Slides 技能：

```text
https://github.com/zarazhangrui/frontend-slides
```

若代理支持读取 GitHub 仓库或浏览文件，应从 `SKILL.md` 开始，按需加载其引用的支撑文件：

- `STYLE_PRESETS.md`
- `viewport-base.css`
- `html-template.md`
- `animation-patterns.md`
- `bold-template-pack/`
- `scripts/`

部分代理若具备文件系统访问权限且知晓本地技能目录，也可代为安装该技能。若不满足此条件，代理仍可直接遵循 `SKILL.md` 在当前会话中运行。

Claude Code 插件提供了自定义市场源安装流程及 `/frontend-slides:frontend-slides` 命令。其他代理通常不使用该命令交互界面。

## 使用方法

### 创建新演示文稿

```text
/frontend-slides:frontend-slides

> "I want to create a pitch deck for my AI startup"
```

若以独立技能方式手动安装，请改用 `/frontend-slides`。

在非 Claude Code 代理中，指示代理调用 Frontend Slides 技能并指向本仓库或 `SKILL.md`。

该技能将执行以下流程：

1. 询问你的内容需求（幻灯片结构、文案、图片）
2. 生成 3 款视觉风格预览供你对比，根据你的描述推断氛围（若已指定具体风格则跳过此步）
3. 由你选择最终视觉方向
4. 按选定风格生成完整演示文稿
5. 在浏览器中打开预览

### 转换 PowerPoint 文件

```text
/frontend-slides:frontend-slides

> "Convert my presentation.pptx to a web slideshow"
```

该技能将执行以下流程：

1. 提取 PPT 中的所有文本、图片与备注
2. 展示提取内容供你确认
3. 由你选择视觉风格
4. 生成包含全部原始素材的 HTML 演示文稿

## 内置风格

### 深色主题

- **Bold Signal（醒目信号）** —— 自信、高冲击力，暗色背景上的活力卡片设计
- **Electric Studio（电光工作室）** —— 干净利落、专业商务，分栏面板布局
- **Creative Voltage（创意电压）** —— 充满活力、复古现代风，电光蓝搭配霓虹色
- **Dark Botanical（暗调植物）** —— 优雅精致，点缀暖色调

### 浅色主题

- **Notebook Tabs（笔记本标签）** —— 编辑排版风格，井井有条，彩色标签页设计
- **Pastel Geometry（柔和几何）** —— 亲切友好，垂直胶囊元素布局
- **Split Pastel（双色分割）** —— 活泼现代，双色调垂直分割设计
- **Vintage Editorial（复古编辑风）** —— 风趣个性，几何图形主导

### 特色风格

- **Neon Cyber（霓虹赛博）** —— 未来感，粒子背景与霓虹光晕
- **Terminal Green（终端绿）** —— 面向开发者，黑客美学风格
- **Swiss Modern（瑞士现代风）** —— 极简主义，包豪斯灵感，几何构成
- **Paper & Ink（纸墨书香）** —— 文学气息，首字下沉与引用块设计

### Bold 模板包

该技能还内置了来自 `beautiful-html-templates` 的 34 款可选 Bold 设计系统，例如 **Neo-Grid Bold**、**Editorial Tri-Tone**、**Creative Mode**、**Broadside**、**Signal** 与 **Vellum**。

在风格探索阶段，预览集包含：
- 来自 `STYLE_PRESETS.md` 的 1 款安全预设
- 至少 1 款来自 `bold-template-pack/selection-index.json` 的 Bold 模板选项
- 1 款通配符选项，可为其他 Bold 模板或代理自生成的自定义设计

代理会优先读取紧凑的 Bold 模板索引，随后仅加载入围候选项的小型 `preview.md` 卡片用于标题页预览。仅在用户选定某款 Bold 模板作为最终演示文稿时，才会加载该模板完整的 `design.md` 设计系统。若用户选择自定义通配符，代理将把该预览自带的 CSS 与布局体系扩展至完整演示文稿中。

## Bold 模板画廊

Frontend Slides 现已支持调用 [`beautiful-html-templates`](https://github.com/zarazhangrui/beautiful-html-templates) 中的 34 款 Bold 设计系统。每个模板展示三张截图，呈现各视觉体系对不同幻灯片布局的适配效果。点击任意模板名称即可查看源模板库。

### [Soft Editorial（柔和编辑风）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/soft-editorial/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/soft-editorial-4.png" width="32.5%" alt="Soft Editorial — slide 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/soft-editorial-6.png" width="32.5%" alt="Soft Editorial — slide 6" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/soft-editorial-10.png" width="32.5%" alt="Soft Editorial — slide 10" />
</p>

> 暖色纸张搭配 Cormorant Garamond 衬线体，点缀鼠尾草绿、柔粉与柠檬黄。

### [Editorial Forest（编辑森林）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/editorial-forest/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/editorial-forest-1.png" width="32.5%" alt="Editorial Forest — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/editorial-forest-2.png" width="32.5%" alt="Editorial Forest — slide 2" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/editorial-forest-5.png" width="32.5%" alt="Editorial Forest — slide 5" />
</p>

> Source Serif 4 字体搭配森林绿、灰粉色与暖奶油色——静谧而富有巧思的季度汇报美学。

### [Pin & Paper（图钉与纸）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/pin-and-paper/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/pin-and-paper-1.png" width="32.5%" alt="Pin & Paper — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/pin-and-paper-11.png" width="32.5%" alt="Pin & Paper — slide 11" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/pin-and-paper-3.png" width="32.5%" alt="Pin & Paper — slide 3" />
</p>

> 黄色纸张搭配安全别针插画，墨蓝色手写体 Caveat 字体，以及纸质纹理。

### [Sakura Chroma（樱花色谱）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/sakura-chroma/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/sakura-chroma-1.png" width="32.5%" alt="Sakura Chroma — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/sakura-chroma-3.png" width="32.5%" alt="Sakura Chroma — slide 3" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/sakura-chroma-4.png" width="32.5%" alt="Sakura Chroma — slide 4" />
</p>

> 复古日本磁带包装美学：奶油色纸张、对角彩虹丝带、紧凑粗体字与 JIS 标准规格复选框。

### [Stencil & Tablet（模板与石板）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/stencil-tablet/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/stencil-tablet-1.png" width="32.5%" alt="Stencil & Tablet — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/stencil-tablet-3.png" width="32.5%" alt="Stencil & Tablet — slide 3" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/stencil-tablet-8.png" width="32.5%" alt="Stencil & Tablet — slide 8" />
</p>

> 骨色纸张搭配镂空切割标题，六色调大地色系：考古风与现代品牌设计的碰撞。

### [Cobalt Grid（钴蓝网格）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/cobalt-grid/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/cobalt-grid-1.png" width="32.5%" alt="Cobalt Grid — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/cobalt-grid-3.png" width="32.5%" alt="Cobalt Grid — slide 3" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/cobalt-grid-5.png" width="32.5%" alt="Cobalt Grid — slide 5" />
</p>

> 坐标纸画布上的电光钴蓝斜体衬线字，以阶梯状像素故障装饰与极细水平线为基底。

### [Vellum（羊皮卷）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/vellum/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/vellum-1.png" width="32.5%" alt="Vellum — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/vellum-4.png" width="32.5%" alt="Vellum — slide 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/vellum-8.png" width="32.5%" alt="Vellum — slide 8" />
</p>

> 深海军蓝画布搭配暖黄色斜体 Cormorant 衬线字，点缀一抹灰青色。静谧而富有学术气息。

### [Emerald Editorial（翡翠编辑风）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/emerald-editorial/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/emerald-editorial-1.png" width="32.5%" alt="Emerald Editorial — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/emerald-editorial-3.png" width="32.5%" alt="Emerald Editorial — slide 3" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/emerald-editorial-6.png" width="32.5%" alt="Emerald Editorial — slide 6" />
</p>

> 杂志封面商务演示文稿：翡翠绿+海军蓝+纸张配色，搭配双线刊头装饰与粗重的 Bodoni 风格展示衬线体。

### [Neo-Grid Bold（新网格醒目版）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/neo-grid-bold/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/neo-grid-bold-1.png" width="32.5%" alt="Neo-Grid Bold — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/neo-grid-bold-3.png" width="32.5%" alt="Neo-Grid Bold — slide 3" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/neo-grid-bold-8.png" width="32.5%" alt="Neo-Grid Bold — slide 8" />
</p>

> 编辑风新粗野主义，米白纸张上点缀一抹霓虹黄。

### [Editorial Tri-Tone（编辑三色）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/editorial-tri-tone/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/editorial-tri-tone-1.png" width="32.5%" alt="Editorial Tri-Tone — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/editorial-tri-tone-4.png" width="32.5%" alt="Editorial Tri-Tone — slide 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/editorial-tri-tone-3.png" width="32.5%" alt="Editorial Tri-Tone — slide 3" />
</p>

> 三色编辑系统：灰粉、芥末奶油色与深酒红色，搭配 Bricolage 与 Instrument Serif 字体。

### [Creative Mode（创意模式）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/creative-mode/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/creative-mode-1.png" width="32.5%" alt="Creative Mode — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/creative-mode-4.png" width="32.5%" alt="Creative Mode — slide 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/creative-mode-6.png" width="32.5%" alt="Creative Mode — slide 6" />
</p>

> 奶油色画布搭配自信的多色点缀（绿、粉、橙、黄），以及 Archivo Black 展示字体。

### [Monochrome（单色）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/monochrome/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/monochrome-1.png" width="32.5%" alt="Monochrome — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/monochrome-4.png" width="32.5%" alt="Monochrome — slide 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/monochrome-12.png" width="32.5%" alt="Monochrome — slide 12" />
</p>

> 象牙色账本纸搭配全黑文字；Lora 衬线体标题，Jost 正文，完全不使用色彩。

### [People's Platform (Block & Bold)（人民平台）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/peoples-platform/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/peoples-platform-1.png" width="32.5%" alt="People's Platform (Block & Bold) — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/peoples-platform-4.png" width="32.5%" alt="People's Platform (Block & Bold) — slide 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/peoples-platform-8.png" width="32.5%" alt="People's Platform (Block & Bold) — slide 8" />
</p>

> 行动派海报能量：奶油底色上的蓝、橙、红三色，搭配 Alfa Slab 与 Caveat Brush 字体。

### [Pink Script — After Hours（粉色手稿——深夜场）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/pink-script/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/pink-script-1.png" width="32.5%" alt="Pink Script — After Hours — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/pink-script-4.png" width="32.5%" alt="Pink Script — After Hours — slide 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/pink-script-8.png" width="32.5%" alt="Pink Script — After Hours — slide 8" />
</p>

> 黑色画布、亮粉点缀、珍珠奶油色纸张与 Instrument Serif 标题：午夜编辑风的奢华质感。

### [8-Bit Orbit（8位轨道）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/8-bit-orbit/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/8-bit-orbit-1.png" width="32.5%" alt="8-Bit Orbit — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/8-bit-orbit-6.png" width="32.5%" alt="8-Bit Orbit — slide 6" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/8-bit-orbit-5.png" width="32.5%" alt="8-Bit Orbit — slide 5" />
</p>

> 深邃海军蓝背景上的像素风霓虹街机美学。

### [BlockFrame（块框架）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/block-frame/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/block-frame-1.png" width="32.5%" alt="BlockFrame — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/block-frame-4.png" width="32.5%" alt="BlockFrame — slide 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/block-frame-8.png" width="32.5%" alt="BlockFrame — slide 8" />
</p>

> 新粗野主义演示文稿，柔和霓虹色块搭配粗黑边框。

### [Blue Professional（蓝色商务）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/blue-professional/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/blue-professional-1.png" width="32.5%" alt="Blue Professional — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/blue-professional-6.png" width="32.5%" alt="Blue Professional — slide 6" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/blue-professional-8.png" width="32.5%" alt="Blue Professional — slide 8" />
</p>

> 奶油纸背景搭配电光钴蓝点缀；干净现代的商务风格。

### [Bold Poster（醒目海报）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/bold-poster/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/bold-poster-1.png" width="32.5%" alt="Bold Poster — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/bold-poster-4.png" width="32.5%" alt="Bold Poster — slide 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/bold-poster-8.png" width="32.5%" alt="Bold Poster — slide 8" />
</p>

> 编辑风海报美学，超大号 Shrikhand 展示字体搭配一抹消防红点缀。

### [Broadside（宽幅报）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/broadside/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/broadside-1.png" width="32.5%" alt="Broadside — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/broadside-4.png" width="32.5%" alt="Broadside — slide 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/broadside-13.png" width="32.5%" alt="Broadside — slide 13" />
</p>

> 深色编辑画布搭配一抹火焰橙，以及拉丁语/中文双语排版堆叠。

### [Capsule（胶囊）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/capsule/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/capsule-1.png" width="32.5%" alt="Capsule — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/capsule-4.png" width="32.5%" alt="Capsule — slide 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/capsule-8.png" width="32.5%" alt="Capsule — slide 8" />
</p>

> 暖骨色背景上的模块化胶囊卡片，完整柔和流行色系。

### [Cartesian（笛卡尔）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/cartesian/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/cartesian-1.png" width="32.5%" alt="Cartesian — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/cartesian-4.png" width="32.5%" alt="Cartesian — slide 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/cartesian-8.png" width="32.5%" alt="Cartesian — slide 8" />
</p>

> 静谧的暖中性色调搭配经典 Playfair 衬线体；优雅从容。

### [Coral（珊瑚）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/coral/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/coral-1.png" width="32.5%" alt="Coral — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/coral-4.png" width="32.5%" alt="Coral — slide 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/coral-8.png" width="32.5%" alt="Coral — slide 8" />
</p>

> 近黑底色上的奶油色与珊瑚色，搭配超大号 Bebas Neue 字体。

### [Daisy Days（雏菊日）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/daisy-days/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/daisy-days-1.png" width="32.5%" alt="Daisy Days — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/daisy-days-4.png" width="32.5%" alt="Daisy Days — slide 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/daisy-days-8.png" width="32.5%" alt="Daisy Days — slide 8" />
</p>

> 欢快的柔和色系演示文稿，手绘雏菊、星星与彩虹。亲切、柔软且温暖。

### [Grove（林荫）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/grove/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/grove-1.png" width="32.5%" alt="Grove — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/grove-4.png" width="32.5%" alt="Grove — slide 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/grove-8.png" width="32.5%" alt="Grove — slide 8" />
</p>

> 森林绿画布搭配奶油色文字、经典 Playfair 衬线体，以及一抹铁锈红点缀。

### [Mat（垫板）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/mat/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/mat-1.png" width="32.5%" alt="Mat — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/mat-4.png" width="32.5%" alt="Mat — slide 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/mat-8.png" width="32.5%" alt="Mat — slide 8" />
</p>

> 深鼠尾草绿画布搭配骨色纸张与焦橙色点缀；带有木质底色的中世纪现代风格。

### [Playful（俏皮）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/playful/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/playful-1.png" width="32.5%" alt="Playful — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/playful-6.png" width="32.5%" alt="Playful — slide 6" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/playful-8.png" width="32.5%" alt="Playful — slide 8" />
</p>

> 阳光暖桃背景搭配 Syne 展示字体：亲切的独立品牌发布演示文稿。

### [Raw Grid（原始网格）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/raw-grid/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/raw-grid-1.png" width="32.5%" alt="Raw Grid — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/raw-grid-4.png" width="32.5%" alt="Raw Grid — slide 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/raw-grid-8.png" width="32.5%" alt="Raw Grid — slide 8" />
</p>

> 新粗野主义演示文稿，厚边框、错位阴影与粉/鼠尾草绿/墨色配色。

### [Retro Windows（复古 Windows）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/retro-windows/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/retro-windows-1.png" width="32.5%" alt="Retro Windows — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/retro-windows-4.png" width="32.5%" alt="Retro Windows — slide 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/retro-windows-8.png" width="32.5%" alt="Retro Windows — slide 8" />
</p>

> Windows 95 界面风格：灰色标题栏、MS Sans Serif 字体、像素排版，满满怀旧感。

### [Retro Zine（复古独立志）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/retro-zine/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/retro-zine-1.png" width="32.5%" alt="Retro Zine — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/retro-zine-4.png" width="32.5%" alt="Retro Zine — slide 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/retro-zine-8.png" width="32.5%" alt="Retro Zine — slide 8" />
</p>

> 米色纸张搭配绿色点缀与 Bebas Neue + Caveat 字体：以 HTML 形式呈现的 Risograph 印刷风独立杂志。

### [Scatterbrain（思绪漫游）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/scatterbrain/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/scatterbrain-1.png" width="32.5%" alt="Scatterbrain — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/scatterbrain-4.png" width="32.5%" alt="Scatterbrain — slide 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/scatterbrain-8.png" width="32.5%" alt="Scatterbrain — slide 8" />
</p>

> 灵感源自便利贴：柔和便签纸、Caveat 手写体，以及 Shrikhand 与 Zilla Slab 字体堆叠。

### [Signal（信号）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/signal/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/signal-1.png" width="32.5%" alt="Signal — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/signal-18.png" width="32.5%" alt="Signal — slide 18" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/signal-8.png" width="32.5%" alt="Signal — slide 8" />
</p>

> 深海军蓝画布搭配骨色纸张与一抹暗金点缀；庄重而富有机构感。

### [Studio（工作室）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/studio/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/studio-1.png" width="32.5%" alt="Studio — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/studio-4.png" width="32.5%" alt="Studio — slide 4" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/studio-8.png" width="32.5%" alt="Studio — slide 8" />
</p>

> 黑色画布搭配电光黄文字；高电压设计工作室美学。

### [Biennale Yellow（双年展黄）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/biennale-yellow/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/biennale-yellow-1.png" width="32.5%" alt="Biennale Yellow — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/biennale-yellow-5.png" width="32.5%" alt="Biennale Yellow — slide 5" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/biennale-yellow-8.png" width="32.5%" alt="Biennale Yellow — slide 8" />
</p>

> 暖羊皮纸上的阳光黄搭配深靛蓝衬线体与氛围感日光渐变。荷兰编辑风海报能量。

### [Long Table（长桌）](https://github.com/zarazhangrui/beautiful-html-templates/tree/main/templates/long-table/)

<p>
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/long-table-1.png" width="32.5%" alt="Long Table — slide 1" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/long-table-3.png" width="32.5%" alt="Long Table — slide 3" />
  <img src="https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/long-table-7.png" width="32.5%" alt="Long Table — slide 7" />
</p>

> 暖奶油色与铁锈红晚餐俱乐部美学，搭配粗体大写 Grotesque 标题、斜体 Fraunces 字体及胶囊轮廓按钮。

## 架构设计

该技能采用**渐进式披露（progressive disclosure）**机制——主文件 `SKILL.md` 为工作流地图，支撑文件仅在需要时按需加载：

| File | Purpose | Loaded When |
| ------------------------- | ------------------------------ | ------------------------- |
| `SKILL.md` | 核心工作流与规则 | 始终（技能调用时） |
| `STYLE_PRESETS.md` | 12 款精选视觉预设 | 第 2 阶段（风格选择） |
| `bold-template-pack/selection-index.json` | 紧凑的 Bold 模板元数据 | 第 2 阶段（候选筛选） |
| `bold-template-pack/templates/*/preview.md` | 入围 Bold 预览的小型风格卡片 | 第 2 阶段入围后 |
| `bold-template-pack/templates/*/design.md` | 选定 Bold 模板的完整设计系统 | 第 3 阶段用户选定后 |
| `viewport-base.css` | 强制固定阶段的 CSS | 第 3 阶段（生成） |
| `html-template.md` | HTML 结构与 JS 功能 | 第 3 阶段（生成） |
| `animation-patterns.md` | CSS/JS 动画参考 | 第 3 阶段（生成） |
| `scripts/extract-pptx.py` | PPT 内容提取 | 第 4 阶段（转换） |
| `scripts/deploy.sh` | 部署至 Vercel | 第 6 阶段（分享） |
| `scripts/export-pdf.sh` | 导出幻灯片为 PDF | 第 6 阶段（分享） |

仅用于维护的源元数据与再生辅助工具位于面向用户的技能包之外，普通用户无需使用。

此设计遵循代理技能最佳实践：先提供全局地图，随后仅揭示当前决策所需的具体文件。

## 设计理念

该技能的诞生源于以下信念：

1. **制作精美作品无需成为设计师。** 你只需对所见之物做出反应。
2. **依赖项即是债务。** 单个 HTML 文件十年后依然可用。而一个 2019 年的 React 项目？祝你好运。
3. **千篇一律令人遗忘。** 每份演示文稿都应感觉是量身定制的，而非模板批量生成。
4. **注释是一种善意。** 代码应能向未来的你（或任何打开它的人）自我解释。

## 分享演示文稿

创建演示文稿后，该技能提供两种分享方式：

### 部署至在线链接

一条命令即可将幻灯片部署为永久可分享的链接，支持所有设备（手机、平板、笔记本）访问：

```bash
bash scripts/deploy.sh ./my-deck/
# or
bash scripts/deploy.sh ./presentation.html
```

使用 [Vercel](https://vercel.com)（免费套餐）。若是首次使用，技能会引导你完成注册与登录。

### 导出为 PDF

将幻灯片转换为 PDF，适用于邮件、Slack、Notion 或打印：

```bash
bash scripts/export-pdf.sh ./my-deck/index.html
bash scripts/export-pdf.sh ./presentation.html ./output.pdf
```

使用 [Playwright](https://playwright.dev) 以 1920×1080 分辨率截取每张幻灯片并合并为 PDF。按需自动安装。动画效果将不保留（此为静态快照）。

## 环境要求

- 具备文件系统访问权限及 Shell 命令执行能力的本地代码代理
- 仅在使用自定义市场源安装及 `/frontend-slides:frontend-slides` 命令时需要 Claude Code
- 用于 PPT 转换：需安装 `python-pptx` 库的 Python 环境
- 用于链接部署：Node.js + Vercel 账号（免费）
- 用于 PDF 导出：Node.js（自动安装 Playwright）

## 致谢

由 [@zarazhangrui](https://github.com/zarazhangrui) 创建。

## 许可证

MIT —— 自由使用、修改与分享。