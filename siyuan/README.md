# Home assistant插件：SiYuan

SiYuan是一个注重隐私的个人知识管理系统，支持细粒度的块级引用和Markdown所见即所得编辑。

看起来很受欢迎，但有订阅插件和可选的中国数据中心。请谨慎使用

_感谢大家给我的仓库加星！要加星，请点击下面的图片，它将在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个插件基于[docker镜像](https://github.com/siyuan-note/siyuan)。

## 安装

这个插件的安装非常简单，与其他Hass.io插件的安装方式相同。

1. [将我的Hass.io插件仓库][repository]添加到你的Hass.io实例。
1. 安装这个插件。
1. 设置访问码和端口
1. 点击`保存`按钮以保存你的配置。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 应该可以通过`<your-ip>:port`打开WebUI。
1. 数据应该存储在`/addon_config/2effc9b9_siyuan`

## 配置

```
port : 6806 #你想要运行的端口。
```

Webui可以在`<your-ip>:port`找到。

[repository]: https://github.com/jdeath/homeassistant-addons