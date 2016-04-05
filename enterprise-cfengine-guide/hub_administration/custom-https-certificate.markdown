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

You can get the fully qualified hostname on your hub by running the following
commands.

```console
[root@hub ~]# cf-promises --show-vars | grep "default:sys\.fqhost"
default:sys.fqhost                       hub                                                          inventory,source=agent,attribute_name=Host name
```

```console
[root@hub ~]# hostname -f
hub
```
