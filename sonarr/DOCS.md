# Home Assistant Community Add-on: Sonarr

智能PVR（个人视频录像机）适用于新闻组和BitTorrent用户。

## 安装

此插件的安装过程非常简单，与安装任何其他Home Assistant插件的方式相同。

1. 点击下面的Home Assistant“我的”按钮，在您的Home Assistant实例中打开此插件。

   ![在您的Home Assistant实例中打开此插件][addon-badge]][addon]

1. 点击“安装”按钮以安装插件。
1. 启动“Sonarr”插件
1. 检查“Sonarr”插件的日志，以查看是否一切顺利。
1. 点击“打开Web UI”以打开Sonarr界面。
1. 完成屏幕上显示的向导。

## 配置

_此插件运行无需任何配置。_

## 已知问题和限制

- 此插件不支持Home Assistant的Ingress功能（即，将插件放入Home Assistant侧边栏的切换按钮）。
  考虑到涉及的因素太多，要使其正常工作非常困难，如果尝试这样做，很容易出错。您可以考虑使用iframe面板。

## 更改日志与发布

此存储库使用[GitHub的发布][releases]功能维护更改日志。

发布基于[语义版本控制][semver]，并使用`MAJOR.MINOR.PATCH`的格式。简而言之，版本将根据以下情况增加：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的bug修复和软件包更新。

## 支持

有问题？

您有几个选项来获得答案：

- 用于插件支持和功能请求的[Home Assistant社区插件Discord聊天服务器][discord]。
- 用于一般Home Assistant讨论和问题的[Home Assistant Discord聊天服务器][discord-ha]。
- Home Assistant的[社区论坛][forum]。
- 加入Reddit的[homeassistant子版块][reddit]在[/r/homeassistant][reddit]

您也可以在GitHub上[打开问题][issue]。

## 作者与贡献者

此存储库的原始设置由[Franck Nijhof][frenck]完成。

要查看所有作者和贡献者的完整列表，
请查看[贡献者页面][contributors]。

## 许可证

MIT许可证

版权所有（c）2024-2025 Franck Nijhof

特此授予任何获得此软件及其相关文档文件（“软件”）副本的人，在软件中自由处理的权限，不受任何限制，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权限，并允许获得软件的人这样做，但须遵守以下条件：

上述版权声明和此许可声明应包含在软件的所有副本或重要部分中。

软件按“原样”提供，不提供任何形式的保证，无论是明示的还是暗示的，包括但不限于对适销性、特定用途适用性和非侵权的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害赔偿或其他责任负责，无论这些责任是由合同、侵权或其他行为引起的，均由软件或使用软件或其他交易引起。

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