---
layout: default
title: What is promise locking? 
published: true
sorting: 90
tags: [getting started, faq, locking]
---

By default when the agent runs each promise that has an outcome
of `kept` or `repaired` is **locked** for one minute. So if the
agent runs again within one minute the kept or repaired promise
will be skipped. The `--no-lock` and `-K` options clear locks
at the beginning of the run so a kept or repaired promise
actuated within the previous minute will be actuated again.
Generally when people run the agent manually (during debugging
or testing) the agent is run without locks (because it's not
uncommon to iterate quickly and have back to back executions),
but typically for automatic execution the agent respects these
locks to avoid excessive resource usage and avoid accidental
denial of service.

Versions prior to 3.8 do not allow executions initiated by
`cf-runagent` to ignore locks.
