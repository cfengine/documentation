---
layout: default
title: cf-reactor
keywords: [reactor, events]
aliases:
  - "/reference-components-cf-reactor.html"
---

`cf-reactor` is the CFEngine event reaction daemon. It watches for the events
described by [`events`][events] promises in `reactor` bundles, and as soon as
an event happens, it runs the bundles promised for it, without waiting for the
next scheduled `cf-agent` run.

`cf-reactor` keeps the promises made in `common` and `reactor` bundles, and is
affected by the `common` control body.

```cf3
bundle agent main
{
  methods:
    "motd" usebundle => motd;
}

bundle agent motd
{
  files:
    "/etc/motd" content => "This host is managed by CFEngine$(const.n)";
}

bundle reactor motd_watch
{
  events:
    "motd_deleted"
      when => deleted("/etc/motd"),
      then => motd;
}

body when deleted(path)
{
  file_deleted => "$(path)";
}
```

In this example, `cf-agent` creates `/etc/motd` on its regular runs, and
whenever the file is deleted, `cf-reactor` runs the `motd` bundle right away to
restore it:

```output
    info: Registering a file_deleted watcher for events promise 'motd_deleted', on file '/etc/motd'
  notice: Reactor watcher 'motd_deleted' fired
    info: Created file '/etc/motd', mode 0600
```

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

## Reactor bundles

Bundles of type `reactor` describe the events `cf-reactor` watches for, with
[`events`][events] promises. `cf-reactor` evaluates all the `reactor` bundles of
the policy, so there is no need to list them in a `bundlesequence`. Reactor
bundles taking parameters are not evaluated: `cf-reactor` logs a warning about
them instead.

In a reactor bundle, `cf-reactor` keeps the `meta`, `vars`, `classes` and
`events` promises, in that order. `defaults` and `reports` promises are allowed,
but ignored. Other components, like `cf-agent`, ignore reactor bundles.

Like the other components, `cf-reactor` also evaluates the `vars` and `classes`
promises of `common` bundles, so their variables and classes can be used in
reactor bundles.

Classes defined in reactor bundles are bundle scoped by default, as in agent
bundles. To use a class of a reactor bundle in the bundles run on events, or to
guard `events` promises, define it with [`scope`][classes#scope] `namespace`:

```cf3
bundle reactor watch_nginx_config
{
  classes:
    "nginx_installed"
      expression => fileexists("/usr/sbin/nginx"),
      scope => "namespace";

  events:
    nginx_installed::
      "nginx_config_deleted"
        when => deleted("/etc/nginx/nginx.conf"),
        then => nginx_config_deleted;
}

bundle agent nginx_config_deleted
{
  reports:
    "/etc/nginx/nginx.conf was deleted";
}

body when deleted(path)
{
  file_deleted => "$(path)";
}
```

**Note:** Currently, the classes guarding `events` promises, with class
expressions or with [`if`][Promise types#if] and
[`unless`][Promise types#unless], must be namespace scoped (or hard classes).
When an `events` promise is guarded by a bundle scoped class, its event is
detected, but the [`then`][events#then] bundles are not run.

## Running bundles on events

`cf-reactor` checks for the events of the `events` promises every second. When
an event happens, it runs the bundles of the [`then`][events#then] attribute of
the `events` promise, in order, like a `bundlesequence`. Events are handled one
at a time: the events happening while bundles run are handled next.

Each event gets a fresh run of the bundles:

- Promises act every time: the default [`ifelapsed`][Promise types#ifelapsed] of
  the bundles run on events is `0`, so the promise locks of previous runs don't
  apply. Promises setting `ifelapsed` in their `action` body are still locked
  for that long.
- Functions are evaluated again: their results are not cached between events.
- Classes and variables defined by the run are undone once the event is handled,
  except persistent classes (see [`persistence`][classes#persistence]), which
  stay defined until they expire, as in `cf-agent`.
- Time classes are updated for each event. The other hard classes, and the
  variables like [`sys.date`][sys#sys.date], are discovered when `cf-reactor`
  loads its policy, and are not updated for each event. Use functions like
  [`now()`][now] to get the time of the event.

The bundles run by `cf-reactor` are not part of a `cf-agent` run:

- Only the bundles of the `then` attribute are run, not the `bundlesequence`.
- The class `reactor` is defined, the class `agent` is not.
- `body agent control` does not apply.
- The output of the bundles, like their reports, is in the output of
  `cf-reactor`. When it runs as a systemd service, see `journalctl -u cf-reactor`.

## Policy updates

Like the other daemons, `cf-reactor` reloads its policy when new policy is
validated, which it checks for every 5 minutes. It also reloads its policy when
it receives the SIGHUP signal.

The new policy is validated with `cf-promises` first: if it has errors,
`cf-reactor` logs them and keeps its previous policy, still watching for the
same events. If the policy has errors when `cf-reactor` starts, it falls back to
the failsafe policy, like the other components. The failsafe policy has no
`events` promises, so `cf-reactor` doesn't watch for any event until the policy
is fixed.

When the policy is reloaded, `cf-reactor` stops watching for the events of the
`events` promises that were removed, and starts watching for those of the new
ones. The `events` promises that didn't change keep watching for their events,
without missing those happening while the policy is reloaded.

## Running cf-reactor

Since 3.29.0, `cf-reactor` is installed by all CFEngine packages, Community and
Enterprise, on hubs and clients.

On hosts using systemd, `cf-reactor` runs as the `cf-reactor` service, which is
part of the `cfengine3` service. The Masterfiles Policy Framework ensures
`cf-reactor` is running on Enterprise hubs.

To try out policy with `cf-reactor`, stop the `cf-reactor` service, as only one
instance of `cf-reactor` can run at a time, and run `cf-reactor` in the
foreground with the policy file to test:

```command
systemctl stop cf-reactor
cf-reactor --no-fork --inform --file ./reactor_test.cf
```

**Note:** On Enterprise hubs, the [Enterprise hub tasks][cf-reactor#Enterprise hub tasks]
are not performed while the `cf-reactor` service is stopped.

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
