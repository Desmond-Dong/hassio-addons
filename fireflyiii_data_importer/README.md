# Home assistant add-on: Fireflyiii 数据导入器

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffireflyiii_data_importer%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffireflyiii_data_importer%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffireflyiii_data_importer%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建者](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建者)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/给我买杯咖啡%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/通过Paypal给我买杯咖啡-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库加星的人！要加星请点击下面的图片，然后它会在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/fireflyiii_data_importer/stats.png)

## 关于

["Firefly III"](https://www.firefly-iii.org) 是一个（自托管）个人财务管理器。它可以帮助你跟踪你的支出和收入，从而使你花费更少，存更多。数据导入器是为了帮助你将交易导入 Firefly III。出于安全和维护的原因，它与 Firefly III 分开。

此附加组件基于 Docker 镜像 https://hub.docker.com/r/fireflyiii/data-importer

## 配置

请阅读官方文档了解如何设置变量：https://docs.firefly-iii.org/data-importer。

配置可以根据 https://docs.firefly-iii.org/data-importer/help/config/ 添加到 /addon_configs/xxx-fireflyiii_data_importer/configurations 文件夹中。

通过将文件添加到 /addon_configs/xxx-fireflyiii_data_importer/import_files，可以进行自动导入，具体见：https://docs.firefly-iii.org/data-importer/usage/command_line/

选项可以通过两种方式配置：

- 附加组件选项

```yaml
"CONFIG_LOCATION": config.yaml 的位置 # 设置 config.yaml 的位置（见下文）
"FIREFLY_III_ACCESS_TOKEN": 访问 Firefly 必需的
"FIREFLY_III_CLIENT_ID": 访问 Firefly 的替代方式
"FIREFLY_III_URL": 你的 URL，可以是本地（docker IP）或外部（公用 IP）
"NORDIGEN_ID": 你的 Nordigen 客户端 ID
"NORDIGEN_KEY": 你的 Nordigen 客户端密钥
"SPECTRE_APP_ID": 你的 Spectre / Salt Edge 客户端 ID
"SPECTRE_SECRET": 你的 Spectre / Salt Edge 客户端密钥
"Updates": 每小时|每日|每周 # 设置 /config/addons_config/fireflyiii_data_importer/import_files 中文件的自动上传
"silent": true # 抑制调试消息
```

- Config.yaml（高级用法）

可以通过在配置选项定义的位置的 config.yaml 中将其作为 ENV 变量设置额外变量，详情请参见这个指南：https://github.com/alexbelgium/hassio-addons/wiki/Add%E2%80%90ons-feature-:-add-env-variables

ENV 变量的完整列表可以在此查看：https://github.com/firefly-iii/data-importer/blob/main/.env.example

## 安装

此附加组件的安装非常简单，与安装任何其他附加组件没有什么不同。

1. 将我的附加组件库添加到你的 Home Assistant 实例（在助手附加组件商店右上角，或者如果你已配置我的 HA，请点击下面的按钮）
   [![打开你的 Home Assistant 实例并显示添加附加组件库对话框，带有预填充的特定库 URL。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
2. 安装此附加组件。
3. 点击 `保存` 按钮以保存你的配置。
4. 根据个人喜好设置附加组件选项。
5. 启动附加组件。
6. 检查附加组件的日志以查看一切是否正常。
7. 打开 webUI 并调整软件选项。

## 支持

在 GitHub 上创建一个问题。

## 插图

[repository]: https://github.com/alexbelgium/hassio-addons