# Home assistant add-on: linkding

##  Introduction
linkding是一个可以由你自己托管的收藏夹管理器。
它的设计目标是简洁、快速，并且使用Docker易于设置。

它的名字来源于：
- *link*，通常在常用语言中用作URL和收藏夹的同义词
- *Ding*，德语中意为事物
- ...所以基本上是用于管理你的链接的工具

**功能概述:**
- 清晰的用户界面，优化了可读性
- 使用标签组织收藏夹
- 批量编辑、Markdown笔记、稍后阅读功能
- 与其他用户或访客分享收藏夹
- 自动提供收藏网站的标题、描述和图标
- 自动归档网站，作为本地HTML文件或存档在Internet Archive
- 以Netscape HTML格式导入和导出收藏夹
- 可作为渐进式网络应用（PWA）安装
- [Firefox](https://addons.mozilla.org/firefox/addon/linkding-extension/)和[Chrome](https://chrome.google.com/webstore/detail/linkding-extension/beakmhbijpdhipnjhnclmhgjlddhidpe)的扩展，以及一个收藏夹小工具
- 通过OIDC或认证代理支持单点登录（SSO）
- 用于开发第三方应用的REST API
- 管理员面板，用于用户自助服务和原始数据访问

_感谢大家给我的仓库点亮星标！要点亮星标，请点击下面的图片，然后它就会出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## About

这个插件使用了[docker镜像](https://github.com/sissbruecker/linkding)。

有点消耗内存。这个使用的是常规的linkding镜像，而不是plus版。如果你想使用plus版，下载插件的源代码，放到/addons/目录下，编辑config.json文件，将版本号改为latest-plus，而不是具体的版本号。

## Installation

这个插件的安装非常简单，与安装任何其他Hass.io插件没有区别。

1. [将我的Hass.io插件仓库][repository]添加到你的Hass.io实例。
1. 安装这个插件。
1. 点击`保存`按钮以保存你的配置。
1. 启动插件。
1. 检查插件的日志，看看是否一切正常。
1. 应该可以通过<your-ip>:port访问WebUI。
1. 设置将在 /addon_configs/2effc9b9_linkding 中。
1. 停止插件，编辑settings.yaml文件以更改任何你需要的设置

## Configuration
1. 你必须创建一个初始的超级用户账户。
1. 启动插件
1. 使用homeassistant cli登录
1. `docker ps | grep "link"`，复制显示的第一个十六进制字符串
1. `docker exec -it 3c32b108bd10 python manage.py createsuperuser --username=joe --email=joe@mail.com`
1. 输入密码，然后重启插件
```
port : 9090 #你想要运行的端口。
```

Webui可以在<your-ip>:port找到。

[repository]: https://github.com/jdeath/homeassistant-addons