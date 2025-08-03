## &#9888; Open Request : [✨ [REQUEST] Baikal - 允许使用 Tailscale 证书和密钥来使用 HTTPS (于 2025-07-03 打开)](https://github.com/alexbelgium/hassio-addons/issues/1935) by [@frederickjh](https://github.com/frederickjh)
# Home assistant add-on: Baikal

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fbazarr%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fbazarr%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fbazarr%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库点赞的人！要点赞，请点击下面的图片，然后它会在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![downloads evolution](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/baikal/stats.png)

## 关于

---

[Baikal](https://sabre.io/baikal/) 是一个轻量级的 CalDAV+CardDAV 服务器。它提供了一个广泛的网页界面，可以轻松管理用户、地址簿和日历。它安装快速简单，只需要一个基本的 php 服务器即可。数据可以存储在 MySQL 或 SQLite 数据库中。
它基于以下 docker 镜像：https://github.com/ckulka/baikal-docker

## 配置

---

Webui 可以在 <http://homeassistant:PORT> 找到。
配置可以通过应用 webUI 进行，除了以下选项

```yaml

```

## 安装

---

这个 add-on 的安装非常简单，与安装其他 add-on 没有区别。

1. 将我的 add-ons 仓库添加到你的 home assistant 实例中（在 supervisor add-ons 存储库的右上角，或者如果你已经配置了我的 HA，点击下面的按钮）
   [![打开你的 Home Assistant 实例并显示带有特定仓库 URL 预填充的添加 add-on 仓库对话框。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装这个 add-on。
1. 点击 `保存` 按钮来存储你的配置。
1. 设置 add-on 选项以符合你的偏好。
1. 启动 add-on。
1. 检查 add-on 的日志以查看一切是否正常。
1. 打开 webUI 并调整软件选项。

## 支持

在 github 上创建问题