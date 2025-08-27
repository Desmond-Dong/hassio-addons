# Home assistant插件：mqqtui

MQTT Web界面是一个开源的Web应用程序，它提供了MQTT（消息队列遥测传输）消息流的实时可视化。它允许用户通过直观的Web界面监控MQTT主题、发布消息和查看消息统计信息。

_感谢大家给我的仓库点赞！要点赞请点击下面的图片，它将会出现在右上角。谢谢！_

[![@jdeath/homeassistant-addons仓库的Stargazers列表](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个插件基于[docker镜像](https://github.com/terdia/mqttui)。

## 安装

这个插件的安装非常简单，与安装任何其他Hass.io插件的方式相同。

1. [将我的Hass.io插件仓库][repository]添加到你的Hass.io实例。
1. 安装这个插件。
1. 点击`保存`按钮来存储你的配置。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 应该可以通过<你的IP>:端口访问WebUI。

## 配置

```
port : 5000 #你想运行的端口。
```

Webui可以在<你的IP>:端口找到。

[repository]: https://github.com/jdeath/homeassistant-addons