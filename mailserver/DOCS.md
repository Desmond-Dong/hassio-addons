# Home Assistant 附加组件: 邮件服务器

Postfix/Dovecot 邮件服务器及 Postfixadmin web 界面...

![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield]
![支持 armv7 架构][armv7-shield] ![支持 i386 架构][i386-shield]

## 关于

重要提示: 此附加组件需要安装并运行 MariaDB 附加组件!

此附加组件为您的域提供邮件服务器，属于实验性质。
还可以在 Postfix Admin web 界面中配置其他电子邮件域和帐户。

此附加组件使用以下端口：

smtp：端口 25、465 和 587
imap(s)：993

可以在配置的网络部分更改这些端口。

如果您胆子大，您可能想要将邮件服务器暴露在互联网上。
请参见下面的说明：

要从互联网上接收邮件，SMTP 端口必须在您的路由器中进行重定向。
必须在 DNS 中注册必要的 MX 和 A 记录。
如果您希望能够从您的网络外部检查电子邮件，IMAP 端口也必须被转发。

默认设置将使用 Dovecot 在初始设置期间创建的自签名证书。
这在测试时是可以的，但应该使用“真实”证书。

配置选项“letsencrypt_certs”如果设置为“true”，则将在 Home Assistant 的 /ssl 目录中使用 fullchain.pem 和 privkey.pem。

## 安装

按照以下步骤在您的系统上安装附加组件：

添加库 `https://github.com/erik73/hassio-addons`。
找到 "Mailserver" 附加组件并单击它。
点击 "安装" 按钮。

## 如何使用

### 启动附加组件

安装后，您将看到默认和示例配置。

调整附加组件配置以满足您的需求。
通过点击 "保存" 按钮保存附加组件配置。
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

请注意：在附加组件启动期间，会在 MariaDB 附加组件中创建一个数据库。目前在数据库创建后无法更改用户名或域名。可以更改密码。
更改用户和域名的唯一方法是删除 Postfix Admin 数据库并重启附加组件。
使用 phpMyadmin 附加组件删除数据库。

### 选项: `my_hostname` (必需)

您的邮件服务器的主机名。它应与您在 DNS 中的 A 记录相对应。

#### 选项: `domain_name` (必需)

这是您希望接收邮件的域名。
可以在 postfixadmin 界面中添加其他域名。

#### 选项: `admin_user` (必需)

Postfixadmin 中的管理员用户名。要登录到 web 界面，您必须使用 FQDN。例如：admin@mydomain.no-ip.com。
在当前版本的附加组件中，一旦数据库创建后，这个值无法更改。

#### 选项: `admin_password` (必需)

管理员用户的密码。
此选项可以在初始安装后更改。如果您忘记了密码，这是一项方便的功能！

#### 选项: `letsencrypt_certs` (必需)

如果您使用 Let´s Encrypt 附加组件或以其他方式在 HA 实例的 /ssl 文件夹中安装了证书，则此选项将使用这些证书用于 SMTP 和 IMAP 服务。

文件应命名为 fullchain.pem 和 privkey.pem。

#### 选项: `message_size_limit` (必需)

配置单个邮件的最大大小，以 MB 为单位。
大于此大小的邮件将被拒绝。
如果您希望与普通云邮件提供商兼容，请使用 50 MB。
默认值：10

#### 选项: `enable_mailfilter` (必需)

这将启用与此库中可选 Mailfilter 附加组件的通信。
它将使 Postfix 扫描电子邮件中的垃圾邮件和病毒，并包含可选的 DKIM 签名。为了能够成功地从您的主机发送邮件，而不必担心您的外发邮件被拒绝或被归类为垃圾邮件，DKIM 签名是必须的。您还必须配置您的 DNS 服务器以提供 SPF 和 DMARC。如果 DKIM、SPF 和 DMARC 听起来太复杂，请使用 smtp_relay 选项。

病毒扫描需要大量内存，建议 4-8 GB。
病毒扫描在 Mailfilter 附加组件中默认禁用。

#### 选项: `smtp_relayhost` (可选)

使用此可选设置为外发电子邮件使用中继服务器。ISP 通常会阻止您网络中的外发电子邮件。在这种情况下，您可以使用 ISP 的 SMTP 中继主机来绕过此限制。
输入主机名时使用括号是良好的做法。这将禁用对该主机的 MX 查询，并且是推荐的。您还可以指定要使用的端口。
例如：

```yaml
smtp_relayhost: [smtp.relay.com]:587
```

上述示例表示使用端口 587 进行提交。
如果您的 ISP 需要用户名和密码，使用下面的选项。

#### 选项: `smtp_relayhost_credentials` (可选)

使用此可选设置对您指定的中继服务器进行身份验证。
正确的语法是用户名：密码，您可以从提供商处获得此信息。
仅在您知道用户凭据确实需要以进行中继时使用此选项。

## 支持

有问题吗？

您可以在 [这里提出问题][issue] GitHub。

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
[issue]: https://github.com/erik73/addon-mail/issues
[repository]: https://github.com/erik73/hassio-addons