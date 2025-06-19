## &#9888; 开放请求 : [✨ [请求] Addon ResilioSync - 许可证管理 (打开于 2025-02-16)](https://github.com/alexbelgium/hassio-addons/issues/1773) by [@rsstrene](https://github.com/rsstrene)
## &#9888; 开放问题 : [🐛 [resiliosync] Resilio Sync 无权访问此文件夹: /backup (打开于 2025-06-12)](https://github.com/alexbelgium/hassio-addons/issues/1909) by [@FrankBakermans](https://github.com/FrankBakermans)
# Home Assistant 附加组件: Resilio Sync

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fresiliosync%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fresiliosync%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fresiliosync%2Fconfig.json)

[![Codacy 勋章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub 超级 Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=代码%20检查)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建器)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/请%20我%20喝%20咖啡%20(没有%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/请%20我%20喝%20咖啡%20使用%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库加星的人！想要加星的话，请点击下面的图片，然后它将位于右上角。谢谢！_

[![@alexbelgium/hassio-addons 的 Stargazers 仓库名单](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/resiliosync/stats.png)

## 关于

自托管的文件共享和协作平台。
此附加组件基于来自 linuxserver.io 的 [docker 镜像](https://github.com/linuxserver/resilio-sync)。

## 安装

此附加组件的安装非常简单，与安装其他 Hass.io 附加组件没有区别。

1. [将我的 Hass.io 附加组件仓库][repository] 添加到你的 Hass.io 实例中。
1. 安装此附加组件。
1. 点击 `保存` 按钮以存储你的配置。
1. 启动附加组件。
1. 检查附加组件的日志以查看是否一切顺利。
1. 根据你的偏好仔细配置附加组件，详细信息请参阅官方文档。

## 配置

WebUI 可在 <http://homeassistant:8888> 找到。

```yaml
PGID: user
GPID: user
TZ: 时区
localdisks: sda1 # 将要挂载的硬盘名称以逗号分隔，或使用其标签。例如: sda1, sdb1, MYNAS...
networkdisks: "//SERVER/SHARE" # 可选, 要挂载的 smb 服务器列表，以逗号分隔
cifsusername: "用户名" # 可选, smb 用户名, 所有 smb 共享均相同
cifspassword: "密码" # 可选, smb 密码
cifsdomain: "域" # 可选, 允许设置 smb 共享的域
data_location: 同步文件所在位置
config_location: 配置文件所在位置
```

## 支持

在 GitHub 上创建问题

[repository]: https://github.com/alexbelgium/hassio-addons