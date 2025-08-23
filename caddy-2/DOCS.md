# Home Assistant 拓展程序：Caddy 2

Caddy 2 是一个现代、强大、企业级的开源 Web 服务器，旨在提供简单性、安全性和灵活性。
它独特的优势在于能够默认自动管理 HTTPS，而无需复杂的配置。

## 目录

1. [拓展程序安装](#拓展程序安装)
2. [基本设置示例](#基本设置示例)
3. [配置选项](#配置选项)
4. [高级用法：自定义二进制文件和插件](#高级用法自定义二进制文件--插件)

## 拓展程序安装

要安装 Caddy 2 拓展程序，首先将仓库添加到您的 [Hass.io](https://home-assistant.io/hassio/) 实例中，输入以下 URL：

`https://github.com/einschmidt/hassio-addons`

如果您遇到任何问题，请参考 [官方文档](https://home-assistant.io/hassio/installing_third_party_addons/) 获取指导。

添加仓库后，搜索并安装 "Caddy 2" 拓展程序。

## 基本设置示例

Caddy 2 拓展程序提供多种设置方法，以适应不同的环境和网络配置。这些设置范围从简单到更复杂，允许您根据需要选择合适的自定义级别。

### 默认代理服务器设置（简单）

默认情况下，Caddy 2 作为 Home Assistant 的代理服务器运行，无需 `Caddyfile`。它使用添加程序设置中提供的配置，并自动处理 HTTPS。

**注意**：如果配置目录中找到 `Caddyfile`，则会忽略 `non_caddyfile_config` 设置，以优先使用 Caddyfile。

#### 示例配置

**重要**：_更改配置后，请始终重新启动添加程序。_

要进行基本的代理设置，将 `yourdomain.com` 转发到 Home Assistant，使用以下示例（无需 `Caddyfile`）：

```yaml
non_caddyfile_config:
  email: your@email.com
  domain: yourdomain.com
  destination: localhost
  port: 8123
log_level: info
args: []
env_vars: []
```

**注意**：_这些示例仅供参考。根据您的需求进行自定义。_

### Caddyfile 设置（中级）

对于更高级的自定义，您可以创建并使用 Caddyfile 来定义您的代理服务器的配置。这允许您对路由、标头和 SSL 管理等设置进行更精细的控制。

要使用 Caddyfile，请将其放置在添加程序的配置目录中。您可以使用 [SSH][ssh] 或 [Samba][samba] 添加程序访问此目录。添加程序将仅在特定位置搜索 Caddyfile。

#### 添加程序配置目录

Caddyfile 需要放置在添加程序的配置目录中，该目录位于：

```
/addon_configs/c80c7555_caddy-2
```

##### 访问配置目录

SSH：您可以通过 SSH 访问配置目录，方法是导航到 `/addon_configs/`。

Samba：或者，使用 Samba 添加程序，您可以从网络将此文件夹作为共享目录访问。查找 `addon_configs` 文件夹并找到相应的目录。

#### 管理证书

Caddy 2 可以自动生成 SSL 证书。如果您想使用来自其他添加程序（如 Let’s Encrypt 添加程序）的证书，可以将它们放置在 `/ssl` 目录中。Caddy 2 添加程序将可以访问此文件夹，允许您使用外部证书或为其他服务创建证书。

#### 示例 Caddyfile

一个简单的 Caddyfile，用于将流量转发到 Home Assistant 安装可能如下所示：

```
{
  email your@email.com
}

yourdomain.com {
  reverse_proxy localhost:8123
}
```

对于更高级的配置，请参阅 [Caddyfile 文档](https://caddyserver.com/docs/caddyfile)。

#### Caddyfile 的示例配置

**重要**：_更改配置后，请重新启动添加程序。_

要指示添加程序使用并监视 `Caddyfile`，您的配置应如下所示：

```yaml
non_caddyfile_config: {}
log_level: info
args:
  - "--watch"
env_vars: []
```

**注意**：_根据您的特定设置自定义此示例。_

### 自定义 Caddy 二进制文件设置（高级）

对于高级用户，您可以用自定义的二进制文件替换默认的 Caddy 二进制文件。使用 [SSH][ssh] 或 [Samba][samba] 将您的 `caddy` 二进制文件放置在 [添加程序配置目录](#添加程序配置目录)，添加程序将使用此文件夹中的二进制文件。

#### 示例配置

**重要**：_更改任何配置后，请重新启动添加程序。_

以下是一个使用自定义 Caddy 二进制文件和 `Caddyfile` 的示例配置，并启用了自动更新和格式化：

```yaml
non_caddyfile_config: {}
log_level: info
args:
  - "--watch"
env_vars: []
caddy_upgrade: true
caddy_fmt: true
```

**注意**：_这些示例仅供参考。根据您的设置进行调整。_

## 配置选项

### 选项：`non_caddyfile_config.email`

定义在您的证书颁发机构（CA）创建 ACME 账户时使用的电子邮件地址。建议这样可以帮助在出现问题时管理证书。

**注意**：此选项仅用于默认反向代理设置。如果配置目录中找到 `Caddyfile`，则将被忽略。

### 选项：`non_caddyfile_config.domain`

指定您的设置的域名。

**注意**：此选项仅适用于默认反向代理设置，如果配置目录中存在 `Caddyfile`，则将被忽略。

### 选项：`non_caddyfile_config.destination`

设置反向代理的上游地址。通常，`localhost` 对大多数设置都足够。要针对特定地址，您可以使用 `127.0.0.1`（IPv4）或 `::1`（IPv6）。

**注意**：此选项仅用于默认反向代理设置，如果配置目录中找到 `Caddyfile`，则将被忽略。

### 选项：`non_caddyfile_config.port`

定义上游地址的端口。例如，Home Assistant 通常使用端口 `8123`。

**注意**：此设置仅应用于默认反向代理配置。如果配置目录中存在 `Caddyfile`，则将被忽略。

### 选项：`caddy_upgrade`

启用自定义 Caddy 二进制文件及其插件的自动升级。将此选项设置为 `true` 以允许更新，或设置为 `false` 以禁用更新。默认值为 `false`。

**注意**：此功能仅适用于自定义二进制文件（Caddy 版本 2.4 或更高），如果使用默认 Caddy 二进制文件，则不需要此功能。

### 选项：`caddy_fmt`

启用 `Caddyfile` 的自动格式化和美化。将此选项设置为 `true` 以启用格式化，或设置为 `false` 以禁用格式化。默认情况下，它被禁用。

**注意**：此功能需要有效的 `Caddyfile` 才能工作。

### 选项：`args`

允许您为 Caddy 2 指定额外的命令行参数。将一个或多个参数添加到列表中，它们将在每次添加程序启动时执行。

**注意**：`--config` 参数会自动添加。有关更多信息，请参阅官方 [Caddy 文档](https://caddyserver.com/docs/command-line#caddy-run)。

### 选项：`env_vars`

允许您定义多个环境变量，通常用于自定义 Caddy 二进制文件构建。这些变量可以按以下格式设置：

示例：

```yaml
env_vars:
  - name: NAMECHEAP_API_USER
    value: xxxx
  - name: NAMECHEAP_API_KEY
    value: xxxx
```

### 选项：`env_vars.name`

指定环境变量的名称。

### 选项：`env_vars.value`

指定分配给环境变量的值。

### 选项：`log_level`

控制添加程序日志输出的详细程度。此设置对于调试或监控添加程序的行为非常有用。可用的日志级别如下：

- `trace`：显示详细信息，包括所有内部函数调用。
- `debug`：提供广泛的调试信息。
- `info`：显示典型的事件和信息。
- `warning`：记录意外的非错误情况。
- `error`：记录不需要立即处理的运行时错误。
- `fatal`：使添加程序无法使用的严重错误。

每个级别都包含更严重级别的消息。例如，`debug` 也包括 `info` 消息。默认设置是 `info`，除非正在排除故障，否则建议使用此设置。

## 高级用法：自定义二进制文件和插件

### 概述

此添加程序使用单个二进制文件来启动 Caddy，这使得它高度可定制。您可以运行任何版本的 Caddy 及其所需的任何插件，为高级用户提供最大的灵活性。

### 自定义 Caddy 二进制文件

要构建您自己的 Caddy 版本，包括特定的插件或功能，您可以按照官方 Caddy 文档中提供的说明使用 [`xcaddy` 工具](https://caddyserver.com/docs/build#xcaddy) 进行操作。这允许您编译自己的 Caddy 版本，包含默认二进制文件中不包含的自定义模块或插件。

### 安装自定义二进制文件

要使用自定义构建的 Caddy 二进制文件，请按照以下步骤操作：

1. 使用 `xcaddy` 或获取适合您需求的预构建版本来构建您的自定义 Caddy 二进制文件。
2. 将 `caddy` 二进制文件放置在添加程序的配置文件夹中。
3. 重新启动 Caddy 2 添加程序以开始使用您的自定义 Caddy 版本。

#### 访问配置文件夹

添加程序配置文件夹位于：

```
/addon_configs/c80c7555_caddy-2
```

这是您应放置自定义 `caddy` 二进制文件和相关配置文件的位置。

重新启动添加程序后，Caddy 将使用您提供的自定义二进制文件，允许您利用自定义构建中包含的任何附加功能或插件。

[ssh]: https://home-assistant.io/addons/ssh/
[samba]: https://home-assistant.io/addons/samba/