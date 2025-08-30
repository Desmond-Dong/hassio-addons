# Home assistant add-on: Lidarr

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Flidarr%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Flidarr%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Flidarr%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库星标的人！要星标它，请点击下面的图片，它将在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载趋势](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/lidarr/stats.png)

## 关于

---

[Lidarr](https://lidarr.audio/) 是一个用于 Usenet 和 BitTorrent 用户的音乐收藏管理器。它可以监控多个 RSS 源，以获取您最喜欢的艺术家的最新专辑，并与客户端和索引器接口，以获取、排序和重命名它们。它还可以配置为在更好的质量格式可用时自动升级库中现有文件的质量。
此插件基于以下 Docker 镜像：https://github.com/linuxserver/docker-lidarr

## 安装

---

此插件的安装非常简单，与安装任何其他插件没有区别。

1. 将我的插件仓库添加到您的 home assistant 实例中（在 supervisor 插件商店的右上角，或如果您已配置我的 HA，请点击下面的按钮）
   [![打开您的 Home Assistant 实例并显示带有特定仓库 URL 预填的添加插件仓库对话框。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装此插件。
1. 点击 `保存` 按钮以保存您的配置。
1. 设置插件选项以符合您的偏好
1. 启动插件。
1. 检查插件的日志，以查看是否一切正常。
1. 打开 WebUI 并调整软件选项

## 配置

Webui 可以在 <http://homeassistant:PORT> 或通过 Ingress 侧边栏找到。
配置可以通过应用程序 WebUI 进行，但以下选项除外。

### 选项

| 选项 | 类型 | 默认 | 描述 |
|------|------|------|------|
| `PGID` | int | `0` | 文件权限的组 ID |
| `PUID` | int | `0` | 文件权限的用户 ID |
| `TZ` | str | | 时区（例如，`Europe/London`） |
| `localdisks` | str | | 要挂载的本地驱动器（例如，`sda1,sdb1,MYNAS`） |
| `networkdisks` | str | | 要挂载的 SMB 共享（例如，`//SERVER/SHARE`） |
| `cifsusername` | str | | 网络共享的 SMB 用户名 |
| `cifspassword` | str | | 网络共享的 SMB 密码 |
| `cifsdomain` | str | | 网络共享的 SMB 域 |

### 示例配置

```yaml
PGID: 0
PUID: 0
TZ: "Europe/London"
localdisks: "sda1,sdb1"
networkdisks: "//192.168.1.100/downloads,//nas.local/music"
cifsusername: "mediauser"
cifspassword: "password123"
cifsdomain: "workgroup"
```

### 挂载驱动器

此插件支持挂载本地驱动器和远程 SMB 共享：

- **本地驱动器**：请参阅 [在插件中挂载本地驱动器](https://github.com/alexbelgium/hassio-addons/wiki/Mounting-Local-Drives-in-Addons)
- **远程共享**：请参阅 [在插件中挂载远程共享](https://github.com/alexbelgium/hassio-addons/wiki/Mounting-remote-shares-in-Addons)

## 支持

在 github 上创建问题

## 插图

---

![插图](https://www.geekzone.fr/wp-content/uploads/2018/05/lidarr_1.png)

[repository]: https://github.com/alexbelgium/hassio-addons