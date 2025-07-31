# Home Assistant Add-on: Omni Tools

## 关于

Omni Tools 是一个自托管的网络应用程序，提供各种在线工具用于日常任务。所有文件处理都在客户端完成，确保隐私和安全。

![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield]

## 功能

- **图像工具**：图像调整大小、转换
- **视频工具**：视频剪辑
- **PDF 工具**：PDF 分割、合并
- **文本/列表工具**：各种文本处理工具
- **日期和时间工具**：日期/时间计算器和转换器
- **数学工具**：数学计算器和转换器
- **数据工具**：JSON、CSV、XML 处理器

## 安装

1. 将此仓库添加到您的 Home Assistant Supervisor add-on 商店
2. 安装 "Omni Tools" add-on
3. 启动 add-on
4. 打开 Web UI

## 配置

### 选项：`PUID`

以运行应用程序的用户 ID。默认为 `0`。

### 选项：`PGID`

以运行应用程序的组 ID。默认为 `0`。

### 选项：`TZ`

应用程序的时区设置。

## 使用

1. 通过 Home Assistant 侧边栏或通过导航到 add-on 的 Web UI 访问 Web 界面
2. 从各种工具类别中选择：
   - 图像/视频/音频处理
   - PDF 操作
   - 文本和列表处理
   - 日期和时间工具
   - 数学工具
   - 数据格式转换

所有处理都在您的浏览器中本地完成，以最大程度地确保隐私和安全。

## 支持

有问题？

您有几个选项来获得答案：

- [Home Assistant Discord 聊天服务器][discord]
- Home Assistant [社区论坛][forum]
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

## 作者和贡献者

此仓库的原始设置由 [Alex Belgium][alexbelgium] 完成。

## 许可证

MIT 许可证

版权所有 (c) 2017-2024 Alex Belgium

特此免费授予任何获得此软件及有关文档文件（“软件”）副本的人，在软件上进行处理的权限，不受限制，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权利，并允许提供软件的人这样做，但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件按“原样”提供，不提供任何形式的保证，包括但不限于对适销性、特定用途适用性和非侵权的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害赔偿或其他责任负责，无论是由合同、侵权或其他行为引起的，均与软件或软件的使用或其他交易有关。

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[alexbelgium]: https://github.com/alexbelgium
[discord]: https://discord.gg/c5DvZ4e
[forum]: https://community.home-assistant.io
[reddit]: https://reddit.com/r/homeassistant