ARG BUILD_FROM
#FROM python:3.12-slim
FROM docker.1ms.run/python:slim

ARG CHROME_VERSION="127.0.6533.119-1"
ARG CHROME_VERSION="128.0.6613.119-1"
ARG CHROME_VERSION="129.0.6668.100-1"
ARG CHROME_VERSION="130.0.6723.91-1"
ARG CHROME_VERSION="131.0.6778.85-1"
ARG CHROME_VERSION="132.0.6834.159-1"

# Chrome Stable, but 127 works better
# https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

RUN apt-get update -y && \
	apt-get install -y git wget xvfb jq --no-install-recommends && \
	wget -O /tmp/chrome.deb https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}_amd64.deb && \
	apt-get install -y --no-install-recommends /tmp/chrome.deb && \
	rm /tmp/chrome.deb && \
	google-chrome --version && \
	mkdir /app && cd /app && \
	#git clone --depth=1 https://ghfast.top/github.com/jdeath/MS-Rewards-Farmer.git ./ && \
	#git clone --depth=1 -b develop https://ghfast.top/github.com/jdeath/MS-Rewards-Farmer.git ./ && \
	git clone --depth=1 -b develop https://ghfast.top/github.com/klept0/MS-Rewards-Farmer.git ./ && \
	#git clone --depth=1 -b 30012025-DEV https://ghfast.top/github.com/Rippenkneifer/M------F.git ./ && \
	sed -i 's/Path(__file__).parent.parent/Path.cwd()/g' src/utils.py && \
	sed -i 's/\bdriver.close()\b//g' src/*.py && \
	sed -i 's/self.webdriver.close()//g' src/*.py && \
	sed -i 's/sleep(randint(300, 600))/sleep(randint(120, 300))/g' src/*.py && \
	#sed -i 's/, 5/, 30/g' src/activities.py && \
	#sed -i 's/timeToWait=20/timeToWait=60/g' src/*.py && \
	#sed -i 's/WebDriverWait(self.webdriver, 10)/WebDriverWait(self.webdriver, 20)/g' src/*.py && \
	sed -i 's/timeToWait=40/timeToWait=80/g' src/*.py && \
	sed -i 's/float = 10/float = 30/g' src/utils.py && \
	#sed -i 's/WebDriverWait(self.webdriver, 20)/WebDriverWait(self.webdriver, 60)/g' src/*.py && \
	#sed -i 's/product["Product"]/product["product"]/g' src/userAgentGenerator.py && \
	pip install --no-cache-dir --root-user-action=ignore -r requirements.txt && \
	pip install --no-cache-dir --root-user-action=ignore --upgrade -r requirements.txt

# setting display environment stuff
ENV DISPLAY=:99
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null

WORKDIR /app
COPY run.sh ./
COPY entrypoint.sh ./
RUN chmod a+x ./*.sh

ENTRYPOINT [ "/app/entrypoint.sh" ]
CMD ["/app/run.sh"]

### LABELS
ARG BUILD_ARCH
ARG BUILD_DATE
ARG BUILD_DESCRIPTION
ARG BUILD_NAME
ARG BUILD_REF
ARG BUILD_REPOSITORY
ARG BUILD_VERSION
LABEL \
    io.hass.name="${BUILD_NAME}" \
    io.hass.description="${BUILD_DESCRIPTION}" \
    io.hass.arch="${BUILD_ARCH}" \
    io.hass.type="addon" \
    io.hass.version=${BUILD_VERSION} \
    maintainer="jdeath (https://ghfast.top/github.com/jdeath)" \
    org.opencontainers.image.title="${BUILD_NAME}" \
    org.opencontainers.image.description="${BUILD_DESCRIPTION}" \
    org.opencontainers.image.vendor="Home Assistant Add-ons" \
    org.opencontainers.image.authors="jdeath (https://ghfast.top/github.com/jdeath)" \
    org.opencontainers.image.licenses="MIT" \
    org.opencontainers.image.url="https://ghfast.top/github.com/jdeath" \
    org.opencontainers.image.source="https://ghfast.top/github.com/${BUILD_REPOSITORY}" \
    org.opencontainers.image.documentation="https://ghfast.top/github.com/${BUILD_REPOSITORY}/blob/main/README.md" \
    org.opencontainers.image.created=${BUILD_DATE} \
    org.opencontainers.image.revision=${BUILD_REF} \
    org.opencontainers.image.version=${BUILD_VERSION}