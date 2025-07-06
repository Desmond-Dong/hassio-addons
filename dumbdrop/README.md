# 家居助手插件：Dumb Drop

一个愚蠢简单的文件上传应用程序，提供了一个干净、现代的界面，用于拖放文件。使用 Node.js 和纯 JavaScript 构建。

_感谢所有将我的仓库标为星标的人！要标星，请点击下面的图片，它将出现在右上角。谢谢！_

[![@jdeath/homeassistant-addons 的标星者仓库列表](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此插件使用 [DumbWareio 的 Docker 镜像](https://github.com/DumbWareio/DumbDrop)。

## 安装

此插件的安装非常简单，与安装任何其他 Hass.io 插件没有区别。

1. 将我的 Hass.io 插件仓库 [添加到您的 Hass.io 实例](https://github.com/jdeath/homeassistant-addons)。
1. 点击 `保存` 按钮以保存您的配置。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 应该可以通过 <your-ip>:port 和 ingress 打开 WebUI。默认用户名:密码是 admin:admin
1. 文件将上传到您的智能家居在 /media/dumbdrop/。

## 配置

```
port : 8082 #您想要运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons