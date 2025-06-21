# 家庭助理插件：Webtop KDE Alpine

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fwebtop%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fwebtop%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fwebtop%2Fconfig.json)

[![Codacy 勋章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建者](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢每一个给我的仓库打星的人！要打星请点击下面的图片，然后在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载量演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/webtop/stats.png)

## 关于

[webtop](https://github.com/webtop/webtop) 是一个通过任何现代网页浏览器访问的完整桌面环境。
这个插件基于 Docker 镜像 https://github.com/linuxserver/docker-webtop

## 配置

Webui 可以通过入口访问或在 <http://homeassistant:PORT> 找到。默认情况下端口是禁用的，但可以通过插件选项启用。

默认情况下，镜像是基于 abc 用户的，我们建议使用此用户，因为所有的初始化/配置都是围绕它进行的。默认密码也是 abc。如果您想更改此密码并在访问界面时需要身份验证，只需在 webtop 的 GUI 终端中输入 passwd。然后在访问网页界面时使用路径：

http://localhost:3000/?login=true

应用程序的安装是不持久的，您需要通过插件选项进行安装。不过，它们的配置是持久的。

如果图形不工作，请使用 DRINODE 功能选择您的图形设备。

在这里查看所有潜在的环境变量 : https://docs.linuxserver.io/images/docker-webtop#optional-environment-variables

```yaml
TZ: 时区 ; 根据 https://manpages.ubuntu.com/manpages/trusty/man3/DateTime::TimeZone::Catalog.3pm.html 的国家/城市
additional_apps: engrampa,thunderbird # 允许安装应用程序，因为它们不是持久的
DRINODE: 指定一个自定义图形设备，默认是 /dev/dri/renderD128
DNS_servers: 8.8.8.8,1.1.1.1 # 保持为空以使用路由器的 DNS，或设置自定义 DNS 以避免在本地 DNS 广告删除器中进行垃圾邮件
localdisks: sda1 # 输入要挂载的驱动器硬件名称，以逗号分隔，或其标签。例：sda1, sdb1, MYNAS...
networkdisks: "//SERVER/SHARE" # 可选，挂载的 smb 服务器列表，以逗号分隔
cifsusername: "用户名" # 可选，smb 用户名，所有 smb 共享相同
cifspassword: "密码" # 可选，smb 密码
cifsdomain: "域" # 可选，允许为 smb 共享设置域
```

## 安装

此插件的安装非常简单，与安装其他任何插件没有区别。

1. 将我的插件库添加到您的家庭助理实例（在顶部右侧的主管附加商店中，或如果您已配置我的 HA，则点击下面的按钮）
   [![打开您的家庭助理实例并显示添加插件库对话框，特定库 URL 预填。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装此插件。
1. 点击 `保存` 按钮以保存您的配置。
1. 根据您的偏好设置插件选项
1. 启动插件。
1. 检查插件的日志以查看是否一切顺利。
1. 打开 webUI 并调整软件选项

## 支持

在 GitHub 上创建一个问题

## 插图

![插图](https://www.linuxserver.io/user/pages/content/images/2021/05/menu.png)

[repository]: https://github.com/alexbelgium/hassio-addons