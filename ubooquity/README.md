# Home assistant add-on: Ubooquity

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fubooquity%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=入口&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fubooquity%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fubooquity%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我仓库星标的人！要给星标，请点击下面的图片，然后它将出现在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![downloads evolution](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/ubooquity/stats.png)

## 关于

---

[Ubooquity by vaemendis](https://vaemendis.net/ubooquity/) 是一个免费、轻量级且易于使用的家庭服务器，用于存储您的漫画和电子书。这个插件基于 [docker 镜像](https://github.com/linuxserver/docker-ubooquity) 来自 [linuxserver.io](https://www.linuxserver.io/)。

Ubooquity 支持多种文件类型，尤其偏好 ePUB、CBZ、CBR 和 PDF 文件。它还支持来自图书馆管理软件 Calibre 和 ComicRack 的元数据。Ubooquity 允许您创建用户帐户并为每个共享文件夹设置访问权限。

这个插件有几个可配置的选项：

- 允许挂载本地外部驱动器，或从插件中挂载 SMB 共享（会降低性能）
- **非常重要，可能会导致系统崩溃**：设置 Java 的最大内存使用量。分配给 Ubooquity 的内存量取决于您运行它的硬件。如果这个量太小，您可能会在执行内存密集型操作时饱和它，并会得到 "java.lang.OutOfMemoryError: Java heap space" 错误。如果分配的量过高，系统可能会崩溃，您需要手动重启。值是以兆字节为单位的数字（只需输入数字，不要加 MB）。

建议启用 OPDS 服务器选项，然后您可以通过移动应用连接到您的漫画/电子书服务器（我在 iOS 上使用 [Chunky](https://apps.apple.com/fr/app/chunky-comic-reader/id663567628)（付费），Android 上使用 [Kuboo](https://play.google.com/store/apps/details?id=com.sethchhim.kuboo&hl=fr&gl=US)（免费））

## 安装

这个插件的安装非常简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件仓库][repository] 添加到您的 Hass.io 实例中。
2. 安装这个插件。
3. 点击 `保存` 按钮以保存您的配置。
4. 启动插件。
5. 检查插件的日志，看看是否一切正常。
6. 打开 WebUI，设置管理员密码并调整管理选项

## 配置

WebUI 可以在 <http://homeassistant:PORT> 或通过入口使用。

默认的用户名/密码在启动日志中描述。配置可以通过 WebUI 应用进行，除了以下选项。

### 选项

| 选项 | 类型 | 默认值 | 描述 |
|------|------|--------|-------|
| `PGID` | 整数 | `0` | 文件权限的组 ID |
| `PUID` | 整数 | `0` | 文件权限的用户 ID |
| `TZ` | 字符串 | | 时区（例如，`Europe/London`） |
| `maxmem` | 整数 | `200` | Java 的最大内存使用量（MB） - **关键设置** |
| `ssl` | 布尔值 | `false` | 为 Web 界面启用 HTTPS |
| `certfile` | 字符串 | `fullchain.pem` | TLS 证书的路径 |
| `keyfile` | 字符串 | `privkey.pem` | TLS 密钥文件的路径 |
| `theme` | 列表 | `default` | 主题选择（default/comixology2/plextheme-master） |
| `localdisks` | 字符串 | | 要挂载的本地驱动器（例如，`sda1,sdb1,MYNAS`） |
| `networkdisks` | 字符串 | | 要挂载的 SMB 共享（例如，`//SERVER/SHARE`） |
| `cifsusername` | 字符串 | | SMB 共享的网络用户名 |
| `cifspassword` | 字符串 | | SMB 共享的网络密码 |
| `cifsdomain` | 字符串 | | SMB 共享的网络域 |
| `smbv1` | 布尔值 | `false` | 启用 SMB v1 协议 |

**重要提示**：`maxmem` 设置控制 Java 堆空间。太低会导致 OutOfMemoryError；太高可能会导致 Home Assistant 崩溃。对于具有 2GB+ RAM 的系统，建议默认为 200MB。

### 示例配置

```yaml
PGID: 0
PUID: 0
TZ: "Europe/London"
maxmem: 512
ssl: false
certfile: "fullchain.pem"
keyfile: "privkey.pem"
theme: "comixology2"
localdisks: "sda1,sdb1"
networkdisks: "//192.168.1.100/comics,//nas.local/books"
cifsusername: "comicuser"
cifspassword: "password123"
cifsdomain: "workgroup"
smbv1: false
```

### 挂载驱动器

这个插件支持挂载本地驱动器和远程 SMB 共享：

- **本地驱动器**：参见 [在插件中挂载本地驱动器](https://github.com/alexbelgium/hassio-addons/wiki/Mounting-Local-Drives-in-Addons)
- **远程共享**：参见 [在插件中挂载远程共享](https://github.com/alexbelgium/hassio-addons/wiki/Mounting-remote-shares-in-Addons)

网络磁盘挂载到 `/mnt/share_name`。

## 支持

在 [repository github][repository] 上创建问题，或在 [home assistant 论坛](https://community.home-assistant.io/t/home-assistant-addon-ubooquity/283811) 上提问

## 插图

---

![alt text](https://vaemendis.net/ubooquity/data/images/screenshots/books_library.jpg)

[repository]: https://github.com/alexbelgium/hassio-addons