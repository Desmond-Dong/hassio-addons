# Home Assistant 附加组件：Cloudflared

Cloudflared 通过安全隧道将您的 Home Assistant 实例连接到 Cloudflare 的域名或子域名。这使您可以在不打开路由器端口的情况下将 Home Assistant 实例和其他服务暴露到互联网。此外，您还可以利用 Cloudflare Zero Trust 进一步保护您的连接。

## 免责声明

请确保在使用此附加组件时遵守 [Cloudflare 自助订阅协议][cloudflare-sssa]。

## 初始设置

### 前提条件

1. 一个使用 Cloudflare 作为 DNS 的域名（例如 example.com）。如果您没有一个，请参见 [域名和 Cloudflare 设置][how-tos]。请注意，来自 **Freenom** 的域名已不再有效，因此您必须选择/迁移到其他注册商。
1. 如果您尚未完成，请为您的域名 [在 Cloudflare 中启用 Websockets][cloudflare-websockets]。
1. 在本地隧道（由附加组件管理）或远程隧道（在 Cloudflare 界面中管理）之间进行选择。[了解更多][addon-remote-or-local]。
1. 此附加组件应 [已安装][addon-installation] 但尚未启动。

完成前提条件后，请根据您选择的隧道类型继续下面的步骤。

### 本地隧道附加组件设置（推荐）

在以下步骤中，附加组件将自动创建一个 Cloudflare 隧道，以暴露您的 Home Assistant 实例。

