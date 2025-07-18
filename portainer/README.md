# Home Assistant Community Add-on: Portainer

[![GitHub Release][releases-shield]][releases]
![Project Stage][project-stage-shield]
[![License][license-shield]](LICENSE.md)

![Supports aarch64 Architecture][aarch64-shield]
![Supports amd64 Architecture][amd64-shield]
![Supports armhf Architecture][armhf-shield]
![Supports armv7 Architecture][armv7-shield]
![Supports i386 Architecture][i386-shield]

[![Github Actions][github-actions-shield]][github-actions]
![Project Maintenance][maintenance-shield]
[![GitHub Activity][commits-shield]][commits]

[![Discord][discord-shield]][discord]
[![Community Forum][forum-shield]][forum]

[![Sponsor Frenck via GitHub Sponsors][github-sponsors-shield]][github-sponsors]

[![Support Frenck on Patreon][patreon-shield]][patreon]

轻松管理您的Docker环境。

![The Portainer Hass.io add-on](images/screenshot.png)

## 关于

Portainer是一个开源的轻量级管理界面，允许您轻松管理Docker主机或Docker集群。

管理Docker从未如此简单。Portainer提供Docker的详细概览，并允许您管理容器、镜像、网络和卷。

[:books: 阅读完整插件文档][docs]


## FORKED

该插件已由其作者停止维护，不再从社区仓库提供。
这是一个尽力而为的分叉。

如果您运行Home Assistant，请注意，运行额外的容器不是一个受支持的用例，并且将触发您的系统被标记为不受支持。

## 警告 1

Portainer插件非常强大，并为您提供访问几乎整个系统的权限。虽然这个插件是经过精心创建和维护的，并且考虑了安全性，但在错误或不熟悉的情况下，
它可能会损坏您的系统。

## 警告 2

Portainer插件用于调试Home Assistant及其容器。它并不是为了管理或部署您的自定义软件或第三方容器而设计的。

**Home Assistant DOES NOT SUPPORT运行第三方容器**
在Home Assistant OS或Supervised安装类型上。忽视这一点，将使您的系统变为不受支持！

## 支持

有问题？

[在这里打开问题][issue] GitHub。

## 贡献

这是一个活跃的开源项目。我们始终欢迎那些想要使用代码或为其做出贡献的人。

我们已设置了一个单独的文档，其中包含我们的
[贡献指南](,github/CONTRIBUTING.md)。

感谢您的参与！ :heart_eyes:

## 作者和贡献者

这个仓库的原始设置是由[Franck Nijhof][frenck]完成的。

要查看所有作者和贡献者的完整列表，
请查看[贡献者页面][contributors]。

## 许可证

MIT许可证

版权所有 (c) 2018-2021 Franck Nijhof

特此免费授予任何获得此软件及其相关文档文件（“软件”）副本的人
在不限制的情况下处理软件的权利，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或出售软件副本的权利，并允许提供软件的人这样做，
但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件按“原样”提供，不提供任何形式的保证，明示或暗示，包括但不限于对适销性、特定用途适用性和非侵权性的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害赔偿或其他责任负责，
无论是在合同行为、侵权行为或其他行为中，均不因软件或软件的使用或其他交易而引起。

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[commits-shield]: https://img.shields.io/github/commit-activity/y/hassio-addons/addon-portainer.svg
[commits]: https://github.com/hassio-addons/addon-portainer/commits/main
[contributors]: https://github.com/hassio-addons/addon-portainer/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord-shield]: https://img.shields.io/discord/478094546522079232.svg
[discord]: https://discord.me/hassioaddons
[docs]: https://github.com/hassio-addons/addon-portainer/blob/main/portainer/DOCS.md
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-portainer/68836?u=frenck
[frenck]: https://github.com/frenck
[github-actions-shield]: https://github.com/hassio-addons/addon-portainer/workflows/CI/badge.svg
[github-actions]: https://github.com/hassio-addons/addon-portainer/actions
[github-sponsors-shield]: https://frenck.dev/wp-content/uploads/2019/12/github_sponsor.png
[github-sponsors]: https://github.com/sponsors/frenck
[i386-shield]: https://img.shields.io/badge/i386-no-red.svg
[issue]: https://github.com/hassio-addons/addon-portainer/issues
[license-shield]: https://img.shields.io/github/license/hassio-addons/addon-portainer.svg
[maintenance-shield]: https://img.shields.io/maintenance/yes/2021.svg
[patreon-shield]: https://frenck.dev/wp-content/uploads/2019/12/patreon.png
[patreon]: https://www.patreon.com/frenck
[project-stage-shield]: https://img.shields.io/badge/project%20stage-%20!%20DEPRECATED%20%20%20!-ff0000.svg
[reddit]: https://reddit.com/r/homeassistant
[releases-shield]: https://img.shields.io/github/release/hassio-addons/addon-portainer.svg
[releases]: https://github.com/hassio-addons/addon-portainer/releases
[repository]: https://github.com/hassio-addons/repository