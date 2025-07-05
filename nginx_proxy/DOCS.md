# Home Assistant Add-on: NGINX Home Assistant SSL代理

## 安装

按照以下步骤将add-on安装到您的系统上：

1. 在Home Assistant前端导航到**设置** -> **add-on** -> **add-on商店**。
2. 找到“NGINX Home Assistant SSL代理”add-on并点击它。
3. 点击“安装”按钮。

## 如何使用

NGINX代理add-on通常与[Duck DNS](https://github.com/home-assistant/addons/tree/master/duckdns)和/或[Let's Encrypt](https://github.com/home-assistant/addons/tree/master/letsencrypt) add-on一起使用，以设置对Home Assistant实例的安全远程访问。以下说明涵盖了这种情况。

1. 您的注册域的证书应该已经通过[Duck DNS](https://github.com/home-assistant/addons/tree/master/duckdns)、[Let's Encrypt](https://github.com/home-assistant/addons/tree/master/letsencrypt)或其他方法创建。确保证书文件存在于`/ssl`目录中。
2. 您必须在您的[Home Assistant配置文件](https://www.home-assistant.io/docs/configuration/)中添加以下部分。如果`http`部分正在使用`ssl_certificate`、`ssl_key`或`server_port`键，请确保删除它们。

   ```yaml
   http:
     use_x_forwarded_for: true
     trusted_proxies:
       - 172.30.33.0/24
   ```
3. 在nginx add-on配置中，将`domain`选项更改为您注册的域名（来自DuckDNS或您控制的任何其他域名）。
4. 将所有其他选项保持不变。
5. 保存配置。
6. 启动add-on。
7. 拿出一些耐心，等待几分钟。
8. 检查add-on日志输出以查看结果。

## 配置

add-on配置：

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

### 选项：`domain`（必需）

用于代理的服务器的完全限定域名。

### 选项：`certfile`（必需）

在`/ssl`目录中使用的证书文件。如果您使用默认设置通过[Duck DNS](https://github.com/home-assistant/addons/tree/master/duckdns) add-on创建证书，请保持文件名不变。

### 选项：`keyfile`（必需）

在`/ssl`目录中使用的私钥文件。

### 选项：`hsts`（必需）

发送的[`Strict-Transport-Security`][hsts] HTTP头的值。如果为空，则不发送该头。

### 选项`customize.active`（必需）

如果为true，则从`/share`目录中指定的`default`和`servers`变量读取默认服务器和附加服务器的附加NGINX配置文件。

### 选项`customize.default`（必需）

在`/share`目录中找到的默认服务器的NGINX配置文件的名称。

### 选项`customize.servers`（必需）

在`/share`目录中找到的附加服务器的NGINX配置文件名称。

### 选项`cloudflare`（可选）

如果启用，则通过Cloudflare直接配置Nginx，用于`set_real_ip_from`指令的Nginx配置的IP地址列表。
这样，`ip_ban_enabled`功能就可以使用，并且可以在`/config/customize.yaml`中正确工作。

### 选项`real_ip_from`（可选）

如果指定，则配置Nginx使用代理协议从上游负载均衡器获取真实IP地址；[更多信息](https://docs.nginx.com/nginx/admin-guide/load-balancer/using-proxy-protocol/)。

## 已知问题和限制

- 默认情况下，add-on配置中禁用了端口80，以防该端口被其他组件或add-on（如`emulated_hue`）使用。

## 故障排除

- 通过此代理请求返回`400 Bad Request`响应意味着您可能缺少`trusted_proxies`配置选项，请参阅上文。

## 支持

有问题？

您有几个选项可以回答这些问题：

- [Home Assistant Discord聊天服务器][discord]。
- Home Assistant [社区论坛][forum]。
- 加入[Reddit子版块][reddit]中的[/r/homeassistant][reddit]

如果您发现了一个错误，请[在我们的GitHub上打开一个问题][issue]。

[discord]: https://discord.gg/c5DvZ4e
[forum]: https://community.home-assistant.io
[hsts]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security
[issue]: https://github.com/home-assistant/addons/issues
[reddit]: https://reddit.com/r/homeassistant
[repository]: https://github.com/hassio-addons/repository