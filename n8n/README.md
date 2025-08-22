# Home assistant插件：n8n

n8n是一个可扩展的工作流自动化工具。凭借公平的代码分发模式，n8n将始终拥有可见的源代码，可以自行托管，并允许您添加自己的自定义函数、逻辑和应用程序。n8n的基于节点的 подход 使其具有高度多功能性，使您能够将任何事物连接到任何其他事物。

功能尚未测试，但插件确实可以运行

_感谢所有给我仓库点赞的人！要点赞，请点击下面的图片，它将在右上角显示。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此插件使用 [docker 镜像](https://github.com/n8n-io/n8n)。

## 安装


1. 将我的 Hass.io 插件仓库 [repository] 添加到您的 Hass.io 实例。
1. 点击 `Save` 按钮以保存您的配置。
1. 启动插件。
1. 插件将失败，这是可以接受的
1. 使用 ssh 登录到您的 homeassistant 并运行 `chmod 2777 /addon_configs/2effc9b9_n8n`
1. 启动插件
1. 检查插件的日志以查看是否一切正常。
1. 应该可以通过 <your-ip>:port 打开 WebUI。
1. 设置管理员账户
1. 设置将在 /addon_configs/2effc9b9_n8n

## 配置

```
port : 5678 #您想要运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons