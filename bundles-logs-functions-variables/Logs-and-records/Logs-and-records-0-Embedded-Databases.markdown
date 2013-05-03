---
layout: default
title: Embedded-Databases
categories: [Logs-and-records,Embedded-Databases]
published: true
alias: Logs-and-records-Embedded-Databases.html
tags: [Logs-and-records,Embedded-Databases]
---

### Embedded Databases

The embedded databases can be viewed and printed using the reporting
tool `cf-report`.

Their file extensions will vary based on which library is used to
implement them; either Tokyo Cabinet (`.tcdb`), Quick Database Manager
(`.qdbm`), or Berkeley DB (`.db`). Converting one database format to
another is not handled by CFEngine, but there exist external tools meant
for that purpose.

cf\_Audit.tcdb

A compressed database of auditing information. This file grows very
large is auditing is switched on. By default, only minor information
about CFEngine runs are recorded. This file should be archived and
deleted regularly to avoid choking the system. \

cf\_lastseen.tcdb

A database of hosts that last contacted this host, or were contacted by
this host, and includes the times at which they were last observed. \

cf\_classes.tcdb

A database of classes that have been defined on the current host,
including their relative frequencies, scaled like a probability. \

checksum\_digests.tcdb

The database of hash values used in CFEngine's change management
functions. \

performance.tcdb

A database of last, average and deviation times of jobs recorded by
`cf-agent`. Most promises take an immeasurably short time to check, but
longer tasks such as command execution and file copying are measured by
default. Other checks can be instrumented by setting a
`measurement_class` in the `action` body of a promise. \

stats.tcdb

A database of external file attributes for change management
functionality. \

state/cf\_lock.tcdb

A database of active and inactive locks and their expiry times. Deleting
this database will reset all lock protections in CFEngine. \

state/history.tcdb

Enterprise level versions of CFEngine maintain this long-term trend
database. \

state/cf\_observations.tcdb

This database contains the current state of the observational history of
the host as recorded by `cf-monitord`. \

state/promise\_compliance.tcdb

Enterprise CFEngine (Nova and above) database of individual promise
compliance history. The database is approximate because promise
references can change as policy is edited. It quickly approaches
accuracy as a policy goes unchanged for more than a day. \

state/cf\_state.tcdb

A database of persistent classes active on this current host. \

state/nova\_measures.tcdb

Enterprise CFEngine (Nova and above) database of custom measurables. \

state/nova\_static.tcdb

Enterprise CFEngine (Nova and above) database of static system discovery
data.
