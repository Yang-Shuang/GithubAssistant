# Claude Code 插件目录

一个精选的高质量 Claude Code 插件目录。

> **⚠️ 重要提示：** 在安装、更新或使用插件之前，请确保你信任该插件。Anthropic 不控制插件中包含的 MCP 服务器、文件或第三方软件的内容，也无法验证它们是否按预期运行或是否会发生变化。更多信息请参阅各插件的主页。

## 结构

- **`/plugins`** - Anthropic 团队开发和维护的内部插件
- **`/external_plugins`** - 来自合作伙伴与社区的第三方插件

## 安装

你可以通过 Claude Code 的插件系统直接从本市场安装插件。

要安装，请运行 `/plugin install {plugin-name}@claude-plugins-official`

或在 `/plugin > Discover` 中浏览查找该插件。

## 贡献指南

### 内部插件

内部插件由 Anthropic 团队成员开发。参考实现请参阅 `/plugins/example-plugin`。

### 外部插件

第三方合作伙伴可提交插件以加入该市场。外部插件必须符合质量和安全标准方可获批。如需提交新插件，请使用[插件目录提交表单](https://clau.de/plugin-directory-submission)。

## 插件结构

每个插件均遵循以下标准结构：

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json      # Plugin metadata (required)
├── .mcp.json            # MCP server configuration (optional)
├── commands/            # Slash commands (optional)
├── agents/              # Agent definitions (optional)
├── skills/              # Skill definitions (optional)
└── README.md            # Documentation
```

## 技能包（Skill-bundle）插件

当插件的源码仓库包含技能文件（即 `SKILL.md`），但未提供 `.claude-plugin/plugin.json` 清单时，市场条目可以直接使用 `strict: false` 和显式的 `skills` 数组来声明这些技能。

```json
{
  "name": "example-bundle",
  "description": "Brief description of the bundled skills.",
  "author": { "name": "Author Name" },
  "category": "development",
  "source": {
    "source": "git-subdir",
    "url": "https://github.com/example-org/sdk.git",
    "path": "packages/agent-skills",
    "ref": "main",
    "sha": "<commit sha>"
  },
  "strict": false,
  "skills": [
    "./skill-a",
    "./skill-b",
    "./skill-c"
  ],
  "homepage": "https://github.com/example-org/sdk"
}
```

`skills` 中的每个路径均相对于 `source.path`，并指向包含 `SKILL.md` 的目录。路径可深入多层——例如，`["./libA/skill-1", "./libB/skill-2"]` 会跨多个库子目录暴露精选的子集。在 Claude Code 中，每个技能都会以 `<plugin-name>:<skill-name>` 的形式进行注册。

有关底层架构（Schema）的详细信息，请参阅市场文档中的[严格模式（Strict mode）](https://code.claude.com/docs/en/plugin-marketplaces)。

## 许可证

具体许可证信息请参阅各个关联插件。

## 文档

如需了解开发 Claude Code 插件的更多信息，请参阅[官方文档](https://code.claude.com/docs/en/plugins)。