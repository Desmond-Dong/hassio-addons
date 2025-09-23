# Home Assistant Community Add-on: phpMyAdmin

phpMyAdmin 是一个用于 MySQL & MariaDB 的数据库管理工具。常见的操作（如管理数据库、表、列、关系、索引、用户、权限等）可以通过用户界面进行，同时您仍然可以直接执行任何 SQL 语句。

这个 add-on 专门设计用来管理官方的 Home Assistant MariaDB add-on。

## 安装

这个 add-on 的安装过程非常简单，与其他 Home Assistant add-on 的安装方式相同。

1. 点击下面的 Home Assistant My 按钮，在您的 Home Assistant 实例中打开 add-on。

   [![在您的 Home Assistant 实例中打开这个 add-on。][addon-badge]][addon]

1. 点击 "Install" 按钮来安装 add-on。
1. 启动 "phpMyAdmin" add-on。
1. 享受 add-on 带来的功能吧！

## 配置

**注意**：_更改配置时请记得重启 add-on。_

示例 add-on 配置：

```yaml
log_level: info
```

**注意**：_这只是个示例，不要直接复制粘贴！请创建自己的配置！_

### 选项：`upload_limit`

默认情况下，上传的大小限制（例如在导入操作中）设置为 64MB。这个选项可以增加这个限制，例如，`100` 将是 100MB。

### 选项：`log_level`

`log_level` 选项控制 add-on 的日志输出级别，可以更详细或更简洁，这在处理未知问题时可能很有用。可能的值有：

- `trace`：显示所有细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：常规（通常）有趣的事件。
- `warning`：非错误的异常情况。
- `error`：不需要立即处理的运行时错误。
- `fatal`：出现了严重错误。add-on 变得无法使用。

请注意，每个级别自动包含更严重级别的日志消息，例如，`debug` 也显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，除非您正在调试，否则这是推荐的设置。

## 已知问题和限制

- 这个 add-on 需要 core MariaDB add-on 版本 2.0 或更高版本。
- 这个 add-on 创建的目的是允许管理官方的 Home assistant MariaDB add-on。它不能连接到其他 MySQL 或 MariaDB 服务器。

## 更改日志与发布

这个仓库使用 [GitHub 的发布][releases] 功能来维护一个更改日志。

发布基于 [语义版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将根据以下内容进行递增：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的补丁和软件包更新。

## 支持

有问题？

您有几个选项可以回答这些问题：

- [Home Assistant Community Add-ons Discord 服务器][discord] 用于 add-on 支持和功能请求。
- [Home Assistant Discord 服务器][discord-ha] 用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

您也可以在 GitHub 上 [打开一个 issue][issue]。

## 作者与贡献者

这个仓库的原始设置由 [Franck Nijhof][frenck] 完成。

查看 [贡献者页面][contributors] 获取所有作者和贡献者的完整列表。

## 许可证

MIT 许可证

版权所有 (c) 2021-2025 Franck Nijhof

特此免费授予任何获得此软件及其相关文档文件（以下简称“软件”）副本的人，在不受限制的情况下处理此软件的权利，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权利，并允许提供软件的人这样做，但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件按“原样”提供，不提供任何形式的保证，无论是明示的还是暗示的，包括但不限于对适销性、特定用途适用性和非侵权的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害或其他责任承担责任，无论是由合同、侵权或其他行为引起的，也不论是与软件有关还是与软件的使用或其他交易有关。

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