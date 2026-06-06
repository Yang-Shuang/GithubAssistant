<div align="center">
  <img src="./assets/img/bulb.svg" width="200" alt="light bulb icon">
</div>

# CSS 技巧 [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

一系列助你成为 CSS 高手的实用技巧。

> [!TIP]
> 如需更多优质列表，可查看 [@sindresorhus](https://github.com/sindresorhus/) 精心整理的 [Awesome Lists](https://github.com/sindresorhus/awesome/)。

## 目录

- [技巧](#protips)
- [支持](#support)
- [翻译版本](#translations)
- [贡献指南](CONTRIBUTING.md)

## 技巧

1. [使用 CSS Reset（重置样式）](#use-a-css-reset)
2. [继承 `box-sizing`](#inherit-box-sizing)
3. [使用 `unset` 替代逐个重置属性](#use-unset-instead-of-resetting-all-properties)
4. [在导航栏中使用 `:not()` 添加/移除边框](#use-not-to-applyunapply-borders-on-navigation)
5. [检查字体是否已本地安装](#check-if-font-is-installed-locally)
6. 为 `body` 设置 `line-height`
7. 为表单元素设置 `:focus` 状态
8. 垂直居中任意元素
9. 使用 `aspect-ratio` 替代宽高比计算
10. 逗号分隔的列表样式
11. 使用负数 `nth-child` 选择元素
12. 使用 SVG 图标
13. 使用“脑叶猫头鹰”选择器
14. 使用 `max-height` 实现纯 CSS 滑块
15. 等宽表格单元格
16. 利用 Flexbox 消除 margin hack
17. 使用属性选择器处理空链接
18. 使用 `:is()` 更好地控制优先级（特异性）
19. 设置“默认”链接样式
20. 保持固有比例的元素容器
21. 美化破损图片的显示效果
22. 全局尺寸使用 `rem`，局部尺寸使用 `em`
23. 隐藏未静音的自动播放视频
24. 使用 `:root` 实现响应式字体大小
25. 为表单元素设置 `font-size` 以优化移动端体验
26. 使用 pointer events（指针事件）控制鼠标交互
27. 将用作间距的换行符设置为 `display: none`
28. 使用 `:empty` 隐藏空元素
29. [使用 `margin-inline` 替代传统 margin](#use-margin-inline-instead-of-margin)

### Use a CSS Reset

CSS Reset（重置样式）有助于在不同浏览器间保持样式一致性，为元素提供干净的初始状态。你可以找到许多重置模式，或者采用更简化的写法：

```css
*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
```

这样元素将移除默认的 `margin` 和 `padding`，而 `box-sizing` 能让你通过 CSS 盒模型更好地管理布局。

#### [Demo](https://codepen.io/AllThingsSmitty/pen/kkrkLL)

> [!TIP]
> 如果你采纳了下方关于[继承 `box-sizing`](#inherit-box-sizing)的建议，可能就不需要在 CSS Reset 中包含 `box-sizing` 属性。

<sup>[Back to top](#contents)</sup>

### Inherit `box-sizing`

让 `box-sizing` 从 `html` 继承：

```css
html {
  box-sizing: border-box;
}

*,
*::before,
*::after {
  box-sizing: inherit;
}
```

这使得在插件或其他依赖特定行为的组件中修改 `box-sizing` 变得更加容易。

#### [Demo](https://css-tricks.com/inheriting-box-sizing-probably-slightly-better-best-practice/)

<sup>[Back to top](#contents)</sup>

### Use `unset` Instead of Resetting All Properties

在重置元素属性时，无需逐个重置每个属性：

```css
button {
  background: none;
  border: none;
  color: inherit;
  font: inherit;
  outline: none;
  padding: 0;
}
```

你可以使用 `all` 简写来指定元素的所有属性。将其值设为 `unset` 即可将元素的属性恢复为初始状态：

```css
button {
  all: unset;
}
```

<sup>[Back to top](#contents)</sup>

### Use `:not()` to Apply/Unapply Borders on Navigation

与其先给所有元素添加边框，再移除最后一个元素的边框……不如直接使用 `:not()` 伪类来精准控制目标元素：

```css
/* add border */
.nav li {
  border-right: 1px solid #666;
}
```

...and then taking it off the last element...

```css
/* remove border */
.nav li:last-child {
  border-right: none;
}
```

...use the `:not()` pseudo-class to only apply to the elements you want:

```css
.nav li:not(:last-child) {
  border-right: 1px solid #666;
}
```

Here, the CSS selector is read as a human would describe it.

#### [Demo](https://codepen.io/AllThingsSmitty/pen/LkymvO)

<sup>[Back to top](#contents)</sup>

### Check if Font Is Installed Locally

在远程加载字体前，你可以先检查本地是否已安装该字体，这也是一条提升性能的好建议。感谢 Adam Argyle 分享此技巧及[演示链接](https://codepen.io/argyleink/pen/VwYJpgR)。

```css
@font-face {
  font-family: "Dank Mono";
  src:
    /* Full name */ local("Dank Mono"), /* Postscript name */ local("Dank Mono"),
    /* Otherwise, download it! */ url("//...a.server/fonts/DankMono.woff");
}

code {
  font-family: "Dank Mono", system-ui-monospace;
}
```

<sup>[Back to top](#contents)</sup>

### Add `line-height` to `body`

你无需为每个 `<p>`、`<h*>` 等元素单独设置 `line-height`。只需将其添加到 `body`：

```css
body {
  line-height: 1.5;
}
```

这样文本元素就能轻松继承该属性。

#### [Demo](https://codepen.io/AllThingsSmitty/pen/VjbdYd)

<sup>[Back to top](#contents)</sup>

### Set `:focus` for Form Elements

视力正常的键盘用户依赖焦点状态来确定光标位置。让表单元素的焦点样式比浏览器默认实现更醒目、更统一：

```css
a:focus,
button:focus,
input:focus,
select:focus,
textarea:focus {
  box-shadow: none;
  outline: #000 dotted 2px;
  outline-offset: 0.05em;
}
```

#### [Demo](https://codepen.io/AllThingsSmitty/pen/ePzoOP/)

<sup>[Back to top](#contents)</sup>

### Vertically-Center Anything

这不是魔法，你确实可以垂直居中元素。你可以使用 Flexbox……

```css
html,
body {
  height: 100%;
}

body {
  align-items: center;
  display: flex;
  justify-content: center;
}
```

...and also with CSS Grid:

```css
body {
  display: grid;
  height: 100vh;
  place-items: center;
}
```

> [!TIP]
> 需要居中其他内容吗？无论是水平还是垂直……随时随地都能搞定？CSS-Tricks 上有一篇[非常详细的指南](https://css-tricks.com/centering-css-complete-guide/)涵盖了所有这些方法。

#### [Demo](https://codepen.io/AllThingsSmitty/pen/GqmGqZ)

<sup>[Back to top](#contents)</sup>

### Use `aspect-ratio` Instead of Height/Width

`aspect-ratio` 属性让你能轻松设置元素尺寸并保持宽高比一致。这在响应式网页设计中非常有用，可防止布局偏移（Layout Shift）。配合 `object-fit` 使用，即使图片的宽高值发生变化也不会破坏整体布局。

```css
img {
  aspect-ratio: 16 / 9; /* width / height */
  object-fit: cover;
}
```

你可以在这篇 [web.dev 文章](https://web.dev/articles/aspect-ratio)中了解更多关于 `aspect-ratio` 的信息。

#### [Demo](https://codepen.io/AllThingsSmitty/pen/MWxwoNx/)

<sup>[Back to top](#contents)</sup>

### Comma-Separated Lists

让列表项看起来像真实的逗号分隔文本：

```css
ul > li:not(:last-child)::after {
  content: ",";
}
```

使用 `:not()` 伪类，最后一个元素就不会添加逗号。

> [!NOTE]
> 此技巧对无障碍访问（尤其是屏幕阅读器）可能不够理想。此外，浏览器中无法复制 CSS 生成的内容。请谨慎使用。

<sup>[Back to top](#contents)</sup>

### Select Items Using Negative `nth-child`

在 CSS 中使用负数 `nth-child` 来选择第 1 到第 n 个元素。

```css
li {
  display: none;
}

/* select items 1 through 3 and display them */
li:nth-child(-n + 3) {
  display: block;
}
```

Or, since you've already learned a little about [using `:not()`](#use-not-to-applyunapply-borders-on-navigation), try:

```css
/* select all items except the first 3 and display them */
li:not(:nth-child(-n + 3)) {
  display: block;
}
```

#### [Demo](https://codepen.io/AllThingsSmitty/pen/WxjKZp)

<sup>[Back to top](#contents)</sup>

### Use SVG for Icons

完全没有理由不使用 SVG 图标：

```css
.logo {
  background: url("logo.svg");
}
```

SVG 在所有分辨率下缩放效果极佳，且所有浏览器（包括 IE9）均支持 [back to IE9](http://caniuse.com/#search=svg)。扔掉你的 .png、.jpg 或 .gif 文件吧。

> [!NOTE]
> 如果你的按钮仅依赖 SVG 图标供视力正常用户使用，且 SVG 加载失败时，以下写法有助于维持无障碍访问体验：

```css
.no-svg .icon-only::after {
  content: attr(aria-label);
}
```

<sup>[Back to top](#contents)</sup>

### Use the "Lobotomized Owl" Selector

虽然名字听起来很奇怪，但将通用选择器（`*`）与相邻兄弟选择器（`+`）结合使用，能实现强大的 CSS 效果：

```css
* + * {
  margin-top: 1.5em;
}
```

在此示例中，文档流中紧跟在其他元素之后的所有元素都会获得 `margin-top: 1.5em`。

> [!TIP]
> 想了解“脑叶猫头鹰”选择器的更多信息，推荐阅读 Heydon Pickering 在 _A List Apart_ 上发表的[文章](http://alistapart.com/article/axiomatic-css-and-lobotomized-owls)。

#### [Demo](https://codepen.io/AllThingsSmitty/pen/grRvWq)

<sup>[Back to top](#contents)</sup>

### Use `max-height` for Pure CSS Sliders

结合使用 `max-height` 和溢出隐藏来实现纯 CSS 滑块：

```css
.slider {
  max-height: 200px;
  overflow-y: hidden;
  width: 300px;
}

.slider:hover {
  max-height: 600px;
  overflow-y: scroll;
}
```

鼠标悬停时元素会展开至 `max-height` 设定的值，并通过溢出区域显示滑动条。

<sup>[Back to top](#contents)</sup>

### Equal-Width Table Cells

处理表格有时很头疼。尝试使用 `table-layout: fixed` 来保持单元格等宽：

```css
.calendar {
  table-layout: fixed;
}
```

告别表格布局的烦恼。

#### [Demo](https://codepen.io/AllThingsSmitty/pen/jALALm)

<sup>[Back to top](#contents)</sup>

### Get Rid of Margin Hacks With Flexbox

在处理列间距时，你可以利用 Flexbox 的 `space-between` 属性来摆脱对 `nth-`、`first-child` 和 `last-child` hack 的依赖：

```css
.list {
  display: flex;
  justify-content: space-between;
}

.list .person {
  flex-basis: 23%;
}
```

这样列间距将始终保持均匀分布。

<sup>[Back to top](#contents)</sup>

### Use Attribute Selectors with Empty Links

当 `<a>` 元素没有文本内容但包含 `href` 属性时，显示链接：

```css
a[href^="http"]:empty::before {
  content: attr(href);
}
```

这非常实用。

#### [Demo](https://codepen.io/AllThingsSmitty/pen/zBzXRx)

> [!NOTE]
> 此技巧对无障碍访问（尤其是屏幕阅读器）可能不够理想。此外，浏览器中无法复制 CSS 生成的内容。请谨慎使用。

<sup>[Back to top](#contents)</sup>

### Control Specificity Better With `:is()`

`:is()` 伪类允许一次性匹配多个选择器，从而减少冗余并提升代码可读性。这对于将庞大的选择器规则以更紧凑的形式编写非常有用。

```css
:is(section, article, aside, nav) :is(h1, h2, h3, h4, h5, h6) {
  color: green;
}
```

上述规则集等价于以下冗长的选择器组合……

```css
section h1,
section h2,
section h3,
section h4,
section h5,
section h6,
article h1,
article h2,
article h3,
article h4,
article h5,
article h6,
aside h1,
aside h2,
aside h3,
aside h4,
aside h5,
aside h6,
nav h1,
nav h2,
nav h3,
nav h4,
nav h5,
nav h6 {
  color: green;
}
```

#### [Demo](https://codepen.io/AllThingsSmitty/pen/rNRVxdx)

<sup>[Back to top](#contents)</sup>

### Style "Default" Links

为“默认”链接添加样式：

```css
a[href]:not([class]) {
  color: #008000;
  text-decoration: underline;
}
```

这样通过 CMS 插入的、通常不带 `class` 属性的链接，就能拥有独立的样式，而不会干扰全局级联规则。

<sup>[Back to top](#contents)</sup>

### Intrinsic Ratio Boxes

要创建一个保持固有比例的容器，只需在 div 上设置上下 padding：

```css
.container {
  height: 0;
  padding-bottom: 20%;
  position: relative;
}

.container div {
  border: 2px dashed #ddd;
  height: 100%;
  left: 0;
  position: absolute;
  top: 0;
  width: 100%;
}
```

使用 20% 的 padding 会使元素高度等于其宽度的 20%。无论视口宽度如何变化，子 div 都会保持其宽高比（100% / 20% = 5:1）。

#### [Demo](https://codepen.io/AllThingsSmitty/pen/jALZvE)

<sup>[Back to top](#contents)</sup>

### Style Broken Images

用少量 CSS 让破损图片的显示效果更美观：

```css
img {
  display: block;
  font-family: sans-serif;
  font-weight: 300;
  height: auto;
  line-height: 2;
  position: relative;
  text-align: center;
  width: 100%;
}
```

接着添加伪元素规则，用于显示提示信息及破损图片的 URL 引用：

```css
img::before {
  content: "We're sorry, the image below is broken :(";
  display: block;
  margin-bottom: 10px;
}

img::after {
  content: "(url: " attr(src) ")";
  display: block;
  font-size: 12px;
}
```

> [!TIP]
> 想了解该模式的更多样式细节，可阅读 Ire Aderinokun 的[文章](http://bitsofco.de/styling-broken-images/)。

<sup>[Back to top](#contents)</sup>

### Use `rem` for Global Sizing; Use `em` for Local Sizing

在根元素设置基础字体大小（`html { font-size: 100%; }`）后，将文本元素的字号设为 `em`：

```css
h2 {
  font-size: 2em;
}

p {
  font-size: 1em;
}
```

接着为模块的字号设置为 `rem`：

```css
article {
  font-size: 1.25rem;
}

aside .module {
  font-size: 0.9rem;
}
```

这样每个模块都实现了隔离，更易于样式调整、维护和扩展。

<sup>[Back to top](#contents)</sup>

### Hide Autoplay Videos That Aren't Muted

这是自定义用户样式表的一个绝佳技巧。避免页面加载时自动播放的视频给用户带来声音干扰。如果视频未静音，则不显示：

```css
video[autoplay]:not([muted]) {
  display: none;
}
```

再次利用[` :not()`](#use-not-to-applyunapply-borders-on-navigation)伪类实现这一效果。

<sup>[Back to top](#contents)</sup>

### Use `:root` for Flexible Type

响应式布局中的字体大小应能随视口变化而调整。你可以使用 `:root` 根据视口宽高计算字号：

```css
:root {
  font-size: calc(1vw + 1vh + 0.5vmin);
}
```

现在你就可以基于 `:root` 的计算值来使用 `rem`（根单位）了：

```css
body {
  font: 1rem/1.6 sans-serif;
}
```

#### [Demo](https://codepen.io/AllThingsSmitty/pen/XKgOkR)

<sup>[Back to top](#contents)</sup>

### Set `font-size` on Form Elements for a Better Mobile Experience

为避免移动端浏览器（如 iOS Safari）在点击 `<select>` 下拉菜单时放大表单元素，请在选择器规则中添加 `font-size`：

```css
input[type="text"],
input[type="number"],
select,
textarea {
  font-size: 16px;
}
```

<sup>[Back to top](#contents)</sup>

### Use Pointer Events to Control Mouse Events

[Pointer events（指针事件）](https://developer.mozilla.org/en-US/docs/Web/CSS/pointer-events) 允许你指定鼠标与元素的交互方式。例如，要禁用按钮的默认指针事件：

```css
button:disabled {
  opacity: 0.5;
  pointer-events: none;
}
```

就是这么简单。

<sup>[Back to top](#contents)</sup>

### Set `display: none` on Line Breaks Used as Spacing

正如 [Harry Roberts 指出的那样](https://twitter.com/csswizardry/status/1170835532584235008)，这有助于防止 CMS 用户滥用换行符来制造间距：

```css
br + br {
  display: none;
}
```

<sup>[Back to top](#contents)</sup>

### Use `:empty` to Hide Empty HTML Elements

如果你的 HTML 元素内容为空（例如尚未由 CMS 设置内容或动态注入，如 `<p class="error-message"></p>`），且它在布局中产生了不必要的空白，可使用 `:empty` 伪类将其隐藏。

```css
:empty {
  display: none;
}
```

> [!NOTE]
> 请注意，包含空白字符的元素不被视为空元素，例如 `<p class="error-message"> </p>`。

<sup>[Back to top](#contents)</sup>

## Support

当前版本的 Chrome、Firefox、Safari 和 Edge 浏览器均支持。

<sup>[Back to top](#contents)</sup>

### Use `margin-inline` instead of `margin`

`margin-inline` 定义了元素的行内方向起始和结束外边距。因此，我们可以直接用该属性替代分别设置 `margin-left` 和 `margin-right`。

```css
.div {
  margin-inline: auto;
}
```

对 `margin-block`（定义块级方向的上下外边距）同样适用：

```css
.div {
  margin-block: auto;
}
```

#### [Demo](https://codepen.io/AllThingsSmitty/pen/PwoOQGB)

<sup>[Back to top](#contents)</sup>

## Translations

> [!NOTE]
> 维护不断增长的翻译列表耗费了我大量时间；每新增一条技巧，都需要同步更新十余个翻译版本。因此，各语言的 README 文件可能无法涵盖主文件中列出的全部技巧。

- [简体中文](https://github.com/AllThingsSmitty/css-protips/tree/master/translations/zh-CN)
- [繁体中文](https://github.com/AllThingsSmitty/css-protips/tree/master/translations/zh-TW)
- [德语](https://github.com/AllThingsSmitty/css-protips/tree/master/translations/de-DE)
- [西班牙语](https://github.com/AllThingsSmitty/css-protips/tree/master/translations/es-ES)
- [法语](https://github.com/AllThingsSmitty/css-protips/tree/master/translations/fr-FR)
- [希腊语](https://github.com/AllThingsSmitty/css-protips/tree/master/translations/gr-GR)
- [古吉拉特语](https://github.com/AllThingsSmitty/css-protips/tree/master/translations/gu-IND)
- [意大利语](https://github.com/AllThingsSmitty/css-protips/tree/master/translations/it-IT)
- [日语](https://github.com/AllThingsSmitty/css-protips/tree/master/translations/ja-JP)
- [韩语](https://github.com/AllThingsSmitty/css-protips/tree/master/translations/ko-KR)
- [波兰语](https://github.com/AllThingsSmitty/css-protips/tree/master/translations/pl-PL)
- [巴西葡萄牙语](https://github.com/AllThingsSmitty/css-protips/tree/master/translations/pt-BR)
- [欧洲葡萄牙语](https://github.com/AllThingsSmitty/css-protips/tree/master/translations/pt-PT)
- [俄语](https://github.com/AllThingsSmitty/css-protips/tree/master/translations/ru-RU)
- [越南语](https://github.com/AllThingsSmitty/css-protips/tree/master/translations/vn-VN)

<sup>[Back to top](#contents)</sup>