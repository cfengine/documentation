---
layout: default
title: Client Initiated Reporting / Call collect
sorting: 60
published: true
tags: [cfengine enterprise, reporting, call collect]
---

Pull collect is the default mode of reporting.
In this mode, the reporting hub connects out to hosts to pull reporting data.

In call collect mode, clients initiate the reporting connection, by "calling" the hub first.
The hub keeps the connection open and collects the reports when it's ready.
Call collect is especially useful in environments where agents cannot be reached from the hub.
This could be because of NAT (routes) or firewall rules.

Call collect and Client Initiated Reporting are the same, they both refer to the same functionality.

## How do you enable call collect?

The easiest way to enable call collect is via augments files, modify `/var/cfengine/masterfiles/def.json` on the hub:

```
{
  "classes": {
    "client_initiated_reporting_enabled": [ "any" ]
  },
  "vars": {
    "mpf_access_rules_collect_calls_admit_ips": [ "0.0.0.0/0" ],
    "control_hub_exclude_hosts": [ "0.0.0.0/0" ]
  }
}
```

Client initiated reporting will be enabled on all hosts, since all hosts have the `any` class set.
`mpf_access_rules_collect_calls_admit_ips` controls what network range clients are allowed to connect from.
This should be customized to your environment.
`control_hub_exclude_hosts` will exclude the IPs in the network range(s) from pull collection.
This network range should usually match the one above.
Trying to use both pull and call collect for the same host can cause problems and unnecessary load on the hub.

**See also:** [`call_collect_interval`][cf-serverd#call_collect_interval], [`collect_window`][cf-serverd#collect_window]

## When are hosts collected from? How is collection affected by hub interval?

Call collect hosts are handled as soon as possible.
Agents initiate connections according to their own schedule, and the hub handles them as quickly as possible.
There is a separate call collect thread which waits for incoming connections, and queues them.
Whenever a thread in the cf-hub thread pool is available, it will prioritize the call collect queue before the pull queue.
Neither the call collect thread nor the worker thread pool are affected by the hub reporting schedule (`hub_schedule`).

## How can I see which hosts are call collected?

This is recorded in the PostgreSQL database on the hub, and can be queried from command line:

```
/var/cfengine/bin/psql -d cfdb -c "SELECT * FROM __hosts WHERE iscallcollected='t'";
```

## Are call collect hosts counted for enterprise licenses?

Yes, call collect hosts consume a license.
If you have too many hosts (pull + call) for your license, `cf-hub` will start emitting errors, and skip some hosts.
`cf-hub` prioritizes call collect hosts, and will only skip pull collect hosts when over license.
Note that in other parts of the product, like Mission Portal, there is no distinction between call collect and pull collect hosts.

## How do you disable call collect?

Update the `def.json` file with the new classes and appropriate network ranges.
For hosts which are already using call collect, but shouldn't, the easiest approach is to generate new keys, bootstrap again, and then remove the old host in Mission Portal or via API.
Unfortunately, there is no way, currently, to easily make a host switch back to pull collection.
