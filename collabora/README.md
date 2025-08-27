# Home assistant add-on: collabora

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fcollabora%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fcollabora%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fcollabora%2Fconfig.json)

## 关于

Collabora Online 是一个基于 LibreOffice 技术的协作办公套件。

## 安装

1. 点击下面的 Home Assistant 我的插件商店按钮。
1. 点击“安装”按钮来安装插件。
1. 启动插件。
1. 检查插件的日志，看看是否一切正常。

<a href="https://my.home-assistant.io/redirect/supervisor_addon/?addon=local_collabora" target="_blank"><img src="https://my.home-assistant.io/badges/supervisor_addon.svg" alt="打开你的 Home Assistant 实例并显示添加插件仓库对话框"/></a>

## 配置

Webui 可以在 <http://homeassistant:9980> 或通过 Ingress 访问。

### 选项

配置插件以允许从你的 Nextcloud 实例访问：

- `domain`: 匹配 Nextcloud 主机的正则表达式（例如 `cloud\\.example\\.com`）。
- `username` 和 `password`: Collabora 管理控制台的可选凭证。
- `aliasgroup1`: 允许 WOPI 连接的附加主机名。
- `dictionaries`: 要安装的字典语言列表，空格分隔。
- `extra_params`: 传递给 Collabora 启动脚本的额外参数。

### 自定义脚本和环境变量

此插件支持通过 `addon_config` 映射的自定义脚本和环境变量：

- **自定义脚本**: 查看 [在插件中运行自定义脚本](https://github.com/alexbelgium/hassio-addons/wiki/Running-custom-scripts-in-Addons)
- **环境变量**: 查看 [向你的插件添加环境变量](https://github.com/alexbelgium/hassio-addons/wiki/Add-Environment-variables-to-your-Addon)

## 支持

在 GitHub 上创建问题

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white