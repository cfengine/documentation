---
layout: default
title: Re-installing Enterprise Hub
published: true
tags: [cfengine enterprise, hub administration, re-install]
---

Sometimes it is useful to re-install the hub while still preserving existing
trust and licensing. To preserve trust the `$(sys.workdir)/ppkeys` directory
needs to be backed up and restored. To preserve enterprise licensing
`$(sys.workdir/license.dat)` and `$(sys.workdir)/licenses/.` should be backed
up.

**Note:** Depending on how and when your license was installed
`$(sys.workdir/licenses.dat)` and or `$(sys.workdir)/licenses/.` **may** not
exist. That is **ok**.

**Warning:** This process will not preserve any Mission Portal specific
configuration **except** for the upstream VCS repository configuration. LDAP,
roles, dashboards, and any other configuration done within Mission Portal will
be lost.

This script in
[core/contrib](https://github.com/cfengine/core/blob/master/contrib/enterprise/el-hub-reinstall.sh)
serves as an example.
