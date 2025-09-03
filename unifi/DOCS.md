# Home Assistant Community Add-on: UniFi Network Application

这个插件运行 Ubiquiti Networks 的 UniFi Network Application 软件应用程序，它允许您通过网页浏览器管理您的 UniFi 网络。该插件为 Home Assistant 提供了一键安装和运行解决方案，使用户可以轻松地让他们的网络启动、运行和更新。

## 安装

这个插件的安装非常简单，与安装任何其他 Home Assistant 插件没有什么不同。

1. 点击下面的 Home Assistant 我的按钮，在您的 Home Assistant 实例中打开该插件。

   ![在您的 Home Assistant 实例中打开此插件][ addon-badge ][ addon ]

1. 点击“安装”按钮来安装插件。
1. 检查“UniFi Network Application”的日志，看看是否一切顺利。
1. 点击“打开 Web UI”按钮，并按照初始向导进行操作。
1. 完成向导后，使用刚刚创建的凭据登录。
1. 选择您可以在左侧找到的 Unifi 设备。在那里，选择右上角的设备更新和设置。
1. 向下滚动到设备设置，并在 `Inform Host Override` 标签下方输入运行 Home Assistant 的设备的 IP 或主机名。
1. 勾选 `Inform Host Override` 的复选框选项，使其现在为“已勾选”。
1. 点击“应用更改”按钮来激活设置。
1. 准备就绪！

## 配置

**注意**：_更改配置时请记得重启插件。_

示例插件配置，包含所有可用选项：

```yaml
log_level: info
memory_max: 2048
memory_init: 512
```

**注意**：_这只是个示例，不要复制粘贴！创建您自己的！_

### 选项：`log_level`

`log_level` 选项控制插件的日志输出级别，可以根据需要设置为更详细或更简洁，这在处理未知问题时可能很有用。可能的值有：

- `trace`：显示所有细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：异常事件，但不是错误。
- `error`：运行时错误，不需要立即采取行动。
- `fatal`：出了严重问题。插件变得无法使用。

请注意，每个级别会自动包含更严重级别的日志消息，例如，`debug` 也会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐设置，除非您正在排错。

### 选项：`memory_max`

这个选项允许您更改 UniFi Network Application 允许消耗的内存量。默认情况下，这限制为 256 MB。您可能希望增加此值，以减少 CPU 负载，或者减少此值，以优化系统以降低内存使用。

这个选项以兆字节为单位，例如，默认值为 256。

### 选项：`memory_init`

这个选项允许您更改 UniFi Network Application 在启动时最初保留/消耗的内存量。默认情况下，这限制为 128MB。

这个选项以兆字节为单位，例如，默认值为 128。

## 自动备份

UniFi Network Application 附带了一个自动备份功能。该功能可以正常工作，但已调整为将创建的备份放在不同的位置。

备份在 `/backup/unifi` 中创建。您可以使用 Home Assistant 的常规方法（例如，使用 Samba、终端、SSH）访问这个文件夹。

## 手动采用设备

或者，您可以通过以下步骤手动采用设备（而不是设置自定义的 inform 地址（安装步骤 7-9））：

- 使用 `ubnt` 作为用户名和密码，通过 SSH 连接到设备
- `$ mca-cli`
- `$ set-inform http://<Hassio 的 IP>:<控制器端口（默认：8080）>/inform`
  - 例如：`$ set-inform http://192.168.1.14:8080/inform`

## 已知问题和限制

- AP 似乎卡在“采用”状态：请仔细阅读安装说明。为了使此插件正常工作，您需要更改一些控制器设置。使用 Ubiquiti 发现工具，或者通过 SSH 连接到 AP 并在采用后设置 INFORM 可以解决这个问题。（参见：_手动采用设备_）
- 以下错误可能会在日志中显示，但可以安全地忽略：

  ```
    INFO: I/O exception (java.net.ConnectException) caught when processing
    request: Connection refused (Connection refused)
  ```

  这是一个已知问题，但是插件可以正常工作。

- 由于 UniFi Network Application 软件的安全策略，目前无法使用 `panel_iframe` 将 UniFI 网页界面添加到您的 Home Assistant 前端。
- EDU 类 AP 的广播功能目前无法与这个插件一起使用。由于 Home Assistant 的限制，目前无法打开所需的“范围”端口以使此功能正常工作。
- 由于 UniFi 软件的技术限制，这个插件无法支持 Ingress。
- 在通过 Home Assistant 备份这个插件时，该插件将暂时关闭，并在备份完成后重新启动。这可以防止在备份过程中数据损坏。

## 更改日志和发布

这个仓库使用 [GitHub 的发布功能][releases] 维护一个更改日志。日志的格式基于 [Keep a Changelog][keepchangelog]。

发布基于 [语义版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将根据以下情况增加：

- `MAJOR`：不兼容或主要更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的补丁和包更新。

## 支持

有问题？

您有几个选项来得到答案：

- [Home Assistant Community Add-ons Discord 服务器][discord] 用于插件支持和功能请求。
- [Home Assistant Discord 服务器][discord-ha] 用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

您也可以在 GitHub 上 [打开一个问题][issue]。

## 作者和贡献者

这个仓库的原始设置由 [Franck Nijhof][frenck] 完成。

要查看所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2018-2025 Franck Nijhof

特此免费授予任何获得此软件及其相关文档文件（“软件”）副本的人，在软件上进行操作的权限，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或出售软件副本的权限，并允许提供软件的人这样做，但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件按“原样”提供，不提供任何明示或暗示的保证，包括但不限于对适销性、特定用途适用性和不侵犯版权的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害或其他责任负责，无论是由合同、侵权或其他行为引起的，均与软件或软件的使用或其他交易有关。

[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[addon]: https://my.home-assistant.io/redirect/supervisor_addon/? addon=a0d7b954_unifi&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository
[contributors]: https://github.com/hassio-addons/addon-unifi/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-unifi-controller/56297?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-unifi/issues
[keepchangelog]: http://keepachangelog.com/en/1.0.0/
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-unifi/releases
[semver]: http://semver.org/spec/v2.0.0.htm