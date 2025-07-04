# Home Assistant Community Add-on: Example

这是一个 Home Assistant 的示例插件。启动后，它每 5 秒显示一条随机引言。

它展示了多个功能和结构，例如：

- 完整的 GitHub 仓库。
- 通用 Dockerfile 结构和设置。
- 使用 `config.yaml` 和 `build.yaml` 文件。
- 通用 Shell 脚本结构（`run.sh`）。
- 使用 CodeClimate 进行质量保证。
- 使用 GitLab 进行持续集成和部署。
- 使用社区 Home Assistant 插件构建环境。
- 在基础镜像中少量使用 Bash 函数库。
- 使用 Docker 标签方案。

## 安装

这个插件的安装非常直接，与安装任何其他 Home Assistant 插件没有区别。

1. 点击下面的 Home Assistant 我的按钮，在您的 Home Assistant 实例中打开插件。

   ![在您的 Home Assistant 实例中打开此插件][addon-badge]][addon]

1. 点击“安装”按钮来安装插件。
1. 启动“示例”插件。
1. 检查“示例”插件的日志，查看它在运行中的表现。

## 配置

尽管这个插件只是一个示例插件，但它确实提供了一些配置选项供您尝试。

**注意**：_当配置更改时，请记住重启插件。_

示例插件配置：

```yaml
log_level: info
seconds_between_quotes: 5
```

### 选项：`log_level`

`log_level` 选项控制插件的日志输出级别，可以更改为更详细或更简洁，这在处理未知问题时可能很有用。可能的值有：

- `trace`：显示所有细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：常规（通常）有趣的事件。
- `warning`：异常情况，但不是错误。
- `error`：运行时错误，不需要立即采取行动。
- `fatal`：发生了严重错误。插件变得无法使用。

请注意，每个级别自动包含更严重级别的日志消息，例如，`debug` 也显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐设置，除非您正在解决问题。

### 选项：`seconds_between_quotes`

设置输出每条引言之间的秒数。该值必须在 `1` 到 `120` 秒之间。默认情况下，该值设置为 `5` 秒。

## 更改日志与发布

此仓库使用 [GitHub 的发布][releases] 功能维护变更日志。

发布基于 [语义版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 格式。简而言之，版本将根据以下内容增加：

- `MAJOR`：不兼容或主要更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的补丁和包更新。

## 支持

有问题吗？

您有几个选项来获得答案：

- [Home Assistant 社区插件 Discord 服务器][discord] 用于插件支持和功能请求。
- [Home Assistant Discord 服务器][discord-ha] 用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

您也可以在 GitHub 上 [打开一个问题][issue]。

## 作者与贡献者

此仓库的原始设置由 [Franck Nijhof][frenck] 完成。

要查看所有作者和贡献者的完整列表，
请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有（c）2017-2025 Franck Nijhof

特此授予任何获得此软件和关联文档文件（“软件”）副本的人，在不限制的情况下自由处理软件的权利，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权利，并允许提供软件的人这样做，但需遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件按“原样”提供，不提供任何形式的保证，无论是明示的还是暗示的，包括但不限于适销性、特定用途适用性和不侵犯版权的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害或其他责任负责，无论是合同行为、侵权行为或其他行为，均源于、来自或与软件的使用或其他交易有关。