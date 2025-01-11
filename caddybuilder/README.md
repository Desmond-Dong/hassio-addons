# Home assistant add-on: Caddy Builder

This will build a custom caddy binary for you.

The website (https://caddyserver.com/download) to download custom caddy binaries if often down or not working. This addon will run xcaddy and build a custom binary with whatever plugins you want.

Use the caddy2 homeassistant addon to run the custom caddy binary available at this repo: https://github.com/einschmidt/hassio-addons

Useage info for xcaddy can be found here: https://github.com/caddyserver/xcaddy

_Thanks to everyone having starred my repo! To star it click on the image below, then it will be on top right. Thanks!_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## About

This addon is based on the caddy-builder [docker image](https://hub.docker.com/_/caddy).

## Installation

1. [Add my Hass.io add-ons repository][repository] to your Hass.io instance.
1. Install this add-on.
1. Turn off "Start on Boot" switch
1. Click the `Save` button to store your configuration.
1. Run the addon once. It should fail, that is ok.
1. Copy the [xcaddyCommand.sh](https://raw.githubusercontent.com/jdeath/homeassistant-addons/main/caddybuilder/xcaddyCommand.sh) from this repo to /addon_configs/XXXXXX_caddybuilder (XXXXX is some string like 2effc9b9 and will be created by the previous step)
1. Edit the xcaddyCommand.sh to have the xcaddy command you want to run. Make sure all on one line. Review xcaddy documentation to add plugins.
1. Run the addon. A custom caddy binary should be built in /addon_configs/XXXXXX_caddybuilder/
1. May take a while, so refresh the logs to see if built correctly
1. Copy caddy binary to /share/caddy/
1. Restart [caddy2](https://github.com/einschmidt/hassio-addons) addon (not this addon) and it should use your new custom caddy binary

[repository]: https://github.com/jdeath/homeassistant-addons
