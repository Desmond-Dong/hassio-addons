ARG BUILD_FROM

FROM victoriametrics/victoria-metrics:v1.119.0 as victoriametrics-server
FROM victoriametrics/vmagent:v1.119.0 as victoriametrics-agent
FROM ${BUILD_FROM} AS final

COPY rootfs /
COPY --from=victoriametrics-server /victoria-metrics-prod /usr/local/bin/victoria-metrics-prod
COPY --from=victoriametrics-agent /vmagent-prod /usr/local/bin/vmagent-prod
