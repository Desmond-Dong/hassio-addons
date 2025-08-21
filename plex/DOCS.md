# Home Assistant Community Add-on: Plex Media Server

Plex add-on 将您喜爱的媒体集中在一个地方，使其变得美观且易于享受。此插件提供的 Plex Media Server 整理您的个人视频、音乐和照片收藏，并将它们流式传输到所有您的设备。

## 安装

此插件的安装非常直接，与其他 Home Assistant 插件安装方式相同。

1. 点击下面的 Home Assistant 我的按钮，在您的 Home Assistant 实例中打开插件。

   ![在您的 Home Assistant 实例中打开此插件][addon-badge]][addon]

1. 点击“安装”按钮以安装插件。
1. 访问 <https://www.plex.tv/claim> 并获取您的声明令牌。
1. 使用上一步中获得的声明代码更新插件配置。
1. 保存插件配置。
1. 启动“Plex Media Server”插件。
1. 检查“Plex Media Server”的日志，查看是否一切顺利。
1. 登录 Plex 管理界面并完成设置过程。

**注意**：添加媒体位置时，请使用 `/share` 和 `/media` 作为基本目录。

## 配置

**注意**：更改配置时，请记住重启插件。

示例插件配置：

```yaml
log_level: info
claim_code: claim-cAMrqFrenckFU4x445Tn
```

**注意**：这只是一个示例，请不要复制粘贴！创建您自己的！

### 选项：`log_level`

`log_level` 选项控制插件输出的日志级别，可以更改为更详细或更简洁，这在处理未知问题时可能很有用。可能的值有：

- `trace`：显示所有细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：非错误的异常情况。
- `error`：不需要立即处理的运行时错误。
- `fatal`：发生了严重错误。插件变得无法使用。

请注意，每个级别自动包含更严重级别的日志消息，例如，`debug` 也显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐设置，除非您正在排错。

### 选项：`claim_code`

为了允许您的服务器登录到您的 Plex 账户，它需要一个所谓的“声明代码”。登录 Plex 允许 Plex 定位并连接到您的服务器，并解锁各种功能。

要获取您的代码，请访问 <https://www.plex.tv/claim>。

此代码仅由插件使用一次。一旦服务器成功通过 Plex 身份验证，此代码即可移除。

## 解决与 Plex 的连接问题

Plex 非常简单，设置也很容易。大多数设置会自动检测。尽管如此，它无法识别您家庭网络上的 IP 地址。这可能导致与某些 Plex 应用的连接问题，例如三星 Tizen Plex 应用。

这不是 Plex 的错误，而是因为它运行在 Docker 生态系统中，而此插件就在其中。幸运的是，Plex 中有一个选项可以帮助解决这个问题，但它有点隐藏。

- 登录 Plex 网络界面。
- 转到设置。
- 点击服务器选项卡。
- 在左侧，选择“网络”。
- 确保您正在查看高级视图。
  右上角有一个“显示高级”按钮。
- 将您的自定义 URL 添加到“自定义服务器访问 URL”字段。

自定义 URL 是 Plex 客户端将尝试连接 Plex 的附加 URL。如果您希望列出多个，请用逗号分隔。

示例：

```txt
http://hassio.local:32400,http://192.168.1.88:32400,http://mydomain.duckdns.org:32400
```

## 已知问题和限制

- 此插件支持基于 ARM 的设备，但它们至少必须是 ARMv7 设备。（不支持 Raspberry Pi 1 和 Zero）。
- 此插件可以在 Raspberry Pi 上运行。虽然它仍然有用，但不要期望太多。一般来说，Pi 缺乏处理能力，可能无法流式传输您的媒体；因此不建议在此类设备上使用此插件。
- 此插件无法为您添加/挂载任何额外的 USB 或其他设备。这是 Home Assistant 的限制。如果您希望使用额外设备，您需要自己修改主机系统，并且不受 Home Assistant 项目或社区插件团队的支持。
- Plex Pass 可以为您提供对通过媒体服务器 Beta 版本通道提供的新功能的独家访问权限。目前，运行此“Beta”版本不受此插件支持。
- 此插件不支持通过 DLNA 的 Plex。

## 更改日志和发布

此存储库使用 GitHub 的发布功能[发布]功能维护更改日志。

发布基于[语义版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 格式。简而言之，版本将根据以下方式增加：

- `MAJOR`：不兼容或主要更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的补丁和软件包更新。

## 支持

有问题吗？

您有几个选项来获得答案：

- [Home Assistant 社区插件 Discord 服务器][discord]用于插件支持和功能请求。
- [Home Assistant Discord 服务器][discord-ha]用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit]中的 [/r/homeassistant][reddit]

您也可以在 GitHub 上[打开一个问题][issue]。

## 作者和贡献者

此存储库的原始设置由 [Franck Nijhof][frenck] 完成。

要查看所有作者和贡献者的完整列表，请查看[贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有（c）2018-2025 Franck Nijhof

特此免费授予任何获得此软件及其相关文档文件（“软件”）副本的人，在软件上进行操作的权限，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权利，并允许提供软件的人这样做，但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件按“原样”提供，不提供任何形式的保证，无论是明示的还是暗示的，包括但不限于对适销性、特定用途适用性和非侵权性的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害赔偿或其他责任负责，无论是由合同、侵权或其他行为引起的，均与软件或软件的使用或其他交易无关。

[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[addon]: https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_plex&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository
[contributors]: https://github.com/hassio-addons/addon-plex/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-plex-media-server/54383?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-plex/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-plex/releases
[semver]: https://semver.org/spec/v2.0.0.html