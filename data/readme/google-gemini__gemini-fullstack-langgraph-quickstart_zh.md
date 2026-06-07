# Gemini 全栈 LangGraph 快速入门

本项目展示了一个全栈应用程序，采用 React 前端和由 LangGraph 驱动的后台 Agent（智能体）。该 Agent 旨在对用户查询进行深入研究：动态生成搜索词、使用 Google Search 查询网络、反思结果以识别知识缺口，并迭代优化搜索过程，直到提供有据可查的答案。此应用展示了如何使用 LangGraph 和 Google Gemini 模型构建研究增强型对话 AI。

<img src="./app.png" title="Gemini Fullstack LangGraph" alt="Gemini Fullstack LangGraph" width="90%">

## 功能特性

- 💬 全栈应用，包含 React 前端与 LangGraph 后端。
- 🧠 由 LangGraph Agent 驱动，支持高级研究与对话式 AI。
- 🔍 使用 Google Gemini 模型动态生成搜索查询。
- 🌐 集成 Google Search API 进行网络研究。
- 🤔 通过反思推理识别知识缺口并优化搜索。
- 📄 根据收集的资料生成带引用的答案。
- 🔄 开发期间前后端均支持热重载（Hot-reloading）。

## 项目结构

项目主要分为两个目录：

-   `frontend/`：包含使用 Vite 构建的 React 应用。
-   `backend/`：包含 LangGraph/FastAPI 应用，含研究 Agent 逻辑。

## 快速开始：开发与本地测试

按照以下步骤在本地运行应用程序以进行开发和测试。

**1. 环境准备：**

-   Node.js 和 npm（或 yarn/pnpm）
-   Python 3.11+
-   **`GEMINI_API_KEY`**：后端 Agent 需要配置 Google Gemini API Key。
    1. 进入 `backend/` 目录。
    2. 复制 `backend/.env.example` 文件并命名为 `.env`。
    3. 打开 `.env` 文件，填入你的 Gemini API Key：`GEMINI_API_KEY="YOUR_ACTUAL_API_KEY"`

**2. 安装依赖：**

**后端：**

```bash
cd backend
pip install .
```

**前端：**

```bash
cd frontend
npm install
```

**3. 运行开发服务器：**

**后端与前端：**

```bash
make dev
```
此命令将同时启动前后端开发服务器。打开浏览器并访问前端开发服务器地址（例如 `http://localhost:5173/app`）。

_或者，你也可以分别单独运行后端和前端开发服务器。对于后端，在 `backend/` 目录中打开终端并执行 `langgraph dev`。后端 API 将运行在 `http://127.0.0.1:2024`，同时会自动打开浏览器访问 LangGraph UI。对于前端，在 `frontend/` 目录中打开终端并执行 `npm run dev`。前端服务将运行在 `http://localhost:5173`。_

## 后端 Agent 工作原理（概览）

后端的核心是一个定义在 `backend/src/agent/graph.py` 中的 LangGraph Agent。其工作流程如下：

<img src="./agent.png" title="Agent Flow" alt="Agent Flow" width="50%">

1.  **生成初始查询**：根据你的输入，使用 Gemini 模型生成一组初始搜索词。
2.  **网络研究**：针对每个查询，结合 Google Search API 与 Gemini 模型查找相关网页。
3.  **反思与知识缺口分析**：Agent 会分析搜索结果，判断信息是否充足或是否存在知识缺口。该反思过程由 Gemini 模型执行。
4.  **迭代优化**：如果发现缺口或信息不足，将生成后续查询并重复网络研究与反思步骤（最多循环配置的次数）。
5.  **生成最终答案**：当研究被认为充分后，Agent 会使用 Gemini 模型将收集的信息整合成连贯的答案，并附上网页来源的引用。

## CLI 示例

如需快速解决单次提问，你可以通过命令行直接执行该 Agent。脚本 `backend/examples/cli_research.py` 会运行 LangGraph Agent 并输出最终答案：

```bash
cd backend
python examples/cli_research.py "What are the latest trends in renewable energy?"
```


## 部署

在生产环境中，后端服务器会提供优化后的前端静态构建文件。LangGraph 需要 Redis 实例和 Postgres 数据库。Redis 用作发布-订阅（pub-sub）代理，以支持后台任务实时流式输出。Postgres 用于存储助手、线程、运行记录，持久化线程状态与长期记忆，并以“恰好一次”语义管理后台任务队列的状态。有关如何部署后端服务器的更多详情，请参阅 [LangGraph 文档](https://langchain-ai.github.io/langgraph/concepts/deployment_options/)。下面是一个构建包含优化前端和后端服务的 Docker 镜像并通过 `docker-compose` 运行的示例：

_注意：运行 `docker-compose.yml` 示例需要配置 LangSmith API Key，你可前往 [LangSmith](https://smith.langchain.com/settings) 获取。_

_注意：如果你未运行 `docker-compose.yml` 示例或未将后端服务暴露至公网，请将 `frontend/src/App.tsx` 文件中的 `apiUrl` 更新为你的实际主机地址。目前该值在 docker-compose 环境下默认为 `http://localhost:8123`，开发环境下为 `http://localhost:2024`。_

**1. 构建 Docker 镜像：**

   在**项目根目录**下运行以下命令：
   ```bash
   docker build -t gemini-fullstack-langgraph -f Dockerfile .
   ```
**2. 启动生产服务器：**

   ```bash
   GEMINI_API_KEY=<your_gemini_api_key> LANGSMITH_API_KEY=<your_langsmith_api_key> docker-compose up
   ```

打开浏览器访问 `http://localhost:8123/app/` 即可查看应用。API 服务将运行在 `http://localhost:8123`。

## 技术栈

- [React](https://reactjs.org/)（配合 [Vite](https://vitejs.dev/)） - 用于构建前端用户界面。
- [Tailwind CSS](https://tailwindcss.com/) - 用于样式设计。
- [Shadcn UI](https://ui.shadcn.com/) - 提供组件库。
- [LangGraph](https://github.com/langchain-ai/langgraph) - 用于构建后端研究 Agent。
- [Google Gemini](https://ai.google.dev/models/gemini) - LLM，用于查询生成、反思推理与答案整合。

## 许可证

本项目采用 Apache License 2.0 开源协议。详见 [LICENSE](LICENSE) 文件。