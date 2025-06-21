# 家庭助手附加组件：Sonarr

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fsonarr%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fsonarr%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fsonarr%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有为我的仓库点星的人！点击下方图片来给它点星，然后它将出现在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载进化](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/sonarr/stats.png)

## 关于

---

[Sonarr](https://sonarr.tv/) 是用于 Usenet 和 BitTorrent 用户的个人视频录像机（PVR）。它可以监控多个 RSS 源，以查找您最喜欢的节目的新剧集，并会抓取、排序和重命名它们。它还可以配置为在更高质量的格式可用时自动升级已下载文件的质量。
该附加组件基于 Docker 镜像 https://github.com/linuxserver/docker-sonarr

## 安装

---

安装此附加组件非常简单，与安装其他附加组件没有区别。

1. 将我的附加组件库添加到您的家庭助手实例（在管理员附加组件商店右上角，或如果您已配置我的 HA，请点击下方按钮）
   [![打开您的家庭助手实例并显示带有特定库 URL 预填的添加附加组件库对话框。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装此附加组件。
1. 点击 `保存` 按钮以存储您的配置。
1. 根据您的偏好设置附加组件选项
1. 启动附加组件。
1. 检查附加组件的日志以查看一切是否顺利。
1. 打开 webUI 并调整软件选项。

## 配置

---

WebUI 可以在 <http://homeassistant:PORT> 找到。
默认用户名/密码：在启动日志中描述。
配置可以通过应用程序的 WebUI 完成，以下选项除外：

```yaml
PGID: user
GPID: user
TZ: timezone
localdisks: sda1 # 将您的驱动器的硬件名称以逗号分隔放入，或其标签。例如 sda1, sdb1, MYNAS...
networkdisks: "//SERVER/SHARE" # 可选，列出以逗号分隔的 smb 服务器以挂载
cifsusername: "username" # 可选，smb 用户名，适用于所有 smb 共享
cifspassword: "password" # 可选，smb 密码
connection_mode: ingress_noauth (默认，禁用身份验证以便无缝进入集成), noingress_auth (禁用进入以允许更简单的外部 URL，启用身份验证), ingress_auth (同时启用进入和身份验证)
```

## 支持

在 GitHub 上创建一个问题

## 插图

---

![插图](https://b0b.fr/wp-content/uploads/2016/02/Sonarr-1-1000x924.jpg)

[repository]: https://github.com/alexbelgium/hassio-addons