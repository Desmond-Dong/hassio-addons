[![](logo.png)](https://www.signal.org/)

# Signal Messenger

用于 Signal-CLI Home Assistant 添加组件的 REST API

# 如何使用此添加组件

安装添加组件，选择您想要的端口，然后启动。

添加组件启动后，请按照以下链接中的说明，从“注册电话号码”开始。

https://github.com/bbernhard/signal-cli-rest-api/blob/master/doc/HOMEASSISTANT.md

然后继续这里：

https://www.home-assistant.io/integrations/signal_messenger/

# API 详情

如果您想使用 i.e. REST 在 HA 中接收消息，可以在 [这里](https://bbernhard.github.io/signal-cli-rest-api/) 找到更多详细信息。

强烈建议您使用机器的 IP 地址，而不是上游容器文档中提到的回环地址来注册号码。在 HAOS 中，一切都是容器化的，回环地址仅保留在各自的容器内。

所有的功劳归于 [@bbernhard](https://github.com/bbernhard)，我所做的只是将他的 [工作](https://github.com/bbernhard/signal-cli-rest-api) 制作成一个添加组件。