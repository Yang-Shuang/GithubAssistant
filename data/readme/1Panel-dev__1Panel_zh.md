<p align="center"><a href="https://1panel.pro"><img src="https://resource.1panel.pro/img/1panel-logo.png" alt="1Panel" width="300" /></a></p>

<h3 align="center">原生支持 AI 智能体的开源 VPS 控制面板</h3>

<p align="center">
  全球超过 <strong>2,000,000+</strong> 自建服务用户信赖之选
</p>

<p align="center">
  <a href="https://trendshift.io/repositories/2462" target="_blank"><img src="https://trendshift.io/api/badge/repositories/2462" alt="1Panel-dev%2F1Panel | Trendshift" style="width: 240px; height: auto;" /></a>
</p>

<p align="center">
  <a href="https://www.gnu.org/licenses/gpl-3.0.html"><img src="https://shields.io/github/license/1Panel-dev/1Panel?color=%231890FF" alt="License: GPL v3"></a>
  <a href="https://app.codacy.com/gh/1Panel-dev/1Panel"><img src="https://app.codacy.com/project/badge/Grade/da67574fd82b473992781d1386b937ef" alt="Codacy"></a>
  <a href="https://discord.gg/bUpUqWqdRr"><img src="https://img.shields.io/discord/1318846410149335080?logo=discord&labelColor=%20%235462eb&logoColor=%20%23f5f5f5&color=%20%235462eb" alt="Discord"></a>
  <a href="https://github.com/1Panel-dev/1Panel/releases"><img src="https://img.shields.io/github/v/release/1Panel-dev/1Panel" alt="GitHub release"></a>
  <a href="https://github.com/1Panel-dev/1Panel"><img src="https://img.shields.io/github/stars/1Panel-dev/1Panel?color=%231890FF&style=flat-square" alt="Stars"></a>
</p>

<p align="center">
  <a href="/README.md"><img alt="English" src="https://img.shields.io/badge/English-d9d9d9"></a>
  <a href="/docs/README.zh-Hans.md"><img alt="中文(简体)" src="https://img.shields.io/badge/中文(简体)-d9d9d9"></a>
  <a href="/docs/README.ja.md"><img alt="日本語" src="https://img.shields.io/badge/日本語-d9d9d9"></a>
  <a href="/docs/README.pt-br.md"><img alt="Português (Brasil)" src="https://img.shields.io/badge/Português (Brasil)-d9d9d9"></a>
  <a href="/docs/README.ar.md"><img alt="العربية" src="https://img.shields.io/badge/العربية-d9d9d9"></a>
  <a href="/docs/README.de.md"><img alt="Deutsch" src="https://img.shields.io/badge/Deutsch-d9d9d9"></a>
  <a href="/docs/README.es.md"><img alt="Español" src="https://img.shields.io/badge/Español-d9d9d9"></a>
  <a href="/docs/README.fr.md"><img alt="français" src="https://img.shields.io/badge/français-d9d9d9"></a>
  <a href="/docs/README.ko.md"><img alt="한국어" src="https://img.shields.io/badge/한국어-d9d9d9"></a>
  <a href="/docs/README.id.md"><img alt="Bahasa Indonesia" src="https://img.shields.io/badge/Bahasa Indonesia-d9d9d9"></a>
  <a href="/docs/README.zh-Hant.md"><img alt="中文(繁體)" src="https://img.shields.io/badge/中文(繁體)-d9d9d9"></a>
  <a href="/docs/README.tr.md"><img alt="Türkçe" src="https://img.shields.io/badge/Türkçe-d9d9d9"></a>
  <a href="/docs/README.ru.md"><img alt="Русский" src="https://img.shields.io/badge/Русский-d9d9d9"></a>
  <a href="/docs/README.ms.md"><img alt="Bahasa Melayu" src="https://img.shields.io/badge/Bahasa Melayu-d9d9d9"></a>
</p>

---

## 什么是 1Panel？

1Panel 是一款现代化的开源 VPS 控制面板，也是目前唯一一款**原生支持 AI 智能体（AI Agent）**的工具。你可以通过一个简洁的 Web 界面运行 Ollama 模型、部署 OpenClaw 智能体，并管理整个服务器技术栈，无需记忆任何命令行（CLI）指令。

