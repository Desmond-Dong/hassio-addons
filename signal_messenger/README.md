[![](logo.png)](https://www.signal.org/)

# Signal Messenger

Signal-CLI Home Assistant add-on REST-API

# 如何使用此插件

安装插件，选择您想要的端口，启动。

插件启动后，请按照以下链接中的说明进行操作，从“注册电话号码”开始：

https://github.com/bbernhard/signal-cli-rest-api/blob/master/doc/HOMEASSISTANT.md

然后继续：

https://www.home-assistant.io/integrations/signal_messenger/

# API详细信息

如果您想使用REST接收HA中的消息，您可以在此处找到更多详细信息：

[此处](https://bbernhard.github.io/signal-cli-rest-api/)

强烈建议您使用机器IP地址，而不是上游容器文档中提到的回环地址来注册号码。在HAOS中，一切都是容器化的，回环地址仍然位于各自的容器内部。

所有功劳归于[@bbernhard](https://github.com/bbernhard)，我所做的一切只是采用了他的[工作](https://github.com/bbernhard/signal-cli-rest-api)并制作了一个插件。