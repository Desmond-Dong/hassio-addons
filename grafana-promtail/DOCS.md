# 非官方 Home Assistant 插件：Promtail

Promtail 被打包为 Home Assistant 插件。

## 默认设置

默认情况下，此插件版本的 Promtail 将从 systemd 日志中获取日志。这将包括来自所有插件、管理程序、Home Assistant、Docker 和主机系统本身的所有日志。如果你安装了 Loki 插件，它会将这些日志发送到同一存储库中的 Loki 插件。如果这是你想要的设置，则无需额外配置。

如果你调整了 Loki 插件的配置，或者有一个单独的 Loki 插件，或者有其他日志文件希望 Promtail 监控，请看下面的配置选项。

## 配置

### 选项：`additional_pipeline_stages`

指向包含额外管道阶段列表的 YAML 文件的绝对路径，这些阶段将应用于 [默认日志抓取配置][addon-default-config]。这个选项的主要用途是对你使用的特定插件的日志进行额外处理，如果它们比较嘈杂或难以阅读。

此文件必须仅包含一个 YAML 列表的管道阶段。它们将被添加到已列出的阶段末尾。如果你不喜欢已列出的阶段，请使用 `skip_default_scrape_config` 和 `additional_scrape_configs` 来自己编写配置。以下是此文件内容的示例：

```yaml
- match:
    selector: '{container_name="addon_cebe7a76_hassio_google_drive_backup"}'
    stages:
      - multiline:
          firstline: '^\x{001b}'
```

这个特定示例适用于 [google drive backup 插件][addon-google-drive-backup]。它使用与 Home Assistant 相同的日志格式，在每个日志行的开头输出转义字符，以便在终端中进行颜色编码。在多行阶段中查找该字符，可以使追踪信息与导致错误的日志条目包括在同一日志条目中，从而更易于阅读。

有关如何配置管道阶段的更多信息，请参见 [promtail 文档][promtail-doc-stages]。

**注意**：此插件可以访问 `/ssl`、`/share` 和 `/config/promtail`。请将文件放在这些位置之一，其他位置将无法工作。

### 选项：`skip_default_scrape_config`

Promtail 将使用预定义配置抓取 `systemd journal`，你可以在 [这里][addon-default-config] 找到。如果你只想查看你指定的特定日志文件，或者不喜欢默认配置并想调整，可以将此设置为 `true`。然后，使用的唯一抓取配置将是你在 `additional_scrape_configs` 文件中指定的那些。

**注意**：此插件可以访问 `/ssl`、`/share` 和 `/config/promtail`。请将文件放在这些位置之一，其他位置将无法工作。

### 选项：`additional_scrape_configs`

指向包含 Promtail 使用的额外抓取配置列表的 YAML 文件的绝对路径。这个选项的主要用途是指向由于不使用 `stdout` 进行所有日志记录而由插件创建的额外日志文件。你还可以使用此选项结合 `skip_default_scrape_config` 更改抓取的系统日志。**注意**：如果 `skip_default_scrape_config` 为 `true`，则此字段变为必需（否则将没有抓取配置）。

该文件必须仅包含一个 YAML 列表的抓取配置。以下是此文件内容的示例：

```yaml
- job_name: zigbee2mqtt_messages
  pipeline_stages:
  static_configs:
    - targets:
        - localhost
      labels:
        job: zigbee2mqtt_messages
        __path__: /share/zigbee2mqtt/log/**.txt
```

这个特定示例将导致 Promtail 抓取 [Zigbee2MQTT 插件][addon-z2m] 默认生成的 MQTT 日志。

Promtail 提供了很多配置抓取配置的选项。有关可用选项及其配置方式的更多信息，请参见 [scrape_configs][promtail-doc-scrape-configs] 文档。文档还提供了 [其他示例][promtail-doc-examples]，供你使用。

我还建议在制作自定义抓取配置之前阅读 [Loki 最佳实践][loki-doc-best-practices] 指南。管道功能非常强大，但应避免创建过多标签，这样会适得其反。相反，可以考虑在另一端使用 [LogQL][logql] 的功能。

**注意**：此插件可以访问 `/ssl`、`/share` 和 `/config/promtail`。请将文件放在这些位置之一，其他位置将无法工作。

### 端口：`9080/tcp`

Promtail 在此端口上公开一个 [API][api]。这主要用于由管理程序监视器进行健康检查，不需要在主机上公开。大多数用户应该将此选项保持禁用，除非你有外部应用程序进行健康检查。

对于创建自定义抓取配置的高级用户，此 API 的另一个目的，是公开由 [metrics][promtail-doc-metrics] 管道阶段生成的指标。公开此端口将允许你从网络上的其他系统读取这些指标。

### 选项：`log_level`

`log_level` 选项控制插件的日志输出级别，可以更改为更详细或更简洁，这在处理未知问题时可能很有用。可能的值有：

- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：不错误的异常情况。
- `error`：不需要立即处理的运行时错误。

请注意，每个级别自动包含更严重级别的日志消息，例如，`debug` 也会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非你正在进行故障排除。

## PLG 堆栈（Promtail、Loki 和 Grafana）

Promtail 不是一个独立应用程序，它的任务是查找日志、处理日志并将其发送到 Loki。你可能想要完整的 PLG 堆栈：

- Promtail 用于处理和发送日志
- Loki 用于聚合和索引它们
- Grafana 用于可视化和监控它们

[addon-default-config]: https://github.com/mdegat01/addon-promtail/blob/main/promtail/rootfs/etc/promtail/default-scrape-config.yaml
[addon-google-drive-backup]: https://github.com/sabeechen/hassio-google-drive-backup
[addon-z2m]: https://github.com/zigbee2mqtt/hassio-zigbee2mqtt
[api]: https://grafana.com/docs/loki/latest/clients/promtail/#api
[logql]: https://grafana.com/docs/loki/latest/logql/
[loki-doc-best-practices]: https://grafana.com/docs/loki/latest/best-practices/
[promtail-doc-examples]: https://grafana.com/docs/loki/latest/clients/promtail/configuration/#example-static-config
[promtail-doc-metrics]: https://grafana.com/docs/loki/latest/clients/promtail/configuration/#metrics
[promtail-doc-scrape-configs]: https://grafana.com/docs/loki/latest/clients/promtail/configuration/#scrape_configs
[promtail-doc-stages]: https://grafana.com/docs/loki/latest/clients/promtail/stages/