# Home Assistant 插件：NGINX Home Assistant SSL 代理

## 安装

按照以下步骤在您的系统上安装插件：

1. 在您的 Home Assistant 前端导航到 **设置** -> **插件** -> **插件商店**。
2. 找到 "NGINX Home Assistant SSL 代理" 插件并点击它。
3. 点击 "安装" 按钮。

## 如何使用

NGINX 代理插件通常与 [Duck DNS](https://github.com/home-assistant/addons/tree/master/duckdns) 和/或 [Let's Encrypt](https://github.com/home-assistant/addons/tree/master/letsencrypt) 插件一起使用，以设置对您的 Home Assistant 实例的安全远程访问。以下说明覆盖了这种情况。

1. 您注册域名的证书应该已经通过 [Duck DNS](https://github.com/home-assistant/addons/tree/master/duckdns)、[Let's Encrypt](https://github.com/home-assistant/addons/tree/master/letsencrypt) 或其他方法创建。确保证书文件存在于 `/ssl` 目录中。
2. 您必须在 [Home Assistant configuration.yaml](https://www.home-assistant.io/docs/configuration/) 中添加以下部分。如果 `http` 部分使用了 `ssl_certificate`、`ssl_key` 或 `server_port` 键，请确保将它们移除。

   ```yaml
   http:
     use_x_forwarded_for: true
     trusted_proxies:
       - 172.30.33.0/24
   ```
3. 在 NGINX 插件配置中，将 `domain` 选项更改为您注册的域名（来自 DuckDNS 或任何您控制的域名）。
4. 保持所有其他选项不变。
5. 保存配置。
6. 启动插件。
7. 稍作耐心，等待几分钟。
8. 检查插件日志输出以查看结果。

## 配置

插件配置：

```yaml
domain: home.example.com
certfile: fullchain.pem
keyfile: privkey.pem
hsts: "max-age=31536000; includeSubDomains"
customize:
  active: false
  default: "nginx_proxy_default*.conf"
  servers: "nginx_proxy/*.conf"
cloudflare: false
real_ip_from: []
```

### 选项：`domain`（必填）

要用于代理的服务器完全合格域名。

### 选项：`certfile`（必填）

在 `/ssl` 目录中使用的证书文件。如果您使用默认设置通过 [Duck DNS](https://github.com/home-assistant/addons/tree/master/duckdns) 插件创建证书，则保持文件名不变。

### 选项：`keyfile`（必填）

在 `/ssl` 目录中使用的私钥文件。

### 选项：`hsts`（必填）

要发送的 [`Strict-Transport-Security`][hsts] HTTP 头的值。如果为空，则不会发送该头。

### 选项 `customize.active`（必填）

如果为真，将从 `/share` 目录中指定的 `default` 和 `servers` 变量的文件中读取默认服务器和附加服务器的额外 NGINX 配置文件。

### 选项 `customize.default`（必填）

在 `/share` 目录中找到的默认服务器的 NGINX 配置文件名。

### 选项 `customize.servers`（必填）

在 `/share` 目录中找到的附加服务器的 NGINX 配置文件名。

### 选项 `cloudflare`（可选）

如果启用，配置 Nginx 使用来自 Cloudflare 的 IP 地址列表，这些地址将用于 Nginx 配置中的 `set_real_ip_from` 指令。这样 `ip_ban_enabled` 功能就可以被使用并在 /config/customize.yaml 中正确运作。

### 选项 `real_ip_from`（可选）

如果指定，配置 Nginx 使用代理协议从上游负载均衡器获取真实 IP；[更多信息](https://docs.nginx.com/nginx/admin-guide/load-balancer/using-proxy-protocol/)。

## 已知问题和限制

- 默认情况下，插件配置中禁用端口 80，以防该端口需要用于其他组件或插件，如 `emulated_hue`。

## 故障排除

- 通过此代理的请求返回 `400 Bad Request` 响应意味着您的 `trusted_proxies` 配置选项可能缺失，请查看上述内容。

## 支持

有问题吗？

您有几个选项来获得答案：

- [Home Assistant Discord 聊天服务器][discord]。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

如果您发现了一个错误，请 [在我们的 GitHub 上提交问题][issue]。

[discord]: https://discord.gg/c5DvZ4e
[forum]: https://community.home-assistant.io
[hsts]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security
[issue]: https://github.com/home-assistant/addons/issues
[reddit]: https://reddit.com/r/homeassistant
[repository]: https://github.com/hassio-addons/repository