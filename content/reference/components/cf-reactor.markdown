---
layout: default
title: cf-reactor
keywords: [reactor]
aliases:
  - "/reference-components-cf-reactor.html"
---

`cf-reactor` is the CFEngine event reaction daemon.
We are currently working on making `cf-reactor` respond to events specified in policy language, using `when` bodies and `reactor` bundles.
This feature is coming in 3.29.0 and will be further documented here in the future.

**Notes:**

- In CFEngine Enterprise `cf-reactor` has some extra responsibilities, where it listens to `NOTIFY` events in the PostgreSQL database and performs actions when those events occur.
  One example of such events is refreshing the `host_specific.json` files whenever there is an event in the `cmdb_refresh` channel.

- In the future, the daemon should also take care of inventory refresh for hosts
  (now part of `cf-hub`) and many DB maintenance tasks that are now promises in
  the Masterfiles Policy Framework policy under `/cfe_internal/enterprise`.

**History:**

- In 3.18.2 / 3.20.0 `cf-reactor` was introduced as an Enterprise-only hub component.
- In 3.29.0 `cf-reactor` was moved to CFEngine community to be used as the daemon for event driven CFEngine policy.

## Command reference

{{< CFEngine_include_snippet(cf-reactor.help, [\s]*--[a-z], ^$) >}}
