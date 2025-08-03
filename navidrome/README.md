# Home assistant add-on: Navidrome

[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)
[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%navidrome%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%navidrome%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%navidrome%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20Paypal-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white

_感谢所有给我的仓库点赞的人！要点赞，请点击下面的图片，它将在右上角显示。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载量趋势](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/navidrome/stats.png)

## 关于

各种调整和配置选项的添加。
此插件基于 [docker 镜像](https://hub.docker.com/r/deluan/navidrome)。

## 配置

Webui 可以在 <http://homeassistant:PORT> 或通过 Ingress 在侧边栏中访问。
配置可以通过应用 WebUI 进行，以下选项除外。

有关更多配置详细信息，请参阅 https://www.navidrome.org/docs/usage/configuration-options/。

### 选项

| 选项 | 类型 | 默认值 | 描述 |
|------|------|--------|-------|
| `base_url` | str | `/` | 配置 Navidrome 在代理后面的基本 URL |
| `music_folder` | str | `/data/music` | 存储您音乐库的文件夹 |
| `data_folder` | str | `/data` | 存储应用程序数据（DB）的文件夹 |
| `log_level` | str | `info` | 日志级别（error, warn, info, debug, trace） |
| `ssl` | bool | `false` | 启用 Web 界面的 HTTPS |
| `certfile` | str | | TLS 证书的路径 |
| `keyfile` | str | | TLS 密钥文件的路径 |
| `default_language` | str | | 界面的默认语言 |
| `image_cache_size` | str | | 图片缓存的大小 |
| `transcoding_cache_size` | str | | 转码缓存的大小 |
| `scan_schedule` | str | | 自动库扫描的 Cron 表达式 |
| `password_encryption_key` | str | | 密码加密的密钥 |
| `welcome_message` | str | | 自定义欢迎消息 |
| `lastfm_api_key` | str | | 用于播客的 Last.fm API 密钥 |
| `lastfm_secret` | str | | 用于播客的 Last.fm 密密 |
| `spotify_id` | str | | 用于元数据的 Spotify 客户端 ID |
| `spotify_secret` | str | | 用于元数据的 Spotify 客户端密钥 |
| `localdisks` | str | | 要挂载的本地驱动器（例如，`sda1,sdb1,MYNAS`） |
| `networkdisks` | str | | 要挂载的 SMB 共享（例如，`//SERVER/SHARE`） |
| `cifsusername` | str | | 用于网络共享的 SMB 用户名 |
| `cifspassword` | str | | 用于网络共享的 SMB 密码 |
| `cifsdomain` | str | | 用于网络共享的 SMB 域 |

### 示例配置

```yaml
base_url: "/"
music_folder: "/data/music"
data_folder: "/data"
log_level: "info"
ssl: false
certfile: "fullchain.pem"
keyfile: "privkey.pem"
scan_schedule: "0 2 * * *"
lastfm_api_key: "your-lastfm-key"
localdisks: "sda1,sdb1"
networkdisks: "//192.168.1.100/music"
cifsusername: "musicuser"
cifspassword: "password123"
cifsdomain: "workgroup"
```

### 挂载驱动器

此插件支持挂载本地驱动器和远程 SMB 共享：

- **本地驱动器**：请参阅 [在插件中挂载本地驱动器](https://github.com/alexbelgium/hassio-addons/wiki/Mounting-Local-Drives-in-Addons)
- **远程共享**：请参阅 [在插件中挂载远程共享](https://github.com/alexbelgium/hassio-addons/wiki/Mounting-remote-shares-in-Addons)

### 自定义脚本和环境变量

此插件支持自定义脚本和环境变量：

- **自定义脚本**：请参阅 [在插件中运行自定义脚本](https://github.com/alexbelgium/hassio-addons/wiki/Running-custom-scripts-in-Addons)
- **环境变量**：请参阅 [向您的插件添加环境变量](https://github.com/alexbelgium/hassio-addons/wiki/Add-Environment-variables-to-your-Addon)

## 安装

此插件的安装非常简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件仓库][repository] 添加到您的 Hass.io 实例。
1. 安装此插件。
1. 点击 `保存` 按钮以保存您的配置。
1. 启动插件。
1. 检查插件的日志，看看一切是否正常。
1. 进入 WebUI，您将初始化应用程序
1. 重新启动插件，以应用任何应应用的选项

[repository]: https://github.com/alexbelgium/hassio-addons