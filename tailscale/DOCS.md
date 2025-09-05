# Home Assistant 社区插件：Tailscale

Tailscale 是一个零配置 VPN，可以在几分钟内安装在任何设备上，包括您的 Home Assistant 实例。

在您的服务器、计算机和云实例之间创建一个安全的网络。即使它们被防火墙或子网隔开，Tailscale 也能正常工作。Tailscale 会为您管理防火墙规则，并在您所在的任何地方工作。

## 前置条件

要使用此插件，您需要有一个 Tailscale 账户。

对于个人和业余项目，使用它是免费的，每个用户账户最多可以支持 100 个客户端/设备。您可以使用您的 Google、Microsoft 或 GitHub 账户在以下网址注册：

<https://login.tailscale.com/start>

您也可以在插件安装过程中创建账户，但了解稍后需要去哪里会很有帮助。

## 安装

1. 点击 Home Assistant 下的“我的”按钮，在您的 Home Assistant 实例上打开插件。

   [![在您的 Home Assistant 实例中打开此插件][addon-badge]][addon]

1. 点击“安装”按钮以安装插件。
1. 启动“Tailscale”插件。
1. 检查“Tailscale”插件的日志，查看是否一切顺利。
1. 打开“Tailscale”插件的 Web UI，完成身份验证并将您的 Home Assistant 实例与您的 Tailscale 账户关联。
   **注意**：某些浏览器可能无法与此步骤配合使用。建议在桌面或笔记本电脑上使用 Chrome 浏览器完成此步骤。
1. 再次检查“Tailscale”插件的日志，查看是否一切顺利。
1. 完成！

## 配置

此插件几乎没有任何额外的配置选项用于插件本身。

但是，在登录 Tailscale 时，您可以直接从他们的界面配置您的 Tailscale 网络。

<https://login.tailscale.com/>

插件暴露了“出口节点”功能，您可以从您的 Tailscale 账户启用这些功能。此外，如果 Supervisor 管理您的网络（这是默认设置），插件也将向 Tailscale 广告您子网的所有支持接口的路由。

考虑禁用密钥过期，以避免失去与您的 Home Assistant 设备的连接。有关更多信息，请参阅 [密钥过期][tailscale_info_key_expiry]。

```yaml
accept_dns: true
accept_routes: true
advertise_exit_node: true
advertise_connector: true
advertise_routes:
  - 192.168.1.0/24
  - fd12:3456:abcd::/64
log_level: info
login_server: "https://controlplane.tailscale.com"
share_homeassistant: disabled
share_on_port: 443
snat_subnet_routes: true
stateful_filtering: false
tags:
  - tag:example
  - tag:homeassistant
taildrop: true
userspace_networking: true
```

> [!NOTE]
> 部分配置选项也通过 Web UI 在 Tailscale 的 Web 界面上可用，但它们在那里是只读的。您无法通过 Web UI 修改它们，因为所有在那里所做的更改在插件重新启动时都会丢失。

### 选项：`accept_dns`

如果您在这个设备上遇到 MagicDNS 问题并希望禁用它，您可以使用此选项。

如果没有设置，此选项默认启用。

如果您在同一台机器上运行类似 Pi-hole 或 AdGuard Home 的服务，MagicDNS 可能会导致问题。在这种情况下，禁用 `accept_dns` 将有助于解决问题。您仍然可以在网络上的其他设备上使用 MagicDNS，方法是向您的 Pi-hole 或 AdGuard Home 添加 `100.100.100.100` 作为 DNS 服务器。

### 选项：`accept_routes`

此选项允许您接受您尾网中其他节点广告的子网路由。

更多信息：[子网路由器][tailscale_info_subnets]

如果没有设置，此选项默认启用。

### 选项：`advertise_exit_node`

此选项允许您将此 Tailscale 实例广告为出口节点。

通过将网络上的设备设置为出口节点，您可以使用它按需路由所有公共互联网流量，就像消费型 VPN 一样。

更多信息：[出口节点][tailscale_info_exit_nodes]

如果没有设置，此选项默认启用。

### 选项：`advertise_connector`

此选项允许您将此 Tailscale 实例广告为应用连接器。

当您使用应用连接器时，您指定您希望在尾网上可访问的应用程序，以及这些应用程序的域名。然后，该应用程序的所有流量都将强制通过尾网到一个运行应用连接器的节点，然后再出站到目标域名。这对于应用程序具有 IP 地址白名单的情况很有用：应用连接器节点的 IP 地址可以添加到白名单中，并且尾网上的所有节点都将使用该 IP 地址进行流量出站。

更多信息：[应用连接器][tailscale_info_app_connectors]

如果没有设置，此选项默认启用。

### 选项：`advertise_routes`

此选项允许您向尾网上的其他客户端广告到子网（在您的设备连接的网络中可访问）的路由。

通过将子网路由的 IP 地址和掩码添加到列表中，您可以使用它来使这些子网上的设备在尾网内部可访问。

如果您想禁用此选项，请在配置中指定空列表（`[]` 在 YAML 中）。

