# Ollama 扩展程序 for Home Assistant

请注意，此扩展程序使用 CPU 加速或实验性 Nvidia GPU 支持（如果它对您有效，请报告！）对于 ROCm 的支持仍然悬而未决。

## 模型目录

默认情况下，所有下载的模型都存储在 `/share/ollama` 中。由于历史原因，您也可以将其配置为 `/config/ollama`。请确保您有足够的空间可用。

## Ollama 集成

要下载任何模型，请使用 Ollama 的 API 或与 Home Assistant 集成 [Ollama](https://www.home-assistant.io/integrations/ollama/)：

[![添加 Ollama 集成](https://my.home-assistant.io/badges/brand.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=ollama)

使用以下数据：

- URL: `http://76e18fb5-ollama:11434`

如果您想更改模型，请删除集成（不是扩展程序！）并重新启动集成配置的过程。

## UI 链接的说明

UI 链接仅用于检查 ollama 的 API 是否可用。官方 ollama 图像中不包含聊天功能。