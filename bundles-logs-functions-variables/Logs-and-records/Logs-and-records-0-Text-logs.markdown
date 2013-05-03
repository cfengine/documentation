---
layout: default
title: Text-logs
categories: [Logs-and-records,Text-logs]
published: true
alias: Logs-and-records-Text-logs.html
tags: [Logs-and-records,Text-logs]
---

### Text logs

promise\_summary.log

A time-stamped log of the percentage fraction of promises kept after
each run. \

cf3.HOSTNAME.runlog

A time-stamped log of when each lock was released. This shows the last
time each individual promise was verified. \

cfagent.HOSTNAME.log

Although ambiguously named (for historical reasons) this log contains
the current list of setuid/setgid programs observed on the system.
CFEngine warns about new additions to this list. This log has been
deprecated. \

cf\_value.log

A time stamped log of the business value estimated from the execution of
the automation system. \

cf\_notkept.log

A list of promises, with handles and comments, that were not kept. Nova
enterprise versions only. \

cf\_repaired.log

A list of promises, with handles and comments, that were repaired. Nova
enterprise versions only. \

reports/\*

Enterprise versions of CFEngine use this directory as a default place
for outputting reports. \

reports/class\_notes

Class data in csv format for export to CMDB. \

state/file\_change.log

A time-stamped log of which files have experienced content changes since
the last observation, as determined by the hashing algorithms in
CFEngine. \

state/vars.out

Enterprise level versions of CFEngine use this log to communicate
variable data. \

state/\*\_measure.log

Enterprise level versions of CFEngine maintain user-defined logs based
on specifically promised observations of the system.
