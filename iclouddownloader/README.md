# Home assistant 添加组件：iCloud Downloader

1. 安装组件
1. 运行组件，它将失败，但会为下一步创建我们需要目录
1. 将 iclouddownloader.sh 从此代码库复制到 /addon_configs/2effc9b9_iclouddownloader
1. 编辑命令，输入你的用户名、密码和你想要下载文件的位置
1. 你可以通过复制账户块来添加多个账户，但首先需要让一个账户正常工作！除了最后一个账户之外，所有账户的行尾都应该以 & 结尾，否则组件将在一小时后停止运行
1. 在这里查看所有可能的命令并按你的喜好设置：https://pypi.org/project/icloudpd/1.12.0/
1. 你可以在 Home Assistant 设置->系统->存储中挂载一个 smb/nfs 共享到媒体目录，并指向该位置。位置将是 /media/ShareName/，在该目录下你可以有任意的目录结构，其中 sharename 是你在 homeassistant 中设置的共享名称
1. 运行/重启组件，它将再次失败。（不要点击组件的停止按钮）
1. 选择 1：进入你的 homeassistantIP:8080（或其他你配置的端口）并输入 2FA 代码。Ingress 不起作用
1. 选择 1：现在应该可以下载你的照片
1. 选择 2：在下一个小时内，通过 SSH 登录 home assistant（你必须将 ssh 组件的保护模式设置为 false）
1. 选择 2：运行 'docker exec -it addon_2effc9b9_iclouddownloader /config/iclouddownloader.sh authorize'
1. 选择 2：输入你的 iPhone 上显示的 2fa 代码（你将需要每两个月重复此重新认证步骤）
1. 选择 2：点击 Control-C 或退出终端
1. 选择 2：最后一次重启组件，它应该开始下载照片。

[代码库]: https://github.com/jdeath/homeassistant-addons