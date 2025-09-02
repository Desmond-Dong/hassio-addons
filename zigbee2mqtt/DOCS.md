# 配对

默认情况下，附加组件的 `permit_join` 设置为 `false`。要允许设备加入，您需要在附加组件启动后激活此功能。现在您可以使用 [内置前端](https://www.zigbee2mqtt.io/information/frontend.html) 来实现这一点。有关如何启用内置前端的详细信息，请参阅下一节。

# 启用内置前端

启用 `ingress` 以在您的 UI 中提供前端：**设置 → 附加组件 → Zigbee2MQTT → 在侧边栏中显示**。有关该功能的更多详细信息，请参阅 [Zigbee2MQTT 文档](https://www.zigbee2mqtt.io/information/frontend.html)。

# 配置

## 引导

[引导](https://www.zigbee2mqtt.io/guide/getting-started/#onboarding) 允许您在不手动输入附加组件配置页面上的详细信息的情况下设置 Zigbee2MQTT。当使用全新安装（没有配置）启动附加组件时，前端将显示一个快速设置页面，允许您选择各种设置，以便 Zigbee2MQTT 能够启动。

> [!NOTE]
> 适配器的成功检测可能因您的设置/网络而异。您可能需要在页面上手动输入这些 [详细信息](https://www.zigbee2mqtt.io/guide/configuration/adapter-settings.html#basic-configuration)。

> [!TIP]
> 您可以使用附加组件配置页面中的切换按钮强制引导重新运行（例如，更改适配器）。这将强制引导在您成功配置它后运行。完成后请确保禁用它。

## 手动

启动 Zigbee2MQTT 所需的配置可在附加组件配置中获取。其余选项可以通过 Zigbee2MQTT 前端进行配置。

> [!CAUTION]
> 通过附加组件配置页面配置的设置将优先于 `configuration.yaml` 页面中的设置（例如，您在附加组件配置页面中设置 `rtscts: false`，在 `configuration.yaml` 中设置 `rtscts: true`，`rtscts: false` 将被使用）。如果您想通过 YAML 控制整个配置，请从附加组件配置页面中删除它们。

#### 每个配置部分的示例

- socat
  ```yaml
  enabled: false
  master: pty,raw,echo=0,link=/tmp/ttyZ2M,mode=777
  slave: tcp-listen:8485,keepalive,nodelay,reuseaddr,keepidle=1,keepintvl=1,keepcnt=5
  options: "-d -d"
  log: false
  ```
- mqtt
  ```yaml
  server: mqtt://localhost:1883
  user: my_user
  password: "my_password"
  ```
- serial
  ```yaml
  adapter: zstack
  port: /dev/serial/by-id/usb-Texas_Instruments_TI_CC2531_USB_CDC___0X00124B0018ED3DDF-if00
  ```

# 配置备份

附加组件将在您的数据路径中创建 `configuration.yml` 的备份：`$DATA_PATH/configuration.yaml.bk`。在升级时，您应使用此备份将相关值填写到新配置中，特别是网络密钥，以避免破坏您的网络并重新配对所有设备。
如果未找到以前的备份，则在附加组件启动时将创建您的配置备份。

# 启用看门狗

为了在发生软故障（如“适配器断开连接”）时自动重新启动 Zigbee2MQTT，可以使用看门狗。通过在附加组件配置中添加以下内容来启用它：

```yaml
watchdog: default
```

这将使用默认的看门狗重试延迟：1 分钟、5 分钟、15 分钟、30 分钟、60 分钟。也支持自定义延迟，例如 `watchdog: 5,10,30` 将使用看门狗的重试延迟：5 分钟、10 分钟、30 分钟。有关看门狗的更多信息，请阅读 [文档](https://www.zigbee2mqtt.io/guide/installation/15_watchdog.html)。

# 添加对新设备的支持

如果您有兴趣为 Zigbee2MQTT 添加对新设备的支持，请参阅 [如何支持新设备](https://www.zigbee2mqtt.io/how_tos/how_to_support_new_devices.html)。

# 注意事项

- 根据您的配置，MQTT 服务器配置可能需要包含端口，通常为 `1883` 或 `8883` 用于 SSL 通信。例如，对于 Home Assistant 的 Mosquitto 附加组件，使用 `mqtt://core-mosquitto:1883`。
- 要查找您已暴露的串行端口，请转到 **Supervisor → 系统 → 主机系统 → ⋮ → 硬件**

# Socat

在某些情况下，无法将串行设备转发到 Zigbee2MQTT 运行的容器中。这可能是因为设备根本没有物理连接到机器。

可以使用 Socat 将串行设备通过 TCP 转发到 Zigbee2MQTT。有关更多信息，请参阅 [Socat 手册页面](https://linux.die.net/man/1/socat)。

您可以在 socat 部分中配置 Socat 模块，使用以下选项：

- `enabled` true/false 以启用 Socat（默认：false）
- `master` Socat 命令行中使用的第一个地址（必需）
- `slave` Socat 命令行中使用的第二个地址（必需）
- `options` 添加到 Socat 命令行的额外选项（可选）
- `log` true/false 如果要将 Socat 的 stdout/stderr 记录到 data_path/socat.log（默认：false）

**注意：** 您需要根据需要更改 `master` 和 `slave` 选项。默认值将确保 Socat 在端口 `8485` 上监听，并将其输出重定向到 `/dev/ttyZ2M`。Zigbee2MQTT 的串行端口设置不会自动设置，需要相应地更改。