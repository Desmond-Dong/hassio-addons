# SONOFF Dongle Flasher

![支持 armv7 架构](https://img.shields.io/badge/armv7-yes-green.svg) ![支持 aarch64 架构](https://img.shields.io/badge/aarch64-yes-green.svg) ![支持 amd64 架构](https://img.shields.io/badge/amd64-yes-green.svg)

## 1. 简介
SONOFF Dongle Flasher 支持对 iHost MG21 芯片和 SONOFF Dongle 系列（ZBDongle-P 和 ZBDongle-E）进行在线固件刷新。

## 2. 前提条件
在使用插件之前，请确保串口未被占用（通常被 Zigbee2MQTT 或 ZHA 等服务占用）。
在固件刷新过程中，插件将尝试连接到设备并自动检查串口是否被占用。
如果被占用，插件将尝试为您停止冲突的服务。
[操作指南 >](https://github.com/iHost-Open-Source-Project/ha-operating-system?tab=readme-ov-file#readme)

## 3. 如何安装 SONOFF Dongle Flasher 插件？
### 3.1 将 SONOFF Dongle Flasher 插件添加到仓库
如果您已经添加了此仓库的插件（例如 iHost 硬件控制），请跳过此步骤，直接前往插件商店安装所需的插件。
1. 通过 URL
- 导航到设置 > 插件商店 > 点击右上角的三点菜单（⋮）并选择仓库
- 将仓库 URL 输入输入框：https://github.com/iHost-Open-Source-Project/hassio-ihost-addon
2. 通过按钮点击
- 点击此按钮自动添加插件 

[![打开您的 Home Assistant 实例并显示带有预填充特定仓库 URL 的添加插件仓库对话框。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FiHost-Open-Source-Project%2Fhassio-ihost-addon)
### 3.2 安装 SONOFF Dongle Flasher 插件
1. 在插件商店中搜索 SONOFF Dongle Flasher。
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-sonoff-dongle-flasher/images/find.png)
2. 点击安装
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-sonoff-dongle-flasher/images/install_button.png)
3. 等待安装完成
### 3.3 启动 SONOFF Dongle Flasher 插件
安装完成后，点击 **启动** 以启动插件。等待服务完全启动后再继续。
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-sonoff-dongle-flasher/images/start_button.png)
## 4. 使用 **SONOFF Dongle Flasher 插件** 刷新 Zigbee 固件

打开网页界面并点击 **"连接"**。工具将自动扫描 Home Assistant 运行设备上的 iHost MG21 芯片和连接的 Zigbee Dongles。
（目前仅支持 **SONOFF ZBDongle-P** 和 **SONOFF ZBDongle-E**。） 

![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-sonoff-dongle-flasher/images/MG21_connect_button.png)
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-sonoff-dongle-flasher/images/MG21_connect_scan.png) 

> </font><font color="red">注意*</font> 在点击 **连接** 之前，请确保 **Zigbee2MQTT** 和 **ZHA** 已停止。刷新需要访问串口，当前插件在您点击 **连接** 时会自动检查 iHost 串口是否被 Zigbee2MQTT 或 ZHA 占用。
> 
> 如果任一服务正在运行，插件将自动尝试停止它们。
> 
> 如果在刷新前未停止 Zigbee2MQTT 或 ZHA，您可能会在刷新过程中遇到设备连接失败的问题。*

