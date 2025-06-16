# Home Assistant 插件：Z-Wave JS

## 安装

按照以下步骤在您的系统上安装该插件：

1. 在您的 Home Assistant 界面上导航到 **设置** -> **插件** -> **插件商店**。
2. 找到 "Z-Wave JS" 插件并点击它。
3. 点击 "安装" 按钮。

## 如何使用

该插件需要知道您的 Z-Wave 接口卡的位置，因此，您需要配置插件指向正确的设备。

如果您使用的是 Home Assistant，您可以通过访问 `设置 -> 系统 -> 硬件` 来找到这个值，然后点击三个点菜单并选择 `所有硬件`。如果存在，建议使用 "by-id" 路径指向设备，因为如果系统中添加其他设备，它不会随之改变。

1. 在插件配置中替换 `null` 的 `device` 选项，并在引号中指定设备名称：例如，可以是 `"/dev/serial/by-id/usb-0658_0200-if00"`、 `"/dev/ttyUSB0"`、 `"/dev/ttyAMA0"` 或 `"/dev/ttyACM0"`。
2. 以 `2232666D1...` 的形式设置您的 16 字节（32 个字符十六进制）安全密钥，以便安全连接到兼容设备。建议配置所有四个网络密钥，因为某些启用安全的设备（锁等）如果没有安全添加可能无法正常工作。
   - 需要注意的是，除非设备支持 S2 安全，否则不建议安全连接 _所有_ 设备，因为 S0 安全会使节点在网状网络中发送的消息数量增加三倍。
3. 点击 "保存" 以保存插件配置。
4. 启动插件。
5. 将 Z-Wave JS 集成添加到 Home Assistant，参见文档： <https://www.home-assistant.io/integrations/zwave_js>

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

如果您使用的是 Home Assistant，您可以通过访问 `设置 -> 系统 -> 硬件`，然后点击三个点菜单并选择 `所有硬件` 来找到这个值。如果存在，建议使用 "by-id" 路径指向设备，因为如果系统中添加其他设备，它不会随之改变。

在大多数情况下，这看起来像以下之一：

- `"/dev/serial/by-id/usb-0658_0200-if00"`
- `"/dev/ttyUSB0"`
- `"/dev/ttyAMA0"`
- `"/dev/ttyACM0"`

### 安全密钥

为了充分利用 Z-Wave JS 支持的不同包含方法，需要六个不同的安全密钥：`s0_legacy_key`、`s2_access_control_key`、`s2_authenticated_key`、`s2_unauthenticated_key`、`lr_s2_access_control_key` 和 `lr_s2_authenticated_key`。

如果您来自之前版本的 `zwave-js`，您可能会在 `network_key` 配置选项中有一个存储的密钥。首次启动插件时，密钥将从 `network_key` 迁移到 `s0_legacy_key`，这将确保您的 S0 安全设备继续正常工作。

如果启动时任何密钥缺失，插件将自动为您生成一个。要手动生成网络密钥，您可以在例如 SSH 插件中使用以下脚本：

```bash
hexdump -n 16 -e '4/4 "%08X" 1 "\n"' /dev/random
```

您还可以使用类似于这个网站生成所需的数据：

<https://www.random.org/cgi-bin/randbyte?nbytes=16&format=h>

确保备份这些密钥。如果您必须重建系统而没有备份这些密钥，您将无法与任何安全包含的设备进行通信。这可能意味着您需要对那些设备和控制器进行出厂重置，才能重建您的 Z-Wave 网络。

> 注意：在多个安全级别之间共享密钥存在安全风险，因此如果您选择自己配置这些密钥，请确保使它们唯一！

#### 选项 `s0_legacy_key`

S0 安全 Z-Wave 设备在加入网络之前需要一个网络密钥。该配置选项是必需的，但如果未设置，插件将在启动时自动生成一个新的密钥。

#### 选项 `s2_access_control_key`

必须提供 `s2_access_control_key` 才能包含带有 S2 访问控制安全类的设备。门锁和车库门开启器等设备需要这个安全类。该配置选项是必需的，但如果未设置，插件将在启动时自动生成一个新的密钥。

#### 选项 `s2_authenticated_key`

必须提供 `s2_authenticated_key` 才能包含带有 S2 认证安全类的设备。安全系统、传感器、照明等设备可以请求此安全类。该配置选项是必需的，但如果未设置，插件将在启动时自动生成一个新的密钥。

### 选项 `s2_unauthenticated_key`

必须提供 `s2_unauthenticated_key` 才能包含带有 S2 无认证安全类的设备。这类似于 S2 认证，但未验证所包含的设备是否正确。该配置选项是必需的，但如果未设置，插件将在启动时自动生成一个新的密钥。

#### 选项 `lr_s2_access_control_key`

必须提供 `lr_s2_access_control_key` 才能包含使用 Z-Wave 长距离的设备。该配置选项是必需的，但如果未设置，插件将在启动时自动生成一个新的密钥。

#### 选项 `lr_s2_authenticated_key`

必须提供 `lr_s2_authenticated_key` 才能包含使用 Z-Wave 长距离的设备。该配置选项是必需的，但如果未设置，插件将在启动时自动生成一个新的密钥。

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

