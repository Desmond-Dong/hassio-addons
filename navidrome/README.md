## ⚠️ Open Issue : [🐛 [Navidrome] 添加 Navidrome 到 Music Assistant 时出错。 (已打开 2025-06-19)](https://github.com/alexbelgium/hassio-addons/issues/1919) by [@WCRalph](https://github.com/WCRalph)
# Home assistant 插件：Navidrome

[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)
[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)

![版本](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%navidrome%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=入口&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%navidrome%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%navidrome%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建器)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20Paypal-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white

_感谢所有给我的仓库星标的人！要星标它，请点击下面的图片，然后它将在右上角。谢谢！_

[![@alexbelgium/hassio-addons 的星标者仓库列表](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载量趋势](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/navidrome/stats.png)

## 关于

各种调整和配置选项的添加。
此插件基于 [docker 镜像](https://hub.docker.com/r/deluan/navidrome)。

## 配置

请查看 https://www.navidrome.org/docs/usage/configuration-options/#available-options

```yaml
    "base_url": "localhost",         # 配置 Navidrome 在代理后面的基本 URL
    "music_folder": "/data/music",   # 存储你的音乐库的文件夹。可以是只读的
    "data_folder": "/data/data",     # 存储应用程序数据（数据库）的文件夹
    "log_level": "info",             # 日志级别。用于故障排除。可能的值：error, warn, info, debug, trace
    "certfile": "fullchain.pem",     # TLS 证书的路径
    "keyfile": "privkey.pem",        # TLS 密钥文件的路径
    "ssl": false                     # 应用程序是否使用 https
```

Webui 可以在 `<你的 IP>:端口` 找到。

## 安装

这个插件的安装非常简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件仓库][repository] 添加到你的 Hass.io 实例。
1. 安装这个插件。
1. 点击 `保存` 按钮来存储你的配置。
1. 启动插件。
1. 检查插件的日志，看看是否一切顺利。
1. 进入 Webui，在那里你将初始化应用程序
1. 重新启动插件，以应用任何应该应用的选项

[repository]: https://github.com/alexbelgium/hassio-addons