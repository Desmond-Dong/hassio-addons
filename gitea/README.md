## &#9888; 开放请求 : [✨ [请求] 访问 Gitea app.ini (打开于 2025-06-10)](https://github.com/alexbelgium/hassio-addons/issues/1907) 由 [@UplandJacob](https://github.com/UplandJacob)
# 家庭助手插件：Gitea

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fgitea%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=入口&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fgitea%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fgitea%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20代码%20库)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建工具](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建工具)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/为我买杯咖啡%20(没有%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/用%20Paypal%20为我买杯咖啡-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的库加星的人！要加星，请点击下面的图片，然后它将出现在右上角。谢谢！_

[![@alexbelgium/hassio-addons 的 Stargazers 代码库](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/gitea/stats.png)

## 关于

[Gitea](https://about.gitea.com/) 是一个无痛的自托管一体化软件开发服务，包括 Git 托管、代码审查、团队协作、包注册和 CI/CD。它类似于 GitHub、Bitbucket 和 GitLab。

各种调整和配置选项的添加。
该插件基于 [docker 镜像](https://hub.docker.com/r/gitea/gitea)。

## 配置

```yaml
certfile: fullchain.pem # ssl证书，必须位于 /ssl
keyfile: privkey.pem # ssl密钥文件，必须位于 /ssl
ssl: 应用程序是否应该使用 https
APP_NAME: 应用名称
DOMAIN: 要访问的域名 # 默认 : homeassistant.local
ROOT_URL: 定制 root_url，除非有特定需求，否则不需要
```

Webui 可以在 `<your-ip>:port` 访问。

## 安装

这个插件的安装相当简单，与安装任何其他 Hass.io 插件没有不同。

1. [将我的 Hass.io 插件库][repository] 添加到你的 Hass.io 实例。
1. 安装这个插件。
1. 点击 `保存` 按钮以存储你的配置。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 访问 webui，初始化应用
1. 重启插件，以应用任何应该应用的选项

[repository]: https://github.com/alexbelgium/hassio-addons