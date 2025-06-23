# 家庭助理附加组件: Postgres

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fpostgres%2Fconfig.json)
![访问](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fpostgres%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fpostgres%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有为我的仓库点赞的人！要点赞，请点击下面的图片，然后它会在右上角。谢谢！_

[![@alexbelgium/hassio-addons 的观星者仓库名单](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/postgres/stats.png)

## 关于

PostgreSQL，通常称为“Postgres”，是一种面向对象的关系数据库管理系统（ORDBMS），强调可扩展性和标准兼容性。作为数据库服务器，其主要功能是安全地存储数据并支持最佳实践，并在后续被其他软件应用程序请求时检索数据，无论这些应用程序是在同一台计算机上运行还是在网络（包括互联网）上的另一台计算机上运行。它可以处理从小型单机应用程序到大型面向互联网的应用程序及多个并发用户的工作负载。最近版本还提供了数据库本身的复制，以增强安全性和可扩展性。

该附加组件基于官方镜像: https://hub.docker.com/_/postgres

## 配置

Postgres 默认端口为 5432，并暴露给主机网络。

默认用户: `postgres`
密码: `通过 POSTGRES_PASSWORD 设置`

您可以配置以下选项：
```yaml
POSTGRES_PASSWORD
POSTGRES_USER
POSTGRES_DB
POSTGRES_INITDB_ARGS
POSTGRES_HOST_AUTH_METHOD
```
有关更多信息，请查看 [基本镜像文档](https://hub.docker.com/_/postgres)。

默认情况下，`postgresql.conf` 存储在其他附加组件和 Home Assistant 可访问的卷中，因此您可以方便地通过例如文件编辑器附加组件进行修改。如果您更喜欢更好的安全性，请将 `CONFIG_LOCATION` 更改为例如 `/data/orig/postgresql.conf`，这样仅此附加组件可以访问，但您将需要通过 [Hassio SSH](https://developers.home-assistant.io/docs/operating-system/debugging/) 进行修改。

## 安装

该附加组件的安装非常简单，并且与安装任何其他附加组件没有不同。

1. 将我的附加组件库添加到您的 Home Assistant 实例中（在监督管理者附加组件商店右上角，或者如果您已配置我的 HA，请单击下面的按钮）
   [![打开您的 Home Assistant 实例，并显示添加附加组件仓库对话框，预先填写特定的仓库 URL。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装此附加组件。
1. 单击 `保存` 按钮以保存您的配置。
1. 将附加组件选项设置为您的偏好，至少需要 POSTGRES_PASSWORD。
1. 启动附加组件。
1. 检查附加组件的日志以查看是否一切正常。
1. 使用任何 Postgres 客户端进行连接，例如连接到 `homeassistant.local:5432`

## 支持

在 GitHub 上创建一个问题

[仓库]: https://github.com/alexbelgium/hassio-addons