# Home assistant add-on: Codex

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fcodex%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fcodex%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fcodex%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_Thanks to everyone having starred my repo! To star it click on the image below, then it will be on top right. Thanks!_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![downloads evolution](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/codex/stats.png)

## About

---

[Codex](https://github.com/ajslater/codex) 是一个基于网络的漫画存档浏览器和阅读器
这个插件基于官方的 docker 镜像：https://hub.docker.com/r/ajslater/codex

## 安装

---

这个插件的安装非常简单，与其他插件的安装方式相同。

1. 将我的插件仓库添加到您的 home assistant 实例中（在 supervisor 插件商店的右上角，或者如果您已经配置了我的 HA，请点击下面的按钮）
   [![打开您的 Home Assistant 实例并显示添加插件仓库对话框，预填特定的仓库 URL。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装这个插件。
1. 点击 `保存` 按钮以保存您的配置。
1. 设置插件选项以符合您的偏好。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 打开 webUI 并调整软件选项

## 配置

Webui 可以在 <http://homeassistant:PORT> 找到。
默认的用户名/密码：在启动日志中描述。
配置可以通过 app 的 webUI 进行，除了以下选项

## 添加主题/骨架

您可以将主题/骨架的用户文件夹放置在 /share/codex/www/user，

## 选项

```yaml
PGID: user
GPID: user
TZ : 明确指定时区，长格式（例如 "America/Los Angeles"）。在 Docker 中非常有用，因为 codex 无法自动检测主机机的时区
CODEX_RESET_ADMIN=1 : codex 启动时将重置管理员用户及其密码为默认值。
CODEX_SKIP_INTEGRITY_CHECK=1 : codex 启动时将跳过数据库完整性修复
csrf_allowed : 允许访问应用的地址列表，用逗号分隔
localdisks: sda1 #将您的驱动硬件名称添加到挂载中，用逗号分隔，或其标签。例如。 sda1, sdb1, MYNAS...
networkdisks: "//SERVER/SHARE" #可选，要挂载的 SMB 服务器列表，用逗号分隔
cifsusername: "username" #可选，SMB 用户名，所有 SMB 共享相同
cifspassword: "password" #可选，SMB 密码
```

## 插图

![image](https://github.com/alexbelgium/hassio-addons/assets/44178713/f1cf3cad-5bda-46df-a0f5-864b127d7b6b)

## 支持

在 github 上创建问题

[repository]: https://github.com/alexbelgium/hassio-addons