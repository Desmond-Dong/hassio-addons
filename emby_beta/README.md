# Home assistant add-on: emby

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Femby%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Femby%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Femby%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢大家给我的仓库点赞！要点赞，请点击下面的图片，然后它会在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载量趋势](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/emby/stats.png)

## 关于

[emby](https://emby.media/) 组织视频、音乐、直播电视和照片，并将它们从个人媒体库流式传输到智能电视、流媒体盒子和移动设备。这个容器作为一个独立的 emby 媒体服务器进行打包。

这个插件基于 linuxserver.io 的 [docker 镜像](https://github.com/linuxserver/docker-emby)。
初始插件版本 : https://github.com/petersendev/hassio-addons

## 配置

Webui 可以在 `<你的IP>:8096` 找到，或者在 Home Assistant 通过 Ingress 访问。

```yaml
PGID: user
GPID: user
TZ: 时区
localdisks: sda1 #输入你要挂载的硬件名称，用逗号分隔，或其标签。例如。sda1, sdb1, MYNAS...
networkdisks: "//SERVER/SHARE" #可选，列出要挂载的smb服务器，用逗号分隔
cifsusername: "用户名" #可选，smb用户名，所有smb共享相同
cifspassword: "密码" #可选，smb密码
cifsdomain: "域名" #可选，允许为smb共享设置域名
silent: true #抑制调试消息
```

## 安装

这个插件的安装非常简单，与其他 Hass.io 插件安装没有区别。

1. [将我的 Hass.io 插件仓库][repository]添加到你的 Hass.io 实例。
1. 安装这个插件。
1. 点击 `保存` 按钮来保存你的配置。
1. 启动插件。
1. 检查插件的日志，看看是否一切正常。
1. 仔细配置插件以符合你的喜好，参考官方文档进行配置。

[repository]: https://github.com/alexbelgium/hassio-addons