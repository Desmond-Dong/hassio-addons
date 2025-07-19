# Home assistant add-on: calibre

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fcalibre%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fcalibre%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fcalibre%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库点赞的人！要点赞，请点击下面的图片，然后它将在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![downloads evolution](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/calibre/stats.png)

## 关于

---

[Calibre](https://calibre-ebook.com/) 是一个功能强大且易于使用的电子书管理器。用户称其为卓越且必备的工具。它几乎可以完成所有操作，并在普通电子书软件的基础上更进一步。它也是完全免费和开源的，非常适合普通用户和计算机专家。

这个插件基于以下docker镜像：https://github.com/linuxserver/docker-calibre

## 安装

---

这个插件的安装非常简单，与安装其他插件没有区别。

1. 将我的插件仓库添加到您的home assistant实例中（在supervisor插件商店的右上角，或者如果您已经配置了我的HA，请点击下面的按钮）
   [![打开您的Home Assistant实例并显示带有特定仓库URL预填的添加插件仓库对话框。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装这个插件。
1. 点击`保存`按钮以保存您的配置。
1. 根据您的偏好设置插件选项。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 打开WebUI并调整软件选项

## 配置

---

Webui可以在<http://homeassistant:PORT>找到。
配置可以通过app的WebUI进行，除了以下选项。
请阅读上游容器的文档以获取更多信息：https://github.com/linuxserver/docker-calibre/blob/35b5e3ae06ba95f666687150ca5fd632b8db9e87/README.md#application-setup

特别是，需要手动从桌面应用程序启用Web服务器和无线连接，才能访问它，分别使用端口8081和9090。

```yaml
PGID: user
GPID: user
TZ: timezone
PASSWORD: 可选地设置gui的密码
CLI_ARGS: 可选地传递给calibre的cli启动参数
localdisks: sda1 #用逗号分隔，或其标签放置您驱动器的硬件名称来挂载。例如。 sda1, sdb1, MYNAS...
networkdisks: "//SERVER/SHARE" #可选的，列出要挂载的smb服务器，用逗号分隔
cifsusername: "username" #可选的，smb用户名，所有smb共享相同
cifspassword: "password" #可选的，smb密码
```

## 支持

在github上创建问题

## 插图

---

![illustration](https://calibre.com/img/slider/artistdetails.png)

[repository]: https://github.com/alexbelgium/hassio-addons