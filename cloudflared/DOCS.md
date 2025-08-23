# Home Assistant 插件：Cloudflared

Cloudflared 通过安全的隧道连接您的 Home Assistant 实例到 Cloudflare 域名或子域名。这允许您在不需要在路由器上打开端口的情况下将您的 Home Assistant 实例和其他服务暴露给互联网。此外，您还可以利用 Cloudflare Zero Trust 进一步保护您的连接。

## 免责声明

在使用此插件时，请确保您遵守 [Cloudflare 自助服务订阅协议][cloudflare-sssa]。

## 初始设置

### 前提条件

1. 一个使用 Cloudflare 进行 DNS 解析的域名（例如 example.com）。如果您还没有，请参阅 [域名和 Cloudflare 设置][how-tos]。
   请注意，来自 **Freenom** 的域名现在不再有效，因此您必须选择/迁移到另一个注册商。
1. 如果您尚未完成，请 [在 Cloudflare 中为您的域名激活 Websockets][cloudflare-websockets]。
1. 在插件的本地隧道（由插件管理）和远程隧道（在 Cloudflare 的界面中管理）之间进行选择。[了解更多][addon-remote-or-local]。
1. 此插件应该已经 [安装][addon-installation] 但尚未启动。

完成前提条件后，根据您选择的隧道类型继续操作。

### 本地隧道插件设置（推荐）

在以下步骤中，插件将自动创建 Cloudflare 隧道以暴露您的 Home Assistant 实例。

