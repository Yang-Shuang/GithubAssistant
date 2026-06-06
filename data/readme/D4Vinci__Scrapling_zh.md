<!-- mcp-name: io.github.D4Vinci/Scrapling -->

<h1 align="center">
    <a href="https://scrapling.readthedocs.io">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/docs/assets/cover_dark.svg?sanitize=true">
          <img alt="Scrapling Poster" src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/docs/assets/cover_light.svg?sanitize=true">
        </picture>
    </a>
    <br>
    <small>轻松应对现代网页的数据抓取</small>
</h1>

<p align="center">
    <a href="https://trendshift.io/repositories/14244" target="_blank"><img src="https://trendshift.io/api/badge/repositories/14244" alt="D4Vinci%2FScrapling | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
    <br/>
    <a href="https://github.com/D4Vinci/Scrapling/blob/main/docs/README_AR.md">العربيه</a> | <a href="https://github.com/D4Vinci/Scrapling/blob/main/docs/README_ES.md">Español</a> | <a href="https://github.com/D4Vinci/Scrapling/blob/main/docs/README_PT_BR.md">Português (Brasil)</a> | <a href="https://github.com/D4Vinci/Scrapling/blob/main/docs/README_FR.md">Français</a> | <a href="https://github.com/D4Vinci/Scrapling/blob/main/docs/README_DE.md">Deutsch</a> | <a href="https://github.com/D4Vinci/Scrapling/blob/main/docs/README_CN.md">简体中文</a> | <a href="https://github.com/D4Vinci/Scrapling/blob/main/docs/README_JP.md">日本語</a> |  <a href="https://github.com/D4Vinci/Scrapling/blob/main/docs/README_RU.md">Русский</a> | <a href="https://github.com/D4Vinci/Scrapling/blob/main/docs/README_KR.md">한국어</a>
    <br/>
    <a href="https://github.com/D4Vinci/Scrapling/actions/workflows/tests.yml" alt="Tests">
        <img alt="Tests" src="https://github.com/D4Vinci/Scrapling/actions/workflows/tests.yml/badge.svg"></a>
    <a href="https://badge.fury.io/py/Scrapling" alt="PyPI version">
        <img alt="PyPI version" src="https://badge.fury.io/py/Scrapling.svg"></a>
    <a href="https://clickpy.clickhouse.com/dashboard/scrapling" rel="nofollow"><img src="https://img.shields.io/pypi/dm/scrapling" alt="PyPI package downloads"></a>
    <a href="https://github.com/D4Vinci/Scrapling/tree/main/agent-skill" alt="AI Agent Skill directory">
        <img alt="Static Badge" src="https://img.shields.io/badge/Skill-black?style=flat&label=Agent&link=https%3A%2F%2Fgithub.com%2FD4Vinci%2FScrapling%2Ftree%2Fmain%2Fagent-skill"></a>
    <a href="https://clawhub.ai/D4Vinci/scrapling-official" alt="OpenClaw Skill">
        <img alt="OpenClaw Skill" src="https://img.shields.io/badge/Clawhub-darkred?style=flat&label=OpenClaw&link=https%3A%2F%2Fclawhub.ai%2FD4Vinci%2Fscrapling-official"></a>
    <br/>
    <a href="https://discord.gg/EMgGbDceNQ" alt="Discord" target="_blank">
      <img alt="Discord" src="https://img.shields.io/discord/1360786381042880532?style=social&logo=discord&link=https%3A%2F%2Fdiscord.gg%2FEMgGbDceNQ">
    </a>
    <a href="https://x.com/Scrapling_dev" alt="X (formerly Twitter)">
      <img alt="X (formerly Twitter) Follow" src="https://img.shields.io/twitter/follow/Scrapling_dev?style=social&logo=x&link=https%3A%2F%2Fx.com%2FScrapling_dev">
    </a>
    <br/>
    <a href="https://pypi.org/project/scrapling/" alt="Supported Python versions">
        <img alt="Supported Python versions" src="https://img.shields.io/pypi/pyversions/scrapling.svg"></a>
</p>

