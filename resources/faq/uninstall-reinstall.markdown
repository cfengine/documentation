---
layout: default
title: Uninstalling/Reinstalling
published: true
sorting: 40
tags: [uninstall, reinstall]
---

# What is left behind after uninstalling?

Uninstalling a cfengine package does not remove any user data. Most data
including the host identity (`$(sys.workdir)/ppkeys/localhost.{pub,priv}`),
state, policy, and logs remain.

To completely remove cfengine delete `$(sys.workdir)` typically `/var/cfengine`
or `C:\Program Files\Cfengine` after uninstalling the package.

# Should I delete anything if I am re-installing?

You may want to wipe `$(sys.statedir)` and `$(sys.workdir)/outputs` for a fresh start to log data and history.

You may want to revoke trust of other hosts by deleting
`$(sys.workdir)/ppkeys/*.pub` ( excluding `localhost.pub` ).

Only delete the host identity if you want to generate a new key pair and
establish a new identity for this host.
