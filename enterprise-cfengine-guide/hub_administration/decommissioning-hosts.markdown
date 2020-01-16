---
layout: default
title: Decommissioning hosts
sorting: 30
published: true
tags: [cfengine enterprise, user interface, mission portal]
---

Once a host is shut off, or CFEngine is uninstalled, you should remove it from Mission Portal.
This has 2 benefits:

* Report collection will no longer count it as consuming a license.
* You won't see its data or get alerts for it in Mission Portal.

**Removing a host from the hub / Mission Portal does not uninstall or stop CFEngine on that host.**
Before removing hosts, please ensure that they are either completely gone (VM destroyed) or definitely not running CFEngine.
If the host is still running CFEngine, or there is another host running with the same CFEngine ID, it could reappear in Mission Portal, or cause other problems in reporting.

Hosts can be removed via API or UI, the outcome is the same:

* The host is deleted from all tables/views in PostgreSQL, including `hosts`, `inventory`, etc.
    * There may still be references to the host in reporting data from other hosts.
* The host is deleted from `cf_lastseen.lmdb` the database used for discovering hosts for report collection.
* The hosts cryptographic key is removed from the `ppkeys` directory.

Please note that:

* Users with admin role can delete hosts without reporting data (which don't show up in Mission Portal).
* Host deletion is a scheduled operation, the `cf-hub` process will pick up the deletion request later.
    * This is because of security concerns, the Apache user does not have direct access to the necessary files.
    * It may take a few minutes before the host disappears from all the places listed above.
* For these reasons the HTTP response code is normally `202 Accepted`.
    * At the time of the API response, it is not possible to know whether the host exists in all the places mentioned above.

## Host removal through Mission Portal UI ##

Single hosts can be removed by visiting the host info page, and clicking the trash can next to the host identifier (header):

![Remove host](../Mission-portal-remove-host.png)

## Host removal through Enterprise API ##

If you decommission hosts regularly, it can be cumbersome to use the UI for every host.
Decommissioning can be done via API, for example using curl:

```
curl --user admin:admin http://127.0.0.1/api/host/cf-key -r SHA=92eff6add6e8add0bb51f1af52d8f56ed69b56ccdca27509952ae07fe5b2997b -X DELETE
```

It is a good idea to add this to decommissioning procedure, or automated decommissioning scripts.
(Replace `127.0.0.1` with the IP or hostname of your Mission Portal instance).

## Host removal using cf-key CLI ##

This method is generally not recommended on the CFEngine Enterprise Hub, as it **does not** remove hosts from the PostgreSQL database.

The `cf-key` binary allows you to delete hosts from the `cf_lastseen.lmdb` database and `ppkeys`:

```
cf-key -r SHA=92eff6add6e8add0bb51f1af52d8f56ed69b56ccdca27509952ae07fe5b2997b
```

If there are coherency problems with your `cf_lastseen.lmdb` database, this will prevent you from removing keys.
You are advised to review the output and try to understand why the problems are occurring.
Optionally, you can force the removal of a key, using `--force-removal` in the `cf-key` command.