<p align="center">
    <a href="https://scrapling.readthedocs.io/en/latest/parsing/selection.html"><strong>选择方法</strong></a>
    &middot;
    <a href="https://scrapling.readthedocs.io/en/latest/fetching/choosing.html"><strong>请求器（Fetcher）</strong></a>
    &middot;
    <a href="https://scrapling.readthedocs.io/en/latest/spiders/architecture.html"><strong>爬虫框架（Spider）</strong></a>
    &middot;
    <a href="https://scrapling.readthedocs.io/en/latest/spiders/proxy-blocking.html"><strong>代理轮换</strong></a>
    &middot;
    <a href="https://scrapling.readthedocs.io/en/latest/cli/overview.html"><strong>命令行工具（CLI）</strong></a>
    &middot;
    <a href="https://scrapling.readthedocs.io/en/latest/ai/mcp-server.html"><strong>MCP 服务器</strong></a>
</p>

Scrapling 是一款自适应的网页数据抓取框架，能够处理从单次请求到全规模爬取的各种任务。

其解析器能够学习网页结构的变化，并在页面更新时自动重新定位目标元素。内置的请求器（Fetcher）开箱即用即可绕过 Cloudflare Turnstile 等反爬系统。爬虫框架支持扩展至并发多会话爬取，具备暂停/恢复和自动代理轮换功能——仅需几行 Python 代码即可完成。一个库，零妥协。

提供实时统计与流式传输的极速爬取体验。由网页抓取开发者为同行及普通用户打造，总有一款适合你。

```python
from scrapling.fetchers import Fetcher, AsyncFetcher, StealthyFetcher, DynamicFetcher
StealthyFetcher.adaptive = True
p = StealthyFetcher.fetch('https://example.com', headless=True, network_idle=True)  # 隐蔽地抓取网站！
products = p.css('.product', auto_save=True)                                        # 抓取能抵御网页设计变更的数据！
products = p.css('.product', adaptive=True)                                         # 稍后若网站结构发生变化，传入 `adaptive=True` 即可重新找到它们！
```
或扩展至完整爬取任务：
```python
from scrapling.spiders import Spider, Response

class MySpider(Spider):
  name = "demo"
  start_urls = ["https://example.com/"]

  async def parse(self, response: Response):
      for item in response.css('.product'):
          yield {"title": item.css('h2::text').get()}

MySpider().start()
```

<p align="center">
    <a href="https://dataimpulse.com/?utm_source=scrapling&utm_medium=banner&utm_campaign=scrapling" target="_blank" style="display:flex; justify-content:center; padding:4px 0;">
        <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/DataImpulse.png" alt="At DataImpulse, we specialize in developing custom proxy services for your business. Make requests from anywhere, collect data, and enjoy fast connections with our premium proxies." style="max-height:60px;">
    </a>
</p>