如果您只想暴露其他服务，您可以留空 `external_hostname` 并按照 [以下说明](#configuration) 设置 `additional_hosts`。

1. 按照 [以下说明](#configurationyaml) 在 Home Assistant 配置中配置 `http` 集成。
1. 将 `external_hostname` 插件选项设置为您要用于远程访问的域名/子域名，例如 `ha.example.com`。
1. 启动插件（这将覆盖任何与 `external_hostname` 或 `additional_hosts` 匹配的现有 DNS 条目）。
1. 将插件的日志中的 URL 复制到新标签页以使用 Cloudflare 进行身份验证。
1. 通过远程 URL（无需端口）访问您的 Home Assistant，例如 `https://ha.example.com/`。

现在应该在您的 Cloudflare Teams 仪表板中列出隧道。
请查看以下额外的配置选项。

### 远程隧道插件设置（高级）

在以下步骤中，您将在 Zero Trust 仪表板中手动创建 Cloudflare 隧道，并将令牌提供给插件。

1. 按照 [以下说明](#configurationyaml) 在 Home Assistant 配置中配置 `http` 集成。
1. 按照 [此教程][addon-remote-tunnel] 在 Cloudflare Teams 仪表板中创建 Cloudflare 隧道。
1. 将 `tunnel_token` 插件选项设置为您的 [隧道令牌][create-remote-managed-tunnel]（其他所有配置都将被忽略）。
1. 启动插件，检查日志以确认一切按预期进行。
1. 通过远程 URL（无需端口）访问您的 Home Assistant，例如 `https://ha.example.com/`。

您的隧道现在应该与 Cloudflared 插件相关联。任何配置更改都应该在 Cloudflare Teams 仪表板中进行。

## 配置

**这些配置选项仅适用于本地隧道设置**。更高级的配置可以使用远程隧道设置来实现。

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

**注意**：_更改配置后，请重新启动插件。_

示例插件配置：

```yaml
external_hostname: ha.example.com
additional_hosts:
  - hostname: router.example.com
    service: http://192.168.1.1
  - hostname: website.example.com
    service: http://192.168.1.3:8080
```

**注意**：_这只是个示例，不要复制粘贴！创建您自己的！_

### 选项：`external_hostname`

将 `external_hostname` 选项设置为您要用于访问 Home Assistant 的域名或子域名。

这是可选的，您可以使用 `additional_hosts` 仅暴露其他服务。

**注意**：_在您的 Cloudflare 账户中，隧道名称必须是唯一的。_

```yaml
external_hostname: ha.example.com
```

### 选项：`additional_hosts`

您可以使用 Cloudflare 隧道的内部反向代理来定义除 Home Assistant 之外的其他主机。这样，您可以使用隧道来访问其他系统，如磁盘站、路由器或任何其他系统。

与用于 Home Assistant 的 `external_hostname` 选项类似，Cloudflare 将自动创建 DNS 条目。

向主机添加（可选的）`disableChunkedEncoding` 选项，以禁用分块传输编码。如果您正在运行 WSGI 服务器，例如 Proxmox，则这很有用。有关更多信息，请访问 [Cloudflare 文档][disablechunkedencoding]。

以下是一个为三个附加主机提供的示例条目：

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

**注意 1**：_如果您从列表中删除一个主机名，它将不再提供服务。尽管如此，您还应该手动从 Cloudflare 删除 DNS 条目，因为插件无法删除它。_

**注意 2**：_如果您想完全删除 `additional_hosts` 选项，您必须按照以下方式在配置中添加一个空数组：._

```yaml
additional_hosts: []
```

### 选项：`tunnel_name`

`tunnel_name` 选项允许您将隧道名称更改为除 `homeassistant` 默认名称之外的名称。

**注意**：_在您的 Cloudflare 账户中，隧道名称必须是唯一的。_

```yaml
tunnel_name: myHomeAssistant
```

### 选项：`catch_all_service`

如果您想将所有来自未在 `external_hostname` 或 `additional_hosts` 中定义的主机名的请求转发到某个 URL，您可以使用此选项并定义要转发的 URL。例如，这可以用于反向代理。

**注意**：_如果您想使用 HA 插件 [Nginx Proxy Manager][nginx_proxy_manager] 作为反向代理，您应该设置 `nginx_proxy_manager` 标志（[见下文](#option-nginx_proxy_manager)），并且不使用此选项。_

```yaml
catch_all_service: http://192.168.1.100
```

**注意**：_这将仍然将您定义的 `external_hostname` 转发到 Home Assistant，以及任何潜在的 `additional_hosts` 转发到配置中定义的服务。任何其他传入流量都将被转发到定义的服务。_

为了通过隧道路由主机名，您必须在 Cloudflare 中为所有这些主机名创建单独的 CNAME 记录，指向您的 `external_hostname` 或直接指向您从 `external_hostname` 的 CNAME 条目中获取的隧道 URL。

或者，您可以通过在 Cloudflare 中添加一个名为 `*` 的 CNAME 记录来添加一个 [通配符 DNS 记录](https://blog.cloudflare.com/wildcard-proxy-for-everyone/)。

### 选项：`nginx_proxy_manager`

如果您想使用 Cloudflare 隧道与插件 [Nginx Proxy Manager][nginx_proxy_manager]，您可以通过设置此选项来实现。它将自动将 `catch_all_service` 设置为 Nginx Proxy Manager 的内部 URL。您不需要在配置中添加 `catch_all_service` 选项（如果您无论如何都添加了它，它将被忽略）。_

```yaml
nginx_proxy_manager: true
```

**注意**：_与 `catch_all_service` 类似，这将仍然将您定义的 `external_hostname` 转发到 Home Assistant，以及任何潜在的 `additional_hosts` 转发到配置中定义的服务。任何其他传入流量都将被转发到 Nginx Proxy Manager。_

为了通过隧道路由主机名，您必须在 Cloudflare 中为所有这些主机名创建单独的 CNAME 记录，指向您的 `external_hostname` 或直接指向您从 `external_hostname` 的 CNAME 条目中获取的隧道 URL。

或者，您可以通过在 Cloudflare 中添加一个名为 `*` 的 CNAME 记录来添加一个 [通配符 DNS 记录](https://blog.cloudflare.com/wildcard-proxy-for-everyone/)。

最后，您必须在 Nginx Proxy Manager 中设置您的代理主机，并将它们转发到您喜欢的地方。

### 选项：`use_builtin_proxy`

如果启用，对 Home Assistant 的连接将通过内置的 Nginx 代理进行。Nginx 是作为解决实时日志问题的替代方案实现的。有关详细信息，请参阅讨论 [#744](https://github.com/brenner-tobias/addon-cloudflared/discussions/744)

**注意**：_此选项默认启用。_

### 选项：`post_quantum`

如果您想让 Cloudflared 使用后量子密码学来保护隧道，请设置此标志。

**注意**：_当 `post_quantum` 设置时，cloudflared 将自己限制为隧道的 QUIC 传输。这可能会导致一些用户遇到问题。此外，它将仅允许后量子混合密钥交换，而不会回退到非后量子连接。_

```yaml
post_quantum: true
```

### 选项：`run_parameters`

您可以使用此参数向 cloudflared 守护进程添加额外的运行参数。有关所有可用参数及其解释，请查看 [Cloudflare 文档][cloudflare-run_parameter]。

要添加的有效参数包括：

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

**注意**：_这些参数被添加到默认存在的参数 "no-autoupdate"、"metrics" 和 "loglevel"。此外，对于本地管理的隧道，添加了 "origincert" 和 "config"，而对于远程管理的隧道，添加了 "token"。您不能用此选项覆盖这些参数。_

**注意**：_如果您使用需要路径的选项，您可以使用 /config 作为根。此路径可以通过 VS-code 插件等访问 / / addon_configs。_

```yaml
run_parameters:
  - "--region=us"
  - "--protocol=http2"
  - "--loglevel=debug"
```

### 选项：`log_level`

`log_level` 选项控制插件生成的日志级别，可以更详细或更简洁，这在您处理未知问题时可能很有用。

**注意**：_如果您想更改隧道本身的日志级别，您可以使用 `run_parameters` `--loglevel` 选项。_

```yaml
log_level: debug
```

可能的值是：

- `trace`：显示每个细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的条目。
- `warning`：异常事件，但不是错误。
- `error`：运行时错误，不需要立即采取行动。
- `fatal`：出了严重问题。插件变得无法使用。

请注意，每个级别自动包含更严重级别的日志消息，例如 `debug` 也显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，除非您正在调试，否则这是推荐设置。

## Home Assistant 配置

### configuration.yaml

由于 Home Assistant 会阻止来自代理/反向代理的请求，您需要告诉您的实例允许来自 Cloudflared 插件的请求。插件在本地运行，因此 HA 必须信任 Docker 网络。为此，请将以下行添加到您的 `/config/configuration.yaml`：

**注意**：_您不需要调整这些行，因为 Docker 网络的 IP 范围始终相同。_

```yaml
http:
  use_x_forwarded_for: true
  trusted_proxies:
    - 172.30.33.0/24
```

**如果您使用 Home Assistant 的非标准托管方法（例如 Proxmox），您可能需要在此处添加另一个 IP（范围）。尝试连接后，请查看您的 HA 日志以找到正确的 IP。**

如果您更改了 Home Assistant 端口或在 [HTTP 集成][http-integration] 配置中启用了 SSL，请确保将此类配置直接保留在您的 Home Assistant 的 `configuration.yaml` 中。使用 `!include` 或 [包][homeassistant-packages] 将防止插件能够读取您的 Home Assistant 配置并确定内部通信的正确的 Home Assistant URL。

更改配置后，请重新启动 Home Assistant。

如果您需要帮助更改配置，请按照 [高级配置教程][advancedconfiguration] 操作。

## 插件维基

有关更多高级 [教程][how-tos] 和 [故障排除部分][troubleshooting]，请访问 GitHub 上的 [插件维基][addon-wiki]。

## 作者和贡献者

此存储库的原始设置由 [Tobias Brenner][tobias] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有（c）2025 Tobias Brenner

特此免费授予任何获得此软件及其相关文档文件（“软件”）副本的人，在不受限制的情况下处理该软件的权利，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权利，并允许获得软件的人这样做，但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件按“原样”提供，不提供任何明示或暗示的保证，包括但不限于适销性、特定用途的适用性和不侵犯版权的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害或其他责任承担责任，无论是合同行为、侵权行为还是其他行为，均由软件或使用软件或其他交易引起。