# 使用指定的基础镜像
FROM alpine:3.21.3

# 定义构建参数
ARG BUILD_ARCH

# 安装所需软件
RUN apk add --no-cache wget unzip gcompat

# 设置工作目录
WORKDIR /tmp

# 根据架构下载对应文件
RUN echo ">>> BUILD_ARCH is [$BUILD_ARCH]" && \
    case "$BUILD_ARCH" in \
    amd64) wget -O owjdxb.zip https://raw.githubusercontent.com/desmond-dong/hassio-addons/main/jdxb/owjdxb_x86.zip ;; \
    arm64|aarch64) wget -O owjdxb.zip https://raw.githubusercontent.com/desmond-dong/hassio-addons/main/jdxb/owjdxb_a64.zip ;; \
    *) echo "❌ Unsupported architecture: [$BUILD_ARCH]" && exit 1 ;; \
    esac && \
    unzip owjdxb.zip && \
    mv owjdxb /owjdxb && \
    chmod +x "/owjdxb/bin/owjdxb" && \
    rm -rf /tmp/*


# 复制并设置 run.sh 脚本
COPY run.sh /run.sh
RUN chmod +x /run.sh

# 设置入口点
ENTRYPOINT ["/bin/sh", "/run.sh"]
