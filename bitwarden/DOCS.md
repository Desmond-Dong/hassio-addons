# Home Assistant Community Add-on: Vaultwarden (Bitwarden)

Bitwarden 是一个开源密码管理器，可以加密存储网站凭证等敏感信息。

Bitwarden 平台提供了多种客户端应用程序，包括网页界面、桌面应用程序、浏览器扩展和移动应用程序。

此插件基于轻量级且开源的 [Vaultwarden][vaultwarden] 实现，允许您自行托管这个优秀的密码管理器。

密码盗窃是一个严重的问题。您使用的网站和应用程序每天都在遭受攻击。安全漏洞发生，您的密码被盗。当您在所有地方重复使用相同的密码时，黑客可以轻松访问您的电子邮件、银行和其他重要账户。使用密码管理器！

## 安装

此插件的安装非常直接，与安装任何其他 Home Assistant 插件没有区别。

1. 点击下面的 Home Assistant 我的按钮，在您的 Home Assistant 实例中打开此插件。

   [![在您的 Home Assistant 实例中打开此插件][addon-badge]][addon]

1. 点击“安装”按钮以安装插件。
1. 启动“Vaultwarden (Bitwarden)”插件。
1. 检查“Vaultwarden (Bitwarden)”插件的日志，以查看是否一切顺利并获取管理员令牌/密码。
1. 点击“打开 Web UI”按钮以打开 Vaultwarden。
1. 将 `/admin` 添加到 URL 以访问管理员面板，例如 `http://hassio.local:7277/admin`。使用在第 4 步中获取的管理员令牌登录。
1. 日志中的管理员/令牌仅显示，直到它被保存或更改。在管理员面板中点击保存，以使用随机生成的密码或将其更改为您选择的密码。
1. 请务必将您的管理员令牌保存在安全的地方。**插件将永远不会再次显示它！**

## 配置

**注意**：_更改配置时，请记住重新启动插件。_

示例插件配置：

```yaml
log_level: info
ssl: false
certfile: fullchain.pem
keyfile: privkey.pem
request_size_limit: 10485760
```

**注意**：_这只是一个示例，不要复制粘贴它！创建您自己的！_

### 选项：`log_level`

`log_level` 选项控制插件的日志输出级别，可以更改为更详细或更简洁，这在您处理未知问题时可能很有用。可能的值有：

- `trace`：显示每个细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：异常情况，但不是错误。
- `error`：运行时错误，不需要立即采取行动。
- `fatal`：发生了严重错误。插件变得无法使用。

请注意，每个级别自动包含更严重级别的日志消息，例如 `debug` 也显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐设置，除非您正在排除故障。

### 选项：`ssl`

启用/禁用 SSL（HTTPS）。设置为 `true` 以启用，`false` 否则。

**注意**：_SSL 设置仅适用于直接访问，对 Ingress 服务没有影响。_

### 选项：`certfile`

用于 SSL 的证书文件。

**注意**：_文件必须存储在 `/ssl/` 中，这是默认设置。_

### 选项：`keyfile`

用于 SSL 的私钥文件。

**注意**：_文件必须存储在 `/ssl/` 中，这是默认设置。_

### 选项：`request_size_limit`

默认情况下，API 调用限制为 10MB。这应该足够大多数情况，但如果您想支持大型导入，这可能有限制。另一方面，您可能想将请求大小限制为小于该值，以防止 API 滥用和可能的拒绝服务攻击，特别是如果您在资源有限的情况下运行。

要设置限制，您可以使用此设置：10MB 将是 `10485760`。

## 已知问题和限制

- 由于 Bitwarden Vault 网页界面的技术限制，此插件目前无法支持 Ingress。
- 某些网页浏览器，如 Chrome，不允许在不安全上下文中使用 Web Crypto API。在这种情况下，您可能会遇到类似 `Cannot read property 'importKey'` 的错误。要解决这个问题，您需要启用 SSL 并使用 HTTPS 访问网页界面。

## 更改日志与发布

此存储库使用 [GitHub 的发布][releases] 功能维护更改日志。

发布基于 [语义版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 格式。简而言之，版本将根据以下内容进行递增：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的补丁和软件包更新。

## 支持

有问题吗？

您有几个选项可以回答这些问题：

- [Home Assistant Community Add-ons Discord 服务器][discord] 用于插件支持和功能请求。
- [Home Assistant Discord 服务器][discord-ha] 用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

您也可以在此处 [打开一个 GitHub 问题][issue]。

## 作者与贡献者

此存储库的原始设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2019-2025 Franck Nijhof

特此免费授予任何获得此软件及其相关文档文件（“软件”）副本的人，在软件中自由处理的权利，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或出售软件副本的权利，并允许获得软件的人这样做，但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件按“原样”提供，不提供任何形式的保证，无论是明示的还是暗示的，包括但不限于对适销性、特定用途适用性和非侵权性的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害赔偿或其他责任负责，无论是由合同、侵权或其他行为引起的，均与软件的使用或其他交易有关。

[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[addon]: https://my.home-assistant.io/redirect/supervisor_addon/? addon=a0d7b954_bitwarden&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository
[contributors]: https://github.com/hassio-addons/addon-bitwarden/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-bitwarden-rs/115573?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-bitwarden/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-bitwarden/releases
[semver]: https://semver.org/spec/v2.0.0.html
[vaultwarden]: https://github.com/dani-garcia/vaultwarden