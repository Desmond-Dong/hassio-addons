# Home Assistant 插件：calibre

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fcalibre%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fcalibre%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fcalibre%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢每一位为我的代码库点赞的人！要点赞，请点击下面的图片，之后它会出现在右上角。谢谢！_

[![点赞者 repo 名单 @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/calibre/stats.png)

## 关于

---

[Calibre](https://calibre-ebook.com/) 是一个强大且易于使用的电子书管理器。用户称赞它非常出色且必备。它几乎可以让你做所有事情，并且它的功能超越了普通电子书软件。它也是完全免费的开源软件，非常适合普通用户和计算机专家。

该插件基于 Docker 镜像 https://github.com/linuxserver/docker-calibre

## 安装

---

安装这个插件相当简单，与安装任何其他插件没有区别。

1. 将我的插件仓库添加到你的 Home Assistant 实例中（在主管插件商店的右上角，或者如果你已经配置了我的 HA，请点击下面的按钮）
   [![打开你的 Home Assistant 实例并显示添加插件仓库对话框，特定的仓库 URL 会自动填充。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
2. 安装该插件。
3. 点击 `保存` 按钮以存储你的配置。
4. 根据你的偏好设置插件选项
5. 启动插件。
6. 检查插件的日志以查看一切是否顺利。
7. 打开 webUI 并调整软件选项

## 配置

---

Webui 可以在 <http://homeassistant:PORT> 找到。
配置可以通过应用的 webUI 进行，但以下选项除外。
请阅读上游容器文档以获取更多信息 : https://github.com/linuxserver/docker-calibre/blob/35b5e3ae06ba95f666687150ca5fd632b8db9e87/README.md#application-setup

特别是，网络服务器和无线连接需要从桌面应用手动启用，以便能访问，通过 8081 和 9090 端口分别进行。

```yaml
PGID: user
GPID: user
TZ: timezone
PASSWORD: 可选择性设置 GUI 密码
CLI_ARGS: 可选择性传递 CLI 启动参数给 calibre
localdisks: sda1 #以逗号分隔的驱动器的硬件名称或标签来挂载，例如 sda1, sdb1, MYNAS...
networkdisks: "//SERVER/SHARE" # 可选，列出要挂载的 smb 服务器，以逗号分隔
cifsusername: "username" # 可选，smb 用户名，所有 smb 共享相同
cifspassword: "password" # 可选，smb 密码
```

## 支持

在 GitHub 上创建问题

## 插图

---

![插图](https://calibre.com/img/slider/artistdetails.png)

[仓库]: https://github.com/alexbelgium/hassio-addons