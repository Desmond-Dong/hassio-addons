# Home Assistant 插件：Z-Wave JS

## 安装

按照以下步骤在您的系统上安装插件：

1. 在 Home Assistant 前端导航到 **设置** -> **插件** -> **插件商店**。
2. 找到 "Z-Wave JS" 插件并单击它。
3. 点击 "安装" 按钮。

## 如何使用

插件需要知道您的 Z-Wave 适配器在哪里，因此，
您需要配置插件以指向正确的设备。

如果您使用的是 Home Assistant，您可以通过访问
`设置 -> 系统 -> 硬件`，然后单击三个点的菜单并选择
`所有硬件` 来找到正确的值。如果存在，建议使用设备的 "by-id" 路径，
因为如果添加了其他设备，它不会受到更改的影响。

1. 在插件配置中的 `device` 选项中替换 `null` 并指定
   设备名称，使用引号包裹，例如：
   `"/dev/serial/by-id/usb-0658_0200-if00"`,
   `"/dev/ttyUSB0"`, `"/dev/ttyAMA0"`, 或 `"/dev/ttyACM0"`。
2. 以 `2232666D1...` 的形式设置您的 16 字节（32 个字符十六进制）安全密钥，
   以便安全地连接兼容设备。建议配置所有四个网络密钥，因为某些启用安全性的设备（如锁等）
   如果没有安全添加可能无法正常工作。
   - 需要注意的是，除非所有设备都支持 S2 安全，否则不建议安全连接 _所有_ 设备
     因为 S0 安全会使网状网络上发送的消息数量增加三倍。
3. 点击 "保存" 保存插件配置。
4. 启动插件。
5. 将 Z-Wave JS 集成添加到 Home Assistant，详见文档：
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

如果您使用的是 Home Assistant，您可以通过访问
`设置 -> 系统 -> 硬件`，然后单击三个点的菜单并
选择 `所有硬件` 来找到正确的值。如果存在，建议使用设备的 "by-id" 路径，
因为如果添加了其他设备，它不会受到更改的影响。

在大多数情况下，这看起来像以下之一：

- `"/dev/serial/by-id/usb-0658_0200-if00"`
- `"/dev/ttyUSB0"`
- `"/dev/ttyAMA0"`
- `"/dev/ttyACM0"`

### 安全密钥

有六个不同的安全密钥需要充分利用 Z-Wave JS 支持的不同包含方法：
`s0_legacy_key`、`s2_access_control_key`、`s2_authenticated_key`、`s2_unauthenticated_key`、`lr_s2_access_control_key` 和 `lr_s2_authenticated_key`。

如果您正在使用之前版本的 `zwave-js`，您可能在 `network_key` 配置选项中存储了一个密钥。当插件首次启动时，密钥将从 `network_key` 迁移到 `s0_legacy_key`，这将确保您的 S0 安全设备继续正常工作。

如果在启动时缺少这些密钥，插件将为您自动生成一个。要手动生成网络密钥，您可以在例如 SSH 插件中使用以下脚本：

```bash
hexdump -n 16 -e '4/4 "%08X" 1 "\n"' /dev/random
```

您还可以使用此类网站生成所需的数据：

<https://www.random.org/cgi-bin/randbyte?nbytes=16&format=h>

确保您保留这些密钥的备份。如果您必须重建系统并且没有这些密钥的备份，您将无法与任何安全包含设备通信。这可能意味着您必须在重建 Z-Wave 网络之前对这些设备和您的控制器进行出厂重置。

> 注意：在多个安全类别之间共享密钥是一个安全风险，因此
> 如果您选择自行配置这些密钥，请确保将它们
> 设为唯一！

#### 选项 `s0_legacy_key`

S0 安全 Z-Wave 设备在添加到网络之前需要网络密钥。
此配置选项是必需的，但如果未设置，插件将在启动时自动生成新的密钥。

#### 选项 `s2_access_control_key`

必须提供 `s2_access_control_key` 以包含具有 S2 访问控制安全类的设备。此安全类是门锁和车库门开启器等设备所需的。此配置选项是必需的，但如果未设置，插件将在启动时自动生成新的密钥。

#### 选项 `s2_authenticated_key`

必须提供 `s2_authenticated_key` 以包含具有 S2 已认证安全类的设备。安全系统、传感器、照明等设备可以请求此安全类。此配置选项是必需的，但如果未设置，插件将在启动时自动生成新的密钥。

### 选项 `s2_unauthenticated_key`

必须提供 `s2_unauthenticated_key` 以包含具有 S2 未认证安全类的设备。这与 S2 已认证类似，但不验证是否包含正确的设备。此配置选项是必需的，但如果未设置，插件将在启动时自动生成新的密钥。

#### 选项 `lr_s2_access_control_key`

必须提供 `lr_s2_access_control_key` 以包含使用 Z-Wave 长距离的设备。此配置选项是必需的，但如果未设置，插件将在启动时自动生成新的密钥。

#### 选项 `lr_s2_authenticated_key`

必须提供 `lr_s2_authenticated_key` 以包含使用 Z-Wave 长距离的设备。此配置选项是必需的，但如果未设置，插件将在启动时自动生成新的密钥。

### 选项 `log_level`（可选）

此选项设置 Z-Wave JS 的日志级别。有效选项包括：

- silly
- debug
- verbose
- http
- info
- warn
- error

如果未指定 `log_level`，日志级别将设置为 Supervisor 中设置的级别。

