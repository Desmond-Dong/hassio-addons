# 非官方 Home Assistant 插件：Victoria Metrics

Victoria Metrics (<https://github.com/VictoriaMetrics/VictoriaMetrics>) 被打包为 Home Assistant 插件。

![aarch64-shield](https://img.shields.io/badge/aarch64-yes-green)
![amd64-shield](https://img.shields.io/badge/amd64-yes-green)
![armv7-shield](https://img.shields.io/badge/armv7-yes-green)
![i386-shield](https://img.shields.io/badge/i386-yes-green)

## 安装

按照以下步骤在您的系统上安装该插件：

1. 在您的 Home Assistant 前端中导航到 **Supervisor -> Add-on Store**
1. 通过 URL 添加这个新仓库
   (`https://github.com/bluemaex/home-assistant-addons`)
1. 找到 "Unpoller" 插件并点击它。
1. 点击 "INSTALL" 按钮
1. 阅读插件内的文档
1. 根据您的喜好调整配置
1. 开始进行长期跟踪 👍

## 关于

VictoriaMetrics 是一个快速、经济高效且可扩展的监控解决方案和时间序列数据库。如果您希望为您的 HomeAssistant 数据提供长期存储，并进行比默认 HomeAssistant 保留期更长的自定义评估，它是一个不错的选择。

您可以以两种不同的方式运行此插件：

### 服务器

在低配置计算机（如 Raspberry PI）上运行一个完整的
[超高效时间序列数据库](https://github.com/VictoriaMetrics/VictoriaMetrics#prominent-features) 服务器。

### 代理

此插件简化了本地抓取（即获取）指标，将其缓存到本地临时数据库，并在可达时将其发送到您的集中式 Victoria Metrics 时间序列数据库服务器，从而即使在数据库暂时无法访问时也能够拥有完整数据。

## 最终说明

有关如何配置此插件的信息，请参阅插件页面中的
[文档](DOCS.md)

该项目与 Victoria Metrics、Victoria Metrics 维护团队没有关联，仅是社区努力。Victoria Metrics 本身根据
[Apache License 2.0](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/LICENSE) 发布。