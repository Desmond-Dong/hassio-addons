FROM alpine:3.21.0


ENV NODE_ENV=production


RUN apk add --no-cache nodejs npm \
    && npm install -g musicn \
    && npm cache clean --force

# 设置工作目录（可选）
WORKDIR /app

# 默认运行命令
ENTRYPOINT [ "/usr/local/bin/msc", "-q" ]