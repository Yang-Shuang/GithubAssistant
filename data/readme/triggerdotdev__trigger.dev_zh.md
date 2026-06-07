<div align="center">

![Trigger.dev logo](https://content.trigger.dev/github-header-banner.jpg)

### 构建和部署全托管的 AI Agent（智能体）与工作流

[Website](https://trigger.dev) | [Docs](https://trigger.dev/docs) | [Issues](https://github.com/triggerdotdev/trigger.dev/issues) | [Example projects](https://github.com/triggerdotdev/examples) | [Feature requests](https://triggerdev.featurebase.app/) | [Public roadmap](https://triggerdev.featurebase.app/roadmap) | [Self-hosting](https://trigger.dev/docs/self-hosting/overview) 

[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red.svg)](https://github.com/triggerdotdev/trigger.dev)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/triggerdotdev/trigger.dev/blob/main/LICENSE)
[![npm](https://img.shields.io/npm/v/@trigger.dev/sdk.svg?label=npm)](https://www.npmjs.com/package/@trigger.dev/sdk)
[![SDK downloads](https://img.shields.io/npm/dm/@trigger.dev/sdk.svg?label=SDK%20downloads)](https://www.npmjs.com/package/@trigger.dev/sdk)

[![Twitter Follow](https://img.shields.io/twitter/follow/triggerdotdev?style=social)](https://twitter.com/triggerdotdev)
[![Discord](https://img.shields.io/discord/1066956501299777596?logo=discord&logoColor=white&color=7289da)](https://discord.gg/nkqV9xBYWy)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/triggerdotdev/trigger.dev)
[![GitHub stars](https://img.shields.io/github/stars/triggerdotdev/trigger.dev?style=social)](https://github.com/triggerdotdev/trigger.dev)

</div>

## About Trigger.dev

Trigger.dev 是一个基于 TypeScript 构建 AI 工作流的开源平台。支持长时间运行的任务，内置重试机制、队列管理、可观测性及弹性扩缩容能力。

## The platform designed for building AI agents

使用你熟悉的框架、服务和 LLM（大语言模型）构建 [AI Agent](https://trigger.dev/product/ai-agents)，并将其部署到 Trigger.dev。开箱即用，获得具备持久性、长时间运行能力、重试机制、队列管理、可观测性及弹性扩缩容的任务。

- **无需担心超时**：与 AWS Lambda、Vercel 及其他无服务器平台不同，你的任务执行完全不受超时限制。
- **持久性、重试与队列**：利用我们持久的任务机制、重试策略和队列功能构建稳健的 Agent 和 AI 应用。
- **真正的运行时自由**：通过系统包自定义部署的任务——运行浏览器、Python 脚本、FFmpeg 等。
- **人工介入（Human-in-the-loop）**：编程方式暂停任务，直到人类审批、拒绝或提供反馈。
- **实时应用与流式传输**：通过订阅运行状态或将 AI 响应流式传输到你的应用中，将后台作业移至前台。
- **可观测性与监控**：每次运行都具备完整的链路追踪和日志记录。配置错误告警以快速捕获 Bug。

## Key features:

- **[JavaScript and TypeScript SDK](https://trigger.dev/docs/tasks/overview)** - 使用熟悉的编程模型构建后台任务
- **[Long-running tasks](https://trigger.dev/docs/runs/max-duration)** - 处理资源密集型任务，且不受超时限制
- **[Durable cron schedules](https://trigger.dev/docs/tasks/scheduled#scheduled-tasks-cron)** - 创建并绑定最长可达一年的周期性计划
- **[Trigger.dev Realtime](https://trigger.dev/docs/realtime/overview)** - 触发、订阅获取运行状态的实时更新，支持 LLM 流式响应
- **[Build extensions](https://trigger.dev/docs/config/extensions/overview#build-extensions)** - 直接挂钩到构建系统并自定义构建流程。可运行 Python 脚本、FFmpeg、浏览器等。
- **[React hooks](https://trigger.dev/docs/frontend/react-hooks#react-hooks)** - 通过我们的 React Hooks 包在前端与 Trigger.dev API 交互
- **[Batch triggering](https://trigger.dev/docs/triggering#tasks-batchtrigger)** - 使用 `batchTrigger()` 以自定义负载和选项一次性启动多个任务运行实例
- **[Structured inputs / outputs](https://trigger.dev/docs/tasks/schemaTask#schematask)** - 为任务定义精确的数据 Schema，并在运行时进行有效载荷（Payload）校验
- **[Waits](https://trigger.dev/docs/wait)** - 在任务中添加暂停逻辑，按指定时长挂起执行
- **[Preview branches](https://trigger.dev/docs/deployment/preview-branches)** - 创建隔离环境用于测试和开发。支持与 Vercel 及 Git 工作流集成
- **[Waitpoints](https://trigger.dev/docs/wait-for-token#wait-for-token)** - 在工作流的关键决策节点加入人工审批环节，且不中断整体流程
- **[Concurrency & queues](https://trigger.dev/docs/queue-concurrency#concurrency-and-queues)** - 设置并发规则以管理多个任务的执行顺序
- **[Multiple environments](https://trigger.dev/docs/how-it-works#dev-mode)** - 全面支持 DEV、PREVIEW、STAGING 和 PROD 环境
- **[No infrastructure to manage](https://trigger.dev/docs/how-it-works#trigger-dev-architecture)** - 自动扩缩容的基础设施，彻底消除超时与服务器管理负担
- **[Automatic retries](https://trigger.dev/docs/errors-retrying)** - 若任务遇到未捕获的错误，我们将自动尝试重新执行
- **[Checkpointing](https://trigger.dev/docs/how-it-works#the-checkpoint-resume-system)** - 得益于我们的检查点功能，任务天生具备持久性
- **[Versioning](https://trigger.dev/docs/versioning)** - 原子化版本管理允许你部署新版本而不会影响正在运行的任务
- **[Machines](https://trigger.dev/docs/machines)** - 自定义任务所需的 vCPU 核心数与内存（GB）大小
- **[Observability & monitoring](https://trigger.dev/product/observability-and-monitoring)** - 通过全面的日志记录与可视化工具，监控任务性能的每一个方面
- **[Logging & tracing](https://trigger.dev/docs/logging)** - 为所有任务提供完整的日志记录与追踪功能
- **[Tags](https://trigger.dev/docs/tags#tags)** - 每个运行实例最多可绑定十个标签，支持在控制台、实时面板及 SDK 中进行过滤
- **[Run metadata](https://trigger.dev/docs/runs/metadata#run-metadata)** - 为运行实例附加动态更新的元数据，并可在前端用于实现实时更新
- **[Bulk actions](https://trigger.dev/docs/bulk-actions)** - 同时对多个运行实例执行操作，包括重放（Replaying）和取消
- **[Real-time alerts](https://trigger.dev/docs/troubleshooting-alerts#alerts)** - 选择你偏好的通知方式以接收任务失败与部署状态的提醒

## Write tasks in your codebase

将任务写在最合适的位置：你的代码库中。享受你熟悉的版本控制、本地开发（localhost）、测试与审查体验。

```ts
import { task } from "@trigger.dev/sdk";

//1. You need to export each task
export const helloWorld = task({
  //2. Use a unique id for each task
  id: "hello-world",
  //3. The run function is the main function of the task
  run: async (payload: { message: string }) => {
    //4. You can write code that runs for a long time here, there are no timeouts
    console.log(payload.message);
  },
});
```

## Deployment

使用我们的 SDK 在代码库中编写任务。无需管理基础设施，你的任务会自动扩缩容并连接至我们的云端。当然，你也可以选择自行托管（Self-hosting）。

## Environments

我们支持开发（Development）、预发布（Staging）、预览（Preview）和生产（Production）环境，让你能够在将任务部署到生产环境前充分测试。

## Full visibility of every job run

查看每次运行中的每一个任务，精准掌握执行细节。我们提供完整的链路追踪视图，让你清晰了解每一步的具体操作。

![Trace view image](https://content.trigger.dev/trace-view.png)

# Getting started

最快的上手方式是访问我们的 [Web 应用](https://cloud.trigger.dev) 创建账户和项目，并按照引导流程操作。几分钟内即可构建并部署你的第一个任务。

### Useful links:

- [Quick start](https://trigger.dev/docs/quick-start) - 几分钟内完成环境搭建与运行
- [How it works](https://trigger.dev/docs/how-it-works) - 深入了解 Trigger.dev 的底层运行机制
- [Guides and examples](https://trigger.dev/docs/guides/introduction) - 针对主流框架和用例的详细教程及代码示例

## Self-hosting

如果你倾向于自行托管 Trigger.dev，可参考我们的[自托管指南](https://trigger.dev/docs/self-hosting/overview)：

- [Docker self-hosting guide](https://trigger.dev/docs/self-hosting/docker) - 使用 Docker Compose 快速启动一个 Trigger.dev 实例
- [Kubernetes self-hosting guide](https://trigger.dev/docs/self-hosting/kubernetes) - 使用官方 Helm Chart 将 Trigger.dev 部署到你的 Kubernetes 集群

## Support and community

我们在官方 [Discord 服务器](https://trigger.dev/discord) 拥有活跃的大型社区以提供技术支持，其中包含专门的自托管频道。

## Development

如需在本地搭建开发环境或为开源项目贡献代码，请查阅我们的[开发指南](./CONTRIBUTING.md)。

## Meet the Amazing People Behind This Project:

<a href="https://github.com/triggerdotdev/trigger.dev/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=triggerdotdev/trigger.dev" />
</a>