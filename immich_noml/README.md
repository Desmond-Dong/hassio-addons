# Home Assistant 插件: immich

⚠️ 该项目正在非常积极地开发中。请预期会有错误和变更。请不要将其作为存储您的照片和视频的唯一方式！ （来自开发者）

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fimmich%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fimmich%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fimmich%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库加星的朋友们！要加星请点击下面的图片，然后它将在右上角。谢谢！_

[![Starred repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/immich/stats.png)

## 关于

基于web的文件浏览器。
该插件基于来自imagegenius的[docker镜像](https://github.com/imagegenius/docker-immich)。

## 配置

Postgresql可以是内部或外部的

```yaml
    "PGID": "整数",
    "PUID": "整数",
    "TZ": "字符串?",
    "cifsdomain": "字符串?",
    "cifspassword": "字符串?",
    "cifsusername": "字符串?",
    "data_location": "字符串",
    "localdisks": "字符串?",
    "networkdisks": "字符串?",
    "DB_HOSTNAME": "字符串?",
    "DB_USERNAME": "字符串?",
    "DB_PORT": "整数?",
    "DB_PASSWORD": "字符串?",
    "DB_DATABASE_NAME": "字符串?",
    "JWT_SECRET": "字符串?"
```

## 安装

安装这个插件非常简单，与安装任何其他Hass.io插件没有区别。

1. [将我的Hass.io插件仓库][repository]添加到您的Hass.io实例中。
1. 安装这个插件。
1. 点击`保存`按钮以存储您的配置。
1. 启动插件。
1. 检查插件的日志，以查看一切是否顺利。
1. 小心根据您的偏好配置插件，具体请查看官方文档。

请注意，您需要安装一个单独的postgres插件才能连接数据库。您可以在我的仓库中安装postgres插件。
请务必在启动之前更改密码；否则，之后将无法更改

## 支持

在github上创建一个问题，或在[Home Assistant 论坛](https://community.home-assistant.io/t/home-assistant-addon-immich/282108/3)上提问

[repository]: https://github.com/alexbelgium/hassio-addons
[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg