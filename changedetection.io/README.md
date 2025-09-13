# Home assistant add-on: changedetection.io

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fchangedetection.io%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=入站&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fchangedetection.io%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fchangedetection.io%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=代码检查)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建器)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库点赞的人！要点赞，请点击下面的图片，然后它会在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://reporoster.com/stars/alexbelgium/hassio-addons)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载趋势](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/changedetection.io/stats.png)

## 关于

[Changedetection.io](https://github.com/dgtlmoon/changedetection.io) 提供免费的、开源的网页监控、通知和变化检测。

这个插件基于 linuxserver.io 的 [docker 镜像](https://github.com/linuxserver/docker-changedetection.io)。

## 配置

### 主应用程序

Web 界面可以在 `<你的 IP>:5000` 找到，也可以从插件页面访问。

#### 侧边栏快捷方式

您可以通过以下步骤添加一个指向您的 Changedetection.io 实例的快捷方式：
1. 转到 <kbd>⚙ 设置</kbd> > <kbd>仪表板</kbd>
2. 点击底角处的 <kbd>➕ 添加仪表板</kbd>
3. 选择 <kbd>网页</kbd> 选项，并粘贴从插件页面获得的 Web UI URL。
4. 填写侧边栏项目的标题、图标（建议：`mdi:vector-difference`）以及该面板的**相对 URL**（例如 `change-detection`）。最后，确认它。

### 选项

| 选项 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `PGID` | 整数 | `0` | 文件权限的组 ID |
| `PUID` | 整数 | `0` | 文件权限的用户 ID |
| `TZ` | 字符串 | | 时区（例如，`Europe/London`） |
| `BASE_URL` | 字符串 | | 背后反向代理时的完整 URL |
| `TIMEOUT` | 整数 | `60000` | 毫秒内的请求超时 |

### 示例配置

```yaml
PGID: 0
PUID: 0
TZ: "Europe/London"
BASE_URL: "https://changedetection.mydomain.com"
TIMEOUT: 60000
```

### 连接到 browserless Chrome（来自 @RhysMcW）

在 HA 中，使用文件编辑器插件（或文件浏览器）并编辑 Changedetection.io 配置文件 `/homeassistant/addons_config/changedetection.io/config.yaml`。

在文件的末尾添加以下行：
```yaml
PLAYWRIGHT_DRIVER_URL: ws://2937404c-browserless-chrome:3000/chromium?headless=true&blockAds=true&stealth=true
```

记得根据 YAML 要求在文件末尾添加一个空行。

`2937404c-browserless-chrome` 主机名在 UI 中显示，在 Browserless Chromium 插件页面：
![image](https://github.com/user-attachments/assets/a63514f6-027a-4361-a33f-0d8f87461279)

您也可以通过以下方式获取它：
* 使用 SSH 并运行 `docker exec -i hassio_dns cat "/config/hosts"`
* 从 HA 的 CLI 使用 arp
* 您也应该能够使用您的 HA IP 地址。

然后重启 Changedetection.io 插件 - 之后您就可以在 Changedetection.io 中使用浏览器选项了。

## 安装

这个插件的安装非常简单，与安装任何其他 Hass.io 插件没有区别。

1. 将我的 Hass.io 插件仓库 [repository] 添加到您的 Hass.io 实例。
1. 安装这个插件。
1. 点击 `保存` 按钮以保存您的配置。
1. 启动插件。
1. 检查插件的日志，看看是否一切正常。
1. 仔细配置插件以符合您的偏好，请参考官方文档。