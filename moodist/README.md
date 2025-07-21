# Home assistant插件：Moodist

专注和放松的背景声音。

_感谢大家给我的仓库加星！要加星，请点击下面的图片，它将会出现在右上角。谢谢！_

[![@jdeath/homeassistant-addons 仓库的Star列表](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个插件基于 [docker镜像](https://github.com/remvze/moodist)。

## 安装

这个插件的安装非常简单，与安装任何其他Hass.io插件的方式相同。

1. [将我的Hass.io插件仓库][repository]添加到你的Hass.io实例。
1. 安装这个插件。
1. 点击`保存`按钮来存储你的配置。
1. 启动插件。
1. 检查插件的日志，看看是否一切正常。
1. WebUI应该可以通过ingress或<your-ip>:port来访问。

## 配置

```
port : 8081 #你想要运行的端口。
```

Webui可以在`<your-ip>:port`找到。

[repository]: https://github.com/jdeath/homeassistant-addons