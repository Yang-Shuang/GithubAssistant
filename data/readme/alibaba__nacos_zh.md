<img src="doc/Nacos_Logo.png" width="50%" syt height="50%" />

# Nacos：动态命名与配置服务

[![Gitter](https://badges.gitter.im/alibaba/nacos.svg)](https://gitter.im/alibaba/nacos?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)   [![License](https://img.shields.io/badge/license-Apache%202-4EB1BA.svg)](https://www.apache.org/licenses/LICENSE-2.0.html)
[![CI](https://github.com/alibaba/nacos/actions/workflows/ci.yml/badge.svg?branch=develop)](https://github.com/alibaba/nacos/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/alibaba/nacos/branch/develop/graph/badge.svg)](https://app.Codecov.io/gh/alibaba/nacos/tree/develop)
[![](https://img.shields.io/badge/Nacos-Check%20Your%20Contribution-orange)](https://opensource.alibaba.com/contribution_leaderboard/details?projectValue=nacos)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/alibaba/nacos)

-------

## 核心功能

Nacos（官网：[nacos.io](https://nacos.io)）是一个易于使用的平台，专为动态服务发现、配置和服务管理而设计。它帮助你轻松构建云原生应用和微服务平台。

在 Nacos 中，服务（Service）是一等公民。Nacos 支持几乎所有类型的服务，例如 [Dubbo/gRPC 服务](https://nacos.io/docs/latest/ecology/use-nacos-with-dubbo/)、[Spring Cloud RESTful 服务](https://nacos.io/docs/latest/ecology/use-nacos-with-spring-cloud/) 或 [Kubernetes 服务](https://nacos.io/docs/latest/quickstart/quick-start-kubernetes/)。

Nacos 主要提供以下四大功能：

* **服务发现与服务健康检查** 
    
    Nacos 使服务能够通过 DNS 或 HTTP 接口轻松注册自身并发现其他服务。Nacos 还提供服务的实时健康检查，防止将请求发送到不健康的节点或服务实例。

* **动态配置管理**
  
    动态配置服务允许你跨所有环境集中且动态地管理所有服务的配置。当配置更新时，无需重新部署应用和服务，从而使配置变更更加高效和敏捷。

* **动态 DNS 服务**
    
    Nacos 支持加权路由，使你在数据中心生产环境中更容易实现中间层负载均衡、灵活的策略路由、流量控制以及简单的 DNS 解析服务。它帮助你轻松实现基于 DNS 的服务发现，并防止应用程序与特定厂商的服务发现 API 耦合。

* **服务与元数据管理**
	
    Nacos 提供易于使用的服务仪表板，帮助你管理服务元数据、配置、Kubernetes DNS、服务健康状态和指标统计。
 

## 快速入门
开始使用你的第一个项目非常简单。

### 在云端部署

你可以在云端部署 Nacos，这是启动 Nacos 最简单、最便捷的方式。 

使用以下 [Nacos 部署指南](https://cn.aliyun.com/product/aliware/mse?spm=nacos-website.topbar.0.0.0) 了解更多信息并部署一个稳定且开箱即用的 Nacos 服务器。


### 使用官方启动包快速开始

#### 步骤 1：下载二进制安装包 

你可以从[最新稳定版本](https://github.com/alibaba/nacos/releases)下载该包。  

以 `nacos-server-1.0.0.zip` 为例：
```sh
unzip nacos-server-1.0.0.zip
cd nacos/bin 
``` 

#### 步骤 2：启动服务

在 **Linux/Unix/Mac** 平台上，运行以下命令以独立模式（standalone）启动服务： 
```sh
sh startup.sh -m standalone
```

在 **Windows** 平台上，运行以下命令以独立模式启动服务。或者，你也可以双击 `startup.cmd` 来运行 NacosServer。
```
startup.cmd -m standalone
```

更多详情请参见[快速入门](https://nacos.io/docs/latest/quickstart/quick-start/)。

## 其他开源项目的快速入门：
* [使用命令和控制台快速开始](https://nacos.io/docs/latest/quickstart/quick-start/)

* [与 Dubbo 集成快速开始](https://nacos.io/docs/latest/ecology/use-nacos-with-dubbo/)

* [与 Spring Cloud 集成快速开始](https://nacos.io/docs/latest/ecology/use-nacos-with-spring-cloud/)

* [与 Kubernetes 集成快速开始](https://nacos.io/docs/latest/quickstart/quick-start-kubernetes/)


## 文档

你可以在[Nacos 官网](https://nacos.io/docs/latest/overview/)查看完整文档。

你也可以在线阅读这本电子书：[《NACOS 架构与原理》](https://nacos.io/docs/ebook/kbyo6n/)。

所有最新及长期通知也可在[GitHub Notice Issue](https://github.com/alibaba/nacos/labels/notice)中查阅。

## 贡献代码

欢迎贡献者加入 Nacos 项目。请查看[《CONTRIBUTING》](./CONTRIBUTING.md)了解如何为本项目做出贡献。

### 我该如何贡献？

* 浏览标记为[`good first issue`](https://github.com/alibaba/nacos/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22)或[`contribution welcome`](https://github.com/alibaba/nacos/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22)的 Issue。
* 在[Issue](https://github.com/alibaba/nacos/issues)中回答提问。
* 修复[Issue](https://github.com/alibaba/nacos/issues)中报告的 Bug，并提交 Pull Request。
* 审查现有的[Pull Request](https://github.com/alibaba/nacos/pulls)。
* 改进[官网](https://github.com/nacos-group/nacos-group.github.io)，我们通常需要：
  * 博客文章
  * 文档翻译
  * 关于在企业系统中集成 Nacos 的用例介绍

## 其他相关项目仓库

* [nacos-spring-project](https://github.com/nacos-group/nacos-spring-project) 提供与 Spring 的集成功能。
* [nacos-group](https://github.com/nacos-group) 是托管了 Nacos 生态工具（如 SDK、同步工具等）的仓库。
* [spring-cloud-alibaba](https://github.com/spring-cloud-incubator/spring-cloud-alibaba) 提供基于阿里云中间件（包含 Nacos）的应用开发一站式解决方案。

## 联系方式

* [Gitter](https://gitter.im/alibaba/nacos)：Nacos 社区即时通讯工具，用于消息交流、协作与发现。
* [Twitter](https://twitter.com/nacos2)：在 Twitter 上关注以获取最新 Nacos 动态。
* [Weibo](https://weibo.com/u/6574374908)：在微博（中国版 Twitter）上关注以获取最新 Nacos 动态。
* [Nacos Segmentfault](https://segmentfault.com/t/nacos)：在 Segmentfault 获取最新通知与即时帮助。
* 邮件组：
     * users-nacos@googlegroups.com：Nacos 使用交流讨论。
     * dev-nacos@googlegroups.com：Nacos 开发者讨论（API、功能设计等）。
     * commits-nacos@googlegroups.com：Commit 通知，更新频率极高。
* 加入钉钉群（群 1：21708933(已满)，群 2：30438813(已满)，群 3：31222241(已满)，群 4：12810027056）。 

### 钉钉群二维码

![](https://cdn.nlark.com/yuque/0/2025/png/1577777/1750054497446-f834cba6-fa83-4421-b202-a0dc1d5cc28b.png)

### 钉钉 MCP 群二维码

![](https://cdn.nlark.com/yuque/0/2025/png/1577777/1750054500395-e271cbe4-2dd8-4723-8cd0-bd8a731b812a.png)

### 微信群二维码

![](https://cdn.nlark.com/yuque/0/2025/png/1577777/1750054421702-a7d1421a-ab8e-42da-bc59-01b5d287b290.png)

## 企业服务
如果你需要 Nacos 企业服务支持，或购买云产品服务，可以扫描以下钉钉群加入讨论。你也可以通过阿里云提供的微服务引擎（MSE）直接激活并使用。
https://cn.aliyun.com/product/aliware/mse?spm=nacos-website.topbar.0.0.0

<img src="https://img.alicdn.com/imgextra/i3/O1CN01RTfN7q1KUzX4TcH08_!!6000000001168-2-tps-864-814.png" width="500">


## 下载

- [Nacos 官网下载地址](https://nacos.io/download/nacos-server)
- [GitHub Release](https://github.com/alibaba/nacos/releases)
  
## 用户列表

以下仅为部分使用 Nacos 的企业，仅供参考。如果你正在使用 Nacos，请[在此添加你的公司](https://github.com/alibaba/nacos/issues/273)并分享你的使用场景，帮助我们做得更好。

<table>
  <tr>
    <td><img src="https://data.alibabagroup.com/ecms-files/886024452/296d05a1-c52a-4f5e-abf2-0d49d4c0d6b3.png"  alt="Alibaba Group" width="180" height="120"></td>
    <td><img src="https://a.msstatic.com/huya/main/img/logo.png"  alt="虎牙直播" width="180" height="120"></td>
    <td><img src="https://v.icbc.com.cn/userfiles/Resources/ICBC/shouye/images/2017/logo.png"  alt="ICBC" width="180" height="120"></td>
    <td><img src="https://pic2.iqiyipic.com/lequ/20220422/e7fe69c75e2541f2a931c9e538e2ab9d.jpg"  alt="爱奇艺" width="180" height="120"></td>
  </tr>
  <tr>
    <td><img src="https://img.alicdn.com/tfs/TB1pwi9EwHqK1RjSZJnXXbNLpXa-479-59.png"  alt="平安科技" width="180" height="120"></td>
    <td><img src="https://img.alicdn.com/tfs/TB1MZWSEzDpK1RjSZFrXXa78VXa-269-69.png"  alt="华夏信财" width="180" height="120"></td>
    <td><img src="https://www.urwork.cn/public/images/ui/logo.png"  alt="优客工场" width="180" height="120"></td>
    <td><img src="https://img.alicdn.com/tfs/TB1ebu.EAvoK1RjSZFwXXciCFXa-224-80.png"  alt="贝壳找房" width="180" height="120"></td>
  </tr>
  <tr>
    <td><img src="https://img.alicdn.com/tfs/TB1lxu7EBLoK1RjSZFuXXXn0XXa-409-74.png"  alt="瑞安农村商业银行" width="180" height="120"></td>
    <td><img src="https://img.alicdn.com/tfs/TB1L16eEzTpK1RjSZKPXXa3UpXa-302-50.png"  alt="司法大数据" width="180" height="120"></td>
    <td><img src="https://www.souyidai.com/www-style/images/logo.gif"  alt="搜易贷" width="180" height="120"></td>
    <td><img src="https://img.alicdn.com/tfs/TB1OigyDyLaK1RjSZFxXXamPFXa-168-70.png"  alt="平行云" width="180" height="120"></td>
  </tr>
  <tr>
    <td><img src="https://img.alicdn.com/tfs/TB1gJ4vIhTpK1RjSZR0XXbEwXXa-462-60.jpg"  alt="甘肃紫光" width="180" height="120"></td>
    <td><img src="http://www.seaskylight.com/cn/uploadfiles/image/logo.png"  alt="海云天" width="180" height="120"></td>
    <td><img src="https://img.alicdn.com/tfs/TB1DZWSEzDpK1RjSZFrXXa78VXa-240-62.png"  alt="Acmedcare+" width="180" height="120"></td>
    <td><img src="https://14605854.s21i.faiusr.com/4/ABUIABAEGAAg4OvkzwUo8b-qlwUwxQ449gM!300x300.png"  alt="北京天合互联信息有限公司" width="180" height="120"></td>
  </tr>
  <tr>
    <td><img src="http://www.mwclg.com/static-resource/front/images/home/img_logo_nav.png"  alt="上海密尔克卫化工" width="180" height="120"></td>
    <td><img src="https://www.synwe.com/logo-full.png"  alt="大连新唯" width="180" height="120"></td>
    <td><img src="https://user-images.githubusercontent.com/10215557/51593180-7563af00-1f2c-11e9-95b1-ec2c645d6a0b.png"  alt="立思辰" width="180" height="120"></td>
    <td><img src="https://img.alicdn.com/tfs/TB1zWW2EpYqK1RjSZLeXXbXppXa-262-81.png"  alt="东家" width="180" height="120"></td>
  </tr>
  <tr>
    <td><img src="http://www.sh-guiyao.com/images/logo.jpg"  alt="上海克垚" width="180" height="120"></td>
    <td><img src="http://www.lckjep.com:80//theme/img/logoTop.png"  alt="联采科技" width="180" height="120"></td>
    <td><img src="https://img.alicdn.com/tfs/TB1G216EsbpK1RjSZFyXXX_qFXa-325-53.jpg"  alt="南京28研究所" width="180" height="120"></td>
    <td><img src="https://p1.ifengimg.com/auto/image/2017/0922/auto_logo.png"  alt="凤凰网-汽车" width="180" height="120"></td>
  </tr>
  <tr>
    <td><img src="http://www.sinochemitech.com/zhxx/lib/images/-logo.png"  alt="中化信息" width="180" height="120"></td>
    <td><img src="https://img.alicdn.com/tfs/TB1DXerNgDqK1RjSZSyXXaxEVXa-333-103.png"  alt="一点车" width="180" height="120"></td>
    <td><img src="https://img.alicdn.com/tfs/TB1VfOANgHqK1RjSZFPXXcwapXa-313-40.png"  alt="明传无线" width="180" height="120"></td>
    <td><img src="https://img.alicdn.com/tfs/TB1lvCyNhTpK1RjSZFMXXbG_VXa-130-60.png"  alt="妙优车" width="180" height="120"></td>
  </tr>
  <tr>
    <td><img src="https://img.alicdn.com/tfs/TB1kY9qNgTqK1RjSZPhXXXfOFXa-120-50.png"  alt="蜂巢" width="180" height="120"></td>
    <td><img src="https://img.alicdn.com/tfs/TB1G.GBNbrpK1RjSZTEXXcWAVXa-234-65.png"  alt="华存数据" width="180" height="120"></td>
    <td><img src="https://img.alicdn.com/tfs/TB1qsurNgDqK1RjSZSyXXaxEVXa-300-90.png"  alt="数云" width="180" height="120"></td>
    <td><img src="https://img.alicdn.com/tfs/TB13aywNhTpK1RjSZR0XXbEwXXa-98-38.png"  alt="广通软件" width="180" height="120"></td>
  </tr>
  <tr>
    <td><img src="https://img.alicdn.com/tfs/TB1xqmBNjTpK1RjSZKPXXa3UpXa-162-70.png"  alt="菜菜" width="180" height="120"></td>
    <td><img src="https://img.alicdn.com/tfs/TB18DmINcfpK1RjSZFOXXa6nFXa-200-200.png"  alt="科蓝公司" width="180" height="120"></td>
    <td><img src="https://img.alicdn.com/tfs/TB15uqANXzqK1RjSZFoXXbfcXXa-188-86.png"  alt="浩鲸" width="180" height="120"></td>
    <td><img src="https://img.alicdn.com/tfs/TB1mvmyNkvoK1RjSZPfXXXPKFXa-238-46.png"  alt="未名天日语" width="180" height="120"></td>
  </tr>
  <tr>
    <td><img src="https://img.alicdn.com/tfs/TB1PSWsNmrqK1RjSZK9XXXyypXa-195-130.jpg"  alt="金联创" width="180" height="120"></td>
    <td><img src="https://img.alicdn.com/tfs/TB1k1qzNbvpK1RjSZFqXXcXUVXa-160-69.png"  alt="同窗链" width="180" height="120"></td>
    <td><img src="https://img.alicdn.com/tfs/TB1HdyvNmzqK1RjSZFLXXcn2XXa-143-143.jpg"  alt="顺能" width="180" height="120"></td>
    <td><img src="https://img.alicdn.com/tfs/TB1UdaGNgHqK1RjSZJnXXbNLpXa-277-62.png"  alt="百世快递" width="180" height="120"></td>
  </tr>
  <tr>
    <td><img src="https://img.alicdn.com/tfs/TB17OqENbrpK1RjSZTEXXcWAVXa-240-113.jpg"  alt="汽车之家" width="180" height="120"></td>
    <td><img src="https://img.alicdn.com/tfs/TB1q71ANkvoK1RjSZPfXXXPKFXa-257-104.png"  alt="鲸打卡" width="180" height="120"></td>
    <td><img src="https://img.alicdn.com/tfs/TB1UzuyNhTpK1RjSZR0XXbEwXXa-201-86.jpg"  alt="时代光华" width="180" height="120"></td>
    <td><img src="https://img.alicdn.com/tfs/TB19RCANgHqK1RjSZFPXXcwapXa-180-180.jpg"  alt="康美" width="180" height="120"></td>
  </tr>
  <tr>
    <td><img src="https://img.alicdn.com/tfs/TB1iCGyNb2pK1RjSZFsXXaNlXXa-143-143.jpg"  alt="环球易购" width="180" height="120"></td>
    <td><img src="https://avatars0.githubusercontent.com/u/16344119?s=200&v=4"  alt="Nepxion" width="180" height="120"></td>
    <td><img src="https://img.alicdn.com/tfs/TB1aUe5EpzqK1RjSZSgXXcpAVXa-248-124.png"  alt="chigua" width="180" height="120"></td>
    <td><img src="https://img.alicdn.com/tfs/TB1H9O5EAvoK1RjSZFNXXcxMVXa-221-221.jpg"  alt="宅无限" width="180" height="120"></td>
  </tr>
  <tr>
    <td><img src="https://img.alicdn.com/tfs/TB1rNq4EwHqK1RjSZFgXXa7JXXa-200-200.jpg"  alt="天阙" width="180" height="120"></td>
    <td><img src="https://img.alicdn.com/tfs/TB1CRAxDxYaK1RjSZFnXXa80pXa-190-190.jpg"  alt="联合永道" width="180" height="120"></td>
    <td><img src="https://img.alicdn.com/tfs/TB1.q14ErrpK1RjSZTEXXcWAVXa-219-219.jpg"  alt="明源云" width="180" height="120"></td>
    <td><img src="https://www.daocloud.io/static/Logo-Light.png"  alt="DaoCloud" width="180" height="120"></td>
  </tr>
  <tr>
    <td><img src="https://www.meicai.cn/img/logo.9210b6eb.jpg"  alt="美菜" width="180" height="120"></td>
    <td><img src="https://img5.tianyancha.com/logo/lll/3aad34039972b57e70874df8c919ae8b.png@!f_200x200"  alt="松格科技" width="180" height="120"></td>
    <td><img src="https://www.jsic-tech.com/Public/uploads/20191206/5de9b9baac696.jpg"  alt="集萃智能" width="180" height="120"></td>
    <td><img src="https://www.wuuxiang.com/theme/images/common/logo1.png"  alt="吾享" width="180" height="120"></td>
  </tr>
  <tr>
    <td><img src="http://www.tpson.cn/static/upload/image/20230111/1673427385140440.png"  alt="拓深科技" width="180" height="120"></td>
    <td><img src="https://www.sunline.cn/u_file/fileUpload/2021-06/25/2021062586431.png"  alt="长亮科技" width="180" height="120"></td>
    <td><img src="http://pmt2f499f.pic44.websiteonline.cn/upload/wv0c.png"  alt="深圳易停车库" width="180" height="120"></td>
    <td><img src="http://www.dragonwake.cn/static/css/default/img/logo.png"  alt="武汉日创科技" width="180" height="120"></td>
  </tr>
  <tr>
    <td><img src="https://i4im-web.oss-cn-shanghai.aliyuncs.com/images/logo.png"  alt="易管智能" width="180" height="120"></td>
    <td><img src="https://www.yunzhangfang.com/assets/img/logo.4096cf52.png"  alt="云帐房" width="180" height="120"></td>
    <td><img src="https://www.sinocare.com/sannuo/templates/web/img/bocweb-logo.svg"  alt="三诺生物" width="180" height="120"></td>
    <td></td>
  </tr>
  <tr>
    <td>郑州山水</td>
    <td>知氏教育</td>
    <td></td>
    <td></td>
  </tr>
</table>