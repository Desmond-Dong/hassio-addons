# Hass.io 添加组件：Tandoor 菜谱

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ftandoor_recipes%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=入口&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ftandoor_recipes%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ftandoor_recipes%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建者](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建者)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库点赞的人！要点赞，请点击下面的图片，然后它将出现在右上角。谢谢！_

[![@alexbelgium/hassio-addons 的星标者仓库名册](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载量趋势](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/tandoor_recipes/stats.png)

## 关于

[Tandoor 菜谱](https://github.com/TandoorRecipes/recipes)，由 [vabene1111](https://github.com/vabene1111) 制作，旨在供那些拥有菜谱收藏并希望与家人和朋友分享或简单以整齐的方式存储的人们使用。存在基本的权限系统，但此应用程序不打算作为公共页面运行。

## 配置

Webui 可以在 <http://homeassistant:PORT> 或通过侧边栏使用入口找到。
配置可以通过应用程序的 WebUI 进行，但以下选项除外。

有关入口支持的更多信息，请参阅：https://community.home-assistant.io/t/ingress-access-for-tandoor-recipes/717859
完整文档：https://docs.tandoor.dev/install/docker/

### 选项

| 选项 | 类型 | 默认值 | 描述 |
|------|------|--------|-------|
| `SECRET_KEY` | 字符串 | `YOUR_SECRET_KEY` | **必需**：Django 密钥用于安全 |
| `ALLOWED_HOSTS` | 字符串 | | **必需**：用逗号分隔的 Home Assistant URL 用于入口 |
| `DB_TYPE` | 列表 | `sqlite` | 数据库类型（sqlite 或 postgresql_external） |
| `DEBUG` | 列表 | `0` | 调试模式（0=正常，1=调试） |
| `externalfiles_folder` | 字符串 | | 用于外部菜谱文件导入的文件夹 |
| `POSTGRES_HOST` | 字符串 | | PostgreSQL 主机（postgresql_external 所需） |
| `POSTGRES_PORT` | 字符串 | | PostgreSQL 端口（postgresql_external 所需） |
| `POSTGRES_USER` | 字符串 | | PostgreSQL 用户名（postgresql_external 所需） |
| `POSTGRES_PASSWORD` | 字符串 | | PostgreSQL 密码（postgresql_external 所需） |
| `POSTGRES_DB` | 字符串 | | PostgreSQL 数据库名（postgresql_external 所需） |
| `AI_MODEL_NAME` | 字符串 | | 用于配置 LLM，支持的提供者可以在 [这里](https://docs.litellm.ai/docs/providers/) 找到 |
| `AI_API_KEY` | 字符串 | | 用于访问 LLM 的 API 密钥 |
| `AI_RATELIMIT` | 整数 | | LLM 访问的速率限制 |

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
# AI_MODEL_NAME: "anthropic/claude-4"
# AI_API_KEY: "SECRET KEY"
```

## 安装

此添加组件的安装非常简单，与安装任何其他 Hass.io 添加组件没有区别。

1. [将我的 Hass.io 添加组件仓库][repository] 添加到您的 Hass.io 实例。
1. 安装此添加组件。
1. 点击 `保存` 按钮以保存您的配置。
1. 启动添加组件。
1. 检查添加组件的日志，查看是否一切正常。
1. 仔细配置添加组件以符合您的偏好，请参阅官方文档以获取更多信息。

## 支持

如果您在安装过程中遇到问题，请务必查看 github。

## 截图

![image](https://github.com/TandoorRecipes/recipes/raw/develop/docs/preview.png)

[repository]: https://github.com/alexbelgium/hassio-addons

## 外部菜谱文件
目录 /config/addons_config/tandoor_recipes/externalfiles 可用于将外部文件导入 Tandoor。您可以将此映射到 Docker 中的 /opt/recipes/externalfiles。
按照这里的指示：https://docs.tandoor.dev/features/external_recipes/