# 家居助手插件：皇家价格检查

## 描述
如果皇家加勒比游轮附加项降价，则通知。可以重新定价游轮，只是饮料套餐、互联网、观光等

_感谢大家给我的仓库点赞！要点赞，请点击下面的图片，它将出现在右上角。谢谢！_

[![@jdeath/homeassistant-addons仓库的星标者名单](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)


## 安装

这个插件的安装非常直接，与安装任何其他Hass.io插件没有区别。

1. [将我的Hass.io插件仓库][repository]添加到您的Hass.io实例中。
1. 安装这个插件。
1. 点击`保存`按钮来保存您的配置。
1. 启动插件。它将会失败，这是正常的
1. 前往 /addon-configs/2effc9b9_royalpricecheck
1. 编辑 `/addon-configs/2effc9b9_royalpricecheck/config.yaml`（见下文）
1. 再次运行插件并检查日志
1. 确认工作正常后，使用自动化脚本每天运行一次

## config.yaml
参见 `https://github.com/jdeath/CheckRoyalCaribbeanPrice`

## 自动运行
1. 创建一个自动化脚本每天运行这个插件（在随机时间）

```
alias: 启动皇家价格检查
description: ""
trigger:
  - platform: time
    at: "06:00:00"
condition: []
action:
  - delay: "{{ (range(0, 1)|random|int) }}:{{ (range(1, 59)|random|int) }}:00"
  - service: hassio.addon_start
    data:
      addon: 2effc9b9_royalpricecheck
mode: single
```

# 发送通知。
1. 编辑 `/addon-configs/2effc9b9_royalpricecheck/config.yaml`
1. 配置通知的行

它应该看起来像这样，用于家宅助手通知：
```
# config.yaml
apprise:
  urls:
    - 'hassio://192.168.X.XX/eyXXXXXXXXXXXXXXXX.eyXXXXXXXXXXXXXXXXXxx'
```
其中 `eyXXX.eyXXX` 字符串是家宅助手长生存期令牌。长生存期访问令牌可以在家宅助手用户配置文件的底部“长生存期访问令牌”部分创建。

更多详情：`https://github.com/caronc/apprise/wiki/Notify_homeassistant`

更多详情：`https://github.com/caronc/apprise` 您可以包括多条URL行来发送电子邮件等

# 添加到侧边栏
由于没有WebUI，它不能显示在侧边栏中。但是您可以将以下代码添加到您的家宅助手 `configuration.yaml` 中，通过侧边栏条目显示日志

```
panel_custom:
  - name: panel_rewards
    sidebar_title: Rewards
    sidebar_icon: mdi:medal
    url_path: 'hassio/addon/2effc9b9_royalpricecheck/logs'
    module_url: /api/hassio/app/entrypoint.js
    embed_iframe: true
    require_admin: true
```

# 问题


[repository]: https://github.com/jdeath/homeassistant-addons