## 警告：仅支持 armv7 版本至 0.4.3！后续版本将不再更新！

_感谢所有给我的仓库点赞的人！点击下面的图片点赞，它将在右上角显示。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载趋势](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/mealie/stats.png)

## 关于

Mealie 是一个自托管食谱管理器和餐计划应用，具有 REST API 后端和基于 Vue 的响应式前端应用，为全家人提供愉悦的用户体验。

这个为 Mealie 1.0 构建的插件基于 hendrix04 的 [Docker 镜像](https://hub.docker.com/r/hendrix04/mealie-combined)。
这个插件基于 hay-kot 的 [Docker 镜像](https://hub.docker.com/r/hkotel/mealie)。

## 配置

Web UI 可以在 <http://homeassistant:PORT> 或通过 Ingress 侧边栏访问。
配置可以通过应用 Web UI 进行，除了以下选项。

- 启动插件。稍等片刻并检查日志以查找任何错误。
- 默认凭证：
  - 用户名：changeme@example.com
  - 密码：MyPassword

### 选项

| 选项 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `PGID` | 整数 | `1000` | 文件权限的组 ID |
| `PUID` | 整数 | `1000` | 文件权限的用户 ID |
| `ssl` | 布尔值 | `false` | 为 Web 界面启用 HTTPS |
| `certfile` | 字符串 | `fullchain.pem` | SSL 证书文件（必须位于 /ssl） |
| `keyfile` | 字符串 | `privkey.pem` | SSL 密钥文件（必须位于 /ssl） |
| `BASE_URL` | 字符串 | | 可选的外部基本 URL |
| `DATA_DIR` | 字符串 | `/config` | 数据目录路径 |
| `ALLOW_SIGNUP` | 布尔值 | `true` | 允许新用户注册 |

### 示例配置

```yaml
PGID: 1000
PUID: 1000
ssl: false
certfile: "fullchain.pem"
keyfile: "privkey.pem"
BASE_URL: "https://mealie.mydomain.com"
DATA_DIR: "/config"
ALLOW_SIGNUP: false
```

### 自定义脚本和环境变量

此插件通过 `addon_config` 映射支持自定义脚本和环境变量：

- **自定义脚本**：参见 [在插件中运行自定义脚本](https://github.com/alexbelgium/hassio-addons/wiki/Running-custom-scripts-in-Addons)
- **环境变量**：参见 [为你的插件添加环境变量](https://github.com/alexbelgium/hassio-addons/wiki/Add-Environment-variables-to-your-Addon)

你可以通过创建 `/homeassistant/addons_config/xxx-mealie/config.yaml` 来添加环境变量。

完整的选项列表可以在以下链接找到：https://nightly.mealie.io/documentation/getting-started/installation/backend-config/

## 与 HA 集成

### 详细信息（感谢 @michelangelonz）

创建一个 RESTful 传感器

```yaml
sensor:
  - platform: rest
    resource: "http://###.###.#.#:9090/api/groups/mealplans/today"
    method: GET
    name: Mealie todays meal
    headers:
      Authorization: Bearer <在此处插入 auth>
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

添加一个通用摄像头以获取图像
http://###.###.#.#:9090/api/media/recipes/{{ state_attr('sensor.mealie_todays_meal', 'id') }}/images/min-original.webp

### 全局信息

在此处阅读：https://hay-kot.github.io/mealie/documentation/community-guide/home-assistant/

## 安装

此插件的安装非常简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件仓库][repository] 添加到你的 Hass.io 实例。
1. 安装此插件。
1. 点击 `保存` 按钮以保存你的配置。
1. 启动插件。
1. 检查插件的日志以查看是否一切顺利。
1. 仔细配置插件以满足你的偏好，请参阅官方文档进行配置。

## 支持

如果你在安装过程中遇到问题，请务必查看 GitHub。

[repository]: https://github.com/alexbelgium/hassio-addons