# ESPHome设备构建器测试版

[![ESPHome logo][logo]][website]

[![GitHub stars][github-stars-shield]][repository]
[![Discord][discord-shield]][discord]

## 关于

这个插件允许你编写配置文件，并通过Home Assistant将你的微控制器转变为智能家居设备，**无需编程经验**。
你只需编写YAML配置文件；其余的（空中固件更新、编译）都由ESPHome处理。

<p align="center">
<img title="ESPHome设备构建器截图" src="https://github.com/esphome/home-assistant-addon/raw/main/esphome-beta/images/screenshot.png" width="700px"></img>
</p>

[查看ESPHome文档][website]

## 示例

使用ESPHome，你可以从几行YAML直接生成自定义固件。
例如，要包含一个[DHT22][dht22]温湿度传感器，你只需在配置文件中添加8行YAML：

<img title="ESPHome DHT配置示例" src="https://github.com/esphome/home-assistant-addon/raw/main/esphome-beta/images/dht-example.png" width="500px"></img>

然后只需点击上传，传感器就会神奇地出现在Home Assistant中：

<img title="ESPHome Home Assistant发现" src="https://github.com/esphome/home-assistant-addon/raw/main/esphome-beta/images/temperature-humidity.png" width="600px"></img>

[discord]: https://discord.gg/KhAMKrd
[repository]: https://github.com/esphome/esphome
[discord-shield]: https://img.shields.io/discord/429907082951524364.svg
[github-stars-shield]: https://img.shields.io/github/stars/esphome/esphome.svg?style=social&label=Star&maxAge=2592000
[dht22]: https://beta.esphome.io/components/sensor/dht.html
[releases]: https://beta.esphome.io/changelog/index.html
[logo]: https://github.com/esphome/home-assistant-addon/raw/main/esphome-beta/logo.png
[website]: https://beta.esphome.io/