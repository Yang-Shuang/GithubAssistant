# PAL MCP：多种工作流，统一上下文

<div align="center">

  <em>你的 AI 专属 PAL —— 提供商抽象层（Provider Abstraction Layer）</em><br />
  <sub><a href="docs/name-change.md">原名：Zen MCP</a></sub>

  [查看 PAL 实际运行效果](https://github.com/user-attachments/assets/0d26061e-5f21-4ab1-b7d0-f883ddc2c3da)

👉 **[查看更多示例](#-查看工具实际运行效果)**

### 你的 CLI + 多模型 = 你的 AI 开发团队

**使用你喜爱的 🤖 CLI：**  
[Claude Code](https://www.anthropic.com/claude-code) · [Gemini CLI](https://github.com/google-gemini/gemini-cli) · [Codex CLI](https://github.com/openai/codex) · [Qwen Code CLI](https://qwenlm.github.io/qwen-code-docs/) · [Cursor](https://cursor.com) · _以及更多*

**在单个提示词（prompt）中调用多个模型：**  
Gemini · OpenAI · Anthropic · Grok · Azure · Ollama · OpenRouter · DIAL · 端侧模型

</div>

---

## 🆕 新增 CLI 到 CLI 桥接功能

全新的 **[`clink`](docs/tools/clink.md)**（CLI + Link）工具可将外部 AI CLI 直接接入你的工作流：

- **连接外部 CLI**，如 [Gemini CLI](https://github.com/google-gemini/gemini-cli)、[Codex CLI](https://github.com/openai/codex) 和 [Claude Code](https://www.anthropic.com/claude-code)，直接融入你的工作流
- **CLI 子智能体（Subagents）** —— 从当前 CLI *内部*启动隔离的 CLI 实例！Claude Code 可生成 Codex 子智能体，Codex 可生成 Gemini CLI 子智能体等。将繁重任务（代码审查、漏洞挖掘）卸载到全新的上下文中，同时保持主会话上下文窗口不被污染。每个子智能体仅返回最终结果。
- **上下文隔离** —— 运行独立的调查/分析，避免污染主要工作区
- **角色专业化** —— 生成 `planner`、`codereviewer` 或自定义角色的智能体，并配备专门的系统提示词（system prompts）
- **完整的 CLI 功能** —— Web 搜索、文件检查、MCP 工具访问、最新文档查询
- **无缝连续性** —— 子 CLI 作为一等公民参与对话，工具间共享完整的上下文

```bash
# Codex spawns Codex subagent for isolated code review in fresh context
clink with codex codereviewer to audit auth module for security issues
# Subagent reviews in isolation, returns final report without cluttering your context as codex reads each file and walks the directory structure

# Consensus from different AI models → Implementation handoff with full context preservation between tools
Use consensus with gpt-5 and gemini-pro to decide: dark mode or offline support next
Continue with clink gemini - implement the recommended feature
# Gemini receives full debate context and starts coding immediately
```

👉 **[了解更多关于 clink 的信息](docs/tools/clink.md)**

---

## 为什么选择 PAL MCP？

**既然能统筹所有模型，为何还要依赖单一 AI 模型？**

这是一个基于模型上下文协议（Model Context Protocol）的服务器，可为 [Claude Code](https://www.anthropic.com/claude-code)、[Codex CLI](https://developers.openai.com/codex/cli) 以及 IDE 客户端如 [Cursor](https://cursor.com) 或 [Claude Dev VS Code extension](https://marketplace.visualstudio.com/items?itemName=Anthropic.claude-vscode) 等工具提供强大赋能。**PAL MCP 将你喜爱的 AI 工具连接到多个 AI 模型**，从而增强代码分析、问题解决和协作开发能力。

### 真正的 AI 协作与对话连续性

PAL 支持**对话线程（conversation threading）**，使你的 CLI 能够**与多个 AI 模型讨论想法、交换推理过程、获取第二意见，甚至在不同模型间运行协作辩论**，从而帮助你获得更深入的见解和更好的解决方案。

你的 CLI 始终掌握控制权，但能为每个子任务调用最合适的 AI。上下文在工具和模型间无缝传递，支持复杂的工作流，例如：多模型代码审查 → 自动化规划 → 实现 → precommit（预提交）验证。

> **你掌握控制权。** 你选择的 CLI 负责编排 AI 团队，但工作流由你决定。编写强大的提示词（prompts），在需要时精准调用 Gemini Pro、GPT-5、Flash 或本地离线模型。

<details>
<summary><b>使用 PAL MCP 的理由</b></summary>

以 [Claude Code](https://claude.ai/code) 为例的典型工作流：

1. **多模型编排** —— Claude 与 Gemini Pro、O3、GPT-5 及 50+ 其他模型协同，为每项任务获取最佳分析结果
2. **上下文唤醒魔法** —— 即使 Claude 的上下文重置，也可让其他模型“提醒”Claude 之前的讨论内容，从而无缝继续对话
3. **引导式工作流** —— 强制执行系统化的调查阶段，防止仓促分析并确保彻底检查代码
4. **扩展上下文窗口** —— 通过委派给 Gemini（100万 token）或 O3（20万 token）来突破 Claude 的限制，适用于大型代码库
5. **真正的对话连续性** —— 完整上下文在工具和模型间流动——Gemini 能记住 10 步前 O3 说了什么
6. **特定模型优势** —— Gemini Pro 擅长深度思考，Flash 速度极快，O3 推理能力强，本地 Ollama 注重隐私
7. **专业代码审查** —— 多轮分析、分级严重程度、提供可操作反馈，并汇聚多个 AI 专家的意见达成共识
8. **智能调试助手** —— 系统化的根本原因分析，支持假设追踪与置信度评估
9. **自动模型选择** —— Claude 智能为每个子任务挑选合适的模型（你也可以手动指定）
10. **视觉能力** —— 使用支持视觉的模型分析截图、图表和可视化内容
11. **本地模型支持** —— 在本地运行 Llama、Mistral 或其他模型，实现完全隐私保护且零 API 费用
12. **绕过 MCP Token 限制** —— 自动规避 MCP 的 25K token 上限，适用于大型提示词和响应

**杀手级功能：** 当 Claude 上下文重置时，只需要求“继续由 O3 处理”——其他模型的回复会神奇地唤醒 Claude 的理解能力，无需重新加载文档！

#### 示例：多模型代码审查工作流

1. `Perform a codereview using gemini pro and o3 and use planner to generate a detailed plan, implement the fixes and do a final precommit check by continuing from the previous codereview`
2. 这将触发 [`codereview`](docs/tools/codereview.md) 工作流，Claude 会遍历代码，查找各类问题
3. 经过多轮审查后，收集相关代码并记录发现的问题
4. 维护一个介于 `exploring`（探索）、`low`（低）、`medium`（中）、`high`（高）和 `certain`（确定）之间的 `confidence`（置信度）级别，以跟踪其发现并识别问题的把握程度
5. 生成一份从严重到轻微的问题详细列表
6. 将相关文件、发现等共享给 **Gemini Pro**，以进行第二轮深入的 [`codereview`](docs/tools/codereview.md)
7. 收到回复后，接着对 O3 执行相同操作；若发现新问题，则追加到提示词中
8. 完成后，Claude 汇总所有反馈并合并成一份包含所有严重->轻微问题的单一列表，同时保留代码中的优秀模式。如果 Claude 误解或遗漏了关键内容且其他模型指出了这一点，该列表也会包含新发现或修订意见
9. 如需重大重构，它将使用 [`planner`](docs/tools/planner.md) 工作流将任务拆解为更简单的步骤
10. Claude 随后执行修复高亮问题的实际工作
11. 完成后，Claude 返回 Gemini Pro 进行 [`precommit`](docs/tools/precommit.md) 审查

全部在单个对话线程中完成！第 11 步中的 Gemini Pro *知道*第 7 步中 O3 的建议是什么！它会结合该上下文和审查意见，辅助其最终的预提交（pre-commit）审查。

**将其视为为 Claude Code 打造的 Claude Code。** 这个 MCP 并非魔法，它只是**强力胶水**。

> **请记住：** Claude 始终保持完全控制权——但**你**才是发号施令的人。
> PAL 的设计初衷是让 Claude 仅在必要时与其他模型交互，并进行有意义的来回沟通。
> **你**负责编写强大的提示词，让 Claude 调用 Gemini、Flash、O3 —— 或独立完成任务。
> 你是向导，是提示词工程师，也是幕后操纵者。
> #### 你就是那个真正的 AI —— **真正智能的**。
</details>

#### 推荐 AI 技术栈

<details>
<summary>Claude Code 用户适用</summary>

使用 [Claude Code](https://claude.ai/code) 时，为获得最佳效果：  

- **Sonnet 4.5** —— 负责所有智能体工作与编排
- **Gemini 3.0 Pro** 或 **GPT-5.2 / Pro** —— 深度思考、额外代码审查、调试与验证、预提交分析
</details>

<details>
<summary>Codex 用户适用</summary>

使用 [Codex CLI](https://developers.openai.com/codex/cli) 时，为获得最佳效果：  

- **GPT-5.2 Codex Medium** —— 负责所有智能体工作与编排
- **Gemini 3.0 Pro** 或 **GPT-5.2-Pro** —— 深度思考、额外代码审查、调试与验证、预提交分析
</details>

## 快速入门（5 分钟）

**前置条件：** Python 3.10+、Git、[已安装 uv](https://docs.astral.sh/uv/getting-started/installation/)

**1. 获取 API 密钥**（任选其一或多个）：
- **[OpenRouter](https://openrouter.ai/)** —— 通过一个 API 访问多个模型
- **[Gemini](https://makersuite.google.com/app/apikey)** —— Google 的最新模型
- **[OpenAI](https://platform.openai.com/api-keys)** —— O3、GPT-5 系列
- **[Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)** —— GPT-4o、GPT-4.1、GPT-5 系列的企業级部署
- **[X.AI](https://console.x.ai/)** —— Grok 模型
- **[DIAL](https://dialx.ai/)** —— 厂商无关的模型访问
- **[Ollama](https://ollama.ai/)** —— 本地模型（免费）

**2. 安装**（任选一种方式）：

**选项 A：克隆并自动配置**（推荐）
```bash
git clone https://github.com/BeehiveInnovations/pal-mcp-server.git
cd pal-mcp-server

# Handles everything: setup, config, API keys from system environment. 
# Auto-configures Claude Desktop, Claude Code, Gemini CLI, Codex CLI, Qwen CLI
# Enable / disable additional settings in .env
./run-server.sh  
```

**选项 B：使用 [uvx](https://docs.astral.sh/uv/getting-started/installation/) 即时配置**
```json
// Add to ~/.claude/settings.json or .mcp.json
// Don't forget to add your API keys under env
{
  "mcpServers": {
    "pal": {
      "command": "bash",
      "args": ["-c", "for p in $(which uvx 2>/dev/null) $HOME/.local/bin/uvx /opt/homebrew/bin/uvx /usr/local/bin/uvx uvx; do [ -x \"$p\" ] && exec \"$p\" --from git+https://github.com/BeehiveInnovations/pal-mcp-server.git pal-mcp-server; done; echo 'uvx not found' >&2; exit 1"],
      "env": {
        "PATH": "/usr/local/bin:/usr/bin:/bin:/opt/homebrew/bin:~/.local/bin",
        "GEMINI_API_KEY": "your-key-here",
        "DISABLED_TOOLS": "analyze,refactor,testgen,secaudit,docgen,tracer",
        "DEFAULT_MODEL": "auto"
      }
    }
  }
}
```

**3. 开始使用！**
```
"Use pal to analyze this code for security issues with gemini pro"
"Debug this error with o3 and then get flash to suggest optimizations"
"Plan the migration strategy with pal, get consensus from multiple models"
"clink with cli_name=\"gemini\" role=\"planner\" to draft a phased rollout plan"
```

👉 **[完整设置指南](docs/getting-started.md)**，包含详细安装、Gemini/Codex/Qwen 配置及故障排除
👉 **[Cursor 与 VS Code 设置](docs/getting-started.md#ide-clients)**，获取 IDE 集成说明
📺 **[查看工具实际运行效果](#-查看工具实际运行效果)**，了解真实场景示例

## 提供商配置

只要你的 `.env` 文件中包含凭据，PAL 就会激活相应的提供商。更多自定义选项请参阅 `.env.example`。

## 核心工具

> **注意：** 每个工具都自带独立的多步工作流、参数和描述，即使未使用也会占用宝贵的上下文窗口空间。为优化性能，部分工具默认禁用。请参阅下方的 [工具配置](#tool-configuration) 以启用它们。

**协作与规划** *（默认启用）*
- **[`clink`](docs/tools/clink.md)** —— 将请求桥接到外部 AI CLI（如 Gemini planner、codereviewer 等）
- **[`chat`](docs/tools/chat.md)** —— 头脑风暴想法、获取第二意见、验证方案。配合强大模型（GPT-5.2 Pro、Gemini 3.0 Pro），可生成完整代码/实现
- **[`thinkdeep`](docs/tools/thinkdeep.md)** —— 扩展推理、边界情况分析、替代视角分析
- **[`planner`](docs/tools/planner.md)** —— 将复杂项目拆解为结构化、可执行的计划
- **[`consensus`](docs/tools/consensus.md)** —— 获取多个 AI 模型的专业意见，支持立场引导

**代码分析与质量**
- **[`debug`](docs/tools/debug.md)** —— 系统性调查与根本原因分析
- **[`precommit`](docs/tools/precommit.md)** —— 提交前验证更改，防止回归问题
- **[`codereview`](docs/tools/codereview.md)** —— 专业审查，支持严重程度分级与可操作反馈
- **[`analyze`](docs/tools/analyze.md)** *（默认禁用 - [启用](#tool-configuration)）* —— 理解架构、模式及整个代码库的依赖关系

**开发工具** *（默认禁用 - [启用](#tool-configuration)）*
- **[`refactor`](docs/tools/refactor.md)** —— 智能重构，聚焦分解优化
- **[`testgen`](docs/tools/testgen.md)** —— 全面测试生成，覆盖边界情况
- **[`secaudit`](docs/tools/secaudit.md)** —— 安全审计，支持 OWASP Top 10 分析
- **[`docgen`](docs/tools/docgen.md)** —— 文档生成，附带复杂度分析

**实用工具**
- **[`apilookup`](docs/tools/apilookup.md)** —— 在子进程中强制查询当前年份的 API/SDK 文档（节省当前上下文窗口的 token），避免过时训练数据响应
- **[`challenge`](docs/tools/challenge.md)** —— 通过批判性分析防止“你说得完全正确！”类敷衍回复
- **[`tracer`](docs/tools/tracer.md)** *（默认禁用 - [启用](#tool-configuration)）* —— 静态分析提示词，用于调用流映射

<details>
<summary><b id="tool-configuration">👉 工具配置</b></summary>

### 默认配置

为优化上下文窗口使用量，仅默认启用核心工具：

**默认启用：**
- `chat`、`thinkdeep`、`planner`、`consensus` —— 核心协作工具
- `codereview`、`precommit`、`debug` —— 核心代码质量工具
- `apilookup` —— 快速 API/SDK 信息查询
- `challenge` —— 批判性思维实用工具

**默认禁用：**
- `analyze`、`refactor`、`testgen`、`secaudit`、`docgen`、`tracer`

### 启用额外工具

要启用额外工具，请从 `DISABLED_TOOLS` 列表中移除它们：

**选项 1：编辑你的 `.env` 文件**
```bash
# Default configuration (from .env.example)
DISABLED_TOOLS=analyze,refactor,testgen,secaudit,docgen,tracer

# To enable specific tools, remove them from the list
# Example: Enable analyze tool
DISABLED_TOOLS=refactor,testgen,secaudit,docgen,tracer

# To enable ALL tools
DISABLED_TOOLS=
```

**选项 2：在 MCP 设置中配置**
```json
// In ~/.claude/settings.json or .mcp.json
{
  "mcpServers": {
    "pal": {
      "env": {
        // Tool configuration
        "DISABLED_TOOLS": "refactor,testgen,secaudit,docgen,tracer",
        "DEFAULT_MODEL": "pro",
        "DEFAULT_THINKING_MODE_THINKDEEP": "high",
        
        // API configuration
        "GEMINI_API_KEY": "your-gemini-key",
        "OPENAI_API_KEY": "your-openai-key",
        "OPENROUTER_API_KEY": "your-openrouter-key",
        
        // Logging and performance
        "LOG_LEVEL": "INFO",
        "CONVERSATION_TIMEOUT_HOURS": "6",
        "MAX_CONVERSATION_TURNS": "50"
      }
    }
  }
}
```

**选项 3：启用所有工具**
```json
// Remove or empty the DISABLED_TOOLS to enable everything
{
  "mcpServers": {
    "pal": {
      "env": {
        "DISABLED_TOOLS": ""
      }
    }
  }
}
```

**注意：**
- 核心工具（`version`、`listmodels`）无法禁用
- 更改工具配置后，请重启你的 Claude 会话以使更改生效
- 每个工具都会增加上下文窗口占用量，因此仅启用你需要的工具

</details>

## 📺 查看工具实际运行效果

<details>
<summary><b>chat 工具</b></summary> —— 协作决策与多轮对话

**Redis vs Memcached 选型：**

[Chat Redis or Memcached_web.webm](https://github.com/user-attachments/assets/41076cfe-dd49-4dfc-82f5-d7461b34705d)

**带延续性的多轮对话：**

[Chat With Gemini_web.webm](https://github.com/user-attachments/assets/37bd57ca-e8a6-42f7-b5fb-11de271e95db)

</details>

<details>
<summary><b>consensus 工具</b></summary> —— 多模型辩论与决策

**多模型共识辩论：**

[PAL Consensus Debate](https://github.com/user-attachments/assets/76a23dd5-887a-4382-9cf0-642f5cf6219e)

</details>

<details>
<summary><b>precommit 工具</b></summary> —— 全面的更改验证

**预提交验证工作流：**

<div align="center">
  <img src="https://github.com/user-attachments/assets/584adfa6-d252-49b4-b5b0-0cd6e97fb2c6" width="950">
</div>

</details>

<details>
<summary><b>apilookup 工具</b></summary> —— 当前 vs 过时 API 文档对比

**无 PAL - 过时 API：**

[API without PAL](https://github.com/user-attachments/assets/01a79dc9-ad16-4264-9ce1-76a56c3580ee)

**有 PAL - 当前 API：**

[API with PAL](https://github.com/user-attachments/assets/5c847326-4b66-41f7-8f30-f380453dce22)

</details>

<details>
<summary><b>challenge 工具</b></summary> —— 批判性思维 vs 反射性附和

**无 PAL：**

![without_pal@2x](https://github.com/user-attachments/assets/64f3c9fb-7ca9-4876-b687-25e847edfd87)

**有 PAL：**

![with_pal@2x](https://github.com/user-attachments/assets/9d72f444-ba53-4ab1-83e5-250062c6ee70)

</details>

## 核心功能

**AI 编排**
- **自动模型选择** —— Claude 为每项任务挑选最合适的 AI
- **多模型工作流** —— 在单次对话中串联不同模型
- **对话连续性** —— 上下文在工具和模型间完整保留
- **[上下文唤醒](docs/context-revival.md)** —— 即使上下文重置，也可继续对话

**模型支持**
- **多提供商** —— Gemini、OpenAI、Azure、X.AI、OpenRouter、DIAL、Ollama
- **最新模型** —— GPT-5、Gemini 3.0 Pro、O3、Grok-4、本地 Llama
- **[思考模式](docs/advanced-usage.md#thinking-modes)** —— 平衡推理深度与成本
- **视觉支持** —— 分析图片、图表和截图

**开发者体验**
- **引导式工作流** —— 系统化调查防止仓促分析
- **智能文件处理** —— 自动展开目录，管理 token 限制
- **Web 搜索集成** —— 访问最新文档与最佳实践
- **[大提示词支持](docs/advanced-usage.md#working-with-large-prompts)** —— 绕过 MCP 的 25K token 限制

## 示例工作流

**多模型代码审查：**
```
"Perform a codereview using gemini pro and o3, then use planner to create a fix strategy"
```
→ Claude 系统性地审查代码 → 咨询 Gemini Pro → 获取 O3 的观点 → 制定统一行动计划

**协作调试：**
```
"Debug this race condition with max thinking mode, then validate the fix with precommit"
```
→ 深度调查 → 专家分析 → 解决方案实现 → 预提交验证

**架构规划：**
```
"Plan our microservices migration, get consensus from pro and o3 on the approach"
```
→ 结构化规划 → 多位专家意见 → 达成共识 → 实施路线图

👉 **[高级使用指南](docs/advanced-usage.md)**，涵盖复杂工作流、模型配置与高阶功能

## 快捷链接

**📖 文档**
- [文档概览](docs/index.md) —— 主要指南的高层级地图
- [快速入门](docs/getting-started.md) —— 完整设置指南
- [工具参考](docs/tools/) —— 所有工具及示例
- [高级使用](docs/advanced-usage.md) —— 高阶功能
- [配置说明](docs/configuration.md) —— 环境变量与限制
- [添加提供商](docs/adding_providers.md) —— 特定提供商设置（OpenAI、Azure、自定义网关）
- [模型评级指南](docs/model_ranking.md) —— 智能评分如何驱动自动模式建议

**🔧 设置与支持**
- [WSL 设置](docs/wsl-setup.md) —— Windows 用户适用
- [故障排除](docs/troubleshooting.md) —— 常见问题解答
- [贡献指南](docs/contributions.md) —— 代码规范与 PR 流程

## 许可证

Apache 2.0 许可证 —— 详见 [LICENSE](LICENSE) 文件。

## 致谢

基于**多模型 AI** 协作的强大力量构建 🤝
- **A**ctual **I**ntelligence（真实智能）来自人类本身
- [MCP (Model Context Protocol)](https://modelcontextprotocol.com)
- [Codex CLI](https://developers.openai.com/codex/cli)
- [Claude Code](https://claude.ai/code)
- [Gemini](https://ai.google.dev/)
- [OpenAI](https://openai.com/)
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)

### Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=BeehiveInnovations/pal-mcp-server&type=Date)](https://www.star-history.com/#BeehiveInnovations/pal-mcp-server&Date)