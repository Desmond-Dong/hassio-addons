# 使用固定的基础镜像
FROM docker.1ms.run/library/ubuntu:24.10

# 定义平台相关变量
ARG BUILD_ARCH
ENV BUILD_ARCH=$BUILD_ARCH
RUN apt update \
    && apt install -y --no-install-recommends wget ca-certificates 

RUN case "$BUILD_ARCH" in \
        "i386") \
            wget -q "https://dl.oray.com/hsk/linux/phddns_5.3.0_i386.deb";; \
        "amd64") \
            wget -q "https://dl.oray.com/hsk/linux/phddns_5.3.0_amd64.deb";; \
        *) \
            echo "Unsupported platform: $BUILD_ARCH" && exit 1 ;; \
    esac \
    && dpkg -i phddns*.deb \
    && apt clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && rm phddns*.deb

# 复制并设置运行脚本
COPY run.sh /run.sh
RUN chmod +x /run.sh

# 设置入口点
ENTRYPOINT ["/bin/sh", "/run.sh"]
