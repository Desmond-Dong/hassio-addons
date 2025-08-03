# Home Assistant Add-on: Firefox

在 Home Assistant 中运行 Firefox 作为浏览器，以从家中访问本地或外部网站。

![支持 aarch64 架构][aarch64-shield]
![支持 amd64 架构][amd64-shield]
![支持 armv7 架构][armv7-shield]
![支持 i386 架构][i386-shield]

## 关于

Mozilla Firefox 是由 Mozilla 基金会和其子公司 Mozilla Corporation 开发的免费和开源的网页浏览器。

此插件基于 [docker 镜像](https://github.com/jlesage/docker-firefox) 来自 [Jocelyn Le Sage](https://github.com/jlesage)。

非常感谢他创建了并维护了这些优秀的容器。
他是需要被 [支持](https://github.com/sponsors/jlesage) 的真正英雄。

## 与原始容器的区别

为了使其与 Home Assistant 持久化兼容，我需要重新映射文件夹，为此，启动脚本以 `root` 用户运行。我将在未来尽量避免这种情况。

## 如何使用

只需安装，启动容器，然后点击“打开 Web UI”。您可以使用“在侧边栏中显示”以方便访问。您在 Firefox 中所做的所有操作都会被持久化。即使您停止插件或重新启动 Home Assistant 主机操作系统。

## 下载

在 Firefox 中下载的文件会自动存储到您的 `/share/firefox` 文件夹中。

## 上传

如果您需要通过 Firefox 插件上传文件，您可以使用 [文件编辑器插件](https://github.com/home-assistant/addons/blob/master/configurator/) 将文件上传到您的 `/share/firefox` 文件夹。
文件将在插件的 `downloads` 文件夹中可用。当您选择要上传的文件时，您可以浏览到此位置。

## 导入书签

您可以通过将文件拖放到您的 `/share/firefox` 文件夹中来导入 `bookmarks.html` 文件，并在 Firefox 中导入 `bookmarks.html` 文件。

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg