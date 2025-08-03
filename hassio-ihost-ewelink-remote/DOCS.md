# eWeLink-Remote Gateway
## 1. 简介
eWeLink-Remote Gateway 插件是一个支持添加 eWeLink-Remote 子设备并将子设备同步到 Home Assistant 的 eWeLink-Remote Gateway 网关，例如 **[R5](https://sonoff.tech/product/smart-wall-switches/r5/),[R5W](https://sonoff.tech/product/smart-wall-switches/r5/),[S-Mate](https://sonoff.tech/product/diy-smart-switches/s-mate/),[S-Mate2](https://sonoff.tech/product/diy-smart-switches/s-mate/)**。您可以在 Home Assistant 自动化中选择 eWeLink-Remote 子设备，并通过 eWeLink-Remote Gateway 子设备报告的单击、双击和长按事件触发自动化。**了解更多关于 eWeLink-Remote 的信息** [这里](https://sonoff.tech/news-and-events/what-is-ewelink-remote-control/)。

## 2. 前置条件
要使用 eWeLink-Remote Gateway 插件，请确保您的 Home Assistant 设置满足以下条件：
- 运行 Home Assistant 的设备必须具有功能正常的蓝牙模块（如果没有蓝牙模块，您可以配置一个蓝牙适配器）。
- 启用蓝牙集成
- 在 Home Assistant 中必须启用蓝牙被动扫描。
    - 要启用蓝牙被动扫描：
    转到蓝牙集成 > 配置 > 配置蓝牙选项，选中被动扫描，然后点击提交。

## 3. 如何安装 eWeLink-Remote Gateway 插件？
### 3.1 将 eWeLink-Remote Gateway 插件添加到仓库
如果您已经添加了此仓库的插件（例如 iHost 硬件控制），则可以跳过此步骤，直接前往插件商店安装所需的插件。
1. 通过 URL
- 导航到设置 > 插件商店 > 点击右上角的三点菜单（⋮）并选择仓库
- 在输入框中输入仓库 URL：https://github.com/iHost-Open-Source-Project/hassio-ihost-addon
2. 通过按钮点击
- 点击此按钮自动添加插件    
[![打开您的 Home Assistant 实例并显示添加插件仓库对话框，其中预填充了特定的仓库 URL。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FiHost-Open-Source-Project%2Fhassio-ihost-addon)
### 3.2 安装 eWeLink-Remote Gateway 插件
1. 在插件商店中搜索 eWeLink-Remote Gateway。
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-ewelink-remote/images/find.png)
2. 点击安装
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-ewelink-remote/images/install_Addon.png)
3. 等待安装完成
### 3.3 启动 eWeLink-Remote Gateway 插件
安装后，点击启动以启动插件。等待服务完全启动后再继续操作。
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-ewelink-remote/images/start.png)
## 4. 通过 eWeLink-Remote Gateway 插件添加设备
1. 点击“Web 界面”进入插件操作界面。
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-ewelink-remote/images/open_web_ui1.png)
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-ewelink-remote/images/open_web_ui.png)
**注意*：**
- 要使用 eWeLink-Remote Gateway 插件，Home Assistant 中必须启用蓝牙。如果没有蓝牙硬件模块（可配置的蓝牙适配器）或蓝牙集成未启用，插件将无法工作；
您可以通过查看日志来确定插件是否因蓝牙集成未启用而无法运行。
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-ewelink-remote/images/Log-image.png)
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-ewelink-remote/images/Log-Blue.png)
- 在点击“配对”以开始添加 eWeLink-Remote 子设备之前，您需要配置并启用蓝牙“**被动扫描**”（[被动扫描](https://www.home-assistant.io/integrations/bluetooth/#passive-scanning)）以检测和连接到 eWeLink-Remote 子设备。如果提前未启用，将显示提示页面。您可以按照提示路径（转到蓝牙集成 > 配置 > 配置蓝牙选项，选中被动扫描，然后点击提交。）来启用它。
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-ewelink-remote/images/passive_scanning.png)
2. 点击“配对”以开始添加设备。
倒计时为 180 秒。在添加过程中，您可以手动点击“退出 xxs”以停止添加设备。在倒计时期间按子设备的任何按钮以完成设备添加。
**注意*：**
- 支持 180 秒内添加多个设备
- 添加智能灯光设备的上限为 50 个
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-ewelink-remote/images/Pair.png)
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-ewelink-remote/images/add_device.png)
3. 编辑设备列表  
点击“编辑”以管理已添加的设备，选择相应的设备，然后点击“删除”以确认删除选中的设备
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-ewelink-remote/images/Edit.png)
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-ewelink-remote/images/Del.png)
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-ewelink-remote/images/Del_1.png)
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-ewelink-remote/images/device_deleted.png)
## 5. 在 Home Assistant 中查看设备
1. 在 Home Assistant 中查看设备
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-ewelink-remote/images/HA_device.png)
2. 设备添加成功后，您可以在 Home Assistant 中配置场景作为场景触发条件。
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-ewelink-remote/images/Sence.png)
**注意*：**
- 在 Home Assistant 自动化中成功配置 eWeLink-Remote 子设备后，如果实体名称被更改，自动化配置信息中的实体名称将显示为“未知”，但这不会影响自动化场景触发。
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-ewelink-remote/images/UNknow.png)