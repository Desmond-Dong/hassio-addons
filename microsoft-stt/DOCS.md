# Wyoming Microsoft STT
Wyoming 协议服务器用于 Microsoft Azure 语音转文本。

这个 Python 软件包提供了对 Microsoft Azure 语音转文本的 Wyoming 集成，并且可以直接与 [Home Assistant](https://www.home-assistant.io/) 语音和 [Rhasspy](https://github.com/rhasspy/rhasspy3) 一起使用。

## Azure 语音服务
此程序使用 [Microsoft Azure 语音服务](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/)。您可以注册一个免费的 Azure 账户，该账户包含每月 5 小时的免费层，这对于运行语音助手来说应该足够了，因为每个命令都相对较短。一旦超出这个数量，Azure 可能会为您使用的每秒收费（当前定价为每音频小时 0.36 美元）。我对任何产生的费用不负责，并建议您设置支出限额以减少您的风险。然而，对于正常使用，免费层可能就足够了，并且资源不会自动切换到付费服务。

如果您尚未设置语音资源，请按照以下说明进行操作。（您只需要做一次，并且适用于 [语音转文本](https://github.com/hugobloem/wyoming-microsoft-stt) 和 [文本转语音](https://github.com/hugobloem/wyoming-microsoft-tts)）

1. 在 [portal.azure.com](https://portal.azure.com) 上登录或创建账户。
2. 通过在搜索栏中搜索 `subscription` 创建订阅。[有关更多信息，请参阅 Microsoft Learn](https://learn.microsoft.com/en-gb/azure/cost-management-billing/manage/create-subscription#create-a-subscription-in-the-azure-portal)。
3. 通过搜索 `speech service` 创建语音资源。
4. 选择您创建的订阅，选择或创建资源组，选择一个区域，选择一个可识别的名称，并选择定价层（您可能需要 Free F0）。
5. 创建后，从语音服务页面复制一个密钥。您需要这个密钥来运行此程序。

## 安装
根据您的使用情况，有不同的安装选项。

- **使用 pip**
  克隆存储库并使用 pip 安装软件包。请注意平台要求，如 [此处](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/quickstarts/setup-platform?tabs=linux%2Cubuntu%2Cdotnetcli%2Cdotnet%2Cjre%2Cmaven%2Cnodejs%2Cmac%2Cpypi&pivots=programming-language-python#platform-requirements) 所述。
  ```sh
  pip install .
  ```

- **Home Assistant 插件**
  将以下存储库作为 Home Assistant 的插件存储库添加，或点击下面的按钮。
  [https://github.com/hugobloem/homeassistant-addons](https://github.com/hugobloem/homeassistant-addons)

  [![打开您的 Home Assistant 实例并显示带有特定存储库 URL 预填的添加插件存储库对话框。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fhome-assistant%2Faddons-example)

- **Docker 容器**
  即将推出...

## 使用
根据安装方法的不同，参数的解析方式也不同。然而，每种安装方法都使用相同的选项，如下表所示。您的服务区域和订阅密钥可以在语音资源页面（Azure 语音服务说明的第 5 步）找到。

对于裸金属 Python 安装，程序运行如下：
```python
python -m wyoming-microsoft-stt --<key> <value>
```

| Key | Optional | Description |
|---|---|---|
| `service-region` | No | Azure 服务区域，例如 `uksouth` |
| `subscription-key` | No | Azure 订阅密钥 |
| `uri` | No | 服务器将广播的 Uri，例如 `tcp://0.0.0.0:10300` |
| `download-dir` | Yes | 下载模型的目标目录（默认：） |
| `language` | Yes | 设置转录的默认语言，默认：`en-GB` |
| `update-languages` | Yes | 在启动时下载最新的 languages.json |
| `debug` | Yes | 记录调试消息 |