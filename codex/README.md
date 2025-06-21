# Home assistant 插件: Codex

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fcodex%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fcodex%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fcodex%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub 超级 Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库加星的朋友！要加星，请点击下方图片，然后它会在右上角显示。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/codex/stats.png)

## 关于

---

[Codex](https://github.com/ajslater/codex) 是一个基于网页的漫画档案浏览器和阅读器
这个插件基于官方 Docker 镜像 : https://hub.docker.com/r/ajslater/codex

## 安装

---

这个插件的安装非常简单，与安装任何其他插件没有区别。

1. 将我的插件库添加到你的 Home Assistant 实例（在 Supervisor 的插件商店右上角，或者如果你已经配置了我的 HA，可以点击下面的按钮）
   [![打开你的 Home Assistant 实例并显示添加插件库对话框，特定的库 URL 预填充。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装这个插件。
1. 点击 `保存` 按钮以保存你的配置。
1. 根据你的偏好设置插件选项。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 打开 WebUI 并调整软件选项。

## 配置

WebUI 可以在 <http://homeassistant:PORT> 找到。
默认的用户名/密码：在启动日志中说明。
可以通过应用的 WebUI 进行配置，除非以下选项。

## 添加主题/骨架

你可以将主题/骨架的用户文件夹放置在 /share/codex/www/user 中。

## 选项

```yaml
PGID: user
GPID: user
TZ : 将时区显式设置为长格式（例如 "America/Los Angeles"）。这在 Docker 内部非常有用，因为 Codex 无法自动检测主机机器的时区。
CODEX_RESET_ADMIN=1 : 当 Codex 启动时，将管理员用户及其密码重置为默认值。
CODEX_SKIP_INTEGRITY_CHECK=1 : 启动 Codex 时将跳过数据库完整性修复。
csrf_allowed : 允许访问应用的地址的逗号分隔列表。
localdisks: sda1 # 输入你的驱动器的硬件名称以逗号分隔，或者其标签。例如 sda1, sdb1, MYNAS...
networkdisks: "//SERVER/SHARE" # 可选，要挂载的 smb 服务器列表，以逗号分隔。
cifsusername: "用户名" # 可选，smb 用户名，适用于所有 smb 共享。
cifspassword: "密码" # 可选，smb 密码。
```

## 插图

![图片](https://github.com/alexbelgium/hassio-addons/assets/44178713/f1cf3cad-5bda-46df-a0f5-864b127d7b6b)

## 支持

在 GitHub 上创建一个问题

[仓库]: https://github.com/alexbelgium/hassio-addons