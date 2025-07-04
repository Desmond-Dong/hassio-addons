# Home assistant add-on: Portainer

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fportainer%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fportainer%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fportainer%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

Forked from : https://github.com/hassio-addons/addon-portainer
Implemented changes : 更新到最新版本；Ingress；SSL；通过插件选项设置密码；允许手动覆盖

_感谢所有给我的仓库加星标的人！要加星标，请点击下面的图片，然后它就会在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![downloads evolution](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/portainer/stats.png)

## 关于

---

Portainer 是一个开源的轻量级管理 UI，允许您轻松管理您的 Docker 主机或 Docker 集群。

管理 Docker 从未如此简单。Portainer 提供了 Docker 的详细概览，并允许您管理容器、镜像、网络和卷。

## 恢复备份

打开插件选项并将密码设置为 "空"。重启插件，它将允许您从备份中恢复 Portainer。您需要将您的备份放在一个可访问的文件夹中，例如 /share，以便在插件中挂载

## 警告

Portainer 插件非常强大，几乎可以访问您的整个系统。虽然这个插件是精心创建和维护的，并且考虑到了安全性，但在错误或不熟练的手中，它可能会损坏您的系统。

## 安装

---

这个插件的安装非常简单，与安装任何其他插件没有区别。

1. 将我的插件仓库添加到您的 Home Assistant 实例中（在 supervisor 插件商店的右上角，或点击下面的按钮如果您已经配置了我的 HA）
   [![打开您的 Home Assistant 实例并显示添加插件仓库对话框，并预填了特定的仓库 URL。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装这个插件。
1. 点击 `保存` 按钮以保存您的配置。
1. 根据您的喜好设置插件选项。
1. 启动插件。
1. 检查插件的日志以查看是否一切顺利。
1. 打开 WebUI 并调整软件选项

## 配置

---

Webui 可以在 <http://homeassistant:port> 或使用 Ingress 在侧边栏中找到。
默认的用户名/密码：在启动日志中描述。
配置可以通过应用 WebUI 进行，以下选项除外

```yaml
ssl: true/false
certfile: fullchain.pem #ssl 证书，必须位于 /ssl
keyfile: privkey.pem #sslkeyfile，必须位于 /ssl
password: 定义管理员密码。如果保持空白，将允许手动恢复以前的备份。至少 12 个字符。
```

## 支持

在 github 上创建问题

## 插图

---

![illustration](https://github.com/hassio-addons/addon-portainer/raw/main/images/screenshot.png)