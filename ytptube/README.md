# Home Assistant插件：ytptube

用于yt-dlp的Web GUI，支持播放列表和频道（https://github.com/arabcoders/ytptube）。

_感谢所有给我的仓库加星的人！要加星，请点击下面的图片，然后它会在右上角显示。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

该插件基于[docker镜像](https://github.com/arabcoders/ytptube)。

# YTPTube功能

* 支持多项下载。
* 随机美丽背景。`可以禁用或更改来源`。
* 可以处理直播。
* 定时器可自动排队下载频道或播放列表，在指定时间下载。
* 根据选定事件向目标发送通知。
* 支持每个链接的 `cli选项` & `cookies`。
* 用逗号分隔的多个URL的队列。
* 预设系统以重用常用的yt-dlp选项。
* 简单的文件浏览器。`默认禁用`。
* 内置视频播放器**支持外部字幕的边车**。
* 新的`POST /api/history`端点允许一次发送一个或多个链接。
* 新的`GET /api/history/add?url=http://..`端点允许通过GET请求添加单个项目。
* 现代前端用户界面。
* 使用SQLite作为数据库后端。
* 支持基本身份验证。
* 支持curl_cffi，见[yt-dlp文档](https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#impersonation)
* 对于非技术用户，WebUI的基本模式隐藏了大多数正常功能。
* 容器中捆绑的工具：curl-cffi，ffmpeg，ffprobe，aria2，rtmpdump，mkvtoolnix，mp4box。
* 自动即将开始的直播重新排队。
* 根据自定义定义的条件应用`yt-dlp`选项。
* 自定义浏览器扩展，书签和iOS快捷方式，将链接发送到YTPTube实例。

## 安装

该插件的安装有一些额外步骤。

1. [将我的Hass.io插件仓库][repository]添加到您的Hass.io实例中。
1. 安装该插件。
1. 点击`保存`按钮以存储您的配置。
1. 下载目录默认为/share/ytptube，可以更改为share中的任何位置。
1. 启动该插件。它会失败。
1. ssh进入Home Assistant，输入`chown hassio /addon_configs/2effc9b9_ytptube`。
1. 启动该插件。它会失败。
1. 再次ssh进入Home Assistant，输入`chown hassio /share/ytptube`或您更改过的下载目录。
1. 启动该插件。
1. 检查插件的日志以查看一切是否顺利。
1. 通过<your-ip>:port打开WebUI。Ingress无法工作。

## 配置

```
port : 8081 #您希望运行的端口。
```

Webui可以在`<your-ip>:port`找到。

[repository]: https://github.com/jdeath/homeassistant-addons