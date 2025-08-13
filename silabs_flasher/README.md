# Home Assistant 插件：Silicon Labs Flasher 插件

用于刷写 Silicon Labs 基于的无线电的 Silicon Labs Flasher 插件。

默认情况下，此插件会刷写用于使用 Zigbee（Silicon Labs EmberZNet Zigbee 堆栈）的固件。

**注意：** 确保没有其他插件或集成正在使用该无线电。特别是禁用 Zigbee 家庭自动化集成和 Silicon Labs 多协议插件。

![支持 aarch64 架构][aarch64-shield]
![支持 amd64 架构][amd64-shield]
![支持 armhf 架构][armhf-shield]
![支持 armv7 架构][armv7-shield]
![支持 i386 架构][i386-shield]

## 关于

此插件允许您使用 Gecko 引导加载程序文件格式（gbl）刷写固件。默认情况下，它附带 Home Assistant SkyConnect/ZBT-1 和 Home Assistant Yellow 的固件，用于刷写 Zigbee。

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg