# 基于 LangChain 和 LangGraph 的 AI PDF 聊天机器人与智能体

该单体仓库（monorepo）是一个可自定义的 AI 聊天机器人智能体模板示例。它“导入”PDF 文档，将向量嵌入存储到向量数据库（Supabase）中，随后利用 LangChain 和 LangGraph 作为编排框架，通过 OpenAI（或其他 LLM 提供商）回答用户查询。

此模板也是书籍《Learning LangChain (O'Reilly)》[链接]的配套示例：使用 LangChain 和 LangGraph 构建 AI 与 LLM 应用。

> [!IMPORTANT]
> 本项目已停止积极维护，保留在此仅供参考。请勿期望我们会回复新的 issue 或 pull request。

**聊天机器人界面效果如下：**

<img width="1096" alt="Screenshot 2025-02-20 at 05 39 55" src="https://github.com/user-attachments/assets/3a9ddea7-b718-476b-bdae-38839be20c12" />

## 目录

1. [功能特性](#features)
2. [架构概览](#architecture-overview)
3. [前置条件](#prerequisites)
4. [安装步骤](#installation)
5. [环境变量配置](#environment-variables)
   - [前端变量](#frontend-variables)
   - [后端变量](#backend-variables)
6. [本地开发](#local-development)
   - [运行后端服务](#running-the-backend)
   - [运行前端服务](#running-the-frontend)
7. [使用方法](#usage)
   - [上传/导入 PDF 文件](#uploadingingesting-pdfs)
   - [提问](#asking-questions)
   - [查看聊天记录](#viewing-chat-history)
8. [生产环境构建与部署](#production-build--deployment)
9. [自定义智能体](#customizing-the-agent)
10. [故障排除](#troubleshooting)
11. [后续步骤](#next-steps)

---

## 功能特性

- **文档导入图（Ingestion Graph）**：上传并解析 PDF 为 `Document` 对象，随后将向量嵌入存储到向量数据库（本例使用 Supabase）。
- **检索图（Retrieval Graph）**：处理用户提问，判断是进行文档检索还是直接回答，然后生成带有引用参考的简洁回复。
- **流式响应**：服务端向客户端 UI 实时流式传输部分响应结果。
- **LangGraph 集成**：基于 LangGraph 的状态机方法构建，用于编排导入与检索流程、可视化智能体工作流，并调试图中的每一步骤。  
- **Next.js 前端**：支持文件上传、实时聊天，并可轻松通过 React 组件和 Tailwind CSS 进行扩展。

---

## 架构概览

```ascii
┌─────────────────────┐    1. Upload PDFs    ┌───────────────────────────┐
│Frontend (Next.js)   │ ────────────────────> │Backend (LangGraph)       │
│ - React UI w/ chat  │                      │ - Ingestion Graph         │
│ - Upload .pdf files │ <────────────────────┤   + Vector embedding via  │
└─────────────────────┘    2. Confirmation   │     SupabaseVectorStore   │
(storing embeddings in DB)

┌─────────────────────┐    3. Ask questions  ┌───────────────────────────┐
│Frontend (Next.js)   │ ────────────────────> │Backend (LangGraph)       │
│ - Chat + SSE stream │                      │ - Retrieval Graph         │
│ - Display sources   │ <────────────────────┤   + Chat model (OpenAI)   │
└─────────────────────┘ 4. Streamed answers  └───────────────────────────┘

```
- **Supabase**：用作向量存储，在查询时存储和检索相关文档。  
- **OpenAI**（或其他 LLM 提供商）：用于语言模型推理。  
- **LangGraph**：编排导入、路由和生成回复的“图”步骤。  
- **Next.js** (React)：驱动用户上传 PDF 和实时聊天的用户界面。

系统由以下部分组成：
- **后端**：一个 Node.js/TypeScript 服务，包含用于以下目的的 LangGraph 智能体“图”：
  - **导入（Ingestion）** (`src/ingestion_graph.ts`) - 处理文档的索引与导入
  - **检索（Retrieval）** (`src/retrieval_graph.ts`) - 基于已导入文档进行问答
  - **配置** (`src/shared/configuration.ts`) - 管理后端 API 的配置，包括模型提供商和向量存储
- **前端**：一个 Next.js/React 应用，提供 Web UI 供用户上传 PDF 并与 AI 对话。

---

## 前置条件

1. **Node.js v18+**（推荐使用 Node v20）。
2. **Yarn**（也可使用 npm，但该单体仓库已预配置为 Yarn）。
3. **Supabase 项目**（若计划将嵌入向量存储在 Supabase；参见[设置 Supabase](https://supabase.com/docs/guides/getting-started)）。
   - 你需要：
     - `SUPABASE_URL`
     - `SUPABASE_SERVICE_ROLE_KEY`
     - 一个名为 `documents` 的表和一个用于向量相似度搜索的函数 `match_documents`（参见[LangChain 文档中的设置指南](https://js.langchain.com/docs/integrations/vectorstores/supabase/)）。
4. **OpenAI API Key**（或其他 LLM 提供商的密钥，需由 LangChain 支持）。
5. **LangChain API Key**（免费且可选，但强烈建议用于调试和追踪你的 LangChain/LangGraph 应用）。了解更多请参见[此处](https://docs.smith.langchain.com/administration/how_to_guides/organization_management/create_account_api_key)

---

## 安装步骤

1. **克隆**仓库：

   ```bash
   git clone https://github.com/mayooear/ai-pdf-chatbot-langchain.git
   cd ai-pdf-chatbot-langchain
   ```

2.	安装依赖（从单体仓库根目录执行）：

yarn install

	3.	在后端和前端配置环境变量。详见 `.env.example` 文件。

## 环境变量配置

项目依赖环境变量来配置密钥和端点。每个子项目（后端和前端）都有独立的 `.env.example`。将其复制为 `.env` 并填入你的信息。

### 前端变量

在 frontend 目录下创建 .env 文件：

`cp frontend/.env.example frontend/.env`

```
    NEXT_PUBLIC_LANGGRAPH_API_URL=http://localhost:2024
    LANGCHAIN_API_KEY=your-langsmith-api-key-here # 可选：LangSmith API 密钥
    LANGGRAPH_INGESTION_ASSISTANT_ID=ingestion_graph
    LANGGRAPH_RETRIEVAL_ASSISTANT_ID=retrieval_graph

    LANGCHAIN_TRACING_V2=true # 可选：启用 LangSmith 追踪

    LANGCHAIN_PROJECT="pdf-chatbot" # 可选：LangSmith 项目名称
```

### 后端变量

在 backend 目录下创建 .env 文件：

`cp backend/.env.example backend/.env`

```
    OPENAI_API_KEY=your-openai-api-key-here
    SUPABASE_URL=your-supabase-url-here
    SUPABASE_SERVICE_ROLE_KEY=your-supabase-service-role-key-here

    LANGCHAIN_TRACING_V2=true # 可选：启用 LangSmith 追踪

    LANGCHAIN_PROJECT="pdf-chatbot" # 可选：LangSmith 项目名称
```

**环境变量说明：**

-   `NEXT_PUBLIC_LANGGRAPH_API_URL`：你的 LangGraph 后端服务器运行的 URL。本地开发默认值为 `http://localhost:2024`。 
-   `LANGCHAIN_API_KEY`：你的 LangSmith API 密钥。此为可选，但强烈建议用于调试和追踪应用。
-   `LANGGRAPH_INGESTION_ASSISTANT_ID`：文档导入用的 LangGraph 智能体 ID。默认为 `ingestion_graph`。
-   `LANGGRAPH_RETRIEVAL_ASSISTANT_ID`：问答用的 LangGraph 智能体 ID。默认为 `retrieval_graph`。
-   `LANGCHAIN_TRACING_V2`：启用追踪功能以便在 LangSmith 平台上调试应用。设为 `true` 以启用。
-   `LANGCHAIN_PROJECT`：你的 LangSmith 项目名称。
-   `OPENAI_API_KEY`：你的 OpenAI API 密钥。
-   `SUPABASE_URL`：你的 Supabase URL。
-   `SUPABASE_SERVICE_ROLE_KEY`：你的 Supabase 服务角色密钥。



## 本地开发

该单体仓库使用 Turborepo 管理后端和前端项目。你可以分别运行它们进行开发。

### 运行后端服务

1.	进入 backend 目录：

```bash
cd backend
```

2.	安装依赖（若在根目录已执行过 `yarn install`，则无需重复）。

3.	以开发模式启动 LangGraph：

```bash
yarn langgraph:dev
```

这将在默认端口 2024 上启动本地 LangGraph 服务器。它应会重定向你到一个用于与 LangGraph 服务器交互的 UI。[LangGraph Studio 指南](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/)

### 运行前端服务

1.	进入 frontend 目录：

```bash
cd frontend
```

2.	启动 Next.js 开发服务器：

```bash
yarn dev
```

这将启动一个本地 Next.js 开发服务器（默认端口为 3000）。

在浏览器中访问 http://localhost:3000 即可使用界面。

## 使用方法

当两个服务均运行后：

1.	使用 LangGraph Studio UI 与 LangGraph 服务器交互，确保工作流按预期运行。

2.	访问 http://localhost:3000 使用聊天机器人界面。

3.	通过页面底部的文件上传按钮上传一个小型 PDF 文档。这将触发导入图提取文本，并通过前端 `app/api/ingest` 路由将嵌入向量存储到 Supabase 中。
	
4.	导入完成后，在聊天输入框中提问。

5.	聊天机器人将通过 `app/api/chat` 路由触检索图，从向量数据库中检索最相关的文档，并结合相关 PDF 上下文（如需）进行回答。


### 上传/导入 PDF 文件

点击聊天输入区域的回形针图标。

选择一个或多个 PDF 文件上传，确保总数不超过 5 个，且每个文件大小低于 10MB（你可以在 `app/api/ingest` 路由中修改这些阈值）。

后端将处理 PDF、提取文本，并将嵌入向量存储到 Supabase（或你选择的向量存储）中。

### 提问

-	在聊天输入框中输入你的问题。
-	回复将以流式传输实时显示。如果系统检索到了文档，你会看到每条用于回答的文本块旁附有“查看来源”链接。

### 查看聊天记录

-	系统为每个用户会话（前端）创建唯一的对话线程。所有消息均保留在会话状态中。
-	出于演示目的，当前示例 UI 不会将完整对话持久化存储超出本地线程状态的范围，且跨会话不持久。你可以扩展它以在线程数据库中持久化存储。不过，“已导入的文档”是跨会话持久的，因为它们存储在向量数据库中。


## 部署后端

要将你的 LangGraph 智能体部署到云服务，你可以按照此[指南](https://langchain-ai.github.io/langgraph/cloud/quick_start/?h=studio#deploy-to-langgraph-cloud)使用 LangGraph 官方云，或按照此[指南](https://langchain-ai.github.io/langgraph/how-tos/deploy-self-hosted/)自行托管。

## 部署前端
前端可部署到任何支持 Next.js 的托管平台（如 Vercel、Netlify 等）。

确保在部署环境中设置相关环境变量。特别是，请确认 `NEXT_PUBLIC_LANGGRAPH_API_URL` 指向你的已部署后端 URL。

## 自定义智能体

你可以对后端和前端的智能体进行自定义配置。

### 后端

-	在配置文件 `src/shared/configuration.ts` 中，你可以更改默认配置（即向量存储、k 值和过滤参数），这些配置被导入和检索图共享。在后端，配置可用于图中的每个节点；或从前端传入一个配置对象到图的客户端。
-	你可以在 `src/retrieval_graph/prompts.ts` 文件中调整提示词（prompts）。
-	若想更改检索模型，可在 `src/shared/retrieval.ts` 中实现：添加一个新的检索器函数来封装所需的向量存储客户端，然后更新 `makeRetriever` 函数以返回新的检索器。


### 前端

-	你可以在 `app/api/ingest` 路由中修改文件上传限制。
-	在 `constants/graphConfigs.ts` 中，你可以更改发送给导入和检索图的默认配置对象。这包括模型提供商、k 值（需检索的源文档数量）以及检索器提供商（即向量存储）。


## 故障排除
1. `.env` 未加载
   -	确保已将 `backend` 和 `frontend` 目录下的 `.env.example` 复制为 `.env`。
   -	检查环境变量是否正确，并重启开发服务器。

2. Supabase 向量存储问题
   -	确保已按官方文档配置你的 Supabase 实例（包含 `documents` 表和 `match_documents` 函数）。请查阅 LangChain 关于 Supabase 集成的官方文档。

3. OpenAI 报错
   -	仔细检查你的 `OPENAI_API_KEY`。确保账户余额/配额充足。

4. LangGraph 未运行
   -	若 `yarn langgraph:dev` 失败，请确认 Node 版本 >= 18，且已安装所有依赖项。

5. 网络错误
   -	前端必须指向正确的 `NEXT_PUBLIC_LANGGRAPH_API_URL`。默认值为 `http://localhost:2024`。

## 后续步骤

如果你希望为此项目做出贡献，欢迎提交 pull request。请确保代码文档完善，并在测试文件中包含相应的测试用例。

若想深入了解如何使用 LangChain 和 LangGraph 构建 AI 聊天机器人与智能体，推荐阅读《Learning LangChain (O'Reilly)》[链接]。