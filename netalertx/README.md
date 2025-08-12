# Home assistant add-on: NetAlertX

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fnetalertx%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fnetalertx%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fnetalertx%2Fconfig.json)
![mqtt](https://img.shields.io/badge/服务-MQTT-green.svg?logo=chromecast&logoColor=white)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库点赞的人！要点赞，请点击下面的图片，然后它会在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![downloads evolution](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/netalertx/stats.png)

## 关于

网络存在和入侵检测器。扫描您网络中连接的设备，并在发现新的未知设备时向您发出警报。
此插件基于 jokob-sk 的 [docker 镜像](https://github.com/jokob-sk/NetAlertX/tree/main/dockerfiles)。

## 安装

此插件的安装非常简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件仓库][repository]添加到您的 Hass.io 实例中。
1. 安装此插件。
1. 点击 `保存` 按钮以保存您的配置。
1. 启动插件。
1. 检查插件的日志，看看是否一切正常。
1. 小心配置插件以符合您的偏好，请参阅官方文档以获取相关信息。

## 配置

1. 如果不可用，应用程序在首次运行时将生成默认的 `app.conf` 和 `app.db` 文件。
1. 更好的方式是通过 UI 中的设置部分进行配置，如果 UI 不可用，您可以直接修改 `/app/config/` 文件夹中的 `app.conf`。
1. 您必须指定要扫描哪些网络。这是通过输入从主机可访问的子网来完成的。如果您使用默认的 `ARPSCAN` 插件，您必须在 `SCAN_SUBNETS` 设置中指定至少一个有效的子网和接口。请参阅有关如何设置多个 SUBNETS、VLANs 以及限制的[文档](https://github.com/jokob-sk/NetAlertX/blob/main/docs/SUBNETS.md)，以及用于故障排除和更高级场景的信息。
1. 阅读如何通过 MQTT 插件将设备输入到您的 [Home Assistant 实例](https://github.com/jokob-sk/NetAlertX/blob/main/docs/HOME_ASSISTANT.md)
1. 按照 [备份文档](https://github.com/jokob-sk/NetAlertX/blob/main/docs/BACKUPS.md)备份所有内容。

Webui 可以在 <http://homeassistant:20211> 或使用 HA ingress 找到

<img width="500" alt="image" src="https://github.com/user-attachments/assets/fd74af43-091a-4f38-9879-037ca64cfab9" />

```yaml
PGID: user
GPID: user
```

### 自定义脚本和环境变量

此插件通过 `addon_config` 映射支持自定义脚本和环境变量：

- **自定义脚本**：请参阅 [在插件中运行自定义脚本](https://github.com/alexbelgium/hassio-addons/wiki/Running-custom-scripts-in-Addons)
- **环境变量**：请参阅 [向您的插件添加环境变量](https://github.com/alexbelgium/hassio-addons/wiki/Add-Environment-variables-to-your-Addon)

[repository]: https://github.com/alexbelgium/hassio-addons