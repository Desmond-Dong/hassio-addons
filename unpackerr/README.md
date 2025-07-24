# Home assistant add-on: Unpackerr

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Funpackerr%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=入口&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Funpackerr%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Funpackerr%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=代码检查%20代码库)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建者)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库点赞的人！要点赞，请点击下面的图片，然后它会在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载量趋势](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/unpackerr/stats.png)

## 关于

---
从作者的github中提取：
[unpackerr](https://github.com/unpackerr/unpackerr) 在您的下载主机上作为守护进程运行。它检查完成的下载并将其提取出来，以便Lidarr、Radarr、Readarr、Sonarr可以导入它们。在客户端下载文件后进行提取和删除的选项有很多。

这个插件基于docker镜像 https://hub.docker.com/r/hotio/unpackerr

## 安装

---

这个插件的安装非常简单，与安装任何其他插件没有区别。

1. 将我的插件仓库添加到您的home assistant实例中（在supervisor插件商店的右上角，或如果您已经配置了我的HA，请点击下面的按钮）
   [![打开您的Home Assistant实例并显示带有特定仓库URL预填的添加插件仓库对话框。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装这个插件。
1. 点击`保存`按钮以保存您的配置。
1. 根据您的偏好设置插件的选项。
1. 启动插件。
1. 检查插件的日志，看看是否一切正常。
1. 打开webUI并调整软件选项

## 配置

没有webui。

在 /addon_configs/db21ed7f_unpackerr/unpackerr.conf 中，您可以按照这个环境变量列表设置所有变量：https://github.com/davidnewhall/unpackerr

## 支持

在github上创建问题

[repository]: https://github.com/alexbelgium/hassio-addons