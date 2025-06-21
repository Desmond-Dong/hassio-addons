## &#9888; 打开问题 : [🐛 [Portainer] 无法登录/创建容器/进入容器等 (打开于 2025-05-26)](https://github.com/alexbelgium/hassio-addons/issues/1877) by [@Joriex](https://github.com/Joriex)

# Home Assistant 插件: Portainer

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fportainer%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fportainer%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fportainer%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

从以下地址分支: https://github.com/hassio-addons/addon-portainer
实现的更改 : 更新到最新版本；入口；ssl；通过插件选项设置密码；允许手动覆盖

_感谢所有给我的仓库加星的人！要加星，请点击下面的图片，然后它将出现在右上角。谢谢！_

[![Star获得者的repo目录 @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/portainer/stats.png)

## 关于

---

Portainer是一个开源的轻量级管理用户界面，它允许你轻松管理你的Docker主机或Docker集群。

管理Docker从未如此简单。Portainer提供了Docker的详细概述，并允许你管理容器、镜像、网络和卷。

## 恢复备份

打开插件选项，将密码设置为空。重新启动插件，它将允许从备份中恢复Portainer。你需要将备份放在一个可访问的文件夹中，例如/share，以便在插件中挂载。

## 警告

Portainer插件确实非常强大，并且几乎可以访问你整个系统。虽然这个插件是在小心和安全考虑下创建和维护的，但在错误或没有经验的手中，它可能会损坏你的系统。

## 安装

---

安装这个插件相当简单，与安装任何其他插件没有区别。

1. 将我的插件库添加到你的Home Assistant实例中（在监督器插件商店的右上角，或者如果你已经配置了我的HA，则点击下面的按钮）
   [![打开你的Home Assistant实例并显示添加插件库对话框，预填特定插件库URL。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
2. 安装这个插件。
3. 点击`保存`按钮以存储你的配置。
4. 根据你的偏好设置插件选项。
5. 启动插件。
6. 检查插件的日志以查看一切是否顺利。
7. 打开WebUI并调整软件选项。

## 配置

---

WebUI可以在<http://homeassistant:port>找到，或通过侧边栏使用入口访问。
默认用户名/密码：在启动日志中描述。
可以通过应用程序WebUI进行配置，除了以下选项：

```yaml
ssl: true/false
certfile: fullchain.pem # ssl证书，必须位于/ssl中
keyfile: privkey.pem # ssl密钥文件，必须位于/ssl中
password: 定义管理员密码。如果留空，将允许手动恢复之前的备份。至少12个字符。
```

## 支持

在GitHub上创建一个问题。

## 插图

---

![插图](https://github.com/hassio-addons/addon-portainer/raw/main/images/screenshot.png)