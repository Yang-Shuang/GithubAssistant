<p align="center">
  <img src="https://raw.githubusercontent.com/oramasearch/orama/refs/heads/main/misc/readme/orama-readme-hero-dark.png#gh-dark-mode-only" />
  <img src="https://raw.githubusercontent.com/oramasearch/orama/refs/heads/main/misc/readme/orama-readme-hero-light.png#gh-light-mode-only" />
</p>

[![Tests](https://github.com/oramasearch/orama/actions/workflows/turbo.yml/badge.svg)](https://github.com/oramasearch/orama/actions/workflows/turbo.yml)

如需更多信息、帮助，或希望对 Orama 提供一般性反馈，请加入 [Orama Slack 频道](https://orama.to/slack)。

# 核心功能

- [全文搜索](https://docs.orama.com/docs/orama-js/search)
- [向量搜索](https://docs.orama.com/docs/orama-js/search/vector-search)
- [混合搜索](https://docs.orama.com/docs/orama-js/search/hybrid-search)
- [GenAI 对话会话](https://docs.orama.com/docs/orama-js/answer-engine)
- [搜索过滤](https://docs.orama.com/docs/orama-js/search/filters)
- [地理位置搜索 (Geosearch)](https://docs.orama.com/docs/orama-js/search/geosearch)
- [置顶规则（商品推广）](https://docs.orama.com/docs/orama-js/results-pinning)
- [Facets（分类统计）](https://docs.orama.com/docs/orama-js/search/facets)
- [字段权重提升](https://docs.orama.com/docs/orama-js/search/fields-boosting)
- [拼写容错](https://docs.orama.com/docs/orama-js/search#typo-tolerance)
- [精确匹配](https://docs.orama.com/docs/orama-js/search#exact-match)
- [BM25 算法](https://docs.orama.com/docs/orama-js/search/bm25)
- [30 种语言的词干提取与分词](https://docs.orama.com/docs/orama-js/text-analysis/stemming)
- [插件系统](https://docs.orama.com/docs/orama-js/plugins)

# 安装

你可以通过 `npm`、`yarn`、`pnpm` 或 `bun` 安装 Orama：

```sh
npm i @orama/orama
```

或者直接在浏览器模块中导入它：

```html
<html>
  <body>
    <script type="module">
      import { create, insert, search } from 'https://cdn.jsdelivr.net/npm/@orama/orama@latest/+esm'
    </script>
  </body>
</html>
```

在 Deno 环境中，你可以直接使用相同的 CDN URL，或使用 npm 规范标识符：

```js
import { create, search, insert } from 'npm:@orama/orama'
```

完整文档请查阅 [https://docs.orama.com](https://docs.orama.com)。

# Orama 功能特性

<p align="center">
  <img src="https://raw.githubusercontent.com/oramasearch/orama/refs/heads/main/misc/readme/features-dark.png#gh-dark-mode-only" />
  <img src="https://raw.githubusercontent.com/oramasearch/orama/refs/heads/main/misc/readme/features-light.png#gh-light-mode-only" />
</p>

# 使用方法

Orama 的使用非常简便。首先，你需要创建一个新的数据库实例并设置索引模式：

```js
import { create, insert, remove, search, searchVector } from '@orama/orama'

const db = create({
  schema: {
    name: 'string',
    description: 'string',
    price: 'number',
    embedding: 'vector[1536]', // Vector size must be expressed during schema initialization
    meta: {
      rating: 'number',
    },
  },
})

insert(db, {
  name: 'Noise cancelling headphones',
  description: 'Best noise cancelling headphones on the market',
  price: 99.99,
  embedding: [0.2432, 0.9431, 0.5322, 0.4234, ...],
  meta: {
    rating: 4.5
  }
})

const results = search(db, {
  term: 'Best headphones'
})

// {
//   elapsed: {
//     raw: 21492,
//     formatted: '21μs',
//   },
//   hits: [
//     {
//       id: '41013877-56',
//       score: 0.925085832971998432,
//       document: {
//         name: 'Noise cancelling headphones',
//         description: 'Best noise cancelling headphones on the market',
//         price: 99.99,
//         embedding: [0.2432, 0.9431, 0.5322, 0.4234, ...],
//         meta: {
//           rating: 4.5
//         }
//       }
//     }
//   ],
//   count: 1
// }
```

Orama 目前支持 10 种不同的数据类型：

| Type             | Description                                                                 | Example                                                                     |
| ---------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `string`         | 字符串（字符序列）。                                                        | `'Hello world'`                                                             |
| `number`         | 数值，支持浮点数或整数。                                                    | `42`                                                                        |
| `boolean`        | 布尔值。                                                                    | `true`                                                                      |
| `enum`           | 枚举值。                                                                    | `'drama'`                                                                   |
| `geopoint`       | 地理位置点。                                                                | `{ lat: 40.7128, lon: 74.0060 }`                                            |
| `string[]`       | 字符串数组。                                                                | `['red', 'green', 'blue']`                                                  |
| `number[]`       | 数值数组。                                                                  | `[42, 91, 28.5]`                                                            |
| `boolean[]`      | 布尔值数组。                                                                | `[true, false, false]`                                                      |
| `enum[]`         | 枚举数组。                                                                  | `['comedy', 'action', 'romance']`                                           |
| `vector[<size>]` | 用于向量搜索的数值向量（需在初始化时指定维度大小）。                        | `[0.403, 0.192, 0.830]`                                                     |

# 向量与混合搜索支持

Orama 仅通过在搜索时设置 `mode: 'vector'` 即可同时启用向量搜索和混合搜索。

要执行此类搜索，你需要在查询时提供 [文本嵌入](https://en.wikipedia.org/wiki/Word_embedding)：

```js
import { create, insertMultiple, search } from '@orama/orama'

const db = create({
  schema: {
    title: 'string',
    embedding: 'vector[5]', // we are using a 5-dimensional vector.
  },
});

insert_multiple(db, [
  { title: 'The Prestige', embedding: [0.938293, 0.284951, 0.348264, 0.948276, 0.56472] },
  { title: 'Barbie', embedding: [0.192839, 0.028471, 0.284738, 0.937463, 0.092827] },
  { title: 'Oppenheimer', embedding: [0.827391, 0.927381, 0.001982, 0.983821, 0.294841] },
])

const results = search(db, {
  // Search mode. Can be 'vector', 'hybrid', or 'fulltext'
  mode: 'vector',
  vector: {
    // The vector (text embedding) to use for search
    value: [0.938292, 0.284961, 0.248264, 0.748276, 0.26472],
    // The schema property where Orama should compare embeddings
    property: 'embedding',
  },
  // Minimum similarity to determine a match. Defaults to `0.8`
  similarity: 0.85,
  // Defaults to `false`. Setting to 'true' will return the embeddings in the response (which can be very large).
  includeVectors: true,
})
```

在为向量与混合搜索生成嵌入（embedding）时遇到困难？试试我们的 `@orama/plugin-embeddings` 插件！

```js
import { create } from '@orama/orama'
import { pluginEmbeddings } from '@orama/plugin-embeddings'
import '@tensorflow/tfjs-node' // Or any other appropriate TensorflowJS backend, like @tensorflow/tfjs-backend-webgl

const plugin = await pluginEmbeddings({
  embeddings: {
    // Schema property used to store generated embeddings
    defaultProperty: 'embeddings',
    onInsert: {
      // Generate embeddings at insert-time
      generate: true,
      // properties to use for generating embeddings at insert time.
      // Will be concatenated to generate a unique embedding.
      properties: ['description'],
      verbose: true,
    }
  }
})

const db = create({
  schema: {
    description: 'string',
    // Orama generates 512-dimensions vectors.
    // When using @orama/plugin-embeddings, set the property where you want to store embeddings as `vector[512]`.
    embeddings: 'vector[512]'
  },
  plugins: [plugin]
})

// Orama will generate and store embeddings at insert-time!
await insert(db, { description: 'Classroom Headphones Bulk 5 Pack, Student On Ear Color Varieties' })
await insert(db, { description: 'Kids Wired Headphones for School Students K-12' })
await insert(db, { description: 'Kids Headphones Bulk 5-Pack for K-12 School' })
await insert(db, { description: 'Bose QuietComfort Bluetooth Headphones' })

// Orama will also generate and use embeddings at search time when search mode is set to "vector" or "hybrid"!
const searchResults = await search(db, {
  term: 'Headphones for 12th grade students',
  mode: 'vector',
  similarity: 0.75,
})
```

想使用 OpenAI 的嵌入模型？请使用我们的 [安全代理](https://docs.orama.com/docs/orama-js/plugins/plugin-secure-proxy) 插件，以便在客户端安全地调用 OpenAI。

# 基于 Orama 的 RAG 与对话体验

自 `v3.0.0` 起，Orama 允许你打造属于自己的类 ChatGPT/Perplexity/SearchGPT 体验。这需要调用 OpenAI API，因此我们强烈建议使用 [安全代理插件](https://docs.orama.com/docs/orama-js/plugins/plugin-secure-proxy) 在客户端进行安全调用。该功能免费！

```js
import { create, insert } from '@orama/orama'
import { pluginSecureProxy } from '@orama/plugin-secure-proxy'

const secureProxy = await pluginSecureProxy({
  apiKey: 'my-api-key',
  defaultProperty: 'embeddings',
  models: {
    // The chat model to use to generate the chat answer
    chat: 'openai/gpt-4o-mini'
  }
})

const db = create({
  schema: {
    name: 'string'
  },
  plugins: [secureProxy]
})

insert(db, { name: 'John Doe' })
insert(db, { name: 'Jane Doe' })

const session = new AnswerSession(db, {
  // Customize the prompt for the system
  systemPrompt: 'You will get a name as context, please provide a greeting message',
  events: {
    // Log all state changes. Useful to reactively update a UI on a new message chunk, sources, etc.
    onStateChange: console.log,
  }
})

const response = await session.ask({
  term: 'john'
})

console.log(response) // Hello, John Doe! How are you doing?
```

完整文档请查阅 [官方文档](https://docs.orama.com/docs/orama-js/answer-engine)。

# 官方文档

完整文档请查阅 [https://docs.orama.com/open-source](https://docs.orama.com/open-source)。

# Orama 官方插件

- [Embedding 插件](https://docs.orama.com/docs/orama-js/plugins/plugin-embeddings)
- [安全代理插件](https://docs.orama.com/docs/orama-js/plugins/plugin-secure-proxy)
- [数据分析插件](https://docs.orama.com/docs/orama-js/plugins/plugin-analytics)
- [数据持久化插件](https://docs.orama.com/docs/orama-js/plugins/plugin-data-persistence)
- [QPS 插件](https://docs.orama.com/docs/orama-js/plugins/plugin-qps)
- [PT15 插件](https://docs.orama.com/docs/orama-js/plugins/plugin-pt15)
- [Vitepress 插件](https://docs.orama.com/docs/orama-js/plugins/plugin-vitepress)
- [Docusaurus 插件](https://docs.orama.com/docs/orama-js/plugins/plugin-docusaurus)
- [Astro 插件](https://docs.orama.com/docs/orama-js/plugins/plugin-astro)
- [Nextra 插件](https://docs.orama.com/docs/orama-js/plugins/plugin-nextra)

编写你自己的插件：[https://docs.orama.com/docs/orama-js/plugins/writing-your-own-plugins](https://docs.orama.com/docs/orama-js/plugins/writing-your-own-plugins)

# 许可证

Orama 采用 [Apache 2.0](/LICENSE.md) 开源协议。

<img referrerpolicy="no-referrer-when-downgrade" src="https://static.scarf.sh/a.png?x-pxid=16782f89-15fb-4e03-8e9c-2a06106542f7" />