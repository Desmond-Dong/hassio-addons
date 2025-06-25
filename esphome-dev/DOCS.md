# ESPHome 开发版附加组件

这是 ESPHome 附加组件的 **开发** 版本。

要部署生产节点，请使用主流发布附加组件。

该附加组件使用自动构建的 ESPHome 版本，每天在 UTC 02:00 生成，旨在测试正在开发中的组件。请参见下面的 `esphome_fork` 配置以正确配置该附加组件。一旦您更新了配置，请确保重新构建映像。

## 配置

**注意**：_更改配置时，请记得重启附加组件。_

### 选项: `esphome_fork`

从一个 fork 或分支安装 ESPHome。
例如，要测试一个拉取请求，请使用 `pull/XXXX/head`，其中 `XXXX` 是 PR 编号，
或者您可以指定 fork 所有者的用户名和分支 `username:branch`，这假设库的名称仍为 `esphome`。

如果您需要在映像更新之前测试开发分支的最新提交，可以在此处输入 `dev`。

请注意，您使用的 fork 或分支 **必须** 与 ESPHome 开发保持最新，否则附加组件 **将无法启动**。

## 通用 ESPHome 附加组件配置

通用选项也可用于其他版本。

### 选项: `ssl`

启用或禁用与此附加组件的网络服务器的加密 SSL/TLS (HTTPS) 连接。
将其设置为 `true` 以加密通信，否则设置为 `false`。
请注意，如果将其设置为 `true`，您还必须生成密钥和证书文件以进行加密。例如，可以使用 [Let's Encrypt](https://www.home-assistant.io/addons/lets_encrypt/) 或 [自签名证书](https://www.home-assistant.io/docs/ecosystem/certificates/tls_self_signed_certificate/)。

### 选项: `certfile`

用于 SSL 的证书文件。如果此文件不存在，附加组件将无法启动。

**注意**：该文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认位置。

### 选项: `keyfile`

用于 SSL 的私钥文件。如果此文件不存在，附加组件将无法启动。

**注意**：该文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认位置。

### 选项: `leave_front_door_open`

将此选项添加到附加组件配置中允许您通过将其设置为 `true` 来禁用身份验证。

### 选项: `relative_url`

在相对 URL 下托管 ESPHome 控制面板，以便它可以集成到现有的网络代理（如 NGINX）下的相对 URL。默认为 `/`。

### 选项: `status_use_ping`

默认情况下，控制面板使用 mDNS 检查节点是否在线。如果您的路由器支持 mDNS 转发或 avahi，这在子网之间是不可行的。

将此设置为 `true` 将使 ESPHome 使用 ICMP ping 请求来获取节点状态。如果所有节点在连接时仍始终显示离线状态，请使用此选项。

### 选项: `streamer_mode`

如果设置为 `true`，这将启用流式模式，使 ESPHome 隐藏所有潜在的私人信息。例如 WiFi (B)SSID（可能被用于查找您的位置）、用户名等。请注意，您需要在 YAML 文件中使用 `!secret` 标签，才能在编辑和验证时防止这些信息出现。