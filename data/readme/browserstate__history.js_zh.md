## 说明
尽管现代浏览器中确实存在一些 [关于状态处理的合法 bug 和差异](https://github.com/browserstate/history.js/wiki/The-State-of-the-HTML5-History-API)，但它们现在相对较小，你完全可以直接使用原生的 HTML5 History API。如果你打算支持旧版浏览器，那么 History.js 是你的首选。

之所以添加此说明，是因为 History.js 缺乏足够的资金来维持维护，因此它仅以遗留状态服务于旧版浏览器。它在现代浏览器中可能仍然有效，但确实需要维护。由于该库需要在 HTML5 和 HTML4 模式下、针对每个适配器以及每种浏览器进行手动测试，因此维护非常困难。这意味着需要进行 `` `2^(# of adapters)^(# of browsers and their versions)` `` 次由人工执行的测试。测试必须由人完成，因为某些失败情况需要与浏览器交互（例如从测试套件导航到不同域名再返回，或点击物理后退按钮，或检查物理后退按钮是否真的有效）。这需要耗费大量时间。

尽管 History.js 是最受欢迎的 JavaScript 库之一，甚至曾被拥有数百万用户的公司使用——但现实是，公司的经济状况和做法表明，它们更倾向于 fork（分叉）自己的内部版本并在本地修复，而不是资助开源维护者来为所有人（包括他们自己）做得更好，后者实际上成本更低。但这需要太多不理解该需求的审批层级。

因此，如果你是开源开发者，我建议专注于那些由你自身的咨询工作或公司出资的项目（例如每个成功的开源项目）。否则，当它们变得流行时，最好希望它们易于维护和测试，否则维护成本将高于维护者的空闲时间。

综上所述，该仓库仍然保留用于归档目的、支持旧版浏览器，以及作为无政府式 issue 和 fork 维护的中心枢纽。

祝好，
Benjamin Lupton（Bevry 创始人，History.js 创作者）


欢迎使用 History.js <br/> v1.8b2，2013年6月22日
==================

<!-- BADGES/ -->

<span class="badge-slackin"><a href="https://slack.bevry.me" title="Join this project's slack community"><img src="https://slack.bevry.me/badge.svg" alt="Slack community badge" /></a></span>
<span class="badge-patreon"><a href="http://patreon.com/bevry" title="Donate to this project using Patreon"><img src="https://img.shields.io/badge/patreon-donate-yellow.svg" alt="Patreon donate button" /></a></span>
<span class="badge-gratipay"><a href="https://www.gratipay.com/bevry" title="Donate weekly to this project using Gratipay"><img src="https://img.shields.io/badge/gratipay-donate-yellow.svg" alt="Gratipay donate button" /></a></span>
<span class="badge-flattr"><a href="https://flattr.com/profile/balupton" title="Donate to this project using Flattr"><img src="https://img.shields.io/badge/flattr-donate-yellow.svg" alt="Flattr donate button" /></a></span>
<span class="badge-paypal"><a href="https://bevry.me/paypal" title="Donate to this project using Paypal"><img src="https://img.shields.io/badge/paypal-donate-yellow.svg" alt="PayPal donate button" /></a></span>
<span class="badge-bitcoin"><a href="https://bevry.me/bitcoin" title="Donate once-off to this project using Bitcoin"><img src="https://img.shields.io/badge/bitcoin-donate-yellow.svg" alt="Bitcoin donate button" /></a></span>
<span class="badge-wishlist"><a href="https://bevry.me/wishlist" title="Buy an item on our wishlist for us"><img src="https://img.shields.io/badge/wishlist-donate-yellow.svg" alt="Wishlist browse button" /></a></span>

<!-- /BADGES -->



## 动态
- 2013/06/22：发布 v1.8 Beta 2。修复问题并包含未压缩的打包文件。
- 2013/05/31：发布 v1.8 Beta 1。修复问题。
- 2013/02/14：发布 v1.8 Alpha 4。修复问题。
- 2013/02/05：发布 v1.8 Alpha 3。更新测试。
- 2013/01/21：发布 v1.8 Alpha 2。修正 statechange（状态变更）行为。
- 2013/01/19：发布 v1.8 Alpha 1。开始对 balupton 仓库中的旧 issue 进行分类整理。


### 历史记录
[查看 `HISTORY.md` 文件以获取功能、更改、已解决问题和 bug 的详细列表](https://github.com/browserstate/history.js/blob/master/HISTORY.md#files)


### 参与贡献
如果遇到问题或发现特定浏览器的 bug，请提交 issue。我会尽快修复。如果你有好的解决方案，欢迎提交 Pull Request！我也会审查 balupton 仓库中的旧 issue 并尝试解决它们。


## 设计目标

- 尽可能遵循 [HTML5 History API](https://developer.mozilla.org/en/DOM/Manipulating_the_browser_history)
- 为所有 HTML5 浏览器提供跨兼容体验（它们对 HTML5 History API 的实现略有不同，导致行为各异甚至出现 bug——History.js 修复了这些问题，确保在所有 HTML5 浏览器中的表现符合预期、一致且优秀）
- 为所有 HTML4 浏览器提供向后兼容的体验，使用 hash fallback（哈希回退机制）（包括继续支持 HTML5 History API 的 `data`、`title`、`pushState` 和 `replaceState`），并允许你 [根据应用需求移除对 HTML4 的支持](https://github.com/browserstate/history.js/wiki/Intelligent-State-Handling)
- 为从 HTML4 State（状态）到 HTML5 State 提供向前兼容的体验（例如，当 HTML5 浏览器访问带有 hash fallback 的 URL 时，会自动转换为非 hash 形式的等效 URL）
- 通过适配器尽可能支持更多的 JavaScript 框架；特别是 [Dojo](http://dojotoolkit.org/)、[ExtJS](http://www.sencha.com/)、[jQuery](http://jquery.com/)、[MooTools](http://mootools.net/)、[Right.js](http://rightjs.org/) 和 [Zepto](http://zeptojs.com/)。


## 快速安装

### 通过 Ajaxify 脚本
要使用 HTML5 History API、History.js 和 jQuery 为你的整个网站实现 AJAX 化，只需 [Ajaxify script](https://github.com/browserstate/ajaxify) 即可。就是这么简单。

### 通过 Ajaxify 扩展
如果你无法访问服务器，或者只想先试用 Ajaxify 脚本，可以安装 [History.js It! Google Chrome 扩展](https://github.com/browserstate/historyjsit.crx)，在特定网站上通过 Ajaxify 体验 History.js，而无需在你的服务器上实际安装 History.js/Ajaxify。

### 通过 Ruby on Rails Gem
如果你使用 Rails，那么试用 History.js 最简便的方式是使用 [Wiselinks](https://github.com/igor-alexandrov/wiselinks) gem。Wiselinks 可集成到 Rails 应用中，只需三行代码即可开始使用 History.js。


## 直接使用

### 直接使用 History.js

``` javascript
(function(window,undefined){

	// Bind to StateChange Event
	History.Adapter.bind(window,'statechange',function(){ // Note: We are using statechange instead of popstate
		var State = History.getState(); // Note: We are using History.getState() instead of event.state
	});

	// Change our States
	History.pushState({state:1}, "State 1", "?state=1"); // logs {state:1}, "State 1", "?state=1"
	History.pushState({state:2}, "State 2", "?state=2"); // logs {state:2}, "State 2", "?state=2"
	History.replaceState({state:3}, "State 3", "?state=3"); // logs {state:3}, "State 3", "?state=3"
	History.pushState(null, null, "?state=4"); // logs {}, '', "?state=4"
	History.back(); // logs {state:3}, "State 3", "?state=3"
	History.back(); // logs {state:1}, "State 1", "?state=1"
	History.back(); // logs {}, "Home Page", "?"
	History.go(2); // logs {state:3}, "State 3", "?state=3"

})(window);
```


### 在 HTML5 浏览器中上述操作的效果是怎样的？

1. www.mysite.com
1. www.mysite.com/?state=1
1. www.mysite.com/?state=2
1. www.mysite.com/?state=3
1. www.mysite.com/?state=4
1. www.mysite.com/?state=3
1. www.mysite.com/?state=1
1. www.mysite.com
1. www.mysite.com/?state=3

> 注意：这些 URL 同样适用于 HTML4 浏览器和搜索引擎。因此无需使用 Google ["推荐"](https://github.com/browserstate/history.js/wiki/Intelligent-State-Handling) 的 hashbang (`#!`) fragment-identifier（片段标识符）。


### 在 HTML4 浏览器中它们的效果是怎样的？

1. www.mysite.com
1. www.mysite.com/#?state=1&_suid=1
1. www.mysite.com/#?state=2&_suid=2
1. www.mysite.com/#?state=3&_suid=3
1. www.mysite.com/#?state=4
1. www.mysite.com/#?state=3&_suid=3
1. www.mysite.com/#?state=1&_suid=1
1. www.mysite.com
1. www.mysite.com/#?state=3&_suid=3

> 注意 1：这些 URL 同样适用于 HTML5 浏览器——我们使用 `replaceState` 将这些 HTML4 state（状态）转换为对应的 HTML5 状态，因此用户甚至不会察觉 :-)
>
> 注意 2：在 IE6 中，这些 URL 将自动进行 url-encoded（URL 编码），以防止某些特定浏览器的 bug。
>
> 注意 3：对 HTML4 浏览器（此 hash fallback）的支持是可选的 [- 为什么支持 HTML4 浏览器可能好也可能坏取决于我的应用用例](https://github.com/browserstate/history.js/wiki/Intelligent-State-Handling)


### HTML4 State（状态）中使用的 SUID 是怎么回事？

- SUID（State Unique Identifiers，状态唯一标识符）在我们使用 state 中的 `title` 和/或 `data` 时使用。添加 SUID 允许我们将特定 state 与数据和标题关联起来，同时保持 URL 尽可能简单（不用担心，这已经过测试且运行良好，比我描述的更智能）。
- 如果你没有使用 `title` 或 `data`，我们甚至不会包含 SUID（因为不需要）——如上面的 State 4 所示 :-)
- 我们还会压缩 URL 以确保使用最短的 URL。例如，我们会自动将 `http://www.mysite.com/#http://www.mysite.com/projects/History.js` 调整为 `http://www.mysite.com/#/projects/History.js`。（同样经过测试且运行良好）
- 它适用于域名、子域名、子目录等——无论放在哪里都能正常工作。很智能。
- Safari 5 也会在 URL 后附加一个 SUID，这完全透明但只是一个可见的副作用。它是修复 Safari 5 bug 所必需的。


### 有可用的演示吗？

- 当然有，下载并在浏览器中导航到 demo 目录即可 :-)
- 如果你想要比面向用户的演示更进阶的内容，请在浏览器和编辑器中打开 tests 目录——它会让你大开眼界，并展示 History.js 支持的所有广泛用例。


## 下载与安装

- 下载 History.js 并将其上传到你的 Web 服务器。下载地址：[tar.gz](https://github.com/browserstate/history.js/tarball/master) 或 [zip](https://github.com/browserstate/history.js/zipball/master)

- 引入 History.js

	- 适用于 [Dojo](http://dojotoolkit.org/) v1.8+

		``` html
		<script src="http://www.yourwebsite.com/history.js/scripts/bundled/html4+html5/dojo.history.js"></script>
		```
	
	- 适用于 [ExtJs](http://www.sencha.com/) v1.8+

		``` html
		<script src="http://www.yourwebsite.com/history.js/scripts/bundled/html4+html5/extjs.history.js"></script>
		```
	
	- 适用于 [jQuery](http://jquery.com/) v1.3+

		``` html
		<script src="http://www.yourwebsite.com/history.js/scripts/bundled/html4+html5/jquery.history.js"></script>
		```

	- 适用于 [Mootools](http://mootools.net/) v1.3+

		``` html
		<script src="http://www.yourwebsite.com/history.js/scripts/bundled/html4+html5/mootools.history.js"></script>
		```

	- 适用于 [Right.js](http://rightjs.org/) v2.2+

		``` html
		<script src="http://www.yourwebsite.com/history.js/scripts/bundled/html4+html5/right.history.js"></script>
		```

	- 适用于 [Zepto](http://zeptojs.com/) v0.5+

		``` html
		<script src="http://www.yourwebsite.com/history.js/scripts/bundled/html4+html5/zepto.history.js"></script>
		```

	- 适用于其他所有情况

		``` html
		<script src="http://www.yourwebsite.com/history.js/scripts/bundled/html4+html5/native.history.js"></script>
		```

> 注意：如果你只想支持 HTML5 浏览器而不支持 HTML4 浏览器（即不需要 hash fallback）支持，只需将 URL 中的 `/html4+html5/` 部分改为仅 `/html5/`。参见 [为什么支持 HTML4 浏览器可能好也可能坏取决于我的应用用例](https://github.com/browserstate/history.js/wiki/Intelligent-State-Handling)


## 获取更新

- 订阅 Commit RSS/Atom 更新：
	- 你可以通过 [GitHub Commit Atom Feed](http://feeds.feedburner.com/historyjs) 进行订阅
- 订阅 GitHub 动态 Feed 更新：
	- 你可以点击 History.js [GitHub 项目页面](https://github.com/browserstate/history.js) 右上角的 "watch"（关注）按钮


## 获取支持

- History.js 由像你这样的人维护。如果你发现 bug，请向 [GitHub Issue Tracker](https://github.com/browserstate/history.js/issues) 报告。如果你已修复 bug，请提交 [Pull Request](https://github.com/browserstate/history.js/pulls) 并将你的 fork 添加到 [Network Wiki Page](https://github.com/browserstate/history.js/wiki/Network)。

- 如果你需要付费支持和培训，或有工作邀约，请参阅 [Network Wiki Page](https://github.com/browserstate/history.js/wiki/Network)。如果你具备 History.js 相关资质，也请确保在该页面添加你的详细信息。

- 如果你的公司在项目中使用了 History.js，并希望看到它发展壮大（更好的文档、bug 修复、升级、维护等），并愿意成为企业赞助商，请发送邮件至 sponsor@bevry.me

- 如果你希望获得 History.js 的免费支持，请在 [Stackoverflow](http://stackoverflow.com/about) 上 [发布你的问题](http://stackoverflow.com/questions/ask)，提问时务必使用 `history.js` 标签。

- 如果你创建了使用 History.js 的网站，或知道这样的网站，请确保将其添加到 [Showcase Wiki Page](https://github.com/browserstate/history.js/wiki/Showcase)。

- 如果你喜欢这个项目并想给它点赞，请在 Twitter 上宣传它，并在其 [项目页面](https://github.com/browserstate/history.js) 顶部点击 "watch"（关注）按钮。

- 其他任何问题，请参阅 [History.js GitHub Wiki 站点](https://github.com/browserstate/history.js/wiki)。

感谢！每一份帮助都至关重要！



## 已测试并兼容的浏览器

### HTML5 浏览器

- Firefox 4+
- Chrome 8+
- Opera 11.5+
- Safari 5.0+
- Safari iOS 4.3+


### HTML4 浏览器

- IE 6, 7, 8, 9, (10)
- Firefox 3
- Opera 10, 11.0
- Safari 4
- Safari iOS 4.2, 4.1, 4.0, 3.2



## 公开 API

### 函数

#### State（状态）操作

- `History.pushState(data,title,url)` <br/> 向浏览器推送一个新 state；`data` 可为 null 或对象，`title` 可为 null 或字符串，`url` 必须为字符串
- `History.replaceState(data,title,url)` <br/> 用新 state 替换浏览器中的现有 state；`data` 可为 null 或对象，`title` 可为 null 或字符串，`url` 必须为字符串
- `History.getState()` <br/> 获取浏览器的当前状态，返回包含 `data`、`title` 和 `url` 的对象
- `History.getStateByIndex` <br/> 通过索引获取 state
- `History.getCurrentIndex` <br/> 获取当前索引
- `History.getHash()` <br/> 获取浏览器当前的 hash

#### Adapter（适配器）

- `History.Adapter.bind(element,event,callback)` <br/> 一个与框架无关的事件绑定器，你可以直接使用它或你框架的原生事件绑定器。
- `History.Adapter.trigger(element,event)` <br/> 一个与框架无关的事件触发器，你可以直接使用它或你框架的原生事件触发器。
- `History.Adapter.onDomLoad(callback)` <br/> 一个与框架无关的 onDomLoad 绑定器，你可以直接使用它或你框架的原生 onDomLoad 绑定器。

#### Navigation（导航）

- `History.back()` <br/> 在历史记录中后退一步（等同于点击浏览器的后退按钮）
- `History.forward()` <br/> 在历史记录中前进一步（等同于点击浏览器的前进按钮）
- `History.go(X)` <br/> 如果 X 为负数，则在历史记录中后退 X 步；如果 X 为正数，则在历史记录中前进 X 步

#### Debug（调试）

- `History.log(...)` <br/> 将消息记录到控制台和日志元素中，如果两者都不存在则 fallback 到 alert
- `History.debug(...)` <br/> 与 `History.log` 相同，但仅在 `History.options.debug === true` 时运行



### 配置项

- `History.options.hashChangeInterval` <br/> 两次 hashchange 检查之间的时间间隔应设置为多长
- `History.options.safariPollInterval` <br/> Safari poll 检查的轮询间隔应设置为多长
- `History.options.doubleCheckInterval` <br/> 执行双重检查前的等待时间间隔应设置为多长
- `History.options.disableSuid` <br/> 强制 History 不附加 suid
- `History.options.storeInterval` <br/> store（存储）调用之间的等待时间间隔应设置为多长
- `History.options.busyDelay` <br/> busy（繁忙）事件之间的等待时间间隔应设置为多长
- `History.options.debug` <br/> 如果为 true，将启用调试消息记录
- `History.options.initialTitle` <br/> 初始 state 的标题是什么
- `History.options.html4Mode` <br/> 如果为 true，将强制开启 HTML4 模式（hashtags）
- `History.options.delayInit` <br/> 想要覆盖默认选项并手动调用 init。


### Events（事件）

- `window.onstatechange` <br/> 当页面的 state（状态）发生变化时触发（不包括 hash 变化）
- `window.onanchorchange` <br/> 当页面的 anchor（锚点）发生变化时触发（不包括 state hash）


## 已知问题
- Opera 11 在负载较高时无法创建历史记录条目（事件完美触发，只是历史记录事件失败）——对此我们无能为力
- Mercury iOS 无法应用 URL 更改（hash 和 HTML5 History API state）——对此我们无能为力


## 兼容性说明

- History.js **解决**了以下浏览器 bug：
	- HTML5 浏览器
		- Chrome 8 在回溯到初始状态时，有时不包含正确的 state 数据
		- Safari 5、Safari iOS 4 以及 Firefox 3 和 4 在页面通过带 hash 的 URL 加载时，不会触发 `onhashchange` 事件
		- 与其他浏览器不同，Safari 5 和 Safari iOS 4 在 hash 发生变化时不会触发 `onpopstate` 事件
		- Safari 5 和 Safari iOS 4 在用 `replaceState` 调用替换 hash 后，无法返回到正确的 state / [bug 报告](https://bugs.webkit.org/show_bug.cgi?id=56249)
		- Safari 5 和 Safari iOS 4 在繁忙条件下有时无法应用 state 更改 / [bug 报告](https://bugs.webkit.org/show_bug.cgi?id=42940)
		- Google Chrome 8、9、10 以及 RC 版本前的 Firefox 4 在页面加载后总是会触发 `onpopstate` / [变更建议](http://hacks.mozilla.org/2011/03/history-api-changes-in-firefox-4/)
		- Safari iOS 4.0、4.1、4.2 拥有可用的 HTML5 History API——尽管浏览器实际的物理后退按钮不起作用，因此我们将它们视为 HTML4 浏览器
		- 所有 HTML5 浏览器实际上都没有使用 `pushState` 和 `replaceState` 调用中的 `title` 参数
	- HTML4 浏览器
		- 旧版浏览器如 MSIE 6、7 和 Firefox 2 没有 `onhashchange` 事件
		- MSIE 6 和 7 有时即使被要求也不会应用 hash（需要第二次调用 apply 函数）
		- 非 Opera 的 HTML4 浏览器在 hash 未进行 urlencoded（URL 编码）时有时不会应用该 hash
	- 所有浏览器
		- 一旦离开站点再返回，state 数据和标题将不再保留（包括页面刷新）
		- state 标题永远不会应用到 `document.title`
- 在 HTML4 浏览器中，ReplaceState 功能通过丢弃被替换的 state 来模拟实现，因此当访问该已丢弃的 state 时，会通过相应的 `History.back()` / `History.forward()` 调用将其跳过
- 数据持久化与同步机制如下：大约每隔一秒，state 的 SUID 和 URL 会在存储区和本地会话之间进行同步。当新会话打开一个熟悉的 state（通过 SUID 或 URL）且在本地未找到时，它将尝试加载具有该信息的最后一个已知已存储 state。
- URL 将被最大程度地进行解码，例如 `?key=a%20b%252c` 将变为 `?key=a b c`。这是为了确保浏览器 URL 编码的一致性。
- 更改页面的 hash 会导致 `onpopstate` 触发（这是预期/标准功能）。为确保 HTML5 和 HTML4 浏览器之间的正确兼容性，创建了以下事件：
	- `window.onstatechange`：与 `onpopstate` 事件相同，但它不会为传统锚点触发
	- `window.onanchorchange`：与 `onhashchange` 事件相同，但它不会为 state 触发



## 许可证

依据 [新 BSD 许可证](http://opensource.org/licenses/BSD-3-Clause) 授权
<br/>Copyright &copy;  2014+ [Bevry Pty Ltd](http://bevry.me) <us@bevry.me>
<br/>Copyright &copy;  2011-2013 [Benjamin Arthur Lupton](http://balupton.com) <b@lupton.cc>

获取支持请参阅 [获取支持](#get-support) 部分。