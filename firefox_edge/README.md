# Home Assistant 添加组件：Firefox (Edge)

在 Home Assistant 内部以浏览器的形式运行 Firefox，以便从家中访问本地或外部网站。

![支持 aarch64 架构][aarch64-shield]
![支持 amd64 架构][amd64-shield]
![支持 armv7 架构][armv7-shield]
![支持 i386 架构][i386-shield]

## 关于

Mozilla Firefox 是由 Mozilla 基金会和其子公司 Mozilla 公司开发的一款免费开源网络浏览器。

此添加组件基于 [docker 镜像](https://github.com/jlesage/docker-firefox) 由 [Jocelyn Le Sage](https://github.com/jlesage) 提供。

非常感谢他为创建和维护出色的容器所做的贡献。
他是需要被 [支持](https://github.com/sponsors/jlesage) 的真正英雄。

## 与原始容器的差异

有一些差异是为了使此容器作为添加组件工作而必需的，或者只是基于我的个人偏好所做的调整：

- Edge 版本：此容器不是基于 Alpine **稳定版**，而是基于 Alpine **边缘版**。主要原因是利用可用的最新 Firefox 版本。在启动时，容器可能在日志中显示较旧版本的 Firefox，可以忽略。它尝试在每次容器启动时更新 Firefox。
- 为了使其与 Home Assistant 持久化兼容，我需要重新映射文件夹，为此，启动脚本以 `root` 身份运行。我将在未来尽量避免这种情况。

## 如何使用

只需安装，启动容器，然后点击“打开 Web UI”。您可以使用“在侧边栏中显示”以方便访问。您在 Firefox 中所做的所有操作都会被持久化。即使您停止添加组件或重新启动 Home Assistant 主机操作系统。

## 下载

在 Firefox 中下载的文件将自动存储到您的 `/share/firefox` 文件夹中。

## 上传

如果您需要通过 Firefox 添加组件上传文件，您可以使用 [文件编辑器添加组件](https://github.com/home-assistant/addons/blob/master/configurator/) 将文件上传到您的 `/share/firefox` 文件夹。
文件将在添加组件的 `downloads` 文件夹中可用。您可以在选择要上传的文件时浏览到此位置。

## 导入书签

您可以通过将它们放入您的 `/share/firefox` 文件夹中导入 `bookmarks.html` 文件，并在 Firefox 中导入 `bookmarks.html` 文件。

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg