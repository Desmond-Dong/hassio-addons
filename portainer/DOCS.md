# Home Assistant Community Add-on: Portainer

Portainer 是一个开源轻量级管理界面，使您能够轻松管理一个或多个 Docker 主机或 Docker 集群。

管理 Docker 从未如此简单。Portainer 提供了 Docker 的详细概述，并允许您管理容器、镜像、网络和卷。

## 警告 1

Portainer 附加组件非常强大，可以访问您几乎整个系统。虽然此附加组件是在注意安全的情况下小心创建和维护的，但在错误或缺乏经验的手中，它可能会损坏您的系统。

## 警告 2

Portainer 附加组件旨在调试 Home Assistant 及其容器。它并不用于管理或部署您自定义的软件或第三方容器。

**Home Assistant 不支持在 Home Assistant OS 或监督安装类型上运行第三方容器**。忽略这一点将使您的系统不受支持！

## 安装

要安装此附加组件，您首先需要转到您的个人资料并启用“高级模式”，完成后返回 Home Assistant 附加组件并搜索“Portainer”，并像安装其他任何附加组件一样安装它。

要能够使用此附加组件，您需要在此附加组件上禁用保护模式。没有它，附加组件无法访问 Docker。

1. 在 Supervisor 附加组件商店中搜索“Portainer” 并安装它。
2. 将“保护模式”开关设置为关闭。
3. 启动“Portainer”附加组件。
4. 检查“Portainer”附加组件的日志，以查看一切是否正常。

## 配置

**注意**：_记得在更改配置时重启附加组件。_

附加组件配置示例：

```yaml
log_level: info
agent_secret: password
```

**注意**：_这只是示例，请勿直接复制粘贴！创建您自己的！_

### 选项：`log_level`

`log_level` 选项控制附加组件的日志输出级别，可以更改为更详细或更少详细，这在您处理未知问题时可能会很有用。可能的值有：

- `trace`：显示每个细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：异常情况，不是错误。
- `error`：运行时错误，不需要立即采取行动。
- `fatal`：发生了严重错误。附加组件变得不可用。

请注意，每个级别自动包含从更严重级别的日志消息，例如，`debug` 还会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您在排除故障。

### 选项：`agent_secret`

一个设置共享代理密钥的选项。也必须在远程代理中设置为环境变量。

## 更新日志与版本

该存储库使用 [GitHub 的版本][releases] 功能维护变更日志。

版本基于 [语义版本控制][semver]，使用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将根据以下内容进行递增：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的 bug 修复和包更新。

## 支持

有问题吗？

您有几种选择可以获得答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord] 以获取附加组件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 进行一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 社区][reddit] 在 [/r/homeassistant][reddit]

您还可以在这里 [提交问题][issue] 在 GitHub 上。

## 作者与贡献者

该存储库的最初设置由 [Franck Nijhof][frenck] 完成。

要查看所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2018-2021 Franck Nijhof

特此免费授予任何获得本软件及相关文档文件（“软件”）副本的人无限制地处理软件，包括但不限于使用、复制、修改、合并、发布、分发、再授权和/或销售软件副本的权利，并允许向其提供软件的人这样做，前提是以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

该软件是“按原样”提供的，没有任何明示或暗示的担保，包括但不限于对适销性、特定用途的适用性和非侵权的担保。在任何情况下，作者或版权持有者均不对因使用或其他在软件或其交易中发生的任何索赔、损害或其他责任负责，无论是在合同、侵权或其他方面。

[contributors]: https://github.com/hassio-addons/addon-portainer/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-portainer/68836?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-portainer/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-portainer/releases
[semver]: http://semver.org/spec/v2.0.0.htm