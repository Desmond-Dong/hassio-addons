# ESPHome 开发版插件

这是 ESPHome 插件的 **开发** 版本。

要部署生产节点，请使用主流发布的插件。

该插件使用每天在协调世界时（UTC）02:00 自动构建的 ESPHome 版本，并用于测试开发中的组件。请参阅下面的 `esphome_fork` 配置以正确配置插件。更新配置后，请确保重建映像。

## 配置

**注意**：_记得在更改配置时重启插件。_

### 选项：`esphome_fork`

从一个 fork 或分支安装 ESPHome。
例如，要测试一个拉取请求，请使用 `pull/XXXX/head`，其中 `XXXX` 是 PR 编号，
或者您可以指定 fork 拥有者的用户名和分支 `username:branch`，这
假设该仓库仍然名为 `esphome`。

如果您需要在更新映像之前测试开发分支上的最新提交，可以在此处输入 `dev`。

请注意，您使用的 fork 或分支 **必须** 与 ESPHome 开发版保持最新，
否则插件 **将无法启动**。

## 通用 ESPHome 插件配置

通用选项在其他版本中也可用。

### 选项：`ssl`

启用或禁用与该插件的 web 服务器之间的加密 SSL/TLS（HTTPS）连接。
将其设置为 `true` 以加密通信，`false` 则不加密。
请注意，如果您将其设置为 `true`，还必须生成密钥和证书
文件以进行加密。例如使用 [Let's Encrypt](https://www.home-assistant.io/addons/lets_encrypt/)
或 [自签名证书](https://www.home-assistant.io/docs/ecosystem/certificates/tls_self_signed_certificate/)。

### 选项：`certfile`

用于 SSL 的证书文件。如果此文件不存在，则插件启动将失败。

**注意**：该文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认位置。

### 选项：`keyfile`

用于 SSL 的私钥文件。如果此文件不存在，则插件启动将失败。

**注意**：该文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认位置。

### 选项：`leave_front_door_open`

将此选项添加到插件配置中可以通过将其设置为 `true`
来禁用身份验证。

### 选项：`relative_url`

在相对 URL 下托管 ESPHome 仪表板，以便可以集成
到现有的 Web 代理中，例如在相对 URL 下的 NGINX。默认为 `/`。

### 选项：`status_use_ping`

默认情况下，仪表板使用 mDNS 检查节点是否在线。这在
子网之间不起作用，除非您的路由器支持 mDNS 转发或 avahi。

将其设置为 `true` 将使 ESPHome 使用 ICMP ping 请求来获取节点状态。 如果所有节点即使在连接时也始终显示离线状态，请使用此选项。

### 选项：`streamer_mode`

如果设置为 `true`，则会启用流媒体模式，使 ESPHome 隐藏所有
潜在的私人信息。例如 WiFi (B)SSIDs（可能用于查找您的位置）、用户名等。请注意，您需要在 YAML 文件中使用
`!secret` 标签，以防止这些信息在编辑和验证时显示。