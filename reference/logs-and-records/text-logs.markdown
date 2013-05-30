---
layout: default
title: Text logs
categories: [Reference, Logs and records, Text logs]
published: true
alias: reference-logs-and-records-Text-logs.html
tags: [reference, logs, records]
---

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

* `reports/class_notes`

Class data in csv format for export to CMDB.   

* `state/file_change.log`

A time-stamped log of which files have experienced content changes since
the last observation, as determined by the hashing algorithms in
CFEngine.   

* `state/vars.out`

CFEngine Enterprise uses this log to communicate variable data.

* `state/*_measure.log`

CFEngine Enterprise maintains user-defined logs based on specifically
promised observations of the system.
