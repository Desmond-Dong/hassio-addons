Portainer可以用来在Docker容器中执行自定义命令。它是一个开源的轻量级管理用户界面，让你可以轻松管理Docker主机或Docker集群。

# 快速开始
- 使用此链接添加我的仓库
[![在我的Home Assistant中添加仓库][repository-badge]][repository-url]
- 从我的仓库安装portainer附加组件
- 在附加组件的配置面板中，你可以更改密码
- 在附加组件的主页上，禁用“保护模式”，然后启动附加组件
- 登录（默认用户名是`admin`，默认密码是`homeassistant`）
- 点击环境中的`Primary`（在页面中央）
- 在左侧菜单栏中点击`Containers`
- 增加每页显示的项目数量，以查看所有附加组件
- 点击所选附加组件名称旁边的符号`>_`以打开控制台页面
- 更改用户名，或更常见的是直接点击连接
- 输入你的命令，你对这个特定容器的终端有完全的访问权限（这不会影响你HA系统的其他部分）

# 对你系统的影响
- 安装或运行portainer没有影响
- 手动安装自定义容器将使你的HA状态变为不支持/不健康状态。你将无法升级Home Assistant和任何你可能有的附加组件。停止此自定义容器将重置为正常状态

# 提示与技巧

## 重置数据库
只需在你的附加组件选项中更改密码，数据库将被重置

## 60秒超时
此附加组件包括一个非常长的超时。然而，如果你使用另一个代理层，例如附加组件nginx代理管理器，它的默认超时将为60秒。你需要调整代理层以增加超时。更多详情请见：https://github.com/portainer/portainer/issues/2953#issuecomment-1235795256

## 进一步参考
- 这是一个使用它的完整指南：https://codeopolis.com/posts/beginners-guide-to-portainer/
- 关于portainer的HA社区论坛旧页面：https://community.home-assistant.io/t/home-assistant-community-add-on-portainer

[repository-badge]: https://img.shields.io/badge/Add%20repository%20to%20my-Home%20Assistant-41BDF5?logo=home-assistant&style=for-the-badge
[repository-url]: https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons