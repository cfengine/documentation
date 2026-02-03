---
layout: default
title: Backup and restore
aliases:
  - "/web-ui-hub_administration-backup-and-restore.html"
---

With policy stored in version control there are few things that should be
preserved in your backup and restore plan.

## Hub identity

CFEngines trust model is based on public and private key exchange. In order to
re-provision a hub and for remote agents to retain trust the hubs key pair must
be preserved and restored.

Include `$(sys.workdir)/ppkeys/localhost.pub` and
`$(sys.workdir)ppkeys/localhost.priv` in your backup and restore plan.

**Note:** This is the most important thing to backup.

## Hub license

Enterprise hubs will collect for up to the licensed number of hosts. When
re-provisioning a hub you will need the license that matches the hub identity in
order to be able to collect reports for more than 25 hosts.

Include `$(sys.workdir)/licenses` in your backup plan.

## Hub databases

Data collected from remote hosts and configuration information for Mission
Portal is stored on the hub in PostgreSQL which can be backed up and restored
using standard tools.

If you wish to rebuild a hub and
restore the history of policy outcomes you must backup and restore.

### Host data

`cfdb` stores data related to policy runs on your hosts for example host inventory.

**Backup:**

```command
pg_dump --format=c cfdb > cfdb.bak
```

**Restore:**

```command
pg_restore --format=c --dbname=cfdb cfdb.bak
```

### Mission Portal

`cfmp` and `cfsettings` store Mission Portals configuration information for
example shared dashboards.

**Backup:**

```console
# pg_dump --format=c cfmp > cfmp.bak
# pg_dump --format=c cfsettings > cfsettings.bak
```

**Restore:**

```console
# pg_restore --format=c --dbname=cfmp cfmp.bak
# pg_restore --format=c --dbname=cfsettings cfsettings.bak
```
