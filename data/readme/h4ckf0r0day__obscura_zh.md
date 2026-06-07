<p align="center">
  <img src="https://raw.githubusercontent.com/h4ckf0r0day/obscura/main/assets/icon.png" alt="Obscura" width="80" />
</p>

<h2 align="center">Obscura</h2>

<p align="center">
  <strong>专为 AI 代理和网页抓取设计的开源无头浏览器。</strong><br>
  轻量、隐蔽，基于 Rust 构建。
</p>

---

Obscura 是一款用 Rust 编写的无头浏览器引擎，专为网页抓取和 AI 代理自动化而构建。它通过 V8 运行原生 JavaScript，支持 Chrome DevTools Protocol（CDP），并可作为 Puppeteer 和 Playwright 中 headless Chrome 的无缝替代品。

### 为什么选择 Obscura 而不是无头 Chrome？

专为大规模自动化设计，而非桌面浏览。

| 指标         | Obscura      | Headless Chrome |
|--------------|--------------|------------------|
| 内存占用     | **30 MB**    | 200+ MB          |
| 二进制体积   | **70 MB**    | 300+ MB          |
| 反检测       | **内置**     | 无               |
| 页面加载速度 | **85 ms**    | ~500 ms          |
| 启动时间     | **即时**     | ~2s              |
| Puppeteer    | **支持**     | 支持             |
| Playwright   | **支持**     | 支持             |

## 🎉 突破万星与后续计划

我正在开发 **Obscura Cloud**（托管版），提供托管基础设施、住宅代理和专属技术支持。面向希望直接使用引擎而不想自行运维的用户。

开源引擎将继续采用 Apache-2.0 许可证，功能完整开放。未来绝不会进行任何功能限制或付费墙设置。