👉 观看 [2分钟介绍视频](https://www.youtube.com/watch?v=Jl_wqp-XA08)

## 为什么选择 1Panel？

| | 1Panel | cPanel / Plesk | aaPanel | Webmin |
|--|--------|----------------|---------|--------|
| 免费且开源 | ✅ | ❌ | 部分 | ✅ |
| 原生支持 AI 智能体（AI Agent）运行环境 | ✅ | ❌ | ❌ | ❌ |
| 一键应用商店 | ✅ 165+ 款应用 | ❌ | ✅ | ❌ |
| 现代化界面（2020年后设计） | ✅ | ❌ | 部分 | ❌ |
| Docker / 容器管理 | ✅ | ❌ | ❌ | ❌ |
| 活跃的开发维护 | ✅ | ✅ | ✅ | 较慢 |

## 核心功能

- **AI 智能体运行环境**：在控制台中直接部署 Ollama 大语言模型（LLM）、启动 OpenClaw 个人智能体，并监控 GPU 利用率——无需额外搭建独立的 AI 技术栈。
- **一键部署网站**：自动完成域名绑定、SSL 证书申请与配置、Nginx 设置，零手动操作即可上线生产级网站。
- **应用商店**：内置 Nextcloud、Bitwarden、Umami、NocoBase 等 165+ 款经过验证的开源应用，一键安装与更新。
- **Docker 与容器管理**：通过可视化界面创建、启停、查看容器及镜像，并管理网络和卷——告别繁琐的命令行操作。
- **开箱即用的安全防护**：内置防火墙规则、fail2ban 防暴力破解、容器隔离、WAF（Web 应用防火墙）及审计日志，安装即用。
- **备份与恢复**：支持定时自动备份至 AWS S3、Cloudflare R2 或本地存储，一键即可还原任意快照。

## 快速开始

> **系统要求：** Linux VPS（支持 Debian / Ubuntu / CentOS / Rocky），内存 ≥ 1 GB，可访问互联网。  
> 安装过程仅需约 60 秒。

```bash
bash -c "$(curl -sSL https://resource.1panel.pro/v2/quick_start.sh)"
```

安装完成后，在浏览器中访问 `http://<你的服务器IP>:<端口>/<安全入口>`。如需获取登录凭据，请通过 SSH 执行命令 `1pctl user-info`。

## 界面截图

![1Panel UI](https://resource.1panel.pro/img/overview_en_v2.png)

## Pro 专业版

1Panel 开源版（OSS）永久免费。Pro 版本专为团队与生产环境增加了以下功能：

| Feature | OSS | Pro |
|---------|:---:|:---:|
| 一键安装应用 | ✅ | ✅ |
| AI 智能体（OpenClaw） | 1 个智能体 | 无限使用 |
| WAF & 高级安全防护 | 基础版 | ✅ |
| 网站防篡改保护 | ❌ | ✅ |
| 网站运行状态监控 | ❌ | ✅ |
| 多节点管理 | ❌ | ✅ |
| 自定义 Logo 与主题 | ❌ | ✅ |
| 优先技术支持 | ❌ | ✅ |

**起价 $80/年**。[对比方案并开启 30 天免费试用 →](https://1panel.pro/pricing)

## ⭐ Star 增长记录

[![Star History Chart](https://api.star-history.com/svg?repos=1Panel-dev/1Panel&type=Date)](https://star-history.com/#1Panel-dev/1Panel&Date)

## 社区与支持

- **Discord** —— [加入社区](https://discord.gg/bUpUqWqdRr) 获取帮助、提交功能建议或展示你的项目
- **官方文档** —— [1panel.pro/docs](https://1panel.pro/docs)
- **问题反馈** —— 请前往 [GitHub Issues](https://github.com/1Panel-dev/1Panel/issues) 提交 Bug 报告

## 安全须知

发现安全漏洞？请在公开披露前阅读 [SECURITY.md](/SECURITY.md)。

## 开源协议

本项目基于 [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html) 授权。