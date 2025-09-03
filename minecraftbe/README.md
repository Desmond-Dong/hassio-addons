# Home assistant插件：Minecraft Dedicated Server Bedrock Edition
在Home Assistant上快速运行Minecraft Dedicated Server Bedrock Edition的方法。

_感谢大家给我的仓库加星！要加星，请点击下面的图片，它将出现在右上角。谢谢！_

[![@jdeath/homeassistant-addons仓库的Star贡献者列表](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个插件使用了 [itzg/docker-minecraft-bedrock-server](https://github.com/itzg/docker-minecraft-bedrock-server/) 的docker镜像。

当重新启动插件时，它将自动获取最新版本的Minecraft。

你的世界、设置和服务器可执行文件都存储在 /share/minecraftbe

你可能想要在半夜创建一个服务来重新启动插件，以便更新Minecraft版本（见下文）

如果你想在家助理中监控你的Bedrock服务器，请安装这个集成，因为内置的只监控java: https://github.com/jdeath/Bedrock-Homeassistant

## 安装

这个插件的安装非常简单，与安装任何其他Hass.io插件没有什么不同。

1. 将我的Hass.io插件仓库 [repository] 添加到你的Hass.io实例。
1. 安装这个插件。
2. 如有需要，更改API端口（默认为标准的Minecraft端口）
3. 点击 `保存` 按钮来保存你的配置。
4. 创建目录 /share/minecraftbe
5. 启动插件。
6. 检查插件的日志，看看是否一切顺利。
7. 编辑你想要在 /share/minecraftbe/ 中的任何服务器/权限/白名单属性，并重新启动插件。注意你不能更改 server.properties 中的端口，因为它会被某种原因覆盖。然而，你可以在家助理的插件配置选项卡中更改端口。我只暴露了IP4端口。如果需要IP6，请告诉我。
8. 如果你想外部访问，请确保将你的外部端口转发到你的家助理IP。

## 重启自动化

```
alias: 重启Minecraft服务器
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