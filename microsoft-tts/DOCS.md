# Wyoming Microsoft TTS
Wyoming协议服务器用于Microsoft Azure文本转语音。

此Python软件包提供Wyoming对Microsoft Azure文本转语音的集成，并且可以直接与[Home Assistant](https://www.home-assistant.io/)语音和[Rhasspy](https://github.com/rhasspy/rhasspy3)一起使用。

## Azure语音服务
此程序使用[Microsoft Azure语音服务](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/)。您可以注册一个免费的Azure帐户，该帐户包含每月500K字符的免费套餐，这应该足以运行一个语音助手，因为每个指令相对较短。此外，在Home Assistant中，输出会被缓存，因此每个响应只需要请求一次。一旦超出此数量，Azure可能会对每秒使用的时长收费（当前定价为每音频小时0.36美元）。我不对任何产生的费用负责，并建议您设置消费限额以减少您的风险。然而，对于正常使用，免费套餐可能就足够了，资源不会自动切换到付费服务。

如果您尚未设置语音资源，请按照以下说明进行操作。（您只需要做一次，并且适用于[Speech-to-Text](https://github.com/hugobloem/wyoming-microsoft-stt)和[Text-to-Speech](https://github.com/hugobloem/wyoming-microsoft-tts)）

1. 在[portal.azure.com](https://portal.azure.com)上登录或创建帐户。
2. 通过在搜索栏中搜索`subscription`来创建订阅。[有关更多信息，请参阅Microsoft Learn](https://learn.microsoft.com/en-gb/azure/cost-management-billing/manage/create-subscription#create-a-subscription-in-the-azure-portal)。
3. 通过搜索`speech service`来创建语音资源。
4. 选择您创建的订阅，选择或创建资源组，选择一个区域，选择一个可识别的名称，并选择定价套餐（您可能需要免费F0）。
5. 创建后，从语音服务页面复制一个密钥。您需要这个密钥来运行此程序。

## 安装
根据您的使用情况，有不同的安装选项。

- **使用pip**
  克隆存储库并使用pip安装软件包。请注意这里提到的平台要求[此处](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/quickstarts/setup-platform?tabs=linux%2Cubuntu%2Cdotnetcli%2Cdotnet%2Cjre%2Cmaven%2Cnodejs%2Cmac%2Cpypi&pivots=programming-language-python#platform-requirements)。
  ```sh
  pip install .
  ```

- **Home Assistant插件**
  将以下存储库作为插件存储库添加到您的Home Assistant，或点击下面的按钮。
  [https://github.com/hugobloem/homeassistant-addons](https://github.com/hugobloem/homeassistant-addons)

  [![打开您的Home Assistant实例并显示带有特定存储库URL预填的添加插件存储库对话框。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fhome-assistant%2Faddons-example)

- **Docker容器**
  即将推出...

## 使用
根据安装方法的不同，参数的解析方式也不同。然而，每种安装方法都使用相同的选项，如下表所示。您可以在语音服务资源页面（Azure语音服务说明的第5步）找到您服务区域和订阅密钥。

对于裸机Python安装，程序如下运行：
```python
python -m wyoming-microsoft-tts --<key> <value>
```

| 键 | 可选 | 描述 |
|---|---|---|
| `service-region` | 否 | Azure服务区域，例如 `uksouth` |
| `subscription-key` | 否 | Azure订阅密钥 |
| `uri` | 否 | 服务器将广播的URI，例如 `tcp://0.0.0.0:10300` |
| `download-dir` | 是 | 下载voices.json的目录（默认：/tmp/） |
| `voice` | 是 | 为转写设置的默认语音，默认：`en-GB-SoniaNeural` |
| `auto-punctuation` | 是 | 自动添加标点符号（默认：`".?!"`） |
| `samples-per-chunk` | 是 | 每个音频块的样本数（默认：1024） |
| `update-voices` | 是 | 在启动时下载最新的languages.json |
| `debug` | 是 | 记录调试消息 |