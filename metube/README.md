# Home assistant插件：MeTube

youtube-dl（使用yt-dlp分支）的Web GUI，支持播放列表。允许您从YouTube和其他几十个网站下载视频（https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md）。

_感谢大家给我的仓库加星！要加星，请点击下面的图片，它就会出现在右上角。谢谢！_

[![@jdeath/homeassistant-addons仓库的Star贡献者名单](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个插件基于[docker镜像](https://github.com/alexta69/metube)。

## 安装

这个插件的安装非常简单，与安装任何其他Hass.io插件没有区别。

1. [将我的Hass.io插件仓库][repository]添加到您的Hass.io实例。
1. 安装这个插件。
1. 点击`保存`按钮以保存您的配置。
1. 下载目录默认为/share/metube，可以在share中更改为任何内容。
1. 启动插件。
1. 检查插件的日志以查看是否一切顺利。
1. WebUI应该可以通过ingress或<your-ip>:port访问。

## 配置

```
port : 8081 #您想要运行的端口。
```

Webui可以在`<your-ip>:port`找到。

[repository]: https://github.com/jdeath/homeassistant-addons