更多信息：[子网路由器][tailscale_info_subnets]

如果没有设置，插件默认将向所有支持接口上的您的子网广告路由。

### 选项：`log_level`

可选地，在插件的日志中启用 tailscaled 调试消息。仅在您正在排除故障时才打开它，因为 Tailscale 的守护进程非常健谈。如果 `log_level` 设置为 `info` 或更严重的级别，插件也将选择退出客户端日志上传到 log.tailscale.io。

`log_level` 选项控制插件的日志输出级别，可以更改为更详细或更简洁，这可能有助于您处理未知问题。可能的值有：

- `trace`：显示每个细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `notice`：正常但重要的事件。
- `warning`：异常情况，但不是错误。
- `error`：运行时错误，不需要立即采取行动。
- `fatal`：发生了严重错误。插件变得无法使用。

请注意，每个级别都会自动包含更严重级别的日志消息，例如 `debug` 也显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐设置，除非您正在排除故障。

### 选项：`login_server`

此选项允许您指定自定义控制服务器，而不是默认的 (`https://controlplane.tailscale.com`)。如果您正在运行自己的 Tailscale 控制服务器，例如自托管的 [Headscale] 实例，这很有用。

### 选项：`share_homeassistant`

此选项允许您启用 Tailscale Serve 或 Funnel 功能，在您的尾网或互联网上向您的 Home Assistant 实例提供有效证书。

如果没有设置，此选项默认禁用。

Tailscale 可以在您的尾网域内为您的 Home Assistant 实例提供 TLS 证书。

这可以防止浏览器警告您的 Home Assistant 实例的 HTTP URL 看起来未加密（浏览器不知道 Tailscale 节点之间的连接是使用端到端加密保护的）。

使用 Tailscale Serve 功能，您可以使用提供的证书在尾网内从已连接到尾网的设备访问您的 Home Assistant 实例。

使用 Tailscale Funnel 功能，您不仅可以在尾网内，还可以使用您的 Tailscale 域从更广泛的互联网使用提供的证书访问您的 Home Assistant 实例（例如 `https://homeassistant.tail1234.ts.net`），这些设备**未安装 Tailscale VPN 客户端**（例如，在通用手机、平板电脑和笔记本电脑上）。

**客户端** &#8658; _互联网_ &#8658; **Tailscale Funnel** (TCP 代理) &#8658; **VPN** &#8658; **Tailscale Serve** (HTTPS 代理) &#8594; **HA** (HTTP 服务器)

更多信息：[启用 HTTPS][tailscale_info_https]、[Tailscale Serve][tailscale_info_serve]、[Tailscale Funnel][tailscale_info_funnel]。

1. 配置 Home Assistant 以通过 HTTP 连接访问（这是默认设置）。有关更多信息，请参阅 [HTTP 集成文档][http_integration]。如果您仍然想使用另一个 HTTPS 连接访问 Home Assistant，请使用反向代理插件。

1. Home Assistant 默认会阻止来自反向代理（如 Tailscale Serve）的请求。要启用它，请将以下行添加到您的 `configuration.yaml` 中，不要更改任何内容：

   ```yaml
   http:
     use_x_forwarded_for: true
     trusted_proxies:
       - 127.0.0.1
   ```

1. 导航到管理控制台的 [DNS 页面][tailscale_dns]：
   - 选择一个尾网名称。

   - 如果尚未启用，请启用 MagicDNS。

   - 在 HTTPS 证书部分，点击启用 HTTPS。

1. 可选地，如果您想使用 Tailscale Funnel，请导航到管理控制台的 [访问控制页面][tailscale_acls]：
   - 向尾网策略文件添加所需的 `funnel` 节点属性。有关更多信息，请参阅 [尾网策略文件要求][tailscale_info_funnel_policy_requirement]。

1. 重新启动插件。

**注意**：初始设置后，域名可能需要长达 10 分钟才能公开可用。

**注意**：您不应使用以前用于访问 Home Assistant 的 URL 中的端口号。Tailscale Serve 和 Funnel 在默认的 HTTPS 端口 443（或选项 `share_on_port` 中配置的端口）上工作。

**注意**：如果您遇到奇怪的浏览器行为或奇怪的错误消息，请尝试清除所有与站点相关的 cookie，清除所有浏览器缓存，并重新启动浏览器。

### 选项：`share_on_port`

此选项允许您指定 Tailscale Serve 和 Funnel 功能将用于在尾网和互联网上显示您的 Home Assistant 实例的端口。

Tailscale 仅允许端口 443、8443 和 10000。

如果没有设置，默认使用端口 443。

### 选项：`snat_subnet_routes`

此选项允许子网设备看到从子网路由器发起的流量，这简化了路由配置。

如果没有设置，此选项默认启用。

要支持高级 [站点到站点网络][tailscale_info_site_to_site]（例如，以遍历多个网络），您可以禁用此功能，并按照 [站点到站点网络][tailscale_info_site_to_site] 指南中的步骤操作（注意：插件已经处理了“IP 地址转发”和“将 MSS 限制为 MTU”）。