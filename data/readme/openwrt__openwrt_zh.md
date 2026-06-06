![OpenWrt logo](include/logo.png)

OpenWrt 项目是一个面向嵌入式设备的 Linux 操作系统。与试图创建单一、静态固件（firmware）的做法不同，OpenWrt 提供了一个完全可写的文件系统并自带软件包管理（package management）。这使你摆脱了厂商预置的应用选择与配置限制，允许你通过安装软件包来自定义设备，以适应任何应用场景。对开发者而言，OpenWrt 是一个构建应用程序的框架，无需围绕它重新编译完整的固件；对用户来说，这意味着能够完全自定义设备，以从未设想过的方式使用它。

Sunshine!

## 下载
已编译的固件镜像支持多种架构，并附带了适用于无线路由器使用的软件包集合。若要快速找到可用于从厂商原厂固件迁移至 OpenWrt 的出厂镜像（factory image），请使用 *Firmware Selector*（固件选择器）。

* [OpenWrt Firmware Selector](https://firmware-selector.openwrt.org/)

如果你的设备受支持，请点击 **Info**（信息）链接查看安装说明，或查阅下方的支持资源。

## 
高级用户可能需要额外的或特定的软件包（如 Toolchain、SDK 等）。除了简单的固件下载外，请尝试 Wiki 的下载页面：

* [OpenWrt Wiki Download](https://openwrt.org/downloads)

## Development
若要编译你自己的固件，需要 GNU/Linux、BSD 或 macOS 系统（必须使用区分大小写的文件系统）。由于缺乏区分大小写的文件系统支持，Cygwin 不受支持。

### Requirements
编译 OpenWrt 需要以下工具，软件包名称因发行版而异。完整列表及对应发行版的特定软件包请参见 [Build System Setup](https://openwrt.org/docs/guide-developer/build-system/install-buildsystem) 文档。

```
binutils bzip2 diff find flex gawk gcc-6+ getopt grep install libc-dev libz-dev
make4.1+ perl python3.7+ rsync subversion unzip which
```

### Quickstart
1. Run `./scripts/feeds update -a` to obtain all the latest package definitions defined in feeds.conf / feeds.conf.default

2. Run `./scripts/feeds install -a` to install symlinks for all obtained packages into package/feeds/

3. Run `make menuconfig` to select your preferred configuration for the toolchain, target system & firmware packages.

4. Run `make` to build your firmware. This will download all sources, build the cross-compile toolchain and then cross-compile the GNU/Linux kernel & all chosen applications for your target system.

### Related Repositories
主仓库使用多个子仓库来管理不同类别的软件包。所有软件包均通过名为 `opkg` 的 OpenWrt 软件包管理器进行安装。如果你打算开发 Web 界面或将软件包移植到 OpenWrt，请参见下方的相关仓库。

* [LuCI Web Interface](https://github.com/openwrt/luci): Modern and modular interface to control the device via a web browser.

* [OpenWrt Packages](https://github.com/openwrt/packages): Community repository of ported packages.

* [OpenWrt Routing](https://github.com/openwrt/routing): Packages specifically focused on (mesh) routing.

* [OpenWrt Video](https://github.com/openwrt/video): Packages specifically focused on display servers and clients (Xorg and Wayland).

## Support Information
如需查看受支持设备的列表，请访问 [OpenWrt Hardware Database](https://openwrt.org/supported_devices)（硬件数据库）。

### Documentation
* [Quick Start Guide](https://openwrt.org/docs/guide-quick-start/start): 快速入门指南
* [User Guide](https://openwrt.org/docs/guide-user/start): 用户手册
* [Developer Documentation](https://openwrt.org/docs/guide-developer/start): 开发者文档
* [Technical Reference](https://openwrt.org/docs/techref/start): 技术参考手册

### Support Community
* [Forum](https://forum.openwrt.org): For usage, projects, discussions and hardware advise.（使用咨询、项目交流、讨论及硬件建议）
* [Support Chat](https://webchat.oftc.net/#openwrt): Channel `#openwrt` on **oftc.net**.

### Developer Community
* [Bug Reports](https://bugs.openwrt.org): Report bugs in OpenWrt（提交 Bug 反馈）
* [Dev Mailing List](https://lists.openwrt.org/mailman/listinfo/openwrt-devel): Send patches（发送代码补丁 Patches）
* [Dev Chat](https://webchat.oftc.net/#openwrt-devel): Channel `#openwrt-devel` on **oftc.net**.

## License
OpenWrt 采用 GPL-2.0 许可证授权。