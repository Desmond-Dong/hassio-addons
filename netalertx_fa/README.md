# Home assistant add-on: NetAlertX Full Access

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fnetalertx_fa%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fnetalertx_fa%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fnetalertx_fa%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库点赞的人！要点赞，请点击下面的图片，然后它会在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载趋势](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/netalertx_fa/stats.png)

## 关于

[NetAlertX](https://github.com/jokob-sk/NetAlertX) 是一个 WIFI / LAN 扫描器、入侵检测器和存在检测器，帮助您监控网络中的新设备和潜在的安全威胁。

**这是 Full Access 版本**，与标准的 NetAlertX 插件相比，它提供了额外的权限和网络访问功能。

主要功能：
- 网络设备发现和监控
- 已知设备的存在检测
- 未知设备的入侵检测
- 基于网络的仪表板，用于网络可视化
- 与 Home Assistant 的 MQTT 集成
- 增强权限的网络扫描

## 配置

Webui 可以在 `<你的 IP>:20211` 或通过 Ingress 在侧边栏中找到。

### 选项

| 选项 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `TZ` | 字符串 | `Europe/Berlin` | 时区（例如，`Europe/London`） |
| `APP_CONF_OVERRIDE` | 字符串 | | 额外的应用配置覆盖 |

### 示例配置

```yaml
TZ: "Europe/London"
APP_CONF_OVERRIDE: "SCAN_SUBNETS=['192.168.1.0/24']"
```

### MQTT 集成

此插件支持 MQTT 集成，如果可用，将自动连接到您的 Home Assistant MQTT 中继。NetAlertX 可以将设备存在信息发布到 MQTT 主题，以便与 Home Assistant 自动化集成。

### 自定义脚本和环境变量

此插件通过 `addon_config` 映射支持自定义脚本和环境变量：

- **自定义脚本**：参见 [在插件中运行自定义脚本](https://github.com/alexbelgium/hassio-addons/wiki/Running-custom-scripts-in-Addons)
- **环境变量**：参见 [为您的插件添加环境变量](https://github.com/alexbelgium/hassio-addons/wiki/Add-Environment-variables-to-your-Addon)

## 安装

此插件的安装非常简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件仓库][repository] 添加到您的 Hass.io 实例。
1. 安装此插件。
1. 点击 `保存` 按钮以保存您的配置。
1. 启动插件。
1. 检查插件的日志，看看是否一切正常。
1. 打开 WebUI 以配置您的网络扫描偏好设置。

## Full Access 与标准版本的区别

此 **Full Access** 版本提供：
- `full_access: true` - 完全系统访问
- `host_network: true` - 直接主机网络访问
- 增强权限 (`SYS_ADMIN`, `NET_ADMIN`, `NET_RAW`)
- `udev: true` - 硬件设备访问

如果您需要增强的网络扫描功能，或者标准的 NetAlertX 插件无法为您的设置提供足够的网络访问权限，请使用此版本。

## 支持

在 github 上创建问题，或在 [home assistant 社区论坛](https://community.home-assistant.io/) 上提问

[repository]: https://github.com/alexbelgium/hassio-addons