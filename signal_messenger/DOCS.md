# Signal Messenger 插件 for Home Assistant

这个插件允许您通过 Signal Messenger 向在他们的设备上安装了 Signal Messenger 应用的收件人发送消息。

## 安装

- 将此存储库添加到 Home Assistant Supervisor 插件商店
- 点击安装
- 选择您所需的端口
- 选择您所需的选项
- 点击开始

## 使用

使用说明可以在官方 [文档](https://www.home-assistant.io/integrations/signal_messenger/) 中找到。

## 选项

### 模式

此选项允许您设置 MODE 环境变量。这取代了 Use Native 变量并添加了一个额外的模式。

有效选项：

- 'normal'：每个 REST API 请求都调用 signal-cli JAVA 应用程序（最慢的模式）
- 'native'：每个 REST API 请求都调用编译好的原生镜像（比正常模式更快）
- 'json-rpc'：signal-cli JAVA 应用程序启动一次，REST API 包装器通过 JSON-RPC 与其通信（启动时间较长，但一旦 Java 应用程序运行，应该是最快的）

### 自动接收

此选项由上游项目推荐，如果您没有设置用于监听新消息的 REST API 端点，请启用它。有关更多详细信息，请参阅文档 [这里](https://github.com/bbernhard/signal-cli-rest-api#auto-receive-schedule)。此选项不适用于 json-rpc 模式，在该模式下将被忽略。

有效选项：

- `off`：禁用自动接收
- `on`：启用自动接收（默认）

### SIGNAL-CLI 命令超时

此选项设置在超时 signal cli 命令前等待的秒数。此选项不适用于 json-rpc 模式，在该模式下将被忽略。（默认：60s）

### 重置数据

此选项删除所有数据并重置插件。请注意，所有您的设置都将被销毁。

## 版本控制

此插件遵循上游容器的版本控制。此插件与在此处找到的容器 [这里](https://github.com/bbernhard/signal-cli-rest-api) 的差异非常小。
截至本文写作时，上游容器版本控制使用 0.xx 模式进行发布。此插件遵循相同模式，但使用 0.xx.y，其中 y 表示与 Home Assistant 插件特定更改相关的上游更改。

## 与上游的差异

此插件与上游的主要区别在于持久存储的位置已从：`/home/.local/share/signal-cli` 更改为：`/data`。
还有一个脚本运行以允许设置上述选项。

## 错误报告

错误报告可以提交到 [插件存储库](https://github.com/haberda/hassio_addons)，或提交到 [上游存储库](https://github.com/bbernhard/signal-cli-rest-api)。
在提交报告之前，请尝试确定您的错误是否与插件特定问题相关，还是与应用程序问题相关。插件特定问题应提交到插件存储库，应用程序特定问题应提交到上游存储库。