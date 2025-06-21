ARG BUILD_FROM

FROM ghcr.nju.edu.cn/unpoller/unpoller:v2.15.3 as unpoller-base
FROM ${BUILD_FROM} AS final

COPY rootfs /
COPY --from=unpoller-base /usr/bin/unpoller /usr/local/bin/unpoller
COPY --from=unpoller-base /etc/unpoller/up.conf /etc/unpoller/up.conf

RUN apk add --no-cache gomplate
