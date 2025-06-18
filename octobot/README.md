# 家庭助理插件：MeTube

Octobot 是一个强大的开源加密货币交易机器人。

建议您仅用于模拟，不要连接到您的交易所，因为未经过测试。不支持 aws、efs、s3fs 和其他功能。

_感谢每一个给我的代码库星标的人！要星标，请点击下面的图像，然后它会出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此插件基于 [docker 镜像](https://www.octobot.cloud/en/guides/octobot-installation/install-octobot-with-docker-video)。

## 安装

此插件的安装相当简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件库][repository] 添加到您的 Hass.io 实例。
1. 安装此插件。
1. 单击 `保存` 按钮以存储您的配置。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 打开 WebUI 可通过入口或 <your-ip>:port 访问。

## 配置

```
port : 5001 #您希望运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons