# Home Assistant Community Add-on: Z-Wave JS UI

Z-Wave JS UI 添加组件提供了一个额外的控制面板，允许您配置 Z-Wave 网络的各个方面。它提供了一个解耦的网关，可以使用 Z-Wave JS WebSockets（Home Assistant Z-Wave JS 集成使用）和 MQTT（甚至同时使用）进行通信。

一些优点和使用场景：

- 与 Home Assistant Z-Wave JS 集成兼容。
- 在 Home Assistant 重启之间，您的 Z-Wave 网络将保持运行。
- 您可以直接使用 Node-RED 等工具与您的 Z-Wave 网络进行交互，同时它也适用于 Home Assistant。
- 允许基于 [ESPHome.io][esphome] 的 ESP 设备直接响应或与您的 Z-Wave 网络工作。
- 当找到时，它会使用 Mosquitto 添加组件进行预配置。

此添加组件使用 [Z-Wave JS UI][zwave-js-ui] 软件。

## 安装

此添加组件的安装非常简单，与安装任何其他 Home Assistant 添加组件没有区别。

1. 点击下面的 Home Assistant 我的按钮，在您的 Home Assistant 实例上打开添加组件。

   [![在您的 Home Assistant 实例中打开此添加组件][addon-badge]][addon]

1. 点击“安装”按钮以安装添加组件。
1. 检查“Z-Wave JS UI”添加组件的日志，以查看是否一切顺利。
1. 点击“打开 Web UI”按钮。
1. 享受添加组件！

**注意**：上游项目提供了使用该软件的文档：
<https://zwave-js.github.io/zwave-js-ui/#/>

## 设置 Home Assistant Z-Wave JS 集成

默认情况下，Home Assistant Z-Wave JS 集成将尝试从官方添加组件商店设置官方的“Z-Wave JS”添加组件。

然而，此添加组件提供了一个添加组件 UI，并且具有通过 MQTT 发送/接收数据的能力。所以，如果这是您的需求，这个添加组件可能适合您。

在成功启动添加组件后，是将其与 Home Assistant 连接起来的时候了。

为此：

1. 通过点击 Supervisor 中添加组件页面上的“打开 Web UI”按钮来打开 Z-Wave JS UI 控制面板。
2. 在控制面板中，在菜单中转到“设置”，然后点击右侧出现的“Zwave”条。
3. 输入以下信息：
   - 串口（例如，`/dev/serial/by-id/usb-0658_0200_if00`）
   - 网络密钥（例如，`2232666D100F795E5BB17F0A1BB7A146`）

现在点击“保存”按钮，然后转到菜单中的“控制面板”。如果您已经配对了设备，您应该会看到它们慢慢出现。

现在是为 Home Assistant 设置的时间：

1. 转到设置面板，点击“设备和服务”。
2. 在右下角，点击“+ 添加集成”。
3. 从列表中选择“Z-Wave”集成。
4. 将显示一个对话框，询问是否使用添加组件：
   - **取消选中**那个框，它将安装官方的添加组件。
   - 再次，官方的添加组件是推荐的，所以...
5. 在下一个对话框中，它将询问服务器。输入：
   `ws://a0d7b954-zwavejs2mqtt:3000`
6. 确认并完成！

## 配置

**注意**：_在配置更改时，请重启添加组件。_

示例添加组件配置：

```yaml
log_level: info
```

### 选项：`log_level`

`log_level` 选项控制添加组件的日志输出级别，可以更改为更详细或更简洁，这在您处理未知问题时可能很有用。可能的值是：

- `trace`：显示每个细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：异常情况，但不是错误。
- `error`：运行时错误，不需要立即采取行动。
- `fatal`：出了严重问题。添加组件变得无法使用。

请注意，每个级别自动包含更严重级别的日志消息，例如，`debug` 也显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐设置，除非您正在解决问题。

## 已知问题和限制

- Z-Wave JS UI 支持通过 MQTT 的 Home Assistant 发现。强烈建议**不要**使用该选项。使用上面记录的 Z-Wave JS 集成。

## 更改日志和发布

此存储库使用 [GitHub 的发布][releases] 功能维护更改日志。

发布基于 [语义版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 格式。简而言之，版本将根据以下内容进行递增：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的错误修复和软件包更新。

## 支持

有问题吗？

您有几个选项来获得答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord] 用于添加组件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

您也可以在 GitHub 上[打开一个问题][issue]。

## 作者和贡献者

此存储库的原始设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2021 - 2025 Franck Nijhof

特此免费授予任何获得此软件及其相关文档文件（“软件”）副本的人，在软件上无限制地处理的权限，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权限，并允许获得软件的人这样做，但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分的软件中。

软件按“原样”提供，不提供任何形式的保证，包括但不限于对适销性、特定用途适用性和不侵权的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害赔偿或其他责任承担责任，无论是由合同、侵权或其他行为引起的，也不论是与软件或软件的使用或其他交易有关。