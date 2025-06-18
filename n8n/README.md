# 家庭助手附加组件：n8n

n8n 是一个可扩展的工作流自动化工具。采用公平代码分发模型，n8n 将始终具有可见的源代码，可以自我托管，并允许您添加自定义功能、逻辑和应用程序。n8n 的基于节点的方法使其具有高度的灵活性，能够将任何内容连接到一切。

功能未经过测试，但附加组件确实可以运行

_感谢所有给我的仓库点Star的人！要点Star，请点击下面的图片，然后它将出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

该附加组件使用[docker 镜像](https://github.com/n8n-io/n8n)。

## 安装


1. [将我的 Hass.io 附加组件仓库][repository] 添加到您的 Hass.io 实例中。
1. 点击 `Save` 按钮以保存您的配置。
1. 启动附加组件。
1. 附加组件将会失败，这没关系。
1. SSH 进入您的 homeassistant，运行 `chmod 2777 /addon_configs/2effc9b9_n8n`
1. 启动附加组件
1. 检查附加组件的日志以查看一切是否正常。
1. 打开 WebUI 应该可以通过 <your-ip>:port 访问。
1. 设置管理员帐户
1. 设置将位于 /addon_configs/2effc9b9_n8n

## 配置

```
port : 5678 #您希望运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons