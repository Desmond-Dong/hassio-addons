# Home assistant add-on: Resilio Sync

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fresiliosync%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=入口&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fresiliosync%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fresiliosync%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=代码检查%20代码库)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建者)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我仓库加星标的人！要加星标，请点击下面的图片，然后它就会出现在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载量趋势](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/resiliosync/stats.png)

## 关于

Web上的自托管文件共享和协作平台。
此插件基于linuxserver.io的[docker镜像](https://github.com/linuxserver/resilio-sync)。

## 安装

此插件的安装非常简单，与安装任何其他Hass.io插件的方法相同。

1. 将我的Hass.io插件仓库[repository]添加到您的Hass.io实例。
1. 安装此插件。
1. 点击`保存`按钮以保存您的配置。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 仔细配置插件以满足您的偏好，请参阅官方文档进行配置。

## 配置

Webui位于 <http://homeassistant:8888>。

```yaml
PGID: 用户
GPID: 用户
TZ: 时区
localdisks: sda1 #用逗号分隔，输入您要挂载的驱动器的硬件名称或其标签。例如. sda1, sdb1, MYNAS...
networkdisks: "//SERVER/共享" #可选，列出要挂载的smb服务器，用逗号分隔
cifsusername: "用户名" #可选，smb用户名，所有smb共享相同
cifspassword: "密码" #可选，smb密码
cifsdomain: "域" #可选，允许为smb共享设置域
data_location: 同步文件的位置
config_location: 配置文件的位置
```

## 支持

在github上创建问题

[repository]: https://github.com/alexbelgium/hassio-addons