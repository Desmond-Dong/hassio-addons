# Home assistant插件：Otter Wiki

# 一个Otter Wiki

Otter Wiki是一款基于Python的协作内容管理软件，称为[维基](https://en.wikipedia.org/wiki/Wiki)。内容存储在git仓库中，该仓库记录了所有更改。[Markdown](https://daringfireball.net/projects/markdown)用作标记语言。Otter Wiki使用[python](https://www.python.org/)编写，并使用微框架[Flask](http://flask.pocoo.org/)。[halfmoon](https://www.gethalfmoon.com)用作CSS框架，[CodeMirror](https://codemirror.net/)用作编辑器。[Font Awesome Free](https://fontawesome.com/license/free)提供图标。

## 显著特性

- 极简界面（支持暗黑模式）
- 支持Markdown高亮和表格的编辑器
- 可定制的侧边栏：菜单和/或页面索引
- 完整的变更日志和页面历史记录
- 用户身份验证
- 页面附件
- 扩展Markdown：表格、脚注、高级块、警告和mermaid图表
- （实验性）Git http服务器：克隆、拉取和推送你的wiki内容
- 一个非常可爱的海獭作为标志（由[Christy Presler](http://christypresler.com/)绘制，CC BY 3.0授权）

_感谢所有给我的仓库加星标的人！要加星标，请点击下面的图片，然后它就会出现在右上角。谢谢！_

[![@jdeath/homeassistant-addons仓库的星标者列表](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个插件使用了[docker镜像](https://github.com/redimp/otterwiki)。

## 安装

这个插件的安装非常简单，与安装任何其他Hass.io插件的方法相同。

1. 将我的Hass.io插件仓库[repository]添加到你的Hass.io实例中。
1. 安装这个插件。
1. 点击`保存`按钮来保存你的配置。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 应该可以通过`<your-ip>:port`访问WebUI。
1. 设置将在`/addon_configs/2effc9b9_otterwiki`。

## 配置

```
port : 8084 #你想要运行的端口。
```

Webui可以在`<your-ip>:port`找到。

[repository]: https://github.com/jdeath/homeassistant-addons