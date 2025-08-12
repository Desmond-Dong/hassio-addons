# ESPHome Device Builder (开发分支)

[![ESPHome logo][logo]][website]

[![GitHub stars][github-stars-shield]][repository]
[![Discord][discord-shield]][discord]

## 关于

这个插件允许您编写配置，并通过 Home Assistant 将您的微控制器直接转换为智能家居设备，**无需编程经验**。
您需要做的就是编写 YAML 配置文件；其余的（空中更新、编译）都由 ESPHome 处理。

<p align="center">
<img title="ESPHome Device Builder 截图" src="https://github.com/esphome/home-assistant-addon/raw/main/esphome-dev/images/screenshot.png" width="700px"></img>
</p>

[查看 ESPHome 文档][website]

## 示例

使用 ESPHome，您可以从几行 YAML 直接到定制固件。例如，要包含一个 [DHT22][dht22] 温度和湿度传感器，您只需要在配置文件中包含 8 行 YAML：

<img title="ESPHome DHT 配置示例" src="https://github.com/esphome/home-assistant-addon/raw/main/esphome-dev/images/dht-example.png" width="500px"></img>

然后只需点击上传，传感器就会神奇地出现在 Home Assistant 中：

<img title="ESPHome Home Assistant 发现" src="https://github.com/esphome/home-assistant-addon/raw/main/esphome-dev/images/temperature-humidity.png" width="600px"></img>

[discord]: https://discord.gg/KhAMKrd
[repository]: https://github.com/esphome/esphome
[discord-shield]: https://img.shields.io/discord/429907082951524364.svg
[github-stars-shield]: https://img.shields.io/github/stars/esphome/esphome.svg?style=social&label=Star&maxAge=2592000
[dht22]: https://next.esphome.io/components/sensor/dht.html
[releases]: https://next.esphome.io/changelog/index.html
[logo]: https://github.com/esphome/home-assistant-addon/raw/main/esphome-dev/logo.png
[website]: https://next.esphome.io/