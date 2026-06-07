<h1 align="center" style="padding-top: 60px;padding-bottom: 40px;">
    <a href="https://electerm.html5beta.com">
        <img src="https://github.com/electerm/electerm-resource/raw/master/static/images/electerm.png", alt="" />
    </a>
</h1>

# electerm [![Tweet](https://badgers.space/badge/Tweet/Tweet/social)](https://twitter.com/intent/tweet?text=Open%20sourced%20terminal%2Fssh%2Fsftp%20client(linux%2C%20mac%2C%20win)&url=https%3A%2F%2Fgithub.com%2Felecterm%2Felecterm&hashtags=electerm,ssh,terminal,sftp)

[![GitHub version](https://badgers.space/github/release/electerm/electerm?corner_radius=m)](https://github.com/electerm/electerm/releases)
[![Build Status](https://github.com/electerm/electerm/actions/workflows/mac-test-1.yml/badge.svg)](https://github.com/electerm/electerm/actions)
[![license](https://img.shields.io/github/license/electerm/electerm)](https://github.com/electerm/electerm/blob/master/LICENSE)
[![JavaScript Style Guide](https://img.shields.io/badge/code_style-standard-brightgreen.svg)](https://standardjs.com)
[![Get it from the Snap Store](https://img.shields.io/badge/Snap-Store-green)](https://snapcraft.io/electerm)
[![Get it from the Microsoft Store](https://img.shields.io/badge/Microsoft-Store-blue)](https://www.microsoft.com/store/apps/9NCN7272GTFF)
[![Debian Repository](https://img.shields.io/badge/Debian-Repository-red)](https://electerm-repos.html5beta.com/deb)
[![GitHub Sponsors](https://img.shields.io/github/sponsors/electerm?label=Sponsors)](https://github.com/sponsors/electerm)
[![Powered by manate](https://img.shields.io/badge/Powered%20by-manate-blue)](https://github.com/tylerlong/manate)
[![Discord](https://img.shields.io/badge/Discord-Join-blue?logo=discord)](https://discord.gg/855W7g8EVd)
[![star](https://atomgit.com/electerm/electerm/star/badge.svg)](https://atomgit.com/electerm/electerm)

[![English](https://img.shields.io/badge/English-EN-blue)](README.md) [![中文](https://img.shields.io/badge/中文-Chinese-blue)](README_cn.md)

[![DigitalOcean Referral Badge](https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg)](https://www.digitalocean.com/?refcode=c10bcb28b846&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)

[![Vercel OSS Program](https://vercel.com/oss/program-badge.svg)](https://vercel.com/oss)

开源的终端/SSH/SFTP/Telnet/串口/RDP/VNC/Spice/FTP 客户端（支持 Linux、macOS、Windows）。

对于资深开发者，你也可以尝试在浏览器中运行的 Web 应用版本（支持移动设备）：[electerm-web](https://github.com/electerm/electerm-web) 或 [electerm-web Docker 镜像](https://github.com/electerm/electerm-web-docker)

在线演示：[https://electerm-demo.html5beta.com](https://electerm-demo.html5beta.com)

## Atlas Cloud

<div align="center">
  <a href="https://www.atlascloud.ai/?utm_source=github&utm_medium=link&utm_campaign=electerm">
    <img src="https://github.com/electerm/electerm-resource/blob/master/static/images/atlas-cloud.png?raw=true" alt="Atlas Cloud" width="200" />
  </a>
</div>

[Atlas Cloud](https://www.atlascloud.ai/?utm_source=github&utm_medium=link&utm_campaign=electerm) 为 electerm 中的 AI 驱动工作流提供兼容 OpenAI 的 API 和模型访问权限。

<div align="center">
  <img src="https://github.com/electerm/electerm-resource/raw/master/static/images/electerm.gif", alt="" />
</div>

## Features

- 可作为终端管理器或文件浏览器，同时支持 SSH/SFTP/FTP/Telnet/串口/RDP/VNC/Spice 连接
- 兼容 Windows 7+ (x64/arm64)、macOS 10.15+ (x64/arm64)、Linux(x64/arm64/Loong64)，甚至支持 glibc 2.17+ 的旧版 Linux（如 UOS、Kylin、Ubuntu 18.04 等）
- 全局快捷键切换窗口显示与隐藏（类似 guake，默认为 `ctrl + 2`）
- 跨平台支持（Linux、macOS、Windows）
- 🇺🇸 🇨🇳 🇧🇷 🇷🇺 🇪🇸 🇫🇷 🇹🇷 🇭🇰 🇯🇵 🇸🇦 🇩🇪 🇰🇷 🇮🇩 🇵🇱 多语言支持（[electerm-locales](https://github.com/electerm/electerm-locales)，欢迎贡献或提交修复）
- 双击即可直接编辑远程文件。
- 支持公钥+密码认证。
- 支持 Zmodem（rz、sz）。
- 支持 SSH 隧道。
- 支持 [Trzsz](https://github.com/trzsz/trzsz)(trz/tsz)，功能类似 rz/sz，且兼容 tmux。
- 透明窗口（Mac、Windows）。
- 终端背景图片。
- 全局/会话级代理。
- 快捷命令
- UI/终端主题
- 支持将书签、主题、快捷命令同步至 GitHub/Gitee Secret Gist、WebDAV、自定义服务器或 electerm 云
- 快速向单个或所有终端输入内容。
- AI 助手集成（支持 [DeepSeek](https://www.deepseek.com)、OpenAI 及其他任意 AI API），提供命令建议、脚本编写、解释选中的终端内容以及创建书签等功能。
- MCP（模型上下文协议）小部件，用于 AI 助手和外部工具集成——详见 [MCP Widget Usage Guide](https://github.com/electerm/electerm/wiki/MCP-Widget-Usage-Guide)
- 深度链接支持：可通过 `telnet://192.168.2.31:34554` 或 `ssh://user@host:22` 等 URL 直接打开连接——详见 [Deep link support wiki](https://github.com/electerm/electerm/wiki/Deep-link-support)
- 命令行用法：查看 [wiki](https://github.com/electerm/electerm/wiki/Command-line-usage)

## Download

- [Homepage](https://electerm.html5beta.com)
- [sourceforge](https://sourceforge.net/projects/electerm.mirror/files/)
- [github releases](https://github.com/electerm/electerm/releases)

## Install

- macOS 用户：`brew install --cask electerm`
- 通过 Snap 安装：`sudo snap install electerm --classic`
- 部分 Linux 发行版可在系统自带的应用商店（如 Ubuntu、Deepin、Mint）中获取。
- 某些 Linux 系统的 `rpm`、`deb` 或 `snap` 版本可能无法正常运行，可尝试使用 `tar.gz` 或 `.appImage` 版本。
- Windows 用户可从 [Windows 应用商店](https://www.microsoft.com/store/apps/9NCN7272GTFF) 安装，也推荐使用命令行安装包 [winget](https://github.com/microsoft/winget-cli) 和 [scoop](https://github.com/lukesampson/scoop)：

```powershell
# winget https://github.com/microsoft/winget-cli
winget install electerm.electerm

# scoop https://github.com/lukesampson/scoop
scoop bucket add dorado https://github.com/chawyehsu/dorado
scoop install dorado/electerm
```

- 通过 Debian 软件源安装（适用于基于 Debian/Ubuntu 的系统），使用 `apt` 命令：查看 [https://electerm-repos.html5beta.com/deb](https://electerm-repos.html5beta.com/deb)

- 通过 npm 安装

```bash
npm i -g electerm

```

## Upgrade

- 自动升级：发布新版本后，重新启动 electerm 时会收到升级提示。点击升级按钮即可完成更新。
- 手动下载：直接下载最新版本并重新安装即可。
- npm 方式：若通过 npm 安装，只需再次运行 `npm i -g electerm`。
- 若使用 Snap 或其他发行版系统，这些平台通常会自动提供升级。

## Known issues

[https://github.com/electerm/electerm/wiki/Know-issues](https://github.com/electerm/electerm/wiki/Know-issues)

## Troubleshoot

[https://github.com/electerm/electerm/wiki/Troubleshoot](https://github.com/electerm/electerm/wiki/Troubleshoot)

## Discussion

[![Discord](https://img.shields.io/badge/Discord-Join-blue?logo=discord)](https://discord.gg/855W7g8EVd)

[Discussion board](https://github.com/electerm/electerm/discussions)

![electerm-wechat-group-qr.jpg](https://electerm.html5beta.com/electerm-wechat-group-qr.jpg)

## Support

非常欢迎你的反馈与建议。请随时 [提交 Issue](https://github.com/electerm/electerm/issues)、[发起新讨论](https://github.com/electerm/electerm/discussions/new)、[创建/修复语言文件](https://github.com/electerm/electerm-locales) 或提交 Pull Request，所有贡献均表示热烈欢迎。

## Sponsor this project

GitHub Sponsors

[https://github.com/sponsors/electerm](https://github.com/sponsors/electerm)

Ko-fi

[https://ko-fi.com/zhaoxudong](https://ko-fi.com/zhaoxudong)

微信捐赠

[![wechat donate](https://electerm.html5beta.com/electerm-wechat-donate.png)](https://github.com/electerm)

## Dev

```bash
# May only works in Linux
# needs nodejs/npm, suggest using nvm to install nodejs/npm
# with nodejs 24.x

git clone git@github.com:electerm/electerm.git
cd electerm
npm config set legacy-peer-deps true
npm i

# start vite dev server, requires port 5570
npm start

# in a separate terminal session run app
npm run app

# code format check
npm run lint

# code format fix
npm run fix
```

## Test

```bash
npm run b
npm run prepare-test
cp .sample.env .env

# edit .env, fill your test host/username/password, may only works in mac OS
npm run test
```

## Test build

```bash
# May only works in Linux
# Install yarn first(to do yarn autoclean)
# See https://yarnpkg.com/en/docs/install

# Build linux only with -l
npm i
npm run b
npm run pb
./node_modules/.bin/electron-builder --linux tar.gz
# or replace tar.gz to rpm/deb/AppImage
# check dist/ folder

# build for linux arm/
./node_modules/.bin/electron-builder --linux --arm64
```

## Video guide

- [https://electerm.html5beta.com/videos](https://electerm.html5beta.com/videos)

## Change log

Visit [Releases](https://github.com/electerm/electerm/releases).

## Contact author

[zxdong@gmail.com](mailto:zxdong@gmail.com)


## License

MIT

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=electerm/electerm&type=Date)](https://www.star-history.com/#electerm/electerm&Date)