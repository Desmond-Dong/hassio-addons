# Home assistant add-on: Linkwarden

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Flinkwarden%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Flinkwarden%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Flinkwarden%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库加星标的人！要加星标，请点击下面的图片，然后它就会在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![downloads evolution](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/linkwarden/stats.png)

## 关于

[Linkwarden](https://linkwarden.app/) 是一个协作书签管理器，用于收集、组织和保存网页和文章。它允许团队和个人保存、分类和管理书签，具有标签、集合和全文搜索等功能。

这个插件基于 [官方的 Linkwarden Docker 镜像](https://github.com/linkwarden/linkwarden)。

## 配置

Webui 可以在 `<你的IP>:3000` 或通过 Ingress 在侧边栏中访问。
你需要在启动时创建一个新的用户账户。

### 选项

| 选项 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `NEXTAUTH_SECRET` | 字符串 | **必需** | NextAuth.js 认证的秘密密钥（必须在启动时填写） |
| `NEXTAUTH_URL` | 字符串 | | 自定义 NextAuth URL（可选，如果 Linkwarden 保持在外部） |
| `NEXT_PUBLIC_DISABLE_REGISTRATION` | 布尔值 | `false` | 禁用新用户注册 |
| `NEXT_PUBLIC_CREDENTIALS_ENABLED` | 布尔值 | `true` | 启用用户名/密码登录 |
| `STORAGE_FOLDER` | 字符串 | `/config/library` | 存储数据文件的目录 |
| `DATABASE_URL` | 字符串 | | 外部 PostgreSQL 数据库 URL（留空使用内部数据库） |
| `NEXT_PUBLIC_AUTHENTIK_ENABLED` | 布尔值 | `false` | 启用 Authentik SSO 集成 |
| `AUTHENTIK_CUSTOM_NAME` | 字符串 | `Authentik` | Authentik 按钮的自定义提供者名称 |
| `AUTHENTIK_ISSUER` | 字符串 | | Authentik OpenID 配置发行者 URL |
| `AUTHENTIK_CLIENT_ID` | 字符串 | | 来自 Authentik 提供者概览的客户端 ID |
| `AUTHENTIK_CLIENT_SECRET` | 字符串 | | 来自 Authentik 提供者概览的客户端密钥 |
| `NEXT_PUBLIC_OLLAMA_ENDPOINT_URL` | 字符串 | | 用于 AI 功能的 Ollama 端点 URL |
| `OLLAMA_MODEL` | 字符串 | | 用于 AI 处理的 Ollama 模型名称 |

### 示例配置

```yaml
NEXTAUTH_SECRET: "your-very-long-secret-key-here-at-least-32-characters"
NEXT_PUBLIC_DISABLE_REGISTRATION: false
NEXT_PUBLIC_CREDENTIALS_ENABLED: true
STORAGE_FOLDER: "/config/library"
DATABASE_URL: "postgresql://postgres:homeassistant@localhost:5432/linkwarden"
NEXT_PUBLIC_AUTHENTIK_ENABLED: false
AUTHENTIK_CUSTOM_NAME: "My Authentik"
AUTHENTIK_ISSUER: "https://authentik.my-domain.com/application/o/linkwarden"
AUTHENTIK_CLIENT_ID: "your-client-id"
AUTHENTIK_CLIENT_SECRET: "your-client-secret"
```

### 设置步骤

1. **首次设置**：启动插件后，访问 Web 界面并创建您的第一个用户账户
2. **NEXTAUTH_SECRET**：为 `NEXTAUTH_SECRET` 选项生成一个安全的随机字符串（至少 32 个字符）
3. **数据库**：默认情况下，Linkwarden 使用内部 SQLite 数据库。对于生产使用，请考虑设置 PostgreSQL
4. **认证**：如果您需要 SSO 功能，请配置 Authentik 集成
5. **存储**：书签数据和文件存储在配置的 `STORAGE_FOLDER` 中

### 自定义脚本和环境变量

此插件通过 `addon_config` 映射支持自定义脚本和环境变量：

- **自定义脚本**：请参阅 [在插件中运行自定义脚本](https://github.com/alexbelgium/hassio-addons/wiki/Running-custom-scripts-in-Addons)
- **环境变量**：请参阅 [向您的插件添加环境变量](https://github.com/alexbelgium/hassio-addons/wiki/Add-Environment-variables-to-your-Addon)

### Authentik 集成

要与 Authentik 进行 SSO 集成：

1. 按照 [Linkwarden 文档](https://docs.linkwarden.app/self-hosting/sso-oauth#authentik) 的说明进行操作
2. 将 `NEXT_PUBLIC_AUTHENTIK_ENABLED` 设置为 `true`
3. 使用来自您的 Authentik 提供者概览的值配置 Authentik 特定的选项
4. 注意：从 `AUTHENTIK_ISSUER` URL 中移除尾随的斜杠

### 额外配置

有关高级配置选项，请参阅 [Linkwarden 文档](https://docs.linkwarden.app/self-hosting/environment-variables) 中的完整环境变量列表。

## 安装

此插件的安装非常简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件仓库][repository] 添加到您的 Hass.io 实例。 [![在我的 Home Assistant 中添加仓库][repository-badge]][repository-url]
1. 安装此插件
1. 点击 `保存` 按钮以保存您的配置
1. 将 `NEXTAUTH_SECRET` 选项设置为安全的随机字符串
1. 根据需要配置其他选项
1. 启动插件
1. 检查插件的日志以查看是否一切正常
1. 打开 WebUI 并创建您的第一个用户账户

## 支持

在 github 上创建问题，或在 [home assistant 论坛](https://community.home-assistant.io/t/home-assistant-addon-linkwarden/279247) 上提问。

[repository]: https://github.com/alexbelgium/hassio-addons
[repository-badge]: https://img.shields.io/badge/Add%20repository%20to%20my-Home%20Assistant-41BDF5?logo=home-assistant&style=for-the-badge
[repository-url]: https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons

---

![illustration](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/linkwarden/illustration.png)