# Home Assistant 插件：NGINX Home Assistant SSL 代理

设置一个使用 NGINX 的 SSL 代理，并将流量从 80 端口重定向到 443 端口。

![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield] ![支持 armhf 架构][armhf-shield] ![支持 armv7 架构][armv7-shield] ![支持 i386 架构][i386-shield]

## 关于

设置一个使用 NGINX Web 服务器的 SSL 代理。它通常用于转发 SSL 互联网流量，同时允许未加密的本地流量进出 Home Assistant 实例。

确保在开始使用此插件之前已生成证书。 [Duck DNS](https://github.com/home-assistant/hassio-addons/tree/master/duckdns) 插件可以生成可以被此插件使用的 Let's Encrypt 证书。

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
[discord]: https://discord.gg/c5DvZ4e