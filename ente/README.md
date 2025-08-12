# Home assistant add-on: Ente

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fente%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fente%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fente%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我仓库点赞的人！点击下面的图片点赞，它就会出现在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![downloads evolution](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/ente/stats.png)

## 关于

---

[Ente](https://github.com/ente-io/ente) 是一个自托管、端到端加密的照片和视频存储解决方案。这个插件提供了一个完整的 Ente 服务器设置，包括博物馆 API 服务器和 MinIO S3 兼容的存储后端。

Ente 提供：
- 端到端加密的照片和视频备份
- 人脸识别和搜索
- 跨平台的移动和桌面应用程序
- 从移动设备自动备份照片
- 与家人和朋友共享相册
- 通过自托管完全控制您的数据

这个插件基于官方 Ente 服务器：https://github.com/ente-io/ente/tree/main/server

## 配置

---

Webui 可以在 <http://homeassistant:PORT> 找到。

### 选项

| 选项 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `ENTE_ENDPOINT_URL` | 字符串 | `http://homeassistant.local:8280` | Ente API 将可访问的 URL |
| `MINIO_ROOT_USER` | 字符串 | `minioadmin` | MinIO 根用户名 |
| `MINIO_ROOT_PASSWORD` | 字符串 | `minioadmin` | MinIO 根密码 |
| `MINIO_DATA_LOCATION` | 字符串 | `/config/minio-data` | MinIO 存储数据的路径 |
| `DB_PASSWORD` | 字符串 | `ente` | 内部 PostgreSQL 数据库的密码 |
| `DISABLE_WEB_UI` | 布尔值 | `true` | 禁用 Web UI（使用移动/桌面应用程序） |
| `USE_EXTERNAL_DB` | 布尔值 | `false` | 使用外部 PostgreSQL 数据库 |
| `TZ` | 字符串 | `Europe/Paris` | 时区设置 |

### 外部数据库配置

如果您想使用外部 PostgreSQL 数据库，设置 `USE_EXTERNAL_DB: true` 并配置：

| 选项 | 类型 | 描述 |
|------|------|------|
| `DB_HOSTNAME` | 字符串 | PostgreSQL 服务器主机名 |
| `DB_PORT` | 整数 | PostgreSQL 服务器端口（默认：5432） |
| `DB_USERNAME` | 字符串 | PostgreSQL 用户名 |
| `DB_DATABASE_NAME` | 字符串 | PostgreSQL 数据库名 |

### 示例配置

```yaml
ENTE_ENDPOINT_URL: "http://homeassistant.local:8280"
MINIO_ROOT_USER: "myuser"
MINIO_ROOT_PASSWORD: "mypassword"
MINIO_DATA_LOCATION: "/config/ente-storage"
DB_PASSWORD: "securepassword"
DISABLE_WEB_UI: false
TZ: "America/New_York"
```

### 自定义脚本和环境变量

这个插件支持通过 `addon_config` 映射自定义脚本和环境变量：

- **自定义脚本**：见 [在插件中运行自定义脚本](https://github.com/alexbelgium/hassio-addons/wiki/Running-custom-scripts-in-Addons)
- **环境变量**：见 [向您的插件添加环境变量](https://github.com/alexbelgium/hassio-addons/wiki/Add-Environment-variables-to-your-Addon)

### 挂载驱动器

这个插件支持挂载本地驱动器和远程 SMB 共享：

- **本地驱动器**：见 [在插件中挂载本地驱动器](https://github.com/alexbelgium/hassio-addons/wiki/Mounting-Local-Drives-in-Addons)
- **远程共享**：见 [在插件中挂载远程共享](https://github.com/alexbelgium/hassio-addons/wiki/Mounting-remote-shares-in-Addons)

## 安装

---

这个插件的安装非常简单，与安装其他插件没有区别。

1. 将我的插件仓库添加到您的 home assistant 实例（在 supervisor 插件商店的右上角，或者如果您已配置我的 HA，点击下面的按钮）
   [![打开您的 Home Assistant 实例并显示添加插件仓库对话框，并预填特定的仓库 URL。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装这个插件。
1. 点击 `保存` 按钮保存您的配置。
1. 设置插件选项以符合您的偏好。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。

## 首次设置

---

首次启动插件后：

1. 从以下链接下载 Ente 移动应用程序：
   - [iOS App Store](https://apps.apple.com/app/ente-photos/id1542026904)
   - [Google Play Store](https://play.google.com/store/apps/details?id=io.ente.photos)
   - [F-Droid](https://f-droid.org/packages/io.ente.photos.fdroid/)

2. 在应用程序设置期间，选择 "使用自定义服务器" 并输入您的插件 URL：`http://your-homeassistant-ip:8280`

3. 使用移动应用程序创建新账户

4. **重要**：对于自托管实例，订阅代码不能通过电子邮件发送。检查插件日志以获取验证码：
   ```
   验证码：xxxxxx
   ```

5. 使用日志中的验证码完成账户设置

## 端口

插件公开三个端口：

- **8300** (3000/tcp)：Ente Web UI（如果启用）
- **8280** (8080/tcp)：Ente API 服务器（博物馆）- 应用程序的主要端点
- **8320** (3200/tcp)：MinIO S3 端点（用于存储后端）

## 数据存储

默认情况下，照片和视频存储在 `/config/minio-data`。您可以使用 `MINIO_DATA_LOCATION` 选项更改此位置或挂载外部存储以获得更大的容量。

插件包括：
- PostgreSQL 数据库用于元数据
- MinIO S3 兼容存储用于实际的照片/视频
- Ente 博物馆 API 服务器用于客户端通信

## 备份建议

为了数据安全，定期备份：
- `/config/minio-data`（或您的自定义存储位置）- 包含所有照片/视频
- PostgreSQL 数据库（由插件自动处理）
- 插件配置

## 支持

在 github 上创建问题

[repository]: https://github.com/alexbelgium/hassio-addons