### 选项 `log_to_file`（可选）

启用此选项时，日志将以 `.log` 文件扩展名写入 `/addon_configs/core_zwave_js` 文件夹。

### 选项 `log_max_files`（可选）

当 `log_to_file` 为真时，Z-Wave JS 将为每一天创建一个日志文件。此选项允许您控制 Z-Wave JS 将保留的最大文件数量。

### 选项 `rf_region`（可选）

此设置告诉插件控制器应使用哪个广播频率区域。有效选项包括：

- 自动
- 澳大利亚/新西兰
- 中国
- 欧洲
- 欧洲（长距离）
- 香港
- 印度
- 以色列
- 日本
- 韩国
- 俄罗斯
- 美国
- 美国（长距离）

默认值为自动，它将尝试根据在 Home Assistant 中设置的国家设置正确的区域。

### 选项 `soft_reset`（可选）

此设置告诉插件如何处理 500 系列控制器的软重置：
1. 自动 - 插件将决定是否应为 500 系列控制器启用或禁用软重置。这是默认选项，适用于大多数人。
2. 启用 - 将显式为 500 系列控制器启用软重置。
3. 禁用 - 将显式为 500 系列控制器禁用软重置。

### 选项 `emulate_hardware`（可选）

如果您没有 USB 适配器，可以使用假适配器进行测试。
它将无法控制任何真实设备。

### 选项 `disable_controller_recovery`（可选）：

此设置将禁用 Z-Wave JS 当控制器似乎无反应时的自动恢复过程，
而是让控制器在能够恢复的情况下自行恢复。当控制器无反应时，
命令将开始失败，节点可能会随机标记为死亡。如果控制器无法自行恢复，
您将需要重启插件以尝试恢复。在大多数情况下，用户将不需要使用此功能，因此
仅在您知道自己在做什么和/或被要求时才更改此设置。

### 选项 `disable_watchdog`（可选）：

此设置将阻止 Z-Wave JS 在支持的控制器上启用硬件监视程序。
在大多数情况下，用户将不需要使用此功能，因此
仅在您知道自己在做什么和/或被要求时才更改此设置。

### 选项 `safe_mode`（可选）

此设置将您的网络置于安全模式，这可能会显著降低
网络的性能，但也可能有助于使网络正常运行，以便您可以故障排查问题、获取日志等。
在大多数情况下，用户将不需要使用此功能，因此，仅在您知道自己在做什么和/或被要求时才更改此设置。

### 选项 `network_key`（已弃用）

在以前版本的插件中，这是唯一需要的密钥。随着
在 zwave-js 中引入 S2 安全包含，此选项已被弃用，
取而代之的是 `s0_legacy_key`。如果仍设置，则将在首次启动时将 `network_key` 值迁移到 `s0_legacy_key`。

### 网络问题排查

插件中有几个功能可以帮助您排查网络问题和/或提供数据给 Home Assistant 或 Z-Wave JS 团队以帮助追踪问题：

1. **更新日志级别：** 当您在 GitHub 上打开问题时，将 `log_level` 配置选项设置为 `debug` 并捕捉问题发生时的日志是极其有帮助的。
2. **记录到文件：** `log_to_file` 和 `log_max_files` 配置选项允许您启用并配置该功能。请注意，为了访问日志文件，您需要能够访问 HA 实例的文件系统，您可以通过文件编辑器、samba 或 ssh 插件等访问。
3. **访问 Z-Wave JS 缓存：** Z-Wave JS 将它发现的关于您网络的信息存储在缓存文件中，以便您的设备不会在每次启动时重新审查。在某些情况下，打开 GitHub 问题时，您可能会被要求提供缓存文件。您可以在 `/addon_configs/core_zwave_js/cache` 中访问它们。请注意，为了访问缓存，您需要能够访问 HA 实例的文件系统，您可以通过文件编辑器、samba 或 ssh 插件等访问。
4. **更改软重置行为：** 默认情况下，插件将自动选择是否在启动时软重置控制器。在大多数情况下不应该更改，但如果在故障排查问题时被要求进行更改，您可以使用 `soft_reset` 配置选项进行更改。
5. **禁用控制器恢复：** 默认情况下，如果网络控制器似乎被阻塞，Z-Wave JS 将自动尝试将控制器恢复到正常状态。在大多数情况下不应该更改，但如果在故障排查问题时被要求进行更改，您可以使用 `disable_controller_recovery` 配置选项进行更改。
6. **启用安全模式：** 当 Z-Wave JS 在启动时遇到问题时，有时很难获取有用的日志以排查问题。通过将 `safe_mode` 设置为 true，当 `safe_mode` 设置为 false 时，Z-Wave JS 可能能够启动。请注意，启用 `safe_mode` 会对网络性能产生负面影响，应该谨慎使用。

## 已知问题和限制

- 您的硬件需要与 Z-Wave JS 库兼容

## 支持

有问题吗？

您有多种选择来获得答案：

- [Home Assistant Discord 聊天服务器][discord]。
- Home Assistant [社区论坛][forum]。
- 加入 [/r/homeassistant][reddit] 的 [Reddit 子论坛][reddit]。

如果您发现了一个 bug，请 [在我们的 GitHub 上打开一个问题][issue]。

[discord]: https://discord.gg/c5DvZ4e
[forum]: https://community.home-assistant.io
[issue]: https://github.com/home-assistant/addons/issues
[reddit]: https://reddit.com/r/homeassistant