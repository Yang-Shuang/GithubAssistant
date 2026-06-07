# skills

开放智能体技能生态系统的命令行工具。

<!-- agent-list:start -->
支持 **OpenCode**、**Claude Code**、**Codex**、**Cursor** 以及 [67 个更多](#supported-agents)。
<!-- agent-list:end -->

[![skills.sh](https://skills.sh/b/vercel-labs/skills)](https://skills.sh/vercel-labs/skills)

## 安装技能

```bash
npx skills add vercel-labs/agent-skills
```

## 不安装即可使用技能

为单个技能生成提示词，或交互式启动受支持的编码智能体：

```bash
npx skills use vercel-labs/agent-skills@nextjs | claude
npx skills use vercel-labs/agent-skills --skill nextjs --agent claude-code
```

`skills use` 解析源的方式与 `skills add` 相同，将选定的技能文件写入临时目录，并在未提供 `--agent` 时仅将生成的提示词输出到 stdout。如果提供了 `--agent`，它将使用生成的提示词交互式启动一个受支持的智能体。

### 源格式

```bash
# GitHub shorthand (owner/repo)
npx skills add vercel-labs/agent-skills

# Full GitHub URL
npx skills add https://github.com/vercel-labs/agent-skills

# Direct path to a skill in a repo
npx skills add https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines

# GitLab URL
npx skills add https://gitlab.com/org/repo

# Any git URL
npx skills add git@github.com:vercel-labs/agent-skills.git

# Local path
npx skills add ./my-local-skills
```

### 选项

| Option                    | Description                                                                                                                                        |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-g, --global`            | 安装到用户目录而非项目目录                                                                                                       |
| `-a, --agent <agents...>` | <!-- agent-names:start -->指定目标智能体（例如 `claude-code`、`codex`）。详见 [受支持的智能体](#supported-agents)<!-- agent-names:end --> |
| `-s, --skill <skills...>` | 按名称安装特定技能（使用 `'*'` 表示所有技能）                                                                                         |
| `-l, --list`              | 列出可用技能而不进行安装                                                                                                           |
| `--copy`                  | 复制文件而非创建指向智能体目录的符号链接（Symlink）                                                                                              |
| `-y, --yes`               | 跳过所有确认提示                                                                                                                      |
| `--all`                   | 无提示将所有技能安装到所有智能体                                                                                                   |

### 示例

```bash
# List skills in a repository
npx skills add vercel-labs/agent-skills --list

# Install specific skills
npx skills add vercel-labs/agent-skills --skill frontend-design --skill skill-creator

# Install a skill with spaces in the name (must be quoted)
npx skills add owner/repo --skill "Convex Best Practices"

# Install to specific agents
npx skills add vercel-labs/agent-skills -a claude-code -a opencode

# Non-interactive installation (CI/CD friendly)
npx skills add vercel-labs/agent-skills --skill frontend-design -g -a claude-code -y

# Install all skills from a repo to all agents
npx skills add vercel-labs/agent-skills --all

# Install all skills to specific agents
npx skills add vercel-labs/agent-skills --skill '*' -a claude-code

# Install specific skills to all agents
npx skills add vercel-labs/agent-skills --agent '*' --skill frontend-design
```

### 安装范围

| Scope       | Flag      | Location            | Use Case                                      |
| ----------- | --------- | ------------------- | --------------------------------------------- |
| **Project** | (default) | `./<agent>/skills/` | 随项目提交，与团队共享 |
| **Global**  | `-g`      | `~/<agent>/skills/` | 在所有项目中可用                 |

### 安装方式

交互式安装时，你可以选择以下两种方式：

| Method                    | Description                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------- |
| **Symlink**（推荐）       | 从每个智能体创建指向统一副本的符号链接。单一事实来源，易于更新。 |
| **Copy**                  | 为每个智能体创建独立副本。在不支持符号链接时使用。              |

## 其他命令

| Command                      | Description                                   |
| ---------------------------- | --------------------------------------------- |
| `npx skills use <source>`    | 不安装即可使用单个技能              |
| `npx skills list`            | 列出已安装的技能（别名：`ls`）           |
| `npx skills find [query]`    | 交互式搜索技能或通过关键词查找 |
| `npx skills remove [skills]` | 从智能体中移除已安装的技能           |
| `npx skills update [skills]` | 将已安装的技能更新到最新版本    |
| `npx skills init [name]`     | 创建新的 SKILL.md 模板                |

### `skills list`

列出所有已安装的技能。类似于 `npm ls`。

```bash
# List all installed skills (project and global)
npx skills list

# List only global skills
npx skills ls -g

# Filter by specific agents
npx skills ls -a claude-code -a cursor
```

### `skills find`

交互式搜索技能或通过关键词查找。

```bash
# Interactive search (fzf-style)
npx skills find

# Search by keyword
npx skills find typescript
```

### `skills update`

```bash
# Update all skills (interactive scope prompt)
npx skills update

# Update a single skill by name
npx skills update my-skill

# Update multiple specific skills
npx skills update frontend-design web-design-guidelines

# Update only global or project skills
npx skills update -g
npx skills update -p

# Non-interactive (auto-detects scope: project if in a project, else global)
npx skills update -y
```

| Option          | Description                                                               |
| --------------- | ------------------------------------------------------------------------- |
| `-g, --global`  | 仅更新全局技能                                                 |
| `-p, --project` | 仅更新项目技能                                                |
| `-y, --yes`     | 跳过范围提示（自动检测：如果在项目目录中则为项目，否则为全局） |
| `[skills...]`   | 按名称更新特定技能而非全部                             |

### `skills init`

```bash
# Create SKILL.md in current directory
npx skills init

# Create a new skill in a subdirectory
npx skills init my-skill
```

### `skills remove`

从智能体中移除已安装的技能。

```bash
# Remove interactively (select from installed skills)
npx skills remove

# Remove specific skill by name
npx skills remove web-design-guidelines

# Remove multiple skills
npx skills remove frontend-design web-design-guidelines

# Remove from global scope
npx skills remove --global web-design-guidelines

# Remove from specific agents only
npx skills remove --agent claude-code cursor my-skill

# Remove all installed skills without confirmation
npx skills remove --all

# Remove all skills from a specific agent
npx skills remove --skill '*' -a cursor

# Remove a specific skill from all agents
npx skills remove my-skill --agent '*'

# Use 'rm' alias
npx skills rm my-skill
```

| Option         | Description                                      |
| -------------- | ------------------------------------------------ |
| `-g, --global` | 从全局范围（~/）移除而非项目 |
| `-a, --agent`  | 从特定智能体移除（使用 `'*'` 表示全部）  |
| `-s, --skill`  | 指定要移除的技能（使用 `'*'` 表示全部）     |
| `-y, --yes`    | 跳过确认提示                        |
| `--all`        | `--skill '*' --agent '*' -y` 的简写       |

## 什么是智能体技能？

智能体技能是可复用的指令集，用于扩展你的编码智能体的功能。它们定义在 `SKILL.md` 文件中，包含带有 `name`（名称）和 `description`（描述）的 YAML frontmatter（文件头）。

技能让智能体能够执行以下专业任务：

- 从 git 历史记录生成发布说明
- 遵循团队规范创建 Pull Request（PR）
- 与外部工具集成（如 Linear、Notion 等）

在 **[skills.sh](https://skills.sh)** 发现更多技能。

## 受支持的智能体

技能可安装到以下任意智能体：

<!-- supported-agents:start -->
| 智能体 | `--agent` | Project Path | Global Path |
|-------|-----------|--------------|-------------|
| AiderDesk | `aider-desk` | `.aider-desk/skills/` | `~/.aider-desk/skills/` |
| Amp, Replit, Universal | `amp`, `replit`, `universal` | `.agents/skills/` | `~/.config/agents/skills/` |
| Antigravity | `antigravity` | `.agents/skills/` | `~/.gemini/antigravity/skills/` |
| Antigravity CLI | `antigravity-cli` | `.agents/skills/` | `~/.gemini/antigravity-cli/skills/` |
| AstrBot | `astrbot` | `data/skills/` | `~/.astrbot/data/skills/` |
| Autohand Code CLI | `autohand-code` | `.autohand/skills/` | `~/.autohand/skills/` |
| Augment | `augment` | `.augment/skills/` | `~/.augment/skills/` |
| IBM Bob | `bob` | `.bob/skills/` | `~/.bob/skills/` |
| Claude Code | `claude-code` | `.claude/skills/` | `~/.claude/skills/` |
| OpenClaw | `openclaw` | `skills/` | `~/.openclaw/skills/` |
| Cline, Dexto, Kimi Code CLI, Loaf, Warp, Zed | `cline`, `dexto`, `kimi-code-cli`, `loaf`, `warp`, `zed` | `.agents/skills/` | `~/.agents/skills/` |
| CodeArts Agent | `codearts-agent` | `.codeartsdoer/skills/` | `~/.codeartsdoer/skills/` |
| CodeBuddy | `codebuddy` | `.codebuddy/skills/` | `~/.codebuddy/skills/` |
| Codemaker | `codemaker` | `.codemaker/skills/` | `~/.codemaker/skills/` |
| Code Studio | `codestudio` | `.codestudio/skills/` | `~/.codestudio/skills/` |
| Codex | `codex` | `.agents/skills/` | `~/.codex/skills/` |
| Command Code | `command-code` | `.commandcode/skills/` | `~/.commandcode/skills/` |
| Continue | `continue` | `.continue/skills/` | `~/.continue/skills/` |
| Cortex Code | `cortex` | `.cortex/skills/` | `~/.snowflake/cortex/skills/` |
| Crush | `crush` | `.crush/skills/` | `~/.config/crush/skills/` |
| Cursor | `cursor` | `.agents/skills/` | `~/.cursor/skills/` |
| Deep Agents | `deepagents` | `.agents/skills/` | `~/.deepagents/agent/skills/` |
| Devin for Terminal | `devin` | `.devin/skills/` | `~/.config/devin/skills/` |
| Droid | `droid` | `.factory/skills/` | `~/.factory/skills/` |
| Firebender | `firebender` | `.agents/skills/` | `~/.firebender/skills/` |
| ForgeCode | `forgecode` | `.forge/skills/` | `~/.forge/skills/` |
| Gemini CLI | `gemini-cli` | `.agents/skills/` | `~/.gemini/skills/` |
| GitHub Copilot | `github-copilot` | `.agents/skills/` | `~/.copilot/skills/` |
| Goose | `goose` | `.goose/skills/` | `~/.config/goose/skills/` |
| Hermes Agent | `hermes-agent` | `.hermes/skills/` | `~/.hermes/skills/` |
| inference.sh | `inference-sh` | `.inferencesh/skills/` | `~/.inferencesh/skills/` |
| Jazz | `jazz` | `.jazz/skills/` | `~/.jazz/skills/` |
| Junie | `junie` | `.junie/skills/` | `~/.junie/skills/` |
| iFlow CLI | `iflow-cli` | `.iflow/skills/` | `~/.iflow/skills/` |
| Kilo Code | `kilo` | `.kilocode/skills/` | `~/.kilocode/skills/` |
| Kiro CLI | `kiro-cli` | `.kiro/skills/` | `~/.kiro/skills/` |
| Kode | `kode` | `.kode/skills/` | `~/.kode/skills/` |
| Lingma | `lingma` | `.lingma/skills/` | `~/.lingma/skills/` |
| MCPJam | `mcpjam` | `.mcpjam/skills/` | `~/.mcpjam/skills/` |
| Mistral Vibe | `mistral-vibe` | `.vibe/skills/` | `~/.vibe/skills/` |
| Moxby | `moxby` | `.moxby/skills/` | `~/.moxby/skills/` |
| Mux | `mux` | `.mux/skills/` | `~/.mux/skills/` |
| OpenCode | `opencode` | `.agents/skills/` | `~/.config/opencode/skills/` |
| OpenHands | `openhands` | `.openhands/skills/` | `~/.openhands/skills/` |
| Ona | `ona` | `.ona/skills/` | `~/.ona/skills/` |
| Pi | `pi` | `.pi/skills/` | `~/.pi/agent/skills/` |
| Qoder | `qoder` | `.qoder/skills/` | `~/.qoder/skills/` |
| Qoder CN | `qoder-cn` | `.qoder/skills/` | `~/.qoder-cn/skills/` |
| Qwen Code | `qwen-code` | `.qwen/skills/` | `~/.qwen/skills/` |
| Reasonix | `reasonix` | `.reasonix/skills/` | `~/.reasonix/skills/` |
| Rovo Dev | `rovodev` | `.rovodev/skills/` | `~/.rovodev/skills/` |
| Roo Code | `roo` | `.roo/skills/` | `~/.roo/skills/` |
| Tabnine CLI | `tabnine-cli` | `.tabnine/agent/skills/` | `~/.tabnine/agent/skills/` |
| Terramind | `terramind` | `.terramind/skills/` | `~/.terramind/skills/` |
| Tinycloud | `tinycloud` | `.tinycloud/skills/` | `~/.tinycloud/skills/` |
| Trae | `trae` | `.trae/skills/` | `~/.trae/skills/` |
| Trae CN | `trae-cn` | `.trae/skills/` | `~/.trae-cn/skills/` |
| Windsurf | `windsurf` | `.windsurf/skills/` | `~/.codeium/windsurf/skills/` |
| Zencoder, Zenflow | `zencoder`, `zenflow` | `.zencoder/skills/` | `~/.zencoder/skills/` |
| Neovate | `neovate` | `.neovate/skills/` | `~/.neovate/skills/` |
| Pochi | `pochi` | `.pochi/skills/` | `~/.pochi/skills/` |
| PromptScript | `promptscript` | `.agents/skills/` | N/A (project-only) |
| AdaL | `adal` | `.adal/skills/` | `~/.adal/skills/` |
<!-- supported-agents:end -->

> [!NOTE]
> **Kiro CLI 用户：**默认智能体会自动从 `.kiro/skills/` 和 `~/.kiro/skills/` 加载技能——无需任何配置。如果你使用**自定义智能体**，请将技能添加到其 `.kiro/agents/<agent>.json` 中的 `resources` 字段：
>
> ```json
> {
>   "resources": ["skill://.kiro/skills/**/SKILL.md"]
> }
> ```

该命令行工具会自动检测你已安装的编码智能体。如果未检测到任何智能体，系统将提示你选择要安装到的目标智能体。

## 创建技能

技能是包含带有 YAML frontmatter（文件头）的 `SKILL.md` 文件的目录：

```markdown
---
name: my-skill
description: What this skill does and when to use it
---

# My Skill

Instructions for the agent to follow when this skill is activated.

## When to Use

Describe the scenarios where this skill should be used.

## Steps

1. First, do this
2. Then, do that
```

### 必填字段

- `name`：唯一标识符（小写字母，允许使用连字符）
- `description`：对技能功能的简要说明

### 可选字段

- `metadata.internal`：设置为 `true` 可在常规发现中隐藏该技能。内部技能仅在设置 `INSTALL_INTERNAL_SKILLS=1` 时可见且可安装。适用于开发中的技能或仅用于内部工具的技能。

```markdown
---
name: my-internal-skill
description: An internal skill not shown by default
metadata:
  internal: true
---
```

### 技能发现机制

命令行工具会在仓库中按以下位置搜索技能。每个技能容器目录会向下一层遍历以查找常见的扁平布局（`skills/<name>/SKILL.md`），并向外多一层遍历以查找分类布局（`skills/<category>/<name>/SKILL.md`）。在较浅层级发现的 `SKILL.md` 将覆盖其下方的嵌套文件。使用 `--full-depth` 还可发现这些容器目录之外的 `SKILL.md` 文件（例如位于 `examples/` 或 `tests/` 下）。

<!-- skill-discovery:start -->
- Root directory (if it contains `SKILL.md`)
- `skills/`
- `skills/.curated/`
- `skills/.experimental/`
- `skills/.system/`
- `.aider-desk/skills/`
- `.agents/skills/`
- `data/skills/`
- `.autohand/skills/`
- `.augment/skills/`
- `.bob/skills/`
- `.claude/skills/`
- `.codeartsdoer/skills/`
- `.codebuddy/skills/`
- `.codemaker/skills/`
- `.codestudio/skills/`
- `.commandcode/skills/`
- `.continue/skills/`
- `.cortex/skills/`
- `.crush/skills/`
- `.devin/skills/`
- `.factory/skills/`
- `.forge/skills/`
- `.goose/skills/`
- `.hermes/skills/`
- `.inferencesh/skills/`
- `.jazz/skills/`
- `.junie/skills/`
- `.iflow/skills/`
- `.kilocode/skills/`
- `.kiro/skills/`
- `.kode/skills/`
- `.lingma/skills/`
- `.mcpjam/skills/`
- `.vibe/skills/`
- `.moxby/skills/`
- `.mux/skills/`
- `.openhands/skills/`
- `.ona/skills/`
- `.pi/skills/`
- `.qoder/skills/`
- `.qwen/skills/`
- `.reasonix/skills/`
- `.rovodev/skills/`
- `.roo/skills/`
- `.tabnine/agent/skills/`
- `.terramind/skills/`
- `.tinycloud/skills/`
- `.trae/skills/`
- `.windsurf/skills/`
- `.zencoder/skills/`
- `.neovate/skills/`
- `.pochi/skills/`
- `.adal/skills/`
<!-- skill-discovery:end -->

### 插件清单发现机制

如果存在 `.claude-plugin/marketplace.json` 或 `.claude-plugin/plugin.json`，其中声明的技能也会被发现：

```json
// .claude-plugin/marketplace.json
{
  "metadata": { "pluginRoot": "./plugins" },
  "plugins": [
    {
      "name": "my-plugin",
      "source": "my-plugin",
      "skills": ["./skills/review", "./skills/test"]
    }
  ]
}
```

这实现了对 [Claude Code 插件市场](https://code.claude.com/docs/en/plugin-marketplaces)生态系统的兼容。在清单中声明的技能路径会按其声明的深度进行搜索，不受上述深度遍历规则的影响。

如果在标准位置未找到任何技能，将执行递归搜索。

## 兼容性

由于遵循共享的 [智能体技能规范](https://agentskills.io)，技能在不同智能体之间通常具有兼容性。但部分功能可能因智能体而异：

| Feature         | OpenCode | OpenHands | Claude Code | Cline | CodeBuddy | Codex | Command Code | Kiro CLI | Cursor | Antigravity | Roo Code | Github Copilot | Amp | OpenClaw | Neovate | Pi  | Qoder | Zencoder |
| --------------- | -------- | --------- | ----------- | ----- | --------- | ----- | ------------ | -------- | ------ | ----------- | -------- | -------------- | --- | -------- | ------- | --- | ----- | -------- |
| Basic skills    | Yes      | Yes       | Yes         | Yes   | Yes       | Yes   | Yes          | Yes      | Yes    | Yes         | Yes      | Yes            | Yes | Yes      | Yes     | Yes | Yes   | Yes      |
| `allowed-tools` | Yes      | Yes       | Yes         | Yes   | Yes       | Yes   | Yes          | No       | Yes    | Yes         | Yes      | Yes            | Yes | Yes      | Yes     | Yes | Yes   | No       |
| `context: fork` | No       | No        | Yes         | No    | No        | No    | No           | No       | No     | No          | No       | No             | No  | No       | No      | No  | No    | No       |
| Hooks           | No       | No        | Yes         | Yes   | No        | No    | No           | Yes      | No     | No          | No       | No             | No  | No       | No      | No  | No    | No       |

## 故障排除

### “未找到任何技能”

确保仓库中包含有效的 `SKILL.md` 文件，且 frontmatter（文件头）中同时包含 `name` 和 `description`。

### 智能体无法加载技能

- 确认技能已安装到正确的路径
- 查阅该智能体的文档以了解技能加载要求
- 确保 `SKILL.md` 的 frontmatter 是有效的 YAML 格式

### 权限错误

请确保你对目标目录具有写入权限。

## 环境变量

| Variable                  | Description                                                                |
| ------------------------- | -------------------------------------------------------------------------- |
| `INSTALL_INTERNAL_SKILLS` | 设置为 `1` 或 `true` 以显示并安装标记为 `internal: true` 的技能 |
| `DISABLE_TELEMETRY`       | 设置此项可禁用匿名使用数据收集（Telemetry）                                   |
| `DO_NOT_TRACK`            | 禁用遥测功能的替代方式                                       |

```bash
# Install internal skills
INSTALL_INTERNAL_SKILLS=1 npx skills add vercel-labs/agent-skills --list
```

## 遥测（Telemetry）

该命令行工具会收集匿名使用数据以帮助我们改进产品。不会收集任何个人信息。

在 CI/CD 环境中将自动禁用遥测功能。

## 相关链接

- [智能体技能规范](https://agentskills.io)
- [技能目录](https://skills.sh)
- [Amp Skills Documentation](https://ampcode.com/manual#agent-skills)
- [Antigravity Skills Documentation](https://antigravity.google/docs/skills)
- [Factory AI / Droid Skills Documentation](https://docs.factory.ai/cli/configuration/skills)
- [Claude Code Skills Documentation](https://code.claude.com/docs/en/skills)
- [OpenClaw Skills Documentation](https://docs.openclaw.ai/tools/skills)
- [Cline Skills Documentation](https://docs.cline.bot/features/skills)
- [CodeBuddy Skills Documentation](https://www.codebuddy.ai/docs/ide/Features/Skills)
- [Codex Skills Documentation](https://developers.openai.com/codex/skills)
- [Command Code Skills Documentation](https://commandcode.ai/docs/skills)
- [Crush Skills Documentation](https://github.com/charmbracelet/crush?tab=readme-ov-file#agent-skills)
- [Cursor Skills Documentation](https://cursor.com/docs/context/skills)
- [Firebender Skills Documentation](https://docs.firebender.com/multi-agent/skills)
- [Gemini CLI Skills Documentation](https://geminicli.com/docs/cli/skills/)
- [GitHub Copilot Agent Skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)
- [iFlow CLI Skills Documentation](https://platform.iflow.cn/en/cli/examples/skill)
- [Kimi Code CLI Skills Documentation](https://moonshotai.github.io/kimi-code/en/customization/skills)
- [Kiro CLI Skills Documentation](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#skill-resources)
- [Kode Skills Documentation](https://github.com/shareAI-lab/kode/blob/main/docs/skills.md)
- [OpenCode Skills Documentation](https://opencode.ai/docs/skills)
- [Qwen Code Skills Documentation](https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/)
- [OpenHands Skills Documentation](https://docs.openhands.ai/modules/usage/how-to/using-skills)
- [Pi Skills Documentation](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/skills.md)
- [Qoder Skills Documentation](https://docs.qoder.com/cli/Skills)
- [Replit Skills Documentation](https://docs.replit.com/replitai/skills)
- [Roo Code Skills Documentation](https://docs.roocode.com/features/skills)
- [Trae Skills Documentation](https://docs.trae.ai/ide/skills)
- [Vercel Agent Skills Repository](https://github.com/vercel-labs/agent-skills)

## 许可证

MIT