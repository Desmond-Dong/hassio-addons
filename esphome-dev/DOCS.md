# ESPHome DEV 添加组件

这是 **开发** 版本的 ESPHome 添加组件。

要部署生产节点，请使用主流发布的添加组件。

该添加组件使用的是每天凌晨02:00 UTC自动构建的 ESPHome 版本，用于测试开发中的组件。请参考下方的 `esphome_fork` 配置以正确配置该添加组件。一旦您更新了配置，请确保重新构建镜像。

## 配置

**注意**: _在配置更改时，请记得重启添加组件。_

### 选项: `esphome_fork`

从分支或fork中安装 ESPHome。
例如，要测试一个pull请求，使用 `pull/XXXX/head`，其中 `XXXX` 是PR编号，
或者您可以指定fork所有者的用户名和分支 `username:branch`，假设存储库名称仍然是 `esphome`。

如果您需要在镜像更新前在开发分支上测试最新提交，您可以在其中输入 `dev`。

请注意，您正在使用的分支或fork **必须** 与 ESPHome 开发版本保持最新，
否则添加组件 **将不会启动**。

## 一般 ESPHome 添加组件配置

一般选项在其他版本中也可用。

### 选项: `ssl`

启用或禁用对此添加组件的Web服务器的加密SSL/TLS（HTTPS）连接。
设置为 `true` 以加密通信，否则设置为 `false`。
请注意，如果您将此设置为 `true`，则必须生成加密所需的密钥和证书文件。
例如，使用 [Let's Encrypt](https://www.home-assistant.io/addons/lets_encrypt/)
或 [自签名证书](https://www.home-assistant.io/docs/ecosystem/certificates/tls_self_signed_certificate/)。

### 选项: `certfile`

用于SSL的证书文件。如果此文件不存在，添加组件启动将失败。

**注意**: 文件 **必须** 存储在 `/ssl/`，这是 Home Assistant 的默认路径

### 选项: `keyfile`

用于SSL的私钥文件。如果此文件不存在，添加组件启动将失败。

**注意**: 文件 **必须** 存储在 `/ssl/`，这是 Home Assistant 的默认路径

### 选项: `leave_front_door_open`

将此选项添加到添加组件配置中，允许您通过将其设置为 `true` 来禁用身份验证。

### 选项: `relative_url`

在相对URL下托管 ESPHome 仪表板，以便它可以集成到现有的Web代理（如 NGINX）的相对URL下。默认为 `/`。

### 选项: `status_use_ping`

默认情况下，仪表板使用 mDNS 来检查节点是否在线。这在子网之间不起作用，除非您的路由器支持 mDNS 转发或 avahi。

将此设置为 `true` 将使 ESPHome 使用 ICMP ping 请求来获取节点状态。如果所有节点即使连接时也总是显示离线状态，请使用此选项。

### 选项: `streamer_mode`

如果设置为 `true`，这将启用流模式，使 ESPHome 隐藏所有可能包含隐私信息的内容。例如 WiFi (B)SSID（可用于找到您的位置）、用户名等。
请注意，您需要在您的 YAML 文件中使用 `!secret` 标签来阻止这些内容在编辑和验证时显示。