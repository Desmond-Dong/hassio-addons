# Home assistant add-on: n8n

n8n是一个可扩展的工作流自动化工具。通过公平的代码分发模型，n8n将始终拥有可见的源代码，可以自行托管，并允许您添加自己的自定义函数、逻辑和应用程序。n8n的基于节点的方法使其具有高度的通用性，使您能够将任何事物连接到任何其他事物。

功能尚未测试，但插件确实可以运行

_感谢所有给我仓库加星标的人！要加星标，请点击下面的图片，然后它就会出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此插件使用[docker镜像](https://github.com/n8n-io/n8n)。

## 安装


1. [将我的Hass.io插件仓库][repository]添加到您的Hass.io实例中。
1. 点击`保存`按钮以保存您的配置。
1. 启动插件。
1. 插件将失败，这是正常的
1. 通过ssh进入您的homeassistant并运行`chmod 2777 /addon_configs/2effc9b9_n8n`
1. 启动插件
1. 检查插件的日志以查看是否一切顺利。
1. 应该可以通过<your-ip>:port访问WebUI。
1. 设置管理员账户
1. 设置将在 /addon_configs/2effc9b9_n8n 中

## 配置

```
port : 5678 #您想要运行的端口。
```

Webui可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons