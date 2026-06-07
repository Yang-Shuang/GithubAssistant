<a href="https://github.com/VoltAgent/voltagent">
<img width="1500" height="500" alt="Group 32" src="https://github.com/user-attachments/assets/55b97c47-8506-4be0-b18f-f5384d063cbb" />
</a>

<br />
<br/>

<div align="center">
    <strong>涵盖 10 大类别的 154+ 个 Claude Code 子智能体（Subagent）精选合集。</strong>
    <br />
    <br />
</div>

<div align="center">

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Subagent Count](https://img.shields.io/badge/subagents-154-blue?style=classic)
[![Last Update](https://img.shields.io/github/last-commit/VoltAgent/awesome-claude-code-subagents?label=Last%20update&style=classic)](https://github.com/VoltAgent/awesome-claude-code-subagents)
[![Discord](https://img.shields.io/discord/1361559153780195478.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://s.voltagent.dev/discord)




</div>



# Awesome Claude Code Subagents 

本仓库是 Claude Code 子智能体（Subagent）的权威合集，这些是经过专门设计的 AI 助手，旨在处理特定的开发任务。

## Installation

### As Claude Code Plugin (Recommended)

```bash
claude plugin marketplace add VoltAgent/awesome-claude-code-subagents
claude plugin install <plugin-name>
```

Examples:
```bash
claude plugin install voltagent-lang    # Language specialists
claude plugin install voltagent-infra   # Infrastructure & DevOps
```

请参阅下方的 [Categories](#-categories) 查看所有可用插件。

> **Note**: The `voltagent-meta` orchestration agents work best when other categories installed.

### Option 1: Manual Installation

1. Clone this repository
2. Copy desired agent files to:
   - `~/.claude/agents/` for global access
   - `.claude/agents/` for project-specific use
3. Customize based on your project requirements

### Option 2: Interactive Installer
```bash
git clone https://github.com/VoltAgent/awesome-claude-code-subagents.git
cd awesome-claude-code-subagents
./install-agents.sh
```
This interactive script lets you browse categories, select agents, and install/uninstall them with a single command.

### Option 3: Standalone Installer (no clone required)
```bash
curl -sO https://raw.githubusercontent.com/VoltAgent/awesome-claude-code-subagents/main/install-agents.sh
chmod +x install-agents.sh
./install-agents.sh
```
Downloads agents directly from GitHub without cloning the repository. Requires `curl`.

### Option 4: Agent Installer (use Claude Code to install agents)
```bash
curl -s https://raw.githubusercontent.com/VoltAgent/awesome-claude-code-subagents/main/categories/09-meta-orchestration/agent-installer.md -o ~/.claude/agents/agent-installer.md
```
Then in Claude Code: "Use the agent-installer to show me available categories" or "Find PHP agents and install php-pro globally".

## Ecosystem Tools

用于构建 AI 智能体的工具、平台和服务。

 - 如果你正在使用 TypeScript 构建 AI 智能体，VoltAgent 开箱即用地提供了工具调用（tool use）、记忆机制和多智能体协调功能。

    <a href="https://github.com/VoltAgent/voltagent">
    <img height="80" alt="voltagent-banner" src="https://github.com/user-attachments/assets/7196f50b-ca98-494c-8aa0-11e111c49f96" />
    </a>
<br/>

<div align="center">

<table>
<tr>
<td align="center" width="100%">
<h4>👉 你可以在这里展示你的产品，触达使用 AI 编程智能体（如 Claude Code、Codex、Gemini 等）的开发者。</h4>
     
<a href="https://sponsors.voltagent.dev/#awesome-claude-code-subagents"><img src="https://img.shields.io/badge/📩_Become_a_Sponsor-Contact_Us-blue?style=for-the-badge&logoColor=white" alt="Become a Sponsor" /></a>

</td>
</tr>
</table>

</div>


## 📚 Categories

### [01. Core Development](categories/01-core-development/)
**Plugin:** `voltagent-core-dev`

适用于日常编码任务的核心开发子智能体。

- [**api-designer**](categories/01-core-development/api-designer.md) - REST 和 GraphQL API 架构师
- [**backend-developer**](categories/01-core-development/backend-developer.md) - 可扩展 API 的服务器端专家
- [**design-bridge**](categories/01-core-development/design-bridge.md) - 设计稿到智能体的翻译器
- [**electron-pro**](categories/01-core-development/electron-pro.md) - 桌面应用专家
- [**frontend-developer**](categories/01-core-development/frontend-developer.md) - React、Vue 和 Angular 的 UI/UX 专家
- [**fullstack-developer**](categories/01-core-development/fullstack-developer.md) - 端到端功能开发
- [**graphql-architect**](categories/01-core-development/graphql-architect.md) - GraphQL 架构与联邦（Federation）专家
- [**microservices-architect**](categories/01-core-development/microservices-architect.md) - 分布式系统设计师
- [**mobile-developer**](categories/01-core-development/mobile-developer.md) - 跨平台移动端专家
- [**ui-designer**](categories/01-core-development/ui-designer.md) - 视觉设计与交互专家
- [**websocket-engineer**](categories/01-core-development/websocket-engineer.md) - 实时通信专家

### [02. Language Specialists](categories/02-language-specialists/)
**Plugin:** `voltagent-lang`

具备深厚框架知识的特定语言专家。
- [**typescript-pro**](categories/02-language-specialists/typescript-pro.md) - TypeScript 专家
- [**sql-pro**](categories/02-language-specialists/sql-pro.md) - 数据库查询专家
- [**swift-expert**](categories/02-language-specialists/swift-expert.md) - iOS 和 macOS 专家
- [**vue-expert**](categories/02-language-specialists/vue-expert.md) - Vue 3 Composition API 专家
- [**angular-architect**](categories/02-language-specialists/angular-architect.md) - Angular 15+ 企业级架构模式专家
- [**cpp-pro**](categories/02-language-specialists/cpp-pro.md) - C++ 性能优化专家
- [**csharp-developer**](categories=02-language-specialists/csharp-developer.md) - .NET 生态专家
- [**django-developer**](categories/02-language-specialists/django-developer.md) - Django 4+ Web 开发专家
- [**dotnet-core-expert**](categories/02-language-specialists/dotnet-core-expert.md) - .NET 8 跨平台专家
- [**dotnet-framework-4.8-expert**](categories/02-language-specialists/dotnet-framework-4.8-expert.md) - .NET Framework 遗留企业级系统专家
- [**elixir-expert**](categories/02-language-specialists/elixir-expert.md) - Elixir 和 OTP 容错系统专家
- [**expo-react-native-expert**](categories/02-language-specialists/expo-react-native-expert.md) - Expo 与 React Native 移动端开发专家
- [**fastapi-developer**](categories/02-language-specialists/fastapi-developer.md) - 现代异步 Python API 框架专家
- [**flutter-expert**](categories/02-language-specialists/flutter-expert.md) - Flutter 3+ 跨平台移动专家
- [**golang-pro**](categories/02-language-specialists/golang-pro.md) - Go 并发编程专家
- [**java-architect**](categories=02-language-specialists/java-architect.md) - Java 企业级开发专家
- [**javascript-pro**](categories=02-language-specialists/javascript-pro.md) - JavaScript 开发专家
- [**powershell-5.1-expert**](categories/02-language-specialists/powershell-5.1-expert.md) - Windows PowerShell 5.1 与完整 .NET Framework 自动化专家
- [**powershell-7-expert**](categories=02-language-specialists/powershell-7-expert.md) - 跨平台 PowerShell 7+ 自动化与现代 .NET 专家
- [**kotlin-specialist**](categories/02-language-specialists/kotlin-specialist.md) - 现代 JVM 语言专家
- [**laravel-specialist**](categories=02-language-specialists/laravel-specialist.md) - Laravel 10+ PHP 框架专家
- [**nextjs-developer**](categories=02-language-specialists/nextjs-developer.md) - Next.js 14+ 全栈专家
- [**node-specialist**](categories=02-language-specialists/node-specialist.md) - Node.js 专家
- [**php-pro**](categories=02-language-specialists/php-pro.md) - PHP Web 开发专家
- [**python-pro**](categories/02-language-specialists/python-pro.md) - Python 生态大师
- [**rails-expert**](categories=02-language-specialists/rails-expert.md) - Rails 8.1 快速开发专家
- [**react-specialist**](categories=02-language-specialists/react-specialist.md) - React 18+ 现代模式专家
- [**rust-engineer**](categories=02-language-specialists/rust-engineer.md) - 系统编程专家
- [**spring-boot-engineer**](categories=02-language-specialists/spring-boot-engineer.md) - Spring Boot 3+ 微服务专家
- [**symfony-specialist**](categories=02-language-specialists/symfony-specialist.md) - Symfony 6+/7+/8+ PHP 框架与 Doctrine ORM 专家

### [03. Infrastructure](categories/03-infrastructure/)
**Plugin:** `voltagent-infra`

DevOps、云原生和部署专家。

- [**azure-infra-engineer**](categories=03-infrastructure/azure-infra-engineer.md) - Azure 基础设施与 Az PowerShell 自动化专家
- [**cloud-architect**](categories=03-infrastructure/cloud-architect.md) - AWS/GCP/Azure 云架构专家
- [**database-administrator**](categories=03-infrastructure/database-administrator.md) - 数据库管理专家
- [**docker-expert**](categories=03-infrastructure/docker-expert.md) - Docker 容器化与优化专家
- [**deployment-engineer**](categories=03-infrastructure/deployment-engineer.md) - 部署自动化专家
- [**devops-engineer**](categories=03-infrastructure/devops-engineer.md) - CI/CD 与自动化专家
- [**devops-incident-responder**](categories=03-infrastructure/devops-incident-responder.md) - DevOps 事件管理
- [**incident-responder**](categories=03-infrastructure/incident-responder.md) - 系统事件响应专家
- [**kubernetes-specialist**](categories=03-infrastructure/kubernetes-specialist.md) - 容器编排大师
- [**network-engineer**](categories=03-infrastructure/network-engineer.md) - 网络基础设施专家
- [**platform-engineer**](categories=03-infrastructure/platform-engineer.md) - 平台架构专家
- [**security-engineer**](categories=03-infrastructure/security-engineer.md) - 基础设施安全专家
- [**sre-engineer**](categories=03-infrastructure/sre-engineer.md) - SRE（站点可靠性工程）专家
- [**terraform-engineer**](categories=03-infrastructure/terraform-engineer.md) - IaC（基础设施即代码）专家
- [**terragrunt-expert**](categories=03-infrastructure/terragrunt-expert.md) - Terragrunt 编排与 DRY IaC 专家
- [**windows-infra-admin**](categories=03-infrastructure/windows-infra-admin.md) - Active Directory、DNS、DHCP 和 GPO 自动化专家

### [04. Quality & Security](categories/04-quality-security/)
**Plugin:** `voltagent-qa-sec`

测试、安全和代码质量专家。

- [**accessibility-tester**](categories=04-quality-security/accessibility-tester.md) - A11y 无障碍合规专家
- [**ad-security-reviewer**](categories=04-quality-security/ad-security-reviewer.md) - Active Directory 安全与 GPO 审计专家
- [**ai-writing-auditor**](categories=04-quality-security/ai-writing-auditor.md) - AI 写作模式检测与重写器
- [**architect-reviewer**](categories=04-quality-security/architect-reviewer.md) - 架构评审专家
- [**chaos-engineer**](categories=04-quality-security/chaos-engineer.md) - 系统韧性测试专家
- [**code-reviewer**](categories=04-quality-security/code-reviewer.md) - 代码质量守护者
- [**compliance-auditor**](categories=04-quality-security/compliance-auditor.md) - 法规合规专家
- [**debugger**](categories=04-quality-security/debugger.md) - 高级调试专家
- [**gdpr-ccpa-compliance**](categories=04-quality-security/gdpr-ccpa-compliance.md) - GDPR 和 CCPA 隐私合规专家
- [**error-detective**](categories=04-quality-security/error-detective.md) - 错误分析与解决专家
- [**penetration-tester**](categories=04-quality-security/penetration-tester.md) - 伦理黑客专家
- [**performance-engineer**](categories=04-quality-security/performance-engineer.md) - 性能优化专家
- [**powershell-security-hardening**](categories=04-quality-security/powershell-security-hardening.md) - PowerShell 安全加固与合规专家
- [**qa-expert**](categories=04-quality-security/qa-expert.md) - 测试自动化专家
- [**security-auditor**](categories=04-quality-security/security-auditor.md) - 安全漏洞审计专家
- [**test-automator**](categories=04-quality-security/test-automator.md) - 测试框架专家
- [**ui-ux-tester**](categories=04-quality-security/ui-ux-tester.md) - 全面文档化流程的 UI/UX 测试专家

### [05. Data & AI](categories=05-data-ai/)
**Plugin:** `voltagent-data-ai`

数据工程、机器学习和 AI 专家。

- [**ai-engineer**](categories=05-data-ai/ai-engineer.md) - AI 系统设计与部署专家
- [**data-analyst**](categories=05-data-ai/data-analyst.md) - 数据分析与可视化专家
- [**data-engineer**](categories=05-data-ai/data-engineer.md) - 数据管道架构师
- [**data-scientist**](categories=05-data-ai/data-scientist.md) - 数据分析与洞察专家
- [**database-optimizer**](categories=05-data-ai/database-optimizer.md) - 数据库性能优化专家
- [**llm-architect**](categories=05-data-ai/llm-architect.md) - 大语言模型架构师
- [**machine-learning-engineer**](categories=05-data-ai/machine-learning-engineer.md) - 机器学习系统专家
- [**ml-engineer**](categories=05-data-ai/ml-engineer.md) - 机器学习专家
- [**mlops-engineer**](categories=05-data-ai/mlops-engineer.md) - MLOps 与模型部署专家
- [**nlp-engineer**](categories=05-data-ai/nlp-engineer.md) - NLP（自然语言处理）专家
- [**postgres-pro**](categories=05-data-ai/postgres-pro.md) - PostgreSQL 数据库专家
- [**prompt-engineer**](categories=05-data-ai/prompt-engineer.md) - Prompt 优化专家
- [**reinforcement-learning-engineer**](categories=05-data-ai/reinforcement-learning-engineer.md) - 强化学习与智能体训练专家

### [06. Developer Experience](categories=06-developer-experience/)
**Plugin:** `voltagent-dev-exp`

工具链与开发者生产力专家。

- [**build-engineer**](categories=06-developer-experience/build-engineer.md) - 构建系统专家
- [**cli-developer**](categories=06-developer-experience/cli-developer.md) - CLI（命令行）工具创建者
- [**dependency-manager**](categories=06-developer-experience/dependency-manager.md) - 包管理与依赖项专家
- [**documentation-engineer**](categories=06-developer-experience/documentation-engineer.md) - 技术文档专家
- [**dx-optimizer**](categories=06-developer-experience/dx-optimizer.md) - DX（开发者体验）优化专家
- [**git-workflow-manager**](categories=06-developer-experience/git-workflow-manager.md) - Git 工作流与分支策略专家
- [**legacy-modernizer**](categories=06-developer-experience/legacy-modernizer.md) - 遗留代码现代化专家
- [**mcp-developer**](categories=06-developer-experience/mcp-developer.md) - MCP（模型上下文协议）专家
- [**powershell-ui-architect**](categories=06-developer-experience/powershell-ui-architect.md) - PowerShell UI/UX 专家，涵盖 WinForms、WPF、Metro 框架及 TUI
- [**powershell-module-architect**](categories=06-developer-experience/powershell-module-architect.md) - PowerShell 模块与配置文件架构专家
- [**readme-generator**](categories=06-developer-experience/readme-generator.md) - 仓库 README 生成专家
- [**refactoring-specialist**](categories=06-developer-experience/refactoring-specialist.md) - 代码重构专家
- [**slack-expert**](categories=06-developer-experience/slack-expert.md) - Slack 平台与 @slack/bolt 专家
- [**tooling-engineer**](categories=06-developer-experience/tooling-engineer.md) - 开发者工具链专家
- [**visual-asset-generator**](categories=06-developer-experience/visual-asset-generator.md) - 视觉素材生成专家，通过 prompt-to-asset MCP 跨 30+ 图像模型工作

### [07. Specialized Domains](categories=07-specialized-domains/)
**Plugin:** `voltagent-domains`

特定领域技术专家。

- [**api-documenter**](categories=07-specialized-domains/api-documenter.md) - API 文档专家
- [**blockchain-developer**](categories=07-specialized-domains/blockchain-developer.md) - Web3 与加密货币专家
- [**embedded-systems**](categories=07-specialized-domains/embedded-systems.md) - 嵌入式与实时系统专家
- [**fintech-engineer**](categories=07-specialized-domains/fintech-engineer.md) - 金融科技专家
- [**game-developer**](categories=07-specialized-domains/game-developer.md) - 游戏开发专家
- [**healthcare-admin**](categories=07-specialized-domains/healthcare-admin.md) - 医疗管理专家，涵盖 51 个子智能体，覆盖收入周期、合规性、质量、临床运营、健康 IT 和支付方关系
- [**hipaa-compliance**](categories=07-specialized-domains/hipaa-compliance.md) - HIPAA 合规专家（面向医疗 SaaS 供应商）
- [**iot-engineer**](categories=07-specialized-domains/iot-engineer.md) - IoT 系统开发者
- [**m365-admin**](categories=07-specialized-domains/m365-admin.md) - Microsoft 365、Exchange Online、Teams 和 SharePoint 管理专家
- [**mobile-app-developer**](categories=07-specialized-domains/mobile-app-developer.md) - 移动应用专家
- [**payment-integration**](categories=07-specialized-domains/payment-integration.md) - 支付系统专家
- [**quant-analyst**](categories=07-specialized-domains/quant-analyst.md) - 量化分析专家
- [**risk-manager**](categories=07-specialized-domains/risk-manager.md) - 风险评估与管理专家
- [**seo-specialist**](categories=07-specialized-domains/seo-specialist.md) - SEO（搜索引擎优化）专家

### [08. Business & Product](categories=08-business-product/)
**Plugin:** `voltagent-biz`

产品管理与商业分析。

- [**assumption-mapping**](categories=08-business-product/assumption-mapping.md) - 产品假设风险与验证专家
- [**backlog-grooming**](categories=08-business-product/backlog-grooming.md) - Agile 待办事项梳理专家
- [**business-analyst**](categories=08-business-product/business-analyst.md) - 需求分析专家
- [**content-marketer**](categories=08-business-product/content-marketer.md) - 内容营销专家
- [**customer-success-manager**](categories=08-business-product/customer-success-manager.md) - 客户成功专家
- [**growth-loops**](categories=08-business-product/growth-loops.md) - 增长循环与 PLG（产品驱动增长）机制专家
- [**legal-advisor**](categories=08-business-product/legal-advisor.md) - 法律与合规顾问
- [**license-engineer**](categories=08-business-product/license-engineer.md) - 软件许可与合规系统专家
- [**product-manager**](categories=08-business-product/product-manager.md) - 产品战略专家
- [**project-manager**](categories=08-business-project/project-manager.md) - 项目管理专家
- [**sales-engineer**](categories=08-business-product/sales-engineer.md) - 技术销售专家
- [**scrum-master**](categories=08-business-product/scrum-master.md) - Agile 方法论专家
- [**technical-writer**](categories=08-business-product/technical-writer.md) - 技术文档专家
- [**ux-researcher**](categories=08-business-product/ux-researcher.md) - 用户体验研究专家
- [**wordpress-master**](categories=08-business-product/wordpress-master.md) - WordPress 开发与优化专家
- [**content-quality-editor**](categories=08-business-product/content-quality-editor.md) - AI 内容质量专家，使用 unslop 在发布前剥离 AI 写作模式

### [09. Meta & Orchestration](categories=09-meta-orchestration/)
**Plugin:** `voltagent-meta`

智能体协调与元编程。

- [**airis-mcp-gateway**](https://github.com/agiletec-inc/airis-mcp-gateway) - 基于 Docker 的 MCP 多路复用器，聚合 60+ 工具至 7 个元工具下，上下文 Token 使用量降低 97%。一条命令启动，按需自动启用服务
- [**moai-adk**](https://github.com/modu-ai/moai-adk) - SPEC-first Agentic Development Kit，编排 24 个专业智能体，强制执行 Plan→Run→Sync 工作流、TRUST 5 质量门禁、52 项领域技能及 16 语言项目支持
- [**agent-installer**](categories=09-meta-orchestration/agent-installer.md) - 通过 GitHub 浏览并安装本仓库中的智能体
- [**agent-organizer**](categories=09-meta-orchestration/agent-organizer.md) - 多智能体协调器
- [**codebase-orchestrator**](categories=09-meta-orchestration/codebase-orchestrator.md) - 安全重构治理编排器
- [**context-manager**](categories=09-meta-orchestration/context-manager.md) - 上下文优化专家
- [**error-coordinator**](categories=09-meta-orchestration/error-coordinator.md) - 错误处理与恢复专家
- [**it-ops-orchestrator**](categories=09-meta-orchestration/it-ops-orchestrator.md) - IT 运维工作流编排专家
- [**knowledge-synthesizer**](categories=09-meta-orchestration/knowledge-synthesizer.md) - 知识聚合专家
- [**multi-agent-coordinator**](categories=09-meta-orchestration/multi-agent-coordinator.md) - 高级多智能体编排
- [**performance-monitor**](categories=09-meta-orchestration/performance-monitor.md) - 智能体性能优化监控
- [**pied-piper**](https://github.com/sathish316/pied-piper/) - 编排 AI 子智能体团队以处理重复性 SDLC（软件开发生命周期）工作流
- [**task-distributor**](categories=09-meta-orchestration/task-distributor.md) - 任务分配专家
- [**taskade**](https://github.com/taskade/mcp) - AI 驱动的工作区，具备自主智能体、实时协作及 MCP 集成的工作流自动化功能
- [**workflow-orchestrator**](categories=09-meta-orchestration/workflow-orchestrator.md) - 复杂工作流自动化

### [10. Research & Analysis](categories=10-research-analysis/)
**Plugin:** `voltagent-research`

研究、搜索与分析专家。

- [**ab-test-analysis**](categories=10-research-analysis/ab-test-analysis.md) - A/B 测试分析与上线决策专家
- [**cohort-analysis**](categories=10-research-analysis/cohort-analysis.md) - 用户留存与行为分析专家
- [**first-principles-thinking**](categories=10-research-analysis/first-principles-thinking.md) - 第一性原理问题解决专家
- [**research-analyst**](categories=10-research-analysis/research-analyst.md) - 综合研究专家
- [**search-specialist**](categories=10-research-analysis/search-specialist.md) - 高级信息检索专家
- [**trend-analyst**](categories=10-research-analysis/trend-analyst.md) - 新兴趋势与预测专家
- [**competitive-analyst**](categories=10-research-analysis/competitive-analyst.md) - 竞争情报专家
- [**market-researcher**](categories=10-research-analysis/market-researcher.md) - 市场分析与消费者洞察
- [**project-idea-validator**](categories=10-research-analysis/project-idea-validator.md) - 严格的产品创意上线/否决验证器
- [**data-researcher**](categories=10-research-analysis/data-researcher.md) - 数据发现与分析专家
- [**scientific-literature-researcher**](categories=10-research-analysis/scientific-literature-researcher.md) - 学术论文搜索与证据合成，通过 [BGPT MCP](https://github.com/connerlambden/bgpt-mcp)

## 🤖 Understanding Subagents

子智能体是增强 Claude Code 能力的专业 AI 助手，提供特定任务的领域专长。它们充当专用助手，Claude Code 在遇到特定类型工作时可调用它们。

### What Makes Subagents Special?

**独立的上下文窗口（Context Window）**  
每个子智能体都在其隔离的上下文中运行，防止不同任务之间的相互干扰，并保持主对话线程的清晰性。

**领域专用智能**  
子智能体配备了精心编写的指令，针对其专业领域进行优化，从而在特定任务上表现更优。

**跨项目共享**  
创建子智能体后，你可以在多个项目中重复使用它，并分发给团队成员以确保开发实践的一致性。

**细粒度的工具权限（Tool Permissions）**  
你可以为每个子智能体配置具体的工具访问权限，实现对不同任务类型能力的精细控制。

### Core Advantages

- **内存效率**：隔离的上下文防止主对话被特定任务的细节所淹没
- **更高的准确性**：专用的提示词和配置使特定领域的表现更出色
- **工作流一致性**：团队共享子智能体确保对常见任务的处理方式统一
- **安全控制**：可根据子智能体的类型和用途限制工具访问权限

### Getting Started with Subagents

**1. 访问子智能体管理器**
```bash
/agents
```

**2. 创建你的子智能体**
- 选择项目级或全局级子智能体
- 让 Claude 生成初始版本，然后根据你的需求进行微调
- 提供详细的描述说明该子智能体的用途和触发条件
- 配置工具访问权限（留空则继承所有可用工具）
- 使用内置编辑器自定义系统提示词（按 `e` 键）

**3. 部署并使用**
你的子智能体会立即可用。Claude Code 会在合适时自动调用它，或者你可以显式请求其帮助：
```
> Have the code-reviewer subagent analyze my latest commits
```

### Subagent Storage Locations

| Type | Path | Availability | Precedence |
|------|------|--------------|------------|
| Project Subagents | `.claude/agents/` | Current project only | Higher |
| Global Subagents | `~/.claude/agents/` | All projects | Lower |

Note: When naming conflicts occur, project-specific subagents override global ones.


## 📖 Subagent Structure

Each subagent follows a standardized template:

```yaml
---
name: subagent-name
description: When this agent should be invoked
tools: Read, Write, Edit, Bash, Glob, Grep
model: sonnet
---

You are a [role description and expertise areas]...

[Agent-specific checklists, patterns, and guidelines]...

## Communication Protocol
Inter-agent communication specifications...

## Development Workflow
Structured implementation phases...
```

### Tool Assignment Philosophy

### Smart Model Routing

Each subagent includes a `model` field that automatically routes it to the right Claude model — balancing quality and cost:

| Model | When It's Used | Examples |
|-------|----------------|----------|
| `opus` | Deep reasoning — architecture reviews, security audits, financial logic | `security-auditor`, `architect-reviewer`, `fintech-engineer` |
| `sonnet` | Everyday coding — writing, debugging, refactoring | `python-pro`, `backend-developer`, `devops-engineer` |
| `haiku` | Quick tasks — docs, search, dependency checks | `documentation-engineer`, `seo-specialist`, `build-engineer` |

You can override any agent's model by editing the `model` field in its frontmatter. Set `model: inherit` to use whatever model your main conversation is using.

### Tool Assignment Philosophy

Each subagent's `tools` field specifies Claude Code built-in tools, optimized for their role:
- **Read-only agents** (reviewers, auditors): `Read, Grep, Glob` - analyze without modifying
- **Research agents** (analysts, researchers): `Read, Grep, Glob, WebFetch, WebSearch` - gather information
- **Code writers** (developers, engineers): `Read, Write, Edit, Bash, Glob, Grep` - create and execute
- **Documentation agents** (writers, documenters): `Read, Write, Edit, Glob, Grep, WebFetch, WebSearch` - document with research

Each agent has minimal necessary permissions. You can extend agents by adding MCP servers or external tools to the `tools` field.

## 🧰 Tools

### [subagent-catalog](tools/subagent-catalog/)
Claude Code skill for browsing and fetching subagents from this catalog.

| Command | Description |
|---------|-------------|
| `/subagent-catalog:search <query>` | Find agents by name, description, or category |
| `/subagent-catalog:fetch <name>` | Get full agent definition |
| `/subagent-catalog:list` | Browse all categories |
| `/subagent-catalog:invalidate` | Refresh cache |

**Installation:**
```bash
cp -r tools/subagent-catalog ~/.claude/commands/
```



## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

- Submit new subagents via PR
- Improve existing definitions
- Report issues and bugs

## Contributor ♥️ Thanks
![Contributors](https://contrib.rocks/image?repo=voltagent/awesome-claude-code-subagents&max=500&columns=20&anon=1)


## 📄 License

MIT License - see [LICENSE](LICENSE)

This repository is a curated collection of subagent definitions contributed by both the maintainers and the community. All subagents are provided "as is" without warranty. We do not audit or guarantee the security or correctness of any subagent. Review before use, the maintainers accept no liability for any issues arising from their use.

If you find an issue with a listed subagent or want your contribution removed, please [open an issue](https://github.com/VoltAgent/awesome-claude-code-subagents/issues) and we'll address it promptly.


[codex-badge]: https://img.shields.io/github/stars/VoltAgent/awesome-codex-subagents?style=classic&label=Codex%20Subagents&color=000000&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0yMi4yODIgOS44MjFhNS45ODUgNS45ODUgMCAwIDAtLjUxNi00LjkxIDYuMDQ2IDYuMDQ2IDAgMCAwLTYuNTEtMi45QTYuMDY1IDYuMDY1IDAgMCAwIDQuOTgxIDQuMThhNS45ODUgNS45ODUgMCAwIDAtMy45OTggMi45IDYuMDQ2IDYuMDQ2IDAgMCAwIC43NDMgNy4wOTcgNS45OCA1Ljk4IDAgMCAwIC41MSA0LjkxMSA2LjA1MSA2LjA1MSAwIDAgMCA2LjUxNSAyLjlBNS45ODUgNS45ODUgMCAwIDAgMTMuMjYgMjRhNi4wNTYgNi4wNTYgMCAwIDAgNS43NzItNC4yMDYgNS45OSA1Ljk5IDAgMCAwIDMuOTk3LTIuOSA2LjA1NiA2LjA1NiAwIDAgMC0uNzQ3LTcuMDczek0xMy4yNiAyMi40M2E0LjQ3NiA0LjQ3NiAwIDAgMS0yLjg3Ni0xLjA0bC4xNDEtLjA4MSA0Ljc3OS0yLjc1OGEuNzk1Ljc5NSAwIDAgMCAuMzkyLS42ODF2LTYuNzM3bDIuMDIgMS4xNjhhLjA3MS4wNzEgMCAwIDEgLjAzOC4wNTJ2NS41ODNhNC41MDQgNC41MDQgMCAwIDEtNC40OTQgNC40OTR6TTMuNiAxOC4zMDRhNC40NyA0LjQ3IDAgMCAxLS41MzUtMy4wMTRsLjE0Mi4wODUgNC43ODMgMi43NTlhLjc3MS43NzEgMCAwIDAgLjc4IDBsNS44NDMtMy4zNjl2Mi4zMzJhLjA4LjA4IDAgMCAxLS4wMzMuMDYyTDkuNzQgMTkuOTVhNC41IDQuNSAwIDAgMS02LjE0LTEuNjQ2ek0yLjM0IDcuODk2YTQuNDg1IDQuNDg1IDAgMCAxIDIuMzY2LTEuOTczVjExLjZhLjc2Ni43NjYgMCAwIDAgLjM4OC42NzZsNS44MTUgMy4zNTUtMi4wMiAxLjE2OGEuMDc2LjA3NiAwIDAgMS0uMDcxIDBsLTQuODMtMi43ODZBNC41MDQgNC41MDQgMCAwIDEgMi4zNCA3Ljg3MnptMTYuNTk3IDMuODU1bC01LjgzMy0zLjM4N0wxNS4xMTkgNy4yYS4wNzYuMDc2IDAgMCAxIC4wNzEgMGw0LjgzIDIuNzkxYTQuNDk0IDQuNDk0IDAgMCAxLS42NzYgOC4xMDV2LTUuNjc4YS43OS43OSAwIDAgMC0uNDA3LS42Njd6bTIuMDEtMy4wMjNsLS4xNDEtLjA4NS00Ljc3NC0yLjc4MmEuNzc2Ljc3NiAwIDAgMC0uNzg1IDBMOS40MDkgOS4yM1Y2Ljg5N2EuMDY2LjA2NiAwIDAgMSAuMDI4LS4wNjFsNC44My0yLjc4N2E0LjUgNC41IDAgMCAxIDYuNjggNC42NnptLTEyLjY0IDQuMTM1bC0yLjAyLTEuMTY0YS4wOC4wOCAwIDAgMS0uMDM4LS4wNTdWNi4wNzVhNC41IDQuNSAwIDAgMSA3LjM3NS0zLjQ1M2wtLjE0Mi4wOEw4LjcwNCA1LjQ2YS43OTUuNzk1IDAgMCAwLS4zOTMuNjgxem0xLjA5Ny0yLjM2NWwyLjYwMi0xLjUgMi42MDcgMS41djIuOTk5bC0yLjU5NyAxLjUtMi42MDctMS41eiIvPjwvc3ZnPg==
[codex-link]: https://github.com/VoltAgent/awesome-codex-subagents