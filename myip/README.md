# Home assistant插件：MyIP

MyIP是一个高级IP工具，旨在提供有关您IP地址的广泛信息和诊断。它非常适合需要查看和分析其IP详细信息、检查网站可访问性、执行DNS泄漏测试等的用户。

_感谢大家给我的仓库加星！要加星，请点击下面的图片，它就会出现在右上角。谢谢！_

[![@jdeath/homeassistant-addons的仓库Star列表](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个插件使用的是[docker镜像](https://github.com/jason5ng32/MyIP)。

## 安装

这个插件的安装非常简单，与安装任何其他Hass.io插件的方式没有不同。

1. 将我的Hass.io插件仓库[repository]添加到您的Hass.io实例。
1. 安装这个插件。
1. 点击`保存`按钮以保存您的配置。
1. 应该可以通过<your-ip>:port访问WebUI。

## 配置

```
port : 18966 #您想要运行的端口。
```

Webui可以在<your-ip>:port找到。

[repository]: https://github.com/jdeath/homeassistant-addons