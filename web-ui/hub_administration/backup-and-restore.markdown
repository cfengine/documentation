---
layout: default
title: Backup and Restore
published: true
tags: [cfengine enterprise, hub administration, backup, restore]
---

With policy stored in version control there are few things that should be
preserved in your backup and restore plan.

## Hub Identity

CFEngines trust model is based on public and private key exchange. In order to
re-provision a hub and for remote agents to retain trust the hubs key pair must
be preserved and restored.

Include `$(sys.workdir)/ppkeys/localhost.pub` and
`$(sys.workdir)ppkeys/localhost.priv` in your backup and restore plan.

**Note:** This is the most important thing to backup.

## Hub License

Enterprise hubs will collect for up to the licensed number of hosts. When
re-provisioning a hub you will need the license that matches the hub identity in
order to be able to collect reports for more than 25 hosts.

Include `$(sys.workdir)/licenses` in your backup plan.

## Hub Databases

Data collected from remote hosts and configuration information for Mission
Portal is stored on the hub in PostgreSQL which can be backed up and restored
using standard tools.

If you wish to rebuild a hub and
restore the history of policy outcomes you must backup and restore.

### Host Data

`cfdb` stores data related to policy runs on your hosts for example host inventory.

**Backup:** 

```console
# pg_dump -Fc cfdb > cfdb.bak
```

**Restore:**

```console
# pg_restore -Fc cfdb.bak
```

### Mission Portal

 `cfmp` and `cfsettings` store Mission Portals configuration information for
 example shared dashboards.
 
**Backup:** 
 
```console
# pg_dump -Fc cfmp > cfmp.bak
# pg_dump -Fc cfsettings > cfsettings.bak
```

**Restore:**

```console
# pg_restore -Fc cfmp.bak
# pg_restore -Fc cfsettings.bak
```
