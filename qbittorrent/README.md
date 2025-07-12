# Home assistant add-on: qbittorrent

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fqbittorrent%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fqbittorrent%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fqbittorrent%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库点赞的人！要点赞，请点击下面的图片，然后它会在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载量增长](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/qbittorrent/stats.png)

## 关于

---

[Qbittorrent](https://github.com/qbittorrent/qBittorrent) 是一个跨平台的免费和开源的 BitTorrent 客户端。
这个插件基于 [linuxserver.io](https://www.linuxserver.io/) 的 docker 镜像。

这个插件有几个可配置的选项：

- 允许挂载本地外部驱动器，或从插件中挂载 SMB 共享
- [替代 WebUI](https://github.com/qbittorrent/qBittorrent/wiki/List-of-known-alternate-WebUIs)
- 使用 SSL
- Ingress
- 可选的 OpenVPN 支持
- 允许设置特定的 DNS 服务器

## 配置

---

Webui 可以在 <http://homeassistant:8080> 找到，或在 Ingress 侧边栏中使用。
默认的用户名/密码：在启动日志中描述。
配置可以通过插件 WebUI 进行，以下选项除外

网络磁盘挂载到 /mnt/share 名称

如果您想要最佳速度和连接性，您需要在路由器上映射暴露的端口。

```yaml
PGID: user
GPID: user
ssl: true/false
certfile: fullchain.pem #ssl 证书，必须位于 /ssl
keyfile: privkey.pem #sslkeyfile，必须位于 /ssl
whitelist: "localhost,192.168.0.0/16" # 输入 `null` 以禁用。列出不需要密码的 IP 子网（可选）
customUI: 从列表中选择 # 可以在这里设置替代 WebUI。每个插件启动时设置最新版本。选择 'custom' 以在 Webui 中自行填写
DNS_servers: 8.8.8.8,1.1.1.1 # 保持空白以使用路由器的 DNS，或设置自定义 DNS 以避免在本地 DNS 广告拦截器的情况下进行垃圾邮件
SavePath: "/share/qbittorrent" # 定义下载目录
localdisks: sda1 # 将您的驱动器的硬件名称添加到逗号分隔的列表中，或其标签。例如。sda1, sdb1, MYNAS...
networkdisks: "//SERVER/SHARE" # 可选，列出要挂载的 SMB 服务器，用逗号分隔
cifsusername: "username" # 可选，SMB 用户名，所有 SMB 共享相同
cifspassword: "password" # 可选，SMB 密码
cifsdomain: "domain" # 可选，允许设置 SMB 共享的域
openvpn_enabled: true/false # 是否需要 OpenVPN 启动 qBittorrent
openvpn_config": 例如 "config.ovpn" # 位于 /config/openvpn 中的文件名。如果为空，将使用随机文件
openvpn_username": USERNAME
openvpn_password: YOURPASSWORD
openvpn_alt_mode: 在容器级别而不是应用程序级别绑定
run_duration: 12h # 插件应运行多长时间。必须按数字 + 时间单位格式化（例如：5s，或 2m，或 12h，或 5d...)
silent: true # 抑制调试消息
```

## 安装

---

这个插件的安装非常简单，与安装任何其他插件没有区别。

1. 将我的插件仓库添加到您的 home assistant 实例（在 supervisor 插件商店右上角，或如果您已配置我的 HA，请点击下面的按钮）
   [![打开您的 Home Assistant 实例并显示带有预填充特定仓库 URL 的添加插件仓库对话框。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装这个插件。
1. 点击 `保存` 按钮以保存您的配置。
1. 设置插件的选项以符合您的偏好
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 打开 WebUI 并调整软件选项

## 与 HA 集成

使用 [qBittorrent 集成](https://www.home-assistant.io/integrations/qbittorrent/)

您可以使用以下代码片段来检查和设置替代速度（上述 HA 集成不需要）

```bash
shell_command:
  toggle_torrent_speed: curl -X POST https://<YOUR HA IP>:8081/api/v2/transfer/toggleSpeedLimitsMode -k
sensor:
  - platform: command_line
    name: get_torrent_speed
    command: curl https://<YOUR HA IP>:8081/api/v2/transfer/speedLimitsMode -k
```

如果您不使用 SSL 选项，可以跳过 -k 参数，并在 URL 中使用 http 而不是 https

这些行将暴露一个 `sensor.get_torrent_speed`，每 60 秒更新一次，如果替代速度模式已启用则返回 1，否则返回 0，以及一个 `shell_command.toggle_torrent_speed`，您可以在自动化中作为服务调用

## 常见问题

<details>
  <summary>### ipv6 问题与 OpenVPN (@happycoo)</summary>
添加以下代码到您的 .ovpn 配置

```bash
# 不要通过 VPN 路由 lan
route 192.168.1.0 255.255.255.0 net_gateway

# 停用 ipv6
pull-filter ignore "dhcp-option DNS6"
pull-filter ignore "tun-ipv6"
pull-filter ignore "ifconfig-ipv6"
```

</details>

<details>
  <summary>### 100% cpu</summary>
删除您的 nova3 文件夹在 /config 中并重启 qBittorrent

</details>

<details>
  <summary>### 监控文件夹 (@FaliseDotCom)</summary>

- 进入 config\addons_config\qBittorrent
- 找到（或创建）文件 watched_folders.json
- 粘贴或调整到以下内容：

```json
{
  "folder/to/watch": {
    "add_torrent_params": {
      "category": "",
      "content_layout": "Original",
      "download_limit": -1,
      "download_path": "[folder/for/INCOMPLETE_downloads]",
      "operating_mode": "AutoManaged",
      "ratio_limit": -2,
      "save_path": "[folder/for/COMPLETED_downloads]",
      "seeding_time_limit": -2,
      "skip_checking": false,
      "stopped": false,
      "tags": [],
      "upload_limit": -1,
      "use_auto_tmm": false,
      "use_download_path": true
    },
    "recursive": false
  }
}
```

</details>

<details>
  <summary>### nginx 错误代码 (@Nanianmichaels)</summary>

> [cont-init.d] 30-nginx.sh: 执行中...
> [cont-init.d] 30-nginx.sh: 退出 1。

等待几分钟并重启插件，这可能是因为 github 的暂时不可用

### 使用无效参数的本地挂载 (@antonio1475)

> [cont-init.d] 00-local_mounts.sh: 执行中...
> 本地磁盘挂载...
> mount: 挂载 /dev/sda1 到 /mnt/sda1 失败：无效参数
> [19:19:44] FATAL: 无法挂载本地驱动器！请检查名称。
> [cont-init.d] 00-local_mounts.sh: 退出 0。

尝试通过在 "localdisks" 选项中放置分区标签而不是硬件名称来挂载

</details>

<details>
  <summary>### 使用 OpenVPN 后几天内元数据获取丢失 (@almico)</summary>

在 config.ovpn 中添加 `ping-restart 60`

</details>

<details>
  <summary>### 在小规模窗口中下载信息为空 (@aviadlevy)</summary>

当我的窗口宽度小于 960 像素时，我的下载为空。
解决方案是重置 Vuetorrent 设置。

</details>

## 支持

在 github 上创建问题，或在 [home assistant 论坛](https://community.home-assistant.io/t/home-assistant-addon-qbittorrent/279247) 上提问

---

![插图](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/qbittorrent/illustration.png)