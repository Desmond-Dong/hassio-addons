# rtl_433 Home Assistant Add-on

## 关于

这个插件是一个简单的封装，围绕优秀的 [rtl_433](https://github.com/merbanan/rtl_433) 项目，通过 [支持的SDR接口之一](https://triq.org/rtl_433/HARDWARE.html) 接收无线传感器数据，解码并以多种格式输出，包括JSON和MQTT。无线传感器rtl_433主要理解在433.92 MHz、868 MHz、315 MHz、345 MHz和915 MHz ISM频段上传输的数据。

[查看rtl_433文档](https://triq.org/rtl_433)

## 工作原理

这个插件所做的唯一事情是在Home Assistant OS的supervisor下运行rtl_433。您只需要提供一个配置文件。

默认情况下，rtl_433将接收到的数据打印到终端——您需要配置它将数据发布到MQTT，以便Home Assistant可以访问它，这可以通过配置文件中的一行来实现。

一旦您将rtl_433传感器数据获取到MQTT，您就需要帮助Home Assistant发现并理解这些数据。您可以以多种方式完成：

  * 手动在HA中配置 `sensors` 和 `binary_sensors`，并将它们链接到从rtl_433输出的相应MQTT主题[https://www.home-assistant.io/integrations/sensor.mqtt/](https://www.home-assistant.io/integrations/sensor.mqtt/)，
  * 手动或在计划中运行 [rtl_433_mqtt_hass.py](https://github.com/merbanan/rtl_433/tree/master/examples/rtl_433_mqtt_hass.py) 脚本来自动完成大部分配置，或者
  * 安装 [rtl_433 MQTT自动发现Home Assistant插件](https://github.com/pbkhrv/rtl_433-hass-addons/tree/main/rtl_433_mqtt_autodiscovery)，它会为您运行rtl_433_mqtt_hass.py。

## 前置条件

要使用这个插件，您需要以下条件：

 1. [一个被rtl_433支持的SDR接口](https://triq.org/rtl_433/HARDWARE.html)。

 2. 在一个插入有SDR接口的机器上运行的Home Assistant OS。

 3. 一些被rtl_433支持的无线传感器。支持的协议和设备的完整列表可以在[rtl_433的README](https://github.com/merbanan/rtl_433/blob/master/README.md)的“支持的设备协议”部分找到。

## 安装

 1. 创建一个满足您需求的rtl_433配置文件。如果可能的话，您最好在运行Home Assistant OS的计算机之外完成此操作，这样您就可以自由地实验并迭代，直到您找到一个工作良好的配置。有关更多详细信息，请参阅下文。

 2. 使用您认为合适的方法将配置文件上传到Home Assistant的"/config"目录（通过Samba插件、ssh/scp、文件编辑器插件等）。

 3. 安装插件。

 5. 将您的SDR接口连接到运行插件的机器。

 5. 启动插件。将创建一个默认配置在 `/config/rtl_433/`。要添加或编辑附加配置，请在该目录中创建多个 `.conf.template` 文件。

 6. 启动插件并检查日志。

## 配置

对于“零配置”设置，安装[Mosquitto代理](https://github.com/home-assistant/addons/blob/master/mosquitto/DOCS.md)插件。虽然其他代理可能也可以工作，但它们没有经过测试，需要手动设置。一旦插件安装完成，启动或重新启动rtl_433和rtl_433_mqtt_autodiscovery插件以开始捕获已知的433 MHz协议。

对于更高级的配置，请查看rtl_433源代码中包含的示例配置文件：[rtl_433.example.conf](https://github.com/merbanan/rtl_433/blob/master/conf/rtl_433.example.conf)

请注意，由于配置文件中包含bash变量，**美元符号和其他特殊shell字符需要转义**。例如，要在配置文件中使用字面字符串 `$GPRMC`，请使用 `\$GPRMC`。

`retain` 选项控制MQTT的 `retain` 标志是默认启用还是禁用。它可以通过在 `output` 设置中将 `retain` 设置为 `true` 或 `false` 来按每个无线电覆盖。

在手动配置时，假设您打算将rtl_433数据获取到Home Assistant，配置文件中需要指定的最绝对最小信息是[MQTT连接和认证信息](https://triq.org/rtl_433/OPERATION.html#mqtt-output)：

```
output      mqtt://HOST:PORT,user=XXXX,pass=YYYYYYY
```

rtl_433默认监听433.92MHz，但即使这是您需要的，最好明确指定频率以避免混淆：

```
frequency   433.92M
```

您可能还希望缩小rtl_433应尝试解码的协议列表。完整列表可以在[README](https://github.com/merbanan/rtl_433/blob/master/README.md)的“支持的设备协议”部分找到。假设您想监听Acurite 592TXR温度/湿度传感器：

```
protocol    40
```

最后但同样重要的是，如果您决定使用MQTT自动发现脚本或插件，其文档建议将所有从rtl_433输出的数据转换为SI单位：

```
convert     si
```

假设您只连接了一个USB接口，并且rtl_433能够自动找到它，我们得到一个看起来像这样最少的rtl_433配置文件：

```
output      mqtt://HOST:PORT,user=XXXX,pass=YYYYYYY

frequency   433.92M
protocol    40

convert     si
```

请查看[官方rtl_433文档](https://triq.org/rtl_433)和[配置文件示例](https://github.com/merbanan/rtl_433/tree/master/conf)以获取更多信息。

## 致谢

这个插件基于James Fry的 [rtl4332mqtt Hass.IO 插件](https://github.com/james-fry/hassio-addons/tree/master/rtl4332mqtt)，它反过来基于Chris Kacerguis的项目：[https://github.com/chriskacerguis/honeywell2mqtt](https://github.com/chriskacerguis/honeywell2mqtt)，它反过来基于Marco Verleun的rtl2mqtt镜像：[https://github.com/roflmao/rtl2mqtt](https://github.com/roflmao/rtl2mqtt)。