# 受 Karpathy 启发的 Claude Code 指南

> 看看我的新项目 [Multica](https://github.com/multica-ai/multica) —— 一个用于运行和管理具备可复用技能的编程代理（coding agents）的开源平台。
>
> 在 X 上关注我：[https://x.com/jiayuan_jy](https://x.com/jiayuan_jy)

单个 `CLAUDE.md` 文件，用于改善 Claude Code 的行为表现。内容源自 [Andrej Karpathy 的观察](https://x.com/karpathy/status/2015883857489522876)，针对 LLM（大型语言模型）在编程中常见的陷阱。

English | [简体中文](./README.zh.md)

## 存在的问题

来自 Andrej 的帖子：

> “模型会替你做错误的假设，然后盲目执行而不加核实。它们不管理自身的困惑，不寻求澄清，不暴露矛盾之处，不展示权衡取舍，该反驳时也不反驳。”

> “它们非常喜欢过度复杂化代码和 API，使抽象膨胀不清理死代码……明明 100 行就能实现的事，非要写一套超过 1000 行的臃肿架构。”

> “它们有时仍会作为副作用修改或删除其理解不充分的注释和代码，即使这些内容与当前任务无关（orthogonal）。”

## 解决方案

一个文件中包含四项原则，直接针对上述问题：

| 原则 | 解决的问题 |
|-----------|-----------|
| **先思考后编码** | 错误假设、隐藏的困惑、缺失的权衡 |
| **简洁优先** | 过度复杂化、臃肿的抽象 |
| **精准修改** | 无关改动、触碰不该碰的代码 |
| **目标驱动执行** | 通过测试先行和可验证的成功标准来利用能力 |

## 四项原则详解

### 1. 先思考后编码

**不要假设。不要隐藏困惑。明确展示权衡。**

LLM（大型语言模型）经常默默选择一种解释并直接执行。此原则强制进行显式推理：

- **明确陈述假设** —— 如果不确定，请提问而非猜测
- **展示多种解释** —— 存在歧义时不要默默选择一种
- **该反驳时请反驳** —— 如果存在更简单的方法，请直接指出
- **困惑时停止** —— 明确指出不清楚的地方并请求澄清

### 2. 简洁优先

**解决所需的最少代码。不写任何推测性内容。**

对抗过度工程化的倾向：

- 不要添加超出需求的功能
- 不对一次性使用的代码进行抽象
- 不要添加未要求的“灵活性”或“可配置性”
- 不为不可能发生的场景编写错误处理
- 如果 200 行代码能精简到 50 行，就重写它

**检验标准：** 资深工程师会认为这段代码过度复杂吗？如果是，请简化。

### 3. 精准修改（Surgical Changes）

**只触碰必须改动的部分。仅清理你自己造成的混乱。**

编辑现有代码时：

- 不要“优化”相邻的代码、注释或格式
- 不要重构没有问题的部分
- 遵循现有风格，即使你觉得可以写得更好
- 如果发现无关的死代码，请提出说明——但不要删除它

当你的改动产生孤立资源（如未使用的导入/变量）时：

- 仅移除因你改动而不再使用的 import/变量/函数
- 除非明确要求，否则不要删除原本就存在的死代码

**检验标准：** 每一处修改的行都应能直接追溯到用户的请求。

### 4. 目标驱动执行（Goal-Driven Execution）

**定义成功标准。循环验证直到达标。**

将命令式任务转化为可验证的目标：

| 避免这样写... | 转化为... |
|--------------|-----------------|
| “添加验证” | “为无效输入编写测试，然后让测试通过” |
| “修复 bug” | “编写能复现该问题的测试，然后让测试通过” |
| “重构 X” | “确保前后测试均能通过” |

对于多步任务，请简要说明计划：

```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

明确的成功标准能让 LLM 独立循环执行。模糊的标准（如“让它能跑就行”）则需要不断澄清。

## 安装方式

**选项 A：Claude Code 插件（推荐）**

在 Claude Code 内部，首先添加市场仓库：
```
/plugin marketplace add forrestchang/andrej-karpathy-skills
```

然后安装插件：
```
/plugin install andrej-karpathy-skills@karpathy-skills
```

这将把指南作为 Claude Code 插件安装，使该技能在你的所有项目中均可用。

**选项 B：CLAUDE.md（按项目配置）**

新建项目：
```bash
curl -o CLAUDE.md https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md
```

现有项目（追加）：
```bash
echo "" >> CLAUDE.md
curl https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md >> CLAUDE.md
```

## 与 Cursor 配合使用

本仓库包含一个已提交的 Cursor 项目规则（[`.cursor/rules/karpathy-guidelines.mdc`](.cursor/rules/karpathy-guidelines.mdc)），以便你在 Cursor 中打开该项目时应用相同的指南。有关设置、在其他项目中使用该规则以及其与 Claude Code 的关系，请参阅 **[CURSOR.md](CURSOR.md)**。

## 核心洞察

来自 Andrej：

> “LLM（大型语言模型）在循环执行直至达成特定目标方面表现出色……不要告诉它具体怎么做，给它成功标准，然后看它自己发挥。”

“目标驱动执行”原则正是对此的总结：将命令式指令转化为带有验证循环的声明式目标。

## 如何判断是否生效

如果你观察到以下现象，说明这些指南正在起作用：

- **Diff（差异）中不必要的改动减少** —— 仅出现请求的修改
- **因过度复杂化导致的重写次数减少** —— 代码首次即保持简洁
- **澄清性问题出现在实现之前** —— 而非出错之后
- **PR（Pull Request）干净、精简** —— 无顺手重构或所谓的“优化”

## 自定义配置

这些指南设计为可与项目特定说明合并使用。你可以将它们添加到现有的 `CLAUDE.md` 中，或新建一个文件。

针对项目特定的规则，可添加如下章节：

```markdown
## Project-Specific Guidelines

- Use TypeScript strict mode
- All API endpoints must have tests
- Follow the existing error handling patterns in `src/utils/errors.ts`
```

## 权衡说明

这些指南倾向于**谨慎而非速度**。对于琐碎任务（如简单的拼写错误修正、明显的一行代码修改），请自行判断——并非每次改动都需要严格遵循所有步骤。

其目标是减少非简单工作中的昂贵失误，而非拖慢基础任务的进度。

## 许可证

MIT