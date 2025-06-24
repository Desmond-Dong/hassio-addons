# Home Assistant 社区插件：Portainer

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

轻松管理您的 Docker 环境。

![Portainer Hass.io 插件](images/screenshot.png)

## 关于

Portainer 是一个开源的轻量级管理 UI，允许您
轻松管理 Docker 主机或 Docker 集群。

管理 Docker 从未如此简单。 Portainer 提供了 Docker 的详细
概述，并允许您管理容器、镜像、网络和
卷。

[:books: 阅读完整的插件文档][docs]


## 分支

此插件已被其作者停止支持，且不再从社区库中提供。
这是一个尽力而为的分支。

如果您运行 Home Assistant，请注意运行额外的容器
并不是被支持的用例，这将导致您的系统被标记为
不受支持。

## 警告 1

Portainer 插件非常强大，让您几乎访问
整个系统。虽然此插件在创建和维护时谨慎考虑了
安全性，但在错误或缺乏经验的手中，
它可能会损坏您的系统。

## 警告 2

Portainer 插件用于调试 Home Assistant 及其容器。
它并不旨在或设计用于管理或部署您的自定义软件
或第三方容器。

**Home Assistant 不支持在 Home Assistant OS 或
监督安装类型上运行第三方容器**。忽视这一点将导致
您的系统被标记为不受支持！

## 支持

有问题吗？

[在这里打开一个问题][issue] GitHub。

## 贡献

这是一个活跃的开源项目。我们始终欢迎希望使用
代码或对其做出贡献的人。

我们已设置一个单独的文档，包含我们的
[贡献指南](,github/CONTRIBUTING.md)。

感谢您的参与！:heart_eyes:

## 作者与贡献者

该库的原始设置由 [Franck Nijhof][frenck] 完成。

要查看所有作者和贡献者的完整列表，
请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权 (c) 2018-2021 Franck Nijhof

特此免费授予任何获得本软件及相关文档文件（“软件”）副本的人，来处理
该软件而不受限制，包括但不限于使用、复制、修改、合并、发布、分发、再授权和/或销售
该软件的副本，并允许向其提供软件的人这样做，前提是满足以下条件：

上述版权声明和此授权声明应包含在所有
副本或软件的实质部分中。

该软件是“按原样”提供的，没有任何类型的保证，无论是明确
还是隐含，包括但不限于对适销性、
特定用途适用性和不侵权的保证。在任何情况下，作者或版权持有者均不对任何索赔、损害或其他
责任承担责任，无论是合同诉讼、侵权诉讼或其他，因使用或与
软件或使用或其他交易相关而产生的。

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