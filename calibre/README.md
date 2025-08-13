## 警告：打开问题 : [🐛 [Calibre] linuxserver/docker-calibre 的最新版本需要打开端口 8181 以通过 HTTPS 访问主桌面 GUI（已打开 2025-08-11）](https://github.com/alexbelgium/hassio-addons/issues/2027) 由 [@matthieudevipa](https://github.com/matthieudevipa)
# Home assistant 插件：calibre

![捐款](https://www.buymeacoffee.com/alexbelgium)
![捐款](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fcalibre%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fcalibre%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fcalibre%2Fconfig.json)

![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建器)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢大家给我的仓库点赞！要点赞，请点击下面的图片，然后它就会在右上角。谢谢！_

![@alexbelgium/hassio-addons 的星标者仓库列表](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载量变化](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/calibre/stats.png)

## 关于

---

[Calibre](https://calibre-ebook.com/) 是一个强大且易于使用的电子书管理器。用户说它非常出色，是必备工具。它几乎可以做到任何事情，并且超越了普通的电子书软件。它也是完全免费且开源的，非常适合休闲用户和计算机专家。

这个插件基于 Docker 镜像 https://github.com/linuxserver/docker-calibre

## 安装

---

这个插件的安装非常简单，与安装其他插件没有区别。

1. 将我的插件仓库添加到你的 Home Assistant 实例中（在 supervisor 插件商店的右上角，或者如果你已经配置了我的 HA，点击下面的按钮）
   ![打开你的 Home Assistant 实例并显示添加插件仓库对话框，其中预填了特定的仓库 URL。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装这个插件。
1. 点击 `保存` 按钮以保存你的配置。
1. 设置插件的选项以符合你的偏好。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 打开 WebUI 并调整软件选项。

## 配置

---

Webui 可以在 <http://homeassistant:PORT> 或通过 Ingress 在侧边栏中找到。
请阅读上游容器的文档以获取更多信息：https://github.com/linuxserver/docker-calibre#application-setup

**注意**：需要手动从桌面应用程序启用 Web 服务器和无线连接，分别使用端口 8081 和 9090。

### 选项

| 选项 | 类型 | 默认 | 描述 |
|------|------|------|------|
| `PGID` | int | `0` | 文件权限的组 ID |
| `PUID` | int | `0` | 文件权限的用户 ID |
| `TZ` | str | | 时区（例如，`Europe/London`） |
| `PASSWORD` | str | | 可选的 GUI 访问密码 |
| `CLI_ARGS` | str | | 可选的 Calibre 启动 CLI 参数 |
| `localdisks` | str | | 要挂载的本地驱动器（例如，`sda1,sdb1,MYNAS`） |
| `networkdisks` | str | | 要挂载的 SMB 共享（例如，`//SERVER/SHARE`） |
| `cifsusername` | str | | SMB 共享的网络用户名 |
| `cifspassword` | str | | SMB 共享的网络密码 |
| `cifsdomain` | str | | SMB 共享的网络域 |

### 示例配置

```yaml
PGID: 0
PUID: 0
TZ: "Europe/London"
PASSWORD: "secure-password"
CLI_ARGS: "--with-library=/books"
localdisks: "sda1,sdb1"
networkdisks: "//192.168.1.100/books"
cifsusername: "bookuser"
cifspassword: "password123"
cifsdomain: "workgroup"
```

### 挂载驱动器

这个插件支持挂载本地驱动器和远程 SMB 共享：

- **本地驱动器**：见 [在插件中挂载本地驱动器](https://github.com/alexbelgium/hassio-addons/wiki/Mounting-Local-Drives-in-Addons)
- **远程共享**：见 [在插件中挂载远程共享](https://github.com/alexbelgium/hassio-addons/wiki/Mounting-remote-shares-in-Addons)

### 自定义脚本和环境变量

这个插件通过 `addon_config` 映射支持自定义脚本和环境变量：

- **自定义脚本**：见 [在插件中运行自定义脚本](https://github.com/alexbelgium/hassio-addons/wiki/Running-custom-scripts-in-Addons)
- **环境变量**：见 [为你的插件添加环境变量](https://github.com/alexbelgium/hassio-addons/wiki/Add-Environment-variables-to-your-Addon)

## 支持

在 github 上创建问题

## 插图

---

![插图](https://calibre.com/img/slider/artistdetails.png)

[repository]: https://github.com/alexbelgium/hassio-addons