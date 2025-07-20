# rtl_433 Home Assistant Add-on

## 关于

这个插件是一个简单的包装器，围绕优秀的 [rtl_433](https://github.com/merbanan/rtl_433) 项目，通过 [支持的一种SDR转接器](https://triq.org/rtl_433/HARDWARE.html) 接收无线传感器数据，解码并以多种格式（包括JSON和MQTT）输出。无线传感器rtl_433主要在433.92 MHz、868 MHz、315 MHz、345 MHz和915 MHz ISM频段上传输数据。

[查看rtl_433文档](https://triq.org/rtl_433)

## 工作原理

这个插件唯一做的事情就是在Home Assistant OS守护进程下运行rtl_433。你只需要提供一个配置文件。

默认情况下，rtl_433会将接收到的数据打印到终端——你需要配置它以将数据发布到MQTT，以便Home Assistant可以访问它，这可以在配置文件中的一行代码中完成。

一旦你将rtl_433传感器数据导入MQTT，你将需要帮助Home Assistant发现并理解这些数据。你可以通过以下几种方式完成：

  * 手动在HA中配置 `sensors` 和 `binary_sensors`，并将它们链接到从rtl_433发出的相应的MQTT主题[https://www.home-assistant.io/integrations/sensor.mqtt/]，
  * 手动或在计划中运行[rtl_433_mqtt_hass.py](https://github.com/merbanan/rtl_433/tree/master/examples/rtl_433_mqtt_hass.py)脚本以自动完成大部分配置，或
  * 安装[rtl_433 MQTT自动发现Home Assistant插件](https://github.com/pbkhrv/rtl_433-hass-addons/tree/main/rtl_433_mqtt_autodiscovery)，该插件会为你运行rtl_433_mqtt_hass.py。

## 前置条件

要使用这个插件，你需要以下条件：

 1. [一种被rtl_433支持的SDR转接器](https://triq.org/rtl_433/HARDWARE.html)。

 2. 在连接了SDR转接器的机器上运行Home Assistant OS。

 3. 一些被rtl_433支持的无线传感器。支持协议和设备的完整列表可以在[rtl_433的README](https://github.com/merbanan/rtl_433/blob/master/README.md)的“支持的设备协议”部分找到。

## 安装

 1. 创建一个符合你需求的rtl_433配置文件。如果你在运行Home Assistant OS的计算机之外完成此操作，可能会更好，这样你可以自由地实验并迭代，直到你得到一个工作良好的配置。有关更多详细信息，请参阅下文。

 2. 使用你选择的方法（通过Samba插件、ssh/scp、文件编辑器插件等）将配置文件上传到Home Assistant的"/config"目录。

 3. 安装插件。

 5. 将你的SDR转接器插入运行插件的计算机。

 5. 启动插件。将创建一个默认配置在`/config/rtl_433/`。要添加或编辑其他配置，请在该目录中创建多个`.conf.template`文件。

 6. 启动插件并检查日志。

## 配置

对于“零配置”设置，安装[Mosquitto代理](https://github.com/home-assistant/addons/blob/master/mosquitto/DOCS.md)插件。虽然其他代理可能也能工作，但它们未经测试，需要手动设置。插件安装后，启动或重新启动rtl_433和rtl_433_mqtt_autodiscovery插件以开始捕获已知的433 MHz协议。

对于更高级的配置，请查看rtl_433源代码中包含的示例配置文件：[rtl_433.example.conf](https://github.com/merbanan/rtl_433/blob/master/conf/rtl_433.example.conf)

注意，由于配置文件中包含bash变量，**美元符号和其他特殊shell字符需要转义**。例如，要在配置文件中使用字面字符串`$GPRMC`，请使用`\$GPRMC`。

`retain`选项控制MQTT的`retain`标志是默认启用还是禁用。可以通过在`output`设置中将`retain`设置为`true`或`false`来逐个无线电覆盖。

在手动配置时，假设你打算将rtl_433数据导入Home Assistant，配置文件中需要指定的最低信息是[MQTT连接和认证信息](https://triq.org/rtl_433/OPERATION.html#mqtt-output)：

```
output      mqtt://HOST:PORT,user=XXXX,pass=YYYYYYY
```

rtl_433默认监听433.92MHz，但即使这是你所需要的，最好明确指定频率以避免混淆：

```
frequency   433.92M
```

你可能还想缩小rtl_433尝试解码的协议列表。完整列表可以在[README](https://github.com/merbanan/rtl_433/blob/master/README.md)的“支持的设备协议”部分找到。假设你想监听Acurite 592TXR温度/湿度传感器：

```
protocol    40
```

最后但同样重要的是，如果你决定使用MQTT自动发现脚本或插件，其文档建议将所有从rtl_433输出的数据转换为SI单位：

```
convert     si
```

假设你只连接了一个USB转接器并且rtl_433能够自动找到它，我们得到一个看起来像这样最小的rtl_433配置文件：

```
output      mqtt://HOST:PORT,user=XXXX,pass=YYYYYYY

frequency   433.92M
protocol    40

convert     si
```

请查看[官方rtl_433文档](https://triq.org/rtl_433)和[配置文件示例](https://github.com/merbanan/rtl_433/tree/master/conf)以获取更多信息。

## 致谢

这个插件基于James Fry的[rtl4332mqtt Hass.IO插件](https://github.com/james-fry/hassio-addons/tree/master/rtl4332mqtt)，后者基于Chris Kacerguis的项目：[https://github.com/chriskacerguis/honeywell2mqtt](https://github.com/chriskacerguis/honeywell2mqtt)，后者基于Marco Verleun的rtl2mqtt镜像：[https://github.com/roflmao/rtl2mqtt](https://github.com/roflmao/rtl2mqtt)。