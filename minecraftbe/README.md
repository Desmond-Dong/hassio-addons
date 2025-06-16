# Home assistant 插件：Minecraft 专用服务器 基岩版
在 Home Assistant 上运行 Minecraft 专用服务器基岩版的快速方法。

_感谢所有给我的仓库点星的人！要点星，请点击下面的图片，然后它将显示在右上方。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此插件使用 [itzg/docker-minecraft-bedrock-server](https://github.com/itzg/docker-minecraft-bedrock-server/) docker 镜像。

重启插件时，它会自动获取最新版本的 Minecraft。

你的世界、设置和服务器可执行文件存储在 /share/minecraftbe 中。

你可能想创建一个服务，在半夜重启插件，以更新 Minecraft 版本（见下文）。

如果你想在 Home Assistant 中监控你的基岩服务器，请安装此集成，因为内置的集成仅监控 Java：https://github.com/jdeath/Bedrock-Homeassistant

## 安装

此插件的安装非常简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件库][repository] 添加到你的 Hass.io 实例。
1. 安装此插件。
2. 如果需要，修改 API 端口（默认为标准 Minecraft 端口）。
3. 点击 `Save` 按钮以保存你的配置。
4. 创建目录 /share/minecraftbe。
5. 启动插件。
6. 检查插件的日志以查看一切是否正常。
7. 在 /share/minecraftbe/ 中编辑你想要的任何 server/permissions/whitelist 属性，然后重启插件。请注意，不能在 server.properties 中修改端口，因为它会因为某种原因被覆盖。不过，你可以在 Home Assistant 的插件配置选项卡中更改端口。我只暴露了 IPV4 端口。如果需要 IPV6，请告诉我。
8. 如果你想要外部访问，请确保将外部端口转发到你的 Home Assistant IP。

## 重启自动化

```
alias: 重启 Minecraft 服务器
description: ""
trigger:
  - platform: time
    at: "02:00:00"
condition:
  - condition: time
    before: "00:00:00"
    weekday:
      - mon
      - wed
      - fri
    after: "00:00:00"
action:
  - service: hassio.addon_restart
    data:
      addon: 2effc9b9-minecraftbe
mode: single
```
[repository]: https://github.com/jdeath/homeassistant-addons