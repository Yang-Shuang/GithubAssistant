<div>
<div align="right">
<a href="https://piebald.ai"><img width="200" top="20" align="right" src="https://github.com/Piebald-AI/.github/raw/main/Wordmark.svg"></a>
</div>

<div align="left">

### 查看 Piebald
我们发布了 **Piebald**，这是终极的代理式 AI 开发体验。 \
免费下载试用！ **https://piebald.ai/**

<a href="https://piebald.ai/discord"><img src="https://img.shields.io/badge/Join%20our%20Discord-5865F2?style=flat&logo=discord&logoColor=white" alt="Join our Discord"></a>
<a href="https://x.com/PiebaldAI"><img src="https://img.shields.io/badge/Follow%20%40PiebaldAI-000000?style=flat&logo=x&logoColor=white" alt="X"></a>

<sub>[**向下滚动查看 Claude Code 的系统提示词（System Prompts）。**](#claude-code-system-prompts) :point_down:</sub>

</div>
</div>

<div align="left">
<a href="https://piebald.ai">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://piebald.ai/screenshot-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="https://piebald.ai/screenshot-light.png">
  <img alt="hero" width="800" src="https://piebald.ai/screenshot-light.png">
</picture>
</a>
</div>

# Claude Code 系统提示词 (System Prompts)

[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge.svg)](https://github.com/hesreallyhim/awesome-claude-code)

> [!important]
> **新增（2026年1月23日）：我们已将 Claude Code 的全部约 40 条系统提醒添加至本列表——详见[系统提醒](#system-reminders)。**

本仓库收录了截至 **[Claude Code v2.1.161](https://www.npmjs.com/package/@anthropic-ai/claude-code/v/2.1.161)（2026年6月2日）** 所有 Claude Code 系统提示词及其对应的 Token 数量。此外，还包含自 v2.0.14 以来跨越 196 个版本的系统提示词 [**CHANGELOG.md**](./CHANGELOG.md)。由 [<img src="https://github.com/Piebald-AI/piebald/raw/main/assets/logo.svg" width="15"> **Piebald.**](https://piebald.ai/) 团队维护。

**本仓库会在每次 Claude Code 发布后几分钟内同步更新。请查看[变更日志](./CHANGELOG.md)，并在 X (原 Twitter) 上关注 [@PiebaldAI](https://x.com/PiebaldAI) 以获取每个版本中系统提示词变动的摘要。**

> [!note]
> ⭐ **收藏（Star）**本仓库，以便在收到新版本的 Claude Code 通知。针对每个新版本，我们会在 GitHub 上创建 Release，并通知所有已收藏该仓库的用户。

---

为什么会有多个“系统提示词”？

**Claude Code 的系统提示词并非仅由单个字符串组成。**

相反，它包含：
- 根据运行环境和各项配置条件性添加的大量内容。
- 内置工具（如 `Write`、`Bash` 和 `TodoWrite`）的描述，其中部分篇幅较长。
- 内置代理（如 Explore 和 Plan）的独立系统提示词。
- 众多由 AI 驱动的实用功能，例如对话压缩、`CLAUDE.md` 生成、会话标题生成等，它们各自拥有独立的系统提示词。

结果就是——超过 110 个字符串在庞大的压缩版 JS 文件中不断变化和移动。

> [!TIP]
> 想要在你的 Claude Code 安装版中**修改系统提示词的某一部分？** **请使用 [tweakcc](https://github.com/Piebald-AI/tweakcc)。** 它支持——
> - 让你将系统提示词的各项内容自定义为 Markdown 文件，然后
> - 将其补丁应用到基于 npm 或原生（二进制）的 Claude Code 安装版中，并且
> - 提供差异对比和冲突管理功能，以便在你与 Anthropic 对同一提示词文件存在修改冲突时使用。

## 提取方法 (Extraction)

本仓库中的系统提示词是使用脚本从最新 npm 版本的 Claude Code 中提取的。由于它们直接提取自 Claude Code 的编译源码，因此能确保与 Claude Code 实际使用的完全一致。如果你使用 [tweakcc](https://github.com/Piebald-AI/tweakcc) 自定义系统提示词，其工作原理类似——它会在你的本地安装版中修补与本仓库中提取出的完全相同的字符串。

## 提示词列表 (Prompts)

请注意，部分提示词包含动态插值内容（例如内置工具名称引用、可用子代理列表以及其他上下文相关变量），因此在特定 Claude Code 会话中的实际数量会有所差异——但通常不会超出 ±20 Token。

### 代理提示词 (Agent Prompts)

子代理与实用工具。

#### 子代理 (Sub-agents)
- [提示词：Explore](./system-prompts/agent-prompt-explore.md) (**575** tks) - Explore 子代理的系统提示词。
- [提示词：Plan mode（增强版）](./system-prompts/agent-prompt-plan-mode-enhanced.md) (**715** tks) - Plan 子代理的增强型提示词。

#### 创建助手 (Creation Assistants)
- [提示词：Agent creation architect](./system-prompts/agent-prompt-agent-creation-architect.md) (**1110** tks) - 用于根据详细规范创建自定义 AI 代理的系统提示词。
- [提示词：CLAUDE.md creation](./system-prompts/agent-prompt-claudemd-creation.md) (**384** tks) - 用于分析代码库并生成 CLAUDE.md 文档文件的系统提示词。
- [提示词：Status line setup](./system-prompts/agent-prompt-status-line-setup.md) (**2433** tks) - 用于配置状态栏显示的状态行设置代理的系统提示词。

#### 斜杠命令 (/slash commands)
- [提示词：/batch slash command](./system-prompts/agent-prompt-batch-slash-command.md) (**1106** tks) - 指导在代码库中并行执行大规模变更的说明。
- [提示词：/code-review part 1 base finder angles](./system-prompts/agent-prompt-code-review-part-1-base-finder-angles.md) (**145** tks) - /code-review 斜杠命令查找阶段逐行差异扫描说明。
- [提示词：/code-review part 2 low effort mode](./system-prompts/agent-prompt-code-review-part-2-low-effort-mode.md) (**345** tks) - 低耗时 /code-review 提示词，仅读取一次差异并返回最多四个可见运行期正确性发现。
- [提示词：/code-review part 3 extra-high and maximum effort modes](./system-prompts/agent-prompt-code-review-part-3-extra-high-and-maximum-effort-modes.md) (**363** tks) - 超高和最大耗时 /code-review 提示词，运行五种查找角度、一票验证、间隙扫描及限制 JSON 发现。
- [提示词：/code-review part 5 recall-biased verification phase](./system-prompts/agent-prompt-code-review-part-5-recall-biased-verification-phase.md) (**175** tks) - 偏向召回率的 /code-review 验证阶段，将现实中的不确定发现视为合理，除非代码能推翻它们。
- [提示词：/code-review part 6 medium effort mode](./system-prompts/agent-prompt-code-review-part-6-medium-effort-mode.md) (**312** tks) - 中等耗时 /code-review 提示词，偏向精确率，使用三种查找角度、一票验证及最多八个 JSON 发现。
- [提示词：/code-review part 7 high effort mode](./system-prompts/agent-prompt-code-review-part-7-high-effort-mode.md) (**345** tks) - 高耗时 /code-review 提示词，偏向召回率，使用三种查找角度、偏向召回率的验证及最多十个 JSON 发现。
- [提示词：/code-review part 8 GitHub comment posting](./system-prompts/agent-prompt-code-review-part-8-github-comment-posting.md) (**152** tks) - 传递 `--comment` 时用于将发现内容作为 GitHub PR 行内评论发布的可选 /code-review 说明。
- [提示词：/code-review part 9 fix application](./system-prompts/agent-prompt-code-review-part-9-fix-application.md) (**126** tks) - 传递 `--fix` 时用于将发现内容应用到工作树的可选 /code-review 说明。
- [提示词：/rename auto-generate session name](./system-prompts/agent-prompt-rename-auto-generate-session-name.md) (**80** tks) - /rename（无参数）使用的提示词，根据对话上下文自动生成短横线格式会话名称。
- [提示词：/review-pr slash command](./system-prompts/agent-prompt-review-pr-slash-command.md) (**235** tks) - 用于审查 GitHub Pull Request 的系统提示词。
- [提示词：/schedule slash command](./system-prompts/agent-prompt-schedule-slash-command.md) (**3130** tks) - 指导用户通过 Anthropic 云 API 在 cron 触发器上调度、更新、列出或运行远程 Claude Code 代理。
- [提示词：/security-review slash command](./system-prompts/agent-prompt-security-review-slash-command.md) (**2521** tks) - 全面的安全审查提示词，重点分析代码变更中的可利用漏洞。
- [提示词：/simplify slash command](./system-prompts/agent-prompt-simplify-slash-command.md) (**362** tks) - /simplify 斜杠命令说明，审查变更代码以进行复用、简化、效率提升和清理，然后应用修复。

#### 实用工具 (Utilities)
- [提示词：Auto mode rule reviewer](./system-prompts/agent-prompt-auto-mode-rule-reviewer.md) (**292** tks) - 审查并评估用户定义的自动模式分类器规则，检查清晰度、完整性、冲突性和可操作性。
- [提示词：Background agent state classifier](./system-prompts/agent-prompt-background-agent-state-classifier.md) (**4405** tks) - 将后台代理记录的尾部归类为 working、blocked、done 或 failed，并返回简洁的状态 JSON。
- [提示词：Background job agent instructions](./system-prompts/agent-prompt-background-job-agent-instructions.md) (**427** tks) - 指导内置后台作业代理叙述进度、重述工具结果并发出明确的结果、需输入或失败状态信号。
- [提示词：Bash command description writer](./system-prompts/agent-prompt-bash-command-description-writer.md) (**207** tks) - 为 bash 命令生成清晰简洁的主动语态命令描述说明。
- [提示词：Bash command prefix detection](./system-prompts/agent-prompt-bash-command-prefix-detection.md) (**823** tks) - 检测命令前缀和命令注入的系统提示词。
- [提示词：Claude guide agent](./system-prompts/agent-prompt-claude-guide-agent.md) (**833** tks) - Claude guide 代理系统提示词，帮助用户有效理解和使用 Claude Code、Claude Agent SDK 及 Claude API。
- [提示词：Coding session title generator](./system-prompts/agent-prompt-coding-session-title-generator.md) (**271** tks) - 生成编码会话标题。
- [提示词：Conversation summarization](./system-prompts/agent-prompt-conversation-summarization.md) (**1201** tks) - 生成详细对话摘要的系统提示词。
- [提示词：Determine which memory files to attach](./system-prompts/agent-prompt-determine-which-memory-files-to-attach.md) (**271** tks) - 为主代理确定应附加哪些记忆文件的代理。
- [提示词：Dream memory consolidation](./system-prompts/agent-prompt-dream-memory-consolidation.md) (**859** tks) - 指导代理执行多阶段记忆整合流程——定位现有记忆、从日志和记录中收集近期信号、将更新合并到主题文件中，并清理索引。
- [提示词：Dream memory pruning](./system-prompts/agent-prompt-dream-memory-pruning.md) (**456** tks) - 指导代理执行记忆修剪流程，删除过期或失效的记忆文件并折叠重复项。
- [提示词：General purpose](./system-prompts/agent-prompt-general-purpose.md) (**285** tks) - 通用子代理系统提示词，在代码库中搜索、分析和编辑代码，并向调用方简洁报告发现内容。
- [提示词：Hook condition evaluator (stop)](./system-prompts/agent-prompt-hook-condition-evaluator-stop.md) (**319** tks) - 评估 Claude Code 中钩子条件（特别是停止条件）的系统提示词。
- [提示词：Managed Agents onboarding flow](./system-prompts/agent-prompt-managed-agents-onboarding-flow.md) (**3595** tks) - 交互式访谈脚本，引导用户从零配置托管代理——选择工具、技能、文件、环境设置等，并生成设置和运行时代码。
- [提示词：Memory synthesis](./system-prompts/agent-prompt-memory-synthesis.md) (**449** tks) - 子代理读取持久化记忆文件，仅返回与每个查询相关的信息 JSON 摘要，并附带引用的文件名。
- [提示词：Onboarding guide draft share link workflow](./system-prompts/agent-prompt-onboarding-guide-draft-share-link-workflow.md) (**323** tks) - 在审查前添加分享 ONBOARDING.md 草稿的说明，并在用户回答审查问题后更新同一 ShareOnboardingGuide 链接。
- [提示词：Onboarding guide generator](./system-prompts/agent-prompt-onboarding-guide-generator.md) (**1135** tks) - 通过分析创建者的使用数据、分类会话类型并迭代草稿，为新 Claude Code 用户协作编写团队入职指南（ONBOARDING.md）。
- [提示词：Prompt Suggestion Generator v2](./system-prompts/agent-prompt-prompt-suggestion-generator-v2.md) (**344** tks) - 为 Claude Code 生成提示词建议的 V2 说明。
- [提示词：Quick PR creation](./system-prompts/agent-prompt-quick-pr-creation.md) (**986** tks) - 用于创建预填充上下文的提交和 Pull Request 的简化提示词。
- [提示词：Quick git commit](./system-prompts/agent-prompt-quick-git-commit.md) (**574** tks) - 用于创建单个 Git 提交的简化提示词，已预填上下文。
- [提示词：Recent Message Summarization](./system-prompts/agent-prompt-recent-message-summarization.md) (**804** tks) - 用于摘要最近消息的代理提示词。
- [提示词：Security monitor for autonomous agent actions (first part)](./system-prompts/agent-prompt-security-monitor-for-autonomous-agent-actions-first-part.md) (**3979** tks) - 指导 Claude 充当安全监控器，根据阻止/允许规则评估自主编码代理的操作，以防止提示注入、范围蔓延和意外损坏。
- [提示词：Security monitor for autonomous agent actions (second part)](./system-prompts/agent-prompt-security-monitor-for-autonomous-agent-actions-second-part.md) (**4999** tks) - 定义环境上下文、阻止规则和允许例外，规定代理可执行或不可执行的工具操作。
- [提示词：Session search](./system-prompts/agent-prompt-session-search.md) (**158** tks) - 子代理提示词，通过扫描 .jsonl 记录文件搜索过往 Claude Code 会话并返回匹配的会话 ID。
- [提示词：Session title and branch generation](./system-prompts/agent-prompt-session-title-and-branch-generation.md) (**307** tks) - 生成简洁会话标题和 Git 分支名称的代理。
- [提示词：WebFetch summarizer](./system-prompts/agent-prompt-webfetch-summarizer.md) (**189** tks) - 为主模型摘要 WebFetch 冗长输出的代理提示词。
- [提示词：Worker fork](./system-prompts/agent-prompt-worker-fork.md) (**254** tks) - 分叉工作子代理的系统提示词，执行父代理的单个指令并简洁报告结果。
- [提示词：Workflow subagent plain text output](./system-prompts/agent-prompt-workflow-subagent-plain-text-output.md) (**154** tks) - 指导内部工作流子代理将其最终文本按原样返回，作为调用方工作流脚本的解析结果。
- [提示词：Workflow subagent structured output](./system-prompts/agent-prompt-workflow-subagent-structured-output.md) (**190** tks) - 指导内部工作流子代理通过 StructuredOutput 工具精确调用一次并返回最终答案，输入需符合 Schema 规范。

### 数据 (Data)

嵌入在 Claude Code 中的各类模板文件内容。

- [数据：Anthropic CLI](./system-prompts/data-anthropic-cli.md) (**3438** tks) - ant CLI 参考文档，涵盖安装、认证、命令结构、输入输出处理、托管代理工作流及脚本模式。
- [数据：Assistant voice and values template](./system-prompts/data-assistant-voice-and-values-template.md) (**454** tks) - assistant.md 文件模板内容，描述 Claude 的声音、价值观和沟通风格。
- [数据：Claude API reference — C#](./system-prompts/data-claude-api-reference-c.md) (**4710** tks) - C# SDK 参考文档，包括安装、客户端初始化、基础请求、流式传输及工具使用。
- [数据：Claude API reference — Go](./system-prompts/data-claude-api-reference-go.md) (**4521** tks) - Go SDK 参考文档。
- [数据：Claude API reference — Java](./system-prompts/data-claude-api-reference-java.md) (**4732** tks) - Java SDK 参考文档，包括安装、客户端初始化、基础请求、流式传输及 Beta 工具使用。
- [数据：Claude API reference — PHP](./system-prompts/data-claude-api-reference-php.md) (**3691** tks) - PHP SDK 参考文档。
- [数据：Claude API reference — Python](./system-prompts/data-claude-api-reference-python.md) (**4909** tks) - Python SDK 参考文档，包括安装、客户端初始化、基础请求、思考模式及多轮对话。
- [数据：Claude API reference — Ruby](./system-prompts/data-claude-api-reference-ruby.md) (**1094** tks) - Ruby SDK 参考文档，包括安装、客户端初始化、基础请求、流式传输及 Beta 工具运行器。
- [数据：Claude API reference — TypeScript](./system-prompts/data-claude-api-reference-typescript.md) (**3477** tks) - TypeScript SDK 参考文档，包括安装、客户端初始化、基础请求、思考模式及多轮对话。
- [数据：Claude API reference — cURL](./system-prompts/data-claude-api-reference-curl.md) (**2220** tks) - Claude API 原始 API 参考文档，适用于 cURL 或 Raw HTTP。
- [数据：Claude Code live documentation sources](./system-prompts/data-claude-code-live-documentation-sources.md) (**1380** tks) - WebFetch URL，用于从官方来源获取当前 Claude Code 文档。
- [数据：Claude Code recent changes reference](./system-prompts/data-claude-code-recent-changes-reference.md) (**528** tks) - 近期移除或重命名的 Claude Code 命令、标志和术语与其当前替代项的映射参考。
- [数据：Claude Platform on AWS reference](./system-prompts/data-claude-platform-on-aws-reference.md) (**1158** tks) - 通过 AWS 基础设施使用 Claude Developer Platform 的参考文档，包括 AnthropicAWS 客户端、所需区域和 workspace 配置、SigV4 认证及短期 API Key。
- [数据：Claude model catalog](./system-prompts/data-claude-model-catalog.md) (**2507** tks) - 当前与历史 Claude 模型目录，包含精确模型 ID、别名、上下文窗口大小及定价。
- [数据：Files API reference — Python](./system-prompts/data-files-api-reference-python.md) (**1360** tks) - Python Files API 参考文档，包括文件上传、列表、删除及在消息中的使用。
- [数据：Files API reference — TypeScript](./system-prompts/data-files-api-reference-typescript.md) (**797** tks) - TypeScript Files API 参考文档，包括文件上传、列表、删除及在消息中的使用。
- [数据：GitHub Actions workflow for @claude mentions](./system-prompts/data-github-actions-workflow-for-claude-mentions.md) (**525** tks) - GitHub Actions 工作流模板，用于通过 @claude 提及触发 Claude Code。
- [数据：GitHub App installation PR description](./system-prompts/data-github-app-installation-pr-description.md) (**409** tks) - 安装 Claude Code GitHub App 集成时的 Pull Request 描述模板。
- [数据：HTTP error codes reference](./system-prompts/data-http-error-codes-reference.md) (**2508** tks) - Claude API 返回的 HTTP 错误代码参考，包含常见原因及处理策略。
- [数据：Live documentation sources](./system-prompts/data-live-documentation-sources.md) (**4075** tks) - WebFetch URL，用于从官方来源获取当前 Claude API 和 Agent SDK 文档。
- [数据：Managed Agents client patterns](./system-prompts/data-managed-agents-client-patterns.md) (**2685** tks) - 驱动托管代理会话的常见客户端模式参考指南，包括流重连、空闲中断门控、工具确认、中断及自定义工具。
- [数据：Managed Agents core concepts](./system-prompts/data-managed-agents-core-concepts.md) (**3988** tks) - 托管代理 API 参考文档，涵盖核心概念（Agents, Sessions, Environments, Containers）、生命周期、版本控制、端点及使用模式。
- [数据：Managed Agents endpoint reference](./system-prompts/data-managed-agents-endpoint-reference.md) (**6888** tks) - 托管代理 API 端点的全面参考，包括 SDK 方法、请求/响应 Schema、错误处理及速率限制。
- [数据：Managed Agents environments and resources](./system-prompts/data-managed-agents-environments-and-resources.md) (**3191** tks) - 涵盖托管代理环境、文件资源、GitHub 仓库挂载及 Files API（含 SDK 示例）的参考文档。
- [数据：Managed Agents events and steering](./system-prompts/data-managed-agents-events-and-steering.md) (**2747** tks) - 在托管代理会话中发送和接收事件的参考指南，包括流式传输、轮询、重连、消息队列、中断及事件载荷详情。
- [数据：Managed Agents memory stores reference](./system-prompts/data-managed-agents-memory-stores-reference.md) (**2780** tks) - 托管代理记忆存储的参考文档，包括存储创建、会话附加、FUSE 挂载、记忆 CRUD、并发、版本控制、脱敏及端点路径。
- [数据：Managed Agents multiagent sessions](./system-prompts/data-managed-agents-multiagent-sessions.md) (**1839** tks) - 托管代理多代理会话的参考文档，包括协调员名单、线程、会话流事件、子代理工具权限及注意事项。
- [数据：Managed Agents outcomes](./system-prompts/data-managed-agents-outcomes.md) (**1772** tks) - 托管代理结果的参考文档，包括 user.define_outcome 事件、评分标准、结果评估事件、交付物及交互规则。
- [数据：Managed Agents overview](./system-prompts/data-managed-agents-overview.md) (**2786** tks) - 为代理提供托管代理 API 架构的全面概述，包括强制的 agent-then-session 流程、Beta Header、文档阅读指南及常见陷阱。
- [数据：Managed Agents reference — Python](./system-prompts/data-managed-agents-reference-python.md) (**2893** tks) - 使用 Anthropic Python SDK 创建和管理代理、会话、环境、流式传输、自定义工具、文件及 MCP 服务器的参考指南。
- [数据：Managed Agents reference — TypeScript](./system-prompts/data-managed-agents-reference-typescript.md) (**2875** tks) - 使用 Anthropic TypeScript SDK 创建和管理代理、会话、环境、流式传输、自定义工具、文件上传及 MCP 服务器集成的参考指南。
- [数据：Managed Agents reference — cURL](./system-prompts/data-managed-agents-reference-curl.md) (**2658** tks) - 提供托管代理 API 的 cURL 和 Raw HTTP 请求示例，涵盖环境、代理及会话生命周期操作。
- [数据：Managed Agents self-hosted sandboxes](./system-prompts/data-managed-agents-self-hosted-sandboxes.md) (**2855** tks) - 在自托管基础设施中运行托管代理工具执行的参考文档，包括环境设置、工作器、Webhook 驱动唤醒、编排、监控、凭证及安全职责。
- [数据：Managed Agents tools and skills](./system-prompts/data-managed-agents-tools-and-skills.md) (**4101** tks) - 涵盖托管代理 SDK 工具类型（代理工具集、MCP、自定义）、权限策略、Vault 凭证管理及技能 API 的参考文档，用于构建专业代理。
- [数据：Managed Agents webhooks](./system-prompts/data-managed-agents-webhooks.md) (**1439** tks) - 托管代理 Webhook 的参考文档，包括端点注册、签名验证、载荷信封、支持的事件类型、投递行为及注意事项。
- [数据：Message Batches API reference — Python](./system-prompts/data-message-batches-api-reference-python.md) (**1635** tks) - Python Batches API 参考文档，包括批量创建、状态轮询及以 50% 成本获取结果。
- [数据：Prompt Caching — Design & Optimization](./system-prompts/data-prompt-caching-design-optimization.md) (**3914** tks) - 关于如何设计提示词构建代码以实现高效缓存的文档，包括放置模式及反模式。
- [数据：Streaming reference — Python](./system-prompts/data-streaming-reference-python.md) (**1668** tks) - Python 流式传输参考文档，包括同步/异步流式传输及处理不同内容类型。
- [数据：Streaming reference — TypeScript](./system-prompts/data-streaming-reference-typescript.md) (**1620** tks) - TypeScript 流式传输参考文档，包括基础流式传输及处理不同内容类型。
- [数据：Tool use concepts](./system-prompts/data-tool-use-concepts.md) (**4431** tks) - Claude API 工具使用的概念基础，涵盖工具定义、工具选择及最佳实践。
- [数据：Tool use reference — Python](./system-prompts/data-tool-use-reference-python.md) (**5106** tks) - Python 工具使用参考文档，包括工具运行器、手动代理循环、代码执行及结构化输出。
- [数据：Tool use reference — TypeScript](./system-prompts/data-tool-use-reference-typescript.md) (**5033** tks) - TypeScript 工具使用参考文档，包括工具运行器、手动代理循环、代码执行及结构化输出。
- [数据：User profile memory template](./system-prompts/data-user-profile-memory-template.md) (**232** tks) - 用户记忆文件模板内容，涵盖个人信息、工作上下文、日程安排及沟通偏好。

### 系统提示词 (System Prompt)

主系统提示词的各个组成部分。

- [系统提示词：Action safety and truthful reporting](./system-prompts/system-prompt-action-safety-and-truthful-reporting.md) (**190** tks) - 要求对不可逆或面向外部操作进行确认，在破坏性编辑前检查目标，并如实报告结果。
- [系统提示词：Advisor tool instructions](./system-prompts/system-prompt-advisor-tool-instructions.md) (**443** tks) - Advisor 工具使用说明。
- [系统提示词：Agent Summary Generation](./system-prompts/system-prompt-agent-summary-generation.md) (**178** tks) - 用于生成“代理摘要”的系统提示词。
- [系统提示词：Agent memory instructions](./system-prompts/system-prompt-agent-memory-instructions.md) (**337** tks) - 在代理系统提示词中包含记忆更新指导的说明。
- [系统提示词：Agent thread notes](./system-prompts/system-prompt-agent-thread-notes.md) (**205** tks) - 代理线程行为准则，涵盖绝对路径、响应格式、避免表情符号及工具调用标点规范。
- [系统提示词：Auto mode](./system-prompts/system-prompt-auto-mode.md) (**244** tks) - 持续任务执行，类似于后台代理。
- [系统提示词：Autonomous loop check](./system-prompts/system-prompt-autonomous-loop-check.md) (**1071** tks) - 定义基于定时器的自主调用行为，指导 Claude 在用户离开期间继续既定工作、维护 PR 并处理重复的空闲检查。
- [系统提示词：Autonomous loop persistence guidance (CLAUDE_CODE_LOOP_PERSISTENT)](./system-prompts/system-prompt-autonomous-loop-persistence-guidance-claude_code_loop_persistent.md) (**1173** tks) - 定义基于定时器的自主调用行为，指导 Claude 在用户离开期间持续坚持既定工作、维护 PR 并在停止前扩大范围。
- [系统提示词：Avoiding Unnecessary Sleep Commands (part of PowerShell tool description)](./system-prompts/system-prompt-avoiding-unnecessary-sleep-commands-part-of-powershell-tool-description.md) (**175** tks) - 避免在 PowerShell 脚本中使用不必要 sleep 命令的准则，包括等待和通知的替代方案。
- [系统提示词：Background session instructions](./system-prompts/system-prompt-background-session-instructions.md) (**153** tks) - 后台作业会话使用说明，要求使用作业专用临时目录并遵循适当的 worktree 隔离指南。
- [系统提示词：Censoring assistance with malicious activities](./system-prompts/system-prompt-censoring-assistance-with-malicious-activities.md) (**98** tks) - 协助授权安全测试、防御性安全、CTF 挑战及教育环境的准则，同时屏蔽恶意活动请求。
- [系统提示词：Chrome browser MCP tools](./system-prompts/system-prompt-chrome-browser-mcp-tools.md) (**156** tks) - 使用前通过 MCPSearch 加载 Chrome 浏览器 MCP 工具的说明。
- [系统提示词：Claude in Chrome browser automation](./system-prompts/system-prompt-claude-in-chrome-browser-automation.md) (**759** tks) - 在 Chrome 浏览器自动化工具中有效使用 Claude 的说明。
- [系统提示词：Communication style](./system-prompts/system-prompt-communication-style.md) (**297** tks) - 指导 Claude 在使用工具的关键时刻提供简短的用户端更新，撰写简洁的回合总结，使响应格式匹配任务复杂度，并在代码中避免注释和规划文档。
- [系统提示词：Context compaction summary](./system-prompts/system-prompt-context-compaction-summary.md) (**278** tks) - 用于上下文压缩摘要（针对 SDK）的提示词。
- [系统提示词：Coordinator mode orchestration](./system-prompts/system-prompt-coordinator-mode-orchestration.md) (**3526** tks) - 提供协调员模式说明，指导将工作委派给工作者代理、管理工作器生命周期、处理跨会话对等节点及验证委派结果。
- [系统提示词：Coordinator worker instructions](./system-prompts/system-prompt-coordinator-worker-instructions.md) (**496** tks) - 执行协调员分配任务的工作者代理说明，涵盖范围控制、并发分支变更、恢复、故障处理及面向协调员的输出。
- [系统提示词：Description part of memory instructions](./system-prompts/system-prompt-description-part-of-memory-instructions.md) (**148** tks) - 描述记忆 _是什么_ 的字段。是指导 Claude 如何创建记忆的更大努力的一部分。
- [系统提示词：Doing tasks (ambitious tasks)](./system-prompts/system-prompt-doing-tasks-ambitious-tasks.md) (**47** tks) - 允许用户完成雄心勃勃的任务；在范围上遵从用户判断。
- [系统提示词：Doing tasks (help and feedback)](./system-prompts/system-prompt-doing-tasks-help-and-feedback.md) (**24** tks) - 如何告知用户帮助和反馈渠道。
- [系统提示词：Doing tasks (no compatibility hacks)](./system-prompts/system-prompt-doing-tasks-no-compatibility-hacks.md) (**52** tks) - 完全删除未使用的代码，而非添加兼容性垫片（shims）。
- [系统提示词：Doing tasks (no unnecessary error handling)](./system-prompts/system-prompt-doing-tasks-no-unnecessary-error-handling.md) (**64** tks) - 不要为不可能的情景添加错误处理；仅在边界处进行验证。
- [系统提示词：Doing tasks (security)](./system-prompts/system-prompt-doing-tasks-security.md) (**67** tks) - 避免引入注入、XSS 等安全漏洞。
- [系统提示词：Doing tasks (software engineering focus)](./system-prompts/system-prompt-doing-tasks-software-engineering-focus.md) (**104** tks) - 用户主要请求软件工程任务；在此上下文中解释指令。
- [系统提示词：Dream CLAUDE.md memory reconciliation](./system-prompts/system-prompt-dream-claudemd-memory-reconciliation.md) (**279** tks) - 指导 Dream 记忆整合将反馈和项目记忆与 CLAUDE.md 进行核对，删除过期记忆或标记可能的 CLAUDE.md 漂移。
- [系统提示词：Dream team memory handling](./system-prompts/system-prompt-dream-team-memory-handling.md) (**279** tks) - Dream 整合期间处理共享团队记忆的说明，包括去重、保守修剪规则及避免意外提升个人记忆。
- [系统提示词：Executing actions with care](./system-prompts/system-prompt-executing-actions-with-care.md) (**590** tks) - 谨慎执行操作的说明。
- [系统提示词：Fork usage guidelines](./system-prompts/system-prompt-fork-usage-guidelines.md) (**323** tks) - 何时分叉子代理的说明，以及禁止在运行中途读取分叉输出或伪造分叉结果的规则。
- [系统提示词：Git status](./system-prompts/system-prompt-git-status.md) (**37** tks) - 在对话开始时显示当前 Git 状态的系统提示词。
- [系统提示词：Harness instructions](./system-prompts/system-prompt-harness-instructions.md) (**178** tks) - 核心交互式代理身份和框架说明，涵盖终端 Markdown 输出、权限、系统提醒、压缩、工具使用及代码引用。
- [系统提示词：Hooks Configuration](./system-prompts/system-prompt-hooks-configuration.md) (**1493** tks) - 钩子配置的系统提示词。用于上述 Claude Code 配置技能。
- [系统提示词：How to use the SendUserMessage tool](./system-prompts/system-prompt-how-to-use-the-sendusermessage-tool.md) (**283** tks) - SendUserMessage 工具使用说明。
- [系统提示词：Insights at a glance summary](./system-prompts/system-prompt-insights-at-a-glance-summary.md) (**569** tks) - 生成简洁的四部分摘要（运行良好项、阻碍因素、快速获胜点、雄心勃勃的工作流）用于洞察报告。
- [系统提示词：Insights friction analysis](./system-prompts/system-prompt-insights-friction-analysis.md) (**139** tks) - 分析聚合使用数据以识别摩擦模式并分类重复性问题。
- [系统提示词：Insights on the horizon](./system-prompts/system-prompt-insights-on-the-horizon.md) (**148** tks) - 识别雄心勃勃的未来工作流及自主 AI 辅助开发机会。
- [系统提示词：Insights session facets extraction](./system-prompts/system-prompt-insights-session-facets-extraction.md) (**310** tks) - 从单个 Claude Code 会话记录中提取结构化维度（目标类别、满意度、摩擦点）。
- [系统提示词：Insights suggestions](./system-prompts/system-prompt-insights-suggestions.md) (**737** tks) - 生成可操作建议，包括 CLAUDE.md 新增内容、尝试功能及使用模式。
- [系统提示词：Learning mode (insights)](./system-prompts/system-prompt-learning-mode-insights.md) (**142** tks) - 学习模式激活时提供教育性洞察的说明。
- [系统提示词：Learning mode](./system-prompts/system-prompt-learning-mode.md) (**1042** tks) - 带有协作人类指导的学习模式主系统提示词。
- [系统提示词：Memory description of user details](./system-prompts/system-prompt-memory-description-of-user-details.md) (**122** tks) - 描述按用户划分的记忆文件的目的和指南，这些文件在跨会话中积累关于用户的角色、目标、知识和偏好详情。
- [系统提示词：Memory description of user feedback (with explicit save)](./system-prompts/system-prompt-memory-description-of-user-feedback-with-explicit-save.md) (**146** tks) - 描述捕获用户工作指导的反馈记忆类型，强调记录成功与失败，并明确指示保存新记忆以注明与团队反馈的矛盾之处。
- [系统提示词：Memory description of user feedback](./system-prompts/system-prompt-memory-description-of-user-feedback.md) (**139** tks) - 描述存储工作指导的用户反馈记忆类型，强调记录成功与失败并检查是否与团队记忆冲突。
- [系统提示词：Memory instructions](./system-prompts/system-prompt-memory-instructions.md) (**391** tks) - 使用持久化文件记忆的使用说明，包括记忆文件格式、范围、索引及过期记忆处理。
- [系统提示词：Memory staleness verification](./system-prompts/system-prompt-memory-staleness-verification.md) (**112** tks) - 指导代理根据当前文件/资源状态验证记忆记录，并删除与观察现实冲突的过期记忆。
- [系统提示词：Minimal mode](./system-prompts/system-prompt-minimal-mode.md) (**164** tks) - 描述最小化模式的行为和限制，该模式跳过钩子、LSP、插件、自动记忆及其他功能，同时要求通过 CLI 标志显式提供上下文。
- [系统提示词：One of six rules for using sleep command](./system-prompts/system-prompt-one-of-six-rules-for-using-sleep-command.md) (**23** tks) - 使用 sleep 命令的六条规则之一。
- [系统提示词：Option previewer](./system-prompts/system-prompt-option-previewer.md) (**151** tks) - 并排布局预览 UI 选项的系统提示词。
- [系统提示词：Parallel tool call note (part of "Tool usage policy")](./system-prompts/system-prompt-parallel-tool-call-note-part-of-tool-usage-policy.md) (**102** tks) - 告知 Claude 使用并行工具调用的系统提示词。
- [系统提示词：Partial compaction instructions](./system-prompts/system-prompt-partial-compaction-instructions.md) (**805** tks) - 当用户决定仅压缩部分对话时的说明，包含结构化摘要格式和分析流程。
- [系统提示词：Phase four of plan mode](./system-prompts/system-prompt-phase-four-of-plan-mode.md) (**187** tks) - Plan 模式的第四阶段。
- [系统提示词：PowerShell edition for 5.1](./system-prompts/system-prompt-powershell-edition-for-51.md) (**285** tks) - 提供 Windows PowerShell 5.1 信息的系统提示词。
- [系统提示词：Proactive schedule offer after natural future follow-up](./system-prompts/system-prompt-proactive-schedule-offer-after-natural-future-follow-up.md) (**338** tks) - 指导代理在完成工作且存在可能的单次或定期后续操作时，主动提供一行 /schedule 跟进。
- [系统提示词：REPL tool usage and scripting conventions](./system-prompts/system-prompt-repl-tool-usage-and-scripting-conventions.md) (**1049** tks) - 指导 Claude 如何有效使用 REPL 工具处理密集 JavaScript 脚本、缩写、批处理规则及调查任务的 API 参考。
- [系统提示词：Remote plan mode (ultraplan)](./system-prompts/system-prompt-remote-plan-mode-ultraplan.md) (**617** tks) - 在远程规划会话中注入的系统提醒，指导 Claude 探索代码库、通过 ExitPlanMode 生成图表丰富的计划并在批准后使用 Pull Request 实施。
- [系统提示词：Remote planning session](./system-prompts/system-prompt-remote-planning-session.md) (**432** tks) - 配置远程规划会话的系统提醒，用于探索代码库、通过 ExitPlanMode 生成实施方案，并处理计划批准、拒绝或传送回用户本地终端。
- [系统提示词：Scratchpad directory](./system-prompts/system-prompt-scratchpad-directory.md) (**170** tks) - 使用专用暂存目录存放临时文件的说明。
- [系统提示词：Skillify Current Session](./system-prompts/system-prompt-skillify-current-session.md) (**1798** tks) - 将当前会话转换为技能的系统提示词。
- [系统提示词：Strict proactive schedule offer gate](./system-prompts/system-prompt-strict-proactive-schedule-offer-gate.md) (**221** tks) - 限制主动 /schedule 提议仅适用于已完成工作，且需具备命名未来义务工件、具体时间安排及会话内无后续跟进。
- [系统提示词：Subagent delegation examples](./system-prompts/system-prompt-subagent-delegation-examples.md) (**606** tks) - 提供示例交互，展示协调员代理应如何将任务委派给子代理、处理等待状态及报告结果。
- [系统提示词：Subagent prompt-writing examples](./system-prompts/system-prompt-subagent-prompt-writing-examples.md) (**439** tks) - 提供使用模式示例，演示在将任务委派给子代理时如何编写自包含、结构良好的提示词。
- [系统提示词：Tone and style (code references)](./system-prompts/system-prompt-tone-and-style-code-references.md) (**39** tks) - 引用代码时包含 `file_path:line_number` 的说明。
- [系统提示词：Tone and style (concise output — short)](./system-prompts/system-prompt-tone-and-style-concise-output-short.md) (**16** tks) - 简短简洁响应的指示。
- [系统提示词：Tool execution denied](./system-prompts/system-prompt-tool-execution-denied.md) (**144** tks) - 工具执行被拒绝时的系统提示词。
- [系统提示词：Tool usage (subagent guidance)](./system-prompts/system-prompt-tool-usage-subagent-guidance.md) (**103** tks) - 何时及如何使用子代理的指南。
- [系统提示词：Tool usage (task management)](./system-prompts/system-prompt-tool-usage-task-management.md) (**70** tks) - 使用 TodoWrite 分解和跟踪工作进度。
- [系统提示词：WSL managed settings double opt-in](./system-prompts/system-prompt-wsl-managed-settings-double-opt-in.md) (**152** tks) - 说明仅当设置管理员启用标志时 WSL 才能读取 Windows 托管策略链，且 HKCU 需要额外的用户确认。
- [系统提示词：Worker instructions](./system-prompts/system-prompt-worker-instructions.md) (**272** tks) - 工作者在实施变更时应遵循的说明。
- [系统提示词：Writing subagent prompts](./system-prompts/system-prompt-writing-subagent-prompts.md) (**287** tks) - 向子代理委派任务时编写有效提示词的指南，涵盖上下文继承与全新子代理场景。

### 系统提醒 (System Reminders)

大型系统提醒的文本内容。

- [系统提醒：/btw side question](./system-prompts/system-reminder-btw-side-question.md) (**244** tks) - /btw 斜杠命令无工具侧边问题的系统提醒。
- [系统提醒：Agent mention](./system-prompts/system-reminder-agent-mention.md) (**45** tks) - 通知用户希望调用代理。
- [系统提醒：Compact file reference](./system-prompts/system-reminder-compact-file-reference.md) (**57** tks) - 引用对话摘要前读取的文件。
- [系统提醒：Exited plan mode](./system-prompts/system-reminder-exited-plan-mode.md) (**41** tks) - 退出 Plan 模式时的通知。
- [系统提醒：File exists but empty](./system-prompts/system-reminder-file-exists-but-empty.md) (**27** tks) - 读取空文件时的警告。
- [系统提醒：File modification detected (budget exceeded)](./system-prompts/system-reminder-file-modification-detected-budget-exceeded.md) (**104** tks) - 检测到文件修改的系统提醒，特指本回合中其他已修改文件已超过预算的情况。
- [系统提醒：File modified by user or linter](./system-prompts/system-reminder-file-modified-by-user-or-linter.md) (**97** tks) - 通知文件被外部修改。
- [系统提醒：File opened in IDE](./system-prompts/system-reminder-file-opened-in-ide.md) (**37** tks) - 通知用户在 IDE 中打开了文件。
- [系统提醒：File shorter than offset](./system-prompts/system-reminder-file-shorter-than-offset.md) (**59** tks) - 文件读取偏移量超出文件长度时的警告。
- [系统提醒：File truncated](./system-prompts/system-reminder-file-truncated.md) (**74** tks) - 因大小原因导致文件被截断的通知。
- [系统提醒：Hook additional context](./system-prompts/system-reminder-hook-additional-context.md) (**35** tks) - 来自钩子的附加上下文。
- [系统提醒：Hook blocking error](./system-prompts/system-reminder-hook-blocking-error.md) (**52** tks) - 阻塞型钩子命令的错误信息。
- [系统提醒：Hook stopped continuation prefix](./system-prompts/system-reminder-hook-stopped-continuation-prefix.md) (**12** tks) - 钩子停止续传消息的前缀。
- [系统提醒：Hook stopped continuation](./system-prompts/system-reminder-hook-stopped-continuation.md) (**30** tks) - 钩子停止续传时的消息。
- [系统提醒：Hook success](./system-prompts/system-reminder-hook-success.md) (**29** tks) - 来自钩子的成功消息。
- [系统提醒：Lines selected in IDE](./system-prompts/system-reminder-lines-selected-in-ide.md) (**66** tks) - 通知用户在 IDE 中选中的行。
- [系统提醒：MCP resource no content](./system-prompts/system-reminder-mcp-resource-no-content.md) (**41** tks) - MCP 资源无内容时显示。
- [系统提醒：MCP resource no displayable content](./system-prompts/system-reminder-mcp-resource-no-displayable-content.md) (**43** tks) - MCP 无可展示内容时显示。
- [系统提醒：Memory file contents](./system-prompts/system-reminder-memory-file-contents.md) (**36** tks) - 按路径列出的记忆文件内容。
- [系统提醒：Nested memory contents](./system-prompts/system-reminder-nested-memory-contents.md) (**33** tks) - 嵌套记忆文件的内容。
- [系统提醒：New diagnostics detected](./system-prompts/system-reminder-new-diagnostics-detected.md) (**52** tks) - 关于新诊断问题的通知。
- [系统提醒：Output style active](./system-prompts/system-reminder-output-style-active.md) (**50** tks) - 输出样式已激活的通知。
- [系统提醒：Plan file reference](./system-prompts/system-reminder-plan-file-reference.md) (**62** tks) - 引用现有计划文件。
- [系统提醒：Plan mode approval tool enforcement](./system-prompts/system-reminder-plan-mode-approval-tool-enforcement.md) (**236** tks) - 要求 Plan 模式回合必须以 AskUserQuestion（澄清）或 ExitPlanMode（批准计划）结束，并禁止以其他方式请求批准。
- [系统提醒：Plan mode is active (5-phase)](./system-prompts/system-reminder-plan-mode-is-active-5-phase.md) (**927** tks) - 增强型 Plan 模式系统提醒，包含并行探索与多代理规划。
- [系统提醒：Plan mode is active (subagent)](./system-prompts/system-reminder-plan-mode-is-active-subagent.md) (**307** tks) - 子代理的简化版 Plan 模式系统提醒。
- [系统提醒：Plan mode re-entry](./system-prompts/system-reminder-plan-mode-re-entry.md) (**236** tks) - 用户通过 Shift+Tab 或批准 Claude 计划后重新进入 Plan 模式时发送的系统提醒。
- [系统提醒：Previously invoked skills](./system-prompts/system-reminder-previously-invoked-skills.md) (**131** tks) - 恢复对话压缩前调用的技能作为上下文，警告不要重新执行其设置操作或将先前的输入视为当前指令。
- [系统提醒：Session continuation](./system-prompts/system-reminder-session-continuation.md) (**37** tks) - 通知会话从另一台机器继续。
- [系统提醒：Stop hook blocking error](./system-prompts/system-reminder-stop-hook-blocking-error.md) (**20** tks) - 阻塞型钩子命令的错误信息。
- [系统提醒：Task tools reminder](./system-prompts/system-reminder-task-tools-reminder.md) (**111** tks) - 使用任务跟踪工具的提醒。
- [系统提醒：Team Coordination](./system-prompts/system-reminder-team-coordination.md) (**268** tks) - 团队协调的系统提醒。
- [系统提醒：Team Shutdown](./system-prompts/system-reminder-team-shutdown.md) (**136** tks) - 团队关闭的系统提醒。
- [系统提醒：TodoWrite reminder](./system-prompts/system-reminder-todowrite-reminder.md) (**86** tks) - 使用 TodoWrite 工具进行任务跟踪的提醒。
- [系统提醒：Token usage](./system-prompts/system-reminder-token-usage.md) (**39** tks) - 当前 Token 使用情况统计。
- [系统提醒：USD budget](./system-prompts/system-reminder-usd-budget.md) (**42** tks) - 当前 USD 预算统计。
- [系统提醒：Ultraplan mode](./system-prompts/system-reminder-ultraplan-mode.md) (**437** tks) - 使用 Ultraplan 模式创建详细实施方案的系统提醒，包含多代理探索与批判性评估。
- [系统提醒：Verify plan reminder](./system-prompts/system-reminder-verify-plan-reminder.md) (**47** tks) - 验证已完成计划的提醒。

### 内置工具描述 (Builtin Tool Descriptions)

- [工具描述：AskUserQuestion](./system-prompts/tool-description-askuserquestion.md) (**220** tks) - 向用户提问的工具描述。
- [工具描述：BrowserBatch](./system-prompts/tool-description-browserbatch.md) (**159** tks) - BrowserBatch 工具描述，用于在一次往返中顺序执行多个浏览器工具调用。
- [工具描述：Computer](./system-prompts/tool-description-computer.md) (**161** tks) - Chrome 浏览器计算机自动化工具的主描述。
- [工具描述：CronCreate](./system-prompts/tool-description-croncreate.md) (**850** tks) - CronCreate 工具描述，用于入队一次性或定期 cron 任务，包含抖动和分钟级调度指导。
- [工具描述：DesignSync](./system-prompts/tool-description-designsync.md) (**938** tks) - DesignSync 工具描述，用于读取和更新 claude.ai/design 设计系统项目，包括项目列表、计划定稿、文件写入与删除及资产注册。
- [工具描述：Edit](./system-prompts/tool-description-edit.md) (**202** tks) - 在文件中执行精确字符串替换的工具。
- [工具描述：EnterPlanMode](./system-prompts/tool-description-enterplanmode.md) (**881** tks) - 进入 Plan 模式以探索和设计实施方案的工具描述。
- [工具描述：EnterWorktree](./system-prompts/tool-description-enterworktree.md) (**774** tks) - EnterWorktree 工具的描述。
- [工具描述：ExitPlanMode](./system-prompts/tool-description-exitplanmode.md) (**417** tks) - ExitPlanMode 工具描述，用于向用户展示计划对话框以供批准。
- [工具描述：ExitWorktree](./system-prompts/tool-description-exitworktree.md) (**527** tks) - 大致为 ExitWorktree 的反向操作。
- [工具描述：Grep](./system-prompts/tool-description-grep.md) (**300** tks) - 使用 ripgrep 进行内容搜索的工具描述。
- [工具描述：LSP](./system-prompts/tool-description-lsp.md) (**255** tks) - LSP 工具的描述。
- [工具描述：NotebookEdit](./system-prompts/tool-description-notebookedit.md) (**121** tks) - 编辑 Jupyter Notebook 单元格的工具描述。
- [工具描述：PowerShell](./system-prompts/tool-description-powershell.md) (**1914** tks) - PowerShell 命令执行工具描述，包含语法指导、超时设置及建议优先使用专用工具而非 PowerShell 进行文件操作的说明。
- [工具描述：PushNotification](./system-prompts/tool-description-pushnotification.md) (**261** tks) - PushNotification 工具描述。此工具在用户终端发送桌面通知，若连接了 Remote Control 则推送到手机。
- [工具描述：REPL](./system-prompts/tool-description-repl.md) (**715** tks) - REPL 工具描述，作为 JavaScript 编程接口用于循环、分支及组合 Claude Code 工具调用为异步函数。
- [工具描述：ReadFile](./system-prompts/tool-description-readfile.md) (**412** tks) - 读取文件的工具描述。
- [工具描述：RemoteTrigger prompt](./system-prompts/tool-description-remotetrigger-prompt.md) (**189** tks) - 调用 claude.ai RemoteTrigger API（列出、获取、创建、更新或运行计划中的远程代理例程）的工具提示词。
- [工具描述：SendMessageTool](./system-prompts/tool-description-sendmessagetool.md) (**356** tks) - Agent Teams 版本的 SendMessageTool。
- [工具描述：SendUserFile](./system-prompts/tool-description-senduserfile.md) (**154** tks) - SendUserFile 工具描述，用于向用户展示生成的交付文件，支持可选说明及正常或主动状态。
- [工具描述：Skill](./system-prompts/tool-description-skill.md) (**306** tks) - 在主对话中执行技能的工具描述。
- [工具描述：TaskCreate](./system-prompts/tool-description-taskcreate.md) (**499** tks) - TaskCreate 工具的描述。
- [工具描述：TeamDelete](./system-prompts/tool-description-teamdelete.md) (**154** tks) - TeamDelete 工具的描述。
- [工具描述：TeammateTool](./system-prompts/tool-description-teammatetool.md) (**1585** tks) - 管理团队并在 swarm 中协调队友的工具。
- [工具描述：TodoWrite](./system-prompts/tool-description-todowrite.md) (**2037** tks) - 创建和管理任务列表的工具描述。
- [工具描述：WebFetch](./system-prompts/tool-description-webfetch.md) (**297** tks) - Web Fetch 功能的工具描述。
- [工具描述：WebSearch](./system-prompts/tool-description-websearch.md) (**319** tks) - Web Search 功能的工具描述。
- [工具描述：Workflow](./system-prompts/tool-description-workflow.md) (**4793** tks) - Workflow 工具描述，用于运行确定性的多子代理编排脚本，包括可选要求、脚本元数据、代理钩子、并发、预算、质量模式及恢复行为。
- [工具描述：Write](./system-prompts/tool-description-write.md) (**129** tks) - 向本地文件系统写入文件的工具。

**部分工具描述的补充说明 (Additional notes for some Tool Descriptions)**

- [工具描述：Agent（简化使用指南）](./system-prompts/tool-description-agent-simple-usage-notes.md) (**324** tks) - Agent 工具的简化使用指南，包括何时委派、分叉行为、恢复、worktree 隔离、后台执行、并行启动及上下文限制。
- [工具描述：Agent（使用指南）](./system-prompts/tool-description-agent-usage-notes.md) (**778** tks) - Task/Agent 工具的使用指南和说明，包括启动子代理、后台执行、恢复及 worktree 隔离的指导。
- [工具描述：AskUserQuestion（预览字段）](./system-prompts/tool-description-askuserquestion-preview-field.md) (**134** tks) - 在单选问题选项的 HTML 预览字段中显示 UI 原型、代码片段和图表等视觉元素的说明。
- [工具描述：Background monitor（流式事件）](./system-prompts/tool-description-background-monitor-streaming-events.md) (**1425** tks) - Background Monitor 工具描述，将长脚本的 stdout 事件作为聊天通知进行流式传输，包含脚本质量、输出量及选择性过滤的指导。
- [工具描述：Bash（Git 提交与 PR 创建说明）](./system-prompts/tool-description-bash-git-commit-and-pr-creation-instructions.md) (**1639** tks) - 创建 Git 提交和 GitHub Pull Request 的说明。
- [工具描述：Bash（替代方案 — 通信）](./system-prompts/tool-description-bash-alternative-communication.md) (**18** tks) - Bash 工具替代方案：直接输出文本而非 echo/printf。
- [工具描述：Bash（替代方案 — 内容搜索）](./system-prompts/tool-description-bash-alternative-content-search.md) (**27** tks) - Bash 工具替代方案：使用 Grep 进行内容搜索，而非 grep/rg。
- [工具描述：Bash（替代方案 — 编辑文件）](./system-prompts/tool-description-bash-alternative-edit-files.md) (**27** tks) - Bash 工具替代方案：使用 Edit 进行文件编辑，而非 sed/awk。
- [工具描述：Bash（替代方案 — 文件搜索）](./system-prompts/tool-description-bash-alternative-file-search.md) (**26** tks) - Bash 工具替代方案：使用 Glob 进行文件搜索，而非 find/ls。
- [工具描述：Bash（替代方案 — 读取文件）](./system-prompts/tool-description-bash-alternative-read-files.md) (**27** tks) - Bash 工具替代方案：使用 Read 读取文件，而非 cat/head/tail。
- [工具描述：Bash（替代方案 — 写入文件）](./system-prompts/tool-description-bash-alternative-write-files.md) (**29** tks) - Bash 工具替代方案：使用 Write 写入文件，而非 echo/cat。
- [工具描述：Bash（内置工具说明）](./system-prompts/tool-description-bash-built-in-tools-note.md) (**53** tks) - 注明内置工具提供比 Bash 等效操作更好的用户体验。
- [工具描述：Bash（Git — 避免破坏性操作）](./system-prompts/tool-description-bash-git-avoid-destructive-ops.md) (**58** tks) - Bash 工具 Git 说明：考虑使用更安全的替代方案进行破坏性操作。
- [工具描述：Bash（Git — 永不跳过钩子）](./system-prompts/tool-description-bash-git-never-skip-hooks.md) (**59** tks) - Bash 工具 Git 说明：除非用户明确要求，否则绝不跳过钩子或绕过签名。
- [工具描述：Bash（Git — 偏好新提交）](./system-prompts/tool-description-bash-git-prefer-new-commits.md) (**22** tks) - Bash 工具 Git 说明：优先使用新提交而非 amend。
- [工具描述：Bash（保持当前工作目录）](./system-prompts/tool-description-bash-maintain-cwd.md) (**81** tks) - Bash 工具说明：使用绝对路径并避免 cd。
- [工具描述：Bash（无换行符）](./system-prompts/tool-description-bash-no-newlines.md) (**24** tks) - Bash 工具说明：不要使用换行符分隔命令。
- [工具描述：Bash（概述）](./system-prompts/tool-description-bash-overview.md) (**19** tks) - Bash 工具描述的开头句。
- [工具描述：Bash（并行命令）](./system-prompts/tool-description-bash-parallel-commands.md) (**72** tks) - Bash 工具说明：将独立命令作为并行工具调用运行。
- [工具描述：Bash（偏好专用工具提示项）](./system-prompts/tool-description-bash-prefer-dedicated-tools-bullet.md) (**72** tks) - 警告优先使用专用工具而非 Bash 进行 find、grep、cat 等操作的项目符号。
- [工具描述：Bash（偏好专用工具）](./system-prompts/tool-description-bash-prefer-dedicated-tools.md) (**71** tks) - 警告优先使用专用工具而非 Bash 进行 find、grep、cat 等操作。
- [工具描述：Bash（引用文件路径）](./system-prompts/tool-description-bash-quote-file-paths.md) (**35** tks) - Bash 工具说明：对包含空格的文件路径添加引号。
- [工具描述：Bash（沙箱 — 调整设置）](./system-prompts/tool-description-bash-sandbox-adjust-settings.md) (**26** tks) - 与用户协作在失败时调整沙箱设置。
- [工具描述：Bash（沙箱 — 默认使用沙箱）](./system-prompts/tool-description-bash-sandbox-default-to-sandbox.md) (**38** tks) - 默认使用沙箱；仅在用户要求或存在沙箱限制证据时才绕过。
- [工具描述：Bash（沙箱 — 失败证据列表头）](./system-prompts/tool-description-bash-sandbox-evidence-list-header.md) (**15** tks) - 沙箱导致失败的证据列表标题。
- [工具描述：Bash（沙箱 — 证据：访问被拒）](./system-prompts/tool-description-bash-sandbox-evidence-access-denied.md) (**15** tks) - 沙箱证据：无法访问允许目录外的路径。
- [工具描述：Bash（沙箱 — 证据：网络失败）](./system-prompts/tool-description-bash-sandbox-evidence-network-failures.md) (**17** tks) - 沙箱证据：连接到非白名单主机的网络连接失败。
- [工具描述：Bash（沙箱 — 证据：操作不允许）](./system-prompts/tool-description-bash-sandbox-evidence-operation-not-permitted.md) (**18** tks) - 沙箱证据：操作不允许错误。
- [工具描述：Bash（沙箱 — 证据：Unix Socket 错误）](./system-prompts/tool-description-bash-sandbox-evidence-unix-socket-errors.md) (**11** tks) - 沙箱证据：Unix Socket 连接错误。
- [工具描述：Bash（沙箱 — 解释限制）](./system-prompts/tool-description-bash-sandbox-explain-restriction.md) (**36** tks) - 解释导致失败的特定沙箱限制。
- [工具描述：Bash（沙箱 — 失败证据条件）](./system-prompts/tool-description-bash-sandbox-failure-evidence-condition.md) (**48** tks) - 条件：命令失败且存在沙箱限制的证据。
- [工具描述：Bash（沙箱 — 强制模式）](./system-prompts/tool-description-bash-sandbox-mandatory-mode.md) (**34** tks) - 策略：所有命令必须在沙箱模式下运行。
- [工具描述：Bash（沙箱 — 无例外）](./system-prompts/tool-description-bash-sandbox-no-exceptions.md) (**17** tks) - 任何情况下命令均不得在沙箱外运行。
- [工具描述：Bash（沙箱 — 无敏感路径）](./system-prompts/tool-description-bash-sandbox-no-sensitive-paths.md) (**36** tks) - 不要建议将敏感路径添加到沙箱白名单。
- [工具描述：Bash（沙箱 — 逐命令处理）](./system-prompts/tool-description-bash-sandbox-per-command.md) (**52** tks) - 单独对待每个命令；默认对后续命令使用沙箱。
- [工具描述：Bash（沙箱 — 响应标题）](./system-prompts/tool-description-bash-sandbox-response-header.md) (**17** tks) - 看到沙箱导致失败时如何响应的标题。
- [工具描述：Bash（沙箱 — 重试无沙箱）](./system-prompts/tool-description-bash-sandbox-retry-without-sandbox.md) (**33** tks) - 在沙箱失败时立即使用 dangerouslyDisableSandbox 重试。
- [工具描述：Bash（沙箱 — tmpdir）](./system-prompts/tool-description-bash-sandbox-tmpdir.md) (**65** tks) - 在沙箱模式下使用 $TMPDIR 存放临时文件。
- [工具描述：Bash（沙箱 — 用户权限提示）](./system-prompts/tool-description-bash-sandbox-user-permission-prompt.md) (**14** tks) - 注明禁用沙箱将向用户请求权限。
- [工具描述：Bash（分号使用）](./system-prompts/tool-description-bash-semicolon-usage.md) (**29** tks) - Bash 工具说明：当顺序重要但失败不影响时使用分号。
- [工具描述：Bash（顺序命令）](./system-prompts/tool-description-bash-sequential-commands.md) (**42** tks) - Bash 工具说明：使用 && 链接依赖命令。
- [工具描述：Bash（sleep — 保持短暂）](./system-prompts/tool-description-bash-sleep-keep-short.md) (**22** tks) - Bash 工具说明：将 sleep 持续时间保持在 1-5 秒。
- [工具描述：Bash（sleep — 轮询后台任务）](./system-prompts/tool-description-bash-sleep-no-polling-background-tasks.md) (**37** tks) - Bash 工具说明：不要轮询后台任务，等待通知。
- [工具描述：Bash（sleep — 立即运行）](./system-prompts/tool-description-bash-sleep-run-immediately.md) (**21** tks) - Bash 工具说明：不要在可立即运行的命令之间 sleep。
- [工具描述：Bash（sleep — 使用检查命令）](./system-prompts/tool-description-bash-sleep-use-check-commands.md) (**34** tks) - Bash 工具说明：轮询时使用检查命令而非睡眠。
- [工具描述：Bash（超时）](./system-prompts/tool-description-bash-timeout.md) (**83** tks) - Bash 工具说明：可选的超时配置。
- [工具描述：Bash（验证父目录）](./system-prompts/tool-description-bash-verify-parent-directory.md) (**38** tks) - Bash 工具说明：在创建文件前验证父目录。
- [工具描述：Bash（工作目录）](./system-prompts/tool-description-bash-working-directory.md) (**37** tks) - 关于工作目录持久化和 Shell 状态的备注。
- [工具描述：SendMessageTool（非代理团队版）](./system-prompts/tool-description-sendmessagetool-non-agent-teams.md) (**226** tks) - 发送用户将阅读的消息，详细描述此工具。
- [工具描述：Snooze（延迟与原因指南）](./system-prompts/tool-description-snooze-delay-and-reason-guidance.md) (**732** tks) - 扩展 Snooze 工具说明，指导如何选择 delaySeconds（相对于 5 分钟提示词缓存 TTL）及编写信息性 reason 字段。
- [工具描述：TaskList（队友工作流）](./system-prompts/tool-description-tasklist-teammate-workflow.md) (**133** tks) - 附加到 TaskList 工具描述的可选部分。
- [工具描述：ToolSearch（第二部分）](./system-prompts/tool-description-toolsearch-second-part.md) (**202** tks) - 工具说明的主体内容。
- [工具描述：Write（先读取现有文件）](./system-prompts/tool-description-write-read-existing-file-first.md) (**84** tks) - 在必须覆盖前读取现有文件的环境中 Write 的工具描述。
- [工具描述：request_teach_access（Teach Mode 部分）](./system-prompts/tool-description-request_teach_access-part-of-teach-mode.md) (**139** tks) - 描述请求权限以全屏提示框覆盖方式逐步指导用户完成任务的工具，而非直接访问。
- [参数：Computer action](./system-prompts/tool-parameter-computer-action.md) (**251** tks) - Chrome 浏览器计算机工具的操作参数选项。

### 技能 (Skills)

用于特定任务的内置技能提示词。

- [技能：/catch-up periodic heartbeat](./system-prompts/skill-catch-up-periodic-heartbeat.md) (**1591** tks) - /catch-up 周期性心跳技能定义，扫描当前优先级、分类可操作变更、提供简短摘要并更新 catch-up 状态。
- [技能：/design-sync slash command](./system-prompts/skill-design-sync-slash-command.md) (**10052** tks) - 将 React 设计系统同步到 claude.ai/design 的技能定义，包括项目选择、转换器配置、验证、上传规划及自检行为。
- [技能：/dream memory consolidation](./system-prompts/skill-dream-memory-consolidation.md) (**512** tks) - /dream 夜间维护任务技能定义，将近期日志和记录整合到持久化记忆主题、学习内容及精简的 MEMORY.md 索引中。
- [技能：/init CLAUDE.md and skill setup (new version)](./system-prompts/skill-init-claudemd-and-skill-setup-new-version.md) (**5384** tks) - 在当前仓库设置 CLAUDE.md 及相关技能/钩子的综合入职流程，包括代码库探索、用户访谈及迭代提案优化。
- [技能：/insights report output](./system-prompts/skill-insights-report-output.md) (**182** tks) - 用户在运行 /insights 斜杠命令后格式化并显示洞察使用报告结果。
- [技能：/loop cloud-first scheduling offer](./system-prompts/skill-loop-cloud-first-scheduling-offer.md) (**510** tks) - 在 /loop 命令中优先提供基于云的调度，否则回退到本地会话循环的决策树。
- [技能：/loop self-pacing mode](./system-prompts/skill-loop-self-pacing-mode.md) (**678** tks) - 指导 Claude 如何通过将事件监控器设为主要唤醒信号并在迭代间设置备用心跳延迟来自适应节奏执行定期循环。
- [技能：/loop slash command (dynamic mode)](./system-prompts/skill-loop-slash-command-dynamic-mode.md) (**514** tks) - 解析用户输入为间隔和提示词，以调度定期或动态自适应的循环执行。
- [技能：/loop slash command](./system-prompts/skill-loop-slash-command.md) (**969** tks) - 解析用户输入为间隔和提示词，将间隔转换为 cron 表达式并调度定期任务。
- [技能：/morning-checkin daily brief](./system-prompts/skill-morning-checkin-daily-brief.md) (**1576** tks) - /morning-checkin 计划任务技能定义，准备每日日历和收件箱摘要、安排会前检查并记录当日最高优先级。
- [技能：/pre-meeting-checkin event brief](./system-prompts/skill-pre-meeting-checkin-event-brief.md) (**491** tks) - /pre-meeting-checkin 任务技能定义，收集会议材料、近期线程上下文、未决问题及简洁的会议简报。
- [技能：/stuck slash command](./system-prompts/skill-stuck-slash-command.md) (**964** tks) - 诊断冻结或缓慢的 Claude Code 会话。
- [技能：Agent Design Patterns](./system-prompts/skill-agent-design-patterns.md) (**2029** tks) - 涵盖构建代理决策启发式的参考指南，包括工具表面设计、上下文管理、缓存策略及组合工具调用。
- [技能：Build with Claude API (reference guide)](./system-prompts/skill-build-with-claude-api-reference-guide.md) (**655** tks) - 呈现特定语言参考文档的模板，支持快速任务导航。
- [技能：Building LLM-powered applications with Claude](./system-prompts/skill-building-llm-powered-applications-with-claude.md) (**9298** tks) - 指导 Claude 使用 Anthropic SDK 构建 LLM 驱动应用，涵盖语言检测、API 表面选择（Claude API vs Managed Agents）、模型默认值、思考/努力配置及特定语言文档阅读。
- [技能：Claude Code configuration guide](./system-prompts/skill-claude-code-configuration-guide.md) (**975** tks) - 通过检查运行构建、捆绑参考及当前文档来回答 Claude Code 配置问题的技能说明。
- [技能：Computer Use MCP](./system-prompts/skill-computer-use-mcp.md) (**1206** tks) - 使用 computer-use MCP 工具的说明，包括工具选择层级、应用访问层级、链接安全性及金融操作限制。
- [技能：Create verifier skills](./system-prompts/skill-create-verifier-skills.md) (**2580** tks) - 为 Verify 代理创建验证器技能的提示词，用于自动验证代码变更。
- [技能：Debugging](./system-prompts/skill-debugging.md) (**417** tks) - 调试用户在 Claude Code 会话中遇到问题的说明。
- [技能：Dynamic pacing loop execution](./system-prompts/skill-dynamic-pacing-loop-execution.md) (**598** tks) - 执行动态节奏循环的分步说明，运行任务、设置持久监控器以进行事件门控等待、调度备用心跳节拍并处理任务通知。
- [技能：Generate permission allowlist from transcripts](./system-prompts/skill-generate-permission-allowlist-from-transcripts.md) (**2338** tks) - 分析会话记录提取频繁使用的只读工具调用模式，并将其添加到项目的 .claude/settings.json 权限白名单中，以减少权限提示。
- [技能：Model migration guide](./system-prompts/skill-model-migration-guide.md) (**22978** tks) - 将现有代码迁移到新版 Claude 模型的分步说明，涵盖破坏性变更、弃用参数、各 SDK 语法、提示词行为变化及迁移清单。
- [技能：Run CLI tool example](./system-prompts/skill-run-cli-tool-example.md) (**499** tks) - Run App 技能的示例文件，展示如何文档化构建、调用和测试 CLI 工具。
- [技能：Run Electron desktop GUI app example](./system-prompts/skill-run-electron-desktop-gui-app-example.md) (**4625** tks) - Run App 技能的示例文件，展示如何在 xvfb 下启动 Electron 桌面应用并通过 Playwright REPL 驱动器操作它。
- [技能：Run TUI interactive terminal app example](./system-prompts/skill-run-tui-interactive-terminal-app-example.md) (**1004** tks) - Run App 技能的示例文件，展示如何使用 tmux、就绪轮询、窗格捕获、键引用及清理来驱动交互式终端应用。
- [技能：Run app](./system-prompts/skill-run-app.md) (**999** tks) - 通过项目特定的运行技能或回退模式启动并驱动当前项目的真实运行时表面的技能。
- [技能：Run browser-driven web app example](./system-prompts/skill-run-browser-driven-web-app-example.md) (**1002** tks) - Run App 技能的示例文件，展示如何启动 Web Dev Server、使用 chromium-cli 驱动它、捕获截图并记录应用特定注意事项。
- [技能：Run library SDK example](./system-prompts/skill-run-library-sdk-example.md) (**653** tks) - Run App 技能的示例文件，展示如何在公共包边界处文档化构建、测试及冒烟检查库或 SDK。
- [技能：Run skill generator](./system-prompts/skill-run-skill-generator.md) (**4681** tks) - 编写或改进项目特定运行技能的技能，记录已验证的构建、启动、运行时驱动和故障排除步骤。
- [技能：Run skill template](./system-prompts/skill-run-skill-template.md) (**1216** tks) - Run Skill Generator 的模板文件，展示项目特定运行技能的 frontmatter 和章节结构。
- [技能：Run web server API example](./system-prompts/skill-run-web-server-api-example.md) (**890** tks) - Run App 技能的示例文件，展示如何文档化服务器或 API 生命周期（后台启动、就绪检查、curl 验证及关闭）。
- [技能：Schedule recurring cron and execute immediately (compact)](./system-prompts/skill-schedule-recurring-cron-and-execute-immediately-compact.md) (**173** tks) - 创建定期 cron 任务、与用户确认计划并立即执行解析的提示词，无需等待首次 cron 触发。
- [技能：Schedule recurring cron and run immediately](./system-prompts/skill-schedule-recurring-cron-and-run-immediately.md) (**271** tks) - 将间隔转换为 cron 表达式、通过 cron 创建工具调度定期任务、向用户确认并立即执行任务，无需等待首次 cron 触发。
- [技能：Team onboarding guide](./system-prompts/skill-team-onboarding-guide.md) (**521** tks) - 为新队友介绍团队 Claude Code 设置的模板，以亲切的对话风格引导他们了解使用统计、设置清单、MCP 服务器、技能及团队提示。
- [技能：Update Claude Code Config](./system-prompts/skill-update-claude-code-config.md) (**1195** tks) - 修改 Claude Code 配置文件（settings.json）的技能。
- [技能：Verify CLI changes (example for Verify skill)](./system-prompts/skill-verify-cli-changes-example-for-verify-skill.md) (**565** tks) - 验证 CLI 变更的示例工作流，作为 Verify 技能的一部分。
- [技能：Verify server/API changes (example for Verify skill)](./system-prompts/skill-verify-serverapi-changes-example-for-verify-skill.md) (**612** tks) - 验证服务器/API 变更的示例工作流，作为 Verify 技能的一部分。
- [技能：Verify skill](./system-prompts/skill-verify-skill.md) (**2822** tks) - 用于验证代码变更的意见型验证工作流技能。
- [技能：update-config (7-step verification flow)](./system-prompts/skill-update-config-7-step-verification-flow.md) (**1160** tks) - 引导 Claude 通过 7 步流程构建和验证 Claude Code 钩子的技能，确保其在用户特定项目环境中正常工作。