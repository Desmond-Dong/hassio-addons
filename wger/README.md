## ⚠️ Open Issue : [🐛 [Wger] 环境变量被忽略 / CSRF 验证失败 (于 2025-08-25 打开)](https://github.com/alexbelgium/hassio-addons/issues/2070) by [@IceBotYT](https://github.com/IceBotYT)

# Hass.io Add-ons: Wger

[![赞助](https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white)](https://www.buymeacoffee.com/alexbelgium)
[![赞助](https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white)](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fwger%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=入口&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fwger%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fwger%2Fconfig.json)

[![Codacy 标识](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建者](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建者)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库点赞的人！点击下面的图片点赞，它就会在右上角显示。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载量趋势](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/wger/stats.png)

## 关于

[wger](https://github.com/wger-project/wger) Workout Manager 是一个免费、开源的网页应用，帮助你管理个人锻炼、体重和饮食计划，也可以用作简单的健身房管理工具。它提供了一个 REST API，方便与其他项目和工具集成。

## 配置

- 启动插件。稍等片刻并检查日志中的任何错误。初始启动可能需要长达 15 分钟！
- 打开你的域名：8000（其中 ":8000" 是插件中配置的端口）。
- 默认
  - 用户名：`admin`
  - 密码：`adminadmin`

选项可以通过两种方式配置：

- 插件选项

```yaml
"CONFIG_LOCATION": 配置的 config.yaml 位置 # 设置 config.yaml 的位置（见下文）
```

- config.yaml（高级用法）

附加变量可以通过在 config.yaml 中添加它们，并根据此指南在插件选项中定义的位置将其设置为 ENV 变量：https://github.com/alexbelgium/hassio-addons/wiki/Addons-feature:-add-env-variables

完整的 ENV 变量列表可以在这里查看：不可用

## 安装

这个插件的安装非常简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件仓库][repository]添加到你的 Hass.io 实例。
1. 安装这个插件。
1. 点击 `保存` 按钮来存储你的配置。
1. 启动插件。
1. 检查插件的日志，看看是否一切正常。
1. 仔细配置插件以符合你的偏好，请参阅官方文档进行配置。

## 支持

如果你在安装中有问题，请确保查看 GitHub。

[repository]: https://github.com/alexbelgium/hassio-addons