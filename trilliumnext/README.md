# 家庭助理附加组件：Trillium Next Notes
Trilium Next Notes 是一个层次化的笔记应用程序，专注于构建大型个人知识库。

_感谢所有给我的仓库加星的人！要加星，请点击下方图像，然后它会出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 特性

* 笔记可以排列成任意深度的树。单个笔记可以放在树的多个位置（参见 [克隆](https://triliumnext.github.io/Docs/Wiki/cloning-notes)）
* 丰富的所见即所得笔记编辑，包括例如表格、图像和 [数学](https://triliumnext.github.io/Docs/Wiki/text-notes) 以及 Markdown 的 [自动格式化](https://triliumnext.github.io/Docs/Wiki/text-notes#autoformat)
* 支持编辑 [带源代码的笔记](https://triliumnext.github.io/Docs/Wiki/code-notes)，包括语法高亮
* 快速且便捷的 [笔记之间导航](https://triliumnext.github.io/Docs/Wiki/note-navigation)，全文搜索和 [笔记提升](https://triliumnext.github.io/Docs/Wiki/note-hoisting)
* 无缝的 [笔记版本控制](https://triliumnext.github.io/Docs/Wiki/note-revisions)
* 笔记的 [属性](https://triliumnext.github.io/Docs/Wiki/attributes) 可用于笔记组织、查询和高级 [脚本](https://triliumnext.github.io/Docs/Wiki/scripts)
* 与自托管同步服务器的 [同步](https://triliumnext.github.io/Docs/Wiki/synchronization)
  * 有一个 [第三方服务托管同步服务器](https://trilium.cc/paid-hosting)
* 将笔记 [分享](https://triliumnext.github.io/Docs/Wiki/sharing)（发布）到公共互联网
* 强大的 [笔记加密](https://triliumnext.github.io/Docs/Wiki/protected-notes)，具有每个笔记的粒度
* 使用内置的 Excalidraw 绘制图表（笔记类型为 "canvas"）
* [关系图](https://triliumnext.github.io/Docs/Wiki/relation-map) 和 [链接图](https://triliumnext.github.io/Docs/Wiki/link-map) 用于可视化笔记及其关系
* [脚本](https://triliumnext.github.io/Docs/Wiki/scripts) - 请参见 [高级展示](https://triliumnext.github.io/Docs/Wiki/advanced-showcases)
* 用于自动化的 [REST API](https://triliumnext.github.io/Docs/Wiki/etapi)
* 可在可用性和性能上扩展到超过 100,000 条笔记
* 针对智能手机和平板电脑优化的触控 [移动前端](https://triliumnext.github.io/Docs/Wiki/mobile-frontend)
* [夜间主题](https://triliumnext.github.io/Docs/Wiki/themes)
* [Evernote](https://triliumnext.github.io/Docs/Wiki/evernote-import) 和 [Markdown 导入与导出](https://triliumnext.github.io/Docs/Wiki/markdown)
* [网络剪辑器](https://triliumnext.github.io/Docs/Wiki/web-clipper)，方便保存网页内容

## 安装

1. [将我的 Hass.io 附加组件仓库][repository] 添加到您的 Hass.io 实例。
1. 安装此附加组件。
1. 点击 `保存` 按钮以存储您的配置。
1. 启动附加组件，它会失败，这是正常的。
1. SSH 进入您的家庭助手并运行 `chmod 2777 /2effc9b9/trilliumnext`
1. 启动附加组件。
1. 检查附加组件的日志，以查看是否一切正常。
1. 转到您本地的 homeassistant IP:port 管理端口或入口。
1. 按说明操作。

```
port : 8000 #您要运行管理界面的端口。
```

Webui 可以在 `<your-ip>:port` 或入口处找到。

[repository]: https://github.com/jdeath/homeassistant-addons