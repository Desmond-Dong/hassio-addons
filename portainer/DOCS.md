# Home Assistant 社区附加组件：Portainer

Portainer 是一个开源的轻量级管理用户界面，允许您轻松管理 Docker 主机或 Docker swarm 集群。

管理 Docker 从未如此简单。Portainer 提供了 Docker 的详细概述，并允许您管理容器、镜像、网络和卷。

## 警告 1

Portainer 附加组件非常强大，可以让您接触到几乎整个系统。虽然该附加组件是在小心和考虑安全的情况下创建和维护的，但如果在错误或没有经验的手中，可能会损坏您的系统。

## 警告 2

Portainer 附加组件旨在调试 Home Assistant 及其容器。它并不用于管理或部署您的自定义软件或第三方容器。

**Home Assistant 不支持在 Home Assistant 操作系统或受监控安装类型上运行第三方容器**。忽略此点将使您的系统处于不受支持的状态！

## 安装

要安装此附加组件，您首先需要进入您的个人资料并打开“高级模式”，完成后返回到 Home Assistant 附加组件并搜索“Portainer”并像安装其他任何附加组件一样进行安装。

要能够使用此附加组件，您需要在此附加组件上禁用保护模式。否则，该附加组件无法访问 Docker。

1. 在 Supervisor 附加组件商店中搜索“Portainer”附加组件并进行安装。
1. 将“保护模式”开关设置为关闭。
1. 启动“Portainer”附加组件。
1. 检查“Portainer”附加组件的日志以查看是否一切正常。

## 配置

**注意**：_记得在配置更改时重启附加组件。_

附加组件配置示例：

```yaml
log_level: info
agent_secret: password
```

**注意**：_这只是一个示例，请不要复制粘贴！创建您自己的！_

### 选项：`log_level`

`log_level` 选项控制附加组件的日志输出级别，可以更改为更详细或更少详细，这在处理未知问题时可能会有所帮助。可能的值如下：

- `trace`：显示每个细节，如所有被调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：非错误的特殊情况。
- `error`：无需立即采取行动的运行时错误。
- `fatal`：出了严重的错误。附加组件变得不可用。

请注意，每个级别自动包含来自更严重级别的日志消息，例如，`debug` 也会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这也是推荐的设置，除非您正在进行故障排除。

### 选项：`agent_secret`

设置共享代理秘密的选项。还必须在远程代理中作为环境变量设置。

## 更新日志与发布

该存储库使用 [GitHub 的发布][releases] 功能维护变更日志。

发布基于 [语义化版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将根据以下内容进行递增：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的错误修复和包更新。

## 支持

有问题吗？

您有几种选择可以获得答案：

- [Home Assistant 社区附加组件 Discord 聊天服务器][discord] 获取附加组件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 进行一般的 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 在 [/r/homeassistant][reddit] 加入 [Reddit 子论坛][reddit]。

您还可以在 [这里打开一个问题][issue] GitHub。

## 作者与贡献者

该存储库的原始设置由 [Franck Nijhof][frenck] 完成。

要查看所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2018-2021 Franck Nijhof

特此授予任何获得本软件及其相关文档文件（“软件”）副本的人免费许可，以无限制地处理软件，包括但不限于使用、复制、修改、合并、出版、分发、再许可和/或出售软件副本的权利，以及允许向其提供软件的人进行上述操作，须遵守以下条件：

上述版权声明和本许可通知应包含在软件的所有副本或重要部分中。

本软件按“原样”提供，不含任何类型的明示或暗示担保，包括但不限于对适销性、特定用途的适用性和非侵权的担保。在任何情况下，作者或版权持有者对因使用本软件或其他交易而引起的任何索赔、损害或其他责任，不论是合同行为、侵权行为或其他方式，均不承担任何责任。

[contributors]: https://github.com/hassio-addons/addon-portainer/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-portainer/68836?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-portainer/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-portainer/releases
[semver]: http://semver.org/spec/v2.0.0.htm