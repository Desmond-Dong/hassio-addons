# Home Assistant Community Add-on: ZeroTier One

[ZeroTier][zerotier] 提供了 VPN、SDN 和 SD-WAN 的功能，只需一个系统。管理您在本地和广域网上的所有连接资源，就像整个世界是一个单一的数据中心一样。

人们使用 ZeroTier 无缝连接笔记本电脑、台式机、手机、嵌入式设备、云资源和应用程序，无论他们想去哪里。它将整个世界变成了一个单一的数据中心，您现在可以使用此插件添加您的 Home Assistant 实例。

## 安装

此插件的安装非常简单，与安装任何其他 Home Assistant 插件没有区别。

1. 点击下面的 Home Assistant 我的按钮，在您的 Home Assistant 实例上打开此插件。

   [![在您的 Home Assistant 实例中打开此插件][addon-badge]][addon]

1. 点击“安装”按钮以安装插件。
1. 在 [zerotier.com][zerotier] 创建一个免费账户并获取一个网络 ID。
1. 设置“network_id”插件选项，使用您的网络 ID。
1. 启动“ZeroTier One”插件。
1. 检查“ZeroTier One”插件的日志，看看是否一切正常。
1. 实例将出现在您的 ZeroTier 账户中。

## 配置

**注意**：_更改配置时请记得重启插件。_

示例插件配置：

```yaml
networks:
  - wgfyiwe73747457
  - fhu3888892jjfdk
api_auth_token: ""
```

**注意**：_这只是个示例，不要复制粘贴！创建你自己的！_

### 选项：`log_level`

`log_level` 选项控制插件的日志输出级别，可以更改为更详细或更简洁，这在您处理未知问题时可能很有用。可能的值包括：

- `trace`：显示所有细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：异常情况，但不是错误。
- `error`：运行时错误，不需要立即采取行动。
- `fatal`：出了严重问题。插件变得无法使用。

请注意，每个级别自动包括更严重级别的日志消息，例如，`debug` 也显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐设置，除非您正在排错。

### 选项：`networks`

配置一个或多个要加入的网络（VLAN）的网络标识符。您可以在您的 ZeroTier 账户中找到这个编号。

**注意**：_此选项支持密钥，例如，`!secret zerotier_network_id`。_

### 选项：`api_auth_token`

ZeroTier 提供了一个本地 HTTP JSON API，它使用上面设置的 `port` 选项的端口。它允许工具和程序访问此 ZeroTier 实例以查询数据（或控制它）。

此令牌类似于访问该 API 的密码，如果您不打算使用此功能，可以留空此选项。

有关 ZeroTier JSON API 的更多信息，请参阅他们的文档 [api]。

**注意**：_此选项支持密钥，例如，`!secret zerotier_token`。_

## 更改日志与发布

此存储库使用 GitHub 的发布功能维护更改日志。

发布基于 [语义版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 格式。简而言之，版本将根据以下情况增加：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的补丁和包更新。

## 支持

有问题？

您有几个选项可以回答这些问题：

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

版权所有 (c) 2019-2025 Franck Nijhof

特此免费授予任何获得此软件及其相关文档文件（“软件”）副本的人，在软件上进行处理的权限，不受任何限制，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权限，并允许提供软件的人这样做，但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分的软件中。

软件按“原样”提供，不提供任何明示或暗示的保证，包括但不限于适销性、特定用途适用性和非侵权保证。在任何情况下，作者或版权持有人均不对任何索赔、损害或其他责任承担责任，无论是合同行为、侵权行为还是其他行为，均源于、发生于或与软件的使用或其他交易有关。

[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[addon]: https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_zerotier&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository
[api]: https://www.zerotier.com/manual.shtml#4_1
[contributors]: https://github.com/hassio-addons/addon-zerotier/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-zerotier-one/109091?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-zerotier/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-zerotier/releases
[semver]: https://semver.org/spec/v2.0.0.html
[zerotier]: https://www.zerotier.com/