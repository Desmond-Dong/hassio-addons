ARG BUILD_FROM
FROM ${BUILD_FROM}

# Set shell
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install wyoming-whisper-cpp
WORKDIR /usr/src
ARG WYOMING_WHISPER_CPP_VERSION
ENV PIP_BREAK_SYSTEM_PACKAGES=1

RUN \
    apt-get update \
    && apt-get install -y --no-install-recommends \
        netcat-traditional \
        curl \
        python3 \
        python3-pip \
        build-essential \
    && curl -L -s \
        "https://ghfast.top/github.com/rhasspy/wyoming-whisper-cpp/archive/refs/tags/v${WYOMING_WHISPER_CPP_VERSION}.tar.gz" \
        | tar -zxvf - -C /tmp \
    && mv "/tmp/wyoming-whisper-cpp-${WYOMING_WHISPER_CPP_VERSION}" '/usr/share/wyoming-whisper-cpp' \
    && make -C "/usr/share/wyoming-whisper-cpp/whisper.cpp" main \
    && pip3 install --no-cache-dir -U \
        setuptools \
        wheel \
    && pip3 install --no-cache-dir \
        --extra-index-url https://www.piwheels.org/simple \
        -f . \
        "/usr/share/wyoming-whisper-cpp" \
    && apt-get purge -y --auto-remove \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /
COPY rootfs /

HEALTHCHECK --start-period=10m \
    CMD echo '{ "type": "describe" }' \
        | nc -w 1 localhost 10300 \
        | grep -iq "whisper" \
        || exit 1
