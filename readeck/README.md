# Home assistant add-on: Readeck

Readeck 是一个简单的网络应用程序，允许您保存您喜欢并希望永远保留的网页上的宝贵可读内容。将其视为一个书签管理器和稍后阅读的工具。


_感谢大家给我的仓库加星！要加星，请点击下面的图片，它将在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个插件基于 [docker 镜像](https://codeberg.org/readeck/readeck)。

## 功能

### 🔖 书签

喜欢您正在阅读的页面？将链接粘贴到 Readeck 中，您就完成了！

### 📸 文章、图片和视频

Readeck 为您保存网页的可读内容，供您稍后阅读。它还会检测页面是图片还是视频，并相应地调整其处理过程。

### ⭐ 标签、收藏夹、存档

将书签移动到存档或收藏夹，并添加您想要的尽可能多的标签。

### 🖍️ 高亮

突出显示您书签中的重要内容，以便稍后轻松找到它们。

### 🗃️ 收藏集

如果您需要一个专门的部分，其中包含过去 2 周内所有带有“cat”标签的书签，Readeck 允许您将此搜索查询保存到收藏集中，以便稍后访问。

### 🧩 浏览器扩展

在浏览时想保留一些东西？无需复制和粘贴链接。安装浏览器扩展，即可一键保存书签！

- [适用于 Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/readeck/)
- [适用于 Google Chrome](https://chromewebstore.google.com/detail/readeck/jnmcpmfimecibicbojhopfkcbmkafhee)
- [更多信息及源代码](https://codeberg.org/readeck/browser-extension)

### 📖 电子书导出

比在您的电子阅读器上阅读您收集的文章有什么更好的方法？您可以将任何文章导出为电子书文件（EPUB）。甚至可以导出收藏集为一个单一的书籍！

除此之外，如果您的电子阅读器支持 OPDS，您可以直接从电子阅读器访问 Readeck 的目录和收藏集。

### 🔎 全文搜索

无论是需要从文章中找到模糊的文本片段，还是所有带有特定标签或来自特定网站的文章，我们都为您提供了支持！

### 🚀 快速！

Readeck 是对所谓的无聊但经过验证的技术的现代诠释。它保证非常快的响应时间和流畅的用户体验。

### 🔒 为您的隐私和长期存档而设计

您喜欢的这篇文章明年还在网上吗？10 年后呢？也许不在了；也许所有文本和图片都不见了。出于这个原因，以及为了您的隐私，文本和图片在您保存链接的瞬间都会存储在您的 Readeck 实例中。

除了视频之外，您的浏览器不会向任何外部网站发出任何请求。


## 安装

1. [将我的 Hass.io 插件仓库][repository] 添加到您的 Hass.io 实例。
1. 安装此插件。
1. 点击 `保存` 按钮以保存您的配置。
1. 启动插件。
1. 停止插件并重新启动（这是第一次启动两次所必需的！）
1. 检查插件的日志以查看是否一切正常。
1. 应该可以通过 ingress 或 <your-ip>:port 打开 WebUI。

## 更新
由于源代码没有托管在 github 上，很难自动更新这个。如果您想要最新版本，请提交一个问题

## 配置

```
port : 8000 #您想要运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons