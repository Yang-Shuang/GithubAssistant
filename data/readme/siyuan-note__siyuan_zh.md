<p align="center">
<img alt="思源" src="https://b3log.org/images/brand/siyuan-128.png">
<br>
<em>重构你的思考</em>
<br><br>
<a title="构建状态" target="_blank" href="https://github.com/siyuan-note/siyuan/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/siyuan-note/siyuan/cd.yml?style=flat-square"></a>
<a title="版本发布" target="_blank" href="https://github.com/siyuan-note/siyuan/releases"><img src="https://img.shields.io/github/release/siyuan-note/siyuan.svg?style=flat-square&color=9CF"></a>
<a title="下载统计" target="_blank" href="https://github.com/siyuan-note/siyuan/releases"><img src="https://img.shields.io/github/downloads/siyuan-note/siyuan/total.svg?style=flat-square&color=blueviolet"></a>
<br>
<a title="Docker 拉取量" target="_blank" href="https://hub.docker.com/r/b3log/siyuan"><img src="https://img.shields.io/docker/pulls/b3log/siyuan.svg?style=flat-square&color=green"></a>
<a title="Docker 镜像大小" target="_blank" href="https://hub.docker.com/r/b3log/siyuan"><img src="https://img.shields.io/docker/image-size/b3log/siyuan.svg?style=flat-square&color=ff96b4"></a>
<a title="访问统计" target="_blank" href="https://github.com/siyuan-note/siyuan"><img src="https://hits.b3log.org/siyuan-note/siyuan.svg"></a>
<br>
<a title="AGPLv3 许可证" target="_blank" href="https://www.gnu.org/licenses/agpl-3.0.txt"><img src="http://img.shields.io/badge/license-AGPLv3-orange.svg?style=flat-square"></a>
<a title="代码体积" target="_blank" href="https://github.com/siyuan-note/siyuan"><img src="https://img.shields.io/github/languages/code-size/siyuan-note/siyuan.svg?style=flat-square&color=yellow"></a>
<a title="GitHub 拉取请求" target="_blank" href="https://github.com/siyuan-note/siyuan/pulls"><img src="https://img.shields.io/github/issues-pr-closed/siyuan-note/siyuan.svg?style=flat-square&color=FF9966"></a>
<br>
<a title="GitHub 提交活跃度" target="_blank" href="https://github.com/siyuan-note/siyuan/commits/master"><img src="https://img.shields.io/github/commit-activity/m/siyuan-note/siyuan.svg?style=flat-square"></a>
<a title="最后提交时间" target="_blank" href="https://github.com/siyuan-note/siyuan/commits/master"><img src="https://img.shields.io/github/last-commit/siyuan-note/siyuan.svg?style=flat-square&color=FF9900"></a>
<br><br>
<a title="Twitter" target="_blank" href="https://twitter.com/b3logos"><img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/b3logos?label=Follow&style=social"></a>
<a title="Discord" target="_blank" href="https://discord.gg/dmMbCqVX7G"><img alt="Chat on Discord" src="https://img.shields.io/discord/808152298789666826?label=Discord&logo=Discord&style=social"></a>
<br><br>
<a href="https://trendshift.io/repositories/3949" target="_blank"><img src="https://trendshift.io/api/badge/repositories/3949" alt="siyuan-note%2Fsiyuan | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

<p align="center">
<b>English</b>
| <a href="README_zh_CN.md">中文</a>
| <a href="README_ja_JP.md">日本語</a>
| <a href="README_tr_TR.md">Türkçe</a>
</p>

---

## 目录

* [💡 简介](#-简介)
* [🔮 功能特性](#-功能特性)
* [🏗️ 架构与生态](#️架构与生态)
* [🌟 Star 历史](#-star-历史)
* [🗺️ 开发路线](#️开发路线)
* [🚀 下载与安装](#-下载与安装)
  * [应用商店](#应用商店)
  * [安装包](#安装包)
  * [包管理器](#包管理器)
  * [Docker 部署](#docker-部署)
  * [Unraid 部署](#unraid-部署)
  * [TrueNAS 部署](#truenas-部署)
  * [内测预览版](#内测预览版)
* [🏘️ 社区交流](#️社区交流)
* [🛠️ 开发指南](#️开发指南)
* [❓ 常见问题](#-常见问题)
  * [思源如何存储数据？](#思源如何存储数据)
  * [是否支持通过第三方同步盘进行数据同步？](#是否支持通过第三方同步盘进行数据同步)
  * [思源是开源的吗？](#思源是开源的吗)
  * [如何升级到新版本？](#如何升级到新版本)
  * [某些区块（如列表项中的段落区块）找不到区块图标怎么办？](#某些区块如列表项中的段落区块找不到区块图标怎么办)
  * [数据仓库密钥丢失了该怎么办？](#数据仓库密钥丢失了该怎么办)
  * [需要付费吗？](#需要付费吗)
* [🙏 致谢](#-致谢)
  * [贡献者](#贡献者)

---

## 💡 简介

思源（SiYuan）是一款隐私优先的个人知识管理系统，支持细粒度的区块级引用与 Markdown 所见即所得（WYSIWYG）。

欢迎前往 [思源英文讨论区](https://liuyun.io) 了解更多。

![feature0.png](https://b3logfile.com/file/2025/11/feature0-GfbhEqf.png)

![feature51.png](https://b3logfile.com/file/2025/11/feature5-1-7DJSfEP.png)

## 🔮 功能特性

大部分功能免费开放，即使用于商业用途也无需付费。

* **内容区块**
  * 区块级引用与双向链接
  * 自定义属性（Custom Attributes）
  * SQL 查询嵌入
  * `siyuan://` 协议支持
* **编辑器**
  * 区块式排版
  * Markdown 所见即所得（WYSIWYG）
  * 列表大纲视图
  * 区块放大查看
  * 百万字级长文档编辑
  * 数学公式、图表、流程图、甘特图、时序图、五线谱等
  * 网页剪藏（Web Clipping）
  * PDF 批注链接
* **导出**
  * 块引用与嵌入导出
  * 带资源的标准 Markdown
  * PDF、Word 和 HTML
  * 一键复制到微信公众号、知乎和语雀
* **数据库**
  * 表格视图（Table View）
* 间隔重复复习卡片（Flashcard Spaced Repetition）
* 通过 OpenAI API 实现 AI 写作与问答聊天
* Tesseract OCR 识别
* 多标签页支持，拖拽分屏
* 模板片段（Template Snippet）
* JavaScript/CSS 代码片段注入
* Android / iOS / HarmonyOS 移动端应用
* Docker 部署
* [API](https://github.com/siyuan-note/siyuan/blob/master/API.md)
* 社区插件市场

部分高级功能仅限付费会员使用，详情请参阅 [定价页面](https://b3log.org/siyuan/en/pricing.html)。

## 🏗️ 架构与生态

![SiYuan Arch](https://b3logfile.com/file/2023/05/SiYuan_Arch-Sgu8vXT.png "SiYuan Arch")

| 项目 | 描述 | Forks | Stars | 
|----------------------------------------------------------|-----------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [lute](https://github.com/88250/lute)                    | 编辑器引擎         | ![GitHub forks](https://img.shields.io/github/forks/88250/lute)                 | ![GitHub Repo stars](https://img.shields.io/github/stars/88250/lute)                 |
| [chrome](https://github.com/siyuan-note/siyuan-chrome)   | Chrome/Edge 扩展插件 | ![GitHub forks](https://img.shields.io/github/forks/siyuan-note/siyuan-chrome)  | ![GitHub Repo stars](https://img.shields.io/github/stars/siyuan-note/siyuan-chrome)  |
| [bazaar](https://github.com/siyuan-note/bazaar)          | 社区插件市场         | ![GitHub forks](https://img.shields.io/github/forks/siyuan-note/bazaar)         | ![GitHub Repo stars](https://img.shields.io/github/stars/siyuan-note/bazaar)         |
| [dejavu](https://github.com/siyuan-note/dejavu)          | 数据仓库             | ![GitHub forks](https://img.shields.io/github/forks/siyuan-note/dejavu)         | ![GitHub Repo stars](https://img.shields.io/github/stars/siyuan-note/dejavu)         |
| [petal](https://github.com/siyuan-note/petal)            | 插件 API             | ![GitHub forks](https://img.shields.io/github/forks/siyuan-note/petal)          | ![GitHub Repo stars](https://img.shields.io/github/stars/siyuan-note/petal)          |
| [android](https://github.com/siyuan-note/siyuan-android) | Android 应用         | ![GitHub forks](https://img.shields.io/github/forks/siyuan-note/siyuan-android) | ![GitHub Repo stars](https://img.shields.io/github/stars/siyuan-note/siyuan-android) |
| [ios](https://github.com/siyuan-note/siyuan-ios)         | iOS 应用             | ![GitHub forks](https://img.shields.io/github/forks/siyuan-note/siyuan-ios)     | ![GitHub Repo stars](https://img.shields.io/github/stars/siyuan-note/siyuan-ios)     |
| [harmony](https://github.com/siyuan-note/siyuan-harmony) | HarmonyOS 应用       | ![GitHub forks](https://img.shields.io/github/forks/siyuan-note/siyuan-harmony) | ![GitHub Repo stars](https://img.shields.io/github/stars/siyuan-note/siyuan-harmony) |
| [riff](https://github.com/siyuan-note/riff)              | 间隔重复复习         | ![GitHub forks](https://img.shields.io/github/forks/siyuan-note/riff)           | ![GitHub Repo stars](https://img.shields.io/github/stars/siyuan-note/riff)           |

## 🌟 Star 历史

<a href="https://star-history.com/#siyuan-note/siyuan&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=siyuan-note/siyuan&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=siyuan-note/siyuan&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=siyuan-note/siyuan&type=Date" />
 </picture>
</a>

## 🗺️ 开发路线

* [思源开发计划与进度](https://github.com/orgs/siyuan-note/projects/1)
* [思源更新日志](CHANGELOG.md)

## 🚀 下载与安装

建议优先通过桌面和移动端的**应用商店**进行安装，以便后续一键升级版本。

### 应用商店

移动端：

* [App Store](https://apps.apple.com/us/app/siyuan/id1583226508)
* [Google Play](https://play.google.com/store/apps/details?id=org.b3log.siyuan)
* [F-Droid](https://f-droid.org/packages/org.b3log.siyuan)

桌面端：

* [Microsoft Store](https://apps.microsoft.com/detail/9p7hpmxp73k4)

### 安装包

* [B3log 官方下载](https://b3log.org/siyuan/en/download.html)
* [GitHub Releases](https://github.com/siyuan-note/siyuan/releases)

### 包管理器

#### `siyuan`

[![Packaging status](https://repology.org/badge/vertical-allrepos/siyuan.svg)](https://repology.org/project/siyuan/versions)

#### `siyuan-note`

[![Packaging status](https://repology.org/badge/vertical-allrepos/siyuan-note.svg)](https://repology.org/project/siyuan-note/versions)

### Docker 部署

<details>
<summary>Docker 部署指南</summary>

#### 概述

在服务器上运行思源最简单的方式是通过 Docker 进行部署。

* 镜像名称 `b3log/siyuan`
* [镜像地址](https://hub.docker.com/r/b3log/siyuan)

#### 文件结构

主程序位于 `/opt/siyuan/` 目录下，基本对应 Electron 安装包中 `resources` 文件夹的结构：

* appearance: 图标、主题、语言包
* guide: 用户指南文档
* stage: 界面与静态资源
* kernel: 核心程序

#### 入口脚本（Entrypoint）

入口点在构建 Docker 镜像时设定为：`ENTRYPOINT ["/opt/siyuan/entrypoint.sh"]`。该脚本允许修改容器内运行用户的 `PUID` 和 `PGID`。这在解决宿主机目录挂载时的权限问题时尤为重要。`PUID`（用户 ID）和 `PGID`（组 ID）可通过环境变量传递，便于确保访问宿主机挂载目录时拥有正确的权限。

使用 `docker run b3log/siyuan` 运行容器时，请添加以下参数：

* `--workspace`: 指定工作区文件夹路径，通过宿主机的 `-v` 挂载到容器中
* `--accessAuthCode`: 指定访问授权码

更多参数可通过 `--help` 查看。以下是使用新环境变量的启动命令示例：

```bash
docker run -d \
  -v workspace_dir_host:workspace_dir_container \
  -p 6806:6806 \
  -e PUID=1001 -e PGID=1002 \
  b3log/siyuan \
  --workspace=workspace_dir_container \
  --accessAuthCode=xxx
```

* `PUID`: 自定义用户 ID（可选，未提供时默认为 `1000`）
* `PGID`: 自定义组 ID（可选，未提供时默认为 `1000`）
* `workspace_dir_host`: 宿主机上的工作区文件夹路径
* `workspace_dir_container`: 容器内的工作区文件夹路径，需与 `--workspace` 保持一致
  * 或者，你可以通过环境变量 `SIYUAN_WORKSPACE_PATH` 设置路径。命令行参数优先级始终高于环境变量（若两者同时设置）
* `accessAuthCode`: 访问授权码（请**务必修改**，否则任何人都可访问你的数据）
  * 或者，你可通过环境变量 `SIYUAN_ACCESS_AUTH_CODE` 设置授权码。命令行参数优先级始终高于环境变量（若两者同时设置）
  * 若要禁用访问授权码检查，请将环境变量设置为 `SIYUAN_ACCESS_AUTH_CODE_BYPASS=true`

为简化配置，建议将宿主机和容器内的工作区路径保持一致，例如均设为 `/siyuan/workspace`。对应的启动命令如下：

```bash
docker run -d \
  -v /siyuan/workspace:/siyuan/workspace \
  -p 6806:6806 \
  -e PUID=1001 -e PGID=1002 \
  b3log/siyuan \
  --workspace=/siyuan/workspace/ \
  --accessAuthCode=xxx
```

#### Docker Compose

对于使用 Docker Compose 运行思源的用户，可通过环境变量 `PUID` 和 `PGID` 自定义用户与组 ID。以下是 Docker Compose 配置示例：

```yaml
version: "3.9"
services:
  main:
    image: b3log/siyuan
    command: ['--workspace=/siyuan/workspace/', '--accessAuthCode=${AuthCode}']
    ports:
      - 6806:6806
    volumes:
      - /siyuan/workspace:/siyuan/workspace
    restart: unless-stopped
    environment:
      # 时区标识符列表可参考 https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
      - TZ=${YOUR_TIME_ZONE}
      - PUID=${YOUR_USER_PUID}  # 自定义用户 ID
      - PGID=${YOUR_USER_PGID}  # 自定义组 ID
```

在此配置中：

* `PUID` 和 `PGID` 将动态设置并传递给容器
* 若未提供这些变量，则默认使用 `1000`

通过在环境中指定 `PUID` 和 `PGID`，你无需在 compose 文件中显式编写 `user` 指令（如 `user: '1000:1000'`）。容器启动时会根据环境变量动态调整内部用户与组。

#### 用户权限说明

镜像中的 `entrypoint.sh` 脚本会确保以指定的 `PUID` 和 `PGID` 创建对应的 `siyuan` 用户和组。因此，当你在宿主机创建工作区文件夹时，请注意将文件夹的用户和组所有权设置为你计划使用的 `PUID` 和 `PGID`。例如：

```bash
chown -R 1001:1002 /siyuan/workspace
```

如果你使用了自定义的 `PUID` 和 `PGID`，入口脚本会自动确保容器内创建正确的用户与组，并相应调整挂载卷的所有权。无需在 `docker run` 或 `docker-compose` 中手动传递 `-u` 参数，环境变量已处理该逻辑。

#### 隐藏端口（反向代理）

建议使用 NGINX 反向代理来隐藏 6806 端口，请注意：

* 需配置 WebSocket 反向代理 `/ws`

#### 注意事项

* 务必确认挂载卷路径正确无误，否则容器删除后数据将丢失
* 请勿使用 URL 重写进行重定向，否则可能导致认证问题。建议直接配置反向代理
* 若遇到权限问题，请验证 `PUID` 和 `PGID` 环境变量是否与宿主机挂载目录的所有者匹配

#### 限制说明

* 不支持桌面端与移动端应用连接，仅支持浏览器访问
* 暂不支持导出为 PDF、HTML 和 Word 格式
* 暂不支持导入 Markdown 文件

</details>

### Unraid 部署

<details>
<summary>Unraid 部署指南</summary>

注意：请先在终端中运行 `chown -R 1000:1000 /mnt/user/appdata/siyuan`

模板参考配置：

```
Web UI 端口: 6806
容器端口: 6806
容器路径: /home/siyuan
宿主机路径: /mnt/user/appdata/siyuan
PUID: 1000
PGID: 1000
发布参数: --accessAuthCode=******(访问授权码)
```

</details>

### TrueNAS 部署

<details>
<summary>TrueNAS 部署指南</summary>

注意：请先在 TrueNAS Shell 中运行以下命令。请将 `Pool_1/Apps_Data/siyuan` 替换为你实际的 Apps 数据集路径。

```shell
zfs create Pool_1/Apps_Data/siyuan
chown -R 1001:1002 /mnt/Pool_1/Apps_Data/siyuan
chmod 755 /mnt/Pool_1/Apps_Data/siyuan
```

导航至：Apps -> DiscoverApps -> More Options（右上角，Custom App 旁边）-> Install via YAML

模板参考配置：

```yaml
services:
  siyuan:
    image: b3log/siyuan
    container_name: siyuan
    command: ['--workspace=/siyuan/workspace/', '--accessAuthCode=2222']
    ports:
      - 6806:6806
    volumes:
      - /mnt/Pool_1/Apps_Data/siyuan:/siyuan/workspace  # 请根据实际数据集路径调整
    restart: unless-stopped
    environment:
      - TZ=America/Los_Angeles  # 如需可替换为你的时区
      - PUID=1001
      - PGID=1002
```

</details>

### 内测预览版

我们在重大版本更新前会发布内测预览版，请访问 [https://github.com/siyuan-note/insider](https://github.com/siyuan-note/insider)。

## 🏘️ 社区交流

* [英文讨论区](https://liuyun.io)
* [用户社区汇总](https://liuyun.io/article/1687779743723)
* [Awesome SiYuan（精选资源）](https://github.com/siyuan-note/awesome)

## 🛠️ 开发指南

详见 [开发指南](https://github.com/siyuan-note/siyuan/blob/master/.github/CONTRIBUTING.md)。

## ❓ 常见问题

### 思源如何存储数据？

数据保存在工作区文件夹中，具体位于 `workspace/data/` 目录下：

* `assets`: 保存所有插入的资源文件
* `emojis`: 保存表情图片
* `snippets`: 保存代码片段
* `storage`: 保存查询条件、布局配置和复习卡片等
* `templates`: 保存模板片段
* `widgets`: 保存小组件（Widgets）
* `plugins`: 保存插件
* `public`: 保存公共数据
* 其余文件夹为用户创建的笔记本目录。笔记文件夹内后缀为 `.sy` 的文件用于存储文档数据，数据格式为 JSON

### 是否支持通过第三方同步盘进行数据同步？

**不支持**通过第三方同步盘（如百度网盘、坚果云等）直接同步数据，否则可能导致数据损坏。

虽然不支持第三方同步盘直连，但思源支持连接第三方云存储服务（会员特权）。

此外，你也可以考虑手动导出和导入数据来实现跨设备同步：

* 桌面端：<kbd>设置</kbd> - <kbd>导出</kbd> - <kbd>导出数据</kbd> / <kbd>导入数据</kbd>
* 移动端：<kbd>右侧栏</kbd> - <kbd>关于</kbd> - <kbd>导出数据</kbd> / <kbd>导入数据</kbd>

### 思源是开源的吗？

思源完全开源，欢迎参与贡献：

* [用户界面与核心程序](https://github.com/siyuan-note/siyuan)
* [Android 端](https://github.com/siyuan-note/siyuan-android)
* [iOS 端](https://github.com/siyuan-note/siyuan-ios)
* [HarmonyOS 端](https://github.com/siyuan-note/siyuan-harmony)
* [Chrome 剪藏扩展](https://github.com/siyuan-note/siyuan-chrome)

更多详情请参阅 [开发指南](https://github.com/siyuan-note/siyuan/blob/master/.github/CONTRIBUTING.md)。

### 如何升级到新版本？

* 若通过应用商店安装，请前往对应商店更新
* 若在桌面端通过安装包手动安装，可开启 <kbd>设置</kbd> - <kbd>关于</kbd> - <kbd>自动下载并提示安装更新包</kbd> 选项。思源将自动下载最新版安装包并提示你安装
* 若为手动下载安装包，请重新前往官网或 GitHub Releases 下载最新安装包覆盖安装

你可点击 <kbd>设置</kbd> - <kbd>关于</kbd> - <kbd>当前版本</kbd> 中的 <kbd>检查更新</kbd>，或关注 [官方下载页](https://b3log.org/siyuan/en/download.html) / [GitHub Releases](https://github.com/siyuan-note/siyuan/releases) 获取最新版本。

### 某些区块（如列表项中的段落区块）找不到区块图标怎么办？

列表项下的第一个子区块默认省略了区块图标。你只需将光标移入该区块，然后按下 <kbd>Ctrl+/</kbd> 即可唤出区块菜单进行操作。

### 数据仓库密钥丢失了该怎么办？

* 若此前已在多台设备上正确初始化过数据仓库密钥，则所有设备上的密钥均相同。你可前往 <kbd>设置</kbd> - <kbd>关于</kbd> - <kbd>数据仓库密钥</kbd> - <kbd>复制密钥字符串</kbd> 进行查看
* 若此前未正确配置（例如多台设备的密钥不一致）或所有设备均已不可用且无法获取密钥字符串，可按以下步骤重置：

  1. 手动备份数据。可使用 <kbd>导出数据</kbd> 功能，或直接拷贝文件系统中的 <kbd>workspace/data/</kbd> 文件夹
  2. 前往 <kbd>设置</kbd> - <kbd>关于</kbd> - <kbd>数据仓库密钥</kbd> - <kbd>重置数据仓库</kbd>
  3. 重新初始化数据仓库密钥。在一台设备上完成初始化后，将密钥字符串导入其他设备
  4. 云端同步目录需切换至新目录，旧同步目录已失效，可安全删除
  5. 现有的云快照已失效，可安全删除

### 需要付费吗？

大部分功能免费开放，即使用于商业用途也无需付费。

会员特权需在付费后解锁使用，详情请参阅 [定价页面](https://b3log.org/siyuan/en/pricing.html)。

## 🙏 致谢

思源的诞生离不开众多开源项目与贡献者的支持，具体请参考项目源码中的 `kernel/go.mod`、`app/package.json` 及项目主页。

思源的发展离不开用户的反馈与推广，感谢大家为思源做出的帮助 ❤️

### 贡献者

欢迎加入我们的行列，共同贡献代码，完善思源。

<a href="https://github.com/siyuan-note/siyuan/graphs/contributors">
   <img src="https://contrib.rocks/image?repo=siyuan-note/siyuan" />
</a>