# Home assistant add-on: Fireflyiii data importer

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffireflyiii_data_importer%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffireflyiii_data_importer%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffireflyiii_data_importer%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库点赞的人！要点赞，请点击下面的图片，然后它就会在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载量趋势](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/fireflyiii_data_importer/stats.png)

## 关于

["Firefly III"](https://www.firefly-iii.org) 是一个（自托管）的个人财务管理工具。它可以帮助您跟踪支出和收入，以便您少花钱多储蓄。数据导入器旨在帮助您将交易导入 Firefly III。出于安全和维护的原因，它与 Firefly III 分开。

此插件基于 Docker 镜像 https://hub.docker.com/r/fireflyiii/data-importer

## 配置

Webui 可以在 <http://homeassistant:3474> 找到。

### 设置

1. 确保您有一个正在运行的 Firefly III 实例
2. 配置数据导入器以连接到您的 Firefly III 安装
3. 根据需要设置导入配置和文件

有关完整设置文档，请参阅：https://docs.firefly-iii.org/data-importer

### 选项

| 选项 | 类型 | 必需 | 描述 |
|------|------|------|------|
| `FIREFLY_III_URL` | str | 是 | 您的 Firefly III 实例的 URL |
| `FIREFLY_III_ACCESS_TOKEN` | str | 是 | Firefly III 的个人访问令牌 |
| `CONFIG_LOCATION` | str | 是 | 配置文件的位置 |
| `FIREFLY_III_CLIENT_ID` | str | 否 | OAuth 客户端 ID（访问令牌的替代方案） |
| `NORDIGEN_ID` | str | 否 | Nordigen 客户端 ID 用于银行集成 |
| `NORDIGEN_KEY` | str | 否 | Nordigen 客户端密钥 |
| `SPECTRE_APP_ID` | str | 否 | Spectre/Salt Edge 客户端 ID |
| `SPECTRE_SECRET` | str | 否 | Spectre/Salt Edge 客户端密钥 |
| `AUTO_IMPORT_SECRET` | str | 否 | 自动导入 webhook 的密钥 |
| `CAN_POST_AUTOIMPORT` | bool | 否 | 允许自动导入功能 |
| `CAN_POST_FILES` | bool | 否 | 允许文件上传 |
| `Updates` | list | 否 | 自动导入计划（每小时、每天、每周） |
| `silent` | bool | 否 | 抑制调试消息 |

### 示例配置

```yaml
FIREFLY_III_URL: "http://homeassistant:8082"
FIREFLY_III_ACCESS_TOKEN: "your-access-token-here"
CONFIG_LOCATION: "/config"
NORDIGEN_ID: "your-nordigen-id"
NORDIGEN_KEY: "your-nordigen-key"
Updates: ["daily"]
silent: false
```

### 文件位置

- **配置文件**：`/addon_configs/xxx-fireflyiii_data_importer/configurations/`
  - 在这里存储导入配置文件
  - 查看：https://docs.firefly-iii.org/data-importer/help/config/

- **导入文件**：`/addon_configs/xxx-fireflyiii_data_importer/import_files/`
  - 在这里放置 CSV 文件以进行自动导入
  - 查看：https://docs.firefly-iii.org/data-importer/usage/command_line/

### 获取 Firefly III 访问令牌

1. 登录到您的 Firefly III 实例
2. 转到选项 → 个人资料 → OAuth → 个人访问令牌
3. 创建一个新的令牌，并赋予适当的权限
4. 复制令牌并在 `FIREFLY_III_ACCESS_TOKEN` 选项中使用它

### 自定义脚本和环境变量

此插件通过 `addon_config` 映射支持自定义脚本和环境变量：

- **自定义脚本**：查看 [在插件中运行自定义脚本](https://github.com/alexbelgium/hassio-addons/wiki/Running-custom-scripts-in-Addons)
- **环境变量**：查看 [为您的插件添加环境变量](https://github.com/alexbelgium/hassio-addons/wiki/Add-Environment-variables-to-your-Addon)

## 安装

此插件的安装非常简单，与安装任何其他插件没有区别。

1. 将我的插件仓库添加到您的 home assistant 实例（在 supervisor 插件商店的右上角，或者如果您已经配置了我的 HA，请点击下面的按钮）
   [![打开您的 Home Assistant 实例并显示添加插件仓库对话框，其中包含特定的仓库 URL 预填充。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装此插件。
1. 点击 `保存` 按钮以保存您的配置。
1. 设置插件选项以符合您的偏好
1. 启动插件。
1. 检查插件的日志，看看是否一切正常。
1. 打开 WebUI 并调整软件选项

## 支持

在 github 上创建问题

## 插图

[repository]: https://github.com/alexbelgium/hassio-addons