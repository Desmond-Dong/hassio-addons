# Home Assistant 添加组件：邮件服务器

Postfix/Dovecot 邮件服务器，带 Postfixadmin 网页界面...

![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield]
![支持 armv7 架构][armv7-shield] ![支持 i386 架构][i386-shield]

## 关于

重要提示：此添加组件需要 MariaDB 添加组件已安装并运行！

此添加组件是实验性的，为您的域名提供邮件服务器。
也可以在 Postfix Admin 网页界面中配置额外的电子邮件域名和帐户。

此添加组件使用的端口如下：

smtp：端口 25、465 和 587
imap(s)：993
managesieve：4190
(ManageSieve 允许用户使用支持 Sieve 协议的邮件客户端创建自己的 Sieve 脚本)

可以在配置的网络部分更改这些端口。

关于端口 465 的说明：虽然它曾经是安全 SMTP 提交的标准端口，但现在已被端口 587 取代。尽管端口 465 仍然被一些旧电子邮件系统和客户端支持，但大多数现代设置现在使用端口 587，因为它被认为更健壮和灵活。

如果您勇敢，您可能希望将邮件服务器暴露给互联网。
请参阅以下说明：

要从互联网接收邮件，需要在您的路由器中为重定向添加 SMTP 端口，端口 465 除外（请参阅上面关于端口 465 的说明）。
需要在 DNS 中注册必要的 MX 和 A 记录。
如果您希望能够在您的网络外部检查电子邮件，还需要转发 IMAP 端口。

默认设置将使用 Dovecot 在初始设置期间创建的自签名证书。这对于测试是可以的，但应该使用“真实”证书。

配置选项 "letsencrypt_certs" 如果设置为 "true"，将使用 Home Assistant 中的 /ssl 目录中的 fullchain.pem 和 privkey.pem。

## 安装

按照以下步骤在您的系统上安装此添加组件：

添加仓库 `https://github.com/erik73/hassio-addons`。
找到“邮件服务器”添加组件并点击它。
点击“安装”按钮。

## 如何使用

### 启动添加组件

安装后，您将看到一个默认和示例配置。

调整添加组件配置以匹配您的需求。
通过点击“保存”按钮保存添加组件配置。
启动添加组件。

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

请注意：在启动添加组件时，MariaDB 添加组件中会创建一个数据库。在数据库创建后，目前无法更改用户名或 domain_name。密码可以更改。
更改用户和域名的方法是删除 Postfix Admin 数据库并重新启动添加组件。
使用 phpMyadmin 添加组件删除数据库。

### 选项：`my_hostname`（必需）

您的邮件服务器的主机名。它应与您 DNS 中的 A 记录对应。

#### 选项：`domain_name`（必需）

这是您希望接收邮件的域名。
可以在 postfixadmin 界面中添加额外的域名。

#### 选项：`admin_user`（必需）

Postfixadmin 中的管理员用户名。要登录到网页界面，您必须使用 FQDN。例如：admin@mydomain.no-ip.com。
在添加组件的当前版本中，一旦数据库创建，此选项不能更改。

#### 选项：`admin_password`（必需）

管理员用户的密码。
此选项可以在初始安装后更改。如果您忘记密码，这是一个方便的功能！

#### 选项：`letsencrypt_certs`（必需）

如果您使用 Let’s Encrypt 添加组件或通过其他任何方式在您的 HA 实例的 /ssl 文件夹中安装了证书，此选项将使用这些证书为 SMTP 和 IMAP 服务。

文件应命名为 fullchain.pem 和 privkey.pem。

#### 选项：`message_size_limit`（必需）

配置单个消息/邮件的最大大小（以 MB 为单位）。
大于此大小的消息将被拒绝。
如果您希望与常见的云邮件提供者具有最佳兼容性，请使用 50 MB。
默认值：10

#### 选项：`enable_mailfilter`（必需）

此选项启用与此仓库中的可选 Mailfilter 添加组件的通信。
它将启用 Postfix 扫描电子邮件中的垃圾邮件和病毒，并包括可选的 DKIM 签名。为了能够成功地从您的主机发送电子邮件，而不会导致您的传出电子邮件被拒绝或被分类为垃圾邮件，DKIM 签名是必不可少的。您还必须配置您的 DNS 服务器以提供 SPF 和 DMARC。
如果 DKIM、SPF 和 DMARC 听起来太复杂，请使用 smtp_relay 选项。

病毒扫描需要大量的内存，建议使用 4-8 GB。
Mailfilter 添加组件默认禁用病毒扫描。

#### 选项：`smtp_relayhost`（可选）

使用此可选设置来使用中继服务器发送传出电子邮件。ISP 通常会阻止从您的网络发送传出电子邮件。在这种情况下，您可以使用您的 ISP 的 SMTP 中继主机来绕过此限制。
通常建议在括号内输入主机名。它禁用该主机的 MX 查找，并推荐使用。您还可以指定要使用的端口。例如：

```yaml
[smtp.relay.com]:587
```

上述示例表示端口 587 用于提交。
如果您的 ISP 要求用户名和密码，请使用以下选项。

#### 选项：`smtp_relayhost_credentials`（可选）

使用此可选设置来使用您指定 的中继服务器进行身份验证。正确的语法是 username:password，您可以从提供者那里获得这些信息。
只有在您确实知道需要用户凭证来中继时，才使用此选项。

#### 选项：`mynetworks`（可选）

如果您希望允许特定的网络或 IP 地址通过此服务器中继电子邮件，请使用此可选设置。此选项仅适用于内部网络或主机。在使用它之前，请务必阅读 Postfix 文档，了解设置此选项的安全影响。

```yaml
192.168.1.0/24 192.168.3.12
```

## 支持

有问题？

您可以在此处 [打开问题][issue] GitHub。

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
[issue]: https://github.com/erik73/addon-mail/issues
[repository]: https://github.com/erik73/hassio-addons