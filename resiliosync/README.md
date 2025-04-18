## &#9888; 开放请求 : [✨ [请求] 插件 ResilioSync - 许可证管理 (开启于 2025-02-16)](https://github.com/alexbelgium/hassio-addons/issues/1773) by [@rsstrene](https://github.com/rsstrene)
# 家庭助手插件：Resilio Sync

[![捐款][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐款][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fresiliosync%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=入口&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fresiliosync%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fresiliosync%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub 超级 Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20代码%20库)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建器)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/买我一杯咖啡%20(没有%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/使用%20Paypal%20买我一杯咖啡-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有点赞我仓库的人！要点赞请点击下面的图片，然后它会在右上角显示。谢谢！_

[![@alexbelgium/hassio-addons 的 Stargazers 仓库名单](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/resiliosync/stats.png)

## 关于

自托管的文件共享与协作平台。
该插件基于来自 linuxserver.io 的 [docker 镜像](https://github.com/linuxserver/resilio-sync)。

## 安装

安装此附加组件相当简单，与安装任何其他 Hass.io 附加组件没有什么不同。

1. [将我的 Hass.io 附加组件仓库][repository] 添加到您的 Hass.io 实例。
1. 安装此附加组件。
1. 点击 `保存` 按钮以存储您的配置。
1. 启动此附加组件。
1. 检查附加组件的日志以查看一切是否顺利。
1. 根据您的偏好仔细配置附加组件，具体请参阅官方文档。

## 配置

Webui 可以在 <http://homeassistant:8888> 找到。

```yaml
PGID: user
GPID: user
TZ: 时区
localdisks: sda1 # 填写要挂载的驱动器的硬件名称，用逗号分隔，或其标签。例如：sda1, sdb1, MYNAS...
networkdisks: "//SERVER/SHARE" # 可选，挂载的 smb 服务器列表，用逗号分隔
cifsusername: "username" # 可选，smb 用户名，适用于所有 smb 共享
cifspassword: "password" # 可选，smb 密码
cifsdomain: "domain" # 可选，允许为 smb 共享设置域
data_location: 同步文件所在位置
config_location: 配置文件所在位置
```

## 支持

在 GitHub 上创建一个问题

[repository]: https://github.com/alexbelgium/hassio-addons