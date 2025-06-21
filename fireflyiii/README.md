## &#9888; 打开问题 : [🐛 [Firefly iii] 运行缓慢 (打开于2025-06-09)](https://github.com/alexbelgium/hassio-addons/issues/1891) by [@jandechent](https://github.com/jandechent)
# 家庭助理插件: fireflyiii

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffireflyiii%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffireflyiii%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffireflyiii%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的库星标的人！要星标，请点击下面的图片，然后它会出现在右上角。谢谢！_

[![星标者仓库名册 @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/fireflyiii/stats.png)

## 关于

["Firefly III"](https://www.firefly-iii.org) 是一个（自托管）个人财务管理器。它可以帮助你跟踪你的支出和收入，从而帮助你少花钱，多存钱。
这个插件基于 docker 镜像 https://hub.docker.com/r/fireflyiii/core

## 配置

首次启动前请更改你的 APP_KEY！否则在重置数据库之前将无法使用。

可以通过两种方式配置选项：

- 插件选项

```yaml
"CONFIG_LOCATION": config.yaml 的位置 # 设置 config.yaml 的位置（见下文）
"DB_CONNECTION": "list(sqlite_internal|mariadb_addon|mysql|pgsql)" # 定义要使用的数据库类型：sqlite（默认，嵌入在插件中）；MariaDB（如果安装并运行 MariaDB 插件则自动检测），以及需要设置其他 DB_ 字段的外部数据库（mysql 和 pgsql）
"APP_KEY": 32 个字符 # 这是你的加密密钥，请妥善保管！
"DB_HOST": "CHANGEME" # 仅在使用远程数据库时需要
"DB_PORT": "CHANGEME" # 仅在使用远程数据库时需要
"DB_DATABASE": "CHANGEME" # 仅在使用远程数据库时需要
"DB_USERNAME": "CHANGEME" # 仅在使用远程数据库时需要
"DB_PASSWORD": "CHANGEME" # 仅在使用远程数据库时需要
"Updates": hourly|daily|weekly # 设置自动更新
"silent": true # 如果为 false，则显示调试信息
```

- Config.yaml（高级用法）

可以通过在插件选项定义的位置中的 config.yaml 中添加这些变量，作为 ENV 变量，具体参考此指南：https://github.com/alexbelgium/hassio-addons/wiki/Add%E2%80%90ons-feature-:-add-env-variables

ENV 变量的完整列表可以在这里查看：https://raw.githubusercontent.com/firefly-iii/firefly-iii/main/.env.example

## 安装

这个插件的安装相当简单，与安装其他插件没有区别。

1. 将我的插件库添加到你的家庭助理实例中（在超级用户插件商店的右上角，或者如果你已经配置了我的 HA，可以点击下面的按钮）
   [![打开你的家庭助理实例并显示添加插件库对话框，特定的库 URL 自动填充。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装此插件。
1. 点击 `保存` 按钮以存储你的配置。
1. 根据你的喜好设置插件选项
1. 启动插件。
1. 检查插件的日志以查看一切是否正常。
1. 打开 webUI 并调整软件选项

## 支持

在 GitHub 上创建一个问题

## 插图

![插图](https://raw.githubusercontent.com/firefly-iii/firefly-iii/develop/.github/assets/img/imac-complete.png)

[repository]: https://github.com/alexbelgium/hassio-addons