### 4.1 将 Zigbee NCP 固件刷新到 iHost 内部 MG21 芯片
1. 选择 iHost 的 MG21 芯片并点击 **"确认"**。
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-sonoff-dongle-flasher/images/MG21_connect_scan_confirm_button.png)
2. 等待连接建立。
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-sonoff-dongle-flasher/images/MG21_connect_scan_Waiting%20for%20success.png)
3. 接下来，选择要刷新的 Zigbee 固件版本。（目前支持的版本包括：6.10.9, 7.4.1, 7.4.3, 7.4.4, 8.0.2。此列表仅供参考，可能随时间更新。）
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-sonoff-dongle-flasher/images/MG21_Select%20Firmware.png)
4. 点击 **"刷新"** 以开始刷新固件。
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-sonoff-dongle-flasher/images/MG21_Flash.png)
5. 等待刷新过程完成。
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-sonoff-dongle-flasher/images/MG21_Flash_success.png)
></font><font color="red">注意*</font> 如果您计划将 iHost 从 Home Assistant 切换回 CUBE 系统，请首先将 Zigbee 固件刷新回 **版本 6.10.9**。否则，可能会出现数据丢失或兼容性问题。
>
> 或者，如果您直接将固件升级到 **版本 7.4 或更高版本**，请确保初始配置 Zigbee2MQTT 以使用 **ezsp** 适配器。只有当 Zigbee2MQTT 成功使用 ezsp 启动后，您才可以重新配置它以使用 **ember** 适配器。
>
> **不要跳过此过程并直接使用 ember 适配器**，否则您可能会遇到以下风险：*使用 ember 适配器启动 Zigbee2MQTT 可能会触发错误：*"备份文件是从不受支持的 EZSP 版本创建的。"*这可能会迫使您重新配置整个 Zigbee 网络。
> 
> **详细信息**：请参阅 [GitHub 上关于 v7.4+ 固件兼容性的讨论](https://github.com/Koenkk/zigbee2mqtt/discussions/22919)。


![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-sonoff-dongle-flasher/images/MG21_ewelink_cube.png)
### 4.2 自动扫描 SONOFF ZBDongle-P 或 ZBDongle-E 并刷新 Zigbee 固件

<font color="blue">在刷新前，请将 SONOFF ZBDongle-P 或 SONOFF ZBDongle-E 插入运行 Home Assistant 的设备的 USB 端口。</font>。
1. 打开网页界面并点击 "连接"。它将自动扫描连接到运行 Home Assistant 的设备的 Zigbee Dongle。
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-sonoff-dongle-flasher/images/Dongle_Auto_scan.png)
2. 选择您要刷新的 Dongle 并点击 **"确认"**。
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-sonoff-dongle-flasher/images/Dongle_Auto_confirm.png)
3. 选择您要刷新的 Zigbee 固件版本。
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-sonoff-dongle-flasher/images/Dongle_Auto_Select%20Firmware.png)
4. 点击 **"刷新"** 以开始固件刷新过程。
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-sonoff-dongle-flasher/images/Dongle_Auto_flash.png)
5. 等待刷新过程完成。
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-sonoff-dongle-flasher/images/Dongle_Auto_Flash%20complet.png)
### 4.3 手动定位 SONOFF ZBDongle-P 或 ZBDongle-E 并刷新 Zigbee 固件

<font color="blue">在刷新前，请将 SONOFF ZBDongle-P 或 SONOFF ZBDongle-E 插入运行 Home Assistant 的设备的 USB 端口。</font>

1. 如果在自动扫描期间未找到 Dongle，您可以点击扫描页面上的 **"手动添加设备"** 选项手动定位它。
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-sonoff-dongle-flasher/images/Dongle_Manually.png)

2. 选择 "设备型号" 和 "波特率"，输入 "串口路径"，然后点击 "确认"。
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-sonoff-dongle-flasher/images/Dongle_Manually_Information.png)
您可以按照提示：**"请前往设置 > 系统 > 硬件 > 所有硬件"**，找到您要添加的硬件设备的 **串口路径**。
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-sonoff-dongle-flasher/images/Dongle_Manually_hint1.png)
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-sonoff-dongle-flasher/images/Dongle_Manually_hint2.png)
3. 选择您要刷新的 Zigbee 固件版本。
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-sonoff-dongle-flasher/images/Dongle_Manual_Select%20Firmware.png)

4. 点击 **"刷新"** 以开始刷新固件。
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-sonoff-dongle-flasher/images/Dongle_Manual_flash.png)

5. 等待刷新完成。（在刷新过程中，请禁用 ZHA 和 Zigbee2MQTT。刷新完成后，您可以重新启动它们。）
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-sonoff-dongle-flasher/images/Dongle_Manual_Flash%20complet.png)

> </font><font color="red">注意*</font> 在手动将固件刷新到 ZBDongle-P 时，进度有时可能会卡在 0%。
> 
> **可能的原因：**
> - 型号不匹配：选择的设备型号是 ZBDongle-E，但连接到指定串口的设备是 ZBDongle-P。
> - 因此，串口被占用，无法再次使用。
> 
> **请尝试：**
> - 重启插件以释放串口。
> - 验证并选择与您的设备匹配的正确型号（ZBDongle-P）。
> - 再次刷新固件。