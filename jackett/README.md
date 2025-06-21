# Home Assistant 附加组件: jackett

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fjackett%2Fconfig.json)
![接入](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fjackett%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fjackett%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub 超级校验器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建工具](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有关注我的仓库的人！要关注，请点击下面的图片，然后它会出现在右上角。谢谢！_

[![关注者名单 @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/jackett/stats.png)

## 介绍

[jackett](https://github.com/jackett/jackett) - 一个用于与电影（如 Couchpotato）一起工作的 jackett 的分支。

此附加组件基于来自 linuxserver.io 的 [docker 镜像](https://github.com/linuxserver/docker-jackett)。

## 配置

配置可以通过应用程序 webUI 完成，除了以下选项 :

```yaml
PGID: user
GPID: user
TZ: timezone
localdisks: sda1 # 输入要挂载的驱动器的硬件名称，用逗号分隔，或其标签。例如 sda1, sdb1, MYNAS...
networkdisks: "//SERVER/SHARE" # 可选，要挂载的 smb 服务器列表，用逗号分隔
cifsusername: "username" # 可选，smb 用户名，所有 smb 共享相同
cifspassword: "password" # 可选，smb 密码
```

## 安装

此附加组件的安装非常简单，与安装其他 Hass.io 附加组件没有什么区别。

1. [将我的 Hass.io 附加组件库][repository] 添加到您的 Hass.io 实例。
1. 安装此附加组件。
1. 点击 `保存` 按钮以存储您的配置。
1. 启动附加组件。
1. 检查附加组件的日志以查看是否一切正常。
1. 根据您的偏好仔细配置附加组件，请参阅官方文档以获取详细信息。

[repository]: https://github.com/alexbelgium/hassio-addons