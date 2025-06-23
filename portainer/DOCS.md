Portainer 可以用来在 Docker 容器中执行自定义命令。它是一个开源的轻量级管理 UI，允许您轻松管理 Docker 主机或 Docker Swarm 集群。

# 快速开始
- 使用这个链接添加我的仓库
[![在我的 Home Assistant 上添加仓库][repository-badge]][repository-url]
- 从我的仓库安装 Portainer 附加组件
- 在附加组件的配置面板中，可以更改密码
- 在附加组件的主页面中，禁用“保护模式”，然后启动附加组件
- 登录（默认用户名为 `admin`，默认密码为 `homeassistant`）
- 在环境中点击 `Primary`（在页面中间）
- 在左侧菜单栏中点击 `Containers`
- 增加每页显示的项目数量，以查看所有附加组件
- 点击您所选附加组件名称旁边的 `>_` 符号以打开控制台页面
- 要么更改用户名，或者更常见的是直接点击连接
- 输入您的命令，您对该特定容器的终端拥有完全访问权（这不会影响您 HA 系统的其他部分）

# 对您系统的影响
- 安装或运行 Portainer 不会对系统造成影响
- 手动安装自定义容器会将您的 HA 状态修改为不支持/不健康状态。您将无法升级 Home Assistant 和您可能拥有的任何附加组件。停止此自定义容器将重置正常状态

# 小贴士与技巧

## 重置数据库
只需在您的附加组件选项中更改密码，数据库将被重置

## 超时 60秒
该附加组件包含一个很长的超时时间。然而，如果您使用另一个代理层，例如附加组件 nginx 代理管理器，它将默认超时为 60 秒。您需要调整代理层以增加超时。更多详细信息请访问： https://github.com/portainer/portainer/issues/2953#issuecomment-1235795256

## 进一步参考
- 这里有一个完整的使用指南： https://codeopolis.com/posts/beginners-guide-to-portainer/
- 关于 Portainer 的旧页面在 HA 社区论坛： https://community.home-assistant.io/t/home-assistant-community-add-on-portainer

[repository-badge]: https://img.shields.io/badge/Add%20repository%20to%20my-Home%20Assistant-41BDF5?logo=home-assistant&style=for-the-badge
[repository-url]: https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons