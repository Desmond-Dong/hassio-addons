# Home Assistant Add-on: Mailserver

Postfix/Dovecot mailserver with Postfixadmin web interface...

![Supports aarch64 Architecture][aarch64-shield] ![Supports amd64 Architecture][amd64-shield]
![Supports armv7 Architecture][armv7-shield] ![Supports i386 Architecture][i386-shield]

## About

Important: This addon requires that the MariaDB add-on is installed and running!

This add-on is experimental, and provides a mailserver for your domain.
It is also possible to configure additional email domains and accounts in the
Postfix Admin web interface.

The following ports are used by this addon:

smtp: port 25, 465 and 587
imap(s): 993
managesieve: 4190
(ManageSieve enables users to create their own Sieve scripts with a
mail client that supports the Sieve protocol)

Is is possible to change these in the Network section of the configuration.

A note on port 465: While it was once the standard for secure SMTP submissions,
it has been superseded by port 587. Although port 465 is still supported by some
older email systems and clients, most modern setups now use port 587, as it is
considered more robust and flexible.

If you are brave, you may want to expose the mail server to Internet.
See intructions below:

To recieve mail from the Internet, the SMTP ports have to be added for redirection
in your router, except for port 465 (See the note above regarding port 465).
The necessary MX and A records will have to be registered in DNS.
If you want to be able to check emails from outside of your network the IMAP port
will also have to be forwarded.

The default setup will use self signed certificates created by Dovecot during
the initial setup. It is OK for testing, but "real" certificates should be used.

The config option "letsencrypt_certs" will, is set to "true", use the
fullchain.pem and privkey.pem in the /ssl directory in Home Assistant.

## Installation

Follow these steps to get the add-on installed on your system:

Add the repository `https://github.com/erik73/hassio-addons`.
Find the "Mailserver" add-on and click it.
Click on the "INSTALL" button.

## How to use

### Starting the add-on

After installation you are presented with a default and example configuration.

Adjust the add-on configuration to match your requirements.
Save the add-on configuration by clicking the "SAVE" button.
Start the add-on.

## Configuration

Example configuration:

```yaml
my_hostname: mydomain.no-ip.com
domain_name: mydomain.no-ip.com
admin_user: admin
admin_password: admin
letsencrypt_certs: false
enable_mailfilter: false
message_size_limit: 10
```

Please note: During the startup of the add-on, a database is created in the
MariaDB add-on. There is currently not possible to change user name or
domain_name after the database is created. The password can be changed.
The only way to change user and domain name is to drop the Postfix Admin
datbase and restart the add-on.
Use the phpMyadmin add-on to drop the database.

### Option: `my_hostname` (required)

The hostname of your mailserver. It should correspond to the A-record you
have in your DNS.

#### Option: `domain_name` (required)

This is the name of the domain you want to recieve mail from.
Additional domains can be added in the postfixadmin-interface.

#### Option: `admin_user` (required)

The name of the admin user in postfixadmin. To log in to the web interface
you have to use FQDN. For example: admin@mydomain.no-ip.com.
In the current version of the add-on, this can not be changed once the database
is created.

#### Option: `admin_password` (required)

The password for the admin_user.
This option can be changed after initial install. A handy feature if you forget
your password!

#### Option: `letsencrypt_certs` (required)

If you use the Let´s Encrypt add-on or by any other means have certs
installed in the /ssl folder of your HA instance, this options will
use those certificates for the SMTP and IMAP services.

The files should be named fullchain.pem and privkey.pem.

#### Option: `message_size_limit` (required)

Configures the max size of a single message/mail in MB.
Messages larger than this will get rejected.
If you want the best compatibility with common cloud mail providers, use 50 MB.
Default: 10

#### Option: `enable_mailfilter` (required)

This enables communication with the optional Mailfilter add-on in this repository.
It will enable Postfix to scan emails for SPAM and viruses, and includes optional
DKIM signing. To be able to successfully send email from your host, without risking
having your outgoing emails being rejected or classified as spam, DKIM signing
is a must. You also have to configure your DNS server to provide SPF and DMARC.
If DKIM, SPF and DMARC sounds too complicated, use the smtp_relay option.

The virus scanning requires a lot of memory, and 4-8 GB is recommended.
Virus scanning is disabled by default in the Mailfilter add-on.

#### Option: `smtp_relayhost` (optional)

Use this optional setting to use a relay server for outgoing emails. ISP:s often
block outgoing emails from your network. In that case, you can use your
ISP:s SMTP relay host to bypass this limitation.
It is good practice to enter the hostname within brackets. It disables MX
lookups for that host, and is recommended. You can also specify a port to use.
For example:

```yaml
[smtp.relay.com]:587
```

The above example means port 587 is used for submission.
If your ISP requires a username and password, use the option below.

#### Option: `smtp_relayhost_credentials` (optional)

Use this optional setting to use authentication with the relay server you specified.
The correct syntax is username:password and you get this info from your provider.
Only use this option if you know user credentials are really needed to relay.

#### Option: `mynetworks` (optional)

Use this optional setting if you want to allow specific networks or IP
addresses to relay email through this server. This option should only be
used for internal networks or hosts. Before using it, be sure to read the Postfix
documentation to understand the security implications of setting this option.

```yaml
192.168.1.0/24 192.168.3.12
```

## Support

Got questions?

You could [open an issue here][issue] GitHub.

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
[issue]: https://github.com/erik73/addon-mail/issues
[repository]: https://github.com/erik73/hassio-addons
