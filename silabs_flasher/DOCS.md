# Home Assistant 插件：Silicon Labs Flasher 插件

## 安装

按照以下步骤将插件安装到您的系统上：

1. 在 Home Assistant 前端导航到 **设置** -> **插件、备份和主管** -> **插件商店**。
2. 查找 "Silicon Labs Flasher" 插件并点击它。
3. 点击 "安装" 按钮。

## 如何使用

插件需要一个可通过串口访问的 Silicon Labs 基于的无线模块（例如 Home Assistant 黄色板上的模块、Home Assistant SkyConnect/ZBT-1 或其他基于 USB 的无线适配器）。

1. 在插件配置选项卡中选择正确的 `device` 并点击 `保存`。
2. 启动插件。

## 配置

插件配置：

| 配置项       | 描述                                          |
|-------------|-----------------------------------------------|
| device (必填) | Silicon Labs 无线模块连接的串口服务             |
| bootloader_baudrate | Gecko 引导加载程序的串口波特率（取决于固件）    |
| ezsp_baudrate       | ezsp 的串口波特率（取决于固件）               |
| flow_control        | 如果硬件流控制应启用（取决于固件）             |
| firmware_url        | 自定义 URL 用于从该 URL 闪存固件             |

## 支持

有疑问？

您有几个选项可以获取答案：

- [Home Assistant Discord 聊天服务器][discord]。
- Home Assistant [社区论坛][forum]。
- 加入 Reddit 的 [homeassistant 子版块][reddit] 在 [/r/homeassistant][reddit]

如果您发现了一个错误，请 [在我们的 GitHub 上打开一个问题][issue]。

[discord]: https://discord.gg/c5DvZ4e
[forum]: https://community.home-assistant.io
[reddit]: https://reddit.com/r/homeassistant
[issue]: https://github.com/home-assistant/addons/issues