# 家庭助理插件：ytptube

用于 yt-dlp 的 Web GUI，支持播放列表和频道 (https://github.com/arabcoders/ytptube)。

_感谢所有给我仓库点星的人！要点星，请点击下面的图片，然后它会在右上角显示。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此插件基于 [docker 镜像](https://github.com/arabcoders/ytptube)。

# YTPTube 功能。

* 支持多重下载。
* 随机美丽背景。`可以禁用或更换源`。
* 可以处理直播。
* 调度程序可以在指定时间自动排队下载频道或播放列表。
* 根据选定事件向目标发送通知。
* 支持每个链接的 `cli 选项` 和 `cookies`。
* 通过逗号分隔的多个 URL 排队。
* 预设系统以重用常用的 yt-dlp 选项。
* 简单的文件浏览器。`默认禁用`。
* 内置视频播放器**支持外部字幕的侧车**。
* 新的 `POST /api/history` 端点允许同时发送一个或多个链接。
* 新的 `GET /api/history/add?url=http://..` 端点允许通过 GET 请求添加单个项目。
* 现代前端 UI。
* SQLite 作为数据库后端。
* 支持基本身份验证。
* 支持 curl_cffi，详见 [yt-dlp 文档](https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#impersonation)。
* 为非技术用户提供基本模式的 WebUI，隐藏大多数正常功能。
* 容器中捆绑的工具：curl-cffi、ffmpeg、ffprobe、aria2、rtmpdump、mkvtoolsnix、mp4box。
* 自动即将到来的直播重新排队。
* 根据自定义定义的条件应用 `yt-dlp` 选项。
* 自定义浏览器扩展、书签和 iOS 快捷方式，将链接发送到 YTPTube 实例。

## 安装

安装此插件需要一些额外的步骤。

1. [将我的 Hass.io 插件库][repository] 添加到您的 Hass.io 实例。
1. 安装此插件。
1. 点击 `保存` 按钮以保存您的配置。
1. 下载目录默认为 /share/ytptube，可以更改为 share 中的任何内容。
1. 启动插件。它将失败。
1. 通过 SSH 进入家庭助理并输入 `chown hassio /addon_configs/2effc9b9_ytptube`。
1. 再次启动插件。它将失败。
1. 再次通过 SSH 进入家庭助理并输入 `chown hassio /share/ytptube` 或您更改的下载目录。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 通过 <your-ip>:port 打开 WebUI。Ingress 无法使用。

## 配置

```
port : 8081 # 您想运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons