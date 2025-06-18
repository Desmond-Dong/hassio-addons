# Home Assistant 插件：Fireflyiii 数据导入器

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffireflyiii_data_importer%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffireflyiii_data_importer%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffireflyiii_data_importer%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库加星的人！要加星，请点击下面的图片，然后它会在右上角显示。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/fireflyiii_data_importer/stats.png)

## 关于

["Firefly III"](https://www.firefly-iii.org) 是一个（自托管的）个人财务管理工具。它可以帮助您跟踪支出和收入，以便您能减少开支并增加储蓄。数据导入器旨在帮助您将交易导入 Firefly III。出于安全和维护的原因，它与 Firefly III 分离。

此插件基于 Docker 映像 https://hub.docker.com/r/fireflyiii/data-importer

## 配置

请阅读官方文档以获取有关如何设置变量的信息：https://docs.firefly-iii.org/data-importer。

配置可以添加到 /addon_configs/xxx-fireflyiii_data_importer/configurations 文件夹中，具体请参考：https://docs.firefly-iii.org/data-importer/help/config/

可以通过以下两种方式进行自动导入：

- 插件选项

```yaml
"CONFIG_LOCATION": config.yaml 的位置 # 设置 config.yaml 的位置（见下文）
"FIREFLY_III_ACCESS_TOKEN": 访问 Firefly 所需
"FIREFLY_III_CLIENT_ID": 访问 Firefly 的替代方式
"FIREFLY_III_URL": 您的 URL，既可以是本地（Docker IP），也可以是外部（公共 IP）
"NORDIGEN_ID": 您的 Nordigen 客户端 ID
"NORDIGEN_KEY": 您的 Nordigen 客户端密钥
"SPECTRE_APP_ID": 您的 Spectre / Salt Edge 客户端 ID
"SPECTRE_SECRET": 您的 Spectre / Salt Edge 客户端密钥
"Updates": hourly|daily|weekly # 设置定期上传位于 /config/addons_config/fireflyiii_data_importer/import_files 中的文件
"silent": true # 抑制调试消息
```

- Config.yaml（高级使用）

可以通过在配置 YAML 中设置额外变量为 ENV 变量，具体参见此指南：https://github.com/alexbelgium/hassio-addons/wiki/Add%E2%80%90ons-feature-:-add-env-variables

完整的 ENV 变量列表可以在这里查看：https://github.com/firefly-iii/data-importer/blob/main/.env.example

## 安装

此插件的安装非常简单，与安装任何其他插件没有不同。

1. 将我的插件库添加到您的 Home Assistant 实例中（在监视器插件商店右上方，或者如果您已经配置了我的 HA，请点击下面的按钮）
   [![打开您的 Home Assistant 实例并显示添加插件库对话框，特定库 URL 预填。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装此插件。
1. 点击 `保存` 按钮以保存您的配置。
1. 根据您的偏好设置插件选项。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 打开 webUI 并调整软件选项。

## 支持

在 GitHub 上创建一个问题

## 插图

[repository]: https://github.com/alexbelgium/hassio-addons