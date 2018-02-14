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
via the Status and Setting REST API.

Status and Settings REST API
This example shows using jq to preserve the existing settings and update the
SSL LDAP port to `3269`.

**Note:** The commands are run as root on the hub, and the hubs self signed
certificate is used to connect to the API over https. An accessToken must be
retrieved from /var/cfengine/httpd/htdocs/ldap/config/settings.php.

```console
[root@hub ~]# export CACERT="/var/cfengine/httpd/ssl/certs/hub.cert"
[root@hub ~]# export API="https://hub/ldap/settings"
[root@hub ~]# export AUTH_HEADER="Authorization:<accessToken from settings.php as mentioned above>"
[root@hub ~]# export CURL="curl --silent --cacert ${CACERT} -H ${AUTH_HEADER} ${API}"
[root@hub ~]# ${CURL} | jq '.data'
{
  "domain_controller": "ldap.jumpcloud.com",
  "custom_options": {
    "24582": 3
  },
  "version": 3,
  "group_attribute": "",
  "admin_password": "Password is set",
  "base_dn": "ou=Users,o=5888df27d70bea3032f68a88,dc=jumpcloud,dc=com",
  "login_attribute": "uid",
  "port": 2,
  "use_ssl": true,
  "use_tls": false,
  "timeout": 5,
  "ldap_filter": "(objectClass=inetOrgPerson)",
  "admin_username": "uid=missionportaltesting,ou=Users,o=5888df27d70bea3032f68a88,dc=jumpcloud,dc=com"
}

[root@hub ~]# ${CURL} -X PATCH -d '{"port":3269}'
{"success":true,"data":"Settings successfully saved."}
```
