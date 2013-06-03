---
layout: default
title: Embedded Databases
categories: [Reference, Logs and records,Embedded Databases]
published: true
alias: reference-logs-and-records-embedded-databases.html
tags: [reference, logs, records, embedded, databases]
---

Their file extensions will vary based on which library is used to
implement them: either Tokyo Cabinet (`.tcdb`) or Quick Database Manager
(`.qdbm`).

* `cf_Audit.tcdb`

A compressed database of auditing information. This file grows very
large is auditing is switched on. By default, only minor information
about CFEngine runs are recorded. This file should be archived and
deleted regularly to avoid choking the system.   

* `cf_lastseen.tcdb`

A database of hosts that last contacted this host, or were contacted by
this host, and includes the times at which they were last observed.   

* `cf_classes.tcdb`

A database of classes that have been defined on the current host,
including their relative frequencies, scaled like a probability.   

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
