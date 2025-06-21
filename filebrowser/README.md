## &#9888; 打开问题 : [🐛 [文件浏览器] HA Core 在上传 2 个文件后挂起 (创建于 2025-06-06)](https://github.com/alexbelgium/hassio-addons/issues/1884) by [@UplandJacob](https://github.com/UplandJacob)
# Home Assistant 附加组件: 文件浏览器

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffilebrowser%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffilebrowser%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffilebrowser%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20代码%20基础)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/请%20我%20喝杯%20咖啡%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/请%20我%20喝杯%20咖啡%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的 repo 点赞的人！要点亮它，请点击下方的图片，然后它会在右上角显示。谢谢！_

[![@alexbelgium/hassio-addons 的星标者 repository 名单](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/filebrowser/stats.png)

## 关于

基于网页的 [文件浏览器](https://filebrowser.org/)。
该附加组件基于来自 filebrowser 的 [docker 镜像](https://hub.docker.com/r/filebrowser/filebrowser)。

## 配置

Webui 可以在 <http://homeassistant:port> 找到，端口是你在附加组件选项中映射到 8080 的端口。
默认用户名：“admin”，密码：“admin”

网络磁盘挂载到 `/share/storagecifs`。

```yaml
ssl: true/false
certfile: fullchain.pem # ssl 证书
keyfile: privkey.pem # ssl key file
NoAuth: true/false # 移除密码。更改时重置数据库。
disable_thumbnails : true/false (设置 disable_thumbnails 为 true 或 false；默认 true 以加快速度)
localdisks: sda1 # 输入要挂载的驱动器的硬件名称，以逗号分隔，或其标签。例：sda1, sdb1, MYNAS...
networkdisks: "//SERVER/SHARE" # 可选，要挂载的 smbv2/3 服务器列表，逗号分隔
cifsusername: "用户名" # 可选，smb 用户名，所有 smb 共享相同
cifspassword: "密码" # 可选，smb 密码，所有 smb 共享相同
base_folder: 根文件夹 # 可选，默认为 /
```

## 安装

此附加组件的安装非常简单，与安装其他 Hass.io 附加组件没有区别。

1. [将我的 Hass.io 附加组件仓库][repository] 添加到你的 Hass.io 实例。 [![在我的 Home Assistant 上添加仓库][repository-badge]][repository-url]
1. 安装此附加组件。
1. 点击 `保存` 按钮以保存你的配置。
1. 启动附加组件。
1. 检查附加组件的日志以查看一切是否顺利。
1. 仔细配置附加组件以满足你的需求，请参见 [官方文档](https://filebrowser.org/configuration) 以获取详情。

## 支持

在 GitHub 上创建一个问题，或在 [Home Assistant 论坛](https://community.home-assistant.io/t/home-assistant-addon-filebrowser/282108/3) 上询问。

[repository]: https://github.com/alexbelgium/hassio-addons
[repository-badge]: https://img.shields.io/badge/将%20仓库%20添加%20到%20我的-Home%20Assistant-41BDF5?logo=home-assistant&style=for-the-badge
[repository-url]: https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons
[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg