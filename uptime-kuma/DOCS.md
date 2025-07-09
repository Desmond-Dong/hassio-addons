# Home Assistant Community Add-on: Uptime Kuma

Uptime Kuma 是一个开源的监控工具，最好可以与商业服务（如 "Uptime Robot"）的自托管版本进行比较。

它能够让您监控 HTTP/S、TCP、DNS 及其他协议的服务，并且可以发送您停机或触发 Home Assistant 自动化 webhook 的通知。

## 安装

这个 add-on 的安装过程非常直接，与安装任何其他 Home Assistant add-on 并无不同。

1. 点击下方的 Home Assistant My 按钮，在您的 Home Assistant 实例中打开 add-on。

   [![在您的 Home Assistant 实例中打开此 add-on][addon-badge]][addon]

1. 点击 "Install" 按钮来安装 add-on。
1. 启动 "Uptime Kuma" add-on。
1. 查看 "Uptime Kuma" 的日志，以确认一切是否正常。
1. 点击 "OPEN WEB UI" 按钮进入 Uptime Kuma。

请继续阅读本文档的其余部分以获取进一步说明。

## 配置

这个 add-on 没有配置选项，一切都可以通过 Uptime Kuma 界面进行管理和配置。

## 更改日志与发布

此存储库使用 [GitHub 的发布][releases] 功能维护更改日志。日志的格式基于
[Keep a Changelog][keepchangelog]。

发布基于 [Semantic Versioning][semver]，并使用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将根据以下方式增加：

- `MAJOR`：不兼容或主要更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的 Bug 修复和包更新。

## 支持

有问题吗？

您有几个选项来获得答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord] 用于 add-on 支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 用于一般的 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

您也可以在 GitHub 上 [打开一个问题][issue]。

## 作者与贡献者

此存储库的原始设置由 [Franck Nijhof][frenck] 完成。

要获取所有作者和贡献者的完整列表，
请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2022-2025 Franck Nijhof

特此授予任何获得此软件及其相关文档文件（即 "软件"）副本的人，在不限制的情况下自由处理软件的权利，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权利，并允许提供软件的人这样做，但须遵守以下条件：

上述版权声明和此许可声明应包含在软件的所有副本或重要部分中。

软件按 "原样" 提供，不提供任何形式的保证，包括但不限于对适销性、特定用途适用性和非侵权性的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害赔偿或其他责任负责，无论这些责任是由于合同、侵权或其他行为引起的，还是由于与软件或软件的使用或其他交易有关。