#FROM $BUILD_FROM

FROM docker.1ms.run/library/python:3.13.3-alpine

#RUN apk add --no-cache python3 py-pip \
RUN python3 -m venv /opt/venv \
    && . /opt/venv/bin/activate \
    && /opt/venv/bin/python3 -m pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir websockets mcp-proxy

# 设置 PATH 环境变量，让系统识别虚拟环境中的 Python 和 pip
ENV PATH="/opt/venv/bin:$PATH" \
HA_MCP_ENDPOINT=http://homeassistant.local:8123/mcp_server/sse

# 复制脚本和配置文件
COPY mcp_pipe.py /mcp_pipe.py



# 设置容器启动时执行的入口点
CMD ["python", "/mcp_pipe.py"]
