# 家庭助手附加组件：Changedetection.io

**最优秀且最简单的自托管免费开源网站更改检测追踪、监控和通知服务。 Visualping、Watchtower等的替代品。旨在简化 – 主要目标是简单监控哪些网站存在文本更改，且是免费的。免费开源网页更改检测**

#### 示例用例

- 产品和服务的价格变动
- _缺货通知_ 和 _恢复库存通知_
- 政府部门更新（更改通常只在他们的网站上）
- 新软件发布、当你不在他们的邮件列表中时的安全公告。
- 节日的变更
- 房地产列表变更
- 知道你最喜欢的威士忌打折的时机，或其他特别交易在任何人之前宣布
- 政府网站的COVID相关新闻
- 大学/组织的网站新闻
- 检测并监控JSON API响应的变化
- JSON API监控和警报
- 法律及其他文件的更改
- 当网站上出现文本时通过通知触发API调用
- 使用JSON过滤器和JSON通知连接API
- 根据网页内容的更改创建RSS源
- 监控HTML源代码以检测意外更改，加强你的PCI合规性
- 你有一个非常敏感的URL列表需要监视，而你不想使用付费替代方案。（记住，_你_才是产品）

_需要一个实际支持Javascript的Chrome运行器吗？我们支持通过WebDriver和Playwright获取！</a>_

#### 主要特点

- 大量触发器过滤器，例如“根据文本触发”、“按选择器移除文本”、“忽略文本”、“提取文本”，也可使用正则表达式！
- 使用xPath和CSS选择器针对元素，轻松监控复杂的JSON，使用JsonPath规则
- 在快速的非JS和Chrome JS基础的“提取器”之间切换
- 轻松指定网站检查的频率
- 提取文本前执行JS（适用于登录，见用户界面示例！）
- 覆盖请求头，指定`POST`或`GET`及其他方法
- 使用“视觉选择器”帮助定位特定元素

_感谢每一个给我的仓库点星的人！要点星请点击下面的图片，然后它将位于右上方。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 主要特点


## 安装

该附加组件的安装相当简单，与安装任何其他Hass.io附加组件没有区别。

1. [将我的Hass.io附加组件库][repository]添加到你的Hass.io实例。
2. 安装此附加组件。
3. 转到ip:port。Ingress有些有效，但页面无法正确渲染。


## 如何使用启用Playwright JS的提取器替代内置的纯文本/HTTP客户端

Changedetection.io附加组件本身只能使用内置的纯文本/HTTP客户端获取网站。

许多现代网页使用JavaScript填充内容，它们更动态，有时需要真正的Chrome浏览器来获取内容，尽管许多可能在内置的“提取器”下工作。

你可以配置Changedetection.io使用Playwright提取器获取页面，否则它将使用纯非JS内置浏览器进行获取。使用Playwright提取器提供完整的Changedetection.io功能，包括获取内容的JS浏览器步骤和视觉过滤器选择器。

要使用Playwright提取器，Changedetection.io附加组件需要与由alexbelgium制作的Browserless Chrome附加组件协作。

要安装Browserless Chrome附加组件，在Homeassistant中添加alexbelgium/hassio-addons库（https://github.com/alexbelgium/hassio-addons/）。从Homeassistant界面安装并启动附加组件。要使用Playwright提取器，只需在添加要监控的新站点时在“请求”选项卡中勾选“Playwright Chromium/Javascript”，或将其设置为所有监控站点的系统标准，前往Changedetection.io附加组件的Web界面 > 设置 > 获取，然后选择“Playwright Chromium/Javascript”。

关于Browserless Chrome附加组件的更多信息： https://github.com/alexbelgium/hassio-addons/tree/master/browserless_chrome

两个附加组件需要运行在同一台机器上。在Raspberry Pi 4B上测试，使用Home Assistant 2023.5.3/Supervisor 2023.04.1/操作系统10.1，但应该适用于任何其他版本和amd64设备。

注意：Browserless Chrome附加组件在获取网站时非常消耗资源，包括RAM和CPU。在RPi 4B上运行良好，但可能在旧设备上较慢。最大同时获取限制为1。

[repository]: https://github.com/jdeath/homeassistant-addons