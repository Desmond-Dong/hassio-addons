## ⚠️ Open Request : [✨ [REQUEST] Mealie - add OpenAI support (opened 2025-03-05)](https://github.com/alexbelgium/hassio-addons/issues/1802) by [@tillmannschatz](https://github.com/tillmannschatz)
## ⚠️ Open Issue : [🐛 [Mealie] Quotes in Env Variables are swallowed (opened 2025-07-02)](https://github.com/alexbelgium/hassio-addons/issues/1933) by [@eMerzh](https://github.com/eMerzh)
# Hass.io Add-ons: Mealie

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fmealie%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fmealie%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fmealie%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=代码检查)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

警告 : armv7 仅支持到版本 0.4.3！它不会与后续版本更新

_感谢所有给我的仓库点赞的人！要点赞，请点击下面的图片，然后它将在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载量趋势](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/mealie/stats.png)

## 关于

Mealie 是一个自托管的食谱管理和饮食计划工具，具有 REST API 后端和基于 Vue 的响应式前端应用程序，为整个家庭提供愉悦的用户体验。
这个用于 Mealie 1.0 的插件基于 hendrix04 的 [Docker 镜像](https://hub.docker.com/r/hendrix04/mealie-combined)。
这个插件基于 hay-kot 的 [Docker 镜像](https://hub.docker.com/r/hkotel/mealie)。

## 配置

- 启动插件。等待一段时间并检查日志中的任何错误。
- 打开你的域名.com:9090（其中 ":9090" 是插件中配置的端口）。
- 默认
  - 用户名: changeme@example.com
  - 密码: MyPassword

选项可以通过两种方式配置：

- 插件选项

```yaml
    "BASE_URL": 可选，外部基本 URL
    "PGID": 用户 ID
    "PUID": "组 ID
    "certfile": fullchain.pem #ssl 证书，必须位于 /ssl
    "keyfile": privkey.pem #sslkeyfile，必须位于 /ssl
    "ssl": ssl: true/false
    "ALLOW_SIGNUP": 允许用户注册
```

- Config.yaml
  可以使用在 /homeassistant/addons_config/xxx-mealie/config.yaml 中找到的 config.yaml 文件配置其他选项

完整的选项列表可以在以下链接中查看：https://nightly.mealie.io/documentation/getting-started/installation/backend-config/

## 与 HA 集成

### 详细信息（感谢 @michelangelonz）

创建一个 RESTful 传感器

```yaml
sensor:
  - platform: rest
    resource: "http://###.###.#.#:9090/api/groups/mealplans/today"
    method: GET
    name: Mealie 今天的餐食
    headers:
      Authorization: Bearer <在这里放入认证信息>
    value_template: "{{ value_json.value }}"
    json_attributes_path: $..recipe
    json_attributes:
      - name
      - id
      - totalTime
      - prepTime
      - performTime
      - description
      - slug
```

从属性创建模板传感器

```yaml
- name: TodaysDinner
  unique_id: sensor.TodaysDinner
  state: "{{ state_attr('sensor.mealie_todays_meal', 'name') }}"
- name: TodaysDinnerDescription
  unique_id: sensor.DinnerDescription
  state: "{{ state_attr('sensor.mealie_todays_meal', 'description') }}"
- name: TodaysDinnerSlug
  unique_id: sensor.DinnerSlug
  state: "{{ state_attr('sensor.mealie_todays_meal', 'slug') }}"
- name: TodaysDinnerID
  unique_id: sensor.DinnerID
  state: "{{ state_attr('sensor.mealie_todays_meal', 'id') }}"
```

添加一个通用相机用于图像
http://###.###.#.#:9090/api/media/recipes/{{ state_attr('sensor.mealie_todays_meal', 'id') }}/images/min-original.webp

### 全局信息

阅读这里：https://hay-kot.github.io/mealie/documentation/community-guide/home-assistant/

## 安装

这个插件的安装非常简单，与其他 Hass.io 插件的安装方式相同。

1. [添加我的 Hass.io 插件仓库][repository] 到你的 Hass.io 实例。
1. 安装这个插件。
1. 点击 `保存` 按钮以保存你的配置。
1. 启动插件。
1. 检查插件的日志以查看一切是否正常。
1. 仔细配置插件以符合你的偏好，查看官方文档以了解详细信息。

## 支持

如果你在你的安装中遇到问题，请确保查看 github。

[repository]: https://github.com/alexbelgium/hassio-addons