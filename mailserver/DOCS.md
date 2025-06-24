# Home Assistant 插件：邮件服务器

Postfix/Dovecot 邮件服务器，带有 Postfixadmin Web 界面...

![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield]
![支持 armv7 架构][armv7-shield] ![支持 i386 架构][i386-shield]

## 关于

重要提示：此插件需要已安装并运行 MariaDB 插件！

此插件为您的域提供一个邮件服务器，属于实验性插件。
也可以在 Postfix Admin Web 界面中配置其他电子邮件域和账户。

此插件使用以下端口：

smtp：端口 25、465 和 587
imap(s)：993

可以在配置的网络部分更改这些端口。

如果您勇敢，可以考虑将邮件服务器暴露到互联网。
请参见以下说明：

要从互联网接收邮件，必须在路由器中为 SMTP 端口添加重定向。
所需的 MX 和 A 记录必须在 DNS 中注册。
如果您希望能够从网络外部检查电子邮件，IMAP 端口也必须转发。

默认设置将使用 Dovecot 在初始设置过程中创建的自签名证书。这对于测试是可以的，但应使用“真实”证书。

配置选项 "letsencrypt_certs" 如果设置为 "true"，则将使用位于 Home Assistant /ssl 目录中的 fullchain.pem 和 privkey.pem。

## 安装

按照以下步骤在系统上安装插件：

添加仓库 `https://github.com/erik73/hassio-addons`。
找到 "邮件服务器" 插件并点击。
点击 "安装" 按钮。

## 如何使用

### 启动插件

安装后将展示默认和示例配置。

调整插件配置以匹配您的要求。
通过单击 "保存" 按钮来保存插件配置。
启动插件。

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

请注意：在插件启动期间，将在 MariaDB 插件中创建一个数据库。目前在数据库创建后无法更改用户名或域名。密码可以更改。唯一更改用户和域名的方法是删除 Postfix Admin 数据库并重新启动插件。使用 phpMyadmin 插件删除数据库。

### 选项：`my_hostname`（必需）

邮件服务器的主机名。应与您在 DNS 中的 A 记录相对应。

#### 选项：`domain_name`（必需）

这是您希望接收邮件的域名。
可以在 postfixadmin 界面中添加其他域。

#### 选项：`admin_user`（必需）

Postfixadmin 中的管理员用户名。要登录 Web 界面，您必须使用 FQDN。例如：admin@mydomain.no-ip.com。
在当前版本的插件中，一旦创建数据库，这个值不能更改。

#### 选项：`admin_password`（必需）

管理员用户的密码。
此选项可以在初始安装后更改。如果您忘记密码，这是一个方便的功能！

#### 选项：`letsencrypt_certs`（必需）

如果您使用 Let´s Encrypt 插件或以其他方式在 HA 实例的 /ssl 文件夹中安装了证书，此选项将使用这些证书为 SMTP 和 IMAP 服务。

文件应命名为 fullchain.pem 和 privkey.pem。

#### 选项：`message_size_limit`（必需）

配置单个消息/邮件的最大大小（以 MB 为单位）。
大于此大小的邮件将被拒绝。
如果希望与常见的云邮件提供商保持最佳兼容性，请使用 50 MB。
默认：10

#### 选项：`enable_mailfilter`（必需）

这启用与此仓库中可选的 Mailfilter 插件的通信。
它将启用 Postfix 扫描电子邮件以查找垃圾邮件和病毒，并包含可选的 DKIM 签名。
为了能够成功发送来自您的主机的电子邮件，而不冒被拒绝或被归类为垃圾邮件的风险，DKIM 签名是必须的。
您还需要配置 DNS 服务器以提供 SPF 和 DMARC。
如果 DKIM、SPF 和 DMARC 听起来太复杂，可以使用 smtp_relay 选项。

病毒扫描需要大量内存，建议使用 4-8 GB。
Mailfilter 插件中默认情况下禁用病毒扫描。

#### 选项：`smtp_relayhost`（可选）

使用此可选设置为传出邮件使用中继服务器。ISP 通常会阻止来自您的网络的传出邮件。在这种情况下，您可以使用您的 ISP 的 SMTP 中继主机来绕过此限制。
输入主机名时使用方括号是好的做法。它禁用该主机的 MX 查找，是推荐的做法。您还可以指定要使用的端口。
例如：

```yaml
smtp_relayhost: [smtp.relay.com]:587
```

上面的示例表示端口 587 用于提交。
如果您的 ISP 要求用户名和密码，请使用下面的选项。

#### 选项：`smtp_relayhost_credentials`（可选）

使用此可选设置与您指定的中继服务器进行身份验证。
正确的语法是 username:password，您可以从提供商那里获得这些信息。
只有在确实需要用户凭据以进行中继时才使用此选项。

## 支持

有问题吗？

您可以在 [GitHub 上打开一个问题][issue]。

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
[issue]: https://github.com/erik73/addon-mail/issues
[repository]: https://github.com/erik73/hassio-addons