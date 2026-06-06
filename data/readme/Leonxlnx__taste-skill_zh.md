<p align="center">
  <img src="assets/readme-banner.png" alt="Taste Skill - Anti-slop Agent Skills for premium frontends" width="100%" />
</p>

# Taste Skill

<p align="center">
  <em>面向 AI Agent 的反套路（Anti-Slop）前端框架</em>
</p>

<p align="center">
  <a href="https://tasteskill.dev" title="Taste Skill - tasteskill.dev">
    <img src="assets/taste-skill-logo.webp" width="80" height="80" alt="Taste Skill" />
  </a>
</p>

<p align="center">
  <a href="https://tasteskill.dev">
    <img src="https://img.shields.io/badge/OPEN-tasteskill.dev-%23a855f7?style=for-the-badge&labelColor=%230f172a" alt="Open tasteskill.dev" />
  </a>
</p>

可移植的 **Agent Skills**，用于升级 AI 生成的界面：提供更出色的布局、排版、动效和间距，告别千篇一律的模板化 UI。本仓库还包含用于参考板（网页、移动端、品牌指南）的 **图像生成技能**。将它们与 **ChatGPT Images** 或类似工具配合使用，然后将生成的界面帧交给 Codex、Cursor 或 Claude Code 进行实现。

<p align="center">
<a href="https://github.com/Leonxlnx/taste-skill/stargazers"><img src="https://img.shields.io/github/stars/Leonxlnx/taste-skill?style=for-the-badge&logo=github&labelColor=1e293b&color=fbbf24" alt="GitHub stars"/></a>
<a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-fbbf24?style=for-the-badge&labelColor=1e293b" alt="MIT License"/></a>
<a href="#installing"><img src="https://img.shields.io/badge/Tools-Codex%20%C2%B7%20Cursor%20%C2%B7%20Claude-111827?style=for-the-badge&labelColor=1e293b" alt="Supported agents"/></a>
<a href="https://www.tasteskill.dev/changelog"><img src="https://img.shields.io/badge/Changelog-Latest-059669?style=for-the-badge&labelColor=1e293b" alt="Changelog on tasteskill.dev"/></a>
</p>

## 免责声明

Taste Skill 没有官方的代币、币种或加密货币项目。任何使用我的名字、图像或项目的代币均与我无关，且未获得我的认可。

<p align="center"><sub><a href="#disclaimer">免责声明</a> · <a href="#installing">安装</a> · <a href="#skills">技能列表</a> · <a href="#settings-taste-skill-only">设置项</a> · <a href="#examples">示例</a> · <a href="#support-the-project">赞助支持</a> · <a href="#research">研究背景</a> · <a href="#common-questions">常见问题</a> · <a href="#license">许可证</a></sub></p>

## 反馈与贡献

我们非常欢迎你的反馈。建议与 Bug 报告：

