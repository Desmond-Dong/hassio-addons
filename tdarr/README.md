# 家庭助手插件：Tdarr

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ftdarr%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ftdarr%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ftdarr%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢每一个给我的仓库加星的人！要加星，请点击下面的图片，然后它会显示在右上角。谢谢！_

[![星标的存储库列表 @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/tdarr/stats.png)

## 关于

[Tdarr](https://tdarr.io) 是一个闭源的分布式转码系统，旨在自动化媒体库的转码/重编码管理，并确保你的文件在编解码器/流/容器等方面完全符合你的需求。利用 Tdarr 节点，将你的闲置硬件投入使用，支持 Windows、Linux（包括 Linux arm）和 macOS。

此插件基于 hurlenko 的 [docker 镜像](https://hub.docker.com/r/hurlenko/Tdarr)。

## 配置

Webui 可以在 <http://homeassistant:8265> 找到。
应用文档可以在此处找到 : https://docs.tdarr.io/docs/welcome/what/

```yaml
localdisks: sda1 # 将要挂载的硬盘名称，用逗号分隔，或者其标签。例如 sda1, sdb1, MYNAS...
networkdisks: "//SERVER/SHARE" # 可选，挂载的 smbv2/3 服务器列表，用逗号分隔
cifsusername: "username" # 可选，smb 用户名，所有 smb 共享相同
cifspassword: "password" # 可选，smb 密码，所有 smb 共享相同
```

## 安装

安装此插件非常简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件库][repository] 添加到你的 Hass.io 实例。
1. 安装此插件。
1. 点击 `保存` 按钮以存储你的配置。
1. 启动插件。
1. 检查插件的日志以查看一切是否正常。
1. 根据你的喜好仔细配置插件，请参阅官方文档了解详情。

## 支持

在 GitHub 上创建一个问题，或在 [家庭助手讨论区](https://community.home-assistant.io/t/home-assistant-addon-Tdarr/282108/3) 上询问

[repository]: https://github.com/alexbelgium/hassio-addons
[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg