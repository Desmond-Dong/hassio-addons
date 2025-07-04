# Home Assistant Community Add-on: EMQX

[EMQX][emqx] 是一个开源的 MQTT 中间件，具有高性能的实时消息处理引擎，为大规模的物联网设备提供事件流服务。作为最可扩展的 MQTT 中间件，EMQX 可以帮助您连接任何设备，无论规模大小（包括您的家庭设备）。

[EMQX MQTT 中间件][emqx] 是 Home Assistant 中通常使用的 Mosquitto MQTT 中间件/插件的高级替代品。它具有一个用于配置、管理和调试您的 MQTT 中间件、客户端和流量的用户界面。

虽然 EMQX 主要在其网站上将其产品作为云托管产品销售，但此插件在完全本地、自托管的環境中运行 EMQX。

## 安装

此插件的安装非常直接，与安装任何其他 Home Assistant 插件没有区别。

1. 点击下面的 Home Assistant 我的按钮，在您的 Home Assistant 实例上打开插件。

   [![在您的 Home Assistant 实例中打开此插件。][插件徽章]][插件]

1. 点击“安装”按钮以安装插件。
1. 启动“EMQX”插件。
1. 检查“EMQX”的日志，看看是否一切顺利。
1. 打开 Web UI。
1. 使用默认凭据登录：用户名 `admin` 和密码 `public`。
1. 请确保首先为您的 MQTT 客户端设置身份验证，但在 EMQX Web UI 下的“访问控制”->“身份验证”中设置身份验证方法。
1. 再次阅读上述步骤，并**确保**您已设置身份验证。

_注意：_

- 在配置 Home Assistant 时，将 Zigbee2MQTT 或 Home Assistant 机器上的任何其他 MQTT 应用程序或客户端配置为连接到 eMQX，使用 `homeassistant` 或 `a0d7b954-emqx` 作为要连接的中间件/主机名。
- 在将外部设备连接到您的 EMQX 插件时，使用您的 Home Assistant 实例的 IP 地址或主机名作为要连接的中间件/主机名。

## 配置

您很可能不需要这些配置选项。几乎所有的配置都可以通过此插件提供的 Web UI 来完成。一些更高级/复杂的配置选项不在 Web UI 中可用，但可以使用此选项进行配置（例如，在设置多个实例的集群时）。

**注意**：_更改配置时，请记住重新启动插件。_

示例插件配置：

```yaml
env_vars:
  - name: EMQX_NODE__NAME
    value: "something@else.local"
```

**注意**：_这只是示例，不要复制粘贴！创建您自己的！_

### 选项：`env_vars`

此选项允许您通过使用环境变量来调整 EMQX 的各个方面。查看本章开头的示例，了解配置的外观。

有关使用这些变量的更多信息，请参阅官方 EMQX 文档：

<https://www.emqx.io/docs/en/v5.0/admin/cfg.html>

**注意**：_只接受以 `EMQX_` 开头的环境变量。_\_

## 已知问题和限制

- 此插件不能与 Mosquitto 插件同时运行。
- EMQX 默认使用端口 1883、8083、8084 和 8883。您的现有插件中可能有一个与这些端口冲突。在这种情况下，您需要更改其他插件的端口或更改 EMQX 的监听端口。要更改 EMQX 的端口，您需要临时停止冲突的插件，因为您需要访问 EMQX Web UI 来更改监听端口。
- AlexxIT 的 WebRTC 集成已知会导致端口 8083 的端口冲突。可以暂时禁用集成（类似于上述插件点的操作），以允许访问 EMQX Web UI 来调整监听器。

## 更改日志与发布

此存储库使用 GitHub 的发布功能维护更改日志。

发布基于 [语义版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 格式。简而言之，版本将根据以下内容进行递增：

- `MAJOR`：不兼容或主要更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的补丁和软件包更新。

## 支持

有问题？

您有几个选项来获得答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord] 用于插件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

您也可以在 GitHub 上 [打开一个问题][issue]。

## 作者与贡献者

此存储库的原始设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有（c）2023-2025 Franck Nijhof

特此免费授予任何获得此软件及其相关文档文件（“软件”）副本的人，在不受限制的情况下处理该软件的权利，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权利，并允许获得软件的人这样做，但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件按“原样”提供，不提供任何明示或暗示的保证，包括但不限于对适销性、特定用途适用性和非侵权性的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害赔偿或其他责任承担责任，无论是合同行为、侵权行为或其他行为，均由软件引起、发生或与之有关，或由软件的使用或其他交易引起。