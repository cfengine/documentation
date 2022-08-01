---
layout: default
title: cf-reactor
published: true
tags: [Components, cf-reactor, Enterprise]
keywords: [reactor]
---

`cf-reactor` is the CFEngine event reaction daemon, it lists to `NOTIFY` events
on the `cmdb_refresh`a PostgreSQL channel and upon a message received, it
refreshes the CMDB data file (`host_specific.json`) for the particular host.

**Notes:**

* `cf-reactor` is a CFEngine Enterprise hub specific component.

* Unlike other components there is no control body for `cf-reactor`, all
  promises are hard coded within the component.

* In the future, the daemon should also take care of inventory refresh for hosts
  (now part of `cf-hub`) and many DB maintenance tasks that are now promises in
  the Masterfiles Policy Framework policy under `/cfe_internal/enterprise`.

**History:**

* 3.18.2, 3.20.0 Introduced new component (`cf-reactor`).

## Command reference ##

[%CFEngine_include_snippet(cf-reactor.help, [\s]*--[a-z], ^$)%]
