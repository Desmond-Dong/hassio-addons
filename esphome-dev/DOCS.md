# ESPHome 开发版插件

这是 **开发** 版本的 ESPHome 插件。

要部署生产节点，请使用主流发布插件。

该插件使用每天在 UTC 时间 02:00 自动构建的 ESPHome 版本，用于测试正在开发的组件。请参见下面的 `esphome_fork` 配置，以正确配置插件。一旦更新配置，请确保重建镜像。

## 配置

**注意**: _请记得在配置更改时重启插件。_

### 选项: `esphome_fork`

从一个分支或派生版安装 ESPHome。
例如，要测试一个拉取请求，请使用 `pull/XXXX/head`，其中 `XXXX` 是 PR 编号，
或者您可以指定派生版所有者的用户名和分支 `username:branch`，这假设
仓库的名称仍为 `esphome`。

如果您需要在镜像更新之前测试开发分支上的最新提交，可以在此处输入 `dev`。

请注意，您正在使用的分支或派生版 **必须** 与 ESPHome 开发分支保持最新，
否则插件 **将无法启动**。

## 通用 ESPHome 插件配置

通用选项也适用于其他版本。

### 选项: `ssl`

启用或禁用与该插件的 Web 服务器的加密 SSL/TLS (HTTPS) 连接。
将其设置为 `true` 以加密通信，设置为 `false` 则不加密。
请注意，如果您将其设置为 `true`，您还必须为加密生成密钥和证书文件。
例如使用 [Let's Encrypt](https://www.home-assistant.io/addons/lets_encrypt/)
或 [自签名证书](https://www.home-assistant.io/docs/ecosystem/certificates/tls_self_signed_certificate/)。

### 选项: `certfile`

用于 SSL 的证书文件。如果该文件不存在，插件启动将失败。

**注意**: 文件必须存储在 `/ssl/`，这是 Home Assistant 的默认位置。

### 选项: `keyfile`

用于 SSL 的私钥文件。如果该文件不存在，插件启动将失败。

**注意**: 文件必须存储在 `/ssl/`，这是 Home Assistant 的默认位置。

### 选项: `leave_front_door_open`

将此选项添加到插件配置中可以通过将其设置为 `true` 来禁用身份验证。

### 选项: `relative_url`

在相对 URL 下托管 ESPHome 仪表板，以便可以集成到现有的 Web 代理（如 NGINX）中。默认值为 `/`。

### 选项: `status_use_ping`

默认情况下，仪表板使用 mDNS 检查节点是否在线。除非路由器支持 mDNS 转发或 avahi，否则在子网之间工作不正常。

将此设置为 `true` 将使 ESPHome 使用 ICMP ping 请求获取节点状态。如果所有节点即使连接时也始终显示离线状态，则使用此设置。

### 选项: `streamer_mode`

如果设置为 `true`，这将启用流模式，这使 ESPHome 隐藏所有潜在的私人信息。例如 WiFi (B)SSIDs（可能用于找到您的位置）、用户名等。请注意，您需要在 YAML 文件中使用 `!secret` 标签，以防止这些信息在编辑和验证时显示。