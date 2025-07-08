# eWeLink-远程网关插件


![支持armv7架构](https://img.shields.io/badge/armv7-yes-green.svg)
![支持aarch64架构](https://img.shields.io/badge/aarch64-yes-green.svg)
![支持amd64架构](https://img.shields.io/badge/amd64-yes-green.svg)


## 关于
eWeLink-远程网关插件是一个支持添加eWeLink-远程子设备并将子设备同步到Home Assistant的eWeLink-远程网关。例如**[R5](https://sonoff.tech/product/smart-wall-switches/r5/),[R5W](https://sonoff.tech/product/smart-wall-switches/r5/),[S-Mate](https://sonoff.tech/product/diy-smart-switches/s-mate/),[S-Mate2](https://sonoff.tech/product/diy-smart-switches/s-mate/)**。您可以在Home Assistant自动化中选择eWeLink-远程子设备，并通过eWeLink-远程网关子设备报告的单击、双击和长按事件触发自动化。


## 前置条件
要使用eWeLink-远程网关插件，请确保您的Home Assistant设置满足以下条件：
- 运行Home Assistant的设备必须具有功能正常的蓝牙模块（如果没有蓝牙模块，您可以配置一个蓝牙接收器）。
- 启用蓝牙集成
- 在Home Assistant中必须启用蓝牙被动扫描。

## 安装
1. 前往插件商店 → 点击右上角的**更多**按钮（⋮）→ 选择**仓库**  
2. 粘贴以下URL：  
   [https://github.com/iHost-Open-Source-Project/hassio-ihost-addon](https://github.com/iHost-Open-Source-Project/hassio-ihost-addon)  
3. 或者，只需点击下面的按钮自动添加：

[![添加仓库](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FiHost-Open-Source-Project%2Fhassio-ihost-addon)