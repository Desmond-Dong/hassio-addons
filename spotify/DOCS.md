# Home Assistant Community Add-on: Spotify Connect

Home Assistant Spotify Connect插件允许您使用运行Home Assistant的设备来播放您的Spotify音乐。此插件使用Spotify Connect协议，使其成为一个可以被所有官方客户端控制的设备。

例如；在Raspberry Pi上运行Home Assistant并安装此插件，将允许您在Pi上播放您的Spotify音乐。因此，您只需将您的音响系统连接到Pi并开始播放！

## 安装

此插件的安装非常直接，与安装任何其他Home Assistant插件没有区别。

1. 点击下面的Home Assistant My按钮以在您的Home Assistant实例中打开插件。

   [![在您的Home Assistant实例中打开此插件][ addon-badge]][ addon]

1. 点击“安装”按钮以安装插件。
1. 选择您的音频输出设备，并在该设备上点击“保存”。
1. 启动“Spotify Connect”插件。
1. 检查“Spotify Connect”的日志，以查看一切是否正常。
1. 准备就绪！

## 配置

**注意**：_更改配置时请记住重启插件。_

示例插件配置：

```yaml
log_level: info
name: HomeAssistant
bitrate: 320
initial_volume: 50
username: frenck@example.com
password: MySpotifyPassword
autoplay: true
```

**注意**：_这只是个示例，不要复制粘贴！创建您自己的！_

### 选项：`log_level`

`log_level`选项控制插件的日志输出级别，可以更改为更详细或更简洁，这在您遇到未知问题时可能很有用。可能的值有：

- `trace`：显示所有细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：非错误的异常情况。
- `error`：不需要立即处理的运行时错误。
- `fatal`：发生了严重错误。插件变得无法使用。

请注意，每个级别自动包含更严重级别的日志消息，例如，`debug`也会显示`info`消息。默认情况下，`log_level`设置为`info`，这是推荐设置，除非您正在调试。

将`log_level`设置为`debug`也会在Spotify服务中开启调试模式。

### 选项：`name`

您的设备名称（Spotify Connect目标），在官方Spotify客户端中显示。

### 选项：`bitrate`

Spotify应使用的比特率。越高，音质越好，但插件消耗的数据也越多。

有效值：`96`，`160`（默认）或`320`。

### 选项：`initial_volume`

初始音量，范围从0-100%。此设置在插件启动或从崩溃中恢复时生效。

initial_volume: 50 # 可选

### 选项：`username`

**重要**：_这需要Spotify高级账户！_

您用于登录Spotify高级账户的用户名。设置此选项将使插件专门绑定到您的账户。

当您在网络中发现问题时，这会很有帮助，或者可以禁止网络上的访客使用此插件。

### 选项：`password`

您用于登录Spotify高级账户的密码。

### 选项：`autoplay`

当播放队列结束时，Spotify是否应自动播放相似的歌曲。

## 已知问题和限制

- 此插件需要Spotify高级账户。

## 更改日志与发布

此存储库使用GitHub的发布功能[发布日志]。

发布基于[语义版本控制]，并使用`MAJOR.MINOR.PATCH`格式。简而言之，版本将根据以下内容增加：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的补丁和软件包更新。

## 支持

有问题？

您有几个选项可以回答这些问题：

- Home Assistant Community Add-ons Discord聊天服务器[discord]用于插件支持和功能请求。
- Home Assistant Discord聊天服务器[discord-ha]用于一般Home Assistant讨论和问题。
- Home Assistant社区论坛[forum]。
- 加入Reddit的[Reddit子版块][reddit]在[/r/homeassistant][reddit]

您还可以在GitHub上[打开一个问题][issue]。

## 作者与贡献者

此存储库的原始设置由[Franck Nijhof][frenck]完成。

要查看所有作者和贡献者的完整列表，请查看[贡献者页面][contributors]。

## 许可证

MIT许可证

版权所有（c）2018-2025 Franck Nijhof

特此免费授予任何人获取此软件及其相关文档文件（“软件”）副本的权限，可在软件中自由处理，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权限，并允许提供软件的人这样做，但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件按“原样”提供，不提供任何明示或暗示的保证，包括但不限于对适销性、特定用途适用性和非侵权性的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害或其他责任负责，无论是因合同、侵权或其他行为引起的，均与软件的使用或其他交易有关。

[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[addon]: https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_spotify&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository
[contributors]: https://github.com/hassio-addons/addon-spotify-connect/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-spotify-connect/61210?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-spotify-connect/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-spotify-connect/releases
[semver]: http://semver.org/spec/v2.0.0.htm