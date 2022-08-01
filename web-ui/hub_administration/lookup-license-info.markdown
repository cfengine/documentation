---
layout: default
title: Lookup License Info
published: true
tags: [cfengine enterprise, hub administration, license]
---

Information about the currently issued license can be obtained from the About section in Mission Portal web interface or from the command line as shown here.

**Note:** When the CFEngine Enterprise license expires
**report collection** is limited. No agent side
functionality is changed. However if you are using
functions or features that rely on information collected
by the hub, that information will no longer be a reliable
source of data.

# Get license info via API

Run from the hub itself.

```console
$ curl -u admin http://localhost/api/
```

# Get license info from cf-hub

Run as `root` from the hub itself.

```console
[root@hub ~]# cf-hub --show-license
License file:     /var/cfengine/licenses/hub-SHA=d13c14c3dc46ef1c5824eb70ffae3a1d1c67c7ce70a1e8e8634b1324d0041131.dat
License status:   Valid
License count:    50
Company name:     CFEngine (hub.example.com)
License host key: SHA=2e5c7d9636c5644d023d71859f3296755f8d53d5d183af98efc1540655731fcc
Expiration date:  3018-01-01
Utilization:      20/50 (Approximate)
```

