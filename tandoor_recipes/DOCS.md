## 配置

请查阅 Tandoor Recipes 文档：https://docs.tandoor.dev/install/docker/

```yaml
必需：
    "ALLOWED_HOSTS": "your system url", # 您需要输入您的 homeassistant url（逗号分隔，无空格）以允许 ingress 正常工作
    "DB_TYPE": "list(sqlite|postgresql_external)" # 要使用的数据库类型。
    "SECRET_KEY": "str", # 您的秘密密钥
    "环境": 0|1 # 1 是调试模式，0 是正常模式。除非您正在进行开发，否则应在正常模式下运行。
可选：
    "POSTGRES_HOST": "str?", # 用于 postgresql_external
    "POSTGRES_PORT": "str?", # 用于 postgresql_external
    "POSTGRES_USER": "str?", # 用于 postgresql_external
    "POSTGRES_PASSWORD": "str?", # 用于 postgresql_external
    "POSTGRES_DB": "str?" # 用于 postgresql_external
    "AI_MODEL_NAME": "str?", # 在配置 llm 集成时使用
    "AI_API_KEY": "str?", # 在配置 llm 集成时使用
    "AI_RATELIMIT": "int?", # 在配置 llm 集成时使用
    "externalfiles_folder": "str?" # 您希望在 tandoor 中映射的文件夹。由于 /share/ 和 /media/ 已经映射，因此不需要这个设置。如果该文件夹不存在，则会创建它。
```

此插件现在使用 Tandoor 的集成 Nginx 服务器，并默认暴露端口 80（默认映射到 9928）。

### Mariadb
Mariadb 是 home assistant 社区中一个流行的插件，但它不受 Tandoor Recipes 应用程序的支持。

### 调试模式
这是“环境”设置。
0 是正常模式
1 是调试模式。

### 身份验证
使用外部身份验证。Tandoor Recipes 支持这一点，但目前尚未实现。

### 外部配方文件

目录 `/config/addons_config/tandoor_recipes/externalfiles` 可用于将外部文件导入 Tandoor。您可以通过 Docker 将其映射到 `/opt/recipes/externalfiles`。具体操作请参阅：https://docs.tandoor.dev/features/external_recipes/
目录 `/config`、`/media/` 和 `/share/` 已经映射到插件中。您可以在这些位置手动创建一个文件夹并将其映射到 tandoor：
- 在您想要的位置创建一个目录，例如 `/share/tandoor/recipebook/`
- 在 tandoor 中创建一个 externalstorage 位置 - `/share/tandoor/`
- 监视特定文件夹 - `/share/tandoor/recipebook/`
- 现在同步
- 导入。