# 家庭助理插件：PlanarAlly

# PlanarAlly

一个在你进入平面时的伴侣工具。

PlanarAlly 是一个网页工具，能够为你的 TTRPG/D&D 工具箱添加虚拟战斗地图以及各种额外功能。

一些关键功能包括：

**自我托管**：你可以在任何地方运行这个软件，而不必依赖外部服务\
**离线支持**：这个工具可以在完全离线的环境中使用，适合在黑暗的地牢中玩 D&D。

**简单的图层**：将你的场景组织在图层中，以便于管理。\
**无限画布**：当有限的工作空间仍然不够时！\
**动态照明**：通过光与影的配合提高沉浸感。\
**玩家视野**：限制视野到你的棋子能看到的范围。如果你的同伴在另一个房间，光线对你无效！\
**先手追踪器**：简单的先手追踪器\
**楼层！**：站在阳台上时，可以俯视下层楼！

这个工具是免费使用的，并且是开源的。

_感谢所有为我的仓库点赞的人！要为它点赞，请点击下面的图片，然后它会出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个插件使用 [docker 镜像](https://github.com/Kruptein/PlanarAlly)。

## 安装

安装这个附加组件需要几个额外的步骤。

1. [将我的 Hass.io 插件仓库][repository] 添加到你的 Hass.io 实例。
1. 点击 `保存` 按钮以保存你的配置。
1. 启动插件。
1. 它会失败，没关系。
1. 设置将位于 `/addon_configs/2effc9b9_plannarally`
1. ssh 登录到 homeassistant，输入 `chmod 2777 addon_configs/2effc9b9_plannarally`
2. 启动插件，它会启动，但随后会停止插件。
1. 编辑 `/addon_configs/2effc9b9_plannarally/server_config.cfg`
1. 在 `[General]` 下添加以下两行：

```
save_file = /config/planar.sqlite
assets_directory = /config/assets
```
1. 重启插件。
1. 打开 WebUI，应该可以通过 <your-ip>:port 访问。

## 配置

```
port : 8080 #你希望运行的端口。
```

WebUI 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons