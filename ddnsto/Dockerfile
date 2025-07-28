# 使用基础镜像
FROM alpine:3.21.3

COPY run.sh /run.sh
RUN chmod a+x /run.sh

RUN apk add --no-cache \
    jq \
    curl \
    && rm -rf /var/cache/apk/*
# 设置容器启动时执行的命令
ENTRYPOINT ["/bin/sh", "/run.sh"]
