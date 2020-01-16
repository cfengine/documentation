---
layout: default
title: Hosts and Health
sorting: 30
published: true
tags: [cfengine enterprise, user interface, mission portal]
---

## Host Compliance ##

CFEngine collects data on `promise` compliance. Each host is in one of two groups: out of compliance or fully compliant.

* A host is considered out of compliance if less than 100% of its promises were kept.
* A host is considered fully compliant if 100% of its promises were kept.

You can look at a specific sub-set of your hosts by selecting a category from the menu on the left.

### Host Info ###

Here you will find extensive information on single hosts that CFEngine detects automatically in your environment. Since this is data gathered per host, you need to select a single host from the menu on the left first.

## Host Health ##

![Hosts](Mission-portal-health-dignostics-header.png)

You can get quick access to the health of hosts, including direct links to reports, from the Health drop down at the top of every Enterprise UI screen. Hosts are listed as unhealthy if:

* the hub was not able to connect to and collect data from the host within a set time interval (unreachable host). The time interval can be set in the Mission Portal settings.
* the policy did not get executed for the last three runs. This could be caused by `cf-execd` not running on the host (scheduling deviation) or an error in policy that stops its execution. The hub is still able to contact the host, but it will return stale data because of this deviation.
* two or more hosts use the same key. This is detected by "reporting cookies", randomized tokens generated every report collection. If the client presents a mismatching cookie (compared to last collection) a collision is detected. The number of collisions (per hostkey) that cause the unhealthy status is configurable in [settings][Settings#Preferences].
* reports have recently been collected, but cf-agent has not recently run. "Recently" is defined by the configured run-interval of their cf-agent.

These categories are non-overlapping, meaning a host will only appear in one category at at time even if conditions satisfying multiple categories might be present. This makes reports simpler to read, and makes it easier to detect and fix the root cause of the issue. As one issue is resolved the host might then move to another category.
In either situation the data from that host will be from old runs and probably not reflect the current state of that host.

## Host decommissioning ##

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

### Host removal through Mission Portal UI ###

Single hosts can be removed by visiting the host info page, and clicking the trash can next to the host identifier (header):

![Remove host](Mission-portal-remove-host.png)

### Host removal through Enterprise API ###

If you decommission hosts regularly, it can be cumbersome to use the UI for every host.
Decommissioning can be done via API, for example using curl:

```
curl --user admin:admin http://127.0.0.1/api/host/cf-key -r SHA=92eff6add6e8add0bb51f1af52d8f56ed69b56ccdca27509952ae07fe5b2997b -X DELETE
```

It is a good idea to add this to decommissioning procedure, or automated decommissioning scripts.
(Replace `127.0.0.1` with the IP or hostname of your Mission Portal instance).

### Host removal using cf-key CLI ###

This method is generally not recommended on the CFEngine Enterprise Hub, as it **does not** remove hosts from the PostgreSQL database.

The `cf-key` binary allows you to delete hosts from the `cf_lastseen.lmdb` database and `ppkeys`:

```
cf-key -r SHA=92eff6add6e8add0bb51f1af52d8f56ed69b56ccdca27509952ae07fe5b2997b
```

If there are coherency problems with your `cf_lastseen.lmdb` database, this will prevent you from removing keys.
You are advised to review the output and try to understand why the problems are occurring.
Optionally, you can force the removal of a key, using `--force-removal` in the `cf-key` command.
