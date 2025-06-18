# Home assistant 插件：5etools

一套基于浏览器的工具，供 D&D 5e 的玩家和 DM 使用。下载会从 5etools GitHub 上传图片。没有任何图片或内容托管/发布在 jdeath 的仓库中。不提供支持，因为 Home Assistant 插件创建者并不使用这个。自托管的图片可能会比 5etools 网站的版本滞后一个版本。图片大小为 4 GB，因此安装需要较长时间，请耐心等待。

_感谢所有关注我仓库的人！要关注它，请点击下面的图片，然后它将出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

该插件使用了 [docker 镜像](https://github.com/5etools-mirror-2/5etools-mirror-2.github.io)。

## 安装

安装此插件非常简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件仓库][repository] 添加到您的 Hass.io 实例中。
1. 安装此插件。4 GB 的镜像将需要一段时间才能下载。
1. 点击 `保存` 按钮以存储您的配置。
1. 启动该插件。
1. 检查插件的日志，查看是否一切正常。
1. WebUI 应该可以通过 ingress 或 <your-ip>:port 访问。

## 配置

```
port : 8080 #您要运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons