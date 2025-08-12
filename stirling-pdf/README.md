# Home assistant add-on: Stirling-pdf

这是一个使用Docker的本地托管网络PDF编辑工具。它使您能够在PDF文件上进行各种操作，包括拆分、合并、转换、重新组织、添加图像、旋转、压缩等。这个本地托管的网络应用程序已经发展成为一个功能全面的集合，满足您所有的PDF需求。

Stirling PDF不会发起任何用于记录或跟踪目的的外出调用。

所有文件和PDF要么完全存在于客户端，要么仅在任务执行期间驻留在服务器内存中，或者仅在任务执行期间临时驻留在文件中。用户下载的任何文件在该点之前都将从服务器中删除。

有点耗内存。

_感谢所有给我仓库点赞的人！要点赞，请点击下面的图片，它将在右上角显示。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个插件使用了[docker镜像](https://github.com/Stirling-Tools/Stirling-PDF)。

## 安装

这个插件的安装非常简单，与安装任何其他Hass.io插件没有区别。

1. [将我的Hass.io插件仓库][repository]添加到您的Hass.io实例。
1. 安装这个插件。750 MB的镜像需要一段时间来下载
1. 点击`保存`按钮来存储您的配置。
1. 启动插件。
1. 检查插件的日志，看看是否一切顺利。
1. WebUI应该可以通过<your-ip>:port打开。
1. 设置将在 /addon_configs/2effc9b9_stirling-pdf
1. 停止插件，编辑settings.yaml文件来更改您需要的任何内容
## 配置

```
port : 8080 #您想要运行的端口。
```

Webui可以在<your-ip>:port找到。

[repository]: https://github.com/jdeath/homeassistant-addons