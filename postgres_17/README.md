## ⚠️ 开启问题 : [🐛 [Postgres 17] 与 TeslaMate 在 HomeAssistant 中的错误 (已开启 2025-07-09)](https://github.com/alexbelgium/hassio-addons/issues/1944) 由 [@cortesmario](https://github.com/cortesmario)
# Home assistant 插件：Postgres

![捐赠](https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white) ![捐赠](https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white)

![版本](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fpostgres%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fpostgres%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fpostgres%2Fconfig.json)

![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e) ![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base) ![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建器)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

感谢大家给我的仓库点赞！要点赞请点击下面的图片，然后它就会出现在右上角。谢谢！

![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg) ![下载趋势](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/postgres/stats.png)

## 关于

PostgreSQL，通常简称为 "Postgres"，是一个面向对象的数据库管理系统 (ORDBMS)，注重可扩展性和标准合规性。作为数据库服务器，其主要功能是安全地存储数据，支持最佳实践，并在其他软件应用程序（无论是同一台计算机上的应用程序还是跨网络（包括互联网）运行在其他计算机上的应用程序）请求时检索数据。它可以处理从小型单机应用程序到具有许多并发用户的大型面向互联网的应用程序的工作负载。最近的版本还提供了数据库本身的复制，以增强安全性和可扩展性。

此插件基于官方镜像：https://hub.docker.com/_/postgres

## 配置

Postgres 端口默认为 5432，并暴露给主机网络。

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

更多信息请参考 [基础镜像文档](https://hub.docker.com/_/postgres)。

默认情况下，`postgresql.conf` 存储在可被其他插件和 Home Assistant 访问的卷中，因此您可以通过例如 File Editor 插件方便地修改它。如果您更喜欢更好的安全性，请将 `CONFIG_LOCATION` 更改为例如 `/data/orig/postgresql.conf`，这样它将只能被此插件访问，但您将不得不通过 [Hassio SSH](https://developers.home-assistant.io/docs/operating-system/debugging/) 来修改它。

### 自定义脚本和环境变量

此插件支持通过 `addon_config` 映射的自定义脚本和环境变量：

- **自定义脚本**：请参阅 [在插件中运行自定义脚本](https://github.com/alexbelgium/hassio-addons/wiki/Running-custom-scripts-in-Addons)
- **环境变量**：请参阅 [向您的插件添加环境变量](https://github.com/alexbelgium/hassio-addons/wiki/Add-Environment-variables-to-your-Addon)

## 安装

此插件的安装非常简单，与其他插件的安装方式相同。

1. 将我的插件仓库添加到您的 Home Assistant 实例（在 supervisor 插件商店右上角，或点击下方按钮如果您已配置我的 HA）
   ![打开您的 Home Assistant 实例并显示带有特定仓库 URL 预填充的添加插件仓库对话框](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)
   ![打开您的 Home Assistant 实例并显示带有特定仓库 URL 预填充的添加插件仓库对话框](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装此插件。
2. 点击 `保存` 按钮以保存您的配置。
3. 设置插件选项以符合您的偏好，至少需要设置 `POSTGRES_PASSWORD`。
4. 启动插件。
5. 检查插件的日志以查看是否一切正常。
6. 使用任何 Postgres 客户端连接，例如连接到 `homeassistant.local:5432`。

从 postgres 15 迁移：

- 停止 postgres 15 插件
- 使用 Filebrowser 插件将数据库文件夹从 /addon_configs/xxx-postgres 复制到 /addon_configs/xxx-postgres_latest
- 启动 postgres 17 插件。数据库升级应该会继续。如果升级失败，您的数据仍然安全在 postgres 15 插件中

## 安全

默认情况下，Postgres 将在您的主机系统的本地网络上可达。为了提高安全性，您可以禁用此行为，并使 Postgres 仅对 Home Assistant 内的其他插件可用。

1. 配置所有使用 Postgres 的插件通过内部 DNS 名称连接：`db21ed7f-postgres-latest:5432`。
2. 转到 **设置 → 插件 → Postgres 17 → 配置**，在 **网络** 下，通过清除文本字段删除端口 `5432`。
3. 点击 **保存** 并重启插件。
4. 现在 Postgres 仅对其他插件可用，不再从本地网络（例如笔记本电脑、物联网设备等）可达。

## 支持

在 GitHub 上创建问题

[repository]: https://github.com/alexbelgium/hassio-addons