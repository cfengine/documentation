---
layout: default
title: Custom SSL Certificate
published: true
tags: [cfengine enterprise, hub administration, SSL]
---

When first installed a self-signed ssl certificate is automatically generated
and used to secure Mission Portal and API communications. You can change this
certificate out with a custom one by replacing
`/var/cfengine/httpd/ssl/certs/<hostname>.cert` and
`/var/cfengine/httpd/ssl/private/<hostname>.cert` where hostname is the fully
qualified domain name of the host.

After installing the certificate please make sure that the certificate
at `/var/cfengine/httpd/ssl/certs/<hostname>.cert` is **world-readable on the hub**.
This is needed because the Mission Portal web application needs to access it directly.
You can test by verifying you can access the certificate with a unprivileged user account on the hub.

You can get the fully qualified hostname on your hub by running the following
commands.

```console
[root@hub ~]# cf-promises --show-vars=default:sys\.fqhost
default:sys.fqhost                       hub                                                          inventory,source=agent,attribute_name=Host name
```

```console
[root@hub ~]# hostname -f
hub
```
