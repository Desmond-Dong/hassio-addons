# rtl_433 Home Assistant 插件

## 关于

这个插件是一个简单的封装，围绕优秀的 [rtl_433](https://github.com/merbanan/rtl_433) 项目，能够通过 [支持的 SDR 适配器之一](https://triq.org/rtl_433/HARDWARE.html) 接收无线传感器数据，解码并以多种格式输出，包括 JSON 和 MQTT。rtl_433 理解的无线传感器主要在 433.92 MHz、868 MHz、315 MHz、345 MHz 和 915 MHz ISM 频段发送数据。

[查看 rtl_433 文档](https://triq.org/rtl_433)

## 工作原理

这个插件唯一的功能是让 rtl_433 在 Home Assistant OS 监督下运行。您所需要做的就是提供一个配置文件。

默认情况下，rtl_433 会将接收到的数据打印到终端——您需要配置它以发布数据到 MQTT，以便 Home Assistant 能够访问它，这可以在配置文件中用一行来完成。

一旦将 rtl_433 传感器数据导入到 MQTT，您需要帮助 Home Assistant 发现并理解这些数据。您可以通过多种方式做到这一点：

  * 手动在 HA 中配置 `sensors` 和 `binary_sensors`，并 [将它们链接到 rtl_433 输出的相应 MQTT 主题](https://www.home-assistant.io/integrations/sensor.mqtt/)，
  * 手动运行 [rtl_433_mqtt_hass.py](https://github.com/merbanan/rtl_433/tree/master/examples/rtl_433_mqtt_hass.py) 脚本，或按计划自动执行以完成大部分配置，或
  * 安装 [rtl_433 MQTT 自动发现 Home Assistant 插件](https://github.com/pbkhrv/rtl_433-hass-addons/tree/main/rtl_433_mqtt_autodiscovery)，该插件会为您运行 rtl_433_mqtt_hass.py。

## 先决条件

要使用此插件，您需要以下内容：

 1. [一个支持 rtl_433 的 SDR 适配器](https://triq.org/rtl_433/HARDWARE.html)。

 2. 在安装了 SDR 适配器的机器上运行的 Home Assistant OS。

 3. 一些支持 rtl_433 的无线传感器。支持的协议和设备的完整列表可以在 [rtl_433 的 README](https://github.com/merbanan/rtl_433/blob/master/README.md) 的“支持的设备协议”部分找到。

## 安装

 1. 创建一个符合您需求的 rtl_433 配置文件。最好在与运行 Home Assistant OS 的计算机不同的计算机上进行此操作，以便您可以自由实验并迭代，直到找到一个良好的配置。有关更多细节，请见下文。

 2. 使用适合您的方法将配置文件上传到 Home Assistant 的 “/config” 目录（通过 Samba 插件、ssh/scp、文件编辑插件等）。

 3. 安装插件。

 5. 将您的 SDR 适配器插入运行插件的机器。

 5. 启动插件。一个默认的配置将被创建在 `/config/rtl_433/`。要添加或编辑额外的配置，请在该目录中创建多个 `.conf.template` 文件。

 6. 启动插件并检查日志。

## 配置

对于“零配置”设置，请安装 [Mosquitto broker](https://github.com/home-assistant/addons/blob/master/mosquitto/DOCS.md) 插件。虽然其他代理可能工作，但未经过测试，需要手动设置。一旦插件安装完成，启动或重新启动 rtl_433 和 rtl_433_mqtt_autodiscovery 插件，以开始抓取已知的 433 MHz 协议。

有关更高级的配置，请查看 rtl_433 源代码中包含的示例配置文件：[rtl_433.example.conf](https://github.com/merbanan/rtl_433/blob/master/conf/rtl_433.example.conf)

请注意，由于配置文件中包含 bash 变量，**美元符号和其他特殊 shell 字符需要转义**。例如，要在配置文件中使用字面字符串 `$GPRMC`，请使用 `\$GPRMC`。

`retain` 选项控制 MQTT 的 `retain` 标志是默认启用还是禁用。可以通过在 `output` 设置中将 `retain` 设置为 `true` 或 `false` 来针对每个无线电进行覆盖。

当手动配置时，假设您打算将 rtl_433 数据导入到 Home Assistant，您在配置文件中需要指定的绝对最小内容是 [MQTT 连接和认证信息](https://triq.org/rtl_433/OPERATION.html#mqtt-output):

```
output      mqtt://HOST:PORT,user=XXXX,pass=YYYYYYY
```

rtl_433 默认监听 433.92MHz，但即使这就是您需要的，明确指定频率也是个好主意，以避免混淆：

```
frequency   433.92M
```

您可能还希望缩小 rtl_433 应尝试解码的协议列表。完整列表可以在 [README](https://github.com/merbanan/rtl_433/blob/master/README.md) 的“支持的设备协议”部分找到。假设您想监听 Acurite 592TXR 温度/湿度传感器：

```
protocol    40
```

最后但同样重要的是，如果您决定使用 MQTT 自动发现脚本或插件，其文档建议将 rtl_433 输出的所有数据中的单位转换为国际单位制 (SI)：

```
convert     si
```

假设您只有一个 USB 适配器连接，并且 rtl_433 能够自动找到它，我们得到一个最小的 rtl_433 配置文件，如下所示：

```
output      mqtt://HOST:PORT,user=XXXX,pass=YYYYYYY

frequency   433.92M
protocol    40

convert     si
```

有关更多信息，请查看 [官方 rtl_433 文档](https://triq.org/rtl_433) 和 [配置文件示例](https://github.com/merbanan/rtl_433/tree/master/conf)。

## 版权

这个插件基于 James Fry 的 [rtl4332mqtt Hass.IO 插件](https://github.com/james-fry/hassio-addons/tree/master/rtl4332mqtt)，而后者又基于 Chris Kacerguis 的项目：[https://github.com/chriskacerguis/honeywell2mqtt](https://github.com/chriskacerguis/honeywell2mqtt)，而后者又基于 Marco Verleun 的 rtl2mqtt 镜像：[https://github.com/roflmao/rtl2mqtt](https://github.com/roflmao/rtl2mqtt)。