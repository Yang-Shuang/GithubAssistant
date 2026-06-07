# MiniMax Skills

[中文版](./README_zh.md)

> **Beta** — 本项目正在积极开发中。技能、API 和配置格式可能会在不另行通知的情况下发生变化。欢迎提供反馈与贡献。

面向 AI 编程代理的开发技能集。接入你常用的 AI 编程工具，获取针对前端、全栈、Android、iOS 和着色器开发的结构化、生产级指导。

## Skills

| Skill&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description | Source |
|---------------------------------------|-------------|--------|
| `frontend-dev` | 前端开发：结合高品质 UI 设计、电影级动画（Framer Motion、GSAP）、MiniMax API 生成的 AI 媒体素材（图像、视频、音频、音乐、TTS）、说服性文案撰写（AIDA 框架）以及生成式艺术（p5.js、Three.js、Canvas）。技术栈：React / Next.js、Tailwind CSS。 | Official |
| `fullstack-dev` | 全栈开发：后端架构设计与前后端集成。REST API 设计、认证流程（JWT、Session、OAuth）、实时功能（SSE、WebSocket）、数据库集成（SQL / NoSQL）、生产环境加固及发布清单。引导工作流：需求分析 → 架构设计 → 代码实现。 | Official |
| `android-native-dev` | Android 原生开发：基于 Material Design 3 的 Android 应用开发。涵盖 Kotlin / Jetpack Compose、自适应布局、Gradle 配置、无障碍访问（WCAG）、构建故障排查、性能优化及动效系统。 | Official |
| `ios-application-dev` | iOS 应用开发：覆盖 UIKit、SnapKit 和 SwiftUI 的 iOS 开发指南。包含触摸区域、安全区域、导航模式、动态类型、深色模式、无障碍访问、集合视图及 Apple HIG 规范合规性。 | Official |
| `flutter-dev` | Flutter 开发：跨平台开发技能，涵盖组件模式、Riverpod/Bloc 状态管理、GoRouter 导航、性能优化及测试策略。 | Official |
| `react-native-dev` | React Native 开发：覆盖组件、样式、动画、导航、状态管理、表单、网络请求、性能优化、测试、原生能力及工程化（项目结构、部署、SDK 升级、CI/CD）的指南。 | Official |
| `shader-dev` | 着色器开发：全面的 GLSL 着色器技术，用于创建惊艳的视觉效果——光线步进、SDF 建模、流体模拟、粒子系统、程序化生成、光照、后处理等。兼容 ShaderToy。 | Official |
| `gif-sticker-maker` | GIF 贴纸制作：将照片（人物、宠物、物品、Logo）转换为带配文的 4 张动态 GIF 贴纸。采用 Funko Pop / Pop Mart 风格，由 MiniMax 图像与视频生成 API 驱动。 | Official |
| `minimax-pdf` | MiniMax PDF：基于 Token 的设计系统生成、填充和重新格式化 PDF 文档。从头创建精美 PDF（15 种封面风格）、填写现有表单字段，或将文档重新格式化为新设计风格。输出可打印内容，排版与配色源自文档类型。 | Official |
| `pptx-generator` | PPTX 生成器：生成、编辑和读取 PowerPoint 演示文稿。使用 PptxGenJS 从头创建（封面、目录、内容页、章节分隔符、总结幻灯片）、通过 XML 工作流编辑现有 PPTX，或使用 markitdown 提取文本。 | Official |
| `minimax-xlsx` | MiniMax XLSX：打开、创建、读取、分析、编辑或验证 Excel/电子表格文件（.xlsx、.xlsm、.csv、.tsv）。涵盖通过 XML 模板从头创建 xlsx、使用 pandas 读取与分析、零格式损失地编辑现有文件、公式重算、验证及专业财务排版。 | Official |
| `minimax-docx` | MiniMax DOCX：使用 OpenXML SDK (.NET) 进行专业的 DOCX 文档创建、编辑与格式化。三大流程：从头新建文档、填充/编辑现有文档内容，或通过 XSD 验证门控应用模板格式。 | Official |
| `vision-analysis` | 视觉分析：使用视觉 AI 模型对图像进行分析、描述和信息提取。支持描述生成、OCR、UI 原型审查、图表数据提取及目标检测。由 MiniMax VL API 驱动，并兼容 OpenAI GPT-4V 降级方案。 | Community |
| `minimax-multimodal-toolkit` | MiniMax 多模态工具包：通过 MiniMax API 生成语音、音乐、视频和图像内容——统一入口，覆盖 MiniMax 多模态用例。包含 TTS（文本转语音、声音克隆、声音设计、分段）、音乐（歌曲、纯音乐）、视频（文生视频、图生视频、首尾帧控制、主体参考、模板、长片多场景）、图像（文生图、带角色参考的图生图）及媒体处理（转换、拼接、裁剪、提取，基于 FFmpeg）。 | Official |
| `minimax-music-gen` | MiniMax 音乐生成：使用 MiniMax Music API 生成带人声的歌曲、纯音乐和翻唱。两种模式：基础（一句话输入，直接输出歌曲）与高级控制（编辑歌词、优化提示词、规划结构）。支持歌词生成、风格词汇库、流媒体播放及迭代反馈。 | Official |
| `buddy-sings` | 伙伴歌唱：让你的 Claude Code 宠物（/buddy）唱一首个性化歌曲。解析宠物的名称与性格，生成独特的缓存语音身份，自动收集上下文（对话、记忆、Git 历史）以创作主题歌词，并通过 minimax-music-gen 生成音乐。 | Official |
| `minimax-music-playlist` | MiniMax 音乐歌单：通过分析你的听歌品味生成个性化歌单。构建口味画像（流派、情绪、语言、人声偏好），规划主题曲目列表，使用专辑封面艺术生成歌曲，并根据反馈优化画像。 | Official |

