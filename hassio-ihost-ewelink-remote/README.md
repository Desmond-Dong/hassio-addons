# eWeLink-Remote Gateway Add-on


![Supports armv7 Architecture](https://img.shields.io/badge/armv7-yes-green.svg)
![Supports aarch64 Architecture](https://img.shields.io/badge/aarch64-yes-green.svg)
![Supports amd64 Architecture](https://img.shields.io/badge/amd64-yes-green.svg)


## 关于
eWeLink-Remote Gateway add-on 是一个支持添加 eWeLink-Remote 子设备并将子设备同步到 Home Assistant 的 eWeLink-Remote Gateway 网关，例如 **[R5](https://sonoff.tech/product/smart-wall-switches/r5/),[R5W](https://sonoff.tech/product/smart-wall-switches/r5/),[S-Mate](https://sonoff.tech/product/diy-smart-switches/s-mate/),[S-Mate2](https://sonoff.tech/product/diy-smart-switches/s-mate/)**。您可以在 Home Assistant 自动化中选择 eWeLink-Remote 子设备，并通过 eWeLink-Remote Gateway 子设备报告的单击、双击和长按事件触发自动化。


## 前置条件
要使用 eWeLink-Remote Gateway Add-on，请确保您的 Home Assistant 设置满足以下条件：
- 运行 Home Assistant 的设备必须具有功能正常的蓝牙模块（如果没有蓝牙模块，您可以配置一个蓝牙适配器）。
- 启用蓝牙集成
- 在 Home Assistant 中必须启用蓝牙被动扫描。

## 安装
1. 前往 Add-on Store → 点击右上角的 **更多** 按钮 (⋮) → 选择 **仓库**  
2. 粘贴以下 URL：  
   [https://github.com/iHost-Open-Source-Project/hassio-ihost-addon](https://github.com/iHost-Open-Source-Project/hassio-ihost-addon)  
3. 或者，直接点击下面的按钮自动添加：

[![添加仓库](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FiHost-Open-Source-Project%2Fhassio-ihost-addon)