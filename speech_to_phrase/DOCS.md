# Home Assistant 插件：语音短语

## 安装

按照以下步骤将插件安装到您的系统上：

1. 在 Home Assistant 前端导航到 **设置** -> **插件** -> **插件商店**。
2. 找到 "语音短语" 插件并点击它。
3. 点击 "安装" 按钮。

## 使用方法

安装并运行此插件后，它将根据您的 [暴露][] 实体、区域、楼层和 [句子触发器][sentence trigger] 自动进行自我训练。
插件将在必要时自动重新训练。

插件将自动被 Home Assistant 中的 Wyoming 集成发现。要完成设置，请点击以下我的按钮：

[![打开您的 Home Assistant 实例并开始设置新的集成。](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=wyoming)

或者，您可以手动安装 Wyoming 集成，请参阅
[Wyoming 集成文档](https://www.home-assistant.io/integrations/wyoming/)
以获取更多信息。

### 语音命令

查看 [可用的语音命令](https://github.com/OHF-Voice/speech-to-phrase/blob/main/SENTENCES.md)

### 自定义句子

您可以添加 [自定义句子][] 到 `/share/speech-to-phrase/custom_sentences/<语言>/sentences.yaml`，其中 `<语言>` 是：

* `ca` - 加泰罗尼亚语
* `cs` - 捷克语
* `de` - 德语
* `el` - 希腊语
* `en` - 英语
* `es` - 西班牙语
* `eu` - 巴斯克语
* `fa` - 波斯语/法尔斯语
* `fi` - 芬兰语
* `fr` - 法语
* `hi` - 印地语
* `it` - 意大利语
* `mn` - 蒙古语
* `nl` - 荷兰语
* `pl` - 波兰语
* `pt_PT` - 葡萄牙语
* `ro` - 罗马尼亚语
* `ru` - 俄语
* `sl` - 斯洛文尼亚语
* `sw` - 斯瓦希里语
* `tr` - 土耳其语

## 支持

有问题吗？

您有几个选项来获得答案：

- [Home Assistant Discord 聊天服务器][discord]。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

如果您发现了一个错误，请 [在我们的 GitHub 上打开一个问题][issue]。

[discord]: https://discord.gg/c5DvZ4e
[forum]: https://community.home-assistant.io
[issue]: https://github.com/home-assistant/addons/issues
[reddit]: https://reddit.com/r/homeassistant
[repository]: https://github.com/hassio-addons/repository

[sentence trigger]: https://www.home-assistant.io/docs/automation/trigger/#sentence-trigger
[exposed]: https://www.home-assistant.io/voice_control/voice_remote_expose_devices/
[custom sentences]: https://github.com/OHF-voice/speech-to-phrase?tab=readme-ov-file#custom-sentences