## Installation

### Claude Code

```bash
claude plugin marketplace add https://github.com/MiniMax-AI/skills
claude plugin install minimax-skills
```

### Cursor

```bash
git clone https://github.com/MiniMax-AI/skills.git ~/.cursor/minimax-skills
```

在 Cursor 设置中添加该路径，将技能（skills）目录指向 `~/.cursor/minimax-skills/skills/`。
Windows 环境的安装与验证说明，请参阅 [`.cursor-plugin/INSTALL.md`](.cursor-plugin/INSTALL.md)。

### Codex

```bash
git clone https://github.com/MiniMax-AI/skills.git ~/.codex/minimax-skills

mkdir -p ~/.agents/skills
ln -s ~/.codex/minimax-skills/skills ~/.agents/skills/minimax-skills
```

重启 Codex 以加载技能。Windows 环境的具体操作与详细说明请参阅 [`.codex/INSTALL.md`](.codex/INSTALL.md)。

### OpenCode

```bash
git clone https://github.com/MiniMax-AI/skills.git ~/.minimax-skills

mkdir -p ~/.config/opencode/skills
ln -s ~/.minimax-skills/skills/* ~/.config/opencode/skills/
```

重启 OpenCode 以加载技能。详细说明请参阅 [`.opencode/INSTALL.md`](.opencode/INSTALL.md)。

### VS Code

本仓库目前不提供独立的 VS Code 扩展插件。

如果你使用 VS Code，官方推荐的做法是在集成终端中运行受支持的 CLI 工具之一：
- Codex
- Claude Code
- OpenCode

如果你希望直接配置本仓库的原生本地技能（local-skills），请使用 Cursor 并遵循 [`.cursor-plugin/INSTALL.md`](.cursor-plugin/INSTALL.md) 中的说明。

## Contributing

欢迎提交贡献！在提交 PR 之前，请阅读以下内容：

- [CONTRIBUTING.md](./CONTRIBUTING.md) — PR 格式规范、技能结构要求及开发指南
- [PR Review Rules](./.claude/skills/pr-review/SKILL.md) — 自动化验证检查与质量评审标准

提交前，你可以在本地运行验证脚本：

```bash
python .claude/skills/pr-review/scripts/validate_skills.py
```

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=MiniMax-AI/skills&type=Date)](https://star-history.com/#MiniMax-AI/skills&Date)

## Credits

本仓库中的部分技能灵感来源于或改编自开源社区的工作。完整致谢请参阅 [CREDITS.md](./CREDITS.md)。

## License

[MIT](./LICENSE)