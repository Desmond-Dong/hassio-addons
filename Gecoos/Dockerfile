FROM docker.1ms.run/library/alpine:3.21
ARG BUILD_ARCH
ENV BUILD_ARCH=$BUILD_ARCH
RUN apk add --no-cache wget jq bash

# Download the file using the passed URL
RUN case $BUILD_ARCH in \
    amd64) wget -O /ac "http://file.cnrouter.com/upload/gac/%E5%90%AB%E7%99%BB%E5%BD%95%E9%A1%B5%E9%9D%A2%E7%89%88%E6%9C%AC%EF%BC%88%E4%B8%BB%E8%A6%81%E7%94%A8%E4%BA%8E%E7%8B%AC%E7%AB%8B%E4%BD%BF%E7%94%A8%EF%BC%89/ac_linux_amd64_V2.2_202501031919" && chmod +x /ac ;; \
    aarch64) wget -O /ac "http://file.cnrouter.com/upload/gac/%E5%90%AB%E7%99%BB%E5%BD%95%E9%A1%B5%E9%9D%A2%E7%89%88%E6%9C%AC%EF%BC%88%E4%B8%BB%E8%A6%81%E7%94%A8%E4%BA%8E%E7%8B%AC%E7%AB%8B%E4%BD%BF%E7%94%A8%EF%BC%89/ac_linux_arm64_V2.2_202501031919" && chmod +x /ac ;; \
    armhf) wget -O /ac "http://file.cnrouter.com/upload/gac/%E5%90%AB%E7%99%BB%E5%BD%95%E9%A1%B5%E9%9D%A2%E7%89%88%E6%9C%AC%EF%BC%88%E4%B8%BB%E8%A6%81%E7%94%A8%E4%BA%8E%E7%8B%AC%E7%AB%8B%E4%BD%BF%E7%94%A8%EF%BC%89/ac_linux_arm_V2.2_202501031919" && chmod +x /ac ;; \
    armv7) wget -O /ac "http://file.cnrouter.com/upload/gac/%E5%90%AB%E7%99%BB%E5%BD%95%E9%A1%B5%E9%9D%A2%E7%89%88%E6%9C%AC%EF%BC%88%E4%B8%BB%E8%A6%81%E7%94%A8%E4%BA%8E%E7%8B%AC%E7%AB%8B%E4%BD%BF%E7%94%A8%EF%BC%89/ac_linux_arm_V2.2_202501031919" && chmod +x /ac ;; \
    i386) wget -O /ac "http://file.cnrouter.com/upload/gac/%E5%90%AB%E7%99%BB%E5%BD%95%E9%A1%B5%E9%9D%A2%E7%89%88%E6%9C%AC%EF%BC%88%E4%B8%BB%E8%A6%81%E7%94%A8%E4%BA%8E%E7%8B%AC%E7%AB%8B%E4%BD%BF%E7%94%A8%EF%BC%89/ac_linux_386_V2.2_202501031919" && chmod +x /ac ;; \
    *) echo "Unsupported architecture $BUILD_ARCH" && exit 1 ;; \
    esac && \
    chmod +x /ac

# Copy and prepare the run script
COPY run.sh /run.sh
RUN chmod +x /run.sh

# Set default command
CMD ["/run.sh"]
