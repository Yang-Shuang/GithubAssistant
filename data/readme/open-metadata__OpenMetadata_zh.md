<br /><br />
<p align="center">
    <a href="https://open-metadata.org">
        <img alt="Logo" src="https://github.com/open-metadata/OpenMetadata/assets/40225091/e794ced8-7220-4393-8efc-3faf93bfb503" width="49%">
    </a>
</p>

<p align="center"><b>用 OpenMetadata 赋能你的数据之旅</b></p>

<div align="center">
    
![Commit Activity](https://img.shields.io/github/commit-activity/m/open-metadata/OpenMetadata?style=for-the-badge)
[![Release](https://img.shields.io/github/release/open-metadata/OpenMetadata/all.svg?style=for-the-badge)](https://github.com/open-metadata/OpenMetadata/releases)

</div>

# OpenMetadata

## 面向数据与 AI 的开放语义上下文平台

OpenMetadata 是一个开源平台，用于为人类、AI 助手和智能体（agents）构建可信的数据上下文和业务语义。

OpenMetadata 将技术元数据、数据质量信号、数据血缘关系、列级血缘、所有权、使用情况、策略、对话记录、术语表、分类体系、指标、领域和数据产品整合到一个统一的元数据知识图谱中。凭借 120+ 连接器、开放元数据标准、语义搜索、API、SDK 和 MCP 服务器，OpenMetadata 为每个用户和 AI 系统提供治理良好的上下文，使其能够发现、理解、信任并使用数据。

AI 不需要另一个原始数据库连接器。AI 需要的是上下文（context）。

OpenMetadata 提供以下上下文：
- 存在哪些数据
- 数据的含义是什么
- 谁拥有这些数据
- 数据如何被使用
- 数据来源何处
- 数据流向何方
- 数据是否新鲜、经过测试且值得信赖
- 适用哪些业务概念、术语表词条、分类和策略
- 哪些下游资产、仪表板、管道、指标和机器学习模型依赖于它

---

## 目录

- [为什么在 AI 场景下使用 OpenMetadata？](#why-openmetadata-for-ai)
- [上下文：为 AI 提供数据的完整视图](#context-give-ai-the-full-picture-of-your-data)
- [语义：为 AI 赋予业务含义](#semantics-give-ai-business-meaning)
- [知识图谱与本体论（Ontologies）](#knowledge-graphs-and-ontologies)
- [自动化：利用 AI 激活上下文与语义](#automation-activate-context-and-semantics-with-ai)
- [你能构建什么](#what-you-can-build)
- [工作原理](#how-openmetadata-works)
- [MCP：连接 AI 助手与智能体](#mcp-connect-ai-assistants-and-agents)
- [语义搜索（Semantic Search）](#semantic-search)
- [OpenMetadata 标准](#openmetadata-standards)
- [核心平台能力](#core-platform-capabilities)
- [快速开始](#quickstart)
- [文档与社区](#documentation-and-community)
- [贡献指南](#contributing)
- [许可证](#license)

---

## 为什么在 AI 场景下使用 OpenMetadata？

AI 不仅需要数据访问权限，还需要上下文、语义、信任度、血缘关系、治理能力和运营感知。

将 AI 助手直接连接到数据库、数仓、仪表板或管道，只能让它获得对数据结构的基础访问权限。这不足以让 AI 理解数据的含义、是否可信、由谁拥有、如何受管，以及哪些下游系统依赖于它。

OpenMetadata 为 AI 系统提供发现、理解、治理和使用企业数据所需的上下文和语义。

OpenMetadata 通过结合以下四项能力来实现这一目标：
1. **Context（上下文）** — 来自数据生态系统的技术、运营、信任和血缘元数据。
2. **Semantics（语义）** — 通过术语表、指标、分类、领域、策略和本体论提供的业务含义。
3. **Knowledge Graph（知识图谱）** — 连接资产、列、人员、团队、策略、血缘关系、质量和业务概念的关系网络。
4. **Automation（自动化）** — MCP、语义搜索、API、SDK、事件和工作流，使 AI 助手和智能体能够基于受管元数据采取行动。

借助 OpenMetadata，AI 可以回答以下问题：
- 这个指标的含义是什么？
- 哪些数据集支撑了这个仪表板？
- 谁拥有这个数据产品？
- 该数据集是否经过认证、新鲜且高质量？
- 此列的变更会影响哪些下游仪表板或机器学习模型？
- 即使名称不同，哪些资产与客户购买行为相关？
- 哪些列包含敏感的客户信息？
- 哪些术语表词条和业务概念适用于这个数据集？

---

## 上下文：为 AI 提供数据的完整视图

上下文是描述数据在组织内如何存在、表现、变化、流动和使用情况的元数据。

OpenMetadata 从你的整个数据栈中收集上下文，并将其连接到一个统一的元数据图谱中。

### 技术元数据（Technical Metadata）

OpenMetadata 让 AI 能够访问以下技术元数据：
- 数据库、模式（schema）、表、列、主题（topic）、仪表板、图表、管道、API、搜索索引、机器学习模型和存储资产
- 模式结构、列名、数据类型、约束、描述、示例查询、关联关系和服务元数据
- 服务配置、采集元数据和运营元数据
- 所有者、团队、用户、角色（persona）、领域、数据产品和使用模式

### 数据质量与信任信号（Data Quality and Trust Signals）

AI 不应将每个数据集都视为同等可信。

OpenMetadata 让 AI 能够访问以下信任信号：
- 数据质量测试
- 测试套件与测试结果
- 新鲜度检查（freshness checks）
- 数据量检查
- 空值、唯一性、分布和自定义测试
- 分析结果（profiling results）
- 可观测性信号
- 数据质量历史记录
- 事件、警报和运营健康状态信号

### 数据血缘与影响分析（Data Lineage and Impact）

AI 需要理解数据的来源与去向。

OpenMetadata 捕获以下信息：
- 上游和下游血缘关系
- 表级血缘
- 仪表板血缘
- 管道血缘
- 指标血缘
- 机器学习模型血缘
- API 与主题依赖关系
- 全域数据资产的影响分析

### 列级血缘（Column-Level Lineage）

为了实现精确的 AI 推理，仅表级血缘是不够的。

OpenMetadata 帮助 AI 理解：
- 哪些源列生成了哪些下游列
- 数据列在转换过程中的流转路径
- 哪些仪表板、报告、指标或机器学习模型依赖于特定列
- 当某一列发生变更时，可能引发的问题

### 集成自 120+ 数据服务（Connected from 120+ Data Services）

OpenMetadata 从数据库、数仓、数据湖、仪表板、管道、消息系统、机器学习平台、存储系统、API、搜索系统和元数据系统中整合这些上下文。

上下文可以回答以下问题：
- 存在哪些数据？
- 数据来源何处？
- 谁拥有它？
- 数据是否新鲜？
- 数据是否经过测试？
- 数据是否可信？
- 哪些系统依赖于它？
- 如果发生变更会发生什么？

---

## 语义：为 AI 赋予业务含义

语义是构建在技术上下文之上的业务含义层。

如果没有语义，AI 可能会看到名为 `cust_id`、`acct_id` 或 `buyer_key` 的列，但可能不知道这些字段代表的是客户、账户、买家、家庭还是法律实体。

OpenMetadata 让团队能够在元数据图谱中定义、治理和连接业务含义。

### 业务概念（Business Concepts）

定义对业务至关重要的概念，例如：
- Customer（客户）
- Account（账户）
- Order（订单）
- Revenue（收入）
- Product（产品）
- Consent（授权/同意）
- Churn（流失率）
- Risk（风险）
- Lifetime Value（客户终身价值）
- Net Retention（净留存率）
- Active User（活跃用户）
- Sensitive Data（敏感数据）

### 术语表与术语词条（Glossaries and Glossary Terms）

OpenMetadata 让团队能够创建受管词汇库，包含：
- 业务定义
- 同义词和缩写
- 所有者与审核人
- 相关词条
- 层级结构
- 指向表、列、仪表板、指标和数据产品的链接

### 指标与关键绩效指标（Metrics and KPIs）

指标是 AI 最重要的语义对象之一。

OpenMetadata 帮助 AI 理解：
- 指标的含义
- 计算方式
- 所有者
- 使用的仪表板
- 支撑的数据表
- 定义的术语表词条
- 依赖的下游消费者

### 分类与标签（Classifications and Tags）

OpenMetadata 让团队能够使用受管标签对数据进行分类和标记，例如：
- PII（个人身份信息）
- Sensitive（敏感）
- Confidential（机密）
- Certified（已认证）
- Deprecated（已弃用）
- Tier 1（一级）
- Finance（财务）
- Marketing（营销）
- GDPR / HIPAA / SOX
- ML Feature（机器学习特征）
- Customer Data（客户数据）

### 领域与数据产品（Domains and Data Products）

OpenMetadata 通过以下方式将资产连接到业务所有权边界：
- Domains（领域）
- Data Products（数据产品）
- Teams、Owners、Policies、Personas 和 Data Product Consumers（团队、所有者、策略、角色和数据产品消费者）

### 策略与治理（Policies and Governance）

OpenMetadata 将语义与治理能力连接起来，使 AI 系统能够基于具备策略感知能力的上下文进行推理，而不仅仅是元数据。

这包括：
- Ownership（所有权）、Stewardship（治理责任/管家职责）
- Classification（分类）、Access Control Context（访问控制上下文）、Certification（认证）
- Review Workflows（审核工作流）、Governance Policies（治理策略）、Lifecycle States（生命周期状态）

语义可以回答以下问题：
- 这些数据是什么意思？
- 该列代表什么业务概念？
- 该指标是否已正式定义？
- 该资产是否经过认证？
- 数据是否敏感？
- 适用哪些术语表词条？
- 哪个领域拥有这个数据产品？

---

## 知识图谱与本体论（Ontologies）

OpenMetadata 将上下文和语义整合到一个统一的元数据知识图谱中。

该图谱不仅存储数据资产，还存储数据资产、人员、团队、策略、质量测试、血缘关系、分类、术语表词条、指标、领域和数据产品之间的关系。

这使得 OpenMetadata 成为面向 AI 的语义上下文层。

示例关系：
```text
Table ──hasColumn────────────> Column
Column ──classifiedAs────────> PII
Column ──represents──────────> Customer Identifier
Table ──ownedBy──────────────> Data Engineering Team
Table ──partOf───────────────> Customer 360 Data Product
Dashboard ──dependsOn────────> Table
Metric ──definedBy───────────> Glossary Term
Pipeline ──produces──────────> Table
Column ──flowsTo─────────────> Column
Test Case ──validates────────> Table
Domain ──contains────────────> Data Product
Glossary Term ──relatedTo────> Business Concept
Policy ──governs─────────────> Classification
```

借助该图谱，AI 可以跨关系进行推理：
- 哪些数据集支撑了这个仪表板？
- 这个指标的含义是什么？
- 谁拥有这个数据产品？
- 该表是否新鲜、经过认证且高质量？
- 此列的变更会影响哪些下游仪表板或机器学习模型？
- 即使名称不同，哪些资产与客户购买行为相关？
- 哪些列代表敏感的客户信息？
- 哪些业务概念与此数据产品相关联？

### 本体论与语义互操作性（Ontologies and Semantic Interoperability）

OpenMetadata 建立在开放元数据标准之上。

[OpenMetadata Standards](https://openmetadatastandards.org/) 提供了用于实现元数据互操作性管理的模式、本体论和语义规范，包括：
- 元数据实体、API、配置、事件和关系的 JSON Schema
- 适用于语义网、关联数据和知识图谱用例的 RDF/OWL 本体论
- 用于验证的 SHACL Shapes（形状约束）
- 用于语义互操作的 JSON-LD Contexts（上下文）
- 治理、血缘关系、质量、可观测性、团队、用户、策略和事件的标准

这些标准使 OpenMetadata 不仅仅是一个目录。它成为了互操作性语义元数据、关联数据和大型企业知识图谱的基础设施。

---

## 自动化：利用 AI 激活上下文与语义

OpenMetadata 使元数据图谱具备可操作性（actionable）。

AI 助手、编码智能体、数据团队、治理团队和应用程序可以通过以下方式利用 OpenMetadata：
- MCP
- Semantic Search（语义搜索）
- APIs / SDKs / events / webhooks / ingestion workflows / metadata applications

### MCP Server

OpenMetadata 内置了 MCP 服务器，允许 AI 助手和兼容 MCP 的客户端通过自然语言与元数据图谱进行交互。

借助 OpenMetadata MCP，AI 助手可以：
- 搜索元数据、运行语义搜索、检索实体详情
- 检查上下游血缘关系
- 创建术语表和术语词条、创建血缘关系
- 更新描述、标签、所有者及其他元数据
- 列出数据质量测试定义、创建数据质量测试用例
- 分析数据质量故障的根本原因（root causes）

快速开始使用 MCP：
[OpenMetadata MCP Server Documentation](https://docs.open-metadata.org/how-to-guides/mcp)

### Semantic Search（语义搜索）

语义搜索允许用户和 AI 助手通过含义进行搜索，而不仅仅是精确关键词匹配。

例如，用户可以提问：
> Find tables related to customer purchase behavior and transaction history.

即使查询词中的精确词汇未出现在资产名称中，OpenMetadata 也能返回概念上相关的资产。

这有助于 AI 回答以下问题：
- 哪些数据集与客户行为相关？
- 我们有哪些用于收入预测的仪表板？
- 展示与用户参与度指标相关的资产。
- 查找处理财务合规数据的管道。

### AI SDK

开发者可以使用 OpenMetadata 的 AI SDK，以编程方式构建利用 OpenMetadata MCP 工具的自定义 AI 应用。

AI SDK 使 AI 应用能够从 Python、TypeScript 和 Java 中调用 OpenMetadata 上下文。

### APIs, Events, and Webhooks（API、事件与 Webhook）

OpenMetadata 暴露了 API、事件和 Webhook，以便团队能够在其数据生态系统中自动化元数据工作流。

你可以使用它们来：
- 接入并更新元数据
- 响应元数据变更
- 触发治理工作流
- 集成协作工具
- 构建自定义元数据应用
- 跨系统同步上下文

### Coding Agents and AI Assistants（编码智能体与 AI 助手）

OpenMetadata 可连接到兼容 MCP 的助手和智能体，例如：
- Claude Desktop / Claude Code / Goose / Cursor / VS Code / Codex / custom LLM applications / internal enterprise AI assistants

这使得编码智能体和数据助手在生成 SQL、dbt 模型、文档、测试、迁移计划或影响分析之前，能够理解模式结构、术语定义、所有权、血缘关系、质量要求和下游依赖。

---

## 你能构建什么

### AI Data Discovery（AI 数据发现）

在你的元数据图谱上提出自然语言问题，查找相关资产，即使名称和关键词不完全匹配也能找到。

示例：
> Find datasets related to customer purchase behavior and transaction history.

### Trusted AI Assistants（可信 AI 助手）

将 AI 响应建立在受管元数据之上：所有权、描述、术语表词条、标签、分类体系、质量信号、新鲜度、使用情况和血缘关系。

示例：
> Explain what this dashboard measures and whether the underlying data is trusted.

### Impact Analysis Agents（影响分析智能体）

询问如果表、列、管道、仪表板、指标或机器学习特征发生变更，哪些内容会受到影响。

示例：
> What downstream dashboards and ML models are affected if `customer_id` changes in this table?

### Governance Automation（治理自动化）

使用智能体建议描述、分配术语表词条、识别敏感数据、创建分类体系、提议所有权并管理治理责任工作流。

示例：
> Review this new table, suggest glossary terms, and identify possible PII columns.

### Data Quality Automation（数据质量自动化）

利用 AI 工作流创建测试、总结失败原因、识别根本问题并推荐修复步骤。

示例：
> Investigate why this data quality test failed and identify upstream changes that may have caused it.

### Semantic Knowledge Graphs（语义知识图谱）

使用 OpenMetadata Standards、RDF/OWL、JSON-LD、SHACL 和 OpenMetadata 的实体关系构建互操作性元数据知识图谱。

示例：
> Find all assets related to customer risk that contain sensitive data and are used by revenue dashboards.

### Developer and Coding Agent Workflows（开发者与编码智能体工作流）

将编码智能体连接到 OpenMetadata，使其在生成代码、查询语句、dbt 模型、测试或迁移计划之前，能够理解模式结构、所有权、血缘关系、业务定义和质量要求。

示例：
> Generate a dbt model for this customer table and include tests based on OpenMetadata quality expectations.

---

## 工作原理

OpenMetadata 围绕一个开放的、以模式优先（schema-first）的元数据图谱构建。

```text
                  ┌──────────────────────────────────────────┐
                  │              Data Ecosystem              │
                  │ Warehouses | Lakes | BI | Pipelines | ML │
                  │ APIs | Topics | Storage | Search | SaaS  │
                  └─────────────────────┬────────────────────┘
                                        │
                              120+ Connectors
                                        │
                                        ▼
┌────────────────────────────────────────────────────────────────────┐
│                         OpenMetadata                               │
│                                                                    │
│  Context Layer                                                     │
│  - technical metadata                                              │
│  - quality and observability signals                               │
│  - table and column-level lineage                                  │
│  - ownership, usage, domains, data products                        │
│                                                                    │
│  Semantics Layer                                                   │
│  - business concepts                                               │
│  - glossaries and glossary terms                                   │
│  - classifications and tags                                        │
│  - metrics and KPIs                                                │
│  - ontologies and semantic standards                               │
│                                                                    │
│  Knowledge Graph                                                   │
│  - assets, people, teams, policies, lineage, quality, semantics    │
└─────────────────────────────────────┬──────────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────┐
        ▼                             ▼                             ▼
   Semantic Search                  APIs                         MCP Server
        │                             │                             │
        └─────────────────────────────┼─────────────────────────────┘
                                      ▼
                         AI Assistants and Agents
              Claude | Claude Code | Cursor | VS Code | Codex
                    Goose | Custom Apps | AI SDK Workflows
```

### 平台组件（Platform Components）

OpenMetadata 由五个核心层组成：

1. **Open Metadata Standards**  
   用于元数据互操作性的规范模式、API、RDF/OWL 本体论、SHACL Shapes、JSON-LD Contexts 和事件模型。
2. **Metadata Store and Knowledge Graph**  
   中央存储库，用于存储和连接元数据实体、关系、质量信号、使用情况、血缘关系、所有权和语义。
3. **Ingestion Framework and Connectors**  
   可插拔框架，用于从数据库、数仓、仪表板、管道、消息系统、机器学习平台、存储系统、API 等收集元数据。
4. **APIs, Search, Events, and Webhooks**  
   用于消费、更新、搜索、订阅和自动化元数据的接口。
5. **MCP and AI SDK**  
   面向 AI 的工具，将 OpenMetadata 的上下文和语义暴露给助手、编码智能体和自定义 LLM 应用。

---

## MCP：连接 AI 助手与智能体

OpenMetadata 的 MCP 服务器允许 AI 助手和智能体通过自然语言与你的元数据图谱进行交互。

使用 MCP 为 AI 助手提供对 OpenMetadata 上下文的受管访问权限，包括描述、所有权、血缘关系、术语表词条、标签、分类体系、数据质量结果和语义搜索。

### MCP Tools（MCP 工具）

OpenMetadata MCP 工具包括：

| Tool | What it does |
| --- | --- |
| `search_metadata` | 跨表、仪表板、管道、主题、术语表、指标等进行搜索 |
| `semantic_search` | 基于含义和上下文进行搜索，超越关键词匹配 |
| `get_entity_details` | 检索特定实体的详细元数据 |
| `get_entity_lineage` | 检索实体的上游和下游血缘关系 |
| `create_glossary` | 创建新的术语表 |
| `create_glossary_term` | 创建术语词条 |
| `create_lineage` | 在实体之间创建血缘边（edge） |
| `patch_entity` | 更新描述、标签和所有者等元数据 |
| `get_test_definitions` | 列出数据质量测试定义 |
| `create_test_case` | 创建数据质量测试用例 |
| `root_cause_analysis` | 分析数据质量故障的根本原因 |

### Supported MCP Workflows（支持的 MCP 工作流）

OpenMetadata 文档包含以下环境的设置指南：
- Claude Desktop / Claude Code / Goose / Cursor / VS Code
- Semantic Search through MCP

Codex 和其他兼容 MCP 的编码智能体可以将 OpenMetadata MCP 端点用作外部上下文和工具服务器。

快速开始：
[OpenMetadata MCP Server Documentation](https://docs.open-metadata.org/v1.12.x/how-to-guides/mcp)

### MCP Endpoint（MCP 端点）

```text
https://<YOUR-OPENMETADATA-SERVER>/mcp
```

### Example Prompts（示例提示词）

连接 MCP 客户端后，可尝试以下提示词：

```text
What is the definition of the Revenue metric?

Show me the lineage of the data feeding the Executive Revenue dashboard.

Who owns the Customer 360 data product and when was it last updated?

Find tables related to customer purchase behavior and transaction history.

Which downstream dashboards are affected if this column changes?

Create a glossary term for Net Retention and link it to related metrics.
```

---

## Semantic Search（语义搜索）

语义搜索允许用户和 AI 助手通过含义查找数据资产，而不仅仅是精确关键词匹配。

启用语义搜索后，OpenMetadata 可将自然语言查询转换为向量嵌入，并搜索概念上相关的元数据资产。

示例：
```text
Find tables related to customer purchase behavior and transaction history.
```

这可以返回以下相关资产：
```text
order_transactions
buyer_activity
customer_events
revenue_orders
```

语义搜索有助于：
- 自然语言发现（natural-language discovery）
- AI 数据探索
- 基于概念的搜索
- 跨领域资产发现
- 即使名称不同也能找到关联数据
- 将 LLM 响应锚定在相关的元数据上下文中

了解更多：
[Semantic Search MCP Tool](https://docs.open-metadata.org/v1.12.x/how-to-guides/mcp/semantic-search)

---

## OpenMetadata Standards（OpenMetadata 标准）

OpenMetadata 建立在开放元数据标准之上。

[OpenMetadata Standards](https://openmetadatastandards.org/) 是 OpenMetadata 背后模式、本体论和规范的开源托管地。

它提供：
- 700+ JSON Schemas，涵盖元数据实体、API、配置、事件和关系
- RDF/OWL 本体论，适用于语义网、关联数据和知识图谱用例
- SHACL Shapes，用于元数据验证
- JSON-LD Contexts，用于语义互操作性
- API 和事件模式，用于搜索、Feed、Webhook 和批量操作
- 治理、血缘关系、质量、可观测性、团队、用户、角色、策略和事件的标准

OpenMetadata Standards 实现了：
- 互操作性元数据管理
- 语义元数据建模
- 企业知识图谱构建
- 关联数据和 RDF 集成
- 使用 SHACL 进行元数据验证
- 基于模式优先设计的可扩展性

了解更多：
[OpenMetadata Standards](https://openmetadatastandards.org/)

---

## 核心平台能力（Core Platform Capabilities）

### Discovery and Understanding（发现与理解）
- asset search and discovery（资产搜索与发现）
- semantic search（语义搜索）
- descriptions and documentation（描述与文档）
- sample data and usage context（示例数据与使用上下文）
- ownership and stewardship（所有权与治理责任）
- conversations, tasks, and announcements（对话、任务与公告）

### Governance and Semantics（治理与语义）
- glossaries and glossary terms（术语表与术语词条）
- classifications and tags（分类体系与标签）
- metrics and KPIs（指标与关键绩效指标）
- domains and data products（领域与数据产品）
- policies and roles（策略与角色）
- certification and lifecycle states（认证与生命周期状态）

### Data Quality and Observability（数据质量与可观测性）
- test cases and test suites（测试用例与测试套件）
- profiling（数据分析/画像）
- freshness, volume, null, uniqueness, and distribution checks（新鲜度、数据量、空值、唯一性和分布检查）
- custom tests（自定义测试）
- data quality dashboards（数据质量仪表板）
- alerts and incidents（警报与事件）
- root-cause analysis workflows（根本原因分析工作流）

### Lineage and Impact Analysis（血缘关系与影响分析）
- table lineage（表级血缘）
- column-level lineage（列级血缘）
- dashboard lineage（仪表板血缘）
- pipeline lineage（管道血缘）
- metric lineage（指标血缘）
- ML model lineage（机器学习模型血缘）
- upstream and downstream impact analysis（上下游影响分析）

### Collaboration（协作）
- conversations / tasks / announcements / notifications（对话/任务/公告/通知）
- ownership workflows / documentation workflows / shared stewardship between producers and consumers（所有权工作流/文档工作流/生产者和消费者之间的共享治理责任）

### Security and Access Control（安全与访问控制）
- authentication / authorization / roles and policies（认证/授权/角色与策略）
- SSO integration / bot and user tokens / MCP authentication / governed metadata actions（SSO 集成/机器人和用户令牌/MCP 认证/受管元数据操作）

### Extensibility and Automation（可扩展性与自动化）
- APIs / SDKs / webhooks / events / applications（API/SDK/Webhook/事件/应用）
- ingestion framework / custom connectors / custom properties / MCP tools / AI SDK workflows（接入框架/自定义连接器/自定义属性/MCP 工具/AI SDK 工作流）

---

## 快速开始（Quickstart）

### 1. Try OpenMetadata（试用 OpenMetadata）

使用沙箱探索 OpenMetadata：
[OpenMetadata Sandbox](https://sandbox.open-metadata.org)

### 2. Install OpenMetadata（安装 OpenMetadata）

按照安装指南操作：
[OpenMetadata Quickstart](https://docs.open-metadata.org/latest/quick-start)

### 3. Ingest Metadata（接入元数据）

连接你的数据源并构建元数据图谱。

从以下开始：
- a warehouse or database（数仓或数据库）
- a BI/dashboard tool（BI/仪表板工具）
- an orchestration or pipeline system（编排或管道系统）
- data quality and profiling（数据质量与分析）
- lineage ingestion（血缘接入）

### 4. Build Context（构建上下文）

添加 AI 所需的运营和信任元数据：
- descriptions / owners / teams / domains / data products（描述/所有者/团队/领域/数据产品）
- quality tests / freshness checks / usage / lineage / column-level lineage（质量测试/新鲜度检查/使用情况/血缘关系/列级血缘）

### 5. Add Semantics（添加语义）

添加业务含义：
- glossaries / glossary terms / classifications / tags（术语表/术语词条/分类体系/标签）
- metrics / KPIs / policies / domains / data products（指标/KPI/策略/领域/数据产品）

### 6. Enable Semantic Search（启用语义搜索）

配置语义搜索，以便用户和 AI 助手能够通过含义进行搜索。

了解更多：
```text
https://docs.open-metadata.org/v1.12.x/how-to-guides/mcp/semantic-search
```

### 7. Connect an MCP Client（连接 MCP 客户端）

在 OpenMetadata 中安装或启用 MCP 应用，并连接你首选的兼容 MCP 的客户端。

MCP 端点：
```text
https://<YOUR-OPENMETADATA-SERVER>/mcp
```

MCP 指南：
```text
https://docs.open-metadata.org/v1.12.x/how-to-guides/mcp
```

### 8. Build Custom AI Applications（构建自定义 AI 应用）

使用 AI SDK 将任何 LLM 连接到 OpenMetadata 的 MCP 工具。

AI SDK 文档：
```text
https://docs.open-metadata.org/v1.12.x/api-reference/sdk/ai-sdk
```

---

## 文档与社区（Documentation and Community）

- Documentation: [docs.open-metadata.org](https://docs.open-metadata.org/)
- MCP Server: [OpenMetadata MCP Documentation](https://docs.open-metadata.org/v1.12.x/how-to-guides/mcp)
- OpenMetadata Standards: [openmetadatastandards.org](https://openmetadatastandards.org/)
- Website: [open-metadata.org](https://open-metadata.org/)
- Slack Community: [slack.open-metadata.org](https://slack.open-metadata.org/)
- Blog: [blog.open-metadata.org](https://blog.open-metadata.org/)

---

## 开源与企业级 AI（Open Source and Enterprise AI）

OpenMetadata 是元数据、上下文、语义、治理、质量、血缘关系、API、MCP 和 AI SDK 工作流的开源基础。

如需托管企业功能、AI 智能体、自动化、AI Studio、企业 MCP 工作流、商业支持和托管运营，请参阅 Collate：
- [Collate](https://www.getcollate.io/)
- [Collate AI](https://www.getcollate.io/collate-ai)

---

## 贡献指南（Contributing）

我们欢迎社区的贡献。

你可以通过以下方式参与贡献：
- 改进元数据模式与标准
- 添加连接器
- 优化接入工作流
- 增强 MCP 工具
- 提升语义搜索能力
- 补充文档
- 修复 Bug
- 改善 UI/UX
- 提出新的治理、血缘关系、质量和 AI 用例

请参阅仓库中的贡献指南以开始。

---


## Stargazers（星标用户）

[![Stargazers of @open-metadata/OpenMetadata repo](http://reporoster.com/stars/open-metadata/OpenMetadata)](https://github.com/open-metadata/OpenMetadata/stargazers)

## License
OpenMetadata is released under [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)