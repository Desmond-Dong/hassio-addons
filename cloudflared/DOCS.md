# Home Assistant 插件：Cloudflared

Cloudflared 通过安全的隧道将您的 Home Assistant 实例连接到 Cloudflare 的一个域或子域。这使您能够在不在路由器上打开端口的情况下，将您的 Home Assistant 实例和其他服务暴露到互联网。此外，您可以利用 Cloudflare Zero Trust 来进一步保护您的连接。

## 免责声明

在使用此插件时，请确保您遵守 [Cloudflare 自助订阅协议][cloudflare-sssa]。

## 初始设置

### 前提条件

1. 一个使用 Cloudflare 进行 DNS 的域名（例如 example.com）。如果您没有域名，请参见 [域名和 Cloudflare 设置][how-tos]。
   请注意，来自 **Freenom** 的域名不再有效，因此您必须选择 / 迁移到另一个注册商。
1. 如果您还没有这样做，请 [为您的域名在 Cloudflare 中激活 Websockets][cloudflare-websockets]。
1. 在本地隧道（由插件管理）或远程隧道（在 Cloudflare 的界面中管理）之间进行选择。 [了解更多][addon-remote-or-local]。
1. 此插件应已 [安装][addon-installation] 但尚未启动。

完成前提条件后，根据您选择的隧道类型进行以下操作。

### 本地隧道插件设置（推荐）

在以下步骤中，插件将自动创建一个 Cloudflare 隧道，以便暴露您的 Home Assistant 实例。

