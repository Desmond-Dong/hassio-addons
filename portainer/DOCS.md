### **Portainer 的使用**

Portainer 可以用来在 Docker 容器中执行自定义命令。它是一个开源的轻量级管理界面，允许你轻松管理 Docker 主机或 Docker 集群。

# 快速入门
- 使用此链接添加我的仓库
[![在我的 Home Assistant 中添加仓库][repository-badge]][repository-url]
- 从我的仓库安装 portainer 插件
- 在插件的配置面板中，你可以更改密码
- 在插件的主页中，禁用“保护模式”，然后启动插件
- 登录（默认用户名是 `admin`，默认密码是 `homeassistant`）
- 点击环境中的 `Primary`（在页面中央）
- 点击左侧菜单栏中的 `Containers`
- 将每页显示的项目数量增加到查看所有你的插件
- 点击你选择的插件名称旁边的符号 `>_` 打开控制台页面
- 修改用户名，或者更常见的是直接点击连接
- 输入你的命令，你可以完全访问这个特定容器的终端（这不会影响你 HA 系统的其他部分）

# 对你的系统的影响
- 安装或运行 portainer 没有影响
- 手动安装自定义容器将修改你的 HA 状态为不受支持/不健康状态。你将无法升级 Home Assistant 和任何你可能拥有的插件。停止这个自定义容器将重置正常状态

# 小贴士

## 重置数据库
只需更改你的插件选项中的密码，数据库就会被重置

## 60 秒超时
插件包含一个非常长的超时时间。然而，如果你使用另一个层级的代理，例如插件 nginx proxy manager，它将默认设置为 60 秒的超时时间。你需要调整代理层来增加超时时间。更多详情请参考：https://github.com/portainer/portainer/issues/2953#issuecomment-1235795256

## 更多参考
- 这里是一个使用它的完整指南：https://codeopolis.com/posts/beginners-guide-to-portainer/
- Home Assistant 社区论坛上关于 portainer 的旧页面：https://community.home-assistant.io/t/home-assistant-community-add-on-portainer

[repository-badge]: https://img.shields.io/badge/Add%20repository%20to%20my-Home%20Assistant-41BDF5?logo=home-assistant&style=for-the-badge
[repository-url]: https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons