# Home assistant 插件：iCloud Downloader

1. 安装插件
1. 运行插件，它将失败，但会为下一步创建我们需要目录
1. 将此仓库中的 iclouddownloader.sh 复制到 /addon_configs/2effc9b9_iclouddownloader
1. 编辑命令，使用你的用户名、密码和你想要下载文件的位置
1. 你可以通过复制账户块来添加多个账户，但首先要让一个账户正常工作！除了最后一个账户外，所有账户的行尾都应该有 & 结尾，否则插件将在 1 小时后退出
1. 在这里查看所有可能的命令并按你喜欢的设置：https://pypi.org/project/icloudpd/1.12.0/
1. 你可以在 Home Assistant 设置->系统->存储中挂载一个 smb/nfs 共享到媒体目录，并指向该位置。位置将是 /media/ShareName/，并在该位置下你可以想要的任何目录结构，其中 sharename 是你在 Home Assistant 中命名的共享名
1. 运行/重启插件，它将再次失败。（不要停止插件）
1. 选项 1：进入你的 homeassistantIP:8080（或其他你配置的端口），并输入 2FA 代码。Ingress 不起作用
1. 选项 1：现在应该下载你的照片
1. 选项 2：在接下来的小时内，通过 SSH 登录 Home Assistant（你必须将 ssh 插件的保护模式设置为 false）
1. 选项 2：运行 'docker exec -it addon_2effc9b9_iclouddownloader /config/iclouddownloader.sh authorize'
1. 选项 2：输入你在 iPhone 上显示的 2fa 代码（你将需要每 2 个月重复此重新认证步骤）
1. 选项 2：按 Control-C 或退出终端
1. 选项 2：最后一次重启插件，它应该开始下载照片。





[repository]: https://github.com/jdeath/homeassistant-addons