# 铂金赞助商（Platinum Sponsors）
<table>
  <tr>
    <td width="200">
      <a href="https://coldproxy.com/" target="_blank" title="Residential, IPv6 & Datacenter Proxies for Web Scraping">
        <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/coldproxy.png">
      </a>
    </td>
    <td> <a href="https://coldproxy.com/" target="_blank"><b>ColdProxy</b></a> 提供住宅代理和数据中心代理，用于稳定的网页抓取、公开数据收集以及覆盖 195+ 国家的地理定向测试。
    </td>
  </tr>
  <tr>
    <td width="200">
      <a href="https://hypersolutions.co/?utm_source=github&utm_medium=readme&utm_campaign=scrapling" target="_blank" title="Bot Protection Bypass API for Akamai, DataDome, Incapsula & Kasada">
        <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/HyperSolutions.png">
      </a>
    </td>
    <td> Scrapling 已处理 Cloudflare Turnstile。针对企业级防护，<a href="https://hypersolutions.co?utm_source=github&utm_medium=readme&utm_campaign=scrapling"><b>Hyper Solutions</b></a> 提供 API 端点，可为 <b>Akamai</b>、<b>DataDome</b>、<b>Kasada</b> 和 <b>Incapsula</b> 生成有效的反机器人令牌。只需简单的 API 调用，无需浏览器自动化。</td>
  </tr>
  <tr>
    <td width="200">
      <a href="https://birdproxies.com/t/scrapling" target="_blank" title="At Bird Proxies, we eliminate your pains such as banned IPs, geo restriction, and high costs so you can focus on your work.">
        <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/BirdProxies.jpg">
      </a>
    </td>
    <td>嘿，我们开发了 <a href="https://birdproxies.com/t/scrapling"><b>BirdProxies</b></a>，因为代理不应该复杂或价格虚高。覆盖 195+ 地区的快速住宅和 ISP 代理，定价合理，提供真实技术支持。<br /><b>在着陆页免费试玩我们的 Flappy Bird 游戏，即可获取免费数据额度！</b>
    </td>
  </tr>
  <tr>
    <td width="200">
      <a href="https://evomi.com?utm_source=github&utm_medium=banner&utm_campaign=d4vinci-scrapling" target="_blank" title="Evomi is your Swiss Quality Proxy Provider, starting at $0.49/GB">
        <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/evomi.png">
      </a>
    </td>
    <td><a href="https://evomi.com?utm_source=github&utm_medium=banner&utm_campaign=d4vinci-scrapling"><b>Evomi</b></a>：住宅代理低至 $0.49/GB。配备完全伪造 Chromium 的抓取浏览器、住宅 IP、自动验证码破解和反爬绕过功能。</br><b>免折腾的 Scraper API，支持 MCP 和 N8N 集成。</b>
    </td>
  </tr>
  <tr>
    <td width="200">
      <a href="https://tikhub.io/?utm_source=github.com/D4Vinci/Scrapling&utm_medium=marketing_social&utm_campaign=retargeting&utm_content=carousel_ad" target="_blank" title="Unlock the Power of Social Media Data & AI">
        <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/TikHub.jpg">
      </a>
    </td>
    <td><a href="https://tikhub.io/?utm_source=github.com/D4Vinci/Scrapling&utm_medium=marketing_social&utm_campaign=retargeting&utm_content=carousel_ad" target="_blank">TikHub.io</a> 提供覆盖 TikTok、X、YouTube 及 Instagram 等 16+ 个平台的 900+ 稳定 API，拥有 4000万+ 数据集。<br />同时提供 <a href="https://ai.tikhub.io/?ref=KarimShoair" target="_blank">折扣 AI 模型</a> - Claude、GPT、GEMINI 等最高可享 71% 优惠。
    </td>
  </tr>
  <tr>
    <td width="200">
      <a href="https://www.nsocks.com/?keyword=2p67aivg" target="_blank" title="Scalable Web Data Access for AI Applications">
        <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/nsocks.png">
      </a>
    </td>
    <td><a href="https://www.nsocks.com/?keyword=2p67aivg" target="_blank">Nsocks</a> 为开发者和抓取工具提供高速住宅和 ISP 代理。全球 IP 覆盖，高匿名性，智能轮换，性能可靠，适用于自动化和数据提取。使用 <a href="https://www.xcrawl.com/?keyword=2p67aivg" target="_blank">Xcrawl</a> 简化大规模网页爬取。
    </td>
  </tr>
  <tr>
    <td width="200">
      <a href="https://petrosky.io/d4vinci" target="_blank" title="PetroSky delivers cutting-edge VPS hosting.">
        <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/petrosky.png">
      </a>
    </td>
    <td>合上笔记本。你的爬虫仍在运行。<br /><a href="https://petrosky.io/d4vinci" target="_blank">PetroSky VPS</a> - 专为不间断自动化构建的云服务器。提供 Windows 和 Linux 机器，完全控制权。低至 €6.99/月。
    </td>
  </tr>
  <tr>
    <td width="200">
      <a href="https://substack.thewebscraping.club/p/scrapling-hands-on-guide?utm_source=github&utm_medium=repo&utm_campaign=scrapling" target="_blank" title="The #1 newsletter dedicated to Web Scraping">
        <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/TWSC.png">
      </a>
    </td>
    <td>阅读 <a href="https://substack.thewebscraping.club/p/scrapling-hands-on-guide?utm_source=github&utm_medium=repo&utm_campaign=scrapling" target="_blank">The Web Scraping Club (2025年11月)</a>（专注于网页抓取的 #1 通讯）对 <a href="https://substack.thewebscraping.club/p/scrapling-hands-on-guide?utm_source=github&utm_medium=repo&utm_campaign=scrapling" target="_blank">Scrapling</a> 的完整评测。
    </td>
  </tr>
  <tr>
    <td width="200">
      <a href="https://www.swiftproxy.net/?ref=D4Vinci" target="_blank" title="Scalable Solutions for Web Data Access">
        <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/SwiftProxy.png">
      </a>
    </td>
    <td><a href="https://www.swiftproxy.net/?ref=D4Vinci" target="_blank">Swiftproxy</a> 提供可扩展的住宅代理，覆盖 195+ 国家的 8000万+ IP，提供快速可靠的连接、自动轮换和强大的防封禁性能。提供免费试用。
    </td>
  </tr>
  <tr>
    <td width="200">
      <a href="https://9proxy.com/pricing?tab=traffic&utm_source=Github&utm_campaign=D4vinci" target="_blank" title="Top-Tier Residential Proxy Solution for the Highest Success Rate">
        <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/9proxy.jpg">
      </a>
    </td>
    <td><a href="https://9proxy.com/pricing?tab=traffic&utm_source=Github&utm_campaign=D4vinci" target="_blank">9Proxy</a> 提供低至 $0.015/IP 或 $0.68/GB 的住宅代理。覆盖 90+ 国家的 2000万+ IP。支持粘性或轮换会话，可通过桌面或移动应用管理。
    </td>
  </tr>
  <tr>
    <td width="200">
      <a href="https://go.nodemaven.com/scrapling" target="_blank" title="Proxies with the Highest IP Scores">
        <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/NodeMaven.png">
      </a>
    </td>
    <td><a href="https://go.nodemaven.com/scrapling" target="_blank">NodeMaven</a> - 可靠且提供市场最高质量 IP 的代理提供商。使用促销代码 SCRAPLING35 享受代理 35% 折扣。
    </td>
  </tr>
