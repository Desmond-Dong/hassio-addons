# Home assistant插件：GeoIP Update

GeoIP Update程序执行GeoIP2和GeoLite2二进制数据库的自动更新。

设计用于与@einschmidt Caddy2 Home Assistant插件 `https://github.com/einschmidt/hassio-addons` 一起工作。

注意：最近的Caddy-2更新（v2.0）将配置路径更改为 `/addon_configs/c80c7555_caddy-2`。如果你之前使用的是v1.x版本，请保存此插件的配置，卸载，然后重新安装，然后将配置替换为上述路径。这是必要的，因为插件必须重新构建才能看到新目录

还需要一个自定义的caddy二进制文件，使用 `https://github.com/porech/caddy-maxmind-geolocation` 设置。使用我的 `Caddy Builder` 插件来制作一个。

必须在maxmind.com上设置许可证密钥

_感谢所有给我的仓库点赞的人！要在下面点击图片点赞，它就会出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

Docker镜像通过环境变量进行配置。以下变量是必需的：

* `GEOIPUPDATE_EDITION_IDS` - 空格分隔的数据库版本ID列表。
  版本ID可以由字母、数字和破折号组成。默认 "GeoLite2-ASN GeoLite2-City GeoLite2-Country"。

* `GEOIPUPDATE_ACCOUNT_ID` - 你的MaxMind账户ID（不是你的用户名）。

* `GEOIPUPDATE_LICENSE_KEY` - 你的区分大小写的MaxMind许可证密钥（不是你的密码）。

* `GEOIPUPDATE_FREQUENCY` - `geoipupdate` 运行的间隔小时数。
  如果没有设置此值或设置为 `0`，`geoipupdate` 将运行一次并退出。

* `GEOIPUPDATE_DB_DIR` - geoipupdate将下载数据库的目录。默认是 `/addon_configs/c80c7555_caddy-2` 以与新caddy-2插件保持一致。
  
[repository]: https://github.com/jdeath/homeassistant-addons

## 使用方法
制作一个自定义的caddy构建，包括 `--with github.com/porech/caddy-maxmind-geolocation`，并将其放在 `/share/caddy/`（v1.x）中，文件名可以是 `caddy` 或 `/addon_configs/c80c7555_caddy-2`（v2.0）

编辑 `/share/caddy/Caddyfile`

添加一个GEOFilter块来允许某些国家和你的本地IP地址。我在网上找到了这个，如果你需要帮助，请去Caddyforums提问。

```
(GEOFILTER) {
        @geofilter {
                not maxmind_geolocation {
                        db_path "/share/caddy/GeoLite2-Country.mmdb"
                        allow_countries IT FR
                }
                not remote_ip private_ranges
        }
        respond @geofilter 403
}
```

然后在任何 `reverse_proxy` 指令之前添加这一行
```
import GEOFILTER