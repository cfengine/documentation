---
layout: default
title: cf-reactor
keywords: [reactor, events]
aliases:
  - "/reference-components-cf-reactor.html"
---

`cf-reactor` is the event reaction daemon for CFEngine.
Instead of running policy on a fixed schedule like `cf-agent`, it watches for specific events on the host and runs policy as soon as one happens.

`cf-reactor` keeps the promises made in `reactor` bundles and is affected by the `common` control body.
On event, it runs the bundles of the [`then`][events#then] attribute of the [`events`][events] promise: `reactor` bundles without `events` promises, which behave like `agent` bundles, or `agent` and `common` bundles.
See [Reactor bundles][cf-reactor#Reactor bundles].

**Notes:**

- `cf-reactor` always considers the class `reactor` to be defined.
- This daemon reloads its policy when the SIGHUP signal is received.
- `SIGUSR1` sets the log level to debug.
- `SIGUSR2` sets the log level to notice.
- On CFEngine Enterprise hubs, `cf-reactor` has extra responsibilities, see [Enterprise hub tasks][cf-reactor#Enterprise hub tasks].

**History:**

- In 3.18.2 / 3.20.0 `cf-reactor` was introduced as an Enterprise-only hub component.
- In 3.29.0 `cf-reactor` was moved to CFEngine community, and `reactor` bundles and [`events`][events] promises were introduced for event driven CFEngine policy.

## Command reference

{{< CFEngine_include_snippet(cf-reactor.help, [\s]*--[a-z], ^$) >}}

See also: [Reactor normal ordering][Policy evaluation#Reactor normal ordering]

## Reactor bundles

There are two kinds of `reactor` bundles, depending on whether they have [`events`][events] promises:

- `reactor` bundles **with** `events` promises set up the events to react to.
  Besides `events` promises, they can only have [`meta`][meta], [`vars`][vars] and [`classes`][classes] promises.
  `cf-reactor` evaluates them every time it reads the policy, see [Reactor normal ordering][Policy evaluation#Reactor normal ordering].
- `reactor` bundles **without** `events` promises are run on event, from the [`then`][events#then] attribute of `events` promises.
  They can have all the promise types of `agent` bundles, including [custom promise types][custom], and `cf-reactor` runs them like `cf-agent` runs `agent` bundles.
  They are not evaluated when `cf-reactor` reads the policy.

Having other promise types than `meta`, `vars` and `classes` alongside `events` promises is an error, and so is referring to a `reactor` bundle with `events` promises in a `then` attribute.

With `reactor` bundles without `events` promises, a policy for `cf-reactor` does not need `agent` bundles:

```cf3
body when deleted(file)
{
  file_deleted => "$(file)";
}

bundle reactor watch
{
  vars:
    "file" string => "/tmp/a";

  events:
    "Keep $(file)"
      when => deleted("$(file)"),
      then => { create_file("$(file)"), report_restored("$(file)") };
}

bundle reactor create_file(file)
{
  files:
    "$(file)" create => "true";
}

bundle reactor report_restored(file)
{
  reports:
    "$(file) was restored";
}
```

**Note:** [`methods`][methods] promises can call `agent` and `common` bundles, but not `reactor` bundles.

## Under the hood

`cf-reactor` reads the policy and sets up event watchers based on the event promises declared in `reactor` bundles.
It then starts a thread that polls for each registered event.
When an event is detected, it is added to an event queue along with the corresponding event promise.
The daemon is then signaled to handle the event and run the bundles of the `then` attribute of the event promise, following the same execution model as `cf-agent`.

**Notes:**

- Event detection is based on polling, but `cf-reactor` does not use busy-waiting.
  Instead, the polling thread sleeps between polling cycles and remains dormant when no events are registered.
- `cf-reactor` does not guarantee that an event will be handled immediately after it occurs.
  The delay depends on factors such as the polling interval, policy reloads, and slow code execution.
  However, `cf-reactor` guarantees that changes will be detected as fast as possible and the corresponding code executed, provided that execution does not fail.

## Performance

`cf-reactor` uses these threads:

- A watcher thread checks for events, and queues the events it detects.
- The main thread takes the events from the queue and runs their [`then`][events#then] bundles, one event at a time.
- For `package_installed` and `package_uninstalled` events, a listing thread lists the installed packages every 10 seconds.
  There is one listing thread per [package module][Package modules] (e.g. `apt_get`), shared by all the `events` promises using it, whatever the number of packages they watch.
  The watcher thread compares these lists to detect the events.

How many events per second it can handle depends on the event type and on how long the `then` bundles take to run.

Each `events` promise fires at most once per check, so at most once per [`interval`][events#interval].
With `N` `events` promises and an interval of `I` seconds, `cf-reactor` has at most `N / I` events per second to handle.
Changes happening between two checks are seen as one event.

The figures below were measured on an Amazon EC2 `t2.micro` instance (1 vCPU, Intel Xeon E5-2686 v4 at 2.30 GHz, 1 GB of memory) running Ubuntu 24.04.
Each `events` promise watched its own file, user or package, with the default `interval` of 1 second, and its `then` bundle had a single `reports` promise.

The watched files, users and packages were changed for 30 seconds, at a fixed number of events per second.
The test was repeated with more and more events per second, until `cf-reactor` could no longer handle the events as fast as they happened.
The limit is the most events per second `cf-reactor` can handle for each event type:

| Event type                 | Limit (events/s) |
| -------------------------- | ---------------: |
| `file_deleted`             |              138 |
| `file_created`             |              133 |
| `file_modified`            |              145 |
| `file_content_modified`    |               21 |
| `file_permissions_changed` |               15 |
| `file_owner_changed`       |               14 |
| `file_size_exceeds`        |               25 |
| `user_added`               |     at least 3.8 |
| `user_removed`             |     at least 4.2 |
| `package_installed`        |     at least 1.2 |
| `package_uninstalled`      |     at least 1.2 |

**Notes:**

- Users and packages could not be added or removed fast enough to reach the limit of `cf-reactor`: these figures are lower bounds.
- Above the limit, `cf-reactor` doesn't lose events: they pile up in the queue and are handled late.
- Slower `then` bundles lower these limits.

## Enterprise hub tasks

On CFEngine Enterprise hubs, `cf-reactor` also listens to `NOTIFY` events in the PostgreSQL database and performs actions when those events occur, and runs periodic hub tasks:

- Refreshing the `host_specific.json` files whenever there is an event in the `cmdb_refresh` channel.
- Refreshing the inventory of hosts.
- Handling the requests of the Build application (cfbs requests and responses).
- Running alerts, scheduled reports, the cleanup of hosts, and the update of health failures.
