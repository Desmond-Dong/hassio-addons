## ⚠️ Open Request : [✨ [REQUEST] [Joplin] Add Ingress (opened 2025-06-15)](https://github.com/alexbelgium/hassio-addons/issues/1913) by [@aluavin](https://github.com/aluavin)
# Home assistant add-on: Joplin

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fjoplin%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fjoplin%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fjoplin%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢大家给我的仓库点赞！点击下面的图片为仓库点赞，它就会出现在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![downloads evolution](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/joplin/stats.png)

## 关于

Joplin Server 是一个免费、开源的笔记和待办事项同步应用程序，它可以处理大量笔记并将其组织成笔记本。
使用此服务器，您可以在所有设备上同步所有笔记。

感谢 @poudenes 帮助开发！

项目主页：https://github.com/laurent22/joplin

基于的 Docker 镜像：https://hub.docker.com/r/etechonomy/joplin-server

## 安装

这个插件的安装非常简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件仓库][repository]添加到您的 Hass.io 实例。
1. 安装此插件。
1. 点击“保存”按钮以保存您的配置。
1. 启动插件。
1. 检查插件的日志以查看是否一切顺利。
1. 仔细配置插件以符合您的偏好，请参考官方文档进行配置。

## 配置

Web UI 位于 <http://homeassistant:port>

```yaml
APP_BASE_URL: 这是服务运行的基础公共 URL。例如，如果您希望它从 https://example.com/joplin 运行，这是您应该设置的 URL。基础 URL 可以包括端口。
```

要使用现有的 PostgreSQL 服务器，请在配置中设置以下变量：
确保提供的数据库和用户存在，因为服务器将不会创建它们。

```yaml
DB_CLIENT=pg
POSTGRES_PASSWORD=joplin
POSTGRES_DATABASE=joplin
POSTGRES_USER=joplin
POSTGRES_PORT=5432
POSTGRES_HOST=localhost
```

要使用电子邮件服务，请在配置中设置以下变量：

```yaml
1 = true, 0 = false
MAILER_HOST=mail.example.com
MAILER_PORT=995
MAILER_SECURITY=none, tls, starttls
MAILER_AUTH_USER=info@example.com
MAILER_AUTH_PASSWORD=your_password
MAILER_NOREPLY_NAME=from_name
MAILER_NOREPLY_EMAIL=from_email
MAILER_ENABLED=1
```

## 支持

在 github 上创建问题

[repository]: https://github.com/alexbelgium/hassio-addons