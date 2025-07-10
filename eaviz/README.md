# EZVIZ云信令插件用于Home Assistant

## 概述

此插件使您能够在Home Assistant生态系统中集成EZVIZ云信令。它提供了一个自托管的开源解决方案，确保安全和可定制的通信。

## 主要特点

- EZVIZ云信令服务端
- 支持多种架构：amd64、armhf、armv7、aarch64、i386
- 提供简化的配置选项
- 自动会将实体添加到MQTT集成里

## 安装步骤

1. 访问Home Assistant插件商店
2. 点击右上角的三个点，选择“仓库”
3. 添加以下URL：`https://github.com/Desmond-Dong/hassio-addons`
4. 在列表中找到“EZVIZ云信号接收器”插件并点击“安装”

## 配置详情
需要将内网端口映射到公网。由于萤石后台不支持IPv6，因此需要使用IPv4地址。

1. 请访问 [https://open.ys7.com/](https://open.ys7.com/) 注册一个开发者帐号。
2. 绑定您的设备，访问 [设备绑定页面](https://open.ys7.com/console/device.html)。
3. 在 webhook 中添加您的地址，访问 [消息推送设置](https://open.ys7.com/console/messagePush.html)。



## 📱 关注我

扫描下面二维码，关注我。有需要可以随时给我留言：

<img src="https://gitee.com/desmond_GT/hassio-addons/raw/main/WeChat_QRCode.png" width="50%" /> 📲

## ☕ 赞助支持

如果您觉得我花费大量时间维护这个库对您有帮助，欢迎请我喝杯奶茶，您的支持将是我持续改进的动力！

<div style="display: flex; justify-content: space-between;">
  <img src="https://gitee.com/desmond_GT/hassio-addons/raw/main/1_readme/Ali_Pay.jpg" height="350px" />
  <img src="https://gitee.com/desmond_GT/hassio-addons/raw/main/1_readme/WeChat_Pay.jpg" height="350px" />
</div> 💖

感谢您的支持与鼓励！