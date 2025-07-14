# Home Assistant Community Add-on: Portainer

Portainer 是一个开源的轻量级管理界面，它允许你轻松管理 Docker 主机或 Docker 群集。

管理 Docker 从未如此简单。Portainer 提供了 Docker 的详细概览，并允许你管理容器、镜像、网络和卷。

## 警告 1

Portainer 扩展程序功能非常强大，并赋予你访问整个系统的权限。虽然这个扩展程序是在精心制作并以安全为考虑而创建和维护的，但在错误或不熟悉的情况下，它可能会损坏你的系统。

## 警告 2

Portainer 扩展程序用于调试 Home Assistant 及其容器。它并没有被设计或用于管理或部署你的自定义软件或第三方容器。

**Home Assistant 不支持在 Home Assistant OS 或 Supervised 安装类型上运行第三方容器**。忽视这一点将使你的系统变为不支持状态！

## 安装

要安装此扩展程序，你首先需要进入你的配置文件并开启“高级模式”，完成后返回 Home Assistant 扩展程序并搜索“Portainer”并像安装其他扩展程序一样安装它。

要使用此扩展程序，你需要禁用此扩展程序的“保护模式”。没有它，扩展程序无法访问 Docker。

1. 在 Supervisor 扩展程序商店中搜索“Portainer”并安装它。
1. 将“保护模式”开关设置为关闭。
1. 启动“Portainer”扩展程序。
1. 检查“Portainer”扩展程序的日志，以查看是否一切顺利。

## 配置

**注意**：_在更改配置时，请记住重启扩展程序。_

示例扩展程序配置：

```yaml
log_level: info
agent_secret: password
```

**注意**：_这只是一个示例，不要复制粘贴它！创建你自己的！_

### 选项：`log_level`

`log_level` 选项控制扩展程序的日志输出级别，可以更改为更详细或不详细，这在处理未知问题时可能很有用。可能的值有：

- `trace`：显示每个细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：非错误的异常情况。
- `error`：不需要立即处理的运行时错误。
- `fatal`：发生了严重错误。扩展程序变得无法使用。

请注意，每个级别会自动包含更严重级别的日志消息，例如，`debug` 也会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐设置，除非你在进行故障排除。

### 选项：`agent_secret`

设置共享代理密钥的选项。也必须在远程代理中作为环境变量设置。

## 更改日志与发布

此存储库使用 [GitHub 的发布][releases] 功能维护更改日志。

发布基于 [语义版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 格式。简而言之，版本将根据以下内容进行递增：

- `MAJOR`：不兼容或主要更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的补丁和软件包更新。

## 支持

有问题吗？

你有几个选项可以回答这些问题：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord] 用于扩展程序支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

你也可以在 GitHub 上 [打开一个问题][issue]。

## 作者与贡献者

此存储库的原始设置由 [Franck Nijhof][frenck] 提供。

要查看所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2018-2021 Franck Nijhof

特此授予任何获得本软件及其相关文档文件（“软件”）副本的人，在不限制的情况下自由处理软件的权利，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权利，并允许提供软件的人这样做，但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分的软件中。

软件按“原样”提供，不提供任何明示或暗示的保证，包括但不限于对适销性、特定用途适用性和不侵犯版权的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害或其他责任承担责任，无论这些责任是由于合同、侵权或其他行为引起的，也不论这些责任是由于软件或软件的使用或其他交易引起的。

[contributors]: https://github.com/hassio-addons/addon-portainer/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-portainer/68836?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-portainer/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-portainer/releases
[semver]: http://semver.org/spec/v2.0.0.htm