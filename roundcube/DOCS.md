# Home Assistant Add-on: Roundcube

Roundcube web based email client.

![Supports aarch64 Architecture][aarch64-shield] ![Supports amd64 Architecture][amd64-shield]
![Supports armv7 Architecture][armv7-shield]

## About

Important: This addon requires that the MariaDB add-on is installed and running!

This add-on is experimental, and provides a webmail frontend that connects
to the Mailserver add-on. It also enables you to configure Sieve scripts
for your mailbox.

The following ports are used by this addon:

http or https: 2665

Is is possible to change this in the Network section of the configuration.

If you are brave, you may want to expose Roundcube to the Internet by forwarding
port 2665 in your router. Don´t even consider this unless you have enabled SSL!

You reach the Roundcube interface by clicking the Web UI button in the add-on
page. You can also point your browser to: http://{homeassistant IP}:2665 or
if you enable the SSL option it is http://{homeassistant IP}:2665. It is also
possible to use the hostname insted of IP address.

## Installation

Follow these steps to get the add-on installed on your system:

Add the repository `https://github.com/erik73/hassio-addons`.
Find the "Roundcube" add-on and click it.
Click on the "INSTALL" button.

## How to use

### Starting the add-on

After installation you are presented with a default and example configuration.

Adjust the add-on configuration to match your requirements.
Save the add-on configuration by clicking the "SAVE" button.
Start the add-on.

## Configuration

Please note: During the startup of the add-on, a database is created in the
MariaDB add-on.

### Option: `ssl`

Enables/Disables SSL (HTTPS) on the web interface of Roundcube
Set it `true` to enable it, `false` otherwise.

### Option: `certfile`

The certificate file to use for SSL.

**Note**: _The file MUST be stored in `/ssl/`, which is the default_

### Option: `keyfile`

The private key file to use for SSL.

**Note**: _The file MUST be stored in `/ssl/`, which is the default_

## Support

Got questions?

You could [open an issue here][issue] GitHub.

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[issue]: https://github.com/erik73/addon-roundcube/issues
[repository]: https://github.com/erik73/hassio-addons
