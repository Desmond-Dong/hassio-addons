ARG BUILD_FROM
FROM ${BUILD_FROM}

COPY rootfs /
RUN chmod +x /k2fsa/*.sh

WORKDIR /k2fsa

# 使用 USTC 镜像加速 apt，安装必要工具，执行后立即清理
RUN sed -i 's@/archive.ubuntu.com/@/mirrors.ustc.edu.cn/@g' /etc/apt/sources.list && \
    sed -i 's@/security.ubuntu.com/@/mirrors.ustc.edu.cn/@g' /etc/apt/sources.list && \
    apt update && \
    apt install -y --no-install-recommends wget bzip2 && \
    if [ "$(uname -m)" = "x86_64" ]; then \
        wget -q -O sherpa-onnx.tar.bz2 https://github.com/k2-fsa/sherpa-onnx/releases/download/v1.11.5/sherpa-onnx-v1.11.5-linux-x64-static.tar.bz2 --no-check-certificate; \
    elif [ "$(uname -m)" = "aarch64" ]; then \
        wget -q -O sherpa-onnx.tar.bz2 https://github.com/k2-fsa/sherpa-onnx/releases/download/v1.11.5/sherpa-onnx-v1.11.5-linux-aarch64-static.tar.bz2 --no-check-certificate; \
    fi && \
    tar -xjf sherpa-onnx.tar.bz2 --strip-components=1 -C /k2fsa/ && \
    chmod +x /k2fsa/bin/* && \
    rm -rf /k2fsa/include && \
    rm -rf /k2fsa/lib && \
    rm -rf /k2fsa/bin/*online* && \
    rm -rrf /k2fsa/bin/*vad* && \
    rm -rf /k2fsa/bin/*tts* && \
    rm -rf /k2fsa/bin/*microphone* && \
    rm -rf /k2fsa/bin/*keyword* && \
    rm -rf /k2fsa/bin/*alsa* && \
    rm -rf /k2fsa/bin/*para* && \
    rm -rf /k2fsa/bin/*audio* && \
    rm -rf /k2fsa/bin/*language* && \
    rm -rf sherpa-onnx.tar.bz2 && \
    apt autoremove -y && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

CMD [ "/k2fsa/init.sh" ]


#https://github.com/k2-fsa/sherpa-onnx/releases/download/v1.11.5/sherpa-onnx-v1.11.5-linux-aarch64-static.tar.bz2
#https://github.com/k2-fsa/sherpa-onnx/releases/download/v1.11.5/sherpa-onnx-v1.11.5-linux-x64-static.tar.bz2