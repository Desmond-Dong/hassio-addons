# Home Assistant Community Add-on: ZeroTier One

[ZeroTier][zerotier] delivers the capabilities of VPNs, SDN, and SD-WAN with
a single system. Manage all your connected resources across both local
and wide area networks as if the whole world is a single data center.

People use ZeroTier to seamlessly connect laptops, desktops, phones,
embedded devices, cloud resources, and apps any way they want anywhere they go.
It transforms the entire world into a single data center, to which you
can now add your Home Assistant instance using this add-on.

## 安装

The installation of this add-on is pretty straightforward and not different in
comparison to installing any other Home Assistant add-on.

1. Click the Home Assistant My button below to open the add-on on your Home
   Assistant instance.

   [![Open this add-on in your Home Assistant instance.][addon-badge]][addon]

1. Click the "Install" button to install the add-on.
1. Create a free account at [zerotier.com][zerotier] and get a network ID.
1. Set the "network_id" add-on option with your network ID.
1. Start the "ZeroTier One" add-on
1. Check the logs of the "ZeroTier One" add-on to see if everything went well.
1. The instance will show up in your ZeroTier account.

## 配置

**注意**: _Remember to restart the add-on when the configuration is changed._

Example add-on configuration:

```yaml
networks:
  - wgfyiwe73747457
  - fhu3888892jjfdk
api_auth_token: ""
```

**注意**: _This is just an example, don't copy and paste it! Create your own!_

### 选项: `log_level`

The `log_level` option controls the level of log output by the addon and can
be changed to be more or less verbose, which might be useful when you are
dealing with an unknown issue. Possible values are:

- `trace`: Show every detail, like all called internal functions.
- `debug`: Shows detailed debug information.
- `info`: Normal (usually) interesting events.
- `warning`: Exceptional occurrences that are not errors.
- `error`: Runtime errors that do not require immediate action.
- `fatal`: Something went terribly wrong. Add-on becomes unusable.

Please note that each level automatically includes log messages from a
more severe level, e.g., `debug` also shows `info` messages. By default,
the `log_level` is set to `info`, which is the recommended setting unless
you are troubleshooting.

### 选项: `networks`

Configures one or more network identifiers of the networks (VLAN) to join.
You can find this number in your ZeroTier account.

**注意**: _This option support secrets, e.g., `!secret zerotier_network_id`._

### 选项: `api_auth_token`

ZeroTier exposes a local HTTP JSON API, which uses the port set using the
`port` option above. It allows tools and programs to access this ZeroTier
instance for quering data (or control it).

This token is like a password for accessing that API, you can leave this
option empty if you are not planning on using this feature.

For more information on the ZeroTier JSON API, [check their documentation][api].

**注意**: _This option support secrets, e.g., `!secret zerotier_token`._

## 更改日志 & 发布

This repository keeps a change log using [GitHub's releases][releases]
functionality.

Releases are based on [Semantic Versioning][semver], and use the format
of `MAJOR.MINOR.PATCH`. In a nutshell, the version will be incremented
based on the following:

- `MAJOR`: Incompatible or major changes.
- `MINOR`: Backwards-compatible new features and enhancements.
- `PATCH`: Backwards-compatible bugfixes and package updates.

## 支持

Got questions?

You have several options to get them answered:

- The [Home Assistant Community Add-ons Discord chat server][discord] for add-on
  support and feature requests.
- The [Home Assistant Discord chat server][discord-ha] for general Home
  Assistant discussions and questions.
- The Home Assistant [Community Forum][forum].
- Join the [Reddit subreddit][reddit] in [/r/homeassistant][reddit]

You could also [open an issue here][issue] GitHub.

## 作者 & 贡献者

The original setup of this repository is by [Franck Nijhof][frenck].

For a full list of all authors and contributors,
check [the contributor's page][contributors].

## 许可证

MIT 许可证

版权所有 (c) 2019-2025 Franck Nijhof

特此免费授予任何获得此软件及其相关文档文件（“软件”）副本的人，
在不限制的情况下处理软件的权利，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权利，
并允许获得软件的人这样做，但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件按“原样”提供，不提供任何形式的保证，包括但不限于对适销性、特定用途适用性和非侵权性的保证。
在任何情况下，作者或版权持有人均不对任何索赔、损害赔偿或其他责任承担责任，
无论是由合同、侵权或其他行为引起的，也不论是由软件或软件的使用或其他交易引起的。

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