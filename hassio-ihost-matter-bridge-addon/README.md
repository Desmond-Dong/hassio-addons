# iHost的Matter Bridge

![支持armv7架构](https://img.shields.io/badge/armv7-yes-green.svg)

## 关于

iHost的Matter Bridge插件将Home Assistant设备的实体暴露为Matter设备，使其能够与Matter平台（如Apple Home、Google Home和Amazon Alexa）集成。  
此插件基于iHost Matter Bridge，并通过了Matter认证，以确保协议兼容性和长期可用性。

同时，它兼容网页和移动终端。

## 前置条件

- Matter Bridge插件仅适用于HA over iHost项目，允许用户将Home Assistant设备暴露为Matter设备，并将它们同步到受支持的Matter平台进行控制。
- Home Assistant OS版本必须为15.2.1或更高。

## 安装
1. 前往插件商店 → 点击右上角的**更多**按钮（⋮）→ 选择**仓库**  
2. 粘贴以下URL：  
   [https://github.com/iHost-Open-Source-Project/hassio-ihost-addon](https://github.com/iHost-Open-Source-Project/hassio-ihost-addon)  
3. 或者，直接点击下方按钮自动添加：

[![添加仓库](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FiHost-Open-Source-Project%2Fhassio-ihost-addon)

## 如何使用
查看“[文档](https://github.com/iHost-Open-Source-Project/hassio-ihost-addon/blob/master/hassio-ihost-matter-bridge-addon/DOCS.md)”以了解如何使用iHost的Matter Bridge插件。


## 支持的实体
- 开关
- 二进制传感器
- 灯光
- 事件 
- 百叶窗 
- 气候控制

### ⚠️ 注意

由于智能家居平台在实现Matter标准方面存在差异，**相同的Matter设备在每个生态系统中可能表现出不同的行为**。这包括但不限于：

1. **调色温白炽灯 - 色温未同步。**
   当调色温白炽灯的色温发生变化时，更新后的值未正确反映在Apple Home应用中。

2. **RGB灯 - 颜色变化未同步。**
   更改RGB灯的颜色后，更新后的颜色未正确同步到Apple Home和Google Home应用。

3. **设备状态未实时更新。**
   在Alexa和Google Home应用中，当设备从其他平台进行控制时，设备状态不会自动更新。您需要手动刷新设备列表或打开设备详情页面以查看当前状态。

4. **灯光亮度百分比偏差。**
   在SmartThings应用中，显示的灯光设备亮度百分比始终比实际亮度水平高约1%。

5. **百叶窗位置百分比跨平台反转。**
   百叶窗打开百分比在不同的平台上被解释不同。例如，在Alexa中显示为30%打开的百叶窗，在Apple Home、SmartThings和Google Home中会显示为70%打开。

6. **设备在SmartThings应用中重新同步后未显示。**
   如果之前同步的设备被移除并稍后重新同步，它可能不会立即在SmartThings应用中显示。需要重启SmartThings Hub来解决这个问题。

![image](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/refs/heads/master/hassio-ihost-matter-bridge-addon/images/support-devices.png)
![image](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/refs/heads/master/hassio-ihost-matter-bridge-addon/images/readme-1.png)
![image](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/refs/heads/master/hassio-ihost-matter-bridge-addon/images/readme-1.png)