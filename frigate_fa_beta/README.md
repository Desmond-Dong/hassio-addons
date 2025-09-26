# Home Assistant 添加组件：Frigate (完全访问) Beta

请参考 [发布说明](https://github.com/blakeblackshear/frigate/releases) 了解重大变更。

![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield] ![支持 armv7 架构][armv7-shield]

NVR 支持实时本地对象检测，适用于 IP 摄像头。

您必须在添加组件的配置文件夹中创建一个名为 `config.yml` 的配置文件。

此版本的添加组件请求完全设备访问权限，以便关闭那些在启用保护模式时无法正常工作的设备的保护模式。

[文档](https://docs.frigate.video)

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg