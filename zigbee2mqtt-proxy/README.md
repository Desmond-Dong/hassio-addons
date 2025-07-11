# Home Assistant 插件：Zigbee2MQTT 代理

[![Docker Pulls](https://img.shields.io/docker/pulls/zigbee2mqtt/zigbee2mqtt-proxy-amd64.svg?style=flat-square&logo=docker)](https://cloud.docker.com/u/zigbee2mqtt/repository/docker/dwelch2101/zigbee2mqtt-proxy-amd64)

⚠️ 此插件不包含 Zigbee2MQTT ⚠️

此插件作为外部运行的 Zigbee2MQTT 实例的代理。 
此插件的唯一目的是在 Home Assistant 的侧边栏中添加一个 Zigbee2MQTT 图标，该图标将打开外部运行的 Zigbee2MQTT 前端。

## 选项

- `server` (必需): 这应该是 Zigbee2MQTT 前端正在运行的本地 URL，例如 `http://192.168.2.43:8080`。确保没有尾随斜杠！
- `auth_token` (可选): 仅在您在 Zigbee2MQTT 配置中为前端设置了 `auth_token` 时使用。