</table>

<i><sub>想在这里展示你的广告？点击[此处](https://github.com/sponsors/D4Vinci/sponsorships?tier_id=586646)</sub></i>
# 赞助商 

<!-- sponsors -->

<a href="https://serpapi.com/?utm_source=scrapling" target="_blank" title="Scrape Google and other search engines with SerpApi"><img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/SerpApi.png"></a>
<a href="https://visit.decodo.com/Dy6W0b" target="_blank" title="Try the Most Efficient Residential Proxies for Free"><img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/decodo.png"></a>
<a href="https://hasdata.com/?utm_source=github&utm_medium=banner&utm_campaign=D4Vinci" target="_blank" title="The web scraping service that actually beats anti-bot systems!"><img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/hasdata.png"></a>
<a href="https://proxyempire.io/?ref=scrapling&utm_source=scrapling" target="_blank" title="Collect The Data Your Project Needs with the Best Residential Proxies"><img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/ProxyEmpire.png"></a>
<a href="https://www.webshare.io/?referral_code=48r2m2cd5uz1" target="_blank" title="The Most Reliable Proxy with Unparalleled Performance"><img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/webshare.png"></a>
<a href="https://proxiware.com/?ref=scrapling" target="_blank" title="Collect Any Data. At Any Scale."><img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/proxiware.png"></a>


<!-- /sponsors -->

<i><sub>想在这里展示你的广告？点击[此处](https://github.com/sponsors/D4Vinci)并选择适合你的赞助档位！</sub></i>

---

## 核心特性

### 爬虫框架（Spiders）- 完整的爬取架构
- 🕷️ **类 Scrapy 的 Spider API**：通过 `start_urls`、异步 `parse` 回调以及 `Request`/`Response` 对象定义爬虫。
- ⚡ **并发爬取**：可配置并发限制、域名限速和下载延迟。
- 🔄 **多会话支持**：统一的 HTTP 请求接口，并在单一爬虫中集成隐身无头浏览器——通过 ID 将请求路由到不同会话。
- 💾 **暂停与恢复**：基于检查点的爬取持久化。按 Ctrl+C 优雅关闭；重启后从断点继续。
- 📡 **流式模式**：通过 `async for item in spider.stream()` 实时接收抓取数据并附带统计信息——适用于 UI、管道和长时间运行的爬取任务。
- 🛡️ **请求拦截检测**：自动检测被拦截的请求，并使用可自定义的逻辑进行重试。
- 🤖 **遵守 robots.txt**：可选的 `robots_txt_obey` 标志，尊重 `Disallow`、`Crawl-delay` 和 `Request-rate` 指令，并支持域名级缓存。
- 🧪 **开发模式**：首次运行时将响应缓存到磁盘，后续运行直接回放——无需重复请求目标服务器即可迭代 `parse()` 逻辑。
- 📦 **内置导出**：通过钩子函数、自定义管道或内置的 JSON/JSONL（分别使用 `result.items.to_json()` / `result.items.to_jsonl()`）导出数据。

### 高级网页请求与会话管理
- **HTTP 请求**：使用 `Fetcher` 类实现快速且隐蔽的 HTTP 请求。可模拟浏览器的 TLS 指纹、Header，并支持 HTTP/3。
- **动态加载**：通过 `DynamicFetcher` 类（支持 Playwright Chromium 和 Google Chrome）进行完整的浏览器自动化以抓取动态网页。
- **反爬绕过**：`StealthyFetcher` 提供高级隐身能力和指纹伪造，可轻松绕过所有类型的 Cloudflare Turnstile/Interstitial。
- **会话管理**：通过 `FetcherSession`、`StealthySession` 和 `DynamicSession` 类实现持久化会话支持，跨请求管理 Cookie 和状态。
- **代理轮换**：内置 `ProxyRotator`，支持循环或自定义轮换策略（适用于所有会话类型），并支持单次请求级别的代理覆盖。
- **域名与广告拦截**：可阻断特定域名（及其子域名）的请求，或在基于浏览器的抓取器中启用内置广告拦截（约 3,500 个已知广告/追踪域名）。
- **DNS 泄露防护**：可选的 DNS-over-HTTPS (DoH) 支持，将 DNS 查询路由至 Cloudflare DoH，在使用代理时防止 DNS 泄露。
- **异步支持**：所有请求器和专用异步会话类均提供完整的异步支持。

### 自适应抓取与 AI 集成
- 🔄 **智能元素追踪**：使用智能相似度算法在网页结构变更后重新定位目标元素。
- 🎯 **灵活选择器**：支持 CSS 选择器、XPath 选择器、基于过滤器的搜索、文本搜索、正则表达式搜索等。
- 🔍 **查找相似元素**：自动定位与已找到元素相似的节点。
- 🤖 **内置 MCP 服务器（配合 AI 使用）**：为 AI 辅助网页抓取和数据提取提供内置 MCP 服务器。该服务器具备强大的自定义功能，可在将数据传递给 AI（Claude/Cursor 等）之前利用 Scrapling 提取目标内容，从而减少 Token 消耗、提升操作速度并降低成本。（[演示视频](https://www.youtube.com/watch?v=qyFk3ZNwOxE)）

### 高性能与经过实战检验的架构
- 🚀 **极速性能**：优化后的性能超越大多数 Python 抓取库。
- 🔋 **内存高效**：优化的数据结构和懒加载机制，保持极低的内存占用。
- ⚡ **快速 JSON 序列化**：比标准库快 10 倍。
- 🏗️ **实战检验**：Scrapling 不仅拥有 92% 的测试覆盖率和完整的类型提示覆盖率，过去一年更被数百名网页抓取开发者每日使用。

### 对开发者/爬虫工程师友好的体验
- 🎯 **交互式网页抓取 Shell**：可选内置 IPython shell，集成 Scrapling 功能、快捷键和新工具（如将 curl 请求转换为 Scrapling 请求、在浏览器中查看请求结果），加速脚本开发。
- 🚀 **直接从终端使用**：无需编写任何代码即可直接使用 Scrapling 抓取 URL！
- 🛠️ **丰富的导航 API**：支持父级、同级和子级的高级 DOM 遍历方法。
- 🧬 **增强的文本处理**：内置正则表达式、清洗方法和优化的字符串操作。
- 📝 **自动选择器生成**：为任意元素生成稳健的 CSS/XPath 选择器。
- 🔌 **熟悉的 API**：与 Scrapy/BeautifulSoup 类似，使用与 Scrapy/Parsel 相同的伪元素语法。
- 📘 **完整的类型覆盖**：提供全面的类型提示以支持优秀的 IDE 体验和代码补全。整个代码库在每次更改时都会自动通过 **PyRight** 和 **MyPy** 扫描。
- 🔋 **开箱即用的 Docker 镜像**：每次发布时，会自动构建并推送包含所有浏览器的 Docker 镜像。

## 快速入门

无需深入细节，先带你快速了解 Scrapling 的能力。

### 基础用法
支持会话的 HTTP 请求
```python
from scrapling.fetchers import Fetcher, FetcherSession

with FetcherSession(impersonate='chrome') as session:  # 使用最新版本的 Chrome TLS 指纹
    page = session.get('https://quotes.toscrape.com/', stealthy_headers=True)
    quotes = page.css('.quote .text::text').getall()

# 或使用一次性请求
page = Fetcher.get('https://quotes.toscrape.com/')
quotes = page.css('.quote .text::text').getall()
```
高级隐身模式
```python
from scrapling.fetchers import StealthyFetcher, StealthySession

with StealthySession(headless=True, solve_cloudflare=True) as session:  # 保持浏览器打开直至完成
    page = session.fetch('https://nopecha.com/demo/cloudflare', google_search=False)
    data = page.css('#padded_content a').getall()

# 或使用一次性请求风格，它会在本次请求时打开浏览器，完成后自动关闭
page = StealthyFetcher.fetch('https://nopecha.com/demo/cloudflare')
data = page.css('#padded_content a').getall()
```
完整的浏览器自动化
```python
from scrapling.fetchers import DynamicFetcher, DynamicSession

with DynamicSession(headless=True, disable_resources=False, network_idle=True) as session:  # 保持浏览器打开直至完成
    page = session.fetch('https://quotes.toscrape.com/', load_dom=False)
    data = page.xpath('//span[@class="text"]/text()').getall()  # 如果你偏好 XPath

# 或使用一次性请求风格，它会在本次请求时打开浏览器，完成后自动关闭
page = DynamicFetcher.fetch('https://quotes.toscrape.com/')
data = page.css('.quote .text::text').getall()
```

### 爬虫（Spiders）
构建支持并发请求、多会话类型及暂停/恢复的完整爬取器：
```python
from scrapling.spiders import Spider, Request, Response

class QuotesSpider(Spider):
    name = "quotes"
    start_urls = ["https://quotes.toscrape.com/"]
    concurrent_requests = 10
    
    async def parse(self, response: Response):
        for quote in response.css('.quote'):
            yield {
                "text": quote.css('.text::text').get(),
                "author": quote.css('.author::text').get(),
            }
            
        next_page = response.css('.next a')
        if next_page:
            yield response.follow(next_page[0].attrib['href'])

result = QuotesSpider().start()
print(f"Scraped {len(result.items)} quotes")
result.items.to_json("quotes.json")
```
在单个爬虫中使用多种会话类型：
```python
from scrapling.spiders import Spider, Request, Response
from scrapling.fetchers import FetcherSession, AsyncStealthySession

class MultiSessionSpider(Spider):
    name = "multi"
    start_urls = ["https://example.com/"]
    
    def configure_sessions(self, manager):
        manager.add("fast", FetcherSession(impersonate="chrome"))
        manager.add("stealth", AsyncStealthySession(headless=True), lazy=True)
    
    async def parse(self, response: Response):
        for link in response.css('a::attr(href)').getall():
            # 将受保护的页面路由至隐身会话
            if "protected" in link:
                yield Request(link, sid="stealth")
            else:
                yield Request(link, sid="fast", callback=self.parse)  # 显式回调
```
通过指定 `crawldir` 暂停和恢复长时间运行的爬取任务：
```python
QuotesSpider(crawldir="./crawl_data").start()
```
按 Ctrl+C 优雅暂停——进度会自动保存。稍后重新启动爬虫时，传入相同的 `crawldir`，它将从停止处继续。

### 高级解析与导航
```python
from scrapling.fetchers import Fetcher

# 丰富的元素选择与导航
page = Fetcher.get('https://quotes.toscrape.com/')

# 使用多种选择方法获取引用内容
quotes = page.css('.quote')  # CSS 选择器
quotes = page.xpath('//div[@class="quote"]')  # XPath
quotes = page.find_all('div', {'class': 'quote'})  # BeautifulSoup 风格
# 等同于
quotes = page.find_all('div', class_='quote')
quotes = page.find_all(['div'], class_='quote')
quotes = page.find_all(class_='quote')  # 以此类推...
# 按文本内容查找元素
quotes = page.find_by_text('quote', tag='div')

# 高级导航
quote_text = page.css('.quote')[0].css('.text::text').get()
quote_text = page.css('.quote').css('.text::text').getall()  # 链式选择器
first_quote = page.css('.quote')[0]
author = first_quote.next_sibling.css('.author::text')
parent_container = first_quote.parent

# 元素关系与相似度
similar_elements = first_quote.find_similar()
below_elements = first_quote.below_elements()
```
如果你不想抓取网站，也可以直接使用解析器：
```python
from scrapling.parser import Selector

page = Selector("<html>...</html>")
```
用法完全一致！

### 异步会话管理示例
```python
import asyncio
from scrapling.fetchers import FetcherSession, AsyncStealthySession, AsyncDynamicSession

async with FetcherSession(http3=True) as session:  # `FetcherSession` 感知上下文，可在同步/异步模式下工作
    page1 = session.get('https://quotes.toscrape.com/')
    page2 = session.get('https://quotes.toscrape.com/', impersonate='firefox135')

# 异步会话用法
async with AsyncStealthySession(max_pages=2) as session:
    tasks = []
    urls = ['https://example.com/page1', 'https://example.com/page2']
    
    for url in urls:
        task = session.fetch(url)
        tasks.append(task)
    
    print(session.get_pool_stats())  # 可选 - 浏览器标签页池的状态（忙碌/空闲/错误）
    results = await asyncio.gather(*tasks)
    print(session.get_pool_stats())
```

## CLI & 交互式 Shell

Scrapling 内置强大的命令行界面：

[![asciicast](https://asciinema.org/a/736339.svg)](https://asciinema.org/a/736339)

启动交互式网页抓取 Shell
```bash
scrapling shell
```
无需编写代码即可直接将页面内容提取到文件中（默认提取 `body` 标签内的内容）。若输出文件以 `.txt` 结尾，则提取纯文本；以 `.md` 结尾则为 Markdown 格式的 HTML 内容；以 `.html` 结尾则保留原始 HTML。
```bash
scrapling extract get 'https://example.com' content.md
scrapling extract get 'https://example.com' content.txt --css-selector '#fromSkipToProducts' --impersonate 'chrome'  # 所有匹配 CSS 选择器 '#fromSkipToProducts' 的元素
scrapling extract fetch 'https://example.com' content.md --css-selector '#fromSkipToProducts' --no-headless
scrapling extract stealthy-fetch 'https://nopecha.com/demo/cloudflare' captchas.html --css-selector '#padded_content a' --solve-cloudflare
```

> [!NOTE]
> 本文档力求简洁，因此未详细展开所有功能（包括 MCP 服务器和交互式网页抓取 Shell）。请查阅完整文档：[这里](https://scrapling.readthedocs.io/en/latest/)

## 性能基准测试

Scrapling 不仅功能强大，而且速度极快。以下基准测试将 Scrapling 的解析器与其他流行库的最新版本进行了对比。

### 文本提取速度测试（5000 个嵌套元素）

| # |      Library      | Time (ms) | vs Scrapling | 
|---|:-----------------:|:---------:|:------------:|
| 1 |     Scrapling     |   2.02    |     1.0x     |
| 2 |   Parsel/Scrapy   |   2.04    |     1.01     |
| 3 |     Raw Lxml      |   2.54    |    1.257     |
| 4 |      PyQuery      |   24.17   |     ~12x     |
| 5 |    Selectolax     |   82.63   |     ~41x     |
| 6 |  MechanicalSoup   |  1549.71  |   ~767.1x    |
| 7 |   BS4 with Lxml   |  1584.31  |   ~784.3x    |
| 8 | BS4 with html5lib |  3391.91  |   ~1679.1x   |


### 元素相似度与文本搜索性能

Scrapling 的自适应元素查找能力显著优于其他替代方案：

| Library     | Time (ms) | vs Scrapling |
|-------------|:---------:|:------------:|
| Scrapling   |   2.39    |     1.0x     |
| AutoScraper |   12.45   |    5.209x    |


> 所有基准测试均为 100+ 次运行的平均值。查看 [benchmarks.py](https://github.com/D4Vinci/Scrapling/blob/main/benchmarks.py) 了解具体方法。

## 安装

Scrapling 需要 Python 3.10 或更高版本：

```bash
pip install scrapling
```

此安装仅包含解析器引擎及其依赖项，不包含请求器或命令行工具依赖。

### 可选依赖项

1. 如果你计划使用以下任何额外功能、请求器或其类，则需要安装请求器的依赖项及浏览器依赖项：
    ```bash
    pip install "scrapling[fetchers]"
    
    scrapling install           # 正常安装
    scrapling install  --force  # 强制重新安装
    ```

    这将下载所有浏览器及其系统依赖和指纹伪造依赖。

    或者你也可以通过代码而非命令行进行安装：
    ```python
    from scrapling.cli import install
    
    install([], standalone_mode=False)          # 正常安装
    install(["--force"], standalone_mode=False) # 强制重新安装
    ```

2. 额外功能：
   - 安装 MCP 服务器功能：
       ```bash
       pip install "scrapling[ai]"
       ```
   - 安装 Shell 功能（网页抓取 Shell 和 `extract` 命令）： 
       ```bash
       pip install "scrapling[shell]"
       ```
   - 安装所有功能： 
       ```bash
       pip install "scrapling[all]"
       ```
   请记住，在使用上述任何额外功能后（如果尚未执行），你需要通过 `scrapling install` 安装浏览器依赖项。

### Docker
你还可以通过以下命令从 DockerHub 拉取包含所有扩展和浏览器的镜像：
```bash
docker pull pyd4vinci/scrapling
```
或从 GitHub 注册表下载：
```bash
docker pull ghcr.io/d4vinci/scrapling:latest
```
该镜像通过 GitHub Actions 和仓库主分支自动构建并推送。

## 贡献指南

我们欢迎贡献！请在开始之前阅读我们的[贡献指南](https://github.com/D4Vinci/Scrapling/blob/main/CONTRIBUTING.md)。

## 免责声明

> [!CAUTION]
> 本库仅供教育和研究目的使用。使用该库即表示你同意遵守当地及国际数据抓取和隐私法律法规。作者与贡献者不对任何滥用该软件的行为负责。请始终尊重目标网站的服务条款（ToS）及 robots.txt 文件。

## 🎓 引用指南
如果你在我们的研究中使用了此库，请使用以下引用格式：
```text
  @misc{scrapling,
    author = {Karim Shoair},
    title = {Scrapling},
    year = {2024},
    url = {https://github.com/D4Vinci/Scrapling},
    note = {An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl!}
  }
```

## 许可证

本项目采用 BSD-3-Clause 许可证开源。

## 致谢

该项目包含改编自以下项目的代码：
- Parsel (BSD License)-Used for [translator](https://github.com/D4Vinci/Scrapling/blob/main/scrapling/core/translator.py) submodule

---
<div align="center"><small>Designed & crafted with ❤️ by Karim Shoair.</small></div><br>