# Home Assistant社区插件: phpMyAdmin

phpMyAdmin是一个用于MySQL和MariaDB的数据库管理工具。经常使用的操作（管理数据库、表、列、关系、索引、用户、权限等）可以通过用户界面进行，而你仍然可以直接执行任何SQL语句。

该插件专门设计用于管理官方的Home Assistant MariaDB插件。

## 安装

安装该插件非常简单，与安装任何其他Home Assistant插件没有区别。

1. 点击下面的Home Assistant我的按钮以在你的Home Assistant实例中打开该插件。

   [![在你的Home Assistant实例中打开此插件。][addon-badge]][addon]

1. 点击“安装”按钮以安装该插件。
1. 启动“phpMyAdmin”插件。
1. 享受该插件吧！

## 配置

**注意**: _当配置更改时，请记得重启插件。_

示例插件配置：

```yaml
log_level: info
```

**注意**: _这只是一个示例，请不要复制和粘贴！创建你自己的！_

### 选项: `upload_limit`

默认情况下，上传大小限制（用于导入等操作）设置为64MB。可以通过此选项增加，例如，`100`将是100MB。

### 选项: `log_level`

`log_level`选项控制插件的日志输出级别，可以调整为更详细或更简洁，这在处理未知问题时可能很有用。可能的值包括：

- `trace`：显示每个细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）感兴趣的事件。
- `warning`：不是错误的异常事件。
- `error`：不需要立即采取行动的运行时错误。
- `fatal`：出现了严重问题，插件无法使用。

请注意，每个级别自动包含更严重级别的日志消息，例如，`debug`也会显示`info`消息。默认情况下，`log_level`设置为`info`，这是推荐的设置，除非你在进行故障排除。

## 已知问题和限制

- 此插件需要核心MariaDB插件版本2.0或更高。
- 此插件旨在允许管理官方Home Assistant MariaDB插件。它不能连接到其他MySQL或MariaDB服务器。

## 更新日志和版本

该存储库使用[GitHub的发布][releases]功能维护变更日志。

发布基于[语义版本控制][semver]，并采用`MAJOR.MINOR.PATCH`的格式。简而言之，版本将基于以下内容递增：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的错误修复和软件包更新。

## 支持

有问题？

你有几种选择来获取答案：

- [Home Assistant社区插件Discord聊天服务器][discord]以获取插件支持和功能请求。
- [Home Assistant Discord聊天服务器][discord-ha]进行一般Home Assistant讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入在[/r/homeassistant][reddit]上的[Reddit子论坛][reddit]。

你也可以在这里[提交问题][issue]到GitHub。

## 作者及贡献者

该存储库的最初设置由[Franck Nijhof][frenck]完成。

有关所有作者和贡献者的完整列表，请查看[贡献者页面][contributors]。

## 许可证

MIT许可证

版权所有(c) 2021-2025 Franck Nijhof

特此免费授予任何获得本软件及相关文档文件（“软件”）副本的人处理软件的权利，包括但不限于使用、复制、修改、合并、出版、分发、再授权和/或出售软件副本的权利，并允许向其提供软件的人这样做，须遵守以下条件：

上述版权声明和本许可声明应包含在所有副本或软件的实质性部分中。

本软件按“原样”提供，不提供任何形式的保证，无论是明示还是暗示，包括但不限于对适销性、特定目的适用性和非侵权的保证。在任何情况下，作者或版权持有人对任何索赔、损害或其他责任不承担责任，无论是在合同诉讼、侵权或其他情况下，因本软件或其使用或其他交易而产生。

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