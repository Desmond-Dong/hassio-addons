# 使用基础镜像
FROM easytier:v2.3.2

COPY run.sh /run.sh
RUN chmod a+x /run.sh

RUN apk add --no-cache jq
# 设置容器启动时执行的命令
ENTRYPOINT ["/bin/sh", "/run.sh"]
