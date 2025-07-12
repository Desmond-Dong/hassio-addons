# Home assistant add-on: Photoprism

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fphotoprism%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fphotoprism%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fphotoprism%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

所需最小配置：2核CPU和4GB内存

_感谢所有给我的仓库点赞的人！要点赞，请点击下面的图片，然后它将在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载量趋势](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/photoprism/stats.png)

## 关于

一个基于服务器的应用程序，用于浏览、组织和共享您的个人照片集。

项目主页：https://github.com/photoprism/photoprism

基于的Docker镜像：https://hub.docker.com/r/photoprism/photoprism

## 安装

这个插件的安装非常简单，与安装任何其他Hass.io插件的方法相同。

1. [将我的Hass.io插件仓库][repository]添加到您的Hass.io实例。
1. 安装这个插件。
1. 点击“保存”按钮以保存您的配置。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 仔细配置插件以满足您的偏好，请参阅官方文档。

## 配置

默认用户：admin
默认密码：请更改密码

要访问WebDAV，请使用URL：http://local-ip:addon-port/api/hassio.../originals
第二部分（/api.../originals）在启动插件时会在日志中描述

选项可以通过两种方式配置：

- 插件选项

```yaml
ssl: true/false
certfile: fullchain.pem #ssl证书，必须位于/ssl
keyfile: privkey.pem #sslkeyfile，必须位于/ssl
DB_TYPE: "list(sqlite|mariadb_addon|external)" # Mariadb在插件安装时自动配置，sqlite不需要配置
localdisks: sda1 #将您的驱动器的硬件名称输入，用逗号分隔，或其标签。例如。sda1, sdb1, MYNAS...
networkdisks: "//SERVER/SHARE" #可选，要挂载的smb服务器列表，用逗号分隔
cifsusername: "username" #可选，smb用户名，所有smb共享相同
cifspassword: "password" #可选，smb密码
cifsdomain: "domain" #可选，允许为smb共享设置域
ingress_disable: false #可选，如果为true则禁用ingress，并简化访问的URL为IP:port
UPLOAD_NSFW: "true" 允许上传可能冒犯性的内容
STORAGE_PATH: "/share/photoprism/storage" #缓存、数据库和sidecar文件的存储路径
ORIGINALS_PATH: "/share/photoprism/originals" #包含您的照片和视频收藏的原始路径
IMPORT_PATH: "/share/photoprism/import" #导入文件到原始的路径
BACKUP_PATH: "/share/photoprism/backup" #备份存储路径
CONFIG_LOCATION: "/config/addons_config/config.yaml" #设置config.yaml的位置（见下文）
```

- Config.yaml

通过自定义位于 /config/addons_config/config.yaml 的 config.yaml 来进行配置

完整的选项列表可以在这里查看：https://github.com/photoprism/photoprism/blob/develop/docker-compose.yml

- 外部数据库设置 (@wesleygas)

允许使用外部数据库。这可以通过正确设置 addons_config/photoprism/config.yaml 文件上的以下选项来完成：

```yaml
PHOTOPRISM_DATABASE_DRIVER: "mysql"
PHOTOPRISM_DATABASE_SERVER: "IP:PORT"
PHOTOPRISM_DATABASE_NAME: "photoprism"
PHOTOPRISM_DATABASE_USER: "USERNAME"
PHOTOPRISM_DATABASE_PASSWORD: "PASSWORD
```
## 使用 Photoprism 命令行界面

Photoprism 还提供了一个命令行界面：

https://docs.photoprism.app/getting-started/docker-compose/#command-line-interface

您可以通过Portainer插件或执行 `docker exec -it <photoprism container id> bash` 通过_ssh_ 访问它。

:warning: 不要使用 `docker exec <photoprism container id> photoprism`，因为这会导致不可预测的行为。

## 插图

![1622396210_840_560](https://user-images.githubusercontent.com/44178713/127819841-2281ac79-ea96-4b41-9704-522957c5b9c3.jpg)

## 支持

在github上创建问题

[repository]: https://github.com/alexbelgium/hassio-addons