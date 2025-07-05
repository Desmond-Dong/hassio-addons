# Home Assistant 插件：NGINX Home Assistant SSL 代理

使用 NGINX 设置 SSL 代理，并将端口 80 的流量重定向到 443。

![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield] ![支持 armhf 架构][armhf-shield] ![支持 armv7 架构][armv7-shield] ![支持 i386 架构][i386-shield]

## 关于

使用 NGINX Web 服务器设置 SSL 代理。通常用于转发 SSL 互联网流量，同时允许未加密的本地流量到/从 Home Assistant 实例。

在开始此插件之前，请确保您已经生成了一个证书。[Duck DNS](https://github.com/home-assistant/hassio-addons/tree/master/duckdns) 插件可以生成 Let's Encrypt 证书，该证书可用于此插件。

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
[discord]: https://discord.gg/c5DvZ4e