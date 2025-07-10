FROM alpine:3.21.3

# Add env
ENV LANG C.UTF-8

# Setup base
RUN apk add --no-cache -U --virtual .build-deps \
        git \
 && apk add --no-cache -U aria2 darkhttpd jq \
 && mkdir /web \
 && git clone https://github.com/ziahamza/webui-aria2.git /tmp_webui \
 && mv /tmp_webui/docs/* /web \
 && rm -rf /tmp_web \
 && apk del .build-deps

COPY run.sh /

RUN chmod a+x /run.sh

CMD ["/bin/sh", "/run.sh"]


