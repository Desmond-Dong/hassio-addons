# Home assistant add-on: Changedetection.io

**最好的、最简单的自托管免费开源网站变更检测跟踪、监控和通知服务。是 Visualping、Watchtower 等的替代品。设计简洁 - 主要目标是免费监控哪些网站发生了文本变更。免费开源网页变更检测**

#### 示例用途

- 产品和服务价格发生变化
- 库存不足通知和库存充足通知
- 政府部门更新（变更通常只在他们的网站上）
- 当您不在他们的邮件列表上时，新软件发布、安全警告
- 活节日的变更
- 房地产列表变更
- 知道您最喜欢的威士忌何时打折，或其他特殊优惠何时宣布，在其他人之前
- 政府网站上的 COVID 相关新闻
- 大学/组织网站上的新闻
- 检测和监控 JSON API 响应中的变更
- JSON API 监控和警报
- 法律和其他文件中的变更
- 当网站上的文本出现时，通过通知触发 API 调用
- 使用 JSON 过滤器和 JSON 通知将 API 连接在一起
- 根据网页内容的变更创建 RSS 源
- 监控 HTML 源代码中的意外变更，加强您的 PCI 合规性
- 您有一个非常敏感的 URL 列表要监控，并且您不想使用付费替代方案。（记住，您就是产品）

需要带有 JavaScript 支持的实际 Chrome 运行器？我们支持通过 WebDriver 和 Playwright 进行抓取！

#### 主要功能

- 许多触发过滤器，如“文本触发”、“通过选择器删除文本”、“忽略文本”、“提取文本”，还使用正则表达式！
- 使用 XPath 和 CSS 选择器定位元素，轻松监控复杂的 JSON，使用 JsonPath 规则
- 在快速非 JS 和基于 Chrome JS 的“抓取器”之间切换
- 轻松指定网站应该检查的频率
- 在提取文本之前执行 JS（适用于登录，请查看 UI 中的示例！）
- 覆盖请求头，指定 `POST` 或 `GET` 和其他方法
- 使用“视觉选择器”帮助定位特定元素

感谢每个人给我的存储库星标！要星标它，请点击下面的图片，然后它将在右上角。谢谢！

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 主要功能


## 安装

此插件的安装非常简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件存储库][repository]添加到您的 Hass.io 实例。
1. 安装此插件。
1. 转到 ip:端口。Ingress 类似地工作，但页面无法正确渲染


## 如何使用带有 Playwright JS 的抓取器而不是内置的 Plaintext/HTTP Client

Changedetection.io 插件本身只能使用内置的 Plaintext/HTTP Client 抓取网站。

许多现代网页使用 JavaScript 填充内容，它们更加动态，有时需要真正的 Chrome 浏览器来抓取内容，尽管其中许多可以使用内置的“抓取器”工作

您可以配置 Changedetection.io 使用 Playwright 抓取器抓取页面，否则它将使用普通的非 JS 内置浏览器。使用 Playwright 抓取器提供 Changedetection.io 的全部功能，包括 JS 浏览器步骤来抓取内容以及视觉过滤器选择器。

要使用 Playwright 抓取器，Changedetection.io 插件需要与 alexbelgium 制作的 Browserless Chrome 插件合作。

要安装 Browserless Chrome 插件，请在 Homeassistant 中添加 alexbelgium/hassio-addons 存储库（https://github.com/alexbelgium/hassio-addons/）。从 Homeassistant 界面安装并启动插件。要使用 Playwright 抓取器，只需在添加要监控的新网站时或在将 Playwright Chromium/Javascript 设置为所有监控网站的系统标准时，转到 Changedetection.io 插件的 Web 界面 > 设置 > 抓取并选择“Playwright Chromium/Javascript”。

更多关于 Browserless Chrome 插件的信息：https://github.com/alexbelgium/hassio-addons/tree/master/browserless_chrome

这两个插件需要在同一台机器上运行。已在 Home Assistant 2023.5.3/Supervisor 2023.04.1/操作系统 10.1 在 Raspberry Pi 4B 上测试，但应该与其他版本和 amd64 设备一起工作。

注意：Browserless Chrome 插件在抓取网站时非常消耗资源，无论是在 RAM 还是 CPU 方面。在 Raspberry Pi 4B 上运行良好，在旧设备上可能较慢。最大并发抓取限制为 1。

[repository]: https://github.com/jdeath/homeassistant-addons