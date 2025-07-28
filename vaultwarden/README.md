# Home assistant add-on: Vaultwarden

Rust语言编写的Bitwarden服务器API的替代实现，与上游Bitwarden客户端*兼容，非常适合自托管部署，因为在您的环境中运行官方资源密集型服务可能不是理想的。

此版本、官方homeassistant插件和Alex Belgium的插件之间的区别在于，它将数据存储在/addons_config中，这使得在您意外卸载或进行不良升级时更容易移动它们。您必须确保使用argon加密密码，这现在应该是默认的。另外，内置的homeassistant插件通常不会更新（即使多次请求也是如此）。此插件也仅使用官方的docker镜像，没有任何更改，而其他插件会编辑镜像并添加额外的内容。

_感谢大家给我的仓库加星！要加星，请点击下面的图片，然后它就会在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此插件使用[docker镜像](https://github.com/dani-garcia/vaultwarden)。

## 安装

此插件的安装非常简单，与安装任何其他Hass.io插件没有区别。

1. 将我的Hass.io插件仓库[repository]添加到您的Hass.io实例中。
1. 点击“保存”按钮以保存您的配置。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. WebUI应该可以通过<your-ip>:port访问。
1. 您的数据将存储在 /addon-configs/2effc9b9_vaultwarden/

如果您有一个现有的vaultwarden安装（默认插件或alexbelgium的），
1. 确保我的插件已经运行一次，但然后确保停止它
1. 登录homeassistant cli
1. `docker ps | grep "vault"`
1. 找到docker容器ID
1. `docker cp CONTAINERID:/data /addon-configs/2effc9b9_vaultwarden/`
1. 然后在`/addon-configs/2effc9b9_vaultwarden/`中，将`data`文件夹中的所有内容移动到`/addon-configs/2effc9b9_vaultwarden/`
1. 现在所有文件都应该在`/addon-configs/2effc9b9_vaultwarden/`
1. 停止默认插件，关闭“启动时启动”
1. 启动我的插件
1. 审查文档进行配置：https://github.com/dani-garcia/vaultwarden


## 配置
1. 设置完成后，从外部网络移除对管理控制面板的访问权限
1. 您可以通过停止容器并编辑`/addon-configs/2effc9b9_vaultwarden/config.json`手动配置许多参数
1. 确保您的`admin_token`是argon2加密的：https://github.com/dani-garcia/vaultwarden/wiki/Enabling-admin-page#secure-the-admin_token
1. 如果不是，`docker ps | grep "vault"`和前面的数字/字母是容器ID
2. `docker exec -it containerID /bin/bash`
3. `cd /` `/vaultwarden hash --preset owasp`输入密码，然后替换管理令牌
4. 由于此文件是可访问的，我猜任何人都可以这样做，所以请小心。如果您可以访问您的homeassistant机器，这也可以在容器内部完成，所以实际上并没有更安全


```
port : 7277 #您想要运行的端口。
```

Webui可以在`<your-ip>:port`找到。

[repository]: https://github.com/jdeath/homeassistant-addons