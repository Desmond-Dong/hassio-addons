# ESPHome 附加组件
## 安装

安装此附加组件非常简单，与安装任何其他 Home Assistant 附加组件没有区别。

1. 在 Supervisor 附加组件商店中搜索“ESPHome”附加组件。
2. 按下安装以下载附加组件并在您的机器上解压。这可能需要一些时间。
3. 可选：如果您正在使用 SSL/TLS 证书并希望加密与该附加组件的通信，请在 `ssl` 字段中输入 `true` 并相应地设置 `fullchain` 和 `certfile` 选项。
4. 启动附加组件，检查附加组件的日志以查看是否一切正常。
5. 点击“打开 Web UI”以打开 ESPHome 仪表板。您将被要求输入 Home Assistant 凭据 - ESPHome 使用 Home Assistant 的身份验证系统让您登录。

您可以在 https://esphome.io/ 查看 ESPHome 文档。

## 配置

**注意**：_更改配置后请记得重启附加组件。_

附加组件配置示例：

```json
{
  "ssl": false,
  "certfile": "fullchain.pem",
  "keyfile": "privkey.pem"
}
```

### 选项：`ssl`

启用或禁用对该附加组件的 web 服务器的加密 SSL/TLS (HTTPS) 连接。
设置为 `true` 以加密通信，设置为 `false` 则不加密。
请注意，如果将此设置为 `true`，您还必须生成密钥和证书文件以用于加密。可以使用 [Let's Encrypt](https://www.home-assistant.io/addons/lets_encrypt/) 或 [自签名证书](https://www.home-assistant.io/docs/ecosystem/certificates/tls_self_signed_certificate/)。

### 选项：`certfile`

要用于 SSL 的证书文件。如果此文件不存在，附加组件启动将失败。

**注意**：该文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认位置。

### 选项：`keyfile`

要用于 SSL 的私钥文件。如果此文件不存在，附加组件启动将失败。

**注意**：该文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认位置。

### 选项：`leave_front_door_open`

将此选项添加到附加组件配置中允许您通过将其设置为 `true` 来禁用身份验证。

### 选项：`relative_url`

在相对 URL 下托管 ESPHome 仪表板，以便可以集成到现有的 Web 代理（如 NGINX）中的相对 URL。默认为 `/`。

### 选项：`status_use_ping`

默认情况下，仪表板使用 mDNS 检查节点是否在线。如果您的路由器不支持 mDNS 转发或 avahi，则此方法不适用于子网之间。

将此设置为 `true` 将使 ESPHome 使用 ICMP ping 请求来获取节点状态。如果所有节点始终显示离线状态，即使它们已连接，请使用此选项。

### 选项：`streamer_mode`

如果设置为 `true`，则会启用流模式，这使 ESPHome 隐藏所有潜在的私人信息。例如 WiFi (B)SSIDs（可能用于查找您所在的位置）、用户名等。请注意，在您的 YAML 文件中，您需要使用 `!secret` 标签以防止这些信息在编辑和验证时显示。