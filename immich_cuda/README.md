# Home assistant add-on: Immich CUDA

⚠️ 项目正在非常活跃地开发中。请预期存在错误和变化。不要将其作为存储您照片和视频的唯一方式！（来自开发者）

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fimmich_cuda%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fimmich_cuda%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fimmich_cuda%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我仓库点赞的人！要点赞，请点击下面的图片，然后它就会出现在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![downloads evolution](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/immich_cuda/stats.png)

## 关于

从您的手机直接进行照片和视频备份的解决方案，并支持CUDA硬件加速。这是支持CUDA的Immich版本，它为使用NVIDIA GPU进行机器学习任务提供了硬件加速。

此插件基于 [docker镜像](https://github.com/imagegenius/docker-immich) 的imagegenius，并启用了CUDA支持以增强性能。

## 硬件要求

- **NVIDIA GPU**: 兼容的NVIDIA显卡，支持CUDA
- **CUDA驱动程序**: NVIDIA驱动程序必须在主机系统上正确安装
- **架构**: 仅支持AMD64（ARM架构不支持CUDA）

## 配置

Webui位于 `<your-ip>:8080`。PostgreSQL可以是内部的或外部的。

### 选项

| 选项 | 类型 | 默认值 | 描述 |
|------|------|--------|-------|
| `data_location` | str | `/share/immich` | Immich数据存储的路径 |
| `library_location` | str | | 照片/视频库的路径 |
| `TZ` | str | | 时区（例如，`Europe/London`） |
| `localdisks` | str | | 要挂载的本地驱动器（例如，`sda1,sdb1,MYNAS`） |
| `networkdisks` | str | | 要挂载的SMB共享（例如，`//SERVER/SHARE`） |
| `cifsusername` | str | | SMB网络共享的用户名 |
| `cifspassword` | str | | SMB网络共享的密码 |
| `cifsdomain` | str | | SMB网络共享的域 |
| `DB_HOSTNAME` | str | `homeassistant.local` | 数据库主机名 |
| `DB_USERNAME` | str | `postgres` | 数据库用户名 |
| `DB_PASSWORD` | str | `homeassistant` | 数据库密码 |
| `DB_DATABASE_NAME` | str | `immich` | 数据库名称 |
| `DB_PORT` | int | `5432` | 数据库端口 |
| `DB_ROOT_PASSWORD` | str | | 数据库根密码 |
| `JWT_SECRET` | str | | 用于认证的JWT密钥 |
| `DISABLE_MACHINE_LEARNING` | bool | `false` | 禁用ML功能（不推荐用于CUDA版本） |
| `MACHINE_LEARNING_WORKERS` | int | `1` | ML工作者的数量（可以使用CUDA增加） |
| `MACHINE_LEARNING_WORKER_TIMEOUT` | int | `120` | ML工作者超时（秒） |
| `skip_permissions_check` | bool | `false` | 跳过文件权限检查 |

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

此插件支持挂载本地驱动器和远程SMB共享：

- **本地驱动器**: 参考 [在插件中挂载本地驱动器](https://github.com/alexbelgium/hassio-addons/wiki/Mounting-Local-Drives-in-Addons)
- **远程共享**: 参考 [在插件中挂载远程共享](https://github.com/alexbelgium/hassio-addons/wiki/Mounting-remote-shares-in-Addons)

### 自定义脚本和环境变量

此插件通过 `addon_config` 映射支持自定义脚本和环境变量：

- **自定义脚本**: 参考 [在插件中运行自定义脚本](https://github.com/alexbelgium/hassio-addons/wiki/Running-custom-scripts-in-Addons)
- **环境变量**: 参考 [为您的插件添加环境变量](https://github.com/alexbelgium/hassio-addons/wiki/Add-Environment-variables-to-your-Addon)

## 安装

此插件的安装非常简单，与安装任何其他Hass.io插件没有区别。

**前提条件:**
- 支持CUDA的NVIDIA GPU
- 主机上安装了NVIDIA驱动程序
- AMD64架构（不支持ARM）

**步骤:**
1. [将我的Hass.io插件仓库][repository]添加到您的Hass.io实例。
1. 安装此插件。
1. 点击“保存”按钮以存储您的配置。
1. 启动插件。
1. 检查插件的日志，看看是否一切顺利。
1. 小心配置插件以满足您的偏好，请参考官方文档进行配置。

**数据库设置:**
注意，您需要安装一个单独的postgres插件才能连接数据库。您可以在我的仓库中安装postgres插件。
注意，在启动之前更改密码；之后将无法更改

## 支持

在github上创建问题，或在 [home assistant线程](https://community.home-assistant.io/t/home-assistant-addon-immich/282108/3) 上提问

[repository]: https://github.com/alexbelgium/hassio-addons