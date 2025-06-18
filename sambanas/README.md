# Home Assistant 插件：Samba NAS 共享

通过网络使用 Windows 文件共享共享您的磁盘。

![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield] ![支持 armv7 架构][armv7-shield]

<!--
[![Stargazers repo roster for @dianlight/hassio-addons](https://raw.githubusercontent.com/dianlight/hassio-addons/master/.github/stars2.svg)](https://github.com/dianlight/hassio-addons/stargazers)

![downloads evolution](https://raw.githubusercontent.com/dianlight/hassio-addons/master/sambanas/stats.png)
-->

## 关于 SambaNas 插件开发的重要通知

**SambaNas 插件现在进入维护模式**

此通知是为了告知我们的用户 **SambaNas 插件将现在过渡到维护模式。** 这意味着 **这个版本的插件将不再实现未来的功能。** 我们的开发工作将仅专注于提供 **关键的bug修复**，以确保其对现有用户的持续稳定性。

**推出 SambaNas2：Samba 集成的未来**

我们很高兴地宣布 **SambaNas2**，原始 SambaNas 插件的继任者！SambaNas2 代表了 **从头完全重写，采用 Go 开发并具有全新核心。** 这将带来在性能、稳定性和未来可扩展性方面的显著改进。

**当前状态和即将发布的 Beta 版本**

SambaNas2 目前处于 **Alpha 开发阶段**。我们高兴地宣布 **公共 Beta 版本将在接下来的几周内发布**，并将通过我们的 Beta 渠道提供。

我们鼓励对最新功能和改进感兴趣的用户关注 SambaNas2 Beta 版本的发布。感谢您的持续支持。

## 安装

![动态 JSON 徽章](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fanalytics.home-assistant.io%2Faddons.json&query=%24.1a32f091_sambanas.total&label=SambaNas%20安装&link=https%3A%2F%2Faddonstats.poeschl.xyz%2F%23)
![动态 JSON 徽章](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fanalytics.home-assistant.io%2Faddons.json&query=%24.c9a35110_sambanas.total&label=SambaNas%20β%20安装&link=https%3A%2F%2Faddonstats.poeschl.xyz%2F%23)

## 帮助我！

[![](https://img.shields.io/github/sponsors/dianlight?label=赞助&logo=GitHub)](https://github.com/sponsors/dianlight)

<a href="https://www.buymeacoffee.com/ypKZ2I0"><img src="https://img.buymeacoffee.com/button-api/?text=请给我买杯咖啡&emoji=&slug=ypKZ2I0&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff" /></a>


## 关于

此插件允许您在不同操作系统之间通过网络启用文件共享。
它让您可以在 Windows 和 macOS 设备上访问您的配置文件。
您还可以指定磁盘标签以在引导时挂载并共享。


[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[discord]: https://discord.gg/c5DvZ4e
[forum]: https://community.home-assistant.io
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
[issue]: https://github.com/dianlight/hassio-addons/issues
[reddit]: https://reddit.com/r/homeassistant
[repository]: https://github.com/dianlight/hassio-addons