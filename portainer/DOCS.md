# Home Assistant 社区附加组件：Portainer

Portainer 是一个开源的轻量级管理 UI，允许您轻松管理 Docker 主机或 Docker 集群。

管理 Docker 从未如此简单。Portainer 提供了详尽的 Docker 概述，并允许您管理容器、镜像、网络和卷。

## 警告 1

Portainer 附加组件非常强大，可以访问您几乎所有的系统。虽然这个附加组件是在小心和安全考虑下创建和维护的，但在错误或经验不足的手中，可能会损坏您的系统。

## 警告 2

Portainer 附加组件用于调试 Home Assistant 及其容器。它并不是为了管理或部署您的自定义软件或第三方容器而设计的。

**Home Assistant 不支持在 Home Assistant OS 或受监督安装类型上运行第三方容器。** 忽视这一点，您的系统将会被视为不受支持！

## 安装

要安装此附加组件，您首先需要转到您的个人资料并打开“高级模式”，完成后返回 Home Assistant 附加组件并搜索“Portainer”并像安装其他附加组件一样安装它。

要能够使用此附加组件，您需要在此附加组件上禁用保护模式。没有它，附加组件无法访问 Docker。

1. 在 Supervisor 附加组件商店中搜索“Portainer”附加组件并安装它。
2. 将“保护模式”开关设置为关闭。
3. 启动“Portainer”附加组件。
4. 检查“Portainer”附加组件的日志，查看一切是否顺利。

## 配置

**注意**：_记得在更改配置时重启附加组件。_

示例附加组件配置：

```yaml
log_level: info
agent_secret: password
```

**注意**：_这只是一个示例，请不要复制粘贴！自己创建！_

### 选项：`log_level`

`log_level` 选项控制附加组件的日志输出级别，可以更改为更详细或更简洁，这在您处理未知问题时可能很有用。可能的值有：

- `trace`：显示每个细节，如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：非错误的异常情况。
- `error`：不需要立即采取行动的运行时错误。
- `fatal`：发生了严重错误。附加组件变得不可用。

请注意，每个级别自动包括来自更严重级别的日志消息，例如，`debug` 还会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您在故障排除。

### 选项：`agent_secret`

设置共享代理密钥的选项。必须在远程代理中作为环境变量设置。

## 更新记录和发布

该存储库使用 [GitHub 的发布][releases] 功能保持变更日志。

版本基于 [语义版本控制][semver]，使用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将根据以下内容进行递增：

- `MAJOR`：不兼容或重大变化。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的错误修复和软件包更新。

## 支持

有问题吗？

您有几种选择来获得答案：

- [Home Assistant 社区附加组件 Discord 聊天服务器][discord] 以获取附加组件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 以进行一般 Home Assistant 讨论和提问。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]。

您还可以 [在这里打开问题][issue] GitHub。

## 作者及贡献者

该存储库的原始设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整名单，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2018-2021 Franck Nijhof

特此免费授予任何获得本软件及相关文档文件（“软件”）的人员，无限制地处理该软件，包括但不限于使用、复制、修改、合并、出版、分发、再授权和/或出售该软件的副本，并允许提供该软件的人员这样做，前提是满足以下条件：

上述版权声明和本许可声明应包含在所有软件的副本或实质性部分中。

软件是按“原样”提供的，不保证其任何种类的质量，无论是明示还是暗示，包括但不限于对适销性、特定用途的适用性与不侵权的保证。在任何情况下，作者或版权持有者均不对因使用软件或与软件或其他交易相关的任何索赔、损害或其他责任负责，无论是合同、侵权或其他行为。

[contributors]: https://github.com/hassio-addons/addon-portainer/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-portainer/68836?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-portainer/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-portainer/releases
[semver]: http://semver.org/spec/v2.0.0.htm