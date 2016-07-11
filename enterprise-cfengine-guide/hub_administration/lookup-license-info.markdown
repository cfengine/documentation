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
# cf-hub -Fvn | grep -i expiring
2016-07-11T15:54:23+0000  verbose: Found 25 CFEngine Enterprise licenses, expiring on 2222-12-25 for FREE ENTERPRISE - http://cfengine.com/terms for terms
```

