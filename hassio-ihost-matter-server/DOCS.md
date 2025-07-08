# Home Assistant 添加组件：Matter 服务器

## 安装

按照以下步骤安装此添加组件。

1. 点击 Home Assistant 下的 My 按钮，在您的 Home Assistant 实例上打开添加组件页面。

   [![在您的 Home Assistant 实例中打开此添加组件。][addon-badge]][ addon ]

1. 点击“安装”按钮来安装添加组件。

## 如何使用

启动 Matter 服务器添加组件，使 WebSocket 对 Home Assistant Core 可用。在 Home Assistant Core 中安装 [Matter 集成][matter_integration]。

### 外部访问 WebSocket 接口（高级）

默认情况下，Python Matter 服务器的 WebSocket 接口仅在内部暴露。仍然可以通过主机接口启用访问。为此，点击“显示禁用端口”，并在 Matter 服务器 WebSocket 服务器端口字段中输入一个端口（例如 5580）。

## 配置

添加组件配置：

| 配置         | 描述                                                         |
|-------------|--------------------------------------------------------------|
| log_level   | Matter 服务器组件的日志级别。                               |
| log_level_sdk | Matter SDK 日志的日志级别。                               |
| beta        | 是否在启动时安装最新 beta 版本                               |
| enable_test_net_dcl | 启用用于 PAA 根证书和其他设备信息的测试网 DCL。          |
| bluetooth_adapter_id | 设置 BlueZ 蓝牙控制器 ID（用于本地配置） |

## 支持

有问题？

您有几个选项来获得答案：

- [Home Assistant Discord 聊天服务器][discord]。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

如果您发现了一个错误，请 [在我们的 GitHub 上打开一个问题][issue]。

[addon]: https://my.home-assistant.io/redirect/supervisor_addon/? addon=core_matter_server
[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[discord]: https://discord.gg/c5DvZ4e
[forum]: https://community.home-assistant.io
[reddit]: https://reddit.com/r/homeassistant
[issue]: https://github.com/home-assistant/addons/issues
[matter_server_repo]: https://github.com/home-assistant-libs/python-matter-server
[matter_integration]: https://www.home-assistant.io/integrations/matter/