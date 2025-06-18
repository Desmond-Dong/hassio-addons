# Home Assistant社区插件: Portainer

Portainer是一个开源的轻量级管理用户界面，允许您轻松管理Docker主机或Docker集群。

管理Docker从未如此简单。Portainer提供了Docker的详细概述，并允许您管理容器、镜像、网络和卷。

## 警告 1

Portainer插件功能强大，几乎可以访问您的整个系统。虽然此插件经过细心创建和维护，并考虑了安全性，但在错误或缺乏经验的手中，可能会损害您的系统。

## 警告 2

Portainer插件旨在调试Home Assistant及其容器。它并非用于管理或部署您的自定义软件或第三方容器。

**Home Assistant 不支持在 Home Assistant OS 或监控安装类型上运行第三方容器**。忽略这一点，将使您的系统变得不受支持！

## 安装

要安装此插件，您首先需要转到您的个人资料并启用“高级模式”，完成后返回Home Assistant插件页面搜索“Portainer”并像安装其他插件一样安装它。

要能够使用此插件，您需要禁用此插件的保护模式。没有它，插件将无法访问Docker。

1. 在Supervisor插件商店中搜索“Portainer”插件并安装它。
1. 将“保护模式”开关设置为关闭。
1. 启动“Portainer”插件。
1. 检查“Portainer”插件的日志以查看一切是否正常。

## 配置

**注意**：_更改配置时请记得重启插件。_

示例插件配置：

```yaml
log_level: info
agent_secret: password
```

**注意**：_这只是一个示例，别复制粘贴！创建你自己的！_

### 选项：`log_level`

`log_level`选项控制插件的日志输出级别，并可以更改为更详细或更少详细，在处理未知问题时可能很有用。可能的值为：

- `trace`: 显示每一个细节，如所有被调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 正常（通常）有趣的事件。
- `warning`: 非错误的异常情况。
- `error`: 不需要立即行动的运行时错误。
- `fatal`: 出现了严重错误。插件变得不可用。

请注意，每个级别自动包含来自更严重级别的日志消息，例如，`debug`也会显示`info`消息。默认情况下，`log_level`设置为`info`，这是推荐的设置，除非您正在进行故障排除。

### 选项：`agent_secret`

一个设置共享代理密钥的选项。也必须在远程代理中设置为环境变量。

## 更新日志与发布

该存储库使用[GitHub的发布][releases]功能保留变更日志。

发布基于[语义版本控制][semver]，并使用`MAJOR.MINOR.PATCH`的格式。简而言之，版本将基于以下内容递增：

- `MAJOR`: 不兼容或重大变化。
- `MINOR`: 向后兼容的新功能和增强。
- `PATCH`: 向后兼容的错误修复和包更新。

## 支持

有问题吗？

您有几种方式可以获得答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord] 用于插件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 用于一般的Home Assistant讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit子论坛][reddit] 在[/r/homeassistant][reddit]

您也可以在这里[报告问题][issue] GitHub。

## 作者与贡献者

该存储库的最初设置由 [Franck Nijhof][frenck]完成。

有关所有作者和贡献者的完整列表，请查看[贡献者页面][contributors]。

## 许可证

MIT许可证

版权所有(c) 2018-2021 Franck Nijhof

特此授予任何获得该软件及相关文档文件（“软件”）副本的个人免费授权，可以在不受限制的情况下处理该软件，包括但不限于使用、复制、修改、合并、出版、分发、再许可和/或销售该软件的副本，并允许向软件提供的人员这样做，受以下条件的限制：

上述版权声明和本许可声明应包括在所有软件的副本或实质部分中。

软件按“原样”提供，不提供任何类型的担保，明确或隐含，包括但不限于对适销性、特定用途适用性和非侵权的担保。在任何情况下，作者或版权持有人对此软件或其使用或其他交易所产生的任何索赔、损害或其他责任均不承担责任，无论是在合同、侵权或其他方面。

[contributors]: https://github.com/hassio-addons/addon-portainer/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-portainer/68836?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-portainer/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-portainer/releases
[semver]: http://semver.org/spec/v2.0.0.htm