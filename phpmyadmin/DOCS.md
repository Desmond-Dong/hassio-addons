# Home Assistant Community Add-on: phpMyAdmin

phpMyAdmin 是一个用于 MySQL 和 MariaDB 的数据库管理工具。常用操作（管理数据库、表、列、关系、索引、用户、权限等）可以通过用户界面进行，而您仍然可以直接执行任何 SQL 语句。

此插件专门设计用于管理官方 Home Assistant 的 MariaDB 插件。

## 安装

此插件的安装非常简单，与安装任何其他 Home Assistant 插件没有区别。

1. 点击下面的 Home Assistant My 按钮以在您的 Home Assistant 实例中打开此插件。

   [![在您的 Home Assistant 实例中打开此插件。][addon-badge]][addon]

1. 点击“安装”按钮以安装插件。
1. 启动“phpMyAdmin”插件。
1. 尽情享受该插件吧！

## 配置

**注意**：_记得在更改配置时重启插件。_

示例插件配置：

```yaml
log_level: info
```

**注意**：_这只是一个示例，请不要复制粘贴！请创建您自己的配置！_

### 选项：`upload_limit`

默认情况下，上传大小限制（用于导入等操作）设置为 64MB。您可以通过此选项增加此限制，例如，`100` 将是 100MB。

### 选项：`log_level`

`log_level` 选项控制插件的日志输出级别，可以根据需要更改为更详细或更简洁，这在处理未知问题时可能很有用。可能的值包括：

- `trace`：显示每个细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常为）有趣的事件。
- `warning`：不是错误的异常情况。
- `error`：不需要立即采取行动的运行时错误。
- `fatal`：出现严重错误。插件变得无法使用。

请注意，每个级别自动包含更高级别的日志消息，例如，`debug` 也会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是建议的设置，除非您正在进行故障排除。

## 已知问题和限制

- 此插件需要核心 MariaDB 插件版本 2.0 或更高版本。
- 此插件旨在允许管理官方 Home Assistant 的 MariaDB 插件。它无法连接到其他 MySQL 或 MariaDB 服务器。

## 更新日志与发布

此存储库使用 [GitHub 的发布][releases] 功能维护变更日志。

发布基于 [语义版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将基于以下内容递增：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新功能和增强功能。
- `PATCH`：向后兼容的错误修复和包更新。

## 支持

有问题吗？

您有几个选项可以获得答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord]，用于插件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha]，用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 分论坛][reddit] 在 [/r/homeassistant][reddit]

您还可以在这里 [打开一个问题][issue] GitHub。

## 作者与贡献者

该存储库的原始设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权 (c) 2021-2025 Franck Nijhof

特此授予任何获得该软件及相关文档文件（“软件”）副本的人免费许可，以不受限制地处理该软件，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售该软件的副本，并允许向其提供软件的人这样做，前提是满足以下条件：

以上版权声明和本许可声明应包含在所有副本或软件的实质性部分中。

本软件“按原样”提供，不作任何种类的明示或暗示的担保，包括但不限于对适销性、特定用途适用性和非侵权的担保。在任何情况下，作者或版权持有人均不对因使用本软件或与本软件相关的其他交易而导致的任何索赔、损害或其他责任承担责任，无论是在合同、侵权或其它情况下。

[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[addon]: https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_phpmyadmin&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository
[contributors]: https://github.com/hassio-addons/addon-phpmyadmin/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-phpmyadmin/171729?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-phpmyadmin/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-phpmyadmin/releases
[semver]: https://semver.org/spec/v2.0.0.html