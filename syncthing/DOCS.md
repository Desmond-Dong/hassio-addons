## 配置

通过 [Syncthing 的 Web 界面](/hassio/68413af6_syncthing/ingress)（嵌入在 Home Assistant 中）进行配置。首先从 [*信息* 标签](/hassio/addon/68413af6_syncthing/info) 启动附加组件，然后点击 `打开 Web 界面`。

启动后，Syncthing 显示一个通知（在顶部的黄色框中）：

> 启用了不安全的管理员访问。

这可以安全地忽略，因为它 [不适用于此附加组件](https://github.com/Poeschl/Hassio-Addons/issues/340)。

## Syncthing Home Assistant 集成

如果您想通过 Home Assistant 的 [**Syncthing** 集成](https://www.home-assistant.io/integrations/syncthing/) 监控 Syncthing 附加组件，您需要将 Syncthing 的 Web 界面暴露给（本地）网络，而不仅仅是暴露给 [Home Assistant Supervisor](https://developers.home-assistant.io/docs/supervisor)。

为此，请转到附加组件的 [*配置* 标签](/hassio/addon/68413af6_syncthing/config)，切换 `显示禁用端口` 并在标记为 *Web 前端（不需要 Ingress）* 的字段中输入一个端口号（根据默认值 `8384` 即可）。点击 `保存`，切换到 [*信息* 标签](/hassio/addon/68413af6_syncthing/info) 并点击 `重启`。

要完成设置，请按照集成文档中的 [*先决条件*](https://www.home-assistant.io/integrations/syncthing/#prerequisites) 和 [*配置*](https://www.home-assistant.io/integrations/syncthing/#configuration) 部分进行操作。

请注意，如果您的 Home Assistant 安装可以从互联网访问（例如，因为您启用了 [远程访问](https://www.home-assistant.io/docs/configuration/remote/)），设置上述端口会带来安全影响。在这种情况下，强烈建议通过 Syncthing 的设置设置一个 `GUI 认证用户` 和一个强 `GUI 认证密码`。有关更多信息，请参阅 [*安全原则*](https://docs.syncthing.net/users/security)。

## 可用目录

为了永久保存您的数据，同步文件夹必须放在以下路径之一下：

| 路径           | 描述                                                                                                                                            |
| -------------- | ------------------------------------------------------------------------------------------------------- |
| `/addon_configs` | 所有 Home Assistant 附加组件的配置。                                                                                                               |
| `/addons`       | 本地 Home Assistant 附加组件。                                                                                                                              |
| `/backups`      | Home Assistant 备份。                                                                                                                                    |
| `/config`       | Syncthing 自己的配置。                                                                                                                             |
| `/data`         | Syncthing 自己的内部数据（状态）。不推荐在此处存储同步文件夹。                                                                            |
| `/homeassistant` | Home Assistant 自己的配置。                                                                                                                        |
| **`/media`**    | 要在附加组件和 Home Assistant 之间共享的媒体文件。有关在此路径下自动挂载外部存储设备的方法，请参阅下文。 |
| ***`/share`***   | 要在附加组件和 Home Assistant 之间共享的数据。这是同步文件夹的默认路径。                                                         |
| `/ssl`          | TLS/SSL 证书。                                                                                                                                      |

只有上述目录会被映射到附加组件容器中。如果您将同步文件夹放在任何其他目录（如 `/root` 或 `/mnt`），则在附加组件重启时同步数据会被删除。我们建议将同步文件夹放在 **`/share`** 或 **`/media`** 下。这两个目录都设计为在附加组件之间共享，因此您可以通过 [终端 & SSH](/hassio/addon/core_ssh/info) 附加组件等访问同步文件夹。

此外，请注意：

- Syncthing 附加组件的备份将包括其 `/data` 目录，其中存储其内部状态。此文件夹可能包含几个 GiB 的数据。
- 一个 [*完整* Home Assistant 备份](https://www.home-assistant.io/common-tasks/os/#backup) 将包括 `/addons`、`/config`、`/media`、`/share` 和 `/ssl` 目录及其内容。创建一个 *部分* 备份以特定排除其中任何一个。
- 同步 `/backup` 目录（最好在 [仅发送模式](https://docs.syncthing.net/users/foldertypes.html#send-only-folder) 下）是一种简单的方法，可以自动将 Home Assistant 备份备份到您其他 Syncthing 设备。 😉
- 将数据同步到内存卡（eMMC、SD 等）可能是一个坏主意，因为快速磨损，或者如果同步数据太大而根本不可能。这个问题可以通过以下方式解决：
  - 通过 [配置 Home Assistant 使用外部数据磁盘](https://www.home-assistant.io/common-tasks/os/#using-external-data-disk)，或者
  - 通过在上述目录之一下挂载合适的存储设备（例如 `/media/ext`）并在该路径下放置同步文件夹。

    要自动让 Home Assistant OS 在 `/media` 下挂载 USB 存储设备，请使用以下 udev 规则：
    <!-- markdownlint-disable MD033 -->
    <details>
    <summary><code>80-mount-usb-to-media-by-label.rules</code></summary>
  
    ```sh
    #
    # udev 规则
    #   使用分区名称作为挂载点，将 USB 驱动器挂载到媒体目录
    #
    # 描述：
    #   为 Home Assistant OS 创建，此规则将任何 USB 驱动器挂载到 Hassio 媒体目录 (/mnt/data/supervisor/media)。
    #   当 USB 驱动器连接到主板时，规则会在媒体目录下为每个分区创建一个目录。新创建的分区按分区名称命名。
    #   如果分区没有名称，则使用以下名称格式："usb-{block-name}"，其中 block name 是 sd[a-z][0-9]。
    #
    # 注意 1：
    #   规则名称始终以数字为前缀。在这种情况下，规则使用 80。
    #   这表示 udev 中规则的顺序。低数字优先执行，高数字最后执行。但是，低数字没有高数字可能有的所有功能。
    #   为了使此规则正常运行，请使用大于或等于 80 的数字。
    #
    # 注意 2：
    #   此规则将跳过挂载 'CONFIG' USB 密钥。
    #   https://github.com/home-assistant/operating-system/blob/dev/Documentation/configuration.md
    #
    # 注意 3：
    #   如果操作系统在 USB 驱动器上排序（即 USB 引导），此规则将挂载操作系统分区。
    #   为防止此问题发生，请更新规则以跳过引导 USB 驱动器。
    #   请参阅下面的警告消息。
    #
    # 灵感来源：
    #   https://www.axllent.org/docs/auto-mounting-usb-storage/
    #
    # 有用的链接：
    #   https://wiki.archlinux.org/index.php/Udev
    #
    # udev 命令：
    #   - 重新加载新规则以重新启动 udev：
    #       udevadm control --reload-rules
    #   - 列出 sdb1 的设备属性：
    #       udevadm info --attribute-walk --name=/dev/sdb1
    #   - 列出 sdb1 的环境变量：
    #       udevadm info /dev/sdb1
    #   - 触发 sdb1 的添加/删除事件：
    #       udevadm trigger --verbose --action=add --sysname-match=sdb1
    #       udevadm trigger --verbose --action=remove --sysname-match=sdb1
    #


    # 过滤块设备，否则退出
    # 警告：如果从 USB 驱动器引导（例如：sda），请将 'sd[b-z][0-9]' 更改为
    KERNEL!="sd[a-z][0-9]", GOTO="abort_rule"

    # 跳过非 USB 设备（例如：内部 SATA 驱动器）
    ENV{ID_PATH}!="*-usb-*", GOTO="abort_rule"

    # 将分区信息导入环境变量
    IMPORT{program}="/usr/sbin/blkid -o udev -p %N"

    # 如果分区不是文件系统，则退出
    ENV{ID_FS_USAGE}!="filesystem", GOTO="abort_rule"

    # 如果这是 'CONFIG' USB 密钥，则退出
    ENV{ID_FS_LABEL}=="CONFIG", GOTO="abort_rule"

    # 如果存在，则获取分区名称，否则创建一个
    ENV{ID_FS_LABEL}!="", ENV{dir_name}="%E{ID_FS_LABEL}"
    ENV{ID_FS_LABEL}=="", ENV{dir_name}="usb-%k"

    # 确定挂载点
    ENV{mount_point}="/mnt/data/supervisor/media/%E{dir_name}"

    # 在 'add' 事件（即插入 USB 驱动器）上挂载设备
    ACTION=="add", RUN{program}+="/usr/bin/mkdir -p %E{mount_point}", RUN{program}+="/usr/bin/systemd-mount --no-block --automount=no --collect $devnode %E{mount_point}"

    # 在 'remove' 事件（即拔出或弹出 USB 驱动器）上卸载设备
    ACTION=="remove", ENV{dir_name}!="", RUN{program}+="/usr/bin/systemd-umount %E{mount_point}", RUN{program}+="/usr/bin/rmdir %E{mount_point}"

    # 退出
    LABEL="abort_rule"
    ```

    [来源](https://gist.github.com/eklex/c5fac345de5be9d9bc420510617c86b5)

    </details>

    上述 udev 规则必须放在 Home Assistant OS 主机的 `/etc/udev/rules.d/` 下。这需要 [SSH 访问主机](https://developers.home-assistant.io/docs/operating-system/debugging/#ssh-access-to-the-host) 或一个 [`CONFIG` USB 驱动器](https://github.com/home-assistant/operating-system/blob/dev/Documentation/configuration.md#configuration)，您在其中创建文件 `udev/80-mount-usb-to-media-by-label.rules` 并包含上述内容。更多信息和小型讨论可以在 [Home Assistant 社区论坛](https://community.home-assistant.io/t/solved-mount-usb-drive-in-hassio-to-be-used-on-the-media-folder-with-udev-customization/258406) 上找到。