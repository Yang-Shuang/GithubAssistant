# Agent 技能

Agent 技能是包含指令、脚本和资源的文件夹，AI 智能体可以从中发现并使用它们来执行特定任务。一次编写，处处可用。

Codex 使用技能来帮助打包功能模块，团队和个人可以以可重复的方式利用这些功能完成特定任务。本仓库收录了可供使用和随 Codex 分发的技能。

了解更多：
- [在 Codex 中使用技能](https://developers.openai.com/codex/skills)
- [在 Codex 中创建自定义技能](https://developers.openai.com/codex/skills/create-skill)
- [Agent Skills 开放标准](https://agentskills.io)

## 安装技能

[`.system`](skills/.system/) 目录中的技能会在最新版本的 Codex 中自动安装。

要安装 [`curated`](skills/.curated/)（精选）或 [`experimental`](skills/.experimental/)（实验性）技能，你可以使用 Codex 内置的 `$skill-installer`。

可通过名称安装精选技能（默认指向 `skills/.curated`）：

```
$skill-installer gh-address-comments
```

对于实验性技能，需指定技能文件夹。例如：

```
$skill-installer install the create-plan skill from the .experimental folder
```

或者提供 GitHub 目录链接：

```
$skill-installer install https://github.com/openai/skills/tree/main/skills/.experimental/create-plan
```

安装技能后，请重启 Codex 以加载新技能。

## 许可证

单个技能的许可证信息可直接在该技能目录下的 `LICENSE.txt` 文件中查看。