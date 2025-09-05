# Home Assistant Community Add-on: Bazarr

下载和管理 Sonarr 和 Radarr 的字幕。

## 安装

这个插件的安装非常简单，与其他 Home Assistant 插件的安装方式相同。

1. 点击下方的 Home Assistant 我的按钮，在您的 Home Assistant 实例上打开插件。

   [![在您的 Home Assistant 实例中打开此插件][addon-badge]][addon]

1. 点击“安装”按钮来安装插件。
1. 启动“Bazarr”插件
1. 检查“Bazarr”插件的日志，看看是否一切顺利。
1. 点击“打开 Web UI”来打开 Bazarr 界面。
1. 完成屏幕上显示的向导。

- 将下载文件夹设置为，例如，
  `/media/bazarr/Downloads/complete` 和
  `/media/bazarr/Downloads/incomplete`

## 配置

_此插件运行不需要任何配置。_

## 更改日志与发布

此存储库使用 [GitHub 的发布][releases] 功能来维护更改日志。

发布基于 [语义版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将根据以下情况增加：

- `MAJOR`：不兼容或主要更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的修复和软件包更新。

## 支持

有问题吗？

您有几个选项来获得答案：

- [Home Assistant 社区插件 Discord 聊天服务器][discord] 用于插件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 用于一般的 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

您也可以 [在这里打开问题][issue] GitHub。

## 作者与贡献者

此存储库的原始设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，
请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2024-2025 Franck Nijhof

特此免费授予任何获得此软件及其相关文档文件（“软件”）副本的人，
在软件中自由处理的权限，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权限，
并允许获得软件的人这样做，但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件按“原样”提供，不提供任何明示或暗示的保证，包括但不限于对适销性、特定用途适用性和非侵权的保证。
在任何情况下，作者或版权持有人均不对任何索赔、损害或其他责任承担责任，无论是因合同、侵权或其他行为引起的，
与软件或软件的使用或其他交易有关。

[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[addon]: https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_bazarr&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository
[contributors]: https://github.com/hassio-addons/addon-bazarr/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-bazarr/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-bazarr/releases
[semver]: http://semver.org/spec/v2.0.0.html