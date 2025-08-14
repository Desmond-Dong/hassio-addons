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
Implemented changes : update to latest versions ; ingress ; ssl ; password setting through addon option ; allow manual override

_Thanks to everyone having starred my repo! To star it click on the image below, then it will be on top right. Thanks!_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![downloads evolution](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/portainer/stats.png)

## About

---

Portainer 是一个开源的轻量级管理 UI，它允许你轻松管理你的 Docker 主机或 Docker 群集。

管理 Docker 从未如此简单。Portainer 提供了 Docker 的详细概览，并允许你管理容器、镜像、网络和卷。

## RESTORE BACKUP

打开插件选项并将密码设置为“空”。重启插件，它将允许从备份中恢复 Portainer。你需要将你的备份放在一个可访问的文件夹中，例如 /share，以便在插件中挂载

## WARNING

Portainer 插件非常强大，几乎可以让你访问整个系统。虽然这个插件是精心创建和维护的，并且考虑了安全性，但在错误或缺乏经验的情况下，它可能会损坏你的系统。

## Installation

---

这个插件的安装非常简单，与安装其他插件没有什么不同。

1. 将我的插件仓库添加到你的 Home Assistant 实例中（在 supervisor 插件商店的右上角，或者如果你已经配置了我的 HA，点击下面的按钮）
   [![打开你的 Home Assistant 实例并显示带有特定仓库 URL 预填充的添加插件仓库对话框。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装这个插件。
1. 点击 `保存` 按钮以保存你的配置。
1. 将插件选项设置为你的偏好。
1. 启动插件。
1. 检查插件的日志，看看是否一切顺利。
1. 打开 WebUI 并调整软件选项

## Configuration

Webui 可以在 <http://homeassistant:port> 或使用 Ingress 在侧边栏中找到。
默认用户名是 "admin"，密码在启动日志中描述。

### Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `ssl` | bool | `false` | 启用 Web 界面的 HTTPS |
| `certfile` | str | `fullchain.pem` | SSL 证书文件（在 `/ssl/` 中） |
| `keyfile` | str | `privkey.pem` | SSL 私有密钥文件（在 `/ssl/` 中） |
| `password` | str | `homeassistant` | 管理员密码（至少 12 个字符，留空以恢复备份） |

### Example Configuration

```yaml
ssl: true
certfile: "fullchain.pem"
keyfile: "privkey.pem"
password: "your-secure-password-123"
```

### Custom Scripts and Environment Variables

这个插件支持通过 `addon_config` 映射的自定义脚本和环境变量：

- **Custom scripts**: 查看 [在插件中运行自定义脚本](https://github.com/alexbelgium/hassio-addons/wiki/Running-custom-scripts-in-Addons)
- **Environment variables**: 查看 [为你的插件添加环境变量](https://github.com/alexbelgium/hassio-addons/wiki/Add-Environment-variables-to-your-Addon)

## Support

在 github 上创建问题

## Illustration

---

![illustration](https://github.com/hassio-addons/addon-portainer/raw/main/images/screenshot.png)