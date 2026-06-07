# Vuls: VULnerability Scanner

[![License](https://img.shields.io/github/license/future-architect/vuls.svg?style=flat-square)](https://github.com/future-architect/vuls/blob/master/LICENSE)
[![Go Report Card](https://goreportcard.com/badge/github.com/future-architect/vuls)](https://goreportcard.com/report/github.com/future-architect/vuls)
[![Contributors](https://img.shields.io/github/contributors/future-architect/vuls.svg)](https://github.com/future-architect/vuls/graphs/contributors)

![Vuls-logo](img/vuls_logo.png)

面向 Linux/FreeBSD 的漏洞扫描器，无代理（agent-less），使用 Go 语言编写。  
Twitter: [@vuls_en](https://twitter.com/vuls_en)

![Vuls-Abstract](img/vuls-abstract.png)

![Vulsrepo](https://raw.githubusercontent.com/usiusi360/vulsrepo/master/gallery/demo.gif)

[![asciicast](https://asciinema.org/a/3y9zrf950agiko7klg8abvyck.png)](https://asciinema.org/a/3y9zrf950agiko7klg8abvyck)

![Vuls-slack](img/vuls-slack-en.png)

----

## 概述

对于系统管理员而言，每天进行安全漏洞分析和软件更新可能是一项沉重的负担。
为避免生产环境停机，系统管理员通常会选择不使用包管理器提供的自动更新选项，而是手动执行更新。
这会导致以下问题：

- 系统管理员必须持续关注 NVD（国家漏洞数据库）或类似数据库中的新漏洞。
- 如果服务器上安装了大量软件包，系统管理员可能无法监控所有软件。
- 分析受新漏洞影响的服务器成本高昂，且在分析过程中很容易遗漏一两台服务器。

Vuls 是一款为解决上述问题而创建的工具，具有以下特点：

- 向用户通报与系统相关的漏洞。
- 通知受影响的服务器。
- 自动检测漏洞，防止遗漏。
- 使用 CRON 或其他方法定期生成报告，以便管理漏洞。

![Vuls-Motivation](img/vuls-motivation.png)

----

## 主要功能

### 扫描 Linux/FreeBSD/Windows/macOS 中的漏洞

[支持主要的 Linux/FreeBSD/Windows/macOS](https://vuls.io/docs/en/supported-os.html)

- Alpine、Amazon Linux、CentOS、AlmaLinux、Rocky Linux、Debian、Oracle Linux、Raspbian、RHEL、openSUSE、openSUSE Leap、SUSE Enterprise Linux、Fedora 和 Ubuntu
- FreeBSD
- Windows
- macOS
- 云环境、本地部署、运行中的 Docker 容器

### 高质量扫描

- 漏洞数据库（Vulnerability Database）
  - [NVD](https://nvd.nist.gov/)
  - [JVN(Japanese)](http://jvndb.jvn.jp/apis/myjvn/)

- OVAL（开放漏洞评估语言）
  - [Red Hat](https://www.redhat.com/security/data/oval/)
  - [Debian](https://www.debian.org/security/oval/)
  - [Ubuntu](https://security-metadata.canonical.com/oval/)
  - [SUSE](http://ftp.suse.com/pub/projects/security/oval/)
  - [Oracle Linux](https://linux.oracle.com/security/oval/)

- 安全公告（Security Advisory）
  - [Alpine-secdb](https://git.alpinelinux.org/cgit/alpine-secdb/)
  - [Red Hat Security Advisories](https://access.redhat.com/security/security-updates/)
  - [Debian Security Bug Tracker](https://security-tracker.debian.org/tracker/)
  - [Ubuntu CVE Tracker](https://people.canonical.com/~ubuntu-security/cve/)
  - [Microsoft CVRF](https://api.msrc.microsoft.com/cvrf/v2.0/swagger/index)

- 命令（yum、zypper、pkg-audit）
  - RHSA / ALAS / ELSA / FreeBSD-SA
  - Changelog（更新日志）

- PoC（概念验证代码）、Exploit（漏洞利用）
  - [Exploit Database](https://www.exploit-db.com/)
  - [Metasploit-Framework modules](https://www.rapid7.com/db/?q=&type=metasploit)
  - [qazbnm456/awesome-cve-poc](https://github.com/qazbnm456/awesome-cve-poc)
  - [nomi-sec/PoC-in-GitHub](https://github.com/nomi-sec/PoC-in-GitHub)
  - [gmatuz/inthewilddb](https://github.com/gmatuz/inthewilddb)
  - [projectdiscovery/nuclei-templates](https://github.com/projectdiscovery/nuclei-templates)

- CERT（计算机应急响应团队）
  - [US-CERT](https://www.us-cert.gov/ncas/alerts)
  - [JPCERT](http://www.jpcert.or.jp/at/2019.html)

- KEV（已知被利用漏洞）
  - CISA（美国网络安全与基础设施安全局）：[Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
  - VulnCheck: [VulnCheck KEV](https://vulncheck.com/kev)

- 网络威胁情报（MITRE ATT&CK and CAPEC）
  - [mitre/cti](https://github.com/mitre/cti)

- 依赖库（Libraries）
  - [aquasecurity/vuln-list](https://github.com/aquasecurity/vuln-list)

- WordPress
  - [wpscan](https://wpscan.com/api)

### 扫描模式

[快速扫描 (Fast Scan)](https://vuls.io/docs/en/architecture-fast-scan.html)

- 无需 root 权限，无依赖项
- 对目标服务器的负载几乎为零
- 支持离线模式扫描（无需联网）。（适用于 CentOS、Alma Linux、Rocky Linux、Debian、Oracle Linux、Red Hat、Fedora 和 Ubuntu）

[快速 root 扫描 (Fast Root Scan)](https://vuls.io/docs/en/architecture-fast-root-scan.html)

- 需要 root 权限进行扫描
- 对目标服务器的负载几乎为零
- 使用 `yum-ps` 检测受更新影响的进程（适用于 Amazon Linux、CentOS、Alma Linux、Rocky Linux、Oracle Linux、Fedora 和 RedHat）
- 使用 debian-goodies 的 `checkrestart` 检测已更新但尚未重启的进程（适用于 Debian 和 Ubuntu）
- 支持离线模式扫描（无需联网）。（适用于 CentOS、Alma Linux、Rocky Linux、Debian、Oracle Linux、Red Hat、Fedora 和 Ubuntu）

### [远程扫描、本地扫描与服务器模式](https://vuls.io/docs/en/architecture-remote-local.html)

[远程扫描模式 (Remote scan mode)](https://vuls.io/docs/en/architecture-remote-scan.html)

- 只需在一台机器上配置，并通过 SSH 连接其他目标服务器即可

[本地扫描模式 (Local scan mode)](https://vuls.io/docs/en/architecture-local-scan.html)

- 如果你不希望中央 Vuls 服务器通过 SSH 连接每台服务器，可以使用本地扫描模式。

[服务器模式 (Server mode)](https://vuls.io/docs/en/usage-server.html)

- 首先以服务器模式启动 Vuls，并作为 HTTP 服务器监听。
- 接着在目标服务器上执行命令收集软件信息，然后通过 HTTP 将结果发送至 Vuls 服务器。你将收到 JSON 格式的扫描结果。
- 无需 SSH，无需安装扫描器。仅在目标服务器上直接执行 Linux 命令即可。

### **动态**分析

- 可通过 SSH 连接并执行命令来获取服务器状态。
- 当目标服务器更新了内核等组件但未重启时，Vuls 会发出警告。

### 扫描非操作系统包的漏洞

- 编程语言依赖库
- 自行编译的软件
- 网络设备

Vuls 提供了一些检测这些漏洞的选项：

- [基于 Lockfile 的扫描](https://vuls.io/docs/en/usage-scan-non-os-packages.html#library-vulns-scan)
- [GitHub 集成](https://vuls.io/docs/en/usage-scan-non-os-packages.html#usage-integrate-with-github-security-alerts)
- [基于 CPE（通用平台枚举）的扫描](https://vuls.io/docs/en/usage-scan-non-os-packages.html#cpe-scan)
- [OWASP Dependency Check 集成](https://vuls.io/docs/en/usage-scan-non-os-packages.html#usage-integrate-with-owasp-dependency-check-to-automatic-update-when-the-libraries-are-updated-experimental)

## 扫描 WordPress 核心、主题与插件

- [扫描 WordPress](https://vuls.io/docs/en/usage-scan-wordpress.html)

## 其他特性 (MISC)

- 非破坏性测试
- 在 AWS 上扫描前无需预先授权
  - Vuls 非常适合与持续集成（CI）配合使用，因为测试可以每天运行。这使你能够快速发现漏洞。
- 自动生成配置文件模板
  - 自动检测通过 CIDR 配置的主机，并生成配置文件模板
- 支持邮件和 Slack 通知（支持日语）
- 扫描结果可通过配套软件、终端中的 TUI 查看器或 Web UI（[VulsRepo](https://github.com/ishiDACo/vulsrepo)）进行查看。

----

## Vuls 不做什么

- Vuls 不会自动更新存在漏洞的软件包。

----

## 文档

有关安装、教程、用法等更多信息，请访问 [vuls.io](https://vuls.io/)  
[日本語翻訳ドキュメント](https://vuls.io/ja/)

----

## 作者

Vuls 由 kotakanbe（[@kotakanbe](https://twitter.com/kotakanbe)）创建，[这些优秀的人](https://github.com/future-architect/vuls/graphs/contributors)也做出了贡献。

## 参与贡献

请参阅 [vulsdoc](https://vuls.io/docs/en/how-to-contribute.html)

----

## 赞助商

|  |  |
| ------------- | ------------- |
| <a href="https://www.tines.com/?utm_source=oss&utm_medium=sponsorship&utm_campaign=vuls"><img src="img/sponsor/tines.png" align="left" width="600px" ></a> | Tines 是面向安全团队的无代码自动化工具。无需开发团队即可构建强大、可靠的工作流。 |
| <a href="https://www.sakura.ad.jp/"><img src="https://vuls.io/img/icons/sakura.svg" align="left" width="600px" ></a> | SAKURA internet Inc. 成立于 1996 年的互联网公司。我们利用位于日本的自有数据中心，为个人、企业以及教育和公共部门提供“樱花共享服务器”、“樱花 VPS”和“樱花云”等云计算服务。秉持“将你想做的事变为能做的事”的理念，我们为各个领域提供 DX（数字化转型）解决方案。 |

----

## 许可证

请参阅 [LICENSE](https://github.com/future-architect/vuls/blob/master/LICENSE)。