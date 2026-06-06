<h1 align="center">
    <a href="https://crawlee.dev">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/apify/crawlee/master/website/static/img/crawlee-dark.svg?sanitize=true">
          <img alt="Crawlee" src="https://raw.githubusercontent.com/apify/crawlee/master/website/static/img/crawlee-light.svg?sanitize=true" width="500">
        </picture>
    </a>
    <br>
    <small>A web scraping and browser automation library</small>
</h1>

<p align=center>
    <a href="https://trendshift.io/repositories/5179" target="_blank"><img src="https://trendshift.io/api/badge/repositories/5179" alt="apify%2Fcrawlee | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

<p align=center>
    <a href="https://www.npmjs.com/package/@crawlee/core" rel="nofollow"><img src="https://img.shields.io/npm/v/@crawlee/core.svg" alt="NPM latest version" data-canonical-src="https://img.shields.io/npm/v/@crawlee/core/next.svg" style="max-width: 100%;"></a>
    <a href="https://www.npmjs.com/package/@crawlee/core" rel="nofollow"><img src="https://img.shields.io/npm/dm/@crawlee/core.svg" alt="Downloads" data-canonical-src="https://img.shields.io/npm/dm/@crawlee/core.svg" style="max-width: 100%;"></a>
    <a href="https://discord.gg/jyEM2PRvMU" rel="nofollow"><img src="https://img.shields.io/discord/801163717915574323?label=discord" alt="Chat on discord" data-canonical-src="https://img.shields.io/discord/801163717915574323?label=discord" style="max-width: 100%;"></a>
    <a href="https://github.com/apify/crawlee/actions/workflows/test-ci.yml"><img src="https://github.com/apify/crawlee/actions/workflows/test-ci.yml/badge.svg?branch=master" alt="Build Status" style="max-width: 100%;"></a>
</p>

Crawlee 覆盖了你从网页爬取（Crawling）到数据抓取（Scraping）的端到端流程，**帮助你快速构建可靠的爬虫。**

即使使用默认配置，你的爬虫也会表现得像人类一样，从而轻松避开现代反爬机制的检测。Crawlee 提供了爬取网页链接、抓取数据并将其存储到磁盘或云端的工具，同时保持高度的可配置性，以满足你项目的各种需求。

