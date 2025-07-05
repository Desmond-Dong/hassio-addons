# Home Assistant Community Add-on: UniFi Network Application

这个插件运行 Ubiquiti Networks 的 UniFi Network Application 软件应用程序，允许您通过网页浏览器管理您的 UniFi 网络。该插件为 Home Assistant 提供一键安装和运行解决方案，使用户能够轻松地启动、运行和更新其网络。

## 安装

此插件的安装非常直接，与安装任何其他 Home Assistant 插件没有区别。

1. 点击下方的 Home Assistant "我的"按钮，在您的 Home Assistant 实例中打开该插件。

   [![在您的 Home Assistant 实例中打开此插件][ addon-badge]][ addon]

1. 点击 "安装" 按钮来安装插件。
1. 检查 "UniFi Network Application" 的日志，以查看是否一切顺利。
1. 点击 "打开 Web UI" 按钮，并按照初始向导进行操作。
1. 完成向导后，使用刚刚创建的凭据登录。
1. 转到设置（左下角的齿轮图标）-> 系统 -> 高级。
1. 在 `Inform Host` 标签旁边，点击 `覆盖` 的复选框选项，使其现在为 "已选中"。
1. 将 `Inform 主机` 更改为与运行 Home Assistant 的设备的 IP 或主机名匹配。
1. 点击 "应用更改" 按钮以激活设置。
1. 准备就绪！

## 配置

**注意**: _更改配置时，请记得重启插件。_

示例插件配置，包含所有可用选项：

```yaml
log_level: info
memory_max: 2048
memory_init: 512
```

**注意**: _这只是一个示例，不要复制粘贴！自己创建！_

### 选项: `log_level`

`log_level` 选项控制插件的日志输出级别，可以更改为更详细或更简洁，这在您处理未知问题时可能很有用。可能的值有：

- `trace`: 显示所有细节，例如所有调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 普通（通常）有趣的事件。
- `warning`: 非常规的异常情况，但不是错误。
- `error`: 运行时错误，不需要立即采取行动。
- `fatal`: 发生了严重错误。插件变得无法使用。

请注意，每个级别自动包含更严重级别的日志消息，例如，`debug` 也显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐设置，除非您正在解决问题。

### 选项: `memory_max`

此选项允许您更改 UniFi Network Application 允许消耗的内存量。默认情况下，这限制为 256 MB。您可能希望增加此值，以减少 CPU 负载，或减少此值，以优化您的系统以降低内存使用。

此选项以兆字节为单位，例如，默认值为 256。

### 选项: `memory_init`

此选项允许您更改 UniFi Network Application 在启动时最初保留/消耗的内存量。默认情况下，这限制为 128MB。

此选项以兆字节为单位，例如，默认值为 128。

## 自动备份

UniFi Network Application 配备了自动备份功能。此功能可以正常工作，但已调整以将创建的备份放在不同的位置。

备份在 `/backup/unifi` 中创建。您可以使用正常的 Home Assistant 方法访问此文件夹（例如，使用 Samba、终端、SSH）。

## 手动采用设备

除了设置自定义 inform 地址（安装步骤 7-9）之外，您还可以通过以下步骤手动采用设备：

- 使用 `ubnt` 作为用户名和密码通过 SSH 连接到设备
- `$ mca-cli`
- `$ set-inform http://<Hassio 的 IP>:<控制器端口（默认：8080）>/inform`
  - 例如 `$ set-inform http://192.168.1.14:8080/inform`

## 已知问题和限制

- AP 似乎卡在 "采用" 状态：请仔细阅读安装说明。您需要更改一些控制器设置，以便此插件能够正常工作。使用 Ubiquiti 发现工具，或通过 SSH 连接到 AP 并在采用后设置 INFORM 将解决这个问题。（参见：_手动采用设备_）
- 以下错误可能会在日志中显示，但可以安全地忽略：

  ```
    INFO: I/O 异常 (java.net.ConnectException) 在处理请求时捕获：连接被拒绝 (Connection refused)
  ```

  这是一个已知问题，但是插件可以正常工作。

- 由于 UniFi Network Application 软件的安全策略，目前无法使用 `panel_iframe` 将 UniFI 网页界面添加到您的 Home Assistant 前端。
- EDU 类 AP 的广播功能目前无法与此插件一起使用。由于 Home Assistant 的限制，目前无法打开此功能所需的 "范围" 的端口。
- 由于 UniFi 软件的技术限制，此插件不支持 Ingress。
- 通过 Home Assistant 备份此插件时，此插件将临时关闭，并在备份完成后启动。这可以防止在备份过程中数据损坏。

## 更改日志和发布

此存储库使用 [GitHub 的发布][releases] 功能维护更改日志。日志的格式基于 [Keep a Changelog][keepchangelog]。

发布基于 [语义版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将根据以下情况递增：

- `MAJOR`: 不兼容或主要更改。
- `MINOR`: 向后兼容的新功能和增强。
- `PATCH`: 向后兼容的错误修复和软件包更新。

## 支持

有问题？

您有几个选项可以回答它们：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord] 用于插件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 用于一般的 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

您还可以在 GitHub 上 [打开一个问题][issue]。

## 作者和贡献者

此存储库的原始设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2018-2025 Franck Nijhof

特此免费授予任何获得此软件及其相关文档文件（以下简称 "软件"）副本的人，在不受限制的情况下处理软件的权利，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权利，并允许提供软件的人这样做，但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件按 "原样" 提供，不提供任何形式的保证，无论是明示的还是暗示的，包括但不限于对适销性、特定用途适用性和非侵权性的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害赔偿或其他责任承担责任，无论是由合同、侵权或其他行为引起的，均与软件或软件的使用或其他交易有关。

[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[addon]: https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_unifi&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository
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