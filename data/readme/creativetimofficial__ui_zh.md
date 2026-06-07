[![Creative Tim UI](https://raw.githubusercontent.com/creativetimofficial/ui/refs/heads/main/apps/www/public/opengraph-image.png)](https://creative-tim.com/ui)

# Creative Tim UI

[Creative Tim UI](https://creative-tim.com/ui) 是一个基于 [shadcn/ui](https://ui.shadcn.com/) 构建的全面组件库，旨在帮助你更快地开发现代 Web 应用。

## 概述

Creative Tim UI 提供了预构建且可自定义的 React 组件和区块（Blocks），专为打造美观、可直接投入生产环境的 Web 应用而设计。
通过 CLI，你可以轻松将这些组件添加到你的 Next.js 项目中。

## 安装
你可以通过 npx 直接使用 Creative Tim UI CLI：
```bash
# Use directly (recommended)
npx @creative-tim/ui@latest add <component-name>

# Or using shadcn cli
npx shadcn@latest add https://creative-tim.com/ui/r/all.json
```

## 前置要求
在使用 Creative Tim UI 之前，请确保你的 Next.js 项目满足以下要求：
- **Node.js 18** 或更高版本
- 已在项目中初始化 **shadcn/ui**（运行 `npx shadcn@latest init`）
- 已配置 **Tailwind CSS**

## 使用方法

### 安装所有组件
一次性安装所有可用的 Creative Tim UI 组件：
```bash
npx @creative-tim/ui@latest add all
```
该命令将执行以下操作：
- 若未配置，则自动设置 shadcn/ui
- 将所有 Creative Tim UI 组件安装到你配置的组件目录中
- 向你的项目添加必要的依赖项

### 安装特定组件
使用 `add` 命令单独安装组件：
```bash
npx @creative-tim/ui@latest add <component-name>
```
示例：
```bash
# Install the orb component
npx @creative-tim/ui@latest add card
```

### 替代方案：配合 shadcn CLI 使用
你也可以通过标准的 shadcn/ui CLI 安装组件：
```bash
# Install all components
npx shadcn@latest add https://creative-tim.com/ui/r/all.json

# Install a specific component
npx shadcn@latest add https://creative-tim.com/ui/r/button.json
```

所有可用组件均可在[此处](https://creative-tim.com/ui/docs/components)查看，或在此探索示例区块列表[此处](https://creative-tim.com/ui/blocks)。

## 区块（Blocks）

浏览我们按类别整理的即用型区块集合。每个区块均可完全自定义，并通过一条命令添加到你的项目中。

### 应用界面 (Application UI)

<table>
<tr>
<td width="25%">
<a href="https://creative-tim.com/ui/blocks/modals">
<img src="https://raw.githubusercontent.com/creativetimofficial/public-assets/refs/heads/master/david-ui/thumbs/modals-thumbnail.jpg" alt="Modals" />
<br/>
<strong>模态框（Modals）</strong><br/>
<em>5 个区块</em>
</a>
</td>
<td width="25%">
<a href="https://creative-tim.com/ui/blocks/account">
<img src="https://raw.githubusercontent.com/creativetimofficial/public-assets/refs/heads/master/david-ui/thumbs/account-thumbnail.jpg" alt="Account" />
<br/>
<strong>账户（Account）</strong><br/>
<em>7 个区块</em>
</a>
</td>
<td width="25%">
<a href="https://creative-tim.com/ui/blocks/billing">
<img src="https://raw.githubusercontent.com/creativetimofficial/public-assets/refs/heads/master/david-ui/thumbs/billing-thumbnail.jpg" alt="Billing" />
<br/>
<strong>账单（Billing）</strong><br/>
<em>5 个区块</em>
</a>
</td>
</tr>
</table>

### 营销页面 (Marketing)

<table>
<tr>
<td width="25%">
<a href="https://creative-tim.com/ui/blocks/testimonials">
<img src="https://raw.githubusercontent.com/creativetimofficial/public-assets/refs/heads/master/david-ui/thumbs/testimonial-thumbnail.jpg" alt="Testimonial Sections" />
<br/>
<strong>用户评价区块（Testimonial Sections）</strong><br/>
<em>17 个区块</em>
</a>
</td>
<td width="25%">
<a href="https://creative-tim.com/ui/blocks/contact">
<img src="https://raw.githubusercontent.com/creativetimofficial/public-assets/refs/heads/master/david-ui/thumbs/contact-us-thumbnail.jpg" alt="Contact Sections" />
<br/>
<strong>联系我们区块（Contact Sections）</strong><br/>
<em>15 个区块</em>
</a>
</td>
<td width="25%">
<a href="https://creative-tim.com/ui/blocks/footers">
<img src="https://raw.githubusercontent.com/creativetimofficial/public-assets/refs/heads/master/david-ui/thumbs/footer-thumbnail.jpg" alt="Footers" />
<br/>
<strong>页脚（Footers）</strong><br/>
<em>16 个区块</em>
</a>
</td>
</tr>
<tr>
<td width="25%">
<a href="https://creative-tim.com/ui/blocks/faqs">
<img src="https://raw.githubusercontent.com/creativetimofficial/public-assets/refs/heads/master/david-ui/thumbs/faq-thumbnail.jpg" alt="FAQs" />
<br/>
<strong>常见问题（FAQs）</strong><br/>
<em>6 个区块</em>
</a>
</td>
<td width="25%">
<a href="https://creative-tim.com/ui/blocks/blog">
<img src="https://raw.githubusercontent.com/creativetimofficial/public-assets/refs/heads/master/david-ui/thumbs/blog-posts-thumbnail.jpg" alt="Blog" />
<br/>
<strong>博客文章（Blog）</strong><br/>
<em>15 个区块</em>
</a>
</td>
</tr>
</table>

### 电商界面 (Ecommerce UI)
提供用于商品列表、购物车和结账流程的即用型区块。

<table>
<tr>
<td width="25%">
<a href="https://creative-tim.com/ui/blocks/ecommerce">
<img src="https://raw.githubusercontent.com/creativetimofficial/public-assets/refs/heads/master/david-ui/thumbs/ecommerce-thumbnail.jpg" alt="Ecommerce Sections" />
<br/>
<strong>电商页面区块（Ecommerce Sections）</strong><br/>
<em>14 个区块</em>
</a>
</td>
</tr>
</table>

### Web 3.0
专为去中心化应用、区块链项目和加密货币平台打造的创新界面区块。

<table>
<tr>
<td width="25%">
<a href="https://creative-tim.com/ui/blocks/web3">
<img src="https://raw.githubusercontent.com/creativetimofficial/public-assets/refs/heads/master/david-ui/thumbs/collections-thumbnail.jpg" alt="Web 3.0 Cards" />
<br/>
<strong>Web 3.0 卡片（Web 3.0 Cards）</strong><br/>
<em>5 个区块</em>
</a>
</td>
</tr>
</table>

## 贡献指南

如果你希望为 Creative Tim UI 做出贡献，请遵循以下步骤：

1. Fork（复刻）该仓库
2. 创建新分支
3. 对注册表（Registry）中的组件进行修改。
4. 向主分支提交 PR（Pull Request）。

请阅读[贡献指南](/CONTRIBUTING.md)。

## 版权与许可证

Creative Tim UI 建立在开源社区的卓越工作之上：

- **[shadcn/ui](https://ui.shadcn.com/)** - 文档结构、注册表系统及基础（原子）组件均源自 shadcn/ui 的开源工作。[MIT 许可证](https://github.com/shadcn-ui/ui/blob/main/LICENSE.md)
- **[Material Tailwind](https://material-tailwind.com/v3)** by Creative Tim - 区块与组件设计灵感来源于并基于 Material Tailwind 框架。[MIT 许可证](https://github.com/creativetimofficial/material-tailwind/blob/main/LICENSE.md)
- **[Eleven Labs UI](https://github.com/elevenlabs/elevenlabs-ui)** - 为文档结构和区块呈现方式提供了总体灵感。[MIT 许可证](https://github.com/elevenlabs/ui/blob/main/LICENSE.md)
- **[Geist Font](https://vercel.com/font)** by Vercel - 贯穿界面的精美字体。[SIL Open Font License 1.1](https://github.com/vercel/geist-font/blob/main/LICENSE.txt)

感谢这些项目以开源许可证的形式共享其成果。

## 许可证

本项目遵循 [MIT 许可证](https://github.com/creativetimofficial/ui/blob/main/LICENSE.md)。

由 [Creative Tim](https://creative-tim.com) 用心打造。