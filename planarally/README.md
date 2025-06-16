# 家庭助手插件：PlanarAlly

# PlanarAlly

一个为您进入平面世界时提供的伴随工具。

PlanarAlly 是一个网络工具，它为您的 TTRPG/D&D 工具箱添加了虚拟战斗图和各种附加功能。

一些关键特性包括：

**自我托管**：您可以在任何您喜欢的地方运行此软件，而无需依赖外部服务\
**离线支持**：该工具可以在完全离线的设置中使用，以便您在黑暗的地下城中进行 D&D 游戏。

**简单的图层**：以图层组织您的场景，以便于管理。\
**无限画布**：当有限的工作空间仍然不够时！\
**动态照明**：通过使用光影来增强您的沉浸感。\
**玩家视野**：限制视野范围仅限于您的令牌可以看到的部分。您的同伴在另一个房间，没有光线给您！\
**先攻记录器**：简单的先攻记录器\
**楼层！**：在阳台上时可以俯瞰下方的楼层！

此工具免费提供使用，并且是开源的。

_感谢每一个为我的仓库点星的人！要点星请点击下面的图片，然后它将出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此插件使用 [docker 镜像](https://github.com/Kruptein/PlanarAlly)。

## 安装

此插件的安装需要一些额外步骤。

1. [将我的 Hass.io 插件仓库][repository] 添加到您的 Hass.io 实例。
1. 点击 `保存` 按钮以存储您的配置。
1. 启动插件。
1. 它会失败，这没关系。
1. 设置将在 `/addon_configs/2effc9b9_plannarally` 中。
1. 通过 ssh 登录到 homeassistant，输入 `chmod 2777 addon_configs/2effc9b9_plannarally`
2. 启动插件，它将启动，但随后停止该插件。
1. 编辑 `/addon_configs/2effc9b9_plannarally/server_config.cfg`
1. 在 `[General]` 下添加以下两行：

```
save_file = /config/planar.sqlite
assets_directory = /config/assets
```
1. 重启插件
1. 打开 WebUI，应该可以通过 <your-ip>:port 访问。

## 配置

```
port : 8080 # 您希望运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons