# 代理技能 (Agent Skills)

面向 AI 编程代理的技能集合。技能是打包好的指令和脚本，用于扩展代理的功能。

技能遵循 [Agent Skills](https://agentskills.io/) 格式规范。

[![skills.sh](https://skills.sh/b/vercel-labs/agent-skills)](https://skills.sh/vercel-labs/agent-skills)

## 可用技能

### vercel-optimize

对 Vercel 项目进行全面审计，涵盖成本、性能、可靠性、缓存、函数使用情况及计费优化机会。它会先收集 Vercel 指标数据，随后仅针对这些指标所指向的路由和文件进行深入排查。

**适用场景：**

- 优化已部署的 Vercel 项目
- 降低 Vercel 成本或函数调用量
- 排查缓慢或高成本的接口/路由
- 发现缓存、ISR（增量静态再生）、中间件、图片处理或构建时长问题
- 生成按优先级排序的成本与性能报告

### react-best-practices

来自 Vercel 工程团队的 React 和 Next.js 性能优化指南。包含 8 大类、40 余条规则，并按影响程度进行优先级排序。

**适用场景：**

- 编写新的 React 组件或 Next.js 页面
- 实现数据请求（客户端或服务端）
- 审查代码中的性能问题
- 优化打包体积或加载时间

**覆盖类别：**

- 消除请求瀑布流（关键）
- 打包体积优化（关键）
- 服务端性能（高）
- 客户端数据请求（中高）
- 重渲染优化（中）
- 渲染性能（中）
- JavaScript 微优化（低中）

### web-design-guidelines

审查 UI 代码是否符合 Web 界面最佳实践。审计你的代码是否满足 100 余条规则，涵盖无障碍访问、性能和用户体验（UX）。

**适用场景：**

- “审查我的 UI”
- “检查无障碍访问支持”
- “审计设计实现”
- “审查用户体验”
- “对照最佳实践检查我的网站”

**覆盖类别：**

- 无障碍访问（`aria-labels`、语义化 HTML、键盘事件处理）
- 焦点状态（可见焦点、focus-visible 模式）
- 表单（自动补全、验证、错误处理）
- 动画（`prefers-reduced-motion`、兼容合成器的变换）
- 排版/字体（弯引号、省略号字符、等宽数字 `tabular-nums`）
- 图片（尺寸、懒加载、替代文本）
- 性能（列表虚拟化、布局抖动/重排、预连接）
- 导航与状态（URL 反映状态、深度链接）
- 深色模式与主题（`color-scheme`、`theme-color` meta 标签）
- 触控与交互（`touch-action`、点击高亮）
- 本地化与国际化的（`Intl.DateTimeFormat`、`Intl.NumberFormat`）

### writing-guidelines

审查文档和正文内容是否符合《Vercel 写作手册》规范。审计你的页面是否满足 80 余条规则，涵盖语气、结构、内容类型、代码示例、排版和 AI 工作流。

**适用场景：**

- “审查我的文档”
- “检查写作风格”
- “审计正文内容”
- “审查文档语气与基调”
- “对照写作手册检查此页面”

**覆盖类别：**

- 规划（内容计划、内容类型、面向用户的目标标题）
- 语气与基调（主动语态、直接称呼，禁用词如 `easy`/`simple`/`quick`）
- 按内容类型调整语调（教程、操作指南、参考文档、概念解析、故障排查）
- 标题与结构（句子大小写、描述性副标题、TL;DR 摘要前置）
- 列表（使用场景、加粗/描述格式）
- 代码（语言标签、优先使用 TypeScript、`<Steps/>` 组件、限制 80 列宽 / 25 行）
- 占位符、单位与数字（`snake_case` 文本、递增数字格式、`64 KB`/`200 ms`）
- 排版（标点不用长破折号、使用弯引号、省略号字符、不换行空格）
- 源码格式（不硬换行、不使用 `---` 分隔线规则、严格空行规范）
- 定价与金额页面（表格展示、细节严谨）
- AI 工作流（明确责任归属、企业级模型优先、先规划后执行、披露 AI 使用情况）
- 审查流程（严格 PR 描述规范、作者责任制）

### react-native-guidelines

专为 AI 代理优化的 React Native 最佳实践。包含 7 个章节、16 条规则，涵盖性能、架构及平台特定模式。

**适用场景：**

- 构建 React Native 或 Expo 应用
- 优化移动端性能
- 实现动画或手势交互
- 使用原生模块或平台 API

**覆盖类别：**

- 性能（关键）- FlashList、记忆化缓存（Memoization）、重型计算
- 布局（高）- Flex 模式、安全区域适配、键盘处理
- 动画（高）- Reanimated、手势处理
- 图片（中）- expo-image、缓存策略、懒加载
- 状态管理（中）- Zustand 模式、React Compiler
- 架构（中）- Monorepo 结构、导入规范
- 平台适配（中）- iOS/Android 特定模式

### react-view-transitions

使用 React 的 View Transition API 实现流畅、原生质感的动画。涵盖 `<ViewTransition>` 组件、`addTransitionType` 函数、过渡类型，以及 Next.js 集成（包括 `next/link` 的 `transitionTypes` 属性）。

**适用场景：**

- 添加页面切换或路由动画
- 实现组件进入/退出动画
- 创建共享元素过渡（如列表到详情的形变效果）
- 实现方向性（前进/后退）导航动画
- 在 Next.js App Router 中集成视图过渡
- 实现列表重排序或 Suspense 降级内容展示动画

**涵盖主题：**

- `<ViewTransition>` 组件（触发 `enter`、`exit`、`update`、`share`）
- 用于方向性/上下文特定动画的 `addTransitionType`
- View Transition 类与 CSS 伪元素
- 使用 `name` 属性的共享元素过渡
- 通过 Web Animations API 实现 JS 动画
- `next/link` 上的 Next.js `transitionTypes` 属性
- 开箱即用的 CSS 动画方案（淡入淡出、滑动、缩放、翻转）
- 无障碍访问（支持 `prefers-reduced-motion`）

### composition-patterns

可扩展的 React 组合模式。通过复合组件、状态提升和内部组合，帮助避免布尔类型 Props 泛滥。

**适用场景：**

- 重构包含大量布尔类型 Props 的组件
- 构建可复用的组件库
- 设计灵活的 API 接口
- 审查组件架构

**涵盖模式：**

- 提取复合组件
- 提升状态以减少 Props 传递
- 组合内部实现以提升灵活性
- 避免 Prop Drilling（属性透传）

### vercel-deploy-claimable

将应用和网站即时部署到 Vercel。专为与 claude.ai 及 Claude Desktop 配合使用而设计，支持直接从对话中触发部署。部署内容支持“认领”（Claimable）——用户可将所有权转移至自己的 Vercel 账户。

**适用场景：**

- “部署我的应用”
- “将此部署到生产环境”
- “推送到线上”
- “部署并给我链接”

**功能特性：**

- 自动从 `package.json` 检测 40 多种框架
- 返回预览地址（线上站点）和认领链接（转移所有权）
- 自动处理静态 HTML 项目
- 上传时排除 `node_modules` 和 `.git` 目录

**工作原理：**

1. 将项目打包为 tarball 归档文件
2. 检测框架（Next.js、Vite、Astro 等）
3. 上传至部署服务
4. 返回预览地址和认领链接

**输出示例：**

```
Deployment successful!

Preview URL: https://skill-deploy-abc123.vercel.app
Claim URL:   https://vercel.com/claim-deployment?code=...
```

## 安装

```bash
npx skills add vercel-labs/agent-skills
```

## 使用方式

技能安装后即可自动生效。当检测到相关任务时，代理会自动调用这些技能。

**示例：**

```
Deploy my app
```

```
Review this React component for performance issues
```

```
Help me optimize this Next.js page
```

## 技能结构

每个技能包含：

- `SKILL.md` - 代理指令说明
- `scripts/` - 自动化辅助脚本（可选）
- `references/` - 参考文档（可选）

## 许可证

MIT