Crawlee 可通过 [`crawlee`](https://www.npmjs.com/package/crawlee) NPM 包获取。

> 👉 **在 [Crawlee 项目网站上查看完整文档、指南和示例](https://crawlee.dev)** 👈

> 更偏好使用 🐍 Python 而不是 JavaScript？[👉 查看 Crawlee for Python 👈](https://github.com/apify/crawlee-python)。

## 安装

我们建议查阅 Crawlee 文档中的 [入门教程](https://crawlee.dev/js/docs/introduction) 以获取更多信息。

> Crawlee 需要 **Node.js 16 或更高版本**。

### 通过 Crawlee CLI

尝试 Crawlee 最快的方式是使用 **Crawlee CLI**，并选择 **入门示例**。CLI 会自动安装所有必要的依赖项，并为你生成可供测试的样板代码。

```bash
npx crawlee create my-crawler
```

```bash
cd my-crawler
npm start
```

### 手动安装
如果你更倾向于将 Crawlee **添加到自己的项目中**，可尝试以下示例。由于该示例使用了 `PlaywrightCrawler`，我们还需要安装 [Playwright](https://playwright.dev)。为减小安装包体积，它并未随 Crawlee 捆绑提供。

```bash
npm install crawlee playwright
```

```js
import { PlaywrightCrawler, Dataset } from 'crawlee';

// PlaywrightCrawler crawls the web using a headless
// browser controlled by the Playwright library.
const crawler = new PlaywrightCrawler({
    // Use the requestHandler to process each of the crawled pages.
    async requestHandler({ request, page, enqueueLinks, log }) {
        const title = await page.title();
        log.info(`Title of ${request.loadedUrl} is '${title}'`);

        // Save results as JSON to ./storage/datasets/default
        await Dataset.pushData({ title, url: request.loadedUrl });

        // Extract links from the current page
        // and add them to the crawling queue.
        await enqueueLinks();
    },
    // Uncomment this option to see the browser window.
    // headless: false,
});

// Add first URL to the queue and start the crawl.
await crawler.run(['https://crawlee.dev']);
```

默认情况下，Crawlee 会将数据存储到当前工作目录下的 `./storage` 文件夹中。你可以通过 Crawlee 配置覆盖此路径。详情请参阅 [配置指南](https://crawlee.dev/js/docs/guides/configuration)、[请求存储](https://crawlee.dev/js/docs/guides/request-storage) 和 [结果存储](https://crawlee.dev/js/docs/guides/result-storage)。

### 安装预发布版本

对于 Crawlee 中合并的每一次代码更新，我们都会提供自动化的 Beta 构建版本。你可以在 npm [发布列表](https://www.npmjs.com/package/crawlee?activeTab=versions) 中找到它们。如果你想在我们正式发布前测试新功能或修复方案，可以像这样安装 Beta 版：

```bash
npm install crawlee@next
```

如果你同时使用了 [Apify SDK](https://github.com/apify/apify-sdk-js)，则需要在 `package.json` 文件中指定依赖覆盖（overrides），以避免安装多个版本的 Crawlee：

```json
{
    "overrides": {
       "apify": {
           "@crawlee/core": "$crawlee",
           "@crawlee/types": "$crawlee",
           "@crawlee/utils": "$crawlee"
       }
    }
}
```

## 🛠 功能特性

- 统一的接口支持 **HTTP 和无头浏览器**爬取
- 持久化的待爬 URL **队列**（支持广度优先与深度优先遍历）
- 可扩展的存储方案，同时支持表格数据和文件
- 根据可用系统资源自动进行扩缩容（Scaling）
- 内置代理轮换（Proxy Rotation）与会话管理功能
- 支持通过 Hooks（钩子）自定义生命周期
- 提供 **CLI** 快速初始化项目
- 可配置的路由、错误处理和重试机制
- 预置开箱即用的 Dockerfile
- 使用 TypeScript 编写，全面支持泛型

### 👾 HTTP 爬取

- 零配置原生支持 **HTTP/2**，代理场景同样适用
- 自动生成类浏览器的请求头（Headers）
- 模拟浏览器 TLS 指纹
- 内置高效的 HTML 解析器：Cheerio 和 JSDOM
- 当然，你也可以抓取 JSON API

### 💻 真实浏览器爬取

- 支持 JavaScript 渲染与页面截图
- 同时支持无头（Headless）和有头（Headful）模式
- 零配置生成类浏览器指纹
- 自动化的浏览器管理
- 使用统一的接口调用 Playwright 和 Puppeteer
- 支持 Chrome、Firefox、Webkit 等多种浏览器

## 在 Apify 平台上的使用

Crawlee 开源且可在任何环境中运行，但由于它由 [Apify](https://apify.com) 开发，因此在 Apify 平台上部署和云端运行非常便捷。请访问 [Apify SDK 官网](https://sdk.apify.com) 了解将 Crawlee 部署到 Apify 平台的更多信息。

## 支持

如果你发现 Crawlee 存在任何 Bug 或问题，请前往 [GitHub 提交 Issue](https://github.com/apify/crawlee/issues)。如有其他疑问，你可以在 [Stack Overflow](https://stackoverflow.com/questions/tagged/apify) 提问、在 GitHub Discussions 中讨论，或加入我们的 [Discord 社区](https://discord.com/invite/jyEM2PRvMU)。

## 贡献代码

我们非常欢迎你的代码贡献，并将永远感激你！如果你有改进建议，请提交 Issue 或创建 Pull Request。关于贡献指南和行为规范，请参阅 [CONTRIBUTING.md](https://github.com/apify/crawlee/blob/master/CONTRIBUTING.md)。

## 许可证

本项目采用 Apache License 2.0 开源协议 - 详情请参阅 [LICENSE.md](https://github.com/apify/crawlee/blob/master/LICENSE.md)。