---
layout: default
title: Unable to log into Mission Portal
published: true
sorting: 90
tags: [getting started, installation, faq, Mission Portal]
---

## Mismatched names in SSL certificate

If your ssl certificate does not match the name used to access Mission Portal the api will not be able to authenticate and you will not be able to log in.

Verify the name used to access mission portal resolves correctly:

* `/etc/hosts` contains a proper entry with the fqdn used to access Mission
  Portal listed in the second column.

```
192.168.56.1 hub.cfengine.com hub
```

* `hostname -f` returns the fqdn used to access Mission Portal.
* `hostname -s` returns the short hostname

## Mis-aligned oauth configuration

The API uses oauth internally to authenticate. Verify that `client_secret` for
`client_id` `MP` matches `$config['MP_CLIENT_SECRET']` in
`/var/cfengine/share/GUI/application/config/appsettings.php` and
`$config['encryption_key']` in
`/var/cfengine/share/GUI/application/config/config.php`.

Get `MP` `client_secret`:

```console
[root@hub ~]# psql cfsettings -c "SELECT client_secret from oauth_clients where client_id = 'MP'";
          client_secret           
----------------------------------
 aUI2sAtrPpr1dmwZDCVuKONnMXHYHDLB
(1 row)
```

Get `$config['MP_CLIENT_SECRET']` in
`/var/cfengine/share/GUI/application/config/appsettings.php`:

```console
[root@hub ~]# grep MP_CLIENT_SECRET /var/cfengine/share/GUI/application/config/appsettings.php
$config['MP_CLIENT_SECRET'] = 'aUI2sAtrPpr1dmwZDCVuKONnMXHYHDLB';
```

Get `$config['encryption_key']` in
`/var/cfengine/share/GUI/application/config/config.php`.

```console
[root@hub ~]# grep encryption_key /var/cfengine/share/GUI/application/config/config.php
$config['encryption_key'] = 'aUI2sAtrPpr1dmwZDCVuKONnMXHYHDLB';
```

Correct any mis-matches and run the policy to sync the application config and
try to log into Mission Portal.

```console
[root@hub ~]# cf-agent -Kf update.cf; cf-agent -KI
    info: Updated '/var/cfengine/httpd/htdocs/application/config/config.php' from source '/var/cfengine/share/GUI/application/config/config.php' on 'localhost'
```

