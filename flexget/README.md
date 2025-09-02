# Hass.io Add-ons: Flexget

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fflexget%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fflexget%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fflexget%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库加星的人！要加星，请点击下面的图片，然后它将出现在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![downloads evolution](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/flexget/stats.png)

## 关于

[FlexGet](https://flexget.com/) 是一个用于所有媒体的多功能自动化工具。它可以支持种子、NZB、播客、漫画、电视、电影、RSS、HTML、CSV 等。

主要功能：
- 强大的插件系统，拥有 300 多个插件
- RSS 源处理和过滤
- 与下载客户端的集成
- 基于网络的管理界面
- 定时执行和守护进程模式

## 安装

这个插件的安装非常简单，与安装其他插件没有区别。

1. 将我的插件仓库添加到您的 Home Assistant 实例中（在 supervisor 插件商店的右上角，或者如果您已经配置了我的 HA，请点击下面的按钮）
   [![打开您的 Home Assistant 实例并显示添加插件仓库对话框，并预填了特定的仓库 URL。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装这个插件。
1. 点击 `保存` 按钮以保存您的配置。
1. 根据您的偏好设置插件选项。
1. 启动插件。
1. 检查插件的日志，看看一切是否正常。
1. 打开 WebUI 并调整软件选项

## 配置

Webui 可以在 <http://homeassistant:5050> 找到。
默认密码：`homeassistant123`（通过插件选项更改）。

### 设置步骤

1. 启动插件后访问 Web 界面
2. 创建或编辑您的 FlexGet 配置文件
3. 设置 RSS 源和下载源
4. 配置输出插件以用于您的下载客户端
5. 测试配置并启用定时任务

### 选项

| 选项 | 类型 | 默认值 | 描述 |
|------|------|--------|-------|
| `PGID` | int | `0` | 文件权限的组 ID |
| `PUID` | int | `0` | 文件权限的用户 ID |
| `WebuiPass` | str | `homeassistant123` | Web 界面密码 |
| `FG_PLUGINS` | str | | 需要安装的额外插件 |
| `FG_LOG_LEVEL` | list | | 日志级别（critical/error/warning/info/verbose/debug/trace） |

### 示例配置

```yaml
PGID: 1000
PUID: 1000
WebuiPass: "SecurePassword123"
FG_PLUGINS: "flexget-plugins-extra"
FG_LOG_LEVEL: "info"
```

### 配置文件

FlexGet 使用位于 `/config/flexget/config.yml` 的 YAML 配置文件。示例：

```yaml
tasks:
  tv-shows:
    rss: https://example.com/tv-shows.rss
    series:
      - Breaking Bad
      - Game of Thrones
    transmission:
      host: localhost
      port: 9091
```

有关完整的配置文档，请参阅：https://flexget.com/Configuration

## 支持

如果您在安装过程中遇到问题，请务必查看 github。