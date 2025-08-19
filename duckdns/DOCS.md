# 家居助手插件：DuckDNS

## 安装

按照以下步骤在你的系统上安装插件：

1. 在家居助手前端导航到 **设置** -> **插件** -> **插件商店**。
2. 找到 "DuckDNS" 插件并点击它。
3. 点击 "安装" 按钮。

## 如何使用

1. 访问 [DuckDNS.org](https://www.duckdns.org/) 并通过任何可用的账户服务（Google、Github、Twitter、Persona、Reddit）创建一个账户。
2. 在 `域名` 部分，输入你希望注册的子域名，并点击 `添加域名`。
3. 如果注册成功，子域名将列在 `域名` 部分，并且 `当前 IP` 将是你当前用来访问 `duckdns.org` 的设备的公网 IP 地址。DuckDNS 插件将更新 IP 地址。
4. 在 DuckDNS 插件配置中执行以下操作：
    - 从 `duckdns.org` 处显示账户详情的页面顶部复制 DuckDNS 令牌，并将其粘贴到 `token` 选项中。
    - 使用你注册的完整域名更新 `domains` 选项。例如：`my-domain.duckdns.org`。

## 配置

插件配置：

```yaml
lets_encrypt:
  accept_terms: true
  certfile: fullchain.pem
  keyfile: privkey.pem
token: sdfj-2131023-dslfjsd-12321
domains:
  - my-domain.duckdns.org
aliases: []
seconds: 300
```

此外，你需要配置家居助手核心来获取 SSL 证书。这是通过在 `configuration.yaml` 中的 [HTTP][HTTP] 集成配置中设置以下配置来完成的：

```yaml
http:
  ssl_certificate: /ssl/fullchain.pem
  ssl_key: /ssl/privkey.pem
```

### 选项组 `lets_encrypt`

以下选项用于选项组：`lets_encrypt`。这些设置仅适用于 Let's Encrypt SSL 证书。

#### 选项 `lets_encrypt.accept_terms`

一旦你已经阅读并接受了 Let's Encrypt [订阅协议](https://letsencrypt.org/repository/)，将值更改为 `true` 以使用 Let's Encrypt 服务。

#### 选项 `lets_encrypt.certfile`

Let's Encrypt 生成的证书文件的名称。该文件用于家居助手插件的 SSL，建议保持文件名不变（`fullchain.pem`）以保持兼容性。

**注意**：_文件存储在 `/ssl/`，这是家居助手的默认路径_

#### 选项 `lets_encrypt.keyfile`

Let's Encrypt 生成的私钥文件的名称。私钥文件用于家居助手插件的 SSL，建议保持文件名不变（`privkey.pem`）以保持兼容性。

**注意**：_文件存储在 `/ssl/`，这是家居助手的默认路径_

#### 选项 `lets_encrypt.algo`

将要使用的公钥算法。

支持值：`rsa`、`prime256v1` 和 `secp384r1`。

默认值是 `secp384r1`


### 选项：`ipv4`（可选）

默认情况下，Duck DNS 将自动检测你的 IPv4 地址并使用该地址。
此选项允许你覆盖自动检测并手动指定一个 IPv4 地址。

如果你在这里指定一个 URL，它指向的资源的内容将被获取并用作地址。这可以让你使用类似 https://api.ipify.org/ 或 https://ipv4.text.wtfismyip.com 的服务来获取地址

### 选项：`ipv6`（可选）

默认情况下，Duck DNS 将自动检测你的 IPv6 地址并使用该地址。
此选项允许你覆盖自动检测并手动指定一个 IPv6 地址。

如果你在这里指定一个 URL，它指向的资源的内容将被获取并用作地址。这可以让你使用类似 https://api6.ipify.org/ 或 https://ipv6.text.wtfismyip.com 的服务来获取地址

### 选项：`token`

在 DuckDNS 账户登录页面的顶部找到的 DuckDNS 认证令牌。要对你账户下注册的子域名进行任何更改，需要此令牌。

### 选项：`domains`

你账户下注册的 DuckDNS 子域名列表。可接受的命名约定是 `my-domain.duckdns.org`。
也可以使用 `*.my-domain.duckdns.org > my-domain.duckdns.org` 的语法来签发通配符证书。

### 选项：`aliases`（可选）

在 `domains` 选项上配置的域名别名列表。
这在你想使用你自己的域名时非常有用。创建一个 CNAME 记录指向 DuckDNS 子域名并相应地设置此值。
建议将你的 CNAME 的 TTL 值设置为一个较低值，通常在 60 以下。

例如：

```yaml
domains:
  - my-domain.duckdns.org
aliases:
  - domain: ha.my-domain.com
    alias: my-domain.duckdns.org
```

不要将你的自定义域名添加到 `domains` 数组中。对于证书创建，所有唯一的域名和别名都将被使用。

另外，不要忘记确保 dns-01 挑战可以到达 Duckdns。可能需要为这一点添加一个特定的 CNAME：

```
CNAME _acme-challenge.<own-domain>    _acme-challenge.<domain>.duckdns.org
CNAME                 <own-domain>                    <domain>.duckdns.org
```

### 选项：`seconds`

在更新 DuckDNS 子域名和续订 Let's Encrypt 证书之前等待的秒数。

## 已知问题和限制

- 要登录，DuckDNS 需要 Google、Github、Twitter 或 Persona 中的任何一个服务的免费账户。
- 免费的 DuckDNS 账户最多限制五个子域名。
- 在撰写本文时，Duck DNS 自己的 IPv6 自动检测 [实际上不起作用][duckdns-faq]，但你可以使用 `ipv6` 的 URL 选项来解决这个问题，请继续阅读。

## 支持

有问题？

你有几个选项可以得到答案：

- [家居助手 Discord 聊天服务器][discord]。
- 家居助手 [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 中的 [/r/homeassistant][reddit]

如果你发现了一个错误，请 [在我们的 GitHub 上打开一个问题][issue]。

[discord]: https://discord.gg/c5DvZ4e
[forum]: https://community.home-assistant.io
[issue]: https://github.com/home-assistant/addons/issues
[reddit]: https://reddit.com/r/homeassistant
[duckdns]: https://www.duckdns.org
[duckdns-faq]: https://www.duckdns.org/faqs.jsp
[HTTP]: https://www.home-assistant.io/integrations/http/