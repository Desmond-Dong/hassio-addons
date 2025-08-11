# Home assistant插件：iCloud Downloader

1. 安装插件
1. 运行插件，它将失败，但会为下一步创建我们需要的目录
1. 将此仓库中的iclouddownloader.sh复制到/addon_configs/2effc9b9_iclouddownloader
1. 编辑命令，输入你的用户名、密码和你想要下载文件的位置
1. 你可以通过复制账户块来添加多个账户，但首先需要让一个账户正常工作！除了最后一个账户之外，所有账户的行尾都应该以&结束，否则插件将在1小时后退出
1. 在这里查看所有可能的命令并按你喜欢的设置：https://pypi.org/project/icloudpd/1.12.0/
1. 你可以在Home Assistant设置->系统->存储中挂载一个smb/nfs共享到媒体目录，并指向该位置。位置将是/media/ShareName/，在该目录下你可以想要的任何目录结构，其中sharename是你在家assistant中命名的共享名
1. 运行/重启插件，它将再次失败。（不要停止插件）
1. 选择1：进入你的homeassistantIP:8080（或其他你配置的端口）并输入2FA代码。Ingress无效
1. 选择1：现在应该会下载你的照片
1. 选择2：在下一个小时内，通过SSH登录home assistant（你必须将ssh插件的保护模式设置为false）
1. 选择2：运行'docker exec -it addon_2effc9b9_iclouddownloader /config/iclouddownloader.sh authorize'
1. 选择2：输入你在iPhone上显示的2fa代码（你将需要每两个月重复此重新认证步骤）
1. 选择2：按Control-C或退出终端
1. 选择2：最后一次重启插件，它应该会开始下载照片。

[repository]: https://github.com/jdeath/homeassistant-addons