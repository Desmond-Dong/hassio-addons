# Home Assistant 附加组件：Webtop KDE Alpine

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fwebtop%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=入口&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fwebtop%2Fconfig.json)
![体系结构](https://img.shields.io/badge/dynamic/json?color=success&label=体系结构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fwebtop%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20代码%20库)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建器)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢大家给我的仓库点星！要给它加星，请点击下面的图像，然后它会显示在右上角。谢谢！_

[![Star 统计](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/webtop/stats.png)

## 关于

[webtop](https://github.com/webtop/webtop) 是一个可以通过任何现代浏览器访问的完整桌面环境。
这个附加组件是基于 Docker 镜像 https://github.com/linuxserver/docker-webtop

## 配置

Webui 可以通过入口访问，或在 <http://homeassistant:PORT> 访问。该端口默认禁用，但可以通过附加组件选项启用。

默认情况下，该镜像以 abc 用户为基础，我们建议使用该用户因为所有的初始化和配置都是基于它。默认密码也是 abc。如果您想更改此密码并在访问界面时需要身份验证，只需在 Webtop 的 GUI 终端中输入 passwd。然后在访问 Web 界面时使用以下路径：

http://localhost:3000/?login=true

应用程序的安装不是永久性的，您需要通过附加组件选项进行安装。然而，它们的配置是永久的。

如果图形无法正常工作，请使用 DRINODE 功能选择您的图形设备。

查看所有可能的 ENV 变量： https://docs.linuxserver.io/images/docker-webtop#optional-environment-variables

```yaml
TZ: 时区 ; 根据 https://manpages.ubuntu.com/manpages/trusty/man3/DateTime::TimeZone::Catalog.3pm.html 的国家/城市
additional_apps: engrampa,thunderbird # 允许安装应用程序，因为它们不是持久的
DRINODE: 指定自定义图形设备，默认是 /dev/dri/renderD128
DNS_servers: 8.8.8.8,1.1.1.1 # 保持空白以使用路由器的 DNS，或者设置自定义 DNS 以避免在本地 DNS 广告移除器中的垃圾邮件
localdisks: sda1 # 输入硬盘的硬件名称，多个名称用逗号分隔，或使用其标签。例如：sda1, sdb1, MYNAS...
networkdisks: "//SERVER/SHARE" # 可选，列出要挂载的 smb 服务器，多个服务器用逗号分隔
cifsusername: "用户名" # 可选，smb 用户名，适用于所有 smb 共享
cifspassword: "密码" # 可选，smb 密码
cifsdomain: "域" # 可选，允许为 smb 共享设置域
```

## 安装

此附加组件的安装相当简单，与安装其他任何附加组件没有区别。

1. 将我的附加组件库添加到您的 Home Assistant 实例（在监督者附加组件商店右上角，或如果您已配置我的 HA，请点击下面的按钮）
   [![打开您的 Home Assistant 实例并显示添加附加组件库对话框，预填特定库 URL。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装此附加组件。
1. 点击 `保存` 按钮以存储您的配置。
1. 根据您的偏好设置附加组件选项
1. 启动附加组件。
1. 检查附加组件的日志以查看一切是否正常。
1. 打开 WebUI 并调整软件选项

## 支持

在 GitHub 上创建一个问题

## 插图

![插图](https://www.linuxserver.io/user/pages/content/images/2021/05/menu.png)

[repository]: https://github.com/alexbelgium/hassio-addons