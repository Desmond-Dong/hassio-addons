# ESPHome 开发版本插件

这是 **开发** 版本的 ESPHome 插件。

要部署生产节点，请使用主流发布插件。

该插件使用的是每天在 UTC 时间 02:00 自动构建的 ESPHome 版本，主要用于测试开发中的组件。请参见下面的 `esphome_fork` 配置，以正确配置插件。更新配置后，请确保重新构建映像。

## 配置

**注意**：_更改配置时，请记得重新启动插件。_

### 选项：`esphome_fork`

从一个分支或分叉安装 ESPHome。
例如，要测试一个拉取请求，可以使用 `pull/XXXX/head`，其中 `XXXX` 是 PR 编号，
或者您可以指定分叉拥有者的用户名和分支 `username:branch`，这假设仓库仍然名为 `esphome`。

如果您需要在映像更新之前测试开发分支上的最新提交，可以在这里输入 `dev`。

请注意，您使用的分叉或分支 **必须** 是与 ESPHome 开发版保持同步的，否则插件 **将无法启动**。

## 一般 ESPHome 插件配置

通用选项在其他版本中也可用。

### 选项：`ssl`

启用或禁用与此插件的web服务器的加密 SSL/TLS（HTTPS）连接。
将其设置为 `true` 以加密通信，否则为 `false`。
请注意，如果您将此设置为 `true`，您还必须生成用于加密的密钥和证书文件。例如，可以使用 [Let's Encrypt](https://www.home-assistant.io/addons/lets_encrypt/) 或 [自签名证书](https://www.home-assistant.io/docs/ecosystem/certificates/tls_self_signed_certificate/)。

### 选项：`certfile`

要用于 SSL 的证书文件。如果该文件不存在，插件启动将失败。

**注意**：该文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认设置。

### 选项：`keyfile`

要用于 SSL 的私钥文件。如果该文件不存在，插件启动将失败。

**注意**：该文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认设置。

### 选项：`leave_front_door_open`

将此选项添加到插件配置中可以通过将其设置为 `true` 来禁用身份验证。

### 选项：`relative_url`

在相对 URL 下托管 ESPHome 仪表板，以便可以集成到现有的网络代理中，如在相对 URL 下的 NGINX。默认为 `/`。

### 选项：`status_use_ping`

默认情况下，仪表板使用 mDNS 检查节点是否在线。除非您的路由器支持 mDNS 转发或 avahi，否则无法跨子网工作。

将此设置为 `true` 将使 ESPHome 使用 ICMP ping 请求来获取节点状态。如果所有节点即使在连接时也始终显示离线状态，请使用此选项。

### 选项：`streamer_mode`

如果设置为 `true`，这将启用流模式，使 ESPHome 隐藏所有潜在的私人信息。例如 WiFi (B)SSIDs（可能被用来找到您的位置）、用户名等。请注意，您需要在 YAML 文件中使用 `!secret` 标签，以防止这些内容在编辑和验证时显示出来。