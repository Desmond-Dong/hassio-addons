# Home assistant add-on: wDOSg

wDOSg (web DOS games) 是一个集中的 DOS 游戏库，它允许您从 IGDB 获取元数据，并通过 js-dos 在浏览器中运行您的游戏，使用极简的配置...

_感谢所有给我的仓库点赞的人！要点赞，请点击下面的图片，它将在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个 add-on 使用了 [docker 镜像](https://github.com/SoulRaven80/wdosg)。

## 安装

这个 add-on 的安装需要一些额外的工作。
1. 查阅官方 [仓库](https://github.com/SoulRaven80/wdosg)
1. 获取一个 Twitch 开发者账户 [说明](https://api-docs.igdb.com/#account-creation).
1. 将我的 Hass.io add-ons 仓库 [repository] 添加到您的 Hass.io 实例中。
1. 点击 `保存` 按钮来存储您的配置。
1. 这个 add-on 需要客户端 ID 和密钥。它将为您获取令牌。
1. 启动 add-on。
1. 检查 add-on 的日志，看看是否一切正常。
1. 应该可以通过 <your-ip>:port 打开 WebUI
1. 默认用户/密码 = wdosg@wdosg.com / wdosg
1. 查阅官方文档来制作 jsdos 包。这有点麻烦！最新版本可以直接从您自己的游戏 zip 文件中制作。确保 zip 文件中的游戏直接在 zip 的根目录中，而不是在 zip 内部的文件夹中！
1. 上传您的包并开始玩游戏。
1. 设置将在 /addon_configs/2effc9b9_wdosg 中

## 配置

```
port : 3001 #您想要运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons