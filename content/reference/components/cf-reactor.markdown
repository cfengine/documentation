---
layout: default
title: cf-reactor
keywords: [reactor, events]
aliases:
  - "/reference-components-cf-reactor.html"
---

`cf-reactor` is the event reaction daemon for CFEngine. Instead of running policy on a fixed
schedule like `cf-agent`, it watches for specific events on the host and runs policy
as soon as one happens.

`cf-reactor` keeps the promises made in `reactor` bundles and is affected by the
`common` control body. On event, it runs `agent` bundles.

**Notes:**

- `cf-reactor` always considers the class `reactor` to be defined.
- This daemon reloads its policy when the SIGHUP signal is received.
- `SIGUSR1` sets the log level to debug.
- `SIGUSR2` sets the log level to notice.
- On CFEngine Enterprise hubs, `cf-reactor` has extra responsibilities, see
  [Enterprise hub tasks][cf-reactor#Enterprise hub tasks].

**History:**

- In 3.18.2 / 3.20.0 `cf-reactor` was introduced as an Enterprise-only hub component.
- In 3.29.0 `cf-reactor` was moved to CFEngine community, and `reactor` bundles
  and [`events`][events] promises were introduced for event driven CFEngine
  policy.

## Command reference

{{< CFEngine_include_snippet(cf-reactor.help, [\s]*--[a-z], ^$) >}}

See also: [Reactor normal ordering][Policy evaluation#Reactor normal ordering]

## Under the hood

`cf-reactor` reads the policy and sets up event watchers based on the event promises declared in `reactor` bundles. It then starts a thread that polls for each registered event. When an event is detected, it is added to an event queue along with the corresponding event promise. The daemon is then signaled to handle the event and execute the appropriate `agent` bundles, following the same execution model as `cf-agent`.

**Notes:**

- Event detection is based on polling, but `cf-reactor` does not use busy-waiting. Instead, the polling thread sleeps between polling cycles and remains dormant when no events are registered.
- `cf-reactor` does not guarantee that an event will be handled immediately after it occurs. The delay depends on factors such as the polling interval, policy reloads, and slow code execution. However, `cf-reactor` guarantees that changes will be detected as fast as possible and the corresponding code executed, provided that execution does not fail.

## Enterprise hub tasks

On CFEngine Enterprise hubs, `cf-reactor` also listens to `NOTIFY` events in the
PostgreSQL database and performs actions when those events occur, and runs
periodic hub tasks:

- Refreshing the `host_specific.json` files whenever there is an event in the
  `cmdb_refresh` channel.
- Refreshing the inventory of hosts.
- Handling the requests of the Build application (cfbs requests and responses).
- Running alerts, scheduled reports, the cleanup of hosts, and the update of
  health failures.
