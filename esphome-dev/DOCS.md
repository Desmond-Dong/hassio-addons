# ESPHome DEV add on

这是 **开发** 版本的 ESPHome add on。

要部署生产节点，请使用主流发布的 add on。

该 add on 使用的是每天凌晨02:00 UTC自动构建的 ESPHome 版本，用于测试开发中的组件。有关正确配置 add on 的信息，请参阅下方的 `esphome_fork` 配置。一旦您更新了配置，请确保重新构建镜像。

## 配置

**注意**: _更改配置时，请记得重启 add-on。_

### 选项: `esphome_fork`

从分支或fork中安装 ESPHome。
例如，要测试一个pull请求，使用 `pull/XXXX/head`，其中 `XXXX` 是PR编号；
或者您可以指定fork所有者的用户名和分支 `username:branch`，前提是仓库仍然命名为 `esphome`。

如果您需要在镜像更新前测试dev分支上的最新提交，您可以将 `dev` 输入此处。

请注意，您正在使用的 fork 或分支 **必须** 与 ESPHome dev 保持最新，否则 add-on **将不会启动**。

## 一般 ESPHome add on 配置

一般选项也适用于其他版本。

### 选项: `ssl`

启用或禁用到此 add-on 的网页服务器上的加密 SSL/TLS (HTTPS) 连接。
将其设置为 `true` 以加密通信，否则设置为 `false`。
请注意，如果您将此设置为 `true`，则必须生成加密所需的密钥和证书文件。例如，使用 [Let's Encrypt](https://www.home-assistant.io/addons/lets_encrypt/)
或 [自签名证书](https://www.home-assistant.io/docs/ecosystem/certificates/tls_self_signed_certificate/)。

### 选项: `certfile`

用于 SSL 的证书文件。如果此文件不存在，add-on 启动将失败。

**注意**: 文件 **必须** 存储在 `/ssl/` 中，这是 Home Assistant 的默认设置

### 选项: `keyfile`

用于 SSL 的私钥文件。如果此文件不存在，add-on 启动将失败。

**注意**: 文件 **必须** 存储在 `/ssl/` 中，这是 Home Assistant 的默认设置

### 选项: `leave_front_door_open`

将此选项添加到 add-on 配置中，允许您通过将其设置为 `true` 来禁用身份验证。

### 选项: `relative_url`

在相对 URL 下托管 ESPHome 仪表板，以便它可以集成到现有的网页代理（如 NGINX）中，使用相对 URL。默认为 `/`。

### 选项: `status_use_ping`

默认情况下，仪表板使用 mDNS 来检查节点是否在线。如果您的路由器不支持 mDNS 转发或 avahi，则此方法无法跨子网工作。

将其设置为 `true` 将使 ESPHome 使用 ICMP ping 请求来获取节点状态。如果所有节点即使连接时也总是显示离线状态，请使用此选项。

### 选项: `streamer_mode`

如果设置为 `true`，这将启用流模式，使 ESPHome 隐藏所有可能包含私人信息的内容。例如 WiFi (B)SSID（可用于找到您的位置）、用户名等。请注意，您需要在您的 YAML 文件中使用 `!secret` 标签，以防止在编辑和验证时显示这些信息。