---
layout: default
title: CFEngine Files, Directories and Logs
categories: [Getting Started, Concepts, CFEngine Files, Directories and Logs]
published: true
sorting: 30
alias: overview-system-files-directories-logs.html
tags: [overviews, system overview, files, directories, logs]
---

## Policy files

* `/var/cfengine/masterfiles`

Policy repository which grants access to local or bootstrapped CFEngine 
clients when they need to update their policies. Policies obtained from 
`/var/cfengine/masterfiles` are then cached in `/var/cfengine/inputs` for 
local policy execution. The `cf-agent` executable does not execute policies 
directly from this repository.

* `/var/cfengine/inputs`

Cached policy repository on each CFEngine client. When `cf-agent` is 
invoked by `cf-execd`, it reads only from this directory.

* `/var/cfengine/modules`

Location of scripts used in `commands` promises.

## Output Directories

* `/var/cfengine/outputs`

Directory where `cf-agent` creates its output files. The outputs directory is 
a record of spooled run-reports. These are often mailed to the administrator 
by `cf-execd`, or can be copied to another central location and viewed in an 
alternative browser. However, not all hosts have an email capability or are 
online, so the reports are kept here.

* `/var/cfengine/reports`

Directory used to store reports. Reports are not tidied automatically, so you 
should delete these files after a time to avoid a build up.

* `/var/cfengine/ppkeys`

Directory used to store encrypted public/private keys for CFEngine
client/server network communications.

* `/var/cfengine/state`

State data such as current process identifiers of running processes, 
persistent classes and other cached data.

* `/var/cfengine/lastseen`

Log data for incoming and outgoing connections.

## Logs and Records

On hosts, CFEngine writes numerous logs and records to its private workspace. 

[CFEngine Enterprise][Enterprise Report API] provides solutions 
for centralization and network-wide reporting at an arbitrary scale.

## Embedded Databases

Their file extensions will vary based on which library is used to
implement them: either Tokyo Cabinet (`.tcdb`) or Quick Database Manager
(`.qdbm`).

* `cf_lastseen.tcdb`

A database of hosts that last contacted this host, or were contacted by
this host, and includes the times at which they were last observed.   

* `cf_classes.tcdb`

A database of classes that have been defined on the current host,
including their relative frequencies, scaled like a probability.   

* `cf_variables.tcdb`

A database of variables (name and value) that were defined on the
current host during the last run, including relative frequencies.

* `checksum_digests.tcdb`

The database of hash values used in CFEngine's change management
functions.   

* `performance.tcdb`

A database of last, average and deviation times of jobs recorded by
`cf-agent`. Most promises take an immeasurably short time to check, but
longer tasks such as command execution and file copying are measured by
default. Other checks can be instrumented by setting a
`measurement_class` in the `action` body of a promise.   

* `stats.tcdb`

A database of external file attributes for change management
functionality.   

* `state/cf_lock.tcdb`

A database of active and inactive locks and their expiry times. Deleting
this database will reset all lock protections in CFEngine.   

* `state/history.tcdb`

CFEngine Enterprise maintains this long-term trend database.   

* `state/cf_observations.tcdb`

This database contains the current state of the observational history of
the host as recorded by `cf-monitord`.   

* `state/promise_compliance.tcdb`

CFEngine Enterprise database of individual promise
compliance history. The database is approximate because promise
references can change as policy is edited. It quickly approaches
accuracy as a policy goes unchanged for more than a day.   

* `state/cf_state.tcdb`

A database of persistent classes active on this current host.   

* `state/nova_measures.tcdb`

CFEngine Enterprise database of custom measurements.

* `state/nova_static.tcdb`

CFEngine Enterprise database of static system discovery data.

## Text logs

* `promise_summary.log`

A time-stamped log of the percentage fraction of promises kept after
each run.   

* `cf3.HOSTNAME.runlog`

A time-stamped log of when each lock was released. This shows the last
time each individual promise was verified.   

* `cfagent.HOSTNAME.log`

Although ambiguously named (for historical reasons) this log contains
the current list of setuid/setgid programs observed on the system.
CFEngine warns about new additions to this list. This log has been
deprecated.   

* `cf_value.log`

A time stamped log of the business value estimated from the execution of
the automation system.   

* `cf_notkept.log`

In CFEngine Enterprise, a list of promises, with handles and comments, that 
were not kept.

* `cf_repaired.log`

In CFEngine Enterprise, a list of promises, with handles and comments, that were repaired.

* `reports/*`

CFEngine Enterprise uses this directory as a default place for outputting
reports.

* `state/cf_procs`
A cache of the process table. This is useful for `measurement` promises about processes.

* `state/cf_rootprocs`
A cache of the process table of processes owned by the root user. This is useful for `measurement` promises about processes.

* `state/cf_otherprocs`
A cache of the process table for processes not owned by the root user. This is useful for `measurement` promises about processes.

* `state/file_changes.log`

A time-stamped log of which files have experienced content changes since
the last observation, as determined by the hashing algorithms in
CFEngine.   

* `state/*_measure.log`

CFEngine Enterprise maintains user-defined logs based on specifically
promised observations of the system.

* `state/env_data`

This file contains a list of currently discovered classes and variable
values that characterize the anomaly alert environment. They are altered
by the monitor daemon.   

* `/var/logs/cfengine-install.log`

This file contains logs related to the CFEngine package installation.

## Process Information

The CFEngine components keep their current process identifier number in
`pid files' in the work directory. For example:

    cf-execd.pid
    cf-serverd.pid
