# Home assistant add-on: Epic Games Free

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fepicgamesfree%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=入口&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fepicgamesfree%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=成功&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fepicgamesfree%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库点赞的人！要点赞，请点击下面的图片，然后它会在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![downloads evolution](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/epicgamesfree/stats.png)

## 关于

[Epic Games Store Weekly Free Games](https://github.com/claabs/epicgames-freegames-node) : 自动登录并兑换Epic Games商店的促销免费游戏。支持多个账户、2FA、验证码绕过、验证码通知和计划运行。
此插件基于Docker镜像 https://hub.docker.com/r/charlocharlie/epicgames-freegames

## 配置

Webui可以在<http://homeassistant:PORT>找到。

没有插件选项。所有配置文件（配置和cookies）都必须根据文档手动添加到/config/addons_config/epicgamesfree/中（配置文件的文档在这里 https://github.com/claabs/epicgames-freegames-node#json-configuration 和cookies的文档在这里 https://github.com/claabs/epicgames-freegames-node#cookie-import）

如果此文件不存在，它将在首次启动时创建。

最后一个发布日志提到，由于Epic对自动化检测的改进，自动兑换不再可能。取而代之的是，会通过您首选的通知方法发送兑换链接（感谢 @Shiroe93）

## 安装

此插件的安装非常简单，与安装任何其他插件没有什么不同。

1. 将我的插件仓库添加到您的home assistant实例（在右上角的supervisor插件商店，或如果您已配置我的HA，请点击下面的按钮）
   [![打开您的Home Assistant实例并显示带有特定仓库URL预填的添加插件仓库对话框。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装此插件。
1. 点击`保存`按钮以保存您的配置。
1. 根据您的喜好设置插件选项
1. 启动插件。
1. 检查插件的日志，看看是否一切顺利。
1. 打开WebUI并调整软件选项

## 支持

### 超时错误

请尝试在您的config.json中添加`"browserNavigationTimeout": 300000,` (https://github.com/alexbelgium/hassio-addons/issues/675#issuecomment-1407675351)

### 其他错误

在github上创建问题

[repository]: https://github.com/alexbelgium/hassio-addons