**[加入等待列表 →](https://tally.so/r/gDWzdD)**

## 安装

### 下载二进制文件

从 [Releases](https://github.com/h4ckf0r0day/obscura/releases) 页面获取最新版本的预编译文件：

```bash
# Linux x86_64
curl -LO https://github.com/h4ckf0r0day/obscura/releases/latest/download/obscura-x86_64-linux.tar.gz
tar xzf obscura-x86_64-linux.tar.gz
./obscura fetch https://example.com --eval "document.title"

# Linux ARM64 (aarch64)
curl -LO https://github.com/h4ckf0r0day/obscura/releases/latest/download/obscura-aarch64-linux.tar.gz
tar xzf obscura-aarch64-linux.tar.gz

# Arch Linux (AUR)
yay -S obscura-browser

# macOS Apple Silicon
curl -LO https://github.com/h4ckf0r0day/obscura/releases/latest/download/obscura-aarch64-macos.tar.gz
tar xzf obscura-aarch64-macos.tar.gz

# macOS Intel
curl -LO https://github.com/h4ckf0r0day/obscura/releases/latest/download/obscura-x86_64-macos.tar.gz
tar xzf obscura-x86_64-macos.tar.gz

# Windows
Download the `.zip` from the releases page and extract it manually.
```

无需安装 Chrome、Node.js 或其他依赖。发布包中同时包含 `obscura` 和 `obscura-worker`；请将它们放在同一目录下，以便使用并行 `scrape` 命令。

Linux 发布版基于 Ubuntu 22.04 编译，因此下载的二进制文件可在搭载 glibc 2.35+ 的常见 LTS 服务器上正常运行。

### Docker

```bash
docker run -d --name obscura -p 127.0.0.1:9222:9222 h4ckf0r0day/obscura
```

镜像托管在 [Docker Hub](https://hub.docker.com/r/h4ckf0r0day/obscura)。采用基于 `distroless/cc` 的多阶段构建，不含 Shell 和包管理器，压缩后体积约 57 MB。

### 从源码编译

```bash
git clone https://github.com/h4ckf0r0day/obscura.git
cd obscura
cargo build --release

# With stealth mode (anti-detection + tracker blocking)
cargo build --release --features stealth
```

需要 Rust 1.75+（[安装指南](https://rustup.rs)）。首次编译约需 5 分钟（V8 从源码编译，后续会缓存加速）。

## 快速上手

### 抓取页面

```bash
# Get the page title
obscura fetch https://example.com --eval "document.title"

# Extract all links
obscura fetch https://example.com --dump links

# Render JavaScript and dump HTML
obscura fetch https://news.ycombinator.com --dump html

# Write dump or eval output to a file
obscura fetch https://example.com --dump text --output page.txt

# Stream the raw response body verbatim (binary-safe; bypasses the JS/DOM layer).
# Use this for images, JSON, JS, CSS, or any non-HTML resource.
obscura fetch https://picsum.photos/200/300 --dump original > photo.jpg

# List every sub-resource URL the page would fetch (NDJSON; one record per asset)
obscura fetch https://example.com --dump assets

# Fetch through an HTTP or SOCKS proxy
obscura --proxy socks5://127.0.0.1:1080 fetch https://example.com --dump text

# Wait for dynamic content
obscura fetch https://example.com --wait-until networkidle0

# Bound navigation time for slow or broken pages
obscura fetch https://example.com --timeout 10
```

### 启动 CDP 服务器

```bash
obscura serve --port 9222

# With stealth mode (anti-detection + tracker blocking)
obscura serve --port 9222 --stealth
```

### 并行抓取

```bash
obscura scrape url1 url2 url3 ... \
  --concurrency 25 \
  --eval "document.querySelector('h1').textContent" \
  --format json

# Suppress scrape progress on stderr for script-friendly output
obscura scrape https://example.com --quiet --format json

# Scrape workers inherit the global proxy
obscura --proxy http://127.0.0.1:8080 scrape https://example.com https://news.ycombinator.com
```

## 与 Puppeteer / Playwright 集成

### Puppeteer

```bash
npm install puppeteer-core
```

```javascript
import puppeteer from 'puppeteer-core';

const browser = await puppeteer.connect({
  browserWSEndpoint: 'ws://127.0.0.1:9222/devtools/browser',
});

const page = await browser.newPage();
await page.goto('https://news.ycombinator.com');

const stories = await page.evaluate(() =>
  Array.from(document.querySelectorAll('.titleline > a'))
    .map(a => ({ title: a.textContent, url: a.href }))
);
console.log(stories);

await browser.disconnect();
```

### Playwright

```bash
npm install playwright-core
```

```javascript
import { chromium } from 'playwright-core';

const browser = await chromium.connectOverCDP({
  endpointURL: 'ws://127.0.0.1:9222',
});

const page = await browser.newContext().then(ctx => ctx.newPage());
await page.goto('https://en.wikipedia.org/wiki/Web_scraping');
console.log(await page.title());

await browser.close();
```

### 表单提交与登录

```javascript
await page.goto('https://quotes.toscrape.com/login');
await page.evaluate(() => {
  document.querySelector('#username').value = 'admin';
  document.querySelector('#password').value = 'admin';
  document.querySelector('form').submit();
});
// Obscura handles the POST, follows the 302 redirect, maintains cookies
```

## 性能基准测试

页面加载速度：

| 页面类型           | Obscura | Chrome |
|--------------------|---------|--------|
| 静态 HTML          | **51 ms** | ~500 ms |
| JS + XHR + fetch   | **84 ms** | ~800 ms |
| 动态脚本渲染       | **78 ms** | ~700 ms |

## 隐身模式（Stealth）

通过 `--features stealth` 启用。

### 防指纹采集
- 每次会话随机化设备指纹（GPU、屏幕分辨率、Canvas、音频、电池状态）
- 模拟真实的 `navigator.userAgentData`（基于 Chrome 145，包含高熵值参数）
- 确保派发的事件满足 `event.isTrusted = true`
- 隐藏内部属性（使 `Object.keys(window)` 安全）
- 原生函数伪装（`Function.prototype.toString()` 返回 `[native code]`）
- 设置 `navigator.webdriver = undefined`（与真实 Chrome 一致）

### 追踪器拦截
- 拦截 3,520 个域名
- 阻止分析、广告、遥测和指纹收集脚本加载
- 彻底阻断追踪器资源请求
- 配合 `--stealth` 参数自动启用

## CDP API 支持

Obscura 完整实现了 Chrome DevTools Protocol，以兼容 Puppeteer 和 Playwright。

| 模块   | 支持的方法                                                                                                                               |
|--------|------------------------------------------------------------------------------------------------------------------------------------------|
| **Target** | createTarget, closeTarget, attachToTarget, createBrowserContext, disposeBrowserContext                                                   |
| **Page**   | navigate, getFrameTree, addScriptToEvaluateOnNewDocument, lifecycleEvents                                                                |
| **Runtime**| evaluate, callFunctionOn, getProperties, addBinding                                                                                        |
| **DOM**    | getDocument, querySelector, querySelectorAll, getOuterHTML, resolveNode                                                                    |
| **Network**| enable, setCookies, getCookies, setExtraHTTPHeaders, setUserAgentOverride                                                                  |
| **Fetch**  | enable, continueRequest, fulfillRequest, failRequest（支持实时拦截）                                                                       |
| **Storage**| getCookies, setCookies, deleteCookies                                                                                                      |
| **Input**  | dispatchMouseEvent, dispatchKeyEvent                                                                                                       |
| **LP**     | getMarkdown（DOM 转 Markdown 转换）                                                                                                        |

## CLI 命令参考

### 调整 V8 引擎参数

Obscura 直接嵌入了 V8 引擎。使用 `--v8-flags` 可将原始参数透传给 V8，语法与 Chromium 的 `--js-flags` 及 Node.js 命令行标志一致。最常见的用途是调大堆内存上限，以解决重度 JS 页面出现的 `JavaScript heap out of memory` 错误：

```bash
obscura --v8-flags "--max-old-space-size=4096" fetch <url>
```

### `obscura serve`（启动服务器）

启动一个 CDP WebSocket 服务。

| 参数             | 默认值   | 说明                           |
|------------------|----------|--------------------------------|
| `--port`         | `9222`   | WebSocket 端口                 |
| `--proxy`        | —        | HTTP/SOCKS5 代理地址           |
| `--stealth`      | off      | 启用反检测与追踪器拦截         |
| `--workers`      | `1`      | 并行工作进程数量               |
| `--obey-robots`  | off      | 遵守 robots.txt 规则           |

### `obscura fetch <URL>`（抓取页面）

获取并渲染单个网页。

| 参数               | 默认值   | 说明                                                                                               |
|--------------------|----------|----------------------------------------------------------------------------------------------------|
| `--dump`           | `html`   | 输出格式：`html`、`text`、`links`、`markdown`、`assets`（页面引用的所有子资源 URL，NDJSON 格式）或 `original`（原始响应体） |
| `--eval`           | —        | 需要执行的 JavaScript 表达式                                                                       |
| `--wait-until`     | `load`   | 等待条件：`load`、`domcontentloaded`、`networkidle0`                                               |
| `--timeout`        | `30`     | 最大导航时间（秒）                                                                                 |
| `--selector`       | —        | 等待指定的 CSS 选择器出现                                                                          |
| `--stealth`        | off      | 反检测模式                                                                                         |
| `--output`         | —        | 将 dump 或 eval 输出写入文件                                                                       |
| `--quiet`          | off      | 隐藏启动横幅信息                                                                                   |
| `--proxy`          | —        | 继承自全局设置的 HTTP/SOCKS5 代理地址                                                              |

### `obscura scrape <URL...>`（并行抓取）

使用工作进程并行抓取多个 URL。

| 参数             | 默认值   | 说明                                           |
|------------------|----------|------------------------------------------------|
| `--concurrency`  | `10`     | 并行工作进程数                                 |
| `--eval`         | —        | 每页执行的 JS 表达式                           |
| `--format`       | `json`   | 输出格式：`json` 或 `text`                     |
| `--quiet`        | off      | 在 stderr 中隐藏抓取进度                       |
| `--proxy`        | —        | 所有工作进程继承的全局 HTTP/SOCKS5 代理地址     |

## MCP（模型上下文协议）支持

Obscura 内置了 MCP 服务器，可向 AI 代理（如 Claude Desktop、Cursor 等）暴露浏览器自动化工具。

### 启动方式

**stdio（默认）** —— 适用于 Claude Desktop 及通过子进程启动的 MCP 客户端：

```bash
obscura mcp
```

**HTTP** —— 适用于通过网络连接的客户端：

```bash
obscura mcp --http --port 8080
# endpoint: http://127.0.0.1:8080/mcp
```

可选参数（两种传输方式均支持）：

| 参数                  | 说明                     |
|-----------------------|--------------------------|
| `--proxy <URL>`       | HTTP/SOCKS5 代理地址     |
| `--user-agent <UA>`   | 自定义 User-Agent 字符串 |
| `--stealth`           | 启用反检测模式           |

### Claude Desktop 配置示例

```json
{
  "mcpServers": {
    "obscura": {
      "command": "obscura",
      "args": ["mcp"]
    }
  }
}
```

### 可用工具

| 工具名                 | 说明                                                                                     |
|------------------------|------------------------------------------------------------------------------------------|
| `browser_navigate`     | 导航至指定 URL（支持可选参数 `waitUntil`: `load` / `domcontentloaded` / `networkidle0`） |
| `browser_snapshot`     | 返回当前页面的 URL、标题和正文文本                                                       |
| `browser_click`        | 通过 CSS 选择器点击元素                                                                  |
| `browser_fill`         | 设置输入框的值（自动触发 `input` + `change` 事件）                                       |
| `browser_type`         | 向输入框追加文本                                                                         |
| `browser_press_key`    | 派发键盘按键事件（支持 `key`，可选指定 `selector`）                                      |
| `browser_select_option`| 按值或文本选择 `<option>`                                                                |
| `browser_evaluate`     | 执行 JavaScript 表达式并返回结果                                                         |
| `browser_wait_for`     | 等待 CSS 选择器出现（支持 `selector`，可选指定超时时间秒数）                             |
| `browser_network_requests` | 列出当前页面发起的网络请求                                                           |
| `browser_console_messages` | 返回页面记录的 Console 日志消息                                                        |
| `browser_close`        | 关闭标签页并重置浏览器状态                                                               |

## 开源协议

Apache-2.0