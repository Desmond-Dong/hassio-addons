# rtl_433 Home Assistant Add-on

## 关于

这个插件是一个围绕优秀的 [rtl_433](https://github.com/merbanan/rtl_433) 项目的简单包装，它通过 [一个支持的 SDR 捅件](https://triq.org/rtl_433/HARDWARE.html) 接收无线传感器数据，解码并以多种格式输出，包括 JSON 和 MQTT。无线传感器 rtl_433 主要在 433.92 MHz、868 MHz、315 MHz、345 MHz 和 915 MHz ISM 频段上传输数据。

[查看 rtl_433 文档](https://triq.org/rtl_433)

## 工作原理

这个插件所做的唯一事情是在 Home Assistant OS 监督器下运行 rtl_433。您需要做的是提供一个配置文件。

默认情况下，rtl_433 将其接收到的数据打印到终端——您需要配置它以将数据发布到 MQTT，以便 Home Assistant 可以访问它，这可以通过配置文件中的一行来完成。

一旦您将 rtl_433 传感器数据放入 MQTT，您就需要帮助 Home Assistant 发现并理解它。您可以通过以下几种方式来做：

  * 手动配置 HA 中的 `sensors` 和 `binary_sensors`，并将它们与从 rtl_433 输出的相应 MQTT 主题 [链接起来](https://www.home-assistant.io/integrations/sensor.mqtt/)，
  * 手动或在计划中运行 [rtl_433_mqtt_hass.py](https://github.com/merbanan/rtl_433/tree/master/examples/rtl_433_mqtt_hass.py) 脚本来自动完成大部分配置，或者
  * 安装 [rtl_433 MQTT 自动发现 Home Assistant 插件](https://github.com/pbkhrv/rtl_433-hass-addons/tree/main/rtl_433_mqtt_autodiscovery)，它会为您运行 rtl_433_mqtt_hass.py。

## 前置条件

要使用这个插件，您需要以下条件：

 1. [一个被 rtl_433 支持的 SDR 捅件](https://triq.org/rtl_433/HARDWARE.html)。

 2. 在一个插入 SDR 捅件的机器上运行的 Home Assistant OS。

 3. 一些被 rtl_433 支持的无线传感器。支持协议和设备的完整列表可以在 [rtl_433 的 README](https://github.com/merbanan/rtl_433/blob/master/README.md) 的“支持的设备协议”部分找到。

## 安装

 1. 创建一个满足您需求的 rtl_433 配置文件。如果您在运行 Home Assistant OS 的计算机之外完成此操作，可能会更好，这样您就可以自由地实验并迭代，直到找到一个工作良好的配置。下面有更多详细信息。

 2. 使用您喜欢的方法（通过 Samba 插件、ssh/scp、文件编辑器插件等）将配置文件上传到 Home Assistant 的 "/config" 目录。

 3. 安装插件。

 4. 将您的 SDR 捅件插入运行插件的机器。

 5. 启动插件。将创建一个默认配置在 `/config/rtl_433/`。要添加或编辑其他配置，请在该目录中创建多个 `.conf.template` 文件。

 6. 启动插件并检查日志。

## 配置

对于“零配置”设置，安装 [Mosquitto 中继](https://github.com/home-assistant/addons/blob/master/mosquitto/DOCS.md) 插件。虽然其他中继可能也可以工作，但它们未经测试并需要手动设置。安装插件后，启动或重新启动 rtl_433 和 rtl_433_mqtt_autodiscovery 插件以开始捕获已知的 433 MHz 协议。

对于更高级的配置，请查看 rtl_433 源代码中包含的示例配置文件：[rtl_433.example.conf](https://github.com/merbanan/rtl_433/blob/master/conf/rtl_433.example.conf)

请注意，由于配置文件中包含 bash 变量，**美元符号和其他特殊 shell 字符需要转义**。例如，要在配置文件中使用字面字符串 `$GPRMC`，请使用 `\$GPRMC`。

`retain` 选项控制 MQTT 的 `retain` 标志是默认启用还是禁用。它可以通过在 `output` 设置中将 `retain` 设置为 `true` 或 `false` 来在每台收音机的基础上覆盖。

在手动配置时，假设您打算将 rtl_433 数据放入 Home Assistant，配置文件中需要指定的绝对最小信息是 [MQTT 连接和认证信息](https://triq.org/rtl_433/OPERATION.html#mqtt-output)：

```
output      mqtt://HOST:PORT,user=XXXX,pass=YYYYYYY
```

rtl_433 默认监听 433.92MHz，但即使这是您需要的，最好明确指定频率以避免混淆：

```
frequency   433.92M
```

您可能还想缩小 rtl_433 应该尝试解码的协议列表。完整列表可以在 [README](https://github.com/merbanan/rtl_433/blob/master/README.md) 的“支持的设备协议”部分找到。假设您想监听 Acurite 592TXR 温湿度传感器：

```
protocol    40
```

最后，如果您决定使用 MQTT 自动发现脚本或插件，其文档建议将所有从 rtl_433 输出的数据转换为 SI 单位：

```
convert     si
```

假设您只有一个 USB 捅件连接并且 rtl_433 能够自动找到它，我们得到一个看起来像这样最小 rtl_433 配置文件：

```
output      mqtt://HOST:PORT,user=XXXX,pass=YYYYYYY

frequency   433.92M
protocol    40

convert     si
```

请查看 [官方 rtl_433 文档](https://triq.org/rtl_433) 和 [配置文件示例](https://github.com/merbanan/rtl_433/tree/master/conf) 以获取更多信息。

## 致谢

这个插件基于 James Fry 的 [rtl4332mqtt Hass.IO 插件](https://github.com/james-fry/hassio-addons/tree/master/rtl4332mqtt)，它反过来基于 Chris Kacerguis 的项目：[https://github.com/chriskacerguis/honeywell2mqtt](https://github.com/chriskacerguis/honeywell2mqtt)，它反过来基于 Marco Verleun 的 rtl2mqtt 镜像：[https://github.com/roflmao/rtl2mqtt](https://github.com/roflmao/rtl2mqtt)。