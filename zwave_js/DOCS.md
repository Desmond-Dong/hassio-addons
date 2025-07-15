# Home Assistant Add-on: Z-Wave JS

## 安装

按照以下步骤将插件安装到您的系统上：

1. 在 Home Assistant 前端导航到 **设置** -> **插件** -> **插件商店**。
2. 找到 "Z-Wave JS" 插件并点击它。
3. 点击 "安装" 按钮。

## 使用方法

插件需要知道您的 Z-Wave 控制器设备的位置，因此，您需要配置插件以指向正确的设备。

如果您使用 Home Assistant，您可以通过进入 `设置 -> 系统 -> 硬件` 并点击三点菜单选择 `所有硬件` 来找到此的正确值。如果存在，建议使用“按 ID”路径到设备，因为如果系统添加了其他设备，它不会改变。

1. 在插件配置中的 `device` 选项中替换 `null` 并用引号指定设备名称：例如，类似于
   `"/dev/serial/by-id/usb-0658_0200-if00"`，
   `"/dev/ttyUSB0"`，`"/dev/ttyAMA0"`，或 `"/dev/ttyACM0"`。
2. 以 `2232666D1...` 形式的 16 字节（32 个字符十六进制）安全密钥，以便安全地连接到兼容的设备。建议配置所有四个网络密钥，因为如果它们没有被安全地添加，一些启用安全的设备（锁等）可能无法正常工作。
   - 作为注释，不建议安全连接所有设备，除非它们支持 S2 安全性，因为 S0 安全性会使网状网络上的消息量增加三倍。
3. 点击 "保存" 以保存插件配置。
4. 启动插件。
5. 将 Z-Wave JS 集成添加到 Home Assistant，请参阅文档：
   <https://www.home-assistant.io/integrations/zwave_js>

## 配置

插件配置：

```yaml
device: /dev/ttyUSB0
s0_legacy_key: 2232666D100F795E5BB17F0A1BB7A146
s2_access_control_key: A97D2A51A6D4022998BEFC7B5DAE8EA1
s2_authenticated_key: 309D4AAEF63EFD85967D76ECA014D1DF
s2_unauthenticated_key: CF338FE0CB99549F7C0EA96308E5A403
lr_s2_access_control_key: E2CEA6B5986C818EEC0D0065D81E2BD5
lr_s2_authenticated_key: 863027C59CFC522A9A3C41976AE54254
```

### 选项 `device`

Z-Wave 控制器设备。

如果您使用 Home Assistant，您可以通过进入 `设置 -> 系统 -> 硬件` 并点击三点菜单选择 `所有硬件` 来找到此的正确值。如果存在，建议使用“按 ID”路径到设备，因为如果系统添加了其他设备，它不会改变。

在大多数情况下，它看起来像以下之一：

- `"/dev/serial/by-id/usb-0658_0200-if00"`
- `"/dev/ttyUSB0"`
- `"/dev/ttyAMA0"`
- `"/dev/ttyACM0"`

### 安全密钥

为了充分利用 Z-Wave JS 支持的不同包含方法，需要六种不同的安全密钥：`s0_legacy_key`，`s2_access_control_key`，`s2_authenticated_key`，`s2_unauthenticated_key`，`lr_s2_access_control_key` 和 `lr_s2_authenticated_key`。

如果您来自 `zwave-js` 的旧版本，您可能有一个存储在 `network_key` 配置选项中的密钥。当插件首次启动时，密钥将从 `network_key` 迁移到 `s0_legacy_key`，这将确保您的 S0 安全设备继续正常工作。

如果这些密钥中的任何一个在启动时丢失，插件将为您自动生成一个。要手动生成网络密钥，您可以使用以下脚本，例如在 SSH 插件中：

```bash
hexdump -n 16 -e '4/4 "%08X" 1 "\n"' /dev/random
```

您还可以使用像这样的网站来生成所需的数据：

