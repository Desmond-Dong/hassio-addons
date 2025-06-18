# Home assistant 插件: changedetection.io

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fchangedetection.io%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fchangedetection.io%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fchangedetection.io%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库加星的人！要加星，请点击下面的图片，然后它将在右上角。谢谢！_

[![星标用户的 repo 名单 @alexbelgium/hassio-addons](https://reporoster.com/stars/alexbelgium/hassio-addons)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/changedetection.io/stats.png)

## 介绍

[Changedetection.io](https://github.com/dgtlmoon/changedetection.io) 提供免费的开源网页监控、通知和变更检测。

该插件基于 linuxserver.io 的 [docker 镜像](https://github.com/linuxserver/docker-changedetection.io)。

## 配置

### 主要应用

Web UI 可以在 `<your-ip>:5000` 找到，也可以从插件页面访问。

#### 侧边栏快捷方式

您可以通过以下步骤添加指向您的 Changedetection.io 实例的快捷方式：
1. 转到 <kbd>⚙ 设置</kbd> > <kbd>仪表盘</kbd>
2. 在底部角落点击 <kbd>➕ 添加仪表盘</kbd>
3. 选择 <kbd>网页</kbd> 选项，并粘贴您从插件页面获取的 Web UI URL。
4. 填写侧边栏项的标题、一个图标（建议：`mdi:vector-difference`），以及该面板的 **相对 URL**（例如 `change-detection`）。最后确认。

### 可配置选项

```yaml
PGID: 用户
GPID: 用户
TZ: Etc/UTC 指定要使用的时区，请参见 https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List
BASE_URL: 当在反向代理后运行时，指定完整的 URL（包括协议）
```

### 连接到无浏览器的 Chrome（来自 @RhysMcW）

在 HA 中，使用文件编辑器插件（或文件浏览器）编辑 `/homeassistant/addons_config/changedetection.io/config.yaml` 中的 Changedetection.io 配置文件。

在文件末尾添加以下行：
```yaml
PLAYWRIGHT_DRIVER_URL: ws://2937404c-browserless-chrome:3000/chromium?launch={"defaultViewport":{"height":720,"width":1280},"headless":false,"stealth":true}&blockAds=true
```

根据 yaml 要求记得在文件末尾也添加一个空行。

`2937404c-browserless-chrome` 主机名在 UI 中显示，在无浏览器的 Chromium 插件页面上：
![图像](https://github.com/user-attachments/assets/a63514f6-027a-4361-a33f-0d8f87461279)

您也可以获取它：
* 通过 SSH 运行 `docker exec -i hassio_dns cat "/config/hosts"`
* 在 HA 中使用 CLI，使用 arp
* 您也应该能够使用您的 HA IP 地址。

然后重启 Changedetection.io 插件 - 之后您可以在 Changedetection.io 中使用浏览器选项。

## 安装

该插件的安装相当简单，与安装其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件仓库添加][repository]到您的 Hass.io 实例。
1. 安装该插件。
1. 点击 `保存` 按钮以存储您的配置。
1. 启动该插件。
1. 检查插件的日志以查看一切是否顺利。
1. 小心地根据您的偏好配置插件，具体请查看官方文档。

[repository]: https://github.com/alexbelgium/hassio-addons