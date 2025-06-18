# Home assistant 添加组件: ytptube

用于 yt-dlp 的 Web GUI，支持播放列表和频道 (https://github.com/arabcoders/ytptube)。

_感谢所有给我的仓库加星的人！想要加星，请点击下面的图片，然后在右上角即可看到。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此插件基于 [docker 镜像](https://github.com/arabcoders/ytptube)。

# YTPTube 特性

* 支持多重下载。
* 随机美丽背景。`可以禁用或更改源`。
* 可以处理直播。
* 调度器可以在指定时间自动排队下载频道或播放列表。
* 根据选定事件向目标发送通知。
* 支持每个链接 `cli 选项` 和 `cookies`。
* 用逗号分隔的多个 URL 队列。
* 预设系统以重用常用的 yt-dlp 选项。
* 简单的文件浏览器。`默认禁用`。
* 内置视频播放器 **支持附带的外部字幕**。
* 新的 `POST /api/history` 端点，允许同时发送一个或多个链接。
* 新的 `GET /api/history/add?url=http://..` 端点，允许通过 GET 请求添加单个项目。
* 现代前端用户界面。
* 使用 SQLite 作为数据库后端。
* 支持基本身份验证。
* 支持 curl_cffi，见 [yt-dlp 文档](https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#impersonation)。
* 为非技术用户提供基本模式的 WebUI，隐藏大部分普通功能。
* 容器中捆绑的工具：curl-cffi, ffmpeg, ffprobe, aria2, rtmpdump, mkvtoolsnix, mp4box。
* 自动重新排队即将到来的直播。
* 根据自定义定义的条件应用 `yt-dlp` 选项。
* 自定义浏览器扩展、书签和 iOS 快捷方式，以将链接发送到 YTPTube 实例。

## 安装

此插件的安装有一些额外步骤。

1. [将我的 Hass.io 附加组件仓库][repository]添加到您的 Hass.io 实例中。
1. 安装此插件。
1. 点击 `保存` 按钮以存储您的配置。
1. 下载目录默认设置为 /share/ytptube，可以更改为共享中的任何内容。
1. 启动插件。它将失败。
1. ssh 进入家庭助理并输入 `chown hassio /addon_configs/2effc9b9_ytptube`。
1. 启动插件。它将失败。
1. 再次 ssh 进入家庭助理并输入 `chown hassio /share/ytptube` 或者如果您更改了下载目录则输入相应的目录。
1. 启动插件。
1. 检查插件的日志以确认一切是否正常。
1. 通过 <your-ip>:port 打开 WebUI。Ingress 不起作用。

## 配置

```
port : 8081 #您希望运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons