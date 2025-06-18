# Home Assistant 附加组件：Mailfilter

基于 Rspamd 和 ClamAV 的邮件过滤器。

![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield]
![支持 armv7 架构][armv7-shield]

## 关于

重要：此附加组件要求 Mailserver 附加组件已经安装并运行！

此附加组件为您的 Mailserver 附加组件提供实验性的邮件过滤器。
它只能对 Mailserver 附加组件进行邮件过滤。

## 安装

请按照以下步骤在您的系统上安装附加组件：

添加仓库 `https://github.com/erik73/hassio-addons`。
找到“Mailfilter”附加组件并点击它。
点击“INSTALL”按钮。

## 如何使用

### 启动附加组件

安装后，您将看到默认配置。

调整附加组件配置以满足您的需求。
通过点击“SAVE”按钮保存附加组件配置。
启动附加组件。

## 配置

示例配置：

```yaml
enable_antivirus: false
enable_dkim_signing: false
```

请注意：杀毒选项将消耗大量内存。
主机上安装的绝对最低内存为 4GB RAM。
根据其他安装的附加组件，6GB 可能不足以使用。

### 选项：`enable_antivirus`（可选）

启用此选项将启用 ClamAV 病毒扫描器。
有关内存考虑因素，请参见上文。

### 选项：`enable_gtube_tests`（可选）

启用此选项将允许 Rspamd 识别特定于 Rspamd 的 GTUBE 类测试模式。
在生产环境中不建议启用此选项，因为它可能会被用来绕过垃圾邮件检查。仅在测试您的设置时使用！

### 选项：`enable_dkim_signing`（可选）

启用外发邮件的 DKIM 签名。
第一次启用此选项时，将生成一个 DKIM 密钥。
如果您禁用此选项，您的密钥将被删除。
再次启用时将生成新的密钥。
密钥将在日志输出中显示。作为参考，以下是附加组件生成密钥的方式：
rspamadm dkim_keygen -b 2048 -s mail -k /ssl/dkim/mail.key

选择器为 'mail'，并生成一个 2048 位的 rsa 密钥。
mail.key 和 mail.pub 文件保存在 Home Assistant 的 /ssl/dkim 目录中。以下是附加组件日志中的示例输出：

```
mail._domainkey IN TXT ( "v=DKIM1; k=rsa; "
	"p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqdBRCqYzshc4LmmkxUkCH/rcIpSe/QdNIVmBrgqZmZ5zzWQi7ShdFOH7V32/VM1VRk2pkjDV7tmfbwslsymsfxgGhVHbU0R3803uRfxAiT2mYu1hCc9351YpZF4WnrdoA3BT5juS3YUo5LsDxvZCxISnep8VqVSAZOmt8wFsZKBXiIjWuoI6XnWrzsAfoaeGaVuUZBmi4ZTg0O4yl"
	"nVlIz11McdZTRe1FlONOzO7ZkQFb7O6ogFepWLsM9tYJ38TFPteqyO3XBjxHzp1AT0UvsPcauDoeHUXgqbxU7udG1t05f6ab5h/Kih+jisgHHF4ZFK3qRtawhWlA9DtS35DlwIDAQAB"
) ;
```

如果您运行自己的 Bind DNS 服务器，只需将记录直接复制并粘贴到您的域区域文件中。
如果您使用 DNS Web 界面，则需要创建一个新的 TXT 记录，名称为 mail._domainkey，而值/内容则需要删除引号并将所有三行连接在一起。
在我们的情况下，TXT 记录的值/内容应如下所示：

```
v=DKIM1; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqdBRCqYzshc4LmmkxUkCH/rcIpSe/QdNIVmBrgqZmZ5zzWQi7ShdFOH7V32/VM1VRk2pkjDV7tmfbwslsymsfxgGhVHbU0R3803uRfxAiT2mYu1hCc9351YpZF4WnrdoA3BT5juS3YUo5LsDxvZCxISnep8VqVSAZOmt8wFsZKBXiIjWuoI6XnWrzsAfoaeGaVuUZBmi4ZTg0O4ylnVlIz11McdZTRe1FlONOzO7ZkQFb7O6ogFepWLsM9tYJ38TFPteqyO3XBjxHzp1AT0UvsPcauDoeHUXgqbxU7udG1t05f6ab5h/Kih+jisgHHF4ZFK3qRtawhWlA9DtS35DlwIDAQAB
```

当 DKIM 选项关闭时，/ssl/dkim 中的密钥文件将被删除。
如果您再次启用该选项，将创建新的密钥。

## 支持

有问题吗？

可以在这里 [打开问题][issue] GitHub。

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
[issue]: https://github.com/erik73/addon-mailfilter/issues
[repository]: https://github.com/erik73/hassio-addons