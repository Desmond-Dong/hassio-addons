# 家居助手插件：5etools

一套基于浏览器的工具，供D&D 5e的玩家和地下城主使用。从5etools GitHub上发布的图像。没有图像或内容在jdeath的仓库上托管/发布。不提供支持，因为家居助手插件创建者不使用这个。自托管图像可能比5etools网站上的版本落后一个修订版。图像是4 GB，所以安装将需要很长时间，请耐心等待。

_感谢大家给我的仓库点赞！要点赞，请点击下面的图像，然后它将出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个插件使用的是[docker镜像](https://github.com/5etools-mirror-2/5etools-mirror-2.github.io)。

## 安装

这个插件的安装非常简单，与其他任何Hass.io插件的安装方式相同。

1. [将我的Hass.io插件仓库][repository]添加到你的Hass.io实例。
1. 安装这个插件。4 GB的图像将需要一段时间来下载
1. 点击`保存`按钮来存储你的配置。
1. 启动插件。
1. 检查插件的日志，看看是否一切正常。
1. 应该可以通过ingress或<your-ip>:port打开WebUI。

## 配置

```
port : 8080 #你想要运行的端口。
```

Webui可以在`<your-ip>:port`找到。

[repository]: https://github.com/jdeath/homeassistant-addons