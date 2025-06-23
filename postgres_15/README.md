# Home assistant 附加组件：Postgres

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fpostgres%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fpostgres%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fpostgres%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢每一个给我的仓库加星的人！要加星请点击下面的图像，然后它将在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/postgres/stats.png)

## 关于

PostgreSQL，通常简称为“Postgres”，是一种对象关系型数据库管理系统（ORDBMS），注重扩展性和标准兼容性。作为数据库服务器，它的主要功能是安全地存储数据并支持最佳实践，并根据其他软件应用程序的请求检索数据，无论是在同一计算机上还是在网络上的另一台计算机上（包括互联网）。它可以处理从小型单机应用程序到大型面向互联网的具有多个并发用户的应用程序的工作负载。最新版本还提供数据库本身的复制，以提高安全性和可扩展性。

此附加组件基于官方镜像：https://hub.docker.com/_/postgres

## 配置

Postgres的默认端口是5432，并暴露给主机网络。

默认用户：`postgres`
密码：`由 POSTGRES_PASSWORD 设置`

您可以配置以下选项：
```yaml
POSTGRES_PASSWORD
POSTGRES_USER
POSTGRES_DB
POSTGRES_INITDB_ARGS
POSTGRES_HOST_AUTH_METHOD
```
有关更多信息，请查看 [基础镜像文档](https://hub.docker.com/_/postgres)。

默认情况下，`postgresql.conf` 存储在其他附加组件和 Home Assistant 可访问的卷中，因此您可以方便地通过例如文件编辑器附加组件修改它。如果您更倾向于更好的安全性，可以将 `CONFIG_LOCATION` 更改为例如 `/data/orig/postgresql.conf`，这样它将仅在此附加组件中可访问，但您将必须通过 [Hassio SSH](https://developers.home-assistant.io/docs/operating-system/debugging/) 进行修改。

## 安装

此附加组件的安装非常简单，与安装任何其他附加组件没有区别。

1. 将我的附加组件库添加到您的 Home Assistant 实例（在超级用户附加组件商店的右上角，或点击下面的按钮，如果您已配置我的 HA）
   [![打开您的 Home Assistant 实例并显示带有特定库 URL 预填充的添加附加组件库对话框。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装此附加组件。
1. 单击 `保存` 按钮以存储您的配置。
1. 根据您的偏好设置附加组件选项，至少需要 POSTGRES_PASSWORD。
1. 启动附加组件。
1. 检查附加组件的日志以查看一切是否顺利。
1. 使用任何 Postgres 客户端连接，例如连接到 `homeassistant.local:5432`

## 支持

在 GitHub 上创建一个问题

[repository]: https://github.com/alexbelgium/hassio-addons