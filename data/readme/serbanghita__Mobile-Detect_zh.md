![Mobile Detect](http://demo.mobiledetect.net/logo-github.png)

MobileDetect, PHP mobile detection class
========================================

[![Build status](https://img.shields.io/github/actions/workflow/status/serbanghita/Mobile-Detect/4.x-test.yml?branch=4.x&label=build&style=flat-square)](https://github.com/serbanghita/Mobile-Detect/actions/workflows/4.x-test.yml)
[![Latest stable version](https://img.shields.io/packagist/v/mobiledetect/mobiledetectlib?style=flat-square)](https://packagist.org/packages/mobiledetect/mobiledetectlib)
[![Latest tag](https://img.shields.io/github/v/tag/serbanghita/Mobile-Detect?filter=4.*&style=flat-square)](https://github.com/serbanghita/Mobile-Detect/tags)
[![Monthly Downloads](https://img.shields.io/packagist/dm/mobiledetect/mobiledetectlib?style=flat-square&label=installs)](https://packagist.org/packages/mobiledetect/mobiledetectlib/stats)
[![Total Downloads](https://img.shields.io/packagist/dt/mobiledetect/mobiledetectlib?style=flat-square&label=installs)](https://packagist.org/packages/mobiledetect/mobiledetectlib/stats)
[![MIT License](https://img.shields.io/packagist/l/mobiledetect/mobiledetectlib?style=flat-square)](https://github.com/serbanghita/Mobile-Detect/blob/4.x/LICENSE)

Mobile Detect 是一个轻量级的 PHP 类，用于检测移动设备（包括平板电脑）。它结合 User-Agent 字符串与特定的 HTTP 请求头来识别移动端环境。

## 安装前须知

MobileDetect 按主版本线维护独立的滚动更新分支。标签遵循 `<主版本>.<次版本>.<补丁版本>` 格式，且始终位于对应的分支上。

| 版本 | 测试 | 命名空间                | 分支                                                          | PHP 版本  | 说明                  |
|---------|-------|--------------------------|-----------------------------------------------------------------|--------------|--------------------------|
| 2.*     | [![2.x tests](https://img.shields.io/github/actions/workflow/status/serbanghita/Mobile-Detect/2.x-test.yml?branch=2.x&style=flat-square)](https://github.com/serbanghita/Mobile-Detect/actions/workflows/2.x-test.yml) | `\Mobile_Detect`         | [`2.x`](https://github.com/serbanghita/Mobile-Detect/tree/2.x)  | \>=5.6,<7.0  | 已弃用               |
| 3.*     | [![3.x tests](https://img.shields.io/github/actions/workflow/status/serbanghita/Mobile-Detect/3.x-test.yml?branch=3.x&style=flat-square)](https://github.com/serbanghita/Mobile-Detect/actions/workflows/3.x-test.yml) | `Detection\MobileDetect` | [`3.x`](https://github.com/serbanghita/Mobile-Detect/tree/3.x)  | \>=7.4,<8.0  | LTS（长期支持）                      |
| 4.*     | [![4.x tests](https://img.shields.io/github/actions/workflow/status/serbanghita/Mobile-Detect/4.x-test.yml?branch=4.x&style=flat-square)](https://github.com/serbanghita/Mobile-Detect/actions/workflows/4.x-test.yml)       | `Detection\MobileDetect` | [`4.x`](https://github.com/serbanghita/Mobile-Detect/tree/4.x)  | \>=8.2 (since 4.10.0, previously \>=8.0) | 当前版本，**推荐** |

## 🤝 赞助与支持

如果你在商业项目、演示文稿、业余爱好或学校项目中使用了 Mobile Detect 开源包，你可以通过 [捐赠小额金额 :+1:](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=mobiledetectlib%40gmail%2ecom&lc=US&item_name=Mobile%20Detect&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_SM%2egif%3aNonHosted) 来赞助我的工作。  

我目前需要自费支付域名和服务器托管费用，并投入大量家庭时间维护该项目及规划后续版本发布。非常感谢任何形式的资金支持。

特别鸣谢：

* 社区贡献者 :+1:（提供捐赠、提交补丁与反馈问题）
* [Gitbook](https://www.gitbook.com/) 团队，为其技术文档工具提供了开源许可证。


## 📃 文档

完整文档已托管于 Gitbook：[https://docs.mobiledetect.net](https://docs.mobiledetect.net)

## 👾 演示

使用你的设备访问：
[https://demo.mobiledetect.net](https://demo.mobiledetect.net)

## 🐛 测试

``` bash
vendor/bin/phpunit -v -c tests/phpunit.xml --coverage-html .coverage
```

## 🤝 参与贡献

详情请参阅 [贡献指南](https://mobile-detect.gitbook.io/home/contribute)。

## 🔒 安全说明

如果你发现任何安全问题，请直接发送邮件至 serbanghita@gmail.com，请勿使用 Issue 跟踪器。

## 🎉 鸣谢

- [Serban Ghita](https://github.com/serbanghita)
- [All Contributors](https://mobile-detect.gitbook.io/home/credits)