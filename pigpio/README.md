# pigpio

将 C 控制库 [pigpio](https://github.com/joan2937/pigpio) 封装在 Home Assistant 插件中，以实现轻松安装。

[![发布版本][release-badge]][release]
![插件阶段][stage-badge]

[![赞助][donation-badge]][donation-url]

## 使用方法

此插件运行 pigpio 守护进程，监听 HTTP 命令并相应地控制 Raspberry Pi 上的 GPIO（目前仅支持 PI 4）。
运行此插件并在 Home Assistant 配置中使用 [remote_rpi_pgio 集成](https://www.home-assistant.io/integrations/remote_rpi_gpio/)，指向 `localhost`，将连接这两个世界。

对于守护进程的附加选项，请使用可选插件设置 `additional_options`。
选项 `-g -f` 将始终被设置！

## 安全性

它访问主机上的 `/dev/mem`，并且具有对原始 IO 数据的完全访问权限。

[stage-badge]: https://img.shields.io/badge/插件阶段-stable-green.svg

[release-badge]: https://img.shields.io/badge/版本-v1.6.0-blue.svg
[release]: https://github.com/Poeschl-HomeAssistant-Addons/pigpio/tree/v1.6.0

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee-%23d32f2f?logo=buy-me-a-coffee&style=for-the-badge&logoColor=white
[donation-url]: https://www.buymeacoffee.com/Poeschl