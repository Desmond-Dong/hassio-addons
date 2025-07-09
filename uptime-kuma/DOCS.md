# Home Assistant Community Add-on: Uptime Kuma

Uptime Kuma 是一个开源的监控工具，它最类似于商业服务（如 "Uptime Robot"）的自托管版本。

它使您能够监控 HTTP/S、TCP、DNS 和其他协议下的服务，并且可以发送您停机通知或触发 Home Assistant 自动化 webhooks。

## 安装

此插件的安装非常简单，与安装任何其他 Home Assistant 插件没有区别。

1. 点击下面的 Home Assistant "我的"按钮，在您的 Home Assistant 实例上打开此插件。

   ![在您的 Home Assistant 实例中打开此插件][addon-badge]][addon]

1. 点击 "安装" 按钮来安装插件。
1. 启动 "Uptime Kuma" 插件。
1. 检查 "Uptime Kuma" 的日志，看看是否一切顺利。
1. 点击 "打开 Web UI" 按钮进入 Uptime Kuma。

请继续阅读此文档以获取进一步说明。

## 配置

此插件没有配置选项，所有内容都可以通过 Uptime Kuma 界面进行管理和配置。

## 更改日志与发布

此存储库使用 [GitHub 的发布][releases] 功能来维护更改日志。日志的格式基于
[Keep a Changelog][keepchangelog]。

发布基于 [语义版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将根据以下情况增加：

- `MAJOR`：不兼容或主要更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的补丁和软件包更新。

## 支持

有问题？

您有几个选项来获得答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord] 用于插件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

您也可以在 GitHub 上 [打开一个问题][issue]。

## 作者与贡献者

此存储库的原始设置由 [Franck Nijhof][frenck] 完成。

要获取所有作者和贡献者的完整列表，
请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有（c）2022-2025 Franck Nijhof

特此授予任何获得此软件及其相关文档文件（“软件”）副本的人，在不限制的情况下自由处理软件的权利，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或出售软件副本的权利，并允许获得软件的人这样做，但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件按“原样”提供，不提供任何形式的保证，无论是明示的还是暗示的，包括但不限于对适销性、特定用途适用性和非侵权性的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害赔偿或其他责任负责，无论是由合同、侵权或其他行为引起的，均与软件或软件的使用或其他交易有关。

[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[addon]: https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_uptime-kuma&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository
[contributors]: https://github.com/hassio-addons/addon-uptime-kuma/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-uptime-kuma/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-uptime-kuma/releases
[semver]: https://semver.org/spec/v2.0.0.html