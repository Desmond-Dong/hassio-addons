# Ollama 插件用于家庭助理

请注意，此插件通过 CPU 加速或实验性 Nvidia GPU 支持运行（如果对您有效，请反馈！）。ROCm 的支持仍在待定中。

## 模型目录

所有下载的模型默认存储在 `/share/ollama`。出于历史原因，您也可以将其配置为 `/config/ollama`。请确保您有足够的可用空间。

## Ollama 集成

要下载任何模型，可以使用 Ollama 的 API 或与家庭助理集成 [Ollama](https://www.home-assistant.io/integrations/ollama/)：

[![添加 Ollama 集成](https://my.home-assistant.io/badges/brand.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=ollama)

使用以下数据：

- URL: `http://76e18fb5-ollama:11434`

如果您想更改模型，请删除集成（而不是插件！）并重新启动集成的配置过程。

## 关于 UI 链接的说明

UI 链接仅用于检查 Ollama 的 API 是否可用。官方镜像中不包含聊天功能。