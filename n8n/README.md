# Home assistant 插件: n8n

n8n 是一个可扩展的工作流程自动化工具。通过公平代码分发模型，n8n 将始终保持源代码透明，可供自托管，并允许您添加自定义功能、逻辑和应用程序。n8n 的基于节点的方法使其具有高度的多功能性，使您能够将任何东西连接到所有东西。

功能未经测试，但插件正常运行

_感谢所有给我的仓库点赞的人！要点赞，请点击下面的图片，然后它将在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个插件使用的是 [docker 镜像](https://github.com/n8n-io/n8n)。

## 安装


1. [将我的 Hass.io 插件库][repository] 添加到您的 Hass.io 实例。
1. 点击 `保存` 按钮以存储您的配置。
1. 启动插件。
1. 插件将失败，这没关系。
1. SSH 进入您的 homeassistant 并运行 `chmod 2777 /addon_configs/2effc9b9_n8n`
1. 启动插件
1. 检查插件的日志以查看是否一切正常。
1. 打开 WebUI 应该通过 <your-ip>:port 工作。
1. 设置管理员账户
1. 设置将位于 /addon_configs/2effc9b9_n8n
## 配置

```
port : 5678 #您想要运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons