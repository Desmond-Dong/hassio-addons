# Start of Selection
FROM docker.1ms.run/library/python:3.13.5-alpine3.22

# 设置时区为上海
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone \
    && python3 -m venv /opt/venv \
    && . /opt/venv/bin/activate \
    && /opt/venv/bin/python3 -m pip install --upgrade pip \
    && pip install --no-cache-dir paho-mqtt requests

ENV PATH="/opt/venv/bin:$PATH"
ENV LANG=C.UTF-8
COPY EZVIZ.py /EZVIZ.py
#WORKDIR /opt/venv

# 设置容器启动时执行的入口点
# Start of Selection
CMD ["python", "/EZVIZ.py"]
