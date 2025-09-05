# Home Assistant Community Add-on: Tor

[![Release][release-shield]][release] ![Project Stage][project-stage-shield] ![Project Maintenance][maintenance-shield]

[![Discord][discord-shield]][discord] [![Community Forum][forum-shield]][forum]

[![Sponsor Frenck via GitHub Sponsors][github-sponsors-shield]][github-sponsors]

[![Support Frenck on Patreon][patreon-shield]][patreon]

保护您的隐私并通过Tor访问Home Assistant。

## 关于

此Tor插件允许您将Home Assistant实例作为洋葱站点访问，
通过[Tor的隐藏服务][tor-hidden-service]功能。启用此功能后，
您无需打开防火墙端口或设置HTTPS即可启用安全的远程访问。

如果您想要：

- 远程访问您的Home Assistant实例，而无需打开防火墙端口或设置VPN。
- 没有想要或知道如何获取SSL/TLS证书和HTTPS配置。
- 想要阻止攻击者甚至能够访问/扫描您的端口和服务器。
- 想要阻止任何人知道您的家庭IP地址并看到您访问Home Assistant的流量。

该插件还提供将Sock代理打开到Tor网络的可能性。允许您通过Home Assistant安装访问Tor，通过您的任何（支持SOCKS）应用程序。

[discord-shield]: https://img.shields.io/discord/478094546522079232.svg
[discord]: https://discord.me/hassioaddons
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-tor/33822?u=frenck
[github-sponsors-shield]: https://frenck.dev/wp-content/uploads/2019/12/github_sponsor.png
[github-sponsors]: https://github.com/sponsors/frenck
[maintenance-shield]: https://img.shields.io/maintenance/yes/2025.svg
[patreon-shield]: https://frenck.dev/wp-content/uploads/2019/12/patreon.png
[patreon]: https://www.patreon.com/frenck
[project-stage-shield]: https://img.shields.io/badge/project%20stage-production%20ready-brightgreen.svg
[release-shield]: https://img.shields.io/badge/version-v6.1.2-blue.svg
[release]: https://github.com/hassio-addons/addon-tor/tree/v6.1.2
[tor-hidden-service]: https://www.torproject.org/docs/hidden-services.html.en