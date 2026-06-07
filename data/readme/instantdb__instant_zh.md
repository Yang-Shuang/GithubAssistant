<p align="center">
  <a href="https://instantdb.com/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://instantdb.com/readmes/logo_with_text_dark_mode.svg">
      <img alt="Shows the Instant logo" src="https://instantdb.com/readmes/logo_with_text_light_mode.svg">
    </picture>
  </a>
</p>

<p align="center">
  <a 
    href="https://discord.com/invite/VU53p7uQcE" >
    <img height=20 src="https://img.shields.io/discord/1031957483243188235" />
  </a>
  <a href="#">
    <img src="https://img.shields.io/github/stars/instantdb/instant" alt="stars">
  </a>
</p>

<p align="center">
   <a href="https://instantdb.com/docs">快速开始</a> · 
   <a href="https://instantdb.com/examples">示例</a> · 
   <a href="https://instantdb.com/tutorial">试用演示</a> · 
   <a href="https://instantdb.com/docs">文档</a> · 
   <a href="https://discord.com/invite/VU53p7uQcE">Discord 社区</a>
<p>

Instant 是用于 AI 编码应用的最佳后端。你获得身份验证（auth）、权限管理、存储、用户在线状态（presence）和实时流（streams）——一切所需，助你打造用户喜爱的应用。

你只需以期望的数据结构编写[关系型查询](https://www.instantdb.com/docs/instaql)，Instant 会自动处理所有数据获取、权限校验和离线缓存（offline caching）。当你[修改数据](https://www.instantdb.com/docs/instaml)时，乐观更新（optimistic updates）与回滚（rollbacks）机制也会由系统自动处理。此外，默认情况下每个查询都支持多人协作。

我们还支持[临时性（ephemeral）](https://www.instantdb.com/docs/presence-and-topics)更新，例如光标位置或在线用户列表。目前我们提供 [JavaScript](https://www.instantdb.com/docs/start-vanilla)、[React](https://www.instantdb.com/docs/) 和 [React Native](https://www.instantdb.com/docs/start-rn) 的 SDK。

代码长什么样？这是一个仅需约 12 行代码的基础聊天应用：

```javascript
// ༼ つ ◕_◕ ༽つ Real-time Chat
// ----------------------------------
// * Updates instantly
// * Multiplayer
// * Works offline

import { init, id } from "@instantdb/react";

const db = init({ 
  appId: process.env.NEXT_PUBLIC_APP_ID,
});

function Chat() {
  // 1. Read
  const { isLoading, error, data } = db.useQuery({
    messages: {},
  });

  // 2. Write
  const addMessage = (message) => {
    db.transact(db.tx.messages[id()].update(message));
  };

  // 3. Render!
  return <UI data={data} onAdd={addMessage} />;
}
```

想亲自体验吗？<a href="https://instantdb.com/tutorial">在浏览器中试用演示</a>。

## Motivation（设计初衷）

开发现代应用充满了繁琐的重复工作（schleps）。通常你从服务端开始：搭建数据库、缓存层、ORM（对象关系映射）框架和 API 接口。接着编写客户端代码：状态管理（stores）、数据选择器（selectors）和数据修改器（mutators）。最后才是编写界面代码。如果要添加多人协作，你需要考虑有状态服务器；如果支持离线模式，则需处理 IndexedDB 和事务队列。

更糟糕的是，每次添加新功能时，你都要重复相同的开发流程：创建数据模型、编写接口、状态管理、选择器，最后是 UI。

有没有更好的方法？

在 2021 年，**我们意识到作为前端工程师所面临的绝大多数繁琐工作，本质上都是伪装成界面问题的数据库难题。**（我们在[这篇文章](https://instantdb.com/essays/next_firebase)中进行了更详细的阐述）

<p align="center">
  <a href="#">
    <img alt="Shows how Instant compresses schleps" src="https://instantdb.com/readmes/compression.svg">
  </a>
</p>

如果客户端直接拥有数据库，你就不必再操心状态管理、选择器、接口或本地缓存：只需编写查询即可。如果这些查询默认就支持多人协作，你就无需担心有状态服务器的问题。如果你的数据库支持回滚机制，乐观更新也就免费获得了。

因此我们创建了 Instant。Instant 为你提供一个可直接在客户端使用的数据库，让你能专注于真正重要的事：快速打造出色的用户体验（UX）。

## Architectural Overview（架构概览）

以下是 Instant 的高层架构工作原理：

<p align="center">
  <a href="#">
    <img alt="Shows how Instant compresses schleps" src="https://instantdb.com/readmes/architecture.svg">
  </a>
</p>

底层实现中，我们将所有用户数据以三元组（triples）的形式存储在一个大型 PostgreSQL 数据库中。多租户架构使我们能够提供持续可用（不会自动暂停）的免费套餐。

一个用 Clojure 编写的同步服务器负责与 PostgreSQL 通信。我们编写了一个查询引擎，支持 Datalog 和 [InstaQL](https://www.instantdb.com/docs/instaql)（一种类似 GraphQL 的关系型查询语言）：

```javascript
// give me all users, their posts and comments
{
  users: {
    posts: {
      comments: {
      }
    }
  }
}
```

受 [Asana 的 WorldStore](https://asana.com/inside-asana/worldstore-distributed-caching-reactivity-part-1) 和 [Figma 的 LiveGraph](https://www.figma.com/blog/how-figmas-multiplayer-technology-works/#syncing-object-properties) 启发，我们通过监听 PostgreSQL 的预写日志（WAL）来检测数据变更并失效相关查询。

前端方面，我们编写了一个客户端三元组存储库。SDK 负责将近期查询的缓存持久化到 Web 端的 IndexedDB 以及 React Native 端的 AsyncStorage 中。

所有数据均经过基于 Google [CEL 库](https://github.com/google/cel-java)构建的权限系统进行校验。

## Getting Started（快速开始）

使用 Instant 最快捷的方式是在 [instantdb.com](https://instantdb.com) 注册账号。[你只需不到 5 分钟即可创建一个可用的应用](https://instantdb.com/docs)。

如有任何疑问，欢迎加入我们的 [Discord](https://discord.com/invite/VU53p7uQcE) 社区交流。

## Contributing（参与贡献）

你可以先加入我们的 [Discord](https://discord.com/invite/VU53p7uQcE) 并做个自我介绍。即使你不参与代码贡献，我们也十分欢迎你的反馈与建议。

如果你想修改代码，请先阅读 [`client`](./client/) 和 [`server`](./server/) 目录下的 README 文件。里面包含了在本地启动 Instant 的详细指南。