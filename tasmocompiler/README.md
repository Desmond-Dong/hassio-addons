# Home assistant 插件：tasmocompiler
 TasmoCompiler 是一个简单的网页 GUI，允许您使用自己的设置编译出出色的 Tasmota 固件。

_感谢所有关注我仓库的朋友！要关注它，请点击下面的图片，然后它将出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

该插件基于 [docker 镜像](https://hub.docker.com/r/benzino77/tasmocompiler)。

## 安装

此插件的安装非常简单，并与安装任何其他 Hass.io 插件没有不同。

1. [将我的 Hass.io 插件仓库][repository] 添加到您的 Hass.io 实例。
1. 安装此插件。
1. 点击 `保存` 按钮以存储您的配置。
1. 启动插件。
1. 检查插件的日志以查看一切是否正常。
1. 转到本地 IP:端口。由于某种原因，Ingress 不可用。
1. 参考官方文档以获取设置支持： https://github.com/benzino77/tasmocompiler
## 配置

```
port: 3000 # 希望运行前端的端口
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons