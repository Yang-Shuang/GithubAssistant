# 上下文工程模板

一个用于入门上下文工程的综合模板——该领域专注于为 AI 编程助手构建必要的上下文信息，使其能够端到端地完成开发任务。

> **上下文工程的效果是提示词（prompt engineering）的 10 倍，更是氛围编程（vibe coding）的 100 倍。**

## 🚀 快速开始

```bash
# 1. Clone this template
git clone https://github.com/coleam00/Context-Engineering-Intro.git
cd Context-Engineering-Intro

# 2. Set up your project rules (optional - template provided)
# Edit CLAUDE.md to add your project-specific guidelines

# 3. Add examples (highly recommended)
# Place relevant code examples in the examples/ folder

# 4. Create your initial feature request
# Edit INITIAL.md with your feature requirements

# 5. Generate a comprehensive PRP (Product Requirements Prompt)
# In Claude Code, run:
/generate-prp INITIAL.md

# 6. Execute the PRP to implement your feature
# In Claude Code, run:
/execute-prp PRPs/your-feature-name.md
```

## 📚 目录

- [什么是上下文工程？](#什么是上下文工程)
- [模板结构](#模板结构)
- [分步指南](#分步指南)
- [如何编写高效的 INITIAL.md 文件](#如何编写有效的-initialmd-files)
- [PRP 工作流](#prp-workflow)
- [有效使用示例](#using-examples-effectively)
- [最佳实践](#best-practices)

## 什么是上下文工程？

上下文工程（Context Engineering）代表了从传统提示词工程的范式转变：

### 提示词工程 vs 上下文工程

**提示词工程：**
- 侧重于巧妙的措辞和特定表述
- 仅局限于你如何描述任务
- 就像给别人一张便利贴

**上下文工程：**
- 一套提供全面上下文的完整系统
- 包含文档、示例、规则、模式以及验证机制
- 就像撰写一部细节详尽的完整剧本

### 为什么上下文工程至关重要

1. **降低 AI 失败率**：大多数智能体（agent）的失败并非模型能力不足，而是上下文缺失导致的。
2. **确保一致性**：AI 会严格遵循你的项目模式与规范。
3. **支持复杂功能开发**：在上下文完善的情况下，AI 能够处理多步骤的实现任务。
4. **自我修正能力**：验证循环机制允许 AI 自动修复自身错误。

## 模板结构

```
context-engineering-intro/
├── .claude/
│   ├── commands/
│   │   ├── generate-prp.md    # Generates comprehensive PRPs
│   │   └── execute-prp.md     # Executes PRPs to implement features
│   └── settings.local.json    # Claude Code permissions
├── PRPs/
│   ├── templates/
│   │   └── prp_base.md       # Base template for PRPs
│   └── EXAMPLE_multi_agent_prp.md  # Example of a complete PRP
├── examples/                  # Your code examples (critical!)
├── CLAUDE.md                 # Global rules for AI assistant
├── INITIAL.md               # Template for feature requests
├── INITIAL_EXAMPLE.md       # Example feature request
└── README.md                # This file
```

本模板暂未将重点放在基于上下文工程的 RAG 和工具集成上，因为我近期会推出更多相关内容。;)

## 分步指南

### 1. 配置全局规则（CLAUDE.md）

``CLAUDE.md`` 文件包含了 AI 助手在每次对话中都会遵循的全局项目规范。模板默认包含：

- **项目感知**：自动读取规划文档、检查任务状态
- **代码结构**：文件大小限制、模块组织方式
- **测试要求**：单元测试模式、覆盖率预期
- **风格规范**：语言偏好、格式化规则
- **文档标准**：函数注释格式、代码注释习惯

**你可以直接使用提供的模板，或根据项目需求进行自定义。**

### 2. 创建初始功能需求

编辑 ``INITIAL.md`` 来描述你想开发的功能：

```markdown
## FEATURE:
[Describe what you want to build - be specific about functionality and requirements]

## EXAMPLES:
[List any example files in the examples/ folder and explain how they should be used]

## DOCUMENTATION:
[Include links to relevant documentation, APIs, or MCP server resources]

## OTHER CONSIDERATIONS:
[Mention any gotchas, specific requirements, or things AI assistants commonly miss]
```

**完整示例请参考 ``INITIAL_EXAMPLE.md``。**

### 3. 生成 PRP（产品需求提示词）

PRP（Product Requirements Prompt，产品需求提示词）是一份综合性的实施蓝图，包含：

- 完整的上下文与文档说明
- 带有验证机制的实施步骤
- 错误处理模式
- 测试要求

它们类似于 PRD（Product Requirements Document，产品需求文档），但经过专门设计，以更精准地指导 AI 编程助手。

在 Claude Code 中运行：
```bash
/generate-prp INITIAL.md
```

**注意：** 斜杠命令是定义在 ``.claude/commands/`` 中的自定义命令。你可以查看其实现代码：
- ``.claude/commands/generate-prp.md`` - 了解如何调研并生成 PRP
- ``.claude/commands/execute-prp.md`` - 了解如何根据 PRP 实现功能

这些命令中的 ``$ARGUMENTS`` 变量会接收你输入在命令名称之后的参数（例如 ``INITIAL.md`` 或 ``PRPs/你的功能名.md``）。

该命令将执行以下操作：
1. 读取你的功能需求
2. 调研代码库中的现有模式
3. 搜索相关文档资料
4. 在 ``PRPs/你的功能名.md`` 中生成一份完整的 PRP

### 4. 执行 PRP

生成后，运行以下命令执行 PRP 以实现你的功能：

```bash
/execute-prp PRPs/your-feature-name.md
```

AI 编程助手将执行以下步骤：
1. 读取 PRP 中的所有上下文信息
2. 制定详细的实施计划
3. 逐步执行并进行验证
4. 运行测试并修复任何问题
5. 确保所有成功标准均已达成

## 如何编写有效的 INITIAL.md 文件

### 核心板块说明

**功能需求（FEATURE）**：具体且全面
- ❌ “构建一个网页爬虫”
- ✅ “使用 BeautifulSoup 构建异步网页爬虫，从电商网站提取产品数据，处理速率限制，并将结果存储至 PostgreSQL”

**示例（EXAMPLES）**：充分利用 ``examples/`` 文件夹
- 将相关的代码模式放入 ``examples/`` 目录中
- 引用需要遵循的具体文件和模式
- 说明哪些方面需要模仿或参考

**文档（DOCUMENTATION）**：包含所有相关资源
- API 文档链接
- 库使用指南
- MCP 服务器文档
- 数据库结构说明

**其他注意事项（OTHER CONSIDERATIONS）**：记录重要细节
- 认证要求
- 速率限制或配额
- 常见陷阱
- 性能要求

## PRP 工作流

### `/generate-prp` 的工作原理

该命令按以下流程执行：

1. **调研阶段**
   - 分析代码库中的现有模式
   - 搜索类似的实现方案
   - 识别需遵循的规范

2. **文档收集**
   - 获取相关的 API 文档
   - 包含库官方文档
   - 补充常见陷阱与特殊注意事项

3. **蓝图生成**
   - 制定分步实施计划
   - 包含验证关卡（检查点）
   - 添加测试要求

4. **质量审查**
   - 评估置信度评分（1-10 分）
   - 确保所有上下文信息均已包含

### `/execute-prp` 的工作原理

1. **加载上下文**：读取完整的 PRP 文件
2. **规划**：使用 TodoWrite 生成详细任务列表
3. **执行**：逐个实现各组件功能
4. **验证**：运行测试与代码检查（linting）
5. **迭代**：修复发现的问题
6. **完成**：确保所有需求均已满足

完整生成示例请参考 ``PRPs/EXAMPLE_multi_agent_prp.md``。

## 有效使用示例

``examples/`` 文件夹对成功至关重要。当 AI 编程助手能够看到可遵循的模式时，其表现会大幅提升。

### 示例中应包含的内容

1. **代码结构模式**
   - 模块组织方式
   - 导入规范
   - 类/函数设计模式

2. **测试模式**
   - 测试文件结构
   - 模拟（Mock）方法
   - 断言风格

3. **集成模式**
   - API 客户端实现
   - 数据库连接方式
   - 认证流程

4. **命令行（CLI）模式**
   - 参数解析
   - 输出格式化
   - 错误处理

### 示例结构

```
examples/
├── README.md           # Explains what each example demonstrates
├── cli.py             # CLI implementation pattern
├── agent/             # Agent architecture patterns
│   ├── agent.py      # Agent creation pattern
│   ├── tools.py      # Tool implementation pattern
│   └── providers.py  # Multi-provider pattern
└── tests/            # Testing patterns
    ├── test_agent.py # Unit test patterns
    └── conftest.py   # Pytest configuration
```

## 最佳实践

### 1. 在 INITIAL.md 中明确表述
- 不要假设 AI 了解你的偏好
- 包含具体的需求与约束条件
- 充分引用示例文件

### 2. 提供全面的示例
- 示例越多，实现效果越好
- 同时展示“应该做”和“不应该做”的内容
- 包含错误处理模式

### 3. 善用验证关卡
- PRP 中包含必须通过的测试命令
- AI 会持续迭代，直到所有验证通过
- 这能确保一次性生成可运行的代码

### 4. 充分利用文档资源
- 包含官方 API 文档
- 添加 MCP 服务器相关资源
- 引用具体的文档章节

### 5. 自定义 CLAUDE.md
- 添加你的项目规范
- 包含特定于项目的规则
- 定义编码标准

## 资源

- [Claude Code 官方文档](https://docs.anthropic.com/en/docs/claude-code)
- [上下文工程最佳实践](https://www.philschmid.de/context-engineering)