# Home Assistant Add-on: Piper

## 安装

按照以下步骤将插件安装到您的系统上：

1. 在 Home Assistant 前端导航到 **设置** -> **插件** -> **插件商店**。
2. 查找 "Piper" 插件并点击它。
3. 点击 "安装" 按钮。

## 如何使用

此插件安装并运行后，它将被 Home Assistant 中的 Wyoming 集成自动发现。要完成设置，请点击以下我的按钮：

[![打开您的 Home Assistant 实例并开始设置新的集成。](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=wyoming)

或者，您可以手动安装 Wyoming 集成，有关更多信息，请参阅
[Wyoming 集成文档](https://www.home-assistant.io/integrations/wyoming/)。

## 配置

### 选项：`voice`

[收听语音样本](https://rhasspy.github.io/piper-samples/)

要使用的 Piper 语音的名称，例如 `en_US-lessac-medium`（默认值）。
语音模型会自动从 https://huggingface.co/rhasspy/piper-voices/tree/v1.0.0 下载。

语音的命名遵循以下方案：`<语言>_<区域>-<名称>-<质量>`
`<名称>` 部分来自用于训练语音的数据集或如果提供了，则是说话者的名称。

语音的质量有四个不同的级别：

- `x_low` - 16Khz，最小/最快
- `low` - 16Khz，快速
- `medium` - 22.05Khz，较慢但听起来更好
- `high` - 22.05Khz，最慢但最好听

在 Raspberry Pi 4 上，最高 `medium` 模型将以可用的速度运行。如果音频质量不是优先考虑，请优先选择 `low` 或 `x-low` 语音，因为它们将比 `medium` 明显更快。

### 选项：`speaker`

如果语音支持多个扬声器，请使用扬声器编号，例如 [`en-us-libritts-high`](https://rhasspy.github.io/piper-samples/#en-us-libritts-high)。

默认情况下，将使用第一个扬声器（扬声器 0）。

### 选项：`length_scale`

加速或减慢语音。值为 1.0 表示使用语音的默认说话速度，小于 1.0 表示更快，大于 1.0 表示更慢。

### 选项：`noise_scale`

通过在音频生成过程中添加噪声来控制音频的变异性。效果高度依赖于语音本身，但通常情况下，值为 0 会去除变异性，而值大于 1 会开始降低音频质量。

### 选项：`noise_w`

控制说话节奏（音素宽度）的变异性。效果高度依赖于语音本身，但通常情况下，值为 0 会去除变异性，而值大于 1 会导致极端的卡顿和停顿。

### 选项：`max_piper_procs`

同时运行的 Piper 进程数量（默认为 1）。每个 Piper 进程将一个语音模型加载到 RAM 中，因此同时使用多个语音需要：

- 随着语音的使用而启动/停止 Piper 进程，或
- 运行更多的 Piper 进程

此插件将为每个请求的语音启动最多 `max_piper_procs` 个 Piper 进程。之后，最不常用的语音将被停止。
如果需要快速切换多个语音，请增加 `max_piper_procs`，但请注意这将增加插件的 RAM 使用量。

### 选项：`update_voices`

每次插件启动时自动下载新语音列表。您还必须重新加载 Home Assistant 中的 Piper Wyoming 集成以查看新语音。

### 选项：`streaming`

启用流式音频支持。这将分割文本到句子边界并随着音频的生成而流式传输。至少需要 HA 2025.7。

### 选项：`debug_logging`

将 DEBUG 级别的消息打印到插件的日志中。

## 自定义语音

将自定义语音文件添加到 `/share/piper` 目录。每个自定义语音必须包含一个模型文件（`<voice>.onnx`）和配置文件（`<voice>.onnx.json`）。
有关如何训练和导出自定义语音的详细信息，请参阅 [训练指南](https://github.com/rhasspy/piper/blob/master/TRAINING.md)。

## 支持

有问题？

您有几个选项可以回答这些问题：

- [Home Assistant Discord 聊天服务器][discord]。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

如果您发现了一个错误，请 [在我们的 GitHub 上打开一个问题][issue]。

[discord]: https://discord.gg/c5DvZ4e
[forum]: https://community.home-assistant.io
[issue]: https://github.com/home-assistant/addons/issues
[reddit]: https://reddit.com/r/homeassistant
[repository]: https://github.com/hassio-addons/repository