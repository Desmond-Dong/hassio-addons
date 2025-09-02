# Home assistant add-on: iCloud Downloader

1. 安装插件
1. 运行插件，它将失败，但会为下一步创建我们需要的目录
1. 将此存储库中的 iclouddownloader.sh 复制到 /addon_configs/2effc9b9_iclouddownloader
1. 编辑命令，输入您的用户名、密码以及您想要下载文件的位置
1. 您可以通过复制帐户块来添加多个帐户，但首先需要让一个帐户工作！除了最后一个帐户外，所有帐户的行尾都应该有 & 结尾，否则插件将在 1 小时后退出
1. 查看这里的所有可能命令并按您喜欢的设置：https://pypi.org/project/icloudpd/1.12.0/
1. 您可以在 Home Assistant 设置->系统->存储中挂载一个 smb/nfs 共享到媒体目录，并指向该位置。位置将是 /media/ShareName/ 以及您希望在下方创建的任何目录结构，其中 sharename 是您在 Home Assistant 中命名的共享名称
1. 运行/重新启动插件，它将再次失败。（不要停止插件）
1. 选择 1：转到您的 homeassistantIP:8080（或您配置的其他端口）并输入 2FA 代码。Ingress 不起作用
1. 选择 1：现在应该下载您的照片
1. 选择 2：在下一个小时中，通过 SSH 登录 Home Assistant（您必须在 ssh 插件中设置保护模式为 false）
1. 选择 2：运行 'docker exec -it addon_2effc9b9_iclouddownloader /config/iclouddownloader.sh authorize'
1. 选择 2：输入您的 iPhone 上显示的 2fa 代码（您将需要每 2 个月重复此重新认证步骤）
1. 选择 2：按 Control-C 或退出终端
1. 选择 2：最后一次重新启动插件，它应该开始下载照片。

[存储库]: https://github.com/jdeath/homeassistant-addons