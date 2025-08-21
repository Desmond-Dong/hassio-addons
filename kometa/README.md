<!-- markdownlint-disable MD043 -->

# Home assistant add-on: Kometa

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fplex_meta_manager%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fplex_meta_manager%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fplex_meta_manager%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有将我的仓库加入星标的人！点击下面的图片将仓库加入星标，它将出现在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![downloads evolution](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/kometa/stats.png)

## 关于

---

[Kometa](https://kometa.wiki/en/latest/) 是一个 Python 3 脚本，可以通过 YAML 配置文件持续运行，以按计划更新您图书馆中电影、节目和收藏的元数据，并自动根据各种方法构建收藏，所有这些方法都在维基中详细说明。

此插件基于 Docker 镜像 <https://github.com/linuxserver/docker-kometa>

## 安装

---

此插件的安装非常简单，与安装任何其他插件没有区别。

1. 将我的插件仓库添加到您的 Home Assistant 实例中（在 Supervisor 插件商店的右上角，或如果您已配置我的 HA，请点击下面的按钮）
   [![打开您的 Home Assistant 实例并显示带有特定仓库 URL 预填的添加插件仓库对话框。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装此插件。
1. 点击 `保存` 按钮以保存您的配置。
1. 根据您的偏好设置插件选项
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 打开 WebUI 并调整软件选项

## 配置

有一个 [教程](https://github.com/Kometa-Team/Kometa#setting-up-the-initial-config-file) 可帮助您快速上手。
更多信息请参阅 [官方维基](https://github.com/Kometa-Team/Kometa)。

选项可以通过两种方式配置：

- 插件选项

```yaml
PUID: 1000 #for UserID - see below for explanation
PGID: 1000 #for GroupID - see below for explanation
TZ: Europe/London #Specify a timezone to use EG Europe/London.
KOMETA_CONFIG: /config/addons_config/kometa/config/config.yml #Specify a custom config file to use.
KOMETA_TIME: 03:00 #Comma-separated list of times to update each day. Format: HH:MM.
KOMETA_RUN: False #Set to True to run without the scheduler.
KOMETA_TEST: False #Set to True to run in debug mode with only collections that have test: true.
KOMETA_NO_MISSING: False #Set to True to run without any of the missing movie/show functions.
```

- Config.yaml (高级用法)

附加变量可以通过在 config.yaml 中添加它们来作为 ENV 变量设置，位置根据此指南定义：<https://github.com/alexbelgium/hassio-addons/wiki/Addons-feature:-add-env-variables>

完整的 ENV 变量列表可以在这里查看：<https://kometa.wiki/en/latest/kometa/environmental/>

## 支持

在 github 上创建问题

## 插图

---

![illustration](https://dausruddin.com/wp-content/uploads/2020/05/plex-meta-manager-v3-1024x515.png)