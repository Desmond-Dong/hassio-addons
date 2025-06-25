# Home Assistant 插件: Piper

## 安装

按照以下步骤在您的系统上安装插件：

1. 在 Home Assistant 前端中导航到 **设置** -> **附加组件** -> **附加组件商店**。
2. 找到 "Piper" 附加组件并点击它。
3. 点击 "安装" 按钮。

## 如何使用

安装并运行此插件后，它将被 Home Assistant 的 Wyoming 集成自动发现。要完成设置，请点击以下我的按钮：

[![打开您的 Home Assistant 实例并开始设置新集成。](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=wyoming)

另外，您也可以手动安装 Wyoming 集成，详见[Wyoming 集成文档](https://www.home-assistant.io/integrations/wyoming/)。

## 配置

### 选项: `voice`

[收听语音样本](https://rhasspy.github.io/piper-samples/)

要使用的 Piper 语音名称，例如 `en_US-lessac-medium`（默认）。语音模型会自动从 https://huggingface.co/rhasspy/piper-voices/tree/v1.0.0 下载。

语音的命名遵循以下方案: `<语言>_<地区>-<名称>-<质量>` `<名称>` 部分来自于用于训练语音的数据集或提供的发言者名称。

语音的质量分为 4 个不同级别：

- `x_low` - 16Khz，最小/最快
- `low` - 16Khz，快
- `medium` - 22.05Khz，较慢但音质更好
- `high` - 22.05Khz，最慢但音质最佳

在 Raspberry Pi 4 上，最多可以以可用的速度运行到 `medium` 模型。如果音质不是优先考虑的因素，请优先选择 `low` 或 `x-low` 语音，因为它们的速度明显快于 `medium`。

### 选项: `speaker`

如果语音支持多个扬声器，则使用扬声器编号，例如 [`en-us-libritts-high`](https://rhasspy.github.io/piper-samples/#en-us-libritts-high)。

默认情况下，将使用第一个扬声器（扬声器 0）。

### 选项: `length_scale`

加快或减慢语音。值为 1.0 表示使用语音的默认说话速度，< 1.0 表示更快，> 1.0 表示更慢。

### 选项: `noise_scale`

通过在音频生成过程中添加噪声来控制音频的可变性。效果很大程度上取决于声音本身，但一般来说，值为 0 会去除可变性，值大于 1 会开始降低音频质量。

### 选项: `noise_w`

控制说话节奏的可变性（音素宽度）。效果很大程度上取决于声音本身，但一般来说，值为 0 去除可变性，值大于 1 会产生明显的口吃和停顿。

### 选项: `max_piper_procs`

同时运行的 Piper 进程数量（默认值为 1）。每个 Piper 进程将一个语音模型加载到 RAM 中，因此同时使用多个语音需要：

- 在使用语音时启动/停止 Piper 进程，或
- 运行更多 Piper 进程

此附加组件将为每个请求的语音启动一个 Piper 进程，最多达到 `max_piper_procs`。之后，将停止最近未使用的语音。
如果您需要快速切换多个语音，请增大 `max_piper_procs`，但请注意，这将增加附加组件的 RAM 使用量。

### 选项: `update_voices`

每次附加组件启动时自动下载新语音的列表。您还必须在 Home Assistant 中重新加载 Piper 的 Wyoming 集成以查看新语音。

### 选项: `streaming`

启用流媒体音频支持。这将在句子边界处将文本分开，并在生成音频时进行流式传输。要求至少 HA 2025.7。

### 选项: `debug_logging`

向附加组件的日志打印 DEBUG 级别消息。

## 自定义语音

将自定义语音文件添加到 `/share/piper` 目录。每个自定义语音必须包括一个模型文件 (`<voice>.onnx`) 和配置文件 (`<voice>.onnx.json`)。
有关如何训练和导出自定义语音的详细信息，请参见[训练指南](https://github.com/rhasspy/piper/blob/master/TRAINING.md)。

## 支持

有问题吗？

您有几个选项可以得到解答：

- [Home Assistant Discord 聊天服务器][discord]。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]。

如果您发现了一个错误，请 [在我们的 GitHub 上打开问题][issue]。

[discord]: https://discord.gg/c5DvZ4e
[forum]: https://community.home-assistant.io
[issue]: https://github.com/home-assistant/addons/issues
[reddit]: https://reddit.com/r/homeassistant
[repository]: https://github.com/hassio-addons/repository