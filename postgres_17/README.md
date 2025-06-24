# Home assistant 插件：Postgres

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fpostgres%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fpostgres%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fpostgres%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建者](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库点星的人！要点星请点击下方图片，然后它会出现在右上角。谢谢！_

[![Stars 为 @alexbelgium/hassio-addons 的仓库名单](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/postgres/stats.png)

## 关于

PostgreSQL，通常简称为 "Postgres"，是一个以可扩展性和标准合规性为重点的对象关系数据库管理系统 (ORDBMS)。作为一个数据库服务器，它的主要功能是安全地存储数据并支持最佳实践，以便在其他软件应用程序请求时进行检索，无论是同一台计算机上的应用程序还是通过网络（包括互联网）在另一台计算机上运行的应用程序。它可以处理从小型单机应用到大型面向互联网的应用程序的工作负载，支持多个并发用户。最近的版本还提供数据库自身的复制功能，以增强安全性和可扩展性。

这个插件基于官方镜像： https://hub.docker.com/_/postgres

## 配置

Postgres 的默认端口是 5432，并暴露给主机网络。

默认用户： `postgres`
密码： `由 POSTGRES_PASSWORD 设置`

您可以配置以下选项：
```yaml
POSTGRES_PASSWORD
POSTGRES_USER
POSTGRES_DB
POSTGRES_INITDB_ARGS
POSTGRES_HOST_AUTH_METHOD
```
有关更多信息，请查看 [基础镜像文档](https://hub.docker.com/_/postgres)。

默认情况下，`postgresql.conf` 存储在可被其他插件和 Home Assistant 访问的卷中，因此您可以方便地通过例如文件编辑器插件进行修改。如果您更喜欢更好的安全性，请将 `CONFIG_LOCATION` 更改为例如 `/data/orig/postgresql.conf`，这样仅该插件可以访问，但您将需要通过 [Hassio SSH](https://developers.home-assistant.io/docs/operating-system/debugging/) 进行修改。

## 安装

此插件的安装非常简单，与安装任何其他插件没有区别。

1. 将我的插件库添加到您的 Home Assistant 实例中（在右上角的监督员插件商店中，或者如果您已配置我的 HA，请点击下面的按钮）
   [![打开您的 Home Assistant 实例并显示添加插件库对话框，特定的库 URL 预先填写。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
2. 安装此插件。
3. 点击 `保存` 按钮以保存您的配置。
4. 根据您的喜好设置插件选项，至少需要 POSTGRES_PASSWORD。
5. 启动插件。
6. 检查插件的日志以查看是否一切正常。
7. 使用任何 Postgres 客户端连接，例如连接到 `homeassistant.local:5432`

## 支持

在 GitHub 上创建一个问题

[仓库]: https://github.com/alexbelgium/hassio-addons