如果您只想暴露其他服务，可以将 `external_hostname` 留空，并根据 [如下所述](#configuration) 设置 `additional_hosts`。

1. 按照 [如下所述](#configurationyaml) 在您的 Home Assistant 配置中配置 `http` 集成。
1. 将附加组件选项 `external_hostname` 设置为您想用于远程访问的域名/子域名，例如：`ha.example.com`。
1. 启动附加组件（这将覆盖任何匹配 `external_hostname` 或 `additional_hosts` 的现有 DNS 条目）。
1. 在新选项卡中粘贴附加组件日志中的 URL 以进行 Cloudflare 身份验证。
1. 通过远程 URL 访问您的 Home Assistant，无需端口，例如：`https://ha.example.com/`。

现在，您的 Cloudflare Teams 控制面板中应列出一个隧道。请查看下面的其他配置选项。

### 远程隧道附加组件设置（高级）

在以下步骤中，您将手动在 Zero Trust 控制面板中创建 Cloudflare 隧道，并将令牌提供给附加组件。

1. 按照 [如下所述](#configurationyaml) 在您的 Home Assistant 配置中配置 `http` 集成。
1. 按照 [此教程][addon-remote-tunnel] 在 Cloudflare Teams 控制面板中创建一个 Cloudflare 隧道。
1. 将附加组件选项 `tunnel_token` 设置为您的 [隧道令牌][create-remote-managed-tunnel]（将忽略所有其他配置）。
1. 启动附加组件，检查日志以确认一切正常。
1. 通过远程 URL 访问您的 Home Assistant，无需端口，例如：`https://ha.example.com/`。

您的隧道现在应与 Cloudflared 附加组件关联。所有配置更改应在 Cloudflare Teams 控制面板中进行。

## 配置

**这些配置选项仅适用于本地隧道设置**。使用远程隧道设置可以实现更高级的配置。

- [`external_hostname`](#option-external_hostname)
- [`additional_hosts`](#option-additional_hosts)
- [`tunnel_name`](#option-tunnel_name)
- [`catch_all_service`](#option-catch_all_service)
- [`nginx_proxy_manager`](#option-nginx_proxy_manager)
- [`use_builtin_proxy`](#option-use_builtin_proxy)
- [`post_quantum`](#option-post_quantum)
- [`run_parameters`](#option-run_parameters)
- [`log_level`](#option-log_level)

### 概述：附加组件配置

**注意**：_请记得在更改配置时重启附加组件。_

附加组件配置示例：

```yaml
external_hostname: ha.example.com
additional_hosts:
  - hostname: router.example.com
    service: http://192.168.1.1
  - hostname: website.example.com
    service: http://192.168.1.3:8080
```

**注意**：_这只是一个示例，请不要复制和粘贴！创建您自己的！_

### 选项：`external_hostname`

将 `external_hostname` 选项设置为您要用于访问 Home Assistant 的域名或子域名。

这是可选的，可以选择使用 `additional_hosts` 仅暴露其他服务。

**注意**：_隧道名称在您的 Cloudflare 账户中需要唯一。_

```yaml
external_hostname: ha.example.com
```

### 选项：`additional_hosts`

您可以使用 Cloudflare Tunnel 的内部反向代理定义 Home Assistant 之外的其他主机。这样，您还可以使用隧道访问其他系统，例如磁盘站、路由器或其他任何东西。

像用于 Home Assistant 的 `external_hostname` 选项一样，DNS 条目将自动创建在 Cloudflare 上。

将（可选的）`disableChunkedEncoding` 选项添加到主机名，以禁用分块传输编码。这在您运行 WSGI 服务器时很有用，例如 Proxmox。有关更多信息，请访问 [Cloudflare 文档][disablechunkedencoding]。

以下是三个额外主机的示例条目：

```yaml
additional_hosts:
  - hostname: router.example.com
    service: http://192.168.1.1
  - hostname: diskstation.example.com
    service: https://192.168.1.2:5001
  - hostname: website.example.com
    service: http://192.168.1.3:8080
    disableChunkedEncoding: true
```

**注意 1**：_如果您从列表中删除一个主机名，它将不再提供服务。尽管如此，您也应该手动从 Cloudflare 中删除 DNS 条目，因为它无法通过附加组件删除。_

**注意 2**：_如果您想完全删除 `additional_hosts` 选项，您必须在配置中添加一个空数组，如下所示：_

```yaml
additional_hosts: []
```

### 选项：`tunnel_name`

` tunnel_name` 选项允许您将隧道名称更改为不同于默认的 `homeassistant`。

**注意**：_隧道名称在您的 Cloudflare 账户中需要唯一。_

```yaml
tunnel_name: myHomeAssistant
```

### 选项：`catch_all_service`

如果您希望将所有未在 `external_hostname` 或 `additional_hosts` 中定义的主机名的请求转发，可以使用此选项并定义一个要转发的 URL。例如，这可以用于反向代理。

**注意**：_如果您希望将 HA 附加组件 [Nginx Proxy Manager][nginx_proxy_manager] 作为反向代理使用，您应该设置标志 `nginx_proxy_manager`（[见下文](#option-nginx_proxy_manager)）而不使用此选项。_

```yaml
catch_all_service: http://192.168.1.100
```

**注意**：_这仍将把您定义的 `external_hostname` 路由到 Home Assistant，以及任何潜在的 `additional_hosts` 路由到您在配置中定义的地方。任何其他传入流量将路由到定义的服务。_

为了通过隧道路由主机名，您必须在 Cloudflare 中为它们创建单独的 CNAME 记录，指向您的 `external_hostname` 或直接指向您可以从 `external_hostname` 的 CNAME 条目获得的隧道 URL。

或者，您可以通过添加一个 CNAME 记录并将名称设置为 `*` 来在 Cloudflare 中添加 [通配符 DNS 记录](https://blog.cloudflare.com/wildcard-proxy-for-everyone/)。

### 选项：`nginx_proxy_manager`

如果您希望将 Cloudflare Tunnel 与 [Nginx Proxy Manager][nginx_proxy_manager] 附加组件一起使用，可以通过设置此选项来实现。它将自动将 `catch_all_service` 设置为 Nginx Proxy Manager 的内部 URL。您不必在配置中添加选项 `catch_all_service`（如果您仍然添加，它将被忽略）。

```yaml
nginx_proxy_manager: true
```

**注意**：_与 `catch_all_service` 一样，这仍将把您定义的 `external_hostname` 路由到 Home Assistant，以及任何潜在的 `additional_hosts` 路由到您在配置中定义的地方。任何其他传入流量将路由到 Nginx Proxy Manager。_

为了通过隧道路由主机名，您必须在 Cloudflare 中为它们创建单独的 CNAME 记录，指向您的 `external_hostname` 或直接指向您可以从 `external_hostname` 的 CNAME 条目获得的隧道 URL。

或者，您可以通过添加一个 CNAME 记录并将名称设置为 `*` 来在 Cloudflare 中添加 [通配符 DNS 记录](https://blog.cloudflare.com/wildcard-proxy-for-everyone/)。

最后，您必须在 Nginx Proxy Manager 中设置您的代理主机并将它们转发到您喜欢的地方。

### 选项：`use_builtin_proxy`

如果启用，则与 Home Assistant 的连接将通过内置的 Nginx 代理进行。Nginx 是作为解决实时日志问题的临时解决方案而实现的。有关讨论，请参见 [#744](https://github.com/brenner-tobias/addon-cloudflared/discussions/744)。

**注意**：_此选项默认为启用。_

### 选项：`post_quantum`

如果您希望 Cloudflared 为隧道使用后量子密码学，请设置此标志。

**注意**：_当 `post_quantum` 被设置时，cloudflared 会限制自己使用 QUIC 传输进行隧道连接。这可能会导致一些用户出现问题。此外，它将仅允许后量子混合密钥交换，而不回落到非后量子连接。_

```yaml
post_quantum: true
```

### 选项：`run_parameters`

您可以使用此参数向 cloudflared 守护进程添加其他运行参数。请查看 [Cloudflare 文档][cloudflare-run_parameter] 以获取所有可用参数及其说明。

可以添加的有效参数包括：

- --​​edge-bind-address
- --edge-ip-version
- --grace-period
- --logfile
- --loglevel
- --pidfile
- --protocol
- --region
- --retries
- --tag
- --ha-connections

**注意**：_这些参数将添加到默认存在的参数 "no-autoupdate"、"metrics" 和 "loglevel" 中。此外，对于本地管理的隧道，"origincert" 和 "config" 被添加，而 "token" 被添加到远程管理的隧道中。您不能通过此选项覆盖这些参数。_

**注意**：_如果您正在使用需要路径的选项，可以将 /config 作为根路径。该路径可以通过例如 VS-code 附加组件通过 /addon_configs 访问。_

```yaml
run_parameters:
  - "--region=us"
  - "--protocol=http2"
  - "--loglevel=debug"
```

### 选项：`log_level`

`log_level` 选项控制附加组件的日志输出级别，可以更改为更详细或更简略，这在您处理未知问题时可能会很有用。

**注意**：_如果您想更改隧道本身的日志级别，可以使用 `run_parameters` 中的 `--loglevel` 选项。_

```yaml
log_level: debug
```

可能的值包括：

- `trace`：显示每个细节，如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：不合常规但不算错误的异常情况。
- `error`：运行时错误，不需要立即行动。
- `fatal`：发生了严重错误。附加组件变得不可用。

请注意，每个级别都会自动包括来自更严重级别的日志消息，例如，`debug` 也会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐设置，除非您正在进行故障排除。

## Home Assistant 配置

### configuration.yaml

由于 Home Assistant 阻止来自代理/反向代理的请求，您需要告诉实例允许来自 Cloudflared 附加组件的请求。该附加组件在本地运行，因此 HA 必须信任 Docker 网络。为此，请将以下行添加到您的 `/config/configuration.yaml` 中：

**注意**：_在这些行中无需调整任何内容，因为 Docker 网络的 IP 范围始终相同。_

```yaml
http:
  use_x_forwarded_for: true
  trusted_proxies:
    - 172.30.33.0/24
```

**如果您使用的是 HA 的非标准托管方法（例如 Proxmox），您可能需要在这里添加另一个 IP（范围）。在尝试连接后检查您的 HA 日志以找到正确的 IP。**

记得在更改配置时重启 Home Assistant。

如果您需要更改配置的帮助，请遵循 [高级配置教程][advancedconfiguration]。

## 附加组件 Wiki

有关更多高级 [操作指南][how-tos] 和 [故障排除部分][troubleshooting]，请访问 [GitHub 上的附加组件 Wiki][addon-wiki]。

## 作者和贡献者

该存储库的初始设置由 [Tobias Brenner][tobias] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2025 Tobias Brenner

特此免费授予任何获得本软件及相关文档文件（"软件"）副本的人，不受限制地处理该软件，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或出售该软件副本的权利，并允许向其提供软件的人这样做，但须遵守以下条件：

上述版权声明和本许可声明应包含在所有副本或实质性部分的 软件中。

软件是 "按原样" 提供的，未经任何种类的保证，无论是明示或暗示，包括但不限于对适销性、特定用途的适用性和非侵权的保证。在任何情况下，作者或版权持有人均不对因使用软件或与软件或其他交易有关的任何索赔、损害或其他责任承担责任，无论是在合同诉讼、侵权还是其他情况下。

[addon-installation]: https://github.com/brenner-tobias/addon-cloudflared#installation
[addon-remote-tunnel]: https://github.com/brenner-tobias/addon-cloudflared/wiki/How-tos#how-to-configure-remote-tunnels
[addon-remote-or-local]: https://github.com/brenner-tobias/addon-cloudflared/wiki/How-tos#local-vs-remote-managed-tunnels
[addon-wiki]: https://github.com/brenner-tobias/addon-cloudflared/wiki
[advancedconfiguration]: https://www.home-assistant.io/getting-started/configuration/
[cloudflare-sssa]: https://www.cloudflare.com/en-gb/terms/
[cloudflare-run_parameter]: https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/configure-tunnels/tunnel-run-parameters/
[cloudflare-websockets]: https://developers.cloudflare.com/network/websockets/
[contributors]: https://github.com/brenner-tobias/addon-cloudflared/graphs/contributors
[how-tos]: https://github.com/brenner-tobias/addon-cloudflared/wiki/How-tos
[nginx_proxy_manager]: https://github.com/hassio-addons/addon-nginx-proxy-manager
[tobias]: https://github.com/brenner-tobias
[troubleshooting]: https://github.com/brenner-tobias/addon-cloudflared/wiki/Troubleshooting
[disablechunkedencoding]: https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/configuration/configuration-file/ingress#disablechunkedencoding
[create-remote-managed-tunnel]: https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/#1-create-a-tunnel