# Home Assistant 社区附加组件：Portainer

[![GitHub Release][releases-shield]][releases]
![项目阶段][project-stage-shield]
[![许可证][license-shield]](LICENSE.md)

![支持 aarch64 架构][aarch64-shield]
![支持 amd64 架构][amd64-shield]
![支持 armhf 架构][armhf-shield]
![支持 armv7 架构][armv7-shield]
![支持 i386 架构][i386-shield]

[![Github Actions][github-actions-shield]][github-actions]
![项目维护][maintenance-shield]
[![GitHub 活动][commits-shield]][commits]

[![Discord][discord-shield]][discord]
[![社区论坛][forum-shield]][forum]

[![通过 GitHub Sponsors 支持 Frenck][github-sponsors-shield]][github-sponsors]

[![在 Patreon 上支持 Frenck][patreon-shield]][patreon]

轻松管理你的 Docker 环境。

![Portainer Hass.io 附加组件](images/screenshot.png)

## 关于

Portainer 是一个开源的轻量级管理用户界面，使您能够轻松管理一个或多个 Docker 主机或 Docker Swarm 集群。

管理 Docker 从未如此简单。Portainer 提供了 Docker 的详细概述，允许您管理容器、镜像、网络和卷。

[:books: 阅读完整的附加组件文档][docs]

## FORKED

此附加组件已被其作者停止维护，并且不再从社区存储库中提供。
这是一个尽力而为的 fork。

如果您运行 Home Assistant，请注意运行其他容器并不是支持的用例，这将导致您的系统被标记为不受支持。

## 警告 1

Portainer 附加组件功能强大，几乎可以让您访问整个系统。尽管该附加组件在创建和维护时都考虑了安全性，在错误或缺乏经验的用户手中，可能会对您的系统造成损害。

## 警告 2

Portainer 附加组件旨在调试 Home Assistant 及其容器。
它并不旨在或设计用于管理或部署您的自定义软件或第三方容器。

**Home Assistant 不支持在 Home Assistant OS 或受监督安装类型上运行第三方容器**。忽视这一点将使您的系统被视为不受支持！

## 支持

有问题吗？

[在此打开问题][issue] GitHub。

## 贡献

这是一个活跃的开源项目。我们始终欢迎希望使用或贡献代码的人。

我们已设立一个单独的文档，包含我们的 [贡献指南](,github/CONTRIBUTING.md)。

感谢您的参与！:heart_eyes:

## 作者和贡献者

该存储库的最初设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可

MIT 许可证

版权所有 (c) 2018-2021 Franck Nijhof

特此无偿授予任何获得本软件及其相关文档文件（“软件”）副本的人，处理软件而不受限制的权利，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本，以及允许提供软件的人这样做，须遵守以下条件：

上述版权声明和本许可声明应包含在所有副本或软件的重要部分中。

软件按“原样”提供，不附有任何形式的保证，无论是明示或暗示的，包括但不限于对适销性、特定用途的适应性和非侵权的保证。无论在合同、侵权或其他方面，作者或版权持有人均不对因使用软件或与软件的使用或其他交易而产生的任何索赔、损害或其他责任承担责任。

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