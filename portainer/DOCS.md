# Home Assistant Community Add-on: Portainer

Portainer 是一个开源的轻量级管理用户界面，可以让您轻松管理 Docker 主机或 Docker 集群。

管理 Docker 从未如此简单。Portainer 提供了 Docker 的详细概述，并允许您管理容器、镜像、网络和卷。

## 警告 1

Portainer 插件非常强大，可以让您访问几乎整个系统。尽管该插件是在安全考虑下精心创建和维护的，但在错误的或缺乏经验的操作者手中，可能会损坏您的系统。

## 警告 2

Portainer 插件旨在调试 Home Assistant 及其容器。它并非用于管理或部署您的自定义软件或第三方容器。

**Home Assistant 不支持在 Home Assistant OS 或监督安装类型上运行第三方容器**。无视这一点，将使您的系统变得不受支持！

## 安装

要安装此插件，您首先需要进入您的个人资料并开启“高级模式”，完成后返回 Home Assistant 的插件页面，搜索“Portainer”并像安装其他插件一样安装它。

要使用此插件，您需要禁用此插件上的保护模式。如果不这样做，插件将无法访问 Docker。

1. 在 Supervisor 插件商店中搜索“Portainer”插件并安装它。
2. 将“保护模式”开关设置为关闭。
3. 启动“Portainer”插件。
4. 检查“Portainer”插件的日志，看一切是否正常。

## 配置

**注意**：_请记住在更改配置时重启插件。_

示例插件配置：

```yaml
log_level: info
agent_secret: password
```

**注意**：_这只是一个示例，请不要直接复制粘贴！创建您自己的！_

### 选项： `log_level`

`log_level` 选项控制插件的日志输出级别，可以根据需要更改为更详细或更简略，这在处理未知问题时可能很有用。可选值为：

- `trace`：显示每个细节，如所有调用的内部函数。
- `debug`：显示详细调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：非错误的异常事件。
- `error`：运行时错误，不需要立即采取行动。
- `fatal`：出现严重错误，插件变得不可用。

请注意，每个级别自动包含更严重级别的日志消息，例如，`debug` 也会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这通常是推荐的设置，除非您正在进行故障排除。

### 选项： `agent_secret`

设置共享代理密钥的选项。必须在远程代理中作为环境变量进行设置。

## 更新日志与版本

此存储库使用 [GitHub 的发布][releases] 功能维护变更日志。

发布基于 [语义版本控制][semver]，使用 `MAJOR.MINOR.PATCH` 格式。简而言之，版本将基于以下内容进行增量：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新特性和增强。
- `PATCH`：向后兼容的错误修复和软件包更新。

## 支持

有问题？

您可以通过以下几种方式获取答案：

- Home Assistant 社区插件 Discord 聊天服务器 [discord] 以获取插件支持和功能请求。
- Home Assistant Discord 聊天服务器 [discord-ha] 以进行一般的 Home Assistant 讨论和提问。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]。

您也可以 [在这里打开一个问题][issue] GitHub。

## 作者与贡献者

此存储库的原始设置由 [Franck Nijhof][frenck] 进行。

要查看所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权 (c) 2018-2021 Franck Nijhof

特此免费授予任何获得本软件及其相关文档文件（“软件”）副本的人，允许在不受限制的情况下处理该软件，包括但不限于使用、复制、修改、合并、出版、分发、再授权和/或出售该软件的副本，并允许向其提供该软件的人这样做，但须遵守以下条件：

上述版权声明和此许可声明应包含在软件的所有副本或实质性部分中。

该软件按“现状”提供，不提供任何种类的明示或暗示的保证，包括但不限于对适销性、特定目的适用性和非侵权的保证。在任何情况下，作者或版权持有者均不对因使用该软件或与该软件相关的其他交易而引起的任何索赔、损害或其他责任承担责任，无论是在合同、侵权或其他方面。

[contributors]: https://github.com/hassio-addons/addon-portainer/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-portainer/68836?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-portainer/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-portainer/releases
[semver]: http://semver.org/spec/v2.0.0.htm