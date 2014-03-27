---
layout: default
title: cf_promises_validated
sorting: 100
categories: [Getting Started, Overviews, System Overview, Default Files, cf_promises_validated]
published: true
alias: getting-started-overviews-default-files-cf-promises-validated.html
tags: [getting started, overviews, system overview, files, default files, file structure, cf_promises_validated]
---

Several components of CFEngine reading policy (e.g. cf-agent, cf-execd, cf-serverd, etc.) require verification from cf-promises that syntax of policies is correct before touching the policy themselves. To illustrate this, if `cf-promises` runs every 5 minutes then there will be 12 checks occurring every hour, 24 hours a day, 7 days a week -- a total of 2016 possible validation checks. Each of those individual validation sessions can take some number of seconds to perform depending on the system, scale, circumstances and configuration.

Starting with CFEngine 3.1.2, the results of every run of `cf-promises` are cached, which makes possible opportunities to avoid the need for verifying promises that may not have changed at all in hours, days or weeks. 

One other feature that makes this efficiency possible is the file `WORKDIR/masterfiles/cf_promises_validated`, which is created by cf-agent (or any other CFEngine component), after it has successfully verified the policy with cf-promises. When the hash content of any file under `WORKDIR/inputs` changes, and validates to be syntactically correct, then a timestamp in `cf_promises_validated` is updated. 

If not, the run of `cf-promises` is skipped and, at the same time, the cf-execd, cf-serverd and cf-monitord daemons will not reload the `policy` unless `cf_promises_validated` has an updated timestamp, which `cf-agent` will normally take care of.

The timestamp itself is updated using `cf-promises -T`, and is currently only used by the Design Center integration. It is not used in Core at all, except for being generally available if anyone wants to run it manually.