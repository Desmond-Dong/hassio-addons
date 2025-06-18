# Home assistant 插件：Livebook

Livebook 是一个用于编写互动和协作代码笔记本的 Web 应用程序

_感谢所有为我的仓库点亮星星的人！要点亮星星，请点击下面的图片，然后它将位于右上角。谢谢！_

[![为 @jdeath/homeassistant-addons 点亮星星的用户列表](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此插件使用 [docker 镜像](https://github.com/livebook-dev/livebook)。

## 安装

这个插件的安装非常简单，与安装其他任何 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件库][repository] 添加到你的 Hass.io 实例。
1. 点击 `保存` 按钮以保存你的配置。
1. 启动插件。
1. 检查插件的日志以查看是否一切顺利。
1. 打开 WebUI 应该可以通过 <你的-ip>:端口 访问。
1. 数据将在 /addon_configs/2effc9b9_livebook 中。

## 配置

```
port : 8080 #你想要运行的端口。
```

Webui 可以在 `<你的-ip>:端口` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons