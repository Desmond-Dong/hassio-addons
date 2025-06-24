# Home Assistant Community Add-on: Portainer

Portainer 是一个开源的轻量级管理用户界面，允许您轻松管理 Docker 主机或 Docker 集群。

管理 Docker 从未如此简单。Portainer 提供了 Docker 的详细概述，并允许您管理容器、镜像、网络和卷。

## 警告 1

Portainer 插件功能强大，几乎可以让您访问整个系统。虽然该插件是在考虑安全性的情况下精心创建和维护的，但在错误或缺乏经验的操作下，它可能会损坏您的系统。

## 警告 2

Portainer 插件旨在用于调试 Home Assistant 及其容器。它并不是为了管理或部署您的自定义软件或第三方容器而设计的。

**Home Assistant 不支持在 Home Assistant OS 或监督安装类型上运行第三方容器。** 忽视这一点将导致您的系统不被支持！

## 安装

要安装此插件，您首先需要进入您的个人资料，并开启“高级模式”。完成后，返回到 Home Assistant 插件，并搜索“Portainer”并像其他插件一样进行安装。

要使用此插件，您需要禁用此插件上的保护模式。没有此模式，该插件无法访问 Docker。

1. 在主管插件商店中搜索“Portainer”插件并安装。
1. 将“保护模式”开关设置为关闭。
1. 启动“Portainer”插件。
1. 检查“Portainer”插件的日志以查看一切是否正常。

## 配置

**注意**：_记得在更改配置后重启插件。_

示例插件配置：

```yaml
log_level: info
agent_secret: password
```

**注意**：_这只是一个示例，不要复制和粘贴！创建您自己的！_

### 选项：`log_level`

`log_level` 选项控制插件的日志输出级别，可以更改为更多或更少的详细信息，这在处理未知问题时可能会很有用。可能的值包括：

- `trace`：显示每个细节，如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：并非错误的异常情况。
- `error`：不需要立即采取行动的运行时错误。
- `fatal`：出现严重问题。插件变得不可用。

请注意，每个级别自动包括来自更严重级别的日志消息，例如，`debug` 还会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您在故障排除。

### 选项：`agent_secret`

设置共享代理秘密的选项。也必须在远程代理中作为环境变量设置。

## 更新日志与版本

此存储库使用 [GitHub 的发行版][releases] 功能维护变更日志。

发行版基于 [语义版本控制][semver]，并使用格式 `MAJOR.MINOR.PATCH`。简而言之，版本将根据以下情况递增：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的错误修复和包更新。

## 支持

有问题吗？

您有几种方式可以得到答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord] 以获取插件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 以进行一般 Home Assistant 讨论和提问。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]。

您也可以在这里 [打开一个问题][issue] GitHub。

## 作者与贡献者

此存储库的最初设置由 [Franck Nijhof][frenck] 完成。

要查看所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2018-2021 Franck Nijhof

特此授予任何获取本软件及相关文档文件（“软件”）副本的人无条件使用本软件的许可，包括但不限于使用、复制、修改、合并、出版、分发、再许可和/或销售本软件副本的权利，以及允许提供本软件的人这样做，遵循以下条件：

上述版权声明和本许可声明应包含在本软件的所有副本或实质性部分中。

本软件按“原样”提供，不附有任何形式的保证，无论是明确的还是隐含的，包括但不限于对适销性、特定用途适用性和不侵权的保证。在任何情况下，作者或版权所有者都不对因使用本软件或涉及本软件的其他交易而引起的任何索赔、损害或其他责任承担责任，无论是在合同、侵权或其他方面。

[contributors]: https://github.com/hassio-addons/addon-portainer/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-portainer/68836?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-portainer/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-portainer/releases
[semver]: http://semver.org/spec/v2.0.0.htm