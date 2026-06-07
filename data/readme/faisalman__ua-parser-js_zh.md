[![https://uaparser.dev](https://raw.githubusercontent.com/faisalman/ua-parser-js/gh-pages/images/uap-header.png)](https://uaparser.dev)
[![https://uaparser.dev](https://github.com/user-attachments/assets/a626166b-17cc-45e3-8ff6-d7e948a5ded0)](https://uaparser.dev)
[![https://uaparser.dev](https://github.com/user-attachments/assets/50da50fc-7c8a-46e3-a2bc-6a8249914372)](https://uaparser.dev)
[![https://uaparser.dev](https://github.com/user-attachments/assets/9f2aaff0-a9b4-4ac9-bdf3-eea8081a2582)](https://uaparser.dev)
    
<p align="center">
<a href="https://www.npmjs.com/package/ua-parser-js"><img src="https://img.shields.io/npm/dw/ua-parser-js?color=red&logo=npm&label=NPM%20DOWNLOADS&style=for-the-badge"></a>
<a href="https://www.jsdelivr.com/package/npm/ua-parser-js"><img src="https://img.shields.io/jsdelivr/gh/hw/faisalman/ua-parser-js?logo=jsdelivr&style=for-the-badge"></a>
<a href="https://github.com/faisalman/ua-parser-js"><img src="https://img.shields.io/github/stars/faisalman/ua-parser-js?color=yellow&logo=github&style=for-the-badge"></a>
<a href="https://bundlephobia.com/package/ua-parser-js@1.0.35"><img src="https://img.shields.io/bundlephobia/minzip/ua-parser-js?logo=hackthebox&logoColor=white&style=for-the-badge"/></a>
<a href="https://github.com/faisalman/ua-parser-js/graphs/contributors"><img src="https://img.shields.io/github/contributors/faisalman/ua-parser-js?color=purple&logo=githubsponsors&style=for-the-badge"></a>
<a href="https://www.npmjs.com/package/ua-parser-js"><img src="https://img.shields.io/npm/v/ua-parser-js.svg?logo=npm&color=red&style=for-the-badge"></a>
<a href="https://cdnjs.com/libraries/UAParser.js"><img src="https://img.shields.io/cdnjs/v/UAParser.js.svg?color=orange&style=for-the-badge"></a>
<img src="https://img.shields.io/ossf-scorecard/github.com/faisalman/ua-parser-js?label=openssf%20scorecard&style=for-the-badge">
<a target="_blank" href="https://discord.com/channels/1406959509087453236/1406959509930381375"><img alt="Discord invite" src="https://dcbadge.limes.pink/api/server/https://discord.com/channels/1406959509087453236/1406959509930381375"></a>
</p>

# UAParser.js

目前最全面、紧凑且及时更新的 JavaScript 库，用于检测用户的浏览器、操作系统（OS）、CPU 及设备的类型/型号。同时支持检测机器人（Bot）、应用程序及其他组件。可无缝运行于浏览器端（客户端）或 Node.js 环境（服务端）。

# 演示

  * 在线演示：https://uaparser.dev


# 文档

  * `版本 1.x` : https://docs.uaparser.dev/v1
  * `版本 2.x` : https://docs.uaparser.dev

在从 `v0.7` / `v1.0` 升级之前，请阅读 [CHANGELOG](CHANGELOG.md) 以了解新增功能与破坏性变更。

# 版本与定价

<table>
    <thead>
        <tr>
            <th></th>
            <th colspan="2">开源版</th>
            <th colspan="3">PRO / 商业版</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>许可协议 (License options)</td>
            <td>MIT (v1.x)</td>
            <td>AGPL (v2.x)</td>
            <td>PRO Personal</td>
            <td>PRO Business</td>
            <td>PRO Enterprise</td>
        </tr>
        <tr>
            <td>浏览器检测 (Browser Detection)</td>
            <td><a href="#demo" title="基础检测">⚠️</a></td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>CPU 检测 (CPU Detection)</td>
            <td><a href="#demo" title="基础检测">⚠️</a></td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>设备检测 (Device Detection)</td>
            <td><a href="#demo" title="基础检测">⚠️</a></td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>渲染引擎检测 (Rendering Engine Detection)</td>
            <td><a href="#demo" title="基础检测">⚠️</a></td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>操作系统检测 (OS detection)</td>
            <td><a href="#demo" title="基础检测">⚠️</a></td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>增强型精度 (Enhanced+ Accuracy)</td>
            <td>❌</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>机器人检测 (Bot Detection)</td>
            <td>❌</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>AI 检测 (AI Detection)</td>
            <td>❌</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>扩展检测（应用程序、库、邮箱、媒体播放器、爬虫等） (Extra Detections)</td>
            <td>❌</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>Client Hints 支持 (Client Hints Support)</td>
            <td>❌</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>CommonJS 支持 (CommonJS Support)</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>ESM 支持 (ESM Support)</td>
            <td>❌</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>TypeScript 类型定义 (TypeScript Definitions)</td>
            <td><a href="#demo" title="社区版">✅</a></td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>npm 模块可用 (npm Module Available)</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>提供直接下载链接 (Direct Downloads Available)</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>允许商业用途 (Commercial Use Allowed)</td>
            <td>✅</td>
            <td>✅</td>
            <td>❌</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>宽松许可协议（非 Copyleft） (Permissive License)</td>
            <td>✅</td>
            <td><strong title="Copyleft 许可证">❌</strong></td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>无开源义务 (No Open-Source Obligations)</td>
            <td>✅</td>
            <td><strong title="Copyleft 许可证">❌</strong></td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>不限最终产品数量 (Unlimited End-Products)</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
            <td><strong title="每许可证限 1 个终端产品">❌</strong></td>
            <td>✅</td>
        </tr>
        <tr>
            <td>不限部署数量 (Unlimited Deployments)</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
            <td><strong title="每许可证限 1 个 TLD 或交付物">❌</strong></td>
            <td>✅</td>
        </tr>
        <tr>
            <td>1年产品支持 (1-year Product Support)</td>
            <td>❌</td>
            <td>❌</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>终身更新 (Lifetime Updates)</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>价格 (Price)</td>
            <td><strong title="按需付费">免费<sup>*</sup> (<a target="_blank" href="https://raw.githubusercontent.com/faisalman/ua-parser-js/1.0.x/license.md">协议</a>)</strong></td>
            <td><strong title="按需付费">免费<sup>*</sup> (<a target="_blank" href="https://raw.githubusercontent.com/faisalman/ua-parser-js/master/LICENSE.md">协议</a>)</strong></td>
            <td><strong title="$14（一次性费用）">$14 (<a target="_blank" href="https://raw.githubusercontent.com/faisalman/ua-parser-js/pro-personal/LICENSE.md">协议</a>)</strong></td>
            <td><strong title="$29（一次性费用）">$29 (<a target="_blank" href="https://raw.githubusercontent.com/faisalman/ua-parser-js/pro-business/LICENSE.md">协议</a>)</strong></td>
            <td><strong title="$599（一次性费用）">$599 (<a target="_blank" href="https://raw.githubusercontent.com/faisalman/ua-parser-js/pro-enterprise/LICENSE.md">协议</a>)</strong></td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <th align="right" colspan="6">
                <h3><a target="_blank" href="https://uaparserjs.lemonsqueezy.com/buy/e236ea87-9b2b-400e-9683-24367f731b35">获取 PRO 版本包 📥</a></h3>
            </th>
        </tr>
    </tfoot>
</table>

# 开发指南

## 贡献者

本项目的成功离不开开源社区中所有杰出人士的贡献。感谢每一位提交代码、报告问题并提供反馈的开发者。

<a href="https://github.com/faisalman/ua-parser-js/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=faisalman/ua-parser-js" />
</a>

使用 [contributors-img](https://contrib.rocks) 生成。

欢迎提交贡献！请首先阅读 [CONTRIBUTING GUIDE](CONTRIBUTING.md) 以获取详细的贡献指南。

## 支持者与赞助商

通过以下任一方式支持 **UAParser.js 开源版**的发展：

[![OpenCollective](https://img.shields.io/badge/OpenCollective-dddddd?style=for-the-badge&logo=opencollective&color=dddddd
)](https://opencollective.com/ua-parser-js)
[![GitHub Sponsors](https://img.shields.io/badge/GitHub_Sponsors-333333?style=for-the-badge&logo=githubsponsors&color=333333
)](https://github.com/sponsors/faisalman)
[![PayPal](https://img.shields.io/badge/Paypal-003087?style=for-the-badge&logo=paypal&color=003087
)](https://paypal.me/faisalman)
[![WeChat/Alipay](https://img.shields.io/badge/Other_Payment_Methods-Alipay_/_WeChat_Pay-09b83e?style=for-the-badge&logo=mastercard&color=09b83e
)](https://uaparserjs.lemonsqueezy.com/checkout/buy/3d71f2f3-cf4d-473c-892a-9d4497c890be)

<a href="https://opencollective.com/ua-parser-js"><img src="https://opencollective.com/ua-parser-js/organizations.svg?avatarHeight=64"></a>
<a href="https://opencollective.com/ua-parser-js"><img src="https://opencollective.com/ua-parser-js/individuals.svg?avatarHeight=64"></a>