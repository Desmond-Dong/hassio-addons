# Home assistant add-on: 5etools

一套基于浏览器的工具，供D&D 5e的玩家和DM使用。下载的图像来自5etools GitHub。没有图像或内容托管/发布在jdeath的库中。由于Home Assistant插件创建者不使用此内容，因此不提供支持。自托管的图像可能比5etools网站落后一个版本。图像大小为4 GB，因此安装将花费较长时间，请耐心等待。

_感谢所有赞助我的库的人！要赞助，请点击下面的图像，然后它将在右上角显示。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此附加组件使用[docker镜像](https://github.com/5etools-mirror-2/5etools-mirror-2.github.io)。

## 安装

此附加组件的安装非常简单，与安装其他Hass.io附加组件并无不同。

1. [将我的Hass.io附加组件库][repository]添加到您的Hass.io实例。
1. 安装此附加组件。下载4 GB的图像将花费一些时间。
1. 单击`保存`按钮以保存您的配置。
1. 启动附加组件。
1. 检查附加组件的日志以查看一切是否正常。
1. WebUI应通过ingress或<your-ip>:port访问。

## 配置

```
port : 8080 #您希望运行的端口。
```

Webui可以通过`<your-ip>:port`找到。

[repository]: https://github.com/jdeath/homeassistant-addons