# Home Assistant 插件: phpMyAdmin

phpMyAdmin是一个用于MySQL和MariaDB的数据库管理工具。常用操作（管理数据库、表、列、关系、索引、用户、权限等）可以通过用户界面进行，同时您仍然可以直接执行任何SQL语句。

此插件专门设计用于管理官方的Home Assistant MariaDB插件。

## 安装

按照以下步骤在您的系统上安装插件：

添加仓库 `https://github.com/erik73/hassio-addons`。
找到"phpMyAdmin"插件并点击它。
点击"安装"按钮。

## 配置

**注意**: _修改配置时请记得重启插件。_

示例插件配置：

```yaml
log_level: info
```

**注意**: _这只是一个示例，别复制粘贴！创建您自己的配置！_

### 选项: `upload_limit`

默认情况下，上传（如导入操作）的大小限制设置为64MB。可以使用此选项增加大小限制，例如，`100`将是100MB。

### 选项: `log_level`

`log_level`选项控制插件的日志输出级别，可以更改为更详细或更简洁的格式，这可能在处理未知问题时非常有用。可能的值包括：

- `trace`: 显示每一个细节，如所有调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 正常（通常）有趣的事件。
- `warning`: 不是错误的异常情况。
- `error`: 不需要立即行动的运行时错误。
- `fatal`: 有严重错误发生。插件变得不可用。

请注意，每个级别自动包含更严重级别的日志消息，例如，`debug`级别也显示`info`消息。默认情况下，`log_level`设置为`info`，这是推荐的设置，除非您在进行故障排除。

## 已知问题和限制

- 此插件需要核心MariaDB插件版本2.0或更高版本。
- 此插件旨在管理官方的Home Assistant MariaDB插件。它无法连接到其他MySQL或MariaDB服务器。

## 更新日志与发布

此仓库使用[GitHub的发布][releases]功能来保持变更日志。

发布基于[语义版本控制][semver]，格式为`MAJOR.MINOR.PATCH`。简而言之，版本的增量基于以下情况：

- `MAJOR`: 不兼容或重大更改。
- `MINOR`: 向后兼容的新功能和增强。
- `PATCH`: 向后兼容的错误修复和软件包更新。

## 支持

有问题吗？

您可以在这里[报告问题][issue] GitHub。

[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[addon]: https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_phpmyadmin&repository_url=https%3A%2F%2Fgithub.com%2Ferik73%2Frepository
[contributors]: https://github.com/erik73/addon-phpmyadmin/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-phpmyadmin/171729?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/erik73/addon-phpmyadmin/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/erik73/addon-phpmyadmin/releases
[semver]: https://semver.org/spec/v2.0.0.html