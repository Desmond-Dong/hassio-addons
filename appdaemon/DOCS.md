# Home Assistant Community Add-on: AppDaemon

[AppDaemon][appdaemon] 是一个松散耦合、多线程、沙盒化的 Python 执行环境，用于编写 Home Assistant 家用自动化软件的自动化应用。它还提供了一个可配置的仪表板（HADashboard），适用于壁挂式平板电脑。

## 安装

这个插件的安装过程非常简单，与安装任何其他 Home Assistant 插件没有区别。

1. 点击下方的 Home Assistant My 按钮，在您的 Home Assistant 实例中打开插件。

   ![在您的 Home Assistant 实例中打开此插件][addon-badge]][ addon]

1. 点击“安装”按钮来安装插件。
1. 启动“AppDaemon”插件
1. 检查“AppDaemon”插件的日志，看看是否一切正常。

:information_source: 请注意，该插件已预配置为与 Home Assistant 连接。无需创建访问令牌或在 AppDaemon 配置中设置您的 Home Assistant URL。

这种自动处理 URL 和令牌的方式与 [AppDaemon 官方文档][appdaemon] 矛盾。官方文档将说明 `ha_url` 和 `token` 选项是必需的。然而，对于插件来说，这不是必需的。

## 配置

**注意**: _更改配置时，请记住重启插件。_

示例插件配置：

```yaml
log_level: info
system_packages:
  - ffmpeg
python_packages:
  - PyMySQL
  - Pillow
```

**注意**: _这只是个示例，不要复制粘贴！创建你自己的！_

### 选项: `log_level`

`log_level` 选项控制插件输出的日志级别，可以更改为更详细或更简洁，这在处理未知问题时可能很有用。可能的值有：

- `trace`: 显示所有细节，例如所有调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 正常（通常）有趣的事件。
- `warning`: 非常规的异常情况，但不是错误。
- `error`: 运行时错误，不需要立即采取行动。
- `fatal`: 发生了严重错误。插件变得无法使用。

请注意，每个级别会自动包含更严重级别的日志消息，例如，`debug` 也显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐设置，除非你在排错。

这些日志级别也会影响 AppDaemon 的日志级别。

### 选项: `system_packages`

允许您指定要安装到 AppDaemon 设置中的额外 [Alpine 软件包][alpine-packages]（例如，`g++`、`make`、`ffmpeg`）。

**注意**: _添加许多软件包将导致插件启动时间更长。_

### 选项: `python_packages`

允许您指定要安装到 AppDaemon 设置中的额外 [Python 软件包][python-packages]（例如，`PyMySQL`、`Requests`、`Pillow`）。

**注意**: _添加许多软件包将导致插件启动时间更长。_

#### 选项: `init_commands`

使用 `init_commands` 选项进一步自定义您的环境。将一个或多个 shell 命令添加到列表中，它们将在每次启动此插件时执行。

## AppDaemon 和 HADashboard 配置

这个插件不会为您配置 AppDaemon 或 HADashboard。然而，它确实在首次运行时创建了一些示例文件来帮助您开始。

AppDaemon 的配置可以在该插件的配置文件夹中找到。

有关配置 AppDaemon 的更多信息，请参考他们提供的详细文档：

<http://appdaemon.readthedocs.io/en/latest/>

## Home Assistant 访问令牌和 ha_url 设置

默认情况下，这个插件不包含 `token`，也不在 `appdaemon.yaml` 配置文件中包含 `ha_url`。**这不是一个错误！**

插件会为您处理这些设置，您无需在 AppDaemon 配置中提供或设置这些内容。

这种自动处理 URL 和令牌的方式与 [AppDaemon 官方文档][appdaemon] 矛盾。官方文档将说明 `ha_url` 和 `token` 选项是必需的。对于插件来说，这些不是必需的。

然而，如果您想覆盖它们，您也可以设置它们。但在一般情况下，这应该是不必要的，也不建议为此插件设置。

## 更改日志与发布

此存储库使用 [GitHub 的发布][releases] 功能来维护更改日志。

发布基于 [语义版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 格式。简而言之，版本将根据以下情况增加：

- `MAJOR`: 不兼容或重大变更。
- `MINOR`: 向后兼容的新功能和增强。
- `PATCH`: 向后兼容的补丁和软件包更新。

## 支持

有问题吗？

您有几个选项来获得答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord] 用于插件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

您也可以在 GitHub 上 [打开一个问题][issue]。

## 作者与贡献者

此存储库的原始设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2021 - 2025 Franck Nijhof

特此免费授予任何获得此软件及其相关文档文件（“软件”）副本的人，在软件上进行的操作不受限制，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权利，并允许提供软件的人进行这些操作，但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件按“原样”提供，不提供任何形式的保证，包括但不限于对适销性、特定用途适用性和非侵权性的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害赔偿或其他责任承担责任，无论是因合同、侵权或其他行为引起的，也无论是直接或间接地与软件或软件的使用或其他交易有关。