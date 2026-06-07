# LangChain4j：用于在 JVM 上构建由 LLM 驱动的应用程序的惯用开源 Java 库

[![Build Status](https://img.shields.io/github/actions/workflow/status/langchain4j/langchain4j/main.yaml?branch=main&style=for-the-badge&label=CI%20BUILD&logo=github)](https://github.com/langchain4j/langchain4j/actions/workflows/main.yaml)
[![Nightly Build](https://img.shields.io/github/actions/workflow/status/langchain4j/langchain4j/nightly_jdk17.yaml?branch=main&style=for-the-badge&label=NIGHTLY%20BUILD&logo=github)](https://github.com/langchain4j/langchain4j/actions/workflows/nightly_jdk17.yaml)
[![CODACY](https://img.shields.io/badge/Codacy-Dashboard-blue?style=for-the-badge&logo=codacy)](https://app.codacy.com/gh/langchain4j/langchain4j/dashboard)

[![Discord](https://img.shields.io/discord/1156626270772269217?logo=discord&style=for-the-badge)](https://discord.gg/JzTFvyjG6R)
[![BlueSky](https://img.shields.io/badge/@langchain4j-follow-blue?logo=bluesky&style=for-the-badge)](https://bsky.app/profile/langchain4j.dev)
[![X](https://img.shields.io/badge/@langchain4j-follow-blue?logo=x&style=for-the-badge)](https://x.com/langchain4j)
[![Maven Version](https://img.shields.io/maven-central/v/dev.langchain4j/langchain4j?logo=apachemaven&style=for-the-badge)](https://search.maven.org/#search|gav|1|g:"dev.langchain4j"%20AND%20a:"langchain4j")


## Introduction

欢迎！

LangChain4j 的目标是简化将 LLM 集成到 Java 应用程序中的过程。

实现方式如下：
1. **统一的 API：**
   大语言模型提供商（如 OpenAI 或 Google Vertex AI）以及嵌入（向量）存储（如 Pinecone 或 Milvus）
   通常使用各自的私有 API。LangChain4j 提供了统一的 API，避免你需要为每个提供商学习并实现特定的接口。
   要试用不同的 LLM 或嵌入存储时，你可以轻松切换它们，而无需重写代码。
   LangChain4j 目前支持 [20+ 主流 LLM 提供商](https://docs.langchain4j.dev/integrations/language-models/)
   以及 [30+ 嵌入存储](https://docs.langchain4j.dev/integrations/embedding-stores/)。
2. **全面的工具箱：**
   自 2023 年初以来，社区一直在构建大量由 LLM 驱动的应用程序，
   并总结出常见的抽象、模式和技巧。LangChain4j 已将这些提炼为实用的代码。
   我们的工具箱涵盖了从底层的提示词模板（prompt templating）、聊天记忆管理、函数调用（function calling），
   到高级模式如 Agent（智能体）和 RAG。
   针对每种抽象，我们提供接口以及基于常见技术的多种即用型实现。
   无论你是要构建聊天机器人，还是开发包含从数据摄入到检索完整流程的 RAG 应用，
   LangChain4j 都提供了丰富的选项。
3. **丰富的示例：**
   这些 [示例](https://github.com/langchain4j/langchain4j-examples) 展示了如何开始创建各种由 LLM 驱动的应用程序，
   为你提供灵感并帮助你快速上手开发。

LangChain4j 的开发始于 2023 年初 ChatGPT 热潮期间。
我们注意到，针对大量现存的 Python 和 JavaScript LLM 库与框架，Java 领域缺乏对应的替代品，
因此我们必须解决这个问题！

**尽管名字相似，但 LangChain4j 并非 Python 版 LangChain 的 Java 移植版本——它是专为 Java 构建的，而非从其他语言移植而来。**
它是一个符合 Java 惯用法的库，从底层设计之初就围绕 Java 规范展开：
类型安全、POJOs、注解、接口、依赖注入、流畅 API（fluent APIs），以及与 Quarkus、Spring Boot、Helidon 和 Micronaut 的一流集成。
其 API、内部实现和发布周期均独立于 Python LangChain 项目。

我们密切关注社区动态，旨在快速引入新技术与集成方案，
确保你能始终掌握最新进展。
该库正处于积极开发中。尽管部分功能仍在完善中，
但核心功能已就绪，你现在就可以开始构建由 LLM 驱动的应用程序了！


## Documentation
文档请参见 [此处](https://docs.langchain4j.dev)。

文档聊天机器人（实验性）可访问 [此处](https://chat.langchain4j.dev/)。


## Getting Started
入门指南请参见 [此处](https://docs.langchain4j.dev/get-started)。


## Code Examples
有关如何使用 LangChain4j 的示例，请参见 [langchain4j-examples](https://github.com/langchain4j/langchain4j-examples) 仓库：
- [纯 Java 示例](https://github.com/langchain4j/langchain4j-examples/tree/main/other-examples/src/main/java)
- [Quarkus 示例](https://github.com/quarkiverse/quarkus-langchain4j/tree/main/samples)（使用 [quarkus-langchain4j](https://github.com/quarkiverse/quarkus-langchain4j) 依赖）
- [Spring Boot 示例](https://github.com/langchain4j/langchain4j-examples/tree/main/spring-boot-example/src/main/java/dev/langchain4j/example)
- [Helidon 示例](https://github.com/helidon-io/helidon-examples/tree/helidon-4.x/examples/integrations/langchain4j)（使用 [io.helidon.integrations.langchain4j](https://mvnrepository.com/artifact/io.helidon.integrations.langchain4j) 依赖）
- [Micronaut 示例](https://github.com/micronaut-projects/micronaut-langchain4j/tree/0.3.x/doc-examples/example-openai-java)（使用 [micronaut-langchain4j](https://micronaut-projects.github.io/micronaut-langchain4j/latest/guide/) 依赖）

## Useful Materials
实用资料请参见 [此处](https://docs.langchain4j.dev/useful-materials)。


## Get Help
如需帮助，请使用 [Discord](https://discord.gg/JzTFvyjG6R) 或 [GitHub Discussions](https://github.com/langchain4j/langchain4j/discussions)。


## Request Features
如有功能需求，请通过 [提交 Issue](https://github.com/langchain4j/langchain4j/issues/new/choose) 告知我们。


## Contribute
贡献指南请参见 [此处](https://github.com/langchain4j/langchain4j/blob/main/CONTRIBUTING.md)。