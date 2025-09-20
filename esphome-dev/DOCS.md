# ESPHome DEV 添加组件

这是 ESPHome 添加组件的**开发**版本。

要部署生产节点，请使用主流发布的添加组件。

该添加组件使用每天凌晨02:00 UTC自动构建的 ESPHome 版本，用于测试开发中的组件。有关配置 `esphome_fork` 的正确配置，请参阅下方的 `esphome_fork` 配置。一旦更新配置，请确保重新构建镜像。

## 配置

**注意**: _更改配置时请记得重启添加组件。_

### 选项: `esphome_fork`

从分支或分支安装 ESPHome。
例如，要测试一个拉取请求，使用 `pull/XXXX/head`，其中 `XXXX` 是 PR 号，
或者你可以指定分支所有者的用户名和分支 `username:branch`，假设存储库仍然命名为 `esphome`。

如果你需要在镜像更新之前在开发分支上测试最新提交，你可以在其中输入 `dev`。

请注意，你正在使用的分支或分支**必须**与 ESPHome 开发同步，
否则添加组件**将不会启动**。


## 一般 ESPHome 添加组件配置

常规选项也适用于其他版本。

### 选项: `ssl`

启用或禁用此添加组件的 Web 服务器到加密 SSL/TLS (HTTPS) 连接。
设置为 `true` 以加密通信，否则设置为 `false`。
请注意，如果你将此设置为 `true`，你也必须生成加密的密钥和证书文件。
例如，使用 [Let's Encrypt](https://www.home-assistant.io/addons/lets_encrypt/)
或 [自签名证书](https://www.home-assistant.io/docs/ecosystem/certificates/tls_self_signed_certificate/)。

### 选项: `certfile`

用于 SSL 的证书文件。如果此文件不存在，添加组件启动将失败。

**注意**: 文件**必须**存储在 `/ssl/`，这是 Home Assistant 的默认路径。

### 选项: `keyfile`

用于 SSL 的私钥文件。如果此文件不存在，添加组件启动将失败。

**注意**: 文件**必须**存储在 `/ssl/`，这是 Home Assistant 的默认路径。

### 选项: `leave_front_door_open`

将此选项添加到添加组件配置中，允许你通过设置为 `true` 来禁用身份验证。

### 选项: `relative_url`

在相对 URL 下托管 ESPHome 仪表板，以便它可以集成到现有的 Web 代理（如 NGINX）下。默认为 `/`。

### 选项: `status_use_ping`

默认情况下，仪表板使用 mDNS 来检查节点是否在线。如果路由器不支持 mDNS 转发或 avahi，则这在子网之间不起作用。

将此设置为 `true` 将使 ESPHome 使用 ICMP ping 请求来获取节点状态。如果所有节点即使在连接时也始终显示离线状态，请使用此选项。

### 选项: `streamer_mode`

如果设置为 `true`，这将启用流模式，使 ESPHome 隐藏所有潜在的私人信息。例如 WiFi (B)SSID（可能用于找到您的位置）、用户名等。请注意，您需要在 YAML 文件中使用 `!secret` 标签来阻止这些在编辑和验证时显示出来。