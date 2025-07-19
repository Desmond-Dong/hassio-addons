# Home Assistant Add-on: stt-fallback

一个使用 [语音转文本实体](https://www.home-assistant.io/integrations/stt) 进行回退的 Home Assistant 拓展。

运行一个 [wyoming](https://github.com/OHF-Voice/wyoming/) 语音转文本 (STT) 服务器，按顺序尝试 STT 实体，直到其中一个成功。

## 安装

按照以下步骤在你的系统上安装该拓展：

1. 在 Home Assistant 前端导航到 **设置** -> **拓展** -> **拓展商店**。
2. 添加商店 https://github.com/rhasspy/hassio-addons
3. 找到 "stt-fallback" 拓展并点击它。
4. 点击 "安装" 按钮。

## 如何使用

安装此拓展后，在配置中输入你的语音转文本实体 ID（用空格分隔）。例如：

```
stt.speech_to_phrase stt.home_assistant_cloud
```

将首先尝试 [Speech-to-Phrase](https://github.com/OHF-voice/speech-to-phrase)，如果失败则回退到 Home Assistant 云。

回退的 STT 服务器将由 Home Assistant 中的 Wyoming 集成自动发现。要完成设置，点击以下我的按钮：

[![打开你的 Home Assistant 实例并开始设置一个新的集成。](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=wyoming)

或者，你可以手动安装 Wyoming 集成，请参阅
[Wyoming 集成文档](https://www.home-assistant.io/integrations/wyoming/)
以获取更多信息。

## 支持

有问题？

你有几个选项来得到解答：

- [Home Assistant Discord 聊天服务器][discord]。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

如果你发现了一个错误，请 [在我们的 GitHub 上打开一个问题][issue]。

[discord]: https://discord.gg/c5DvZ4e
[forum]: https://community.home-assistant.io
[issue]: https://github.com/home-assistant/addons/issues
[reddit]: https://reddit.com/r/homeassistant
[repository]: https://github.com/rhasspy/hassio-addons