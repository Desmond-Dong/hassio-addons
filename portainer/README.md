# Home assistant add-on: Portainer

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fportainer%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fportainer%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fportainer%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

Forked from : https://github.com/hassio-addons/addon-portainer
Implemented changes : update to latest versions ; ingress ; ssl ; password setting through addon option ; allow manual override

_Thanks to everyone having starred my repo! To star it click on the image below, then it will be on top right. Thanks!_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![downloads evolution](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/portainer/stats.png)

## About

---

Portainer 是一个开源的轻量级管理界面，允许您轻松管理您的 Docker 主机或 Docker 群集。

管理 Docker 从未如此简单。Portainer 提供了 Docker 的详细概述，并允许您管理容器、镜像、网络和卷。

## RESTORE BACKUP

打开附加选项并将密码设置为“空”。重启附加组件，它将允许您从备份中恢复 Portainer。您需要将您的备份放在一个可访问的文件夹中，例如 /share，以便在附加组件中挂载

## WARNING

Portainer 附加组件非常强大，并几乎可以访问您的整个系统。虽然这个附加组件是经过精心创建和维护的，并且考虑了安全性，但在错误或不熟练的手中，它可能会损坏您的系统。

## Installation

---

这个附加组件的安装非常简单，与安装任何其他附加组件没有区别。

1. 将我的附加组件存储库添加到您的 Home Assistant 实例中（在 Supervisor 附加组件商店的右上角，或者如果您已配置我的 HA，请点击下面的按钮）
   [![打开您的 Home Assistant 实例并显示附加组件存储库对话框，预填了特定的存储库 URL。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装此附加组件。
1. 点击 `Save` 按钮以保存您的配置。
1. 根据您的偏好设置附加组件选项。
1. 启动附加组件。
1. 检查附加组件的日志，以查看是否一切顺利。
1. 打开 WebUI 并调整软件选项

## Configuration

---

Webui 可以在 <http://homeassistant:port> 找到，或者在 Ingress 侧边栏中找到。
默认的用户名/密码：在启动日志中描述。
配置可以通过应用程序 WebUI 进行，除了以下选项

```yaml
ssl: true/false
certfile: fullchain.pem #ssl 证书，必须位于 /ssl
keyfile: privkey.pem #sslkeyfile，必须位于 /ssl
password: 定义管理员密码。如果保持空白，将允许手动恢复以前的备份。至少 12 个字符。
```

## Support

在 github 上创建问题

## Illustration

---

![illustration](https://github.com/hassio-addons/addon-portainer/raw/main/images/screenshot.png)