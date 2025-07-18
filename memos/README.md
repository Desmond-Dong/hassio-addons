# Home assistant add-on: Memos

一个注重隐私的轻量级笔记服务。轻松捕捉和分享你的精彩想法。

从 Docker 镜像运行：https://github.com/usememos/memos


_感谢大家给我的仓库加星！要加星请点击下面的图片，然后它就会出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)


## 安装

这个 add-on 的安装过程非常简单，与其他任何 Hass.io add-on 的安装方式相同。

1. [将我的 Hass.io add-ons 仓库][repository]添加到你的 Hass.io 实例。
1. 安装这个 add-on。
1. 点击 `保存` 按钮来存储你的配置。
1. 启动 add-on。
1. 检查 add-on 的日志，看看是否一切顺利。
1. 应该可以通过 ingress 或 <your-ip>:port 打开 WebUI。
1. 设置将被保存在 /addons-config/2effc9b9_memos

## 配置

```
port : 5230 #你想要运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons