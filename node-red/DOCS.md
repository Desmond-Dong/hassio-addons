# Home Assistant Community Add-on: Node-RED

[Node-RED][nodered] 是一个用于以新颖有趣的方式连接硬件设备、API 和在线服务的编程工具。

它提供了一个基于浏览器的编辑器，可以轻松地使用调色板中的各种节点来连接流程，并且只需单击一下即可将其部署到其运行时环境中。

## 安装

此插件的安装过程非常简单，与安装任何其他 Home Assistant 插件没有区别。

1. 点击下方的 Home Assistant 我的按钮，在您的 Home Assistant 实例上打开此插件。

   ![在您的 Home Assistant 实例中打开此插件][addon-badge]][addon]

1. 点击“安装”按钮来安装插件。
1. 启动“Node-RED”插件。
1. 检查“Node-RED”的日志，看看是否一切正常。
1. 点击“打开 Web UI”按钮进入 Node-RED。
1. 插件一开箱即可使用！无需配置服务器！

**注意**：插件开箱即预配置！无需添加/更改/更新服务器连接设置！

## 配置

**注意**：更改配置时，请记得重启插件。

示例插件配置：

```yaml
log_level: info
http_node:
  username: MarryPoppins
  password: Supercalifragilisticexpialidocious
http_static:
  username: MarryPoppins
  password: Supercalifragilisticexpialidocious
ssl: true
certfile: fullchain.pem
keyfile: privkey.pem
system_packages:
  - ffmpeg
npm_packages:
  - node-red-admin
init_commands:
  - echo 'This is a test'
  - echo 'So is this...'
```

**注意**：这只是个示例，不要复制粘贴！自己创建！

### 选项：`log_level`

`log_level` 选项控制插件的日志输出级别，可以更改为更详细或更简洁，这在处理未知问题时可能很有用。可能的值有：

- `trace`：显示每个细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：非错误异常情况。
- `error`：不需要立即处理的运行时错误。
- `fatal`：出了严重问题。插件变得无法使用。

请注意，每个级别自动包含更严重级别的日志消息，例如，`debug` 也显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐设置，除非您正在排错。

### 选项：`ssl`

启用/禁用 Web 界面的 SSL（HTTPS）。

设置为 `true` 以启用它，否则设置为 `false`。

**注意**：SSL 设置仅适用于直接访问，对 Ingress 服务无影响。

### 选项：`certfile`

用于 SSL 的证书文件。

**注意**：文件必须存储在 `/ssl/`，这是默认的。

### 选项：`keyfile`

用于 SSL 的私钥文件。

**注意**：文件必须存储在 `/ssl/`，这是默认的。

### 选项：`credential_secret`

凭证由 Node-RED 在存储中加密，使用密钥。此选项允许您指定您的密钥。这可以是您喜欢的任何内容，就像密码一样。确保将其保存在安全的地方。您将来可能需要它！（例如，在恢复备份时）。

**注意**：一旦您设置了此属性，请不要更改它——这样做将阻止 Node-RED 解密您现有的凭证，它们将丢失。

**注意**：如果您已手动启用 Node-RED 中项目的使用，此选项将被 Node-RED 忽略，尽管它是必需的。

### 选项：`theme`

设置 Node-RED 主题之一。目前可用的选项有：

- `default`
- `aurora`
- `cobalt2`
- `dark`
- `dracula`
- `espresso-libre`
- `github-dark`
- `github-dark-default`
- `github-dark-dimmed`
- `midnight-red`
- `monoindustrial`
- `monokai`
- `monokai-dimmed`
- `noctis`
- `oceanic-next`
- `oled`
- `one-dark-pro`
- `one-dark-pro-darker`
- `solarized-dark`
- `solarized-light`
- `tokyo-night`
- `tokyo-night-light`
- `tokyo-night-storm`
- `totallyinformation`
- `zenburn`

### 选项：`http_node`

要为节点定义的 HTTP 端点（`httpNodeRoot`）设置密码保护，可以使用以下属性：

- `username`
- `password`

**注意**：为了使用 `http_node`，您需要在 Ingress 之外使用网络端口来暴露 Node-RED。HTTP 节点也将在 `/endpoint/` 下显示，如 UI 中所示。如果使用 `node-red-dashboard` 模块，它也将在此路径下托管，并将使用此处设置的任何凭证。

### 选项：`http_static`

要为静态内容（httpStatic）设置密码保护，可以使用以下属性：

- `username`
- `password`

### 选项：`system_packages`

允许您指定要安装到您的 Node-RED 设置中的额外 [Alpine 包][alpine-packages]（例如，`g++`、`make`、`ffmpeg`）。

**注意**：添加许多包将导致插件启动时间更长。

### 选项：`npm_packages`

允许您指定要安装到您的 Node-RED 设置中的额外 [NPM 包][npm-packages] 或 [Node-RED 节点][node-red-nodes]（例如，`node-red-dashboard`、`node-red-contrib-ccu`）。

**注意**：添加许多包将导致插件启动时间更长。

### 选项：`init_commands`

使用 `init_commands` 选项可以进一步自定义您的 Node-RED 环境。将一个或多个 Shell 命令添加到列表中，它们将在每次此插件启动时执行。

### 选项：`safe_mode`

将此选项设置为 `true` 将以 `--safe` 标志启动 Node-Red，开始应用程序而不启动任何流程以进行故障排除。

### 选项：`leave_front_door_open`

将此选项添加到插件配置中，允许您通过将其设置为 `true` 并留空用户名和密码来禁用插件的身份验证。

**注意**：我们强烈建议不要使用此功能，即使此插件仅暴露到您的内部网络。使用此功能风险自负！

### 选项：`max_old_space_size`

设置 nodeJS V8 的旧内存部分的最大内存大小（以 MB 为单位）。随着内存消耗接近极限，V8 将花费更多时间进行垃圾回收，以释放未使用的内存。

<https://nodejs.org/api/cli.html#--max-old-space-sizesize-in-megabytes>

## 配置文件夹

插件将将其大部分配置存储在 Node-RED 插件配置文件夹中，包括 `flows.json`。

## 时区配置

插件将使用 Home Assistant 设置中的时区。如果时区不正确，请更新 Home Assistant 中的设置并重启 Node-RED 插件以应用最新配置。

如果您希望特定于 Node-RED 覆盖时区，可以在 `settings.js` 文件中配置。

为此，请使用文本编辑器打开文件，并在 `module.exports = {` 行上方添加以下内容。

`process.env.TZ = "America/Toronto";`

时区需要反映您的环境。

保存文件并重启 Node-RED 插件。

## 已知问题和限制

- 虽然此插件随 Node-RED 仪表板一起提供，但它目前不支持通过 Ingress 访问仪表板。这是 Node-RED 仪表板端的技术限制。

- 如果您无法访问 HTTP 节点或 Node-RED 仪表板，请检查您是否通过在插件的“网络”配置部分设置端口号来启用了直接访问模式。

- 如果您无法访问 HTTP 节点或 Node-RED 仪表板，请检查您的 URL 是否以 `/endpoint/` 开头，否则 Home Assistant 身份验证将生效。

- 如果在更新后看到以下错误：
  `WARNING (MainThread) [hassio.api.proxy] Unauthorized WebSocket access!`。
  请验证 Node-RED 中 Home Assistant 服务器设置的配置。这可以通过双击任何 Home Assistant 节点并选择服务器名称旁边的铅笔图标找到。应选中声明 `I use the Home Assistant Add-On` 的复选框。

## 更改日志和发布

此存储库使用 GitHub 的发布功能功能来维护更改日志。日志的格式基于 [Keep a Changelog][keepchangelog]。

发布基于 [Semantic Versioning][semver]，并使用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将根据以下内容增加：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的补丁和包更新。

## 支持

有问题？

您有几个选项可以回答这些问题：

- Home Assistant Community Add-ons Discord 服务器 [discord] 用于插件支持和功能请求。
- Home Assistant Discord 服务器 [discord-ha] 用于一般 Home Assistant 讨论和问题。
- Home Assistant 社区论坛 [forum]。
- 加入 Reddit 子版块 [reddit] 中的 `/r/homeassistant` [reddit]。
- Node-RED 文档 [nodered-docs]

您也可以在 GitHub 上 [打开问题][issue]。

## 作者和贡献者

此存储库的原始设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2018-2025 Franck Nijhof

特此授予任何获得此软件及其相关文档文件（“软件”）副本的人，在不限制的前提下自由处理软件的权利，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权利，并允许获得软件的人这样做，但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件按“原样”提供，不提供任何形式的保证，包括但不限于对适销性、特定用途适用性和非侵权性的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害或其他责任负责，无论该索赔、损害或其他责任是由合同、侵权或其他行为引起的，均与软件或软件的使用或其他交易无关。

[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[addon]: https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_nodered&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository
[alpine-packages]: https://pkgs.alpinelinux.org/packages
[contributors]: https://github.com/hassio-addons/addon-node-red/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-node-red/55023?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-node-red/issues
[node-red-nodes]: https://flows.nodered.org/?type=node&num_pages=1
[nodered-docs]: https://nodered.org/docs
[nodered]: https://nodered.org
[npm-packages]: https://www.npmjs.com
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-node-red/releases
[semver]: https://semver.org/spec/v2.0.0.html