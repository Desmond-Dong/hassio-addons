# Home assistant add-on: Fireflyiii data importer

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffireflyiii_data_importer%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffireflyiii_data_importer%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffireflyiii_data_importer%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_Thanks to everyone having starred my repo! To star it click on the image below, then it will be on top right. Thanks!_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![downloads evolution](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/fireflyiii_data_importer/stats.png)

## About

["Firefly III"](https://www.firefly-iii.org) 是一个（自托管）个人财务管理工具。它可以帮助您跟踪支出和收入，以便您减少开支并增加储蓄。数据导入器旨在帮助您将交易导入 Firefly III。出于安全和维护的原因，它与 Firefly III 分开。

此插件基于 Docker 镜像 https://hub.docker.com/r/fireflyiii/data-importer

## Configuration

阅读官方文档以了解如何设置变量：https://docs.firefly-iii.org/data-importer。

配置可以添加在 /addon_configs/xxx-fireflyiii_data_importer/configurations 文件夹中，根据：https://docs.firefly-iii.org/data-importer/help/config/。

通过在 /addon_configs/xxx-fireflyiii_data_importer/import_files 中添加文件，可以进行自动导入，根据：https://docs.firefly-iii.org/data-importer/usage/command_line/。

选项可以通过两种方式配置：

- 插件选项

```yaml
"CONFIG_LOCATION": config.yaml 的位置 # 设置 config.yaml 的位置（见下文）
"FIREFLY_III_ACCESS_TOKEN": 访问 Firefly 所需的令牌
"FIREFLY_III_CLIENT_ID": 访问 Firefly 的另一种方式
"FIREFLY_III_URL": 您的 URL，可以是本地（Docker IP），也可以是外部（公网 IP）
"NORDIGEN_ID": 您的 Nordigen 客户端 ID
"NORDIGEN_KEY": 您的 Nordigen 客户端密钥
"SPECTRE_APP_ID": 您的 Spectre / Salt Edge 客户端 ID
"SPECTRE_SECRET": 您的 Spectre / Salt Edge 客户端密钥
"Updates": 每小时|每天|每周 # 设置在 /config/addons_config/fireflyiii_data_importer/import_files 中设置的文件的自动上传
"silent": true # 抑制调试消息
```

- Config.yaml（高级用法）

通过在 config.yaml 中添加它们，可以按此指南将附加变量设置为 ENV 变量：https://github.com/alexbelgium/hassio-addons/wiki/Add%E2%80%90ons-feature-:-add-env-variables

ENV 变量的完整列表可以在此处查看：https://github.com/firefly-iii/data-importer/blob/main/.env.example

## Installation

此插件的安装非常简单，与其他插件的安装没有区别。

1. 将我的插件仓库添加到您的 Home Assistant 实例中（在 supervisor 插件商店的右上角，或点击下方按钮，如果您已配置我的 HA）
   [![打开您的 Home Assistant 实例并显示带有特定仓库 URL 预填的添加插件仓库对话框。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装此插件。
1. 点击 `Save` 按钮保存您的配置。
1. 设置插件选项以符合您的偏好。
1. 启动插件。
1. 检查插件的日志，查看是否一切正常。
1. 打开 WebUI 并调整软件选项

## Support

在 github 上创建问题

## Illustration

[repository]: https://github.com/alexbelgium/hassio-addons