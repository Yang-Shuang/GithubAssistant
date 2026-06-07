# Contains Studio AI 智能体集合

一套专为加速和优化快速开发各个环节而设计的 AI 智能体（AI Agents）合集。每个智能体都是其领域的专家，随时准备在需要时调用。

## 📥 安装

1. **克隆本仓库：**
   ```bash
   git clone https://github.com/contains-studio/agents.git
   ```

2. **复制到你的 Claude Code 智能体目录：**
   ```bash
   cp -r agents/* ~/.claude/agents/
   ```
   
   或者手动将所有智能体文件复制到你本地的 `~/.claude/agents/` 目录。

3. **重启 Claude Code** 以加载新的智能体。

## 🚀 快速开始

这些智能体会自动在 Claude Code 中可用。只需描述你的任务，系统就会触发相应的智能体。你也可以通过直接提及名称来显式调用某个智能体。

📚 **了解更多：** [Claude Code Sub-Agents Documentation](https://docs.anthropic.com/en/docs/claude-code/sub-agents)

### 使用示例
- "Create a new app for tracking meditation habits" → `rapid-prototyper`
- "What's trending on TikTok that we could build?" → `trend-researcher`
- "Our app reviews are dropping, what's wrong?" → `feedback-synthesizer`
- "Make this loading screen more fun" → `whimsy-injector`

## 📁 目录结构

智能体按部门分类，便于快速查找：

```
contains-studio-agents/
├── design/
│   ├── brand-guardian.md
│   ├── ui-designer.md
│   ├── ux-researcher.md
│   ├── visual-storyteller.md
│   └── whimsy-injector.md
├── engineering/
│   ├── ai-engineer.md
│   ├── backend-architect.md
│   ├── devops-automator.md
│   ├── frontend-developer.md
│   ├── mobile-app-builder.md
│   ├── rapid-prototyper.md
│   └── test-writer-fixer.md
├── marketing/
│   ├── app-store-optimizer.md
│   ├── content-creator.md
│   ├── growth-hacker.md
│   ├── instagram-curator.md
│   ├── reddit-community-builder.md
│   ├── tiktok-strategist.md
│   └── twitter-engager.md
├── product/
│   ├── feedback-synthesizer.md
│   ├── sprint-prioritizer.md
│   └── trend-researcher.md
├── project-management/
│   ├── experiment-tracker.md
│   ├── project-shipper.md
│   └── studio-producer.md
├── studio-operations/
│   ├── analytics-reporter.md
│   ├── finance-tracker.md
│   ├── infrastructure-maintainer.md
│   ├── legal-compliance-checker.md
│   └── support-responder.md
├── testing/
│   ├── api-tester.md
│   ├── performance-benchmarker.md
│   ├── test-results-analyzer.md
│   ├── tool-evaluator.md
│   └── workflow-optimizer.md
└── bonus/
    ├── joker.md
    └── studio-coach.md
```

## 📋 完整智能体列表

### 工程部门（`engineering/`）
- **ai-engineer** - 集成真正能落地交付的 AI/机器学习功能
- **backend-architect** - 设计可扩展的 API 与服务器架构
- **devops-automator** - 持续部署且不破坏现有系统
- **frontend-developer** - 构建极速响应的用户界面
- **mobile-app-builder** - 打造原生 iOS/Android 体验
- **rapid-prototyper** - 数天内而非数周内完成 MVP 开发
- **test-writer-fixer** - 编写能捕获真实 Bug 的测试用例

### 产品部门（`product/`）
- **feedback-synthesizer** - 将用户抱怨转化为功能需求
- **sprint-prioritizer** - 在 6 天冲刺周期内交付最大价值
- **trend-researcher** - 发掘病毒式传播机会

### 市场部门（`marketing/`）
- **app-store-optimizer** - 霸占应用商店搜索结果排名
- **content-creator** - 跨平台生成营销内容
- **growth-hacker** - 发现并利用病毒式增长循环
- **instagram-curator** - 精通视觉内容运营策略
- **reddit-community-builder** - 在 Reddit 赢得社区支持而不被封号
- **tiktok-strategist** - 打造可分享营销时刻
- **twitter-engager** - 借势趋势实现病毒式互动

### 设计部门（`design/`）
- **brand-guardian** - 保持全平台视觉标识一致
- **ui-designer** - 设计开发者真正能落地的界面
- **ux-researcher** - 将用户洞察转化为产品改进
- **visual-storyteller** - 创作高转化、易传播的视觉内容
- **whimsy-injector** - 为每次交互注入惊喜感

### 项目管理（`project-management/`）
- **experiment-tracker** - 数据驱动的功能验证
- **project-shipper** - 发布稳定不崩溃的产品
- **studio-producer** - 让团队专注交付而非开会

### 工作室运营（`studio-operations/`）
- **analytics-reporter** - 将数据转化为可落地的洞察
- **finance-tracker** - 保持工作室持续盈利
- **infrastructure-maintainer** - 低成本扩展基础设施
- **legal-compliance-checker** - 在快速迭代中确保合规
- **support-responder** - 将愤怒用户转化为忠实拥趸

### 测试与基准（`testing/`）
- **api-tester** - 确保 API 在高负载下稳定运行
- **performance-benchmarker** - 提升整体性能与速度
- **test-results-analyzer** - 从测试失败中挖掘规律
- **tool-evaluator** - 甄选真正提效的工具
- **workflow-optimizer** - 消除工作流瓶颈

## 🎁 附加智能体
- **studio-coach** - 统筹 AI 团队，追求卓越表现
- **joker** - 用技术幽默调节气氛

## 🎯 主动触发智能体

部分智能体会在特定场景下自动触发：
- **studio-coach** - 当复杂的多智能体任务开始，或需要指导时
- **test-writer-fixer** - 实现功能、修复 Bug 或修改代码后
- **whimsy-injector** - 进行 UI/UX 变更后
- **experiment-tracker** - 添加功能开关（Feature Flags）时

## 💡 最佳实践

1. **让智能体协同工作** - 许多任务需要多个智能体配合才能发挥最大效用
2. **描述具体明确** - 清晰的任务描述有助于提升你的智能体表现
3. **信任专业领域能力** - 每个智能体都专为特定领域设计，请充分授权
4. **快速迭代** - 智能体支持“6天冲刺”开发理念

## 🔧 技术细节

### 智能体结构
每个智能体包含以下部分：
- **name**（名称）：唯一标识符
- **description**（描述）：使用场景说明及示例
- **color**（颜色）：视觉识别标记
- **tools**（工具）：智能体可访问的特定工具列表
- **System prompt**（系统提示词）：详细的领域知识与操作指令

### 添加新智能体
1. 在对应部门文件夹中创建新的 `.md` 文件
2. 遵循现有格式，包含 YAML Frontmatter（前置元数据）
3. 提供 3-4 个详细的使用示例
4. 撰写全面的系统提示词（不少于 500 字）
5. 使用真实任务测试智能体

## 📊 智能体性能评估

通过以下指标跟踪智能体的有效性：
- 任务完成时间
- 用户满意度
- 错误率
- 功能采纳率
- 开发速度

## 🚦 状态说明

- ✅ **Active**：功能完整且已测试通过
- 🚧 **Coming Soon**：开发中
- 🧪 **Beta**：有限功能测试中

## 🛠️ 为你的工作室定制智能体

### 智能体定制待办清单

在创建或修改适配你特定需求的智能体时，请使用此清单：

#### 📋 必需组件
- [ ] **YAML Frontmatter（前置元数据）**
  - [ ] `name`：智能体唯一标识符（使用 kebab-case 命名规范）
  - [ ] `description`：使用说明 + 附带上下文/注释的 3-4 个详细示例
  - [ ] `color`：视觉识别标记（如 blue、green、purple、indigo）
  - [ ] `tools`：智能体可访问的特定工具（Write、Read、MultiEdit、Bash 等）

#### 📝 系统提示词要求（500+ words）
- [ ] **智能体身份**：明确的角色定义与专业领域
- [ ] **核心职责**：5-8 项具体的主要任务
- [ ] **领域专长**：技术能力与知识范围
- [ ] **工作室集成**：你的智能体如何融入 6 天冲刺工作流
- [ ] **最佳实践**：具体的方法论与操作策略
- [ ] **约束条件**：明确你应该做/不应做的事项
- [ ] **成功指标**：衡量智能体有效性的方法

#### 🎯 按智能体类型所需的示例

**工程类智能体**需提供以下场景示例：
- [ ] 功能实现需求
- [ ] Bug 修复场景
- [ ] 代码重构任务
- [ ] 架构决策

**设计类智能体**需提供以下场景示例：
- [ ] 新建 UI 组件
- [ ] 设计规范（Design System）工作
- [ ] 用户体验问题
- [ ] 视觉标识任务

**市场类智能体**需提供以下场景示例：
- [ ] 营销活动创建需求
- [ ] 特定平台内容需求
- [ ] 增长机会挖掘
- [ ] 品牌定位任务

**产品类智能体**需提供以下场景示例：
- [ ] 功能优先级决策
- [ ] 用户反馈分析
- [ ] 市场调研需求
- [ ] 战略规划需求

**运营类智能体**需提供以下场景示例：
- [ ] 流程优化
- [ ] 工具评估
- [ ] 资源管理
- [ ] 性能分析

#### ✅ 测试与验证清单
- [ ] **触发测试**：你的智能体能按预期正确激活
- [ ] **工具访问**：智能体能正确使用所有指定工具
- [ ] **输出质量**：回复内容具有帮助性且可落地执行
- [ ] **边界情况**：智能体能妥善处理意外或复杂场景
- [ ] **协同集成**：在多智能体工作流中与其他智能体配合良好
- [ ] **性能表现**：能在合理时间内完成任务
- [ ] **文档说明**：示例能准确反映真实使用模式

#### 🔧 智能体文件结构模板

```markdown
---
name: your-agent-name
description: Use this agent when [scenario]. This agent specializes in [expertise]. Examples:\n\n<example>\nContext: [situation]\nuser: "[user request]"\nassistant: "[response approach]"\n<commentary>\n[why this example matters]\n</commentary>\n</example>\n\n[3 more examples...]
color: agent-color
tools: Tool1, Tool2, Tool3
---

You are a [role] who [primary function]. Your expertise spans [domains]. You understand that in 6-day sprints, [sprint constraint], so you [approach].

Your primary responsibilities:
1. [Responsibility 1]
2. [Responsibility 2]
...

[Detailed system prompt content...]

Your goal is to [ultimate objective]. You [key behavior traits]. Remember: [key philosophy for 6-day sprints].
```

#### 📂 部门专属指南

**工程（`engineering/`）**：聚焦实现速度、代码质量与测试
**设计（`design/`）**：强调用户体验、视觉一致性与快速迭代  
**市场（`marketing/`）**：瞄准病毒传播潜力、平台专长与增长指标
**产品（`product/`）**：优先保障用户价值、数据驱动决策与市场契合度
**运营（`studio-operations/`）**：优化流程、减少摩擦并扩展系统
**测试（`testing/`）**：确保质量、定位瓶颈并验证性能
**项目管理（`project-management/`）**：协调团队、按时交付并控制范围

#### 🎨 自定义选项

根据你的需求修改以下元素：
- [ ] 调整示例以匹配你的产品类型
- [ ] 添加智能体可访问的特定工具
- [ ] 根据你的 KPI 修改成功指标
- [ ] 按需更新部门结构
- [ ] 为你的品牌定制智能体颜色

## 🤝 贡献指南

如需优化现有智能体或建议新增智能体：
1. 使用上方的定制清单
2. 结合真实项目进行充分测试
3. 记录性能改进情况
4. 与社区分享成功模式