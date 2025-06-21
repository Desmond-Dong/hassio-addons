# Home assistant 插件：Radarr

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fradarr%2Fconfig.json)
![进入](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fradarr%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fradarr%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库加星的朋友！点击下方图片给它加星，之后它会出现在右上角。谢谢！_

[![Star数统计](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/radarr/stats.png)

## 关于

---

[Radarr](https://radarr.video/)是一个用于Usenet和BitTorrent用户的电影集合管理器。它可以监控多个RSS源以获取新电影，并将与客户端和索引器接口，以抓取、排序和重命名它们。它还可以配置为在库中存在更高质量格式时，自动升级现有文件的质量。
此插件基于docker镜像 https://github.com/linuxserver/docker-radarr

## 安装

---

此插件的安装非常简单，与安装任何其他插件没有区别。

1. 将我的插件库添加到您的Home Assistant实例中（在右上角的主管插件商店中，或如果您已配置我的HA，请点击下方按钮）
   [![打开您的Home Assistant实例并显示带有特定存储库URL预填充的添加插件库对话框。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
2. 安装此插件。
3. 点击 `保存` 按钮以存储您的配置。
4. 根据您的偏好设置插件选项
5. 启动插件。
6. 检查插件的日志以查看是否一切正常。
7. 打开WebUI并调整软件选项

## 配置

---

WebUI可以在 <http://homeassistant:PORT> 找到。
默认用户名/密码：在启动日志中描述。
可以通过应用程序的WebUI进行配置，除了以下选项：

```yaml
PGID: user
GPID: user
TZ: timezone
localdisks: sda1 #请输入您要挂载的驱动器的硬件名称，用逗号分隔，或其标签。例如：sda1, sdb1, MYNAS...
networkdisks: "//SERVER/SHARE" # 可选，列出要挂载的smb服务器，用逗号分隔
cifsusername: "username" # 可选，smb用户名，所有smb共享相同
cifspassword: "password" # 可选，smb密码
connection_mode: ingress_noauth (默认，禁用身份验证以允许无缝进入集成)，noingress_auth（禁用进入以允许更简单的外部URL，启用身份验证），ingress_auth（同时启用进入和身份验证）
```

## 支持

在GitHub上创建问题

## 插图

---

![插图](https://dausruddin.com/wp-content/uploads/2020/05/radarr-v3-1024x515.png)

[仓库]: https://github.com/alexbelgium/hassio-addons