# Awesome Cursor Rules [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

<p align="center">
  <a href="https://coderabbit.ai/?utm_source=oss&utm_medium=sponsorship&utm_campaign=awesome-cursorrules" target="_blank">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="./LOCKUP_VERTICAL_25D_DARK.png">
      <img alt="Awesome Cursor Logo" src="./LOCKUP_VERTICAL_25D_LIGHT.png" width="500">
    </picture>
  </a>
</p>

Cursor Project Rules（项目规则）通过提供项目特定的指导和可复用的编码规范，增强 Cursor AI 编辑器的行为表现。

[Cursor AI](https://cursor.sh/) 是一款基于 AI 的代码编辑器。Cursor 项目规则是基于 Markdown 的 `.mdc` 文件，存放在 `.cursor/rules/` 目录中，用于告诉 Cursor 在特定项目、文件类型、框架和工作流下应如何表现。

<h2>Sponsorships</h2>
<p align="center">
    <h3><a href="https://coderabbit.ai/?utm_source=oss&utm_medium=sponsorship&utm_campaign=awesome-cursorrules">Coderabbit.ai - 将代码审查时间与 Bug 数量减半。立竿见影。</h3>
	  <a href="https://coderabbit.ai/?utm_source=oss&utm_medium=sponsorship&utm_campaign=awesome-cursorrules">
		  <img alt="CodeRabbit.ai Sponsorship Logo" src="./cr_logo.png" width=350>
	  </a>
	<h3><a href="https://getunblocked.com/unblocked-mcp/?utm_source=oss&utm_medium=sponsorship&utm_campaign=awesome-cursorrules">Unblocked MCP - 用团队知识库为 Cursor 赋能</h3> 
	  <a href="https://getunblocked.com/unblocked-mcp/?utm_source=oss&utm_medium=sponsorship&utm_campaign=awesome-cursorrules">
		  <img alt="Unblocked Sponsorship Logo" src="https://github.com/claire-gong-18/awesome-cursorrules/blob/main/Unblocked-logo-sq-words-over-gradient-1024w.png?raw=true" width=250>
	  </a>
	<h3><a href="https://go.warp.dev/awesome-cursorrules">Warp - 专为多 AI Agent 编码打造的终端</h3>
	  <a href="https://go.warp.dev/awesome-cursorrules">
		  <img alt="Warp Sponsorship Logo" src="https://github.com/user-attachments/assets/8d50d811-fabe-4610-a537-c5a5a9224864" width=350>
	  </a>
</p>

## 目录

- [为什么使用 Cursor 规则](#为什么使用-cursor-规则)
- [规则列表](#规则列表)
  - [前端框架与库](#前端框架与库)
  - [后端与全栈开发](#后端与全栈开发)
  - [移动端开发](#移动端开发)
  - [游戏与图形开发](#游戏与图形开发)
  - [CSS 与样式](#css-与样式)
  - [状态管理](#状态管理)
  - [数据库与 API](#数据库与-api)
  - [测试](#测试)
  - [托管与部署](#托管与部署)
  - [构建工具与开发工作流](#构建工具与开发工作流)
  - [特定语言规范](#特定语言规范)
  - [安全](#安全)
  - [文档编写](#文档编写)
- [相关目录](#相关目录)
- [如何使用](#如何使用)

## 为什么使用 Cursor 规则

Cursor 规则帮助开发者为 Cursor AI 定义项目特定的指令。本仓库采用现代化的 `.mdc` 项目规则格式。

定制化的行为意味着 Cursor 能够响应项目的特定需求，而不仅仅依赖通用的编程知识。规则可以描述本地架构、首选库、常用方法、领域约束以及其他上下文信息，从而使生成的代码更具相关性。

一致性是另一大优势。通过在 `.mdc` 文件中定义编码规范和最佳实践，团队可以引导 Cursor 生成符合项目风格、命名规范、结构和审查期望的代码。

项目规则还能减少重复的手动编辑工作。范围明确的规则能让 Cursor 预先获取可复用的项目知识，因此建议更有可能在首次尝试时就契合代码库，且不太需要反复进行相同的修改。

对于团队而言，共享的 `.cursor/rules/*.mdc` 文件能够确保所有贡献者在使用 AI 辅助时保持一致。无论规则涵盖的是框架使用、安全要求、测试规范还是工作流细节，每个人都可以基于相同的项目特定指南进行开发。

将选定的 `.mdc` 文件添加到 `.cursor/rules/` 目录中，即可在你的项目中直接使用这些规则。

## 规则列表

### 前端框架与库

- [Angular (Novo Elements)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/angular-novo-elements-cursorrules-prompt-file.mdc) - 结合 Novo Elements UI 库进行 Angular 开发。
- [Angular (TypeScript)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/angular-typescript-cursorrules-prompt-file.mdc) - 结合 TypeScript 集成进行 Angular 开发。
- [Astro (TypeScript)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/astro-typescript-cursorrules-prompt-file.mdc) - 结合 TypeScript 集成进行 Astro 开发。
- [Beefree SDK (TypeScript, JavaScript, CSS, HTML, React, Angular, Vue)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/beefreeSDK-nocode-content-editor-cursorrules-prompt-file.mdc) - 将 Beefree SDK 的无代码内容编辑器（用于邮件、页面和弹窗）嵌入 Web 应用。
- [Cursor AI (React, TypeScript, shadcn/ui)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/cursor-ai-react-typescript-shadcn-ui-cursorrules-p.mdc) - 结合 React、TypeScript 和 shadcn/ui 集成进行 Cursor AI 开发。
- [Next.js 15 (React 19, Vercel AI, Tailwind)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/nextjs15-react19-vercelai-tailwind-cursorrules-prompt-file.mdc) - 结合 React 19、Vercel AI 和 Tailwind CSS 集成进行 Next.js 开发。
- [Next.js 15 (Supabase, TypeScript, Security)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/nextjs15-supabase-cursorrules-prompt-file.mdc) - 27 条架构规则防止 AI 幻觉：不安全的认证（getSession vs getUser）、同步参数、已弃用导入、缺失 RLS 以及 Stripe 密钥泄露。专为 Cursor Agent 和 Claude Code 构建。
- [Next.js 14 (Tailwind, SEO)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/cursorrules-cursor-ai-nextjs-14-tailwind-seo-setup.mdc) - 结合 Tailwind CSS 和 SEO 优化进行 Next.js 开发。
- [Next.js (React, Tailwind)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/nextjs-react-tailwind-cursorrules-prompt-file.mdc) - 结合 React 和 Tailwind CSS 集成进行 Next.js 开发。
- [Next.js (React, TypeScript)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/nextjs-react-typescript-cursorrules-prompt-file.mdc) - 结合 React 和 TypeScript 集成进行 Next.js 开发。
- [Next.js (SEO Development)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/nextjs-seo-dev-cursorrules-prompt-file.mdc) - 结合 SEO 优化进行 Next.js 开发。
- [Next.js (Supabase Todo App)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/nextjs-supabase-todo-app-cursorrules-prompt-file.mdc) - 结合 Supabase 集成进行待办事项应用的 Next.js 开发。
- [Next.js (TanStack Query v5)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/nextjs-tanstack-query-cursorrules-prompt-file.mdc) - 使用 TanStack Query v5 的 Next.js App Router，涵盖 HydrationBoundary 模式、Server Actions 作为 mutations 以及乐观更新。
- [Next.js (Type LLM)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/next-type-llm.mdc) - 结合 Type LLM 集成进行 Next.js 开发。
- [Next.js (Tailwind, TypeScript)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/nextjs-tailwind-typescript-apps-cursorrules-prompt.mdc) - 结合 Tailwind CSS 和 TypeScript 集成进行 Next.js 开发。
- [Next.js (TypeScript App)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/nextjs-typescript-app-cursorrules-prompt-file.mdc) - 结合 TypeScript 集成进行 Next.js 开发。
- [Next.js (TypeScript)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/nextjs-typescript-cursorrules-prompt-file.mdc) - 结合 TypeScript 集成进行 Next.js 开发。
- [Next.js (TypeScript, Tailwind)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/nextjs-typescript-tailwind-cursorrules-prompt-file.mdc) - 结合 TypeScript 和 Tailwind CSS 集成进行 Next.js 开发。
- [Next.js (Vercel, Supabase)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/nextjs-vercel-supabase-cursorrules-prompt-file.mdc) - 结合 Vercel 和 Supabase 集成进行 Next.js 开发。
- [Next.js (Vercel, TypeScript)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/nextjs-vercel-typescript-cursorrules-prompt-file.mdc) - 结合 Vercel 和 TypeScript 集成进行 Next.js 开发。
- [Next.js (App Router)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/nextjs-app-router-cursorrules-prompt-file.mdc) - 结合 App Router 集成进行 Next.js 开发。
- [Next.js (Material UI, Tailwind CSS)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/nextjs-material-ui-tailwind-css-cursorrules-prompt.mdc) - 结合 Material UI 和 Tailwind CSS 集成进行 Next.js 开发。
- [Qwik (Basic Setup with TypeScript and Vite)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/qwik-basic-cursorrules-prompt-file.mdc) - 结合 TypeScript 和 Vite 集成进行 Qwik 开发。
- [Qwik (with Tailwind CSS)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/qwik-tailwind-cursorrules-prompt-file.mdc) - 结合 Tailwind CSS 集成进行 Qwik 开发。
- [React Components Creation](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/react-components-creation-cursorrules-prompt-file.mdc) - React 组件创建与开发。
- [React (FormEngine AI Form Builder)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/react-formengine-ai-form-builder-cursorrules-prompt-file.mdc) - 通过截图、PDF、HTML 或文本描述生成 React 表单，并使用经过验证的 FormEngine JSON schema。支持 RSuite、Material UI 或 Mantine 渲染。
- [React (Next.js UI Development)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/react-nextjs-ui-development-cursorrules-prompt-fil.mdc) - 结合 Next.js UI 集成进行 React 开发。
- [React Router v7](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/react-router-v7.mdc) - Framework 模式、数据路由器（Data Routers）、加载器（Loaders）、操作（Actions）、路由模块及渐进式增强。
- [React (TypeScript, Next.js, Node.js)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/react-typescript-nextjs-nodejs-cursorrules-prompt-.mdc) - 结合 TypeScript、Next.js 和 Node.js 集成进行 React 开发。
- [React (TypeScript, Symfony)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/react-typescript-symfony-cursorrules-prompt-file.mdc) - 结合 TypeScript 和 Symfony 集成进行 React 开发。
- [Semiotic (React, D3, Data Visualization)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/semiotic-react-dataviz-cursorrules-prompt-file.mdc) - Semiotic 数据可视化库，支持 30+ 图表类型、MCP Server 及 AI 辅助图表生成。
- [Shopify Theme (Liquid, JavaScript, CSS)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/shopify-theme-dev-liquid.mdc) - Shopify 主题开发，涵盖 Liquid 模板、区块 Schema、前端资源、性能优化及无障碍访问。
- [Solid.js (Basic Setup)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/solidjs-basic-cursorrules-prompt-file.mdc) - Solid.js 基础设置与开发。
- [Solid.js (TypeScript)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/solidjs-typescript-cursorrules-prompt-file.mdc) - 结合 TypeScript 集成进行 Solid.js 开发。
- [Solid.js (Tailwind CSS)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/solidjs-tailwind-cursorrules-prompt-file.mdc) - 结合 Tailwind CSS 集成进行 Solid.js 开发。
- [Svelte 5 vs Svelte 4](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/svelte-5-vs-svelte-4-cursorrules-prompt-file.mdc) - 对比 Svelte 5 与 Svelte 4 的开发实践。
- [SvelteKit (RESTful API, Tailwind CSS)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/sveltekit-restful-api-tailwind-css-cursorrules-pro.mdc) - 结合 RESTful API 和 Tailwind CSS 集成进行 SvelteKit 开发。
- [SvelteKit (Tailwind CSS, TypeScript)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/sveltekit-tailwindcss-typescript-cursorrules-promp.mdc) - 结合 Tailwind CSS 和 TypeScript 集成进行 SvelteKit 开发。
- [SvelteKit (TypeScript Guide)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/sveltekit-typescript-guide-cursorrules-prompt-file.mdc) - 结合 TypeScript 集成进行 SvelteKit 开发。
- [TanStack Router (React)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/tanstack-router-react-cursorrules-prompt-file.mdc) - TanStack Router v1，支持基于文件的路由、类型化参数、搜索验证、加载器、认证守卫及路由预加载。
- [Vue 3 (Nuxt 3 Development)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/vue-3-nuxt-3-development-cursorrules-prompt-file.mdc) - 结合 Nuxt 3 集成进行 Vue 3 开发。
- [Vue 3 (Nuxt 3, TypeScript)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/vue-3-nuxt-3-typescript-cursorrules-prompt-file.mdc) - 结合 TypeScript 集成进行 Vue 3 开发。
- [Vue 3 (Composition API)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/vue3-composition-api-cursorrules-prompt-file.mdc) - 结合 Composition API 集成进行 Vue 3 开发。
- [Vue/Nuxt Full AI Stack](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/vue-claude-stack.mdc) - 为 Vue 3 & Nuxt 3 提供完整的 AI 编码设置，包含 Cursor Project Rules、CLAUDE.md、Copilot 指令及生成技能。

### 后端与全栈开发

- [Cloudflare Workers (Hono, Angular)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/cloudflare-workers-hono-angular-saas-cursorrules-prompt-file.mdc) - 在 Cloudflare Workers 上构建全栈 SaaS 应用，结合 Hono API、Angular 前端、类型化 RPC、D1/Neon 及生产级可观测性。
- [Convex Best Practices](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/convex-cursorrules-prompt-file.mdc) - Convex 开发最佳实践。
- [Deno Integration](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/deno-integration-techniques-cursorrules-prompt-fil.mdc) - Deno 集成技术指南。
- [Drupal 11](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/drupal-11-cursorrules-prompt-file.mdc) - 现代 CMS 开发。
- [Elixir Engineer Guidelines](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/elixir-engineer-guidelines-cursorrules-prompt-file.mdc) - Elixir 工程师指南。
- [Elixir (Phoenix, Docker)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/elixir-phoenix-docker-setup-cursorrules-prompt-fil.mdc) - 结合 Phoenix 和 Docker 集成进行 Elixir 开发。
- [ES Module (Node.js)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/es-module-nodejs-guidelines-cursorrules-prompt-fil.mdc) - ES Module 开发及 Node.js 指南。
- [Go Backend Scalability](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/go-backend-scalability-cursorrules-prompt-file.mdc) - Go 后端可扩展性架构。
- [Go ServeMux REST API](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/go-servemux-rest-api-cursorrules-prompt-file.mdc) - 结合 ServeMux REST API 集成进行 Go 开发。
- [Go (Basic Setup)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/htmx-go-basic-cursorrules-prompt-file.mdc) - Go 基础设置与开发。
- [Go with Fiber](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/htmx-go-fiber-cursorrules-prompt-file.mdc) - 结合 Fiber 集成进行 Go 开发。
- [Go Temporal DSL](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/go-temporal-dsl-prompt-file.mdc) - 结合 Temporal DSL 集成进行 Go 开发。
- [Google ADK](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/google-adk.mdc) - Google Agent Development Kit：Agent、工具、会话、记忆体、制品、评估与部署。
- [HOL (Hedera TypeScript SDK)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/hol-hedera-typescript-cursorrules-prompt-file.mdc) - Hashgraph Online 开发，结合 TypeScript，使用 RegistryBrokerClient 在 Hedera 上构建 AI Agent。
- [HTMX (Basic Setup)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/htmx-basic-cursorrules-prompt-file.mdc) - HTMX 基础设置与开发。
- [HTMX (Flask)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/htmx-flask-cursorrules-prompt-file.mdc) - 结合 Flask 集成进行 HTMX 开发。
- [HTMX (Django)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/htmx-django-cursorrules-prompt-file.mdc) - 结合 Django 集成进行 HTMX 开发。
- [Java (Spring Boot, JPA)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/java-springboot-jpa-cursorrules-prompt-file.mdc) - 结合 Spring Boot 和 JPA 集成进行 Java 开发。
- [Knative (Istio, Typesense, GPU)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/knative-istio-typesense-gpu-cursorrules-prompt-fil.mdc) - 结合 Istio、Typesense 和 GPU 集成进行 Knative 开发。
- [Kotlin Ktor Development](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/kotlin-ktor-development-cursorrules-prompt-file.mdc) - 结合 Ktor 集成进行 Kotlin 开发。
- [Laravel (PHP 8.3)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/laravel-php-83-cursorrules-prompt-file.mdc) - 结合 PHP 8.3 集成进行 Laravel 开发。
- [Laravel (TALL Stack)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/laravel-tall-stack-best-practices-cursorrules-prom.mdc) - Laravel TALL Stack 最佳实践。
- [Manifest](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/manifest-yaml-cursorrules-prompt-file.mdc) - 基于 YAML 的配置与元数据文件规范。
- [Momen.app (Backend-as-a-Service)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/momen-cursurrules-prompt-file.mdc) - 使用 Momen.app 作为无头 BaaS（Headless BaaS），结合 GraphQL API、Actionflows、AI Agent 和 Stripe 集成构建自定义前端。
- [Node.js (MongoDB)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/nodejs-mongodb-cursorrules-prompt-file-tutorial.mdc) - 结合 MongoDB 集成进行 Node.js 开发。
- [Node.js (MongoDB, JWT, Express, React)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/nodejs-mongodb-jwt-express-react-cursorrules-promp.mdc) - 结合 MongoDB、JWT、Express 和 React 集成进行 Node.js 开发。
- [Rails 8 (Basic Setup)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/rails-cursorrules-prompt-file.mdc) - Rails 基础设置与开发。
- [Python (FastAPI)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/py-fast-api.mdc) - Python FastAPI 后端开发与最佳实践。
- [Python 3.12 (FastAPI Best Practices)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/python-312-fastapi-best-practices-cursorrules-prom.mdc) - Python FastAPI 开发最佳实践。
- [Python (Django Best Practices)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/python-django-best-practices-cursorrules-prompt-fi.mdc) - Python Django 开发最佳实践。
- [Python (FastAPI Best Practices)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/python-fastapi-best-practices-cursorrules-prompt-f.mdc) - Python FastAPI 开发最佳实践。
- [Python (FastAPI Scalable API)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/python-fastapi-scalable-api-cursorrules-prompt-fil.mdc) - Python FastAPI 可扩展 API 集成开发。
- [Python (FastAPI Production Architecture)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/fastapi-production-architecture-cursorrules-prompt-file.mdc) - FastAPI 服务架构：Router/Service/Repository 边界、类型化 Provider 适配器、隔离舱（Bulkhead）、幂等性及领域异常处理。
- [Python (Flask JSON Guide)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/python-flask-json-guide-cursorrules-prompt-file.mdc) - Python Flask JSON 指南。
- [Python LLM & ML Workflow](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/python-llm-ml-workflow-cursorrules-prompt-file.mdc) - Python LLM 与机器学习工作流集成开发。
- [Salesforce (Apex)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/salesforce-apex-cursorrules-prompt-file.mdc) - 结合 Apex 集成进行 Salesforce 开发。
- [TanStack Start](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/tanstack-start-cursorrules-prompt-file.mdc) - 全栈 React 框架，包含 Server Functions、API Routes、defer() 流式传输、SSR 及多平台部署。
- [TypeScript (NestJS Anti-Hallucination)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/nestjs-anti-hallucination-cursorrules-prompt-file.mdc) - 阻止已弃用、幻影或错误的 NestJS 导入、装饰器、Provider、模块及测试模式的规则。
- [TypeScript (NestJS Best Practices)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/typescript-nestjs-best-practices-cursorrules-promp.mdc) - TypeScript NestJS 最佳实践。
- [TYPO3 CMS Extension](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/typo3cms-extension-cursorrules-prompt-file.mdc) - TYPO3 CMS 扩展集成开发。
- [WordPress (PHP, Guzzle, Gutenberg)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/wordpress-php-guzzle-gutenberg-cursorrules-prompt-.mdc) - 结合 PHP、Guzzle 和 Gutenberg 集成进行 WordPress 开发。
- [WordPress (macOS)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/cursorrules-cursor-ai-wordpress-draft-macos-prompt.mdc) - macOS 环境下的 WordPress 开发。
- [WordPress Full AI Stack](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/wordpress-claude-stack.mdc) - 为 WordPress 提供完整的 AI 编码设置——主题、插件、Gutenberg、WooCommerce、ACF、REST API，配合 Cursor Project Rules、CLAUDE.md、Copilot 指令及 5 项生成技能。

### 移动端开发

- [Android Native (Jetpack Compose)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/android-jetpack-compose-cursorrules-prompt-file.mdc) - 结合 Jetpack Compose 集成进行 Android 原生开发。
- [Cursor Rules Pack v2](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/cursor-rules-pack-v2-cursorrules-prompt-file.mdc) - 7 个经过生产验证的示例规则（依赖纪律、错误处理、状态管理、Webhook 安全等）。详见打包 README。
- [Flutter Expert](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/flutter-app-expert-cursorrules-prompt-file.mdc) - Flutter 专家级开发指南。
- [HarmonyOS ArkTS](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/harmony-arkts.mdc) - 组件、状态、资源、生命周期、布局及无障碍访问规范。
- [NativeScript](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/nativescript-cursorrules-prompt-file.mdc) - 跨平台移动应用开发指南。
- [React Native Expo](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/react-native-expo-cursorrules-prompt-file.mdc) - 基于 Expo 的移动应用开发。
- [SwiftUI Guidelines](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/swiftui-guidelines-cursorrules-prompt-file.mdc) - SwiftUI 开发指南。
- [TypeScript (Expo, Jest, Detox)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/typescript-expo-jest-detox-cursorrules-prompt-file.mdc) - 结合 Expo、Jest 和 Detox 集成进行 TypeScript 开发。
- [UIKit Guidelines](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/uikit-guidelines-cursorrules-prompt-file.mdc) - UIKit 开发指南。

### 游戏与图形开发

- [ASCII Simulation Game](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/ascii-simulation-game-cursorrules-prompt-file.mdc) - 基于文本的模拟游戏开发。
- [Blender Python Add-ons](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/blender-python-addon.mdc) - 运算符、面板、属性、注册机制及 API 安全的脚本编写规范。
- [DragonRuby Best Practices](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/dragonruby-best-practices-cursorrules-prompt-file.mdc) - DragonRuby 开发最佳实践集成。
- [GameMaker GML](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/gamemaker-gml.mdc) - GameMaker Language 项目、对象、事件、房间、数据结构及注重性能的游戏逻辑代码。
- [Graphical Apps Development](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/graphical-apps-development-cursorrules-prompt-file.mdc) - 交互式可视化应用开发。
- [Unity (C#)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/unity-cursor-ai-c-cursorrules-prompt-file.mdc) - 结合 C# 集成进行 Unity 开发。

### CSS 与样式

- [Landing Page Image Quality](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/landing-page-image-quality-cursorrules-prompt-file.mdc) - 避免占位符或失效图片 URL，使用稳定视觉资源，并检查 Alt 文本、尺寸、许可协议及响应式行为。
- [Tailwind CSS (Next.js Guide)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/tailwind-css-nextjs-guide-cursorrules-prompt-file.mdc) - 结合 Next.js 集成进行 Tailwind CSS 开发。
- [Tailwind (React, Firebase)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/tailwind-react-firebase-cursorrules-prompt-file.mdc) - 结合 React 和 Firebase 集成进行 Tailwind 开发。
- [Tailwind (shadcn/ui Integration)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/tailwind-shadcn-ui-integration-cursorrules-prompt-.mdc) - 结合 shadcn/ui 集成进行 Tailwind 开发。
- [HTML (Tailwind CSS, JavaScript)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/html-tailwind-css-javascript-cursorrules-prompt-fi.mdc) - 结合 Tailwind CSS 和 JavaScript 集成进行 HTML 开发。
- [JavaScript (Astro, Tailwind CSS)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/javascript-astro-tailwind-css-cursorrules-prompt-f.mdc) - 结合 Astro 和 Tailwind CSS 集成进行 JavaScript 开发。
- [React (Styled Components)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/react-styled-components-cursorrules-prompt-file.mdc) - 结合 Styled Components 集成进行 React 开发。
- [React (Chakra UI)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/react-chakra-ui-cursorrules-prompt-file.mdc) - 结合 Chakra UI 集成进行 React 开发。
- [RTL / Right-to-Left (i18n, Tailwind, React Native)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/rtl-right-to-left-i18n-cursorrules-prompt-file.mdc) - RTL（从右至左）开发，结合逻辑 CSS 属性、Tailwind 逻辑类名、双向文本及 rtlify-ai 自动化审计。
- [Toss-Style Design System](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/toss-style-design-system.mdc) - 克制型产品 UI：受限配色、灰度层级、排版、卡片设计、指标展示、暗色模式及无障碍访问规范。

### 状态管理

- [React (Redux, TypeScript)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/react-redux-typescript-cursorrules-prompt-file.mdc) - 结合 Redux 和 TypeScript 集成进行 React 开发。
- [React (MobX)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/react-mobx-cursorrules-prompt-file.mdc) - 结合 MobX 集成进行 React 开发。
- [React (React Query)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/react-query-cursorrules-prompt-file.mdc) - 结合 React Query 集成进行 React 开发。
- [React (TanStack Router + Query)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/react-tanstack-router-query-cursorrules-prompt-file.mdc) - 结合 TanStack Router v1 和 TanStack Query v5 的 React SPA，实现零加载旋转图标路由及类型安全的服务器状态管理。
- [React (Zustand)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/react-zustand-cursorrules-prompt-file.mdc) - Zustand 状态管理：Store、Selectors、Middleware、持久化及测试规范。
- [TanStack Query v5](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/tanstack-query-v5-cursorrules-prompt-file.mdc) - Query Options、Key Factories、Mutations、乐观更新、无限查询（Infinite Queries）、Suspense 及预取（Prefetching）。
- [Vue (Pinia)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/vue-pinia-cursorrules-prompt-file.mdc) - Vue 3 Pinia 状态管理：Store、Composition API 使用、SSR、持久化及测试。

### 数据库与 API

- [GraphQL (Apollo Client)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/react-graphql-apollo-client-cursorrules-prompt-file.mdc) - 结合 Apollo Client 集成进行 GraphQL 开发。
- [Snowflake Cortex AI](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/snowflake-cortex-ai-cursorrules-prompt-file.mdc) - AI_COMPLETE、AI_CLASSIFY、AI_EXTRACT、Cortex Search 及 RAG 应用开发。
- [Snowflake Data Engineering](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/snowflake-data-engineering-cursorrules-prompt-file.mdc) - Snowflake SQL、数据管道（Dynamic Tables, Streams, Tasks, Snowpipe）、半结构化数据、Snowflake PostgreSQL 及成本优化。
- [Snowflake Snowpark Python & dbt](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/snowflake-snowpark-dbt-cursorrules-prompt-file.mdc) - Snowpark Python（DataFrames, UDFs, Stored Procedures）及结合 Snowflake Adapter 的 dbt。
- [TypeScript (Axios)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/typescript-axios-cursorrules-prompt-file.mdc) - 结合 Axios 集成进行 TypeScript 开发。

### 测试

- [Cypress API Testing](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/cypress-api-testing-cursorrules-prompt-file.mdc) - Cypress API 测试指南。
- [Cypress Accessibility Testing](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/cypress-accessibility-testing-cursorrules-prompt-file.mdc) - Cypress 无障碍测试指南。
- [Cypress Defect Tracking](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/cypress-defect-tracking-cursorrules-prompt-file.mdc) - Cypress 缺陷跟踪指南。
- [Cypress E2E Testing](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/cypress-e2e-testing-cursorrules-prompt-file.mdc) - Cypress E2E 测试指南。
- [Cypress Integration Testing](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/cypress-integration-testing-cursorrules-prompt-file.mdc) - Cypress 集成测试指南。
- [Jest Unit Testing](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/jest-unit-testing-cursorrules-prompt-file.mdc) - Jest 单元测试指南。
- [Playwright API Testing](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/playwright-api-testing-cursorrules-prompt-file.mdc) - Playwright API 测试指南。
- [Playwright Accessibility Testing](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/playwright-accessibility-testing-cursorrules-prompt-file.mdc) - Playwright 无障碍测试指南。
- [Playwright Defect Tracking](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/playwright-defect-tracking-cursorrules-prompt-file.mdc) - Playwright 缺陷跟踪指南。
- [Playwright E2E Testing](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/playwright-e2e-testing-cursorrules-prompt-file.mdc) - Playwright E2E 测试指南。
- [Playwright Integration Testing](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/playwright-integration-testing-cursorrules-prompt-file.mdc) - Playwright 集成测试指南。
- [PR Review (security / performance / tests / architecture)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/pr-review-cursorrules-prompt-file.mdc) - 聚焦 PR 审查，包含严重性分级、文件与行号引用，以及针对安全、性能、测试和架构的独立审查视角。
- [PR Template](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/pr-template-cursorrules-prompt-file.mdc) - PR 模板集成指南。
- [QA Bug Report](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/qa-bug-report-cursorrules-prompt-file.mdc) - QA 缺陷报告规范。
- [TestRail Test Case](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/testrail-test-case-cursorrules-prompt-file.mdc) - TestRail 测试用例集成指南。
- [Vitest Unit Testing](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/vitest-unit-testing-cursorrules-prompt-file.mdc) - Vitest 单元测试指南。
- [Xray Test Case](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/xray-test-case-cursorrules-prompt-file.mdc) - Xray 测试用例集成指南。

### 托管与部署

- [Cloudflare Email to Telegram](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/cloudflare-email-telegram-cursorrules-prompt-file.mdc) - 通过 Cloudflare Email Routing 和 Workers，使用 mail2tg CLI 设置邮件转发至 Telegram。
- [Netlify](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/netlify-official-cursorrules-prompt-file.mdc) - Netlify 官方部署平台集成指南。
- [Vercel](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/vercel-deployment-cursorrules-prompt-file.mdc) - Vercel 部署：Serverless Functions、Edge Runtime、Middleware、缓存、CI/CD 及生产就绪配置。

### 构建工具与开发工作流

- [AI Agent Specialist](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/ai-agent-specialist.mdc) - TypeScript、React、Node.js、清晰架构、测试及 WHY-oriented 工程指导。
- [Alpha Skills](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/alpha-skills-quant-factor-research.mdc) - Cursor 量化因子研究技能：评估因子、运行回测、通过自然语言挖掘新 Alpha。
- [Anti-Over-Engineering](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/anti-overengineering.mdc) - 保持变更范围明确、简单，并直接响应用户需求。
- [Anti-Sycophancy Code Discipline](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/anti-sycophancy-code-discipline-cursorrules-prompt-file.mdc) - 17 条指令阻止最常见的 LLM 编程诚信问题：幻觉 API、虚构签名、虚假自信验证、制造紧迫感妥协、权威驱动软化及自引用注释。将 `.mdc` 放入 `.cursor/rules/` 即可生效。
- [Chrome Extension (JavaScript/TypeScript)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/chrome-extension-dev-js-typescript-cursorrules-pro.mdc) - 结合 JavaScript 和 TypeScript 集成进行 Chrome 扩展开发。
- [Code Guidelines](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/code-guidelines-cursorrules-prompt-file.mdc) - 代码规范指南集成。
- [Code Pair Interviews](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/code-pair-interviews.mdc) - 面试练习与结对编程会话指南。
- [Code Style Consistency](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/code-style-consistency-cursorrules-prompt-file.mdc) - 代码风格一致性规范集成。
- [Embedded MCU / STM32 / HAL](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/embedded-stm32-hal.mdc) - 嵌入式 C/C++ 开发：STM32 HAL、中断、DMA、内存约束及硬件导向测试。
- [Engineering Ticket Template](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/engineering-ticket-template-cursorrules-prompt-file.mdc) - 工程任务单模板集成指南。
- [GitHub Code Quality](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/github-code-quality-cursorrules-prompt-file.mdc) - GitHub 代码质量规范集成。
- [GitHub Instructions](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/github-cursorrules-prompt-file-instructions.mdc) - GitHub 开发指令集成指南。
- [Git Commit Messages](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/git-conventional-commit-messages.mdc) - Git 约定式提交信息规范。
- [Kubernetes (MkDocs Documentation)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/kubernetes-mkdocs-documentation-cursorrules-prompt.mdc) - Kubernetes 结合 MkDocs 文档集成开发。
- [Linux (NVIDIA CUDA, Python)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/linux-nvidia-cuda-python-cursorrules-prompt-file.mdc) - Linux 结合 NVIDIA CUDA 和 Python 集成开发。
- [Network Troubleshooting](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/network-troubleshoot.mdc) - 开发者网络故障安全诊断：目标范围检查、TLS 与代理护栏，以及用户确认的修复方案。
- [Optimize (DRY, SOLID Principles)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/optimize-dry-solid-principles-cursorrules-prompt-f.mdc) - DRY 与 SOLID 原则优化指南。
- [Project Epic Template](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/project-epic-template-cursorrules-prompt-file.mdc) - 项目史诗（Epic）模板集成指南。
- [Python Containerization](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/python-containerization-cursorrules-prompt-file.mdc) - Python 容器化开发指南。
- [Python (GitHub Setup)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/python-github-setup-cursorrules-prompt-file.mdc) - Python GitHub 环境设置集成指南。
- [ROS / ROS2](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/ros-ros2.mdc) - ROS 与 ROS2：包、节点、启动文件、消息、服务、动作、仿真及测试规范。
- [Tauri (Svelte, TypeScript Guide)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/tauri-svelte-typescript-guide-cursorrules-prompt-f.mdc) - Tauri 结合 Svelte 和 TypeScript 指南集成开发。
- [TypeScript Code Convention](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/typescript-code-convention-cursorrules-prompt-file.mdc) - TypeScript 代码规范集成指南。
- [VSCode Extension (Electron/TypeScript)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/vscode-extension-dev-typescript-cursorrules-prompt-file.mdc) - VSCode 扩展结合 Electron 和 TypeScript 集成开发。
- [Web App Optimization](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/web-app-optimization-cursorrules-prompt-file.mdc) - Web 应用优化指南集成。
- [Ankra CLI (Kubernetes Cluster Management)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/ankra-cli.mdc) - Ankra CLI Kubernetes 集群管理集成开发。

### 特定语言规范

- [AutoML and Hyperparameter Optimization](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/automl-hyperparameter-optimization.mdc) - Python ML 模型搜索、验证设计、搜索空间、实验追踪及时序 AutoML。
- [Fortran](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/fortran.mdc) - 现代 Fortran 科学计算：模块、显式接口、Kind 参数、内存安全及测试规范。
- [JavaScript/TypeScript Code Quality](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/javascript-typescript-code-quality-cursorrules-pro.mdc) - JavaScript 与 TypeScript 代码质量集成指南。
- [JavaScript (Chrome APIs)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/javascript-chrome-apis-cursorrules-prompt-file.mdc) - Chrome API 集成开发指南。
- [Optimize (Rell Blockchain Code)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/optimize-rell-blockchain-code-cursorrules-prompt-f.mdc) - Rell 区块链代码优化指南。
- [Pandas (scikit-learn Guide)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/pandas-scikit-learn-guide-cursorrules-prompt-file.mdc) - Pandas 结合 scikit-learn 指南集成开发。
- [Plasticode (Telegram API)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/plasticode-telegram-api-cursorrules-prompt-file.mdc) - Telegram API 集成开发指南。
- [PyQt6 (EEG Processing)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/pyqt6-eeg-processing-cursorrules-prompt-file.mdc) - PyQt6 EEG（脑电图）处理集成指南。
- [Python/TypeScript Guide](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/python--typescript-guide-cursorrules-prompt-file.mdc) - Python 结合 TypeScript 指南集成开发。
- [Python Best Practices](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/python-cursorrules-prompt-file-best-practices.mdc) - Python 最佳实践集成指南。
- [Python Developer](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/python-developer-cursorrules-prompt-file.mdc) - Python 开发者规范集成指南。
- [Python Projects Guide](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/python-projects-guide-cursorrules-prompt-file.mdc) - Python 项目指南集成开发。
- [PySpark ETL Best Practices](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/pyspark-etl-best-practices-cursorrules-prompt-file.mdc) - PySpark ETL：代码风格、Join、窗口函数、Map 操作及 Iceberg 模式最佳实践。
- [PyTorch (scikit-learn)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/pytorch-scikit-learn-cursorrules-prompt-file.mdc) - PyTorch 结合 scikit-learn 集成开发指南。
- [R Best Practices](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/r-cursorrules-prompt-file-best-practices.mdc) - R 语言最佳实践集成指南。
- [Rust](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/rust-general.mdc) - 安全、惯用的 Rust 应用与库开发规范。
- [Solidity (Foundry)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/solidity-foundry-cursorrules-prompt-file.mdc) - Solidity 结合 Foundry 集成开发指南。
- [Solidity (Hardhat)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/solidity-hardhat-cursorrules-prompt-file.mdc) - Solidity 结合 Hardhat 集成开发指南。
- [Solidity (React Blockchain Apps)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/solidity-react-blockchain-apps-cursorrules-prompt-.mdc) - Solidity 结合 React 区块链应用集成开发指南。
- [Solana Wallet-Aware Coding](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/solana-wallet-aware.mdc) - Solana 钱包安全：隔离签名者、程序白名单、MEV 感知交易处理及操作护栏规范。
- [TypeScript (LLM Tech Stack)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/typescript-llm-tech-stack-cursorrules-prompt-file.mdc) - TypeScript LLM 技术栈集成开发指南。
- [TypeScript (Node.js, Next.js, AI)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/typescript-nodejs-nextjs-ai-cursorrules-prompt-fil.mdc) - TypeScript 结合 Node.js、Next.js 和 AI 集成开发指南。
- [TypeScript (Node.js, Next.js, React, UI, CSS)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/typescript-nodejs-nextjs-react-ui-css-cursorrules-.mdc) - TypeScript 结合 Node.js、Next.js、React、UI 和 CSS 集成开发指南。
- [TypeScript (Node.js, React, Vite)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/typescript-nodejs-react-vite-cursorrules-prompt-fi.mdc) - TypeScript 结合 Node.js、React 和 Vite 集成开发指南。
- [TypeScript (React, Next.js, Cloudflare)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/typescript-react-nextjs-cloudflare-cursorrules-pro.mdc) - TypeScript 结合 React、Next.js 和 Cloudflare 集成开发指南。
- [TypeScript (React, NextUI, Supabase)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/typescript-react-nextui-supabase-cursorrules-promp.mdc) - TypeScript 结合 React、NextUI 和 Supabase 集成开发指南。
- [TypeScript (shadcn/ui, Next.js)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/typescript-shadcn-ui-nextjs-cursorrules-prompt-fil.mdc) - TypeScript 结合 shadcn/ui 和 Next.js 集成开发指南。
- [TypeScript (Vite, Tailwind)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/typescript-vite-tailwind-cursorrules-prompt-file.mdc) - TypeScript 结合 Vite 和 Tailwind 集成开发指南。
- [TypeScript (Vue.js)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/typescript-vuejs-cursorrules-prompt-file.mdc) - TypeScript 结合 Vue.js 集成开发指南。
- [TypeScript (Zod, Tailwind, Next.js)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/typescript-zod-tailwind-nextjs-cursorrules-prompt-.mdc) - TypeScript 结合 Zod、Tailwind 和 Next.js 集成开发指南。
- [WebAssembly (Z80 Cellular Automata)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/webassembly-z80-cellular-automata-cursorrules-prom.mdc) - WebAssembly Z80 元胞自动机集成开发指南。
- [TypeScript (Next.js)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/typescript-nextjs-cursorrules-prompt-file.mdc) - TypeScript Next.js 集成开发指南。
- [TypeScript (Next.js, React)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/typescript-nextjs-react-cursorrules-prompt-file.mdc) - TypeScript 结合 Next.js 和 React 集成开发指南。
- [TypeScript (Next.js, React, Tailwind, Supabase)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/typescript-nextjs-react-tailwind-supabase-cursorru.mdc) - TypeScript 结合 Next.js、React、Tailwind 和 Supabase 集成开发指南。
- [TypeScript (Next.js, Supabase)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/typescript-nextjs-supabase-cursorrules-prompt-file.mdc) - TypeScript 结合 Next.js 和 Supabase 集成开发指南。
- [TypeScript (Node.js, Next.js App)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/typescript-nodejs-nextjs-app-cursorrules-prompt-fi.mdc) - TypeScript 结合 Node.js 和 Next.js 应用集成开发指南。
- [TypeScript (React)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/typescript-react-cursorrules-prompt-file.mdc) - TypeScript React 集成开发指南。
- [TypeScript (Clasp App Script)](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/typescript-clasp-cursorrules-prompt-file.mdc) - TypeScript Clasp 脚本集成开发指南。
- [C++ Programming Guidelines](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/cpp-programming-guidelines-cursorrules-prompt-file.mdc) - C++ 编程规范集成指南。
- [TensorFlow and Deep Learning](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/tensorflow-deep-learning.mdc) - TensorFlow 模型开发、训练、评估、导出与部署指南。

### 安全

- [DevSecOps, SSDLC, and AppSec](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/security-devsecops-ssdls-appsec.mdc) - 安全编码、密钥处理、依赖卫生、认证授权、安全测试及合规文档规范。

### 文档编写

- [Gherkin Style Testing](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/gherkin-style-testing-cursorrules-prompt-file.mdc) - 行为驱动场景与验收标准规范。
- [How-To Documentation](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/how-to-documentation-cursorrules-prompt-file.mdc) - 任务导向指南与流程文档编写规范。
- [README Best Practices](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/readme-best-practices-cursorrules-prompt-file.mdc) - README 最佳实践集成指南。

## 相关目录

- [CursorList](https://cursorlist.com)
- [CursorDirectory](https://cursor.directory/)

## 如何使用

### 项目规则

1. 如果你尚未安装，请先安装 Cursor AI。
2. 浏览上述规则列表，找到符合你需求的 `.mdc` 规则文件。
3. 如果项目中尚不存在 `.cursor/rules/` 目录，请创建它。
4. 将选定的 `.mdc` 文件复制到 `.cursor/rules/` 目录中。
5. 根据你的具体项目需求对规则进行自定义调整。

## 贡献指南

欢迎提交贡献！如果你有一条优秀的 Cursor 规则想要分享：

1. Fork 本仓库。
2. 为规则选择一个描述性的 slug，例如 `react-typescript` 或 `python-fastapi`。
3. 在 `rules/` 目录下添加规范的 `.mdc` 规则文件。
4. 新增的 `rules/*.mdc` 文件必须以如下 frontmatter 开头：

   ```yaml
   ---
   description: One-line summary of what this rule helps Cursor do
   globs: **/*.ts, **/*.tsx
   alwaysApply: false
   ---
   ```

   `description` 字段向 Cursor 和贡献者说明该规则的作用。`globs` 字段列出规则应自动附加的文件模式。使用 `alwaysApply: false` 可将规则限制在匹配或请求的上下文中；仅当需要适用于所有请求的通用指导时，才使用 `alwaysApply: true`。

5. 更新主 README.md 文件，将你的贡献添加到相应分类下。
6. 确保你的贡献符合仓库的格式与命名规范。
7. 提交 Pull Request。

请确保你的贡献是原创的，或基于现有工作时已正确署名。保持描述中立、实用，并聚焦于可复用的 Cursor 规则价值。

## 附录与赞助信息

### 赞助商

- [coderabbit.ai](https://coderabbit.ai/?utm_source=oss&utm_medium=sponsorship&utm_campaign=awesome-cursorrules) - 将代码审查时间与 Bug 数量减半。
- [Unblocked MCP](https://getunblocked.com/unblocked-mcp/?utm_source=oss&utm_medium=sponsorship&utm_campaign=awesome-cursorrules) - 为 Cursor 工作流提供团队知识库支持。
- [Warp](https://go.warp.dev/awesome-cursorrules) - 专为多 AI Agent 编码打造的终端工作流。