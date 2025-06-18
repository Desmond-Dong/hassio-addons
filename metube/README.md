# Home assistant add-on: MeTube

为 youtube-dl （使用 yt-dlp 分支）提供的 Web GUI，支持播放列表。允许您从 YouTube 和其他几十个网站下载视频（https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md）。

_感谢所有给我的仓库点星的人！要点星，请点击下面的图片，然后它将出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个插件基于 [docker image](https://github.com/alexta69/metube)。

## 安装

这个插件的安装非常简单，和安装其他任何 Hass.io 插件没有什么不同。

1. [将我的 Hass.io 插件仓库][repository]添加到您的 Hass.io 实例中。
1. 安装此插件。
1. 点击 `Save` 按钮以保存您的配置。
1. 下载目录默认为 /share/metube，可以更改为 share 中的任何内容。
1. 启动插件。
1. 检查插件的日志以查看一切是否正常。
1. 可以通过 ingress 或 <your-ip>:port 打开 WebUI。

## 配置

```
port : 8081 # 您想要运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons