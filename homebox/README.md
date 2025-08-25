# Home assistant add-on: Homebox

Homebox 是为家庭用户构建的库存和组织系统！它注重简单易用，是您家庭库存、组织和管理的完美解决方案。在开发这个项目时，我尽量遵循以下原则：

- _简单_ - Homebox 设计得简单易用。无需复杂的设置或配置。使用单个 Docker 容器，或者通过为您的选择平台编译二进制文件自行部署。
- _飞快_ - Homebox 是用 Go 编写的，这使得它非常快速，并且部署所需的资源极少。通常，整个容器的空闲内存使用量不到 50MB。
- _便携_ - Homebox 设计得便携，可以在任何地方运行。我们使用 SQLite 和嵌入式 Web UI，使其易于部署、使用和备份。

_感谢所有星标我的仓库的人！要星标它，请点击下面的图片，它将出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个插件使用了 [docker 镜像](https://github.com/sysadminsmedia/homebox)。

## 安装

这个插件的安装非常直接，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件仓库][repository]添加到您的 Hass.io 实例。
1. 安装这个插件。
1. 点击 `保存` 按钮以保存您的配置。
1. 启动插件。
1. 检查插件的日志，看看是否一切正常。
1. 通过 ingress 或 <your-ip>:port 应该可以打开 WebUI。
1. 注册一个用户
1. 转到插件配置并禁用用户注册，如果您希望这样做

## 配置

```
port : 7745 #您想要运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons