# 智能体插件市场

> 开箱即用的智能体工作流构建模块：**84 个插件**、**192 个智能体（agents）**、> **156 项技能（skills）**、**102 条命令（commands）** —— 专为 Claude Code 打造，并可通过单一 Markdown 源码原生支持 OpenAI Codex CLI、Cursor、OpenCode、Gemini CLI 和 GitHub Copilot。

[![Claude Code](https://img.shields.io/badge/Claude%20Code-native-blueviolet)](#claude-code) [![Codex CLI](https://img.shields.io/badge/Codex%20CLI-supported-black)](docs/harnesses.md) [![Cursor](https://img.shields.io/badge/Cursor-supported-purple)](docs/harnesses.md) [![OpenCode](https://img.shields.io/badge/OpenCode-supported-green)](docs/harnesses.md) [![Gemini CLI](https://img.shields.io/badge/Gemini%20CLI-supported-blue)](GEMINI.md) [![Copilot](https://img.shields.io/badge/Copilot-supported-lightgrey)](docs/harnesses.md)

> [!NOTE]
> 单一事实来源（`plugins/`），适配五种运行环境（harness）。每个环境都会生成符合其原生规范的产物，而非最低兼容性的通用翻译。
> 能力矩阵详见 [docs/harnesses.md](docs/harnesses.md)。

## 快速开始

选择你的运行环境（harness）：

### Claude Code

```bash
/plugin marketplace add wshobson/agents
/plugin install python-development          # or any of 84 plugins
```

[→ 查看完整的 Claude Code 安装指南、故障排除与插件目录](docs/usage.md)

### Codex CLI · Cursor · OpenCode · Gemini CLI · Copilot

Codex 和 Cursor 可通过已提交的注册表（指向源文件 `plugins/`）直接安装：

```bash
npx codex-marketplace add wshobson/agents        # Codex; then install individual plugins
# Cursor: add the marketplace, then `/plugin install <name>` (reads .cursor-plugin/ + source)
```

Gemini 和 OpenCode 需通过克隆仓库并执行生成命令安装（转换后的目录结构已被 `.gitignore`）：

```bash
gh repo clone wshobson/agents ~/agents && cd ~/agents
make generate HARNESS=gemini && gemini extensions install .   # Gemini
make install-opencode                                          # OpenCode (runs generate + symlinks)
```

各环境的具体设置与注意事项：[docs/harnesses.md](docs/harnesses.md)。Gemini 专属配置：[GEMINI.md](GEMINI.md)（Gemini CLI 也会自动加载）。

## 内容概览

| | 数量 | 说明 |
|---|---:|---|
| **插件（Plugins）** | 84 | 细粒度、单一用途的可安装单元（82 个本地 + 2 个通过 git-subdir 引入的外部） |
| **智能体（Agents）** | 192 | 领域专家（涵盖架构、编程语言、基础设施、安全、数据、ML、文档、商业、SEO 等） |
| **技能（Skills）** | 156 | 模块化知识包，支持渐进式加载（激活时按需载入） |
| **命令（Commands）** | 102 | 斜杠命令：项目脚手架生成、安全扫描、测试代码生成、基础设施配置等 |
| **编排器（Orchestrators）** | 16 | 多智能体协同工作流（涵盖全栈开发、安全、ML、事件响应等） |

浏览完整目录：[docs/plugins.md](docs/plugins.md) · [docs/agents.md](docs/agents.md) · [docs/agent-skills.md](docs/agent-skills.md)

## 工作原理

每个插件均保持独立且可组合：智能体、命令和技能会根据目录结构自动发现。**安装某个插件仅将其组件加载到上下文中**，不会引入整个市场的内容。

```
plugins/python-development/
├── .claude-plugin/plugin.json
├── agents/             # 3 Python agents (python-pro, django-pro, fastapi-pro)
├── commands/           # 1 scaffolding command
└── skills/             # 16 specialized skills (async, testing, packaging, …)
```

三层模型策略：

| 层级 | 模型 | 用途 |
|---|---|---|
| 1 | Opus 4.7 | 架构设计、安全审查、代码评审、生产级关键任务 |
| 2 | inherit（继承） | 用户自定义选择——后端、前端、AI/ML、垂直领域专用 |
| 3 | Sonnet   | 文档编写、测试生成、调试排错、API 参考查询 |
| 4 | Haiku    | 快速运维任务、SEO 优化、部署操作、内容生成 |

[→ 查看模型配置详情](docs/agents.md#model-configuration)

## 多运行环境（Multi-Harness）支持

本市场通过单一 Markdown 源码，向五种智能体运行环境分发内容。每个适配器都会生成符合该环境原生规范的产物（而非最低兼容性的通用翻译）：

| 运行环境（Harness） | 生成产物 | 说明 |
|---|---|---|
| **Claude Code** | （事实来源/源文件） | 原生 `marketplace.json` + `plugins/` |
| **Codex CLI** | `.agents/plugins/marketplace.json` + `plugins/*/.codex-plugin/plugin.json`（已提交）；`.codex/skills/`, `.codex/agents/`（gitignore） | 遵守 8 KB 技能容量限制；命令转换为技能 |
| **Cursor** | `.cursor-plugin/`, `.cursor/rules/` | 轻量级市场 + 精选规则；复用 `.claude/` 目录结构 |
| **OpenCode** | `.opencode/agents/`, `.opencode/commands/`, `.opencode/skills/` | `permission:` 块源自 `tools:` 白名单；使用 OpenCode 兼容的技能命名 |
| **Gemini CLI** | `skills/`, `agents/`, `commands/`（TOML） | 原生技能 + 子智能体（符合 2026年4月规范） |
| **Copilot** | `.copilot/agents/`, `.copilot/skills/`, `.copilot/commands/` | Markdown 智能体配置 + SKILL.md 技能文件 + 命令即技能；模型映射至 GPT-5 系列 |

```bash
make generate-all                        # all five
make validate                            # structural checks
make garden                              # drift / dead-link / cap detection
```

Codex 和 Cursor 通过已提交的注册表从源码安装；Gemini 和 OpenCode 需克隆仓库后执行 `make`。

[→ 查看完整能力矩阵与各环境深度指南](docs/harnesses.md)

## 质量评估

[`plugin-eval`](plugins/plugin-eval/) 是一个三层评估框架，用于测量和认证插件/技能的质量：

- **静态分析（Static）** —— 确定性结构检查（<2秒，免费）
- **LLM 裁判（LLM Judge）** —— 跨四个维度的语义评估（约30秒，使用 Haiku + Sonnet）
- **蒙特卡洛模拟（Monte Carlo）** —— 通过 50-100 次模拟运行验证统计可靠性（约2-5分钟）

```bash
uv run plugin-eval score path/to/skill --depth quick
uv run plugin-eval certify path/to/skill
```

[→ PluginEval 框架文档](docs/plugin-eval.md)

## 文档索引

详细说明位于 `docs/` 目录中。建议按以下顺序阅读：

- **[docs/plugins.md](docs/plugins.md)** —— 全部 84 个插件的完整目录
- **[docs/agents.md](docs/agents.md)** —— 按分类列出的所有 192 个智能体
- **[docs/agent-skills.md](docs/agent-skills.md)** —— 支持渐进式加载的 156 项技能详解
- **[docs/usage.md](docs/usage.md)** —— 命令、工作流与使用示例
- **[docs/architecture.md](docs/architecture.md)** —— 架构设计原则
- **[docs/harnesses.md](docs/harnesses.md)** —— 跨运行环境能力矩阵
- **[docs/authoring.md](docs/authoring.md)** —— 可移植内容编写规范
- **[docs/plugin-eval.md](docs/plugin-eval.md)** —— 质量评估框架说明
- **[docs/round-trip-results.md](docs/round-trip-results.md)** —— 真实 CLI 验证用例

Gemini 专属配置：[GEMINI.md](GEMINI.md)。其他所有运行环境的设置、能力差异及注意事项均位于 [docs/harnesses.md](docs/harnesses.md)。

参与贡献：[CONTRIBUTING.md](CONTRIBUTING.md) · 编写指南：[docs/authoring.md](docs/authoring.md)

## 外部记忆集成

[Pensyve](https://github.com/major7apps/pensyve) 作为外部 `git-subdir` 条目包含在市场中，供 Claude Code 使用。Pensyve 同时也为该市场支持的其他运行环境维护着直接的上游集成。

| 运行环境（Harness） | Pensyve 集成方式 |
|---|---|
| Claude Code | 从本市场执行 `/plugin install pensyve`（位于 `integrations/claude-code`） |
| Codex CLI | [integrations/codex-plugin](https://github.com/major7apps/pensyve/tree/main/integrations/codex-plugin) |
| Cursor | [integrations/cursor](https://github.com/major7apps/pensyve/tree/main/integrations/cursor) |
| OpenCode | [integrations/opencode-plugin](https://github.com/major7apps/pensyve/tree/main/integrations/opencode-plugin) |
| Gemini CLI | `gemini extensions install https://github.com/major7apps/pensyve` |
| Copilot | 仓库根目录下的 `.copilot/`，或通过 `make install-copilot` 安装至 `~/.copilot/` |

## 许可证

MIT —— 详见 [LICENSE](LICENSE)。

## Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=wshobson/agents&type=date&legend=top-left)](https://www.star-history.com/#wshobson/agents&type=date&legend=top-left)