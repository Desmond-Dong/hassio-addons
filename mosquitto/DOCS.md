# Home Assistant 插件：Mosquitto 代理

## 安装

按照以下步骤在您的系统上安装插件：

1. 在 Home Assistant 前端导航到 **设置** -> **插件** -> **插件商店**。
2. 找到 "Mosquitto 代理" 插件并点击它。
3. 点击 "安装" 按钮。

## 使用方法

该插件有一些可用选项。要使插件运行：

1. 启动插件。
2. 请耐心等待几分钟。
3. 检查插件日志输出以查看结果。

通过 Home Assistant 的前端 **设置** -> **人员** -> **用户** 创建一个用于 MQTT 的新用户（即不在 Mosquitto 的 **配置** 选项卡中创建）。
注意：

1. 此名称不能是 `homeassistant` 或 `addons`，这些是保留的用户名。
2. 如果您看不到创建新用户的选项，请确保在您的 Home Assistant 配置中启用了 **高级模式**。

要使用 Mosquitto 作为代理，请转到集成页面并单击一次即可安装配置：

1. 在 Home Assistant 前端导航到 **设置** -> **设备与服务** -> **集成**。
2. MQTT 应该作为已发现的集成出现在页面的顶部
3. 选择它并如果需要，勾选启用 MQTT 发现的复选框，然后提交。

如果您有旧的 MQTT 设置可用，请删除此旧集成并重新启动 Home Assistant 以查看新集成。

## 配置

插件配置：

```yaml
logins: []
customize:
  active: false
  folder: mosquitto
certfile: fullchain.pem
keyfile: privkey.pem
require_certificate: false
```

### 选项：`logins`（可选）

一个本地用户列表，它们将被创建为用户名和密码。您不需要这样做，因为您也可以使用 Home Assistant 用户，而无需任何配置。如果特别希望使用本地用户：

```yaml
logins:
  - username: user
    password: passwd
```

您还可以使用从 `pw` 命令（Mosquitto 容器中存在）获得的哈希密码可选地设置 `password` 值。如果这样做，您必须在 `username` 和 `password` 值旁边指定 `password_pre_hashed: true`：

```console
$ pw -p "foo"
PBKDF2$sha512$100000$qsU7xQ8YCV/9nRuBBJVTxA==$jqw94Ej3aEr97UofY6rClmVCRkTdDiubQW0A6ZYmUI+pZjW9Hax+2w2FeYB3y5ut1SliB7+HAwIl2iONLKkohw==
```

```yaml
logins:
  - username: user
    password: "PBKDF2$sha512$100000$qsU7xQ8YCV/9nRuBBJVTxA==$jqw94Ej3aEr97UofY6rClmVCRkTdDiubQW0A6ZYmUI+pZjW9Hax+2w2FeYB3y5ut1SliB7+HAwIl2iONLKkohw=="
    password_pre_hashed: true
```

**注意**：此插件不支持匿名登录；所有连接都必须使用用户名/密码连接。`allow_anonymous true` 或任何匿名 ACL 都将无法与此插件一起工作。

#### 选项：`customize.active`

如果设置为 `true`，将读取额外的配置文件，请参阅下一个选项。

默认值：`false`

#### 选项：`customize.folder`

读取额外的配置文件（`*.conf`）的文件夹。

### 选项：`cafile`（可选）

包含根证书的文件。将此文件放置在 Home Assistant 的 `ssl` 文件夹中。

### 选项：`certfile`

包含证书及其链的文件。将此文件放置在 Home Assistant 的 `ssl` 文件夹中。

**关于 `certfile` 和 `keyfile` 的说明**  
- 如果不提供 `certfile` 和 `keyfile`
  - 在未加密端口（默认：`1883`，`1884` 用于 WebSocket）上可能存在未加密连接
- 如果提供 `certfile` 和 `keyfile`
  - 在未加密端口（默认：`1883`，`1884` 用于 WebSocket）上可能存在未加密连接
  - 在加密端口（默认：`8883`，`8884` 用于 WebSocket）上可能存在加密连接
     - 在这种情况下，客户端必须信任服务器的证书