如果您只想暴露其他服务，可以将 `external_hostname` 留空，并将 `additional_hosts` 设置为 [如下](#configuration)。

1. 按 [如下](#configurationyaml) 配置您 Home Assistant 配置中的 `http` 集成。
1. 将 `external_hostname` 插件选项设置为您希望用于远程访问的域名/子域名，例如 `ha.example.com`。
1. 启动插件（这将覆盖任何与 `external_hostname` 或 `additional_hosts` 匹配的现有 DNS 条目）。
1. 在新标签页中粘贴插件日志中的 URL，以便与 Cloudflare 进行身份验证。
1. 通过远程 URL 访问您的 Home Assistant，没有端口，例如 `https://ha.example.com/`。

现在在您的 Cloudflare Teams 仪表板中应列出一个隧道。
请查看下面的其他配置选项。

### 远程隧道插件设置（高级）

在接下来的步骤中，您将手动在 Zero Trust Dashboard 中创建一个 Cloudflare 隧道，并将令牌提供给插件。

1. 按 [如下](#configurationyaml) 配置您 Home Assistant 配置中的 `http` 集成。
1. 在 Cloudflare Teams 仪表板中创建 Cloudflare 隧道，按照 [此如何做][addon-remote-tunnel]。
1. 将 `tunnel_token` 插件选项设置为您的 [隧道令牌][create-remote-managed-tunnel]（所有其他配置将被忽略）。
1. 启动插件，检查日志以确认一切如预期般进展。
1. 通过远程 URL 访问您的 Home Assistant，没有端口，例如 `https://ha.example.com/`。

您的隧道现在应与 Cloudflared 插件关联。任何配置更改应在 Cloudflare Teams 仪表板中进行。

## 配置

**这些配置选项仅适用于本地隧道设置**。使用远程隧道设置可以获得更高级的配置。

- [`external_hostname`](#option-external_hostname)
- [`additional_hosts`](#option-additional_hosts)
- [`tunnel_name`](#option-tunnel_name)
- [`catch_all_service`](#option-catch_all_service)
- [`nginx_proxy_manager`](#option-nginx_proxy_manager)
- [`use_builtin_proxy`](#option-use_builtin_proxy)
- [`post_quantum`](#option-post_quantum)
- [`run_parameters`](#option-run_parameters)
- [`log_level`](#option-log_level)

### 概述：插件配置

**注意**：_请记得在更改配置后重新启动插件。_

示例插件配置：

```yaml
external_hostname: ha.example.com
additional_hosts:
  - hostname: router.example.com
    service: http://192.168.1.1
  - hostname: website.example.com
    service: http://192.168.1.3:8080
```

**注意**：_这只是一个示例，不要复制粘贴！自己创建一个！_

### 选项： `external_hostname`

将 `external_hostname` 选项设置为您希望用于访问 Home Assistant 的域名或子域名。

这是可选的，`additional_hosts` 也可以用于仅暴露其他服务。

**注意**：_隧道名称在您的 Cloudflare 帐户中需要是唯一的。_

```yaml
external_hostname: ha.example.com
```

### 选项： `additional_hosts`

您可以使用 Cloudflare 隧道的内部反向代理来定义除了 Home Assistant 之外的其他主机。这样，您也可以使用隧道访问其他系统，例如磁盘阵列、路由器或其他任何东西。

与用于 Home Assistant 的 `external_hostname` 选项类似，DNS 条目将自动在 Cloudflare 中创建。

将（可选的）`disableChunkedEncoding` 选项添加到主机名，以禁用分块传输编码。如果您正在运行一个 WSGI 服务器，比如 Proxmox，这将很有用。请访问 [Cloudflare 文档][disablechunkedencoding] 获取更多信息。

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

**注意 1**：_如果您从列表中删除一个主机名，它将不再提供服务。但请您也手动从 Cloudflare 删除该 DNS 条目，因为插件无法删除。_

**注意 2**：_如果您想完全删除 `additional_hosts` 选项，您必须在配置中添加一个空数组，如下所示：_

```yaml
additional_hosts: []
```

### 选项： `tunnel_name`

`tunnel_name` 选项允许您将隧道名称更改为其他名称，而不是默认的 `homeassistant`。

**注意**：_隧道名称在您的 Cloudflare 帐户中需要是唯一的。_

```yaml
tunnel_name: myHomeAssistant
```

### 选项： `catch_all_service`

如果您希望将来自未在 `external_hostname` 或 `additional_hosts` 中定义的任何主机名的所有请求转发，可以使用此选项并定义一个转发的 URL。例如，这可以用于反向代理。

**注意**：_如果您想使用 HA 插件 [Nginx Proxy Manager][nginx_proxy_manager] 作为反向代理，您应该设置标志 `nginx_proxy_manager`（[见下](#option-nginx_proxy_manager)），而不要使用此选项。_

```yaml
catch_all_service: http://192.168.1.100
```

**注意**：_这仍将将您的定义的 `external_hostname` 路由到 Home Assistant，以及任何潜在的 `additional_hosts` 路由到您在配置中定义的位置。任何其他传入流量将被路由到定义的服务。_

为了通过隧道路由主机名，您必须在 Cloudflare 中为所有主机名创建各自的 CNAME 记录，指向您的 `external_hostname` 或直接指向您可以从 `external_hostname` 的 CNAME 条目中获取的隧道 URL。

或者，您可以通过添加CNAME记录，使用 `*` 作为名称，在 Cloudflare 中添加 [通配符 DNS 记录](https://blog.cloudflare.com/wildcard-proxy-for-everyone/)。

### 选项： `nginx_proxy_manager`

如果您希望将 Cloudflare 隧道与插件 [Nginx Proxy Manager][nginx_proxy_manager] 一起使用，可以通过设置此选项来实现。这将自动将 `catch_all_service` 设置为 Nginx Proxy Manager 的内部 URL。您不必在配置中添加 `catch_all_service` 选项（如果您仍然添加，它将被忽略）。

```yaml
nginx_proxy_manager: true
```

**注意**：_与 `catch_all_service` 一样，这仍将将您的定义的 `external_hostname` 路由到 Home Assistant，以及任何潜在的 `additional_hosts` 路由到您在配置中定义的位置。任何其他传入流量将被路由到 Nginx Proxy Manager。_

为了通过隧道路由主机名，您必须为所有主机名在 Cloudflare 中创建个别的 CNAME 记录，指向您的 `external_hostname` 或直接指向您可以从 `external_hostname` 的 CNAME 条目中获取的隧道 URL。

或者，您可以通过添加CNAME记录，使用 `*` 作为名称，在 Cloudflare 中添加 [通配符 DNS 记录](https://blog.cloudflare.com/wildcard-proxy-for-everyone/)。

最后，您必须在 Nginx Proxy Manager 中设置您的代理主机，并将它们转发到您希望的地方。

### 选项： `use_builtin_proxy`

如果启用，则将通过内置的 Nginx 代理与 Home Assistant 建立连接。Nginx 被实现为解决实时日志问题的解决方法。有关参考，请参见讨论 [#744](https://github.com/brenner-tobias/addon-cloudflared/discussions/744)

**注意**：_此选项默认启用。_

### 选项： `post_quantum`

如果您希望 Cloudflared 在隧道中使用后量子密码学，请设置此标志。

**注意**：_当 `post_quantum` 被设置时，cloudflared 将限制其通过 QUIC 传输建立隧道连接。这可能会给某些用户带来问题。此外，它只允许后量子混合密钥交换，而不会回退到非后量子连接。_

```yaml
post_quantum: true
```

### 选项： `run_parameters`

您可以使用此参数向 cloudflared 守护程序添加额外的运行参数。请查看 [Cloudflare 文档][cloudflare-run_parameter] 获取所有可用参数及其说明。

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

**注意**：_这些参数将被添加到默认存在的参数 "no-autoupdate"、"metrics" 和 "loglevel" 中。此外，对于本地管理的隧道，"origincert" 和 "config" 也被添加，而 "token" 被添加到远程管理的隧道中。您无法通过此选项覆盖这些参数。_

**注意**：_如果您使用的选项需要路径，您可以使用 /config 作为根路径。此路径可以通过 VS-code 插件通过 /addon_configs 访问。_

```yaml
run_parameters:
  - "--region=us"
  - "--protocol=http2"
  - "--loglevel=debug"
```

### 选项： `log_level`

`log_level` 选项控制插件的日志输出级别，可以更改为更多或更少的详细信息，这在处理未知问题时可能会很有用。

**注意**：_如果您想更改隧道本身的日志级别，可以使用 `run_parameters` 的 `--loglevel` 选项。_

```yaml
log_level: debug
```

可能的值包括：

- `trace`：显示每个细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：不算错误的特殊情况。
- `error`：不需要立即处理的运行时错误。
- `fatal`：发生了严重错误。插件变得不可用。

请注意，每个级别自动包含更高严重级别的日志消息，例如，`debug` 也显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您正在进行故障排除。

## Home Assistant 配置

### configuration.yaml

由于 Home Assistant 阻止来自代理/反向代理的请求，您需要告诉您的实例允许来自 Cloudflared 插件的请求。该插件在本地运行，因此 HA 必须信任 Docker 网络。为此，请在您的 `/config/configuration.yaml` 中添加以下行：

**注意**：_不需要修改这些行中的任何内容，因为 Docker 网络的 IP 范围始终相同。_

```yaml
http:
  use_x_forwarded_for: true
  trusted_proxies:
    - 172.30.33.0/24
```

**如果您使用的是 HA 的非标准托管方法（例如 Proxmox），您可能需要在此处添加另一个 IP（范围）。请在尝试连接后检查 HA 日志以查找正确的 IP。**

请记得在更改配置后重新启动 Home Assistant。

如果您需要更改配置的帮助，请遵循 [高级配置教程][advancedconfiguration]。

## 插件维基

有关更多高级 [如何做][how-tos] 和 [故障排除部分][troubleshooting]，请访问 [GitHub 上的插件维基][addon-wiki]。

## 作者与贡献者

此存储库的初始设置由 [Tobias Brenner][tobias] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2025 Tobias Brenner

特此免费授予任何获得此软件及其相关文档文件（“软件”）副本的人，使用软件而不受限制，包括但不限于使用、复制、修改、合并、出版、分发、再许可和/或出售软件副本的权利，并允许向其提供软件的人这样做，前提是遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或实质性部分中。

软件是按“原样”提供的，没有任何形式的保证，无论是明示或暗示，包括但不限于对适销性的保证、特定目的的适用性和非侵权的保证。在任何情况下，作者或版权持有者均不对因软件或使用软件或其他交易而引起的任何索赔、损害或其他责任负责，无论是在合同诉讼、侵权还是其他方面。

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