# Ollama Addon for Home Assistant

请注意，此插件使用CPU加速或实验性Nvidia GPU支持运行（如果它对您有效，请报告！）。对于ROCm，支持仍然在等待中。

## 模型目录

默认情况下，所有下载的模型都存储在`/share/ollama`中。由于历史原因，您也可以将其配置为`/config/ollama`。请确保您有足够的空间可用。

## Ollama集成

要下载任何模型，请使用Ollama的API或与Home Assistant集成[Ollama](https://www.home-assistant.io/integrations/ollama/)：

[![添加Ollama集成](https://my.home-assistant.io/badges/brand.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=ollama)

使用以下数据：

- URL: `http://76e18fb5-ollama:11434`

如果您想更改模型，请删除集成（不是插件！）并重新启动集成配置过程。

## UI链接的说明

UI链接仅用于检查Ollama的API是否可用。官方Ollama镜像中没有包含聊天功能。