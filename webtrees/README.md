# Home assistant add-on: Webtrees

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fwebtrees%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=入口&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fwebtrees%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fwebtrees%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库点赞的人！要点赞，请点击下面的图片，它将在右上角显示。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![downloads evolution](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/webtrees/stats.png)

## 关于

[webtrees](http://www.webtrees.net) 是网络领先的在线协作家谱应用程序。

这个插件基于以下 Docker 镜像：https://github.com/NathanVaughn/webtrees-docker

## 配置

Web UI 可以在 <http://homeassistant:PORT> 找到。

名称和密码通过启动向导定义。

选项可以通过两种方式配置：

- 插件选项

```yaml
LANG: "en-US" # webtrees 的默认语言
BASE_URL: "http://192.168.178.69" # 你访问 webtrees 的 URL
DB_TYPE: "sqlite" # 你的数据库类型：sqlite 用于自动配置，或外部用于手动配置
CONFIG_LOCATION: config.yaml 的位置（见下文）
localdisks: sda1 # 将你的驱动硬件名称输入到其中，用逗号分隔，或其标签。例如。 sda1, sdb1, MYNAS...
networkdisks: "//SERVER/SHARE" # 可选，要挂载的 SMB 服务器的列表，用逗号分隔
cifsusername: "username" # 可选，SMB 用户名，所有 SMB 共享相同
cifspassword: "password" # 可选，SMB 密码
trusted_headers: 单个地址，或 CIDR 格式的地址范围
base_url_portless: 无端口的基 URL
```

- config.yaml

可以给 config.yaml 文件添加自定义环境变量。包含此文件的文件夹不是 root/config 目录的一部分（HA 的 configuration.yaml 在此目录中），而是 /root/addon_configs（[HA 文档](https://developers.home-assistant.io/blog/2023/11/06/public-addon-config/)）。完整的环境变量可以在以下位置找到：https://github.com/linuxserver/docker-paperless-ng。它必须在启动插件时以有效的 YAML 格式输入。

## 安装

这个插件的安装非常简单，与安装任何其他插件没有区别。

1. 将我的插件仓库添加到你的 home assistant 实例中（在右上角的 supervisor 插件商店中，或点击下面的按钮如果你已经配置了我的 HA）
   [![打开你的 Home Assistant 实例并显示添加插件仓库对话框，其中包含特定的仓库 URL 预填。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装这个插件。
1. 点击 `保存` 按钮以保存你的配置。
1. 设置插件选项以符合你的偏好。
1. 启动插件。
1. 检查插件的日志以查看一切是否正常。
1. 打开 Web UI 并调整软件选项

## 远程访问

可以免费暴露这个插件以供外部访问（给家人和朋友）。
这可以做到，而不会将你的网络暴露给外部。
解决这个问题的一种方案是 [Cloudflare 隧道](https://github.com/brenner-tobias/addon-cloudflared)。论坛和 YouTube 上有很多关于如何做这个的材料，以及如何使用额外的规则和 Google 邮件验证来保护它。
以下是配置集成的注意事项：

Webtrees 配置

```yaml
BASE_URL: httpS://your_tunnel_domain_name.example.com
# 这是你要访问页面的外部 URL。
# 尽管插件的默认配置不使用 SSL，但在使用 Cloudflare 时，base_url 必须是 https
# 这是因为当隧道运行时，Cloudflare 会将其自己的 SSL 应用于连接。
# 如果 base_url 是 http://，这会导致不匹配，并且某些块将无法正确加载
ssl: false #禁用，Cloudflare 负责处理这个问题
base_url_portless: true #必须启用

#其余是标准的
DATA_LOCATION: /config/data
certfile: fullchain.pem
keyfile: privkey.pem
```

Cloudflared 配置

```yaml
external_hostname: "" #无，以保持 HA 仅通过 Nabu Casa 可访问，但也可以用于同时做这两件事
additional_hosts:
  - hostname: your_tunnel_domain_name.example.com #注意这与 webtrees 配置中的相同
    service: http://your_HA_IP:9999 #注意这里它是 http 并带端口，尽管 webtrees 配置为无端口
tunnel_name: Your_tunnel_name
```

## 支持

在 github 上创建问题

## 插图

![illustration](https://installatron.infomaniak.com/installatron//images/ss2_webtrees.jpg)