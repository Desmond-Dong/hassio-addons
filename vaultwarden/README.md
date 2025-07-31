# Home assistant add-on: Vaultwarden

一种用 Rust 编写的 Bitwarden 服务器 API 的替代实现，与上游的 Bitwarden 客户端*兼容，非常适合自托管部署，其中运行官方的资源密集型服务可能并不理想。

此版本、官方的 homeassistant add-on 和 Alex Belgium 的 add-on 之间的区别在于此版本将数据存储在 /addons_config 中，这使得在您意外卸载或进行不良升级时更容易移动它们。您必须确保使用 argon 加密的密码，这现在应该是默认的。此外，内置的 homeassistant 中的一个通常不会更新（即使多次请求后也是如此）。此 add-on 也仅使用官方的 docker 镜像，没有进行任何更改，而其他 add-on 会编辑镜像并添加额外的内容。

_感谢所有 star 我的仓库！要 star 它，请点击下面的图片，然后它将出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此 add-on 使用了 [docker 镜像](https://github.com/dani-garcia/vaultwarden)。

## 安装

此 add-on 的安装非常简单，与安装任何其他 Hass.io add-on 没有区别。

1. [将我的 Hass.io add-ons 仓库][repository] 添加到您的 Hass.io 实例。
1. 点击 `保存` 按钮以保存您的配置。
1. 启动 add-on。
1. 检查 add-on 的日志以查看是否一切正常。
1. WebUI 应该可以通过 <your-ip>:port 工作。
1. 您的数据将存储在 /addon-configs/2effc9b9_vaultwarden/

如果您有一个现有的 vaultwarden 安装（默认 add-on 或 alexbelgium 的），
1. 确保我的 add-on 已经运行一次，但然后确保停止它
1. 登录 homeassistant cli
1. `docker ps | grep "vault"`
1. 找到 docker containerID
1. `docker cp CONTAINERID:/data /addon-configs/2effc9b9_vaultwarden/`
1. 然后在 `/addon-configs/2effc9b9_vaultwarden/` 将 `data` 文件夹中的所有内容移动到 `/addon-configs/2effc9b9_vaultwarden/`
1. 现在所有文件应该都在 `/addon-configs/2effc9b9_vaultwarden/`
1. 停止默认 add-on，关闭 "启动时自动启动"
1. 启动我的 add-on
1. 查阅文档进行配置：https://github.com/dani-garcia/vaultwarden


## 配置
1. 设置完成后，从外部网络中删除对管理控制面板的访问权限
1. 您可以通过停止容器并编辑 `/addon-configs/2effc9b9_vaultwarden/config.json` 手动配置许多参数
1. 确保您的 `admin_token` 是 argon2 加密的：https://github.com/dani-garcia/vaultwarden/wiki/Enabling-admin-page#secure-the-admin_token
1. 如果不是，`docker ps | grep "vault"`，前面的数字/字母是 containerID
2. `docker exec -it containerID /bin/bash`
3. `cd /` `/vaultwarden hash --preset owasp` 输入密码，然后替换 admin token
4. 由于此文件是可访问的，我猜任何人都可以这样做，所以请小心。如果您可以访问您的 homeassistant 机器，这也可以在容器内完成，所以实际上并没有更安全


```
port : 7277 #您想要运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons