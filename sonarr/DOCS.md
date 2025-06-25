# Home Assistant Community Add-on: Sonarr

新sgroup和bittorrent用户的智能PVR。

## 安装

此插件的安装非常简单，与安装其他Home Assistant插件没有什么不同。

1. 点击下面的 Home Assistant 我的按钮以打开您 Home Assistant 实例上的插件。

   [![在您的 Home Assistant 实例中打开此插件。][addon-badge]][addon]

1. 点击“安装”按钮以安装插件。
1. 启动“Sonarr”插件。
1. 检查“Sonarr”插件的日志以查看一切是否顺利。
1. 点击“打开网页界面”以打开 Sonarr 界面。
1. 完成屏幕上的向导。

## 配置

_此插件运行不需要任何配置。_

## 已知问题和限制

- 此插件不支持 Home Assistant 的 Ingress 功能（即，将插件放在 Home Assistant 侧边栏的切换）。
  考虑到需要处理的变量实在太多，如果要实现这个功能，很容易出错。您可以考虑使用 iframe 面板来代替。

## 更新日志与发布

该存储库使用 [GitHub的发布][releases] 功能保留变更日志。

发布基于 [语义版本控制][semver]，采用 `MAJOR.MINOR.PATCH` 的格式。简单来说，版本将根据以下内容进行递增：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新功能和增强功能。
- `PATCH`：向后兼容的bug修复和包更新。

## 支持

有问题吗？

您有几种方式可以获得答案：

- [Home Assistant社区插件 Discord 聊天服务器][discord]以获取插件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha]以进行一般的 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [/r/homeassistant][reddit] 的 [Reddit 子版块][reddit]

您也可以在 [这里打开一个问题][issue] GitHub。

## 作者与贡献者

该存储库的原始设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2024-2025 Franck Nijhof

特此授予任何获得本软件及相关文档文件（简称“软件”）副本的人，无偿地处置该软件的权利，包括但不限于使用、复制、修改、合并、出版、分发、再授权和/或出售该软件副本的权利，以及允许提供该软件的人这样做，但需遵循以下条件：

上述版权声明和本许可声明应包含在所有副本或软件的重要部分中。

该软件是按“原样”提供的，不提供任何种类的保证，无论是明示还是暗示，包括但不限于对适销性、特定用途的适用性和非侵权的保证。在任何情况下，作者或版权持有人均不对因使用软件或与之相关的其他交易而引起的索赔、损害或其他责任负责，无论是合同、侵权还是其他方式。

[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[addon]: https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_sonarr&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository
[contributors]: https://github.com/hassio-addons/addon-sonarr/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-sonarr/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-sonarr/releases
[semver]: http://semver.org/spec/v2.0.0.html