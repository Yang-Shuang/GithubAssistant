# [Spring AI Alibaba](https://java2ai.com)

[![License](https://img.shields.io/badge/license-Apache%202-4EB1BA.svg)](https://www.apache.org/licenses/LICENSE-2.0.html)
[![CI Status](https://github.com/alibaba/spring-ai-alibaba/actions/workflows/build-and-test.yml/badge.svg?branch=main)](https://github.com/alibaba/spring-ai-alibaba/actions/workflows/build-and-test.yml)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/alibaba/spring-ai-alibaba)
[![Maven Central](https://img.shields.io/badge/Maven%20Central-v1.1.2.2-blue)](https://central.sonatype.com/artifact/com.alibaba.cloud.ai/spring-ai-alibaba/1.1.2.2)
[![gitleaks badge](https://img.shields.io/badge/protected%20by-gitleaks-blue)](https://github.com/gitleaks/gitleaks)

<html>
    <h3 align="center">
      生产就绪（Production-ready）的框架，用于构建智能体、工作流和多智能体应用。
    </h3>
    <h3 align="center">
      <a href="https://java2ai.com/docs/quick-start/" target="_blank">智能体框架文档</a>,
      <a href="https://java2ai.com/docs/frameworks/graph-core/quick-start/" target="_blank">Graph 文档</a>,
      <a href="https://java2ai.com/ecosystem/spring-ai/reference/concepts/" target="_blank">Spring AI</a>,
      <a href="https://github.com/alibaba/spring-ai-alibaba/tree/main/examples" target="_blank">示例</a>.
    </h3>
</html>

## 架构

<p align="center">
    <img src="./docs/imgs/architecture-new.png" alt="architecture" style="max-width: 740px; height: auto" />
</p>

**Spring AI Alibaba Admin** 是一个一站式的智能体（Agent）平台，支持可视化的智能体开发、可观测性监控、评估以及 MCP 管理等。它还集成了 Dify 等开源低代码平台，支持从 DSL 快速迁移至 Spring AI Alibaba 项目。

**Spring AI Alibaba Agent Framework**（智能体框架）是一个智能体开发框架，内置了**上下文工程（Context Engineering）**和**人在回路（Human In The Loop）**支持，可快速构建智能体。对于需要更复杂流程控制的场景，该框架提供了内置的工作流组件，如 `SequentialAgent`、`ParallelAgent`、`RoutingAgent` 和 `LoopAgent`。

**Spring AI Alibaba Graph** 作为智能体框架的底层运行时，提供持久化、工作流编排和流式处理等长运行有状态智能体所需的核心能力。与智能体框架相比，用户可基于 Graph API 构建更灵活的多智能体工作流。

## 核心特性

* **[多智能体编排](https://github.com/alibaba/spring-ai-alibaba/tree/main/examples/multiagent-patterns)**：使用内置的 `SequentialAgent`、`ParallelAgent`、`RoutingAgent` 和 `LoopAgent` 模式组合多个智能体，以执行复杂任务。

* **[多模态支持](https://github.com/alibaba/spring-ai-alibaba/tree/main/examples/multimodal)**：ReactAgent 支持文本与媒体输入（图像理解）；基于工具的 ReactAgent 可生成图片或音频。

* **[语音智能体](https://github.com/alibaba/spring-ai-alibaba/tree/main/examples/voice-agent)**：基于 WebSocket 的实时语音智能体，支持流式音频或文本输入，并以生成的音频作为响应。

* **[上下文工程](https://java2ai.com/docs/frameworks/agent-framework/tutorials/hooks)**：内置上下文工程策略的最佳实践以提升智能体的可靠性与性能，包括人在回路、上下文压缩、上下文编辑、模型与工具调用限制、工具重试、规划及动态工具选择等。

* **[基于图的工作流](https://java2ai.com/docs/frameworks/graph-core/quick-start)**：提供基于图的运行时和工作流 API，支持条件路由、嵌套图、并行执行和状态管理。支持将工作流导出为 PlantUML 和 Mermaid 格式。

* **[A2A（智能体间通信）支持](https://java2ai.com/docs/frameworks/agent-framework/advanced/a2a)**：集成 Nacos 实现智能体到智能体的通信，支持跨服务的分布式智能体协调与协作。

* **[丰富的模型、工具与 MCP 支持](https://java2ai.com/integration/chatmodels/dashScope)**：依托 Spring AI 的核心概念，支持多种大语言模型（LLM）提供商（如 DashScope、OpenAI 等）、工具调用以及模型上下文协议（MCP）。

* **[一站式智能体平台](https://java2ai.com/ecosystem/admin/quick-start)**：以可视化方式构建智能体，支持无代码部署或导出为独立的 Java 项目。

<p align="center">
    <img src="./docs/imgs/saa-admin.png" alt="architecture" style="max-width: 740px; height: auto" />
</p>

## 快速开始

### 前置条件

* 需要 JDK 17+。
* 选择你的大语言模型（LLM）提供商并获取 API-KEY。

### 快速运行聊天机器人

社区在 [examples/chatbot](https://github.com/alibaba/spring-ai-alibaba/tree/main/examples/chatbot) 提供了一个聊天机器人示例。

1. 下载代码。

	```shell
	git clone --depth=1 https://github.com/alibaba/spring-ai-alibaba.git
	cd spring-ai-alibaba
	```

2. 启动 ChatBot。

	启动前，请先设置 API-KEY（访问 <a href="https://bailian.console.aliyun.com/?apiKey=1&tab=api#/api" target="_blank">阿里云百炼</a> 获取）：
	```shell
	# 本示例使用 'spring-ai-alibaba-starter-dashscope'，如需了解如何配置 OpenAI/DeepSeek，请访问 https://java2ai.com。
	export AI_DASHSCOPE_API_KEY=your-api-key
	```
	
	```shell
	# 若使用 mvnw 则无需提前安装 Maven。
	./mvnw -pl examples/chatbot spring-boot:run
	```

3. 与 ChatBot 对话。

	打开浏览器并访问 [http://localhost:8080/chatui/index.html](http://localhost:8080/chatui/index.html) 即可开始对话。
	
<p align="center">
	<img src="./docs/imgs/chatbot-chat-ui.gif" alt="chatbot-ui" style="max-width: 740px; height: auto" />
</p>

## 聊天机器人代码说明

1. 添加依赖

	```xml
	<dependencies>
	  <dependency>
	    <groupId>com.alibaba.cloud.ai</groupId>
	    <artifactId>spring-ai-alibaba-agent-framework</artifactId>
	    <version>1.1.2.0</version>
	  </dependency>
	  <!-- 假设你计划使用 DashScope 模型。有关如何选型，请参阅相关文档。-->
	  <dependency>
	    <groupId>com.alibaba.cloud.ai</groupId>
	    <artifactId>spring-ai-alibaba-starter-dashscope</artifactId>
	    <version>1.1.2.1</version>
	  </dependency>
	</dependencies>
	```

2. 定义 ChatBot
   
   有关编写 ChatBot 的更多详情，请查阅官网的 [快速开始](https://java2ai.com/docs/quick-start) 文档。

## 📚 文档
* [概述](https://java2ai.com/docs/overview) - 框架高层概览
* [快速开始](https://java2ai.com/docs/quick-start) - 使用一个简单的智能体入门
* [智能体框架教程](https://java2ai.com/docs/frameworks/agent-framework/tutorials/agents) - 逐步操作指南
* [使用 Graph API 构建复杂工作流](https://java2ai.com/docs/frameworks/agent-framework/advanced/context-engineering) - 深入的多智能体与工作流构建用户指南
* [Spring AI 基础](https://java2ai.com/ecosystem/spring-ai/reference/concepts) - AI 应用核心概念，包括 ChatModel、MCP、Tool、Messages 等。
* [聊天记忆（Chat Memory）](https://docs.spring.io/spring-ai/reference/api/chatclient.html#chat-memory) - Spring AI 关于聊天记忆仓库及使用的参考文档

## 项目结构

本项目包含以下核心组件：

* spring-ai-alibaba-agent-framework: 专为构建智能体设计的多智能体框架，内置上下文工程最佳实践。
* spring-ai-alibaba-graph: 智能体框架的底层运行时。建议开发者使用智能体框架，但直接使用 Graph API 也完全没问题。
* spring-ai-alibaba-admin: 一站式智能体平台，支持可视化开发、可观测性监控、评估及 MCP 管理等。
* spring-ai-alibaba-studio: 内置的 UI 工具，用于以可视化方式快速调试智能体。
* spring-boot-starters: 集成 Agent Framework 与 Nacos 的启动器，提供 A2A 和动态配置功能。

## Spring AI Alibaba 生态系统
 Repository | Description | ⭐
  --- | --- | ---
| [Spring AI Alibaba Graph](https://github.com/alibaba/spring-ai-alibaba/tree/main/spring-ai-alibaba-graph-core) | 用于构建、管理和部署长运行有状态智能体的底层编排框架与运行时。 | ![GitHub Repo stars](https://img.shields.io/github/stars/alibaba/spring-ai-alibaba?style=for-the-badge&label=)
| [Spring AI Alibaba Admin](https://github.com/spring-ai-alibaba/spring-ai-alibaba-admin) | 智能体应用开发的本地可视化套件，支持项目管理、运行时可视化、链路追踪及智能体评估。 | ![GitHub Repo stars](https://img.shields.io/github/stars/spring-ai-alibaba/spring-ai-alibaba-admin?style=for-the-badge&label=)
| [Spring AI Extensions](https://github.com/spring-ai-alibaba/spring-ai-extensions) | Spring AI 核心概念的扩展实现，包括 DashScopeChatModel、MCP 注册中心等。 |  ![GitHub Repo stars](https://img.shields.io/github/stars/spring-ai-alibaba/spring-ai-extensions?style=for-the-badge&label=)
| [Spring AI Alibaba Examples](https://github.com/spring-ai-alibaba/examples) | Spring AI Alibaba 官方示例集合。 |  ![GitHub Repo stars](https://img.shields.io/github/stars/spring-ai-alibaba/examples?style=for-the-badge&label=)
| [JManus](https://github.com/spring-ai-alibaba/jmanus) | 基于 Spring AI Alibaba 实现的 Java 版 Manus，目前已在阿里巴巴集团多项业务中投入使用。 | ![GitHub Repo stars](https://img.shields.io/github/stars/spring-ai-alibaba/jmanus?style=for-the-badge&label=)
| [DataAgent](https://github.com/spring-ai-alibaba/dataagent) | 基于 Spring AI Alibaba 的自然语言转 SQL 项目，支持直接使用自然语言查询数据库，无需编写复杂 SQL。 | ![GitHub Repo stars](https://img.shields.io/github/stars/spring-ai-alibaba/dataagent?style=for-the-badge&label=)
| [DeepResearch](https://github.com/spring-ai-alibaba/deepresearch) | 基于 spring-ai-alibaba-graph 实现的深度研究应用。 | ![GitHub Repo stars](https://img.shields.io/github/stars/spring-ai-alibaba/deepresearch?style=for-the-badge&label=)

## 联系我们

* 钉钉群（Dingtalk Group），搜索 `94405033092` 并加入。

<img src="./docs/imgs/dingding-group.png" style="width: 260px; height: auto"/>

* 微信公众号，扫描下方二维码关注。

<img src="./docs/imgs/wechat-account.jpg" style="width: 260px; height: auto"/>

## 资源
* [AI-Native Application Architecture White Paper](https://developer.aliyun.com/ebook/8479)：**《AI 原生应用架构白皮书》**：由 40 位一线工程师联合编写，15 位行业专家联署。这篇超 20 万字的白皮书是首部全面聚焦 AI 原生应用全生命周期 DevOps 的指南。它系统拆解了核心概念与关键挑战，提供了切实可行的解决方案与架构洞察。


## ⭐ Star 历史

[![Star History Chart](https://starchart.cc/alibaba/spring-ai-alibaba.svg?variant=adaptive)](https://starchart.cc/alibaba/spring-ai-alibaba)

---

<p align="center">
    由 Spring AI Alibaba 团队 ❤️ 打造