- 在 GitHub 上提交 Pull Request 或 Issue  
- 私信 [@lexnlin](https://x.com/lexnlin) 或 [@blueemi99](https://x.com/blueemi99)  
- 发送邮件至 [hello@tasteskill.dev](mailto:hello@tasteskill.dev)

## 安装

[`npx skills add`](https://github.com/vercel-labs/agent-skills) CLI 会扫描本仓库中的 `skills/` 文件夹，因此**以下所有技能（代码与图像生成类）的安装方式相同。**

```bash
npx skills add https://github.com/Leonxlnx/taste-skill
```

通过其**安装名称**（SKILL frontmatter 中的 `name:` 字段，而非文件夹名）安装单个技能：

```bash
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"
```

你也可以将任意 `SKILL.md` 复制到你的项目中，或直接粘贴到 ChatGPT / Codex 对话中。

### 从旧版本升级

默认的 `taste-skill`（安装名称为 `design-taste-frontend`）现已升级为 **v2（实验性版本）**，这是对原版 v1 的重大重写。如果你已安装 v1，只需重新运行安装命令即可升级：

```bash
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"
```

安装名称未发生变化，因此无需更新脚本。新版 `SKILL.md` 会直接覆盖旧版文件。

如果你依赖 v1 的确切行为并希望显式锁定它：

```bash
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend-v1"
```

完整 v1 到 v2 的差异对比及设计考量请参阅 [CHANGELOG.md](CHANGELOG.md)。

## 技能列表

每个技能仅负责单一功能；你无需一次性全部使用。**实现类技能**输出代码，**图像生成类技能**仅输出参考图片。

`安装名称` 列即为传递给 `--skill` 参数的确切值。

| Skill (folder) | Install name | Description |
| --- | --- | --- |
| **taste-skill** | `design-taste-frontend` | 🆕 **v2（实验性）** - 默认技能的重大重写。读取需求简报，推断设计语言，调节三个旋钮（VARIANCE / MOTION / DENSITY）。包含需求推断、设计系统映射、禁用硬破折号、GSAP 标准代码骨架、重审协议及严格的预检检查。正积极迭代至 v2.0.0 稳定版。 |
| **taste-skill-v1** | `design-taste-frontend-v1` | taste-skill 的原始 v1 版本，保留用于依赖其确切行为的项目。仅当 v2 默认设置破坏了你工作流中的特定功能时使用。 |
| **gpt-tasteskill** | `gpt-taste` | GPT/Codex 专用更严格变体：更高的布局方差、更强的 GSAP 指导方向及激进的防套路策略。 |
| **image-to-code-skill** | `image-to-code` | 图像优先流程：生成网站参考图，分析它们，然后实现匹配的界面代码。 |
| **redesign-skill** | `redesign-existing-projects` | 现有项目：先审计界面，再修复布局、间距、层级与样式。 |
| **soft-skill** | `high-end-visual-design` | 精致、沉稳、高端的 UI，采用柔和对比度、充足留白、高级字体及弹性动效。 |
| **output-skill** | `full-output-enforcement` | 当模型交付半成品时：强制完整输出，禁止占位符注释。 |
| **minimalist-skill** | `minimalist-ui` | 编辑类/产品型 UI（Notion/Linear 风格），克制配色，结构清晰。 |
| **brutalist-skill** | `industrial-brutalist-ui` | 硬核机械语言：瑞士排版、高对比度、实验性布局。 |
| **stitch-skill** | `stitch-design-taste` | Google Stitch 兼容规则，包含可选的 `DESIGN.md` 导出格式。 |

### 图像生成技能

仅输出设计图片（不含代码）。配合 ChatGPT Images、Codex 图像模式或任何能生成图像的 Agent 使用。

| Skill (folder) | Install name | Description |
| --- | --- | --- |
| **imagegen-frontend-web** | `imagegen-frontend-web` | 网站原型：首页横幅、着陆页、多区块页面，强调排版、间距与反套路视觉指导。 |
| **imagegen-frontend-mobile** | `imagegen-frontend-mobile` | 移动端界面与流程：iOS/Android/跨平台，高保真原型图，可读性强且风格统一。 |
| **brandkit** | `brandkit` | 品牌指南板：Logo 方向、配色方案、字体排印及全品类身份应用。 |

### 我该使用哪一个？

- 默认首选 **taste-skill**，它是最稳妥的通用设置。（现为 v2 实验版——详见 [CHANGELOG](CHANGELOG.md) 中的变更说明。）
- 如果你依赖原版 taste-skill 的确切行为，请安装 **taste-skill-v1**。 
- 当你需要更严格的 GPT/Codex 专属规则以及更强的动效/布局强制约束时，使用 **gpt-taste**。 
- 对于“图像生成 → 分析 → 代码实现”的网站工作流，使用 **image-to-code-skill**。 
- 针对现有代码库进行优化而非从零开始编写样式时，使用 **redesign-skill**。 
- 当视觉风格方向已确定时，可添加 **soft-skill**、**minimalist-skill** 或 **brutalist-skill**。 
- 如果 Agent 总是截断输出内容，请添加 **output-skill**。 
- 当交付物为**图片**（原型图、交互流程、品牌板）时，使用 **imagegen-frontend-web**、**imagegen-frontend-mobile** 或 **brandkit**，然后将结果交由你的代码生成 Agent。

### 图像优先工作流建议

对于 **image-to-code-skill**，请在提示词中明确说明流程，例如：`遵循该技能规范：生成图片，然后进行分析，最后编写代码。`

### ChatGPT Images 与 Codex

附加或粘贴 **\`imagegen-frontend-web\`**、**\`imagegen-frontend-mobile\`** 或 **\`brandkit\`**，并请求你需要的界面帧/草图，然后将渲染结果喂给 Codex、Cursor 或 Claude Code。当你希望在一个工作流中同时完成参考图生成与代码实现时，请使用 **image-to-code-skill**。

## 设置项（仅 taste-skill）

文件顶部的数值为 1-10 的调节旋钮：

- **DESIGN_VARIANCE**（设计方差）：布局实验性（低值：居中/简洁 · 高值：非对称/现代）。
- **MOTION_INTENSITY**（动效强度）：动画深度（低值：悬停效果 · 高值：滚动/磁性交互）。
- **VISUAL_DENSITY**（视觉密度）：视口信息量（低值：宽敞留白 · 高值：密集仪表盘）。

## 示例

由 taste-skill 生成：

<p>
  <img src="examples/floria-top.webp" width="400" />
  <img src="examples/floria-bottom.webp" width="400" />
</p>

## 支持该项目

如果 Taste Skill 对你有所帮助，欢迎考虑赞助：

[在 GitHub 上赞助](https://github.com/sponsors/Leonxlnx)

### 当前赞助商

<a href="https://github.com/dnakov"><img src="https://github.com/dnakov.png" width="40" height="40" style="border-radius:50%" alt="dnakov" title="dnakov" /></a>
<a href="https://github.com/AkramReshad"><img src="https://github.com/AkramReshad.png" width="40" height="40" style="border-radius:50%" alt="AkramReshad" title="AkramReshad" /></a>
<a href="https://github.com/ajmalaksar25"><img src="https://github.com/ajmalaksar25.png" width="40" height="40" style="border-radius:50%" alt="ajmalaksar25" title="ajmalaksar25" /></a>
<a href="https://github.com/krikkkk"><img src="https://github.com/krikkkk.png" width="40" height="40" style="border-radius:50%" alt="krikkkk" title="krikkkk" /></a>
<a href="https://github.com/navanchauhan"><img src="https://github.com/navanchauhan.png" width="40" height="40" style="border-radius:50%" alt="navanchauhan" title="navanchauhan" /></a>
<a href="https://github.com/robinebers"><img src="https://github.com/robinebers.png" width="40" height="40" style="border-radius:50%" alt="robinebers" title="robinebers" /></a>
<a href="https://github.com/JKc66"><img src="https://github.com/JKc66.png" width="40" height="40" style="border-radius:50%" alt="JKc66" title="JKc66" /></a>
<a href="https://github.com/u2393696078-rgb"><img src="https://github.com/u2393696078-rgb.png" width="40" height="40" style="border-radius:50%" alt="u2393696078-rgb" title="u2393696078-rgb" /></a>
<a href="https://github.com/a-human-created-this"><img src="https://github.com/a-human-created-this.png" width="40" height="40" style="border-radius:50%" alt="a-human-created-this" title="a-human-created-this" /></a>
<a href="https://github.com/AtharvaJaiswal005"><img src="https://github.com/AtharvaJaiswal005.png" width="40" height="40" style="border-radius:50%" alt="AtharvaJaiswal005" title="AtharvaJaiswal005" /></a>
<a href="https://github.com/ghughes7"><img src="https://github.com/ghughes7.png" width="40" height="40" style="border-radius:50%" alt="ghughes7" title="ghughes7" /></a>
<a href="https://github.com/mccun934"><img src="https://github.com/mccun934.png" width="40" height="40" style="border-radius:50%" alt="mccun934" title="mccun934" /></a>

<p align="center">
 <a href="https://www.star-history.com/leonxlnx/taste-skill">
  <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/badge?repo=Leonxlnx/taste-skill&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/badge?repo=Leonxlnx/taste-skill" />
   <img alt="Star History Rank" src="https://api.star-history.com/badge?repo=Leonxlnx/taste-skill" />
  </picture>
 </a>
</p>

## 研究背景

塑造这些技能的理念与背景文章位于 [`research/`](research/) 目录中。

## 常见问题

**与其他 AI 设计技能有何不同？**  
提供多种专业变体，关键技能支持可调旋钮，并内置基于专项研究的防重复规则。所有技能均与主流代码生成 Agent 兼容，不绑定特定框架。

**是否支持 React、Vue、Svelte？**  
是的。规则针对设计意图而非单一框架的 API。

**什么是 SKILL.md？**  
一种 Agent 可自动加载的可移植指令文件；可通过 `npx skills add` 安装，或直接复制到仓库/对话中。

**图像生成技能是否也通过 `npx skills add` 安装？**  
是的。它们与代码类技能一同存放在 `skills/` 目录下，因此相同的 CLI 会自动识别并安装它们。

## 许可证

[MIT 许可证](LICENSE) · © 2026 Leonxlnx