# 非官方 Home Assistant 附加组件：Traefik

Traefik 打包为 Home Assistant 附加组件。

## 安装

按照以下步骤在您的系统上安装附加组件：

1. 在您的 Home Assistant 前端导航到 **Supervisor -> Add-on Store**
1. 通过 URL 添加这个新的存储库 (`https://github.com/bluemaex/home-assistant-addons`)
1. 找到 "Traefik" 附加组件并点击它。
1. 点击 "INSTALL" 按钮

## 如何使用

在配置部分，您需要设置所需的配置路径。这个路径可以是您 Home Assistant 配置或 Hass.io 共享目录中的一个目录，因为这两者都是以只读方式挂载到该附加组件中的。

您放置在那里的任何 Traefik 端点配置将会被该附加组件自动识别。更新也将由 Traefik 自动处理。

您还可以在配置中启用 Let's Encrypt 支持，并在需要时设置其他环境变量。

该附加组件提供两个 Traefik 入口点。`web` 在端口 80 上，`web-secure` 在端口 443 上。

### 示例动态 Traefik 配置

```yaml
http:
  routers:
    redirectToHttpsRouter:
      entryPoints: ["web"]
      middlewares: ["httpsRedirect"]
      rule: "HostRegexp(`{host:.+}`)"
      service: noopService

    homeAssistantRouter:
      rule: "Host(`localhost`)"
      entryPoints: ["web-secure"]
      tls:
        certResolver: le
      service: homeAssistantService

    metricsRouter:
      rule: "Host(`localhost`) && PathPrefix(`/traefik-metrics`)"
      entryPoints: ["web-secure"]
      tls:
        certResolver: le
      service: prometheus@internal

  middlewares:
    httpsRedirect:
      redirectScheme:
        scheme: https

  services:
    noopService:
      loadBalancer:
        servers:
          - url: "http://localhost"

    homeAssistantService:
      loadBalancer:
        servers:
          - url: "http://homeassistant:8123"
```

## 配置

完整的附加组件示例配置，用于 Let's Encrypt 配合 Cloudflare DNS 代理，在您的 Home Assistant 配置目录中的动态配置：

```yaml
log_level: INFO
access_logs: false
forwarded_headers_insecure: true
dynamic_configuration_path: /config/traefik
letsencrypt:
  enabled: true
  email: example@home-assistant.io
  challenge_type: dnsChallenge
  provider: cloudflare
  delayBeforeCheck: 10
  resolvers:
    - "1.1.1.1:53"
pilot_token: "My-SUPER-secret-Pilot-Token-Here"
env_vars:
  - CF_DNS_API_TOKEN=YOUR-API-TOKEN-HERE
  - ANOTHER_ENV_VARIABLE=SOME-VALUE
```

### 选项 `log_level`（必填）

`log_level` 选项控制附加组件的日志输出级别，可以更改为更详细或更简单的输出，这在处理未知问题时可能很有用。可能的值包括：

- `trace`: 显示每一个细节，例如所有调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 正常（通常）有趣的事件。
- `warning`: 非错误的异常情况。
- `error`: 不需要立即处理的运行时错误。
- `fatal`: 出现了严重问题，附加组件变得无法使用。

请注意，每个级别会自动包含更严重级别的日志消息，例如 `debug` 还显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您在进行故障排除。

### 选项 `access_logs`（必填）

是否启用访问日志以输出到标准输出。这些日志将显示在 Hass.io 附加组件面板中。

### 选项 `forwarded_headers_insecure`（必填）

启用不安全的转发头。当启用此选项时，转发头（`X-Forwarded-*`）将不会被 Traefik 头替换。仅在您信任您所转发的代理时启用此选项。

> **\_注意** 如果要使 Cloudflare 的 `X-Forwarded-*` 代理头正常工作，必须启用此选项。\_

### 选项 `dynamic_configuration_path`（必填）

动态端点配置的目录路径。请参见上面的示例。

### 选项 `letsencrypt.enabled`（必填）

是否启用 Let's Encrypt。当启用此选项时，将激活 `le` certResolver 以供使用。您还需要设置 Let's Encrypt 的电子邮件和挑战类型。否则，Traefik 将无法启动。

### 选项 `letsencrypt.email`

您希望用于 Let's Encrypt 的个人电子邮件。

> _**注意** 启用 Let's Encrypt 时这是必需的。_

### 选项 `letsencrypt.challenge_type`

您希望用于 Let's Encrypt 的挑战类型。有效的选项有：

- `tlsChallenge`
- `httpChallenge`
- `dnsChallenge`

有关挑战类型及选择建议的更多信息，请参见 Traefik 文档中[ACME 部分](https://docs.traefik.io/https/acme/)。

### 选项 `letsencrypt.provider`

在使用 `dnsChallenge` 时，您还需要设置一个提供程序。提供程序列表可以在 Traefik 文档中的[Let's Encrypt 提供程序部分](https://docs.traefik.io/https/acme/#providers)中找到。

### 选项 `letsencrypt.delayBeforeCheck`

默认情况下，提供程序将在允许 ACME 验证之前验证 TXT DNS 挑战记录。如果 `delayBeforeCheck` 被设置且大于零，则此检查会延迟配置的秒数。

此设置在内部网络阻止外部 DNS 查询时很有用。有关更多信息，请查看 Traefik 文档中关于此主题的[内容](https://docs.traefik.io/https/acme/#dnschallenge)。

### 选项 `letsencrypt.resolvers`

手动设置在执行验证步骤时要使用的 DNS 服务器。对于内部 DNS 解析地址与公共互联网地址不一致的情况（例如，使用 FQDN 作为主机名的局域网），此选项非常有用。

有关更多信息，请参见 Traefik 文档中关于此主题的[内容](https://docs.traefik.io/https/acme/#resolvers)。

### 选项 `pilot_token`

手动设置 Traefik pilot token，以将实例连接到您的 pilot 帐户进行监控。

有关更多信息，请访问[Traefik pilot 网站](https://https://pilot.traefik.io/)。

### 选项 `metrics`

您可以启用 Traefik 的 prometheus 指标服务。如果您启用它，则需要在配置文件中添加相应的路由器。

有关更多信息，请参见[Traefik Prometheus 文档](https://doc.traefik.io/traefik/observability/metrics/prometheus/)。

```yaml
metricsRouter:
  rule: "Host(`hass.io`) && PathPrefix(`/metrics`)"
  entryPoints: ["web-secure"]
  tls:
    certResolver: le
  service: prometheus@internal
```

### 选项 `env_vars`

可以添加的可选环境变量。这些额外的配置值对于 Let's Encrypt DNS 挑战提供者可能是必要的。有关具体示例，请参见上面的示例配置。

## 入口点

此映像公开了两个 HTTP(S) 访问端口。这些也在 Traefik 中配置为入口点。您可以在动态配置中使用这些端口。

### 入口点 `web`，端口 `80`

端口 80 用于 HTTP 访问。

当使用支持的 Let's Encrypt 提供者（即 Cloudflare）并使用 DNS Challenge 时，您也可以将该端口映射到另一个随机端口，让 CloudFlare 进行 HTTP 到 HTTPS 的转发。

### 入口点 `web-secure`，端口 `443`

端口 443 用于 HTTPS 访问。