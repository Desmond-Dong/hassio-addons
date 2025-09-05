# Home assistant add-on: Livebook

Livebook 是一个用于编写交互式和协作式代码笔记本的 Web 应用程序

_感谢大家给我的仓库点赞！要点赞，请点击下面的图片，它将会出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个 add-on 使用了 [docker 镜像](https://github.com/livebook-dev/livebook)。

## 安装

这个 add-on 的安装非常简单，与安装任何其他 Hass.io add-on 没有区别。

1. [将我的 Hass.io add-ons 仓库][repository] 添加到你的 Hass.io 实例中。
1. 点击 `Save` 按钮来保存你的配置。
1. 启动 add-on。
1. 检查 add-on 的日志，看看是否一切顺利。
1. 应该可以通过 <your-ip>:port 来打开 WebUI。
1. 数据将在 /addon_configs/2effc9b9_livebook 中。

## 配置

```
port : 8080 # 你想要运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons