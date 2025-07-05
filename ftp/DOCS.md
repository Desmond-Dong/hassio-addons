# Home Assistant Community Add-on: FTP

FTP协议有时会派上用场。虽然它比较老旧，但仍然有其用途。例如，大多数IP摄像头仍然支持通过FTP上传图像或视频。

此插件为Hass.io提供了一种相对安全的方式来实现FTP服务器。虽然FTP由于其（未加密）的性质并不是完全安全的，但此插件支持FTP over SSL (FTPS) 并将其虚拟用户限制在其主目录中。

当然，如果你真的想这样做，你也可以使用此插件通过FTP再次访问你的Home Assistant配置。

## 安装

此插件的安装非常简单，与安装任何其他Home Assistant插件没有区别。

1. 点击下面的Home Assistant我的按钮，在您的Home Assistant实例上打开此插件。

   ![在您的Home Assistant实例中打开此插件][插件徽章][插件]

1. 点击“安装”按钮来安装插件。
1. 启动“FTP”插件
1. 检查“FTP”插件的日志，看看是否一切顺利。

## 配置

**注意**：_更改配置时请记得重启插件。_

示例插件配置：

```yaml
log_level: info
port: 21
data_port: 20
banner: Welcome to the Hass.io FTP service.
pasv: true
pasv_min_port: 30000
pasv_max_port: 30010
pasv_address: ""
ssl: false
certfile: fullchain.pem
keyfile: privkey.pem
implicit_ssl: false
max_clients: 5
users:
  - username: hassio
    password: changeme
    allow_chmod: true
    allow_download: true
    allow_upload: true
    allow_dirlist: true
    addons: false
    backup: true
    config: true
    media: true
    share: true
    ssl: false
  - username: camera
    password: changeme
    allow_chmod: false
    allow_download: false
    allow_upload: true
    allow_dirlist: true
    addons: false
    backup: false
    config: false
    media: false
    share: true
    ssl: false
```

**注意**：_这只是一个示例，不要复制粘贴！自己创建！_

### 选项：`log_level`

`log_level`选项控制插件的日志输出级别，可以更改为更详细或更简洁，这在处理未知问题时可能很有用。可能的值有：

- `trace`：显示所有细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：异常情况，但不是错误。
- `error`：运行时错误，不需要立即处理。
- `fatal`：出了严重问题。插件变得无法使用。

请注意，每个级别自动包含更严重级别的日志消息，例如，`debug`也显示`info`消息。默认情况下，`log_level`设置为`info`，这是推荐设置，除非你在解决问题。

这些日志级别也会影响FTP服务器的日志级别。

### 选项：`port`

FTP监听传入FTP连接的端口。

### 选项：`data_port`

从其中发起PORT样式连接的端口。

### 选项：`banner`

此字符串选项允许你提供FTP服务器在首次连接时显示的问候横幅。

### 选项：`pasv`

如果你想要禁用PASV方法来获取数据连接，请将其设置为`false`。有关被动与主动FTP的更多信息，请参阅[这个优秀的Stack Overflow][passive-vs-active]答案。

### 选项：`pasv_min_port`

为PASV样式数据连接分配的最小端口。可用于指定一个较窄的端口范围以帮助防火墙。

### 选项：`pasv_max_port`

为PASV样式数据连接分配的最大端口。可用于指定一个较窄的端口范围以帮助防火墙。

### 选项：`pasv_address`

使用此选项来覆盖FTP服务器在响应PASV命令时宣传的IP地址。提供一个数字IP地址，或提供一个主机名，它将在启动时为您进行DNS解析。如果留空，地址将从传入的连接套接字中获取。

### 选项：`pasv_addr_resolve`

设置为`true`以允许为PASV连接解析主机名。

### 选项：`ssl`

启用/禁用FTP服务器的SSL。设置为`true`以启用它，`false`否则。

### 选项：`certfile`

用于SSL的证书文件。

**注意**：_文件必须存储在`/ssl/`中，这是默认的_

### 选项：`keyfile`

用于SSL的私钥文件。

**注意**：_文件必须存储在`/ssl/`中，这是默认的_

### 选项：`implicit_ssl`

