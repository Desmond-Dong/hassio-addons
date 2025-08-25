# Home assistant插件：mitmproxy

Mitmproxy是您用于调试、测试、隐私测量和渗透测试的多功能工具。它可以用于拦截、检查、修改和重放Web流量，例如HTTP/1、HTTP/2、WebSocket或任何其他SSL/TLS保护的协议。您可以对各种消息类型进行美化和解码，从HTML到Protobuf，实时拦截特定消息，在它们到达目的地之前进行修改，并稍后重放给客户端或服务器。

使用mitmweb以图形界面使用mitmproxy的主要功能。您喜欢Chrome的开发者工具吗？mitmweb为任何其他应用程序或设备提供类似体验，并具有额外的功能，如请求拦截和重放。

_感谢所有将我的仓库标星的人！要标星它，请点击下面的图片，它将在右上角。谢谢！_

[![@jdeath/homeassistant-addons的Starazers仓库花名册](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此插件基于[docker镜像](https://github.com/mitmproxy/mitmproxy)。

## 安装

1. 将我的Hass.io插件仓库[repository]添加到您的Hass.io实例。
1. 安装此插件。
1. 点击`保存`按钮以存储您的代理端口和WebUI端口的配置。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 您的证书将生成在 /addon_configs/2effc9b9_mitmproxy
1. 如果您有来自其他安装的证书，请将它们复制到此目录。
1. 应该可以通过 <your-ip>:port 打开WebUI。
1. 密码是 `homeassistant`

Webui可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons