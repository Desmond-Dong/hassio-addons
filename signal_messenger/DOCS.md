# Signal Messenger 附加组件用于 Home Assistant

这个附加组件允许你通过 Signal Messenger 向在其设备上安装 Signal Messenger 应用程序的接收者发送消息。

## 安装

- 将此库添加到 Home Assistant Supervisor 附加组件商店
- 点击安装
- 选择你想要的端口
- 选择你希望的选项
- 点击启动

## 使用

使用说明可以在官方 [文档](https://www.home-assistant.io/integrations/signal_messenger/) 中找到。

## 选项

### 模式

此选项允许你设置 MODE 环境变量。它替代了使用原生变量并增加了一个额外的模式。

有效选项：

- 'normal'：每个 REST API 请求都会调用 signal-cli JAVA 应用程序（最慢模式）
- 'native'：每个 REST API 请求都会调用一个编译的原生映像（比正常模式快）
- 'json-rpc'：signal-cli JAVA 应用程序只启动一次，REST API 包装器通过 JSON-RPC 与其通信（启动时间慢，但一旦 Java 应用程序运行，它应该是最快的）

### 自动接收

如果你没有设置用于监听新消息的 REST API 端点，则建议启用此选项。更多详情请查看文档 [这里](https://github.com/bbernhard/signal-cli-rest-api#auto-receive-schedule)。此选项不适用于 json-rpc 模式，并将在该模式中被忽略。

有效选项：

- `off`：禁用自动接收
- `on`：启用自动接收（默认）

### SIGNAL-CLI 命令超时

此选项设置在超时 signal cli 命令之前的等待时间（以秒为单位）。此选项不适用于 json-rpc 模式，并将在该模式中被忽略。（默认：60秒）

### 重置数据

此选项会删除所有数据并重置附加组件。请注意，所有设置将被销毁。

## 版本控制

该附加组件遵循上游容器的版本控制。这个附加组件与在 [这里](https://github.com/bbernhard/signal-cli-rest-api) 找到的容器之间几乎没有差别。在写这篇文章时，上游容器版本使用 0.xx 模式发布。该附加组件遵循相同的模式，但使用 0.xx.y，其中 y 表示与 Home Assistant 附加组件特定更改相关的上游更改。

## 与上游的差异

该附加组件与上游之间的主要区别在于持久存储的位置已从 `/home/.local/share/signal-cli` 更改为 `/data`。
还有一个脚本运行以允许设置上述选项。

## 错误报告

错误报告可以通过 [附加组件库](https://github.com/haberda/hassio_addons) 或 [上游库](https://github.com/bbernhard/signal-cli-rest-api) 提交。请在提交报告之前尝试确定您的错误是否与附加组件特定问题或应用程序问题相关。附加组件特定问题应提交给附加组件库，应用程序特定问题应提交给上游库。