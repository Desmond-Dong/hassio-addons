# Home Assistant 添加程序：Cloudflared

Cloudflared 通过安全的隧道将您的 Home Assistant 实例连接到 Cloudflare 域名或子域名。这允许您在不打开路由器端口的情况下将您的 Home Assistant 实例和其他服务暴露给互联网。此外，您还可以利用 Cloudflare Zero Trust 进一步保护您的连接。

## 免责声明

在使用此添加程序时，请确保您遵守 [Cloudflare 自助服务订阅协议][cloudflare-sssa]。

## 初始设置

### 前提条件

1. 一个使用 Cloudflare 进行 DNS 的域名（例如 example.com）。如果您还没有，请参阅 [域名和 Cloudflare 设置][how-tos]。
   请注意，来自 **Freenom** 的域名不再有效，因此您必须选择/迁移到另一个注册商。
1. 如果您尚未完成，请 [在 Cloudflare 中为您的域名激活 Websockets][cloudflare-websockets]。
1. 在添加程序管理本地隧道或 Cloudflare 界面管理的远程隧道之间进行选择。[了解更多][addon-remote-or-local]。
1. 此添加程序应已 [安装][addon-installation] 但尚未启动。

完成前提条件后，根据您选择的隧道类型，继续以下步骤。

### 本地隧道添加程序设置（推荐）

在以下步骤中，添加程序将自动创建 Cloudflare 隧道以公开您的 Home Assistant 实例。

