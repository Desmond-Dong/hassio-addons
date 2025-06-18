# rtl_433 Home Assistant 插件

## 介绍

这个插件是一个简单的包装器，围绕着优秀的 [rtl_433](https://github.com/merbanan/rtl_433) 项目，该项目通过 [一个受支持的 SDR 转接头](https://triq.org/rtl_433/HARDWARE.html) 接收无线传感器数据，解码并以多种格式（包括 JSON 和 MQTT）输出。rtl_433 理解的无线传感器主要在 433.92 MHz、868 MHz、315 MHz、345 MHz 和 915 MHz ISM 频段内传输数据。

[查看 rtl_433 文档](https://triq.org/rtl_433)

## 工作原理

这个插件的唯一功能是在 Home Assistant OS 监督程序下运行 rtl_433。你所需要做的就是提供一个配置文件。

默认情况下，rtl_433 会将接收到的数据打印到终端 - 你需要配置它以将数据发布到 MQTT，以便 Home Assistant 能够访问这些数据，这可以通过在配置文件中添加一行来完成。

一旦你将 rtl_433 传感器数据发送到 MQTT，你就需要帮助 Home Assistant 发现并理解这些数据。你可以通过多种方式来做到这一点：

  * 手动配置 HA 中的 `sensors` 和 `binary_sensors`，并 [链接到 rtl_433 输出的适当 MQTT 主题](https://www.home-assistant.io/integrations/sensor.mqtt/)，
  * 手动或定期运行 [rtl_433_mqtt_hass.py](https://github.com/merbanan/rtl_433/tree/master/examples/rtl_433_mqtt_hass.py) 脚本，自动完成大部分配置，或
  * 安装 [rtl_433 MQTT 自动发现 Home Assistant 插件](https://github.com/pbkhrv/rtl_433-hass-addons/tree/main/rtl_433_mqtt_autodiscovery)，该插件会为你运行 rtl_433_mqtt_hass.py。

## 先决条件

使用这个插件，你需要以下条件：

 1. [一个受 rtl_433 支持的 SDR 转接头](https://triq.org/rtl_433/HARDWARE.html)。

 2. 在带有 SDR 转接头的机器上运行的 Home Assistant OS。

 3. 一些受 rtl_433 支持的无线传感器。完整的受支持协议和设备列表可以在 [rtl_433 的 README](https://github.com/merbanan/rtl_433/blob/master/README.md) 的“受支持设备协议”部分找到。

## 安装

 1. 创建一个 rtl_433 配置文件，以满足你的需求。如果你在另一台与 Home Assistant OS 不同的计算机上进行操作，会更好，这样你可以自由地进行实验并反复修改，直到找到合适的配置。请参见下文获取更多细节。

 2. 使用你喜欢的任何方法（通过 Samba 插件、ssh/scp、文件编辑器插件等）将配置文件上传到 Home Assistant 的 "/config" 目录。

 3. 安装插件。

 5. 将 SDR 转接头插入运行插件的机器。

 5. 启动插件。默认配置将被创建在 `/config/rtl_433/`。要添加或编辑其他配置，请在该目录中创建多个 `.conf.template` 文件。

 6. 启动插件并检查日志。

## 配置

对于“零配置”设置，安装 [Mosquitto 代理](https://github.com/home-assistant/addons/blob/master/mosquitto/DOCS.md) 插件。尽管其他代理也可能工作，但它们未经测试，并且需要手动设置。安装插件后，启动或重启 rtl_433 和 rtl_433_mqtt_autodiscovery 插件，以开始捕获已知的 433 MHz 协议。

要进行更高级的配置，请查看 rtl_433 源代码中包含的示例配置文件：[rtl_433.example.conf](https://github.com/merbanan/rtl_433/blob/master/conf/rtl_433.example.conf)

请注意，由于配置文件中包含 bash 变量，**美元符号和其他特殊 shell 字符需要转义**。例如，要在配置文件中使用字面字符串 `$GPRMC`，请使用 `\$GPRMC`。

`retain` 选项控制 MQTT 的 `retain` 标志是否默认启用或禁用。可以通过在 `output` 设置中将 `retain` 设置为 `true` 或 `false` 来按无线电单元覆盖。

手动配置时，假设你打算将 rtl_433 数据引入 Home Assistant，在配置文件中你需要指定的最低内容是 [MQTT 连接和认证信息](https://triq.org/rtl_433/OPERATION.html#mqtt-output):

```
output      mqtt://HOST:PORT,user=XXXX,pass=YYYYYYY
```

rtl_433 默认监听 433.92MHz，但即使这正是你需要的，显式指定频率以避免混淆也是一个好主意：

```
frequency   433.92M
```

你可能还想缩小 rtl_433 应该尝试解码的协议列表。完整列表可以在 [README](https://github.com/merbanan/rtl_433/blob/master/README.md) 的“受支持设备协议”部分找到。假设你想监听 Acurite 592TXR 温度/湿度传感器：

```
protocol    40
```

最后但同样重要的是，如果你决定使用 MQTT 自动发现脚本或插件，其文档建议将来自 rtl_433 的所有数据中的单位转换为 SI：

```
convert     si
```

假设你只有一个 USB 转接头连接，并且 rtl_433 能够自动找到它，我们得到了一个最小的 rtl_433 配置文件，如下所示：

```
output      mqtt://HOST:PORT,user=XXXX,pass=YYYYYYY

frequency   433.92M
protocol    40

convert     si
```

请查看 [官方 rtl_433 文档](https://triq.org/rtl_433) 和 [配置文件示例](https://github.com/merbanan/rtl_433/tree/master/conf) 以获取更多信息。

## 版权

这个插件基于 James Fry 的 [rtl4332mqtt Hass.IO 插件](https://github.com/james-fry/hassio-addons/tree/master/rtl4332mqtt)，而该插件又基于 Chris Kacerguis 的项目：[https://github.com/chriskacerguis/honeywell2mqtt](https://github.com/chriskacerguis/honeywell2mqtt)，而该项目又基于 Marco Verleun 的 rtl2mqtt 镜像：[https://github.com/roflmao/rtl2mqtt](https://github.com/roflmao/rtl2mqtt)。