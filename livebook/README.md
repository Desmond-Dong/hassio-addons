# 家庭助理插件：Livebook

Livebook 是一个用于编写交互式和协作式代码笔记本的 web 应用程序

_感谢每一个给我的仓库点星的人！要点星，请点击下面的图片，然后它会出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

该插件使用 [docker 镜像](https://github.com/livebook-dev/livebook)。

## 安装

这个插件的安装非常简单，与安装其他任何 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件仓库][repository] 添加到您的 Hass.io 实例。
1. 点击 `保存` 按钮以存储您的配置。
1. 启动该插件。
1. 检查插件的日志以查看一切是否顺利。
1. WebUI 应该可以通过 <your-ip>:port 访问。
1. 数据将存储在 /addon_configs/2effc9b9_livebook 中。
## 配置

```
port : 8080 #您希望运行的端口。
```

WebUI 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons