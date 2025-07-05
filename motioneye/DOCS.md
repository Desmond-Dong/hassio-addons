# Home Assistant 社区插件：motionEye

motionEye 是一个流行的用于 camera 软件的界面，名为 motion。这个插件提供两者，允许您将您的相机添加到您的 Hass.io 设置中。

motionEye 是一个开源的 CCTV 和 NVR，既美观又非常易于使用。它可以用作婴儿监视器、建筑工地蒙太奇查看器、商店摄像头 DVR、花园安全系统，以及更多。

motionEye 的一些酷炫功能：

- 支持大量的相机，包括 IP 相机。
- 通过将多个 motionEye 实例连接在一起来添加多个相机。例如，在您的网络中使用 Pi Zero + Pi 摄像头的 MotionEyeOS。
- 支持将录制上传到 Google Drive 和 Dropbox。
- motion 检测，包括电子邮件通知和计划。
- 可以连续、motion 或 timelapse 记录，并具有保留设置。
- 支持在配置中实现 "[action buttons][motioneye-wiki-action-buttons]"。

## 安装

这个插件的安装非常简单，与安装任何其他 Home Assistant 插件没有区别。

1. 点击下面的 Home Assistant 我的按钮，在您的 Home Assistant 实例中打开插件。

   [![在您的 Home Assistant 实例中打开此插件。][addon-badge]][addon]

1. 点击“安装”按钮来安装插件。
1. 启动“motionEye”插件
1. 检查“motionEye”插件的日志，看看是否一切顺利。
1. 点击“OPEN WEB UI”按钮来打开网页界面
1. 使用用户名“admin”，无需密码登录。
1. 使用安全的密码编辑您的管理员账户！

默认情况下，Home Assistant 附带社区插件商店。但是，如果它丢失了（出于任何原因），您可以通过点击下面的按钮来添加它。

[![将存储库添加到您的 Home Assitant 实例。][repository-badge]][repository]

## 配置

**注意**：_更改配置时请重新启动插件。_

示例插件配置：

```yaml
log_level: info
ssl: true
certfile: mycertfile.pem
keyfile: mykeyfile.pem
```

**注意**：_这只是一个示例，不要复制粘贴它！创建您自己的！_

### 选项：`log_level`

`log_level` 选项控制插件的日志输出级别，可以更改为更详细或更简洁，这在您处理未知问题时可能很有用。可能的值是：

- `trace`：显示每个细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：非异常的异常情况。
- `error`：不需要立即采取行动的运行时错误。
- `fatal`：发生了严重错误。插件变得无法使用。

请注意，每个级别自动包含更严重级别的日志消息，例如，`debug` 也显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐设置，除非您正在排除故障。

### 选项：`motion_webcontrol`

启用在端口 `7999` 上运行的 motion webcontrol 端点。

:warning: MotionEye HTTP webcontrol **不**支持身份验证，**不**支持 SSL！仅在您知道自己在做什么时启用它！**永远不要**将此端口暴露给外部世界！

### 选项：`ssl`

在 motionEye 的网页界面上启用/禁用 SSL (HTTPS)。设置为 `true` 以启用它，`false` 否则。

### 选项：`certfile`

用于 SSL 的证书文件。

**注意**：_文件必须存储在 `/ssl/`，这是默认的_

### 选项：`keyfile`

用于 SSL 的私钥文件。

**注意**：_文件必须存储在 `/ssl/`，这是默认的_

### 选项：`action_buttons`

如果配置，将创建一个脚本来实现 [action button][motioneye-wiki-action-buttons]。

示例 action buttons 配置：

```yaml
action_buttons:
  - type: light_on
    camera: 1
    command: "curl -s 192.168.1.1/index.html?light=ON > /dev/null"
  - type: light_off
    camera: 1
    command: "curl -s 192.168.1.1/index.html?light=OFF > /dev/null"
```

#### 子选项：`action_buttons.type`

动作按钮的类型。接受的类型是：

- `lock` 和 `unlock`。
- `light_on` 和 `light_off`。
- `alarm_on` 和 `alarm_off`。
- `up`、`right`、`down` 和 `left`。
- `zoom_in` 和 `zoom_out`。
- `preset1` 到 `preset9`。

#### 子选项：`action_buttons.camera`

相机识别编号。对应于在 motionEye UI 中设置的相机编号。

#### 子选项：`action_buttons.command`

按钮被按下时执行的 bash shell 命令。

## 更改日志与发布

此存储库使用 [GitHub 的发布][releases] 功能来维护更改日志。

发布基于 [语义版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将根据以下内容进行增量：

- `MAJOR`：不兼容或主要更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的 bug 修复和软件包更新。

## 支持

有问题？

您有几个选项来获得答案：

- [Home Assistant 社区插件 Discord 服务器][discord] 用于插件支持和功能请求。
- [Home Assistant Discord 服务器][discord-ha] 用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

您也可以在 [GitHub 上打开一个问题][issue]。

## 作者与贡献者

此存储库的原始设置由 [Franck Nijhof][frenck] 完成。

要查看所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2018-2025 Franck Nijhof

特此免费授予任何获得此软件及其相关文档文件（“软件”）副本的人，在软件上进行的未经限制的交易，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权利，并允许提供软件的人这样做，但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分的软件中。

软件按“原样”提供，不提供任何形式的保证，无论是明示的还是暗示的，包括但不限于对适销性、特定用途适用性和非侵权的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害赔偿或其他责任承担责任，无论这些责任是由于合同、侵权或其他行为引起的，均与软件或使用软件或其他交易有关。

[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[addon]: https://my.home-assistant.io/redirect/supervisor_addon/? addon=a0d7b954_motioneye
[contributors]: https://github.com/hassio-addons/addon-motioneye/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[dockerhub]: https://hub.docker.com/r/hassioaddons/motioneye
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-motioneye/71826?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-motioneye/issues
[motioneye-wiki-action-buttons]: https://github.com/motioneye-project/motioneye/wiki/Action-Buttons
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-motioneye/releases
[repository-badge]: https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg
[repository]: https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository
[semver]: https://semver.org/spec/v2.0.0.html