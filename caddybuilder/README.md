# Home assistant add-on: Caddy Builder

这将为您构建一个自定义的caddy二进制文件。

下载自定义caddy二进制文件的网站（https://caddyserver.com/download）经常无法访问或无法工作。此插件将运行xcaddy并使用您想要的任何插件构建自定义二进制文件。

使用caddy2 homeassistant插件来运行此仓库中提供的自定义caddy二进制文件：https://github.com/einschmidt/hassio-addons

xcaddy的用法信息可以在以下位置找到：https://github.com/caddyserver/xcaddy

_感谢所有将我的仓库标为星标的人！要标星，请点击下面的图片，然后它将出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此插件基于caddy-builder [docker镜像](https://hub.docker.com/_/caddy)。

## 安装

1. 将我的Hass.io插件仓库[repository]添加到您的Hass.io实例。
1. 安装此插件。
1. 关闭“启动时启动”开关
1. 点击“保存”按钮以保存您的配置。
1. 运行插件一次。它应该失败，这是可以接受的。
1. 将此仓库中的[xcaddyCommand.sh](https://raw.githubusercontent.com/jdeath/homeassistant-addons/main/caddybuilder/xcaddyCommand.sh)复制到/addon_configs/XXXXXX_caddybuilder（XXXXX是一些如2effc9b9的字符串，并由上一步创建）
1. 编辑xcaddyCommand.sh以运行您想要的xcaddy命令。确保所有内容都在一行上。查看xcaddy文档以添加插件。
1. 运行插件。自定义caddy二进制文件应该会在/addon_configs/XXXXXX_caddybuilder/中构建
1. 可能需要一些时间，所以刷新日志以查看是否正确构建
1. 将caddy二进制文件复制到/share/caddy/
1. 重启[caddy2](https://github.com/einschmidt/hassio-addons)插件（不是此插件），它应该使用您新的自定义caddy二进制文件

[repository]: https://github.com/jdeath/homeassistant-addons