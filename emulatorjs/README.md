# 家庭助手插件：EmulatorJS
基于浏览器的模拟，可以在几乎任何设备上便携运行，适用于许多复古游戏机。使用Libretro和EmulatorJS之间的多种模拟器混合。

_感谢所有给我的repo点星的人！要点星，请点击下面的图片，然后它将出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此插件基于来自linuxserver的[docker镜像](https://github.com/linuxserver/docker-emulatorjs)。基于浏览器的模拟，可以在几乎任何设备上便携运行，适用于许多复古游戏机。使用Libretro和EmulatorJS之间的多种模拟器混合。

## 安装

此插件的安装相当简单，与安装任何其他Hass.io插件没有不同。

1. [将我的Hass.io插件仓库][repository]添加到您的Hass.io实例。
1. 安装此插件。
1. 单击`保存`按钮以保存您的配置。
1. 创建目录/share/emulatorjs以存储您的游戏/艺术文件。
1. 创建/share/emulatorjs/config和/share/emulatorjs/data。
1. 启动插件。
1. 检查插件的日志以查看一切是否顺利。
1. 将rom文件放置在/share/emulatorjs/data/EMULATORNAME/roms中的正确文件夹中。
1. 转到管理端口。
1. 点击扫描您添加游戏的模拟器。
1. 点击模拟器框，执行步骤1和步骤2。
1. 打开WebUI应该进入PlayerUI，访问您的本地homeassistant IP:port或管理端口。
1. 您的游戏应该可以使用。
1. 请查阅官方文档以获取设置支持：https://github.com/linuxserver/docker-emulatorjs
1. 如果启动插件导致擦除您的设置，停止插件并重新启动。 有时映射到/share/emulatorjs可能会失败。

## 配置

```
adminport : 3000 #您想运行管理界面的端口。
port: 89 #您想运行前端的端口。
```

Webui可以在`<your-ip>:port`找到。应该可以通过ingress访问。管理端口无法通过ingress访问。

[repository]: https://github.com/jdeath/homeassistant-addons