## 警告：打开问题：[birdnet-go 启动失败（打开于 2025-09-06）](https://github.com/alexbelgium/hassio-addons/issues/2086) by [@smcdako](https://github.com/smcdako)
# Home assistant 插件：Birdnet-Go

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fbirdnet-go%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=入口&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fbirdnet-go%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fbirdnet-go%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建者](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建者)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库星标的人！要给星标，请点击下面的图片，然后它就会在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://reporoster.com/stars/alexbelgium/hassio-addons)](https://github.com/alexbelgium/hassio-addons/stargazers)


![下载趋势](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/birdnet-go/stats.png)

## 关于

[BirdNET-Go](https://github.com/tphakala/birdnet-go/tree/main) 是一个用于持续鸟类监测和识别的 AI 解决方案，由 @tphakala 开发。

这个插件基于他们的 Docker 镜像。

## 配置

安装并首次启动插件后，WebUI 可以在 <http://homeassistant:8080> 找到。
您需要一个麦克风：可以使用连接到 HA 的麦克风，或者使用 RTSP 摄像机的音频流。

音频片段文件夹可以通过在插件选项中挂载它来存储在外部或 SMB 驱动器上，然后指定路径而不是 "clips/"。例如，"/mnt/NAS/Birdnet/"

选项可以通过三种方式配置：

- 插件选项

```yaml
ALSA_CARD : 卡号（通常是 0 或 1），请查看 https://github.com/tphakala/birdnet-go/blob/main/doc/installation.md#deciding-alsa_card-value
TZ: Etc/UTC 指定一个时区来使用，请查看 https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List
COMMAND : realtime --rtsp url # 允许提供鸟net-go 的参数
```

- config.yaml
使用 Filebrowser 插件在 /config/db21ed7f_birdnet-go/config.yaml 文件中配置额外的变量

- config_env.yaml
在那里可以配置额外的环境变量

### 挂载驱动器

这个插件支持挂载本地驱动器和远程 SMB 共享：

- **本地驱动器**：请查看 [在插件中挂载本地驱动器](https://github.com/alexbelgium/hassio-addons/wiki/Mounting-Local-Drives-in-Addons)
- **远程共享**：请查看 [在插件中挂载远程共享](https://github.com/alexbelgium/hassio-addons/wiki/Mounting-remote-shares-in-Addons)

### 自定义脚本和环境变量

这个插件支持通过 `addon_config` 映射来配置自定义脚本和环境变量：

- **自定义脚本**：请查看 [在插件中运行自定义脚本](https://github.com/alexbelgium/hassio-addons/wiki/Running-custom-scripts-in-Addons)
- **环境变量**：请查看 [向您的插件添加环境变量](https://github.com/alexbelgium/hassio-addons/wiki/Add-Environment-variables-to-your-Addon)

## 安装

这个插件的安装非常简单，与安装任何其他插件没有什么不同。

1. 将我的插件仓库添加到您的 Home Assistant 实例（在右上角的 Supervisor 插件商店中，或者如果您已经配置了我的 HA，请点击下面的按钮）

   [![打开您的 Home Assistant 实例并显示一个具有特定仓库 URL 预填的添加插件仓库对话框。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装这个插件。
1. 点击 `保存` 按钮以保存您的配置。
1. 将插件选项设置为您的偏好。
1. 启动插件。
1. 检查插件的日志，看看是否一切正常。
1. 打开 WebUI 并调整软件选项

## 与 HA 集成

Home Assistant 集成说明在这里，[Birdnet-Go 插件：Home Assistant 集成](./HAINTEGRATION.md)

## 使用 VLC 设置 RTSP 源

VLC 打开一个 TCP 端口，但流是 UDP。因此需要配置 Birdnet-Go 使用 UDP。调整 config.yaml 文件为 UDP 或使用 birdnet-go 命令行选项：

`--rtsptransport udp --rtsp rtsp://192.168.1.21:8080/stream.sdp`

### Linux 说明

使用以下命令之一运行 vlc 而不使用界面：

```bash
# 这应该适用于大多数设备
/usr/bin/vlc -I dummy -vvv alsa://hw:0,0 --no-sout-all --sout-keep --sout '#transcode{acodec=mpga}:rtp{sdp=rtsp://:8080/stream.sdp}'

# 如果第一个命令不起作用，请尝试这个
/usr/bin/vlc -I dummy -vvv alsa://hw:4,0 --no-sout-all --sout-keep --sout '#rtp{sdp=rtsp://:8080/stream.sdp}'
```

运行 `arecord -l` 以获取麦克风硬件信息

```text
**** 捕获硬件设备列表 ****
card 0: PCH [HDA Intel PCH], device 0: ALC3220 Analog [ALC3220 Analog]
  子设备: 1/1
  子设备 #0: 子设备 #0
card 2: S7 [SteelSeries Arctis 7], device 0: USB Audio [USB Audio]
  子设备: 1/1
  子设备 #0: 子设备 #0
card 3: Nano [Yeti Nano], device 0: USB Audio [USB Audio]
  子设备: 1/1
  子设备 #0: 子设备 #0
card 4: 设备 [USB PnP Sound Device], device 0: USB Audio [USB Audio]
  子设备: 0/1
  子设备 #0: 子设备 #0
```

hw:4,0 = **card 4**: 设备 [USB PnP Sound Device], **device 0**: USB Audio [USB Audio]

Systemd 服务文件示例。根据情况调整用户:组。如果您想以 root 身份运行，您可能需要运行 vlc-wrapper 而不是 vlc。

```text
[Unit]
Description=VLC Birdnet RTSP 服务器
Wants=network-online.target
After=network-online.target

[Service]
Type=simple
StandardOutput=journal
ExecStart=/usr/bin/vlc -I dummy -vvv alsa://hw:0,0 --sout '#transcode{acodec=mpga}:rtp{sdp=rtsp://:8080/stream.sdp}'
User=someone
Group=somegroup

[Install]
WantedBy=multi-user.target
```

## 常见问题

尚未提供

## 支持

在 GitHub 上创建一个问题