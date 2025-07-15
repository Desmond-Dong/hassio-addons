# SONOFF Dongle Flasher

![Supports armv7 Architecture](https://img.shields.io/badge/armv7-yes-green.svg) ![Supports aarch64 Architecture](https://img.shields.io/badge/aarch64-yes-green.svg) ![Supports amd64 Architecture](https://img.shields.io/badge/amd64-yes-green.svg)
 
## About

SONOFF Dongle Flasher 支持iHost MG21芯片和SONOFF Dongle系列（ZBDongle-P和ZBDongle-E）的在线固件刷新。

## Prerequisites

在使用插件之前，请确保串口未被使用（它通常被Zigbee2MQTT或ZHA等服务占用）。
在固件刷新过程中，插件将尝试连接到设备并自动检查串口是否被占用。
如果被占用，插件将尝试为您停止冲突的服务。
[操作指南 >](https://github.com/iHost-Open-Source-Project/ha-operating-system?tab=readme-ov-file#readme)


## Installation
1. 前往插件商店 → 点击右上角的**更多**按钮（⋮）→ 选择**仓库**  
2. 粘贴以下URL：  
   [https://github.com/iHost-Open-Source-Project/hassio-ihost-addon](https://github.com/iHost-Open-Source-Project/hassio-ihost-addon)  
3. 或者，直接点击下方按钮自动添加：

[![添加仓库](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FiHost-Open-Source-Project%2Fhassio-ihost-addon)

## How to use

有关如何使用SONOFF Dongle Flasher插件的详细信息，请参阅“文档”。