如果设置为`true`，则所有连接的第一件事就是期望进行SSL握手（FTPS协议）。

### 选项：`max_clients`

这是同时可以连接的最大客户端数量。任何额外的连接客户端将收到错误消息。

### 选项：`users`

此选项允许你指定一个或多个用户。每个用户可以拥有其自己的权限，如下面的子选项中定义。

#### 子选项：`username`

用户需要用来登录FTP服务器的用户名。一个有效的用户名最多有32个字符，只包含`A-Z`和`0-9`。
用户名可以包含连字符（`-`），但不得以连字符开头或结尾。

#### 子选项：`password`

用户登录时使用的密码。

#### 子选项：`allow_chmod`

将此选项设置为`true`将允许该用户使用`SITE CHMOD`命令。

#### 子选项：`allow_download`

将此选项设置为`true`将允许用户从FTP服务器下载文件。

#### 子选项：`allow_upload`

此选项控制是否允许任何更改文件系统的FTP命令。

这些命令是`STOR`、`DELE`、`RNFR`、`RNTO`、`MKD`、`RMD`、`APPE`和`SITE`。

#### 子选项：`allow_dirlist`

将此选项设置为`true`，允许用户使用列表命令浏览用户被授予访问权限的所有目录。

#### 子选项：`addons`

允许用户访问`/addons`目录。

#### 子选项：`backup`

允许用户访问`/backup`目录。

#### 子选项：`config`

允许用户访问`/config`目录。

#### 子选项：`media`

允许用户访问`/media`目录。

#### 子选项：`share`

允许用户访问`/share`目录。

#### 子选项：`ssl`

允许用户访问`/ssl`目录。

### 选项：`i_like_to_be_pwned`

在插件配置中添加此选项允许你通过将其设置为`true`来绕过HaveIBeenPwned密码要求。

**注意**：_我们强烈建议选择一个更强的/更安全的密码，而不是使用此选项！自己承担风险！_

## 更改日志与发布

此存储库使用GitHub的[发布][releases]功能来维护更改日志。

发布基于[语义版本控制][semver]，并使用`MAJOR.MINOR.PATCH`的格式。简而言之，版本将根据以下内容增加：

- `MAJOR`：不兼容或主要更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的错误修复和软件包更新。

## 支持

有问题吗？

你有几个选项来获得答案：

- [Home Assistant Community Add-ons Discord聊天服务器][discord]用于插件支持和功能请求。
- [Home Assistant Discord聊天服务器][discord-ha]用于一般Home Assistant讨论和问题。
- Home Assistant的[社区论坛][forum]。
- 加入Reddit的[Reddit子版块][reddit]在[/r/homeassistant][reddit]

你也可以在GitHub上[打开一个问题][issue]。

## 作者与贡献者

此存储库的原始设置由[Franck Nijhof][frenck]完成。

要查看所有作者和贡献者的完整列表，请查看[贡献者页面][contributors]。

## 许可证

MIT许可证

版权所有（c）2017-2025 Franck Nijhof

特此授予任何人免费获得此软件及其相关文档文件（“软件”）的副本的权限，可以在软件中自由处理，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件的副本，并允许提供软件的人这样做，但需遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件按“原样”提供，不提供任何形式的保证，包括但不限于对适销性、特定用途适用性和非侵权的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害或其他责任承担责任，无论是合同行为、侵权行为或其他行为，均由软件或软件的使用或其他交易引起。

[插件徽章]: https://my.home-assistant.io/badges/supervisor_addon.svg
[插件]: https://my.home-assistant.io/redirect/supervisor_addon/? addon=a0d7b954_ftp&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository
[贡献者]: https://github.com/hassio-addons/addon-ftp/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[论坛]: https://community.home-assistant.io/t/home-assistant-community-add-on-ftp/36799?u=frenck
[frenck]: https://github.com/frenck
[问题]: https://github.com/hassio-addons/addon-ftp/issues
[passive-vs-active]: https://stackoverflow.com/a/1699163/299699
[reddit]: https://reddit.com/r/homeassistant
[发布]: https://github.com/hassio-addons/addon-ftp/releases
[semver]: http://semver.org/spec/v2.0.0.htm