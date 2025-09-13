## 警告：打开问题 : [🐛 Guacamole 插件 1.6.0-7 失败，显示错误网关；1.6.0-4 是可以工作的（于 2025-09-02 打开）](https://github.com/alexbelgium/hassio-addons/issues/2082) 由 [@730522js](https://github.com/730522js)
# Home assistant 插件：Guacamole

[![捐款][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐款][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fguacamole%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=入口&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fguacamole%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fguacamole%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建者](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建者)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有星标我的仓库的人！要星标它，请点击下面的图片，然后它会在右上角。谢谢！_

[![星标者的仓库列表 @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载量趋势](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/guacamole/stats.png)

## 关于

[Apache Guacamole](https://guacamole.apache.org/) 是一个无客户端的远程桌面网关，支持标准协议如 VNC、RDP 和 SSH。它提供了一个基于 Web 的界面，用于访问远程系统，而用户设备上无需安装任何客户端软件。Guacamole 作为代理，在基于 Web 的前端和实际远程桌面协议之间进行翻译。

此插件结合了 Guacamole 服务器（guacd）和 Web 应用组件，并集成了 PostgreSQL 数据库，用于存储连接配置和用户管理。该解决方案提供了一个完整的远程桌面网关，可以通过 Web 浏览器从任何地方安全地访问计算机和服务器。

此插件基于以下 Docker 镜像：https://github.com/abesnier/docker-guacamole

## 配置

Web 界面位于 `<你的 IP>:8080` 或通过入口在侧边栏中访问。

默认用户名为 `guacadmin`，密码为 `guacadmin`。强烈建议在首次登录后立即更改此密码。

### 选项

| 选项 | 类型 | 默认 | 描述 |
|------|------|------|------|
| `EXTENSIONS` | str | `auth-totp` | 启用 Guacamole 扩展（例如，`auth-totp`） |
| `TZ` | str | | 时区（例如，`Europe/London`） |

### 示例配置

```yaml
EXTENSIONS: "auth-totp"
TZ: "Europe/London"
```

### 数据库设置

插件自动配置 PostgreSQL 数据库，用于存储 Guacamole 配置、用户和连接。数据库文件存储在 `/config/postgres`，并在首次启动时自动创建。

### 自定义脚本和环境变量

此插件通过 `addon_config` 映射支持自定义脚本和环境变量：

- **自定义脚本**：参见 [在插件中运行自定义脚本](https://github.com/alexbelgium/hassio-addons/wiki/Running-custom-scripts-in-Addons)
- **环境变量**：参见 [为您的插件添加环境变量](https://github.com/alexbelgium/hassio-addons/wiki/Add-Environment-variables-to-your-Addon)

## 安装

此插件的安装非常简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件仓库][repository] 添加到您的 Hass.io 实例。
1. 安装此插件。
1. 点击 `保存` 按钮以保存您的配置。
1. 启动插件。
1. 检查插件的日志，查看是否一切正常。
1. 进入 Web 界面，使用默认凭据（`guacadmin`/`guacadmin`）登录。
1. 立即更改默认密码以增强安全性。
1. 通过 Guacamole Web 界面配置您的远程连接。

## 设置

安装并首次登录后：

1. **更改默认密码**：进入设置 → 用户 → guacadmin 并更改密码
2. **创建连接**：使用 Web 界面添加 RDP、VNC 或 SSH 连接到您的远程系统
3. **配置扩展**：如果使用 TOTP 身份验证，请在用户设置中配置它
4. **用户管理**：创建其他用户并根据需要分配连接权限

## 支持

在 [GitHub][repository] 上创建问题

[repository]: https://github.com/alexbelgium/hassio-addons