### 选项：`keyfile`

包含私钥的文件。将此文件放置在 Home Assistant 的 `ssl` 文件夹中。

**关于 `certfile` 和 `keyfile` 的说明**  
- 如果不提供 `certfile` 和 `keyfile`
  - 在未加密端口（默认：`1883`，`1884` 用于 WebSocket）上可能存在未加密连接
- 如果提供 `certfile` 和 `keyfile`
  - 在未加密端口（默认：`1883`，`1884` 用于 WebSocket）上可能存在未加密连接
  - 在加密端口（默认：`8883`，`8884` 用于 WebSocket）上可能存在加密连接
     - 在这种情况下，客户端必须信任服务器的证书

### 选项：`require_certificate`

如果设置为 `false`：
- 客户端**不需要**提供证书来连接，用户名/密码就足够了
- `cafile` 选项被忽略

如果设置为 `true`：
- 客户端**需要**提供自己的证书来连接，用户名/密码**不足以**连接
- 必须提供证书机构（CA）：`cafile` 选项
- 客户端证书必须由提供的 CA（`cafile`）签名

### 选项：`debug`

如果设置为 `true`，将启用 mosquitto 及其认证插件的调试日志记录。这有助于追踪问题，但长期运行此选项不推荐，因为敏感信息将被记录。

## Home Assistant 用户管理

此插件附加到 Home Assistant 用户系统，因此 MQTT 客户端可以使用这些凭证。本地用户也可以在插件的配置选项中独立设置。对于 Home Assistant 内部生态系统，我们注册了 `homeassistant` 和 `addons`，因此这些可能不能用作用户名。

## 禁用不安全端口（1883/1884）上的监听

从插件页面的网络卡片中删除端口（将它们设置为空白）以禁用它们。

### 访问控制列表（ACLs）

可以基于登录到 Mosquitto 的用户来限制对主题的访问。在这种情况下，建议为每个客户端创建单独的用户并创建适当的 ACL。

有关更多信息，请参阅以下链接：

- [Mosquitto 主题限制](http://www.steves-internet-guide.com/topic-restriction-mosquitto-configuration/)
- [Mosquitto.conf 手册页](https://mosquitto.org/man/mosquitto-conf-5.html)

添加以下配置以启用对所有主题的**无限制**访问 `[YOUR_MQTT_USER]`。

**注意**：Home Assistant 期望 `homeassistant` 和 `addons` 用户对所有主题具有无限制的读写访问权限。如果您选择启用 ACL，您应像下面演示的那样授予这些用户此访问权限。否则您将遇到问题。

1. 启用自定义标志

    ```yaml
      customize:
        active: true
        folder: mosquitto
    ```

2. 创建 `/share/mosquitto/acl.conf` 并包含以下内容：

    ```text
    acl_file /share/mosquitto/accesscontrollist
    ```

3. 创建 `/share/mosquitto/accesscontrollist` 并包含以下内容：

    ```text
    user addons
    topic readwrite #
    
    user homeassistant
    topic readwrite #
    
    user [YOUR_MQTT_USER]
    topic readwrite #
    ```

`/share` 文件夹可以通过 SMB 访问，或在主机文件系统下的 `/usr/share/hassio/share` 中访问。

## 支持

有问题吗？

您有几个选项来获得答案：

- [Home Assistant Discord 聊天服务器][discord]
- Home Assistant [社区论坛][forum]
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

如果您发现了一个错误，请在我们的 GitHub 上[打开一个问题][issue]。

[discord]: https://discord.gg/c5DvZ4e
[forum]: https://community.home-assistant.io
[issue]: https://github.com/home-assistant/addons/issues
[reddit]: https://reddit.com/r/homeassistant
[repository]: https://github.com/hassio-addons/repository
[mosquitto]: https://mosquitto.org/