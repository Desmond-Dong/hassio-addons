# Home Assistant 插件：Fireflyiii 数据导入器

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffireflyiii_data_importer%2Fconfig.json)
![访问权限](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffireflyiii_data_importer%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffireflyiii_data_importer%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库加星的人！要加星请点击下方图像，然后它将显示在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/fireflyiii_data_importer/stats.png)

## 关于

["Firefly III"](https://www.firefly-iii.org) 是一款（自托管的）个人财务管理器。它可以帮助你跟踪支出和收入，从而可以减少开支并增加储蓄。数据导入器的构建旨在帮助你将交易导入 Firefly III。它与 Firefly III 分开是出于安全和维护的考虑。

此插件基于 Docker 镜像 https://hub.docker.com/r/fireflyiii/data-importer

## 配置

请阅读官方文档以获取有关如何设置变量的信息：https://docs.firefly-iii.org/data-importer。

可以在 /addon_configs/xxx-fireflyiii_data_importer/configurations 文件夹中根据以下信息添加配置：https://docs.firefly-iii.org/data-importer/help/config/

通过在 /addon_configs/xxx-fireflyiii_data_importer/import_files 中添加文件可以进行自动导入，具体请参见：https://docs.firefly-iii.org/data-importer/usage/command_line/

选项可以通过两种方式配置：

- 插件选项

```yaml
"CONFIG_LOCATION": config.yaml 的位置 # 设置 config.yaml 的位置（见下文）
"FIREFLY_III_ACCESS_TOKEN": 访问 Firefly 所需
"FIREFLY_III_CLIENT_ID": 访问 Firefly 的替代方式
"FIREFLY_III_URL": 你的 URL，既可以是本地（docker IP），也可以是外部（公用 IP）
"NORDIGEN_ID": 你的 Nordigen 客户端 ID
"NORDIGEN_KEY": 你的 Nordigen 客户端密钥
"SPECTRE_APP_ID": 你的 Spectre / Salt Edge 客户端 ID
"SPECTRE_SECRET": 你的 Spectre / Salt Edge 客户端密钥
"Updates": hourly|daily|weekly # 设置在 /config/addons_config/fireflyiii_data_importer/import_files 中指定文件的自动上传
"silent": true # 抑制调试信息
```

- Config.yaml（高级用法）

可以通过在插件选项中定义的位置的 config.yaml 中添加它们将附加变量设置为 ENV 变量，详细请参考本指南：https://github.com/alexbelgium/hassio-addons/wiki/Add%E2%80%90ons-feature-:-add-env-variables

完整的 ENV 变量列表请参见：https://github.com/firefly-iii/data-importer/blob/main/.env.example

## 安装

此插件的安装非常简单，与安装任何其他插件没有区别。

1. 将我的插件库添加到您的 Home Assistant 实例（在超级管理员插件商店右上角，或者如果您已经配置了我的 HA，请点击下方按钮）
   [![打开你的 Home Assistant 实例，并显示添加插件库对话框，预填充特定的库 URL。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
2. 安装此插件。
3. 点击 `保存` 按钮以存储您的配置。
4. 根据您的喜好设置插件选项
5. 启动插件。
6. 检查插件的日志以查看一切是否正常。
7. 打开 webUI 并调整软件选项

## 支持

在 GitHub 上创建一个问题

## 插图

[repository]: https://github.com/alexbelgium/hassio-addons