# Home Assistant Community Add-on: AppDaemon

[AppDaemon][appdaemon] 是一个松耦合、多线程、沙盒化的 Python 执行环境，用于编写 Home Assistant 家庭自动化软件的自动化应用。它还提供了一个可配置的仪表板 (HADashboard)，适合安装在墙壁上的平板电脑上。

## 安装

这个插件的安装过程非常简单，与其他 Home Assistant 插件的安装方式相同。

1. 点击下面的 Home Assistant My 按钮来在你的 Home Assistant 实例中打开插件。

   ![在你的 Home Assistant 实例中打开这个插件][ addon-badge ][ addon ]

1. 点击 "Install" 按钮来安装插件。
1. 启动 "AppDaemon" 插件
1. 查看 "AppDaemon" 插件的日志，以确认一切是否正常。

:information_source: 请注意，这个插件已经预先配置好与 Home Assistant 连接。无需创建访问令牌或设置 Home Assistant URL 在 AppDaemon 配置中。

这种自动处理 URL 和令牌的方式与 [AppDaemon 官方文档][appdaemon] 冲突。官方文档会声明 `ha_url` 和 `token` 选项是必需的。然而，对于这个插件来说，这并非必需的。

## 配置

**注意**: _记得在更改配置时重启插件。_

示例插件配置：

```yaml
log_level: info
system_packages:
  - ffmpeg
python_packages:
  - PyMySQL
  - Pillow
```

**注意**: _这只是一个示例，不要复制粘贴它！创建你自己的！_

### 选项: `log_level`

`log_level` 选项控制插件输出的日志级别，可以根据需要设置为更详细或更简洁，这在处理未知问题时可能很有用。可能的值有：

- `trace`: 显示所有细节，例如所有调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 通常的（通常）有趣的正常事件。
- `warning`: 非常规的事件，但不是错误。
- `error`: 运行时错误，不需要立即采取行动。
- `fatal`: 发生了严重错误。插件变得无法使用。

请注意，每个级别会自动包含更严重级别的日志消息，例如，`debug` 也会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非你在进行故障排除。

这些日志级别也会影响 AppDaemon 的日志级别。

### 选项: `system_packages`

允许你指定额外的 [Alpine 软件包][alpine-packages] 安装到你的 AppDaemon 设置中（例如，`g++`、`make`、`ffmpeg`）。

**注意**: _添加许多软件包会导致插件启动时间变长。_

### 选项: `python_packages`

允许你指定额外的 [Python 软件包][python-packages] 安装到你的 AppDaemon 设置中（例如，`PyMySQL`、`Requests`、`Pillow`）。

**注意**: _添加许多软件包会导致插件启动时间变长。_

#### 选项: `init_commands`

使用 `init_commands` 选项可以进一步自定义你的环境。将一个或多个 Shell 命令添加到列表中，它们将在每次插件启动时执行。

## AppDaemon 和 HADashboard 配置

这个插件不会为你配置 AppDaemon 或 HADashboard。然而，它会在首次运行时创建一些示例文件来帮助你开始。

AppDaemon 的配置可以在这个插件的配置文件夹中找到。

有关配置 AppDaemon 的更多信息，请参考他们提供的详细文档：

<http://appdaemon.readthedocs.io/en/latest/>

## Home Assistant 访问令牌和 ha_url 设置

默认情况下，这个插件不带有 `token` 和 `ha_url` 在 `appdaemon.yaml` 配置文件中。**这不是一个错误！**

插件会为你处理这些设置，你无需在 AppDaemon 配置中提供或设置这些内容。

这种自动处理 URL 和令牌的方式与 AppDaemon 官方文档冲突。官方文档会声明 `ha_url` 和 `token` 选项是必需的。对于这个插件来说，这些并不是必需的。

然而，如果你希望覆盖它们，你可以自由设置它们。然而，在一般情况下，这可能不是必需的，也不推荐使用这个插件。

## 更改日志与发布

这个仓库使用 [GitHub 的发布][releases] 功能来维护更改日志。

发布基于 [语义版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将根据以下内容进行增加：

- `MAJOR`: 不兼容或主要更改。
- `MINOR`: 向后兼容的新功能和增强。
- `PATCH`: 向后兼容的补丁和软件包更新。

## 支持

有问题吗？

你有几个选项来获得答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord] 用于插件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 用于一般的 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

你也可以在 GitHub 上 [打开一个问题][issue]。

## 作者与贡献者

这个仓库的原始设置由 [Franck Nijhof][frenck] 完成。

要查看所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2021 - 2025 Franck Nijhof

特此免费授予任何获得此软件及其相关文档文件（“软件”）副本的人，在不受限制的情况下处理该软件的权利，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权利，并允许获得软件的人这样做，但须满足以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件按“原样”提供，不提供任何形式的保证，包括但不限于对适销性、特定用途适用性和非侵权的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害或其他责任负责，无论这些责任是由于合同、侵权或其他行为引起的，还是由于与软件的使用或其他交易有关。