# ESPHome DEV插件

这是**开发**版本的ESPHome插件。

要部署生产节点，请使用主流发布的插件。

该插件使用每天凌晨02:00 UTC自动构建的ESPHome版本，用于测试开发中的组件。查看下面的`esphome_fork`配置以正确配置插件。一旦你更新了配置，请确保重新构建镜像。

## 配置

**注意**: _更改配置时请记住重启插件。_

### 选项: `esphome_fork`

从分支或分支安装ESPHome。
例如，要测试一个拉取请求，使用`pull/XXXX/head`，其中`XXXX`是PR编号，
或者你可以指定分支所有者的用户名和分支`username:branch`，假设仓库名称仍然是`esphome`。

如果你需要在镜像更新前测试dev分支上的最新提交，你可以在其中输入`dev`。

请注意，你正在使用的分支或分支**必须**与ESPHome dev同步，
否则插件**将不会启动**。

## 一般ESPHome插件的配置

常规选项也适用于其他版本。

### 选项: `ssl`

启用或禁用加密的SSL/TLS（HTTPS）连接到此插件的Web服务器。
设置为`true`以加密通信，否则设置为`false`。
请注意，如果你将此设置为`true`，你也必须生成加密的密钥和证书文件。例如使用[Let's Encrypt](https://www.home-assistant.io/addons/lets_encrypt/)
或[自签名证书](https://www.home-assistant.io/docs/ecosystem/certificates/tls_self_signed_certificate/)。

### 选项: `certfile`

用于SSL的证书文件。如果此文件不存在，插件启动将失败。

**注意**: 文件**必须**存储在`/ssl/`中，这是Home Assistant的默认值

### 选项: `keyfile`

用于SSL的私钥文件。如果此文件不存在，插件启动将失败。

**注意**: 文件**必须**存储在`/ssl/`中，这是Home Assistant的默认值

### 选项: `leave_front_door_open`

将此选项添加到插件配置中，允许你通过将其设置为`true`来禁用身份验证。

### 选项: `relative_url`

在相对URL下托管ESPHome仪表板，以便它可以集成到现有的Web代理（如NGINX）的相对URL下。默认值为`/`。

### 选项: `status_use_ping`

默认情况下，仪表板使用mDNS来检查节点是否在线。这不会跨子网工作，除非你的路由器支持mDNS转发或avahi。

将其设置为`true`将使ESPHome使用ICMP ping请求来获取节点状态。如果所有节点即使在连接时也总是显示离线状态，请使用此选项。

### 选项: `streamer_mode`

如果设置为`true`，这将启用流模式，使ESPHome隐藏所有可能包含私人信息的详细信息。例如WiFi (B)SSID（这可能被用来找到你的位置）、用户名等。请注意，你需要在你的YAML文件中使用`!secret`标签来阻止这些信息在编辑和验证时显示出来。