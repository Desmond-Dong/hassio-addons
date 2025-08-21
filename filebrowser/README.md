# Home assistant add-on: Filebrowser

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffilebrowser%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffilebrowser%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffilebrowser%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我仓库加星标的人！要加星标，请点击下面的图片，它将出现在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![downloads evolution](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/filebrowser/stats.png)

## 关于

基于 Web 的文件管理界面，提供了一种安全的方式，用于浏览、上传、下载、编辑和管理您的 Home Assistant 系统上的文件。Filebrowser 提供了一个干净、现代的界面，通过 Web 浏览器处理文件，支持多种文件格式、预览功能和全面的文件操作。

此插件基于官方 Filebrowser 项目的 [docker 镜像](https://hub.docker.com/r/filebrowser/filebrowser)。

## 安装

此插件的安装非常简单，与安装任何其他 Home Assistant 插件没有区别。

1. 将我的 Home Assistant 插件仓库 [repository] 添加到您的 Home Assistant 实例中。
1. 安装此插件。
1. 点击 `保存` 按钮以保存您的配置。
1. 启动插件。
1. 检查插件的日志，看看是否一切正常。
1. 通过侧边栏或 `<your-ip>:8071` 访问 Web UI。

## 配置

Web UI 可以在 `<your-ip>:8071` 或通过使用 Ingress 的 Home Assistant 侧边栏找到。

**默认凭证：**
- 用户名：`admin`
- 密码：`admin`

**重要：** 首次登录后立即更改默认凭证以增强安全性。

### 选项

| 选项 | 类型 | 默认值 | 描述 |
|------|------|--------|-------|
| `ssl` | bool | `false` | 启用 Web 界面的 HTTPS |
| `certfile` | str | `fullchain.pem` | SSL 证书文件（在 `/ssl/` 中） |
| `keyfile` | str | `privkey.pem` | SSL 私有密钥文件（在 `/ssl/` 中） |
| `NoAuth` | bool | `true` | 禁用身份验证（更改时重置数据库） |
| `disable_thumbnails` | bool | `true` | 禁用缩略图生成以提高性能 |
| `base_folder` | str | *(可选)* | 文件浏览器的根文件夹（默认为所有映射文件夹） |
| `localdisks` | str | *(可选)* | 挂载的本地驱动器（例如，`sda1,sdb1,MYNAS`） |
| `networkdisks` | str | *(可选)* | 要挂载的 SMB 共享（例如，`//SERVER/SHARE`） |
| `cifsusername` | str | *(可选)* | SMB 网络共享的用户名 |
| `cifspassword` | str | *(可选)* | SMB 网络共享的密码 |
| `cifsdomain` | str | *(可选)* | SMB 网络共享的域 |

### 示例配置

```yaml
ssl: true
certfile: "fullchain.pem"
keyfile: "privkey.pem"
NoAuth: false
disable_thumbnails: false
base_folder: "/share"
localdisks: "sda1,sdb1"
networkdisks: "//192.168.1.100/files,//nas.local/documents"
cifsusername: "fileuser"
cifspassword: "password123"
cifsdomain: "workgroup"
```

## 设置

1. 启动插件并等待其初始化。
1. 通过 Home Assistant 侧边栏或 `<your-ip>:8071` 访问 Web 界面。
1. 使用默认凭证登录：
   - 用户名：`admin`
   - 密码：`admin`
1. **重要：** 通过点击 "设置" > "用户管理" 立即更改默认密码。
1. 通过 Web 界面配置您的首选设置。
1. 如果禁用身份验证 (`NoAuth: true`)，将跳过登录屏幕。

### 挂载驱动器

此插件支持挂载本地驱动器和远程 SMB 共享：

- **本地驱动器**：参见 [在插件中挂载本地驱动器](https://github.com/alexbelgium/hassio-addons/wiki/Mounting-Local-Drives-in-Addons)
- **远程共享**：参见 [在插件中挂载远程共享](https://github.com/alexbelgium/hassio-addons/wiki/Mounting-remote-shares-in-Addons)

### 自定义脚本和环境变量

此插件支持通过 `addon_config` 映射的自定义脚本和环境变量：

- **自定义脚本**：参见 [在插件中运行自定义脚本](https://github.com/alexbelgium/hassio-addons/wiki/Running-custom-scripts-in-Addons)
- **环境变量**：参见 [为您的插件添加环境变量](https://github.com/alexbelgium/hassio-addons/wiki/Add-Environment-variables-to-your-Addon)

## 支持

在 GitHub 上创建问题，或在 [Home Assistant 社区线程](https://community.home-assistant.io/t/home-assistant-addon-filebrowser/282108/3) 上提问。

[repository]: https://github.com/alexbelgium/hassio-addons
[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg