<p align="center" style="text-align:center;">
  <img src="resources/serena-logo.svg#gh-light-mode-only" style="width:500px">
  <img src="resources/serena-logo-dark-mode.svg#gh-dark-mode-only" style="width:500px">
</p>

<h3 align="center">
    专为你的编程智能体打造的 IDE
</h3>

<div align="center">
  <a href="https://discord.com/invite/cVUNQmnV4r"><img src="https://img.shields.io/badge/discord-join-5865F2?style=flat-square&labelColor=0a0e14&logo=discord&logoColor=5865F2" alt="discord"></a>
  <a href="https://github.com/oraios/serena/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-b0e8ff?style=flat-square&labelColor=0a0e14" alt="license"></a>
</div>
<br>


* Serena 提供了核心的**语义代码检索、编辑、重构和调试工具**，其功能类似于集成开发环境（IDE），在符号（symbol）层面运行并利用关系结构。
* 它通过模型上下文协议（Model Context Protocol, **MCP**）与任意客户端/大语言模型（LLM）集成。
  
Serena 的**以智能体优先的工具设计**采用了稳健的高级抽象，使其区别于依赖行号或基础搜索模式等低级概念的方法。

实际上，这意味着你的智能体能够运行得**更快、更高效且更可靠**，尤其是在大型和复杂的代码库中。

