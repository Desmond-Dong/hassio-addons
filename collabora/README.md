# Home assistant add-on: Collabora

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fcollabora%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fcollabora%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fcollabora%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有星标我的仓库的人！要星标它，请点击下面的图片，然后它将出现在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![downloads evolution](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/collabora/stats.png)

## 关于

Collabora Online 是一个基于 LibreOffice 技术的协作办公套件。

## 安装

---

1. 将我的插件仓库添加到您的 Home Assistant 实例中，或点击下方的 My 链接。
1. 安装插件。
1. 启动插件。
1. 检查插件日志以验证是否成功启动。

<a href="https://my.home-assistant.io/redirect/supervisor_addon/?addon=local_collabora" target="_blank"><img src="https://my.home-assistant.io/badges/supervisor_addon.svg" alt="打开您的 Home Assistant 实例并显示添加插件仓库对话框"/></a>

## 配置

---

Webui 可以在 `http://homeassistant:9980` 或通过 Ingress 访问。

### 选项

| 选项 | 类型 | 默认值 | 描述 |
|------|------|--------|-------|
| `aliasgroup1` | 字符串 | | Nextcloud 外部域名，点用转义符（例如 `nextcloud_domain\\.com`） |
| `domain1` | 字符串 | | Collabora 外部域名，点用转义符（例如 `code_domain\\.com`） |
| `extra_params` | 字符串 | | 传递给 Collabora 启动脚本的额外参数 |
| `username` | 字符串 | | Collabora 管理控制台的用户名 |
| `password` | 字符串 | | Collabora 管理控制台的密码 |
| `dictionaries` | 字符串 | | 要安装的字典语言列表，空格分隔 |

### 示例配置

```yaml
aliasgroup1: nextcloud_domain\.com
domain1: code_domain\.com
extra_params: ""
username: admin
password: changeme
```

### 使用 Collabora 与 Nextcloud

1. 安装 Collabora 插件并配置上述选项。
1. 启动插件并将 Collabora 服务器暴露到一个外部域名。
1. 安装并配置 Nextcloud 插件。
1. 在 Nextcloud 中，安装 **Nextcloud Office** 应用。
1. 在 Nextcloud **管理设置 → Office** 中，将 Collabora 服务器 URL 设置为 `https://yourdomain:9980` 并启用 **禁用证书验证**。

### 自定义脚本和环境变量

此插件通过 `addon_config` 映射支持自定义脚本和环境变量：

- **自定义脚本**：参见 [在插件中运行自定义脚本](https://github.com/alexbelgium/hassio-addons/wiki/Running-custom-scripts-in-Addons)
- **环境变量**：参见 [为您的插件添加环境变量](https://github.com/alexbelgium/hassio-addons/wiki/Add-Environment-variables-to-your-Addon)

## 支持

在 GitHub 上创建问题。