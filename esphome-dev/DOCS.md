# ESPHome 开发者附加组件

这是 ESPHome 附加组件的 **开发** 版本。

要部署生产节点，请使用主流版本的附加组件。

该附加组件使用 ESPHome 的一个版本，该版本每天在 UTC 时间 02:00 自动构建，并用于测试开发中的组件。请参见下面的 `esphome_fork` 配置以正确配置附加组件。更新配置后，确保重新构建镜像。

## 配置

**注意**：_在更改配置时，请记得重新启动附加组件。_

### 选项： `esphome_fork`

从一个分叉或分支安装 ESPHome。
例如，要测试一个拉取请求，请使用 `pull/XXXX/head`，其中 `XXXX` 是 PR 编号，
或者您可以指定分叉所有者的用户名和分支 `username:branch`，这
假设存储库仍命名为 `esphome`。

如果您需要在图像更新之前测试开发分支上的最新提交，可以在此处输入 `dev`。

请注意，您使用的分叉或分支 **必须** 与 ESPHome 开发版本保持最新，
否则附加组件 **将无法启动**。

## 一般 ESPHome 附加组件配置

一般选项在其他版本中也可用。

### 选项： `ssl`

启用或禁用与该附加组件的 Web 服务器进行加密的 SSL/TLS (HTTPS) 连接。
将其设置为 `true` 以加密通信，设置为 `false` 则不加密。
请注意，如果您将其设置为 `true`，还必须生成用于加密的密钥和证书
文件。例如使用 [Let's Encrypt](https://www.home-assistant.io/addons/lets_encrypt/)
或 [自签名证书](https://www.home-assistant.io/docs/ecosystem/certificates/tls_self_signed_certificate/)。

### 选项： `certfile`

用于 SSL 的证书文件。如果此文件不存在，附加组件启动将失败。

**注意**：文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认路径。

### 选项： `keyfile`

用于 SSL 的私钥文件。如果此文件不存在，附加组件启动将失败。

**注意**：文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认路径。

### 选项： `leave_front_door_open`

将此选项添加到附加组件配置中允许您通过将其设置为 `true` 来禁用
身份验证。

### 选项： `relative_url`

在相对 URL 下托管 ESPHome 仪表板，以便可以集成
到现有的 Web 代理如 NGINX 下的相对 URL 中。默认值为 `/`。

### 选项： `status_use_ping`

默认情况下，仪表板使用 mDNS 检查节点是否在线。此方法
在子网之间不起作用，除非您的路由器支持 mDNS 转发或 avahi。

将此设置为 `true` 将使 ESPHome 使用 ICMP ping 请求来获取节点状态。如果所有节点即使连接时也始终显示离线状态，请使用此设置。

### 选项： `streamer_mode`

如果设置为 `true`，这将启用流模式，使 ESPHome 隐藏所有
潜在的私人信息。例如 WiFi (B)SSIDs（可能用于定位）、用户名等。请注意，您需要在 YAML 文件中使用
`!secret` 标签以防止这些信息在编辑和验证时显示。