> [!IMPORTANT]
> 请勿通过 MCP 市场或插件商店安装 Serena！它们包含过时且不理想的安装命令。请按照我们的[快速开始](#quick-start)指南操作。

## 快速演示

https://github.com/user-attachments/assets/8d11646e-b80e-4723-b9d7-32d6101b5f58

:tv: 更长视频：[5分钟了解 Serena（YouTube）](https://www.youtube.com/watch?v=5QN7gN1KYLA)

## “终端用户”怎么说

虽然下载和配置 Serena 的是人类，但我们的“终端用户”本质上是 AI 智能体。作为实际使用 Serena 工具的一方，它们最能评估 Serena 的价值。

我们设计了一个中立的评估提示词（prompt），引导智能体执行约 20 项代表日常开发工作的常规编码任务，以此估算在与内置工具配合使用时，Serena 工具带来的增值效果。 

以下是这些智能体的评价总结（一句话）：

**在大型 Python 代码库上使用 Claude Code（Opus 4.6 high）：**
> “Serena 的 IDE 级语义工具是我工具箱中最重要的补充——跨文件重命名、移动和引用查找，这些原本需要我小心翼翼且容易出错的 8–12 个步骤，现在只需一次原子调用即可完成。我一定会要求与我合作的任何开发者都配置它们。”

**在 Java 代码库上使用 Codex CLI（GPT 5.4 high）：**
> “作为一名编码 AI 智能体，我会要求我的开发者添加 Serena。它弥补了我对符号、引用和重构的 IDE 级理解缺失，将脆弱的代码修改转化为更稳健、更快且更有信心的变更，而这正是语义关键之处。”

**在大型多语言 Monorepo 上使用 Copilot CLI（GPT 5.4 medium）：**
> “作为一名编码智能体，我绝对会要求我的开发者添加 Serena。它让我在处理真实代码时明显更敏锐、更从容——尤其是符号感知导航、跨文件重构和 Monorepo 依赖跳转——而我依然会使用内置工具进行微小的文本编辑和非代码工作。”

不同环境下的不同智能体得出了独立且一致的结论。

_给你的智能体提供它一直要求的工具，并将 Serena MCP 添加到你的客户端吧！_

查看我们的[文档](https://oraios.github.io/serena/04-evaluation/000_evaluation-intro.html)以获取完整的方法论和更详细的评估结果，或者在你选择的项目上自行运行评估。
 

## Serena 的工作原理

Serena 为编码工作流提供了必要的[工具](https://oraios.github.io/serena/01-about/035_tools.html)，但实际工作需要由大语言模型（LLM）来执行并编排工具调用。

Serena 可通过**模型上下文协议（MCP）**扩展你现有 AI 客户端的功能。大多数现代 AI 聊天客户端都直接支持 MCP，包括：
* 基于终端的客户端（如 Claude Code、Codex、OpenCode 或 Gemini-CLI），
* IDE 及其助手插件（适用于 VSCode、Cursor 和 JetBrains IDE，如 Copilot、Junie、JetBrains AI Assistant 等），
* 桌面端和 Web 客户端（如 Claude Desktop、Codex App 或 OpenWebUI）。

<img src="resources/serena-block-diagram.svg">

:tv: 另请参阅：[5分钟了解 Serena（YouTube）](https://www.youtube.com/watch?v=5QN7gN1KYLA)

要将 Serena MCP 服务器连接到你的客户端，你可以选择：
* 向客户端提供一个启动命令，使其能够启动 MCP 服务器；或
* 以 HTTP 模式手动启动 Serena MCP 服务器，并向客户端提供该 URL。

请参阅下方的[快速开始](#quick-start)部分了解如何上手。

## 编程语言支持与语义分析能力

Serena 提供了一套基于代码符号理解的通用代码查询与编辑功能。借助这些能力，你的智能体发现并编辑代码的方式，就像经验丰富的开发者利用 IDE 功能一样自然。即使在非常庞大和复杂的项目中，Serena 也能高效地找到正确的上下文并采取正确操作！

支撑这些能力的技术有两种可选方案：

* **语言服务器（Language Servers）**实现语言服务器协议（LSP）——这是默认使用的免费/开源替代方案。
* **Serena JetBrains 插件**，它利用你 JetBrains IDE 强大的代码分析与编辑能力（付费插件；提供试用版）。

你可以根据偏好和需求选择其中一种后端。

### 语言服务器

Serena 集成了一个强大的抽象层，用于集成实现 LSP 的语言服务器。底层语言服务器通常是开源项目，或至少可免费使用。

使用 Serena 的语言服务器后端时，我们提供**对 40 多种编程语言的支持**，包括 Ada / SPARK、AL、Angular、Ansible、Bash、BSL、C#、C/C++、Clojure、Crystal、CUE、Dart、Elixir、Elm、Erlang、Fortran、F#、GDScript、GLSL、Go、Groovy、Haskell、Haxe、HLSL、HTML、Java、JavaScript、JSON、Julia、Kotlin、Lean 4、Lua、Luau、Markdown、MATLAB、mSL、Nix、OCaml、Perl、PHP、PowerShell、Python、R、Ruby、Rust、Scala、SCSS / Sass / CSS、Solidity、Svelte、Swift、TOML、TypeScript、WGSL、YAML 和 Zig。

### Serena JetBrains 插件

付费的 Serena JetBrains 插件（提供试用版）充分利用了你 JetBrains IDE 的强大代码分析能力。该插件自然支持 JetBrains IDE 所支持的所有编程语言和框架，包括 IntelliJ IDEA、PyCharm、Android Studio、WebStorm、PhpStorm、RubyMine、GoLand 等（暂不支持 Rider 和 CLion）。

<a href="https://plugins.jetbrains.com/plugin/28946-serena/"><img src="docs/_static/images/jetbrains-marketplace-button.png"></a>

有关插件的详细使用说明，请参阅我们的[文档页面](https://oraios.github.io/serena/02-usage/025_jetbrains_plugin.html)。

## 功能特性

Serena 提供了丰富的工具用于高效代码检索、编辑和重构，并配备了一套内存系统以支持长期运行的智能体工作流。

鉴于其功能广泛，Serena 通过提供多层配置系统来适应你的需求。

<details>
<summary>详情</summary>

### 代码检索

Serena 的检索工具允许智能体在符号层面探索代码库，无需读取整个文件即可理解结构和关系。

| 功能                       | 语言服务器 | JetBrains 插件 |
|----------------------------------|------------------|------------------|
| 查找符号                      | 支持              | 支持              |
| 符号概览（文件大纲）   | 支持              | 支持              |
| 查找引用符号         | 支持              | 支持              |
| 在项目依赖中搜索   | --               | 支持              |
| 类型层次结构                   | --               | 支持              |
| 查找声明                 | 支持*             | 支持              |
| 查找实现             | 支持**            | 支持              |
| 查询外部项目          | 支持              | 支持              |
| 诊断/检查          | 支持              | 支持              |

*: Will generally not work for declarations in external dependencies. <br>
**: Only available for some languages, limited by the language server functionality. 

### 代码重构

如果没有精确的重构工具，智能体将被迫依赖不可靠且消耗大量 Token 的搜索替换操作。

| 功能                                | 语言服务器   | JetBrains 插件                  |
|-------------------------------------------|--------------------|-----------------------------------|
| 重命名                                    | 支持（仅限符号） | 支持（符号、文件、目录） |
| 移动（符号、文件、目录）            | --                 | 支持                               |
| 内联                                    | --                 | 支持                               |
| 传播删除（移除未使用的代码）  | --                 | 支持                               |

### 符号编辑

Serena 的符号编辑工具比常规替代方案更不易出错，且大幅节省 Token。

| 功能             | 语言服务器  | JetBrains 插件 |
|------------------------|-------------------|------------------|
| 替换符号体    | 支持               | 支持              |
| 在符号后插入    | 支持               | 支持              |
| 在符号前插入   | 支持               | 支持              |
| 安全删除            | 支持               | 支持              |

### 交互式调试

该功能仅限 JetBrains 插件使用。Serena 支持一款高度通用的调试工具，允许智能体通过持续的 REPL 风格界面设置断点、检查变量、评估表达式并控制执行流程。

### 基础功能

除了语义能力外，Serena 还提供了一套基础工具以完善功能。当你在 Claude Code 或 Codex 等智能体运行框架内使用 Serena 时，这些工具默认通常会被禁用，因为外层框架已提供重叠的文件、搜索和 Shell 功能。

- **`search_for_pattern`** – 跨代码库的灵活正则表达式搜索 
- **`replace_content`** – 针对智能体优化的基于正则和字面量的文本替换
- **`list_dir` / `find_file`** – 目录列表与文件搜索
- **`read_file`** – 读取文件或文件片段
- **`execute_shell_command`** – 执行 Shell 命令（如构建、测试、代码检查）

### 内存管理

内存系统是长期运行智能体工作流的基础，尤其是在需要跨会话、用户和项目共享知识时。尽管设计简洁，我们收到了许多用户的积极反馈，他们倾向于将 Serena 的内存管理系统与智能体的内部系统（例如 `AGENTS.md` 文件）结合使用。如果你偏好其他方案，也可以轻松将其禁用。

### 可配置性

通过简单调整几行 YAML，即可灵活地按场景配置 Serena 的激活工具、工具描述、提示词（prompt）、语言后端细节等众多方面。为实现这一点，Serena 提供了多个层级（可组合）的配置选项：

* 全局配置
* MCP 启动命令（CLI）配置
* 项目级配置（支持本地覆盖）
* 执行上下文特定配置（例如针对特定客户端）
* 动态可组合的配置片段（模式）

</details>

## 快速开始

**前置条件**。Serena 由 *uv* 管理，[安装 uv](https://docs.astral.sh/uv/getting-started/installation/) 是唯一必需的前置步骤。

> [!NOTE]
> 使用语言服务器后端时，可能需要安装额外的依赖项以支持特定语言；详见[语言支持](https://oraios.github.io/serena/01-about/020_programming-languages.html)页面。

**安装 Serena**。通过 uv 安装 Serena 的命令如下：

```bash
uv tool install -p 3.13 serena-agent
```

安装成功后，你的 Shell 中即可使用 `serena` 命令。

**初始化 Serena**。要初始化 Serena 并验证配置是否正确，只需运行：

```bash
serena init
```

默认情况下，这将配置 Serena 使用语言服务器后端。若要改用 JetBrains 后端，请添加参数 `-b JetBrains`（详见[JetBrains 插件文档页面](https://oraios.github.io/serena/02-usage/025_jetbrains_plugin.html)以获取更多使用说明）。无论选择哪种方式，你都会收到一条成功消息，表明 Serena 已成功初始化。

**配置你的客户端**。要将 Serena 连接到你偏好的 MCP 客户端，通常需要在[你的客户端中配置启动命令](https://oraios.github.io/serena/02-usage/030_clients.html)。点击链接可获取针对 Claude Code、Codex、Claude Desktop、支持 MCP 的 IDE 以及其他客户端（如本地和 Web GUI）的具体设置指南。 

> [!TIP]
> 快速上手虽然简单，但 Serena 是一款功能强大的工具包，拥有众多配置选项。我们强烈建议你通读[用户指南](https://oraios.github.io/serena/02-usage/000_intro.html)以充分利用 Serena。
> 
> 特别是，我们推荐阅读以下内容：
>   * [Serena 的项目工作流](https://oraios.github.io/serena/02-usage/040_workflow.html) 以及
>   * [配置 Serena](https://oraios.github.io/serena/02-usage/050_configuration.html)。

## 用户指南

有关如何高效使用 Serena 的详细操作说明，请参阅[用户指南](https://oraios.github.io/serena/02-usage/000_intro.html)。

## 致谢

Serena 的很大一部分功能，尤其是多语言支持，由开源社区贡献。我们非常感谢众多使这一切成为可能的贡献者，他们也在塑造 Serena 今日的面貌中发挥了重要作用。

<!-- mcp-name: io.github.oraios/serena -->