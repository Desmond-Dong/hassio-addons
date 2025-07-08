# iHost 的 Matter Bridge

## 简介

iHost 的 Matter Bridge 插件将 Home Assistant 设备的实体暴露为 Matter 兼容设备，使其能够与 Matter 平台（如 Apple Home、Google Home 和 Amazon Alexa）集成。  
该插件基于 iHost Matter Bridge，并已通过 Matter 认证，以确保协议兼容性和长期可用性。

同时，它兼容网页和移动终端。

## 前置条件

**iHost 的 Matter Bridge 插件** 仅设计用于 **HA over iHost** 项目，允许用户将 Home Assistant 设备的实体暴露为 Matter 设备，并同步到受支持的 Matter 平台进行控制。

因此，该插件仅在 Home Assistant 在 iHost 上运行时才有效。了解 [<u>如何在 iHost 上运行 Home Assistant 操作系统？</u>](https://github.com/iHost-Open-Source-Project/ha-operating-system?tab=readme-ov-file#readme)

## 如何安装 Matter Bridge 插件？

### 将 Matter Bridge 插件添加到仓库

如果您已经从该仓库添加了插件（例如，iHost 硬件控制），则可以跳过此步骤，直接前往插件商店安装所需的插件。

#### 通过 URL

-   导航到 **设置 > 插件商店 > 点击右上角的三点菜单（⋮）并选择仓库**。
-   将仓库 URL 输入到输入框中： [<u>https://github.com/iHost-Open-Source-Project/hassio-ihost-addon</u>](https://github.com/iHost-Open-Source-Project/hassio-ihost-addon)

#### 通过按钮点击

-   点击此按钮 [![添加仓库](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FiHost-Open-Source-Project%2Fhassio-ihost-addon) 自动添加插件。

### 安装 Matter Bridge 插件

1.  在插件商店中搜索 **Matter Bridge**。

![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-matter-bridge-addon/images/search.png)

2.  点击 **安装**。

![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-matter-bridge-addon/images/install.png)

3.  等待安装完成。

## 启动 Matter Bridge 插件

安装后，点击 **启动** 以启动插件。等待服务完全启动后再继续。

![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-matter-bridge-addon/images/start-addon.png)

## 使用 Matter Bridge 插件将 Home Assistant 设备同步到 Matter Fabric

1.  点击 **打开 WEB UI** 以访问 Matter Bridge 配对页面。  
    点击 **开始** 查看 Matter Bridge 配对的准备工作。  
    ![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-matter-bridge-addon/images/start-1.png)  
    ![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-matter-bridge-addon/images/start-2.png)  
    ![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-matter-bridge-addon/images/start-3.png)
2.  按照说明将 Home Assistant 添加为 Matter Bridge 并将其设备同步到连接的 Matter Fabric。

-   点击 **开始配对**。
-   使用任何 Matter 兼容平台的 App 扫描 **QR 码** 或输入 **数字设置码** 来配对 Matter Bridge，包括：
    -   Apple Home App
    -   Amazon Alexa App
    -   Google Home App
    -   Samsung SmartThings
-   **前往设备列表** 并 **选择您要同步到 Matter 平台的实体**，包括：
    -   开关
    -   二进制传感器
    -   灯光
    -   事件
    -   百叶窗
    -   气候控制

### ⚠️ 注意

由于智能家庭平台在实现 Matter 标准时存在差异，**相同的 Matter 设备在各个生态系统中可能表现不同**。这包括但不限于：

1. **可调白炽灯 - 色温未同步。**
   当可调白炽灯的色温发生变化时，更新后的值未正确反映在 Apple Home App 中。

2. **RGB 灯 - 颜色变化未同步。**
   更改 RGB 灯的颜色后，更新后的颜色未正确同步到 Apple Home 和 Google Home App。

3. **设备状态未实时更新。**
   在 Alexa 和 Google Home App 中，当设备从其他平台进行控制时，设备状态不会自动更新。您需要手动刷新设备列表或打开设备详情页面以查看当前状态。

4. **灯光亮度百分比偏差。**
   在 SmartThings App 中，显示的灯光设备亮度百分比始终比实际亮度高约 1%。

5. **窗帘位置百分比跨平台反转。**
   窗帘开启百分比在不同的平台上解释不同。例如，在 Alexa 中显示为 30% 开启的窗帘，在 Apple Home、SmartThings 和 Google Home 中将显示为 70% 开启。

6. **设备在 SmartThings App 中重新同步后未显示。**
   如果已同步的设备被移除并稍后重新同步，它可能无法立即在 SmartThings App 中显示。需要重启 SmartThings Hub 才能解决此问题。


![image](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/refs/heads/master/hassio-ihost-matter-bridge-addon/images/support-devices.png)

![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-matter-bridge-addon/images/qr-code.png)  
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-matter-bridge-addon/images/add-success.png)

## 管理已连接的 Fabric

配对 Matter Bridge 后，所有已连接的 Matter Fabric 都将显示在配对页面上。

-   点击以 **移除** 访问您的 Matter Bridge 及其桥接设备的已连接 Matter Fabric。
-   右侧点击 **全部移除** 可以移除所有已连接的 Matter Fabric。

![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-matter-bridge-addon/images/remove-all.png)
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-matter-bridge-addon/images/remove-all-confirm.png)

## **<font style="color:#000000;">管理需要同步到 Matter 平台的实体</font>**

点击右上角的 **设备列表** 以访问支持和不支持的 Home Assistant 设备列表，用于同步到 Matter Fabric。  

-   点击 **支持设备** 列表旁边的 **编辑**
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-matter-bridge-addon/images/device-list-1.png)  


-   选择您要同步的实体，或取消选中以从已连接的 Matter Fabric 中移除。
-   点击 **保存**。
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-matter-bridge-addon/images/device-list-2.png)  
![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-matter-bridge-addon/images/device-list-3.png)