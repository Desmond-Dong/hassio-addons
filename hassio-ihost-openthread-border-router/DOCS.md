# Home Assistant Add-on: OpenThread Border Router

## 安装

按照以下步骤将插件安装到您的系统上：

1. 在 Home Assistant 前端导航到 **设置** -> **插件、备份和监督器** -> **插件商店**。
2. 点击右上角菜单并选择“仓库”
3. 添加“https://github.com/home-assistant/addons”以添加“Home Assistant 开发插件仓库”。
4. 查找“OpenThread Border Router”插件并点击它。
5. 点击“安装”按钮。

## 如何使用

您需要一个由 OpenThread 支持的 802.15.4 兼容无线电。Home Assistant 黄色以及 Home Assistant SkyConnect/Connect ZBT-1 都可以运行 OpenThread。此插件会自动在这些系统上安装必要的固件。

如果您使用的是 Home Assistant 黄色，请选择 `/dev/ttyAMA1` 作为设备。

> 重要！
>
> 当使用 iHost 的内置 **MG21** 芯片（位于 `/dev/ttyS4`）与此插件一起使用时，必须**禁用硬件流控制**，以便 OpenThread Border Router 正常运行。

![](https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-addon/master/hassio-ihost-openthread-border-router/images/otbr_configuration.png)

### 备选无线电

网站 [openthread.io 维护一个支持的平台的列表][openthread-platforms]，列出了其他支持 Thread 的无线电。一个文档完善的开发无线电是 Nordic Semiconductor 的 [nRF52840 Dongle][nordic-nrf52840-dongle]。Dongle 需要一个较新的 OpenThread RCP 固件版本。
[这篇文章][nordic-nrf52840-dongle-install] 概述了为 nRF52840 Dongle 安装 RCP 固件的步骤。

加载固件后，请按照以下步骤操作：

1. 在插件配置选项卡中选择正确的 `device` 并点击 `保存`。
2. 启动插件。

### OpenThread Border Router

此插件使您的 Home Assistant 安装成为 OpenThread Border Router (OTBR)。边境路由器可用于通过 Thread 组网 Matter 设备。Home Assistant Core 将自动检测此插件并创建一个名为“Open Thread Border Router”的新集成。从 Home Assistant Core 2023.3 开始，OTBR 将自动配置。Thread 集成允许检查网络配置。

### Web 界面（高级）

OTBR 还提供了一个 Web 界面。但是，Web 界面有一些限制（例如，形成网络不会生成一个离链可路由的 IPv6 前缀，这会导致在首次重启插件时更改 IPv6 地址）。仍然可以启用 Web 界面用于调试目的。确保在主机接口上公开 Web UI 端口和 REST API 端口（后者需要在端口 8081 上）。为此，点击“显示禁用端口”并在 OpenThread Web UI 中输入一个端口（例如 8080），在 OpenThread REST API 端口字段中输入 8081。

## 配置

插件配置：

| 配置       | 描述                                                    |
|------------|----------------------------------------------------------|
| device     | OpenThread RCP 无线电连接的串口（必需）                   |
| baudrate   | 串口波特率（取决于固件）                               |
| flow_control | 是否启用硬件流控制（取决于固件）                       |
| autoflash_firmware | 自动安装/更新固件（Home Assistant SkyConnect/Yellow）     |
| otbr_log_level | 设置 OpenThread BorderRouter Agent 的日志级别          |
| firewall   | 启用 OpenThread Border Router 防火墙以阻止不必要的数据流 |
| nat64      | 启用 NAT64 以允许 Thread 设备访问 IPv4 地址              |
| network_device | 连接到基于网络的 RCP 的 IP 地址和端口（见下文）       |

> [!WARNING]
> OTBR 期望连接的 RCP 无线电位于可靠的链路上，如 UART 或 SPI。使用 TCP/IP 来访问远程 RCP 无线电会破坏这一假设。如果 TCP/IP 连接失败，OTBR 将无法干净地关闭，并在您的网络中留下过时的路由。这将导致 Thread 设备在即使其他路由器可用的情况下也可能在长达 30 分钟（路由生命周期）内无法访问。
>
> RCP 协议不是设计为在 IP 网络上传输的：它是一个对时间敏感的协议。如果您的网络链路具有过高的延迟，您可能会遇到 Thread 问题。由于 Thread 具有网络功能，建议在 RCP 无线电插入的系统上运行 Thread 边境路由器。

> [!NOTE]
> 使用网络设备时，您仍然需要设置一个虚拟串口设备，例如 `/dev/ttyS3`。

## 支持

有问题？

您有几个选项可以获取答案：

- [Home Assistant Discord 聊天服务器][discord]。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]。

如果您发现了一个错误，请在我们的 GitHub 上[打开一个问题][issue]。

[discord]: https://discord.gg/c5DvZ4e
[forum]: https://community.home-assistant.io
[reddit]: https://reddit.com/r/homeassistant
[issue]: https://github.com/home-assistant/addons/issues
[openthread-platforms]: https://openthread.io/platforms
[nordic-nrf52840-dongle]: https://www.nordicsemi.com/Products/Development-hardware/nrf52840-dongle
[nordic-nrf52840-dongle-install]: https://docs.nordicsemi.com/bundle/ncs-latest/page/nrf/protocols/thread/tools.html#configuring_a_radio_co-processor