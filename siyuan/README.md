# Home assistant add-on: SiYuan

SiYuan 是一款注重隐私的个人知识管理系统，支持细粒度的块级引用和 Markdown WYSIWYG。

看起来很受欢迎，但有订阅加成和可选的中国数据中心。请谨慎使用

_感谢大家给我的仓库加星！要加星，请点击下面的图片，它就会出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个插件基于 [docker 镜像](https://github.com/siyuan-note/siyuan)。

## 安装

这个插件的安装非常直接，与其他任何 Hass.io 插件的安装方式相同。

1. [将我的 Hass.io 插件仓库][repository] 添加到你的 Hass.io 实例。
1. 安装这个插件。
1. 设置访问码和端口
1. 点击 `保存` 按钮来保存你的配置。
1. 启动插件。
1. 检查插件的日志，看看一切是否正常。
1. 通过 <your-ip>:port 应该可以打开 WebUI。
1. 数据应该存储在 /addon_config/2effc9b9_siyuan

## 配置

```
port : 6806 #你想要运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons