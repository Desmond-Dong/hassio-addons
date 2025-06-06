# syntax=docker/dockerfile:1
#
# DEV MASS image: base image + MASS installed from prebuilt wheel
#
FROM ghcr.nju.edu.cn/music-assistant/base:latest

ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# ensure UV is installed
COPY --from=ghcr.nju.edu.cn/astral-sh/uv:latest /uv /uvx /bin/

# add some additional packages that are useful for debugging
RUN set -x \
    && apk update \
    && apk add -f jq htop git && \
    # pre-install base requirements to save a bit of startup time
    uv venv $VIRTUAL_ENV && \
    uv pip install \
    --no-cache \
    --link-mode=copy \
    -r "https://raw.githubusercontent.com/music-assistant/server/refs/heads/dev/requirements_all.txt"

VOLUME [ "/data" ]
EXPOSE 8095

RUN chmod 777 -R /app && \
    chmod 777 -R /tmp

COPY entrypoint.sh /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
