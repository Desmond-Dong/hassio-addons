# ESPHome 开发版插件

这是 ESPHome 插件的**开发**版本。

要部署生产节点，请使用主流发布的插件。

该插件使用的是每天凌晨 02:00 UTC 自动构建的 ESPHome 版本，用于测试开发中的组件。请参考下方的 `esphome_fork` 配置来正确配置插件。一旦更新配置，请确保重新构建镜像。

## 配置

**注意**：_配置更改时，请记得重启插件。_

### 选项：`esphome_fork`

从分支或分支安装 ESPHome。
例如，要测试一个拉取请求，使用 `pull/XXXX/head`，其中 `XXXX` 是 PR 编号，
或者您可以指定分支所有者的用户名和分支 `username:branch`，假设仓库名称仍然是 `esphome`。

如果您需要在镜像更新前测试开发分支上的最新提交，可以在此处输入 `dev`。

请注意，您正在使用的分支或分支**必须**与 ESPHome 开发版保持最新，
否则插件**将不会启动**。

## 一般 ESPHome 插件配置

常规选项也适用于其他版本。

### 选项：`ssl`

启用或禁用加密的 SSL/TLS（HTTPS）连接到此插件的 Web 服务器。
将其设置为 `true` 以加密通信，`false` 否则。
请注意，如果您将其设置为 `true`，您还必须生成加密所需的密钥和证书文件。
例如，使用 [Let's Encrypt](https://www.home-assistant.io/addons/lets_encrypt/)
或 [自签名证书](https://www.home-assistant.io/docs/ecosystem/certificates/tls_self_signed_certificate/)。

### 选项：`certfile`

用于 SSL 的证书文件。如果此文件不存在，插件启动将失败。

**注意**：文件**必须**存储在 `/ssl/`，这是 Home Assistant 的默认路径。

### 选项：`keyfile`

用于 SSL 的私钥文件。如果此文件不存在，插件启动将失败。

**注意**：文件**必须**存储在 `/ssl/`，这是 Home Assistant 的默认路径。

### 选项：`leave_front_door_open`

在插件配置中添加此选项允许您通过将其设置为 `true` 来禁用身份验证。

### 选项：`relative_url`

在相对 URL 下托管 ESPHome 仪表板，以便它可以集成到现有的 Web 代理（如 NGINX）的相对 URL 下。默认值为 `/`。

### 选项：`status_use_ping`

默认情况下，仪表板使用 mDNS 来检查节点是否在线。这跨子网不起作用，除非您的路由器支持 mDNS 转发或 avahi。

将其设置为 `true` 将使 ESPHome 使用 ICMP ping 请求来获取节点状态。如果所有节点始终显示离线状态，即使它们已连接，请使用此选项。

### 选项：`streamer_mode`

如果设置为 `true`，这将启用流模式，使 ESPHome 隐藏所有潜在的私人信息。例如 WiFi (B)SSID（可能被用来定位您的位置）、用户名等。
请注意，您需要在 YAML 文件中使用 `!secret` 标签来防止这些信息在编辑和验证时显示。