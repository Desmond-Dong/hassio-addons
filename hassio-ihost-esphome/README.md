# ESPHome 设备构建器

[![ESPHome logo][logo]][website]

[![GitHub stars][github-stars-shield]][repository]
[![Discord][discord-shield]][discord]
![支持 armv7 架构](https://img.shields.io/badge/armv7-yes-green.svg)


### 免责声明

此存储库提供 **为 armv7 架构定制的 ESPHome 插件和容器镜像**，这些不再由官方 ESPHome 发行版支持。

我们仅维护 **32 位架构** 的兼容性和构建基础设施。
如果您遇到与 **平台架构无关** 的问题（例如 ESPHome 核心功能、YAML 配置或设备支持），请向 [官方 ESPHome 存储库](https://github.com/esphome/esphome) 报告它们。


## 安装
1. 前往插件商店 → 点击右上角的 **更多** 按钮 (⋮) → 选择 **存储库**  
2. 粘贴以下 URL:  
   [https://github.com/iHost-Open-Source-Project/hassio-ihost-addon](https://github.com/iHost-Open-Source-Project/hassio-ihost-addon)  
3. 或者，直接点击下方按钮自动添加：

[![添加存储库](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FiHost-Open-Source-Project%2Fhassio-ihost-addon)

## 关于

此插件允许您编写配置，并通过 Home Assistant **无需编程经验** 将您的微控制器直接转换为智能家居设备。
您需要做的只是在配置文件中编写 YAML 配置文件；其余的（空中更新、编译）都由 ESPHome 处理。

<p align="center">
<img title="ESPHome Device Builder 截图" src="https://github.com/esphome/home-assistant-addon/raw/main/esphome/images/screenshot.png" width="700px"></img>
</p>

[查看 ESPHome 文档][website]

## 示例

使用 ESPHome，您可以从几行 YAML 直接转换到定制的固件。例如，要包含一个 [DHT22][dht22] 温度和湿度传感器，您只需要在配置文件中包含 8 行 YAML：

<img title="ESPHome DHT 配置示例" src="https://github.com/esphome/home-assistant-addon/raw/main/esphome/images/dht-example.png" width="500px"></img>

然后只需点击上传，传感器就会神奇地在 Home Assistant 中出现：

<img title="ESPHome Home Assistant 发现" src="https://github.com/esphome/home-assistant-addon/raw/main/esphome/images/temperature-humidity.png" width="600px"></img>

[discord]: https://discord.gg/KhAMKrd
[repository]: https://github.com/esphome/esphome
[discord-shield]: https://img.shields.io/discord/429907082951524364.svg
[github-stars-shield]: https://img.shields.io/github/stars/esphome/esphome.svg?style=social&label=Star&maxAge=2592000
[dht22]: https://esphome.io/components/sensor/dht.html
[releases]: https://esphome.io/changelog/index.html
[logo]: https://github.com/esphome/home-assistant-addon/raw/main/esphome/logo.png
[website]: https://esphome.io/