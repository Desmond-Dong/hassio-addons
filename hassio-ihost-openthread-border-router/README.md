# Home Assistant 插件：OpenThread 边界路由器插件

![支持 armv7 架构](https://img.shields.io/badge/armv7-yes-green.svg)

OpenThread 边界路由器插件。该插件使用上游的 OpenThread 边界路由器实现，并将其封装为 Home Assistant 的插件。

**注意：** 这需要支持 802.15.4 的无线电设备，并带有 OpenThread RCP 固件。

> 重要！！！
>
> 当使用 iHost 的内置 **MG21** 芯片（位于 `/dev/ttyS4`）与此插件一起使用时，**必须禁用硬件流控制**，以便 OpenThread 边界路由器能正常工作。

![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-openthread-border-router/images/otbr_configuration.png)

## 关于

此插件允许您形成或加入 Thread 网络，并将 Home Assistant 设置为 Thread 边界路由器。

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg


## 安装
1. 前往插件商店 → 点击右上角的 **更多** 按钮（⋮）→ 选择 **仓库**  
2. 粘贴以下 URL：  
   [https://github.com/iHost-Open-Source-Project/hassio-ihost-addon](https://github.com/iHost-Open-Source-Project/hassio-ihost-addon)  
3. 或者，直接点击下面的按钮自动添加：

[![添加仓库](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FiHost-Open-Source-Project%2Fhassio-ihost-addon)