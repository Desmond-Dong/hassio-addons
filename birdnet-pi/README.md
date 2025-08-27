## 警告：打开问题：[🐛 [Birdnet-Pi] Birdnet Docker无法打开网页终端登录错误（于2025-08-02打开）](https://github.com/alexbelgium/hassio-addons/issues/1991) by [@ignmedia](https://github.com/ignmedia)

# Home assistant插件：birdnet-pi

![捐赠](https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white)
![捐赠](https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white)

![版本](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fbirdnet-pi%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fbirdnet-pi%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fbirdnet-pi%2Fconfig.json)

![Codacy徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)(https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)(https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建器)(https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我仓库点赞的人！要点赞请点击下面的图片，然后它将出现在右上角。谢谢！_

![星标者仓库列表](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)(https://github.com/alexbelgium/hassio-addons/stargazers)

![下载趋势](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/birdnet-pi/stats.png)

## 关于

_注意：如需在没有HomeAssistant（经典Docker容器）的情况下使用，请参阅[这里](https://github.com/alexbelgium/hassio-addons/blob/master/birdnet-pi/README_standalone.md)_

---

[birdnet-pi](https://github.com/Nachtzuster/BirdNET-Pi) 是一个用于连续鸟类监测和识别的AI解决方案，最初由 @mcguirepr89 在GitHub上开发（https://github.com/mcguirepr89/BirdNET-Pi），目前由 @Nachtzuster 和其他开发者在一个活跃的分叉中继续维护（https://github.com/Nachtzuster/BirdNET-Pi）。

插件的特性：
- 由 [linuxserver](https://github.com/linuxserver/docker-baseimage-debian) 提供的稳健基础镜像
- 感谢 https://github.com/gdraheim/docker-systemctl-replacement，使得docker系统正常工作
- 使用HomeAssistant的pulseaudio服务器
- 使用HomeAssistant的tmpfs来在RAM中存储临时文件，避免磁盘磨损
- 将所有配置文件暴露到 /config 以允许持久化和轻松访问
- 允许修改存储鸟类歌曲的位置（最好是一个外部硬盘）
- 支持ingress，以允许安全远程访问而不暴露端口

## 配置

---

安装并首次启动插件
Webui可以通过两种方式找到：
- 通过HomeAssistant的ingress（无需密码，但某些功能无法工作）
- 使用 <http://homeassistant:port> 直接访问，端口为birdnet.conf中定义的端口。当提示输入密码时，用户名是 `birdnet`，密码是可以在birdnet.con中定义的（默认为空白）。这与插件选项中的密码不同，后者是访问网页终端必须使用的密码

网页终端访问：用户名 `pi`，密码：在插件选项中定义的密码

您需要一个麦克风：可以使用连接到HomeAssistant的麦克风，或使用RSTP摄像头的音频流。

选项可以通过三种方式配置：

- 插件选项

```yaml
BIRDSONGS_FOLDER: 存储鸟类歌曲文件的文件夹 # 如果您想避免分析过程中的磁盘拥塞，应将其设置为SSD
MQTT_DISABLED : 如果为true，将禁用自动mqtt发布。仅在已经有一个本地代理可用时才有效
LIVESTREAM_BOOT_ENABLED: 从启动时开始直播，或从设置中开始
PROCESSED_FOLDER_ENABLED : 如果启用，您需要在birdnet.conf（或birdnet的设置）中设置最后要保存的wav文件数量，将它们保存在tmpfs中的临时文件夹 "/tmp/Processed" 中（因此不会磨损磁盘），如果您想检索它们。此数量可以从插件选项中调整
TZ: Etc/UTC 指定一个时区使用，见 https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List
pi_password: 设置访问网页终端的用户密码
localdisks: sda1 #将您的硬盘的硬件名称用逗号分隔，或其标签。例如。 sda1, sdb1, MYNAS...
networkdisks: "//SERVER/SHARE" #可选，要挂载的smb服务器列表，用逗号分隔
cifsusername: "username" #可选，smb用户名，所有smb共享相同
cifspassword: "password" #可选，smb密码
cifsdomain: "domain" #可选，允许为smb共享设置域
```

- config.yaml
使用Filebrowser插件在 /config/db21ed7f_birdnet-pi/config.yaml 中找到的 config.yaml 文件配置附加变量

- config_env.yaml
在那里可以配置附加环境变量

### 挂载驱动器

此插件支持本地驱动器和远程SMB共享的挂载：

- **本地驱动器**：参见 [在插件中挂载本地驱动器](https://github.com/alexbelgium/hassio-addons/wiki/Mounting-Local-Drives-in-Addons)
- **远程共享**：参见 [在插件中挂载远程共享](https://github.com/alexbelgium/hassio-addons/wiki/Mounting-remote-shares-in-Addons)

### 自定义脚本和环境变量

此插件通过 `addon_config` 映射支持自定义脚本和环境变量：

- **自定义脚本**：参见 [在插件中运行自定义脚本](https://github.com/alexbelgium/hassio-addons/wiki/Running-custom-scripts-in-Addons)
- **环境变量**：参见 [为您的插件添加环境变量](https://github.com/alexbelgium/hassio-addons/wiki/Add-Environment-variables-to-your-Addon)

## 安装

---

此插件的安装非常简单，与安装任何其他插件没有区别。

1. 将我的插件仓库添加到您的Home Assistant实例中（在supervisor插件商店的右上角，或如果您已经配置了我的HA，请点击下面的按钮）
   ![打开您的Home Assistant实例并显示带有预填充特定仓库URL的添加插件仓库对话框](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)(https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装此插件。
1. 点击 `保存` 按钮以保存您的配置。
1. 设置插件选项以符合您的偏好
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 打开WebUI并调整软件选项

## 与Home Assistant的集成

---
### Apprise

您可以使用apprise通过mqtt发送通知，然后使用HomeAssistant对这些通知进行操作
更多信息：https://wander.ingstar.com/projects/birdnetpi.html

### 自动mqtt

如果安装了mqtt，插件将自动更新birdnet主题，以每个检测到的物种

## 使用ssl

---

选项1：安装let's encrypt插件，生成证书。它们默认存储在 /ssl 中，为certfile.pem和keyfile.pem。只需在插件选项中启用ssl，它就会工作。

选项2：启用端口80，将您的BirdNET-Pi URL设置为https。证书将由caddy自动生成

## 改进检测

---

### 增益卡片

使用Terminal标签中的alsamixer，确保音量足够高，但不要太高（不要在红色部分）
https://github.com/mcguirepr89/BirdNET-Pi/wiki/Adjusting-your-sound-card

### Ferrite

在我的情况下，添加ferrite beads导致噪声更差

### 辅助到usb适配器

根据我的测试，只有使用KT0210的适配器（如Ugreen的）可以工作。我无法检测到基于ALC的适配器

### 麦克风比较

推荐麦克风（[完整讨论在这里](https://github.com/mcguirepr89/BirdNET-Pi/discussions/39)）：
- Clippy EM272 (https://www.veldshop.nl/en/smart-clippy-em272z1-mono-omni-microphone.html) + ugreen辅助到usb连接器：最佳灵敏度，使用领夹技术
- Boya By-LM40：最佳性价比
- Hyperx Quadcast：最佳灵敏度，使用心形技术

结论，使用Dahua的麦克风已经足够好，EM272是最优的，但Boya by-lm40是一个非常好的折衷方案，因为birndet模型分析0-15000Hz范围

![图片](https://github.com/alexbelgium/hassio-addons/assets/44178713/df992b79-7171-4f73-b0c0-55eb4256cd5b)

### Denoise（[完整讨论在这里](https://github.com/mcguirepr89/BirdNET-Pi/discussions/597)）

Denoise受到严肃研究人员的批评。但它似乎显著提高了检测质量！在HomeAssistant中如何进行：
- 使用Portainer插件，进入hassio_audio容器，并修改文件 /etc/pulse/system.pa 以添加行 `load-module module-echo-cancel`
- 进入Terminal插件，并输入 `ha audio restart`
- 在插件选项中选择echo取消设备作为输入设备

### 高通滤波器

应避免使用，因为模型使用了整个0-15khz范围

## 常见问题

尚未提供

## 支持

在github上创建一个问题

---

![插图](https://raw.githubusercontent.com/tphakala/birdnet-pi/main/doc/birdnet-pi-dashboard.webp)