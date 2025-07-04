## 警告：仅支持armv7版本至0.4.3！后续版本将不再更新

_感谢所有星标我的仓库的人！要星标它，请点击下面的图片，然后它将在右上角。谢谢！_

[![Starazers仓库之星](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载趋势](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/mealie/stats.png)

## 关于

Mealie是一个自托管食谱管理和饮食计划工具，具有RestAPI后端和基于Vue的响应式前端应用程序，为全家人提供愉悦的用户体验。

这个mealie 1.0的插件基于[hendrix04的组合docker镜像](https://hub.docker.com/r/hendrix04/mealie-combined)。

这个插件基于[hay-kot的docker镜像](https://hub.docker.com/r/hkotel/mealie)。

## 配置

- 启动插件。稍等片刻，检查日志中是否有任何错误。
- 打开yourdomain.com:9090（其中":9090"是插件中配置的端口）。
- 默认
  - 用户名：changeme@example.com
  - 密码：MyPassword

选项可以通过两种方式配置：

- 插件选项

```yaml
    "BASE_URL": 可选，外部基本URL
    "PGID": 用户ID
    "PUID": "组ID
    "certfile": fullchain.pem #ssl证书，必须位于/ssl
    "keyfile": privkey.pem #sslkeyfile，必须位于/ssl
    "ssl": ssl: true/false
    "ALLOW_SIGNUP": 允许用户注册
```

- config.yaml
  可以使用在/homeassistant/addons_config/xxx-mealie/config.yaml中找到的config.yaml文件配置其他选项

完整的选项列表可以在以下位置查看：https://nightly.mealie.io/documentation/getting-started/installation/backend-config/

## 与HA集成

### 详细信息（感谢@michelangelonz）

创建一个RESTful传感器

```yaml
sensor:
  - platform: rest
    resource: "http://###.###.#.#:9090/api/groups/mealplans/today"
    method: GET
    name: Mealie今天的餐食
    headers:
      Authorization: Bearer <在这里放置授权信息>
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

添加一个通用相机以获取图像
http://###.###.#.#:9090/api/media/recipes/{{ state_attr('sensor.mealie_todays_meal', 'id') }}/images/min-original.webp

### 全局信息

阅读这里：https://hay-kot.github.io/mealie/documentation/community-guide/home-assistant/

## 安装

这个插件的安装非常简单，与其他任何Hass.io插件的安装方式相同。

1. [将我的Hass.io插件仓库][repository]添加到您的Hass.io实例。
1. 安装此插件。
1. 点击“保存”按钮以保存您的配置。
1. 启动插件。
1. 检查插件的日志，看看是否一切顺利。
1. 仔细配置插件以符合您的喜好，请参考官方文档进行配置。

## 支持

如果您在安装过程中遇到问题，请务必查看github。

[repository]: https://github.com/alexbelgium/hassio-addons