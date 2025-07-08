# Home Assistant Add-on: Silicon Labs Zigbee/OpenThread Multiprotocol Add-on

基于Silicon Labs的无线电设备（如SONOFF ZBDongle-E）的Zigbee/OpenThread多协议容器。

![支持armv7架构][armv7-shield]
![支持aarch64架构][aarch64-shield]
![支持amd64架构][amd64-shield]

## 关于

此插件允许您在单个基于Silicon Labs的无线电设备上同时使用Zigbee和OpenThread协议。该无线电设备需要安装RCP Multi-PAN固件以支持多个IEEE 802.15.4个人区域网络（PAN）。该插件基于Silicon Labs Multiprotocol Add-on进行修改，并在SONOFF ZBDongle-E上成功测试。

[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg

### 注意事项

1. 由于ZHA集成目前仅支持EZSP v14，而MultiPAN固件基于EZSP v16，因此它只能与Zigbee2MQTT (Z2M)一起使用。
2. 在使用此插件之前，您必须首先通过[SONOFF Dongle Flasher][sonoff-dongle-flasher]刷写MultiPAN固件。

## 已知问题

启用**Silicon Labs Multiprotocol Add-on**后，在首次启动Zigbee2MQTT时可能会报告`ASH_ERROR_TIMEOUTS`错误。重新启动Zigbee2MQTT通常可以解决此问题。此问题已报告给Silicon Labs，目前正在调查中。

[sonoff-dongle-flasher]: https://dongle.sonoff.tech/sonoff-dongle-flasher