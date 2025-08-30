# Home assistant add-on: Openproject

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fopenproject%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fopenproject%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fopenproject%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=代码检查)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建者)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/请给我一杯咖啡-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/请给我一杯咖啡-Paypal-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white

_感谢所有给我仓库加星标的人！要加星标，请点击下面的图片，然后它将在右上角显示。谢谢！_

[![加星标者仓库列表 for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载趋势](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/openproject/stats.png)

## 关于

这个插件基于 [docker 镜像](https://hub.docker.com/r/openproject/openproject)。

## 配置

填写默认插件选项以启动插件。确保特别是配置主机名，使用你的 homeassistant ip + 插件暴露端口
对于附加选项，使用 config.yaml 系统：https://github.com/alexbelgium/hassio-addons/wiki/Addons-feature:-add-env-variables

Webui 可以在 `<你的ip>:端口` 找到。

## 安装

这个插件的安装非常简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件仓库][repository] 添加到你的 Hass.io 实例。
1. 安装这个插件。
1. 点击 `保存` 按钮来保存你的配置。
1. 启动插件。
1. 检查插件的日志，看看一切是否正常。
1. 进入 webui，在那里初始化应用
1. 重新启动插件，以应用任何应该应用的选项

默认管理员密码（登录：admin，密码：admin）。

[repository]: https://github.com/alexbelgium/hassio-addons