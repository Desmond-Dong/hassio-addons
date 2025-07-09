# 家助理件：Roundcube

基于网络的邮件客户端。

![支持aarch64架构][aarch64-shield] ![支持amd64架构][amd64-shield]
![支持armv7架构][armv7-shield]

## 关于

重要提示：此插件需要安装并运行MariaDB插件！

此插件是实验性的，它提供了一个连接到Mailserver插件的Web邮件前端。它还允许您为您的邮箱配置Sieve脚本。

您可以通过点击插件页面中的Web UI按钮来使用ingress功能访问Roundcube界面。使用您的IMAP凭据登录。
如果您想直接访问插件，您可以在可选端口部分指定一个端口。假设您设置了端口2665：
将您的浏览器指向：http://{homeassistant IP}:2665。
如果您启用SSL选项，则它是https://{homeassistant IP}:2665。
也可以使用主机名而不是IP地址。
如果您想将您选择的端口转发到您的路由器，强烈推荐使用HTTPS！

## 安装

按照以下步骤在您的系统上安装插件：

添加仓库 `https://github.com/erik73/hassio-addons`。
找到“Roundcube”插件并点击它。
点击“安装”按钮。

## 如何使用

### 启动插件

安装后，您将看到一个默认和示例配置。

调整插件配置以匹配您的需求。
通过点击“保存”按钮保存插件配置。
启动插件。

## 配置

请注意：在插件启动期间，会在MariaDB插件中创建一个数据库。

### 选项：`ssl`

在Roundcube的Web界面启用/禁用SSL（HTTPS）
将其设置为`true`以启用它，否则设置为`false`。

### 选项：`certfile`

用于SSL的证书文件。

**注意**：_文件必须存储在`/ssl/`中，这是默认的_

### 选项：`keyfile`

用于SSL的私钥文件。

**注意**：_文件必须存储在`/ssl/`中，这是默认的_

## 支持

有问题？

您可以在此处[打开一个GitHub问题][issue]。

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[issue]: https://github.com/erik73/addon-roundcube/issues
[repository]: https://github.com/erik73/hassio-addons