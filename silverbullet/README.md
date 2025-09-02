# Home assistant add-on: SilverBullet

SilverBullet 是一款专为具有黑客思维的人优化的笔记应用。我们都记笔记。外面有成千上万种笔记应用。字面意义上。如果有一种应用能让你的笔记不仅仅是纯文本文件，让你的笔记本质上成为一个你可以查询的数据库；你可以在其上构建自定义知识应用，那该多好？如果你愿意，这是一个可定制的笔记本？

_感谢大家给我的仓库点赞！要点赞，请点击下面的图片，它就会出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个插件基于 [docker 镜像](https://github.com/silverbulletmd/silverbullet)。

## 安装

这个插件的安装非常直接，与其他任何 Hass.io 插件的安装方式相同。

1. [将我的 Hass.io 插件仓库][repository] 添加到你的 Hass.io 实例。
1. 安装这个插件。
1. 点击 `保存` 按钮来存储你的配置。
1. 如果你想要密码保护，将 SB_HOME 字段设置为 UserName:Password，例如 Mike:Pass123
1. 启动插件。
1. 检查插件的日志，看看一切是否正常。
1. 应该可以通过 ingress 或 <your-ip>:port 打开 WebUI。
1. 数据应该存储在 /addon_config/2effc9b9_silverbullet

## 配置

```
port : 8081 # 你想要运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons