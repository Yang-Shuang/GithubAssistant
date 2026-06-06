<div align="center">

# 🚀 SuperClaude Framework

[![Run in Smithery](https://smithery.ai/badge/skills/SuperClaude-Org)](https://smithery.ai/skills?ns=SuperClaude-Org&utm_source=github&utm_medium=badge)


### **将 Claude Code 转变为结构化的开发平台**

<p align="center">
  <a href="https://github.com/hesreallyhim/awesome-claude-code/">
  <img src="https://awesome.re/mentioned-badge-flat.svg" alt="Mentioned in Awesome Claude Code">
  </a>
<a href="https://github.com/SuperClaude-Org/SuperGemini_Framework" target="_blank">
  <img src="https://img.shields.io/badge/Try-SuperGemini_Framework-blue" alt="Try SuperGemini Framework"/>
</a>
<a href="https://github.com/SuperClaude-Org/SuperQwen_Framework" target="_blank">
  <img src="https://img.shields.io/badge/Try-SuperQwen_Framework-orange" alt="Try SuperQwen Framework"/>
</a>
  <img src="https://img.shields.io/badge/version-4.3.0-blue" alt="Version">
  <a href="https://github.com/SuperClaude-Org/SuperClaude_Framework/actions/workflows/test.yml">
    <img src="https://github.com/SuperClaude-Org/SuperClaude_Framework/actions/workflows/test.yml/badge.svg" alt="Tests">
  </a>
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome">
</p>

<p align="center">
  <a href="https://superclaude.netlify.app/">
    <img src="https://img.shields.io/badge/🌐_Visit_Website-blue" alt="Website">
  </a>
  <a href="https://pypi.org/project/superclaude/">
    <img src="https://img.shields.io/pypi/v/SuperClaude.svg?" alt="PyPI">
  </a>
  <a href="https://pepy.tech/projects/superclaude">
    <img src="https://static.pepy.tech/personalized-badge/superclaude?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads" alt="PyPI sats">
  </a>
  <a href="https://www.npmjs.com/package/@bifrost_inc/superclaude">
    <img src="https://img.shields.io/npm/v/@bifrost_inc/superclaude.svg" alt="npm">
  </a>
</p>

<p align="center">
  <a href="README.md">
    <img src="https://img.shields.io/badge/🇺🇸_English-blue" alt="English">
  </a>
  <a href="README-zh.md">
    <img src="https://img.shields.io/badge/🇨🇳_中文-red" alt="中文">
  </a>
  <a href="README-ja.md">
    <img src="https://img.shields.io/badge/🇯🇵_日本語-green" alt="日本語">
  </a>
</p>

<p align="center">
  <a href="#-quick-installation">快速开始</a> •
  <a href="#-support-the-project">支持项目</a> •
  <a href="#-whats-new-in-v4">功能特性</a> •
  <a href="#-documentation">文档中心</a> •
  <a href="#-contributing">贡献指南</a>
</p>

</div>

---

<div align="center">

## 📊 **框架统计**

| **命令数** | **代理（Agent）** | **模式** | **MCP 服务器** |
|:------------:|:----------:|:---------:|:---------------:|
| **30** | **20** | **7** | **8** |
| Slash Commands | 专业 AI | 行为驱动 | 集成扩展 |

涵盖从头脑风暴到部署的完整开发生命周期的 30 个斜杠命令。

</div>

---

<div align="center">

## 🎯 **概述**

SuperClaude 是一个**元编程配置框架**，通过行为指令注入和组件编排，将 Claude Code 转变为一个结构化的开发平台。它借助强大的工具和智能代理（Agent），提供系统化的工作流自动化功能。


## 免责声明

本项目与 Anthropic 无关，也未获得其认可或背书。
Claude Code 是由 [Anthropic](https://www.anthropic.com/) 开发并维护的产品。

## 📖 **面向开发者与贡献者**

**使用 SuperClaude Framework 的核心文档：**

| 文档 | 用途 | 阅读时机 |
|----------|---------|--------------|
| **[PLANNING.md](PLANNING.md)** | 架构、设计原则、绝对规则 | 会话开始时、实施前 |
| **[TASK.md](TASK.md)** | 当前任务、优先级、待办列表 | 每日工作前 |
| **[KNOWLEDGE.md](KNOWLEDGE.md)** | 经验总结、最佳实践、故障排查 | 遇到问题时、学习模式时 |
| **[CONTRIBUTING.md](CONTRIBUTING.md)** | 贡献规范、工作流程 | 提交 PR 前 |
| **[命令参考手册](docs/user-guide/commands.md)** | 全部 30 个 `/sc:*` 命令的完整参考，含语法、示例、工作流与决策指南 | 学习 SuperClaude、选择合适命令时 |

> **💡 进阶提示**：Claude Code 会在会话开始时读取这些文件，以确保开发过程始终符合项目规范并保持高质量。
>
> **📚 初次使用 SuperClaude？** 建议从 [命令参考手册](docs/user-guide/commands.md) 开始——其中包含可视化决策树、详细的命令对比和工作流示例，帮助你快速理解该在何时使用哪些命令。

## ⚡ **快速安装**

> **⚠️ 重要说明**：旧版文档中描述的 TypeScript 插件系统尚未开放（计划于 v5.0 推出）。当前安装请遵循以下步骤进行 v4.x 版本部署。

### **当前稳定版本 (v4.3.0)**

SuperClaude 目前使用斜杠命令（Slash Commands）体系。

**方式一：pipx（推荐）**
```bash
# 从 PyPI 安装
pipx install superclaude

# 安装命令（将安装全部 30 个斜杠命令）
superclaude install

# 安装 MCP 服务器（可选，用于增强功能）
superclaude mcp --list         # 列出可用的 MCP 服务器
superclaude mcp                # 交互式安装
superclaude mcp --servers tavily --servers context7  # 安装指定服务器

# 验证安装
superclaude install --list
superclaude doctor
```

安装完成后，重启 Claude Code 即可使用以下命令：
- `/sc:research` - 深度网页研究（结合 Tavily MCP 增强）
- `/sc:brainstorm` - 结构化头脑风暴
- `/sc:implement` - 代码实现
- `/sc:test` - 测试工作流
- `/sc:pm` - 项目管理
- `/sc` - 显示全部 30 个可用命令

**方式二：从 Git 直接安装**
```bash
# 克隆仓库
git clone https://github.com/SuperClaude-Org/SuperClaude_Framework.git
cd SuperClaude_Framework

# 运行安装脚本
./install.sh
```

### **v5.0 即将推出（开发中）**

我们正在积极开发全新的 TypeScript 插件系统（详见 Issue [#419](https://github.com/SuperClaude-Org/SuperClaude_Framework/issues/419)）。发布后，安装将简化为：

```bash
# 此功能尚未开放
/plugin marketplace add SuperClaude-Org/superclaude-plugin-marketplace
/plugin install superclaude
```

**状态**：开发中。暂无确切发布时间（ETA）。

### **性能增强（可选 MCP 服务器）**

如需实现 **2-3 倍执行速度提升**与 **减少 30-50% Token 消耗**，可选择安装以下 MCP 服务器：

```bash
# 用于性能增强的可选 MCP 服务器（通过 airis-mcp-gateway）：
# - Serena: 代码理解（快 2-3 倍）
# - Sequential: 高效推理（节省 30-50% Token）
# - Tavily: 网页搜索，用于深度研究
# - Context7: 官方文档查询
# - Mindbase: 跨会话语义搜索（可选增强功能）

# 注：错误学习功能可通过内置 ReflexionMemory 直接使用（无需额外安装）
# Mindbase 提供语义搜索增强（需搭配 "recommended" 配置使用）
# MCP 服务器安装指南：https://github.com/agiletec-inc/airis-mcp-gateway
# 详细说明见 docs/mcp/mcp-integration-policy.md
```

**性能对比：**
- **不安装 MCP**：功能完整，标准性能 ✅
- **安装 MCP**：速度提升 2-3 倍，Token 消耗减少 30-50% ⚡

</div>

---

<div align="center">

## 💖 **支持本项目**

> 说实话，维护 SuperClaude 需要投入大量时间和精力。
> 
> *光是 Claude Max 订阅每月就要花费 100 美元用于测试，更不用说花在文档编写、Bug 修复和功能开发上的时间了。*
> *如果你在日常工作中觉得 SuperClaude 很有价值，欢迎考虑支持本项目。*
> *哪怕是一点点赞助也能覆盖基础开销，让开发持续进行下去。*
> 
> 每一位贡献者都很重要，无论是通过代码、反馈还是实际支持。感谢你们成为这个社区的一部分！🙏

<table>
<tr>
<td align="center" width="33%">
  
### ☕ **Ko-fi**
[![Ko-fi](https://img.shields.io/badge/Support_on-Ko--fi-ff5e5b?logo=ko-fi)](https://ko-fi.com/superclaude)

*一次性赞助*

</td>
<td align="center" width="33%">

### 🎯 **Patreon**
[![Patreon](https://img.shields.io/badge/Become_a-Patron-f96854?logo=patreon)](https://patreon.com/superclaude)

*月度赞助*

</td>
<td align="center" width="33%">

### 💜 **GitHub**
[![GitHub Sponsors](https://img.shields.io/badge/GitHub-Sponsor-30363D?logo=github-sponsors)](https://github.com/sponsors/SuperClaude-Org)

*灵活赞助档位*

</td>
</tr>
</table>

### **你的支持将用于：**

| 项目 | 成本/影响 |
|------|-------------|
| 🔬 **Claude Max 测试** | $100/月，用于验证与测试 |
| ⚡ **功能开发** | 新增能力与性能优化 |
| 📚 **文档编写** | 全面指南与示例库 |
| 🤝 **社区支持** | 快速响应问题与提供帮助 |
| 🔧 **MCP 集成** | 测试新服务器连接 |
| 🌐 **基础设施** | 托管与部署成本 |

> **注意**：完全没有压力——无论是否赞助，该项目都会保持开源。知道大家在使用并认可它就已经是很大的动力了！贡献代码、文档或帮忙宣传也同样重要！🙏

</div>

---

<div align="center">

## 🎉 **v4.1 更新内容**

> *版本 4.1 专注于稳定斜杠命令架构、增强代理能力，并全面优化文档体系。*

<table>
<tr>
<td width="50%">

### 🤖 **更智能的代理系统**
**20 个专业领域代理**：
- PM Agent 通过系统化文档记录实现持续学习
- Deep Research 代理支持自主网页研究
- 安全工程师可检测真实漏洞
- 前端架构师深入理解 UI 模式
- 基于上下文的自动协调机制
- 按需调用的领域专业知识

</td>
<td width="50%">

### ⚡ **性能优化**
**更小的框架体积，支撑更大的项目：**
- 减少框架占用空间
- 为代码分配更多上下文窗口
- 支持更长对话轮次
- 启用复杂操作能力

</td>
</tr>
<tr>
<td width="50%">

### 🔧 **MCP 服务器集成**
**8 款强大服务器，CLI 一键安装：**

```bash
# 列出可用的 MCP 服务器
superclaude mcp --list

# 安装指定服务器
superclaude mcp --servers tavily context7

# 交互式安装
superclaude mcp
```

**可用服务器列表：**
- **Tavily** → 核心网页搜索（深度研究）
- **Context7** → 官方文档查询
- **Sequential-Thinking** → 多步推理
- **Serena** → 会话持久化与记忆
- **Playwright** → 跨浏览器自动化
- **Magic** → UI 组件生成
- **Morphllm-Fast-Apply** → 上下文感知代码修改
- **Chrome DevTools** → 性能分析

</td>
<td width="50%">

### 🎯 **行为模式（Behavioral Modes）**
**7 种自适应模式**，适配不同场景：
- **头脑风暴** → 提出关键问题
- **商业评审团** → 多专家战略分析
- **深度研究** → 自主网页调研
- **编排协调** → 高效工具调度
- **Token 优化** → 节省 30-50% 上下文
- **任务管理** → 系统化组织
- **自省模式** → 元认知分析

</td>
</tr>
<tr>
<td width="50%">

### 📚 **文档全面重构**
**面向开发者的完全重写：**
- 真实案例与使用场景
- 常见陷阱记录
- 实用工作流示例
- 更清晰的导航结构

</td>
<td width="50%">

### 🧪 **稳定性增强**
**聚焦可靠性提升：**
- 核心命令 Bug 修复
- 测试覆盖率优化
- 更健壮的错误处理机制
- CI/CD 流水线改进

</td>
</tr>
</table>

</div>

---

<div align="center">

## 🔬 **深度研究能力**

### **与 DR 代理架构对齐的自主网页研究能力**

SuperClaude v4.2 引入了全面的深度研究（Deep Research）功能，支持自主、自适应且智能的网页调研。

<table>
<tr>
<td width="50%">

### 🎯 **自适应规划**
**三种智能策略：**
- **仅规划模式**：针对明确查询直接执行
- **意图规划**：对模糊请求进行澄清确认
- **统一模式**：协作式计划优化（默认）

</td>
<td width="50%">

### 🔄 **多跳推理（Multi-Hop Reasoning）**
**最多支持 5 次迭代搜索：**
- 实体扩展（论文 → 作者 → 作品）
- 概念深化（主题 → 细节 → 案例）
- 时间演进（当前 → 历史）
- 因果链推导（结果 → 原因 → 预防）

</td>
</tr>
<tr>
<td width="50%">

### 📊 **质量评分**
**基于置信度的验证体系：**
- 来源可信度评估（0.0-1.0）
- 覆盖完整性追踪
- 综合连贯性评价
- 最低阈值：0.6，目标值：0.8

</td>
<td width="50%">

### 🧠 **基于案例的学习**
**跨会话智能积累：**
- 模式识别与复用
- 策略随时间持续优化
- 成功查询模板自动保存
- 性能提升追踪记录

</td>
</tr>
</table>

### **研究命令用法**

```bash
# 基础研究（自动匹配深度）
/research "latest AI developments 2024"

# 控制研究深度（通过 TypeScript 选项配置）
/research "quantum computing breakthroughs"  # depth: exhaustive

# 指定策略选择
/research "market analysis"  # strategy: planning-only

# 领域过滤研究（集成 Tavily MCP）
/research "React patterns"  # domains: reactjs.org,github.com
```

### **研究深度等级**

| 深度 | 来源数 | 跳数 | 耗时 | 适用场景 |
|:-----:|:-------:|:----:|:----:|----------|
| **快速（Quick）** | 5-10 | 1 | ~2分钟 | 基础事实、简单查询 |
| **标准（Standard）** | 10-20 | 3 | ~5分钟 | 通用研究（默认） |
| **深度（Deep）** | 20-40 | 4 | ~8分钟 | 全面分析 |
| **详尽（Exhaustive）** | 40+ | 5 | ~10分钟 | 学术级研究 |

### **集成工具编排**

深度研究系统智能协调多个工具：
- **Tavily MCP**：核心网页搜索与信息发现
- **Playwright MCP**：复杂内容提取
- **Sequential MCP**：多步推理与综合
- **Serena MCP**：记忆与学习持久化
- **Context7 MCP**：技术文档查询

</div>

---

<div align="center">

## 📚 **文档中心**

### **SuperClaude 完整指南**

<table>
<tr>
<th align="center">🚀 入门指南</th>
<th align="center">📖 用户手册</th>
<th align="center">🛠️ 开发者资源</th>
<th align="center">📋 参考文档</th>
</tr>
<tr>
<td valign="top">

- 📝 [**快速开始指南**](docs/getting-started/quick-start.md)  
  *快速上手运行*

- 💾 [**安装指南**](docs/getting-started/installation.md)  
  *详细配置说明*

</td>
<td valign="top">

- 🎯 [**斜杠命令**](docs/reference/commands-list.md)
  *按分类整理的全部 30 个命令*

- 🤖 [**代理指南**](docs/user-guide/agents.md)  
  *20 个专业代理详解*

- 🎨 [**行为模式**](docs/user-guide/modes.md)  
  *7 种自适应模式说明*

- 🚩 [**参数标志（Flags）指南**](docs/user-guide/flags.md)  
  *控制运行行为*

- 🔧 [**MCP 服务器**](docs/user-guide/mcp-servers.md)  
  *8 款服务器集成配置*

- 💼 [**会话管理**](docs/user-guide/session-management.md)  
  *状态保存与恢复*

</td>
<td valign="top">

- 🏗️ [**技术架构**](docs/developer-guide/technical-architecture.md)  
  *系统设计细节*

- 💻 [**代码贡献指南**](docs/developer-guide/contributing-code.md)  
  *开发工作流规范*

- 🧪 [**测试与调试**](docs/developer-guide/testing-debugging.md)  
  *质量保证流程*

</td>
<td valign="top">
- 📓 [**示例食谱**](docs/reference/examples-cookbook.md)  
  *真实世界案例集*

- 🔍 [**故障排查**](docs/reference/troubleshooting.md)  
  *常见问题与解决方案*

</td>
</tr>
</table>

</div>

---

<div align="center">

## 🤝 **贡献指南**

### **加入 SuperClaude 社区**

我们欢迎各种形式的贡献！以下是你可以参与的方式：

| 优先级 | 领域 | 说明 |
|:--------:|------|-------------|
| 📝 **高** | 文档优化 | 改进指南、补充示例、修正错别字 |
| 🔧 **高** | MCP 集成 | 添加服务器配置、测试连接功能 |
| 🎯 **中** | 工作流 | 创建命令模式与使用配方（Recipes） |
| 🧪 **中** | 测试验证 | 补充单元测试、验证新功能 |
| 🌐 **低** | 国际化 (i18n) | 将文档翻译为其他语言 |

<p align="center">
  <a href="CONTRIBUTING.md">
    <img src="https://img.shields.io/badge/📖_Read-Contributing_Guide-blue" alt="Contributing Guide">
  </a>
  <a href="https://github.com/SuperClaude-Org/SuperClaude_Framework/graphs/contributors">
    <img src="https://img.shields.io/badge/👥_View-All_Contributors-green" alt="Contributors">
  </a>
</p>

</div>

---

<div align="center">

## ⚖️ **开源许可**

本项目采用 **MIT License** 许可协议 - 详见 [LICENSE](LICENSE) 文件。

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?" alt="MIT License">
</p>

</div>

---

<div align="center">

## ⭐ **星标历史**

<a href="https://www.star-history.com/#SuperClaude-Org/SuperClaude_Framework&Timeline">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=SuperClaude-Org/SuperClaude_Framework&type=Timeline&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=SuperClaude-Org/SuperClaude_Framework&type=Timeline" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=SuperClaude-Org/SuperClaude_Framework&type=Timeline" />
 </picture>
</a>


</div>

---

<div align="center">

### **🚀 由 SuperClaude 社区满怀热情打造**

<p align="center">
  <sub>Made with ❤️ for developers who push boundaries</sub>
</p>

<p align="center">
  <a href="#-superclaude-framework">回到顶部 ↑</a>
</p>

</div>

---

## 📋 **全部 30 个命令**

<details>
<summary><b>点击展开完整命令列表</b></summary>

### 🧠 规划与设计（4）
- `/brainstorm` - 结构化头脑风暴
- `/design` - 系统架构设计
- `/estimate` - 时间与工作量评估
- `/spec-panel` - 需求规格分析

### 💻 开发（5）
- `/implement` - 代码实现
- `/build` - 构建工作流
- `/improve` - 代码优化改进
- `/cleanup` - 重构与清理
- `/explain` - 代码解释说明

### 🧪 测试与质量（4）
- `/test` - 测试用例生成
- `/analyze` - 代码静态分析
- `/troubleshoot` - 调试排错
- `/reflect` - 复盘总结

### 📚 文档（2）
- `/document` - 文档自动生成
- `/help` - 命令帮助查询

### 🔧 版本控制（1）
- `/git` - Git 操作封装

### 📊 项目管理（3）
- `/pm` - 项目统筹管理
- `/task` - 任务跟踪分配
- `/workflow` - 工作流自动化

### 🔍 研究与分析（2）
- `/research` - 深度网页研究
- `/business-panel` - 商业战略分析

### 🎯 实用工具（9）
- `/agent` - AI 代理调度
- `/index-repo` - 仓库索引构建
- `/index` - 索引快捷别名
- `/recommend` - 命令智能推荐
- `/select-tool` - 工具选择匹配
- `/spawn` - 并行任务派发
- `/load` - 加载历史会话
- `/save` - 保存当前状态
- `/sc` - 显示全部命令

[**📖 查看详细命令参考手册 →**](docs/reference/commands-list.md)

</details>