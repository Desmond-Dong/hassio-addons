# Home Assistant Community Add-on: Advanced SSH & Web Terminal

这个插件允许你使用 SSH 或 Web Terminal 登录到你的 Home Assistant 实例，从而访问你的文件夹，并且还包括一个命令行工具，用于执行重启、更新和检查实例等操作。

这是一个增强版的 Home Assistant 提供的 [SSH 插件][hass-ssh]，它侧重于安全性、可用性、灵活性，并提供通过 Web 界面访问的功能。

## 注意

高级 SSH & Web Terminal 插件非常强大，它几乎可以访问你系统中的所有工具和硬件。

虽然这个插件是经过精心创建和维护的，并且考虑了安全性，但在错误或不熟悉的情况下，它可能会损坏你的系统。

## 功能

这个插件当然提供了一个基于 [OpenSSH][openssh] 的 SSH 服务器，以及一个基于 Web 的 Terminal（可以包含在你的 Home Assistant 前端）。

此外，它还提供了以下功能：

- 直接从 Home Assistant 前端访问命令行！
- SSH 的安全默认配置：
  - 仅允许使用配置的用户登录，即使创建了更多用户。
  - 仅使用已知的安全密码和算法。
  - 限制登录尝试次数，以更好地抵御暴力攻击。
- 提供一个 SSH 兼容模式选项，允许旧客户端连接。
- 支持 Mosh，允许漫游和间歇性连接。
- 默认情况下禁用 SFTP 支持，但用户可以配置。
- 如果 Home Assistant 是通过通用 Linux 安装器安装的，则兼容。
- 用户名是可配置的，因此 `root` 不再是必须的。
- 在插件重启之间持久化自定义 SSH 客户端设置和密钥
- 日志级别，以便更容易地排除问题。
- 对音频、uart/串行设备和 GPIO 引脚的硬件访问。
- 以更高权限运行，允许你调试和测试更多情况。
- 可以访问主机系统的 dbus。
- 可以选择访问主机系统上运行的 Docker 实例。
- 在主机网络级别运行，允许你打开端口或运行小守护进程。
- 在启动时安装自定义 Alpine 软件包。这允许你安装你喜欢的工具，这些工具将每次登录时都可用。
- 在插件启动时执行自定义命令，以便你可以根据喜好定制 Shell。
- [ZSH][zsh] 作为默认 Shell。对初学者更容易使用，对有经验的用户更高级。它甚至预装了 ["Oh My ZSH"][ohmyzsh]，并启用了某些插件。
- 包含一套合理的工具：curl、Wget、RSync、GIT、Nmap、Mosquitto 客户端、MariaDB/MySQL 客户端、Awake（“网络唤醒”）、Nano、Vim、tmux，以及一些常用的网络工具。

## 安装

这个插件的安装非常简单，与安装任何其他 Home Assistant 插件没有区别。

1. 点击下面的 Home Assistant My 按钮来在你的 Home Assistant 实例上打开插件。

   ![在你的 Home Assistant 实例上打开这个插件][addon-badge]][addon]

1. 点击“安装”按钮来安装插件。
1. 配置 `username` 和 `password`/`authorized_keys` 选项。
1. 启动“高级 SSH & Web Terminal”插件。
1. 检查“高级 SSH & Web Terminal”插件的日志，看看是否一切正常。

## 配置

**注意**：_配置更改后，请记得重启插件。_

SSH 插件配置：

```yaml
log_level: info
ssh:
  username: homeassistant
  password: ""
  authorized_keys:
    - ssh-ed25519 AASDJKJKJFWJFAFLCNALCMLAK234234.....
  sftp: false
  compatibility_mode: false
  allow_agent_forwarding: false
  allow_remote_port_forwarding: false
  allow_tcp_forwarding: false
zsh: true
share_sessions: true
packages:
  - build-base
init_commands:
  - ls -la
```

**注意**：_这只是一个示例，不要复制粘贴！创建你自己的！_

### 选项：`log_level`

`log_level` 选项控制插件的日志输出级别，可以更详细或更简洁，这在处理未知问题时可能很有用。可能的值有：

- `trace`：显示所有细节，如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：非错误的异常情况。
- `error`：不需要立即处理的运行时错误。
- `fatal`：发生了严重错误。插件变得无法使用。

请注意，每个级别自动包含更严重级别的日志消息，例如，`debug` 也显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非你在排除问题。

使用 `trace` 或 `debug` 日志级别将 SSH 和 Terminal 守护进程置于调试模式。在 SSH 以调试模式运行时，它将只能接受一次连接。

### 选项组 `ssh`

---

以下选项属于 `ssh` 选项组。这些设置仅适用于 SSH 守护进程。

#### 选项 `ssh`：`username`

这个选项允许你更改使用 SSH 登录时的用户名。它仅用于身份验证；认证后，你将是 `root` 用户。使用 `root` 作为用户名是可能的，但不推荐。用户名将按推荐实践转换为小写。

**注意**：_由于限制，你需要将此选项设置为 `root` 才能启用 SFTP 功能。_

#### 选项 `ssh`：`password`

设置登录密码。将其留空将禁用使用密码进行身份验证的可能性。从安全角度来看，我们强烈建议不要使用此选项。

#### 选项 `ssh` `authorized_keys`

向你的 SSH 服务器添加一个或多个公钥以用于身份验证。这是推荐的方法，而不是设置密码。

请查看 GitHub 创建的出色的 [文档][github-ssh]，了解如何使用公钥/私钥对以及如何创建它们。

**注意**：_请确保将密钥指定为列表，通过在 `[]` 中逗号分隔粘贴。_

#### 选项 `ssh`：`sftp`

设置为 `true` 时，插件将在 SSH 守护进程上启用 SFTP 支持。请仅在计划使用它时启用它。

**注意**：_由于限制，你需要将用户名设置为 `root` 才能启用 SFTP 功能。_

#### 选项 `ssh`：`compatibility_mode`

这个 SSH 插件侧重于安全性，因此仅启用了已知的安全加密方法。然而，一些旧客户端不支持这些方法。将此选项设置为 `true` 将启用原始默认方法集，允许这些客户端连接。

**注意**：_启用此选项会降低 SSH 服务器的安全性！_

#### 选项 `ssh`：`allow_agent_forwarding`

指定是否允许 ssh-agent 转发。

**注意**：_启用此选项会降低 SSH 服务器的安全性！尽管如此，这个警告是有争议的。_

#### 选项 `ssh`：`allow_remote_port_forwarding`

指定是否允许远程主机连接到为客户端转发的端口。

**注意**：_启用此选项会影响所有远程转发，因此在这样做之前要慎重考虑。_

#### 选项 `ssh`：`allow_tcp_forwarding`

指定是否允许 TCP 转发。

**注意**：_启用此选项会降低 SSH 服务器的安全性！尽管如此，这个警告是有争议的。_

### 共享设置

---

以下选项在 SSH 和 Web Terminal 之间共享。

#### 选项：`zsh`

插件预装并配置了 ZSH 作为默认 Shell。然而，ZSH 可能不是你的首选。通过将此选项设置为 `false`，你将禁用 ZSH，插件将回退到 Bash。

#### 选项：`share_sessions`

默认情况下，Web 客户端和 SSH 之间的终端会话是共享的。这允许你从任一方继续你之前离开的终端。

此选项允许你通过将其设置为 `false` 来禁用此行为，这实际上将 SSH 设置为像以前一样行为。

#### 选项：`packages`

允许你指定要安装到你的 Shell 环境中的额外 [Alpine 软件包](https://pkgs.alpinelinux.org/packages)（例如，Python、Joe、Irssi）。

**注意**：_添加许多软件包将导致插件启动时间更长。_

#### 选项：`init_commands`

使用 `init_commands` 选项可以进一步定制你的 Shell 环境。将一个或多个 Shell 命令添加到列表中，它们将在每次插件启动时执行。

## 已知问题和限制

- 当 SFTP 启用时，用户名必须设置为 `root`。
- 如果你想使用 rsync 进行文件传输，用户名必须设置为 `root`。

## 更改日志与发布

此存储库使用 GitHub 的发布功能功能维护一个更改日志。

发布基于 [语义版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 格式。简而言之，版本将根据以下情况增加：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的补丁和软件包更新。

## 支持

有问题？

你有几个选项可以回答这些问题：

- Home Assistant Community Add-ons Discord 聊天服务器 [discord] 用于插件支持和功能请求。
- Home Assistant Discord 聊天服务器 [discord-ha] 用于一般 Home Assistant 讨论和问题。
- Home Assistant 社区论坛 [forum]。
- 加入 Reddit 子版块 [reddit] 在 [/r/homeassistant][reddit]

你也可以在 GitHub 上 [打开一个问题][issue]。

## 作者与贡献者

此存储库的原始设置由 [Franck Nijhof][frenck] 完成。

要查看所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有（c）2017-2025 Franck Nijhof

特此免费授予任何获得此软件及其相关文档文件（“软件”）副本的人，在不受限制的情况下处理软件的权利，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或出售软件副本的权利，并允许获得软件的人这样做，但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件按“原样”提供，不提供任何类型的保证，无论是明示的还是暗示的，包括但不限于对适销性、特定用途的适用性和非侵权性的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害或其他责任承担责任，无论是由合同、侵权或其他行为引起的，也不论是由软件或其使用或其他交易引起的。