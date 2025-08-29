# Home Assistant Community Add-on: Z-Wave JS UI

Z-Wave JS UI add-on 提供了一个额外的控制面板，允许您配置 Z-Wave 网络的各个方面。它提供了一个解耦网关，可以使用 Z-Wave JS WebSocket（由 Home Assistant Z-Wave JS 集成使用）和 MQTT（甚至同时）进行通信。

一些优点和使用场景：

- 与 Home Assistant Z-Wave JS 集成兼容。
- 您的 Z-Wave 网络将在 Home Assistant 重启之间持续运行。
- 您可以直接使用 Node-RED 等工具与您的 Z-Wave 网络进行交互，同时它仍然可用于 Home Assistant。
- 允许基于 [ESPHome.io][esphome] 的 ESP 设备直接响应或与您的 Z-Wave 网络工作。
- 当找到 Mosquitto add-on 时，它会自动进行预配置。

此 add-on 使用 [Z-Wave JS UI][zwave-js-ui] 软件。

## 安装

此 add-on 的安装过程非常简单，与安装任何其他 Home Assistant add-on 没有区别。

1. 点击下面的 Home Assistant My 按钮，在您的 Home Assistant 实例上打开 add-on。

   [![在您的 Home Assistant 实例中打开此 add-on][addon-badge]][addon]

1. 点击“安装”按钮来安装 add-on。
1. 检查“Z-Wave JS UI” add-on 的日志，看看是否一切顺利。
1. 点击“打开 WEB UI”按钮。
1. 享受 add-on！

**注意**：上游项目有关使用该软件的文档：
<https://zwave-js.github.io/zwave-js-ui/#/>

## 设置 Home Assistant Z-Wave JS 集成

默认情况下，Home Assistant Z-Wave JS 集成将尝试从官方 add-on 商店设置官方的“Z-Wave JS” add-on。

然而，此 add-on 提供了一个 add-on UI，并且具有通过 MQTT 发送/接收数据的能力。所以，如果您喜欢这个功能，这个 add-on 可能适合您。

在成功启动 add-on 后，是时候将其与 Home Assistant 连接起来了。

为此：

1. 通过点击 Supervisor 中 add-on 页面上的“打开 WEB UI”按钮来打开 Z-Wave JS UI 控制面板。
2. 在控制面板中，在菜单中转到“设置”，然后点击右侧出现的“Zwave”条目。
3. 输入以下信息：
   - 串行端口（例如，`/dev/serial/by-id/usb-0658_0200_if00`）
   - 网络密钥（例如，`2232666D100F795E5BB17F0A1BB7A146`）

点击“保存”按钮，然后导航到菜单中的“控制面板”。如果您已经配对了设备，您应该会看到它们逐渐出现。

现在，是时候设置 Home Assistant 了：

1. 转到设置面板，点击“设备和服务”。
2. 在右下角，点击“+ 添加集成”。
3. 从列表中选择“Z-Wave”集成。
4. 将显示一个对话框，询问是否使用 add-on：
   - **取消勾选**该框，它将安装官方 add-on。
   - 再次，官方 add-on 是推荐的，所以...
5. 在下一个对话框中，它将询问服务器。输入：
   `ws://a0d7b954-zwavejs2mqtt:3000`
6. 确认并完成！

## 配置

**注意**：_更改配置时，请记得重启 add-on。_

示例 add-on 配置：

```yaml
log_level: info
```

### 选项：`log_level`

`log_level` 选项控制 add-on 的日志输出级别，可以更改为更详细或更简洁，这在处理未知问题时可能很有用。可能的值有：

- `trace`：显示所有细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：非错误的异常情况。
- `error`：不需要立即采取行动的运行时错误。
- `fatal`：发生了严重错误，add-on 变得无法使用。

请注意，每个级别自动包含更严重级别的日志消息，例如，`debug` 也显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您正在调试。

## 已知问题和限制

- Z-Wave JS UI 支持通过 MQTT 的 Home Assistant 发现。强烈建议**不要**使用该选项。改用上面文档中描述的 Z-Wave JS 集成。

## 更改日志与发布

此存储库使用 [GitHub 的发布][releases] 功能维护更改日志。

发布基于 [语义版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 格式。简而言之，版本将根据以下内容进行递增：

- `MAJOR`：不兼容或主要更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的补丁和包更新。

## 支持

有问题？

您有几个选项来获得答案：

- [Home Assistant Community Add-ons Discord 服务器][discord] 用于 add-on 支持和功能请求。
- [Home Assistant Discord 服务器][discord-ha] 用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

您也可以在 GitHub 上[打开一个问题][issue]。

## 作者与贡献者

此存储库的原始设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2021 - 2025 Franck Nijhof

特此授予任何人免费获得此软件和关联文档文件（“软件”）副本的权限，可以在软件上不受限制地处理，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权利，并允许提供软件的人这样做，但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分的软件中。

软件按“原样”提供，不提供任何明示或暗示的保证，包括但不限于适销性、特定用途适用性和不侵犯版权的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害或其他责任承担责任，无论是合同行为、侵权行为或其他行为，均由软件或使用软件或其他交易引起。

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