# Home assistant add-on: Changedetection.io

**最好的、最简单的自托管免费开源网站变更检测跟踪、监控和通知服务。Visualping、Watchtower等的替代品。专为简单设计——主要目标是免费监控哪些网站发生了文本变更。免费开源网页变更检测**

#### 示例用例

- 产品和服务价格变更
- _缺货通知_和_重新有货通知_
- 政府部门更新（变更通常只在其网站上）
- 新软件发布、安全公告，而您不在其邮件列表上时。
- 活节日的变更
- 房地产列表变更
- 知道您最喜欢的威士忌何时打折，或其他人宣布其他特别优惠之前
- 政府网站上的新冠疫情相关新闻
- 大学/组织网站上的新闻
- 检测和监控JSON API响应中的变更
- JSON API监控和警报
- 法律和其他文件中的变更
- 当网站出现文本时通过通知触发API调用
- 使用JSON过滤器和JSON通知将API粘合在一起
- 基于网页内容变更创建RSS订阅源
- 监控HTML源代码的意外变更，加强您的PCI合规性
- 您有一个非常敏感的URL列表要监控，并且您不想使用付费替代方案。（记住，_您_就是产品）

_需要带有JavaScript支持的Chrome运行器？我们支持通过WebDriver和Playwright进行抓取！_

#### 主要功能

- 许多触发过滤器，如“文本触发”、“通过选择器删除文本”、“忽略文本”、“提取文本”，还使用正则表达式！
- 使用XPath和CSS选择器定位元素，轻松使用JsonPath规则监控复杂的JSON
- 在基于JS的快速非JS和Chrome JS的“抓取器”之间切换
- 轻松指定网站检查的频率
- 在提取文本之前执行JS（适用于登录，请查看UI中的示例！）
- 覆盖请求头，指定`POST`或`GET`和其他方法
- 使用“可视化选择器”帮助定位特定元素

_感谢大家给我的仓库星标！要星标它，请点击下面的图片，然后它将在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 主要功能


## 安装

此插件的安装非常简单，与安装任何其他Hass.io插件没有区别。

1. [将我的Hass.io插件仓库][repository]添加到您的Hass.io实例。
1. 安装此插件。
1. 前往ip:port。Ingress有点像工作，但页面无法正确渲染


## 如何使用带有Playwright JS的抓取器而不是内置的Plaintext/HTTP客户端

Changedetection.io插件本身只能使用内置的Plaintext/HTTP客户端抓取网站。

许多现代网页使用JavaScript填充内容，它们更动态，有时需要真正的Chrome浏览器来抓取内容，尽管许多可以使用内置的'抓取器'工作

您可以将Changedetection.io配置为使用Playwright抓取器抓取页面，否则它将使用普通的非JS内置浏览器。使用Playwright抓取器提供Changedetection.io的全部功能，包括用于抓取内容的JS浏览器步骤和可视化过滤器选择器。

要使用Playwright抓取器，Changedetection.io插件需要与alexbelgium制作的Browserless Chrome插件合作。

要安装Browserless Chrome插件，请在Homeassistant中添加alexbelgium/hassio-addons仓库（https://github.com/alexbelgium/hassio-addons/）。从Homeassistant界面安装并启动插件。要使用Playwright抓取器，只需在添加要监控的新网站或将其设置为所有监控网站的系统标准时，在“请求”选项卡中选中“Playwright Chromium/Javascript”。前往您的Changedetection.io插件的Web界面 > 设置 > 抓取，并选择“Playwright Chromium/Javascript”。

更多关于Browserless Chrome插件的信息：https://github.com/alexbelgium/hassio-addons/tree/master/browserless_chrome

这两个插件需要在同一台机器上运行。在Raspberry Pi 4B上的Home Assistant 2023.5.3/Supervisor 2023.04.1/操作系统10.1上进行了测试，但应该与其他版本和amd64设备一起工作。

注意：Browserless Chrome插件在抓取网站时相当消耗资源，无论是在RAM和CPU方面。在RPi 4B上运行良好，在旧设备上可能较慢。最大同时抓取限制为1。

[repository]: https://github.com/jdeath/homeassistant-addons