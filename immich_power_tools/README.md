# Home assistant add-on: Immich Power Tools

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fimmich_power_tools%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fimmich_power_tools%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fimmich_power_tools%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢大家给我的仓库加星！要加星，请点击下面的图片，然后它就会出现在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载量趋势](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/immich_power_tools/stats.png)

## 关于

[Immich Power Tools](https://github.com/varun-raj/immich-power-tools) 提供了高级工具来组织和管理您的 Immich 照片库。这个插件扩展了 Immich 的功能，提供了强大的特性用于照片组织、分析和管理。

主要功能：
- 高级照片组织工具
- 照片管理的批量操作
- AI 驱动的照片分析和标记
- 使用 Google Maps 集成进行地理照片映射
- 重复检测和管理
- 高级搜索和过滤功能

这个插件基于 [immich-power-tools](https://github.com/varun-raj/immich-power-tools) 项目。

## 配置

Webui 可以在 `<你的IP>:8001` 找到。

### 选项

| 选项 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `IMMICH_URL` | 字符串 | **必需** | 内部 Immich 服务器 URL（例如，`http://homeassistant:3001`） |
| `EXTERNAL_IMMICH_URL` | 字符串 | **必需** | 用于浏览器访问的外部 Immich 服务器 URL |
| `IMMICH_API_KEY` | 字符串 | **必需** | 用于认证的 Immich API 密钥 |
| `DB_HOST` | 字符串 | **必需** | 数据库主机名（例如，`core-mariadb` 或 `homeassistant`） |
| `DB_USERNAME` | 字符串 | **必需** | 数据库用户名 |
| `DB_PASSWORD` | 字符串 | **必需** | 数据库密码 |
| `DB_DATABASE_NAME` | 字符串 | **必需** | 数据库名（通常是 `immich`） |
| `DB_PORT` | 字符串 | **必需** | 数据库端口（通常是 `5432` 用于 PostgreSQL） |
| `GOOGLE_MAPS_API_KEY` | 字符串 | | 用于地理功能的 Google Maps API 密钥 |
| `GEMINI_API_KEY` | 字符串 | | 用于 AI 功能的 Google Gemini API 密钥 |

### 示例配置

```yaml
IMMICH_URL: "http://homeassistant:3001"
EXTERNAL_IMMICH_URL: "https://your-immich-domain.com"
IMMICH_API_KEY: "your-immich-api-key-here"
DB_HOST: "core-mariadb"
DB_USERNAME: "immich"
DB_PASSWORD: "your-db-password"
DB_DATABASE_NAME: "immich"
DB_PORT: "5432"
GOOGLE_MAPS_API_KEY: "your-google-maps-api-key"
GEMINI_API_KEY: "your-gemini-api-key"
```

### 前置条件

在使用这个插件之前，请确保您已经：

1. **运行 Immich 服务器** - 这个插件需要一个正常工作的 Immich 安装
2. **数据库访问** - 您需要直接访问您的 Immich 数据库
3. **Immich API 密钥** - 从您的 Immich 管理面板生成 API 密钥

### 获取 API 密钥

**Immich API 密钥：**
1. 打开您的 Immich 网页界面
2. 转到 **管理** > **API 密钥**
3. 点击 **创建 API 密钥**
4. 复制生成的密钥

**Google Maps API 密钥**（可选）：
1. 访问 [Google Cloud Console](https://console.cloud.google.com/)
2. 创建一个新项目或选择一个现有项目
3. 启用 Maps JavaScript API
4. 创建凭证（API 密钥）

**Google Gemini API 密钥**（可选）：
1. 访问 [Google AI Studio](https://makersuite.google.com/app/apikey)
2. 为 Gemini 创建一个新的 API 密钥

### 自定义脚本和环境变量

这个插件支持通过 `addon_config` 映射自定义脚本和环境变量：

- **自定义脚本**：查看 [在插件中运行自定义脚本](https://github.com/alexbelgium/hassio-addons/wiki/Running-custom-scripts-in-Addons)
- **环境变量**：查看 [为您的插件添加环境变量](https://github.com/alexbelgium/hassio-addons/wiki/Add-Environment-variables-to-your-Addon)

## 安装

这个插件的安装过程非常简单，与安装任何其他 Hass.io 插件没有区别。

1. 将我的 Hass.io 插件仓库 [repository] 添加到您的 Hass.io 实例。
1. 安装这个插件。
1. 配置所有必需的数据库和 API 设置。
1. 点击 `保存` 按钮以保存您的配置。
1. 启动插件。
1. 检查插件的日志，看看是否一切正常。
1. 打开 WebUI 开始使用这些强大的工具。

## 支持

在 github 上创建问题，或访问 [home assistant 社区论坛](https://community.home-assistant.io/) 提问

更多关于 Immich Power Tools 的信息，请访问：https://github.com/varun-raj/immich-power-tools

[repository]: https://github.com/alexbelgium/hassio-addons