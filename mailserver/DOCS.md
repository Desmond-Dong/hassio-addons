# Home Assistant 插件：邮件服务器

Postfix/Dovecot 邮件服务器与 Postfixadmin Web 界面...

![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield]
![支持 armv7 架构][armv7-shield] ![支持 i386 架构][i386-shield]

## 介绍

重要提示：此插件需要安装并运行 MariaDB 插件！

这个插件是实验性的，并为您的域提供邮件服务器。
还可以在 Postfix Admin Web 界面中配置其他电子邮件域和账户。

该插件使用以下端口：

smtp：端口 25、465 和 587
imap(s)：993

可以在配置的网络部分更改这些设置。

如果您敢于尝试，可以选择将邮件服务器暴露给互联网。
请按照以下说明操作：

要从互联网接收邮件，SMTP 端口必须在路由器中添加重定向。
必要的 MX 和 A 记录需在 DNS 中注册。
如果您希望能够从网络外部检查电子邮件，IMAP 端口也必须进行转发。

默认设置将使用 Dovecot 在初始设置期间生成的自签名证书。
测试时这样可以，但应使用“真实”的证书。

配置选项 "letsencrypt_certs" 设置为 "true" 时，将使用 Home Assistant 中 /ssl 目录下的 fullchain.pem 和 privkey.pem。

## 安装

按照以下步骤在您的系统上安装插件：

添加仓库 `https://github.com/erik73/hassio-addons`。
找到“邮件服务器”插件并点击它。
点击“安装”按钮。

## 如何使用

### 启动插件

安装后，您将看到默认的示例配置。

调整插件配置以符合您的需求。
通过点击“保存”按钮保存插件配置。
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

请注意：在插件启动期间，会在 MariaDB 插件中创建一个数据库。
数据库创建后，当前无法更改用户名或 domain_name。密码可以更改。
更改用户和域名的唯一方法是删除 Postfix Admin 数据库并重启插件。
使用 phpMyadmin 插件删除数据库。

### 选项：`my_hostname`（必填）

您的邮件服务器的主机名。它应与您在 DNS 中的 A 记录相对应。

#### 选项：`domain_name`（必填）

这是您希望接收邮件的域名。
可以在 postfixadmin 界面中添加其他域。

#### 选项：`admin_user`（必填）

postfixadmin 中的管理员用户名。要登录 Web 界面，您必须使用 FQDN。例如：admin@mydomain.no-ip.com。
在当前版本的插件中，数据库创建后无法更改。

#### 选项：`admin_password`（必填）

管理员用户的密码。
此选项在初次安装后可以更改。如果您忘记了密码，这是一项方便的功能！

#### 选项：`letsencrypt_certs`（必填）

如果您使用 Let's Encrypt 插件或以其他方式在 HA 实例的 /ssl 文件夹中安装了证书，此选项将使用这些证书进行 SMTP 和 IMAP 服务。

文件应命名为 fullchain.pem 和 privkey.pem。

#### 选项：`message_size_limit`（必填）

配置单个邮件的最大大小（MB）。
大于此限制的邮件将被拒绝。
如果您希望与常见云邮件提供商有最佳兼容性，请使用 50 MB。
默认值：10

#### 选项：`enable_mailfilter`（必填）

这启用与此仓库中的可选 Mailfilter 插件的通信。
它将使 Postfix 扫描电子邮件以查找垃圾邮件和病毒，并包括可选的 DKIM 签名。为了能够成功发送来自您的主机的电子邮件，而不冒着被拒绝或被归类为垃圾邮件的风险，DKIM 签名是必须的。您还必须配置您的 DNS 服务器以提供 SPF 和 DMARC。
如果 DKIM、SPF 和 DMARC 听起来太复杂，请使用 smtp_relay 选项。

病毒扫描需要大量内存，建议使用 4-8 GB。
在 Mailfilter 插件中，病毒扫描默认是禁用的。

#### 选项：`smtp_relayhost`（可选）

使用此可选设置为外发电子邮件使用中继服务器。互联网服务提供商（ISP）通常会阻止您网络中的外发电子邮件。在这种情况下，您可以使用 ISP 的 SMTP 中继主机来绕过此限制。
推荐在方括号内输入主机名。这将禁用该主机的 MX 查找，并是推荐做法。您还可以指定要使用的端口。
例如：

```yaml
smtp_relayhost: [smtp.relay.com]:587
```

上述示例意味着使用端口 587 进行提交。
如果您的 ISP 需要用户名和密码，请使用以下选项。

#### 选项：`smtp_relayhost_credentials`（可选）

使用此可选设置与您指定的中继服务器进行身份验证。
正确的语法为 username:password，您可以从提供商那里获得此信息。
只有在您确实需要用户凭据进行中继的情况下，才使用此选项。

## 支持

有问题吗？

您可以在这里 [开一个问题][issue] GitHub。

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
[issue]: https://github.com/erik73/addon-mail/issues
[repository]: https://github.com/erik73/hassio-addons