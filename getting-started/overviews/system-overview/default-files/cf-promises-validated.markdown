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

Starting with CFEngine 3.1.2, the results of every run of `cf-promises` are cached, which makes possible opportunities to avoid the need for verifying promises that may not have changed at all in hours, days or weeks. One other feature that makes this efficiency possible begins simply by touching the file `WORKDIR/masterfiles/cf_promises_validated`. 

The `cf_promises_validated` file is created by cf-agent (or any other CFEngine component), after it has successfully verified the policy with cf-promises. Also, before running cf-promises, the components check if any file is either included by `body common control` inputs or exists under `WORKDIR/inputs` (recursively), and is newer than the file `cf_promises_validated` (based on modification time). If not, the run of `cf-promises` is skipped.