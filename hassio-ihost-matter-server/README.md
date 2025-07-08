# Home Assistant Add-on: Matter Server

![Supports armv7 Architecture](https://img.shields.io/badge/armv7-yes-green.svg)

此存储库提供 **为 armv7 定制的 Matter Server add-on 和容器镜像**，这些 add-on 和镜像没有得到官方 Matter Server 分发的支持。

## 前置条件

- Home Assistant OS 版本必须为 15.2.1 或更高版本。

## 安装
1. 前往 Add-on Store → 点击右上角的 **更多** 按钮 (⋮) → 选择 **存储库**  
2. 粘贴以下 URL：  
   [https://github.com/iHost-Open-Source-Project/hassio-ihost-addon](https://github.com/iHost-Open-Source-Project/hassio-ihost-addon)  
3. 或者，直接点击下面的按钮自动添加：

[![添加存储库](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FiHost-Open-Source-Project%2Fhassio-ihost-addon)


## 关于

Home Assistant Core 的 Matter Python WebSocket 服务器。Matter（曾被称为 Connected Home over IP 或 CHIP）是一个基于 IPv6 的智能家居标准。此 add-on 提供了一个 Matter 控制器，允许你进行 Matter 设备的配置和控制。匹配的 Home Assistant Core 集成通过 WebSocket 与此服务器通信。