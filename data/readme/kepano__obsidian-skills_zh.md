适用于 Obsidian 的 Agent 技能。

这些技能遵循 [Agent Skills 规范](https://agentskills.io/specification)，因此可与任何兼容该规范的 Agent（包括 Claude Code 和 Codex CLI）配合使用。

## 安装

### Marketplace

```
/plugin marketplace add kepano/obsidian-skills
/plugin install obsidian@obsidian-skills
```

### npx skills

```
npx skills add git@github.com:kepano/obsidian-skills.git
```

如果不希望使用 SSH，也可以改用 HTTPS：

```
npx skills add https://github.com/kepano/obsidian-skills
```

### 手动安装

#### Claude Code

将此仓库的内容添加到你的 Obsidian 库（vault）根目录下的 `/.claude` 文件夹中（或者你与 Claude Code 配合使用的任意文件夹）。更多详情请参阅 [官方 Claude Skills 文档](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)。

#### Codex CLI

将 `skills/` 目录复制到你的 Codex 技能路径中（通常为 `~/.codex/skills`）。标准技能格式请参阅 [Agent Skills 规范](https://agentskills.io/specification)。

#### OpenCode

将整个仓库克隆到 OpenCode 的技能目录（`~/.opencode/skills/`）中：

```sh
git clone https://github.com/kepano/obsidian-skills.git ~/.opencode/skills/obsidian-skills
```

请勿仅复制内部的 `skills/` 文件夹，请克隆完整仓库，以确保目录结构为 `~/.opencode/skills/obsidian-skills/skills/<skill-name>/SKILL.md`。

OpenCode 会自动发现 `~/.opencode/skills/` 下的所有 `SKILL.md` 文件。无需修改 `opencode.json` 或任何配置文件。重启 OpenCode 后即可使用这些技能。

## 技能列表

| Skill | Description |
|-------|-------------|
| [obsidian-markdown](skills/obsidian-markdown) | 创建和编辑包含 Wiki 链接、嵌入内容（embeds）、提示块（callouts）、页面属性（properties）及其他 Obsidian 专属语法的 [Obsidian Flavored Markdown](https://help.obsidian.md/obsidian-flavored-markdown) (`.md`) |
| [obsidian-bases](skills/obsidian-bases) | 创建和编辑包含视图、筛选器、公式及摘要的 [Obsidian Bases](https://help.obsidian.md/bases/syntax) (`.base`) |
| [json-canvas](skills/json-canvas) | 创建和编辑包含节点（nodes）、边（edges）、分组（groups）及连接（connections）的 [JSON Canvas](https://jsoncanvas.org/) 文件（`.canvas`） |
| [obsidian-cli](skills/obsidian-cli) | 通过 [Obsidian CLI](https://help.obsidian.md/cli) 与 Obsidian 库进行交互，包括插件和主题开发 |
| [defuddle](skills/defuddle) | 使用 [Defuddle](https://github.com/kepano/defuddle-cli) 从网页中提取纯净的 Markdown，去除冗余内容以节省 Token |