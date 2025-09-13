# Home Assistant Community Add-on: FTP

[![Release][release-shield]][release] ![Project Stage][project-stage-shield] ![Project Maintenance][maintenance-shield]

[![Discord][discord-shield]][discord] [![Community Forum][forum-shield]][forum]

[![Sponsor Frenck via GitHub Sponsors][github-sponsors-shield]][github-sponsors]

[![Support Frenck on Patreon][patreon-shield]][patreon]

一个安全且快速的FTP服务器，用于Home Assistant

## 关于

FTP协议有时会派上用场。虽然它已经过时，但仍然有其用途。例如，大多数IP摄像头仍然支持通过FTP上传图像或视频。

此插件以合理安全的方式为Hass.io提供FTP服务器。虽然FTP由于其（未加密）的性质并不完全安全，但此插件支持FTP over SSL（FTPS）并将在其主目录中隔离虚拟用户。

当然，如果你真的想这样做，你也可以使用此插件再次通过FTP访问你的Home Assistant配置。

[discord-shield]: https://img.shields.io/discord/478094546522079232.svg
[discord]: https://discord.me/hassioaddons
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-ftp/36799?u=frenck
[github-sponsors-shield]: https://frenck.dev/wp-content/uploads/2019/12/github_sponsor.png
[github-sponsors]: https://github.com/sponsors/frenck
[maintenance-shield]: https://img.shields.io/maintenance/yes/2025.svg
[patreon-shield]: https://frenck.dev/wp-content/uploads/2019/12/patreon.png
[patreon]: https://www.patreon.com/frenck
[project-stage-shield]: https://img.shields.io/badge/project%20stage-production%20ready-brightgreen.svg
[release-shield]: https://img.shields.io/badge/version-v5.3.3-blue.svg
[release]: https://github.com/hassio-addons/addon-ftp/tree/v5.3.3