<https://www.random.org/cgi-bin/randbyte?nbytes=16&format=h>

确保备份这些密钥。如果您必须重建您的系统并且没有这些密钥的备份，您将无法与任何安全包含的设备通信。这可能意味着您必须对那些设备和控制器执行工厂重置，然后再重建您的 Z-Wave 网络。

> 注意：在多个安全类之间共享密钥是一种安全风险，因此，如果您选择自行配置这些密钥，请确保使它们唯一！

#### 选项 `s0_legacy_key`

S0 安全 Z-Wave 设备在添加到网络之前需要一个网络密钥。此配置选项是必需的，但如果未设置，插件将在启动时自动生成一个新的。

#### 选项 `s2_access_control_key`

必须提供 `s2_access_control_key` 以便使用 S2 访问控制安全类包含设备。此类安全类由门锁和车库门 opener 等设备需要。此配置选项是必需的，但如果未设置，插件将在启动时自动生成一个新的。

#### 选项 `s2_authenticated_key`

必须提供 `s2_authenticated_key` 以便使用 S2 认证安全类包含设备。安全系统、传感器、照明等设备可以请求此类安全类。此配置选项是必需的，但如果未设置，插件将在启动时自动生成一个新的。

### 选项 `s2_unauthenticated_key`

必须提供 `s2_unauthenticated_key` 以便使用 S2 未认证安全类包含设备。这与 S2 认证类似，但没有验证是否包含正确的设备。此配置选项是必需的，但如果未设置，插件将自动生成一个新的。

#### 选项 `lr_s2_access_control_key`

必须提供 `lr_s2_access_control_key` 以便使用 Z-Wave 长距离包含设备。此配置选项是必需的，但如果未设置，插件将自动生成一个新的。

#### 选项 `lr_s2_authenticated_key`

必须提供 `lr_s2_authenticated_key` 以便使用 Z-Wave 长距离包含设备。此配置选项是必需的，但如果未设置，插件将自动生成一个新的。

### 选项 `log_level`（可选）

此选项设置 Z-Wave JS 的日志级别。有效选项为：

- silly
- debug
- verbose
- http
- info
- warn
- error

如果没有指定 `log_level`，日志级别将设置为 Supervisor 中设置的级别。

### 选项 `log_to_file`（可选）

启用此选项时，日志将写入 `/addon_configs/core_zwave_js` 文件夹，扩展名为 `.log`。

### 选项 `log_max_files`（可选）

当 `log_to_file` 为 true 时，Z-Wave JS 将为每一天创建一个日志文件。此选项允许您控制 Z-Wave JS 将保留的最大文件数。

### 选项 `rf_region`（可选）

此设置告诉插件控制器应使用的无线电频率区域。有效选项为：

- Automatic
- Australia/New Zealand
- China
- Europe
- Europe (Long Range)
- Hong Kong
- India
- Israel
- Japan
- Korea
- Russia
- USA
- USA (Long Range)

默认是 Automatic，它将尝试根据 Home Assistant 中设置的国家设置正确的区域。

### 选项 `soft_reset`（可选）

此设置告诉插件如何处理 500 系列控制器的软重置：
1. Automatic - 插件将决定是否应启用或禁用 500 系列控制器的软重置。这是默认选项，应该适用于大多数人。
2. Enabled - 将明确启用 500 系列控制器的软重置。
3. Disabled - 将明确禁用 500 系列控制器的软重置。

### 选项 `emulate_hardware`（可选）

如果您没有 USB 指示器，您可以使用一个假指示器进行测试。它将无法控制任何真实设备。

### 选项 `disable_controller_recovery`（可选）：

此设置将禁用 Z-Wave JS 在控制器似乎无响应时的自动恢复过程，并将允许控制器自行恢复，如果它能够这样做。当控制器无响应时，命令将开始失败，节点可能会随机被标记为已死。如果控制器无法自行恢复，您需要重新启动插件以尝试恢复。在大多数情况下，用户永远不会需要使用此功能，因此，除非您知道自己在做什么和/或被要求这样做，否则请不要更改此设置。

