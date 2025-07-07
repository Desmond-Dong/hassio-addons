# Home Assistant Add-on: Mailfilter

基于 Rspamd 和 ClamAV 的 Mailfilter。

![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield]
![支持 armv7 架构][armv7-shield]

## 关于

重要提示：此插件需要 Mailserver 插件已安装并正在运行！

此插件是实验性的，为您的 Mailserver 插件提供邮件过滤器。
它只能过滤 Mailserver 插件中的邮件。

## 安装

按照以下步骤在您的系统上安装插件：

添加仓库 `https://github.com/erik73/hassio-addons`。
找到 "Mailfilter" 插件并点击它。
点击 "INSTALL" 按钮。

## 如何使用

### 启动插件

安装后，您将看到一个默认配置。

调整插件配置以匹配您的需求。
点击 "SAVE" 按钮保存插件配置。
启动插件。

## 配置

示例配置：

```yaml
enable_antivirus: false
enable_dkim_signing: false
```

请注意：防病毒选项将消耗大量内存。
最低要求是在主机上安装 4GB 的 RAM。
根据安装的其他插件，6GB 可能仍然不够。

### 选项：`enable_antivirus` (可选)

启用此选项将启用 ClamAV 病毒扫描器。
有关内存考虑的详细信息，请参阅上文。

### 选项：`enable_gtube_tests` (可选)

启用此选项将使 Rspamd 能够识别 GTUBE 类似的特定于 Rspamd 的测试模式。不推荐在生产环境中启用此选项，因为它可能会被用来绕过垃圾邮件检查。仅在测试您的设置时使用它！

### 选项：`enable_dkim_signing` (可选)

为发出的邮件启用 DKIM 签名。
启用此选项后第一次启动时，将生成一个 DKIM 密钥。
如果您关闭此选项，您的密钥将被删除。
再次启用它将生成新的密钥。
密钥将显示在日志输出中。以下是插件如何生成密钥的示例：

```
rspamadm dkim_keygen -b 2048 -s mail -k /ssl/dkim/mail.key
```

选择器是 'mail'，生成一个 2048 位的 RSA 密钥。
mail.key 和 mail.pub 文件保存在 Home Assistant 的 /ssl/dkim 目录中。
以下是插件日志中的示例输出：

```
mail._domainkey IN TXT ( "v=DKIM1; k=rsa; "
	"p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqdBRCqYzshc4LmmkxUkCH/rcIpSe/QdNIVmBrgqZmZ5zzWQi7ShdFOH7V32/VM1VRk2pkjDV7tmfbwslsymsfxgGhVHbU0R3803uRfxAiT2mYu1hCc9351YpZF4WnrdoA3BT5juS3YUo5LsDxvZCxISnep8VqVSAZOmt8wFsZKBXiIjWuoI6XnWrzsAfoaeGaVuUZBmi4ZTg0O4yl"
	"nVlIz11McdZTRe1FlONOzO7ZkQFb7O6ogFepWLsM9tYJ38TFPteqyO3XBjxHzp1AT0UvsPcauDoeHUXgqbxU7udG1t05f6ab5h/Kih+jisgHHF4ZFK3qRtawhWlA9DtS35DlwIDAQAB"
) ;
```

如果您正在运行自己的 Bind DNS 服务器，只需将记录直接复制粘贴到您的域区域文件中。
如果您使用 DNS 网络界面，则需要创建一个新的 TXT 记录，将 mail.\_domainkey 作为名称，而值/内容则需要删除引号并将所有三行连接在一起。
在这种情况下，TXT 记录的值/内容应如下所示：

```
v=DKIM1; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqdBRCqYzshc4LmmkxUkCH/rcIpSe/QdNIVmBrgqZmZ5zzWQi7ShdFOH7V32/VM1VRk2pkjDV7tmfbwslsymsfxgGhVHbU0R3803uRfxAiT2mYu1hCc9351YpZF4WnrdoA3BT5juS3YUo5LsDxvZCxISnep8VqVSAZOmt8wFsZKBXiIjWuoI6XnWrzsAfoaeGaVuUZBmi4ZTg0O4ylnVlIz11McdZTRe1FlONOzO7ZkQFb7O6ogFepWLsM9tYJ38TFPteqyO3XBjxHzp1AT0UvsPcauDoeHUXgqbxU7udG1t05f6ab5h/Kih+jisgHHF4ZFK3qRtawhWlA9DtS35DlwIDAQAB
```

当 DKIM 选项关闭时，/ssl/dkim 中的密钥文件将被删除。
如果您再次启用该选项，将创建一个新的密钥。

## 支持

有问题？

您可以在此处 [打开问题][issue] GitHub。

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
[issue]: https://github.com/erik73/addon-mailfilter/issues
[repository]: https://github.com/erik73/hassio-addons