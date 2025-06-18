## &#9888; 开放请求 : [✨ [请求] 访问 Gitea app.ini (开放于 2025-06-10)](https://github.com/alexbelgium/hassio-addons/issues/1907) 作者 [@UplandJacob](https://github.com/UplandJacob)
# Home Assistant 插件：Gitea

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fgitea%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=入口&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fgitea%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fgitea%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub 超级Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建器)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/买我一杯咖啡%20(不%20接受%20PayPal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/通过%20PayPal%20买我一杯咖啡-0070BA?logo=paypal&style=flat&logoColor=white

_感谢每一个给我的代码库点星的人！要点星请点击下面的图像，然后它将位于右上角。谢谢！_

[![@alexbelgium/hassio-addons 的 Stargazers 代码库成员](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载进展](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/gitea/stats.png)

## 关于

[Gitea](https://about.gitea.com/) 是一种无痛的自托管全功能软件开发服务，包含 Git 托管、代码审查、团队协作、包注册和 CI/CD。它类似于 GitHub、Bitbucket 和 GitLab。

添加各种调整和配置选项。
这个插件基于 [docker 镜像](https://hub.docker.com/r/gitea/gitea)。

## 配置

```yaml
certfile: fullchain.pem #ssl 证书，必须位于 /ssl
keyfile: privkey.pem #ssl 密钥文件，必须位于 /ssl
ssl: 应用程序是否使用 https
APP_NAME: 应用程序名称
DOMAIN: 可访问的域名 # 默认：homeassistant.local
ROOT_URL: 自定义 root_url，除非有特定需求，否则不需要
```

Web 界面可以在 `<你的-ip>:端口` 找到。

## 安装

安装此插件非常简单，与安装其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件库][repository] 添加到你的 Hass.io 实例。
1. 安装此插件。
1. 点击 `保存` 按钮以存储你的配置。
1. 启动插件。
1. 检查插件的日志，查看一切是否正常。
1. 进入 web 界面，初始化应用程序
1. 重启插件，以应用任何应应用的选项

[repository]: https://github.com/alexbelgium/hassio-addons