启用此选项后，日志将写入 `/addon_configs/core_zwave_js` 文件夹，文件扩展名为 `.log`。

### 选项 `log_max_files`（可选）

当 `log_to_file` 为真时，Z-Wave JS 将为每一天创建一个日志文件。此选项允许您控制 Z-Wave JS 将保留的文件的最大数量。

### 选项 `rf_region`（可选）

此设置告诉插件控制器应使用哪个无线频率区域。有效选项包括：

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

默认值为自动，它将尝试根据 Home Assistant 中设置的国家来设置正确的区域。

### 选项 `soft_reset`（可选）

此设置告诉插件如何处理 500 系列控制器的软重置：
1. 自动 - 插件将决定是否应为 500 系列控制器启用或禁用软重置。这是默认选项，适用于大多数人。
2. 启用 - 将显式为 500 系列控制器启用软重置。
3. 禁用 - 将显式为 500 系列控制器禁用软重置。

### 选项 `emulate_hardware`（可选）

如果您没有 USB 接口卡，可以使用假接口卡进行测试。它将无法控制任何真实设备。

### 选项 `disable_controller_recovery`（可选）

此设置将禁用 Z-Wave JS 的自动恢复过程，当控制器似乎无响应时，它将让控制器自行恢复（如果可能的话）。在控制器无响应时，命令将开始失败，节点可能会随机标记为死亡。如果控制器无法自行恢复，您将需要重新启动插件以尝试恢复。在大多数情况下，用户将不需要使用此功能，因此仅在您知道自己在做什么和/或被要求时更改此设置。

### 选项 `disable_watchdog`（可选）

此设置将防止 Z-Wave JS 在支持的控制器上启用硬件看门狗。在大多数情况下，用户将不需要使用此功能，因此仅在您知道自己在做什么和/或被要求时更改此设置。

### 选项 `safe_mode`（可选）

此设置将您的网络置于安全模式，这可能会显著降低网络性能，但也可能有助于使网络启动并运行，以便您可以排除故障、获取日志等。在大多数情况下，用户将不需要使用此功能，因此仅在您知道自己在做什么和/或被要求时更改此设置。

### 选项 `network_key`（已弃用）

在之前版本的插件中，这是唯一需要的密钥。随着 S2 安全包含在 zwave-js 中的引入，此选项已被弃用，取而代之的是 `s0_legacy_key`。如果仍然设置，`network_key` 值将在首次启动时迁移到 `s0_legacy_key`。

### 排查网络问题

插件中提供了一些功能，可以帮助您排查网络问题和/或向 Home Assistant 或 Z-Wave JS 团队提供数据以帮助追踪问题：

1. **更新日志级别：** 在打开 GitHub 问题时，将 `log_level` 配置选项设置为 `debug` 并捕获问题发生时的情况非常有用。
2. **记录到文件：** `log_to_file` 和 `log_max_files` 配置选项允许您启用和配置该功能。请注意，要访问日志文件，您需要能够访问 HA 实例的文件系统，您可以使用文件编辑器、samba 或 ssh 插件等方式访问。
3. **访问 Z-Wave JS 缓存：** Z-Wave JS 将它发现的有关您网络的信息存储在缓存文件中，以便您的设备不必在每次启动时重新访谈。在某些情况下，打开 GitHub 问题时，您可能会被要求提供缓存文件。您可以在 `/addon_configs/core_zwave_js/cache` 中访问它们。请注意，要访问缓存，您需要能够访问 HA 实例的文件系统，您可以使用文件编辑器、samba 或 ssh 插件等方式访问。
4. **更改软重置行为：** 默认情况下，插件将自动选择是否在启动时软重置控制器。在大多数情况下不应该更改，但如果在排除问题时被要求进行更改，您可以使用 `soft_reset` 配置选项进行更改。
5. **禁用控制器恢复：** 默认情况下，如果网络控制器似乎被阻塞，Z-Wave JS 将自动尝试将控制器恢复到健康状态。在大多数情况下不应该更改，但如果在排除问题时被要求进行更改，您可以使用 `disable_controller_recovery` 配置选项进行更改。
6. **启用安全模式：** 当 Z-Wave JS 启动时遇到问题时，有时很难获取有用的日志来排除问题。通过将 `safe_mode` 设置为 true，Z-Wave JS 可能能够在它以 `safe_mode` 设置为 false 的情况下无法启动时启动。请注意，启用 `safe_mode` 将对网络性能产生负面影响，并应谨慎使用。

## 已知问题和限制

- 您的硬件需要与 Z-Wave JS 库兼容

## 支持

有问题吗？

您有多种选择可以获得答案：

- [Home Assistant Discord 聊天服务器][discord]。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 论坛][reddit] 在 [/r/homeassistant][reddit]。

如果您发现了错误，请 [在我们的 GitHub 上提出问题][issue]。

[discord]: https://discord.gg/c5DvZ4e
[forum]: https://community.home-assistant.io
[issue]: https://github.com/home-assistant/addons/issues
[reddit]: https://reddit.com/r/homeassistant