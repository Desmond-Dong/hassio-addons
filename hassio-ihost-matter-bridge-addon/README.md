# Matter Bridge for iHost

![Supports armv7 Architecture](https://img.shields.io/badge/armv7-yes-green.svg)

## 关于

Matter Bridge for iHost 插件将 Home Assistant 设备的实体暴露为 Matter 兼容设备，使其能够与 Matter 平台集成，例如 Apple Home、Google Home 和 Amazon Alexa。
此插件基于 iHost Matter Bridge，并已通过 Matter 认证，以确保协议兼容性和长期可用性。

同时，它与网页和移动终端兼容。

## 前提条件

- Matter Bridge 插件仅适用于 HA over iHost 项目，允许用户将 Home Assistant 设备暴露为 Matter 设备，并同步到受支持的 Matter 平台进行控制。
- Home Assistant OS 版本必须为 15.2.1 或更高版本。

## 安装
1. 前往插件商店 → 点击右上角的 **更多** 按钮（⋮） → 选择 **仓库**  
2. 粘贴以下 URL：  
   [https://github.com/iHost-Open-Source-Project/hassio-ihost-addon](https://github.com/iHost-Open-Source-Project/hassio-ihost-addon)  
3. 或者，直接点击下方按钮自动添加：

[![Add Repository](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FiHost-Open-Source-Project%2Fhassio-ihost-addon)

## 如何使用
查看 “[文档](https://github.com/iHost-Open-Source-Project/hassio-ihost-addon/blob/master/hassio-ihost-matter-bridge-addon/DOCS.md)” 了解如何使用 SONOFF Dongle Flasher For iHost 插件的详细信息。


## 支持的实体
- 开关
- 二进制传感器
- 灯光
- 事件 
- 百叶窗 
- 气候控制

### ⚠️ 注意事项

由于智能家居平台在实现 Matter 标准时存在差异，**相同的 Matter 设备在不同的生态系统中可能会表现出不同的行为**。这包括但不限于：

1. **可调白炽灯 - 色温未同步。**
   当可调白炽灯的色温发生变化时，更新后的值未能正确反映在 Apple Home 应用中。

2. **RGB 灯 - 颜色变化未同步。**
   更改 RGB 灯的颜色后，更新后的颜色未能正确同步到 Apple Home 和 Google Home 应用。

3. **设备状态未实时更新。**
   在 Alexa 和 Google Home 应用中，当从其他平台控制设备时，设备状态不会自动更新。您需要手动刷新设备列表或打开设备详情页面以查看当前状态。

4. **灯光亮度百分比偏差。**
   在 SmartThings 应用中，显示的灯光设备亮度百分比始终比实际亮度水平高约 1%。

5. **百叶窗位置百分比跨平台反转。**
   百叶窗开百分比在不同的平台上解释不同。例如，在 Alexa 中显示为 30% 开的百叶窗，在 Apple Home、SmartThings 和 Google Home 中会显示为 70% 开。

6. **设备在 SmartThings 应用中重新同步后未显示。**
   如果已同步的设备被移除并重新同步，它可能不会立即在 SmartThings 应用中显示。需要重启 SmartThings Hub 才能解决此问题。

![image](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/refs/heads/master/hassio-ihost-matter-bridge-addon/images/support-devices.png)
![image](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/refs/heads/master/hassio-ihost-matter-bridge-addon/images/readme-1.png)
![image](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/refs/heads/master/hassio-ihost-matter-bridge-addon/images/readme-1.png)