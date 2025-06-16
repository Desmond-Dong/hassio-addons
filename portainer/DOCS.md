# Home Assistant 社区附加组件：Portainer

Portainer 是一个开源的轻量级管理 UI，允许您轻松管理 Docker 主机或 Docker swarm 集群。

管理 Docker 从未如此简单。Portainer 提供了 Docker 的详细概述，并允许您管理容器、镜像、网络和卷。

## 警告 1

Portainer 附加组件功能强大，几乎可以访问您的整个系统。虽然这个附加组件是在认真考虑安全性并进行维护的情况下创建的，但在错误或缺乏经验的用户手中，它可能会损坏您的系统。

## 警告 2

Portainer 附加组件旨在调试 Home Assistant 及其容器。它不是用于管理或部署您的自定义软件或第三方容器的。

**Home Assistant 不支持在 Home Assistant 操作系统或受监督安装类型上运行第三方容器**。忽视这一点，将使您的系统被视为不受支持！

## 安装

要安装此附加组件，您首先需要前往您的个人资料并开启“高级模式”，完成后返回 Home Assistant 附加组件，搜索“Portainer”并按通常安装其他附加组件的方式进行安装。

要能够使用此附加组件，您需要禁用该附加组件的保护模式。没有它，附加组件无法访问 Docker。

1. 在 Supervisor 附加组件商店中搜索“Portainer”并安装。
1. 将“保护模式”开关设置为关闭。
1. 启动“Portainer”附加组件。
1. 检查“Portainer”附加组件的日志，以查看一切是否顺利。

## 配置

**注意**：_修改配置后，请记得重启附加组件。_

示例附加组件配置：

```yaml
log_level: info
agent_secret: password
```

**注意**：_这只是示例，请不要复制粘贴！自己创建！_

### 选项：`log_level`

`log_level` 选项控制附加组件的日志输出级别，可以更改为更少或更多详细，当您处理未知问题时，这可能会非常有用。可能的值包括：

- `trace`：显示每个细节，比如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：不算错误的异常情况。
- `error`：不需要立即处理的运行时错误。
- `fatal`：出现了严重错误，附加组件变得无法使用。

请注意，各个级别自动包括更高级别的日志消息，例如，`debug` 也显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您在故障排除。

### 选项：`agent_secret`

一个选项，用于设置共享的代理密钥。也必须在远程代理中作为环境变量设置。

## 更新日志与版本发布

这个存储库使用 [GitHub 的发布][releases] 功能维护更新日志。

版本发布基于 [语义版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将根据以下规则增加：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新特性和增强。
- `PATCH`：向后兼容的错误修复和包更新。

## 支持

有问题吗？

您有几种选项来获得答案：

- [Home Assistant 社区附加组件 Discord 聊天服务器][discord]，用于附加组件支持和特性请求。
- [Home Assistant Discord 聊天服务器][discord-ha]，用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [/r/homeassistant][reddit] 的 [Reddit 子论坛][reddit]。

您也可以在此 [打开一个问题][issue] 在 GitHub 上。

## 作者与贡献者

该存储库的最初设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2018-2021 Franck Nijhof

授予任何获得本软件及相关文档文件（“软件”）副本的人，免费、无条件地处理软件，包括但不限于使用、复制、修改、合并、出版、分发、再授权和/或出售软件的副本，及允许向其提供软件的人这样做，但须遵守以下条件：

上述版权声明和此许可声明应包括在所有副本或软件的实质部分中。

软件按“原样”提供，不提供任何类型的担保，明示或暗示，包括但不限于对适销性、特定用途适用性和非侵权的担保。在任何情况下，作者或版权持有人均不对因使用软件或其他交易而产生的任何索赔、损害或其他责任负责，无论是在合同诉讼、侵权或其他情况中产生的。

[contributors]: https://github.com/hassio-addons/addon-portainer/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-portainer/68836?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-portainer/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-portainer/releases
[semver]: http://semver.org/spec/v2.0.0.htm