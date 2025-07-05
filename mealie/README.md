## ⚠️ Open Request : [✨ [REQUEST] Mealie - 添加 OpenAI 支持 (已打开 2025-03-05)](https://github.com/alexbelgium/hassio-addons/issues/1802) by [@tillmannschatz](https://github.com/tillmannschatz)
## ⚠️ Open Issue : [🐛 [Mealie] 环境变量中的引号被吞没 (已打开 2025-07-02)](https://github.com/alexbelgium/hassio-addons/issues/1933) by [@eMerzh](https://github.com/eMerzh)
# Hass.io 插件：Mealie

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fmealie%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=入口&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fmealie%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fmealie%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建器)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

警告：仅支持 armv7 版本至 0.4.3！后续版本将不再更新

_感谢所有星标我的仓库！要星标它，请点击下面的图片，然后它将在右上角。谢谢！_

[![星标者仓库轮班表 @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载量趋势](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/mealie/stats.png)

## 关于

Mealie 是一个自托管的食谱管理和饮食计划工具，具有 RestAPI 后端和基于 Vue 的响应式前端应用程序，为全家人提供愉悦的用户体验。
这个 Mealie 1.0 的插件基于 hendrix04 的 [合并 Docker 镜像](https://hub.docker.com/r/hendrix04/mealie-combined)。
这个插件基于 hay-kot 的 [Docker 镜像](https://hub.docker.com/r/hkotel/mealie)。

## 配置

- 启动插件。等待一段时间，并检查日志中的任何错误。
- 打开你的域名.com:9090（其中 ":9090" 是插件中配置的端口）。
- 默认
  - 用户名：changeme@example.com
  - 密码：MyPassword

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

- config.yaml
  可以使用在 /homeassistant/addons_config/xxx-mealie/config.yaml 中找到的 config.yaml 文件配置其他选项

完整选项列表可以在以下链接查看：https://nightly.mealie.io/documentation/getting-started/installation/backend-config/

## 与 Home Assistant 集成

### 详细信息（感谢 @michelangelonz）

创建一个 RESTful 传感器

```yaml
sensor:
  - platform: rest
    resource: "http://###.###.#.#:9090/api/groups/mealplans/today"
    method: GET
    name: Mealie 今天的主食
    headers:
      Authorization: Bearer <在这里放置认证信息>
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

添加一个通用摄像头用于图像
http://###.###.#.#:9090/api/media/recipes/{{ state_attr('sensor.mealie_todays_meal', 'id') }}/images/min-original.webp

### 全局信息

在此处阅读：https://hay-kot.github.io/mealie/documentation/community-guide/home-assistant/

## 安装

这个插件的安装非常简单，与其他 Hass.io 插件安装没有区别。

1. [添加我的 Hass.io 插件仓库][repository] 到你的 Hass.io 实例。
1. 安装这个插件。
1. 点击 `保存` 按钮保存你的配置。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 仔细配置插件以符合你的偏好，参考官方文档进行配置。

## 支持

如果你在安装中遇到问题，请确保检查 GitHub。

[repository]: https://github.com/alexbelgium/hassio-addons