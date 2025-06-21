# Home Assistant 插件: Openproject

[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)
[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%openproject%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%openproject%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%openproject%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20Paypal-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white

_感谢每一位给我的代码库点赞的人！要点赞，请点击下面的图片，然后它会显示在右上方。谢谢！_

[![点赞者名单 @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载量变化](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/openproject/stats.png)

## 关于

该插件基于 [docker 镜像](https://hub.docker.com/r/openproject/openproject)。

## 配置

填写默认插件选项以启动插件。确保特别配置主机名，使用你的 Home Assistant IP + 插件暴露的端口。
有关更多选项，请使用 config.yaml 系统 : https://github.com/alexbelgium/hassio-addons/wiki/Add%E2%80%90ons-feature-:-add-env-variables

Webui 可以在 `<你的-ip>:端口` 找到。

## 安装

该插件的安装非常简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件代码库][repository] 添加到你的 Hass.io 实例。
1. 安装该插件。
1. 点击 `保存` 按钮以存储你的配置。
1. 启动插件。
1. 检查插件的日志以查看一切是否正常。
1. 访问 Webui，在那里初始化应用。
1. 重启插件，以应用任何应该应用的选项。

默认管理密码 (登录: admin, 密码: admin)。

[repository]: https://github.com/alexbelgium/hassio-addons