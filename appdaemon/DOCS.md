# Home Assistant 社区插件: AppDaemon

[AppDaemon][appdaemon] 是一个松耦合、多线程、沙箱式的 Python 执行环境，用于为 Home Assistant 家居自动化软件编写自动化应用程序。它还提供了一个可配置的仪表板（HADashboard），适合墙挂式平板电脑。

## 安装

这个插件的安装非常简单，与安装其他 Home Assistant 插件没有什么不同。

1. 点击下面的 Home Assistant 我的按钮，以在您的 Home Assistant 实例中打开插件。

   [![在您的 Home Assistant 实例中打开此插件。][addon-badge]][addon]

1. 点击“安装”按钮以安装插件。
1. 启动“AppDaemon”插件
1. 检查“AppDaemon”插件的日志，以查看一切是否顺利。

:information_source: 请注意，插件已预先配置以连接到 Home Assistant。无需创建访问令牌或在 AppDaemon 配置中设置您的 Home Assistant URL。

这种对 URL 和令牌的自动处理与 [AppDaemon 官方文档][appdaemon] 相冲突。官方文档将指出需要 `ha_url` 和 `token` 选项。然而，对于该插件，这并不是必需的。

## 配置

**注意**: _请记得在更改配置后重启插件。_

示例插件配置：

```yaml
log_level: info
system_packages:
  - ffmpeg
python_packages:
  - PyMySQL
  - Pillow
```

**注意**: _这只是一个示例，请不要复制粘贴！请创建您自己的！_

### 选项: `log_level`

`log_level` 选项控制插件的日志输出级别，可以更改为更详细或更简洁，这在处理未知问题时可能会很有用。可能的值包括：

- `trace`: 显示每一个细节，如所有调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 正常（通常是）有趣的事件。
- `warning`: 非错误的异常事件。
- `error`: 不需要立即处理的运行时错误。
- `fatal`: 出现严重错误。插件变得不可用。

请注意，每个级别自动包括来自更严重级别的日志消息，例如，`debug` 也会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您在排错。

这些日志级别也会影响 AppDaemon 的日志级别。

### 选项: `system_packages`

允许您指定要安装到您的 AppDaemon 设置中的额外 [Alpine 包][alpine-packages]（例如，`g++`，`make`，`ffmpeg`）。

**注意**: _添加许多包会导致插件启动时间变长。_

### 选项: `python_packages`

允许您指定要安装到您的 AppDaemon 设置中的额外 [Python 包][python-packages]（例如，`PyMySQL`，`Requests`，`Pillow`）。

**注意**: _添加许多包会导致插件启动时间变长。_

#### 选项: `init_commands`

通过 `init_commands` 选项进一步自定义您的环境。将一个或多个 shell 命令添加到列表中，它们会在每次启动该插件时执行。

## AppDaemon 和 HADashboard 配置

该插件不会为您配置 AppDaemon 或 HADashboard。然而，它会创建一些示例文件，以帮助您在首次运行时入门。

AppDaemon 的配置可以在此插件的配置文件夹中找到。

有关配置 AppDaemon 的更多信息，请参阅他们提供的详细文档：

<http://appdaemon.readthedocs.io/en/latest/>

## Home Assistant 访问令牌和 ha_url 设置

默认情况下，该插件不带 `token` 也不带 `ha_url` 在 `appdaemon.yaml` 配置文件中。 **这不是一个错误！**

插件会为您处理这些设置，您无需在 AppDaemon 配置中提供或设置这些。

这种 URL 和令牌的自动处理与 AppDaemon 官方文档相冲突。官方文档将指出需要 `ha_url` 和 `token` 选项。然而，对于该插件，这并不是必需的。

但是，您可以自由设置它们，如果您想要覆盖；然而，在一般使用中，这种设置通常不是必需的，并且不推荐用于该插件。

## 更新日志 & 发布

该库使用 [GitHub 的发布][releases] 功能保持变更日志。

发布基于 [语义版本控制][semver]，使用 `MAJOR.MINOR.PATCH` 格式。简而言之，版本将根据以下情况增加：

- `MAJOR`: 不兼容或重大更改。
- `MINOR`: 向后兼容的新功能和增强。
- `PATCH`: 向后兼容的错误修复和包更新。

## 支持

有问题？

您有几种选择来获取答案：

- [Home Assistant 社区插件 Discord 聊天服务器][discord] 以获取插件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 用于一般的 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

您也可以 [在这里提出问题][issue] GitHub。

## 作者 & 贡献者

该库的最初设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可

MIT 许可证

版权所有 (c) 2021 - 2024 Franck Nijhof

特此授予任何获得本软件及相关文档文件（“软件”）副本的人，免费处理该软件的权利，包括但不限于使用、复制、修改、合并、发布、分发、再授权和/或销售该软件副本的权利，并允许向其提供软件的人员这样做，须遵守以下条件：

上述版权声明和本许可声明应包括在所有副本或软件的实质性部分中。

该软件在“原样”基础上提供，不提供任何类型的担保，无论是明示或暗示，包括但不限于对适销性、特定用途适用性的担保和非侵权的担保。在任何情况下，作者或版权持有者均不对因使用该软件或其他交易引起的任何索赔、损害或其他责任承担责任，无论是在合同诉讼、侵权行为或其他方式中。

[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[addon]: https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_appdaemon&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository
[alpine-packages]: https://pkgs.alpinelinux.org/packages
[appdaemon]: https://appdaemon.readthedocs.io
[contributors]: https://github.com/hassio-addons/addon-appdaemon/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-appdaemon-4/163259?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-appdaemon/issues
[python-packages]: https://pypi.org/
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-appdaemon/releases
[semver]: http://semver.org/spec/v2.0.0.htm