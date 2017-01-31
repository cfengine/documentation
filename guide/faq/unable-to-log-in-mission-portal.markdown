---
layout: default
title: Unable to log into Mission Portal
published: true
sorting: 90
tags: [getting started, installation, faq, Mission Portal]
---

Problems logging into Mission Portal can usually be traced to mis-matched names
in SSL Certificates.

If you are having issues logging into Mission Portal please verify the following
configuration:

* `/etc/hosts` contains a proper entry with the fqdn used to access Mission
  Portal listed in the second column.

```
192.168.33.1 hub.cfengine.com hub
```

* `hostname -f` returns the fqdn used to access Mission Portal.
* `hostname -s` returns the short hostname
