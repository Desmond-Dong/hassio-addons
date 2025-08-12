# Home assistant add-on: CommaFeed

一个受Google Reader启发的自托管RSS阅读器，基于Quarkus和React/TypeScript。

_感谢所有给我的仓库加星的人！要加星，请点击下面的图片，它将出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个add-on使用的是[docker镜像](https://github.com/Athou/commafeed/)。

## 安装

这个add-on的安装过程非常简单，与安装任何其他Hass.io add-on没有区别。

1. [将我的Hass.io add-ons仓库][repository]添加到你的Hass.io实例。
1. 点击`保存`按钮以保存你的配置。
1. 启动add-on。
1. 检查add-on的日志以查看是否一切顺利。
1. 应该可以通过<你的IP>:端口和ingress来打开WebUI。默认用户名:密码是admin:admin
1. 设置将在 /addon_configs/2effc9b9_commafeed 中

## 配置

```
port : 8082 #你想要运行的端口。
```

Webui可以在 `<你的IP>:端口` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons