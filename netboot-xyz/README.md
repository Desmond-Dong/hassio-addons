# Home Assistant Community Add-on: Netboot.xyz
![支持aarch64架构][aarch64-shield] ![支持amd64架构][amd64-shield] ![支持armhf架构][armhf-shield] ![支持armv7架构][armv7-shield] ![支持i386架构][i386-shield]
![项目维护][maintenance-shield]

Netboot.xyz PXE 服务器用于 Homeassistant OS

## 关于

netboot.xyz 是一种在 BIOS 中从一个地方进行 PXE 启动各种操作系统安装程序或工具的方法，而不需要去获取运行该工具的介质。iPXE 用于提供一个用户友好的菜单，从 BIOS 中即可轻松选择您想要的操作系统，以及任何特定类型的版本或可启动标志。

您可以将 ISO 远程附加到服务器，将其设置为 Grub 中的救援选项，或者甚至设置您的家庭网络默认启动到它，以便它始终可用。

## 安装

[![FaserF Homeassistant Addons](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FFaserF%2Fhassio-addons)
<br />
此附加组件的安装非常简单，与安装其他自定义 Home Assistant 附加组件没有区别。<br />
只需点击上面的链接或将我的仓库添加到 hassio 附加组件存储库： <https://github.com/FaserF/hassio-addons>

## 配置

**注意**：_记得在更改配置后重新启动附加组件。_

示例附加组件配置：

```yaml
path: /media/netboot/image
path_config: /media/netboot/config
dhcp_range: 192.168.178.200
```
<br />

**注意**：_这只是一个示例，请不要直接复制粘贴！请创建您自己的！_

### 选项： `path`

此选项是必需的。根据您的 ISO 文件及其他内容所在的位置进行更改。

注意：必须位于 /media 文件夹中的某个位置！其他文件夹对该附加组件不可见。

### 选项： `path_config`

此选项是必需的。根据您的 netboot.xyz 配置文件及其他内容所在的位置进行更改。

注意：必须位于 /media 文件夹中的某个位置！其他文件夹对该附加组件不可见。

### 选项： `dhcp_range`

此选项是必需的。根据您的网络进行更改。尝试在最后范围内使用较高的 IP（例如 100 或 200）

## 入口

此附加组件支持 Homeassistant 入口。但似乎存在一些 bug。

## 后安装
在第一次启动之前，我建议检查 netboot 配置。<br />
前往 <http://YOUR-HOMEASSISTANT-IP:3000> -> 菜单 -> boot.cfg<br />

### Windows
1. 根据您的 WinPE 位置更改以下行： <br />
   set win_base_url <http://YOUR-SERVER-IP:PortForTheNGINXserver/WinPE> <br />

   例如，如果您将提取的文件直接托管在 netboot.xyz 服务器上，而您的 IP 地址是 192.168.178.2： <br />
   set win_base_url <http://192.168.178.2:85/WinPE> <br />

2. 将 Windows PE 文件复制到您的 $path 文件夹 -> WinPE -> x64<br />
   示例：/media/netboot/image/WinPE/x64<br />

3. 解压 Windows ISO 并将文件复制到您的 $path 文件夹中的任何位置，例如：<br />
   /media/netboot/image/windows<br />

4. 安装 Samba Share Homeassistant 附加组件并启动它<br />
   这是为了为 WinPE 提供 win10 ISO<br />

5. 在启动 WinPE 后输入以下行<br />
net use Z: \ \YOUR-SERVER-IP\$path /user:YOUR-SERVER-IP\mySambaUser myPassword<br />
net use Z: \ \192.168.178.2\media\netboot\image\windows /user:192.168.178.2\mySambaUser myPassword<br />
Z:\setup.exe <br />

更多信息： <br />
<https://netboot.xyz/faq/windows/>

### 自动化此 Windows 安装过程

修改您的 WinPE：<br />
1. 在 WinPE 位置的一个新文件夹 "Scripts" 中创建一个 Main.cmd 文件 <br />
   例如：/media/netboot/image/WinPE/x64/Scripts/Start.cmd<br />
   然后将上面的两行添加到该脚本中<br />
   然后修改 wpeinit 以使用该脚本。
2. 创建一个 autounattend.xml 文件。您可以在这里找到我提供的一些示例： <https://github.com/FaserF/WindowsPostInstaller/tree/master/autounattend><br />

请查看 <https://github.com/netbootxyz/netboot.xyz/discussions/757><br />

## 支持

有问题或疑问？

您可以在这里 [打开一个问题][issue] GitHub。
请记住，此软件仅在 Raspberry Pi 4 上运行的 armv7 中经过测试。

### 已知问题
1. PXE 启动后，若未将 PXE DHCP 选项配置在路由器设置中，启动将运行多个超时<br />
2. 对 boot.cfg 的更改似乎会被 netboot.xyz 忽略。它将始终使用默认配置。 <https://github.com/netbootxyz/netboot.xyz/discussions/861> <br />

## 作者和贡献者

该程序最初来自 Netboot.xyz 项目。如需更多信息，请访问此页面： <https://netboot.xyz/>
hassio 附加组件由 [FaserF] 提供。

## 许可证

MIT 许可证

版权所有 (c) 2019-2025 FaserF & Netboot.xyz 项目

特此免费授予任何获得该软件及相关文档文件（“软件”）副本的人在不受限制的情况下处理该软件的权利，包括但不限于使用、复制、修改、合并、发布、分发、再授权和/或销售该软件的副本，并允许向其提供软件的人这样做，但须符合以下条件：

上述版权声明和本许可声明应包含在所有副本或实质性部分的软件中。

该软件是按“原样”提供的，不提供任何类型的保证，明示或暗示，包括但不限于对适销性、特定用途适用性和非侵权的保证。在任何情况下，作者或版权持有者均不对因使用该软件或与之相关的任何索赔、损害或其他责任承担责任，无论是在合同诉讼、侵权或其他情况下。

[maintenance-shield]: https://img.shields.io/maintenance/yes/2025.svg
[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
[FaserF]: https://github.com/FaserF/
[issue]: https://github.com/FaserF/hassio-addons/issues