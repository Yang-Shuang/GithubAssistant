# Ralph

![Ralph](ralph.webp)

Ralph 是一个自主 AI Agent 循环，它会反复运行 AI 编程工具（[Amp](https://ampcode.com) 或 [Claude Code](https://docs.anthropic.com/en/docs/claude-code)），直到所有 PRD 条目全部完成。每次迭代都是一个具有干净上下文的全新实例。记忆通过 git 历史记录、`progress.txt` 和 `prd.json` 持久化保存。

基于 [Geoffrey Huntley 的 Ralph 模式](https://ghuntley.com/ralph/)。

[阅读我关于如何使用 Ralph 的深度文章](https://x.com/ryancarson/status/2008548371712135632)

## 前置条件

- 已安装并认证以下任一 AI 编程工具：
  - [Amp CLI](https://ampcode.com)（默认）
  - [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (`npm install -g @anthropic-ai/claude-code`)
- 已安装 `jq`（macOS 上执行 `brew install jq`）
- 项目的 git 仓库

## 设置

### 方式一：复制到你的项目中

将 Ralph 相关文件复制到你的项目中：

```bash
# From your project root
mkdir -p scripts/ralph
cp /path/to/ralph/ralph.sh scripts/ralph/

# Copy the prompt template for your AI tool of choice:
cp /path/to/ralph/prompt.md scripts/ralph/prompt.md    # For Amp
# OR
cp /path/to/ralph/CLAUDE.md scripts/ralph/CLAUDE.md    # For Claude Code

chmod +x scripts/ralph/ralph.sh
```

### 方式二：全局安装 Skills（适用于 Amp）

将 skills 复制到你使用的 Amp 或 Claude 配置中，以便在所有项目中通用：

For AMP
```bash
cp -r skills/prd ~/.config/amp/skills/
cp -r skills/ralph ~/.config/amp/skills/
```

For Claude Code (manual)
```bash
cp -r skills/prd ~/.claude/skills/
cp -r skills/ralph ~/.claude/skills/
```

### 方式三：作为 Claude Code 市场插件使用

将 Ralph 市场添加到 Claude Code：

```bash
/plugin marketplace add snarktank/ralph
```

然后安装 Skills：

```bash
/plugin install ralph-skills@ralph-marketplace
```

安装后可用的 Skills：
- `/prd` - Generate Product Requirements Documents
- `/ralph` - Convert PRDs to prd.json format

当你要求 Claude 执行以下操作时，Skills 会自动触发：
- "create a prd", "write prd for", "plan this feature"
- "convert this prd", "turn into ralph format", "create prd.json"

### 配置 Amp 自动交接（推荐）

添加到 `~/.config/amp/settings.json`：

```json
{
  "amp.experimental.autoHandoff": { "context": 90 }
}
```

这将在上下文窗口满时自动触发交接，使 Ralph 能够处理超出单个上下文窗口的大型 Story（用户故事）。

## 工作流

### 1. 创建 PRD

使用 PRD Skill 生成详细的需求文档：

```
Load the prd skill and create a PRD for [your feature description]
```

回答澄清问题。该 Skill 会将输出保存到 `tasks/prd-[feature-name].md`。

### 2. 将 PRD 转换为 Ralph 格式

使用 Ralph Skill 将 Markdown PRD 转换为 JSON：

```
Load the ralph skill and convert tasks/prd-[feature-name].md to prd.json
```

这将生成 `prd.json`，其中包含为自主执行而结构化的用户故事（User Stories）。

### 3. 运行 Ralph

```bash
# Using Amp (default)
./scripts/ralph/ralph.sh [max_iterations]

# Using Claude Code
./scripts/ralph/ralph.sh --tool claude [max_iterations]
```

默认迭代次数为 10 次。使用 `--tool amp` 或 `--tool claude` 选择你的 AI 编程工具。

Ralph 将执行以下操作：
1. Create a feature branch (from PRD `branchName`)
2. Pick the highest priority story where `passes: false`
3. Implement that single story
4. Run quality checks (typecheck, tests)
5. Commit if checks pass
6. Update `prd.json` to mark story as `passes: true`
7. Append learnings to `progress.txt`
8. Repeat until all stories pass or max iterations reached

## 关键文件

| File | Purpose |
|------|---------|
| `ralph.sh` | The bash loop that spawns fresh AI instances (supports `--tool amp` or `--tool claude`) |
| `prompt.md` | Prompt template for Amp |
| `CLAUDE.md` | Prompt template for Claude Code |
| `prd.json` | User stories with `passes` status (the task list) |
| `prd.json.example` | Example PRD format for reference |
| `progress.txt` | Append-only learnings for future iterations |
| `skills/prd/` | Skill for generating PRDs (works with Amp and Claude Code) |
| `skills/ralph/` | Skill for converting PRDs to JSON (works with Amp and Claude Code) |
| `.claude-plugin/` | Plugin manifest for Claude Code marketplace discovery |
| `flowchart/` | Interactive visualization of how Ralph works |

## 流程图

[![Ralph Flowchart](ralph-flowchart.png)](https://snarktank.github.io/ralph/)

**[查看交互式流程图](https://snarktank.github.io/ralph/)** - 点击逐步查看带动画的说明。

`flowchart/` 目录包含源代码。在本地运行：

```bash
cd flowchart
npm install
npm run dev
```

## 核心概念

### 每次迭代 = 全新上下文

每次迭代都会启动一个具有干净上下文的**新 AI 实例**（Amp 或 Claude Code）。迭代之间的唯一记忆保留为：
- Git history (commits from previous iterations)
- `progress.txt` (learnings and context)
- `prd.json` (which stories are done)

### 控制任务粒度

每个 PRD 条目都应足够小，以便在一个上下文窗口内完成。如果任务过大，LLM 会在结束前耗尽上下文容量，导致生成的代码质量低下。

合适大小的 Story：
- Add a database column and migration
- Add a UI component to an existing page
- Update a server action with new logic
- Add a filter dropdown to a list

过大（需拆分）：
- "Build the entire dashboard"
- "Add authentication"
- "Refactor the API"

### 更新 `AGENTS.md` 至关重要

每次迭代后，Ralph 都会将经验教训更新到相关的 `AGENTS.md` 文件中。这很关键，因为 AI 编程工具会自动读取这些文件，从而使后续迭代（以及未来的你）能够受益于已发现的代码模式、注意事项和约定规范。

建议添加到 `AGENTS.md` 的内容示例：
- Patterns discovered ("this codebase uses X for Y")
- Gotchas ("do not forget to update Z when changing W")
- Useful context ("the settings panel is in component X")

### 反馈循环机制

只有在存在反馈循环的情况下，Ralph 才能正常工作：
- Typecheck catches type errors
- Tests verify behavior
- CI must stay green (broken code compounds across iterations)

### UI Story 的浏览器验证

前端 Story 的验收标准中必须包含 "Verify in browser using dev-browser skill"。Ralph 将使用该 Skill 导航至页面、与 UI 交互，并确认更改已生效。

### 停止条件

当所有 Story 的 `passes` 均为 `true` 时，Ralph 会输出 `<promise>COMPLETE</promise>` 并退出循环。

## 调试

检查当前状态：

```bash
# See which stories are done
cat prd.json | jq '.userStories[] | {id, title, passes}'

# See learnings from previous iterations
cat progress.txt

# Check git history
git log --oneline -10
```

## 自定义 Prompt

将 `prompt.md`（适用于 Amp）或 `CLAUDE.md`（适用于 Claude Code）复制到项目后，请根据你的项目进行自定义：
- Add project-specific quality check commands
- Include codebase conventions
- Add common gotchas for your stack

## 归档机制

当你启动新功能（使用不同的 `branchName`）时，Ralph 会自动将之前的运行记录进行归档。归档文件保存至 `archive/YYYY-MM-DD-feature-name/`。

## 参考资料

- [Geoffrey Huntley's Ralph article](https://ghuntley.com/ralph/)
- [Amp documentation](https://ampcode.com/manual)
- [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code)