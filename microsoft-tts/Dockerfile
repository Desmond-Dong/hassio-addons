ARG BUILD_FROM
FROM ${BUILD_FROM}
ARG BUILD_ARCH

COPY --from=ghcr.nju.edu.cn/astral-sh/uv:latest /uv /uvx /bin/

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install Microsoft-tts
WORKDIR /usr/src

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        netcat-traditional \
        curl 
        
# Copy files
WORKDIR /
COPY rootfs /
COPY pyproject.toml /

RUN uv sync

HEALTHCHECK --start-period=10m \
CMD echo '{ "type": "describe" }' \
    | nc -w 1 localhost 10200 \
    | grep -q "microsoft" \
    || exit 1
