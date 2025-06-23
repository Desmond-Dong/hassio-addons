# 家庭助理附加组件：Trillium
Trilium Notes 是一个层次化的笔记应用程序，专注于构建大型个人知识库。

_感谢所有为我的仓库点星的人！要给它点星，请点击下面的图片，然后它将出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 特点

* 笔记可以排列成任意深度的树。单个笔记可以放置在树中的多个位置（参见 [克隆](https://github.com/zadam/trilium/wiki/Cloning-notes)）
* 丰富的所见即所得笔记编辑，包括例如表格、图片和 [数学](https://github.com/zadam/trilium/wiki/Text-notes#math-support)，并支持 markdown [自动格式化](https://github.com/zadam/trilium/wiki/Text-notes#autoformat)
* 支持编辑 [带有源代码的笔记](https://github.com/zadam/trilium/wiki/Code-notes)，包括语法高亮
* 快速且便捷的 [笔记之间导航](https://github.com/zadam/trilium/wiki/Note-navigation)、全文搜索和 [笔记提升](https://github.com/zadam/trilium/wiki/Note-hoisting)
* 无缝的 [笔记版本控制](https://github.com/zadam/trilium/wiki/Note-revisions)
* 笔记 [属性](https://github.com/zadam/trilium/wiki/Attributes) 可用于笔记组织、查询和高级 [脚本](https://github.com/zadam/trilium/wiki/Scripts)
* 与自托管同步服务器的 [同步](https://github.com/zadam/trilium/wiki/Synchronization)
  * 有一个 [第三方服务用于托管同步服务器](https://trilium.cc/paid-hosting)
* [共享](https://github.com/zadam/trilium/wiki/Sharing)（发布）笔记到公共互联网
* 强大的 [笔记加密](https://github.com/zadam/trilium/wiki/Protected-notes)，具备按笔记粒度加密
* 使用内置的 Excalidraw 绘图（笔记类型为 "canvas"）
* [关系图](https://github.com/zadam/trilium/wiki/Relation-map) 和 [链接图](https://github.com/zadam/trilium/wiki/Link-map) 用于可视化笔记及其关系
* [脚本](https://github.com/zadam/trilium/wiki/Scripts) - 请参见 [高级展示](https://github.com/zadam/trilium/wiki/Advanced-showcases)
* 用于自动化的 [REST API](https://github.com/zadam/trilium/wiki/ETAPI)
* 在可用性和 100,000 个笔记以上的性能上都表现良好
* 针对智能手机和平板电脑优化的 [移动前端](https://github.com/zadam/trilium/wiki/Mobile-frontend)
* [夜间主题](https://github.com/zadam/trilium/wiki/Themes)
* [印象笔记](https://github.com/zadam/trilium/wiki/Evernote-import) 和 [Markdown 导入与导出](https://github.com/zadam/trilium/wiki/Markdown)
* [网页剪辑器](https://github.com/zadam/trilium/wiki/Web-clipper) 方便保存网页内容

## 安装

1. [将我的 Hass.io 附加组件仓库][repository] 添加到您的 Hass.io 实例中。
1. 安装此附加组件。
1. 点击 `Save` 按钮保存您的配置。
1. 在您的 homeassistant 上创建目录 `/share/trillium/`
1. 通过 SSH 登录到您的家庭助理并运行 `chmod 2777 /share/trillium`
1. 启动附加组件。
1. 检查附加组件的日志，以查看一切是否正常。
1. 转到您的本地 homeassistant IP:端口管理端口或入口。
1. 按照说明进行操作

```
port : 8000 #您希望运行管理界面的端口。
```

Webui 可以在 `<your-ip>:port` 或入口中找到。

[repository]: https://github.com/jdeath/homeassistant-addons