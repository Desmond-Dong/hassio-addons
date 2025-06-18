# Home assistant add-on: Changedetection.io

**最好的和最简单的自托管免费开源网站变更检测、跟踪、监控和通知服务。是 Visualping、Watchtower 等的替代品。旨在简单，主要目标是免费监控哪些网站有文本变化。免费开源网页变更检测**

#### 示例用例

- 产品和服务的价格发生变化
- _缺货通知_和_补货通知_
- 政府部门更新（更改通常仅在他们的网站上）
- 新软件发布，当您不在他们的邮件列表中时的安全通知。
- 节日变更
- 房地产列表变更
- 了解您喜爱的威士忌何时降价，或其他特价在任何人之前宣布
- 政府网站上的 COVID 相关消息
- 大学/组织的官方网站上的新闻
- 检测和监控 JSON API 响应中的变化 
- JSON API 监控和警报
- 法律和其他文档的变化
- 当网站上出现文本时通过通知触发 API 调用
- 使用 JSON 过滤器和 JSON 通知连接 APIs
- 根据网络内容的变化创建 RSS 订阅
- 监控 HTML 源代码的意外变化，加强您的 PCI 合规性
- 您有一个非常敏感的 URL 列表需要关注，您_不_想使用付费替代品。（记住，_您_是产品）

_需要一个实际支持 JavaScript 的 Chrome 运行程序吗？我们支持通过 WebDriver 和 Playwright 进行提取！_

#### 主要特性

- 丰富的触发过滤器，如“基于文本触发”、“按选择器移除文本”、“忽略文本”、“提取文本”，还可以使用正则表达式！
- 使用 xPath 和 CSS 选择器定位元素，轻松监控复杂的 JSON，使用 JsonPath 规则
- 在快速的非 JS 和基于 Chrome JS 的“提取器”之间切换
- 轻松指定网站检查频率
- 提取文本前执行 JS（适合登录，请参见 UI 中的示例！）
- 覆盖请求头，指定 `POST` 或 `GET` 和其他方法
- 使用“可视选择器”帮助定位特定元素

_感谢所有给我的仓库加星的朋友！要给它加星，请点击下面的图片，然后它将显示在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 主要特性


## 安装

此插件的安装非常简单，与安装其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件库][repository] 添加到您的 Hass.io 实例。
1. 安装此插件。
1. 访问 ip:port。Ingress 有点作用，但页面无法正确渲染


## 如何使用启用 Playwright JS 的提取器，而不是内置的 Plaintext/HTTP 客户端

Changedetection.io 插件本身只能使用内置的 Plaintext/HTTP 客户端提取网站。

许多现代网页使用 JavaScript 填充内容，这些网页更为动态，有时需要真正的 Chrome 浏览器来提取内容，尽管许多网页可以使用内置的“提取器”

您可以配置 Changedetection.io 使用 Playwright 提取器提取页面，否则它将使用内置的非 JS 浏览器进行提取。使用 Playwright 提取器提供了完整的 Changedetection.io 功能，包括 JS 浏览器步骤以提取内容和可视过滤选择器。

要使用 Playwright 提取器，Changedetection.io 插件需要与 alexbelgium 制作的无浏览器 Chrome 插件配合使用。

要安装无浏览器 Chrome 插件，请在 Homeassistant 中添加 alexbelgium/hassio-addons 库（https://github.com/alexbelgium/hassio-addons/）。从 Homeassistant 界面安装并启动该插件。要使用 Playwright 提取器，只需在添加要监控的新网站时在“请求”选项卡中勾选“Playwright Chromium/Javascript”，或将其设置为所有监控网站的系统标准，前往您的 Changedetection.io 插件的 Web 界面 > 设置 > 提取，选择“Playwright Chromium/Javascript”。

更多关于无浏览器 Chrome 插件的信息：https://github.com/alexbelgium/hassio-addons/tree/master/browserless_chrome

两个插件需要在同一台机器上运行。已在 Raspberry Pi 4B 上测试 Home Assistant 2023.5.3/Supervisor 2023.04.1/Operating System 10.1，但应该也能在其他版本及 amd64 设备上运行。

注意：无浏览器 Chrome 插件在提取网站时相当耗费资源，无论是在 RAM 还是 CPU 的使用上。在 RPi 4B 上运行良好，但在较旧的设备上可能较慢。最大同时提取数量限制为 1。


[repository]: https://github.com/jdeath/homeassistant-addons