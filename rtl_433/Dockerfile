ARG BUILD_FROM
FROM $BUILD_FROM as builder
MAINTAINER koying@spax.pm

ENV LANG C.UTF-8

# Copied with minor edits from https://ghfast.top/github.com/hertzg/rtl_433_docker/blob/master/images/alpine/build-context/Dockerfile
RUN apk add --no-cache --virtual .buildDeps \
    build-base \
    libusb-dev \
    librtlsdr-dev \
    cmake \
    git

WORKDIR /build

RUN git clone https://ghfast.top/github.com/koying/rtl_433
WORKDIR ./rtl_433

# Build a specific commit or tag.
ARG GitRevision=master
RUN git checkout ${GitRevision}
WORKDIR ./build
RUN cmake ..
RUN make -j 4

WORKDIR /build/root
WORKDIR /build/rtl_433/build
RUN make DESTDIR=/build/root/ install

FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apk add --no-cache libusb \
    librtlsdr \
    sed
WORKDIR /root
COPY --from=builder /build/root/ /

# Run script
COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
