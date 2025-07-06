# Home Assistant Community Add-on: Nginx Proxy Manager

这个插件使您能够轻松地将传入连接转发到任何地方，包括免费的SSL，而无需了解太多关于Nginx或Let’s Encrypt的信息。

将您的域名转发到您的Home Assistant、插件或在家中或任何其他地方运行的网站，直接从简单而强大的界面进行操作。

想要用用户名/密码保护网站吗？好吧，它也可以做到！启用身份验证并创建一个可以访问该特定应用程序的用户名/密码列表。

对于高级用户，您可以通过提供额外的Nginx指令来自定义Nginx代理管理器中每个主机的行为。

## 安装

这个插件的安装非常简单，与安装任何其他Home Assistant插件没有什么不同。

1. 点击下面的Home Assistant My按钮，在您的Home Assistant实例上打开插件。

   [![在您的Home Assistant实例中打开此插件][addon-badge]][addon]

1. 点击“安装”按钮来安装插件。
1. 启动“Nginx Proxy Manager”插件
1. 检查“Nginx Proxy Manager”插件的日志，看看是否一切顺利。
1. 点击“打开Web UI”按钮，并使用以下凭据登录：
   `admin@example.com` / `changeme`
1. 将您的路由器的端口`443`（可选：`80`）转发到您的Home Assistant机器。
1. 享受插件带来的便利！

## 配置

这个插件不提供任何配置。

## 更改日志与发布

这个存储库使用GitHub的发布功能[发布]来维护更改日志。

发布基于[语义版本控制][semver]，并使用`MAJOR.MINOR.PATCH`的格式。简而言之，版本将根据以下情况增加：

- `MAJOR`：不兼容或主要更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的bug修复和软件包更新。

## 支持

有问题吗？

您有几个选项来获得答案：

- 用于插件支持和功能请求的[Home Assistant Community Add-ons Discord聊天服务器][discord]。
- 用于一般Home Assistant讨论和问题的[Home Assistant Discord聊天服务器][discord-ha]。
- Home Assistant的[社区论坛][forum]。
- 加入[Reddit的subreddit][reddit]在[/r/homeassistant][reddit]。

您也可以在这里[打开GitHub上的问题][issue]。

## 作者与贡献者

这个存储库的原始设置由[Franck Nijhof][frenck]完成。

要查看所有作者和贡献者的完整列表，请查看[贡献者页面][contributors]。

## 许可证

MIT许可证

版权所有（c）2019-2025 Franck Nijhof

特此授予任何人免费获得此软件及其相关文档文件（“软件”）的副本的权限，在软件上进行操作，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权利，并允许软件提供者这样做，但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件按“原样”提供，不提供任何明示或暗示的保证，包括但不限于对适销性、特定用途适用性和非侵权性的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害或其他责任承担责任，无论这些责任是由于合同、侵权或其他行为引起的，还是由于软件的使用或其他交易引起的。

[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[addon]: https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_nginxproxymanager&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository
[contributors]: https://github.com/hassio-addons/addon-nginx-proxy-manager/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-nginx-proxy-manager/111830?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-nginx-proxy-manager/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-nginx-proxy-manager/releases
[semver]: https://semver.org/spec/v2.0.0.html