# ESPHome Add-on
## 安装

这个 add-on 的安装过程非常直接，与安装任何其他 Home Assistant add-on 没有区别。

1. 在 Supervisor add-on 商店中搜索“ESPHome” add-on。
2. 点击安装以下载 add-on 并在你的机器上解压它。这可能需要一些时间。
3. 可选：如果你正在使用 SSL/TLS 证书并希望加密与这个 add-on 的通信，请在 `ssl` 字段中输入 `true`，并相应地设置 `fullchain` 和 `certfile` 选项。
4. 启动 add-on，检查 add-on 的日志以查看是否一切顺利。
5. 点击“打开 Web UI”以打开 ESPHome 仪表板。系统会要求你输入 Home Assistant 凭据 - ESPHome 使用 Home Assistant 的认证系统来登录。

你可以在 https://esphome.io/ 查看ESPHome 文档。

## 配置

**注意**：_更改配置时请记得重启 add-on。_

示例 add-on 配置：

```json
{
  "ssl": false,
  "certfile": "fullchain.pem",
  "keyfile": "privkey.pem"
}
```

### 选项：`ssl`

启用或禁用加密的 SSL/TLS (HTTPS) 连接到此 add-on 的 Web 服务器。
设置为 `true` 以加密通信，否则设置为 `false`。
请注意，如果你将此设置为 `true`，你必须生成密钥和证书文件进行加密。例如使用 [Let's Encrypt](https://www.home-assistant.io/addons/lets_encrypt/)
或 [自签名证书](https://www.home-assistant.io/docs/ecosystem/certificates/tls_self_signed_certificate/)。

### 选项：`certfile`

用于 SSL 的证书文件。如果此文件不存在，add-on 启动将失败。

**注意**：文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认路径。

### 选项：`keyfile`

用于 SSL 的私钥文件。如果此文件不存在，add-on 启动将失败。

**注意**：文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认路径。

### 选项：`leave_front_door_open`

将此选项添加到 add-on 配置中，允许你通过设置为 `true` 来禁用认证。

### 选项：`relative_url`

在相对 URL 下托管 ESPHome 仪表板，以便它可以集成到现有的 Web 代理（如 NGINX）的相对 URL 下。默认值为 `/`。

### 选项：`status_use_ping`

默认情况下，仪表板使用 mDNS 来检查节点是否在线。如果不在同一子网，除非你的路由器支持 mDNS 转发或 avahi，否则这不起作用。

将此设置为 `true` 将使 ESPHome 使用 ICMP ping 请求来获取节点状态。如果所有节点即使在连接时也总是显示离线状态，请使用此选项。

### 选项：`streamer_mode`

如果设置为 `true`，这将启用 streamer 模式，使 ESPHome 隐藏所有潜在的个人隐私信息。例如 WiFi (B) SSID（这些可能被用来找到你的位置）、用户名等。请注意，你需要在你的 YAML 文件中使用 `!secret` 标签来阻止这些信息在编辑和验证时显示。