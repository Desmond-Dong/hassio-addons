# Home assistant 插件：tasmocompiler
 TasmoCompiler 是一个简单的网页 GUI，允许您使用自己的设置编译出色的 Tasmota 固件
   
_感谢所有给我的仓库加星的人！要加星请点击下面的图片，然后它将出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个插件基于 [docker 镜像](https://hub.docker.com/r/benzino77/tasmocompiler) 

## 安装

这个插件的安装非常简单，与安装任何其他 Hass.io 插件并无不同。

1. [将我的 Hass.io 插件库][repository] 添加到您的 Hass.io 实例中。
1. 安装这个插件。
1. 点击 `保存` 按钮以保存您的配置。
1. 启动插件。
1. 检查插件的日志以查看一切是否顺利。
1. 进入本地 IP:port。由于某种原因，Ingress 不可用。
1. 查阅官方文档以获取设置支持：https://github.com/benzino77/tasmocompiler
## 配置

```
port: 3000 # 您想要运行前端的端口
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons