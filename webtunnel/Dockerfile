# 使用指定的基础镜像
FROM alpine:3.21.2
ARG BUILD_ARCH
# 安装所需软件
RUN apk add --no-cache wget tar libstdc++ libgcc libc6-compat


# 设置工作目录
WORKDIR /tmp

# 根据架构下载对应文件
RUN case "$BUILD_ARCH" in \
    amd64) wget -O WebTunnelCore.tar.gz https://w.pgrm.top/download/linux/WebTunnelCore-linux-x64-250612.tar.gz ;; \
    aarch64) wget -O WebTunnelCore.tar.gz https://w.pgrm.top/download/linux/WebTunnelCore-linux-arm64-250612.tar.gz ;; \
    *) echo "Unsupported architecture $BUILD_ARCH" && exit 1 ;; \
    esac && \
    tar -xzvf WebTunnelCore.tar.gz -C / && \
    chmod +x "/WebTunnelCore" \
    && rm -rf /tmp/*

    
# 设置入口点
ENTRYPOINT ["/WebTunnelCore", "--config=/data/.webtunnel"]