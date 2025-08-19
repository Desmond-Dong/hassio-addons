# Home Assistant Add-on: FreshRSS

一个免费、可自托管的聚合器。

## 安装

将此仓库添加到你的 [Hass.io](https://home-assistant.io/hassio/) 实例：

`https://github.com/einschmidt/hassio-addons`

如果你遇到问题，可以参考 [官方文档](https://home-assistant.io/hassio/installing_third_party_addons/)。

然后安装 "FreshRSS" 添加项。

## 配置

**注意**：_当配置更改时，请记住重启添加项。_

示例添加项配置：

```yaml
log_level: info
base_url: example.domain.com
ssl: false
certfile: fullchain.pem
keyfile: privkey.pem
```

### 选项：`log_level`

`log_level` 选项控制添加项的日志输出级别，可以更改为更详细或不详细，这在处理未知问题时可能很有用。可能的值有：

- `trace`：显示每个细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：非错误的异常情况。
- `error`：不需要立即处理的运行时错误。
- `fatal`：出了严重问题。添加项变得无法使用。

请注意，每个级别都会自动包含更严重级别的日志消息，例如，`debug` 也会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，除非你在排除故障，否则这是推荐设置。

### 选项：`base_url`

FreshRSS 实例的可访问地址。

### 选项：`ssl`

启用/禁用 Web 界面的 SSL (HTTPS)！将其设置为 `true` 以启用它，否则设置为 `false`。

### 选项：`certfile`

用于 SSL 的证书文件。

**注意**：_文件必须存储在 `/ssl/` 中，这是默认设置。_

### 选项：`keyfile`

用于 SSL 的私钥文件。

**注意**：_文件必须存储在 `/ssl/` 中，这是默认设置。_

## 第三方扩展

此添加项允许你使用 **addon_config** 文件夹存储和管理 FreshRSS 扩展。

- 此文件夹在添加项内部映射自 **Home Assistant addon_config 目录**。
- 如果从 GitHub 仓库安装，它存储在：

```
/addon_configs/{REPO}_freshrss/extensions