如果您只想公开其他服务，可以留空 `external_hostname` 并按照 [以下说明](#configuration)设置 `additional_hosts`。

1. 按照 [以下说明](#configurationyaml)在 Home Assistant 配置中配置 `http` 集成。
1. 将 `external_hostname` 添加程序选项设置为您要用于远程访问的域名/子域名，例如 `ha.example.com`。
1. 启动添加程序（这将覆盖任何与 `external_hostname` 或 `additional_hosts` 匹配的现有 DNS 条目）。
1. 将添加程序日志中的 URL 复制到新选项卡以使用 Cloudflare 进行身份验证。
1. 通过远程 URL（无需端口）访问您的 Home Assistant，例如 `https://ha.example.com/`。

现在，您的 Cloudflare Teams 仪表板中应该列出了隧道。
请查看以下额外的配置选项。

### 远程隧道添加程序设置（高级）

在以下步骤中，您将在 Zero Trust 仪表板中手动创建 Cloudflare 隧道，并将令牌提供给添加程序。

1. 按照 [以下说明](#configurationyaml)在 Home Assistant 配置中配置 `http` 集成。
1. 按照 [此教程][addon-remote-tunnel] 在 Cloudflare Teams 仪表板中创建 Cloudflare 隧道。
1. 将 `tunnel_token` 添加程序选项设置为您的 [隧道令牌][create-remote-managed-tunnel]（将忽略所有其他配置）。
1. 启动添加程序，检查日志以确认一切按预期进行。
1. 通过远程 URL（无需端口）访问您的 Home Assistant，例如 `https://ha.example.com/`。

现在，您的隧道应与 Cloudflared 添加程序相关联。任何配置更改都应在 Cloudflare Teams 仪表板中进行。

## 配置

**这些配置选项仅适用于本地隧道设置**。更高级的配置可以使用远程隧道设置来实现。

- [`external_hostname`](#option-external_hostname)
- [`additional_hosts`](#option-additional_hosts)
- [`tunnel_name`](#option-tunnel_name)
- [`catch_all_service`](#option-catch_all_service)
- [`nginx_proxy_manager`](#option-nginx_proxy_manager)
- [`post_quantum`](#option-post_quantum)
- [`run_parameters`](#option-run_parameters)
- [`log_level`](#option-log_level)

### 概述：添加程序配置

**注意**：_更改配置后，请重启添加程序。_

示例添加程序配置：

```yaml
external_hostname: ha.example.com
additional_hosts:
  - hostname: router.example.com
    service: http://192.168.1.1
  - hostname: website.example.com
    service: http://192.168.1.3:8080
```

**注意**：_这只是一个示例，请不要复制粘贴！创建您自己的！_

### 选项：`external_hostname`

将 `external_hostname` 选项设置为您要用于访问 Home Assistant 的域名或子域名。

这是可选的，您也可以使用 `additional_hosts` 仅公开其他服务。

**注意**：_在您的 Cloudflare 账户中，隧道名称必须是唯一的。_

```yaml
external_hostname: ha.example.com
```

### 选项：`additional_hosts`

您可以使用 Cloudflare 隧道的内部反向代理来定义除 Home Assistant 之外的其他主机。这样，您就可以使用隧道来访问其他系统，如磁盘站、路由器或任何其他系统。

与用于 Home Assistant 的 `external_hostname` 选项一样，Cloudflare 将自动创建 DNS 条目。

将（可选的）`disableChunkedEncoding` 选项添加到主机名，以禁用分块传输编码。如果您正在运行 WSGI 服务器，例如 Proxmox，则这很有用。有关更多信息，请访问 [Cloudflare 文档][disablechunkedencoding]。

以下是一个三个附加主机的示例条目：

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

**注意 1**：_如果您从列表中删除了主机名，它将不再提供服务。尽管如此，您还应该手动从 Cloudflare 中删除 DNS 条目，因为添加程序无法删除它。_

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

如果您想将任何未在 `external_hostname` 或 `additional_hosts` 中定义的主机名的请求转发到某个 URL，您可以使用此选项并定义要转发到的 URL。例如，这可以用于反向代理。

**注意**：_如果您想使用 HA 添加程序 [Nginx Proxy Manager][nginx_proxy_manager] 作为反向代理，您应该设置 `nginx_proxy_manager` 标志（[见下文](#option-nginx_proxy_manager)）并不要使用此选项。_

```yaml
catch_all_service: http://192.168.1.100
```

**注意**：_这将仍然将您定义的 `external_hostname` 转发到 Home Assistant，以及任何潜在的 `additional_hosts` 转发到配置中定义的位置。任何其他传入流量都将被路由到定义的服务。_

为了通过隧道路由主机名，您必须在 Cloudflare 中为所有这些主机名创建单独的 CNAME 记录，指向您的 `external_hostname` 或直接指向您可以从 `external_hostname` 的 CNAME 条目中获取的隧道 URL。

或者，您可以通过在 Cloudflare 中添加一个名为 `*` 的 CNAME 记录来添加一个 [通配符 DNS 记录](https://blog.cloudflare.com/wildcard-proxy-for-everyone/)。

### 选项：`nginx_proxy_manager`

如果您想使用 Cloudflare 隧道与添加程序 [Nginx Proxy Manager][nginx_proxy_manager]，您可以通过设置此选项来实现。它将自动将 `catch_all_service` 设置为 Nginx Proxy Manager 的内部 URL。您不需要在配置中添加 `catch_all_service` 选项（如果您仍然添加它，它将被忽略）。_

```yaml
nginx_proxy_manager: true
```

**注意**：_与 `catch_all_service` 一样，这将仍然将您定义的 `external_hostname` 转发到 Home Assistant，以及任何潜在的 `additional_hosts` 转发到配置中定义的位置。任何其他传入流量都将被路由到 Nginx Proxy Manager。_

为了通过隧道路由主机名，您必须在 Cloudflare 中为所有这些主机名创建单独的 CNAME 记录，指向您的 `external_hostname` 或直接指向您可以从 `external_hostname` 的 CNAME 条目中获取的隧道 URL。

或者，您可以通过在 Cloudflare 中添加一个名为 `*` 的 CNAME 记录来添加一个 [通配符 DNS 记录](https://blog.cloudflare.com/wildcard-proxy-for-everyone/)。

最后，您必须在 Nginx Proxy Manager 中设置您的代理主机名，并将它们转发到您喜欢的地方。

### 选项：`post_quantum`

如果您想让 Cloudflared 使用后量子密码学来保护隧道，请设置此标志。

**注意**：_当 `post_quantum` 被设置时，cloudflared 会将隧道连接限制为 QUIC 传输。这可能会导致某些用户出现问题。此外，它将仅允许后量子混合密钥交换，而不会回退到非后量子连接。_

```yaml
post_quantum: true
```

### 选项：`run_parameters`

您可以使用此参数向 cloudflared 守护进程添加额外的运行参数。有关所有可用参数及其说明，请查看 [Cloudflare 文档][cloudflare-run_parameter]。

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

**注意**：_这些参数被添加到默认存在的参数 "no-autoupdate"、"metrics" 和 "loglevel"。此外，对于本地管理的隧道，"origincert" 和 "config" 被添加，而 "token" 被添加到远程管理的隧道。您不能使用此选项覆盖这些参数。_

**注意**：_如果您使用需要路径的选项，您可以使用 /config 作为根。此路径可以通过 VS-code 添加程序等途径访问 / / addon_configs。_

```yaml
run_parameters:
  - "--region=us"
  - "--protocol=http2"
  - "--loglevel=debug"
```

### 选项：`log_level`

`log_level` 选项控制添加程序的日志输出级别，可以更详细或更简洁，这在您处理未知问题时可能很有用。

**注意**：_如果您想更改隧道本身的日志级别，您可以使用 `run_parameters` `--loglevel` 选项。_

```yaml
log_level: debug
```

可能的值：

- `trace`：显示每个细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：异常情况，但不是错误。
- `error`：运行时错误，不需要立即采取行动。
- `fatal`：出了严重问题。添加程序变得无法使用。

请注意，每个级别都会自动包含更严重级别的日志消息，例如 `debug` 也显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，除非您正在排错，否则这是推荐设置。

## Home Assistant 配置

### configuration.yaml

由于 Home Assistant 阻止来自代理/反向代理的请求，您需要告诉您的实例允许来自 Cloudflared 添加程序的请求。添加程序在本地运行，因此 HA 必须信任 Docker 网络。为此，请将以下行添加到您的 `/config/configuration.yaml`：

**注意**：_您不需要修改这些行，因为 Docker 网络的 IP 范围始终相同。_

```yaml
http:
  use_x_forwarded_for: true
  trusted_proxies:
    - 172.30.33.0/24
```

**如果您使用 Home Assistant 的非标准托管方法（例如 Proxmox），您可能需要在此处添加另一个 IP(范围)。在尝试连接后检查您的 HA 日志以找到正确的 IP。**

**重要**：添加程序读取您的 `configuration.yaml` 以检测您的 Home Assistant 端口和是否使用 SSL。**如果您在 [HTTP 集成][http-integration] 中更改了默认端口或启用了 SSL，您必须将整个 `http:` 块直接放在 `configuration.yaml` 中。** **不要**将其移动到 [`!include`][homeassistant-config-splitting] 文件或 [`!include_dir_*`][homeassistant-config-packages] 目录中，因为添加程序不会跟踪额外的 YAML 文件。

当配置更改时，请记住重启 Home Assistant。

如果您需要帮助更改配置，请按照 [高级配置教程][advancedconfiguration] 进行操作。

## 添加程序 Wiki

有关更多高级 [教程][how-tos] 和 [故障排除部分][troubleshooting]，请访问 [GitHub 上的添加程序 Wiki][ addon-wiki]。

## 作者和贡献者

此存储库的原始设置由 [Tobias Brenner][tobias] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2025 Tobias Brenner

特此免费授予任何获得此软件和关联文档文件（“软件”）副本的人，在软件上不受限制地处理的权利，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权利，并允许获得软件的人这样做，但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件按“原样”提供，不提供任何形式的保证，包括但不限于对适销性、特定用途适用性和非侵权性的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害赔偿或其他责任承担责任，无论是在合同行为、侵权行为或其他行为中，均是由于与软件或使用或其他交易有关。