### 选项 `disable_watchdog`（可选）：

此设置将阻止 Z-Wave JS 在支持的控制器上启用硬件看门狗。在大多数情况下，用户永远不会需要使用此功能，因此，除非您知道自己在做什么和/或被要求这样做，否则请不要更改此设置。

### 选项 `safe_mode`（可选）

此设置将您的网络置于安全模式，这可能会显著降低网络性能，但也可能有助于启动网络，以便您可以解决问题、获取日志等。在大多数情况下，用户永远不会需要使用此功能，因此，除非您知道自己在做什么和/或被要求这样做，否则请不要更改此设置。

### 选项 `network_key`（已弃用）

在插件的旧版本中，这是唯一需要的密钥。随着在 zwave-js 中引入 S2 安全包含，此选项已被弃用，改为 `s0_legacy_key`。如果仍然设置，`network_key` 值将在首次启动时迁移到 `s0_legacy_key`。

### 网络问题故障排除

插件中有几个功能可以帮助您在解决网络问题时提供数据，或者提供给 Home Assistant 或 Z-Wave JS 团队以帮助跟踪问题：

1. **更新日志级别**：在打开 GitHub 问题时要设置 `log_level` 配置选项为 `debug` 并捕获问题发生的时间。
2. **记录到文件**：`log_to_file` 和 `log_max_files` 配置选项允许您启用和配置。请注意，为了访问日志文件，您需要能够访问您的 HA 实例的文件系统，您可以通过文件编辑器、samba 或 ssh 插件等方式完成。
3. **访问 Z-Wave JS 缓存**：Z-Wave JS 将有关您网络的信息存储在缓存文件中，以便您的设备在每次启动时不需要重新面试。在某些情况下，当打开 GitHub问题时，您可能会被要求提供缓存文件。您可以在 `/addon_configs/core_zwave_js/cache` 中找到它们。请注意，为了访问缓存，您需要能够访问您的 HA 实例的文件系统，您可以通过文件编辑器、samba 或 ssh 插件等方式完成。
4. **更改软重置行为**：默认情况下，插件将自动选择在启动时是否软重置控制器。在大多数情况下不应更改，但如果在解决问题时被要求更改，您可以使用 `soft_reset` 配置选项完成。
5. **禁用控制器恢复**：默认情况下，如果网络控制器似乎卡住，Z-Wave JS 将自动尝试将控制器恢复到健康状态。在大多数情况下不应更改，但如果在解决问题时被要求更改，您可以使用 `disable_controller_recovery` 配置选项完成。
6. **启用安全模式**：当 Z-Wave JS 启动时遇到问题时，有时很难获取有用的日志来解决问题。通过将 `safe_mode` 设置为 true，Z-Wave JS 可能能够在设置为 false 时无法启动的情况下启动。请注意，启用 `safe_mode` 将对网络性能产生负面影响，应谨慎使用。

## 已知问题和限制

- 您的硬件需要与 Z-Wave JS 库兼容

## 支持

有问题？

您有几个选项可以回答它们：

- [Home Assistant Discord 服务器](https://discord.gg/c5DvZ4e)
- [Home Assistant 社区论坛](https://community.home-assistant.io)
- 加入 [Reddit 子版块](https://reddit.com/r/homeassistant) 在 [/r/homeassistant](https://reddit.com/r/homeassistant)

如果您发现了一个错误，请在我们的 GitHub 上[打开一个问题](https://github.com/home-assistant/addons/issues)。

[discord]: https://discord.gg/c5DvZ4e
[forum]: https://community.home-assistant.io
[issue]: https://github.com/home-assistant/addons/issues
[reddit]: https://reddit.com/r/homeassistant