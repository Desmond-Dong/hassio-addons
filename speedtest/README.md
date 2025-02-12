# Home assistant add-on: Speedtest

A self-hosted, lightweight speed test implemented in JavaScript, and based on Web Workers and XMLHttpRequest.
 
_Thanks to everyone having starred my repo! To star it click on the image below, then it will be on top right. Thanks!_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## About

This addon is based on the [docker image](https://hub.docker.com/r/e7db/speedtest) . A self-hosted, lightweight speed test implemented in JavaScript 

## Installation

The installation of this add-on is pretty straightforward and not different in
comparison to installing any other Hass.io add-on.

1. [Add my Hass.io add-ons repository][repository] to your Hass.io instance.
1. Install this add-on.
1. Click the `Save` button to store your configuration.
1. Start the add-on.
1. Check the logs of the add-on to see if everything went well.
1. Open WebUI will not work if reverse proxy, go to your local homeassistant IP:port admin port.
1. Consult official docs for setup support: https://hub.docker.com/r/e7db/speedtest

## Configuration

```
port: 89 # port you want to run frontend on
```

Webui can be found at `<your-ip>:port`.

[repository]: https://github.com/jdeath/homeassistant-addons
