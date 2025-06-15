# Home Assistant 附加组件：邮件服务器

带有 Postfixadmin Web 界面的 Postfix/Dovecot 邮件服务器...

![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield]
![支持 armv7 架构][armv7-shield] ![支持 i386 架构][i386-shield]

## 关于

重要提示：此附加组件需要安装并运行 MariaDB 附加组件!

此附加组件为您的域提供邮件服务器，且仍在实验阶段。
还可以在 Postfix Admin Web 界面中配置其他邮件域和帐户。

此附加组件使用以下端口：

smtp：端口 25、465 和 587
imap(s)：993

可以在配置的网络部分更改这些端口。

如果您大胆，可以将邮件服务器暴露到互联网。
请参阅下面的说明：

要从 Internet 接收邮件，必须在路由器中为 SMTP 端口添加重定向。
必要的 MX 和 A 记录必须在 DNS 中注册。
如果希望能够从网络外部检查电子邮件，还必须转发 IMAP 端口。

默认设置将使用 Dovecot 在初始设置期间创建的自签名证书。
这对于测试是可以的，但应使用“真实”证书。

配置选项 "letsencrypt_certs" 如果设置为 "true"，将使用 Home Assistant 中 /ssl 目录下的 fullchain.pem 和 privkey.pem。

## 安装

按照以下步骤在您的系统上安装附加组件：

添加存储库 `https://github.com/erik73/hassio-addons`。
找到“邮件服务器”附加组件并点击它。
点击“安装”按钮。

## 如何使用

### 启动附加组件

安装后，您将看到默认示例配置。

调整附加组件配置以匹配您的要求。
通过点击“保存”按钮保存附加组件配置。
启动附加组件。

## 配置

示例配置：

```yaml
my_hostname: mydomain.no-ip.com
domain_name: mydomain.no-ip.com
admin_user: admin
admin_password: admin
letsencrypt_certs: false
enable_mailfilter: false
message_size_limit: 10
```

请注意：在附加组件启动期间，会在 MariaDB 附加组件中创建数据库。
创建数据库后，当前无法更改用户名或 domain_name。密码可以更改。
更改用户和域名的唯一方法是删除 Postfix Admin 数据库并重新启动附加组件。
使用 phpMyadmin 附加组件删除数据库。

### 选项：`my_hostname`（必填）

您的邮件服务器的主机名。它应该与您在 DNS 中的 A 记录相对应。

#### 选项：`domain_name`（必填）

这是您希望接收邮件的域名。
可以在 postfixadmin 界面中添加其他域。

#### 选项：`admin_user`（必填）

postfixadmin 中的管理员用户名。要登录 Web 界面，您必须使用 FQDN。例如：admin@mydomain.no-ip.com。
在当前版本的附加组件中，一旦创建数据库后，此项不能更改。

#### 选项：`admin_password`（必填）

管理员用户的密码。
此选项可以在初始安装后更改。如果您忘记密码，这是一个非常方便的功能！

#### 选项：`letsencrypt_certs`（必填）

如果您使用 Let's Encrypt 附加组件或以其他方式在您的 HA 实例的 /ssl 文件夹中安装了证书，则此选项将使用这些证书进行 SMTP 和 IMAP 服务。

文件应命名为 fullchain.pem 和 privkey.pem。

#### 选项：`message_size_limit`（必填）

配置单个消息/邮件的最大大小（单位：MB）。
大于此大小的消息将被拒绝。
如果希望与常见云邮件提供商最好兼容，请使用 50 MB。
默认：10

#### 选项：`enable_mailfilter`（必填）

这将启用与此存储库中的可选 Mailfilter 附加组件的通信。
它将启用 Postfix 扫描电子邮件中的垃圾邮件和病毒，并包括可选的 DKIM 签名。
为了能够成功从主机发送电子邮件，而不风险让您的发件电子邮件被拒绝或被归类为垃圾邮件，DKIM 签名是必需的。
您还必须配置 DNS 服务器以提供 SPF 和 DMARC。
如果 DKIM、SPF 和 DMARC 听起来太复杂，请使用 smtp_relay 选项。

病毒扫描需要大量内存，建议使用 4-8 GB。
Mailfilter 附加组件默认情况下禁用病毒扫描。

#### 选项：`smtp_relayhost`（可选）

使用此可选设置为出站电子邮件使用中继服务器。ISP 通常会阻止来自您的网络的外发电子邮件。此时，您可以使用您的 ISP 的 SMTP 中继主机来绕过此限制。
最好在方括号内输入主机名。这将禁用该主机的 MX 查找，且是推荐的。您还可以指定要使用的端口。
例如：

```yaml
smtp_relayhost: [smtp.relay.com]:587
```

上述示例表示使用端口 587 进行提交。
如果您的 ISP 要求用户名和密码，请使用以下选项。

#### 选项：`smtp_relayhost_credentials`（可选）

使用此可选设置与您指定的中继服务器进行身份验证。
正确的语法是 username:password，您可以从您的提供商处获得此信息。
仅在您知道确实需要用户凭据进行中继的情况下使用此选项。

## 支持

有问题吗？

您可以 [在这里提出问题][issue] GitHub。

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
[issue]: https://github.com/erik73/addon-mail/issues
[repository]: https://github.com/erik73/hassio-addons