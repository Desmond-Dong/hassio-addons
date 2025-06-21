ARG BUILD_FROM

FROM grafana/loki:3.5.1 as loki-base
FROM ${BUILD_FROM} AS final

COPY rootfs /
COPY --from=loki-base /usr/bin/loki /usr/bin/loki

RUN apk add --no-cache gomplate

RUN adduser -g "loki" --home /data/loki --disabled-password loki
