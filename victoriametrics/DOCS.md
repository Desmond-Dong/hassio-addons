# 非官方 Home Assistant 插件：VictoriaMetrics

将 VictoriaMetrics 打包为 Home Assistant 插件。

## HomeAssistant

要将数据从 Home Assistant 发送到 VictoriaMetrics，您可以使用
[InfluxDB][integration-influxdb] 或
[Prometheus][integration-prometheus] 整合。

您可以根据自己的喜好进行配置。确保包含/排除您所需的实体/域。

### InfluxDB 特点

请注意以下两点：

1. VictoriaMetrics 仅保存整数和日期值。它不保存字符串值。
2. 您选择的 `measurement_attr` 的值。这决定了您如何创建系列，如果您希望每个实体都有自己的系列，最好选择 `entity_id`。对于基于 `domain` 或 `measurement` 的系列，您应选择相应的值。
   请参考 [官方整合文档][integration-influxdb-measurement]。

为了避免出现大量空的指标，调整 `ignore_attributes` 来排除您不感兴趣的内容是很重要的。下面是一个很多异常的例子。您可以将其设置为全局或针对每个实体。

```yaml
influxdb:
  api_version: 1
  host: <<<请使用插件信息页面中的主机名>>>
  port: 8428
  max_retries: 3

  measurement_attr: entity_id

  tags_attributes:
    - friendly_name
    - unit_of_measurement

  ignore_attributes:
    - app_id
    - app_name
    - access_token
    - assumed_state
    - attribution
    - auto_update
    - color
    - device_class
    - device_file
    - device_trackers
    - editable
    - effect
    - effect_list
    - entity_id
    - entity_picture
    - event
    - forecast
    - friendly_name
    - frontend_stream_type
    - has_date
    - has_time
    - hs_color
    - id
    - icon
    - last_triggered
    - level_config
    - marker_type
    - max
    - max_color_temp_kelvin
    - max_mireds
    - media_content_type
    - media_title
    - media_artist
    - media_album_name
    - media_duration
    - media_position
    - media_position_updated_at
    - min
    - min_color_temp_kelvin
    - min_mireds
    - mode
    - next_dawn
    - next_duska
    - next_midnight
    - next_noon
    - next_rising
    - next_setting
    - on_level
    - options
    - pattern
    - power_on_behavior
    - precipitation_unit
    - preset_modes
    - pressure_unit
    - release_summary
    - release_url
    - rgb_color
    - skipped_version
    - source_list
    - state_class
    - state_closed
    - state_open
    - stateExtra
    - step
    - source
    - sound_mode
    - sound_mode_list
    - sound_mode_raw
    - supported_color_modes
    - supported_features
    - temperature_unit
    - unit_of_measurement
    - unitOfMeasure
    - user_id
    - visibility_unit
    - wind_speed_unit
    - writable
    - xy_color
```

## 配置

### 保留

在这里您可以指定 VictoriaMetrics 应该保留其数据多长时间。您可以将其设置为任何 VictoriaMetrics 支持的字符串（[查看文档][documentation-metrics]）。
默认值为 `5y`。

### 自定义启动参数

您可以通过此文本框传递服务器或代理支持的任何命令行参数。随意使用，选择权在您。

### 自定义配置文件

如果您想从 Home Assistant 或任何其他服务抓取 Prometheus 端点，您只需在指定的配置文件夹中创建一个 `prometheus.yaml` 文件，它将被自动导入：

```yaml
global:
  scrape_interval: 1m
  scrape_timeout: 15s

scrape_configs:
  - job_name: "home-assistant"
    scrape_interval: "5s"
    scrape_timeout: "4s"
    metrics_path: /api/prometheus
    authorization:
      credentials: "<<您的令牌>>"
    scheme: http
    static_configs:
      - targets: ["http://homeassistant:8123/api/prometheus"]
```

如果由于某些原因您需要为 VMAgent 或服务器进行特殊配置：
您可以在额外的命令行参数中指定 Home Assistant 配置路径中的任何文件。

[documentation-metrics]: https://github.com/VictoriaMetrics/VictoriaMetrics#retention
[integration-influxdb]: https://www.home-assistant.io/integrations/influxdb/
[integration-prometheus]: https://www.home-assistant.io/integrations/prometheus/
[integration-influxdb-measurement]: https://www.home-assistant.io/integrations/influxdb/#measurement_attr