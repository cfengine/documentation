---
layout: default
title: cf-check
sorting: 80
aliases:
  - "/reference-components-cf-check.html"
---

The `cf-check` binary can be used to inspect, dump, diagnose, and repair LMDB databases used by CFEngine.
The diagnosis and repair parts of `cf-check` are built into CFEngine, meaning corrupt databases are automatically fixed and users normally don't need to run these commands manually.

## Help output (`--help`)

The `--help` command line option gives you an overview of what the tool can do:

```command
cf-check --help
```

```output
{{< CFEngine_include_markdown(cf-check.help, .*) >}}
```

## Inspecting databases

The `dump` command can be used to look at the contents of each database in a JSON5 format.

```command
cf-check dump /var/cfengine/state/cf_lastseen.lmdb
```

```json {output}
{
  "a172.31.7.155": "SHA=9153587b09d8426fd6b3e2dc6c47c29891e2a20430148725ce6e7d95d48637c0",
  "kSHA=9153587b09d8426fd6b3e2dc6c47c29891e2a20430148725ce6e7d95d48637c0": "172.31.7.155",
  "qiSHA=9153587b09d8426fd6b3e2dc6c47c29891e2a20430148725ce6e7d95d48637c0": {
    "Q": { "dq": 190.0, "expect": 173.8105, "q": 245.0, "var": 14173.7558 },
    "acknowledged": false,
    "lastseen": 1772732121
  },
  "qoSHA=9153587b09d8426fd6b3e2dc6c47c29891e2a20430148725ce6e7d95d48637c0": {
    "Q": { "dq": 190.0, "expect": 173.8105, "q": 245.0, "var": 14173.7558 },
    "acknowledged": false,
    "lastseen": 1772732121
  },
  "version": "2"
}
```

We use JSON5 because it has some nice additions to normal JSON, like allowing trailing commas and escape sequences which make binary (non-ascii) data more readable.

**Tip:** You can use `json5` and `jq` if you want to convert to JSON and format the output;

```command
cf-check dump /var/cfengine/state/cf_lastseen.lmdb | json5 | jq
```

```json {output}
{
  "a172.31.7.155": "SHA=9153587b09d8426fd6b3e2dc6c47c29891e2a20430148725ce6e7d95d48637c0",
  "kSHA=9153587b09d8426fd6b3e2dc6c47c29891e2a20430148725ce6e7d95d48637c0": "172.31.7.155",
  "qiSHA=9153587b09d8426fd6b3e2dc6c47c29891e2a20430148725ce6e7d95d48637c0": {
    "Q": { "dq": 190, "expect": 173.7718, "q": 245, "var": 14127.5535 },
    "acknowledged": false,
    "lastseen": 1772732421
  },
  "qoSHA=9153587b09d8426fd6b3e2dc6c47c29891e2a20430148725ce6e7d95d48637c0": {
    "Q": { "dq": 190, "expect": 173.7718, "q": 245, "var": 14127.5535 },
    "acknowledged": false,
    "lastseen": 1772732421
  },
  "version": "2"
}
```

## Diagnosing potentially corrupt database files

The `diagnose` command can be used to check the state of databases.
By default it will look at all the LMDB databases (in `/var/cfengine/state/`).
Technically it will attempt to open the database, and run some per-database validation checks (based on the filename).
This work is done in a forked subprocess, so if it crashes or fails in any way, the parent `cf-check` process can handle it and print a summary.

```command
cf-check diagnose
```

```output
info: No filenames specified, defaulting to .lmdb files in /var/cfengine/state
info: Status of '/var/cfengine/state/history.lmdb': OK [0% usage]
info: Status of '/var/cfengine/state/cf_state.lmdb': OK [0% usage]
info: Status of '/var/cfengine/state/nova_cookies.lmdb': OK [0% usage]
info: Status of '/var/cfengine/state/nova_track.lmdb': OK [0% usage]
info: Status of '/var/cfengine/state/nova_measures.lmdb': OK [0% usage]
info: Status of '/var/cfengine/state/cf_changes.lmdb': OK [0% usage]
info: Status of '/var/cfengine/state/packages_installed_apt_get.lmdb': OK [0% usage]
info: Status of '/var/cfengine/state/cf_lock.lmdb': OK [0% usage]
info: Status of '/var/cfengine/state/performance.lmdb': OK [0% usage]
info: Status of '/var/cfengine/state/cf_lastseen.lmdb': OK [0% usage]
info: Status of '/var/cfengine/state/cf_observations.lmdb': OK [0% usage]
info: Status of '/var/cfengine/state/nova_agent_execution.lmdb': OK [0% usage]
info: Status of '/var/cfengine/state/packages_updates_apt_get.lmdb': OK [0% usage]
info: Status of '/var/cfengine/state/nova_static.lmdb': OK [0% usage]
info: All 14 databases healthy
```

You can also specify a specific filename:

```command
cf-check diagnose /var/cfengine/state/cf_lastseen.lmdb
```

```output
info: Status of '/var/cfengine/state/cf_lastseen.lmdb': OK [0% usage]
info: All 1 databases healthy
```

## Repairing corrupt databases

The `repair` command builds on the functionality of the `diagnose` command, but attempts to fix the situation when there are corrupt databases found.

```command
cf-check repair /var/cfengine/state/cf_state.lmdb
```

```output
  info: Status of '/var/cfengine/state/cf_state.lmdb': LMDB_INVALID_DATABASE [0% usage]
 error: Problems detected in 1/1 databases
notice: 1 corrupt database to fix
  info: Backing up to '/var/cfengine/backups/1772733351-WZgDKk/'
  info: Copying: '/var/cfengine/state/cf_state.lmdb' -> '/var/cfengine/backups/1772733351-WZgDKk/cf_state.lmdb'
 error: Failed to repair file '/var/cfengine/state/cf_state.lmdb', removing
notice: Database repair successful
```
