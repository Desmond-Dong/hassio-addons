# Home Assistant Community Add-on: Bookstack

BookStack 是一个简单、可自托管、易于使用的平台，用于组织和存储信息。请支持此软件的开发者 [Bookstack].

## 安装

此插件的安装过程非常直接，与安装任何其他 Home Assistant 插件没有区别。

1. 在插件商店中搜索 "bookstack" 插件并安装它。
1. 启动 "bookstack" 插件
1. 检查 "bookstack" 插件的日志，以查看是否一切正常。
1. 默认登录信息为 admin@admin.com/password。

## 配置

**注意**：_更改配置时，请记得重启插件。_

示例插件配置：

```yaml
log_level: info
ssl: false
certfile: fullchain.pem
keyfile: privkey.pem
envvars:
  - name: SESSION_COOKIE_NAME
    value: bookstack_session
```

**注意**：_这只是个示例，不要复制粘贴！自己创建！_

### 选项：`log_level`

`log_level` 选项控制插件的日志输出级别，可以更改为更详细或更简洁，这在处理未知问题时可能很有用。可能的值有：

- `trace`：显示所有细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：非错误的异常情况。
- `error`：不需要立即处理的运行时错误。
- `fatal`：出现了严重问题。插件变得无法使用。

请注意，每个级别自动包含更严重级别的日志消息，例如，`debug` 也显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐设置，除非您正在排错。

### 选项：`ssl`

启用/禁用 Bookstack 面板 Web 界面的 SSL（HTTPS）。

设置为 `true` 以启用它，否则设置为 `false`。

### 选项：`certfile`

用于 SSL 的证书文件。

**注意**：_文件必须存储在 `/ssl/`，这是默认的。_

### 选项：`keyfile`

用于 SSL 的私钥文件。

**注意**：_文件必须存储在 `/ssl/`，这是默认的。_

### 选项：`remote_mysql_host`

如果使用外部数据库，MySQL/MariaDB 数据库的主机名/地址。

### 选项：`remote_mysql_database`

仅适用于使用远程 MySQL 数据库时，数据库名称。

### 选项：`remote_mysql_username`

仅适用于使用远程 MySQL 数据库时，具有权限的用户名。

### 选项：`remote_mysql_password`

仅适用于使用远程 MySQL 数据库时，上述用户的密码。

### 选项：`remote_mysql_port`

仅适用于使用远程 MySQL 数据库时，数据库服务器正在监听的端口。

### 选项：`show_appkey`

如果设置为 `true`，将在插件日志中显示当前配置的 appkey。如果出现恢复情况，应记录下来。

### 选项：`appkey`

允许用户定义 appkey，以便从其他系统恢复。如果设置，在首次运行时将自动从配置中删除。

### 选项：`envvars`

这允许设置环境变量来控制 Bookstack 配置，如文档中所述：

<https://www.bookstackapp.com/docs/>

**注意**：_更改这些选项可能会导致您的实例出现问题。自己承担风险！_

这些是区分大小写的，并且任何特定配置设置的项目将优先。

#### 子选项：`name`

要设置的环境变量的名称。

#### 子选项：`value`

要设置的环境变量的值。

## 数据库使用

默认情况下，Bookstack 将自动使用并配置 Home Assistant MariaDB 插件，该插件应在启动前安装，这可以在配置中更改为使用外部 MySql/MariaDB 数据库。请注意，这两个选项之间没有简单的升级路径。

## 已知问题和限制

- 由于应用程序存储图像文件的方式，Ingress 将无法工作。

## 更改日志和发布

此存储库使用 [GitHub 的发布] 功能维护更改日志。

发布基于 [语义版本控制]，并使用 `MAJOR.MINOR.PATCH` 格式。简而言之，版本将根据以下情况递增：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的补丁和包更新。

## 支持

有问题？

您有几个选项可以回答它们：

- [Home Assistant Community Add-ons Discord 服务器] 用于插件支持和功能请求。
- [Home Assistant Discord 服务器] 用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛]。
- 加入 [Reddit 子版块] 在 [/r/homeassistant]。

您也可以 [在 GitHub 上打开一个问题]。

## 作者和贡献者

此存储库的原始设置由 [Paul Sinclair] 完成。

要查看所有作者和贡献者的完整列表，请查看 [贡献者页面]。

## 许可证

MIT 许可证

版权所有 (c) 2019-2025 Paul Sinclair

特此免费授予任何获得此软件及其相关文档文件（“软件”）副本的人，在不限制的情况下处理软件的权利，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权利，并允许提供软件的人进行这些操作，但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件按“原样”提供，不提供任何形式的保证，包括但不限于对适销性、特定用途适用性和非侵权的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害或其他责任负责，无论是由合同、侵权或其他行为引起的，也不论是与软件有关还是与软件的使用或其他交易有关。