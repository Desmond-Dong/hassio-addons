# Home Assistant 附加组件：MariaDB

## 安装

按照以下步骤在您的系统上安装附加组件：

1. 在您的 Home Assistant 前端中导航到 **设置** -> **附加组件** -> **附加组件商店**。
2. 找到 "MariaDB" 附加组件并点击它。
3. 点击 "安装" 按钮。

## 如何使用

1. 将 `logins` -> `password` 字段设置为强密码和独特的值。
2. 启动附加组件。
3. 检查附加组件日志输出以查看结果。
4. 将 `recorder` 集成添加到您的 Home Assistant 配置中。

## 附加组件配置

MariaDB 服务器附加组件可以根据您的喜好进行调整。本节描述了每个附加组件配置选项。

示例附加组件配置：

```yaml
databases:
  - homeassistant
logins:
  - username: homeassistant
    password: PASSWORD
  - username: read_only_user
    password: PASSWORD
rights:
  - username: homeassistant
    database: homeassistant
  - username: read_only_user
    database: homeassistant
    privileges:
      - SELECT
```

### 选项：`databases`（必需）

数据库名称，例如 `homeassistant`。允许多个。

### 选项：`logins`（必需）

此部分定义了在 MariaDB 中创建用户的信息。[创建用户][createuser] 文档。

### 选项：`logins.username`（必需）

数据库用户登录名，例如 `homeassistant`。[用户名][username] 文档。

### 选项：`logins.password`（必需）

用户登录的密码。应为强密码和独特值。

### 选项：`rights`（必需）

此部分授予用户在 MariaDB 中的特权。[授予][grant] 文档。

### 选项：`rights.username`（必需）

这应该是 `logins` 中定义的相同用户名。

### 选项：`rights.database`（必需）

这应该是 `databases` 中定义的相同数据库。

### 选项：`rights.privileges`（可选）

要授予此用户的特权列表，来自 [授予][grant]，如 `SELECT` 和 `CREATE`。如果省略，则将 `ALL PRIVILEGES` 授予用户。限制 Home Assistant 使用的用户权限不建议，但如果您想允许其他应用程序查看记录器数据，则应创建一个限制为只读访问数据库的用户。

### 选项：`mariadb_server_args`（可选）

一些用户在大型数据库上执行 Home Assistant 架构更新时遇到了 [错误][migration-issues]。定义推荐的参数可以帮助（如果有可用的内存）。

示例：`--innodb_buffer_pool_size=512M`

## Home Assistant 配置

MariaDB 将由 Home Assistant 内的 `recorder` 和 `history` 组件使用。有关设置此内容的更多信息，请参阅 Home Assistant 的 [recorder 集成][mariadb-ha-recorder] 文档。

示例 Home Assistant 配置：

```yaml
recorder:
  db_url: mysql://homeassistant:password@core-mariadb/homeassistant?charset=utf8mb4
```

## 支持

有问题吗？

您可以在 [这里打开一个问题][issue] GitHub。

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
[issue]: https://github.com/erik73/addon-mariadb/issues
[repository]: https://github.com/erik73/hassio-addons