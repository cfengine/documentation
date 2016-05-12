---
layout: default
title: Configure a custom LDAP port
published: true
tags: [cfengine enterprise, hub administration, ldap]
---

Mission Portals User settings and preferences provides a radio button
encryption. This controls the encryption and the port to connect to.

![Ldap Settings](custom-ldap-port-settings.png)

If you want to configure LDAP authentication to use a custom port you can do so
via the [Status and Setting REST API][API].

This example shows using jq to preserve the existing settings and update the
LDAP port to =3268= and the LDAP SSL port to =3269=.

**Note:** The commands are run as root on the hub, and the hubs self signed
certificate is used to connect to the API over https. Authentication is done via
a `~/.netrc` file as indicated by the `--netrc` option.

```console
[root@hub ~]# export CURL="curl --netrc --silent --cacert /var/cfengine/httpd/ssl/certs/hub.cert https://hub/api/settings "
[root@hub ~]# ${CURL} | jq '.data[0] + {"ldapPort": 3268, "ldapPortSSL": 3269}' | ${CURL} -X POST -d @-
[root@hub ~]# curl --netrc --silent --cacert /var/cfengine/httpd/ssl/certs/hub.cert https://hub/api/settings^C
[root@hub ~]# $CURL | jq '.data[0]'
{
  "blueHostHorizon": 900,
  "hostIdentifier": "default.sys.fqhost",
  "ldapBaseDN": "dc=cfengine,dc=com",
  "ldapEnabled": true,
  "ldapEncryption": "ssl",
  "ldapFilter": "(objectClass=inetOrgPerson)",
  "ldapHost": "ldap.intra.cfengine.com",
  "ldapLoginAttribute": "uid",
  "ldapPassword": "",
  "ldapPort": 3268,
  "ldapPortSSL": 3269,
  "ldapUsername": "",
  "logLevel": "error",
  "rbacEnabled": true,
  "sketchActivationAlertTimeout": 60
}
```
