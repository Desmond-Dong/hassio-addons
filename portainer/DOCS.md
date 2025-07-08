# Home Assistant Community Add-on: Portainer

Portainer 是一个开源的轻量级管理 UI，它允许你轻松管理 Docker 主机或 Docker 群集。

管理 Docker 从未如此简单。Portainer 提供了 Docker 的详细概览，并允许你管理容器、镜像、网络和卷。

## 警告 1

Portainer Add-on 非常强大，它几乎可以让你访问整个系统。虽然这个 Add-on 是在精心设计和考虑安全性的情况下创建和维护的，但在错误或不熟悉的情况下，它可能会损坏你的系统。

## 警告 2

Portainer Add-on 的目的是用于调试 Home Assistant 及其容器。它并没有被设计或用于管理或部署你的自定义软件或第三方容器。

**Home Assistant 不支持在 Home Assistant OS 或 Supervised 安装类型上运行第三方容器**。忽视这一点将使你的系统变为不受支持！

## 安装

要安装这个 Add-on，你首先需要进入你的配置文件并开启“高级模式”，完成后返回 Home Assistant Add-ons 并搜索“Portainer”并像安装其他 Add-on 一样安装它。

要使用这个 Add-on，你需要禁用这个 Add-on 的保护模式。没有它，Add-on 无法访问 Docker。

1. 在 Supervisor Add-on 商店中搜索“Portainer”并安装它。
1. 将“保护模式”开关设置为关闭。
1. 启动“Portainer”Add-on。
1. 检查“Portainer”Add-on 的日志，看看是否一切顺利。

## 配置

**注意**：_在配置更改时，请记得重启 Add-on。_

示例 Add-on 配置：

```yaml
log_level: info
agent_secret: password
```

**注意**：_这只是一个示例，不要复制和粘贴它！创建你自己的！_

### 选项：`log_level`

`log_level` 选项控制 Add-on 的日志输出级别，可以更改为更详细或更简洁，这在处理未知问题时可能很有用。可能的值包括：

- `trace`：显示每个细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：非错误的异常情况。
- `error`：不需要立即处理的运行时错误。
- `fatal`：出现了严重问题。Add-on 变得无法使用。

请注意，每个级别会自动包含更严重级别的日志消息，例如，`debug` 也会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非你正在解决问题。

### 选项：`agent_secret`

设置一个共享代理密钥的选项。也必须在远程代理中作为环境变量设置。

## 更改日志与发布

这个仓库使用 [GitHub 的发布][releases] 功能来维护更改日志。

发布基于 [语义版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将根据以下情况增加：

- `MAJOR`：不兼容或主要更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的 Bug 修复和软件包更新。

## 支持

有问题？

你有几个选项来得到答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord] 用于 Add-on 支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

你也可以在 GitHub 上 [打开一个问题][issue]。

## 作者与贡献者

这个仓库的原始设置由 [Franck Nijhof][frenck] 完成。

要查看所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2018-2021 Franck Nijhof

特此免费授予任何获得此软件及其相关文档文件（“软件”）副本的人，在不受限制的情况下处理软件的权利，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权利，并允许提供软件的人这样做，但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分的软件中。

软件按“原样”提供，不提供任何形式的保证，包括但不限于对适销性、特定用途适用性和不侵犯任何权利的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害或其他责任负责，无论是合同行为、侵权行为还是其他行为，均不因软件或使用软件或其他行为而引起的责任。