# Home Assistant 插件：Whisper

## 安装

按照以下步骤在您的系统上安装插件：

1. 在您的 Home Assistant 前端导航到 **设置** -> **插件** -> **插件商店**。
2. 找到 "Whisper" 插件并点击它。
3. 点击 "安装" 按钮。

## 如何使用

安装并运行此插件后，它将被 Home Assistant 中的 Wyoming 集成自动发现。要完成设置，请点击以下我的按钮：

[![打开您的 Home Assistant 实例并开始设置新集成。](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=wyoming)

或者，您可以手动安装 Wyoming 集成，详细信息请参见 [Wyoming 集成文档](https://www.home-assistant.io/integrations/wyoming/)。

## 配置

### 选项：`language`

插件的默认语言。在 Home Assist 2023.8+ 中，不同的 [Assist 管道](https://www.home-assistant.io/voice_control/voice_remote_local_assistant/) 可以同时使用多种语言。

如果您选择 "auto"，模型的运行速度将会 **大大** 降低，但会自动检测所说的语言。

[支持语言的性能](https://github.com/openai/whisper#available-models-and-languages)

[两字母语言代码列表](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)

### 选项：`model`

用于转录的 Whisper 模型。选择 `custom` 来使用 `custom_model` 中的模型名称，该模型可能是类似 "Systran/faster-distil-whisper-small.en" 的 HuggingFace 模型 ID。

默认模型是 `auto`，对于像 Raspberry Pi 4 这样的 ARM 设备选择 `tiny-int8`，否则选择 `base-int8`。
压缩模型 (`int8`) 的准确性略低于其对应模型，但更小且更快。[Distilled](https://github.com/huggingface/distil-whisper) 模型未压缩，但比未蒸馏版本更快且更小。

可用模型：

- `auto`（根据 CPU 选择）
- `tiny-int8`（压缩）
- `tiny`
- `tiny.en`（仅英语）
- `base-int8`（压缩）
- `base`
- `base.en`（仅英语）
- `small-int8`（压缩）
- `distil-small.en`（蒸馏，仅英语）
- `small`
- `small.en`（仅英语）
- `medium-int8`（压缩）
- `distil-medium.en`（蒸馏，仅英语）
- `medium`
- `medium.en`（仅英语）
- `large`
- `large-v1`
- `distil-large-v2`（蒸馏，仅英语）
- `large-v2`
- `distil-large-v3`（蒸馏，仅英语）
- `large-v3`
- `turbo`（比 `large-v3` 更快）

### 选项：`custom_model`

转换模型目录的路径，或来自 HuggingFace Hub 的 CTranslate2 转换的 Whisper 模型 ID，如 "Systran/faster-distil-whisper-small.en"。

如果 `custom_model_type` 设置为 `transformers`，则必须使用 HuggingFace 的 transformers Whisper 模型 ID，如 "openai/whisper-tiny.en"。

要使用本地自定义 Whisper 模型，请首先在插件的配置目录中创建一个 `models` 子目录（如果该目录尚不存在）。然后将您的模型目录复制到：
`/addon_configs/core_whisper/models/<your-model-dir>`。
接着，将 `custom_model` 路径设置为：
`/config/models/<your-model-dir>`。对于本地模型，路径必须以 `/config/models/` 开头，因为这是插件通过容器挂载卷访问您的 Home Assistant 配置目录的方式。

### 选项：`custom_model_type`

可以是 `faster-whisper`（默认值）或 `transformers`。

当设置为 `transformers` 时，`custom_model` 选项必须是 HuggingFace  transformers 的 Whisper 模型，如 "openai/whisper-tiny.en"。

**注意：** 目前不支持 transformers 基于模型的初始提示。

### 选项：`beam_size`

在转录过程中同时考虑的候选数量（请参见 [波束搜索](https://en.wikipedia.org/wiki/Beam_search)）。
默认值 `0` 将会自动选择 `1` 的 ARM 设备，如 Raspberry Pi 4，其他情况下选择 `5`。

增加波束大小将提高准确性，但会影响性能。

### 选项：`initial_prompt`

音频描述可以帮助 Whisper 更好地转录不寻常的单词。
请参见 [这个讨论](https://github.com/openai/whisper/discussions/963) 以获取一个示例。

## 备份

Whisper 模型文件可能很大，因此在备份时会自动排除，并在恢复时重新下载远程模型。
在使用本地自定义 Whisper 模型恢复备份后，请手动再次复制您的模型目录。

## 支持

有问题吗？

您有几种方式可以得到答案：

- [Home Assistant Discord 聊天服务器][discord]。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]。

如果您发现了一个错误，请 [在我们的 GitHub 上开一个问题][issue]。

[discord]: https://discord.gg/c5DvZ4e
[forum]: https://community.home-assistant.io
[issue]: https://github.com/home-assistant/addons/issues
[reddit]: https://reddit.com/r/homeassistant
[repository]: https://github.com/hassio-addons/repository