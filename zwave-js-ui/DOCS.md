# Home Assistant Community Add-on: Z-Wave JS UI

Z-Wave JS UI 添加程序提供了一个额外的控制面板，允许您配置 Z-Wave 网络的各个方面。它提供了一个解耦网关，可以使用 Z-Wave JS WebSockets（Home Assistant Z-Wave JS 集成使用）和 MQTT（甚至可以同时使用）进行通信。

一些优点和使用场景：

- 与 Home Assistant Z-Wave JS 集成兼容。
- 您的 Z-Wave 网络将在 Home Assistant 重启之间继续运行。
- 您可以直接使用 Node-RED 等工具与您的 Z-Wave 网络进行交互，同时它仍然可用于 Home Assistant。
- 允许基于 [ESPHome.io][esphome] 的 ESP 设备直接响应或与您的 Z-Wave 网络协同工作。
- 当找到时，会使用 Mosquitto 添加程序进行预配置。

此添加程序使用 [Z-Wave JS UI][zwave-js-ui] 软件。

## 安装

此添加程序的安装非常简单，与安装任何其他 Home Assistant 添加程序没有区别。

1. 点击下方的 Home Assistant My 按钮以在您的 Home Assistant 实例中打开添加程序。

   ![在您的 Home Assistant 实例中打开此添加程序][addon-badge]][addon]

1. 点击“安装”按钮以安装添加程序。
1. 检查“Z-Wave JS UI”添加程序的日志，以查看是否一切顺利。
1. 点击“打开 Web UI”按钮。
1. 享受添加程序！

**注意**：上游项目在使用软件本身方面有文档：
<https://zwave-js.github.io/zwave-js-ui/#/>

## 设置 Home Assistant Z-Wave JS 集成

默认情况下，Home Assistant Z-Wave JS 集成将尝试从官方添加程序商店设置官方的“Z-Wave JS”添加程序。

然而，此添加程序将提供一个添加程序 UI，并且具有通过 MQTT 发送/接收数据的能力。因此，如果您需要这些功能，这个添加程序可能适合您。

在成功启动添加程序后，是将其与 Home Assistant 连接起来的时候了。

为此：

1. 通过点击 Supervisor 中添加程序页面上的“打开 Web UI”按钮来打开 Z-Wave JS UI 控制面板。
2. 在控制面板中，在菜单中转到“设置”，然后点击出现的右侧的“Zwave”条。
3. 输入以下信息：
   - 串口（例如：`/dev/serial/by-id/usb-0658_0200_if00`）
   - 网络密钥（例如：`2232666D100F795E5BB17F0A1BB7A146`）

现在点击“保存”按钮，然后导航到菜单中的“控制面板”。如果您已经配对了设备，您应该会看到它们逐渐显示出来。

现在，是设置 Home Assistant 的时候了：

1. 转到设置面板并点击“设备和服务”。
2. 在右下角，点击“+ 添加集成”。
3. 从列表中选择“Z-Wave”集成。
4. 将会显示一个对话框，询问是否使用添加程序：
   - **取消选中**该框，它将安装官方添加程序。
   - 再次，官方添加程序是推荐的，所以...
5. 在下一个对话框中，它会要求输入服务器。输入：
   `ws://a0d7b954-zwavejs2mqtt:3000`
6. 确认并完成！

## 配置

**注意**：_在配置更改时，请重启添加程序。_

示例添加程序配置：

```yaml
log_level: info
```

### 选项：`log_level`

`log_level` 选项控制添加程序的日志输出级别，可以更改为更详细或不详细，这在处理未知问题时可能很有用。可能的值有：

- `trace`：显示每个细节，如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：异常事件，但不是错误。
- `error`：运行时错误，不需要立即采取行动。
- `fatal`：发生了严重错误。添加程序变得无法使用。

请注意，每个级别自动包含更严重级别的日志消息，例如，`debug` 也显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐设置，除非您正在解决问题。

## 已知问题和限制

- Z-Wave JS UI 支持 Home Assistant 通过 MQTT 进行发现。强烈建议**不要**使用该选项。使用上面记录的 Z-Wave JS 集成。

## 更改日志和发布

此存储库使用 [GitHub 的发布][releases] 功能来维护更改日志。

发布基于 [语义版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 格式。简而言之，版本将根据以下情况增加：

- `MAJOR`：不兼容或主要更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的补丁和软件包更新。

## 支持

有问题吗？

您有几个选项来获得答案：

- [Home Assistant Community Add-ons Discord 服务器][discord] 用于添加程序支持和功能请求。
- [Home Assistant Discord 服务器][discord-ha] 用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

您也可以在 GitHub 上[打开一个问题][issue]。

## 作者和贡献者

此存储库的原始设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2021 - 2025 Franck Nijhof

特此授予任何获得此软件及其相关文档文件（“软件”）副本的人，在不限制的情况下自由处理软件的权利，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权利，并允许向提供软件的人这样做，但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件按“原样”提供，不提供任何形式的保证，无论是明示的还是暗示的，包括但不限于对适销性、特定用途适用性和非侵权的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害或其他责任承担责任，无论是由合同、侵权或其他行为引起的，也不论是由软件或软件的使用或其他交易引起的。

[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[addon]: https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_zwavejs2mqtt&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository
[contributors]: https://github.com/hassio-addons/addon-zwave-js-ui/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[esphome]: https://esphome.io/components/mqtt.html#on-message-trigger
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg
[forum]: https://community.home-assistant.io/?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-zwave-js-ui/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-zwave-js-ui/releases
[semver]: https://semver.org/spec/v2.0.0.html
[zwave-js-ui]: https://github.com/zwave-js/zwave-js-ui