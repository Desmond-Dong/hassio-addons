# Hass.io Add-ons: Tandoor Recipes

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ftandoor_recipes%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ftandoor_recipes%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ftandoor_recipes%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有将我的仓库标为星标的人！要标星，请点击下面的图片，然后它将出现在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载趋势](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/tandoor_recipes/stats.png)

## 关于

[Tandoor recipes](https://github.com/TandoorRecipes/recipes)，由 [vabene1111](https://github.com/vabene1111) 制作，旨在供那些拥有食谱集合并希望与家人和朋友分享或简单地以整齐的方式存储它们的人使用。存在基本的权限系统，但此应用程序不打算作为公共页面运行。

## 配置

Webui 可以在 <http://homeassistant:PORT> 或通过 Ingress 侧边栏访问。
配置可以通过应用程序的 WebUI 进行，但以下选项除外。

有关 Ingress 支持的信息，请参阅：https://community.home-assistant.io/t/ingress-access-for-tandoor-recipes/717859
完整文档：https://docs.tandoor.dev/install/docker/

### 选项

| 选项 | 类型 | 默认值 | 描述 |
|------|------|--------|-------|
| `SECRET_KEY` | 字符串 | `YOUR_SECRET_KEY` | **必需**：Django 密钥用于安全 |
| `ALLOWED_HOSTS` | 字符串 | | **必需**：用于 Ingress 的逗号分隔的 Home Assistant URL |
| `DB_TYPE` | 列表 | `sqlite` | 数据库类型（sqlite 或 postgresql_external） |
| `DEBUG` | 列表 | `0` | 调试模式（0=正常，1=调试） |
| `externalfiles_folder` | 字符串 | | 用于外部食谱文件导入的文件夹 |
| `POSTGRES_HOST` | 字符串 | | PostgreSQL 主机（postgresql_external 所需） |
| `POSTGRES_PORT` | 字符串 | | PostgreSQL 端口（postgresql_external 所需） |
| `POSTGRES_USER` | 字符串 | | PostgreSQL 用户名（postgresql_external 所需） |
| `POSTGRES_PASSWORD` | 字符串 | | PostgreSQL 密码（postgresql_external 所需） |
| `POSTGRES_DB` | 字符串 | | PostgreSQL 数据库名称（postgresql_external 所需） |

### 示例配置

```yaml
SECRET_KEY: "your-very-long-secret-key-here"
ALLOWED_HOSTS: "homeassistant.local,192.168.1.100"
DB_TYPE: "sqlite"
DEBUG: "0"
externalfiles_folder: "/config/addons_config/tandoor_recipes/externalfiles"
# 对于外部 PostgreSQL：
# POSTGRES_HOST: "core-postgres"
# POSTGRES_PORT: "5432"
# POSTGRES_USER: "tandoor"
# POSTGRES_PASSWORD: "secure_password"
# POSTGRES_DB: "tandoor_recipes"
```

## 安装

此插件的安装非常简单，与其他 Hass.io 插件安装没有区别。

1. [将我的 Hass.io 插件仓库][repository]添加到您的 Hass.io 实例。
1. 安装此插件。
1. 点击 `保存` 按钮以保存您的配置。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 仔细配置插件以符合您的偏好，请参阅官方文档以获取详细信息。

## 支持

如果您在安装中遇到问题，请务必查看 GitHub。

## 截图

![image](https://github.com/TandoorRecipes/recipes/raw/develop/docs/preview.png)

[repository]: https://github.com/alexbelgium/hassio-addons

## 外部食谱文件
目录 /config/addons_config/tandoor_recipes/externalfiles 可用于将外部文件导入 Tandoor。您可以将此映射到 Docker 中的 /opt/recipes/externalfiles。
根据以下说明：https://docs.tandoor.dev/features/external_recipes/