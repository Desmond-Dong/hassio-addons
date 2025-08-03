# Home assistant 添加组件：Immich OpenVINO

⚠️ 项目正在非常积极地开发中。预计会有错误和变化。不要将其作为存储您照片和视频的唯一方式！（来自开发者）

[![赞助][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![赞助][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fimmich_openvino%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fimmich_openvino%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fimmich_openvino%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建器)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有星标我的仓库的人！要星标它，请点击下面的图片，然后它就会在右上角。谢谢！_

[![星标者的仓库名单 for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载量变化](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/immich_openvino/stats.png)

## 关于

直接从您的手机上以 OpenVINO 硬件加速支持的方式自托管照片和视频备份解决方案。这是 Immich 的 OpenVINO 启用版本，它为使用 Intel GPU 和 CPU 的机器学习任务提供了硬件加速。

此添加组件基于 imagegenius 的 [docker 镜像](https://github.com/imagegenius/docker-immich)，并启用了 OpenVINO 支持，以在 Intel 硬件上增强性能。

## 硬件要求

- **Intel 硬件**：兼容的 Intel CPU 或 Intel 集成/离散 GPU
- **OpenVINO 支持**：具有 OpenVINO 工具兼容性的 Intel 硬件
- **架构**：仅 AMD64（OpenVINO 支持针对 Intel x86-64 架构进行了优化）
- **Intel GPU 驱动程序**：在主机系统上正确安装的 Intel GPU 驱动程序（如果使用 Intel GPU 加速）

## 配置

Web UI 位于 `<your-ip>:8080`。PostgreSQL 可以是内部的或外部的。

### 选项

| 选项 | 类型 | 默认值 | 描述 |
|------|------|--------|-------|
| `data_location` | 字符串 | `/share/immich` | Immich 数据存储的路径 |
| `library_location` | 字符串 | | 照片/视频库的路径 |
| `TZ` | 字符串 | | 时区（例如，`Europe/London`） |
| `localdisks` | 字符串 | | 要挂载的本地驱动器（例如，`sda1,sdb1,MYNAS`） |
| `networkdisks` | 字符串 | | 要挂载的 SMB 共享（例如，`//SERVER/SHARE`） |
| `cifsusername` | 字符串 | | SMB 共享的网络用户名 |
| `cifspassword` | 字符串 | | SMB 共享的网络密码 |
| `cifsdomain` | 字符串 | | SMB 共享的网络域 |
| `DB_HOSTNAME` | 字符串 | `homeassistant.local` | 数据库主机名 |
| `DB_USERNAME` | 字符串 | `postgres` | 数据库用户名 |
| `DB_PASSWORD` | 字符串 | `homeassistant` | 数据库密码 |
| `DB_DATABASE_NAME` | 字符串 | `immich` | 数据库名称 |
| `DB_PORT` | 整数 | `5432` | 数据库端口 |
| `DB_ROOT_PASSWORD` | 字符串 | | 数据库根密码 |
| `JWT_SECRET` | 字符串 | | 用于身份验证的 JWT 密钥 |
| `DISABLE_MACHINE_LEARNING` | 布尔值 | `false` | 禁用 ML 功能（不推荐用于 OpenVINO 版本） |
| `MACHINE_LEARNING_WORKERS` | 整数 | `1` | ML 工作线程的数量（可以使用 OpenVINO 增加数量） |
| `MACHINE_LEARNING_WORKER_TIMEOUT` | 整数 | `120` | ML 工作线程超时（秒） |

### 示例配置

```yaml
data_location: "/share/immich"
library_location: "/media/photos"
TZ: "Europe/London"
localdisks: "sda1,sdb1"
networkdisks: "//192.168.1.100/photos"
cifsusername: "photouser"
cifspassword: "password123"
DB_HOSTNAME: "core-mariadb"
DB_USERNAME: "immich"
DB_PASSWORD: "secure_password"
DB_DATABASE_NAME: "immich"
JWT_SECRET: "your-secret-key-here"
DISABLE_MACHINE_LEARNING: false
MACHINE_LEARNING_WORKERS: 2
MACHINE_LEARNING_WORKER_TIMEOUT: 180
```

### 挂载驱动器

此添加组件支持挂载本地驱动器和远程 SMB 共享：

- **本地驱动器**：参见 [在添加组件中挂载本地驱动器](https://github.com/alexbelgium/hassio-addons/wiki/Mounting-Local-Drives-in-Addons)
- **远程共享**：参见 [在添加组件中挂载远程共享](https://github.com/alexbelgium/hassio-addons/wiki/Mounting-remote-shares-in-Addons)

### 自定义脚本和环境变量

此添加组件通过 `addon_config` 映射支持自定义脚本和环境变量：

- **自定义脚本**：参见 [在添加组件中运行自定义脚本](https://github.com/alexbelgium/hassio-addons/wiki/Running-custom-scripts-in-Addons)
- **环境变量**：参见 [向您的添加组件添加环境变量](https://github.com/alexbelgium/hassio-addons/wiki/Add-Environment-variables-to-your-Addon)

## 安装

此添加组件的安装非常简单，与安装任何其他 Hass.io 添加组件没有区别。

**前提条件：**
- Intel CPU 或 Intel GPU 用于 OpenVINO 加速
- AMD64 架构（ARM 不支持）
- 安装了 Intel GPU 驱动程序（如果使用 Intel GPU 加速）

**步骤：**
1. 将我的 Hass.io 添加组件仓库 [repository] 添加到您的 Hass.io 实例。
1. 安装此添加组件。
1. 点击 `保存` 按钮以存储您的配置。
1. 启动添加组件。
1. 检查添加组件的日志，查看是否一切正常。
1. 仔细配置添加组件以满足您的偏好，请参阅官方文档进行配置。

**数据库设置：**
注意，您需要安装一个单独的 postgres 添加组件才能连接数据库。您可以在我的仓库中安装 postgres 添加组件。
注意在启动之前更改密码；之后将无法更改

## 支持

在 github 上创建问题，或在 [home assistant 论坛](https://community.home-assistant.io/t/home-assistant-addon-immich/282108/3) 上提问

[repository]: https://github.com/alexbelgium/hassio-addons