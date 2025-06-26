# Home Assistant Community Add-on: AppDaemon

[AppDaemon][appdaemon] 是一个松散耦合的、多线程的、沙盒化的 Python 执行环境，旨在为 Home Assistant 家庭自动化软件编写自动化应用程序。它还提供一个可配置的仪表板（HADashboard），适合墙壁挂置的平板电脑。

## 安装

此插件的安装过程相当简单，与安装其他 Home Assistant 插件没有区别。

1. 点击下面的 Home Assistant 我的按钮以打开您 Home Assistant 实例中的插件。

   [![在您的 Home Assistant 实例中打开此插件。][addon-badge]][addon]

1. 点击“安装”按钮以安装插件。
1. 启动“AppDaemon”插件。
1. 检查“AppDaemon”插件的日志，以查看是否一切正常。

:information_source: 请注意，该插件已预配置与 Home Assistant 连接。无需在 AppDaemon 配置中创建访问令牌或设置您的 Home Assistant URL。

这种自动处理 URL 和令牌的方式与 [AppDaemon 官方文档][appdaemon] 冲突。官方文档将说明 `ha_url` 和 `token` 选项是必需的。然而，对于此插件，这不需要。

## 配置

**注意**：_记得在更改配置后重启插件。_

示例插件配置：

```yaml
log_level: info
system_packages:
  - ffmpeg
python_packages:
  - PyMySQL
  - Pillow
```

**注意**：_这只是一个示例，不要复制和粘贴！创建您自己的！_

### 选项： `log_level`

`log_level` 选项控制插件的日志输出级别，可以根据需要更改为更详细或更简洁，这在处理未知问题时可能会很有用。可能的值包括：

- `trace`：显示每个细节，如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：不属于错误的异常情况。
- `error`：运行时错误，不需要立即处理。
- `fatal`：出现严重问题。插件变得不可用。

请注意，每个级别自动包括来自更严重级别的日志消息，例如，`debug` 还会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您在进行故障排除。

这些日志级别也会影响 AppDaemon 的日志级别。

### 选项： `system_packages`

允许您指定要安装到 AppDaemon 设置中的其他 [Alpine 包][alpine-packages]（例如，`g++`、`make`、`ffmpeg`）。

**注意**：_添加多个包将导致插件的启动时间变长。_

### 选项： `python_packages`

允许您指定要安装到 AppDaemon 设置中的其他 [Python 包][python-packages]（例如，`PyMySQL`、`Requests`、`Pillow`）。

**注意**：_添加多个包将导致插件的启动时间变长。_

#### 选项： `init_commands`

使用 `init_commands` 选项进一步自定义您的环境。将一个或多个 shell 命令添加到列表中，它们将在每次启动此插件时执行。

## AppDaemon 和 HADashboard 配置

此插件不会为您配置 AppDaemon 或 HADashboard。然而，它会在第一次运行时创建一些示例文件以帮助您入门。

AppDaemon 的配置可以在此插件的配置文件夹中找到。

有关配置 AppDaemon 的更多信息，请参阅他们提供的详细文档：

<http://appdaemon.readthedocs.io/en/latest/>

## Home Assistant 访问令牌和 ha_url 设置

默认情况下，此插件不包含 `token` 和 `ha_url` 在 `appdaemon.yaml` 配置文件中。**这不是错误！**

该插件为您处理这些设置，您不需要在 AppDaemon 配置中提供或设置这些。

这种对 URL 和令牌的自动处理与 AppDaemon 官方文档冲突。官方文档将说明 `ha_url` 和 `token` 选项是必需的。对于此插件，这些不是必需的。

不过，您可以自由设置它们，如果您想要覆盖，但通常情况下，这是不需要的，并且不建议对于此插件。

## 更新日志与发行版

此仓库使用 [GitHub 的发布][releases] 功能保留变更日志。

发布基于 [语义版本控制][semver]，使用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将根据以下内容进行递增：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新特性和增强功能。
- `PATCH`：向后兼容的错误修复和包更新。

## 支持

有问题吗？

您有几种选择可以获得解答：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord]，用于插件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha]，用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]。

您还可以 [在这里提出问题][issue] GitHub。

## 作者与贡献者

此仓库的原始设置由 [Franck Nijhof][frenck] 完成。

要查看所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2021 - 2025 Franck Nijhof

特此免费授权任何获取该软件及其相关文档文件（“软件”）副本的人，不受限制地使用、复制、修改、合并、发布、分发、再授权和/或出售该软件的副本，并允许提供该软件的人这样做，受以下条件的限制：

上述版权声明和此许可声明应包含在所有副本或软件的实质性部分中。

本软件按“现状”提供，不提供任何形式的担保，无论是明示或暗示的，包括但不限于对适销性、特定用途的适用性和不侵权的保证。在任何情况下，作者或版权持有人均不对因使用本软件或与本软件的使用或其他交易有关的任何索赔、损害或其他责任负责，无论是基于合同、侵权或其他方式。

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